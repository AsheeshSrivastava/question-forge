"""
Report Generator - Create quality reports and dashboards
"""

from typing import List, Dict
from pathlib import Path
import json
from datetime import datetime
from .parser import Question
from .analyzer import QuestionAnalyzer
from .validators import QualityValidator


class ReportGenerator:
    """Generate comprehensive quality reports"""

    def __init__(self, config_path: str = "config.yaml"):
        self.analyzer = QuestionAnalyzer(config_path)
        self.validator = QualityValidator(config_path)

    def generate_summary_report(self, questions: List[Question]) -> str:
        """Generate text summary report"""

        validation = self.validator.validate_batch(questions)

        report = []
        report.append("=" * 60)
        report.append("QUESTIONFORGE QUALITY REPORT")
        report.append('"Small fixes, big clarity" - Quest & Crossfire')
        report.append("=" * 60)
        report.append("")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Questions: {validation['total']}")
        report.append("")

        # Overall metrics
        report.append("OVERALL QUALITY")
        report.append("-" * 40)
        report.append(f"Average Score: {validation['average_score']:.2f}/5.00")
        report.append(f"Target: {validation['threshold']:.1f}/5.0")
        report.append(f"Questions ≥{validation['threshold']}: {validation['passed']} ({100*validation['passed']/validation['total']:.1f}%)")
        report.append("")

        # Distribution
        report.append("QUALITY DISTRIBUTION")
        report.append("-" * 40)
        dist = validation['distribution']
        total = validation['total']

        report.append(f"  5.0 (Excellent):     {dist['excellent']:3d} questions ({100*dist['excellent']/total:.1f}%)")
        report.append(f"  4.5-4.9 (Very Good): {dist['very_good']:3d} questions ({100*dist['very_good']/total:.1f}%)")
        report.append(f"  4.0-4.4 (Good):      {dist['good']:3d} questions ({100*dist['good']/total:.1f}%)")
        report.append(f"  3.5-3.9 (Adequate):  {dist['adequate']:3d} questions ({100*dist['adequate']/total:.1f}%)")
        report.append(f"  3.0-3.4 (Needs Work): {dist['needs_work']:3d} questions ({100*dist['needs_work']/total:.1f}%)")
        report.append(f"  <3.0 (Poor):         {dist['poor']:3d} questions ({100*dist['poor']/total:.1f}%)")
        report.append("")

        # Failed questions
        if validation['failed'] > 0:
            report.append("QUESTIONS NEEDING REFINEMENT")
            report.append("-" * 40)
            for failed in validation['failed_questions'][:10]:  # Top 10
                report.append(f"  [{failed['id']}] Score: {failed['score']:.2f}")
                report.append(f"    {failed['question']}")
                if failed['top_issue']:
                    report.append(f"    Issue: {failed['top_issue']['criterion']} (score: {failed['top_issue']['score']:.2f})")
                report.append("")

            if len(validation['failed_questions']) > 10:
                report.append(f"  ... and {len(validation['failed_questions']) - 10} more")
                report.append("")

        report.append("=" * 60)

        return "\n".join(report)

    def generate_before_after_report(self, before: List[Question], after: List[Question]) -> str:
        """Generate before/after comparison report"""

        before_val = self.validator.validate_batch(before)
        after_val = self.validator.validate_batch(after)

        report = []
        report.append("=" * 60)
        report.append("BEFORE/AFTER REFINEMENT REPORT")
        report.append("=" * 60)
        report.append("")

        # Summary
        report.append("BEFORE REFINEMENT:")
        report.append(f"  Average Score: {before_val['average_score']:.2f}/5.00")
        report.append(f"  Questions ≥4.8: {before_val['passed']} ({100*before_val['passed']/before_val['total']:.1f}%)")
        report.append("")

        report.append("AFTER REFINEMENT:")
        report.append(f"  Average Score: {after_val['average_score']:.2f}/5.00 ⬆️ +{after_val['average_score'] - before_val['average_score']:.2f}")
        report.append(f"  Questions ≥4.8: {after_val['passed']} ({100*after_val['passed']/after_val['total']:.1f}%) ⬆️ +{100*(after_val['passed']-before_val['passed'])/before_val['total']:.1f}%")
        report.append("")

        # Distribution changes
        report.append("DISTRIBUTION CHANGES:")
        report.append("-" * 60)
        report.append(f"{'Category':<20} {'Before':<12} {'After':<12} {'Change'}")
        report.append("-" * 60)

        categories = ['excellent', 'very_good', 'good', 'adequate', 'needs_work', 'poor']
        labels = ['Excellent (≥4.8)', 'Very Good (4.5-4.7)', 'Good (4.0-4.4)',
                  'Adequate (3.5-3.9)', 'Needs Work (3.0-3.4)', 'Poor (<3.0)']

        for cat, label in zip(categories, labels):
            before_count = before_val['distribution'][cat]
            after_count = after_val['distribution'][cat]
            change = after_count - before_count
            change_str = f"+{change}" if change > 0 else str(change)

            report.append(f"{label:<20} {before_count:<12} {after_count:<12} {change_str}")

        report.append("")
        report.append("=" * 60)

        return "\n".join(report)

    def generate_detailed_json_report(self, questions: List[Question], output_path: str):
        """Generate detailed JSON report with all metrics"""

        data = {
            "meta": {
                "generated": datetime.now().isoformat(),
                "total_questions": len(questions),
                "tool": "QuestionForge v2.0",
                "philosophy": "Small fixes, big clarity",
                "scoring_criteria": 7,
                "standards": ["Academic (CMU, Wiggins & McTighe)", "Industry (AWS, NCCA, ISO)"]
            },
            "questions": []
        }

        for q in questions:
            scores = self.analyzer.analyze(q)
            passes, validation = self.validator.validate(q)
            issues = self.analyzer.identify_issues(q, scores)

            q_data = {
                "id": q.id,
                "question": q.question,
                "topic": q.topic,
                "difficulty": q.difficulty,
                "style": q.style,
                "scores": scores,
                "passes_threshold": passes,
                "issues": [{"category": cat, "description": desc, "priority": pri}
                          for cat, desc, pri in issues],
                "refinement_history": q.refinement_history if hasattr(q, 'refinement_history') else []
            }

            data["questions"].append(q_data)

        # Summary stats
        all_scores = [self.analyzer.analyze(q)["overall"] for q in questions]
        validation = self.validator.validate_batch(questions)

        data["summary"] = {
            "average_score": validation["average_score"],
            "passed": validation["passed"],
            "failed": validation["failed"],
            "pass_rate": round(100 * validation["passed"] / validation["total"], 2),
            "distribution": validation["distribution"]
        }

        # Save to file
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return output_path

    def generate_html_report(self, questions: List[Question], output_path: str):
        """Generate HTML report with charts (basic version)"""

        validation = self.validator.validate_batch(questions)

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>QuestionForge Quality Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .tagline {{
            font-style: italic;
            opacity: 0.9;
        }}
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .metric-value {{
            font-size: 48px;
            font-weight: bold;
            color: #667eea;
        }}
        .metric-label {{
            color: #666;
            font-size: 14px;
            text-transform: uppercase;
        }}
        .distribution-bar {{
            height: 30px;
            background: #e0e0e0;
            border-radius: 5px;
            overflow: hidden;
            margin: 10px 0;
        }}
        .bar-segment {{
            height: 100%;
            float: left;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 12px;
        }}
        .excellent {{ background: #10b981; }}
        .very-good {{ background: #3b82f6; }}
        .good {{ background: #6366f1; }}
        .adequate {{ background: #f59e0b; }}
        .needs-work {{ background: #ef4444; }}
        .poor {{ background: #991b1b; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔥 QuestionForge v2.0 Quality Report</h1>
        <p class="tagline">"Small fixes, big clarity" - Quest & Crossfire</p>
        <p>7-Criteria Scoring | Academic + Industry Standards</p>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px;">
        <div class="metric-card">
            <div class="metric-label">Total Questions</div>
            <div class="metric-value">{validation['total']}</div>
        </div>

        <div class="metric-card">
            <div class="metric-label">Average Score</div>
            <div class="metric-value">{validation['average_score']:.2f}</div>
        </div>

        <div class="metric-card">
            <div class="metric-label">Pass Rate (≥4.8)</div>
            <div class="metric-value">{100*validation['passed']/validation['total']:.1f}%</div>
        </div>
    </div>

    <div class="metric-card">
        <h2>Quality Distribution</h2>
        <div class="distribution-bar">
            <div class="bar-segment excellent" style="width: {100*validation['distribution']['excellent']/validation['total']:.1f}%">
                {validation['distribution']['excellent']}
            </div>
            <div class="bar-segment very-good" style="width: {100*validation['distribution']['very_good']/validation['total']:.1f}%">
                {validation['distribution']['very_good']}
            </div>
            <div class="bar-segment good" style="width: {100*validation['distribution']['good']/validation['total']:.1f}%">
                {validation['distribution']['good']}
            </div>
            <div class="bar-segment adequate" style="width: {100*validation['distribution']['adequate']/validation['total']:.1f}%">
                {validation['distribution']['adequate']}
            </div>
            <div class="bar-segment needs-work" style="width: {100*validation['distribution']['needs_work']/validation['total']:.1f}%">
                {validation['distribution']['needs_work']}
            </div>
            <div class="bar-segment poor" style="width: {100*validation['distribution']['poor']/validation['total']:.1f}%">
                {validation['distribution']['poor']}
            </div>
        </div>

        <div style="margin-top: 20px;">
            <p><span class="excellent" style="padding: 5px 10px; border-radius: 3px;">■</span> Excellent (≥4.8): {validation['distribution']['excellent']} questions</p>
            <p><span class="very-good" style="padding: 5px 10px; border-radius: 3px;">■</span> Very Good (4.5-4.7): {validation['distribution']['very_good']} questions</p>
            <p><span class="good" style="padding: 5px 10px; border-radius: 3px;">■</span> Good (4.0-4.4): {validation['distribution']['good']} questions</p>
            <p><span class="adequate" style="padding: 5px 10px; border-radius: 3px;">■</span> Adequate (3.5-3.9): {validation['distribution']['adequate']} questions</p>
            <p><span class="needs-work" style="padding: 5px 10px; border-radius: 3px;">■</span> Needs Work (3.0-3.4): {validation['distribution']['needs_work']} questions</p>
            <p><span class="poor" style="padding: 5px 10px; border-radius: 3px;">■</span> Poor (<3.0): {validation['distribution']['poor']} questions</p>
        </div>
    </div>

    <div class="metric-card">
        <p style="text-align: center; color: #667eea; font-weight: bold;">
            Built with QuestionForge - Quest & Crossfire Arsenal
        </p>
    </div>
</body>
</html>
"""

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w') as f:
            f.write(html)

        return output_path
