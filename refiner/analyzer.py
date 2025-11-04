"""
Question Analyzer - Quality scoring algorithms
"Small fixes, big clarity" - Quest & Crossfire
v2.0: Enhanced with academic + industry standards
"""

import re
from typing import Dict, List, Tuple
import yaml
from pathlib import Path
from .parser import Question

# Bloom's taxonomy hierarchy for construct validity checks
BLOOM_LEVELS = ["remember", "understand", "apply", "analyze", "evaluate", "create"]


class QuestionAnalyzer:
    """Analyze and score questions against quality criteria"""

    def __init__(self, config_path: str = "config.yaml"):
        """Load configuration"""
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.weights = self.config['scoring']['weights']
        self.threshold = self.config['scoring']['threshold']

        # Load templates for analysis
        self.diverse_names = self.config['templates']['diverse_names']
        self.realistic_vars = self.config['templates']['realistic_variables']

    def analyze(self, question: Question) -> Dict[str, float]:
        """Analyze question and return scores for each criterion (v2.0 - 7 criteria)"""

        scores = {
            "adult_learning": self._score_adult_learning(question),
            "people_first": self._score_people_first(question),
            "blooms": self._score_blooms_alignment(question),
            "practical": self._score_practical_application(question),
            "rag": self._score_rag_optimization(question),
            "construct_validity": self._score_construct_validity(question),
            "cognitive_depth": self._score_cognitive_depth(question)
        }

        # Calculate weighted overall score
        overall = sum(scores[k] * self.weights[k] for k in scores.keys())
        scores["overall"] = round(overall, 2)

        return scores

    def _score_adult_learning(self, q: Question) -> float:
        """Score based on adult learning principles"""
        score = 3.0  # Base score

        text = q.question.lower()

        # Real-world context indicators
        real_world_terms = [
            "analyze", "build", "process", "manage", "track", "calculate",
            "customer", "user", "data", "file", "report", "system",
            "inventory", "sales", "revenue", "score", "student"
        ]

        if any(term in text for term in real_world_terms):
            score += 0.8

        # Problem-centered approach
        if q.style == "scenario_task":
            score += 0.5

        if "you need" in text or "you're" in text or "you have" in text:
            score += 0.4  # Contextual framing

        # Avoid abstract examples (penalty)
        abstract_vars = re.findall(r'\b([xy]|foo|bar|test)\b', text)
        if abstract_vars:
            score -= 0.5 * len(set(abstract_vars))

        # Check for practical variable names
        practical_vars = []
        for category in self.realistic_vars.values():
            practical_vars.extend(category)

        if any(var in text for var in practical_vars):
            score += 0.6

        # Code context analysis
        if q.code_context:
            # Check for realistic code
            code_lower = q.code_context.lower()
            if any(var in code_lower for var in practical_vars):
                score += 0.4
            # Penalty for x, y variables in code
            if re.search(r'\b[xy]\s*=', code_lower):
                score -= 0.3

        return max(1.0, min(5.0, score))

    def _score_people_first(self, q: Question) -> float:
        """Score based on people-first principles"""
        score = 3.5  # Base score

        text_all = f"{q.question} {q.code_context or ''} {' '.join(q.keywords)}"
        text_lower = text_all.lower()

        # Check for diverse names
        names_found = [name for name in self.diverse_names if name.lower() in text_lower]
        if names_found:
            score += 0.7

        # Western-only names (penalty)
        western_only = ["alice", "bob", "john", "jane", "mike"]
        if any(name in text_lower for name in western_only) and not names_found:
            score -= 0.4

        # Inclusive language check
        gendered_terms = ["he ", "she ", "his ", "her ", "him "]
        if any(term in text_lower for term in gendered_terms):
            score -= 0.5  # Penalty for gendered examples

        # Cognitive load appropriateness
        word_count = len(q.question.split())
        if q.difficulty == "starter":
            if word_count > 50:
                score -= 0.4  # Too complex for starter
        elif q.difficulty == "stretch":
            if word_count < 10:
                score -= 0.3  # Too simple for stretch

        # Growth mindset framing
        positive_terms = ["learn", "understand", "explore", "discover", "fix", "improve"]
        if any(term in text_lower for term in positive_terms):
            score += 0.3

        # Negative framing (penalty)
        negative_terms = ["don't you know", "obviously", "simply", "just"]
        if any(term in text_lower for term in negative_terms):
            score -= 0.6

        # Jargon without context (penalty)
        jargon_terms = ["legb", "gil", "monkey patch", "mro"]
        if any(term in text_lower for term in jargon_terms):
            # Check if there's explanation/context
            if "(" not in q.question:  # No parenthetical explanation
                score -= 0.4

        return max(1.0, min(5.0, score))

    def _score_blooms_alignment(self, q: Question) -> float:
        """Score based on Bloom's taxonomy alignment"""

        if not q.bloom_level:
            return 3.0  # Penalty for missing Bloom's level

        bloom = q.bloom_level.lower()
        difficulty = q.difficulty.lower()
        style = q.style.lower()

        # Expected alignment from config
        expected_blooms = set(self.config['blooms'].get(difficulty, []))

        # Perfect alignment
        if bloom in expected_blooms:
            score = 5.0
        else:
            score = 3.0  # Misalignment

        # Style consistency check
        style_bloom_map = {
            "single_word": "remember",
            "fill_in_blank": "remember",
            "short_question": ["remember", "understand"],
            "explain_concept": ["understand", "analyze"],
            "predict_output": "apply",
            "debug_fix": ["apply", "analyze"],
            "scenario_task": ["apply", "create"],
            "compare_contrast": ["analyze", "evaluate"],
            "rewrite": ["create"]
        }

        expected_for_style = style_bloom_map.get(style, [])
        if isinstance(expected_for_style, str):
            expected_for_style = [expected_for_style]

        if bloom not in expected_for_style:
            score -= 0.5  # Style-Bloom mismatch

        return max(1.0, min(5.0, score))

    def _score_practical_application(self, q: Question) -> float:
        """Score based on practical application and industry relevance"""
        score = 3.0  # Base score

        text_all = f"{q.question} {q.code_context or ''} {' '.join(q.keywords)}"
        text_lower = text_all.lower()

        # Industry-standard practices
        industry_terms = [
            "pep 8", "python 3", "best practice", "convention",
            "api", "json", "csv", "database", "file",
            "testing", "debug", "error", "exception"
        ]

        if any(term in text_lower for term in industry_terms):
            score += 0.7

        # Tool awareness
        tool_terms = [
            "ide", "debugger", "linter", "pip", "venv", "pytest",
            "git", "terminal", "console", "interpreter"
        ]

        if any(term in text_lower for term in tool_terms):
            score += 0.8

        # Job-relevant context
        job_terms = [
            "project", "application", "script", "program",
            "user", "client", "production", "deployment"
        ]

        if any(term in text_lower for term in job_terms):
            score += 0.5

        # Real development workflows
        workflow_terms = [
            "testing", "debugging", "refactoring", "code review",
            "documentation", "version control"
        ]

        if any(term in text_lower for term in workflow_terms):
            score += 0.6

        # Current Python version (bonus)
        if "python 3.1" in text_lower or "python 3" in text_lower:
            score += 0.3

        # Outdated practices (penalty)
        if "python 2" in text_lower:
            score -= 1.0

        return max(1.0, min(5.0, score))

    def _score_rag_optimization(self, q: Question) -> float:
        """Score based on RAG (keyword + semantic) search optimization"""
        score = 3.0  # Base score

        # Keyword search optimization
        keyword_count = len(q.keywords) if q.keywords else 0

        if keyword_count >= 7:
            score += 1.0
        elif keyword_count >= 5:
            score += 0.7
        elif keyword_count >= 3:
            score += 0.4
        else:
            score -= 0.5  # Too few keywords

        # Keyword quality (variety and specificity)
        if q.keywords:
            unique_words = set()
            for kw in q.keywords:
                unique_words.update(kw.lower().split())

            if len(unique_words) >= 10:
                score += 0.5

        # Semantic search optimization
        question_length = len(q.question)

        if q.style == "single_word":
            if len(q.question.split()) == 1:
                score -= 1.5  # Single word not good for semantic search
        else:
            if question_length >= 50:
                score += 0.6  # Good context for embeddings
            elif question_length < 20:
                score -= 0.4  # Too short

        # Natural language phrasing
        question_starters = ["what", "how", "why", "when", "which", "explain", "describe"]
        if any(q.question.lower().startswith(starter) for starter in question_starters):
            score += 0.5

        # Relationship mapping
        if q.prerequisites and len(q.prerequisites) > 0:
            score += 0.4

        if q.subtopics and len(q.subtopics) > 1:
            score += 0.3

        # Duplicates check quality
        if q.duplicates_check and len(q.duplicates_check) > 20:
            score += 0.3

        return max(1.0, min(5.0, score))

    def _score_construct_validity(self, q: Question) -> float:
        """Score construct validity - does question measure what it claims?

        Based on:
        - Wiggins & McTighe (Understanding by Design)
        - NCCA accreditation standards
        - AWS SME item writing guidelines

        Checks:
        1. Style-Bloom's alignment (from config)
        2. Single-word questions (low validity)
        3. Ambiguous phrasing
        4. Clear assessment target
        """
        score = 3.5  # Base score

        # Check style-Bloom's alignment
        if q.style and q.bloom_level:
            style_bloom_map = self.config.get('construct_validity', {}).get('style_bloom_map', {})
            expected_blooms = style_bloom_map.get(q.style, [])

            if isinstance(expected_blooms, str):
                expected_blooms = [expected_blooms]

            if q.bloom_level.lower() in [b.lower() for b in expected_blooms]:
                score += 1.0  # Perfect alignment
            else:
                score -= 0.8  # Misalignment - measuring wrong thing

        # Single-word questions have low construct validity
        if q.style == "single_word":
            word_count = len(q.question.split())
            if word_count == 1:
                score -= 1.5  # Single word cannot assess understanding
            elif word_count < 5:
                score -= 0.5  # Too short for valid assessment

        # Check for ambiguous phrasing
        text_lower = q.question.lower()
        ambiguous_terms = ["some", "sometimes", "usually", "often", "may", "might", "could"]
        ambiguous_count = sum(1 for term in ambiguous_terms if term in text_lower)
        if ambiguous_count > 2:
            score -= 0.6  # Too much ambiguity

        # Check for clear assessment target
        assessment_verbs = ["explain", "describe", "analyze", "compare", "implement",
                           "write", "debug", "fix", "predict", "identify"]
        if any(verb in text_lower for verb in assessment_verbs):
            score += 0.5  # Clear what's being assessed

        # Check for "trick question" patterns (poor construct validity)
        trick_patterns = ["except", "not true", "incorrect", "false"]
        if any(pattern in text_lower for pattern in trick_patterns):
            score -= 0.4  # Negative framing reduces validity

        # Code context strengthens construct validity
        if q.code_context and len(q.code_context) > 50:
            score += 0.4  # Clear assessment artifact

        return max(1.0, min(5.0, score))

    def _score_cognitive_depth(self, q: Question) -> float:
        """Score cognitive depth using Six Facets of Understanding

        Based on Wiggins & McTighe framework:
        1. Explanation - can explain concepts
        2. Interpretation - can make meaning
        3. Application - can use knowledge
        4. Perspective - can see viewpoints
        5. Empathy - can relate to context
        6. Self-knowledge - metacognitive awareness

        Returns: 1.0-5.0 based on facets detected
        """
        score = 2.0  # Base score (surface level)

        text_all = f"{q.question} {q.code_context or ''}".lower()

        # Load Six Facets configuration
        six_facets = self.config.get('cognitive_depth', {}).get('six_facets', {})

        facets_detected = 0
        facet_details = []

        # Check each facet
        for facet_name, facet_config in six_facets.items():
            patterns = facet_config.get('patterns', [])
            weight = facet_config.get('weight', 1.0)

            # Check if any pattern matches
            facet_found = any(pattern in text_all for pattern in patterns)

            if facet_found:
                facets_detected += weight
                facet_details.append(facet_name)

        # Score based on facet count and depth
        if facets_detected >= 3.0:
            score = 5.0  # Exceptional depth - 3+ facets
        elif facets_detected >= 2.0:
            score = 4.0  # Strong depth - 2 facets
        elif facets_detected >= 1.0:
            score = 3.0  # Moderate depth - 1 facet
        elif facets_detected >= 0.5:
            score = 2.5  # Some depth
        else:
            score = 2.0  # Surface level (factual recall)

        # Check for pure memorization (penalty)
        memorization_indicators = ["what is", "define", "list", "name", "state"]
        if any(indicator in text_all for indicator in memorization_indicators):
            # Only penalize if no other facets detected
            if facets_detected == 0:
                score = 1.5  # Rote memorization

        # Bloom's level consistency check
        if q.bloom_level:
            bloom_lower = q.bloom_level.lower()

            # Higher Bloom's should have more facets
            if bloom_lower in ["create", "evaluate"] and facets_detected < 2.0:
                score -= 0.5  # Claimed high level but shallow depth
            elif bloom_lower in ["analyze", "apply"] and facets_detected < 1.0:
                score -= 0.3  # Mid-level should have some depth

        # Scenario-based questions typically have more depth
        if q.style == "scenario_task" and facets_detected >= 2.0:
            score += 0.3  # Bonus for rich scenarios

        return max(1.0, min(5.0, score))

    def identify_issues(self, question: Question, scores: Dict[str, float]) -> List[Tuple[str, str, int]]:
        """Identify specific issues with a question
        Returns: List of (category, description, priority) tuples
        Priority: 1=critical, 2=important, 3=nice-to-have
        """
        issues = []

        # Single-word question
        if question.style == "single_word" and len(question.question.split()) == 1:
            issues.append(("style", "Single-word question needs expansion for semantic search", 1))

        # Abstract variables
        abstract_vars = re.findall(r'\b([xy]|foo|bar|test)\b', question.question.lower())
        if abstract_vars:
            issues.append(("adult_learning", f"Abstract variables ({', '.join(set(abstract_vars))}) - use realistic names", 1))

        # Missing Bloom's level
        if not question.bloom_level:
            issues.append(("blooms", "Missing Bloom's taxonomy level", 2))

        # Bloom's misalignment
        if question.bloom_level and question.difficulty:
            expected = set(self.config['blooms'].get(question.difficulty, []))
            if question.bloom_level.lower() not in expected:
                issues.append(("blooms", f"Bloom's '{question.bloom_level}' doesn't match difficulty '{question.difficulty}'", 2))

        # Insufficient keywords
        if not question.keywords or len(question.keywords) < 5:
            issues.append(("rag", f"Only {len(question.keywords or [])} keywords - need 5-7 minimum", 2))

        # Western-only names
        western_names = ["alice", "bob", "john", "jane"]
        if any(name in question.question.lower() for name in western_names):
            issues.append(("people_first", "Use globally diverse names (Priya, Chen, Amara, etc.)", 2))

        # No real-world context
        if scores["adult_learning"] < 3.5:
            issues.append(("adult_learning", "Add real-world context or practical scenario", 1))

        # Tool awareness missing
        if scores["practical"] < 3.5 and question.difficulty == "stretch":
            issues.append(("practical", "Consider mentioning development tools or workflows", 3))

        # Construct validity issues (v2.0)
        if scores["construct_validity"] < 3.5:
            # Check style-Bloom's alignment
            if question.style and question.bloom_level:
                style_bloom_map = self.config.get('construct_validity', {}).get('style_bloom_map', {})
                expected_blooms = style_bloom_map.get(question.style, [])
                if isinstance(expected_blooms, str):
                    expected_blooms = [expected_blooms]
                if question.bloom_level.lower() not in [b.lower() for b in expected_blooms]:
                    issues.append(("construct_validity",
                                  f"Style '{question.style}' doesn't align with Bloom's '{question.bloom_level}' - may measure wrong thing", 1))

            # Check for ambiguous phrasing
            ambiguous_terms = ["some", "sometimes", "usually", "often", "may", "might", "could"]
            ambiguous_count = sum(1 for term in ambiguous_terms if term in question.question.lower())
            if ambiguous_count > 2:
                issues.append(("construct_validity",
                              f"Too much ambiguous language ({ambiguous_count} terms) - reduces validity", 2))

        # Cognitive depth issues (v2.0)
        if scores["cognitive_depth"] < 3.0:
            if question.bloom_level and question.bloom_level.lower() in ["analyze", "evaluate", "create"]:
                issues.append(("cognitive_depth",
                              "High Bloom's level but shallow depth - add explanation, perspective, or application facets", 1))
            else:
                issues.append(("cognitive_depth",
                              "Surface-level question - consider adding 'why', 'how', or 'compare' elements", 2))

        return sorted(issues, key=lambda x: x[2])  # Sort by priority

    def get_improvement_suggestions(self, question: Question, scores: Dict[str, float]) -> List[str]:
        """Get actionable improvement suggestions"""
        suggestions = []

        issues = self.identify_issues(question, scores)

        for category, description, priority in issues:
            if priority == 1:
                suggestions.append(f"🔴 {description}")
            elif priority == 2:
                suggestions.append(f"🟡 {description}")
            else:
                suggestions.append(f"🟢 {description}")

        return suggestions
