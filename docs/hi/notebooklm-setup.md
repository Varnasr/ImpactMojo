# NotebookLM सेटअप

[notebooklm-py](https://github.com/teng-lin/notebooklm-py) का उपयोग करके ImpactMojo के 12 AI Study Companion notebooks का प्रोग्रामेटिक प्रबंधन।

## इंस्टॉलेशन

```bash
pip install -r requirements.txt
playwright install chromium
```

## प्रमाणीकरण

एक-बार का सेटअप — Google OAuth के लिए एक ब्राउज़र खोलता है:

```bash
notebooklm login
```

उसी Google अकाउंट का उपयोग करें जिसके पास 11 course notebooks का स्वामित्व है। क्रेडेंशियल्स स्थानीय रूप से संग्रहीत होते हैं और कभी कमिट नहीं किए जाते।

इससे सत्यापित करें:

```bash
notebooklm status
```

## उपयोग

### प्रबंधन स्क्रिप्ट

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

### CLI (notebooklm-py अंतर्निहित)

```bash
notebooklm list                          # List all notebooks
notebooklm sources list <notebook-id>    # List sources in a notebook
notebooklm ask <notebook-id> "question"  # Ask a question
notebooklm audio <notebook-id>           # Generate audio overview
```

## Registry

`data/notebooklm-registry.json` course slugs को notebook IDs से मैप करता है। यह ऑटोमेशन के लिए सत्य का एकमात्र स्रोत है — notebook IDs course HTML पेजों में भी एम्बेड किए गए हैं, लेकिन स्क्रिप्ट्स जो पढ़ती हैं वह registry ही है।

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

## सीमाएँ

- **अनौपचारिक API** — अप्रलेखित Google APIs का उपयोग करता है जो बिना सूचना के टूट सकती हैं
- **इंटरैक्टिव प्रमाणीकरण** — `notebooklm login` को एक ब्राउज़र की आवश्यकता होती है, CI/headless में नहीं चल सकता
- **प्रति-मशीन क्रेडेंशियल्स** — auth tokens स्थानीय रूप से संग्रहीत होते हैं, repo में नहीं
- **दर सीमाएँ** — Google अनुरोधों को थ्रॉटल कर सकता है; तेज़-तर्रार ऑपरेशन से बचें
