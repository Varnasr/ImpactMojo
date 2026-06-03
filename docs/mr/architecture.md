# आर्किटेक्चर

> **हे पृष्ठ कोणासाठी आहे?** हे पृष्ठ प्रामुख्याने डेव्हलपर आणि तांत्रिक योगदानकर्त्यांसाठी आहे. तुम्ही शिक्षक किंवा प्रॅक्टिशनर असाल, तर मुख्य मुद्दा खालील "वापरकर्त्यांसाठी याचा अर्थ काय" विभागात आहे — तुम्ही तांत्रिक तपशील वगळू शकता.

## वापरकर्त्यांसाठी याचा अर्थ काय

ImpactMojo दक्षिण आशियातील प्रॅक्टिशनरांसाठी तयार केले आहे, ज्यांच्यापैकी अनेक जण मंद इंटरनेट कनेक्शन किंवा जुन्या उपकरणांवर आहेत. आमच्या तांत्रिक निवडींचा तुमच्या अनुभवासाठी काय अर्थ आहे ते येथे आहे:

- **जलद लोडिंग** — साइट सोप्या, हलक्या कोडमध्ये बनवली आहे (कोणतेही जड frameworks नाहीत). 2G/3G कनेक्शनवरही पृष्ठे झटपट लोड होतात.
- **ऑफलाइन काम करते** — एकदा तुम्ही एखादे पृष्ठ भेट दिल्यानंतर, ते तुमच्या उपकरणावर जतन होते. तुम्ही इंटरनेट कनेक्शनशिवाय फ्लॅगशिप अभ्यासक्रम वापरू शकता.
- **कोणत्याही इन्स्टॉलेशनची गरज नाही** — सर्व काही तुमच्या वेब ब्राउझरमध्ये चालते. डाउनलोड करण्यासाठी कोणतेही ॲप नाही, इन्स्टॉल करण्यासाठी कोणतेही सॉफ्टवेअर नाही.
- **तुमचा डेटा सुरक्षित आहे** — लॉगिन आणि खाते डेटा Supabase (एक विश्वसनीय डेटाबेस सेवा) द्वारे हाताळला जातो. प्रीमियम साधने वेळ-मर्यादित सुरक्षा tokens वापरतात त्यामुळे तुमचा प्रवेश चोरला जाऊ शकत नाही.
- **कोणत्याही उपकरणावर काम करते** — फोन, टॅब्लेट, लॅपटॉप, डेस्कटॉप — जुने किंवा नवे. आधुनिक हार्डवेअरची गरज असणारी तंत्रज्ञाने आम्ही जाणीवपूर्वक टाळतो.

## तांत्रिक आढावा

ImpactMojo ही कोणताही build step नसलेली static HTML/CSS/JS साइट आहे, जिच्यामागे प्रमाणीकरणासाठी Supabase आणि होस्टिंगसाठी Netlify आहे. प्रीमियम साधने स्वतंत्र Netlify साइट्स म्हणून तैनात केली जातात, प्रत्येक एका JWT auth-gate ने संरक्षित आहे.

## सिस्टीम आकृती

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

## प्रमुख डिझाइन निर्णय

### framework का नाही?

ImpactMojo दक्षिण आशियातील प्रॅक्टिशनरांना सेवा देते, ज्यांच्यापैकी अनेक जण कमी-बँडविड्थ कनेक्शन आणि जुन्या उपकरणांवर आहेत. एक vanilla HTML/CSS/JS साइट:
- शून्य JS bundle ओव्हरहेडसह जलद लोड होते
- polyfills शिवाय कोणत्याही ब्राउझरवर काम करते
- कोणत्याही build step शिवाय static साइट म्हणून दिली जाऊ शकते
- समजायला आणि योगदान द्यायला सोपी आहे

### प्रीमियम साधनांसाठी स्वतंत्र Netlify साइट्स का?

प्रत्येक प्रीमियम साधन (VaniScribe, Qual Lab, इत्यादी) स्वतंत्रपणे बनवले गेले होते. त्यांना स्वतंत्र साइट्स म्हणून होस्ट करणे:
- स्वतंत्र तैनाती आणि पुनरावृत्तीला परवानगी देते
- अपयश वेगळे करते — एक साधन बंद पडल्याने इतरांवर परिणाम होत नाही
- JWT auth-gate सोपे करते: प्रति साइट एक edge function
- वेगवेगळ्या संघांना वेगवेगळी साधने सांभाळू देते

### session-आधारित प्रमाणीकरणाऐवजी JWT का?

- **Stateless:** प्रत्येक resource साइट request वर कोणताही डेटाबेस lookup नाही
- **Cross-domain:** मुख्य साइट आणि resource साइट्स वेगवेगळ्या डोमेनवर आहेत
- **अल्पायुषी:** 5-मिनिटांचे tokens अडवले गेल्यास एक्सपोजर मर्यादित करतात
- **Session cookies:** प्रारंभिक JWT पडताळणीनंतर, 24h cookie पुन्हा-प्रमाणीकरण टाळते

### Supabase का?

- मोफत tier आमच्या auth गरजा पूर्ण करते
- profiles साठी अंगभूत Row Level Security
- serverless JWT minting साठी Edge Functions
- संरचित डेटासाठी PostgreSQL
- थेट उपलब्ध Google OAuth + Magic Links

## पर्यावरण व्हेरिएबल (Environment Variables)

### मुख्य साइट (impactmojo.in)
कोणत्याही server-side env vars ची गरज नाही — Supabase क्रेडेन्शियल्स `js/auth.js` मध्ये आहेत (फक्त public anon key).

### Supabase Edge Function (mint-resource-token)
| Variable | वर्णन |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | JWTs साठी HMAC-SHA256 signing key |
| `SUPABASE_URL` | Supabase द्वारे आपोआप पुरवले जाते |
| `SUPABASE_ANON_KEY` | Supabase द्वारे आपोआप पुरवले जाते |
| `SUPABASE_SERVICE_ROLE_KEY` | आपोआप पुरवले जाते; RLS ला बायपास करून profiles वाचते |

### Resource Netlify साइट्स (प्रति साइट)
| Variable | वर्णन |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | वरीलप्रमाणेच तीच HMAC key |
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
| `profiles` | वापरकर्ता खाती, tier, streak, आवडी |
| `user_progress` | प्रति-अभ्यासक्रम प्रगती ट्रॅकिंग |
| `bookmarks` | वापरकर्ता बुकमार्क |
| `user_notes` | वैयक्तिक नोट्स |
| `certificates` | badge metadata सह जारी केलेली प्रमाणपत्रे |
| `payments` | पेमेंट इतिहास |
| `coaching_bookings` | कोचिंग सत्र बुकिंग |
| `organizations` | संस्था नोंदी |
| `organization_members` | वापरकर्ता ↔ संस्था सदस्यत्व |
| `learning_paths` | सानुकूल संस्था शिक्षण मार्ग |
| `learning_path_assignments` | देय तारखांसह मार्ग ↔ वापरकर्ता असाइनमेंट |
| `portfolio_items` | वापरकर्ता पोर्टफोलिओ नोंदी |
| `challenge_submissions` | लाइव्ह केस चॅलेंज सबमिशन |
| `challenge_requests` | संस्थांकडून सानुकूल चॅलेंज विनंत्या |
| `cohorts` | सुरुवात/समाप्ती तारखांसह प्रशिक्षण cohorts (v10.8.0) |
| `cohort_members` | Cohort नावनोंदणी + प्रगती ट्रॅकिंग (v10.8.0) |
| `cohort_discussions` | cohorts मधील चर्चा सूत्रे (v10.8.0) |
| `notifications` | इन-ॲप + ईमेल सूचना लॉग (v10.8.0) |
| `notification_preferences` | प्रति-वापरकर्ता ईमेल opt-in/out (v10.8.0) |
| `course_content` | Edge Function द्वारे दिलेला डायनॅमिक अभ्यासक्रम HTML |
| `badge_shares` | Badge शेअरिंग ट्रॅकिंग |

## Supabase Edge Functions

| Function | उद्देश्य |
|----------|---------|
| `mint-resource-token` | प्रीमियम resource प्रवेशासाठी JWT minting |
| `issue-certificate` | अभ्यासक्रम पूर्ण झाल्यावर प्रमाणपत्र जारी करणे |
| `game-agent` | खेळांसाठी MiroFish AI agent engine (multi-provider LLM) |
| `serve-course-content` | डायनॅमिक अभ्यासक्रम आशय देणे |
| `send-notification` | ईमेल सूचना: streak स्मरणपत्रे, cohort अंतिम मुदती, मॅन्युअल (v10.8.0) |

## फाइल रचना

संपूर्ण निर्देशिका मांडणीसाठी [README → Project Structure](https://github.com/ImpactMojo/ImpactMojo#project-structure) पहा.
