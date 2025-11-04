# QuestionForge - Product Roadmap

**Last Updated:** November 4, 2025
**Current Version:** 2.0 (Production)

---

## 🎯 Vision

Transform educational content quality through systematic, standards-based assessment and refinement.

**Core Philosophy:** "Small fixes, big clarity" - Quest & Crossfire

---

## ✅ v2.0 - Academic + Industry Standards (COMPLETE)

**Release Date:** November 4, 2025
**Status:** ✅ Production Ready

### Delivered Features:
- ✅ 7-criteria scoring system
- ✅ Construct validity assessment (Wiggins & McTighe)
- ✅ Cognitive depth assessment (Six Facets of Understanding)
- ✅ Academic standards validation (CMU, UbD, Bloom's, SIGCSE)
- ✅ Industry standards validation (AWS, NCCA, ISO 17024/29990)
- ✅ Expert review infrastructure (comprehensive rubric)
- ✅ Python question quality assessment
- ✅ Batch processing and refinement
- ✅ Rich terminal UI with reports (text, HTML, JSON)

### Scope:
- **Content Type:** Educational questions only
- **Language:** Python programming
- **Use Case:** Question bank quality improvement

**Documentation:** README.md, VALIDATION_FRAMEWORK.md, EXPERT_REVIEW_RUBRIC.md, TEST_RESULTS_V2.md

---

## 📋 v2.1 - Multi-Language Support (PLANNED)

**Estimated Timeline:** 4-6 weeks
**Priority:** 🟡 Medium
**Status:** 📋 Scoped, awaiting decision

### Goals:
Enable QuestionForge to assess questions for multiple programming languages beyond Python.

### Features:
- [ ] Language field in Question dataclass
- [ ] Language-specific configuration system
- [ ] Support for JavaScript (ES6+, ESLint, Airbnb Style)
- [ ] Support for Java (Java 17+, Oracle Conventions)
- [ ] Language-specific templates and patterns
- [ ] Language-specific jargon and best practices
- [ ] Naming convention validation (snake_case, camelCase, PascalCase)
- [ ] Version currency checks per language
- [ ] Language extension guide for adding new languages

### Architecture Changes:
```yaml
# config.yaml expansion
languages:
  python:
    naming_convention: "snake_case"
    version_current: "3.10+"
    standards: ["PEP 8"]
    jargon: ["legb", "gil", "mro"]

  javascript:
    naming_convention: "camelCase"
    version_current: "ES6+"
    standards: ["ESLint", "Airbnb Style"]
    jargon: ["hoisting", "closure", "event loop"]

  java:
    naming_convention: "camelCase"
    version_current: "Java 17+"
    standards: ["Oracle Conventions"]
    jargon: ["jvm", "garbage collection"]
```

### Deliverables:
- Python + 2 languages (JavaScript, Java)
- Language extension developer guide
- 30 test questions per language
- Updated documentation

### Benefits:
- 3x addressable market (Python → Python + JS + Java)
- Reusable framework for any programming language
- Community contributions possible (language configs)

### Effort Estimate:
- Initial framework: 1 week
- JavaScript support: 1 week
- Java support: 1 week
- Testing & documentation: 1 week
- **Total:** 4 weeks

---

## 🚀 v2.5 - ContentForge (Concept Phase)

**Estimated Timeline:** 8-12 weeks
**Priority:** 🔴 Low (Future exploration)
**Status:** 💡 Concept, needs validation

### Vision:
Extend QuestionForge principles to assess general educational content quality, not just questions.

### Proposed Scope Expansion:

**New Content Types:**
1. **Tutorials** - Step-by-step guides
2. **Explanations** - Conceptual articles
3. **Code Examples** - Standalone snippets
4. **Reference Documentation** - API docs, quick reference
5. **Exercises** - Practice problems without formal assessment

### Architecture Concept:
```python
# New base class
@dataclass
class ContentItem:
    content: str
    content_type: str  # question, tutorial, explanation, example, reference
    purpose: str
    target_audience: str  # beginner, intermediate, advanced
    keywords: List[str]
    prerequisites: List[str]

# Existing Question becomes subclass
@dataclass
class Question(ContentItem):
    # Question-specific fields
    bloom_level: str
    style: str

@dataclass
class Tutorial(ContentItem):
    # Tutorial-specific fields
    steps: List[str]
    learning_outcomes: List[str]
    time_estimate_minutes: int

@dataclass
class Explanation(ContentItem):
    # Explanation-specific fields
    concept: str
    depth_level: str  # surface, moderate, deep
    analogies: List[str]
```

### Adapted Scoring Criteria:

| Original (Questions) | Adapted (General Content) | Applicability |
|---------------------|---------------------------|---------------|
| Adult Learning | Practical Context | 90% |
| People-First | Inclusive Language | 100% |
| Bloom's Alignment | Learning Enablement | 60% (redesign) |
| Practical Application | Industry Relevance | 80% |
| RAG Optimization | Search Optimization | 100% |
| Construct Validity | Purpose Alignment | 40% (redesign) |
| Cognitive Depth | Conceptual Depth | 70% |

### Key Questions to Answer:
- ❓ What does "4.8/5 quality" mean for a tutorial vs. a question?
- ❓ How do we measure "construct validity" for explanatory content?
- ❓ What transformation strategies apply to tutorials?
- ❓ Should this be a fork (ContentForge) or extension (QuestionForge v3)?

### Deliverables (if pursued):
- [ ] Content type ontology
- [ ] Adapted scoring criteria
- [ ] Content-specific transformers
- [ ] Separate CLI or unified interface
- [ ] 100+ content samples for validation
- [ ] Expert review for new content types

### Benefits:
- Assess entire curriculum, not just questions
- Quality gate for all educational materials
- Unified quality framework

### Risks:
- Scope creep (trying to do too much)
- Loss of focus (questions are core strength)
- Diluted quality standards (different content needs different criteria)

### Decision Factors:
- ✅ Pursue if: Strong demand for tutorial/content assessment
- ❌ Skip if: Question assessment is sufficient for market
- 🔄 Revisit: After v2.1 ships and user feedback collected

### Effort Estimate:
- Requirements & design: 2 weeks
- Architecture refactor: 2 weeks
- Tutorial scorer: 2 weeks
- Explanation scorer: 2 weeks
- Testing & validation: 2 weeks
- Documentation: 1 week
- **Total:** 11 weeks

---

## 📊 v3.0 - Psychometric Validation (Long-term)

**Estimated Timeline:** 6-12 months
**Priority:** ⏳ Long-term
**Status:** 📋 Planned, requires prerequisites

### Prerequisites:
- ❌ Real student response data (100+ students per question)
- ❌ LMS integration or data pipeline
- ❌ Statistical expertise (psychometrician consultant)
- ❌ Institutional partnership (school/university)

### Goals:
Add empirical, statistical validation to complement expert validation.

### Features:
- [ ] Item difficulty calculation (p-value)
- [ ] Item discrimination analysis (point-biserial correlation)
- [ ] Reliability analysis (Cronbach's alpha)
- [ ] Factor analysis (validate 7 criteria independence)
- [ ] Differential item functioning (DIF) analysis
- [ ] Standard error of measurement (SEM)
- [ ] Test information curves
- [ ] Automated flagging of problematic items

### Standards Compliance:
- NCCA full accreditation requirements
- APA/AERA/NCME Standards for Educational and Psychological Testing
- ISO/IEC 17024 complete compliance

### Deliverables:
- [ ] Student data ingestion pipeline
- [ ] Psychometric analysis module
- [ ] Statistical validation reports
- [ ] Item quality dashboard with statistical metrics
- [ ] Legal defensibility documentation
- [ ] Published validation study

### Benefits:
- NCCA-level certification readiness
- Legally defensible assessment quality
- Empirical validation of 4.8/5 threshold
- Continuous quality improvement with data

### Effort Estimate:
- Data pipeline: 4 weeks
- Psychometric module: 8 weeks
- Validation study design: 4 weeks
- Data collection: 12-24 weeks (external dependency)
- Analysis & reporting: 4 weeks
- Publication: 8-12 weeks
- **Total:** 6-12 months

---

## 🔬 Research & Validation Track (Parallel)

**Ongoing Activities:**

### Phase 1: Expert Review Validation (Next 2-3 weeks)
- [ ] Recruit 4 expert reviewers (2 academic, 2 industry)
- [ ] Distribute 30-question sample + rubric
- [ ] Collect expert ratings
- [ ] Calculate inter-rater reliability (Fleiss' Kappa)
- [ ] Compute correlation with QuestionForge scores
- [ ] Calibrate weights if needed
- [ ] Publish validation report

**Success Criteria:** Correlation ≥0.7 with expert consensus

### Phase 2: A/B Testing (Month 2-3)
- [ ] Partner with educational institution
- [ ] Test refined vs. unrefined questions with students
- [ ] Measure: completion time, error rates, satisfaction
- [ ] Analyze: Do refined questions perform better?

**Success Criteria:** Statistically significant improvement in 2+ metrics

### Phase 3: Case Study Publication (Month 3-6)
- [ ] Write up validation study
- [ ] Submit to SIGCSE or ICER
- [ ] Present at conference
- [ ] Publish as open-source case study

**Success Criteria:** Peer-reviewed publication or accepted conference paper

---

## 🛠️ Technical Debt & Maintenance

### v2.x Maintenance (Ongoing)
- [ ] Bug fixes as reported
- [ ] Dependency updates (quarterly)
- [ ] Security patches (as needed)
- [ ] Performance optimizations (if bottlenecks found)
- [ ] Windows/Mac/Linux compatibility testing

### Code Quality Improvements
- [ ] Add unit tests (pytest suite)
- [ ] Add integration test suite
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Code coverage ≥80%
- [ ] Type hints throughout (mypy validation)
- [ ] Linting (ruff or pylint)

### Documentation Improvements
- [ ] Video tutorial (YouTube)
- [ ] API documentation (if library mode added)
- [ ] Cookbook with common recipes
- [ ] Troubleshooting guide
- [ ] FAQ section

---

## 🌟 Feature Requests Backlog

### High Priority (v2.x)
- [ ] Interactive refinement mode (approve/reject suggestions)
- [ ] Bulk refinement with confidence thresholds
- [ ] Question similarity detection (find duplicates)
- [ ] Prerequisite graph visualization
- [ ] Web UI (optional, for non-technical users)

### Medium Priority (v3.x)
- [ ] LMS integration (Canvas, Moodle, Blackboard)
- [ ] Git integration (track question changes)
- [ ] Collaborative review mode (multiple reviewers)
- [ ] Question versioning and rollback
- [ ] Export to QTI format (IMS Question & Test Interoperability)

### Low Priority (Future)
- [ ] Browser extension (assess questions on any page)
- [ ] API service (cloud-hosted)
- [ ] Mobile app for reviewers
- [ ] Machine learning suggestions (GPT-based improvements)
- [ ] Automated answer generation

---

## 📈 Success Metrics

### v2.0 Success (Current)
- ✅ All 7 criteria implemented
- ✅ All tests passing
- ✅ Documentation complete
- ⏳ Expert validation pending

### v2.1 Success (Multi-Language)
- [ ] 3+ languages supported
- [ ] 100+ questions analyzed across languages
- [ ] Community contributions (1+ language added by external dev)

### v2.5 Success (ContentForge)
- [ ] 4+ content types supported
- [ ] 500+ content items assessed
- [ ] Validation study published

### v3.0 Success (Psychometric)
- [ ] 1000+ student responses collected
- [ ] Statistical validation published
- [ ] NCCA compliance documented

---

## 🎯 Decision Framework

### When to Pursue v2.1 (Multi-Language):
- ✅ If: 3+ requests for non-Python languages
- ✅ If: Market research shows demand
- ✅ If: Resources available (4-6 weeks dev time)

### When to Pursue v2.5 (ContentForge):
- ✅ If: 10+ requests for tutorial/content assessment
- ✅ If: Questions are proven successful
- ✅ If: Clear differentiation from existing tools
- ❌ If: Would dilute focus on questions

### When to Pursue v3.0 (Psychometric):
- ✅ If: Institutional partner committed
- ✅ If: Student data pipeline established
- ✅ If: Psychometrician consultant engaged
- ❌ If: No access to real student data

---

## 💡 Innovation Ideas (Blue Sky)

### AI-Powered Enhancements
- GPT-based question generation from learning objectives
- Automatic distractor generation (multiple choice)
- Natural language refinement suggestions
- Semantic similarity search (find related questions)

### Gamification
- Question quality leaderboard
- Badges for refinement milestones
- Team challenges (who can refine most questions)

### Social Features
- Public question bank marketplace
- Peer review system
- Quality seal/certification for question banks
- Community voting on best questions

---

## 📅 Timeline Overview

```
2025 Q4 (Current):
├── Nov 4: v2.0 Release ✅
├── Nov-Dec: Expert validation study
└── Dec: v2.0.1 bug fixes

2026 Q1:
├── Jan: Validation study results
├── Feb: Decision point - v2.1 vs v2.5
└── Mar: Begin v2.1 or v2.5 development

2026 Q2-Q3:
├── v2.1 or v2.5 development
└── Public beta testing

2026 Q4:
├── v2.1/v2.5 release
└── Plan v3.0 with institutional partners

2027+:
└── v3.0 psychometric validation (if prerequisites met)
```

---

## 🤝 Contribution Opportunities

### For Community Contributors:
- Add new programming language configs
- Translate documentation
- Create question bank samples
- Report bugs and issues
- Suggest improvements

### For Researchers:
- Validate scoring criteria
- Conduct A/B testing studies
- Publish case studies
- Contribute to psychometric module

### For Institutions:
- Pilot testing with question banks
- Provide student data (anonymized)
- Co-author validation studies
- Sponsor feature development

---

## 📞 Roadmap Governance

**Owner:** Quest & Crossfire Arsenal
**Review Cycle:** Quarterly
**Input Sources:**
- User feedback
- Market research
- Academic partnerships
- Technical feasibility

**Priority System:**
- 🔴 Low - Nice to have, no timeline
- 🟡 Medium - Valuable, pending resources
- 🟢 High - Critical, actively planned
- ⏳ Long-term - Multi-year horizon

---

**Last Updated:** November 4, 2025
**Next Review:** February 2026 (after expert validation)
**Feedback:** Open an issue or contact Quest & Crossfire
