#!/usr/bin/env python3
"""Second-pass i18n corrections: brand names + residual howlers.

Pass 1 (fix-i18n-mistranslations.py) fixed practitioner/title errors. A full
audit then surfaced a bigger systematic error: the BRAND NAME "ImpactMojo" was
translated into native script all over the page dictionaries —
प्रभावमोजो / इम्पॅक्टमोजो / ইম্প্যাক্টমোজি / இம்பேக்ட்மோஜோ — plus the product names
DevEconomics and PinPoint Ventures. Brand names must always stay in Latin script.

Also: Hindi "Capstone Project" -> "समाप्‍त परियोजना" ("finished/discontinued
project") on every course page, and residual Bengali "practitioner" -> "doctor".

Care taken:
- Marathi "मोज" is also the root of "measure" (मोजमाप/मोजले/मोजतो) — only the
  unambiguous ImpactMojo brand tokens are replaced, never those.
- The Bengali doctor-word fix is conditional on the English SOURCE containing
  practitioner/practice (and not a medical context), so legitimate medical
  uses are untouched.
Re-runnable and idempotent.
"""
import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- brand-token substring replacements (applied to every value), per language ----
# longest-first ordering is enforced at runtime so suffixed forms win.
BRAND = {
    "hi": {
        "प्रभाव मोज़ो": "ImpactMojo",      # "ImpactMojo Labs" -> प्रभाव मोज़ो लैब्स
        "प्रभावमोजो": "ImpactMojo",
        "पिनपॉइंट वेंचर्स": "PinPoint Ventures",
        "देवइकोनॉमिक्स": "DevEconomics",
    },
    "mr": {
        "इम्पॅक्टमोजोच्या": "ImpactMojo च्या",
        "'इम्पॅक्टमोजो'": "'ImpactMojo'",
        "इम्पॅक्टमोजो": "ImpactMojo",
        "प्रभावकमोजो": "ImpactMojo",
        "प्रभावमोज": "ImpactMojo",
    },
    "bn": {
        "ইম্প্যাক্টমোজিওর": "ImpactMojo-র",
        "ইম্প্যাক্টমোজিও": "ImpactMojo-ও",
        "ইম্প্যাক্টমোজি": "ImpactMojo",
        "ইম্প্যাক্টমোজো": "ImpactMojo",
        "প্রভাবমোজো": "ImpactMojo",
        "প্রভাবমোজ": "ImpactMojo",
        "ইমপ্যাক্ট মোজো": "ImpactMojo",
        "ইমপ্যাক্ট মোজ": "ImpactMojo",
        "দেবইকোনমিকস": "DevEconomics",
    },
    "ta": {
        "தாக்கமோஜோவின்": "ImpactMojo",
        "இம்பேக்ட்மோஜோ": "ImpactMojo",
        "இம்பாக்ஸ்ட்மோஜோ": "ImpactMojo",
        "பின்பாயிண்ட் வென்ச்சர்ஸ்": "PinPoint Ventures",
    },
}

# ---- Hindi exact-key fixes ----
HI_EXACT = {
    "Capstone Project": "कैपस्टोन प्रोजेक्ट",
    "Capstone project": "कैपस्टोन प्रोजेक्ट",
}

# ---- Bengali residual practitioner->doctor, conditional on English source ----
BN_DOC = [("চিকিৎসকদের", "অনুশীলনকারীদের"),
          ("চিকিৎসকের", "অনুশীলনকারীর"),
          ("চিকিৎসক", "অনুশীলনকারী")]
MED = ("biomedical", "treatment", "health", "clinic", "medical", "medicine",
       "therap", "dispensary", "hospital", "doctor", "patient")


def main():
    grand = 0
    for lang in ["hi", "ta", "bn", "mr"]:
        brand = sorted(BRAND.get(lang, {}).items(), key=lambda kv: -len(kv[0]))
        for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
            changed = 0
            for k, v in list(d.items()):
                if not isinstance(v, str):
                    continue
                nv = v
                # exact-key fixes (hi)
                if lang == "hi" and k in HI_EXACT:
                    nv = HI_EXACT[k]
                # brand token normalisation
                for a, b in brand:
                    if a in nv:
                        nv = nv.replace(a, b)
                # bn conditional practitioner fix
                if lang == "bn":
                    ks = k.lower()
                    if ("practitioner" in ks or "practice" in ks) and not any(x in ks for x in MED):
                        for a, b in BN_DOC:
                            if a in nv:
                                nv = nv.replace(a, b)
                if nv != v:
                    d[k] = nv
                    changed += 1
            if changed:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
                grand += changed
                print(f"  {lang}/{os.path.basename(path):42s} {changed:3d} fixed")
    print(f"\nTotal strings corrected (pass 2): {grand}")


if __name__ == "__main__":
    main()
