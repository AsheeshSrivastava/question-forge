# QuestionForge v2.0 - Quick Start Guide

**"Small fixes, big clarity"** - Ready to use in 5 minutes!

---

## 📋 Prerequisites

Before you start, make sure you have:

- ✅ **Python 3.7+** installed
- ✅ **pip** (Python package manager)
- ✅ **Terminal/Command Prompt** access

**Check your Python version:**
```bash
python --version
# or
py --version
```

---

## 🚀 Installation (First Time Setup)

### Step 1: Navigate to QuestionForge Directory

```bash
cd D:\claude-projects\question-forge
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**This will install:**
- PyYAML (configuration)
- Rich (beautiful terminal output)
- Click (CLI framework)
- Pandas, NumPy (data processing)
- NLTK (text analysis)
- OpenPyXL (Excel export)
- pytest (testing)

**Installation time:** ~1-2 minutes

### Step 3: Verify Installation

```bash
py main.py version
```

**Expected output:**
```
🔥 QuestionForge v2.0.0
"Small fixes, big clarity" - Quest & Crossfire

✨ Enhanced with Academic + Industry Standards
7-Criteria Scoring | CMU, Wiggins & McTighe, AWS, NCCA, ISO

Built by Asheesh for Aethelgard Academy
```

✅ **If you see this, you're ready to go!**

---

## 🎯 Quick Test Run (30 seconds)

Let's test QuestionForge with the included sample questions:

```bash
py main.py analyze test_questions.jsonl
```

**You should see:**
```
🔍 QuestionForge - Quality Analysis
"Small fixes, big clarity" - Quest & Crossfire

✓ Loaded 10 questions

  Analyzing quality... ━━━━━━━━━━━━━━━━━━━━━━━━ 100%

QUALITY DISTRIBUTION:
┌──────────────────────┬───────┬────────────┐
│ Category             │ Count │ Percentage │
├──────────────────────┼───────┼────────────┤
│ Excellent (≥4.8)     │ 0     │ 0.0%       │
│ Very Good (4.5-4.7)  │ 0     │ 0.0%       │
│ Good (4.0-4.4)       │ 1     │ 10.0%      │
│ Adequate (3.5-3.9)   │ 5     │ 50.0%      │
│ Needs Work (3.0-3.4) │ 4     │ 40.0%      │
│ Poor (<3.0)          │ 0     │ 0.0%       │
└──────────────────────┴───────┴────────────┘

Average Score: 3.58/5.00
Target: 4.8/5.0
Questions ≥4.8: 0/10 (0.0%)

⚠️  10 questions need refinement
```

✅ **Congratulations! QuestionForge is working!**

---

## 📖 Basic Usage

### 1. Analyze Your Question Bank

**Command:**
```bash
py main.py analyze YOUR_QUESTIONS.jsonl
```

**What it does:**
- Loads your questions from JSONL file
- Scores each question on 7 criteria (1.0-5.0 scale)
- Shows quality distribution
- Identifies questions needing improvement

**Example with your own file:**
```bash
py main.py analyze my_python_questions.jsonl
```

---

### 2. Refine Questions to 4.8/5 Quality

**Command:**
```bash
py main.py refine test_questions.jsonl --output refined.jsonl
```

**What it does:**
- Analyzes all questions
- Suggests improvements (expand single-word, add real-world context, etc.)
- Auto-applies refinements
- Saves improved questions to new file

**Options:**
```bash
# Interactive mode (approve each change)
py main.py refine test_questions.jsonl --interactive

# Auto mode (apply all suggestions)
py main.py refine test_questions.jsonl --auto --output refined.jsonl

# Dry run (see suggestions without saving)
py main.py refine test_questions.jsonl --dry-run
```

---

### 3. Generate Quality Reports

**Command:**
```bash
py main.py report test_questions.jsonl refined.jsonl
```

**What it does:**
- Compares before/after refinement
- Shows improvement metrics
- Generates text report

**Generate HTML report:**
```bash
py main.py report test_questions.jsonl refined.jsonl --html
```

**Generate JSON export:**
```bash
py main.py report test_questions.jsonl refined.jsonl --json output.json
```

---

## 📝 Your Question Format (JSONL)

QuestionForge expects questions in JSONL format (one JSON object per line):

**Example question:**
```json
{
  "id": "q_py_basics_001",
  "topic": "Python Basics",
  "question": "What is the correct way to declare a variable in Python?",
  "style": "short_question",
  "difficulty": "starter",
  "bloom_level": "remember",
  "keywords": ["variable", "declaration", "syntax", "python basics"],
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

**Optional but recommended:**
- `bloom_level` - remember, understand, apply, analyze, evaluate, create
- `keywords` - List of keywords for RAG optimization
- `prerequisites` - List of prerequisite question IDs
- `subtopics` - List of subtopics

**Supported question styles:**
- `single_word` - One-word answer
- `short_question` - Brief question
- `predict_output` - What will this code output?
- `debug_fix` - Find and fix the bug
- `scenario_task` - Real-world scenario
- `fill_in_blank` - Complete the code
- `explain_concept` - Explain a concept
- `compare_contrast` - Compare two approaches
- `rewrite` - Improve this code

---

## 🎯 Real-World Workflow

### Scenario: You have 50 Python questions to improve

**Step 1: Analyze current quality**
```bash
py main.py analyze my_50_questions.jsonl
```

**Step 2: Refine questions**
```bash
py main.py refine my_50_questions.jsonl --output my_50_questions_refined.jsonl
```

**Step 3: Generate comparison report**
```bash
py main.py report my_50_questions.jsonl my_50_questions_refined.jsonl --html
```

**Step 4: Review HTML report**
- Open `report.html` in your browser
- See before/after scores
- Identify remaining issues

**Step 5: Manual review**
- Review refined questions
- Make final edits if needed
- Run analyze again to verify 4.8/5 threshold

**Time investment:** ~30 minutes for 50 questions (mostly automated)

---

## 📊 Understanding Your Scores

QuestionForge v2.0 scores questions on **7 criteria**:

| Criterion | Weight | What it Measures |
|-----------|--------|-----------------|
| **Adult Learning** | 20% | Real-world context, practical examples |
| **People-First** | 15% | Inclusive language, diverse examples |
| **Bloom's Alignment** | 15% | Correct cognitive level for difficulty |
| **Practical Application** | 15% | Industry relevance, tool awareness |
| **RAG Optimization** | 10% | Keyword richness, searchability |
| **Construct Validity** | 15% | Measures what it claims to measure |
| **Cognitive Depth** | 10% | Six Facets of Understanding |

**Overall Score = Weighted Average**

**Quality Thresholds:**
- **≥4.8** - Excellent (flagship quality)
- **4.5-4.7** - Very Good (minor improvements)
- **4.0-4.4** - Good (acceptable)
- **3.5-3.9** - Adequate (needs work)
- **3.0-3.4** - Needs Work (significant issues)
- **<3.0** - Poor (major overhaul needed)

---

## 🔧 Configuration (Optional)

The `config.yaml` file controls scoring weights and templates.

**Location:** `D:\claude-projects\question-forge\config.yaml`

**Common customizations:**

**1. Adjust scoring weights:**
```yaml
scoring:
  weights:
    adult_learning: 0.25      # Increase importance
    people_first: 0.15
    blooms: 0.15
    practical: 0.15
    rag: 0.10
    construct_validity: 0.10  # Decrease importance
    cognitive_depth: 0.10
```

**2. Change quality threshold:**
```yaml
scoring:
  threshold: 4.5  # Lower bar (was 4.8)
```

**3. Add custom templates:**
```yaml
templates:
  diverse_names:
    - Priya
    - Chen
    - Amara
    - YourCustomName  # Add your own
```

⚠️ **Warning:** Weights must sum to 1.0 (100%)

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'yaml'"

**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

---

### Problem: "UnicodeEncodeError" or emoji display issues

**Solution:** This is fixed in v2.0, but if you still see it:
- Use Windows Terminal (not CMD)
- Or upgrade to Windows 11
- Or run: `chcp 65001` before running QuestionForge

---

### Problem: "FileNotFoundError: test_questions.jsonl"

**Solution:** Make sure you're in the correct directory
```bash
cd D:\claude-projects\question-forge
```

---

### Problem: Scores seem wrong or unexpected

**Solution:** Check your question format
- Verify all required fields present
- Check `bloom_level` matches `difficulty`
- Ensure `style` is one of the supported types

---

### Problem: Refinement isn't improving scores

**Solution:** Some issues require manual fixes
- Review the specific issues reported
- Construct validity issues often need human judgment
- Cognitive depth may need question restructuring

---

## 📚 Next Steps

### For Your First Real Use:

1. **Prepare your questions** in JSONL format (see example above)
2. **Analyze** to see current quality
3. **Refine** to improve scores
4. **Review** refined questions manually
5. **Generate report** to document improvements

### Learn More:

- **README.md** - Full feature documentation
- **USAGE_GUIDE.md** - Comprehensive usage examples
- **QUICK_REFERENCE.md** - Command reference
- **VALIDATION_FRAMEWORK.md** - Standards and criteria details
- **SCOPE_ANALYSIS.md** - What QuestionForge can/cannot do

### Get Advanced:

- **Custom transformers** - Add your own refinement strategies
- **Language configs** - Add JavaScript/Java support (v2.1)
- **Expert validation** - Use EXPERT_REVIEW_RUBRIC.md

---

## 💡 Pro Tips

**Tip 1: Start Small**
- Test with 5-10 questions first
- Understand the scoring
- Then scale to full question bank

**Tip 2: Review Refined Questions**
- Auto-refinement is good, not perfect
- Always do a final human review
- Look for construct validity issues

**Tip 3: Iterate**
- First pass: Fix obvious issues (abstract variables, single words)
- Second pass: Improve cognitive depth
- Third pass: Polish and perfect

**Tip 4: Use Reports**
- HTML reports are great for stakeholders
- JSON exports are great for data analysis
- Track progress over time

**Tip 5: Preserve Originals**
- Always output to a NEW file (`--output refined.jsonl`)
- Keep original questions as backup
- QuestionForge preserves originals in metadata

---

## 🎓 Example Session

Let's walk through a complete session:

```bash
# 1. Navigate to QuestionForge
cd D:\claude-projects\question-forge

# 2. Check version
py main.py version
# Output: QuestionForge v2.0.0 ✅

# 3. Analyze sample questions
py main.py analyze test_questions.jsonl
# Output: Average 3.58/5.00, 0 questions ≥4.8

# 4. Refine questions
py main.py refine test_questions.jsonl --output test_refined.jsonl
# Output: Applied 15 transformations, new average: 4.52/5.00

# 5. Generate HTML report
py main.py report test_questions.jsonl test_refined.jsonl --html
# Output: report.html created

# 6. Open report in browser
start report.html  # Windows
# or
open report.html   # Mac/Linux

# 7. Review and celebrate! 🎉
```

**Time:** 5 minutes total
**Result:** Professional-quality questions validated against academic + industry standards

---

## ✅ You're Ready!

QuestionForge v2.0 is now at your fingertips. Start with:

```bash
cd D:\claude-projects\question-forge
py main.py analyze test_questions.jsonl
```

**Need Help?**
- Check USAGE_GUIDE.md for detailed examples
- Check TEST_RESULTS_V2.md to see what's tested
- Check SCOPE_ANALYSIS.md to understand capabilities

**Questions or Issues?**
- Open an issue in the project
- Contact Quest & Crossfire Arsenal
- Consult the comprehensive documentation

---

**Happy refining! 🔥**

**"Small fixes, big clarity" - Quest & Crossfire**
