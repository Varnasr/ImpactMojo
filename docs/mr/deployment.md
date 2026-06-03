# डिप्लॉयमेंट मार्गदर्शक

## मुख्य साइट (impactmojo.in)

### Netlify सेटअप

मुख्य साइट GitHub वरील `main` ब्रँचमधून आपोआप डिप्लॉय होते.

- **Build command:** काहीही नाही (static site)
- **Publish directory:** `.` (root)
- **Custom domain:** `www.impactmojo.in`

### क्लीन URL राउटिंग

`_redirects` फाइल क्लीन URL ला `index.html` कडे पुनर्लेखित करते:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

`js/router.js` स्क्रिप्ट URL पाथ वाचते आणि संबंधित विभाग/मॉडल उघडते.

### Supabase कॉन्फिगरेशन

1. एक Supabase प्रकल्प तयार करा
2. ऑथेंटिकेशन सक्षम करा (Email, Google OAuth, Magic Links)
3. `profiles` टेबल तयार करा (स्कीमासाठी README पाहा)
4. **anon key** आणि **project URL** `js/auth.js` मध्ये कॉपी करा
5. `supabase functions deploy` वापरून `mint-resource-token` Edge Function डिप्लॉय करा

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## प्रीमियम रिसोर्स साइट्स

प्रत्येक प्रीमियम साधन ही JWT auth-gate edge function असलेली स्वतंत्र Netlify साइट आहे.

### सेटअप पायऱ्या (प्रति साइट)

1. Netlify वर **साइट तयार करा** (manual deploy किंवा linked repo)

2. Netlify dashboard → Site settings → Environment variables मध्ये **environment variables सेट करा**:
   - `RESOURCE_TOKEN_SECRET` — Supabase Edge Function मध्ये वापरलेली तीच HMAC key ("Secret", Production context म्हणून सेट करा)
   - `RESOURCE_ID` — या साइटसाठी अद्वितीय slug (गुप्त नाही, सर्व contexts)

3. **edge function सह डिप्लॉय करा:**
   - साइट rootमध्ये `netlify.toml` समाविष्ट करा
   - `netlify/edge-functions/auth-gate.ts` समाविष्ट करा
   - Netlify CLI किंवा API द्वारे डिप्लॉय करा

### Resource ID मॅपिंग

| साइट | RESOURCE_ID |
|------|-------------|
| *(खासगी — Netlify dashboard पाहा)* | `rq-builder` |
| *(खासगी — Netlify dashboard पाहा)* | `code-convert-pro` |
| *(खासगी — Netlify dashboard पाहा)* | `qual-insights` |
| *(खासगी — Netlify dashboard पाहा)* | `vaniscribe` |

### नवीन HMAC Secret तयार करणे

```bash
openssl rand -base64 32
```

सर्व resource साइट्स आणि Supabase Edge Function मध्ये तेच secret वापरा.

### Auth Gate तपासणे

डिप्लॉयमेंटनंतर, थेट resource साइटला भेट द्या. तुम्हाला येथे रीडायरेक्ट केले जायला हवे:
```
https://www.impactmojo.in/login?reason=expired
```

जर तुम्हाला 500 error दिसली, तर `RESOURCE_TOKEN_SECRET` आणि `RESOURCE_ID` दोन्ही योग्यरीत्या सेट केले आहेत का ते तपासा.

## नवीन प्रीमियम रिसोर्स साइट जोडणे

1. साधन एक static HTML/JS साइट म्हणून तयार करा
2. Netlify वर डिप्लॉय करा
3. `RESOURCE_TOKEN_SECRET` आणि `RESOURCE_ID` env vars जोडा
4. auth-gate edge function सह डिप्लॉय करा (`netlify-resource-template/` वापरा)
5. `supabase/functions/mint-resource-token/index.ts` मधील tier ACL मध्ये resource id जोडा
6. `js/resource-launch.js` मधील `RESOURCE_URLS` मध्ये URL जोडा
7. `premium.html` वर `data-resource-id="your-id"` सह एक card जोडा
