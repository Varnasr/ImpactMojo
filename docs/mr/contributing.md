# ImpactMojo मध्ये योगदान देणे

योगदान देण्यात तुम्ही दाखवलेल्या स्वारस्याबद्दल धन्यवाद! ImpactMojo हे विकास समुदायाद्वारे आणि त्यांच्यासाठी तयार केले आहे. तुम्ही एखादी कालबाह्य आकडेवारी लक्षात घेणारे व्यावसायिक असाल, उत्तम केस स्टडी असलेले शिक्षक असाल, किंवा बग दुरुस्त करू शकणारे डेव्हलपर असाल — तुमच्यासाठी योगदान देण्याचा एक अर्थपूर्ण मार्ग नक्की आहे.

## तुम्हाला तांत्रिक असण्याची गरज नाही

आमची सर्वात मौल्यवान योगदाने प्रोग्रामरकडून नव्हे तर अनेकदा व्यावसायिकांकडून येतात. कोडची एकही ओळ न लिहिता तुम्ही कशी मदत करू शकता ते येथे आहे:

| तुम्ही काय करू शकता | कसे | अडचण |
|-----------------|-----|------------|
| **त्रुटीची नोंद करा** | तुटलेली लिंक, चुकीची आकडेवारी, किंवा कालबाह्य संदर्भ सापडला? एक [Content Issue](https://github.com/ImpactMojo/ImpactMojo/issues/new?template=content_issue.md) उघडा | खूप सोपे |
| **एखादा विषय सुचवा** | समाविष्ट करायला हवा असा विषय माहीत आहे? एक [Discussion](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) सुरू करा | खूप सोपे |
| **केस स्टडी शेअर करा** | तुमच्या कामातील वास्तविक विकास केस स्टडी आहे? आम्हाला hello@impactmojo.in वर ईमेल करा | सोपे |
| **आशय भाषांतरित करा** | अभ्यासक्रम हिंदी, तमिळ, बंगाली, तेलुगू किंवा मराठीत उपलब्ध करून देण्यास मदत करा | सोपे–मध्यम |
| **आशयाचे पुनरावलोकन करा** | तुम्ही MEL, gender studies, किंवा development economics मधील तज्ज्ञ आहात? अचूकतेसाठी अभ्यासक्रमांचे पुनरावलोकन करण्यास आम्हाला मदत करा | सोपे |
| **हँडआउट लिहा** | तुम्हाला चांगल्या प्रकारे माहीत असलेल्या विषयावर एक संदर्भपत्रक तयार करा | मध्यम |

## तांत्रिक योगदानकर्त्यांसाठी

जर तुम्हाला HTML, CSS, किंवा JavaScript सोयीचे असेल, तर योगदान देण्याचे अनेक मार्ग आहेत:

| क्षेत्र | उदाहरणे | अडचण |
|------|----------|------------|
| **Bug fixes** | तुटलेल्या लिंक्स, layout अडचणी, JavaScript errors | सोपे–मध्यम |
| **Accessibility** | WCAG अनुपालन, screen reader समर्थन, keyboard navigation | मध्यम |
| **Design** | UI/UX सुधारणा, मोबाइल अनुभव | मध्यम |
| **Tools & Labs** | परस्परसंवादी शिक्षण साधने तयार करणे किंवा सुधारणे | कठीण |
| **Games** | नवीन economics simulations | मध्यम–कठीण |

### सुरुवात कशी करावी (तांत्रिक)

ImpactMojo हा एक vanilla HTML/CSS/JS प्रकल्प आहे — कोणत्याही frameworks नाहीत, build step नाही. तुम्ही फक्त एक web browser आणि एक साधा server वापरून तो स्थानिकरीत्या चालवू शकता:

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

### Commit संदेश संकेत

प्रत्येक commit संदेश बदलाचा प्रकार वर्णन करणाऱ्या एका prefixने सुरू होतो:

| Prefix | केव्हा वापरावा | उदाहरण |
|--------|---------------|---------|
| `Add:` | नवीन feature, course, किंवा tool | `Add: interactive budget planning lab` |
| `Fix:` | Bug fix किंवा तुटलेली लिंक | `Fix: broken nav dropdown on mobile Safari` |
| `Update:` | विद्यमान आशय किंवा कोडमध्ये सुधारणा | `Update: MEL course module 3 with 2025 data` |
| `Translate:` | भाषांतर कार्य | `Translate: gender studies course to Hindi` |
| `Docs:` | दस्तऐवजीकरण बदल | `Docs: add workshop facilitation guide` |
| `Refactor:` | कोड पुनर्रचना (वर्तनात बदल नाही) | `Refactor: extract auth logic to separate file` |
| `Test:` | tests जोडणे किंवा अद्ययावत करणे | `Test: add accessibility checks for games` |
| `CI:` | CI/CD pipeline बदल | `CI: add broken link checker workflow` |
| `Chore:` | देखभाल (dependencies, configs) | `Chore: update dependabot config` |

### Pull Request मार्गदर्शक तत्त्वे

- PR केंद्रित ठेवा — प्रति PR एक feature किंवा fix
- डेस्कटॉप आणि मोबाइलवर चाचणी करा
- दृश्यात्मक बदलांसाठी screenshots समाविष्ट करा
- बदल प्रीमियम features ला प्रभावित करत असल्यास नमूद करा

## आशय लेखन शैली

जर तुम्ही शैक्षणिक आशयात योगदान देत असाल, तर आम्ही ज्याचे लक्ष्य ठेवतो ते येथे आहे:

- **सूर:** सुलभ पण काटेकोर. २–३ वर्षांचा अनुभव असलेल्या व्यावसायिकासाठी लिहा.
- **उदाहरणे:** दक्षिण आशियाई संदर्भ (भारत, बांगलादेश, नेपाळ, श्रीलंका) प्राधान्याने वापरा.
- **जार्गन:** पहिल्या वापरात संज्ञांची व्याख्या करा. ती सर्वसामान्य क्षेत्रीय संज्ञा असल्यास, ती [ImpactLex](https://www.impactmojo.in/impactlex/) मध्ये जोडा.
- **श्रेय:** नेहमी स्रोतांचा उल्लेख करा. शक्य असेल तिथे [DevDiscourses](https://www.impactmojo.in/dataverse) ला लिंक करा.
- **Accessibility:** स्पष्ट headings, प्रतिमांसाठी alt text, आणि पुरेसा रंग कॉन्ट्रास्ट वापरा.

## अडचणींची नोंद करणे

योग्य template सह [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) वापरा:

- **Bug Report** — काहीतरी तुटले आहे (link, layout, error)
- **Feature Request** — नवीन कल्पना किंवा सुधारणा
- **Content Issue** — तथ्यात्मक त्रुटी, कालबाह्य माहिती, हरवलेला विषय

## समुदाय चॅनेल

- [WhatsApp PLC](https://chat.whatsapp.com/EsBjbKaQfupG1HbtajTjHM) — व्यावसायिकांमधील समवयस्क चर्चा
- [Discord](https://discord.gg/M3ZCmUe7ab) — तांत्रिक चर्चा आणि प्रयोग
- [Telegram](https://t.me/impactmojo) — मोफत संसाधने आणि अद्यतने
- [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions) — कल्पना, प्रश्नोत्तरे आणि घोषणा
- **Email:** hello@impactmojo.in — इतर कोणत्याही गोष्टीसाठी
