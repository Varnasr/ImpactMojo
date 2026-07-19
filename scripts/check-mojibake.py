#!/usr/bin/env python3
"""Mojibake / encoding-corruption guard for the ImpactMojo repo.

WHY: the site previously suffered character-encoding corruption ("mojibake") —
UTF-8 punctuation (em-dashes, ellipses, bullets, smart quotes) saved through a
broken CP1252/Latin-1 round-trip and resurfacing as garbage such as Ã©, â€™, "¢,
or founders""¦. One such remnant in js/faq-bank.js silently broke an entire
script in production. This guard fails CI if any KNOWN mojibake signature
reappears, so the problem can never quietly creep back in.

DESIGN: detection only (never auto-fix — the correct replacement needs human
intent). Patterns are deliberately HIGH-SIGNAL / zero-false-positive: they do
NOT flag legitimate Unicode the site uses on purpose — real em-dash, ellipsis,
rupee sign, (C), section sign, middot, plus-minus, smart quotes, or the
Devanagari / Tamil / Bengali / Marathi i18n strings.

USAGE:
    python3 scripts/check-mojibake.py            # scan; exit 1 if any found
    python3 scripts/check-mojibake.py --verbose  # also list clean files
"""
import os, re, sys

# (label, regex) — each pattern matches ONLY corruption, never legitimate text.
# Codepoints are spelled with \u escapes so the patterns stay readable/reliable.
PATTERNS = [
    ("A-tilde + em-dash (corrupted multiplication sign, e.g. a \u00d7 close button)",
     re.compile('\u00c3\u2014')),
    ("eth + Latin-cap-Y mojibake (corrupted 4-byte emoji, e.g. \U0001f9ed)",
     re.compile('\u00f0\u0178')),
    ("U+FFFD replacement char",
     re.compile('�')),
    ("C1 control char (U+0080-U+009F)",
     re.compile('[-]')),
    ("A-tilde mojibake (corrupted accented latin: e-acute, n-tilde, u-uml)",
     re.compile('Ã[ -¿]')),
    ("A-circumflex mojibake (corrupted degree/copyright/registered/nbsp)",
     re.compile('Â[ £©®°·½]')),
    ("a-circumflex+euro mojibake (corrupted smart quotes/dashes/ellipsis)",
     re.compile('â[€‚™]')),
    ('collapsed punctuation (double-quote + cent/broken-bar: was bullet/ellipsis)',
     re.compile('"[¢¦]')),
]

TEXT_EXTS = (".html", ".htm", ".js", ".mjs", ".ts", ".json", ".css", ".md",
             ".txt", ".xml", ".svg", ".csv", ".yml", ".yaml", ".toml")
SKIP_DIRS = {".git", "node_modules", "Backups", ".netlify", "dist", "build", ".cache",
             # Claude's internal notes/rules/skills — NOT shipped to the site, and the
             # place where mojibake examples are legitimately documented for reference.
             ".claude"}


def iter_files(root="."):
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            # skip this guard's own source: its regexes necessarily contain the
            # very characters it hunts for.
            if fn == "check-mojibake.py":
                continue
            if fn.endswith(TEXT_EXTS):
                yield os.path.join(dirpath, fn)


def scan_file(path):
    out = []
    try:
        text = open(path, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError) as e:
        # a tracked text file that isn't valid UTF-8 is itself a corruption signal
        out.append((0, 0, "not valid UTF-8", str(e)[:60]))
        return out
    for i, line in enumerate(text.split("\n"), 1):
        for label, rx in PATTERNS:
            for m in rx.finditer(line):
                snippet = line[max(0, m.start() - 30):m.start() + 20].strip()
                out.append((i, m.start() + 1, label, snippet))
    return out


def main():
    verbose = "--verbose" in sys.argv
    total = bad_files = 0
    for path in sorted(iter_files()):
        hits = scan_file(path)
        if hits:
            bad_files += 1
            print("\nFAIL  " + path)
            for line, col, label, snippet in hits:
                total += 1
                loc = f"{line}:{col}" if line else "file"
                print(f"    {loc:>9}  {label}")
                print(f"               ...{snippet}...")
        elif verbose:
            print("ok    " + path)
    print("\n" + "=" * 64)
    if total:
        print(f"FAIL - {total} mojibake hit(s) across {bad_files} file(s).")
        print("Each is an encoding-corruption signature. Replace it with the")
        print("intended character (em-dash, ellipsis, bullet, quote, (C), ...).")
        return 1
    print("PASS - no mojibake signatures found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
