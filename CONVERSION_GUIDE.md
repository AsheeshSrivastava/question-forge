# QuestionForge - Question Bank Conversion Guide

**Convert your existing questions to QuestionForge JSONL format**

---

## 🎯 Quick Start

**If you have questions in CSV, Excel, or JSON:**

```bash
# Navigate to QuestionForge
cd D:\claude-projects\question-forge

# Convert your file
python convert_to_jsonl.py YOUR_QUESTIONS.csv -o questions.jsonl

# Analyze with QuestionForge
py main.py analyze questions.jsonl
```

**That's it!** 🎉

---

## 📋 Supported Input Formats

The converter supports:

### 1. CSV Files
- ✅ Simple spreadsheet format
- ✅ Easy to create in Excel
- ✅ Good for bulk import

### 2. Excel Files (.xlsx, .xls)
- ✅ Native Excel format
- ✅ Supports multiple sheets
- ✅ Good for complex data

### 3. JSON Files
- ✅ Structured format
- ✅ Good for API exports
- ✅ Supports nested data

### 4. Python Database
- ✅ Direct from SQL query
- ✅ Pandas DataFrame
- ✅ See examples below

---

## 📝 Required Fields

Your questions MUST have these fields:

| Field | Description | Example |
|-------|-------------|---------|
| **id** | Unique identifier | `q_py_001` |
| **topic** | Main category | `Python Basics` |
| **question** | Question text | `What is a variable?` |
| **style** | Question format | `short_question` |
| **difficulty** | Level | `starter`, `core`, or `stretch` |

---

## 🎨 Optional Fields (Recommended)

| Field | Description | Example |
|-------|-------------|---------|
| **bloom_level** | Cognitive level | `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create` |
| **keywords** | Search terms | `["variable", "syntax"]` |
| **subtopics** | Categories | `["variables", "basics"]` |
| **prerequisites** | Dependencies | `["q_py_001"]` |
| **code_context** | Code snippet | `x = 5` |

---

## 🔧 Method 1: Convert from CSV

### Step 1: Create CSV File

**Option A: Use Excel**
1. Open Excel
2. Create columns: `id`, `topic`, `question`, `style`, `difficulty`
3. Add your questions
4. Save As → CSV (UTF-8)

**Option B: Use Google Sheets**
1. Create spreadsheet with columns
2. File → Download → CSV

### Step 2: Convert to JSONL

```bash
python convert_to_jsonl.py questions.csv -o questions.jsonl
```

### CSV Example:

```csv
id,topic,question,style,difficulty,bloom_level,keywords
q_py_001,Python Basics,What is a variable?,short_question,starter,remember,"variable,syntax,basics"
q_py_002,Functions,Write a function to add two numbers,scenario_task,core,apply,"function,parameters"
```

**See:** `examples/example_input.csv` for complete example

---

## 📊 Method 2: Convert from Excel

### Step 1: Prepare Excel File

Create an Excel file with these columns:

| id | topic | question | style | difficulty | bloom_level | keywords |
|----|-------|----------|-------|------------|-------------|----------|
| q_py_001 | Python Basics | What is a variable? | short_question | starter | remember | variable,syntax |

### Step 2: Convert to JSONL

```bash
# Default (first sheet)
python convert_to_jsonl.py questions.xlsx -o questions.jsonl

# Specific sheet
python convert_to_jsonl.py questions.xlsx -s "Questions" -o questions.jsonl

# Sheet by index (0 = first sheet)
python convert_to_jsonl.py questions.xlsx -s 0 -o questions.jsonl
```

---

## 📋 Method 3: Convert from JSON

### Step 1: Create JSON File

```json
{
  "questions": [
    {
      "id": "q_py_001",
      "topic": "Python Basics",
      "question": "What is a variable?",
      "style": "short_question",
      "difficulty": "starter",
      "bloom_level": "remember",
      "keywords": ["variable", "syntax", "basics"]
    }
  ]
}
```

### Step 2: Convert to JSONL

```bash
python convert_to_jsonl.py questions.json -o questions.jsonl
```

**See:** `examples/example_input.json` for complete example

---

## 🗄️ Method 4: Convert from Python Database

### From SQL Database

```python
import sqlite3
import sys
sys.path.append('D:/claude-projects/question-forge')
from convert_to_jsonl import QuestionConverter

# Connect to database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Query questions
cursor.execute("""
    SELECT
        id,
        topic,
        question_text as question,
        question_type as style,
        difficulty_level as difficulty,
        bloom_level,
        keywords,
        subtopics
    FROM questions
    WHERE subject = 'Python'
""")

# Convert to dictionaries
columns = [desc[0] for desc in cursor.description]
questions = [dict(zip(columns, row)) for row in cursor.fetchall()]

# Convert to JSONL
converter = QuestionConverter()
normalized_questions = converter.from_dict_list(questions)
converter.to_jsonl(normalized_questions, 'questions.jsonl')
converter.print_summary()

print("\n✅ Converted database questions to questions.jsonl")
```

### From Pandas DataFrame

```python
import pandas as pd
from convert_to_jsonl import QuestionConverter

# Load from database
df = pd.read_sql("""
    SELECT * FROM questions WHERE subject = 'Python'
""", connection)

# Or load from CSV
df = pd.read_csv('questions.csv')

# Convert to dictionaries
questions = df.to_dict('records')

# Convert to JSONL
converter = QuestionConverter()
normalized_questions = converter.from_dict_list(questions)
converter.to_jsonl(normalized_questions, 'questions.jsonl')
converter.print_summary()
```

### From Python List

```python
from convert_to_jsonl import QuestionConverter

# Your questions as Python dictionaries
questions = [
    {
        'id': 'q_py_001',
        'topic': 'Python Basics',
        'question': 'What is a variable?',
        'style': 'short_question',
        'difficulty': 'starter',
        'bloom_level': 'remember',
        'keywords': ['variable', 'syntax', 'basics']
    },
    {
        'id': 'q_py_002',
        'topic': 'Functions',
        'question': 'Write a function to add two numbers',
        'style': 'scenario_task',
        'difficulty': 'core',
        'bloom_level': 'apply',
        'keywords': ['function', 'parameters', 'addition']
    }
]

# Convert
converter = QuestionConverter()
normalized_questions = converter.from_dict_list(questions)
converter.to_jsonl(normalized_questions, 'questions.jsonl')
converter.print_summary()
```

---

## 🔄 Field Mapping

The converter automatically maps common field names:

| Your Field | Maps To |
|------------|---------|
| `question_id` | `id` |
| `subject` | `topic` |
| `question_text` | `question` |
| `question_type` | `style` |
| `level` | `difficulty` |
| `bloom` | `bloom_level` |
| `tags` | `keywords` |
| `sub_topics` | `subtopics` |
| `prereqs` | `prerequisites` |

**Example:** If your CSV has `question_id` and `subject`, they'll be mapped to `id` and `topic` automatically.

---

## ✅ Valid Values

### Question Styles
Must be one of:
- `single_word` - One-word answer
- `short_question` - Brief question
- `predict_output` - What will this code output?
- `debug_fix` - Find and fix the bug
- `scenario_task` - Real-world task
- `fill_in_blank` - Complete the code
- `explain_concept` - Explain a concept
- `compare_contrast` - Compare two approaches
- `rewrite` - Improve this code

### Difficulty Levels
Must be one of:
- `starter` - Beginner level
- `core` - Intermediate level
- `stretch` - Advanced level

### Bloom's Taxonomy Levels
Must be one of:
- `remember` - Recall facts
- `understand` - Explain concepts
- `apply` - Use knowledge
- `analyze` - Break down problems
- `evaluate` - Judge quality
- `create` - Build something new

---

## 🎯 Complete Example Workflow

### Scenario: You have 100 questions in Excel

**Step 1: Prepare Excel File**
```
File: python_questions.xlsx
Columns: id, topic, question, style, difficulty, bloom_level, keywords
Rows: 100 questions
```

**Step 2: Convert to JSONL**
```bash
cd D:\claude-projects\question-forge
python convert_to_jsonl.py python_questions.xlsx -o python_questions.jsonl
```

**Output:**
```
📊 Reading Excel: python_questions.xlsx
✅ Loaded 100 questions from Excel
💾 Saving to JSONL: python_questions.jsonl
✅ Saved 100 questions to python_questions.jsonl

============================================================
📊 CONVERSION SUMMARY
============================================================

✅ All questions converted successfully!

============================================================

🎉 Success! Ready to use with QuestionForge:
   py main.py analyze python_questions.jsonl
```

**Step 3: Analyze with QuestionForge**
```bash
py main.py analyze python_questions.jsonl
```

**Step 4: Upload to Hugging Face App**
1. Go to your QuestionForge Space
2. Upload `python_questions.jsonl`
3. Click "Analyze Quality"
4. See scores!

---

## ⚠️ Common Issues & Solutions

### Issue: "Missing required field 'id'"

**Cause:** Questions don't have unique IDs

**Solution:** Add ID column to your file
```python
# Quick fix in Python
import pandas as pd

df = pd.read_csv('questions.csv')
df['id'] = ['q_py_' + str(i).zfill(3) for i in range(1, len(df) + 1)]
df.to_csv('questions_with_ids.csv', index=False)
```

---

### Issue: "Invalid style 'multiple_choice'"

**Cause:** Style value not recognized

**Solution:** Map to valid style
```python
style_mapping = {
    'multiple_choice': 'short_question',
    'true_false': 'short_question',
    'code_output': 'predict_output',
    'find_bug': 'debug_fix'
}

# Apply mapping
df['style'] = df['style'].map(style_mapping)
```

---

### Issue: Keywords showing as string instead of list

**Cause:** Keywords in CSV as comma-separated string

**Solution:** Converter handles this automatically!
```csv
# This works:
keywords
"variable,syntax,basics"

# Converts to:
"keywords": ["variable", "syntax", "basics"]
```

---

### Issue: Excel has multiple sheets

**Solution:** Specify sheet name or index
```bash
# By name
python convert_to_jsonl.py questions.xlsx -s "Python Questions" -o output.jsonl

# By index (0 = first sheet)
python convert_to_jsonl.py questions.xlsx -s 0 -o output.jsonl
```

---

## 🔍 Validating Your Conversion

After conversion, verify the output:

```bash
# Check first question
head -n 1 questions.jsonl

# Count questions
wc -l questions.jsonl

# View in readable format
python -m json.tool < questions.jsonl | head -n 50
```

**Expected output (first question):**
```json
{"id": "q_py_001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter", "bloom_level": "remember", "keywords": ["variable", "syntax"], "subtopics": [], "prerequisites": [], "language": "en"}
```

---

## 💡 Pro Tips

**Tip 1: Start Small**
```bash
# Test with first 10 questions
head -n 10 questions.csv > test_10.csv
python convert_to_jsonl.py test_10.csv -o test_10.jsonl
py main.py analyze test_10.jsonl
```

**Tip 2: Validate Before Converting**
- Ensure all required fields present
- Check for duplicate IDs
- Verify style values are valid

**Tip 3: Use Excel for Initial Cleanup**
- Sort by difficulty
- Filter incomplete questions
- Standardize formatting
- Then convert to JSONL

**Tip 4: Batch Processing**
```bash
# Convert multiple files
python convert_to_jsonl.py module1.csv -o module1.jsonl
python convert_to_jsonl.py module2.csv -o module2.jsonl

# Combine (if needed)
cat module1.jsonl module2.jsonl > all_questions.jsonl
```

**Tip 5: Keep Backups**
```bash
# Always backup original
cp original_questions.xlsx original_questions_backup.xlsx

# Version your JSONLs
python convert_to_jsonl.py questions.xlsx -o questions_v1.jsonl
```

---

## 📚 Templates

### CSV Template

Download: `examples/example_input.csv`

```csv
id,topic,question,style,difficulty,bloom_level,keywords,subtopics,prerequisites
q_py_001,Python Basics,Your question here,short_question,starter,remember,"keyword1,keyword2","subtopic1,subtopic2",
```

### Excel Template

1. Open Excel
2. Create columns: id, topic, question, style, difficulty, bloom_level, keywords, subtopics, prerequisites
3. Add validation dropdowns for style, difficulty, bloom_level
4. Fill in questions
5. Save as .xlsx

### JSON Template

Download: `examples/example_input.json`

```json
{
  "questions": [
    {
      "id": "q_py_001",
      "topic": "Python Basics",
      "question": "Your question here",
      "style": "short_question",
      "difficulty": "starter",
      "bloom_level": "remember",
      "keywords": ["keyword1", "keyword2"],
      "subtopics": ["subtopic1"],
      "prerequisites": []
    }
  ]
}
```

---

## 🚀 Advanced: Database Export Script

```python
#!/usr/bin/env python3
"""
Export questions from database to QuestionForge JSONL
"""

import sqlite3
from convert_to_jsonl import QuestionConverter

def export_from_database(db_path, output_path, subject='Python'):
    """Export questions from SQLite database"""

    # Connect
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query with proper mapping
    cursor.execute("""
        SELECT
            q.id,
            q.topic,
            q.question_text as question,
            q.question_type as style,
            q.difficulty_level as difficulty,
            q.bloom_level,
            q.keywords,
            q.subtopics,
            q.prerequisites,
            q.code_snippet as code_context
        FROM questions q
        WHERE q.subject = ?
        AND q.active = 1
        ORDER BY q.id
    """, (subject,))

    # Convert to dicts
    columns = [desc[0] for desc in cursor.description]
    questions = []

    for row in cursor.fetchall():
        q = dict(zip(columns, row))
        questions.append(q)

    conn.close()

    # Convert to JSONL
    converter = QuestionConverter()
    normalized = converter.from_dict_list(questions)
    converter.to_jsonl(normalized, output_path)
    converter.print_summary()

    print(f"\n✅ Exported {len(normalized)} questions to {output_path}")
    return normalized


if __name__ == '__main__':
    # Usage
    questions = export_from_database(
        db_path='questions.db',
        output_path='python_questions.jsonl',
        subject='Python'
    )

    print(f"\n🎉 Ready to analyze:")
    print(f"   py main.py analyze python_questions.jsonl")
```

---

## ✅ Verification Checklist

After conversion, check:

- [ ] File size reasonable (not empty, not huge)
- [ ] Each line is valid JSON
- [ ] All questions have required fields
- [ ] IDs are unique
- [ ] Styles are valid values
- [ ] Difficulties are valid values
- [ ] Keywords are arrays (not strings)
- [ ] No special character issues

**Quick verify:**
```bash
# Count lines
wc -l questions.jsonl

# Check first question
head -n 1 questions.jsonl | python -m json.tool

# Analyze with QuestionForge
py main.py analyze questions.jsonl
```

---

## 🎯 Next Steps

After conversion:

1. **Verify** - Check output looks correct
2. **Test** - Analyze with QuestionForge CLI
3. **Upload** - Use in Hugging Face app
4. **Refine** - Improve to 4.8/5 quality
5. **Celebrate!** 🎉

---

**Need help? Check:**
- `examples/` folder for templates
- `convert_to_jsonl.py` source code
- QuestionForge documentation

**"Small fixes, big clarity"** - Starting with good data! 🔥
