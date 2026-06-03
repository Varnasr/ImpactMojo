# ImpactMojo में योगदान देना

योगदान देने में आपकी रुचि के लिए धन्यवाद! ImpactMojo विकास समुदाय द्वारा और उसके लिए बनाया गया है। चाहे आप एक व्यवसायी हों जिसने एक पुराना आँकड़ा देखा हो, एक शिक्षक हों जिसके पास एक बेहतरीन केस स्टडी हो, या एक डेवलपर हों जो किसी बग को ठीक कर सकता हो — आपके योगदान का एक सार्थक तरीका मौजूद है।

## आपका तकनीकी होना ज़रूरी नहीं है

हमारे सबसे मूल्यवान योगदानों में से कई व्यवसायियों से आते हैं, प्रोग्रामर से नहीं। यहाँ बताया गया है कि आप कोड की एक भी पंक्ति लिखे बिना कैसे मदद कर सकते हैं:

| आप क्या कर सकते हैं | कैसे | कठिनाई |
|-----------------|-----|------------|
| **त्रुटि की रिपोर्ट करें** | टूटा हुआ लिंक, गलत आँकड़ा या पुराना संदर्भ मिला? एक [Content Issue](https://github.com/ImpactMojo/ImpactMojo/issues/new?template=content_issue.md) खोलें | बहुत आसान |
| **विषय सुझाएँ** | कोई ऐसा विषय जानते हैं जिसे कवर किया जाना चाहिए? एक [Discussion](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) शुरू करें | बहुत आसान |
| **केस स्टडी साझा करें** | आपके काम से कोई वास्तविक विकास केस स्टडी है? हमें hello@impactmojo.in पर ईमेल करें | आसान |
| **कंटेंट का अनुवाद करें** | कोर्स को हिंदी, तमिल, बांग्ला, तेलुगु या मराठी में उपलब्ध कराने में मदद करें | आसान–मध्यम |
| **कंटेंट की समीक्षा करें** | क्या आप MEL, जेंडर अध्ययन या विकास अर्थशास्त्र के विशेषज्ञ हैं? सटीकता के लिए कोर्स की समीक्षा में हमारी मदद करें | आसान |
| **हैंडआउट लिखें** | किसी ऐसे विषय पर संदर्भ शीट बनाएँ जिसे आप अच्छी तरह जानते हैं | मध्यम |

## तकनीकी योगदानकर्ताओं के लिए

यदि आप HTML, CSS या JavaScript के साथ सहज हैं, तो योगदान देने के कई तरीके हैं:

| क्षेत्र | उदाहरण | कठिनाई |
|------|----------|------------|
| **बग फिक्स** | टूटे लिंक, लेआउट समस्याएँ, JavaScript त्रुटियाँ | आसान–मध्यम |
| **सुगम्यता** | WCAG अनुपालन, स्क्रीन रीडर समर्थन, कीबोर्ड नेविगेशन | मध्यम |
| **डिज़ाइन** | UI/UX सुधार, मोबाइल अनुभव | मध्यम |
| **Tools & Labs** | इंटरैक्टिव लर्निंग टूल बनाएँ या सुधारें | कठिन |
| **गेम** | नए अर्थशास्त्र सिमुलेशन | मध्यम–कठिन |

### शुरुआत करना (तकनीकी)

ImpactMojo एक वैनिला HTML/CSS/JS प्रोजेक्ट है — कोई फ्रेमवर्क नहीं, कोई बिल्ड स्टेप नहीं। आप इसे केवल एक वेब ब्राउज़र और एक साधारण सर्वर के साथ स्थानीय रूप से चला सकते हैं:

```bash
# 1. Fork and clone the repository
git clone https://github.com/<your-username>/ImpactMojo.git
cd ImpactMojo

# 2. Start a local server (pick whichever you have)
python -m http.server 8000
# or: npx http-server -p 8080

# 3. Open http://localhost:8000 in your browser

# 4. Create a branch for your changes
git checkout -b feature/your-feature-name

# 5. Make your changes, test locally

# 6. Commit using the prefix convention
git commit -m "Add: descriptive summary of what you did"

# 7. Push and open a Pull Request on GitHub
git push origin feature/your-feature-name
```

### कमिट संदेश परिपाटी

प्रत्येक कमिट संदेश एक उपसर्ग से शुरू होता है जो परिवर्तन के प्रकार का वर्णन करता है:

| उपसर्ग | कब उपयोग करें | उदाहरण |
|--------|---------------|---------|
| `Add:` | नई सुविधा, कोर्स या टूल | `Add: interactive budget planning lab` |
| `Fix:` | बग फिक्स या टूटा लिंक | `Fix: broken nav dropdown on mobile Safari` |
| `Update:` | मौजूदा कंटेंट या कोड में सुधार | `Update: MEL course module 3 with 2025 data` |
| `Translate:` | अनुवाद कार्य | `Translate: gender studies course to Hindi` |
| `Docs:` | दस्तावेज़ परिवर्तन | `Docs: add workshop facilitation guide` |
| `Refactor:` | कोड पुनर्गठन (कोई व्यवहार परिवर्तन नहीं) | `Refactor: extract auth logic to separate file` |
| `Test:` | टेस्ट जोड़ना या अपडेट करना | `Test: add accessibility checks for games` |
| `CI:` | CI/CD पाइपलाइन परिवर्तन | `CI: add broken link checker workflow` |
| `Chore:` | रखरखाव (निर्भरताएँ, कॉन्फ़िग) | `Chore: update dependabot config` |

### Pull Request दिशानिर्देश

- PR को केंद्रित रखें — प्रति PR एक सुविधा या फिक्स
- डेस्कटॉप और मोबाइल पर परीक्षण करें
- दृश्य परिवर्तनों के लिए स्क्रीनशॉट शामिल करें
- ध्यान दें यदि परिवर्तन premium सुविधाओं को प्रभावित करते हैं

## कंटेंट लेखन शैली

यदि आप शैक्षिक कंटेंट में योगदान दे रहे हैं, तो हम जो लक्ष्य रखते हैं वह यहाँ है:

- **टोन:** सुलभ परंतु कठोर। 2–3 वर्ष के अनुभव वाले व्यवसायी के लिए लिखें।
- **उदाहरण:** दक्षिण एशियाई संदर्भ को प्राथमिकता दें (भारत, बांग्लादेश, नेपाल, श्रीलंका)।
- **शब्दजाल:** पहली बार उपयोग पर शब्दों को परिभाषित करें। यदि यह एक सामान्य सेक्टर शब्द है, तो इसे [ImpactLex](https://www.impactmojo.in/impactlex/) में जोड़ें।
- **श्रेय:** हमेशा स्रोतों का उल्लेख करें। जहाँ संभव हो [DevDiscourses](https://www.impactmojo.in/dataverse) से लिंक करें।
- **सुगम्यता:** स्पष्ट शीर्षकों, छवियों के लिए alt text, और पर्याप्त रंग कंट्रास्ट का उपयोग करें।

## समस्याओं की रिपोर्ट करना

उपयुक्त टेम्पलेट के साथ [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) का उपयोग करें:

- **Bug Report** — कुछ टूटा हुआ है (लिंक, लेआउट, त्रुटि)
- **Feature Request** — एक नया विचार या सुधार
- **Content Issue** — तथ्यात्मक त्रुटि, पुरानी जानकारी, गायब विषय

## समुदाय चैनल

- [WhatsApp PLC](https://chat.whatsapp.com/EsBjbKaQfupG1HbtajTjHM) — व्यवसायियों के बीच सहकर्मी चर्चाएँ
- [Discord](https://discord.gg/M3ZCmUe7ab) — तकनीकी चर्चाएँ और प्रयोग
- [Telegram](https://t.me/impactmojo) — निःशुल्क संसाधन और अपडेट
- [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions) — विचार, प्रश्नोत्तर और घोषणाएँ
- **ईमेल:** hello@impactmojo.in — किसी भी अन्य चीज़ के लिए
