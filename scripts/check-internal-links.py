#!/usr/bin/env python3
"""Internal-link guard.

Checks every internal href/src across tracked HTML files against the
files that actually exist, the way Netlify resolves them:

  - pretty URLs:      /teach        -> teach.html
  - directory links:  /courses/mel/ -> courses/mel/index.html
  - case-insensitive: /labs/X.html matches Labs/X.html
  - netlify.toml redirect sources count as resolvable

External links (http/https/mailto/tel), pure fragments (#...), and
template/data URLs are ignored — the advisory lychee CI job covers the
external web. This guard is strict about what we fully control: links
between our own pages.

Exit 0 + PASS when clean; exit 1 with a file:line listing otherwise.
"""

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

SKIP_FILE_PREFIXES = ("Backups/", "node_modules/", "netlify-resource-template/",
                      "netlify-env-files/", "tests/", "ops/", "docs/",
                      "scripts/templates/")  # relative links valid only post-instantiation
SKIP_TARGET_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "data:",
                        "javascript:", "blob:", "{", "${", "whatsapp:")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         cwd=ROOT, check=True).stdout.splitlines()
    return out


def load_redirect_sources():
    """Exact and prefix redirect sources from netlify.toml."""
    exact, prefixes = set(), []
    toml = (ROOT / "netlify.toml").read_text(encoding="utf-8")
    for m in re.finditer(r'from\s*=\s*"([^"]+)"', toml):
        src = m.group(1)
        if "*" in src or ":" in src:
            prefixes.append(src.split("*")[0].split(":")[0].lower())
        else:
            exact.add(src.lower())
    # edge functions declare their routes in export const config = { path: ... }
    for ef in (ROOT / "netlify" / "edge-functions").glob("*.ts"):
        src_text = ef.read_text(encoding="utf-8", errors="ignore")
        cfg = re.search(r"export\s+const\s+config\s*=\s*\{(.*?)\}", src_text, re.S)
        if cfg:
            for pm in re.finditer(r'["\'](/[^"\']+)["\']', cfg.group(1)):
                route = pm.group(1)
                if "*" in route or ":" in route:
                    prefixes.append(route.split("*")[0].split(":")[0].lower())
                else:
                    exact.add(route.lower())
    return exact, prefixes


def main():
    files = tracked_files()
    disk = {}  # lowercase path -> real path
    disk_dirs = set()
    for f in files:
        disk[f.lower()] = f
        parts = f.split("/")
        for i in range(1, len(parts)):
            disk_dirs.add("/".join(parts[:i]).lower())

    redirect_exact, redirect_prefixes = load_redirect_sources()

    def resolves(target, basedir):
        t = unquote(target).split("#", 1)[0].split("?", 1)[0]
        if not t:
            return True  # pure fragment/query
        if t.startswith("/"):
            rel = t[1:]
        else:
            joined = (Path(basedir) / t)
            try:
                rel = str(joined.resolve().relative_to(ROOT))
            except ValueError:
                return True  # escapes root — let lychee judge
        rel = rel.rstrip("/")
        low = rel.lower()
        if low == "":
            return True  # site root
        if low in disk:
            return True
        if low + "/index.html" in disk or low + "/index.htm" in disk:
            return True
        if low + ".html" in disk:   # pretty URL (works even when a same-named dir exists)
            return True
        if low in disk_dirs:
            # directory with no index.html and no .html sibling — Netlify 404s
            return False
        path_form = "/" + low
        if path_form in redirect_exact:
            return True
        for p in redirect_prefixes:
            if p and path_form.startswith(p):
                return True
        return False

    attr = re.compile(r'\b(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)
    broken = []
    checked = 0
    for f in files:
        if not f.endswith(".html") or f.startswith(SKIP_FILE_PREFIXES):
            continue
        if "_template" in f or "/PAGE-TEMPLATE" in f or f.startswith("PAGE-TEMPLATE"):
            continue  # placeholder links ([URL], /courses/[COURSE]/) by design
        checked += 1
        text = (ROOT / f).read_text(encoding="utf-8", errors="ignore")
        # ignore script/style bodies — templates and JS-built URLs live there
        # (replace with equivalent newlines so reported line numbers stay true)
        text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>",
                      lambda m: "\n" * m.group(0).count("\n"), text,
                      flags=re.S | re.I)
        basedir = str((ROOT / f).parent)
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in attr.finditer(line):
                t = m.group(1).strip()
                if not t or t.startswith(SKIP_TARGET_PREFIXES) or t.startswith("#"):
                    continue
                if not resolves(t, basedir):
                    broken.append(f"{f}:{lineno}: {t}")

    if broken:
        print(f"FAIL — {len(broken)} broken internal link(s) across {checked} pages:\n")
        for b in broken[:200]:
            print(f"  {b}")
        if len(broken) > 200:
            print(f"  … and {len(broken) - 200} more")
        return 1
    print(f"PASS — all internal links resolve across {checked} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
