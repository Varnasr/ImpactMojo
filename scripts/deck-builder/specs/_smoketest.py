"""Smoke test spec — validates the builder end to end. Not a real course."""
DECK = {
    "slug": "_smoketest",
    "title": "Smoke Test 101",
    "description": "Builder smoke test.",
    "slides": [
        {"type": "title", "main": "Smoke<br>Test<br>101", "sub": "Validating the deck builder.",
         "tags": ["Test", "100 Slides"]},
        {"type": "toc", "title": "What We Cover",
         "items": [{"name": "Section One", "slides": "Slides 3-4"},
                   {"name": "Section Two", "slides": "Slides 5-6"}]},
        {"type": "divider", "num": "01", "label": "Section One", "title": "A Section Divider"},
        {"type": "content", "label": "Demo", "title": "Components Showcase", "titleSize": "md",
         "blocks": [
             {"t": "body", "html": "A paragraph of <strong>body</strong> text to verify rendering."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "68%", "label": "Some metric", "color": "green", "source": "Source 2024"},
                 {"num": "1.2x", "label": "Another", "color": "amber"},
                 {"num": "₹4.3L", "label": "Third", "color": "indigo"}]},
             {"t": "bullets", "color": "cyan", "items": ["First point", "Second point"]},
         ]},
        {"type": "content", "label": "Charts", "title": "A Chart Slide",
         "blocks": [
             {"t": "chart", "canvas": "smokeChart", "title": "Demo Bar", "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["A", "B", "C"], "datasets": [{"label": "x", "data": [3, 5, 2],
                       "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{ legend:{ display:false } } }"}},
         ]},
        {"type": "end", "headline": "Thank You", "byline": "End of smoke test.",
         "ctas": [{"label": "Home", "href": "https://www.impactmojo.in"}]},
    ],
}
