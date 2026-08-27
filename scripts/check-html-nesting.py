#!/usr/bin/env python3
"""Blog posts must have balanced block markup.

The share / newsletter / related-posts tail is duplicated verbatim across every
post in blog/, which makes splicing a new body into an existing post's shell the
obvious way to write one. That is how #1033 happened: the split point was
`<div class="share-section">` and the `</div>` closing `.article-content` sat
immediately before it, so it went with the old body. The newsletter block then
became a descendant of `.article-content` and inherited

    .article-content a { color: var(--accent-color); text-decoration: underline }

which made the Substack button blue link text on a blue gradient. Nothing
errored. The page rendered. `check-h1-survives-chrome` and `check-viewport`
both passed, because the h1 and the viewport meta were fine.

A second, older instance was latent rather than visible: p-values-and-confidence
-intervals.html had the same unclosed `.article-content`, with no styling
symptom, waiting for someone to add a rule that would give it one.

So this checks nesting, not appearance: every element that opens must close, in
order. It is deliberately narrow -- the tag stack only, no attribute or CSS
opinions -- so it stays quiet unless the markup is genuinely malformed.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Void elements never close. `p` and `li` are omitted-end-tag elements in HTML5
# and are legitimately left open all over this repo, so they are not tracked.
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
UNTRACKED = VOID | {"p", "li", "dt", "dd", "option", "thead", "tbody", "tfoot",
                    "tr", "td", "th", "colgroup", "optgroup", "rt", "rp"}

EXEMPT = {}   # path -> reason. A stale entry fails too (see below).


class Nesting(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.problems = [], []

    def handle_starttag(self, tag, attrs):
        if tag in UNTRACKED:
            return
        self.stack.append((tag, self.getpos()[0], dict(attrs).get("class", "")))

    def handle_endtag(self, tag):
        if tag in UNTRACKED:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for j in range(len(self.stack) - 1, i, -1):
                    self.problems.append(("never closed",) + self.stack[j])
                del self.stack[i:]
                return
        self.problems.append(("closed but never opened", tag, self.getpos()[0], ""))

    def finish(self):
        for item in reversed(self.stack):
            self.problems.append(("never closed",) + item)
        return self.problems


def main():
    files = sorted(ROOT.joinpath("blog").glob("*.html"))
    if not files:
        print("FAIL - no files found in blog/")
        return 1

    exempt = {ROOT / k for k in EXEMPT}
    failures, checked = [], 0
    for f in files:
        rel = f.relative_to(ROOT).as_posix()
        p = Nesting()
        try:
            p.feed(f.read_text(encoding="utf-8"))
        except Exception as exc:                      # a parse error is a failure
            failures.append((rel, [("unparseable", str(exc)[:80], 0, "")]))
            continue
        problems = p.finish()
        if f in exempt:
            if not problems:
                failures.append((rel, [("exemption is stale: this file is fine now", "", 0, "")]))
            continue
        checked += 1
        if problems:
            failures.append((rel, problems))

    for k in EXEMPT:
        if not (ROOT / k).exists():
            failures.append((k, [("exemption is stale: file no longer exists", "", 0, "")]))

    if failures:
        print("FAIL - %d file(s) in blog/ have unbalanced markup:" % len(failures))
        for rel, problems in failures:
            print("  %s" % rel)
            for kind, tag, line, cls in problems[:6]:
                where = " line %s" % line if line else ""
                what = "<%s%s>" % (tag, ' class="%s"' % cls if cls else "")
                print("      %s  %s%s" % (kind, what, where))
            if len(problems) > 6:
                print("      ... and %d more" % (len(problems) - 6))
        print("\nA missing </div> does not error and does not show up in any other")
        print("guard: the page still renders, with the later blocks nested inside")
        print("the earlier one and inheriting its styles. See #1033.")
        return 1

    print("PASS - block markup nests correctly in all %d blog post(s)%s."
          % (checked, " (%d exempted on purpose)" % len(EXEMPT) if EXEMPT else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
