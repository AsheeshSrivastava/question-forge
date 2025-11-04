"""
QuestionForge v2.0 - Gradio Web Interface
Hugging Face Spaces Deployment

"Small fixes, big clarity" - Quest & Crossfire
"""

import gradio as gr
import json
import tempfile
from pathlib import Path
from typing import Dict, List, Tuple

# Import QuestionForge components
from refiner.parser import QuestionParser
from refiner.analyzer import QuestionAnalyzer
from refiner.validators import QualityValidator
from refiner.transformers import QuestionTransformer
from refiner.reporters import ReportGenerator


class QuestionForgeApp:
    """Web interface for QuestionForge v2.0"""

    def __init__(self):
        self.analyzer = QuestionAnalyzer("config.yaml")
        self.validator = QualityValidator("config.yaml")
        self.transformer = QuestionTransformer("config.yaml")
        self.reporter = ReportGenerator("config.yaml")

    def analyze_questions(self, file) -> Tuple[str, str, str]:
        """Analyze uploaded question bank"""

        if file is None:
            return "⚠️ Please upload a JSONL file", "", ""

        try:
            # Parse questions
            questions = QuestionParser.parse_jsonl(file.name)

            if not questions:
                return "❌ No valid questions found in file", "", ""

            # Analyze all questions
            results = []
            all_scores = []

            for q in questions:
                scores = self.analyzer.analyze(q)
                all_scores.append(scores['overall'])
                issues = self.analyzer.identify_issues(q, scores)

                results.append({
                    'id': q.id,
                    'question': q.question[:100] + '...' if len(q.question) > 100 else q.question,
                    'overall': scores['overall'],
                    'issues': len(issues)
                })

            # Create summary
            avg_score = sum(all_scores) / len(all_scores)
            passed = sum(1 for s in all_scores if s >= 4.8)

            summary = f"""
# 🔍 Analysis Results

**Questions Analyzed:** {len(questions)}
**Average Score:** {avg_score:.2f}/5.00
**Target:** 4.8/5.0
**Questions ≥4.8:** {passed}/{len(questions)} ({100*passed/len(questions):.1f}%)

---

## Quality Distribution

"""

            # Count distribution
            dist = {
                'Excellent (≥4.8)': sum(1 for s in all_scores if s >= 4.8),
                'Very Good (4.5-4.7)': sum(1 for s in all_scores if 4.5 <= s < 4.8),
                'Good (4.0-4.4)': sum(1 for s in all_scores if 4.0 <= s < 4.5),
                'Adequate (3.5-3.9)': sum(1 for s in all_scores if 3.5 <= s < 4.0),
                'Needs Work (3.0-3.4)': sum(1 for s in all_scores if 3.0 <= s < 3.5),
                'Poor (<3.0)': sum(1 for s in all_scores if s < 3.0)
            }

            for category, count in dist.items():
                pct = 100 * count / len(questions)
                summary += f"- **{category}:** {count} questions ({pct:.1f}%)\n"

            # Create detailed table
            details = "| Question ID | Score | Issues |\n|------------|-------|--------|\n"
            for r in results[:20]:  # Show first 20
                details += f"| {r['id']} | {r['overall']:.2f} | {r['issues']} |\n"

            if len(results) > 20:
                details += f"\n*...and {len(results) - 20} more questions*\n"

            # Status message
            if avg_score >= 4.8:
                status = "✅ **Excellent!** Your questions meet flagship quality standards."
            elif avg_score >= 4.0:
                status = f"🟡 **Good progress!** {len(questions) - passed} questions need refinement."
            else:
                status = f"⚠️ **Needs work.** Most questions need refinement to reach 4.8/5."

            return status, summary, details

        except Exception as e:
            return f"❌ Error analyzing file: {str(e)}", "", ""

    def refine_questions(self, file, auto_apply: bool = True) -> Tuple[str, str]:
        """Refine questions to 4.8/5 quality"""

        if file is None:
            return "⚠️ Please upload a JSONL file", None

        try:
            # Parse questions
            questions = QuestionParser.parse_jsonl(file.name)

            if not questions:
                return "❌ No valid questions found", None

            # Refine questions
            refined_count = 0
            transformations = []

            for q in questions:
                scores = self.analyzer.analyze(q)

                if scores['overall'] < 4.8:
                    # Get transformation suggestions
                    suggestions = self.transformer.suggest_transformations(q, scores)

                    if suggestions and auto_apply:
                        # Apply best transformation
                        best = suggestions[0]
                        improved = self.transformer.apply_transformation(q, best)

                        if improved:
                            refined_count += 1
                            transformations.append({
                                'id': q.id,
                                'strategy': best['strategy'],
                                'before': scores['overall'],
                                'after': best['projected_score']
                            })

            # Save refined questions to temp file
            output_path = tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False)
            QuestionParser.save_jsonl(questions, output_path.name)

            # Create summary
            summary = f"""
# ✨ Refinement Complete

**Questions Processed:** {len(questions)}
**Questions Refined:** {refined_count}
**Transformations Applied:** {len(transformations)}

---

## Top Improvements

"""

            for t in transformations[:10]:
                improvement = t['after'] - t['before']
                summary += f"- **{t['id']}:** {t['before']:.2f} → {t['after']:.2f} (+{improvement:.2f}) via *{t['strategy']}*\n"

            if len(transformations) > 10:
                summary += f"\n*...and {len(transformations) - 10} more improvements*\n"

            summary += f"""

---

## 📥 Download Your Refined Questions

Click the download button below to get your improved question bank!
"""

            return summary, output_path.name

        except Exception as e:
            return f"❌ Error refining questions: {str(e)}", None

    def compare_before_after(self, original_file, refined_file) -> str:
        """Compare original vs refined questions"""

        if original_file is None or refined_file is None:
            return "⚠️ Please upload both original and refined files"

        try:
            original = QuestionParser.parse_jsonl(original_file.name)
            refined = QuestionParser.parse_jsonl(refined_file.name)

            # Calculate scores
            original_scores = [self.analyzer.analyze(q)['overall'] for q in original]
            refined_scores = [self.analyzer.analyze(q)['overall'] for q in refined]

            orig_avg = sum(original_scores) / len(original_scores)
            ref_avg = sum(refined_scores) / len(refined_scores)
            improvement = ref_avg - orig_avg

            orig_passed = sum(1 for s in original_scores if s >= 4.8)
            ref_passed = sum(1 for s in refined_scores if s >= 4.8)

            report = f"""
# 📊 Before/After Comparison

## Overall Improvement

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Average Score | {orig_avg:.2f} | {ref_avg:.2f} | +{improvement:.2f} ✨ |
| Questions ≥4.8 | {orig_passed} ({100*orig_passed/len(original):.1f}%) | {ref_passed} ({100*ref_passed/len(refined):.1f}%) | +{ref_passed - orig_passed} |

---

## Quality Distribution Shift

**Before:**
- Excellent (≥4.8): {sum(1 for s in original_scores if s >= 4.8)} questions
- Very Good (4.5-4.7): {sum(1 for s in original_scores if 4.5 <= s < 4.8)} questions
- Good (4.0-4.4): {sum(1 for s in original_scores if 4.0 <= s < 4.5)} questions
- Needs Work (<4.0): {sum(1 for s in original_scores if s < 4.0)} questions

**After:**
- Excellent (≥4.8): {sum(1 for s in refined_scores if s >= 4.8)} questions ⬆️
- Very Good (4.5-4.7): {sum(1 for s in refined_scores if 4.5 <= s < 4.8)} questions
- Good (4.0-4.4): {sum(1 for s in refined_scores if 4.0 <= s < 4.5)} questions
- Needs Work (<4.0): {sum(1 for s in refined_scores if s < 4.0)} questions ⬇️

---

## Individual Question Improvements

"""

            # Show top improvements
            improvements = []
            for i, (orig, ref) in enumerate(zip(original, refined)):
                orig_score = original_scores[i]
                ref_score = refined_scores[i]
                if ref_score > orig_score:
                    improvements.append({
                        'id': orig.id,
                        'before': orig_score,
                        'after': ref_score,
                        'improvement': ref_score - orig_score
                    })

            improvements.sort(key=lambda x: x['improvement'], reverse=True)

            for imp in improvements[:10]:
                report += f"- **{imp['id']}:** {imp['before']:.2f} → {imp['after']:.2f} (+{imp['improvement']:.2f})\n"

            if len(improvements) > 10:
                report += f"\n*...and {len(improvements) - 10} more improvements*\n"

            return report

        except Exception as e:
            return f"❌ Error comparing files: {str(e)}"


# Initialize app
app = QuestionForgeApp()

# Create Gradio interface
with gr.Blocks(title="QuestionForge v2.0", theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🔥 QuestionForge v2.0

    **"Small fixes, big clarity"** - Quest & Crossfire

    Professional question quality assessment validated against academic and industry standards.

    🎓 **Standards:** CMU, Wiggins & McTighe, AWS, NCCA, ISO 17024/29990

    ---
    """)

    with gr.Tabs():

        # Tab 1: Analyze
        with gr.Tab("📊 Analyze Questions"):
            gr.Markdown("""
            ### Step 1: Upload Your Questions

            Upload a JSONL file containing your questions. Each line should be a JSON object with:
            - `id`, `topic`, `question`, `style`, `difficulty` (required)
            - `bloom_level`, `keywords`, `prerequisites` (recommended)
            """)

            analyze_input = gr.File(label="Upload JSONL File", file_types=[".jsonl"])
            analyze_btn = gr.Button("🔍 Analyze Quality", variant="primary")

            analyze_status = gr.Markdown()
            analyze_summary = gr.Markdown()
            analyze_details = gr.Markdown()

            analyze_btn.click(
                fn=app.analyze_questions,
                inputs=[analyze_input],
                outputs=[analyze_status, analyze_summary, analyze_details]
            )

        # Tab 2: Refine
        with gr.Tab("✨ Refine Questions"):
            gr.Markdown("""
            ### Step 2: Refine to 4.8/5 Quality

            Upload your questions and QuestionForge will automatically improve them using:
            - Real-world context addition
            - Abstract variable replacement
            - Diverse name substitution
            - Bloom's taxonomy alignment
            - Cognitive depth enhancement
            """)

            refine_input = gr.File(label="Upload JSONL File", file_types=[".jsonl"])
            refine_auto = gr.Checkbox(label="Auto-apply improvements", value=True)
            refine_btn = gr.Button("✨ Refine Questions", variant="primary")

            refine_summary = gr.Markdown()
            refine_output = gr.File(label="📥 Download Refined Questions")

            refine_btn.click(
                fn=app.refine_questions,
                inputs=[refine_input, refine_auto],
                outputs=[refine_summary, refine_output]
            )

        # Tab 3: Compare
        with gr.Tab("📈 Before/After Comparison"):
            gr.Markdown("""
            ### Step 3: Compare Results

            Upload both your original and refined question files to see the improvements.
            """)

            compare_original = gr.File(label="Original Questions (JSONL)", file_types=[".jsonl"])
            compare_refined = gr.File(label="Refined Questions (JSONL)", file_types=[".jsonl"])
            compare_btn = gr.Button("📊 Generate Comparison", variant="primary")

            compare_output = gr.Markdown()

            compare_btn.click(
                fn=app.compare_before_after,
                inputs=[compare_original, compare_refined],
                outputs=[compare_output]
            )

        # Tab 4: Documentation
        with gr.Tab("📖 Documentation"):
            gr.Markdown("""
            # QuestionForge v2.0 Documentation

            ## 🎯 What is QuestionForge?

            QuestionForge is a professional-grade question quality assessment tool that scores educational questions on **7 criteria**:

            1. **Adult Learning (20%)** - Real-world context, practical examples
            2. **People-First (15%)** - Inclusive language, diverse representation
            3. **Bloom's Alignment (15%)** - Correct cognitive level for difficulty
            4. **Practical Application (15%)** - Industry relevance, tool awareness
            5. **RAG Optimization (10%)** - Keyword richness, searchability
            6. **Construct Validity (15%)** - Measures what it claims to measure
            7. **Cognitive Depth (10%)** - Six Facets of Understanding

            **Overall Score = Weighted Average** (Target: ≥4.8/5.0 for flagship quality)

            ---

            ## 📝 Question Format (JSONL)

            Each line in your JSONL file should contain one question as a JSON object:

            ```json
            {
              "id": "q_py_basics_001",
              "topic": "Python Basics",
              "question": "What is the correct way to declare a variable in Python?",
              "style": "short_question",
              "difficulty": "starter",
              "bloom_level": "remember",
              "keywords": ["variable", "declaration", "syntax"],
              "prerequisites": [],
              "subtopics": ["variables", "syntax"]
            }
            ```

            **Required fields:**
            - `id` - Unique identifier
            - `topic` - Main topic/category
            - `question` - The question text
            - `style` - Question format (see below)
            - `difficulty` - starter, core, or stretch

            **Supported question styles:**
            - `single_word`, `short_question`, `predict_output`, `debug_fix`
            - `scenario_task`, `fill_in_blank`, `explain_concept`
            - `compare_contrast`, `rewrite`

            ---

            ## 🎓 Standards Validation

            QuestionForge v2.0 is validated against:

            **Academic Standards:**
            - Carnegie Mellon Eberly Center (Backward Design)
            - Wiggins & McTighe (Understanding by Design)
            - Anderson & Krathwohl (Revised Bloom's Taxonomy)
            - ACM SIGCSE (CS Education Research)

            **Industry Standards:**
            - AWS SME Item Writing Guidelines
            - NCCA Accreditation Standards
            - ISO 17024 (Certification of Persons)
            - ISO 29990 (Learning Services Quality)

            ---

            ## 🚀 How to Use

            ### 1. Analyze Tab
            - Upload your JSONL file
            - Click "Analyze Quality"
            - Review scores and distribution
            - Identify questions needing improvement

            ### 2. Refine Tab
            - Upload your JSONL file
            - Enable auto-apply (recommended)
            - Click "Refine Questions"
            - Download improved question bank

            ### 3. Compare Tab
            - Upload original and refined files
            - Click "Generate Comparison"
            - Review before/after metrics
            - Celebrate improvements! 🎉

            ---

            ## 💡 Tips for Best Results

            1. **Start with good metadata** - Include bloom_level, keywords, prerequisites
            2. **Use realistic examples** - Avoid x, y, foo, bar
            3. **Add context** - Scenario-based questions score higher
            4. **Be inclusive** - Use globally diverse names (Priya, Chen, Amara)
            5. **Iterate** - Run analyze → refine → analyze again

            ---

            ## 📊 Quality Thresholds

            - **≥4.8** - Excellent (flagship quality)
            - **4.5-4.7** - Very Good (minor improvements)
            - **4.0-4.4** - Good (acceptable)
            - **3.5-3.9** - Adequate (needs work)
            - **<3.5** - Needs significant improvement

            ---

            ## 🔒 Privacy

            This is a **private space**. Your questions are:
            - ✅ Processed in real-time
            - ✅ Never stored permanently
            - ✅ Not shared with anyone
            - ✅ Secure and confidential

            ---

            ## 📞 Support

            For questions or issues, contact Quest & Crossfire Arsenal.

            **Version:** 2.0.0
            **Built for:** Aethelgard Academy
            """)

    gr.Markdown("""
    ---

    **QuestionForge v2.0** | Built by Asheesh for Aethelgard Academy | "Small fixes, big clarity" 🔥
    """)

# Launch app
if __name__ == "__main__":
    demo.launch()
