"""
Question Parser - JSONL handling and validation
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class Question:
    """Represents a single question with all metadata"""

    # Required fields
    id: str
    topic: str
    question: str
    style: str
    difficulty: str

    # Common fields
    subtopics: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    bloom_level: Optional[str] = None
    answer_type: Optional[str] = None
    expected_time_sec: Optional[int] = None
    duplicates_check: Optional[str] = None
    language: str = "en"
    code_context: Optional[str] = None
    constraints: Optional[Dict[str, Any]] = None

    # Refinement metadata
    original_question: Optional[str] = None
    refinement_history: List[Dict[str, Any]] = field(default_factory=list)
    quality_scores: Optional[Dict[str, float]] = None
    last_refined: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values"""
        data = asdict(self)
        return {k: v for k, v in data.items() if v is not None}

    def update_from_refinement(self, refined_question: str, strategy: str, score_improvement: float):
        """Record a refinement"""
        if self.original_question is None:
            self.original_question = self.question

        self.refinement_history.append({
            "timestamp": datetime.now().isoformat(),
            "strategy": strategy,
            "old_question": self.question,
            "new_question": refined_question,
            "score_improvement": score_improvement
        })

        self.question = refined_question
        self.last_refined = datetime.now().isoformat()


class QuestionParser:
    """Parse and validate question banks"""

    REQUIRED_FIELDS = {"id", "topic", "question", "style", "difficulty"}
    VALID_STYLES = {
        "single_word", "short_question", "predict_output", "debug_fix",
        "scenario_task", "fill_in_blank", "explain_concept",
        "compare_contrast", "rewrite"
    }
    VALID_DIFFICULTIES = {"starter", "core", "stretch"}
    VALID_BLOOM_LEVELS = {
        "remember", "understand", "apply", "analyze", "evaluate", "create"
    }

    @staticmethod
    def parse_jsonl(file_path: str) -> List[Question]:
        """Parse JSONL file into Question objects"""
        questions = []
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Question bank not found: {file_path}")

        with path.open('r', encoding='utf-8') as f:
            content = f.read()

        # Handle different JSONL formats
        # Format 1: One JSON per line
        # Format 2: JSON objects separated by } (legacy format)

        try:
            # Try standard JSONL (newline-separated)
            lines = content.strip().split('\n')
            for line_num, line in enumerate(lines, 1):
                if not line.strip():
                    continue

                try:
                    data = json.loads(line)
                    question = QuestionParser._dict_to_question(data)
                    questions.append(question)
                except json.JSONDecodeError:
                    # If fails, might be legacy format
                    pass

        except Exception:
            # Try legacy format (} separated)
            try:
                json_objects = content.strip().split('}')
                for obj in json_objects:
                    obj = obj.strip()
                    if not obj:
                        continue

                    # Add back the closing brace
                    obj += '}'

                    # Handle escaped characters
                    obj = obj.replace('\\[', '[').replace('\\]', ']')
                    obj = obj.replace('\\_', '_').replace('\\*', '*')

                    data = json.loads(obj)
                    question = QuestionParser._dict_to_question(data)
                    questions.append(question)

            except Exception as e:
                raise ValueError(f"Failed to parse question bank: {e}")

        if not questions:
            raise ValueError("No valid questions found in file")

        return questions

    @staticmethod
    def _dict_to_question(data: Dict[str, Any]) -> Question:
        """Convert dictionary to Question object with validation"""

        # Check required fields
        missing = QuestionParser.REQUIRED_FIELDS - set(data.keys())
        if missing:
            raise ValueError(f"Missing required fields: {missing} in question {data.get('id', 'unknown')}")

        # Validate style
        if data['style'] not in QuestionParser.VALID_STYLES:
            print(f"⚠️  Warning: Unknown style '{data['style']}' in question {data['id']}")

        # Validate difficulty
        if data['difficulty'] not in QuestionParser.VALID_DIFFICULTIES:
            print(f"⚠️  Warning: Invalid difficulty '{data['difficulty']}' in question {data['id']}")

        # Validate Bloom's level if present
        bloom = data.get('bloom_level') or data.get('bloom')
        if bloom and bloom not in QuestionParser.VALID_BLOOM_LEVELS:
            print(f"⚠️  Warning: Invalid Bloom's level '{bloom}' in question {data['id']}")

        # Normalize field names
        normalized = {
            'id': data['id'],
            'topic': data['topic'],
            'question': data['question'],
            'style': data['style'],
            'difficulty': data['difficulty'],
            'subtopics': data.get('subtopics', []),
            'keywords': data.get('keywords', []),
            'prerequisites': data.get('prerequisites', []),
            'bloom_level': bloom,
            'answer_type': data.get('answer_type'),
            'expected_time_sec': data.get('expected_time_sec'),
            'duplicates_check': data.get('duplicates_check'),
            'language': data.get('language', 'en'),
            'code_context': data.get('code_context'),
            'constraints': data.get('constraints'),
            'original_question': data.get('original_question'),
            'refinement_history': data.get('refinement_history', []),
            'quality_scores': data.get('quality_scores'),
            'last_refined': data.get('last_refined'),
        }

        return Question(**normalized)

    @staticmethod
    def save_jsonl(questions: List[Question], output_path: str, pretty: bool = False):
        """Save questions to JSONL file"""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w', encoding='utf-8') as f:
            for question in questions:
                data = question.to_dict()
                if pretty:
                    line = json.dumps(data, ensure_ascii=False, indent=2)
                else:
                    line = json.dumps(data, ensure_ascii=False)
                f.write(line + '\n')

    @staticmethod
    def save_json(questions: List[Question], output_path: str):
        """Save questions to pretty JSON file"""
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = [q.to_dict() for q in questions]

        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def validate_question_bank(questions: List[Question]) -> Dict[str, Any]:
        """Validate entire question bank and return stats"""

        stats = {
            "total_questions": len(questions),
            "validation_passed": True,
            "errors": [],
            "warnings": [],
            "distribution": {
                "by_difficulty": {},
                "by_style": {},
                "by_topic": {},
                "by_bloom": {}
            }
        }

        # Count distributions
        for q in questions:
            # Difficulty
            stats["distribution"]["by_difficulty"][q.difficulty] = \
                stats["distribution"]["by_difficulty"].get(q.difficulty, 0) + 1

            # Style
            stats["distribution"]["by_style"][q.style] = \
                stats["distribution"]["by_style"].get(q.style, 0) + 1

            # Topic
            stats["distribution"]["by_topic"][q.topic] = \
                stats["distribution"]["by_topic"].get(q.topic, 0) + 1

            # Bloom
            if q.bloom_level:
                stats["distribution"]["by_bloom"][q.bloom_level] = \
                    stats["distribution"]["by_bloom"].get(q.bloom_level, 0) + 1

            # Validate completeness
            if not q.keywords or len(q.keywords) < 3:
                stats["warnings"].append(f"Question {q.id}: Insufficient keywords ({len(q.keywords)})")

            if q.style == "single_word" and len(q.question.split()) == 1:
                stats["warnings"].append(f"Question {q.id}: Single-word question (needs expansion)")

            if not q.bloom_level:
                stats["warnings"].append(f"Question {q.id}: Missing Bloom's level")

        return stats
