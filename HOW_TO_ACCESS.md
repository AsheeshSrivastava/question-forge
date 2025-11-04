# How to Access QuestionForge v2.0

**Quick Answer:** Open your terminal and run commands from the QuestionForge directory!

---

## 🎯 3 Simple Steps to Get Started

### Step 1: Open Your Terminal

**Windows:**
- Press `Win + R`
- Type `cmd` or `powershell`
- Press Enter

**OR** Use Windows Terminal (recommended):
- Press `Win + X`
- Select "Windows Terminal"

---

### Step 2: Navigate to QuestionForge

**Copy and paste this command:**

```bash
cd D:\claude-projects\question-forge
```

**Press Enter**

✅ **You're now in the QuestionForge directory!**

---

### Step 3: Run QuestionForge

**Try this command:**

```bash
py main.py version
```

**You should see:**
```
🔥 QuestionForge v2.0.0
"Small fixes, big clarity" - Quest & Crossfire

✨ Enhanced with Academic + Industry Standards
7-Criteria Scoring | CMU, Wiggins & McTighe, AWS, NCCA, ISO

Built by Asheesh for Aethelgard Academy
```

🎉 **Congratulations! QuestionForge is running!**

---

## ✅ First-Time Setup (Do This Once)

If this is your first time using QuestionForge, you need to install dependencies:

```bash
# Make sure you're in the QuestionForge directory
cd D:\claude-projects\question-forge

# Install dependencies
pip install -r requirements.txt
```

**Wait 1-2 minutes while packages install...**

✅ **Setup complete! You're ready to use QuestionForge.**

---

## 🚀 Your First Analysis (30 Seconds)

Let's test QuestionForge with sample questions:

**1. Make sure you're in the right directory:**
```bash
cd D:\claude-projects\question-forge
```

**2. Run analysis on test questions:**
```bash
py main.py analyze test_questions.jsonl
```

**3. Watch the magic happen!** ✨

You'll see:
- ✓ Loaded 10 questions
- Progress bar
- Quality distribution table
- Average scores
- Recommendations

---

## 📖 Common Commands

Once you're in the QuestionForge directory (`D:\claude-projects\question-forge`), use these commands:

### See Available Commands
```bash
py main.py --help
```

### Check Version
```bash
py main.py version
```

### Analyze Questions
```bash
py main.py analyze YOUR_FILE.jsonl
```

### Refine Questions
```bash
py main.py refine YOUR_FILE.jsonl --output refined.jsonl
```

### Generate Report
```bash
py main.py report original.jsonl refined.jsonl --html
```

---

## 🗂️ File Locations

**QuestionForge Application:**
```
D:\claude-projects\question-forge\
```

**Your Questions Should Be:**
- In the same directory: `D:\claude-projects\question-forge\YOUR_QUESTIONS.jsonl`
- OR specify full path: `py main.py analyze "C:\My Questions\questions.jsonl"`

**Sample Questions (for testing):**
```
D:\claude-projects\question-forge\test_questions.jsonl
```

**Configuration:**
```
D:\claude-projects\question-forge\config.yaml
```

---

## 💡 Quick Tips

**Tip 1: Stay in the Directory**
- Always run commands from `D:\claude-projects\question-forge`
- If you're not sure where you are, type: `cd` (shows current directory)

**Tip 2: Use Tab Completion**
- Type `py main.py ana` then press TAB
- It will auto-complete to `py main.py analyze`

**Tip 3: Copy File Paths Easily**
- Drag and drop your JSONL file into the terminal
- The full path will be pasted automatically

**Tip 4: Check Your Python**
- If `py` doesn't work, try `python` or `python3`
- Check version: `python --version` (need 3.7+)

---

## 🔧 If Something Goes Wrong

### "py is not recognized"
**Problem:** Python not in PATH

**Solution 1:** Use full path
```bash
python main.py version
# or
python3 main.py version
```

**Solution 2:** Reinstall Python and check "Add to PATH" during installation

---

### "No module named 'yaml'" or similar
**Problem:** Dependencies not installed

**Solution:**
```bash
cd D:\claude-projects\question-forge
pip install -r requirements.txt
```

---

### "FileNotFoundError: test_questions.jsonl"
**Problem:** You're in the wrong directory

**Solution:**
```bash
# Navigate to correct directory
cd D:\claude-projects\question-forge

# Verify you're in the right place
dir
# You should see: main.py, config.yaml, test_questions.jsonl
```

---

### Command prompt shows weird characters instead of emojis
**Problem:** Windows console encoding

**Solution:** This is fixed in v2.0, but if you still see it:
- Use Windows Terminal (modern, supports emojis)
- Or run: `chcp 65001` before using QuestionForge

---

## 📱 Using QuestionForge from Anywhere

Want to run QuestionForge from any directory? Here's how:

### Option 1: Always CD First (Recommended)
```bash
cd D:\claude-projects\question-forge
py main.py analyze "C:\My Documents\my_questions.jsonl"
```

### Option 2: Use Full Path
```bash
py "D:\claude-projects\question-forge\main.py" analyze "C:\My Documents\my_questions.jsonl"
```

### Option 3: Add to PATH (Advanced)
- Add `D:\claude-projects\question-forge` to your system PATH
- Then you can run `questionforge` from anywhere
- See Windows documentation for adding to PATH

---

## 🎓 Complete Example Session

Let me walk you through a complete session, start to finish:

```bash
# 1. Open Terminal (Win + X → Windows Terminal)

# 2. Go to QuestionForge directory
cd D:\claude-projects\question-forge

# 3. Check if it works
py main.py version
# ✅ Shows: QuestionForge v2.0.0

# 4. Analyze test questions
py main.py analyze test_questions.jsonl
# ✅ Shows: Quality analysis with scores

# 5. Refine questions
py main.py refine test_questions.jsonl --output my_refined.jsonl
# ✅ Creates: my_refined.jsonl with improved questions

# 6. Generate HTML report
py main.py report test_questions.jsonl my_refined.jsonl --html
# ✅ Creates: report.html

# 7. Open report in browser
start report.html
# ✅ Opens: Beautiful HTML report showing improvements

# 8. Celebrate! 🎉
```

**Total Time:** 5 minutes
**Difficulty:** Easy!

---

## 📚 What's in the QuestionForge Directory?

When you run `dir` in the QuestionForge directory, you'll see:

```
D:\claude-projects\question-forge\
├── main.py                    # Main application (run this!)
├── config.yaml                # Configuration file
├── requirements.txt           # Dependencies list
├── test_questions.jsonl      # Sample questions (for testing)
├── refiner/                  # Core scoring engine
│   ├── analyzer.py           # 7-criteria scoring
│   ├── transformers.py       # Refinement strategies
│   └── ...
├── README.md                 # Overview
├── QUICK_START.md           # This guide!
├── USAGE_GUIDE.md           # Detailed usage
├── VALIDATION_FRAMEWORK.md  # Standards documentation
└── ... (more docs)
```

**Files you'll interact with:**
- `main.py` - Run this to use QuestionForge
- `config.yaml` - Customize settings (optional)
- `test_questions.jsonl` - Sample questions to practice with
- `YOUR_QUESTIONS.jsonl` - Your actual questions (you create this)

---

## ✅ Checklist: Am I Ready?

Before using QuestionForge on your real questions, verify:

- ✅ I can navigate to `D:\claude-projects\question-forge`
- ✅ I can run `py main.py version` and see v2.0.0
- ✅ I can run `py main.py analyze test_questions.jsonl` successfully
- ✅ I have my questions in JSONL format (or know how to create them)
- ✅ I understand the basic commands (analyze, refine, report)

**All checked?** You're ready to use QuestionForge! 🚀

---

## 🎯 Your Action Plan

**Right Now (5 minutes):**
1. Open terminal
2. Run: `cd D:\claude-projects\question-forge`
3. Run: `py main.py analyze test_questions.jsonl`
4. See it work!

**Next (30 minutes):**
1. Read QUICK_START.md for detailed usage
2. Prepare your questions in JSONL format
3. Run analysis on your questions
4. Review scores and understand criteria

**Later (ongoing):**
1. Refine questions to 4.8/5 quality
2. Generate reports for stakeholders
3. Track quality improvements over time
4. Explore advanced features (custom transformers, etc.)

---

## 📞 Need More Help?

**Documentation:**
- **QUICK_START.md** - Detailed getting started guide (you're here!)
- **README.md** - Feature overview
- **USAGE_GUIDE.md** - Comprehensive examples
- **SCOPE_ANALYSIS.md** - What can/cannot be done

**Support:**
- Check existing documentation first
- Review troubleshooting section above
- Contact Quest & Crossfire Arsenal

---

**You're all set! Open that terminal and give it a try! 🔥**

```bash
cd D:\claude-projects\question-forge
py main.py version
```

**Let's make those questions flagship quality! 💯**
