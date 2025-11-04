# Contributing to QuestionForge

Thank you for your interest in improving question quality assessment!

## 🎯 Project Overview

QuestionForge is a research-backed tool for analyzing educational questions based on CMU, AWS, and ISO standards. Contributions should maintain this academic rigor.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Familiarity with educational assessment (helpful)
- Understanding of Bloom's Taxonomy (helpful)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AsheeshSrivastava/question-forge.git
   cd question-forge
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   # CLI mode
   python main.py analyze examples/example_input.json

   # Gradio web interface
   python app.py
   ```

## 📐 Code Standards

### Python
- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Add docstrings (Google style) to all functions
- Maximum line length: 88 characters (Black formatter)

Example:
```python
def analyze_question(question: str, criteria: dict) -> float:
    """Analyze a question against quality criteria.

    Args:
        question: The question text to analyze
        criteria: Dictionary of scoring criteria

    Returns:
        Quality score between 0.0 and 5.0

    Raises:
        ValueError: If question is empty or criteria invalid
    """
    pass
```

### Documentation
- Update README for new features
- Add examples for new functionality
- Document scoring criteria changes
- Update ROADMAP.md for major features

### Quality Framework
- **Do not** modify scoring criteria without research backing
- Cite sources for new criteria
- Maintain weighted scoring integrity
- Preserve educational theory alignment

## 🔬 Research Standards

This project is grounded in educational research. When adding features:

1. **Cite sources** - Reference academic papers, standards, or frameworks
2. **Maintain validity** - New criteria should be empirically justified
3. **Document rationale** - Explain why changes improve question quality
4. **Test thoroughly** - Use diverse question types for validation

**Example of good research backing:**
```markdown
**New Criterion:** Scenario-Based Context

**Research Foundation:**
- Merrill's First Principles of Instruction (problem-centered learning)
- Schank's Goal-Based Scenarios (1994)
- Situated cognition theory (Brown, Collins, & Duguid, 1989)

**Rationale:** Questions with authentic scenarios show higher
engagement and transfer to real-world applications.

**Implementation:** Award points for questions that include
realistic contexts, stakeholders, and constraints.
```

## 🧪 Testing

### Running Tests
```bash
# If tests exist
pytest tests/ -v

# Test with sample files
python main.py analyze examples/example_input.json
```

### Adding Tests
- Test new scoring criteria
- Test edge cases (empty questions, long questions, special characters)
- Test file format conversions
- Verify scoring consistency

**Example test structure:**
```python
def test_adult_learning_scoring():
    """Test that adult learning principles are scored correctly."""
    question_with_context = {
        "question": "You're managing a team project...",
        "style": "scenario_task"
    }
    score = analyzer.score_adult_learning(question_with_context)
    assert score >= 4.0  # Should score high for "You're" and scenario

    question_without_context = {
        "question": "Define polymorphism",
        "style": "short_question"
    }
    score = analyzer.score_adult_learning(question_without_context)
    assert score <= 2.0  # Should score low for abstract question
```

## 🔧 Pull Request Process

1. **Create feature branch**
   ```bash
   git checkout -b feature/scoring-enhancement
   ```

2. **Make changes**
   - Follow code standards
   - Add tests
   - Update documentation

3. **Run quality checks**
   ```bash
   # Format code (if using Black)
   black refiner/

   # Run linter
   flake8 refiner/

   # Run tests
   pytest tests/

   # Test with sample files
   python main.py analyze examples/example_input.json
   ```

4. **Commit changes**
   ```bash
   git commit -m "feat: add metacognitive scoring dimension"
   ```

   **Commit message format:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation only
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance

5. **Push and create PR**
   ```bash
   git push origin feature/scoring-enhancement
   ```

   **In your Pull Request, include:**
   - Clear description of changes
   - Reference research/sources
   - Explain educational benefit
   - Test results
   - Before/after examples (if applicable)

**Good PR Description Example:**
```markdown
## New Feature: Metacognitive Prompting Criterion

### Research Foundation
- Flavell's Metacognition Theory (1979)
- Zimmerman's Self-Regulated Learning (2002)
- Schraw & Dennison's Metacognitive Awareness Inventory

### What This Adds
Scores questions based on whether they prompt learners to:
- Reflect on their thinking process
- Evaluate their approach
- Consider alternative strategies

### Example
**Before (Score 2.5):**
"Write a function to sort a list"

**After (Score 4.5):**
"Write a function to sort a list. Which sorting algorithm did you choose
and why? How would your choice change for very large datasets?"

### Test Results
- Tested on 105 sample questions
- Correlation with expert ratings: 0.82
- Adds ~0.3 to overall quality scores for questions with metacognitive prompts
```

## 📂 Project Structure

```
question-forge/
├── refiner/                   # Core refinement engine
│   ├── __init__.py            # Package exports
│   ├── parser.py              # JSONL parsing & validation
│   ├── analyzer.py            # 7-criteria quality scoring
│   ├── transformers.py        # Question transformation logic
│   ├── validators.py          # Threshold validation
│   ├── reporters.py           # Report generation
│   └── rag_optimizer.py       # RAG optimization scoring
├── strategies/                # Transformation strategies (Phase 2)
├── templates/                 # Question templates (Phase 2)
├── examples/                  # Sample question files
│   ├── example_input.csv      # CSV template
│   ├── example_input.json     # JSON template
│   └── test_*.jsonl           # Test question banks
├── main.py                    # CLI interface
├── app.py                     # Gradio web interface
├── config.yaml                # Configuration
├── requirements.txt           # Dependencies
├── LICENSE                    # AGPL-3.0
├── CONTRIBUTING.md            # This file
└── README.md                  # Project documentation
```

## 📊 Contribution Areas

### High Priority ✅
- Phase 2 implementation (automated refinement)
- Validation testing with real educators
- Support for more question types (JavaScript, Java, SQL)
- Psychometric analysis tools

### Medium Priority 🟡
- Additional export formats (PDF, XML)
- Batch processing optimization
- UI/UX improvements for Gradio interface
- More comprehensive examples

### Low Priority 🔵
- Internationalization (non-English questions)
- Cloud deployment options
- Integration with LMS platforms (Moodle, Canvas)

## 🐛 Bug Reports

Include:
- Question input (if safe to share)
- Expected vs actual scoring
- Error messages and full traceback
- Python version and OS
- Input file format (JSONL, JSON, CSV)

**Example Bug Report:**
```markdown
**Bug:** Adult Learning scoring gives 0.0 for scenario questions

**Question Input:**
{
  "question": "You're building a payment system...",
  "style": "scenario_task"
}

**Expected:** Score ~4.0+ (has "You're" and real-world context)
**Actual:** Score 0.0

**Error Log:**
```
Traceback (most recent call last):
  File "refiner/analyzer.py", line 45, in score_adult_learning
    score = criteria.get('adult_learning', 0)
KeyError: 'adult_learning'
```

**Environment:**
- Python: 3.9.7
- OS: Windows 11
- QuestionForge version: 2.0
```

## 💡 Feature Requests

For new features, please:

1. **Check if it already exists** - Review ROADMAP.md and open issues
2. **Explain educational value** - Why does this improve question quality?
3. **Provide use cases** - Who benefits and how?
4. **Cite research** if applicable
5. **Consider implementation complexity**

**Good Feature Request Example:**
```markdown
**Feature:** Distractor Analysis for Multiple Choice Questions

**Educational Value:**
Analyzes distractors (wrong answers) to ensure they:
- Represent common misconceptions
- Are plausible but incorrect
- Test understanding, not trick knowledge

**Use Cases:**
- Certification exam writers validating distractor quality
- Educators creating formative assessments
- EdTech companies maintaining question banks

**Research Foundation:**
- Haladyna & Downing (1989) - Distractor writing guidelines
- Case & Swanson (1998) - Constructing Written Test Questions

**Implementation Complexity:** Medium
- Need MC question format support
- Distractor quality heuristics
- Misconception detection
```

## 🔍 Code Review Checklist

Before submitting PR, verify:

- [ ] Code follows PEP 8
- [ ] Functions have docstrings
- [ ] Type hints added
- [ ] Tests written (if applicable)
- [ ] Documentation updated
- [ ] No hardcoded values (use config.yaml)
- [ ] Error handling in place
- [ ] Research sources cited (if new criteria)
- [ ] Tested with sample questions

## ❓ Questions & Support

- **Email:** asheesh.srivastava@questabdcrossfire.com
- **LinkedIn:** [linkedin.com/in/asheesh-ranjan-srivastava](https://www.linkedin.com/in/asheesh-ranjan-srivastava/)
- **Issues:** GitHub issues with `question` label
- **Documentation:** Check guides in repository:
  - `QUICK_START.md` - Getting started
  - `USER_GUIDE_FILE_FORMAT.md` - File format details
  - `CONVERSION_GUIDE.md` - Database conversion
  - `ROADMAP.md` - Future plans

## 📜 License

By contributing, you agree that your contributions will be licensed under **AGPL-3.0**.

This means:
- Your code remains open source
- Derivative works must also be AGPL-3.0
- Network use triggers source disclosure requirement
- Commercial use is allowed (with license compliance)

## ⚠️ Important Notes

### For Educators
- This tool is for **assessment quality improvement**, not cheating detection
- Use ethically and in compliance with your institution's policies
- Test thoroughly before using for high-stakes assessments

### For Developers
- Maintain academic integrity in all contributions
- Don't game the scoring system with keyword stuffing
- Focus on genuine quality improvements
- Preserve research foundations

### For Researchers
- We welcome validation studies
- If you use QuestionForge in research, please cite this repository
- Share findings to improve the tool

## 🙏 Acknowledgments

Contributions welcome from:
- **Educators** - Validate criteria, test with real questions
- **Developers** - Code improvements, new features
- **Researchers** - Validation studies, psychometric analysis
- **Writers** - Documentation improvements
- **Testers** - Bug reports, edge cases

---

## 🎯 Current Focus (Phase 2)

We're currently building:
- **Automated refinement** - Transform questions to 4.8/5.0
- **Before/after comparison** - Visual diff of improvements
- **Interactive review** - Approve/reject suggestions
- **Bulk processing** - Handle large question banks

**Want to help?** We're looking for:
- Educators to test Phase 1 analysis
- Question banks to validate against (any subject)
- Feedback on quality criteria weights
- Ideas for transformation strategies

---

**Built with rigor. Focused on clarity. Designed for impact.** 🔥

**"Small fixes, big clarity."** - Systematic improvements compound into excellence.
