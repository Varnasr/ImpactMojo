# ডিপ্লয়মেন্ট গাইড

## প্রধান সাইট (impactmojo.in)

### Netlify সেটআপ

প্রধান সাইটটি GitHub-এর `main` ব্রাঞ্চ থেকে স্বয়ংক্রিয়ভাবে ডিপ্লয় হয়।

- **Build command:** None (static site)
- **Publish directory:** `.` (root)
- **Custom domain:** `www.impactmojo.in`

### ক্লিন URL রাউটিং

`_redirects` ফাইলটি ক্লিন URL-গুলিকে `index.html`-এ পুনর্লিখন করে:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

`js/router.js` স্ক্রিপ্টটি URL পাথটি পড়ে এবং সংশ্লিষ্ট সেকশন/মোডাল খোলে।

### Supabase কনফিগারেশন

1. একটি Supabase প্রজেক্ট তৈরি করুন
2. অথেন্টিকেশন সক্রিয় করুন (Email, Google OAuth, Magic Links)
3. `profiles` টেবিল তৈরি করুন (স্কিমার জন্য README দেখুন)
4. **anon key** এবং **project URL** কপি করে `js/auth.js`-এ দিন
5. `supabase functions deploy` দিয়ে `mint-resource-token` Edge Function ডিপ্লয় করুন

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## প্রিমিয়াম রিসোর্স সাইট

প্রতিটি প্রিমিয়াম টুল হল একটি পৃথক Netlify সাইট, যাতে একটি JWT auth-gate এজ ফাংশন থাকে।

### সেটআপ ধাপসমূহ (প্রতিটি সাইটের জন্য)

1. Netlify-তে **সাইট তৈরি করুন** (manual deploy বা linked repo)

2. Netlify ড্যাশবোর্ড → Site settings → Environment variables-এ **environment variables সেট করুন**:
   - `RESOURCE_TOKEN_SECRET` — Supabase Edge Function-এ ব্যবহৃত একই HMAC key ("Secret" হিসেবে সেট করুন, Production context)
   - `RESOURCE_ID` — এই সাইটের জন্য অনন্য slug (secret নয়, সব context)

3. **এজ ফাংশন সহ ডিপ্লয় করুন:**
   - সাইট রুটে `netlify.toml` অন্তর্ভুক্ত করুন
   - `netlify/edge-functions/auth-gate.ts` অন্তর্ভুক্ত করুন
   - Netlify CLI বা API দিয়ে ডিপ্লয় করুন

### Resource ID ম্যাপিং

| সাইট | RESOURCE_ID |
|------|-------------|
| *(private — see Netlify dashboard)* | `rq-builder` |
| *(private — see Netlify dashboard)* | `code-convert-pro` |
| *(private — see Netlify dashboard)* | `qual-insights` |
| *(private — see Netlify dashboard)* | `vaniscribe` |

### একটি নতুন HMAC Secret তৈরি করা

```bash
openssl rand -base64 32
```

সমস্ত রিসোর্স সাইট এবং Supabase Edge Function-এ একই secret ব্যবহার করুন।

### Auth Gate যাচাই করা

ডিপ্লয়মেন্টের পরে, রিসোর্স সাইটটিতে সরাসরি যান। আপনাকে এখানে পুনঃনির্দেশিত করা উচিত:
```
https://www.impactmojo.in/login?reason=expired
```

আপনি যদি একটি 500 error দেখেন, তাহলে `RESOURCE_TOKEN_SECRET` এবং `RESOURCE_ID` উভয়ই সঠিকভাবে সেট করা আছে কিনা পরীক্ষা করুন।

## একটি নতুন প্রিমিয়াম রিসোর্স সাইট যুক্ত করা

1. টুলটিকে একটি static HTML/JS সাইট হিসেবে তৈরি করুন
2. Netlify-তে ডিপ্লয় করুন
3. `RESOURCE_TOKEN_SECRET` এবং `RESOURCE_ID` env vars যুক্ত করুন
4. auth-gate এজ ফাংশন সহ ডিপ্লয় করুন (`netlify-resource-template/` ব্যবহার করুন)
5. `supabase/functions/mint-resource-token/index.ts`-এ tier ACL-এ resource ID যুক্ত করুন
6. `js/resource-launch.js`-এ `RESOURCE_URLS`-এ URL যুক্ত করুন
7. `data-resource-id="your-id"` সহ `premium.html`-এ একটি কার্ড যুক্ত করুন
