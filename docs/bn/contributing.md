# ImpactMojo-তে অবদান রাখা

অবদান রাখতে আগ্রহী হওয়ার জন্য ধন্যবাদ! ImpactMojo উন্নয়ন সম্প্রদায়ের দ্বারা এবং তাদের জন্যই নির্মিত। আপনি একজন অনুশীলনকারী হোন যিনি একটি পুরনো পরিসংখ্যান লক্ষ্য করেছেন, একজন শিক্ষাবিদ হোন যার কাছে একটি দুর্দান্ত কেস স্টাডি আছে, বা একজন ডেভেলপার হোন যিনি একটি বাগ ঠিক করতে পারেন — আপনার জন্য অবদান রাখার একটি অর্থপূর্ণ উপায় আছে।

## আপনাকে প্রযুক্তিগত হতে হবে না

আমাদের সবচেয়ে মূল্যবান অবদানের অনেকগুলো প্রোগ্রামারদের কাছ থেকে নয়, অনুশীলনকারীদের কাছ থেকে আসে। এক লাইন কোডও না লিখে আপনি কীভাবে সাহায্য করতে পারেন তা এখানে:

| আপনি কী করতে পারেন | কীভাবে | কঠিনতা |
|-----------------|-----|------------|
| **একটি ত্রুটি রিপোর্ট করুন** | একটি ভাঙা লিঙ্ক, ভুল পরিসংখ্যান বা পুরনো রেফারেন্স পেয়েছেন? একটি [Content Issue](https://github.com/ImpactMojo/ImpactMojo/issues/new?template=content_issue.md) খুলুন | খুব সহজ |
| **একটি বিষয় প্রস্তাব করুন** | এমন একটি বিষয় জানেন যা কভার করা উচিত? একটি [Discussion](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) শুরু করুন | খুব সহজ |
| **একটি কেস স্টাডি শেয়ার করুন** | আপনার কাজ থেকে একটি বাস্তব উন্নয়ন কেস স্টাডি আছে? আমাদের hello@impactmojo.in-এ ইমেল করুন | সহজ |
| **কনটেন্ট অনুবাদ করুন** | কোর্সগুলো হিন্দি, তামিল, বাংলা, তেলেগু বা মারাঠিতে উপলব্ধ করতে সাহায্য করুন | সহজ–মাঝারি |
| **কনটেন্ট পর্যালোচনা করুন** | আপনি কি MEL, জেন্ডার স্টাডিজ বা উন্নয়ন অর্থনীতিতে বিশেষজ্ঞ? নির্ভুলতার জন্য কোর্স পর্যালোচনায় আমাদের সাহায্য করুন | সহজ |
| **একটি handout লিখুন** | আপনি ভালো জানেন এমন একটি বিষয়ে একটি রেফারেন্স শিট তৈরি করুন | মাঝারি |

## প্রযুক্তিগত অবদানকারীদের জন্য

আপনি যদি HTML, CSS বা JavaScript-এর সাথে স্বাচ্ছন্দ্যবোধ করেন, তাহলে অবদান রাখার অনেক উপায় আছে:

| ক্ষেত্র | উদাহরণ | কঠিনতা |
|------|----------|------------|
| **বাগ ফিক্স** | ভাঙা লিঙ্ক, layout সমস্যা, JavaScript ত্রুটি | সহজ–মাঝারি |
| **অ্যাক্সেসিবিলিটি** | WCAG সম্মতি, screen reader সমর্থন, keyboard নেভিগেশন | মাঝারি |
| **ডিজাইন** | UI/UX উন্নতি, মোবাইল অভিজ্ঞতা | মাঝারি |
| **Tools & Labs** | ইন্টারঅ্যাক্টিভ শিক্ষণ টুল তৈরি বা উন্নত করুন | কঠিন |
| **গেম** | নতুন অর্থনীতির সিমুলেশন | মাঝারি–কঠিন |

### শুরু করা (প্রযুক্তিগত)

ImpactMojo একটি vanilla HTML/CSS/JS প্রকল্প — কোনো framework নেই, কোনো build step নেই। আপনি শুধুমাত্র একটি ওয়েব ব্রাউজার এবং একটি সাধারণ সার্ভার দিয়ে এটি স্থানীয়ভাবে চালাতে পারেন:

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

### Commit বার্তা প্রথা

প্রতিটি commit বার্তা একটি উপসর্গ দিয়ে শুরু হয় যা পরিবর্তনের ধরন বর্ণনা করে:

| উপসর্গ | কখন ব্যবহার করবেন | উদাহরণ |
|--------|---------------|---------|
| `Add:` | নতুন ফিচার, কোর্স বা টুল | `Add: interactive budget planning lab` |
| `Fix:` | বাগ ফিক্স বা ভাঙা লিঙ্ক | `Fix: broken nav dropdown on mobile Safari` |
| `Update:` | বিদ্যমান কনটেন্ট বা কোডের উন্নতি | `Update: MEL course module 3 with 2025 data` |
| `Translate:` | অনুবাদের কাজ | `Translate: gender studies course to Hindi` |
| `Docs:` | ডকুমেন্টেশন পরিবর্তন | `Docs: add workshop facilitation guide` |
| `Refactor:` | কোড পুনর্গঠন (কোনো আচরণ পরিবর্তন নেই) | `Refactor: extract auth logic to separate file` |
| `Test:` | টেস্ট যোগ বা আপডেট করা | `Test: add accessibility checks for games` |
| `CI:` | CI/CD pipeline পরিবর্তন | `CI: add broken link checker workflow` |
| `Chore:` | রক্ষণাবেক্ষণ (dependencies, configs) | `Chore: update dependabot config` |

### Pull Request নির্দেশিকা

- PR-গুলো কেন্দ্রীভূত রাখুন — প্রতি PR-এ একটি ফিচার বা ফিক্স
- ডেস্কটপ এবং মোবাইলে পরীক্ষা করুন
- ভিজ্যুয়াল পরিবর্তনের জন্য screenshots অন্তর্ভুক্ত করুন
- পরিবর্তনগুলো premium ফিচারকে প্রভাবিত করলে উল্লেখ করুন

## কনটেন্ট লেখার শৈলী

আপনি যদি শিক্ষামূলক কনটেন্টে অবদান রাখেন, আমরা যা লক্ষ্য করি তা এখানে:

- **টোন:** সহজলভ্য কিন্তু কঠোর। 2–3 বছরের অভিজ্ঞতাসম্পন্ন একজন অনুশীলনকারীর জন্য লিখুন।
- **উদাহরণ:** দক্ষিণ এশীয় প্রেক্ষাপটকে অগ্রাধিকার দিন (ভারত, বাংলাদেশ, নেপাল, শ্রীলঙ্কা)।
- **পরিভাষা:** প্রথম ব্যবহারে পরিভাষা সংজ্ঞায়িত করুন। এটি একটি সাধারণ সেক্টর পরিভাষা হলে, এটি [ImpactLex](https://www.impactmojo.in/impactlex/)-এ যোগ করুন।
- **স্বীকৃতি:** সর্বদা উৎস উল্লেখ করুন। যেখানে সম্ভব [DevDiscourses](https://www.impactmojo.in/dataverse)-এর সাথে লিঙ্ক করুন।
- **অ্যাক্সেসিবিলিটি:** স্পষ্ট শিরোনাম, ছবির জন্য alt text, এবং পর্যাপ্ত রঙের কনট্রাস্ট ব্যবহার করুন।

## সমস্যা রিপোর্ট করা

উপযুক্ত template সহ [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) ব্যবহার করুন:

- **Bug Report** — কিছু ভেঙে গেছে (লিঙ্ক, layout, ত্রুটি)
- **Feature Request** — একটি নতুন ধারণা বা উন্নতি
- **Content Issue** — তথ্যগত ত্রুটি, পুরনো তথ্য, অনুপস্থিত বিষয়

## কমিউনিটি চ্যানেল

- [WhatsApp PLC](https://chat.whatsapp.com/EsBjbKaQfupG1HbtajTjHM) — অনুশীলনকারীদের মধ্যে সমকক্ষ আলোচনা
- [Discord](https://discord.gg/M3ZCmUe7ab) — প্রযুক্তিগত আলোচনা এবং পরীক্ষা-নিরীক্ষা
- [Telegram](https://t.me/impactmojo) — বিনামূল্যে সম্পদ এবং আপডেট
- [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions) — ধারণা, প্রশ্নোত্তর এবং ঘোষণা
- **ইমেল:** hello@impactmojo.in — অন্য যেকোনো কিছুর জন্য
