---
title: QuestionForge v2.0
emoji: 🔥
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# 🔥 QuestionForge v2.0

**"Small fixes, big clarity"** - Quest & Crossfire

Professional question quality assessment validated against academic and industry standards.

## 🎯 What is QuestionForge?

QuestionForge transforms mediocre educational questions into flagship-quality assessments through systematic, data-driven improvements.

**7-Criteria Scoring System:**
1. **Adult Learning (20%)** - Real-world context, practical examples
2. **People-First (15%)** - Inclusive language, diverse representation
3. **Bloom's Alignment (15%)** - Correct cognitive level for difficulty
4. **Practical Application (15%)** - Industry relevance, tool awareness
5. **RAG Optimization (10%)** - Keyword richness, searchability
6. **Construct Validity (15%)** - Measures what it claims to measure
7. **Cognitive Depth (10%)** - Six Facets of Understanding

**Target:** ≥4.8/5.0 for flagship quality

---

## 🎓 Standards Validation

QuestionForge v2.0 is validated against top-tier academic and industry standards:

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

### 1. Analyze Questions
- Upload your JSONL file
- Click "Analyze Quality"
- Review scores and distribution

### 2. Refine Questions
- Upload your JSONL file
- Enable auto-apply
- Click "Refine Questions"
- Download improved questions

### 3. Compare Results
- Upload original and refined files
- Click "Generate Comparison"
- Review improvements

---

## 📝 Question Format (JSONL)

Upload a JSONL file where each line is a JSON object:

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

**Required fields:** `id`, `topic`, `question`, `style`, `difficulty`

**Supported styles:** `single_word`, `short_question`, `predict_output`, `debug_fix`, `scenario_task`, `fill_in_blank`, `explain_concept`, `compare_contrast`, `rewrite`

---

## 🔒 Privacy

This is a **private space**. Your questions are:
- ✅ Processed in real-time
- ✅ Never stored permanently
- ✅ Not shared with anyone
- ✅ Secure and confidential

---

## 💡 Example Use Cases

- **Course Developers:** Ensure question quality before publishing
- **Assessment Teams:** Validate exam questions against standards
- **Content Creators:** Improve learning materials systematically
- **Educators:** Get data-driven feedback on question design

---

## 📊 Quality Thresholds

- **≥4.8** - Excellent (flagship quality)
- **4.5-4.7** - Very Good (minor improvements)
- **4.0-4.4** - Good (acceptable)
- **3.5-3.9** - Adequate (needs work)
- **<3.5** - Needs significant improvement

---

## 🎯 Current Scope (v2.0)

**Content Type:** Educational questions with learning objectives

**Language:** Python programming (v2.1 will add JavaScript, Java)

**Use Case:** Question bank quality improvement

---

## 📈 Roadmap

- **v2.1:** Multi-language support (JavaScript, Java)
- **v2.5:** Content quality assessment (tutorials, docs)
- **v3.0:** Psychometric validation with student data

---

## 📞 Support

**Built by:** Asheesh for Aethelgard Academy

**Contact:** Quest & Crossfire Arsenal

**Version:** 2.0.0

**Philosophy:** "Small fixes, big clarity" 🔥

---

## 📚 Documentation

For comprehensive documentation, see:
- [Validation Framework](https://github.com/yourusername/questionforge/blob/main/VALIDATION_FRAMEWORK.md)
- [Expert Review Rubric](https://github.com/yourusername/questionforge/blob/main/EXPERT_REVIEW_RUBRIC.md)
- [Scope Analysis](https://github.com/yourusername/questionforge/blob/main/SCOPE_ANALYSIS.md)

---

**Transform your questions from good to flagship. Try QuestionForge today!** ✨
