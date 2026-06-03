# डिप्लॉयमेंट गाइड

## मुख्य साइट (impactmojo.in)

### Netlify सेटअप

मुख्य साइट GitHub पर `main` ब्रांच से स्वचालित रूप से डिप्लॉय होती है।

- **Build command:** None (static site)
- **Publish directory:** `.` (root)
- **Custom domain:** `www.impactmojo.in`

### क्लीन URL रूटिंग

`_redirects` फ़ाइल क्लीन URL को `index.html` में फिर से लिखती है:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

`js/router.js` स्क्रिप्ट URL पथ को पढ़ती है और संगत खंड/modal खोलती है।

### Supabase कॉन्फ़िगरेशन

1. एक Supabase प्रोजेक्ट बनाएँ
2. प्रमाणीकरण सक्षम करें (Email, Google OAuth, Magic Links)
3. `profiles` टेबल बनाएँ (स्कीमा के लिए README देखें)
4. **anon key** और **project URL** को `js/auth.js` में कॉपी करें
5. `mint-resource-token` Edge Function को `supabase functions deploy` के साथ डिप्लॉय करें

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## Premium Resource साइटें

प्रत्येक premium टूल एक अलग Netlify साइट है जिसमें एक JWT auth-gate edge function होता है।

### सेटअप चरण (प्रति साइट)

1. Netlify पर **साइट बनाएँ** (मैन्युअल डिप्लॉय या लिंक की गई repo)

2. Netlify dashboard → Site settings → Environment variables में **एनवायरनमेंट वेरिएबल सेट करें**:
   - `RESOURCE_TOKEN_SECRET` — वही HMAC key जो Supabase Edge Function में उपयोग किया गया है ("Secret", Production context के रूप में सेट करें)
   - `RESOURCE_ID` — इस साइट के लिए अद्वितीय slug (गुप्त नहीं, सभी contexts)

3. **edge function के साथ डिप्लॉय करें:**
   - साइट रूट में `netlify.toml` शामिल करें
   - `netlify/edge-functions/auth-gate.ts` शामिल करें
   - Netlify CLI या API के माध्यम से डिप्लॉय करें

### Resource ID मैपिंग

| Site | RESOURCE_ID |
|------|-------------|
| *(private — see Netlify dashboard)* | `rq-builder` |
| *(private — see Netlify dashboard)* | `code-convert-pro` |
| *(private — see Netlify dashboard)* | `qual-insights` |
| *(private — see Netlify dashboard)* | `vaniscribe` |

### एक नया HMAC Secret बनाना

```bash
openssl rand -base64 32
```

सभी resource साइटों और Supabase Edge Function में एक ही secret का उपयोग करें।

### Auth Gate को सत्यापित करना

डिप्लॉयमेंट के बाद, सीधे resource साइट पर जाएँ। आपको यहाँ रीडायरेक्ट किया जाना चाहिए:
```
https://www.impactmojo.in/login?reason=expired
```

यदि आपको 500 त्रुटि दिखती है, तो जाँचें कि `RESOURCE_TOKEN_SECRET` और `RESOURCE_ID` दोनों सही ढंग से सेट हैं।

## एक नई Premium Resource साइट जोड़ना

1. टूल को एक स्थैतिक HTML/JS साइट के रूप में बनाएँ
2. Netlify पर डिप्लॉय करें
3. `RESOURCE_TOKEN_SECRET` और `RESOURCE_ID` env vars जोड़ें
4. auth-gate edge function के साथ डिप्लॉय करें (`netlify-resource-template/` का उपयोग करें)
5. `supabase/functions/mint-resource-token/index.ts` में tier ACL में resource ID जोड़ें
6. `js/resource-launch.js` में `RESOURCE_URLS` में URL जोड़ें
7. `premium.html` पर `data-resource-id="your-id"` के साथ एक कार्ड जोड़ें
