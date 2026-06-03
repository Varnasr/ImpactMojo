# NotebookLM அமைப்பு

[notebooklm-py](https://github.com/teng-lin/notebooklm-py) பயன்படுத்தி ImpactMojo-வின் 12 AI Study Companion notebooks-ஐ நிரல்வழியில் நிர்வகித்தல்.

## நிறுவல்

```bash
pip install -r requirements.txt
playwright install chromium
```

## அங்கீகாரம் (Authentication)

ஒரு முறை அமைப்பு — Google OAuth-க்காக ஒரு உலாவியைத் திறக்கிறது:

```bash
notebooklm login
```

11 course notebooks-ஐ வைத்திருக்கும் Google கணக்கைப் பயன்படுத்தவும். சான்றுகள் உள்ளூரில் சேமிக்கப்படுகின்றன, ஒருபோதும் commit செய்யப்படுவதில்லை.

இதன் மூலம் சரிபார்க்கவும்:

```bash
notebooklm status
```

## பயன்பாடு

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

`data/notebooklm-registry.json` course slugs-ஐ notebook IDs-உடன் இணைக்கிறது. இது தானியக்கத்திற்கான ஒரே உண்மை மூலமாகும் — notebook IDs course HTML பக்கங்களிலும் உட்பொதிக்கப்பட்டுள்ளன, ஆனால் scripts படிப்பது registry-ஐயே.

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

## வரம்புகள்

- **அதிகாரப்பூர்வமற்ற API** — அறிவிப்பின்றி உடைந்து போகக்கூடிய ஆவணப்படுத்தப்படாத Google APIs-ஐப் பயன்படுத்துகிறது
- **ஊடாடும் auth** — `notebooklm login`-க்கு ஒரு உலாவி தேவை, CI/headless-இல் இயங்க முடியாது
- **ஒரு இயந்திரத்திற்கான சான்றுகள்** — auth tokens உள்ளூரில் சேமிக்கப்படுகின்றன, repo-வில் அல்ல
- **Rate limits** — Google கோரிக்கைகளைக் கட்டுப்படுத்தலாம்; விரைவான-தொடர் செயல்பாடுகளைத் தவிர்க்கவும்
