"""
RAG Optimizer - Optimize questions for keyword + semantic search
"""

import re
from typing import List, Set, Dict
import yaml
from .parser import Question


class RAGOptimizer:
    """Optimize questions for RAG retrieval (keyword + semantic)"""

    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.min_keywords = self.config['rag']['min_keywords']
        self.max_keywords = self.config['rag']['max_keywords']

    def optimize_keywords(self, question: Question) -> Question:
        """Enhance keyword metadata"""

        keywords = set(question.keywords) if question.keywords else set()

        # Extract from question text
        text_lower = question.question.lower()
        words = set(re.findall(r'\b\w{4,}\b', text_lower))  # Words 4+ chars

        # Remove common stop words
        stop_words = {
            'what', 'which', 'that', 'this', 'from', 'with', 'have',
            'would', 'could', 'should', 'will', 'can', 'does', 'do'
        }
        words -= stop_words

        keywords.update(words)

        # Add synonyms for common terms
        synonyms = {
            'function': ['def', 'method', 'procedure'],
            'variable': ['identifier', 'name', 'symbol'],
            'loop': ['iteration', 'repeat', 'cycle'],
            'list': ['array', 'sequence', 'collection'],
            'error': ['exception', 'bug', 'issue'],
        }

        for term, syns in synonyms.items():
            if term in keywords:
                keywords.update(syns)

        # Add Python-specific context
        if question.topic:
            keywords.add(question.topic.lower().replace(' & ', '_').replace(' ', '_'))

        if question.subtopics:
            for st in question.subtopics:
                keywords.add(st.lower().replace(' ', '_'))

        # Limit to max keywords (keep most relevant)
        if len(keywords) > self.max_keywords:
            # Prefer: topic words > code terms > general
            prioritized = []
            for kw in keywords:
                if kw in text_lower:
                    prioritized.append((kw, 2))  # In question text = high priority
                else:
                    prioritized.append((kw, 1))

            prioritized.sort(key=lambda x: x[1], reverse=True)
            keywords = set([kw for kw, pri in prioritized[:self.max_keywords]])

        question.keywords = sorted(list(keywords))

        return question

    def optimize_semantic(self, question: Question) -> Question:
        """Optimize for semantic/embedding search"""

        # Ensure question is not too short
        if len(question.question) < 50 and question.style != "single_word":
            # Already handled by transformer
            pass

        # Add related concepts if missing
        if not hasattr(question, 'related_concepts') or not question.related_concepts:
            related = self._infer_related_concepts(question)
            if related:
                # Store in duplicates_check if no better field
                if not question.duplicates_check:
                    question.duplicates_check = f"Related: {', '.join(related)}"
                else:
                    question.duplicates_check += f" | Related: {', '.join(related)}"

        return question

    def _infer_related_concepts(self, question: Question) -> List[str]:
        """Infer related concepts from question content"""

        related = []

        # Map topics to related concepts
        topic_concepts = {
            "Data Types": ["mutability", "type conversion", "type checking"],
            "Control Flow": ["loops", "conditionals", "iteration"],
            "Functions": ["parameters", "return values", "scope", "recursion"],
            "Operators": ["precedence", "arithmetic", "comparison", "logical"],
            "Errors & Exceptions": ["error handling", "try-except", "debugging"],
        }

        if question.topic in topic_concepts:
            related.extend(topic_concepts[question.topic])

        # Infer from keywords
        if question.keywords:
            for kw in question.keywords[:3]:  # Top 3 keywords
                related.append(kw)

        return list(set(related))[:5]  # Max 5 related concepts

    def add_search_metadata(self, question: Question) -> Question:
        """Add comprehensive search metadata"""

        # Ensure all search fields are populated
        if not question.keywords:
            question = self.optimize_keywords(question)

        if not question.subtopics:
            # Infer from question
            question.subtopics = self._infer_subtopics(question)

        question = self.optimize_semantic(question)

        return question

    def _infer_subtopics(self, question: Question) -> List[str]:
        """Infer subtopics from question content"""

        text_lower = question.question.lower()
        subtopics = []

        # Common subtopic patterns
        patterns = {
            "syntax": r'\b(syntax|colon|indentation|statement)\b',
            "variables": r'\b(variable|identifier|name|assign)\b',
            "functions": r'\b(function|def|return|parameter)\b',
            "loops": r'\b(loop|for|while|iteration)\b',
            "conditionals": r'\b(if|else|elif|condition)\b',
            "errors": r'\b(error|exception|bug|debug)\b',
        }

        for topic, pattern in patterns.items():
            if re.search(pattern, text_lower):
                subtopics.append(topic)

        return subtopics[:3]  # Max 3 subtopics

    def validate_rag_readiness(self, question: Question) -> Dict[str, any]:
        """Check if question is optimized for RAG"""

        issues = []
        score = 5.0

        # Keyword check
        if not question.keywords or len(question.keywords) < self.min_keywords:
            issues.append(f"Insufficient keywords ({len(question.keywords or [])} < {self.min_keywords})")
            score -= 1.5

        # Semantic check
        if len(question.question) < 30:
            issues.append(f"Question too short for good embeddings ({len(question.question)} chars)")
            score -= 1.0

        if question.style == "single_word" and len(question.question.split()) == 1:
            issues.append("Single-word question not ideal for semantic search")
            score -= 2.0

        # Metadata completeness
        if not question.subtopics:
            issues.append("Missing subtopics metadata")
            score -= 0.5

        if not question.duplicates_check:
            issues.append("Missing duplicates_check field (helps semantic differentiation)")
            score -= 0.5

        return {
            "rag_ready": score >= 4.0,
            "score": max(1.0, score),
            "issues": issues
        }
