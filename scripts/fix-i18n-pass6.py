#!/usr/bin/env python3
"""Pass 6: enforce protected brand/tool/journal/acronym NAME labels (glossary).

The glossary detector (scripts/check-i18n-glossary.py) found that short NAME
labels were translated into unrelated common words in every language:
  Tableau -> 'plank/picture', Flourish -> 'growth', RAWGraphs -> 'raw picture',
  Datawrapper -> 'factsheet/database', Econometrica/Economica -> 'economics',
  EPW -> 'news', Indian Opinion -> 'opinion', FieldCases -> 'cases/field',
  NudgeKit -> 'application', PolicyDhara -> 'policy', Pomodoro Timer -> garbled,
  M&E -> 'graph/lesson/report/data', MEAL Workshops -> 'food workshops'.

For these pure-name labels the correct rendering is the name itself, verbatim.
Setting the value to the English key keeps the name intact and clean across all
four languages (transliterations like MGNREGA->मनरेगा and intentional renderings
like Marginalia->हाशिया are NOT in this list, so they're untouched).
"""
import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# pure-name labels (no translatable verb) -> keep the name verbatim
PROTECT = [
    "Tableau", "Flourish", "RAWGraphs", "Datawrapper", "Datawrapper/Flourish",
    "Tableau/Power BI", "Econometrica", "Economica", "EPW", "Indian Opinion",
    "FieldCases", "NudgeKit", "PolicyDhara", "Pomodoro Timer",
    "M&E", "M&E Dashboards", "M&E frameworks", "M&E Applications",
    "M&E Methods", "M&E Specialists", "M&E Professionals", "MEAL Workshops",
]


def main():
    total = 0
    for lang in ["hi", "ta", "bn", "mr"]:
        for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            d = json.load(open(path, encoding="utf-8"))
            ch = 0
            for label in PROTECT:
                if label in d and d[label] != label:
                    d[label] = label
                    ch += 1
            if ch:
                json.dump(d, open(path, "w", encoding="utf-8"),
                          ensure_ascii=False, separators=(",", ":"))
                total += ch
    print(f"Total pass-6 protected-label enforcements: {total}")


if __name__ == "__main__":
    main()
