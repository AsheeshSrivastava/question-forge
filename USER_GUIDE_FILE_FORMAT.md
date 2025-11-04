# QuestionForge - File Format & Structure Guide

**For Users Uploading Questions to QuestionForge**

---

## 🎯 Quick Summary

QuestionForge accepts **JSONL files** (JSON Lines format) where each line is a complete, valid JSON object representing one question.

**File Extension:** `.jsonl`
**Encoding:** UTF-8
**Format:** One JSON object per line (no commas between lines)
**Size Limit:** 10 MB per file recommended

---

## 📋 Required File Format: JSONL

### What is JSONL?

JSONL (JSON Lines) is a format where:
- Each line contains **one complete JSON object**
- No commas between lines
- No wrapping array `[...]` around the file
- Each line can be parsed independently

### Example of Correct JSONL:

```jsonl
{"id": "q-001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter"}
{"id": "q-002", "topic": "Functions", "question": "How do you define a function?", "style": "short_question", "difficulty": "starter"}
{"id": "q-003", "topic": "OOP", "question": "What is inheritance?", "style": "short_question", "difficulty": "core"}
```

### ❌ NOT This (Regular JSON Array):

```json
[
  {"id": "q-001", "topic": "Python Basics", "question": "What is a variable?"},
  {"id": "q-002", "topic": "Functions", "question": "How do you define a function?"}
]
```

---

## 📝 Required Fields

Every question **MUST** have these 5 fields:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **id** | string | Unique identifier for the question | `"q-py-001"` or `"q-001"` |
| **topic** | string | Main subject category | `"Python Basics"` or `"Functions"` |
| **question** | string | The actual question text | `"What is a variable in Python?"` |
| **style** | string | Question format type (see below) | `"short_question"` |
| **difficulty** | string | Difficulty level (see below) | `"starter"` |

### Minimal Valid Example:

```json
{
  "id": "q-001",
  "topic": "Python Basics",
  "question": "What is a variable?",
  "style": "short_question",
  "difficulty": "starter"
}
```

---

## ✨ Optional Fields (Highly Recommended)

These fields improve question quality and QuestionForge's analysis:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| **bloom_level** | string | Cognitive level (see below) | `"understand"` |
| **keywords** | array | Search terms for RAG retrieval | `["variable", "syntax", "basics"]` |
| **subtopics** | array | Specific subcategories | `["variables", "declaration"]` |
| **prerequisites** | array | Required prior knowledge (question IDs) | `["q-001", "q-002"]` |
| **code_context** | string | Code snippet for context | `"x = 5\nprint(x)"` |

### Complete Example with Optional Fields:

```json
{
  "id": "q-py-001",
  "topic": "Python Basics",
  "subtopics": ["variables", "syntax"],
  "question": "What is a variable in Python, and how do you create one?",
  "style": "short_question",
  "difficulty": "starter",
  "bloom_level": "understand",
  "keywords": ["variable", "declaration", "syntax", "assignment"],
  "prerequisites": [],
  "code_context": "x = 5\ny = 'hello'"
}
```

---

## 🎨 Valid Values for Special Fields

### 1. Question Style (`style` field)

Choose **ONE** of these 9 accepted values:

| Style | Description | Use Case |
|-------|-------------|----------|
| `single_word` | One-word answer | Quick recall: "What keyword defines a function?" → "def" |
| `short_question` | Brief question requiring short answer | "How do you create a list in Python?" |
| `predict_output` | Predict what code will output | "What will this code print: print(5 + 3)?" |
| `debug_fix` | Find and fix a bug in code | "Fix the error in this code: def add(a b): return a+b" |
| `scenario_task` | Real-world task or problem | "Write a function to validate email addresses" |
| `fill_in_blank` | Complete missing code or text | "The keyword ___ is used to import modules" |
| `explain_concept` | Explain a concept in detail | "Explain what object-oriented programming means" |
| `compare_contrast` | Compare two concepts | "What's the difference between list and tuple?" |
| `rewrite` | Improve or refactor code | "Rewrite this loop as a list comprehension" |

**❌ Invalid Examples:**
- `"multiple_choice"` (not supported - use `"short_question"` instead)
- `"true_false"` (not supported - use `"short_question"` instead)
- `"essay"` (not supported - use `"explain_concept"` instead)

### 2. Difficulty Level (`difficulty` field)

Choose **ONE** of these 3 levels:

| Level | Description | Learner Profile |
|-------|-------------|-----------------|
| `starter` | Beginner level | New to programming or the topic |
| `core` | Intermediate level | Has basic knowledge, building skills |
| `stretch` | Advanced level | Experienced, ready for complex concepts |

**❌ Invalid Examples:**
- `"easy"`, `"beginner"`, `"basic"` → Use `"starter"`
- `"medium"`, `"intermediate"` → Use `"core"`
- `"hard"`, `"advanced"`, `"expert"` → Use `"stretch"`

### 3. Bloom's Taxonomy Level (`bloom_level` field - optional)

Choose **ONE** of these 6 cognitive levels:

| Level | Description | Question Example |
|-------|-------------|------------------|
| `remember` | Recall facts | "What is the syntax for a for loop?" |
| `understand` | Explain concepts | "Explain how list comprehensions work" |
| `apply` | Use knowledge in new situations | "Write a function to calculate factorial" |
| `analyze` | Break down problems | "Why does this code cause a memory leak?" |
| `evaluate` | Judge quality or make decisions | "Which sorting algorithm is best for this case?" |
| `create` | Build something new | "Design a class hierarchy for a library system" |

**Guideline:** Match `bloom_level` to question `style`:
- `remember` → often `single_word` or simple `short_question`
- `understand` → `explain_concept`, `compare_contrast`
- `apply` → `scenario_task`, `fill_in_blank`
- `analyze` → `debug_fix`, `predict_output`
- `evaluate` → `compare_contrast`, `scenario_task`
- `create` → `scenario_task`, `rewrite`

---

## 📐 Complete Template

Copy and modify this template for your questions:

```json
{
  "id": "q-YOUR-ID-HERE",
  "topic": "Your Topic Here",
  "subtopics": ["subtopic1", "subtopic2"],
  "question": "Your question text here?",
  "style": "short_question",
  "difficulty": "starter",
  "bloom_level": "understand",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "prerequisites": [],
  "code_context": ""
}
```

**Save as:** `your_questions.jsonl`

---

## ✅ Validation Checklist

Before uploading your JSONL file, verify:

### File Format:
- [ ] File extension is `.jsonl`
- [ ] File encoding is UTF-8
- [ ] Each line is a complete JSON object
- [ ] No commas between lines
- [ ] No wrapping array `[...]`
- [ ] No empty lines (optional, but recommended to avoid)

### Required Fields (Every Question Must Have):
- [ ] `id` - Unique string identifier
- [ ] `topic` - Subject category
- [ ] `question` - Question text
- [ ] `style` - One of 9 valid values
- [ ] `difficulty` - One of 3 valid values (starter, core, stretch)

### Valid Values:
- [ ] `style` is one of: single_word, short_question, predict_output, debug_fix, scenario_task, fill_in_blank, explain_concept, compare_contrast, rewrite
- [ ] `difficulty` is one of: starter, core, stretch
- [ ] `bloom_level` (if used) is one of: remember, understand, apply, analyze, evaluate, create

### Data Types:
- [ ] `keywords` is an **array** `["item1", "item2"]`, NOT a string `"item1, item2"`
- [ ] `subtopics` is an **array** `["topic1"]`, NOT a string `"topic1"`
- [ ] `prerequisites` is an **array** `["q-001"]`, NOT a string `"q-001"`

### Content Quality:
- [ ] Each question has a unique ID
- [ ] Question text is clear and complete
- [ ] No special characters causing encoding issues
- [ ] Code context (if used) is properly escaped

---

## 🛠️ How to Create a JSONL File

### Method 1: From CSV/Excel (Easiest)

If you have questions in a spreadsheet:

1. **Create columns:** id, topic, question, style, difficulty, bloom_level, keywords
2. **Save as CSV** (UTF-8 encoding)
3. **Use the converter:**
   ```bash
   cd D:\claude-projects\question-forge
   python convert_to_jsonl.py your_questions.csv -o your_questions.jsonl
   ```

See `DATABASE_TO_JSONL_QUICKSTART.md` for detailed instructions.

### Method 2: From Python Script

```python
import json

questions = [
    {
        "id": "q-001",
        "topic": "Python Basics",
        "question": "What is a variable?",
        "style": "short_question",
        "difficulty": "starter",
        "bloom_level": "remember",
        "keywords": ["variable", "basics"]
    },
    {
        "id": "q-002",
        "topic": "Functions",
        "question": "How do you define a function?",
        "style": "short_question",
        "difficulty": "starter",
        "bloom_level": "remember",
        "keywords": ["function", "def", "syntax"]
    }
]

# Save as JSONL
with open('questions.jsonl', 'w', encoding='utf-8') as f:
    for q in questions:
        json.dump(q, f, ensure_ascii=False)
        f.write('\n')

print("Created questions.jsonl")
```

### Method 3: From Text Editor

1. Open text editor (VS Code, Notepad++, etc.)
2. Type one JSON object per line
3. Save with `.jsonl` extension
4. Ensure UTF-8 encoding

**Example content:**
```jsonl
{"id": "q-001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter"}
{"id": "q-002", "topic": "Functions", "question": "How do you define a function?", "style": "short_question", "difficulty": "starter"}
```

---

## 🧪 Testing Your File

Before uploading to Hugging Face, test locally:

```bash
# Navigate to QuestionForge directory
cd D:\claude-projects\question-forge

# Test your file
py main.py analyze your_questions.jsonl
```

**Expected output:**
- ✅ "Loaded X questions"
- ✅ Quality scores for each criteria
- ✅ No validation errors

**If you see errors:**
- Check field names match exactly (case-sensitive)
- Verify style and difficulty values are valid
- Ensure JSON is properly formatted
- Check for encoding issues (use UTF-8)

---

## ❌ Common Mistakes & How to Fix

### Mistake 1: Using Regular JSON Instead of JSONL

**Wrong:**
```json
[
  {"id": "q-001", "question": "..."},
  {"id": "q-002", "question": "..."}
]
```

**Correct:**
```jsonl
{"id": "q-001", "question": "..."}
{"id": "q-002", "question": "..."}
```

**Fix:** Remove the outer array `[...]` and commas between objects.

---

### Mistake 2: Keywords as String Instead of Array

**Wrong:**
```json
{"keywords": "variable, syntax, basics"}
```

**Correct:**
```json
{"keywords": ["variable", "syntax", "basics"]}
```

**Fix:** Use square brackets and quotes around each keyword.

---

### Mistake 3: Invalid Style Value

**Wrong:**
```json
{"style": "multiple_choice"}
```

**Correct:**
```json
{"style": "short_question"}
```

**Fix:** Use one of the 9 accepted style values.

---

### Mistake 4: Invalid Difficulty Value

**Wrong:**
```json
{"difficulty": "easy"}
```

**Correct:**
```json
{"difficulty": "starter"}
```

**Fix:** Use starter, core, or stretch only.

---

### Mistake 5: Missing Required Fields

**Wrong:**
```json
{"id": "q-001", "question": "What is a variable?"}
```

**Correct:**
```json
{
  "id": "q-001",
  "topic": "Python Basics",
  "question": "What is a variable?",
  "style": "short_question",
  "difficulty": "starter"
}
```

**Fix:** Include all 5 required fields.

---

### Mistake 6: Encoding Issues (Special Characters)

**Problem:** File has characters like é, ñ, ü that show as �

**Fix:**
1. Save file with UTF-8 encoding
2. In Python:
   ```python
   with open('questions.jsonl', 'w', encoding='utf-8') as f:
       # Write questions
   ```
3. In text editor: Save As → Encoding: UTF-8

---

### Mistake 7: Code Context Not Escaped

**Wrong:**
```json
{"code_context": "x = 5\nprint(x)"}
```
(Newline not escaped)

**Correct:**
```json
{"code_context": "x = 5\\nprint(x)"}
```
OR use JSON properly:
```python
q = {"code_context": "x = 5\nprint(x)"}  # Python handles escaping
json.dump(q, f)  # Outputs properly escaped
```

---

## 📊 File Structure Examples

### Example 1: Minimal Starter Questions (20 questions)

```jsonl
{"id": "q-001", "topic": "Python Basics", "question": "What keyword defines a function?", "style": "single_word", "difficulty": "starter"}
{"id": "q-002", "topic": "Python Basics", "question": "How do you create a comment in Python?", "style": "short_question", "difficulty": "starter"}
{"id": "q-003", "topic": "Data Types", "question": "What is the difference between list and tuple?", "style": "compare_contrast", "difficulty": "starter"}
...
```

### Example 2: Complete Core Questions (10 questions)

```jsonl
{"id": "q-101", "topic": "Functions", "subtopics": ["parameters", "arguments"], "question": "What is the difference between *args and **kwargs in Python?", "style": "explain_concept", "difficulty": "core", "bloom_level": "understand", "keywords": ["args", "kwargs", "parameters", "variable arguments"], "prerequisites": ["q-001"], "code_context": "def func(*args, **kwargs):\n    pass"}
{"id": "q-102", "topic": "OOP", "subtopics": ["classes", "methods"], "question": "Write a class Dog with a method bark() that prints 'Woof!'", "style": "scenario_task", "difficulty": "core", "bloom_level": "apply", "keywords": ["class", "method", "OOP", "instance"], "prerequisites": ["q-050"], "code_context": ""}
...
```

### Example 3: Advanced Stretch Questions (5 questions)

```jsonl
{"id": "q-201", "topic": "Performance", "subtopics": ["optimization", "complexity"], "question": "Why might using a generator expression be more memory-efficient than a list comprehension for large datasets?", "style": "explain_concept", "difficulty": "stretch", "bloom_level": "analyze", "keywords": ["generator", "list comprehension", "memory", "lazy evaluation", "performance"], "prerequisites": ["q-150", "q-151"], "code_context": "# List comprehension\nsquares = [x**2 for x in range(1000000)]\n\n# Generator expression\nsquares_gen = (x**2 for x in range(1000000))"}
...
```

---

## 🎯 Best Practices

### 1. Question IDs
- Use consistent naming: `q-001`, `q-002`, OR `q-py-001`, `q-py-002`
- Make them sequential and meaningful
- Include topic prefix if managing multiple subjects: `q-py-001`, `q-js-001`

### 2. Keywords
- Include 3-5 relevant keywords per question
- Use terms that learners would search for
- Include synonyms and related concepts
- Example: `["function", "def", "syntax", "define", "declaration"]`

### 3. Subtopics
- Use 1-3 specific subtopics
- More specific than main topic
- Example: Topic="Functions", Subtopics=`["parameters", "return values"]`

### 4. Question Text
- Be clear and specific
- Use complete sentences
- Include context if needed
- Avoid ambiguity

### 5. Code Context
- Provide code snippets when relevant
- Keep code concise and focused
- Use proper escaping for special characters
- Example:
  ```json
  {"code_context": "def add(a, b):\\n    return a + b"}
  ```

---

## 🚀 Quick Start: Upload to QuestionForge

### Step 1: Prepare Your File
1. Create JSONL file with questions
2. Validate using checklist above
3. Test locally (optional): `py main.py analyze your_questions.jsonl`

### Step 2: Upload to Hugging Face
1. Go to your QuestionForge Space
2. Click "Analyze Questions" tab
3. Upload your `.jsonl` file
4. Click "Analyze Quality"

### Step 3: Review Results
- View 7-criteria quality scores
- Check for validation warnings
- Review detailed analysis per question

### Step 4: Refine (if needed)
1. Switch to "Refine Questions" tab
2. Upload your file
3. Set target threshold (default: 4.8/5.0)
4. Click "Refine Questions"
5. Download improved version

---

## 📞 Need Help?

### Resources:
- **Quick Conversion Guide:** `DATABASE_TO_JSONL_QUICKSTART.md`
- **Comprehensive Guide:** `CONVERSION_GUIDE.md`
- **Testing Guide:** `QUICK_START.md`
- **Example Files:** `examples/` folder

### Troubleshooting:
- File won't parse → Check JSON syntax with online validator
- Validation errors → Review "Valid Values" section above
- Encoding issues → Ensure UTF-8 encoding
- Size too large → Split into multiple files (<10MB each)

### Testing Locally:
```bash
cd D:\claude-projects\question-forge
py main.py analyze your_questions.jsonl
```

---

## ✅ Summary: File Format Requirements

**Format:** JSONL (JSON Lines)
- One JSON object per line
- No commas between lines
- UTF-8 encoding
- `.jsonl` file extension

**Required Fields (5):**
- `id` (string)
- `topic` (string)
- `question` (string)
- `style` (string - one of 9 values)
- `difficulty` (string - one of 3 values)

**Recommended Fields:**
- `bloom_level` (string - one of 6 values)
- `keywords` (array)
- `subtopics` (array)
- `prerequisites` (array)
- `code_context` (string)

**Valid Values:**
- **Style:** single_word, short_question, predict_output, debug_fix, scenario_task, fill_in_blank, explain_concept, compare_contrast, rewrite
- **Difficulty:** starter, core, stretch
- **Bloom Level:** remember, understand, apply, analyze, evaluate, create

---

**Your questions are ready for QuestionForge when all items in the validation checklist are checked!** ✨

---

**"Small fixes, big clarity"** - Start with the right format for best results! 🔥
