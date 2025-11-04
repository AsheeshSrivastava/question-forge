# QuestionForge - Scope Analysis & Extension Opportunities

**Date:** November 4, 2025
**Version:** 2.0
**Purpose:** Define current scope, limitations, and extension possibilities

---

## 🎯 Current Scope (v2.0)

### ✅ What QuestionForge IS Designed For

**1. Educational Questions (Primary Use Case)**
- Assessment questions with learning objectives
- Question formats: single_word, short_question, predict_output, debug_fix, scenario_task, fill_in_blank, explain_concept, compare_contrast, rewrite
- Metadata: Bloom's level, difficulty, style, keywords, prerequisites
- Purpose: Evaluate student understanding

**2. Python Programming Focus**
- Python-specific terminology (PEP 8, LEGB, GIL, MRO)
- Python best practices validation
- Python code examples and syntax
- Python development workflows

**3. Educational Quality Assessment**
- Adult learning principles (andragogy)
- Pedagogical soundness (Bloom's taxonomy)
- People-first inclusivity
- Practical application
- Construct validity (measures what it claims)
- Cognitive depth (Six Facets)

### ❌ What QuestionForge is NOT Currently Designed For

**1. General Content Quality Assessment**
- ❌ Tutorial/guide quality
- ❌ Documentation quality
- ❌ Blog post/article quality
- ❌ Code comment quality
- ❌ README file quality

**2. Answer Validation**
- ❌ Does not score answer quality
- ❌ Does not validate correct answers
- ❌ Does not check distractor quality (multiple choice options)
- ❌ Does not grade rubrics

**3. Non-Question Content**
- ❌ Not for code quality analysis (use linters instead)
- ❌ Not for prose/writing quality (use writing tools)
- ❌ Not for video/multimedia content

---

## 🔬 Deep Dive: Can It Be Extended?

### Question 1: Can QuestionForge Assess General Content Quality?

**Short Answer:** 🟡 **PARTIALLY - Requires Significant Adaptation**

#### What Would Transfer Well:

**1. Adult Learning Principles (90% applicable)**
```
✅ Real-world context → Applies to tutorials
✅ Practical examples → Applies to docs
✅ Concrete variables → Applies to code examples
✅ Avoiding abstract → Applies to explanations
```

**2. People-First Principles (100% applicable)**
```
✅ Diverse names → Applies to all content
✅ Inclusive language → Applies to all content
✅ Accessible phrasing → Applies to all content
✅ Growth mindset → Applies to all content
```

**3. Practical Application (80% applicable)**
```
✅ Industry relevance → Applies to tutorials
✅ Tool awareness → Applies to guides
✅ Job-relevant → Applies to training content
⚠️ Best practices → Depends on content type
```

**4. RAG Optimization (100% applicable)**
```
✅ Keyword richness → Applies to all searchable content
✅ Semantic search → Applies to all content
✅ Relationship mapping → Applies to docs
```

**5. Cognitive Depth (70% applicable)**
```
✅ Explanation facet → Applies to tutorials
✅ Application facet → Applies to examples
✅ Perspective facet → Applies to comparisons
⚠️ Self-knowledge → Less relevant for reference docs
```

#### What Would NOT Transfer:

**1. Bloom's Taxonomy (10% applicable)**
```
❌ Designed for learning objectives
❌ Questions assess understanding
❌ Tutorials teach, not assess
⚠️ Could adapt: "What level of understanding does this enable?"
```

**2. Construct Validity (20% applicable)**
```
❌ "Does this question measure what it claims?"
❌ Not applicable to explanatory content
⚠️ Could adapt: "Does this content achieve its stated purpose?"
```

#### Architecture Changes Needed:

**Current Architecture (Question-Specific):**
```python
@dataclass
class Question:
    question: str          # The question text
    style: str            # Question format
    bloom_level: str      # Cognitive level being assessed
    answer_type: str      # Expected answer format
```

**Proposed Generic Architecture:**
```python
@dataclass
class Content:
    content: str          # The main content
    content_type: str     # tutorial, explanation, example, reference
    purpose: str          # What this content aims to achieve
    target_audience: str  # beginner, intermediate, advanced

    # Reuse existing fields
    keywords: List[str]
    prerequisites: List[str]
```

**Effort Required:** 🔴 **HIGH** (4-6 weeks)
- New parser for different content types
- New transformers for content-specific improvements
- Adapt 7 criteria scoring (some need redesign)
- New validation thresholds
- New test suite

**Verdict:**
✅ **POSSIBLE** but requires fork/extension: "ContentForge"
⚠️ **NOT RECOMMENDED** for v2.x - keep focus on questions

---

### Question 2: Can QuestionForge Support Other Programming Languages?

**Short Answer:** 🟢 **YES - Relatively Easy Extension**

#### Current Python-Specific Elements:

**1. Config Templates (config.yaml):**
```yaml
# PYTHON-SPECIFIC:
realistic_variables:
  strings: [name, username, email, ...]  # Language-agnostic ✅
  numbers: [price, quantity, score, ...]  # Language-agnostic ✅

# Would need language variants for:
# - Naming conventions (snake_case vs camelCase vs PascalCase)
# - Standard library references
# - Idioms and patterns
```

**2. Analyzer Checks (analyzer.py):**
```python
# Lines 233-238: Python-specific
if "python 3.1" in text_lower or "python 3" in text_lower:
    score += 0.3
if "python 2" in text_lower:
    score -= 1.0

# Lines 139-143: Python jargon
jargon_terms = ["legb", "gil", "monkey patch", "mro"]
```

**3. Practical Scoring (analyzer.py):**
```python
# Lines 196-200: Python standards
industry_terms = [
    "pep 8", "python 3", "best practice", ...
]
```

#### How to Extend to Other Languages:

**Option A: Language Field (RECOMMENDED)**

```python
# 1. Add language to Question dataclass
@dataclass
class Question:
    # ... existing fields ...
    language: str = "python"  # NEW: python, javascript, java, etc.

# 2. Update config.yaml
languages:
  python:
    naming_convention: "snake_case"
    version_current: "3.10+"
    version_legacy: "2.x"
    standards: ["PEP 8"]
    jargon: ["legb", "gil", "mro"]

  javascript:
    naming_convention: "camelCase"
    version_current: "ES6+"
    version_legacy: "ES5"
    standards: ["ESLint", "Airbnb Style"]
    jargon: ["hoisting", "closure", "event loop"]

  java:
    naming_convention: "camelCase"
    version_current: "Java 17+"
    version_legacy: "Java 8"
    standards: ["Oracle Conventions"]
    jargon: ["jvm", "garbage collection", "interface"]

# 3. Update analyzer to use language config
def _score_practical_application(self, q: Question) -> float:
    lang_config = self.config['languages'].get(q.language, {})
    standards = lang_config.get('standards', [])
    current_version = lang_config.get('version_current')
    legacy_version = lang_config.get('version_legacy')

    # Check for current standards
    if any(std.lower() in text_lower for std in standards):
        score += 0.7

    # Check for legacy version (penalty)
    if legacy_version and legacy_version.lower() in text_lower:
        score -= 1.0
```

**Effort Required:** 🟡 **MEDIUM** (1-2 weeks per language)
- Add language field to dataclass
- Create language configs in YAML
- Update analyzer to use language configs
- Create language-specific templates
- Test with sample questions

**Languages Easy to Add:**
- ✅ JavaScript (similar ecosystem)
- ✅ Java (well-established standards)
- ✅ C# (clear conventions)
- ✅ Go (opinionated style)
- ✅ Rust (strong conventions)

**Languages Harder to Add:**
- ⚠️ C/C++ (multiple styles, less standardized)
- ⚠️ PHP (fragmented ecosystem)
- ⚠️ Ruby (convention-heavy but varies)

---

## 🎯 Scope Expansion Roadmap

### v2.1 - Multi-Language Support (4-6 weeks)

**Goal:** Support Python + 2 other languages

**Tasks:**
1. ✅ Add `language` field to Question dataclass
2. ✅ Create language configs (Python, JavaScript, Java)
3. ✅ Update analyzer to use language-specific patterns
4. ✅ Create language-specific templates
5. ✅ Test with 30 questions per language
6. ✅ Document language extension guide

**Benefit:** 3x addressable market (Python → Python + JS + Java)

---

### v2.5 - Content Quality Scoring (8-12 weeks)

**Goal:** Fork QuestionForge → Create "ContentForge"

**New Supported Types:**
- Tutorials (step-by-step guides)
- Explanations (conceptual articles)
- Code Examples (standalone snippets)
- Reference Docs (API documentation)

**Architecture:**
```python
# New base class
class ContentItem:
    content: str
    content_type: str
    purpose: str

# Subclasses
class Question(ContentItem):
    # Existing Question fields

class Tutorial(ContentItem):
    steps: List[str]
    learning_outcomes: List[str]

class Explanation(ContentItem):
    concept: str
    depth_level: str
```

**Adapted Criteria:**
1. ✅ Adult Learning → "Practical Context"
2. ✅ People-First → Unchanged
3. 🔄 Bloom's → "Learning Enablement" (what can learner do after?)
4. ✅ Practical → Unchanged
5. ✅ RAG → Unchanged
6. 🔄 Construct Validity → "Purpose Alignment"
7. ✅ Cognitive Depth → Unchanged

**Benefit:** Assess entire curriculum, not just questions

---

### v3.0 - Psychometric Analysis (Requires Student Data)

**Goal:** Add statistical validation

**New Capabilities:**
- Item difficulty (p-value) from student performance
- Item discrimination (point-biserial correlation)
- Reliability (Cronbach's alpha)
- Factor analysis (validate 7 criteria independence)

**Requirements:**
- ❌ Need real student response data
- ❌ Need sample size: 100+ students per question
- ❌ Need LMS integration or data pipeline

**Benefit:** NCCA-level psychometric validation

---

## 📊 Comparison Matrix

| Feature | v2.0 (Current) | v2.1 (Multi-Lang) | v2.5 (ContentForge) | v3.0 (Psychometric) |
|---------|---------------|-------------------|---------------------|---------------------|
| **Question Quality** | ✅ Python | ✅ 3+ languages | ✅ All languages | ✅ + Statistics |
| **Tutorial Quality** | ❌ | ❌ | ✅ | ✅ |
| **Code Example Quality** | ❌ | ❌ | ✅ | ✅ |
| **Docs Quality** | ❌ | ❌ | ✅ | ✅ |
| **Language Support** | Python only | Python + 2 | Any | Any |
| **Student Data** | ❌ | ❌ | ❌ | ✅ Required |
| **Standards** | Academic + Industry | Same | Same | + Psychometric |
| **Use Case** | Question banks | Question banks | Full curriculum | Certification exams |

---

## 🎯 Current Scope Summary

### ✅ QuestionForge v2.0 IS:
- **Specialized** - Question quality assessment
- **Python-focused** - But extensible to other languages (v2.1)
- **Educational** - Learning objectives and pedagogy
- **Standards-based** - Academic + Industry validation
- **Automated** - Batch processing, systematic improvement

### ❌ QuestionForge v2.0 IS NOT:
- **General content tool** - Not for tutorials, docs, articles (yet)
- **Code quality tool** - Not a linter or static analyzer
- **Answer validator** - Doesn't check correctness
- **Multi-language** - Python-only (until v2.1)
- **Statistical** - No psychometric analysis (until v3.0)

---

## 💡 Recommendations

### For Your Use Case:

**If you need:** Question quality for Python curriculum
→ ✅ **Use v2.0 NOW** - Perfect fit

**If you need:** Question quality for JS/Java curriculum
→ ⏳ **Wait for v2.1** (4-6 weeks) OR **Adapt config yourself** (2 weeks)

**If you need:** Tutorial/content quality assessment
→ ⏳ **Wait for ContentForge v2.5** (3-4 months) OR **Hire custom development**

**If you need:** Psychometric validation
→ ⏳ **Wait for v3.0** (6+ months) + **Collect student data**

### Quick Extension Guide:

**To add JavaScript support (DIY - 1 week):**
1. Add JavaScript language config to `config.yaml`
2. Update 3 checks in `analyzer.py` (lines 196-238)
3. Test with 10 sample JS questions
4. Document in README

**To assess tutorial quality (Advanced - 4 weeks):**
1. Create `Tutorial` dataclass
2. Create `TutorialAnalyzer` class
3. Adapt 5/7 criteria (drop Bloom's, adapt construct validity)
4. Create tutorial-specific transformers
5. Build separate CLI command or fork codebase

---

## 📞 Support & Custom Development

If you need:
- ✅ Multi-language support (v2.1 features early)
- ✅ Content quality assessment (ContentForge)
- ✅ Custom criteria or adaptations
- ✅ Integration with your LMS/CMS
- ✅ Psychometric consulting

**Contact:** Quest & Crossfire Arsenal

---

**Last Updated:** November 4, 2025
**Next Review:** After v2.1 release
