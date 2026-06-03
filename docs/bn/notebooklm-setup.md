# NotebookLM সেটআপ

[notebooklm-py](https://github.com/teng-lin/notebooklm-py) ব্যবহার করে ImpactMojo-র 12টি AI Study Companion notebooks-এর প্রোগ্রাম্যাটিক ব্যবস্থাপনা।

## ইনস্টলেশন

```bash
pip install -r requirements.txt
playwright install chromium
```

## প্রমাণীকরণ (Authentication)

একবারের সেটআপ — Google OAuth-এর জন্য একটি ব্রাউজার খোলে:

```bash
notebooklm login
```

11টি course notebooks-এর মালিক Google অ্যাকাউন্ট ব্যবহার করুন। ক্রেডেনশিয়াল স্থানীয়ভাবে সংরক্ষিত হয় এবং কখনও commit করা হয় না।

যাচাই করুন:

```bash
notebooklm status
```

## ব্যবহার

### Management script

```bash
# Check auth status
python3 scripts/notebooklm-manage.py status

# List all notebooks with registry cross-reference
python3 scripts/notebooklm-manage.py list

# Sync registry titles from live API
python3 scripts/notebooklm-manage.py sync-registry

# Add a reading/URL to a course notebook
python3 scripts/notebooklm-manage.py add-source devecon https://example.com/paper.pdf

# Generate audio overview for a course
python3 scripts/notebooklm-manage.py generate-audio gandhi
```

### CLI (notebooklm-py built-in)

```bash
notebooklm list                          # List all notebooks
notebooklm sources list <notebook-id>    # List sources in a notebook
notebooklm ask <notebook-id> "question"  # Ask a question
notebooklm audio <notebook-id>           # Generate audio overview
```

## Registry

`data/notebooklm-registry.json` course slug-গুলিকে notebook ID-এর সাথে মানচিত্রিত করে। এটি অটোমেশনের জন্য একমাত্র সত্যের উৎস — notebook ID-গুলি course HTML পৃষ্ঠাগুলিতেও এম্বেড করা থাকে, কিন্তু scripts যা পড়ে তা হল registry।

## Course notebooks

| Slug | Course |
|------|--------|
| sel | Social and Emotional Learning 101 |
| dataviz | Data Visualization 101 |
| devai | Development & AI 101 |
| devecon | Development Economics 101 |
| gandhi | Gandhi & Nonviolence 101 |
| gender | Gender & Equity 101 |
| law | Law & Justice 101 |
| media | Media & Information 101 |
| mel | MEAL 101 |
| poa | Policy & Advocacy 101 |
| pubpol | Public Policy 101 |

## সীমাবদ্ধতা

- **অনানুষ্ঠানিক API** — অবিজ্ঞপ্ত Google APIs ব্যবহার করে যা পূর্বঘোষণা ছাড়াই ভেঙে যেতে পারে
- **ইন্টারঅ্যাক্টিভ auth** — `notebooklm login`-এর জন্য একটি ব্রাউজার প্রয়োজন, CI/headless-এ চলতে পারে না
- **প্রতি-মেশিন ক্রেডেনশিয়াল** — auth token স্থানীয়ভাবে সংরক্ষিত হয়, repo-তে নয়
- **Rate limits** — Google অনুরোধ থ্রটল করতে পারে; দ্রুত-পরপর অপারেশন এড়িয়ে চলুন
