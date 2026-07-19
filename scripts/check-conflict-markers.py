#!/usr/bin/env python3
"""Merge-conflict-marker guard.

Fails if any tracked text file contains git conflict markers — the exact
failure that shipped `<<<<<<< Updated upstream` to the live homepage,
broke site search (invalid search-index.json), and corrupted the sitemap
on 2026-07-19 (PR #817, a `git stash pop` committed unresolved).

The local pre-commit hook already checks this, but hooks only run where
`npm install` has set core.hooksPath and can be skipped with --no-verify.
CI cannot be skipped.

Only the distinctive marker forms are matched (`<<<<<<< ` and `>>>>>>> `
at line start, with the ref suffix); a bare `=======` line is NOT flagged
because Markdown uses it as a heading underline.
"""

import re
import subprocess
import sys

MARKER = re.compile(r"^(<{7} |>{7} |\|{7} )")
SKIP_DIRS = ("Backups/", "node_modules/", ".git/")
SKIP_FILES = ("scripts/check-conflict-markers.py",)
BINARY_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf",
              ".woff", ".woff2", ".ttf", ".eot", ".mp3", ".mp4", ".zip",
              ".xlsx", ".pptx", ".docx")


def main():
    files = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    ).stdout.splitlines()

    hits = []
    for path in files:
        if path.startswith(SKIP_DIRS) or path in SKIP_FILES:
            continue
        if path.lower().endswith(BINARY_EXT):
            continue
        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                for lineno, line in enumerate(f, 1):
                    if MARKER.match(line):
                        hits.append(f"{path}:{lineno}: {line.strip()[:60]}")
        except (OSError, IsADirectoryError):
            continue

    if hits:
        print(f"FAIL — {len(hits)} merge-conflict marker(s) found:\n")
        for h in hits:
            print(f"  {h}")
        print("\nResolve the conflicts before merging — these render as "
              "garbled text on the live site and can break JSON/XML files.")
        return 1

    print(f"PASS — no merge-conflict markers in {len(files)} tracked files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
