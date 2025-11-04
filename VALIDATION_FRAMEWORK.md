# QuestionForge Validation Framework
## Comprehensive Quality Standards (Academic + Industry)

**Version:** 2.0 - Enhanced with Industry & Academic Benchmarks
**Date:** November 4, 2025
**Philosophy:** "Small fixes, big clarity" - Quest & Crossfire

---

## Executive Summary

This framework integrates **3 tiers of quality standards**:

1. **Academic Standards**: Carnegie Mellon, Wiggins & McTighe, ACM SIGCSE
2. **Industry Standards**: AWS, IBM, Microsoft, Google, CompTIA, NCCA accreditation
3. **Quest & Crossfire Principles**: Brand-specific excellence criteria

**Result:** 7-criteria comprehensive scoring system (up from 5) aligned with flagship educational and professional certification standards.

---

## 🎓 Academic Standards Analysis

### Carnegie Mellon University (Eberly Center)

**Source:** [CMU Teaching & Learning Principles](https://www.cmu.edu/teaching/principles/)

**Key Principles for Assessment Design:**

| Principle | Description | QuestionForge Implementation |
|-----------|-------------|------------------------------|
| **Backward Design** | Align objectives → assessment → instruction | ✅ Validate Bloom's level matches difficulty |
| **Prior Knowledge** | Build on existing understanding | ✅ Check prerequisites metadata |
| **Knowledge Organization** | Structure affects learning | ⚠️ NEW: Add cognitive structure criterion |
| **Motivation** | Engage through relevance | ✅ Real-world context scoring |
| **Mastery Development** | Skills → integration → application | ⚠️ NEW: Add progression validation |

**CMU Standards We're Missing:**
- Knowledge organization assessment
- Mastery progression validation
- Transfer task design

### Wiggins & McTighe (Understanding by Design)

**Source:** Understanding by Design Framework, 1998

**Three Stages of Backward Design:**

1. **Stage 1: Desired Results** → Define learning goals
   - ✅ We validate: Topic, Bloom's level, difficulty

2. **Stage 2: Evidence** → Determine acceptable evidence of understanding
   - ❌ **CRITICAL GAP**: We don't validate that question *actually measures* what it claims

3. **Stage 3: Learning Plan** → Design learning activities
   - N/A (not applicable to isolated question design)

**Six Facets of Understanding:**

| Facet | Definition | QuestionForge Assessment |
|-------|------------|--------------------------|
| 1. **Explanation** | Can explain concepts clearly | ⚠️ Partially - "explain_concept" style |
| 2. **Interpretation** | Can make meaning, tell stories | ❌ Not assessed |
| 3. **Application** | Can use knowledge effectively | ✅ "practical" criterion |
| 4. **Perspective** | Can see different viewpoints | ❌ Not assessed |
| 5. **Empathy** | Can relate to others' experiences | ⚠️ Partially - "people_first" |
| 6. **Self-Knowledge** | Metacognitive awareness | ❌ Not assessed |

**UbD Standards We're Missing:**
- ❌ Construct validity (does it measure what it claims?)
- ❌ Cognitive depth (Six Facets assessment)
- ❌ Essential questions framework
- ❌ Authentic assessment validation

### ACM SIGCSE (CS Education Research)

**Source:** SIGCSE Paper Review Guidelines

**Quality Standards:**

| Standard | Description | QuestionForge Implementation |
|----------|-------------|------------------------------|
| **Theory-Grounded** | Based on educational theory | ✅ Bloom's, adult learning, UDL |
| **Clear Questions** | Explicit learning objectives | ✅ Validated in metadata |
| **Replicability** | Others can reproduce | ✅ Transparent methodology |
| **Evidence-Based** | Claims supported by evidence | ❌ No empirical validation yet |
| **Proper Reporting** | Adequate detail provided | ✅ Full documentation |

**SIGCSE Standards We're Missing:**
- ❌ Empirical validation with learners
- ❌ Learning outcome correlation

---

## 🏢 Industry Standards Analysis

### AWS Certification (Amazon Web Services)

**Source:** AWS SME Item Writing Course, AWS Certification Blog

**AWS Item Writing Standards:**

| Standard | Description | Adoption in QuestionForge |
|----------|-------------|---------------------------|
| **Job Task Analysis (JTA)** | Align to real job tasks | ✅ "practical" criterion |
| **Standard Setting** | Psychometrically determined pass score | ⚠️ Our 4.8/5 is theoretical, not data-driven |
| **Beta Testing** | Field test with real candidates | ❌ Not done |
| **SME Review** | Multiple expert reviews | ⚠️ No expert review yet |
| **Psychometric Validation** | Statistical item analysis | ❌ Not implemented |
| **Distractor Quality** | Plausible but incorrect options | ⚠️ Not assessed |
| **Citation Required** | Correct answers backed by documentation | ⚠️ Not required in our schema |

**AWS Item Structure Requirements:**

1. **Stem** (scenario):
   - Business context
   - Technology used
   - Clear problem statement

2. **Responses** (4-6 options):
   - 1 correct answer with citation
   - 3-5 distractors (plausible but incorrect)
   - Each with rationale

3. **Quality Checks**:
   - No "all of the above" or "none of the above"
   - No grammatical clues to correct answer
   - Culturally neutral
   - Appropriate difficulty for target role

**AWS Standards We're Missing:**
- ❌ Distractor quality assessment
- ❌ Citation requirements
- ❌ Psychometric validation
- ❌ Field testing

### NCCA Accreditation (National Commission for Certifying Agencies)

**Source:** NCCA Standards for Accreditation of Certification Programs

**NCCA Requirements (Based on APA/AERA/NCME Standards):**

| Requirement | Description | QuestionForge Status |
|-------------|-------------|----------------------|
| **Validity Evidence** | Test measures what it claims | ❌ Not validated |
| **Reliability** | Consistent results | ❌ Not tested |
| **Job Analysis** | Linked to real-world competencies | ✅ "practical" criterion |
| **Standard Setting** | Defensible pass/fail cut score | ⚠️ 4.8/5 not empirically set |
| **Item Analysis** | Statistical quality metrics | ❌ Not implemented |
| **Blueprint Adherence** | Coverage of content domains | ✅ 18 topics validated |
| **Legal Defensibility** | Can withstand challenge | ⚠️ Uncertain without validation |

**Psychometric Standards:**

1. **Item Difficulty** (p-value): % who answer correctly
   - Target: 0.30 - 0.90 (30-90% correct)
   - Status: ❌ Not measured

2. **Item Discrimination** (point-biserial): Separates high/low performers
   - Target: ≥0.20
   - Status: ❌ Not measured

3. **Reliability** (Cronbach's alpha): Internal consistency
   - Target: ≥0.70 for low-stakes, ≥0.90 for high-stakes
   - Status: ❌ Not measured

**NCCA Standards We're Missing:**
- ❌ ALL psychometric validation
- ❌ Empirical standard setting
- ❌ Legal defensibility evidence

### CompTIA & ISO 17024

**Source:** CompTIA Exam Development Process, ISO 17024 Accreditation

**CompTIA Process:**
- 5,000+ SME hours per exam
- Psychologist/psychometrician-led development
- ISO 17024 accredited (international certification standard)

**ISO 17024 Requirements:**
- Competence defined through job/occupation analysis
- Assessment methods appropriate for competencies
- Exam developed by qualified personnel
- Security and confidentiality maintained
- Regular review and updates

**Standards We're Missing:**
- ❌ SME hour investment tracking
- ❌ Psychometrician review
- ❌ ISO compliance

### IBM, Microsoft, Google Cloud

**Common Industry Standards:**

| Standard | IBM | Microsoft | Google | QuestionForge |
|----------|-----|-----------|--------|---------------|
| **Rigorous Development** | ✅ | ✅ | ✅ | ⚠️ Partially |
| **SME Review** | ✅ | ✅ | ✅ | ❌ Not yet |
| **Regular Updates** | ✅ Quarterly | ✅ Ongoing | ✅ Regular | ⚠️ Versioned |
| **Practical Focus** | ✅ Job-based | ✅ Role-based | ✅ Role-based | ✅ Yes |
| **Stackable Credentials** | ✅ | ✅ | ✅ | ⚠️ Could add |

### ISO 29990 (Learning Services Quality)

**Key Principles:**
- Focus on learner and learning outcomes
- Design based on actual learning needs
- Evaluation of learning results
- Quality management system

**Alignment:** ✅ Strong - Adult learning focus, outcome-oriented

### ADDIE/SAM (Corporate Training Models)

**ADDIE Evaluation Phase:**
- **Formative**: Ongoing feedback during development
- **Summative**: End assessment of effectiveness
- **Kirkpatrick's 4 Levels**:
  1. Reaction (satisfaction)
  2. Learning (knowledge gain)
  3. Behavior (skill transfer)
  4. Results (business impact)

**QuestionForge Alignment:**
- ✅ Formative: Our scoring = ongoing quality check
- ❌ Summative: No learning outcome validation
- ❌ Kirkpatrick Levels: Not measured

---

## 📊 Comprehensive Standards Comparison Matrix

### Current vs. Required Standards

| Standard Category | Sub-Standard | Academic | Industry | Quest & Crossfire | Current Status | Priority |
|-------------------|--------------|----------|----------|-------------------|----------------|----------|
| **Content Validity** | Alignment to objectives | ✅ Required | ✅ Required | ✅ Required | ✅ Implemented | — |
| **Content Validity** | Blueprint coverage | ✅ Required | ✅ Required | — | ✅ Implemented | — |
| **Construct Validity** | Measures what claims | ✅ **CRITICAL** | ✅ **CRITICAL** | ✅ Required | ❌ **MISSING** | 🔴 **HIGH** |
| **Cognitive Depth** | Six Facets | ✅ Required | — | ✅ Required | ❌ **MISSING** | 🔴 **HIGH** |
| **Practical Application** | Job relevance | ✅ Required | ✅ **CRITICAL** | ✅ Required | ✅ Implemented | — |
| **Inclusive Design** | UDL/People-first | ✅ Required | ⚠️ Emerging | ✅ **CRITICAL** | ✅ Implemented | — |
| **Adult Learning** | Andragogy principles | ✅ Required | ✅ Required | ✅ Required | ✅ Implemented | — |
| **RAG Optimization** | Search readiness | — | ⚠️ Nice-to-have | ✅ Required | ✅ Implemented | — |
| **Psychometric Quality** | Item statistics | — | ✅ **CRITICAL** | — | ❌ **MISSING** | 🟡 **MEDIUM** |
| **Distractor Quality** | Multiple choice | ⚠️ Recommended | ✅ Required | — | ❌ **MISSING** | 🟢 **LOW** |
| **Empirical Validation** | Learning outcomes | ✅ **CRITICAL** | ✅ Required | ✅ Required | ❌ **MISSING** | 🟡 **MEDIUM** |
| **Expert Review** | SME validation | ✅ Required | ✅ **CRITICAL** | ✅ Required | ❌ **MISSING** | 🔴 **HIGH** |
| **Standard Setting** | Pass score | — | ✅ **CRITICAL** | — | ⚠️ Theoretical | 🟡 **MEDIUM** |

### Priority Legend:
- 🔴 **HIGH**: Implement immediately (v2.0)
- 🟡 **MEDIUM**: Implement soon (v2.1)
- 🟢 **LOW**: Future enhancement (v3.0)

---

## 🎯 QuestionForge v2.0: Enhanced Scoring Framework

### Proposed 7-Criteria System

| # | Criterion | Weight | Old | New | Source |
|---|-----------|--------|-----|-----|--------|
| 1 | **Adult Learning** | 20% | ✅ 25% | ⬇️ 20% | CMU, ADDIE |
| 2 | **People-First** | 15% | ✅ 20% | ⬇️ 15% | UDL, Quest & Crossfire |
| 3 | **Bloom's Alignment** | 15% | ✅ 20% | ⬇️ 15% | Anderson & Krathwohl |
| 4 | **Practical Application** | 15% | ✅ 20% | ⬇️ 15% | AWS, IBM, ISO 17024 |
| 5 | **RAG Optimization** | 10% | ✅ 15% | ⬇️ 10% | Quest & Crossfire |
| 6 | **Construct Validity** | 15% | ❌ NEW | ✅ 15% | **Wiggins & McTighe, NCCA** |
| 7 | **Cognitive Depth** | 10% | ❌ NEW | ✅ 10% | **Wiggins & McTighe Six Facets** |
| | **TOTAL** | **100%** | 100% | 100% | |

### New Criterion 6: Construct Validity (15% weight)

**Definition:** Does the question actually measure what it claims to measure?

**Scoring Rubric:**

**5.0 - Excellent Construct Validity:**
- Question style perfectly matches Bloom's level
- Cannot answer correctly without target understanding
- No shortcuts or alternative solution paths
- Clear, unambiguous correct answer
- Distractors (if any) are diagnostic

**4.0 - Good Construct Validity:**
- Question style mostly matches Bloom's level
- Requires target understanding to answer
- Minimal alternative solution paths
- Correct answer is clear

**3.0 - Adequate Construct Validity:**
- Question style somewhat matches Bloom's level
- Could potentially guess without full understanding
- Some ambiguity in correct answer

**2.0 - Poor Construct Validity:**
- Question style doesn't match Bloom's level
- Can answer correctly without target understanding
- Significant ambiguity or multiple interpretations

**1.0 - Invalid:**
- Measures something completely different than claimed
- Trick question or gotcha
- Impossible to answer correctly

**Validation Checks:**

1. **Style-Bloom's Alignment:**
   ```python
   style_bloom_map = {
       "single_word": ["remember"],
       "short_question": ["remember", "understand"],
       "predict_output": ["apply"],
       "debug_fix": ["apply", "analyze"],
       "scenario_task": ["apply", "create"],
       "explain_concept": ["understand"],
       "compare_contrast": ["analyze"],
       "fill_in_blank": ["remember", "apply"],
       "rewrite": ["evaluate", "create"]
   }
   ```

2. **Answer Path Analysis:**
   - Single clear path = 5.0
   - Multiple paths converge = 4.0
   - Alternative shortcuts exist = 3.0
   - Can guess without understanding = 2.0

3. **Distractor Quality (for multiple choice):**
   - All plausible, reveal misconceptions = +1.0
   - Some plausible = +0.5
   - Obviously wrong = -1.0

### New Criterion 7: Cognitive Depth (10% weight)

**Definition:** How many of Wiggins & McTighe's Six Facets of Understanding does the question assess?

**Six Facets:**

1. **Explanation** - Can explain concepts, principles, processes
2. **Interpretation** - Can make meaning, tell stories, translate
3. **Application** - Can use knowledge effectively in new situations
4. **Perspective** - Can see different viewpoints, consider alternatives
5. **Empathy** - Can relate to others' experiences, see sensitively
6. **Self-Knowledge** - Metacognitive awareness, know what you don't know

**Scoring Rubric:**

**5.0 - Exceptional Depth (3+ Facets):**
- Assesses 3 or more facets simultaneously
- Example: Scenario requiring explanation + application + perspective

**4.0 - Strong Depth (2 Facets):**
- Assesses 2 facets clearly
- Example: Compare/contrast requiring interpretation + perspective

**3.0 - Moderate Depth (1 Facet):**
- Assesses 1 facet clearly
- Most questions will score here

**2.0 - Surface Level:**
- Primarily factual recall
- Minimal cognitive engagement

**1.0 - Rote Memorization:**
- Pure fact regurgitation
- No understanding required

**Facet Detection:**

```python
facet_patterns = {
    "explanation": ["explain", "why does", "how does", "what causes"],
    "interpretation": ["what does it mean", "interpret", "significance"],
    "application": ["use", "apply", "solve", "implement", "build"],
    "perspective": ["compare", "contrast", "alternative", "tradeoff"],
    "empathy": ["impact on", "user experience", "accessibility"],
    "self_knowledge": ["debug", "reflect", "assess your understanding"]
}
```

---

## 🔬 Expert Review Rubric

### Academic Expert Review (Educators)

**Reviewer Qualifications:**
- PhD or Master's in CS Education or related field
- 5+ years teaching experience
- Published in CS education venues (SIGCSE, ICER, etc.)

**Review Criteria:**

| Criterion | Rating (1-5) | Evidence Required |
|-----------|--------------|-------------------|
| **Pedagogical Soundness** | ___ | Aligns with educational theory |
| **Learning Objective Clarity** | ___ | Clear what students should demonstrate |
| **Bloom's Accuracy** | ___ | Cognitive level correctly identified |
| **Prerequisite Logic** | ___ | Prerequisites are necessary and sufficient |
| **Cognitive Load** | ___ | Appropriate complexity for target level |
| **Inclusive Language** | ___ | Accessible to diverse learners |
| **Real-World Relevance** | ___ | Connects to authentic practice |

**Overall Academic Quality:** ___/5.0

### Industry Expert Review (Practitioners)

**Reviewer Qualifications:**
- 5+ years professional Python development
- Industry certification (AWS, Microsoft, etc.) preferred
- Experience hiring/mentoring junior developers

**Review Criteria:**

| Criterion | Rating (1-5) | Evidence Required |
|-----------|--------------|-------------------|
| **Job Relevance** | ___ | Skills tested are used in actual jobs |
| **Industry Standards** | ___ | Follows best practices (PEP 8, etc.) |
| **Practical Applicability** | ___ | Not just academic, but work-ready |
| **Tool/Framework Awareness** | ___ | References real tools (pytest, git, etc.) |
| **Common Pitfalls** | ___ | Addresses mistakes professionals make |
| **Interview Readiness** | ___ | Question style prepares for tech interviews |
| **Current Technology** | ___ | Uses modern Python (3.10+, not legacy) |

**Overall Industry Quality:** ___/5.0

### Combined Expert Score

```
Expert Score = (Academic Quality × 0.5) + (Industry Quality × 0.5)
```

**Calibration with QuestionForge:**
- Expert Score ≥4.8 AND QuestionForge ≥4.8 = ✅ **Production Ready**
- Expert Score ≥4.8 BUT QuestionForge <4.8 = ⚠️ **False Negative** (our tool too strict)
- Expert Score <4.8 BUT QuestionForge ≥4.8 = ⚠️ **False Positive** (our tool too lenient)
- Expert Score <4.8 AND QuestionForge <4.8 = ✅ **Correctly Identified** (needs work)

**Inter-Rater Reliability:**
- Minimum 2 academic + 2 industry reviewers per sample
- Calculate Fleiss' Kappa (target: ≥0.60 "substantial agreement")

---

## 📋 Validation Study Design (Future)

### Phase 1: Expert Review (Immediate)

**Sample Size:** 30 questions (10 each: starter/core/stretch)

**Process:**
1. Select representative sample from question bank
2. Recruit 4 expert reviewers (2 academic, 2 industry)
3. Blind review (reviewers don't see QuestionForge scores)
4. Compare expert scores with QuestionForge scores
5. Calculate correlation, identify discrepancies
6. Refine scoring algorithms

**Timeline:** 2-4 weeks

**Cost:** $1,000-2,000 (expert honoraria)

### Phase 2: Pilot Testing (Near-Term)

**Sample Size:** 100 questions with 30 students

**Process:**
1. Administer original questions (pre-refinement) to Group A
2. Administer refined questions to Group B
3. Measure:
   - Comprehension (can they answer follow-up questions?)
   - Time to mastery (how long to get it right?)
   - Retention (remember 1 week later?)
   - Transfer (apply to novel situation?)
4. Correlate student performance with QuestionForge scores

**Hypothesis:** Questions with higher QuestionForge scores → better learning outcomes

**Timeline:** 2-3 months (requires IRB approval)

**Cost:** $5,000-10,000 (participant compensation, data analysis)

### Phase 3: Full Validation (Long-Term)

**Sample Size:** 500+ questions, 200+ students

**Process:**
1. Full deployment in Aethelgard platform
2. Track learning analytics:
   - Question attempts
   - Time spent
   - Success rates
   - Prerequisite pathway effectiveness
3. A/B test: Refined vs. Original questions
4. Measure business outcomes:
   - Course completion rates
   - Certification pass rates
   - Time to job readiness

**Timeline:** 6-12 months post-launch

**Cost:** Integrated into platform operations

**Publication:** Submit to ACM SIGCSE or similar venue

---

## 🎯 Immediate Action Items

### For QuestionForge v2.0 (This Week):

1. ✅ **Add Construct Validity Criterion** (4-6 hours)
   - Implement style-Bloom's validation
   - Add answer path analysis
   - Update scoring weights

2. ✅ **Add Cognitive Depth Criterion** (3-4 hours)
   - Implement Six Facets detection
   - Update scoring weights
   - Add facet metadata to output

3. ✅ **Update Configuration** (1 hour)
   - Revise config.yaml with new criteria
   - Document standard sources
   - Add validation flags

4. ✅ **Create Expert Review Template** (2 hours)
   - Design review forms (academic + industry)
   - Create scoring rubric
   - Provide example reviews

5. ✅ **Documentation Update** (2 hours)
   - Update README with validation framework
   - Add standards comparison section
   - Document expert review process

**Total Effort:** 12-15 hours (1.5-2 workdays)

### For Validation (Next 2-4 Weeks):

6. **Recruit Expert Reviewers**
   - 2 academic (CS educators)
   - 2 industry (senior developers)
   - Provide honoraria ($250-500 each)

7. **Conduct Expert Review**
   - Blind review of 30 sample questions
   - Compare with QuestionForge scores
   - Analyze discrepancies

8. **Calibrate Tool**
   - Adjust weights if needed
   - Refine scoring algorithms
   - Validate 4.8/5 threshold

---

## 📖 References & Standards Documents

### Academic Sources:

1. **Wiggins, G., & McTighe, J. (1998).** *Understanding by Design.* Alexandria, VA: ASCD.
2. **Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001).** *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives.* New York: Longman.
3. **Carnegie Mellon University Eberly Center.** *Teaching & Learning Principles.* Retrieved from https://www.cmu.edu/teaching/principles/
4. **ACM SIGCSE.** *Paper Review Guidelines.* Retrieved from https://sigcse2024.sigcse.org/track/sigcse-ts-2024-Papers-1

### Industry Sources:

5. **AWS.** *AWS Certification Subject Matter Expert (SME) Item Writing Course.* Retrieved from https://aws.amazon.com/training
6. **NCCA (National Commission for Certifying Agencies).** *Standards for the Accreditation of Certification Programs.* Retrieved from https://www.credentialingexcellence.org/
7. **CompTIA.** *Exam Development Process.* Retrieved from https://www.comptia.org/en-us/resources/test-policies/exam-development/
8. **ISO 17024:2012.** *Conformity assessment — General requirements for bodies operating certification of persons.*
9. **ISO 29990:2010.** *Learning services for non-formal education and training — Basic requirements for service providers.*

### Psychometric Standards:

10. **American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014).** *Standards for educational and psychological testing.* Washington, DC: American Educational Research Association.

---

## 🏆 Target: Flagship Quality

**Current QuestionForge v1.0:**
- 5-criteria scoring
- Academic theory-based
- Quest & Crossfire aligned
- **Status:** Good foundation, needs validation

**Enhanced QuestionForge v2.0:**
- 7-criteria scoring
- Academic + Industry standards
- Expert review validated
- **Status:** Comprehensive, production-ready

**Validated QuestionForge v3.0 (Future):**
- Empirically validated with learners
- Psychometrically sound
- ACM SIGCSE published
- **Status:** Research-grade, gold standard

---

**"Small fixes, big clarity - Now with academic rigor AND industry standards."** 🔥

