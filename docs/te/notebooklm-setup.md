# NotebookLM సెటప్

[notebooklm-py](https://github.com/teng-lin/notebooklm-py) ఉపయోగించి ImpactMojo యొక్క 12 AI అధ్యయన సహచర నోట్‌బుక్‌ల ప్రోగ్రామాటిక్ నిర్వహణ.

## ఇన్‌స్టాలేషన్

```bash
pip install -r requirements.txt
playwright install chromium
```

## ప్రామాణీకరణ

ఒక-సారి సెటప్ — Google OAuth కోసం ఒక బ్రౌజర్‌ను తెరుస్తుంది:

```bash
notebooklm login
```

11 కోర్సు నోట్‌బుక్‌లను కలిగి ఉన్న Google ఖాతాను ఉపయోగించండి. ఆధారాలు స్థానికంగా నిల్వ చేయబడతాయి మరియు ఎప్పుడూ కమిట్ చేయబడవు.

దీనితో ధృవీకరించండి:

```bash
notebooklm status
```

## వినియోగం

### నిర్వహణ స్క్రిప్ట్

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

### CLI (notebooklm-py అంతర్నిర్మిత)

```bash
notebooklm list                          # List all notebooks
notebooklm sources list <notebook-id>    # List sources in a notebook
notebooklm ask <notebook-id> "question"  # Ask a question
notebooklm audio <notebook-id>           # Generate audio overview
```

## రిజిస్ట్రీ

`data/notebooklm-registry.json` కోర్సు స్లగ్‌లను నోట్‌బుక్ IDలకు మ్యాప్ చేస్తుంది. ఇది ఆటోమేషన్ కోసం సత్యం యొక్క ఏకైక మూలం — నోట్‌బుక్ IDలు కోర్సు HTML పేజీలలో కూడా పొందుపరచబడ్డాయి, కానీ స్క్రిప్ట్‌లు చదివేది రిజిస్ట్రీ.

## కోర్సు నోట్‌బుక్‌లు

| స్లగ్ | కోర్సు |
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

## పరిమితులు

- **అనధికారిక API** — నోటీసు లేకుండా విఫలం కావచ్చే డాక్యుమెంట్ చేయని Google APIలను ఉపయోగిస్తుంది
- **ఇంటరాక్టివ్ ప్రామాణీకరణ** — `notebooklm login` కు ఒక బ్రౌజర్ అవసరం, CI/హెడ్‌లెస్‌లో నడవదు
- **యంత్రం-వారీ ఆధారాలు** — ప్రామాణీకరణ టోకెన్లు రిపోలో కాదు, స్థానికంగా నిల్వ చేయబడతాయి
- **రేట్ పరిమితులు** — Google అభ్యర్థనలను నియంత్రించవచ్చు; వేగవంతమైన కార్యకలాపాలను నివారించండి
