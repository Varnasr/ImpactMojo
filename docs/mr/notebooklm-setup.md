# NotebookLM सेटअप

[notebooklm-py](https://github.com/teng-lin/notebooklm-py) वापरून ImpactMojo च्या 12 AI Study Companion notebooks चे प्रोग्रामॅटिक व्यवस्थापन.

## इन्स्टॉलेशन

```bash
pip install -r requirements.txt
playwright install chromium
```

## प्रमाणीकरण

एक-वेळचा सेटअप — Google OAuth साठी एक ब्राउझर उघडतो:

```bash
notebooklm login
```

11 course notebooks ज्या Google अकाउंटच्या मालकीची आहेत तेच अकाउंट वापरा. क्रेडेन्शियल्स स्थानिक पातळीवर साठवली जातात आणि कधीही कमिट केली जात नाहीत.

याने पडताळणी करा:

```bash
notebooklm status
```

## वापर

### व्यवस्थापन स्क्रिप्ट

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

### CLI (notebooklm-py अंतर्भूत)

```bash
notebooklm list                          # List all notebooks
notebooklm sources list <notebook-id>    # List sources in a notebook
notebooklm ask <notebook-id> "question"  # Ask a question
notebooklm audio <notebook-id>           # Generate audio overview
```

## Registry

`data/notebooklm-registry.json` हे course slugs ला notebook IDs शी मॅप करते. ऑटोमेशनसाठी हे सत्याचे एकमेव स्रोत आहे — notebook IDs course HTML पानांमध्येही एम्बेड केलेले असतात, पण स्क्रिप्ट्स जे वाचतात ते registry च असते.

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

## मर्यादा

- **अनधिकृत API** — अदस्तऐवजीकृत Google APIs वापरते ज्या पूर्वसूचनेशिवाय बंद पडू शकतात
- **इंटरॅक्टिव्ह प्रमाणीकरण** — `notebooklm login` ला ब्राउझरची आवश्यकता असते, CI/headless मध्ये चालू शकत नाही
- **प्रति-मशीन क्रेडेन्शियल्स** — auth tokens स्थानिक पातळीवर साठवले जातात, repo मध्ये नाही
- **दर मर्यादा** — Google विनंत्या थ्रॉटल करू शकते; जलद-गती ऑपरेशन्स टाळा
