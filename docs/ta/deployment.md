# வரிசைப்படுத்தல் வழிகாட்டி

## முதன்மைத் தளம் (impactmojo.in)

### Netlify அமைப்பு

முதன்மைத் தளம் GitHub இல் உள்ள `main` கிளையிலிருந்து தானாகவே வரிசைப்படுத்தப்படுகிறது.

- **Build command:** None (static site)
- **Publish directory:** `.` (root)
- **Custom domain:** `www.impactmojo.in`

### Clean URL Routing

`_redirects` கோப்பு clean URL-களை `index.html` க்கு மீண்டும் எழுதுகிறது:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

`js/router.js` script URL பாதையைப் படித்து, தொடர்புடைய பிரிவு/modal ஐத் திறக்கிறது.

### Supabase கட்டமைப்பு

1. ஒரு Supabase திட்டத்தை உருவாக்கவும்
2. அங்கீகாரத்தை இயக்கவும் (Email, Google OAuth, Magic Links)
3. `profiles` table ஐ உருவாக்கவும் (schema-க்கு README பார்க்கவும்)
4. **anon key** மற்றும் **project URL** ஐ `js/auth.js` க்கு நகலெடுக்கவும்
5. `mint-resource-token` Edge Function ஐ `supabase functions deploy` உடன் வரிசைப்படுத்தவும்

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## Premium Resource தளங்கள்

ஒவ்வொரு premium கருவியும் ஒரு JWT auth-gate edge function கொண்ட தனி Netlify தளம்.

### அமைப்பு படிகள் (ஒவ்வொரு தளத்திற்கும்)

1. Netlify இல் **தளத்தை உருவாக்கவும்** (கைமுறை வரிசைப்படுத்தல் அல்லது இணைக்கப்பட்ட repo)

2. Netlify dashboard → Site settings → Environment variables இல் **environment variables ஐ அமைக்கவும்**:
   - `RESOURCE_TOKEN_SECRET` — Supabase Edge Function இல் பயன்படுத்தப்படும் அதே HMAC key ("Secret", Production context ஆக அமைக்கவும்)
   - `RESOURCE_ID` — இந்தத் தளத்திற்கான தனித்துவமான slug (ரகசியம் அல்ல, அனைத்து contexts)

3. **edge function உடன் வரிசைப்படுத்தவும்:**
   - தளத்தின் root இல் `netlify.toml` ஐச் சேர்க்கவும்
   - `netlify/edge-functions/auth-gate.ts` ஐச் சேர்க்கவும்
   - Netlify CLI அல்லது API மூலம் வரிசைப்படுத்தவும்

### Resource ID Mapping

| Site | RESOURCE_ID |
|------|-------------|
| *(private — see Netlify dashboard)* | `rq-builder` |
| *(private — see Netlify dashboard)* | `code-convert-pro` |
| *(private — see Netlify dashboard)* | `qual-insights` |
| *(private — see Netlify dashboard)* | `vaniscribe` |

### ஒரு புதிய HMAC Secret ஐ உருவாக்குதல்

```bash
openssl rand -base64 32
```

அனைத்து resource தளங்கள் மற்றும் Supabase Edge Function இல் அதே secret ஐப் பயன்படுத்தவும்.

### Auth Gate ஐ சரிபார்த்தல்

வரிசைப்படுத்தலுக்குப் பிறகு, resource தளத்தை நேரடியாகப் பார்வையிடவும். நீங்கள் இங்கு திருப்பி விடப்பட வேண்டும்:
```
https://www.impactmojo.in/login?reason=expired
```

நீங்கள் 500 பிழையைக் கண்டால், `RESOURCE_TOKEN_SECRET` மற்றும் `RESOURCE_ID` இரண்டும் சரியாக அமைக்கப்பட்டுள்ளனவா என்பதைச் சரிபார்க்கவும்.

## ஒரு புதிய Premium Resource தளத்தைச் சேர்த்தல்

1. கருவியை ஒரு static HTML/JS தளமாக உருவாக்கவும்
2. Netlify இல் வரிசைப்படுத்தவும்
3. `RESOURCE_TOKEN_SECRET` மற்றும் `RESOURCE_ID` env vars ஐச் சேர்க்கவும்
4. auth-gate edge function உடன் வரிசைப்படுத்தவும் (`netlify-resource-template/` ஐப் பயன்படுத்தவும்)
5. `supabase/functions/mint-resource-token/index.ts` இல் உள்ள tier ACL இல் resource ID ஐச் சேர்க்கவும்
6. `js/resource-launch.js` இல் உள்ள `RESOURCE_URLS` இல் URL ஐச் சேர்க்கவும்
7. `premium.html` இல் `data-resource-id="your-id"` உடன் ஒரு card ஐச் சேர்க்கவும்
