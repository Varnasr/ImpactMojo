# टाइपोग्राफी

## फॉन्ट स्टैक

ImpactMojo सभी 242+ पृष्ठों पर एक मानकीकृत तीन-फॉन्ट प्रणाली का उपयोग करता है:

| भूमिका | फॉन्ट | वज़न | फॉलबैक |
|------|------|---------|----------|
| **शीर्षक** | Inter | 400, 500, 600, 700, 800 | sans-serif |
| **मुख्य पाठ** | Amaranth | 400, 700 | sans-serif |
| **कोड / मोनोस्पेस** | JetBrains Mono | 400 | monospace |
| **बहुभाषी** | Noto Sans (देवनागरी, बंगाली, तमिल, तेलुगु) | 400, 700 | sans-serif |

## Google Fonts लोडिंग

सभी पृष्ठ एक ही Google Fonts URL के माध्यम से फॉन्ट लोड करते हैं:

```html
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono&family=Noto+Sans:wght@400;700&display=swap" rel="stylesheet">
```

## डिज़ाइन टोकन

### फॉन्ट परिवार

```css
--font-heading: 'Inter', sans-serif;
--font-body: 'Amaranth', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

### फॉन्ट आकार

| टोकन | आकार | उपयोग |
|-------|------|-------|
| `--text-xs` | 0.75rem | लेबल, कैप्शन |
| `--text-sm` | 0.875rem | द्वितीयक पाठ, मेटाडेटा |
| `--text-base` | 1rem | मुख्य पाठ |
| `--text-lg` | 1.125rem | लीड पैराग्राफ |
| `--text-xl` | 1.25rem | अनुभाग शीर्षक (h3) |
| `--text-2xl` | 1.5rem | पृष्ठ शीर्षक (h2) |
| `--text-3xl` | 1.875rem | हीरो शीर्षक (h1) |

### फॉन्ट वज़न

| टोकन | वज़न | उपयोग |
|-------|--------|-------|
| `--font-normal` | 400 | मुख्य पाठ |
| `--font-medium` | 500 | नेविगेशन, बटन |
| `--font-semibold` | 600 | उपशीर्षक |
| `--font-bold` | 700 | शीर्षक, ज़ोर |
| `--font-extrabold` | 800 | हीरो पाठ |

## एन्कोडिंग

सभी HTML फ़ाइलें UTF-8 एन्कोडिंग का उपयोग करती हैं:

```html
<meta charset="UTF-8">
```

यह निम्नलिखित के सही रेंडरिंग को सुनिश्चित करता है:
- हिन्दी (हिन्दी), बंगाली (বাংলা), तमिल (தமிழ்), तेलुगु (తెలుగు)
- शैक्षणिक सामग्री में विशेष वर्ण (em-dashes, smart quotes, आदि)

## पिछले फॉन्ट (v10.0.0 में हटाए गए)

v10.0.0 टाइपोग्राफी मानकीकरण के दौरान निम्नलिखित फॉन्ट हटा दिए गए:

- Poppins (शीर्षकों के लिए Inter से प्रतिस्थापित)
- Fraunces (हटाया गया)
- Merriweather (हटाया गया)
- Source Serif 4 (हटाया गया)
- Source Sans 3 (हटाया गया)
- Cormorant Garamond (हटाया गया)
- Georgia (फॉलबैक श्रृंखलाओं से हटाया गया)
