#!/usr/bin/env python3
"""Correct machine-translation errors in the per-page i18n dictionaries.

The core UI strings (i18n/<lang>.json, built from i18n/overrides/) were
hand-reviewed and are fine. The per-page course content (i18n/pages/<lang>/*.json)
was bulk machine-translated with no context and never reviewed, producing
context-blind howlers:

  practitioner            -> "doctor/physician"  (चिकित्सक / மருத்துவர் / চিকিৎসক)
  dev-practitioner cohort -> "religious-physician group" (धार्मिक-चिकित्सक)
  Evidence-Based Practice -> "evidence-based medical treatment"
  Field Companions        -> "village residents" / "female friends"
  Course Papers           -> "exam papers" (प्रश्नपत्र)
  Marginalia              -> "edges/shores" (किनारे)
  Understanding Development-> "Understanding Development" as word-salad (समझ विकास)
  Sixty-eight terms       -> "eighty-six time-periods"
  The Indicator Ate ...   -> "the director attacked the village" (mr)
  ImpactMojo (brand)      -> "Impact: Mojo" (प्रभावः मोजो)

This applies an auditable, exact-key correction map (keyed by the ENGLISH
source string, so it never depends on the broken value) plus, for Hindi only,
surgical substring fixes that cannot collide with legitimate medical terms
(जैव चिकित्सा "biomedical", causal-inference चिकित्सा "treatment" are left alone:
they contain चिकित्सा, never the practitioner-noun चिकित्सक).

Goal: language that is easy to understand and correct — not formal and bad.
Everyday loanwords the sector actually uses (प्रैक्टिशनर, कोर्स, फील्ड, लाइव) are
preferred over Sanskritized coinages. Re-runnable and idempotent.
"""
import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Shared English source strings (recur across all course pages as cross-link cards)
DOJO = ("56 weekly dojo sessions in the South Asian dev-practitioner cohort — "
        "case clinics, paper discussions, live Q&A.")
PRAC_WEEKLY = "Weekly practice sessions in the practitioner cohort."
HOLISTIC = "courses for holistic practitioner development."
JOIN = "Join fellow practitioners across South Asia"
LEGAL_LIT = "Legal Literacy for Practitioners"
UNDERSTAND_DEV = "Understanding Development: An Economics Perspective"
SIXTY8 = ("Sixty-eight terms from the course, defined for development practitioners "
          "rather than corporate analysts. Search, or filter by part of the workflow.")

# ----- exact-key correction maps: English source -> natural, correct translation -----
FIX = {
    "hi": {
        "Marginalia": "हाशिया",
        "Explore Marginalia": "हाशिया देखें",
        "The Indicator Ate the Village": "इंडिकेटर गाँव को खा गया",
        UNDERSTAND_DEV: "विकास को समझना: एक आर्थिक नज़रिया",
        "Understanding Development: Theory, Evidence & Policy":
            "विकास को समझना: सिद्धांत, सबूत और नीति",
        "Field Companions": "फील्ड साथी",
        "Course Papers Collection": "कोर्स के रिसर्च पेपर",
        "Evidence-Based Practice": "सबूत-आधारित प्रैक्टिस",
        DOJO: ("दक्षिण एशिया के डेवलपमेंट प्रैक्टिशनर समुदाय में हर हफ़्ते 56 डोजो सेशन — "
               "केस क्लिनिक, पेपर पर चर्चा, और लाइव सवाल-जवाब।"),
        PRAC_WEEKLY: "प्रैक्टिशनर समुदाय में हर हफ़्ते प्रैक्टिस सेशन।",
        HOLISTIC: "प्रैक्टिशनर के संपूर्ण विकास के लिए कोर्स।",
        JOIN: "दक्षिण एशिया भर के साथी प्रैक्टिशनर्स से जुड़ें",
        LEGAL_LIT: "प्रैक्टिशनर्स के लिए कानूनी साक्षरता",
        SIXTY8: ("कोर्स के 68 शब्द, कॉर्पोरेट एनालिस्ट के लिए नहीं बल्कि डेवलपमेंट "
                 "प्रैक्टिशनर्स के लिए समझाए गए। सर्च करें, या वर्कफ़्लो के हिस्से के हिसाब से फ़िल्टर करें।"),
    },
    "mr": {
        "Marginalia": "हाशिया",
        "Explore Marginalia": "हाशिया पाहा",
        "The Indicator Ate the Village": "इंडिकेटरने गाव गिळून टाकलं",
        UNDERSTAND_DEV: "विकास समजून घेणे: एक आर्थिक दृष्टिकोन",
        "Field Companions": "फील्ड सोबती",
        "Evidence-Based Practice": "पुराव्यावर आधारित प्रॅक्टिस",
        DOJO: ("दक्षिण आशियातील डेव्हलपमेंट प्रॅक्टिशनर समुदायात दर आठवड्याला 56 डोजो सत्रे — "
               "केस क्लिनिक, पेपरवर चर्चा, आणि थेट प्रश्नोत्तरे."),
        HOLISTIC: "प्रॅक्टिशनरच्या संपूर्ण विकासासाठी कोर्सेस.",
        JOIN: "दक्षिण आशियातील सहकारी प्रॅक्टिशनर्सशी जोडा",
    },
    "ta": {
        "Marginalia": "ஓரக்குறிப்புகள்",
        "Explore Marginalia": "ஓரக்குறிப்புகளைப் பாருங்கள்",
        UNDERSTAND_DEV: "வளர்ச்சியைப் புரிந்துகொள்ளுதல்: ஒரு பொருளாதாரக் கண்ணோட்டம்",
        "Field Companions": "கள சகாக்கள்",
        "Course Papers Collection": "பாடநெறி ஆய்வுக் கட்டுரைகள்",
        "Evidence-Based Practice": "சான்று அடிப்படையிலான நடைமுறை",
        "RCTs & Policy": "RCTs & கொள்கை",
        DOJO: ("தெற்காசிய டெவலப்மென்ட் நடைமுறையாளர் குழுவில் வாரந்தோறும் 56 டோஜோ அமர்வுகள் — "
               "வழக்காய்வுகள், ஆய்வுக் கட்டுரை விவாதங்கள், நேரடி கேள்வி-பதில்."),
        PRAC_WEEKLY: "நடைமுறையாளர் குழுவில் வாராந்திர பயிற்சி அமர்வுகள்.",
        HOLISTIC: "முழுமையான நடைமுறையாளர் மேம்பாட்டுக்கான படிப்புகள்.",
        JOIN: "தெற்காசியா முழுவதும் உள்ள சக நடைமுறையாளர்களுடன் இணையுங்கள்.",
    },
    "bn": {
        "Marginalia": "প্রান্তটীকা",
        UNDERSTAND_DEV: "উন্নয়নকে বোঝা: একটি অর্থনৈতিক দৃষ্টিভঙ্গি",
        "Field Companions": "মাঠ সঙ্গী",
        "Course Papers Collection": "কোর্সের গবেষণাপত্র সংকলন",
        "Evidence-Based Practice": "প্রমাণ-ভিত্তিক অনুশীলন",
        DOJO: ("দক্ষিণ এশিয়ার উন্নয়ন-অনুশীলনকারী দলে সাপ্তাহিক 56টি দোজো সেশন — "
               "কেস ক্লিনিক, গবেষণাপত্র আলোচনা, সরাসরি প্রশ্নোত্তর।"),
        PRAC_WEEKLY: "অনুশীলনকারীদের দলে সাপ্তাহিক অনুশীলন সেশন।",
        JOIN: "দক্ষিণ এশিয়া জুড়ে সহ-অনুশীলনকারীদের সঙ্গে যুক্ত হোন",
    },
}

# ----- Hindi-only residual substring fixes (after exact-key pass) -----
# Safe: चिकित्सक (practitioner-noun) is never legitimate here; the real medical
# term चिकित्सा (biomedical / causal "treatment") has no क-ending and is untouched.
# Order matters: longest first.
HI_SUBSTR = [
    ("चिकित्सकों", "प्रैक्टिशनर्स"),   # practitioners (oblique/plural)
    ("चिकित्सक", "प्रैक्टिशनर"),        # practitioner
    ("झंडाध्वज", "फ्लैगशिप कोर्स"),     # flagship (was mistranslated "flagpole")
    # brand name must never be translated:
    ("प्रभावः मोजो", "ImpactMojo"),
    ("प्रभावःमोज़ो", "ImpactMojo"),
    ("प्रभावःमोजो", "ImpactMojo"),
    ("प्रभावः मोज़ो", "ImpactMojo"),
    ("इम्पैक्टमोज़ो", "ImpactMojo"),
    ("इम्पैक्टमोजो", "ImpactMojo"),
]


def main():
    grand = 0
    for lang, fixmap in FIX.items():
        for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
            changed = 0
            for k, v in list(d.items()):
                if k in fixmap and d[k] != fixmap[k]:
                    d[k] = fixmap[k]; changed += 1
                elif lang == "hi" and isinstance(v, str):
                    nv = v
                    for a, b in HI_SUBSTR:
                        if a in nv:
                            nv = nv.replace(a, b)
                    if nv != v:
                        d[k] = nv; changed += 1
            if changed:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
                grand += changed
                print(f"  {lang}/{os.path.basename(path):42s} {changed:3d} fixed")
    print(f"\nTotal strings corrected: {grand}")


if __name__ == "__main__":
    main()
