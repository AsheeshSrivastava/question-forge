# QuestionForge - File Format Quick Reference Card

**One-page guide for uploading questions**

---

## ✅ File Requirements

| Requirement | Value |
|-------------|-------|
| **Format** | JSONL (JSON Lines) |
| **Extension** | `.jsonl` |
| **Encoding** | UTF-8 |
| **Structure** | One JSON object per line |
| **Size Limit** | <10 MB recommended |

---

## 📝 Minimal Valid Question

```json
{"id": "q-001", "topic": "Python Basics", "question": "What is a variable?", "style": "short_question", "difficulty": "starter"}
```

**Required fields:** `id`, `topic`, `question`, `style`, `difficulty`

---

## 🎨 Valid Values

### Style (pick one):
```
single_word | short_question | predict_output | debug_fix |
scenario_task | fill_in_blank | explain_concept |
compare_contrast | rewrite
```

### Difficulty (pick one):
```
starter | core | stretch
```

### Bloom Level - optional (pick one):
```
remember | understand | apply | analyze | evaluate | create
```

---

## ✨ Recommended Fields

```json
{
  "id": "q-001",
  "topic": "Functions",
  "subtopics": ["parameters", "return"],
  "question": "How do you define a function with default parameters?",
  "style": "short_question",
  "difficulty": "core",
  "bloom_level": "apply",
  "keywords": ["function", "parameters", "default", "def"],
  "prerequisites": [],
  "code_context": "def greet(name='World'):\n    return f'Hello {name}'"
}
```

---

## ⚠️ Common Mistakes

| Wrong | Correct |
|-------|---------|
| `"keywords": "var,syntax"` | `"keywords": ["var", "syntax"]` |
| `"style": "multiple_choice"` | `"style": "short_question"` |
| `"difficulty": "easy"` | `"difficulty": "starter"` |
| `[{...}, {...}]` (JSON array) | One object per line (JSONL) |

---

## 🧪 Quick Test

```bash
cd D:\claude-projects\question-forge
py main.py analyze your_file.jsonl
```

Expected: "✓ Loaded X questions"

---

## 📚 Full Documentation

- **Complete Guide:** `USER_GUIDE_FILE_FORMAT.md`
- **Conversion Help:** `DATABASE_TO_JSONL_QUICKSTART.md`
- **Examples:** `examples/` folder
- **Test Files:** `test_starter_questions.jsonl` (see format)

---

## ✅ Pre-Upload Checklist

- [ ] File ends with `.jsonl`
- [ ] One JSON object per line (no commas between)
- [ ] All 5 required fields present
- [ ] Style value is valid (one of 9)
- [ ] Difficulty value is valid (one of 3)
- [ ] Keywords/subtopics are arrays, not strings
- [ ] File saved as UTF-8

**Ready to upload!** 🚀
