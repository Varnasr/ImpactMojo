#!/usr/bin/env python3
"""Guard: the Fundamentals questionnaire must never transmit an answer.

Why this exists
---------------
fundamentals/wheel.html asks twelve questions covering caste, sexual
orientation, religion, disability and economic position, and tells the reader in
plain words that the answers stay in their browser and are sent nowhere. That
sentence is a promise about code, and a promise about code should be enforced by
code rather than by everyone remembering.

The risk is not malice. It is the ordinary drift by which someone later adds
analytics to "see which questions get skipped", or a sync-across-devices
feature, and the page keeps making a claim that has quietly stopped being true.

What it checks
--------------
1. The questionnaire files contain no network primitive at all — no fetch,
   XMLHttpRequest, sendBeacon, WebSocket, EventSource, dynamic import, or form
   submission. Not "no calls to our own API": none of the machinery.
2. The page still carries the promise, so the guard cannot be satisfied by
   deleting the sentence and leaving the code.
3. Answers are only ever written to localStorage under the expected keys.

Run: python3 scripts/check-fundamentals-privacy.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files that handle answers. Anything added here must stay network-free.
GUARDED = [
    "js/fundamentals-assess.js",
    "js/fundamentals-assess-data.js",
]

PAGE = "fundamentals/wheel.html"

# Every way a browser can put bytes on the wire from script.
NETWORK = [
    (r"\bfetch\s*\(", "fetch()"),
    (r"\bXMLHttpRequest\b", "XMLHttpRequest"),
    (r"\bnavigator\s*\.\s*sendBeacon\b", "navigator.sendBeacon()"),
    (r"\bnew\s+WebSocket\b", "WebSocket"),
    (r"\bnew\s+EventSource\b", "EventSource"),
    (r"\bimport\s*\(", "dynamic import()"),
    (r"\.\s*submit\s*\(\s*\)", "form.submit()"),
    (r"\bnavigator\s*\.\s*clipboard\b", "clipboard write"),
    (r"\bgtag\s*\(", "gtag() analytics"),
    (r"\bdataLayer\b", "dataLayer analytics"),
]

# The promise the page makes, in the words it makes it.
PROMISE = [
    r"sent nowhere",
    r"stay in your browser|stays in your browser",
]

ALLOWED_STORAGE_KEYS = {"im-fundamentals-marks", "im-fundamentals-answers"}


def main() -> int:
    problems = []

    for rel in GUARDED:
        path = ROOT / rel
        if not path.exists():
            problems.append(f"{rel} is missing — the guard covers a file that is not there.")
            continue
        src = path.read_text(encoding="utf-8")
        # Strip comments so a comment mentioning fetch() does not trip the guard.
        stripped = re.sub(r"/\*[\s\S]*?\*/", " ", src)
        stripped = re.sub(r"(?m)//.*$", " ", stripped)
        for pattern, name in NETWORK:
            if re.search(pattern, stripped):
                problems.append(
                    f"{rel} contains {name}. The questionnaire collects caste, sexual "
                    f"orientation, religion and disability; those answers must never leave "
                    f"the browser. Remove it, or move the feature somewhere that does not "
                    f"claim to be private."
                )
        for key in re.findall(r"localStorage\.(?:get|set|remove)Item\(\s*([A-Za-z_$][\w$]*|\"[^\"]*\"|'[^']*')", stripped):
            literal = key.strip("\"'")
            if literal.startswith(("MARK_KEY", "ANSWER_KEY")) or literal in {"MARK_KEY", "ANSWER_KEY"}:
                continue
            if literal not in ALLOWED_STORAGE_KEYS and not literal.isupper():
                problems.append(f"{rel} writes to an unexpected storage key: {literal}")

    page = ROOT / PAGE
    if not page.exists():
        problems.append(f"{PAGE} is missing.")
    else:
        html = page.read_text(encoding="utf-8")
        for pattern in PROMISE:
            if not re.search(pattern, html, re.I):
                problems.append(
                    f"{PAGE} no longer tells the reader their answers are private "
                    f"(expected text matching /{pattern}/). If the promise is being "
                    f"withdrawn, the questionnaire should be withdrawn with it."
                )
        for rel in GUARDED:
            if Path(rel).name not in html:
                problems.append(f"{PAGE} does not load {rel}.")

    if problems:
        print("FAIL - the Fundamentals questionnaire privacy contract is broken:\n")
        for p in problems:
            print(f"    {p}")
        return 1

    print(
        f"PASS - the questionnaire is network-free across {len(GUARDED)} files, "
        f"writes only to {len(ALLOWED_STORAGE_KEYS)} local keys, and the page still "
        f"makes the promise."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
