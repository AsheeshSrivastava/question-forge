"""
Question Transformer - Apply refinement strategies
"Small fixes, big clarity" - Quest & Crossfire
"""

import re
import random
from typing import Dict, List, Tuple, Optional
import yaml
from .parser import Question
from .analyzer import QuestionAnalyzer


class QuestionTransformer:
    """Transform questions to improve quality"""

    def __init__(self, config_path: str = "config.yaml"):
        """Load configuration"""
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.analyzer = QuestionAnalyzer(config_path)
        self.diverse_names = self.config['templates']['diverse_names']
        self.realistic_vars = self.config['templates']['realistic_variables']
        self.contexts = self.config['templates']['real_world_contexts']

    def transform(self, question: Question, auto: bool = False) -> Tuple[Question, str, float]:
        """
        Transform a question to improve quality
        Returns: (transformed_question, strategy_used, score_improvement)
        """

        # Get current scores
        current_scores = self.analyzer.analyze(question)
        current_overall = current_scores["overall"]

        # Identify issues by priority
        issues = self.analyzer.identify_issues(question, current_scores)

        if not issues:
            return question, "no_changes_needed", 0.0

        # Apply highest priority transformation
        category, description, priority = issues[0]

        transformed = Question(**question.to_dict())  # Deep copy
        strategy = "unknown"

        if category == "style" and "single-word" in description.lower():
            transformed, strategy = self._expand_single_word(transformed)

        elif category == "adult_learning" and "abstract" in description.lower():
            transformed, strategy = self._replace_abstract_variables(transformed)

        elif category == "adult_learning" and "real-world" in description.lower():
            transformed, strategy = self._add_real_world_context(transformed)

        elif category == "people_first" and "diverse names" in description.lower():
            transformed, strategy = self._diversify_names(transformed)

        elif category == "blooms":
            transformed, strategy = self._fix_blooms_alignment(transformed)

        elif category == "rag" and "keywords" in description.lower():
            transformed, strategy = self._enhance_keywords(transformed)

        elif category == "practical":
            transformed, strategy = self._add_practical_context(transformed)

        else:
            # Generic enhancement
            transformed, strategy = self._generic_enhancement(transformed)

        # Calculate score improvement
        new_scores = self.analyzer.analyze(transformed)
        new_overall = new_scores["overall"]
        improvement = round(new_overall - current_overall, 2)

        # Update refinement metadata
        transformed.update_from_refinement(
            refined_question=transformed.question,
            strategy=strategy,
            score_improvement=improvement
        )
        transformed.quality_scores = new_scores

        return transformed, strategy, improvement

    def _expand_single_word(self, q: Question) -> Tuple[Question, str]:
        """Expand single-word questions to full questions"""

        word = q.question.strip().lower()

        # Common single-word expansions
        expansions = {
            "indentation": "In Python, what syntactic feature determines code block structure, replacing curly braces used in languages like Java?",
            "scope": "What term describes the region of a program where a variable is accessible?",
            "break": "What keyword is used to exit a loop early in Python?",
            "continue": "Which keyword skips the current iteration of a loop and proceeds to the next one?",
            "return": "What keyword is used to send a value back from a function to its caller?",
            "lambda": "What keyword creates anonymous functions in Python?",
            "yield": "Which keyword is used in generator functions to produce values one at a time?",
            "import": "What keyword is used to include external modules or packages in a Python script?",
            "with": "Which keyword is used to manage context (like file handling) with automatic cleanup?",
            "class": "What keyword is used to define a new object type in Python?",
            "recursion": "What programming technique involves a function calling itself to solve a problem?",
            "iterator": "What object in Python implements the __iter__() and __next__() methods for sequential access?",
            "keyword": "What term describes reserved words in Python that have special meaning and cannot be used as identifiers?",
            "symbol": "What character is used to write single-line comments in Python?",
            "none": "What is the value in Python that represents the absence of a value or null?",
        }

        if word in expansions:
            q.question = expansions[word]
        else:
            # Generic expansion
            q.question = f"What is the purpose or meaning of '{q.question}' in Python?"

        # Update style
        q.style = "short_question"

        return q, "expand_single_word"

    def _replace_abstract_variables(self, q: Question) -> Tuple[Question, str]:
        """Replace abstract variables (x, y, foo, bar) with realistic names"""

        text = q.question

        # Map abstract to realistic based on context
        replacements = {
            'x': 'price',
            'y': 'quantity',
            'foo': 'calculate_total',
            'bar': 'get_discount',
            'num': 'score',
            'test': 'validate_email',
        }

        # Smarter replacement based on context
        if 'swap' in text.lower():
            replacements = {'x': 'current_price', 'y': 'new_price'}
        elif 'list' in text.lower() or 'number' in text.lower():
            replacements = {'x': 'scores', 'y': 'grades'}
        elif 'variable' in text.lower():
            replacements = {'x': 'username', 'y': 'email'}

        for old, new in replacements.items():
            text = re.sub(rf'\b{old}\b', new, text, flags=re.IGNORECASE)

        q.question = text

        # Also update code_context if present
        if q.code_context:
            for old, new in replacements.items():
                q.code_context = re.sub(rf'\b{old}\b', new, q.code_context, flags=re.IGNORECASE)

        return q, "replace_abstract_variables"

    def _add_real_world_context(self, q: Question) -> Tuple[Question, str]:
        """Add practical real-world context to questions"""

        # Choose appropriate context based on topic
        context_map = {
            "Data Types": self.contexts["data_analysis"],
            "Control Flow": self.contexts["automation"],
            "Functions": self.contexts["general"],
            "Files & I/O": self.contexts["automation"],
            "Strings": self.contexts["web_development"],
        }

        contexts = context_map.get(q.topic, self.contexts["general"])
        context_example = random.choice(contexts)

        # Reframe question with context
        text = q.question.lower()

        if "list of numbers" in text:
            q.question = q.question.replace(
                "list of numbers",
                f"list of customer order values: [342, 501, 289, 612, 445]"
            )

        elif "variable" in text and "swap" not in text:
            # Add context about what variable represents
            q.question = f"You're building a user registration form. {q.question}"

        elif q.style == "scenario_task" and not any(word in text for word in ["you're", "you need", "build"]):
            # Add scenario framing
            q.question = f"You're {context_example}. {q.question}"

        return q, "add_real_world_context"

    def _diversify_names(self, q: Question) -> Tuple[Question, str]:
        """Replace Western-only names with globally diverse names"""

        text = q.question

        western_to_diverse = {
            "alice": random.choice(["Priya", "Amara", "Sofia"]),
            "bob": random.choice(["Chen", "Kofi", "Ahmed"]),
            "john": random.choice(["Arjun", "Diego", "Kwame"]),
            "jane": random.choice(["Yuki", "Elena", "Fatima"]),
            "mike": random.choice(["Carlos", "Rashid", "Mei"]),
        }

        for old, new in western_to_diverse.items():
            text = re.sub(rf'\b{old}\b', new, text, flags=re.IGNORECASE)

        # Also replace in code_context
        if q.code_context:
            for old, new in western_to_diverse.items():
                q.code_context = re.sub(rf'\b{old}\b', new, q.code_context, flags=re.IGNORECASE)

        q.question = text

        return q, "diversify_names"

    def _fix_blooms_alignment(self, q: Question) -> Tuple[Question, str]:
        """Fix Bloom's taxonomy misalignment"""

        # Get correct Bloom's level for difficulty
        expected_blooms = self.config['blooms'].get(q.difficulty, [])

        if not expected_blooms:
            return q, "no_bloom_fix_needed"

        # Choose most appropriate Bloom's level based on style
        style_bloom_map = {
            "single_word": "remember",
            "fill_in_blank": "remember",
            "short_question": "understand",
            "explain_concept": "understand",
            "predict_output": "apply",
            "debug_fix": "apply",
            "scenario_task": "apply",
            "compare_contrast": "analyze",
            "rewrite": "create",
        }

        suggested_bloom = style_bloom_map.get(q.style, expected_blooms[0])

        # Check if suggested is in expected
        if suggested_bloom not in expected_blooms:
            suggested_bloom = expected_blooms[0]

        q.bloom_level = suggested_bloom

        return q, "fix_blooms_alignment"

    def _enhance_keywords(self, q: Question) -> Tuple[Question, str]:
        """Enhance keyword metadata for better RAG"""

        existing = set(q.keywords) if q.keywords else set()

        # Extract potential keywords from question
        text = q.question.lower()
        words = re.findall(r'\b\w+\b', text)

        # Common Python keywords to add
        python_terms = [
            "python", "syntax", "code", "programming", "function",
            "variable", "data", "type", "loop", "condition"
        ]

        # Add relevant Python terms
        for term in python_terms:
            if term in text and term not in existing:
                existing.add(term)

        # Add topic-based keywords
        topic_keywords = {
            "Data Types": ["int", "str", "float", "list", "tuple", "dict", "set", "bool"],
            "Control Flow": ["if", "else", "elif", "for", "while", "break", "continue"],
            "Functions": ["def", "return", "parameter", "argument", "call"],
            "Operators": ["arithmetic", "comparison", "logical", "assignment"],
        }

        if q.topic in topic_keywords:
            for kw in topic_keywords[q.topic]:
                if kw.lower() in text:
                    existing.add(kw)

        # Convert back to list
        q.keywords = sorted(list(existing))

        return q, "enhance_keywords"

    def _add_practical_context(self, q: Question) -> Tuple[Question, str]:
        """Add mention of practical tools or workflows"""

        if q.difficulty == "stretch":
            # Add tool awareness
            tool_hints = {
                "debugging": " (Consider using Python's pdb debugger or print statements to trace execution.)",
                "testing": " (This is commonly tested using pytest or unittest frameworks.)",
                "style": " (Use linters like flake8 or black to check code quality.)",
            }

            for key, hint in tool_hints.items():
                if key in q.question.lower() and hint not in q.question:
                    q.question += hint
                    break

        return q, "add_practical_context"

    def _generic_enhancement(self, q: Question) -> Tuple[Question, str]:
        """Generic enhancements when no specific strategy applies"""

        # Ensure question ends with proper punctuation
        if not q.question.strip().endswith(('?', '.', ':')):
            if '?' not in q.question:
                q.question = q.question.strip() + '?'

        # Capitalize first letter
        q.question = q.question[0].upper() + q.question[1:]

        return q, "generic_enhancement"

    def batch_transform(self, questions: List[Question], auto: bool = False, threshold: float = 4.8) -> Dict[str, any]:
        """
        Transform multiple questions
        Returns summary statistics
        """

        results = {
            "total": len(questions),
            "transformed": 0,
            "unchanged": 0,
            "improvements": [],
            "strategies_used": {},
        }

        for i, q in enumerate(questions):
            current_score = self.analyzer.analyze(q)["overall"]

            if current_score >= threshold:
                results["unchanged"] += 1
                continue

            transformed, strategy, improvement = self.transform(q, auto=auto)

            if improvement > 0:
                results["transformed"] += 1
                results["improvements"].append(improvement)
                results["strategies_used"][strategy] = results["strategies_used"].get(strategy, 0) + 1

                # Update original question in list
                questions[i] = transformed

        if results["improvements"]:
            results["avg_improvement"] = sum(results["improvements"]) / len(results["improvements"])
        else:
            results["avg_improvement"] = 0.0

        return results
