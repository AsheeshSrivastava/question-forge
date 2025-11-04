#!/usr/bin/env python3
"""
QuestionForge - Professional Question Refinement System
"Small fixes, big clarity" - Quest & Crossfire

Usage:
    python main.py analyze questions.jsonl
    python main.py refine questions.jsonl --output refined.jsonl
    python main.py report original.jsonl refined.jsonl
"""

import sys
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    os.system('')  # Enables ANSI escape sequences
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint
from pathlib import Path

from refiner import (
    QuestionParser,
    QuestionAnalyzer,
    QuestionTransformer,
    QualityValidator,
    RAGOptimizer,
    ReportGenerator
)

console = Console()


@click.group()
def cli():
    """🔥 QuestionForge - "Small fixes, big clarity" """
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
def analyze(input_file):
    """Analyze question bank quality"""

    console.print("\n[bold cyan]🔍 QuestionForge - Quality Analysis[/bold cyan]")
    console.print("[italic]\"Small fixes, big clarity\" - Quest & Crossfire[/italic]\n")

    # Parse questions
    with console.status("[bold green]Loading question bank...", spinner="dots"):
        questions = QuestionParser.parse_jsonl(input_file)

    console.print(f"✓ Loaded {len(questions)} questions\n")

    # Validate
    validator = QualityValidator(threshold=4.8)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Analyzing quality...", total=len(questions))

        validation = validator.validate_batch(questions)

        progress.update(task, advance=len(questions))

    # Display results
    console.print("\n[bold]QUALITY DISTRIBUTION:[/bold]")

    dist = validation['distribution']
    total = validation['total']

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Category", style="dim")
    table.add_column("Count")
    table.add_column("Percentage")

    categories = [
        ("Excellent (≥4.8)", "excellent", "green"),
        ("Very Good (4.5-4.7)", "very_good", "cyan"),
        ("Good (4.0-4.4)", "good", "blue"),
        ("Adequate (3.5-3.9)", "adequate", "yellow"),
        ("Needs Work (3.0-3.4)", "needs_work", "red"),
        ("Poor (<3.0)", "poor", "bright_red")
    ]

    for label, key, color in categories:
        count = dist[key]
        pct = f"{100*count/total:.1f}%"
        table.add_row(label, f"[{color}]{count}[/{color}]", f"[{color}]{pct}[/{color}]")

    console.print(table)

    # Summary panel
    avg_score = validation['average_score']
    passed = validation['passed']
    pass_rate = 100 * passed / total

    if avg_score >= 4.8:
        score_color = "green"
        status_emoji = "✅"
    elif avg_score >= 4.0:
        score_color = "yellow"
        status_emoji = "⚠️"
    else:
        score_color = "red"
        status_emoji = "❌"

    summary = f"""
[bold]Average Score:[/bold] [{score_color}]{avg_score:.2f}/5.00[/{score_color}] {status_emoji}
[bold]Target:[/bold] 4.8/5.0
[bold]Questions ≥4.8:[/bold] {passed}/{total} ([{score_color}]{pass_rate:.1f}%[/{score_color}])

[bold]Status:[/bold] {'[green]Ready for batch processing! 🚀[/green]' if avg_score >= 4.8 else '[yellow]Refinement recommended[/yellow]'}
"""

    console.print(Panel(summary, title="📊 Summary", border_style="cyan"))

    # Show top issues if needed
    if passed < total:
        console.print(f"\n[yellow]⚠️  {total - passed} questions need refinement[/yellow]")
        console.print(f"[dim]Run: python main.py refine {input_file} --output refined.jsonl[/dim]\n")


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', default='refined.jsonl', help='Output file path')
@click.option('--auto', is_flag=True, help='Auto-apply all refinements')
@click.option('--interactive', '-i', is_flag=True, help='Interactive review mode')
@click.option('--threshold', '-t', default=4.8, help='Quality threshold')
def refine(input_file, output, auto, interactive, threshold):
    """Refine questions to 4.8/5 quality"""

    console.print("\n[bold cyan]🔨 QuestionForge - Batch Refinement[/bold cyan]")
    console.print("[italic]\"Small fixes, big clarity\" - Quest & Crossfire[/italic]\n")

    # Parse questions
    with console.status("[bold green]Loading question bank...", spinner="dots"):
        questions = QuestionParser.parse_jsonl(input_file)

    console.print(f"✓ Loaded {len(questions)} questions\n")

    # Analyze before
    analyzer = QuestionAnalyzer()
    transformer = QuestionTransformer()

    before_scores = [analyzer.analyze(q)["overall"] for q in questions]
    avg_before = sum(before_scores) / len(before_scores)

    console.print(f"[dim]Average score before refinement: {avg_before:.2f}/5.00[/dim]\n")

    # Refine
    refined_count = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Refining questions...", total=len(questions))

        for i, q in enumerate(questions):
            current_score = analyzer.analyze(q)["overall"]

            if current_score >= threshold:
                progress.update(task, advance=1)
                continue

            # Transform
            transformed, strategy, improvement = transformer.transform(q, auto=auto)

            if improvement > 0:
                if interactive:
                    # Show suggestion (simplified for now)
                    console.print(f"\n[yellow]Question {i+1}/{len(questions)}:[/yellow] {q.question[:60]}...")
                    console.print(f"[dim]Suggested: {transformed.question[:60]}...[/dim]")
                    console.print(f"[green]Improvement: +{improvement:.2f}[/green]")

                    if click.confirm("Apply?", default=True):
                        questions[i] = transformed
                        refined_count += 1
                else:
                    questions[i] = transformed
                    refined_count += 1

            progress.update(task, advance=1)

    # Analyze after
    after_scores = [analyzer.analyze(q)["overall"] for q in questions]
    avg_after = sum(after_scores) / len(after_scores)

    # Save
    QuestionParser.save_jsonl(questions, output)

    # Results
    console.print("\n[bold green]✨ Refinement Complete![/bold green]\n")

    results_table = Table(show_header=True, header_style="bold magenta")
    results_table.add_column("Metric")
    results_table.add_column("Before")
    results_table.add_column("After")
    results_table.add_column("Change")

    results_table.add_row(
        "Average Score",
        f"{avg_before:.2f}/5.00",
        f"[green]{avg_after:.2f}/5.00[/green]",
        f"[green]⬆️ +{avg_after - avg_before:.2f}[/green]"
    )

    passed_before = sum(1 for s in before_scores if s >= threshold)
    passed_after = sum(1 for s in after_scores if s >= threshold)

    results_table.add_row(
        f"Questions ≥{threshold}",
        f"{passed_before} ({100*passed_before/len(questions):.1f}%)",
        f"[green]{passed_after} ({100*passed_after/len(questions):.1f}%)[/green]",
        f"[green]⬆️ +{passed_after - passed_before}[/green]"
    )

    results_table.add_row(
        "Refined",
        "-",
        f"[cyan]{refined_count}[/cyan]",
        "-"
    )

    console.print(results_table)

    console.print(f"\n[bold green]✓ Output saved to:[/bold green] {output}")
    console.print(f"\n[dim]🎯 Ready for batch processing![/dim]\n")


@cli.command()
@click.argument('original_file', type=click.Path(exists=True))
@click.argument('refined_file', type=click.Path(exists=True), required=False)
@click.option('--html', is_flag=True, help='Generate HTML report')
@click.option('--json', is_flag=True, help='Generate JSON report')
def report(original_file, refined_file, html, json):
    """Generate quality reports"""

    console.print("\n[bold cyan]📊 QuestionForge - Quality Report[/bold cyan]")
    console.print("[italic]\"Small fixes, big clarity\" - Quest & Crossfire[/italic]\n")

    # Parse
    with console.status("[bold green]Loading questions...", spinner="dots"):
        original = QuestionParser.parse_jsonl(original_file)
        if refined_file:
            refined = QuestionParser.parse_jsonl(refined_file)
        else:
            refined = None

    reporter = ReportGenerator()

    # Generate text report
    if refined:
        report_text = reporter.generate_before_after_report(original, refined)
    else:
        report_text = reporter.generate_summary_report(original)

    console.print(report_text)

    # Generate HTML
    if html:
        html_path = f"{Path(original_file).stem}_report.html"
        questions = refined if refined else original
        reporter.generate_html_report(questions, html_path)
        console.print(f"\n[green]✓ HTML report saved to:[/green] {html_path}")

    # Generate JSON
    if json:
        json_path = f"{Path(original_file).stem}_report.json"
        questions = refined if refined else original
        reporter.generate_detailed_json_report(questions, json_path)
        console.print(f"\n[green]✓ JSON report saved to:[/green] {json_path}")

    console.print()


@cli.command()
def version():
    """Show version information"""
    console.print("\n[bold cyan]🔥 QuestionForge v2.0.0[/bold cyan]")
    console.print("[italic]\"Small fixes, big clarity\" - Quest & Crossfire[/italic]")
    console.print("\n[green]✨ Enhanced with Academic + Industry Standards[/green]")
    console.print("[dim]7-Criteria Scoring | CMU, Wiggins & McTighe, AWS, NCCA, ISO[/dim]")
    console.print("\n[dim]Built by Asheesh for Aethelgard Academy[/dim]\n")


if __name__ == '__main__':
    cli()
