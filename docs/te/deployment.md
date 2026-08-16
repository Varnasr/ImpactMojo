# విస్తరణ మార్గదర్శి

## ప్రధాన సైట్ (impactmojo.in)

### Netlify సెటప్

ప్రధాన సైట్ GitHub లో `main` బ్రాంచ్ నుండి స్వయంచాలకంగా విస్తరిస్తుంది.

- **బిల్డ్ కమాండ్:** ఏదీ లేదు (స్టాటిక్ సైట్)
- **పబ్లిష్ డైరెక్టరీ:** `.` (రూట్)
- **అనుకూల డొమైన్:** `www.impactmojo.in`

### క్లీన్ URL రూటింగ్

`_redirects` ఫైల్ క్లీన్ URLలను `index.html` కు తిరిగి రాస్తుంది:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

`js/router.js` స్క్రిప్ట్ URL మార్గాన్ని చదివి సంబంధిత విభాగం/మోడల్‌ను తెరుస్తుంది.

### Supabase కాన్ఫిగరేషన్

1. ఒక Supabase ప్రాజెక్ట్‌ను సృష్టించండి
2. ప్రామాణీకరణను ప్రారంభించండి (Email, Google OAuth, Magic Links)
3. `profiles` పట్టికను సృష్టించండి (స్కీమా కోసం README చూడండి)
4. **anon key** మరియు **project URL** ను `js/auth.js` కు కాపీ చేయండి
5. `supabase functions deploy` తో `mint-resource-token` Edge Function ను విస్తరించండి

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## ప్రీమియం వనరు సైట్‌లు

ప్రతి ప్రీమియం సాధనం ఒక JWT auth-gate ఎడ్జ్ ఫంక్షన్‌తో ఒక ప్రత్యేక Netlify సైట్.

### సెటప్ దశలు (ఒక్కో సైట్‌కు)

1. Netlify లో **సైట్‌ను సృష్టించండి** (మాన్యువల్ డిప్లాయ్ లేదా లింక్డ్ రిపో)

2. Netlify డాష్‌బోర్డ్ → Site settings → Environment variables లో **పర్యావరణ వేరియబుల్స్‌ను సెట్ చేయండి**:
   - `RESOURCE_TOKEN_SECRET` — Supabase Edge Function లో ఉపయోగించిన అదే HMAC కీ ("Secret", Production context గా సెట్ చేయండి)
   - `RESOURCE_ID` — ఈ సైట్‌కు ప్రత్యేక స్లగ్ (రహస్యం కాదు, అన్ని సందర్భాలు)

3. **ఎడ్జ్ ఫంక్షన్‌తో విస్తరించండి:**
   - సైట్ రూట్‌లో `netlify.toml` ను చేర్చండి
   - `netlify/edge-functions/auth-gate.ts` ను చేర్చండి
   - Netlify CLI లేదా API ద్వారా విస్తరించండి

### వనరు ID మ్యాపింగ్

| సైట్ | RESOURCE_ID |
|------|-------------|
| *(ప్రైవేట్ — Netlify డాష్‌బోర్డ్ చూడండి)* | `rq-builder` |
| *(ప్రైవేట్ — Netlify డాష్‌బోర్డ్ చూడండి)* | `code-convert-pro` |
| *(ప్రైవేట్ — Netlify డాష్‌బోర్డ్ చూడండి)* | `qual-insights` |
| *(ప్రైవేట్ — Netlify డాష్‌బోర్డ్ చూడండి)* | `vaniscribe` |

### కొత్త HMAC రహస్యాన్ని ఉత్పత్తి చేయడం

```bash
openssl rand -base64 32
```

అన్ని వనరు సైట్‌లు మరియు Supabase Edge Function అంతటా అదే రహస్యాన్ని ఉపయోగించండి.

### Auth Gate ను ధృవీకరించడం

విస్తరణ తర్వాత, వనరు సైట్‌ను నేరుగా సందర్శించండి. మీరు దీనికి మళ్లించబడాలి:
```
https://www.impactmojo.in/login?reason=expired
```

మీకు 500 లోపం కనిపిస్తే, `RESOURCE_TOKEN_SECRET` మరియు `RESOURCE_ID` రెండూ సరిగ్గా సెట్ చేయబడ్డాయో లేదో తనిఖీ చేయండి.

## కొత్త ప్రీమియం వనరు సైట్‌ను జోడించడం

1. సాధనాన్ని స్టాటిక్ HTML/JS సైట్‌గా సృష్టించండి
2. Netlify కు విస్తరించండి
3. `RESOURCE_TOKEN_SECRET` మరియు `RESOURCE_ID` env వేరియబుల్స్‌ను జోడించండి
4. auth-gate ఎడ్జ్ ఫంక్షన్‌తో విస్తరించండి (`netlify-resource-template/` ఉపయోగించండి)
5. `supabase/functions/mint-resource-token/index.ts` లో tier ACL కు వనరు ID ను జోడించండి
6. `js/resource-launch.js` లో `RESOURCE_URLS` కు URL ను జోడించండి
7. `data-resource-id="your-id"` తో `premium.html` లో ఒక కార్డును జోడించండి
