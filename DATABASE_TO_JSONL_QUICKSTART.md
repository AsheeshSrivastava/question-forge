# QuestionForge - Database to JSONL Quick Start

**Get your Python questions from database into QuestionForge in 5 minutes!**

---

## 🎯 What You Need

✅ Your question bank in a database (SQLite, MySQL, PostgreSQL, or Python script)
✅ Python 3.7+ installed
✅ 5 minutes of your time

---

## 🚀 Three Methods (Choose One)

### **Method 1: CSV Export (Easiest - Recommended!)**

**If you can export your database to CSV:**

1. **Export from database to CSV**
   - Open your database tool
   - Run: `SELECT * FROM questions WHERE subject='Python'`
   - Export to CSV (e.g., `python_questions.csv`)

2. **Convert CSV to JSONL**
   ```bash
   cd D:\claude-projects\question-forge
   python convert_to_jsonl.py python_questions.csv -o python_questions.jsonl
   ```

3. **Done!** Use in QuestionForge or upload to Hugging Face

**Time:** 2 minutes ⚡

---

### **Method 2: Excel Export (Super Easy)**

**If you can export to Excel:**

1. **Export from database to Excel**
   - Save as `python_questions.xlsx`

2. **Convert Excel to JSONL**
   ```bash
   cd D:\claude-projects\question-forge
   python convert_to_jsonl.py python_questions.xlsx -o python_questions.jsonl
   ```

3. **Done!**

**Time:** 2 minutes ⚡

---

### **Method 3: Direct Database Connection (Advanced)**

**If you want to export directly from database:**

**Step 1:** Edit `export_from_database.py`

```python
# Line 18-19: Set your database path
DATABASE_TYPE = 'sqlite'
DATABASE_PATH = 'path/to/your/questions.db'  # CHANGE THIS

# Line 35-47: Edit your SQL query to match your table
SQL_QUERY = """
    SELECT
        id,                          -- Question ID
        topic,                       -- Topic/category
        question_text as question,   -- Question text
        question_type as style,      -- Question format
        difficulty_level as difficulty,  -- starter/core/stretch
        bloom_level,                 -- Bloom's taxonomy level
        keywords,                    -- Keywords (comma-separated or array)
        subtopics                    -- Subtopics
    FROM your_table_name            -- CHANGE THIS
    WHERE subject = 'Python'        -- CHANGE THIS if needed
"""

# Line 51: Set output filename
OUTPUT_FILE = 'python_questions.jsonl'
```

**Step 2:** Run the export

```bash
cd D:\claude-projects\question-forge
python export_from_database.py
```

**Step 3:** Done!

**Time:** 5 minutes (first time), 30 seconds (after setup)

---

## 📋 What Your Database Needs

**Minimum required columns:**

| Your Column | QuestionForge Needs | Example |
|-------------|---------------------|---------|
| Any ID column | `id` | `q_py_001` |
| Topic/Category | `topic` | `Python Basics` |
| Question text | `question` | `What is a variable?` |
| Question type | `style` | `short_question` |
| Difficulty | `difficulty` | `starter` |

**The converter automatically maps common names:**
- `question_id` → `id`
- `subject` → `topic`
- `question_text` → `question`
- `question_type` → `style`
- `level` → `difficulty`

---

## ✅ Valid Values

Your database should have these values (converter validates):

### Question Styles (pick one):
- `short_question` - Brief question
- `scenario_task` - Real-world task
- `debug_fix` - Find and fix bug
- `predict_output` - What does this print?
- `explain_concept` - Explain something
- (see CONVERSION_GUIDE.md for all 9 styles)

### Difficulty Levels:
- `starter` - Beginner
- `core` - Intermediate
- `stretch` - Advanced

### Bloom's Levels (optional but recommended):
- `remember` - Recall facts
- `understand` - Explain concepts
- `apply` - Use knowledge
- `analyze` - Break down problems
- `evaluate` - Judge quality
- `create` - Build something

---

## 🎯 Complete Example

### Your Database Table:

```sql
CREATE TABLE questions (
    id VARCHAR(50) PRIMARY KEY,
    subject VARCHAR(50),
    topic VARCHAR(100),
    question_text TEXT,
    question_type VARCHAR(50),
    difficulty_level VARCHAR(20),
    bloom_level VARCHAR(20),
    keywords TEXT,
    active BOOLEAN
);
```

### Your Data:

| id | subject | topic | question_text | question_type | difficulty_level | bloom_level | keywords |
|----|---------|-------|---------------|---------------|------------------|-------------|----------|
| q_py_001 | Python | Python Basics | What is a variable? | short_question | starter | remember | variable,syntax |
| q_py_002 | Python | Functions | Write a function to add two numbers | scenario_task | core | apply | function,parameters |

### Export Query:

```sql
SELECT
    id,
    topic,
    question_text as question,
    question_type as style,
    difficulty_level as difficulty,
    bloom_level,
    keywords
FROM questions
WHERE subject = 'Python'
AND active = true
ORDER BY id;
```

### Export to CSV:

Save as `python_questions.csv`:
```csv
id,topic,question,style,difficulty,bloom_level,keywords
q_py_001,Python Basics,What is a variable?,short_question,starter,remember,"variable,syntax"
q_py_002,Functions,Write a function to add two numbers,scenario_task,core,apply,"function,parameters"
```

### Convert to JSONL:

```bash
python convert_to_jsonl.py python_questions.csv -o python_questions.jsonl
```

### Result (`python_questions.jsonl`):

```jsonl
{"id": "q_py_001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter", "bloom_level": "remember", "keywords": ["variable", "syntax"], "subtopics": [], "prerequisites": [], "language": "en"}
{"id": "q_py_002", "topic": "Functions", "question": "Write a function to add two numbers", "style": "scenario_task", "difficulty": "core", "bloom_level": "apply", "keywords": ["function", "parameters"], "subtopics": [], "prerequisites": [], "language": "en"}
```

### Upload to Hugging Face:

1. Go to your QuestionForge Space
2. Go to "Analyze Questions" tab
3. Upload `python_questions.jsonl`
4. Click "Analyze Quality"
5. See scores! 🎉

---

## 💡 Pro Tips

### Tip 1: Test with 10 Questions First

```sql
-- Export just 10 questions to test
SELECT * FROM questions
WHERE subject = 'Python'
LIMIT 10;
```

Save to CSV, convert, verify it works, then export all.

### Tip 2: Filter Active Questions Only

```sql
SELECT * FROM questions
WHERE subject = 'Python'
AND active = true
AND question_text IS NOT NULL;
```

### Tip 3: Add Missing IDs

If your questions don't have IDs:

```python
import pandas as pd

df = pd.read_csv('questions.csv')
df['id'] = ['q_py_' + str(i).zfill(3) for i in range(1, len(df) + 1)]
df.to_csv('questions_with_ids.csv', index=False)
```

### Tip 4: Standardize Values

Before export, update your database:

```sql
-- Standardize difficulty levels
UPDATE questions
SET difficulty_level = 'starter'
WHERE difficulty_level IN ('easy', 'beginner', 'basic');

UPDATE questions
SET difficulty_level = 'core'
WHERE difficulty_level IN ('medium', 'intermediate');

UPDATE questions
SET difficulty_level = 'stretch'
WHERE difficulty_level IN ('hard', 'advanced', 'expert');

-- Standardize question types
UPDATE questions
SET question_type = 'short_question'
WHERE question_type IN ('multiple_choice', 'short_answer', 'text');

UPDATE questions
SET question_type = 'scenario_task'
WHERE question_type IN ('coding', 'programming', 'write_code');
```

---

## 🐛 Troubleshooting

### Problem: "No questions found"

**Check:**
- SQL WHERE clause not too restrictive
- Table/column names are correct
- Questions exist in database

**Solution:**
```sql
-- Test query first
SELECT COUNT(*) FROM questions WHERE subject = 'Python';
```

---

### Problem: "Missing required field 'id'"

**Cause:** ID column missing or named differently

**Solution:** Add to SELECT with alias
```sql
SELECT
    question_id as id,  -- Map your ID column
    ...
```

---

### Problem: Keywords showing as string instead of array

**Cause:** Keywords stored as comma-separated text

**Solution:** Converter handles this automatically!
```
Input: "variable,syntax,basics"
Output: ["variable", "syntax", "basics"]
```

---

### Problem: Special characters broken (é, ñ, etc.)

**Cause:** Encoding issue

**Solution:** Use UTF-8 encoding
```sql
-- In MySQL
SELECT * FROM questions INTO OUTFILE 'questions.csv'
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

---

## ✅ Verification

After conversion, verify:

```bash
# Count questions
wc -l python_questions.jsonl
# Output: 238 python_questions.jsonl

# Check first question
head -n 1 python_questions.jsonl | python -m json.tool

# Analyze with QuestionForge
py main.py analyze python_questions.jsonl
```

**Expected:**
```
✅ Loaded X questions
📊 Average score, distribution, issues
```

---

## 🎯 Your Action Plan

**Right now (5 minutes):**

1. **Export your questions to CSV**
   - Use your database tool (phpMyAdmin, DBeaver, etc.)
   - Or run SQL query and save as CSV

2. **Convert to JSONL**
   ```bash
   cd D:\claude-projects\question-forge
   python convert_to_jsonl.py YOUR_FILE.csv -o questions.jsonl
   ```

3. **Test locally**
   ```bash
   py main.py analyze questions.jsonl
   ```

4. **Upload to Hugging Face**
   - Go to your QuestionForge Space
   - Upload `questions.jsonl`
   - Analyze!

**Total time:** 5 minutes from database to analysis! 🚀

---

## 📚 Full Documentation

- **CONVERSION_GUIDE.md** - Comprehensive conversion guide
- **convert_to_jsonl.py** - Main converter script
- **export_from_database.py** - Direct database export helper
- **examples/** folder - Sample files (CSV, Excel, JSON)

---

## 🎉 Success!

Once converted, you can:

✅ Analyze with QuestionForge CLI
✅ Upload to Hugging Face web app
✅ Refine to 4.8/5 quality
✅ Download improved questions
✅ Export back to database if needed

---

**Questions? Check CONVERSION_GUIDE.md for complete examples!**

**"Small fixes, big clarity"** - Starting with your data! 🔥
