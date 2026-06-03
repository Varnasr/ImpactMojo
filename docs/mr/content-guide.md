# आशय मार्गदर्शक

हे पान ImpactMojo मध्ये शैक्षणिक आशय कसा संरचित केला जातो याचे दस्तऐवजीकरण करते, जे अभ्यासक्रम, labs, games, आणि संसाधने जोडू किंवा सुधारू इच्छिणाऱ्या योगदानकर्त्यांसाठी आहे.

## आशय प्रकार

| प्रकार | संख्या | स्वरूप | प्रवेश |
|------|-------|--------|--------|
| Flagship Courses | 11 | बहु-module (प्रत्येकी १२–१३ modules) | मोफत |
| Foundational Courses | 38 | एक-पान किंवा बहु-विभाग | मोफत |
| Interactive Labs | 11 | HTML/JS workbenches | मोफत |
| Learning Games | 16 | HTML/JS simulations | मोफत |
| Premium Tools | 9 | स्वतंत्र Netlify साइट्स | सशुल्क tiers |
| ImpactLex | 390+ संज्ञा | PWA शब्दकोश | मोफत |
| Dev Case Studies | 200 | निवडक ग्रंथालय | मोफत |
| DevDiscourses | 500+ | निवडक papers/पुस्तके | मोफत |
| Handouts | 400+ | HTML pages | मोफत |
| BookSummaries | 28 | परस्परसंवादी पुस्तक साथी | मोफत (Specials) |
| Deep Dives | 5 | निवडक भाष्ययुक्त वाचन सूची | मोफत (Specials) |
| 101 Course Decks | 38 | 4 native HTML (100 slides) + 34 Gamma presentations | मोफत |
| Blog posts | सुरू | HTML लेख | मोफत |
| Podcast | Episodes | Audio (Spotify) | मोफत |

## Learning Tracks

आशय ६ tracks मध्ये संघटित केला आहे:

1. **MEL & Research** — Monitoring, evaluation, गुणात्मक/परिमाणात्मक पद्धती
2. **Economics & Policy** — Development economics, political economy, fundraising
3. **Gender & Equity** — Gender studies, WEE, care economy, data feminism
4. **Governance & Society** — Constitution, decolonization, community development
5. **Health & Wellbeing** — Public health, climate, SEL, livelihoods
6. **Communication & Data** — Data literacy, visual ethnography, BCC, advocacy

## Flagship Course रचना

प्रत्येक flagship अभ्यासक्रम एका सुसंगत रचनेचे अनुसरण करतो:

- **13 modules** (अंदाजे)
- ५०–६५ मुख्य संज्ञांचा **Lexicon**
- **दक्षिण आशियाई संदर्भ** — भारत, बांगलादेश, नेपाळ, श्रीलंका मधील उदाहरणे
- **केस स्टडीज** — वास्तविक विकास कार्यक्रम आणि मूल्यांकने
- **Reflection prompts** — व्यावसायिकांना त्यांच्या कामाशी जोडण्यासाठी
- **पुढील वाचन** — DevDiscourses मधून निवडलेले

### उदाहरण: MEL for Development
```
Module 1:  What is MEL?
Module 2:  Theories of Change
Module 3:  Indicators & Frameworks
Module 4:  Data Collection Methods
...
Module 13: MEL for Learning & Adaptation
Lexicon:   65 terms with definitions
```

## Interactive Labs

Labs ही HTML/JS workbenches आहेत जी व्यावसायिकांना संकल्पना लागू करू देतात. प्रत्येक lab:

- एक मार्गदर्शित workflow (टप्प्याटप्प्याने) असते
- एक output तयार करते (framework, plan, analysis)
- परिणाम export करू शकते (प्रीमियम आवृत्त्यांमध्ये PDF/PNG)
- कोणत्याही serverची गरज नसते — संपूर्णपणे browserमध्ये चालते

## Learning Games

Games ही एका HTML page म्हणून तयार केलेली economics simulations आहेत:

- **स्वयंपूर्ण** — प्रत्येक game ही एक HTML फाइल आहे
- **डेटा-चालित** — शक्य असेल तिथे वास्तविक आर्थिक मापदंड
- **Debriefable** — वर्ग किंवा कार्यशाळा वापरासाठी रचलेली
- **मोबाइल-अनुकूल** — प्रतिसादात्मक layouts

## नवीन आशय जोडणे

### नवीन foundational अभ्यासक्रम जोडणे

1. विद्यमान course pattern चे अनुसरण करून एक नवीन HTML फाइल तयार करा
2. `catalog.html` मधील catalog मध्ये अभ्यासक्रम जोडा
3. `index.html` मधील मुख्य साइटच्या course listing मध्ये तो जोडा
4. README आशय यादी अद्ययावत करा

### नवीन game जोडणे

1. game logic सह एक एकल HTML फाइल तयार करा
2. योग्य directory मध्ये किंवा स्वतंत्र Netlify साइट म्हणून ती host करा
3. `index.html` आणि `catalog.html` मधील games विभागात ती जोडा

### Handouts जोडणे

Handouts repo मधून गतिशीलपणे लोड केले जातात. handouts संग्रहात HTML फाइल्स जोडा आणि त्या आपोआप दिसतील.

## बहुभाषिक आशय

आशय ६ भाषांत उपलब्ध आहे:
- English (प्राथमिक)
- Hindi
- Tamil
- Bengali
- Telugu
- Marathi

भाषांतर योगदानांचे स्वागत आहे. मार्गदर्शक तत्त्वांसाठी [Contributing](Contributing) पाहा.

## शैली मार्गदर्शक

- **सूर:** सुलभ पण काटेकोर. २–३ वर्षांचा अनुभव असलेल्या व्यावसायिकासाठी लिहा.
- **उदाहरणे:** दक्षिण आशियाई संदर्भ (भारत, बांगलादेश, नेपाळ, श्रीलंका) प्राधान्याने वापरा.
- **जार्गन:** पहिल्या वापरात संज्ञांची व्याख्या करा. क्षेत्र-प्रमाणित असल्यास ImpactLex मध्ये जोडा.
- **श्रेय:** स्रोतांचा उल्लेख करा. शक्य असेल तिथे DevDiscourses ला लिंक करा.
- **Accessibility:** semantic HTML, प्रतिमांसाठी alt text, पुरेसा रंग कॉन्ट्रास्ट वापरा.

## Deep Dive कसा लिहावा

Deep Dives ही निवडक भाष्ययुक्त वाचन सूची आहेत. प्रत्येक सूची ही एका नावाने ओळखल्या जाणाऱ्या curator च्या आवाजासह एक संपादकीय कलाकृती असते, तटस्थ ग्रंथसूची नव्हे — एका स्वतंत्र references पानापेक्षा long-form निबंध-स्वरूपी-अभ्यासक्रमाच्या जवळची.

### Deep Dive ची रचना

1. **Hero** — शीर्षक, एका ओळीची tagline, topic chip, वाचनांची संख्या.
2. **Curator card** — नाव, भूमिका, २–३ वाक्यांचे bio. `Editor's Pick` (अंतर्गत) किंवा `Invited Curator` म्हणून चिन्हांकित करा.
3. **Editor's Note** — curator च्या आवाजातील २–४ परिच्छेदांचा framing निबंध. हाच मुख्य गाभा आहे; सूची ही पावती आहे.
4. **३–६ विषयाधारित विभाग** — उदा. "Foundations", "Recent Debates", "Voices from the Field". सपाट सूची करू नका.
5. **वाचन आयटम** — प्रत्येकासाठी: एक type badge (📘 Book / 📄 Paper / 🎙 Podcast / 🎬 Film / 📊 Dataset / 📰 Article / 🌐 Web), outbound link सह संपूर्ण citation, आणि ती कृती का महत्त्वाची आहे व ती अभ्यासक्रमात कशी बसते हे सांगणारे २–४ वाक्यांचे भाष्य.
6. **संबंधित ImpactMojo आशय** — २–४ अभ्यासक्रम, labs, games, किंवा book companions ना cross-link करा.
7. **सुचवलेले citation** — APA-शैलीचा citation block.
8. **Contribute CTA** — pitch फॉर्मला लिंक.

### तयार करायच्या / अद्ययावत करायच्या फाइल्स

नवीन Deep Dive जोडण्यासाठी:

1. `/DeepDives/_template.html` → `/DeepDives/{slug}.html` कॉपी करा. शीर्षक, tagline, topic, curator, editor's note, विभाग, वाचने भरा.
2. `/data/deep-dives.json` मध्ये एक नोंद जोडा (id, title, tagline, topic, url, curator, sections, tags, reading_count, published).
3. `/data/search-index.json` मध्ये `"type": "deep-dive"` आणि `"category": "Deep Dives"` सह एक नोंद जोडा.
4. `/sitemap.xml` मध्ये एक `<url>` नोंद जोडा.
5. `catalog.html` च्या `allContent` array मध्ये एक card जोडा (`type: 'deep-dive'`, एक track निवडा).
6. (पर्यायी) flagship-दर्जाचे असल्यास `/index.html` मधील Deep Dives विभाग संपादित करून मुख्यपृष्ठावर वैशिष्ट्यीकृत करा.
7. सर्वत्र count मजकूर अद्ययावत करा — `(5 Deep Dives|5 readings)` साठी grep करा आणि संख्या वाढवा.

### संपादकीय मार्गदर्शक तत्त्वे

- **तटस्थतेपेक्षा curator चा आवाज.** दृष्टिकोनाशिवायची सूची ही केवळ ग्रंथसूची आहे. वाचकाच्या हातात तुम्ही काय देऊ इच्छिता आणि का ते सांगा.
- **मिश्र माध्यमांना प्रोत्साहन.** एका चांगल्या Deep Dive मध्ये academic गाभ्यासोबत किमान एक podcast, एक dataset, आणि एक व्यावसायिक-केंद्रित स्रोत असतो.
- **भाष्य करा, सारांश नको.** दोन ते चार वाक्ये. ही कृती का, आता का, कोणी वाचावी.
- **उदारपणे cross-link करा.** "Related ImpactMojo Content" block वापरून वाचकांना सूचीवर आधारित अभ्यासक्रम, labs, आणि book companions कडे पाठवा.
- **व्याप्तीत राहा.** प्रत्येक Deep Dive हा एक सुसंगत विषय आहे — संपूर्ण क्षेत्र समाविष्ट करण्याचा प्रयत्न करू नका.
