# 🔥 QuestionForge v2.0

**Professional Question Quality Assessment & Refinement Tool**

Transform educational questions into high-quality assessments using research-backed standards from CMU, AWS, and ISO certifications.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace%20Space-yellow)](https://huggingface.co/spaces/asheeshsrivastava9/Qnc-QuestionForger)

> **"Small fixes, big clarity."** - Targeted improvements that dramatically enhance question quality.

---

## 🚀 Live Demo

Try QuestionForge now: **[https://huggingface.co/spaces/asheeshsrivastava9/Qnc-QuestionForger](https://huggingface.co/spaces/asheeshsrivastava9/Qnc-QuestionForger)**

**Current Status:**
- ✅ **Phase 1 (LIVE):** Question analysis & quality scoring
- 🛠️ **Phase 2 (In Progress):** Automated refinement & before/after comparison

---

## ✨ What Is QuestionForge?

QuestionForge analyzes educational questions using **7 research-backed quality criteria** and provides actionable scores to improve your content.

### 7 Quality Criteria

| Criterion | Weight | Based On |
|-----------|--------|----------|
| **Adult Learning Principles** | 20% | Andragogy, real-world context |
| **People-First Language** | 15% | Inclusive, learner-centered tone |
| **Bloom's Taxonomy Alignment** | 15% | Cognitive level matching |
| **Practical Application** | 15% | Industry relevance, hands-on skills |
| **RAG Optimization** | 10% | Search-friendly, retrievable |
| **Construct Validity** | 15% | Tests what it claims (Wiggins & McTighe) |
| **Cognitive Depth** | 10% | Six Facets of Understanding |

**Target Quality:** 4.8/5.0

---

## 📊 Standards & Research

QuestionForge combines:

### Academic Foundations
- **CMU Eberly Center** - Teaching Excellence & Educational Innovation
- **Wiggins & McTighe** - Understanding by Design (UbD)
- **Bloom's Taxonomy** - Anderson & Krathwohl Revised Taxonomy
- **ACM SIGCSE** - Computer Science Education Standards

### Industry Standards
- **AWS SME Item Writing Standards** - Professional certification best practices
- **NCCA Accreditation Standards** - National Commission for Certifying Agencies
- **ISO 17024/29990** - Certification and learning services quality

---

## 🎯 Key Features

### Current (Phase 1)
- ✅ **7-Criteria Quality Scoring** - Comprehensive analysis across all dimensions
- ✅ **Detailed Reports** - Question-by-question breakdown with improvement suggestions
- ✅ **JSONL Format Support** - Optimized for RAG/AI systems
- ✅ **Batch Processing** - Analyze entire question banks
- ✅ **Export Options** - JSON, CSV, Markdown reports

### Coming Soon (Phase 2)
- 🛠️ **Automated Refinement** - AI-powered question transformation to 4.8/5.0
- 🛠️ **Before/After Comparison** - Visual diff showing improvements
- 🛠️ **Interactive Review Mode** - Approve/reject suggestions
- 🛠️ **Bulk Refinement** - Process hundreds of questions efficiently

### Future (Phase 3+)
- 🔮 **Multi-Language Support** - JavaScript, Java, SQL, and more
- 🔮 **General Content Quality** - Beyond programming questions
- 🔮 **Psychometric Analysis** - IRT models for assessment science

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/AsheeshSrivastava/question-forge.git
cd question-forge
pip install -r requirements.txt
```

### Usage (CLI)

```bash
# Analyze questions
python main.py analyze questions.jsonl

# Refine questions (Phase 2 - coming soon)
python main.py refine questions.jsonl --output refined.jsonl

# Generate comparison report (Phase 2 - coming soon)
python main.py report original.jsonl refined.jsonl
```

### Usage (Web App)

1. Visit: [https://huggingface.co/spaces/asheeshsrivastava9/Qnc-QuestionForger](https://huggingface.co/spaces/asheeshsrivastava9/Qnc-QuestionForger)
2. Upload your JSONL file
3. Click "Analyze Quality"
4. View detailed scores and suggestions

---

## 📝 Question Format (JSONL)

QuestionForge accepts **JSONL** files (one JSON object per line).

### Minimal Example
```json
{"id": "q-001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter"}
```

### Complete Example
```json
{
  "id": "q-py-001",
  "topic": "Python Basics",
  "subtopics": ["variables", "syntax"],
  "question": "How would you explain variables to a beginner programmer?",
  "style": "explain_concept",
  "difficulty": "starter",
  "bloom_level": "understand",
  "keywords": ["variable", "declaration", "syntax", "memory"],
  "prerequisites": [],
  "code_context": "x = 5\ny = 'hello'"
}
```

### Required Fields
- `id` - Unique identifier
- `topic` - Subject category
- `question` - Question text
- `style` - Question format (see valid values below)
- `difficulty` - Level: `starter`, `core`, or `stretch`

### Optional Fields (Recommended)
- `bloom_level` - Cognitive level: `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create`
- `keywords` - Array of search terms for RAG
- `subtopics` - Subcategories
- `prerequisites` - Prerequisite question IDs
- `code_context` - Code snippet for context

### Valid Question Styles
- `single_word` - One-word answer
- `short_question` - Brief question
- `predict_output` - Code output prediction
- `debug_fix` - Find and fix bug
- `scenario_task` - Real-world task
- `fill_in_blank` - Complete code/text
- `explain_concept` - Explain in detail
- `compare_contrast` - Compare two concepts
- `rewrite` - Improve/refactor code

📖 **Complete Format Guide:** See `USER_GUIDE_FILE_FORMAT.md`

---

## 🛠️ Project Structure

```
question-forge/
├── refiner/                   # Core refinement engine
│   ├── __init__.py            # Package exports
│   ├── parser.py              # JSONL parsing & validation
│   ├── analyzer.py            # 7-criteria quality scoring
│   ├── transformers.py        # Question transformation logic
│   ├── validators.py          # Threshold validation
│   └── reporters.py           # Report generation
├── strategies/                # Transformation strategies
├── templates/                 # Question templates
├── examples/                  # Sample question files
├── main.py                    # CLI interface
├── app.py                     # Gradio web interface
├── config.yaml                # Configuration
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── QUICK_START.md             # Getting started guide
├── USER_GUIDE_FILE_FORMAT.md  # Complete format specification
├── CONVERSION_GUIDE.md        # Database to JSONL conversion
└── ROADMAP.md                 # Future development plans
```

---

## 📊 Example Results

### Before QuestionForge
```
Question: "Explain polymorphism"
Score: 3.2/5.0

Issues:
❌ No people-first language
❌ No real-world context
❌ Passive, abstract tone
❌ Missing practical application
```

### After QuestionForge (Phase 2)
```
Question: "You're building a payment system that needs to process
credit cards, PayPal, and cryptocurrency. How would you use
polymorphism to handle these different payment methods?"

Score: 4.8/5.0

Improvements:
✅ Direct address ("You're building...")
✅ Real-world scenario (payment system)
✅ Concrete examples (credit cards, PayPal, crypto)
✅ Practical application (industry-relevant)
```

---

## 🎯 Who Should Use QuestionForge?

- **Educators & Instructional Designers** - Creating course assessments
- **Certification Programs** - Ensuring question quality standards
- **EdTech Companies** - Maintaining high-quality content
- **Training Departments** - Developing workplace learning materials
- **Bootcamp Instructors** - Validating technical questions
- **Content Creators** - Building educational resources

---

## 📈 Roadmap

### v2.0 (Current) - Analysis & Scoring ✅
- ✅ 7-criteria quality analysis
- ✅ Detailed scoring reports
- ✅ JSONL format support
- ✅ Web app (Hugging Face Spaces)
- ✅ CLI interface
- 🛠️ Automated refinement (Phase 2 - in progress)

### v2.1 (Q1 2025) - Multi-Language Support
- JavaScript question analysis
- Java question analysis
- SQL question analysis
- Generic programming questions

### v2.5 (Q2 2025) - ContentForge
- General content quality assessment
- Tutorial and documentation analysis
- Non-programming educational content

### v3.0 (2025-2026) - Psychometric Analysis
- Item Response Theory (IRT) models
- Difficulty calibration
- Discrimination analysis
- Full assessment science integration

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
1. **Test & Provide Feedback** - Try the tool with your question banks
2. **Report Issues** - Found a bug or have a suggestion? Open an issue
3. **Improve Documentation** - Help make guides clearer
4. **Add Features** - Submit pull requests for new functionality
5. **Share Use Cases** - Tell us how you're using QuestionForge

### Development Setup
```bash
git clone https://github.com/AsheeshSrivastava/question-forge.git
cd question-forge
pip install -r requirements.txt
python main.py --help
```

### Testing Your Changes
```bash
# Run with sample questions
python main.py analyze examples/example_input.json
```

---

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
- **[USER_GUIDE_FILE_FORMAT.md](USER_GUIDE_FILE_FORMAT.md)** - Complete file format specification
- **[CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)** - Convert from CSV/Excel/Database
- **[DATABASE_TO_JSONL_QUICKSTART.md](DATABASE_TO_JSONL_QUICKSTART.md)** - 5-minute database conversion
- **[ROADMAP.md](ROADMAP.md)** - Future development plans
- **[SCOPE_ANALYSIS.md](SCOPE_ANALYSIS.md)** - Current capabilities & limitations

---

## 🧪 Testing

Sample question files included in `examples/`:
- `example_input.csv` - CSV template
- `example_input.json` - JSON template
- Test files with 105 Python questions (starter, core, stretch)

```bash
# Test with sample file
python main.py analyze examples/example_input.json
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means
- ✅ Free to use for commercial and non-commercial projects
- ✅ Can modify and distribute
- ✅ Must include original license and copyright notice
- ✅ No warranty provided

---

## 👨‍💻 Author

**Asheesh Ranjan Srivastava**
- **Email:** asheeshsrivastava9@gmail.com
- **LinkedIn:** [linkedin.com/in/asheesh-ranjan-srivastava](https://www.linkedin.com/in/asheesh-ranjan-srivastava/)
- **GitHub:** [github.com/AsheeshSrivastava](https://github.com/AsheeshSrivastava)
- **Portfolio:** [AsheeshSrivastava/portfolio](https://github.com/AsheeshSrivastava/portfolio)

---

## 🙏 Acknowledgments

### Research & Standards
- **CMU Eberly Center** for Teaching Excellence frameworks
- **Grant Wiggins & Jay McTighe** for Understanding by Design
- **Anderson & Krathwohl** for Bloom's Taxonomy Revision
- **AWS** for SME Item Writing Standards
- **NCCA** for accreditation guidelines
- **ISO** for international quality standards

### Inspiration
Built with the **"Small fixes, big clarity"** philosophy from Quest & Crossfire, emphasizing that incremental, systematic improvements compound into excellence.

---

## 📞 Support & Feedback

### Get Help
- **Documentation:** Check guides in the repository
- **Issues:** [Open an issue](https://github.com/AsheeshSrivastava/question-forge/issues) on GitHub
- **Email:** asheeshsrivastava9@gmail.com

### Share Feedback
Using QuestionForge? We'd love to hear about it!
- Share your results
- Suggest improvements
- Report what's working well

---

## 🎯 Current Focus

**Phase 2 Development (In Progress):**
- Automated question refinement to 4.8/5.0 target
- Before/after comparison visualization
- Interactive review and approval workflow
- Batch processing for large question banks

**Want to help?** We're looking for:
- Educators to test Phase 1 analysis
- Question banks to validate against
- Feedback on quality criteria
- Ideas for Phase 2 features

---

## ⭐ Star This Repo

If QuestionForge helps improve your educational content, please star this repository!

---

**Built with rigor. Focused on clarity. Designed for impact.** 🔥

**"Small fixes, big clarity."** - Transform your questions systematically.

---

## 📈 Statistics

- **Lines of Code:** 3,000+ (Python)
- **Documentation:** 20,000+ words across 10+ guides
- **Test Questions:** 105 sample Python questions included
- **Quality Criteria:** 7 research-backed standards
- **Supported Formats:** JSONL, JSON, CSV
- **Deployment:** HuggingFace Spaces (public demo)
- **Status:** Phase 1 Live | Phase 2 In Development

---

Last Updated: November 2025
