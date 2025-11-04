# QuestionForge Quick Reference

**"Small fixes, big clarity"** - Quest & Crossfire

## Commands

```bash
# Analyze quality
python main.py analyze questions.jsonl

# Refine (automatic)
python main.py refine questions.jsonl -o refined.jsonl

# Refine (interactive)
python main.py refine questions.jsonl -o refined.jsonl --interactive

# Generate report
python main.py report original.jsonl refined.jsonl

# Generate HTML report
python main.py report original.jsonl refined.jsonl --html

# Version info
python main.py version
```

## Scoring Criteria (5.0 scale)

| Criterion | Weight | What It Measures |
|-----------|--------|------------------|
| **Adult Learning** | 25% | Real-world context, practical examples |
| **People-First** | 20% | Inclusive language, diverse names |
| **Bloom's Taxonomy** | 20% | Cognitive level alignment |
| **Practical Application** | 20% | Tools, frameworks, job relevance |
| **RAG Optimization** | 15% | Keywords, searchability |

**Target:** 4.8/5.0 for flagship quality

## Quality Tiers

| Tier | Score Range | Status |
|------|-------------|--------|
| Excellent | ≥4.8 | ✅ Ready for production |
| Very Good | 4.5-4.7 | 🟡 Minor polish needed |
| Good | 4.0-4.4 | 🟡 Refinement recommended |
| Adequate | 3.5-3.9 | ⚠️ Needs work |
| Needs Work | 3.0-3.4 | ❌ Major issues |
| Poor | <3.0 | ❌ Critical problems |

## Transformation Strategies

1. **Expand Single-Word** (+0.5-1.5)
   - "indentation" → Full question about Python's block structure

2. **Replace Abstract Variables** (+0.3-0.9)
   - x, y, foo → price, quantity, username

3. **Diversify Names** (+0.2-0.6)
   - Alice, Bob → Priya, Chen, Amara

4. **Add Real-World Context** (+0.4-1.0)
   - Abstract scenario → Business/industry use case

5. **Fix Bloom's Alignment** (+0.2-0.4)
   - Match cognitive level to difficulty tier

6. **Enhance Keywords** (+0.1-0.3)
   - Expand metadata for better search

## Typical Refinement Path

```
Round 1: 3.5 → 3.8 (+0.3)  [Fix major issues]
Round 2: 3.8 → 4.2 (+0.4)  [Additional improvements]
Round 3: 4.2 → 4.6 (+0.4)  [Polish]
Round 4: 4.6 → 4.8+ (+0.2+) [Final push to threshold]
```

## Common Issues & Fixes

| Issue | Score Impact | Solution |
|-------|--------------|----------|
| Single-word question | -1.5 | Expand to full question |
| Abstract variables (x, y) | -0.9 | Use realistic names |
| Western-only names | -0.6 | Use diverse global names |
| Wrong Bloom's level | -0.4 | Align with difficulty |
| < 5 keywords | -0.3 | Enhance metadata |

## Best Practices

✅ **DO:**
- Run multiple refinement rounds
- Backup original files first
- Use `--interactive` for critical content
- Validate with reports after refinement
- Customize `config.yaml` for your domain

❌ **DON'T:**
- Overwrite originals without backup
- Expect 4.8+ in one round
- Skip validation after refinement
- Ignore refinement_history metadata

## File Structure

```
question-forge/
├── main.py              # CLI entry point
├── config.yaml          # Scoring & transformation config
├── requirements.txt     # Dependencies
├── README.md            # Project overview
├── USAGE_GUIDE.md       # Full documentation
├── QUICK_REFERENCE.md   # This file
└── refiner/
    ├── __init__.py
    ├── parser.py        # JSONL parsing
    ├── analyzer.py      # Quality scoring
    ├── transformers.py  # Refinement strategies
    ├── validators.py    # Threshold validation
    ├── rag_optimizer.py # Search optimization
    └── reporters.py     # Report generation
```

## Quest & Crossfire Principles

| Principle | Implementation |
|-----------|----------------|
| **Small fixes** | One transformation per question per run |
| **Big clarity** | Transparent scoring, detailed history |
| **Systematic** | Repeatable, data-driven process |
| **Reflective** | Tracks all changes, enables rollback |
| **Honest** | Real scores, no grade inflation |

## Windows Users

If you see emoji encoding errors:

```bash
# Use 'py' launcher instead of 'python'
py main.py analyze questions.jsonl

# Encoding fix is built into main.py v1.0+
```

## Integration Example

```python
from refiner import QuestionParser, QuestionAnalyzer, QuestionTransformer

# Load questions
questions = QuestionParser.parse_jsonl("questions.jsonl")

# Analyze
analyzer = QuestionAnalyzer()
for q in questions:
    scores = analyzer.analyze(q)
    print(f"{q.id}: {scores['overall']}/5.0")

# Transform
transformer = QuestionTransformer()
for i, q in enumerate(questions):
    if scores['overall'] < 4.8:
        transformed, strategy, improvement = transformer.transform(q)
        questions[i] = transformed

# Save
QuestionParser.save_jsonl(questions, "refined.jsonl")
```

## Support

- 📖 **Full Guide:** See `USAGE_GUIDE.md`
- 🐛 **Issues:** GitHub Issues
- 💡 **Philosophy:** Quest & Crossfire Arsenal - "Small fixes, big clarity"

---

**Built with ◇ by Quest & Crossfire**
