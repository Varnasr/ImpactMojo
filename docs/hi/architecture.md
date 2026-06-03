# आर्किटेक्चर

> **यह पृष्ठ किसके लिए है?** यह पृष्ठ मुख्य रूप से डेवलपर्स और तकनीकी योगदानकर्ताओं के लिए है। यदि आप एक शिक्षक या प्रैक्टिशनर हैं, तो मुख्य बात नीचे "उपयोगकर्ताओं के लिए इसका क्या अर्थ है" खंड में है — आप तकनीकी विवरण छोड़ सकते हैं।

## उपयोगकर्ताओं के लिए इसका क्या अर्थ है

ImpactMojo दक्षिण एशिया के प्रैक्टिशनरों के लिए बनाया गया है, जिनमें से कई धीमे इंटरनेट कनेक्शन या पुराने उपकरणों पर हैं। हमारे तकनीकी विकल्पों का आपके अनुभव के लिए यह अर्थ है:

- **तेज़ लोडिंग** — साइट सरल, हल्के कोड से बनी है (कोई भारी फ्रेमवर्क नहीं)। 2G/3G कनेक्शन पर भी पृष्ठ जल्दी लोड होते हैं।
- **ऑफ़लाइन काम करता है** — एक बार जब आप किसी पृष्ठ पर जा चुके होते हैं, तो यह आपके उपकरण पर सहेज लिया जाता है। आप बिना इंटरनेट कनेक्शन के फ्लैगशिप पाठ्यक्रमों तक पहुँच सकते हैं।
- **कोई इंस्टॉलेशन की आवश्यकता नहीं** — सब कुछ आपके वेब ब्राउज़र में चलता है। डाउनलोड करने के लिए कोई ऐप नहीं, इंस्टॉल करने के लिए कोई सॉफ़्टवेयर नहीं।
- **आपका डेटा सुरक्षित है** — लॉगिन और खाता डेटा Supabase (एक विश्वसनीय डेटाबेस सेवा) द्वारा संभाला जाता है। प्रीमियम उपकरण समय-सीमित सुरक्षा टोकन का उपयोग करते हैं ताकि आपकी पहुँच चुराई न जा सके।
- **किसी भी उपकरण पर काम करता है** — फ़ोन, टैबलेट, लैपटॉप, डेस्कटॉप — पुराना या नया। हम जानबूझकर ऐसी तकनीकों से बचते हैं जिनके लिए आधुनिक हार्डवेयर की आवश्यकता होती है।

## तकनीकी अवलोकन

ImpactMojo एक स्टैटिक HTML/CSS/JS साइट है जिसमें कोई build step नहीं है, जिसके पीछे प्रमाणीकरण के लिए Supabase और होस्टिंग के लिए Netlify है। प्रीमियम उपकरण अलग Netlify साइटों के रूप में तैनात किए जाते हैं, जिनमें से प्रत्येक एक JWT auth-gate द्वारा सुरक्षित है।

## सिस्टम आरेख

```
┌──────────────────────────────────────────────────────────┐
│                    impactmojo.in                         │
│                  (Netlify — main site)                   │
│                                                          │
│  index.html ─── js/auth.js ──── Supabase Auth            │
│                 js/router.js    (login, signup, profiles) │
│                 js/premium.js                             │
│                 js/resource-launch.js                     │
└──────────┬───────────────────────────────────────────────┘
           │
           │ User clicks premium tool
           ▼
┌──────────────────────────────────────────────────────────┐
│        Supabase Edge Function                            │
│        mint-resource-token                               │
│                                                          │
│  1. Verify user session (access_token)                   │
│  2. Check subscription_tier in profiles table            │
│  3. Check subscription_status = 'active'                 │
│  4. Verify tier permits requested resource               │
│  5. Mint short-lived JWT (5 min, HMAC-SHA256)            │
└──────────┬───────────────────────────────────────────────┘
           │
           │ window.open(resourceUrl + '?token=...')
           ▼
┌──────────────────────────────────────────────────────────┐
│        Resource Site (private Netlify deployment)          │
│        Netlify Edge Function: auth-gate.ts               │
│                                                          │
│  1. Check for resource_session cookie                     │
│  2. If no cookie, check ?token= query parameter          │
│  3. Verify JWT signature (same HMAC secret)              │
│  4. Verify resource claim matches RESOURCE_ID            │
│  5. Set 24h session cookie, redirect to clean URL        │
│                                                          │
│  No cookie + no token → redirect to login                │
└──────────────────────────────────────────────────────────┘
```

## प्रमुख डिज़ाइन निर्णय

### कोई फ्रेमवर्क क्यों नहीं?

ImpactMojo दक्षिण एशिया के प्रैक्टिशनरों की सेवा करता है, जिनमें से कई कम-बैंडविड्थ कनेक्शन और पुराने उपकरणों पर हैं। एक वैनिला HTML/CSS/JS साइट:
- शून्य JS bundle ओवरहेड के साथ तेज़ी से लोड होती है
- बिना polyfills के किसी भी ब्राउज़र पर काम करती है
- बिना किसी build step के एक स्टैटिक साइट के रूप में परोसी जा सकती है
- समझना और योगदान देना आसान है

### प्रीमियम उपकरणों के लिए अलग Netlify साइटें क्यों?

प्रत्येक प्रीमियम उपकरण (VaniScribe, Qual Lab, आदि) स्वतंत्र रूप से बनाया गया था। उन्हें अलग साइटों के रूप में होस्ट करना:
- स्वतंत्र तैनाती और पुनरावृत्ति की अनुमति देता है
- विफलताओं को अलग करता है — एक उपकरण के बंद होने से दूसरों पर असर नहीं पड़ता
- JWT auth-gate को सरल बनाता है: प्रति साइट एक edge function
- विभिन्न टीमों को विभिन्न उपकरणों का स्वामित्व रखने देता है

### session-आधारित प्रमाणीकरण के बजाय JWT क्यों?

- **Stateless:** प्रत्येक resource साइट request पर कोई डेटाबेस lookup नहीं
- **Cross-domain:** मुख्य साइट और resource साइटें अलग-अलग डोमेन पर हैं
- **अल्पायु:** 5-मिनट के टोकन रोके जाने पर एक्सपोज़र को सीमित करते हैं
- **Session cookies:** प्रारंभिक JWT सत्यापन के बाद, एक 24h cookie पुनः-प्रमाणीकरण से बचाती है

### Supabase क्यों?

- मुफ़्त tier हमारी auth आवश्यकताओं को कवर करता है
- profiles के लिए अंतर्निहित Row Level Security
- serverless JWT minting के लिए Edge Functions
- संरचित डेटा के लिए PostgreSQL
- बॉक्स से बाहर Google OAuth + Magic Links

## पर्यावरण चर (Environment Variables)

### मुख्य साइट (impactmojo.in)
किसी server-side env vars की आवश्यकता नहीं — Supabase क्रेडेंशियल `js/auth.js` में हैं (केवल public anon key)।

### Supabase Edge Function (mint-resource-token)
| Variable | वर्णन |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | JWTs के लिए HMAC-SHA256 signing key |
| `SUPABASE_URL` | Supabase द्वारा स्वतः प्रदान |
| `SUPABASE_ANON_KEY` | Supabase द्वारा स्वतः प्रदान |
| `SUPABASE_SERVICE_ROLE_KEY` | स्वतः प्रदान; RLS को बायपास करते हुए profiles पढ़ता है |

### Resource Netlify साइटें (प्रति साइट)
| Variable | वर्णन |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | ऊपर जैसी ही HMAC key |
| `RESOURCE_ID` | अद्वितीय slug: `rq-builder`, `toc-workbench-pro`, `code-convert-pro`, `qual-insights`, `vaniscribe`, `devdata-practice`, `viz-cookbook`, `devecon-toolkit`, `field-notes-pro`, `toc-workshop-pro`, `logframe-pro`, `chart-selector-pro`, `stakeholder-pro`, `empathy-pro`, `policy-canvas-pro`, `ai-canvas-pro` |

## Tier Access Control

```
explorer:      []  (free content only)
practitioner:  [rq-builder, toc-workbench-pro]
professional:  [rq-builder, toc-workbench-pro, code-convert-pro, qual-insights, vaniscribe,
                devdata-practice, viz-cookbook, devecon-toolkit,
                toc-workshop-pro, logframe-pro, chart-selector-pro, stakeholder-pro,
                empathy-pro, policy-canvas-pro, ai-canvas-pro, field-notes-pro]
organization:  [same as professional]
```

## Supabase Database Tables

| Table | उद्देश्य |
|-------|---------|
| `profiles` | उपयोगकर्ता खाते, tier, streak, रुचियाँ |
| `user_progress` | प्रति-पाठ्यक्रम प्रगति ट्रैकिंग |
| `bookmarks` | उपयोगकर्ता बुकमार्क |
| `user_notes` | व्यक्तिगत नोट्स |
| `certificates` | badge metadata के साथ जारी किए गए प्रमाणपत्र |
| `payments` | भुगतान इतिहास |
| `coaching_bookings` | कोचिंग सत्र बुकिंग |
| `organizations` | संस्था रिकॉर्ड |
| `organization_members` | उपयोगकर्ता ↔ संस्था सदस्यता |
| `learning_paths` | कस्टम संस्था सीखने के मार्ग |
| `learning_path_assignments` | नियत तिथियों के साथ मार्ग ↔ उपयोगकर्ता असाइनमेंट |
| `portfolio_items` | उपयोगकर्ता पोर्टफोलियो प्रविष्टियाँ |
| `challenge_submissions` | लाइव केस चैलेंज सबमिशन |
| `challenge_requests` | संस्थाओं से कस्टम चैलेंज अनुरोध |
| `cohorts` | प्रारंभ/समाप्ति तिथियों के साथ प्रशिक्षण cohorts (v10.8.0) |
| `cohort_members` | Cohort नामांकन + प्रगति ट्रैकिंग (v10.8.0) |
| `cohort_discussions` | cohorts के भीतर चर्चा सूत्र (v10.8.0) |
| `notifications` | इन-ऐप + ईमेल सूचना लॉग (v10.8.0) |
| `notification_preferences` | प्रति-उपयोगकर्ता ईमेल opt-in/out (v10.8.0) |
| `course_content` | Edge Function के माध्यम से परोसा गया डायनेमिक पाठ्यक्रम HTML |
| `badge_shares` | Badge साझाकरण ट्रैकिंग |

## Supabase Edge Functions

| Function | उद्देश्य |
|----------|---------|
| `mint-resource-token` | प्रीमियम resource पहुँच के लिए JWT minting |
| `issue-certificate` | पाठ्यक्रम पूर्ण होने पर प्रमाणपत्र जारी करना |
| `game-agent` | खेलों के लिए MiroFish AI agent engine (multi-provider LLM) |
| `serve-course-content` | डायनेमिक पाठ्यक्रम आशय परोसना |
| `send-notification` | ईमेल सूचनाएँ: streak अनुस्मारक, cohort समयसीमा, मैनुअल (v10.8.0) |

## फ़ाइल संरचना

पूर्ण निर्देशिका लेआउट के लिए [README → Project Structure](https://github.com/ImpactMojo/ImpactMojo#project-structure) देखें।
