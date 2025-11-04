# QuestionForge Usage Guide

**"Small fixes, big clarity"** - Quest & Crossfire Arsenal

## Overview

QuestionForge is a professional question refinement system designed to elevate educational content to flagship quality (4.8/5.0 standard). Built with Quest & Crossfire principles, it provides systematic, data-driven question improvement through automated analysis and transformation.

## Installation

```bash
# Clone or navigate to question-forge directory
cd question-forge

# Install dependencies
pip install -r requirements.txt
```

**Requirements:**
- Python 3.7+
- PyYAML, Rich, Click, Pandas, NumPy, NLTK

## Quick Start

### 1. Analyze Question Quality

Check the quality distribution of your question bank:

```bash
python main.py analyze questions.jsonl
```

**Output:**
- Overall quality score
- Distribution across quality tiers
- Pass rate against 4.8/5 threshold
- List of questions needing refinement

**Example Output:**
```
🔍 QuestionForge - Quality Analysis

✓ Loaded 10 questions

QUALITY DISTRIBUTION:
┌──────────────────────┬───────┬────────────┐
│ Category             │ Count │ Percentage │
├──────────────────────┼───────┼────────────┤
│ Excellent (≥4.8)     │ 0     │ 0.0%       │
│ Very Good (4.5-4.7)  │ 0     │ 0.0%       │
│ Good (4.0-4.4)       │ 1     │ 10.0%      │
│ Adequate (3.5-3.9)   │ 5     │ 50.0%      │
│ Needs Work (3.0-3.4) │ 4     │ 40.0%      │
└──────────────────────┴───────┴────────────┘

Average Score: 3.67/5.00 ❌
Target: 4.8/5.0
Questions ≥4.8: 0/10 (0.0%)
```

### 2. Refine Questions

Apply automated transformations to improve quality:

```bash
# Automatic mode (apply all improvements)
python main.py refine questions.jsonl --output refined.jsonl

# Interactive mode (review each change)
python main.py refine questions.jsonl --output refined.jsonl --interactive

# Custom quality threshold
python main.py refine questions.jsonl --output refined.jsonl --threshold 4.5
```

**What Gets Refined:**
- ✅ Single-word questions → Expanded to full questions
- ✅ Abstract variables (x, y, foo) → Real-world names (price, quantity)
- ✅ Western-only names (Alice, Bob) → Globally diverse (Priya, Chen, Amara)
- ✅ Bloom's taxonomy misalignment → Corrected levels
- ✅ Insufficient keywords → Enhanced metadata
- ✅ Missing real-world context → Added practical scenarios

**Output:**
```
🔨 QuestionForge - Batch Refinement

✓ Loaded 10 questions
Average score before: 3.67/5.00

Refining questions... ━━━━━━━━━━━━━━━━ 100%

✨ Refinement Complete!

┌────────────────┬───────────┬───────────┬─────────┐
│ Metric         │ Before    │ After     │ Change  │
├────────────────┼───────────┼───────────┼─────────┤
│ Average Score  │ 3.67/5.00 │ 3.94/5.00 │ ⬆️ +0.27 │
│ Questions ≥4.8 │ 0 (0.0%)  │ 0 (0.0%)  │ ⬆️ +0    │
│ Refined        │ -         │ 6         │ -       │
└────────────────┴───────────┴───────────┴─────────┘

✓ Output saved to: refined.jsonl
```

### 3. Generate Reports

Create before/after comparison reports:

```bash
# Text report to console
python main.py report original.jsonl refined.jsonl

# Generate HTML dashboard
python main.py report original.jsonl refined.jsonl --html

# Generate detailed JSON report
python main.py report original.jsonl refined.jsonl --json
```

**Report Types:**

**Text Report** (console):
```
============================================================
BEFORE/AFTER REFINEMENT REPORT
============================================================

BEFORE: Average 3.67/5.00 | Pass: 0 (0.0%)
AFTER:  Average 3.94/5.00 | Pass: 0 (0.0%) ⬆️ +0.27

DISTRIBUTION CHANGES:
Good (4.0-4.4):       1 → 4  (+3)
Needs Work (3.0-3.4): 4 → 1  (-3)
```

**HTML Report**: Visual dashboard with color-coded quality bars

**JSON Report**: Complete metrics with scores, issues, and refinement history

## Quest & Crossfire Compliance

QuestionForge embodies the **"Small fixes, big clarity"** philosophy:

### 1. **Small Fixes**
- One transformation per question per run
- Targeted, surgical improvements
- Preserves original intent and metadata

### 2. **Big Clarity**
- Transparent scoring (5 criteria breakdown)
- Detailed refinement history tracking
- Before/after comparisons

### 3. **Systematic**
- Repeatable, data-driven process
- Consistent quality standards (4.8/5 threshold)
- Automated validation

### 4. **Reflective**
- Tracks all transformations
- Shows score improvements
- Enables rollback if needed

### 5. **Honest**
- Real scores, no inflation
- Clear identification of issues
- Realistic improvement expectations

## Scoring System

Questions are evaluated across **5 criteria**:

### 1. Adult Learning (25% weight)
**What it measures:** Practical relevance, real-world context, problem-oriented

**High score:**
- Uses realistic variable names (price, quantity, username)
- Includes business/industry context
- Problem-centered scenarios

**Low score:**
- Abstract variables (x, y, foo, bar)
- Academic/theoretical framing
- Lacks real-world application

### 2. People-First Principles (20% weight)
**What it measures:** Inclusive language, diverse representation, appropriate complexity

**High score:**
- Globally diverse names (Priya, Chen, Amara, Kofi)
- Gender-neutral examples
- Culturally aware content

**Low score:**
- Western-only names (Alice, Bob, John)
- Gendered assumptions
- Single cultural perspective

### 3. Bloom's Taxonomy Alignment (20% weight)
**What it measures:** Cognitive level matches difficulty tier

**Alignment:**
- **Starter** → Remember/Understand
- **Core** → Apply/Analyze
- **Stretch** → Analyze/Evaluate/Create

**Misalignment:**
- Stretch question with "Remember" level
- Starter question requiring "Create" level

### 4. Practical Application (20% weight)
**What it measures:** Industry tools, frameworks, job relevance

**High score:**
- Mentions tools (pytest, debugger, linters)
- References frameworks/libraries
- Career-relevant skills

**Low score:**
- Pure syntax without context
- No mention of tools/workflows
- Disconnected from practice

### 5. RAG Optimization (15% weight)
**What it measures:** Search readiness (keyword + semantic)

**High score:**
- 5-15 relevant keywords
- Question length ≥50 characters
- Rich metadata (subtopics, context)

**Low score:**
- < 5 keywords
- Single-word questions
- Missing metadata

## Transformation Strategies

QuestionForge applies transformations in priority order:

### 1. Expand Single-Word Questions
**Before:**
```json
{
  "question": "indentation",
  "style": "single_word"
}
```

**After:**
```json
{
  "question": "In Python, what syntactic feature determines code block structure, replacing curly braces used in languages like Java?",
  "style": "short_question"
}
```

**Score improvement:** +0.5 to +1.5

### 2. Replace Abstract Variables
**Before:**
```json
{
  "question": "What happens when you swap x and y?",
  "code_context": "x = 5\ny = 10"
}
```

**After:**
```json
{
  "question": "What happens when you swap current_price and new_price?",
  "code_context": "current_price = 5\nnew_price = 10"
}
```

**Score improvement:** +0.3 to +0.9

### 3. Diversify Names
**Before:**
```json
{
  "question": "Calculate Alice's total score",
  "code_context": "alice_scores = [85, 90, 78]"
}
```

**After:**
```json
{
  "question": "Calculate Priya's total score",
  "code_context": "priya_scores = [85, 90, 78]"
}
```

**Score improvement:** +0.2 to +0.6

### 4. Add Real-World Context
**Before:**
```json
{
  "question": "Process a list of numbers",
  "style": "scenario_task"
}
```

**After:**
```json
{
  "question": "You're building a sales analytics dashboard. Process a list of customer order values to calculate total revenue.",
  "style": "scenario_task"
}
```

**Score improvement:** +0.4 to +1.0

### 5. Fix Bloom's Alignment
**Before:**
```json
{
  "difficulty": "core",
  "bloom_level": "remember",  // Misaligned
  "style": "predict_output"
}
```

**After:**
```json
{
  "difficulty": "core",
  "bloom_level": "apply",     // Corrected
  "style": "predict_output"
}
```

**Score improvement:** +0.2 to +0.4

### 6. Enhance Keywords
**Before:**
```json
{
  "keywords": ["python", "function"]
}
```

**After:**
```json
{
  "keywords": ["python", "function", "def", "return", "parameter", "argument", "call"]
}
```

**Score improvement:** +0.1 to +0.3

## Configuration

Customize scoring and transformations in `config.yaml`:

```yaml
scoring:
  weights:
    adult_learning: 0.25
    people_first: 0.20
    blooms: 0.20
    practical: 0.20
    rag: 0.15

  threshold: 4.8  # Quality bar for flagship content

templates:
  diverse_names:
    - Priya      # Indian
    - Chen       # Chinese
    - Amara      # African
    - Sofia      # Spanish
    - Ahmed      # Arabic
    - Yuki       # Japanese
    - Carlos     # Latin American

  realistic_variables:
    financial: [price, cost, revenue, profit, total]
    user_data: [username, email, password, user_id]
    measurements: [height, weight, temperature, distance]

  real_world_contexts:
    web_development:
      - "building a REST API for a todo app"
      - "processing user registration forms"
    data_analysis:
      - "analyzing customer purchase patterns"
      - "calculating quarterly sales metrics"
    automation:
      - "automating file backup workflows"
      - "scraping product data from e-commerce sites"

rag:
  min_keywords: 5
  max_keywords: 15
```

## Best Practices

### Iterative Refinement
Run refinement multiple times for best results:

```bash
# Round 1: Fix major issues
python main.py refine bank.jsonl -o round1.jsonl

# Round 2: Additional improvements
python main.py refine round1.jsonl -o round2.jsonl

# Round 3: Final polish
python main.py refine round2.jsonl -o final.jsonl

# Compare progress
python main.py report bank.jsonl final.jsonl
```

**Expected progression:**
- Round 1: 3.5 → 3.8 (+0.3)
- Round 2: 3.8 → 4.2 (+0.4)
- Round 3: 4.2 → 4.6 (+0.4)
- Rounds 4-5: 4.6 → 4.8+ (final push to threshold)

### Interactive Review for Critical Content
Use `--interactive` for high-stakes question banks:

```bash
python main.py refine flagship_questions.jsonl -o refined.jsonl --interactive
```

This allows you to:
- Review each suggested change
- Accept/reject transformations
- Preserve domain-specific terminology
- Maintain brand voice

### Backup Original Files
Always preserve originals:

```bash
cp questions.jsonl questions_backup.jsonl
python main.py refine questions.jsonl -o questions_refined.jsonl
```

### Validate After Refinement
Check that refinement actually improved scores:

```bash
# Before
python main.py analyze original.jsonl

# After
python main.py analyze refined.jsonl

# Comparison
python main.py report original.jsonl refined.jsonl
```

## Troubleshooting

### "Average score decreased after refinement"
**Cause:** Transformation introduced new issues (rare)

**Solution:**
1. Review refinement_history in output JSONL
2. Identify problematic transformation
3. Manually revert or adjust
4. Submit issue on GitHub

### "No questions were refined"
**Cause:** All questions already meet threshold

**Solution:**
- Check with `python main.py analyze` first
- Lower threshold if needed: `--threshold 4.5`
- Questions may already be high quality!

### "Score improved but still below 4.8"
**Cause:** Multiple issues per question, tool applies one per run

**Solution:**
Run multiple refinement rounds (see Best Practices above)

### "Windows encoding error with emojis"
**Cause:** Windows console doesn't support UTF-8 by default

**Solution:**
Already fixed in main.py (v1.0). If issue persists:
```bash
# Run with UTF-8 encoding
chcp 65001
python main.py analyze questions.jsonl
```

## Advanced Usage

### Custom Transformation Pipeline
Edit `refiner/transformers.py` to add custom transformations:

```python
def _add_custom_context(self, q: Question) -> Tuple[Question, str]:
    """Add your domain-specific context"""
    if q.topic == "Your Topic":
        q.question = f"[Custom Context] {q.question}"
    return q, "custom_context_added"
```

### Batch Processing Large Question Banks
For 500+ questions, use batching:

```bash
# Split into chunks
split -l 100 questions.jsonl chunk_

# Process each chunk
for file in chunk_*; do
    python main.py refine $file -o refined_$file
done

# Merge results
cat refined_chunk_* > all_refined.jsonl
```

### Integration with CI/CD
Enforce quality standards in your pipeline:

```yaml
# .github/workflows/question-quality.yml
name: Question Quality Check
on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: |
          cd question-forge
          python main.py analyze ../questions.jsonl
          # Exit 1 if average < 4.8
```

## Output File Formats

### JSONL Format (questions.jsonl)
```json
{
  "id": "py-fund-001",
  "topic": "Functions",
  "question": "What keyword defines a function?",
  "style": "single_word",
  "difficulty": "starter",
  "bloom_level": "remember",
  "keywords": ["function", "def", "syntax"],
  "original_question": "def",  // If refined
  "refinement_history": [
    {
      "timestamp": "2025-11-04T06:00:00",
      "strategy": "expand_single_word",
      "old_question": "def",
      "new_question": "What keyword defines a function?",
      "score_improvement": 0.85
    }
  ],
  "quality_scores": {
    "adult_learning": 3.5,
    "people_first": 3.0,
    "blooms": 5.0,
    "practical": 3.0,
    "rag": 4.5,
    "overall": 3.75
  }
}
```

### JSON Report Format
```json
{
  "meta": {
    "generated": "2025-11-04T06:00:00",
    "total_questions": 10,
    "tool": "QuestionForge v1.0",
    "philosophy": "Small fixes, big clarity"
  },
  "summary": {
    "average_score": 3.94,
    "passed": 0,
    "failed": 10,
    "pass_rate": 0.0,
    "distribution": {
      "excellent": 0,
      "very_good": 0,
      "good": 4,
      "adequate": 5,
      "needs_work": 1,
      "poor": 0
    }
  },
  "questions": [
    // ... detailed per-question metrics
  ]
}
```

## FAQ

**Q: How long does refinement take?**
A: ~0.1-0.3 seconds per question. 100 questions ≈ 10-30 seconds.

**Q: Will my original questions be overwritten?**
A: No. Output is always written to a new file specified with `--output`.

**Q: Can I undo a refinement?**
A: Yes. The `original_question` field preserves the original text, and `refinement_history` tracks all changes.

**Q: What if I disagree with a transformation?**
A: Use `--interactive` mode to review and reject unwanted changes, or manually edit the output JSONL.

**Q: Does this work with languages other than Python questions?**
A: Currently optimized for Python, but can be adapted. Edit `config.yaml` to customize for your domain.

**Q: How does this compare to manual review?**
A: QuestionForge handles structural/metadata issues faster than humans. Manual review still valuable for domain accuracy and nuance.

**Q: Is 4.8/5 realistic?**
A: Yes, with 3-5 refinement rounds + manual touch-ups. Flagship content deserves flagship quality!

## Support

**Issues:** https://github.com/your-repo/question-forge/issues
**Documentation:** https://github.com/your-repo/question-forge/wiki
**Philosophy:** "Small fixes, big clarity" - Quest & Crossfire

---

**Built with ◇ by the Quest & Crossfire Arsenal**

*Where chaos becomes clarity.*
