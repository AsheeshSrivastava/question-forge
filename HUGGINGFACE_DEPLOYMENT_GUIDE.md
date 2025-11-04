# QuestionForge v2.0 - Hugging Face Deployment Guide

**Deploy QuestionForge as a private web app on Hugging Face Spaces**

---

## 🎯 What You'll Get

After deployment, you'll have:
- ✅ **Web interface** - No CLI needed, use from any browser
- ✅ **Private space** - Only you can access it
- ✅ **File upload** - Drag and drop JSONL files
- ✅ **One-click analysis** - Instant quality scores
- ✅ **Auto-refinement** - Download improved questions
- ✅ **Before/after comparison** - Visual metrics
- ✅ **Always available** - Access from anywhere

---

## 📋 Prerequisites

Before you start:

1. **Hugging Face Account** (free)
   - Go to https://huggingface.co/join
   - Sign up for free account

2. **Git installed** (for uploading files)
   - Windows: Download from https://git-scm.com/
   - Or use Hugging Face web UI (simpler, no Git needed)

---

## 🚀 Deployment Method 1: Web UI (Easiest)

### Step 1: Create a New Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in details:
   - **Space name:** `questionforge-v2` (or your choice)
   - **License:** MIT
   - **SDK:** Gradio
   - **Visibility:** **Private** ✅ (IMPORTANT!)
   - Click **"Create Space"**

### Step 2: Upload Files

You need to upload these files from `D:\claude-projects\question-forge\`:

**Required files:**
1. `app.py` - Main web interface
2. `config.yaml` - Configuration
3. `requirements_huggingface.txt` - Rename to `requirements.txt`
4. `README_HUGGINGFACE.md` - Rename to `README.md`

**Required folders:**
5. `refiner/` - Complete folder with all Python files
   - `__init__.py`
   - `analyzer.py`
   - `parser.py`
   - `transformers.py`
   - `validators.py`
   - `reporters.py`
   - `rag_optimizer.py`

**How to upload:**

1. **In your Space page**, click **"Files"** tab
2. Click **"Add file"** → **"Upload files"**
3. **Drag and drop** or **browse** for files
4. Upload one by one or select multiple
5. Click **"Commit changes to main"**

**Important:** Rename these files when uploading:
- `requirements_huggingface.txt` → `requirements.txt`
- `README_HUGGINGFACE.md` → `README.md`

### Step 3: Wait for Build

- Hugging Face will automatically build your app (~2-3 minutes)
- You'll see build logs in the **"Logs"** tab
- When done, you'll see **"Running"** status

### Step 4: Access Your App

- Click the **"App"** tab
- Your private QuestionForge interface is ready! 🎉
- Bookmark the URL for easy access

---

## 🚀 Deployment Method 2: Git CLI (Advanced)

### Step 1: Create Space (same as above)

Follow Step 1 from Method 1 to create your Space.

### Step 2: Clone Space Repository

```bash
# Install Git LFS (for large files)
git lfs install

# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/questionforge-v2
cd questionforge-v2
```

### Step 3: Copy Files

```bash
# From your QuestionForge directory
cd D:\claude-projects\question-forge

# Copy files to Space directory
copy app.py C:\path\to\questionforge-v2\
copy config.yaml C:\path\to\questionforge-v2\
copy requirements_huggingface.txt C:\path\to\questionforge-v2\requirements.txt
copy README_HUGGINGFACE.md C:\path\to\questionforge-v2\README.md

# Copy refiner folder
xcopy /E /I refiner C:\path\to\questionforge-v2\refiner\
```

### Step 4: Commit and Push

```bash
cd C:\path\to\questionforge-v2

# Add files
git add .

# Commit
git commit -m "Deploy QuestionForge v2.0"

# Push to Hugging Face
git push
```

### Step 5: Wait for Build

- Go to your Space page on Hugging Face
- Wait for build to complete (~2-3 minutes)
- App will launch automatically

---

## 📁 Required File Structure

Your Hugging Face Space should have this structure:

```
questionforge-v2/
├── app.py                    # Main Gradio interface
├── config.yaml               # Configuration
├── requirements.txt          # Dependencies (renamed from requirements_huggingface.txt)
├── README.md                 # Space description (renamed from README_HUGGINGFACE.md)
├── refiner/                  # Core engine
│   ├── __init__.py
│   ├── analyzer.py
│   ├── parser.py
│   ├── transformers.py
│   ├── validators.py
│   ├── reporters.py
│   └── rag_optimizer.py
└── .gitattributes            # Auto-created by Hugging Face
```

---

## ✅ Verification Checklist

After deployment, verify everything works:

### Test 1: App Loads
- [ ] Go to your Space URL
- [ ] See QuestionForge interface with 4 tabs
- [ ] No error messages

### Test 2: Analyze Function
- [ ] Go to "Analyze Questions" tab
- [ ] Upload `test_questions.jsonl` from your local copy
- [ ] Click "Analyze Quality"
- [ ] See results table with scores

### Test 3: Refine Function
- [ ] Go to "Refine Questions" tab
- [ ] Upload `test_questions.jsonl`
- [ ] Click "Refine Questions"
- [ ] Download refined file
- [ ] Open and verify it's valid JSONL

### Test 4: Compare Function
- [ ] Go to "Before/After Comparison" tab
- [ ] Upload original and refined files
- [ ] Click "Generate Comparison"
- [ ] See before/after metrics

✅ **If all 4 tests pass, deployment is successful!**

---

## 🔒 Privacy Settings

Your Space is **private by default**, but verify:

1. Go to your Space page
2. Click **"Settings"**
3. Under **"Visibility"**, confirm it shows **"Private"**
4. **Who can access:**
   - ✅ You (owner)
   - ❌ Public (disabled)
   - Optional: Add specific users if needed

**Private means:**
- Only you see the app
- Questions you upload are not visible to others
- Processing happens in your isolated environment
- No public URL accessible

---

## 🐛 Troubleshooting

### Problem: "Building" status stuck for >5 minutes

**Solution:**
1. Check **"Logs"** tab for errors
2. Common issues:
   - Missing `requirements.txt` (must rename from `requirements_huggingface.txt`)
   - Missing `refiner/` folder files
   - Syntax error in `app.py`

**Fix:** Delete the Space and recreate, ensuring all files uploaded correctly

---

### Problem: "Error loading model" or import errors

**Solution:**
- Check `requirements.txt` exists and has correct content
- Verify all files from `refiner/` folder are present
- Check **"Logs"** for specific missing module

---

### Problem: File upload doesn't work

**Solution:**
- Verify file is valid JSONL format
- Check file size (<10MB for free tier)
- Try with `test_questions.jsonl` first to isolate issue

---

### Problem: "Too many requests" or slow performance

**Solution:**
- Hugging Face Spaces have rate limits on free tier
- Upgrade to Pro for better performance ($9/month)
- Or use during off-peak hours

---

## 💰 Costs

**Free Tier:**
- ✅ Perfect for personal use
- ✅ Private Spaces allowed
- ⚠️ May have queue during peak times
- ⚠️ Limited compute resources

**Pro Tier ($9/month):**
- ✅ Faster compute
- ✅ No queues
- ✅ Better uptime
- ✅ Recommended for production use

**For Your Use Case:** Free tier is sufficient for analyzing question banks occasionally.

---

## 🔄 Updating Your Deployment

### Method 1: Web UI

1. Go to your Space
2. Click **"Files"** tab
3. Click on file to edit (e.g., `app.py`)
4. Make changes
5. Click **"Commit changes"**
6. Space will rebuild automatically

### Method 2: Git CLI

```bash
cd C:\path\to\questionforge-v2

# Make changes to files

# Commit and push
git add .
git commit -m "Update to v2.0.1"
git push
```

---

## 📊 Usage Tips

### For Best Performance:

1. **Upload smaller batches**
   - Instead of 500 questions at once, do 50-100 at a time
   - Faster processing, less timeout risk

2. **Use during off-peak hours**
   - Free tier has better performance during nights/weekends (UTC)

3. **Download refined files immediately**
   - Files in temp storage may be cleared periodically

4. **Keep backups locally**
   - Always keep original questions on your computer

---

## 🎯 Example Workflow

Here's how to use your deployed QuestionForge:

### Scenario: You have 100 Python questions to refine

**Step 1: Access your Space**
```
https://huggingface.co/spaces/YOUR_USERNAME/questionforge-v2
```

**Step 2: Analyze**
1. Go to "Analyze Questions" tab
2. Upload `my_100_questions.jsonl`
3. Click "Analyze Quality"
4. Review: Average 3.8/5.0, 0 questions ≥4.8

**Step 3: Refine**
1. Go to "Refine Questions" tab
2. Upload `my_100_questions.jsonl`
3. Enable "Auto-apply improvements"
4. Click "Refine Questions"
5. Download `refined_questions.jsonl`

**Step 4: Compare**
1. Go to "Before/After Comparison" tab
2. Upload original and refined files
3. Click "Generate Comparison"
4. See improvement: 3.8 → 4.6 average

**Step 5: Review**
1. Open downloaded file locally
2. Manual review of refined questions
3. Make final edits if needed

**Time:** 10-15 minutes total for 100 questions! 🚀

---

## 🌟 Advanced Configuration

### Custom Thresholds

Edit `config.yaml` in your Space:

```yaml
scoring:
  threshold: 4.5  # Lower threshold (was 4.8)
  passing_score: 3.8
```

### Custom Templates

Add your own diverse names:

```yaml
templates:
  diverse_names:
    - Priya
    - Chen
    - YourName  # Add custom names
```

After editing, commit changes and Space will rebuild.

---

## 📞 Getting Help

**If deployment fails:**

1. **Check logs**
   - Go to Space → "Logs" tab
   - Look for error messages

2. **Common fixes:**
   - Rename `requirements_huggingface.txt` to `requirements.txt`
   - Ensure all `refiner/` files uploaded
   - Verify `app.py` has no syntax errors

3. **Test locally first:**
   ```bash
   cd D:\claude-projects\question-forge
   pip install gradio
   python app.py
   ```
   If it works locally, deployment should work

4. **Contact support:**
   - Hugging Face Community Forum
   - Quest & Crossfire Arsenal

---

## ✨ Success!

Once deployed, you have:

✅ **Professional web interface** - No CLI needed
✅ **Private and secure** - Your questions stay private
✅ **Always available** - Access from any device
✅ **Shareable** - Can add team members if needed
✅ **Free** - No hosting costs with free tier

**Bookmark your Space URL and start refining questions!** 🔥

---

## 📚 Next Steps

After deployment:

1. **Test with sample questions** - Verify everything works
2. **Analyze your real questions** - Get baseline scores
3. **Refine to 4.8/5** - Auto-improve quality
4. **Document improvements** - Generate reports for stakeholders
5. **Share with team** - Add collaborators if needed (Settings → Add user)

---

**Deployment Time:** 15-30 minutes
**Difficulty:** Easy (web UI) to Medium (Git CLI)
**Result:** Professional question quality assessment platform! 🎉

---

**"Small fixes, big clarity"** - Now available as a web app!
