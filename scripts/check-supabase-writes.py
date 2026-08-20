#!/usr/bin/env python3
"""Supabase write-path guard.

Two failures hid the same bug for eight months, and this guards both.

`user_progress` had 0 rows ever inserted against 17,022 reads, while the
code that writes it looked fine. Two things kept that invisible:

  1. The call discarded its result:

         await sb.from('user_progress').upsert({ ... });

     supabase-js RESOLVES with { data, error } — it does not throw. A
     rejected insert is therefore indistinguishable from a successful one
     unless you read `error`. The surrounding try/catch could never fire.

  2. Nothing ever asserted that a table the code writes to had in fact
     received a write.

STATIC mode (default, no credentials, runs on every push) catches (1): a
write whose result is thrown away, or captured and never checked.

LIVE mode (--live, needs SUPABASE_PAT, scheduled only) catches (2): for
every table the code writes to, assert pg_stat_user_tables.n_tup_ins > 0.
A table with a writer that has never once received a row is either a dead
feature or a broken one; both are worth knowing.

A line can opt out with the token "write-ignore" (e.g. a deliberate
fire-and-forget where losing the write is genuinely acceptable).

Usage:
  python3 scripts/check-supabase-writes.py           # static, exit 1 on findings
  python3 scripts/check-supabase-writes.py --live    # also probe insert counts
  python3 scripts/check-supabase-writes.py --list    # show every write call found
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_PREFIXES = ("Backups/", "node_modules/", "tests/", "netlify-resource-template/")
SCAN_SUFFIXES = (".js", ".html", ".mjs")

# A write through PostgREST or Storage: `.from('t')` … then a mutating verb.
#
# Written to be linear-time. An earlier version used a nested optional group
# with `[^;]*?` inside a `.*?` lead, which backtracked catastrophically on a
# long line and hung — and a guard that hangs is worse than no guard, because
# a hung CI job neither passes nor fails, it just reads as "still running".
#
# So: match `.from('table')` on its own, then look at the bounded text that
# follows to find the verb. No nested quantifiers, nothing to backtrack into.
FROM_RE = re.compile(
    r"""(?P<obj>[A-Za-z_$][\w$.]*)
        \.(?:storage\.)?from\(\s*['"](?P<table>[A-Za-z_]\w*)['"]\s*\)
    """,
    re.VERBOSE,
)
VERBS = ("insert", "upsert", "update", "delete", "upload", "remove")
# How much of the chain after `.from('t')` may be searched for the verb.
CHAIN_WINDOW = 300


def verb_after(tail):
    """First mutating verb in the method chain following `.from('t')`.

    Deliberately a plain scan rather than a regex: the chain is unbounded in
    shape, and any regex expressing it needs nested quantifiers, which is what
    made the first version of this guard hang. Stops at `;` so a later
    statement on the same line cannot be attributed to this call.
    """
    stop = tail.find(";")
    window = tail[:stop] if stop != -1 else tail[:CHAIN_WINDOW]
    best, pos = None, len(window) + 1
    for v in VERBS:
        i = window.find("." + v + "(")
        if i == -1:
            i = window.find(". " + v + "(")
        if i != -1 and i < pos:
            best, pos = v, i
    return best

OPT_OUT = "write-ignore"
# How far after the call to look for a check of the captured result.
LOOKAHEAD = 20


def tracked_files():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         cwd=ROOT, check=True).stdout.splitlines()
    return [f for f in out
            if f.endswith(SCAN_SUFFIXES) and not f.startswith(SKIP_PREFIXES)]


THEN_RE = re.compile(r"\.\s*then\s*\(\s*(?:async\s+)?(?:function\s*)?\(?\s*"
                     r"(?P<param>[A-Za-z_$][\w$]*)?")


def then_checks_error(tail):
    """True when the call is consumed by .then(cb) and cb inspects `.error`.

    supabase-js is promise-based, so this is a legitimate way to handle a
    failure and must not be reported. `.then(function () {…})` with no
    parameter cannot inspect anything, so it stays a finding.
    """
    m = THEN_RE.search(tail[:CHAIN_WINDOW])
    if not m:
        return False
    param = m.group("param")
    if not param:
        return False
    body = tail[m.end(): m.end() + CHAIN_WINDOW * 2]
    return re.search(rf"\b{re.escape(param)}\s*(?:\.|\?\.)\s*error\b", body) is not None


def classify(lines, idx, col, tail):
    """Return (status, detail). status in {'ok','discarded','unchecked'}."""
    if then_checks_error(tail):
        return "ok", "handled in .then callback"

    # Everything on the line before this call decides how its result is handled.
    before = lines[idx][:col].rstrip()
    if before.endswith("await"):
        before = before[:-len("await")].rstrip()

    # Destructured: `var { error } = await ...` / `const { data, error } = ...`
    destructured = re.search(r"\{([^{}]*)\}\s*=\s*$", before)
    if destructured:
        names = [n.strip().split(":")[-1].strip()
                 for n in destructured.group(1).split(",")]
        if any(n == "error" or n.endswith("Error") for n in names):
            return "ok", "destructured error"
        # `{ data } = await ...` — data captured, error dropped
        return "unchecked", "destructures result but not `error`"

    # Assigned to a variable: `var res = await ...`
    assigned = re.search(r"(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*$", before)
    if assigned:
        var = assigned.group(1)
        window = "\n".join(lines[idx: idx + LOOKAHEAD])
        if re.search(rf"\b{re.escape(var)}\s*(?:\.|\?\.)\s*error\b", window):
            return "ok", f"checks {var}.error"
        return "unchecked", f"captures result as `{var}` but never reads {var}.error"

    # Plain assignment to an existing name, or a return — treat as captured.
    if re.search(r"(?:=|return)\s*$", before):
        return "ok", "result returned or assigned"

    # Nothing captures it at all.
    return "discarded", "result discarded — a rejected write is indistinguishable from success"


def scan():
    findings, calls = [], []
    for rel in tracked_files():
        path = ROOT / rel
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if ".from(" not in text:
            continue
        lines = text.splitlines()
        # Offset of the first character of each line, so a match anywhere in
        # the file maps back to a line. The chain is searched across the whole
        # text, not just the rest of one line: formatting a long call over
        # several lines must not make the guard go blind to it. (It did —
        # reformatting four calls dropped the detected count from 17 to 13.)
        starts, off = [], 0
        for ln in lines:
            starts.append(off)
            off += len(ln) + 1

        def line_of(pos):
            lo, hi = 0, len(starts) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if starts[mid] <= pos:
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        for m in FROM_RE.finditer(text):
            verb = verb_after(text[m.end():m.end() + CHAIN_WINDOW])
            if verb is None:
                continue                          # a read, not a write
            idx = line_of(m.start())
            if OPT_OUT in lines[idx]:
                continue
            table = m.group("table")
            calls.append((rel, idx + 1, table, verb))
            status, detail = classify(lines, idx, m.start() - starts[idx],
                                      text[m.end():])
            if status != "ok":
                findings.append((rel, idx + 1, table, verb, status, detail,
                                 lines[idx].strip()[:100]))
    return findings, calls


# ----------------------------------------------------------------- live mode

def live_insert_counts(tables):
    """n_tup_ins per table via the Supabase Management API. Needs SUPABASE_PAT."""
    pat = os.environ.get("SUPABASE_PAT")
    if not pat:
        return None, "SUPABASE_PAT is not set"
    ref = "ddyszmfffyedolkcugld"
    names = ",".join("'%s'" % t.replace("'", "") for t in sorted(tables))
    sql = ("select relname, n_tup_ins from pg_stat_user_tables "
           f"where schemaname='public' and relname in ({names});")
    req = urllib.request.Request(
        f"https://api.supabase.com/v1/projects/{ref}/database/query",
        data=json.dumps({"query": sql}).encode(),
        headers={"Authorization": f"Bearer {pat}",
                 "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            rows = json.loads(r.read().decode())
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        return None, f"query failed: {e}"
    return {row["relname"]: row["n_tup_ins"] for row in rows}, None


def main(argv):
    findings, calls = scan()

    if "--list" in argv:
        print(f"{len(calls)} Supabase write calls across "
              f"{len({c[0] for c in calls})} files:\n")
        for rel, ln, table, verb in sorted(calls):
            print(f"  {rel}:{ln}  {verb:<6} -> {table}")
        return 0

    failed = False

    if findings:
        failed = True
        print(f"FAIL - {len(findings)} Supabase write(s) whose failure would be "
              f"silent:\n")
        for rel, ln, table, verb, status, detail, src in findings:
            print(f"  {rel}:{ln}")
            print(f"      {verb} -> {table}: {detail}")
            print(f"      {src}")
        print("\n  supabase-js resolves with { data, error } rather than throwing,")
        print("  so a try/catch around one of these cannot fire. Destructure")
        print("  `error` and act on it, or mark the line `write-ignore` if losing")
        print("  the write is genuinely acceptable.")
    else:
        print(f"PASS - all {len(calls)} Supabase writes surface their errors.")

    if "--live" in argv:
        tables = sorted({c[2] for c in calls})
        counts, err = live_insert_counts(tables)
        print()
        if err:
            print(f"SKIP - live insert-count probe not run ({err}).")
        else:
            never = [t for t in tables
                     if t in counts and counts[t] == 0]
            absent = [t for t in tables if t not in counts]
            for t in sorted(counts):
                mark = "never written" if counts[t] == 0 else f"{counts[t]} inserts"
                print(f"  {t:<28} {mark}")
            if absent:
                print(f"\n  not present in this database: {', '.join(absent)}")
            if never:
                failed = True
                print(f"\nFAIL - {len(never)} table(s) have writing code but have "
                      f"NEVER received a row:")
                for t in never:
                    print(f"    {t}")
                print("\n  Either the feature is broken or it was never wired to a")
                print("  UI. Both are worth knowing; neither should be silent.")
            else:
                print("\nPASS - every table with a writer has received writes.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
