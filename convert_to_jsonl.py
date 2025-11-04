#!/usr/bin/env python3
"""
QuestionForge - Question Bank Converter
Convert various formats to JSONL for QuestionForge

"Small fixes, big clarity" - Quest & Crossfire
"""

import json
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any
import argparse

# Try importing optional dependencies
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("⚠️  pandas not installed. Excel/CSV conversion will use basic CSV reader.")

try:
    import openpyxl
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False


class QuestionConverter:
    """Convert question banks to QuestionForge JSONL format"""

    # Required fields
    REQUIRED_FIELDS = ['id', 'topic', 'question', 'style', 'difficulty']

    # Valid values
    VALID_STYLES = [
        'single_word', 'short_question', 'predict_output', 'debug_fix',
        'scenario_task', 'fill_in_blank', 'explain_concept',
        'compare_contrast', 'rewrite'
    ]

    VALID_DIFFICULTIES = ['starter', 'core', 'stretch']

    VALID_BLOOM_LEVELS = [
        'remember', 'understand', 'apply', 'analyze', 'evaluate', 'create'
    ]

    def __init__(self):
        self.questions = []
        self.errors = []
        self.warnings = []

    def validate_question(self, q: Dict[str, Any]) -> bool:
        """Validate a single question"""
        valid = True

        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in q or not q[field]:
                self.errors.append(f"Question {q.get('id', 'unknown')}: Missing required field '{field}'")
                valid = False

        if not valid:
            return False

        # Validate style
        if q.get('style') and q['style'] not in self.VALID_STYLES:
            self.warnings.append(f"Question {q['id']}: Invalid style '{q['style']}'. Valid: {', '.join(self.VALID_STYLES)}")

        # Validate difficulty
        if q.get('difficulty') and q['difficulty'] not in self.VALID_DIFFICULTIES:
            self.warnings.append(f"Question {q['id']}: Invalid difficulty '{q['difficulty']}'. Valid: {', '.join(self.VALID_DIFFICULTIES)}")

        # Validate Bloom's level
        if q.get('bloom_level') and q['bloom_level'] not in self.VALID_BLOOM_LEVELS:
            self.warnings.append(f"Question {q['id']}: Invalid bloom_level '{q['bloom_level']}'. Valid: {', '.join(self.VALID_BLOOM_LEVELS)}")

        return True

    def normalize_question(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize and clean question data"""

        # Create base question
        question = {
            'id': str(raw.get('id', raw.get('question_id', ''))),
            'topic': str(raw.get('topic', raw.get('subject', 'Python'))),
            'question': str(raw.get('question', raw.get('question_text', ''))),
            'style': str(raw.get('style', raw.get('question_type', 'short_question'))),
            'difficulty': str(raw.get('difficulty', raw.get('level', 'core'))),
        }

        # Add optional fields if present
        optional_fields = {
            'subtopics': ['subtopics', 'sub_topics', 'categories'],
            'keywords': ['keywords', 'tags', 'search_terms'],
            'prerequisites': ['prerequisites', 'prereqs', 'dependencies'],
            'bloom_level': ['bloom_level', 'bloom', 'cognitive_level'],
            'answer_type': ['answer_type', 'expected_answer'],
            'expected_time_sec': ['expected_time_sec', 'time_seconds', 'duration'],
            'duplicates_check': ['duplicates_check', 'duplicate_check'],
            'language': ['language', 'lang'],
            'code_context': ['code_context', 'code', 'code_snippet'],
        }

        for target_field, source_fields in optional_fields.items():
            for source_field in source_fields:
                if source_field in raw and raw[source_field]:
                    value = raw[source_field]

                    # Handle list fields
                    if target_field in ['subtopics', 'keywords', 'prerequisites']:
                        if isinstance(value, str):
                            # Split comma-separated strings
                            value = [v.strip() for v in value.split(',') if v.strip()]
                        elif not isinstance(value, list):
                            value = [str(value)]

                    question[target_field] = value
                    break

        # Set defaults for optional fields
        if 'keywords' not in question:
            question['keywords'] = []
        if 'subtopics' not in question:
            question['subtopics'] = []
        if 'prerequisites' not in question:
            question['prerequisites'] = []
        if 'language' not in question:
            question['language'] = 'en'

        return question

    def from_csv(self, filepath: str) -> List[Dict[str, Any]]:
        """Convert CSV file to questions"""
        print(f"📄 Reading CSV: {filepath}")

        questions = []

        if HAS_PANDAS:
            # Use pandas for better CSV handling
            df = pd.read_csv(filepath)
            for _, row in df.iterrows():
                raw = row.to_dict()
                question = self.normalize_question(raw)
                if self.validate_question(question):
                    questions.append(question)
        else:
            # Use basic CSV reader
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    question = self.normalize_question(row)
                    if self.validate_question(question):
                        questions.append(question)

        print(f"✅ Loaded {len(questions)} questions from CSV")
        return questions

    def from_excel(self, filepath: str, sheet_name: str = 0) -> List[Dict[str, Any]]:
        """Convert Excel file to questions"""
        print(f"📊 Reading Excel: {filepath}")

        if not HAS_PANDAS:
            raise ImportError("pandas is required for Excel conversion. Install: pip install pandas openpyxl")

        questions = []
        df = pd.read_excel(filepath, sheet_name=sheet_name)

        for _, row in df.iterrows():
            raw = row.to_dict()
            question = self.normalize_question(raw)
            if self.validate_question(question):
                questions.append(question)

        print(f"✅ Loaded {len(questions)} questions from Excel")
        return questions

    def from_json(self, filepath: str) -> List[Dict[str, Any]]:
        """Convert JSON file to questions"""
        print(f"📋 Reading JSON: {filepath}")

        questions = []

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Handle both list of questions and object with questions array
        if isinstance(data, list):
            raw_questions = data
        elif isinstance(data, dict) and 'questions' in data:
            raw_questions = data['questions']
        else:
            raise ValueError("JSON must be a list or object with 'questions' array")

        for raw in raw_questions:
            question = self.normalize_question(raw)
            if self.validate_question(question):
                questions.append(question)

        print(f"✅ Loaded {len(questions)} questions from JSON")
        return questions

    def from_dict_list(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Convert list of dictionaries to questions"""
        print(f"🔄 Processing {len(data)} questions from Python data")

        questions = []
        for raw in data:
            question = self.normalize_question(raw)
            if self.validate_question(question):
                questions.append(question)

        print(f"✅ Processed {len(questions)} questions")
        return questions

    def to_jsonl(self, questions: List[Dict[str, Any]], output_path: str):
        """Save questions to JSONL file"""
        print(f"💾 Saving to JSONL: {output_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            for question in questions:
                # Remove None values
                clean_question = {k: v for k, v in question.items() if v is not None}
                json_line = json.dumps(clean_question, ensure_ascii=False)
                f.write(json_line + '\n')

        print(f"✅ Saved {len(questions)} questions to {output_path}")

    def print_summary(self):
        """Print conversion summary"""
        print("\n" + "="*60)
        print("📊 CONVERSION SUMMARY")
        print("="*60)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors[:10]:
                print(f"  - {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more errors")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings[:10]:
                print(f"  - {warning}")
            if len(self.warnings) > 10:
                print(f"  ... and {len(self.warnings) - 10} more warnings")

        if not self.errors and not self.warnings:
            print("\n✅ All questions converted successfully!")

        print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(
        description='Convert question banks to QuestionForge JSONL format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert CSV to JSONL
  python convert_to_jsonl.py questions.csv -o questions.jsonl

  # Convert Excel to JSONL
  python convert_to_jsonl.py questions.xlsx -o questions.jsonl

  # Convert JSON to JSONL
  python convert_to_jsonl.py questions.json -o questions.jsonl

  # Specify Excel sheet
  python convert_to_jsonl.py questions.xlsx -s "Sheet2" -o questions.jsonl
        """
    )

    parser.add_argument('input', help='Input file (CSV, Excel, or JSON)')
    parser.add_argument('-o', '--output', required=True, help='Output JSONL file')
    parser.add_argument('-s', '--sheet', default=0, help='Excel sheet name or index (default: 0)')
    parser.add_argument('--format', choices=['csv', 'excel', 'json'], help='Force input format (auto-detect if not specified)')

    args = parser.parse_args()

    # Create converter
    converter = QuestionConverter()

    # Detect format
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Error: File not found: {args.input}")
        sys.exit(1)

    format_type = args.format
    if not format_type:
        ext = input_path.suffix.lower()
        if ext == '.csv':
            format_type = 'csv'
        elif ext in ['.xlsx', '.xls']:
            format_type = 'excel'
        elif ext == '.json':
            format_type = 'json'
        else:
            print(f"❌ Error: Unknown file extension: {ext}")
            print("   Specify format with --format csv/excel/json")
            sys.exit(1)

    # Convert
    try:
        if format_type == 'csv':
            questions = converter.from_csv(args.input)
        elif format_type == 'excel':
            questions = converter.from_excel(args.input, args.sheet)
        elif format_type == 'json':
            questions = converter.from_json(args.input)

        if questions:
            converter.to_jsonl(questions, args.output)
            converter.print_summary()
            print(f"\n🎉 Success! Ready to use with QuestionForge:")
            print(f"   py main.py analyze {args.output}")
        else:
            print("\n❌ No valid questions found!")
            converter.print_summary()
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
