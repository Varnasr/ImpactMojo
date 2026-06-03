# टायपोग्राफी

## फॉन्ट स्टॅक

ImpactMojo सर्व 242+ पृष्ठांवर एक प्रमाणित तीन-फॉन्ट प्रणाली वापरते:

| भूमिका | फॉन्ट | वजने | फॉलबॅक |
|------|------|---------|----------|
| **शीर्षके** | Inter | 400, 500, 600, 700, 800 | sans-serif |
| **मुख्य मजकूर** | Amaranth | 400, 700 | sans-serif |
| **कोड / monospace** | JetBrains Mono | 400 | monospace |
| **बहुभाषिक** | Noto Sans (देवनागरी, बंगाली, तमिळ, तेलुगू) | 400, 700 | sans-serif |

## Google Fonts लोडिंग

सर्व पृष्ठे एकाच Google Fonts URL द्वारे फॉन्ट लोड करतात:

```html
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono&family=Noto+Sans:wght@400;700&display=swap" rel="stylesheet">
```

## डिझाइन टोकन

### फॉन्ट कुटुंबे

```css
--font-heading: 'Inter', sans-serif;
--font-body: 'Amaranth', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

### फॉन्ट आकार

| टोकन | आकार | वापर |
|-------|------|-------|
| `--text-xs` | 0.75rem | लेबल, मथळे |
| `--text-sm` | 0.875rem | दुय्यम मजकूर, मेटाडेटा |
| `--text-base` | 1rem | मुख्य मजकूर |
| `--text-lg` | 1.125rem | लीड परिच्छेद |
| `--text-xl` | 1.25rem | विभाग शीर्षके (h3) |
| `--text-2xl` | 1.5rem | पृष्ठ शीर्षके (h2) |
| `--text-3xl` | 1.875rem | हिरो शीर्षके (h1) |

### फॉन्ट वजने

| टोकन | वजन | वापर |
|-------|--------|-------|
| `--font-normal` | 400 | मुख्य मजकूर |
| `--font-medium` | 500 | नेव्हिगेशन, बटणे |
| `--font-semibold` | 600 | उपशीर्षके |
| `--font-bold` | 700 | शीर्षके, भर |
| `--font-extrabold` | 800 | हिरो मजकूर |

## एन्कोडिंग

सर्व HTML फायली UTF-8 एन्कोडिंग वापरतात:

```html
<meta charset="UTF-8">
```

हे खालील गोष्टींचे योग्य रेंडरिंग सुनिश्चित करते:
- हिंदी (हिन्दी), बंगाली (বাংলা), तमिळ (தமிழ்), तेलुगू (తెలుగు)
- शैक्षणिक मजकुरातील विशेष अक्षरे (em-dashes, smart quotes, इ.)

## मागील फॉन्ट (v10.0.0 मध्ये काढले)

v10.0.0 टायपोग्राफी प्रमाणीकरणादरम्यान खालील फॉन्ट काढून टाकले गेले:

- Poppins (शीर्षकांसाठी Inter ने बदलले)
- Fraunces (काढले)
- Merriweather (काढले)
- Source Serif 4 (काढले)
- Source Sans 3 (काढले)
- Cormorant Garamond (काढले)
- Georgia (फॉलबॅक साखळ्यांमधून काढले)
