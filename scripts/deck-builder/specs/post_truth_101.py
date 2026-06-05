# -*- coding: utf-8 -*-
"""
Post-Truth Politics 101 — ImpactMojo 101 Series (native deck spec)
How emotion, identity and falsehood beat facts — and how to build resilience.
Build: python3 scripts/deck-builder/build.py post_truth_101
"""

DECK = {
    "slug": "post-truth-101",
    "title": "Post-Truth Politics 101",
    "description": ("Post-Truth Politics 101 — a free foundational course for development "
                    "practitioners, communicators and citizens in South Asia on why emotion, "
                    "identity and falsehood beat facts: from mis- and disinformation to echo "
                    "chambers, the believing brain, the attention economy, synthetic media and "
                    "building resilience through media literacy. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Post-Truth<br>Politics<br>101",
         "sub": "Why Emotion &amp; Identity Beat Facts &mdash; and How to Build Resilience. "
                "A Foundational Course for Practitioners, Communicators &amp; Citizens in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What 'Post-Truth' Means"},
             {"name": "A Taxonomy of Falsehood"},
             {"name": "How Falsehoods Spread"},
             {"name": "Echo Chambers &amp; Filter Bubbles"},
             {"name": "The Believing Brain"},
             {"name": "Propaganda &amp; Manufacturing Consent"},
             {"name": "The Attention Economy"},
             {"name": "Synthetic Media"},
             {"name": "Polarisation"},
             {"name": "Why It Matters for Development"},
             {"name": "Building Resilience"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What &lsquo;Post-Truth&rsquo; Means"},

        {"type": "content", "label": "Word of the Year", "title": "'Post-truth' is the word of an era",
         "blocks": [
             {"t": "body", "html": "In 2016, in the wake of Brexit and the US election, "
              "<strong>Oxford Dictionaries</strong> named <em>post-truth</em> its Word of the "
              "Year &mdash; reporting a roughly twenty-fold spike in usage over the previous year."},
             {"t": "term", "word": "Post-truth",
              "def": "Relating to circumstances in which objective facts are less influential in "
              "shaping public opinion than appeals to emotion and personal belief. "
              "(Oxford Dictionaries Word of the Year, 2016.)"},
             {"t": "hbox", "color": "cyan", "html": "'Post' here does not mean facts have "
              "vanished. It means they no longer settle the argument."},
         ]},

        {"type": "content", "label": "The Shift", "title": "When feelings outrank facts",
         "blocks": [
             {"t": "body", "html": "Post-truth is not simply lying &mdash; lying is as old as "
              "speech. What is new is a public sphere where <strong>how a claim makes you feel</strong>, "
              "and <strong>whose side it signals</strong>, matter more than whether it is true."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Old contest", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Rival claims judged against shared evidence; "
                   "being caught wrong carried a cost."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Post-truth contest", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Claims judged by identity and emotion; "
                   "a fact-check can even harden belief."}]}]},
         ]},

        {"type": "content", "label": "Not New, but Newly Powerful", "title": "Old impulse, new infrastructure",
         "blocks": [
             {"t": "body", "html": "Rumour, propaganda and demagoguery are ancient. What "
              "amplifies them now is <strong>infrastructure</strong>: smartphones in billions of "
              "pockets, algorithmic feeds, group chats and an economy that pays for attention."},
             {"t": "flow", "steps": [
                 "ANCIENT: rumour, oratory, pamphlets",
                 "BROADCAST: press, radio, television",
                 "NETWORKED: social media, group chats",
                 "GENERATIVE: synthetic text, image &amp; video at scale"]},
         ]},

        {"type": "content", "label": "Truth Decay", "title": "Four symptoms of a post-truth public sphere",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Disagreement about facts</strong>, not just values &mdash; even on the verifiable",
                 "<strong>A blurred line</strong> between opinion and fact in how news is consumed",
                 "<strong>Rising volume and influence</strong> of opinion over reporting",
                 "<strong>Declining trust</strong> in once-respected sources of information"]},
             {"t": "hbox", "color": "amber", "html": "The RAND Corporation calls this cluster "
              "'Truth Decay'. None of the four requires anyone to tell an outright lie."},
         ]},

        {"type": "content", "label": "Why It Matters Here", "title": "South Asia is a front line, not a footnote",
         "blocks": [
             {"t": "body", "html": "With hundreds of millions of new, mobile-first internet users, "
              "dozens of languages and dense kinship and faith networks, South Asia is where "
              "post-truth dynamics play out at their largest human scale &mdash; often with "
              "<strong>life-and-death stakes</strong>."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Mobile-first", "label": "Most users came online on a phone, via cheap data, "
                  "into closed messaging groups", "color": "cyan"},
                 {"num": "Many languages", "label": "Falsehood travels in tongues most fact-checking "
                  "tools barely cover", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Scope", "title": "What this course will and won't do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "We will", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Name the mechanisms behind post-truth",
                      "Show how falsehood spreads and persuades",
                      "Build practical habits of resilience"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "We won't", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Pick a political side",
                      "Pretend any one tribe alone is fooled",
                      "Offer a tidy technological fix"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Susceptibility to falsehood is human, not "
              "partisan. That humility is the starting point."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Diagnosis", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Types of falsehood and how they spread",
                      "Bubbles, the believing brain, propaganda",
                      "The attention economy and synthetic media"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Response", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Polarisation and its real-world harms",
                      "Why it matters for development",
                      "Fact-checking, prebunking and media literacy"]}]}]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "A Taxonomy of Falsehood"},

        {"type": "content", "label": "Precision Helps", "title": "Not all falsehood is the same",
         "blocks": [
             {"t": "body", "html": "Lumping everything together as 'fake news' hides what matters: "
              "<strong>was it meant to deceive, and was it meant to harm?</strong> Those two "
              "questions sort the field into three useful categories."},
             {"t": "hbox", "color": "amber", "html": "The term 'fake news' is now so weaponised "
              "&mdash; used to dismiss inconvenient reporting &mdash; that researchers prefer the "
              "sharper words that follow."},
         ]},

        {"type": "content", "label": "The Core Distinction", "title": "Mis-, dis- and mal-information",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "False?", "Intent to harm?", "Example"],
              "rows": [
                  ["Misinformation", "Yes", "No", "Sharing a wrong cure, believing it true"],
                  ["Disinformation", "Yes", "Yes", "A fabricated rumour seeded to incite a riot"],
                  ["Malinformation", "No (mostly true)", "Yes", "Leaking private data to harm someone"]]},
             {"t": "hbox", "color": "cyan", "html": "Framework: Wardle &amp; Derakhshan (Council "
              "of Europe, 2017). The axes are <em>falseness</em> and <em>intent to harm</em>."},
         ]},

        {"type": "content", "label": "Misinformation", "title": "False, but shared in good faith",
         "blocks": [
             {"t": "term", "word": "Misinformation",
              "def": "False or misleading information spread without intent to deceive. The sharer "
              "believes it is true &mdash; an anxious relative forwarding a bogus health tip."},
             {"t": "hbox", "color": "amber", "html": "Most of what floods family group chats is "
              "misinformation, not disinformation. It is sincere &mdash; and that sincerity is "
              "exactly what makes it travel."},
         ]},

        {"type": "content", "label": "Disinformation", "title": "False, and weaponised on purpose",
         "blocks": [
             {"t": "term", "word": "Disinformation",
              "def": "False information created and spread deliberately to deceive, manipulate or "
              "harm &mdash; for political, financial or social gain."},
             {"t": "body", "html": "Disinformation is engineered. It is seeded by actors who know "
              "it is false and design it to <strong>exploit a fault line</strong> &mdash; a "
              "communal tension, an election, a fear."},
         ]},

        {"type": "content", "label": "Malinformation", "title": "True, but deployed to wound",
         "blocks": [
             {"t": "term", "word": "Malinformation",
              "def": "Genuine information taken out of context, or private information exposed, "
              "in order to cause harm &mdash; doxxing, leaks, selective truths."},
             {"t": "hbox", "color": "red", "html": "Malinformation is the trickiest, because the "
              "facts check out. The deception is in the framing, the timing and the omission."},
         ]},

        {"type": "content", "label": "The Family of Falsehood", "title": "Rumour, propaganda, hoax, satire",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Form", "What it is"],
              "rows": [
                  ["Rumour", "Unverified claim passed on, often filling an information vacuum"],
                  ["Propaganda", "Information shaped to promote a cause, true or false"],
                  ["Hoax", "A deliberate fabrication designed to be believed"],
                  ["Satire / parody", "False on purpose, but meant to be understood as a joke"],
                  ["Clickbait", "Misleading framing engineered to harvest clicks"],
                  ["Conspiracy theory", "An all-explaining secret-plot narrative, resistant to evidence"]]},
         ]},

        {"type": "content", "label": "Satire's Edge Case", "title": "When a joke stops being read as a joke",
         "blocks": [
             {"t": "body", "html": "Satire is legitimate &mdash; until it is screenshotted, "
              "stripped of its source and reshared as fact. Then a parody headline becomes, in "
              "effect, <strong>misinformation by accident</strong>."},
             {"t": "hbox", "color": "amber", "html": "Context collapse: when content jumps "
              "platforms and audiences, the cues that signalled 'this is a joke' fall away."},
         ]},

        {"type": "content", "label": "Why Labels Matter", "title": "The right name shapes the right response",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Misinformation</strong> &rarr; correct gently; the sharer is not the enemy",
                 "<strong>Disinformation</strong> &rarr; expose the source and the motive, not just the claim",
                 "<strong>Malinformation</strong> &rarr; challenge the framing and protect the harmed",
                 "<strong>Satire</strong> &rarr; restore the missing context, don't censor the joke"]},
             {"t": "hbox", "color": "cyan", "html": "Diagnosis before treatment. The category "
              "tells you whether to educate, to debunk or to defend."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "How Falsehoods Spread"},

        {"type": "content", "label": "Old Wisdom", "title": "'A lie travels halfway round the world&hellip;'",
         "blocks": [
             {"t": "quote",
              "text": "A lie can travel halfway around the world while the truth is still putting "
              "on its shoes.",
              "attr": "&mdash; widely attributed to Mark Twain (and to Swift before him); the "
              "attribution itself is disputed"},
             {"t": "hbox", "color": "amber", "html": "Fittingly, the quote's own origin is a small "
              "case study in how a tidy story outruns the messy truth."},
         ]},

        {"type": "content", "label": "The Evidence", "title": "False news really does spread faster",
         "blocks": [
             {"t": "chart", "canvas": "spreadReachChart",
              "title": "Cumulative reach of true vs false stories over time (illustrative shape)",
              "source": "Illustrative, patterned on Vosoughi, Roy &amp; Aral, Science (2018)",
              "type": "line",
              "data": {"labels": ["0h", "2h", "6h", "12h", "24h", "48h", "72h"],
                       "datasets": [
                           {"label": "False stories",
                            "data": [1, 60, 320, 760, 1500, 2400, 3000],
                            "borderColor": "#EF4444", "backgroundColor": "rgba(239,68,68,0.08)",
                            "tension": 0.35, "pointRadius": 3, "fill": True},
                           {"label": "True stories",
                            "data": [1, 20, 70, 150, 300, 480, 600],
                            "borderColor": "#10B981", "backgroundColor": "rgba(16,185,129,0.08)",
                            "tension": 0.35, "pointRadius": 3, "fill": True}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'People reached (illustrative)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Vosoughi, Roy &amp; Aral (<em>Science</em>, 2018) "
              "studied ~126,000 stories on Twitter and found false news spread "
              "<strong>farther, faster and deeper</strong> than the truth &mdash; and people, not "
              "bots, did most of the spreading."},
         ]},

        {"type": "content", "label": "The Surprise Premium", "title": "Why falsehood out-runs fact",
         "blocks": [
             {"t": "body", "html": "The same study found false stories were markedly "
              "<strong>more novel</strong> than true ones, and inspired more "
              "<strong>surprise and disgust</strong>. Truth is often dull; lies can be tailored to "
              "be thrilling."},
             {"t": "bullets", "color": "amber", "items": [
                 "Novelty grabs attention and feels worth sharing",
                 "Strong emotion &mdash; fear, anger, awe &mdash; drives the forward button",
                 "The truth must compete while bound by being true"]},
         ]},

        {"type": "content", "label": "Virality", "title": "How a rumour goes from one to a million",
         "blocks": [
             {"t": "flow", "steps": [
                 "SEED: a single false post or forward",
                 "AMPLIFY: a few high-reach accounts share",
                 "CASCADE: each share exposes new networks",
                 "SATURATE: it feels 'everywhere', so it feels true"]},
             {"t": "hbox", "color": "cyan", "html": "Ubiquity masquerades as verification. 'I keep "
              "seeing it' is mistaken for 'it must be confirmed'."},
         ]},

        {"type": "content", "label": "Network Structure", "title": "Each hop multiplies the reach",
         "blocks": [
             {"t": "chart", "canvas": "rumourReachChart",
              "title": "People reached as a rumour is re-forwarded, hop by hop (illustrative)",
              "source": "Illustrative; assumes each person forwards to several others",
              "type": "bar",
              "data": {"labels": ["Seed", "Hop 1", "Hop 2", "Hop 3", "Hop 4", "Hop 5"],
                       "datasets": [{"label": "People reached",
                                     "data": [1, 8, 64, 512, 4096, 32768],
                                     "backgroundColor": "#EF4444"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ type:'logarithmic', title:{display:true,text:'People reached (log scale)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "A few highly connected <strong>hubs</strong> "
              "&mdash; influencers, large groups &mdash; turbo-charge this. In South Asia, a "
              "forward from a trusted relative carries the credibility of the relationship, not "
              "the source."},
         ]},

        {"type": "content", "label": "The Closed-Loop Problem", "title": "Encrypted chats: trusted, untraceable",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Why it spreads", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Forwarded by people you trust",
                      "No visible like-count or fact-check label",
                      "End-to-end encryption hides the origin"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Why it's hard to fight", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Outsiders can't see what's circulating",
                      "Corrections rarely reach the same group",
                      "Speed outpaces any moderator"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Forward-limit features (capping how many "
              "chats a message can be relayed to) slow, but do not stop, viral falsehood."},
         ]},

        {"type": "content", "label": "Bots", "title": "Automated accounts at scale",
         "blocks": [
             {"t": "term", "word": "Bot",
              "def": "An automated account that posts, likes or reshares without a human behind "
              "each action &mdash; used to manufacture the illusion of popularity or consensus."},
             {"t": "body", "html": "Bots rarely persuade you directly. Their job is to "
              "<strong>amplify</strong> &mdash; to make a fringe view trend, so that real humans "
              "assume it is mainstream and pass it on."},
         ]},

        {"type": "content", "label": "Coordinated Inauthentic Behaviour", "title": "The troll farm and the IT cell",
         "blocks": [
             {"t": "term", "word": "Coordinated inauthentic behaviour (CIB)",
              "def": "Groups of accounts working together to mislead about who they are and what "
              "they are doing &mdash; the platform term for organised influence operations."},
             {"t": "hbox", "color": "red", "html": "Whether called a 'troll farm', an 'IT cell' or "
              "a 'PR operation', the pattern is the same: paid or volunteer networks manufacturing "
              "consensus and drowning out dissent."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Echo Chambers &amp; Filter Bubbles"},

        {"type": "content", "label": "The Coined Term", "title": "Eli Pariser and the 'filter bubble'",
         "blocks": [
             {"t": "term", "word": "Filter bubble",
              "def": "The intellectual isolation that results when algorithms selectively show you "
              "content they predict you'll like &mdash; quietly editing out the rest. Coined by "
              "activist Eli Pariser (2011)."},
             {"t": "body", "html": "Pariser's worry: personalisation creates a "
              "<strong>unique universe of information</strong> for each of us, and we rarely "
              "notice what has been filtered away."},
         ]},

        {"type": "content", "label": "Bubble vs Chamber", "title": "Two related, distinct ideas",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Filter bubble", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Algorithm-driven and often invisible. The "
                   "platform decides what you don't see."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Echo chamber", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Choice-driven and social. You surround "
                   "yourself with the like-minded, and dissent is muffled."}]}]},
             {"t": "hbox", "color": "amber", "html": "One is done <em>to</em> you; the other you "
              "help build. In practice they reinforce each other."},
         ]},

        {"type": "content", "label": "The Mechanism", "title": "Algorithmic curation, in one picture",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 540 280" width="540" height="260" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # the wider world of information (left)
                 '<text x="70" y="24" text-anchor="middle" fill="#94A3B8" font-size="12">All information</text>'
                 '<circle cx="40" cy="60" r="9" fill="#10B981"/>'
                 '<circle cx="40" cy="100" r="9" fill="#F59E0B"/>'
                 '<circle cx="40" cy="140" r="9" fill="#EF4444"/>'
                 '<circle cx="40" cy="180" r="9" fill="#6366F1"/>'
                 '<circle cx="40" cy="220" r="9" fill="#0EA5E9"/>'
                 '<circle cx="95" cy="80" r="9" fill="#EF4444"/>'
                 '<circle cx="95" cy="130" r="9" fill="#10B981"/>'
                 '<circle cx="95" cy="180" r="9" fill="#F59E0B"/>'
                 # the filter
                 '<rect x="200" y="40" width="26" height="200" rx="6" fill="#0EA5E9" fill-opacity="0.15" '
                 'stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="213" y="262" text-anchor="middle" fill="#0EA5E9" font-size="12">filter</text>'
                 # arrows in
                 '<line x1="110" y1="130" x2="198" y2="130" stroke="#334155" stroke-width="1.5"/>'
                 # the bubble (right)
                 '<circle cx="410" cy="140" r="86" fill="#6366F1" fill-opacity="0.10" stroke="#6366F1" stroke-width="2"/>'
                 '<text x="410" y="44" text-anchor="middle" fill="#6366F1" font-size="12">Your feed</text>'
                 '<circle cx="380" cy="115" r="9" fill="#0EA5E9"/>'
                 '<circle cx="430" cy="120" r="9" fill="#0EA5E9"/>'
                 '<circle cx="400" cy="160" r="9" fill="#0EA5E9"/>'
                 '<circle cx="440" cy="170" r="9" fill="#0EA5E9"/>'
                 '<line x1="240" y1="130" x2="320" y2="140" stroke="#334155" stroke-width="1.5"/>'
                 '</svg></div>'),},
             {"t": "hbox", "color": "cyan", "html": "Only content the model predicts you'll engage "
              "with passes the filter. The rest is silently dropped &mdash; you never know it existed."},
         ]},

        {"type": "content", "label": "Homophily", "title": "Birds of a feather cluster together",
         "blocks": [
             {"t": "term", "word": "Homophily",
              "def": "The tendency to connect with people similar to ourselves. Our networks are "
              "homogeneous before any algorithm touches them."},
             {"t": "body", "html": "Echo chambers begin in human nature. We befriend, follow and "
              "marry within our groups &mdash; so our information diet is "
              "<strong>already narrow</strong> when the platform starts personalising it."},
         ]},

        {"type": "content", "label": "Selective Exposure", "title": "We seek what we already believe",
         "blocks": [
             {"t": "term", "word": "Selective exposure",
              "def": "The habit of choosing information sources that agree with our existing views, "
              "and avoiding those that challenge them."},
             {"t": "hbox", "color": "amber", "html": "Algorithms did not invent this; they "
              "industrialised it. Selective exposure is the demand; the filter bubble is the "
              "frictionless supply."},
         ]},

        {"type": "content", "label": "A Caveat", "title": "How sealed are the bubbles, really?",
         "blocks": [
             {"t": "body", "html": "Honesty check: some researchers find the average person's "
              "online diet is <strong>more varied</strong> than the strong 'sealed bubble' story "
              "suggests, and that incidental exposure to other views still happens."},
             {"t": "hbox", "color": "cyan", "html": "The nuance: bubbles are real but leaky, and "
              "matter most for the highly engaged partisans who drive online discourse. Avoid both "
              "complacency and panic."},
         ]},

        {"type": "content", "label": "The Real Harm", "title": "Why bubbles still matter",
         "blocks": [
             {"t": "bullets", "items": [
                 "They make extreme views feel <strong>normal and majority</strong>",
                 "They starve us of the friction that corrects error",
                 "They let falsehoods circulate <strong>uncontested</strong> within a group",
                 "They make the other side feel alien &mdash; fuelling polarisation"]},
             {"t": "hbox", "color": "amber", "html": "The danger is less that you hear only one "
              "view, and more that you stop hearing the people who hold the others as people."},
         ]},

        {"type": "content", "label": "Breaking Out", "title": "Letting air into the bubble",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Follow a few thoughtful sources you usually disagree with",
                 "Notice when a feed only ever flatters your priors",
                 "Seek the strongest version of the other case, not the weakest",
                 "Talk to real people outside your usual circle"]},
             {"t": "hbox", "color": "cyan", "html": "You cannot delete the algorithm, but you can "
              "feed it deliberately &mdash; and step outside it on purpose."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "The Believing Brain"},

        {"type": "content", "label": "The Premise", "title": "We are not the rational machines we imagine",
         "blocks": [
             {"t": "body", "html": "Falsehood succeeds partly because of how human cognition "
              "works. We are pattern-seekers and tribe-members first, dispassionate evaluators of "
              "evidence a distant second. These are <strong>features, not bugs</strong> &mdash; "
              "and they can be exploited."},
             {"t": "quote", "text": "It is the peculiar and perpetual error of the human "
              "understanding to be more moved and excited by affirmatives than by negatives.",
              "attr": "&mdash; Francis Bacon, 1620, anticipating confirmation bias"},
         ]},

        {"type": "content", "label": "Confirmation Bias", "title": "We collect evidence for our side",
         "blocks": [
             {"t": "term", "word": "Confirmation bias",
              "def": "The tendency to search for, interpret and recall information in a way that "
              "confirms what we already believe &mdash; and to discount what doesn't."},
             {"t": "hbox", "color": "amber", "html": "Two people can read the same report and each "
              "walk away surer of opposite conclusions. The data was identical; the filter was not."},
         ]},

        {"type": "content", "label": "Motivated Reasoning", "title": "Reasoning toward the answer we want",
         "blocks": [
             {"t": "term", "word": "Motivated reasoning",
              "def": "Using our reasoning powers not to find the truth, but to justify a conclusion "
              "we are already emotionally committed to."},
             {"t": "body", "html": "The unsettling finding: <strong>more</strong> knowledge and "
              "numeracy can make this worse, because the clever are better at building arguments "
              "for whatever their group already believes."},
         ]},

        {"type": "content", "label": "The Illusory-Truth Effect", "title": "Repeat a thing and it starts to feel true",
         "blocks": [
             {"t": "term", "word": "Illusory-truth effect",
              "def": "The finding that simply repeating a statement increases the likelihood that "
              "people will judge it true &mdash; even when they know better, and even for "
              "implausible claims."},
             {"t": "hbox", "color": "red", "html": "This is the engine of propaganda and the "
              "viral forward. Familiarity is mistaken for credibility. Repetition is a weapon."},
         ]},

        {"type": "content", "label": "The Backfire Effect", "title": "Does correction sometimes backfire?",
         "blocks": [
             {"t": "body", "html": "An influential idea held that correcting a falsehood can "
              "<strong>strengthen</strong> belief in it &mdash; the so-called "
              "<strong>backfire effect</strong>. The story spread widely among communicators."},
             {"t": "hbox", "color": "amber", "html": "Treat with care: later research found the "
              "backfire effect is <strong>rare and hard to reproduce</strong>. For most people, "
              "most of the time, clear correction <em>does</em> help. Don't let the myth scare you "
              "off correcting."},
         ]},

        {"type": "content", "label": "Continued Influence", "title": "Why a debunked claim lingers",
         "blocks": [
             {"t": "term", "word": "Continued-influence effect",
              "def": "The tendency for misinformation to keep shaping our reasoning even after we "
              "have heard, and accepted, a correction."},
             {"t": "hbox", "color": "cyan", "html": "The fix is not just to say 'that's false' but "
              "to supply a <strong>replacement explanation</strong> &mdash; a true story that fills "
              "the gap the lie was occupying."},
         ]},

        {"type": "content", "label": "Dunning&ndash;Kruger", "title": "The least skilled are often the most sure",
         "blocks": [
             {"t": "term", "word": "Dunning&ndash;Kruger effect",
              "def": "A pattern in which people with low ability in a domain tend to overestimate "
              "that ability &mdash; they lack the very skill needed to see their own gaps."},
             {"t": "body", "html": "Combined with motivated reasoning, this breeds the loud, "
              "unshakeable confidence that travels so well online &mdash; while genuine experts "
              "hedge, qualify and lose the room."},
         ]},

        {"type": "content", "label": "Defence", "title": "Knowing your brain's blind spots",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Ask of agreeable news: <em>would I check this if it cut the other way?</em>",
                 "Treat the feeling of certainty as a signal to slow down, not speed up",
                 "Notice repetition for what it is &mdash; not evidence",
                 "Stay humble: these biases are not other people's problem, they are yours too"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Propaganda &amp; Manufacturing Consent"},

        {"type": "content", "label": "The Father of Spin", "title": "Edward Bernays and 'Propaganda' (1928)",
         "blocks": [
             {"t": "body", "html": "Freud's nephew <strong>Edward Bernays</strong> fused "
              "psychoanalysis with publicity to found modern public relations. His 1928 book was "
              "titled, without embarrassment, <em>Propaganda</em>."},
             {"t": "quote", "text": "The conscious and intelligent manipulation of the organized "
              "habits and opinions of the masses is an important element in democratic society.",
              "attr": "&mdash; Edward Bernays, Propaganda, 1928"},
         ]},

        {"type": "content", "label": "Engineering Consent", "title": "Selling things by selling feelings",
         "blocks": [
             {"t": "body", "html": "Bernays' insight was to appeal not to reason but to "
              "<strong>desire and identity</strong> &mdash; famously rebranding cigarettes for "
              "women as 'torches of freedom'. He sold the feeling, and the product followed."},
             {"t": "hbox", "color": "amber", "html": "Post-truth politics is, in part, Bernays' "
              "method turned on citizenship itself: sell the emotion, and the belief follows."},
         ]},

        {"type": "content", "label": "The Propaganda Model", "title": "Herman &amp; Chomsky, 'Manufacturing Consent' (1988)",
         "blocks": [
             {"t": "body", "html": "Edward Herman and Noam Chomsky argued that mass media in "
              "market societies don't need overt censorship to serve power. Structural "
              "<strong>filters</strong> shape the news before it reaches you."},
             {"t": "term", "word": "Manufacturing consent",
              "def": "The idea that media systems generate public agreement with elite agendas "
              "through built-in economic and institutional filters, not crude state control."},
         ]},

        {"type": "content", "label": "The Five Filters", "title": "How news gets shaped at the source",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Filter", "How it shapes the news"],
              "rows": [
                  ["Ownership", "Profit-driven owners set the boundaries of acceptable coverage"],
                  ["Advertising", "Outlets serve audiences advertisers want; don't bite the hand"],
                  ["Sourcing", "Reliance on official and corporate sources for cheap content"],
                  ["Flak", "Organised pushback punishes inconvenient reporting"],
                  ["A common enemy", "A unifying threat (the 'other') disciplines the debate"]]},
             {"t": "hbox", "color": "cyan", "html": "Note the model is debated, but its core "
              "question endures: <em>what shapes the news before anyone lies?</em>"},
         ]},

        {"type": "content", "label": "Framing", "title": "The frame decides what you think about",
         "blocks": [
             {"t": "term", "word": "Framing",
              "def": "Selecting and emphasising certain aspects of an issue to promote a "
              "particular interpretation &mdash; without stating a single falsehood."},
             {"t": "body", "html": "'Tax relief' versus 'tax cuts for the rich.' "
              "'Migrants' versus 'refugees.' Same facts, different worlds. The "
              "<strong>frame</strong> does the persuading before the argument begins."},
         ]},

        {"type": "content", "label": "Agenda-Setting", "title": "Media may not tell you what to think&hellip;",
         "blocks": [
             {"t": "term", "word": "Agenda-setting",
              "def": "The power of media to shape which issues we consider important, by choosing "
              "what to cover and how prominently."},
             {"t": "hbox", "color": "amber", "html": "Cohen's classic line: the press may not "
              "succeed in telling people <em>what</em> to think, but it is stunningly successful "
              "in telling them <em>what to think about</em>."},
         ]},

        {"type": "content", "label": "The Firehose", "title": "A new model: drown the truth in noise",
         "blocks": [
             {"t": "body", "html": "Classic propaganda pushed one consistent message. A newer "
              "tactic &mdash; the <strong>firehose of falsehood</strong> &mdash; floods the zone "
              "with many contradictory claims, fast and shameless, to exhaust and confuse rather "
              "than convince."},
             {"t": "hbox", "color": "red", "html": "The goal is not to make you believe a "
              "particular lie, but to make you believe <em>nothing</em> &mdash; cynicism is the "
              "win condition."},
         ]},

        {"type": "content", "label": "The Through-Line", "title": "From Bernays to the feed",
         "blocks": [
             {"t": "flow", "steps": [
                 "1928: Bernays &mdash; engineer desire",
                 "1988: Herman &amp; Chomsky &mdash; structural filters",
                 "2010s: platforms &mdash; algorithmic amplification",
                 "Now: firehose + synthetic media at zero marginal cost"]},
             {"t": "hbox", "color": "cyan", "html": "The aim has been constant for a century: "
              "shape belief without seeming to. Only the tooling keeps getting cheaper and faster."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The Attention Economy"},

        {"type": "content", "label": "The Real Currency", "title": "When attention is the product",
         "blocks": [
             {"t": "term", "word": "Attention economy",
              "def": "An economy in which human attention is the scarce resource being bought and "
              "sold. Platforms compete to capture and hold your eyes, then sell that access to "
              "advertisers."},
             {"t": "quote", "text": "If you're not paying for the product, you are the product.",
              "attr": "&mdash; an old advertising adage, revived for the social-media age"},
         ]},

        {"type": "content", "label": "The Business Model", "title": "Free to you, because you are the inventory",
         "blocks": [
             {"t": "flow", "steps": [
                 "You give attention &amp; data, for free",
                 "Platform maximises time-on-app",
                 "Advertisers buy your attention",
                 "Revenue rewards whatever keeps you scrolling"]},
             {"t": "hbox", "color": "amber", "html": "Truth was never the objective function. "
              "<strong>Engagement</strong> is &mdash; and the two only sometimes coincide."},
         ]},

        {"type": "content", "label": "Outrage Pays", "title": "The feed is optimised for feeling, not fact",
         "blocks": [
             {"t": "chart", "canvas": "engagementChart",
              "title": "Relative engagement by emotional tone of content (illustrative)",
              "source": "Illustrative shape; consistent with research on moral-emotional language online",
              "type": "bar",
              "data": {"labels": ["Calm / factual", "Positive", "Fearful", "Outraged / angry"],
                       "datasets": [{"label": "Relative engagement",
                                     "data": [22, 40, 70, 100],
                                     "backgroundColor": ["#94A3B8", "#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'Engagement (illustrative index)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Content that triggers moral outrage tends to "
              "be shared most. An algorithm chasing engagement will therefore learn to "
              "<strong>serve you anger</strong> &mdash; without anyone deciding to."},
         ]},

        {"type": "content", "label": "Where News Comes From", "title": "The feed is now the front page",
         "blocks": [
             {"t": "chart", "canvas": "newsSourceChart",
              "title": "Share of adults who get news mainly via social media &amp; messaging (illustrative)",
              "source": "Illustrative; directional, not exact figures",
              "type": "doughnut",
              "data": {"labels": ["Social / messaging apps", "TV", "Print / websites direct", "Radio / other"],
                       "datasets": [{"data": [48, 28, 16, 8],
                                     "backgroundColor": ["#EF4444", "#0EA5E9", "#6366F1", "#94A3B8"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "amber", "html": "When the feed is the main source of news, "
              "the engagement algorithm becomes, in effect, the editor &mdash; one optimised for "
              "attention, not accuracy. (Magnitudes illustrative.)"},
         ]},

        {"type": "content", "label": "Infinite Scroll", "title": "Designed so you can't look away",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Infinite scroll:</strong> no natural stopping cue",
                 "<strong>Variable rewards:</strong> the next post might be the great one (the slot-machine pull)",
                 "<strong>Notifications:</strong> manufactured urgency to bring you back",
                 "<strong>Autoplay:</strong> the next video starts before you choose"]},
             {"t": "hbox", "color": "cyan", "html": "These are not accidents. They are persuasive "
              "design choices &mdash; and they keep you in the place where falsehood spreads."},
         ]},

        {"type": "content", "label": "Misaligned Incentives", "title": "Nobody has to want the harm",
         "blocks": [
             {"t": "body", "html": "This is the crucial, uncomfortable point: an engagement-driven "
              "system can <strong>degrade public truth as a side-effect</strong>, with no villain "
              "intending it. The incentive does the damage automatically."},
             {"t": "hbox", "color": "amber", "html": "Don't look only for bad actors. Look at the "
              "machine's objective function &mdash; that is where most of the harm is manufactured."},
         ]},

        {"type": "content", "label": "The Creator Layer", "title": "The incentive flows downhill",
         "blocks": [
             {"t": "body", "html": "Because attention is money, <strong>creators</strong> learn "
              "what the algorithm rewards and feed it: sharper takes, scarier thumbnails, surer "
              "claims. The platform's incentive becomes the publisher's, then the public's."},
             {"t": "hbox", "color": "red", "html": "Nuance, doubt and 'it's complicated' are "
              "competitively disadvantaged. The market quietly pays a premium for certainty &mdash; "
              "including false certainty."},
         ]},

        {"type": "content", "label": "Reclaiming Attention", "title": "Spend the scarce resource on purpose",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Notice when you feel provoked &mdash; that is the product working",
                 "Turn off non-essential notifications and autoplay",
                 "Choose sources deliberately, rather than letting the feed choose",
                 "Add friction: pause before you share something that made you furious"]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Synthetic Media"},

        {"type": "content", "label": "The New Terrain", "title": "When seeing is no longer believing",
         "blocks": [
             {"t": "body", "html": "For a century, a photograph or recording was strong evidence. "
              "<strong>Synthetic media</strong> &mdash; content created or altered by software "
              "&mdash; is dissolving that trust, at falling cost and rising quality."},
             {"t": "hbox", "color": "amber", "html": "The deepest danger is not any single fake. "
              "It is the erosion of the shared assumption that recordings show something real."},
         ]},

        {"type": "content", "label": "Fake News Sites", "title": "Dressing falsehood as journalism",
         "blocks": [
             {"t": "body", "html": "The cheapest synthetic format needs no AI: a website built to "
              "<strong>look like a real news outlet</strong> &mdash; logo, masthead, datelines "
              "&mdash; publishing invented stories for clicks or influence."},
             {"t": "hbox", "color": "cyan", "html": "During the 2016 US election, a cluster of "
              "such sites was famously traced to teenagers in Veles, North Macedonia, chasing ad "
              "revenue &mdash; falsehood as a pure business."},
         ]},

        {"type": "content", "label": "Cheapfakes", "title": "Most manipulation is low-tech",
         "blocks": [
             {"t": "term", "word": "Cheapfake",
              "def": "Misleading media made with simple, cheap techniques &mdash; mislabelling, "
              "slowing or speeding a clip, cropping, or recaptioning a real but unrelated image."},
             {"t": "hbox", "color": "red", "html": "Reality check: cheapfakes do far more damage "
              "today than deepfakes. An old photo from another country, recaptioned as local "
              "'breaking news', has ignited real violence."},
         ]},

        {"type": "content", "label": "Miscontextualised Images", "title": "The real photo, the false caption",
         "blocks": [
             {"t": "body", "html": "The single most common visual falsehood in South Asia: a "
              "genuine image or video, <strong>stripped of its true context</strong> and "
              "recaptioned to inflame &mdash; an old riot, a foreign accident, a film scene, sold "
              "as today's local event."},
             {"t": "hbox", "color": "amber", "html": "Defence is simple and powerful: a reverse "
              "image search often reveals where and when the picture really came from."},
         ]},

        {"type": "content", "label": "Deepfakes", "title": "When AI puts words in your mouth",
         "blocks": [
             {"t": "term", "word": "Deepfake",
              "def": "Synthetic video, audio or images generated by AI to convincingly depict "
              "people saying or doing things they never did. Named for the 'deep learning' behind it."},
             {"t": "body", "html": "Voice clones now need only seconds of audio; face-swaps run on "
              "consumer hardware. The frontier risks: fake statements by leaders, and "
              "<strong>non-consensual intimate imagery</strong> used to silence women."},
         ]},

        {"type": "content", "label": "The Liar's Dividend", "title": "The subtler danger of deepfakes",
         "blocks": [
             {"t": "term", "word": "Liar's dividend",
              "def": "Once people know any recording <em>could</em> be fake, the guilty can "
              "dismiss <em>genuine</em> evidence as a deepfake &mdash; and be believed."},
             {"t": "hbox", "color": "red", "html": "So synthetic media corrodes truth twice: it "
              "lets fakes pass as real, <strong>and</strong> lets the real be waved away as fake. "
              "Doubt itself becomes a shield for the powerful."},
         ]},

        {"type": "content", "label": "Generative AI at Scale", "title": "Falsehood with no marginal cost",
         "blocks": [
             {"t": "body", "html": "Generative AI can now produce fluent text, images and voices "
              "in any language, instantly and almost free. It can write a thousand unique, "
              "native-sounding fake comments in the time it took to write one."},
             {"t": "hbox", "color": "amber", "html": "The bottleneck on disinformation used to be "
              "human effort. That bottleneck is gone &mdash; raising the premium on verification, "
              "not production."},
         ]},

        {"type": "content", "label": "Spotting the Synthetic", "title": "Habits beat detectors",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Distrust emotionally perfect, source-less viral clips",
                 "Reverse-image-search striking photos before believing or sharing",
                 "Check whether any credible outlet reports the same thing",
                 "Watch for tell-tale glitches &mdash; but assume they'll soon vanish"]},
             {"t": "hbox", "color": "cyan", "html": "No detector is reliable for long. The durable "
              "skill is to check the <strong>source and context</strong>, not to spot the pixels."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Polarisation"},

        {"type": "content", "label": "Two Kinds", "title": "Polarisation isn't only about issues",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Ideological", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Genuine disagreement about policy &mdash; "
                   "taxes, rights, the role of the state. Normal and healthy in a democracy."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Affective", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Disliking, distrusting and fearing the other "
                   "side as people. This is the corrosive kind."}]}]},
             {"t": "hbox", "color": "amber", "html": "You can polarise affectively while barely "
              "disagreeing on policy. Increasingly, we hate the team more than we dispute the plan."},
         ]},

        {"type": "content", "label": "Affective Polarisation", "title": "Hating the other side",
         "blocks": [
             {"t": "term", "word": "Affective polarisation",
              "def": "The tendency for people across a political divide to feel growing dislike "
              "and distrust toward the other group &mdash; not over ideas, but over identity."},
             {"t": "body", "html": "Its markers: I wouldn't want my child to marry one of "
              "<em>them</em>; I assume the worst of their motives; I believe bad news about them "
              "without checking."},
         ]},

        {"type": "content", "label": "Us vs Them", "title": "The mind runs on tribes",
         "blocks": [
             {"t": "body", "html": "Humans form group identities effortlessly &mdash; and once a "
              "line is drawn, we favour the in-group and suspect the out-group automatically. "
              "Politics, religion and caste supply ready-made lines."},
             {"t": "hbox", "color": "cyan", "html": "Disinformation rarely invents a divide. It "
              "<strong>finds an existing fault line and pours in water</strong>, then waits for "
              "the freeze."},
         ]},

        {"type": "content", "label": "The Doom Loop", "title": "Falsehood and division feed each other",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 460 300" width="460" height="280" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # four nodes in a loop
                 '<rect x="150" y="20" width="160" height="48" rx="8" fill="#EF4444" fill-opacity="0.12" stroke="#EF4444" stroke-width="2"/>'
                 '<text x="230" y="49" text-anchor="middle" fill="#EF4444" font-size="13">Falsehood about "them"</text>'
                 '<rect x="300" y="120" width="150" height="48" rx="8" fill="#F59E0B" fill-opacity="0.12" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="375" y="149" text-anchor="middle" fill="#F59E0B" font-size="13">Anger &amp; distrust</text>'
                 '<rect x="150" y="220" width="160" height="48" rx="8" fill="#6366F1" fill-opacity="0.12" stroke="#6366F1" stroke-width="2"/>'
                 '<text x="230" y="249" text-anchor="middle" fill="#6366F1" font-size="13">Deeper division</text>'
                 '<rect x="10" y="120" width="150" height="48" rx="8" fill="#0EA5E9" fill-opacity="0.12" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="85" y="149" text-anchor="middle" fill="#0EA5E9" font-size="13">Ready to believe more</text>'
                 # arrows clockwise
                 '<path d="M312,52 Q380,80 378,118" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#ah)"/>'
                 '<path d="M372,170 Q330,210 312,232" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#ah)"/>'
                 '<path d="M148,238 Q90,210 86,170" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#ah)"/>'
                 '<path d="M88,118 Q120,80 168,54" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#ah)"/>'
                 '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
                 '<path d="M0,0 L6,3 L0,6 Z" fill="#334155"/></marker></defs>'
                 '</svg></div>'),},
             {"t": "hbox", "color": "red", "html": "Each turn of the loop makes the next "
              "falsehood easier to believe. Division is both the cause and the product."},
         ]},

        {"type": "content", "label": "The Trust Collapse", "title": "Falling trust in shared institutions",
         "blocks": [
             {"t": "chart", "canvas": "trustDeclineChart",
              "title": "Trust in news media over time (illustrative downward trend)",
              "source": "Illustrative; directional pattern, not specific national figures",
              "type": "line",
              "data": {"labels": ["2005", "2009", "2013", "2017", "2021", "2024"],
                       "datasets": [{"label": "Share who trust most news",
                                     "data": [62, 56, 50, 44, 40, 37],
                                     "borderColor": "#EF4444", "backgroundColor": "rgba(239,68,68,0.08)",
                                     "tension": 0.3, "pointRadius": 4, "fill": True}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:80, title:{display:true,text:'% trusting (illustrative)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "When no source is trusted in common, there "
              "is no shared referee. Each side keeps its own facts &mdash; and the post-truth "
              "condition becomes self-sustaining."},
         ]},

        {"type": "content", "label": "Cooling It Down", "title": "What actually reduces the heat",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Correct the caricature: most of the other side is more moderate than you think",
                 "Build contact &mdash; real cross-group relationships shrink fear",
                 "Separate the argument from the person; attack ideas, not identities",
                 "Refuse to share content whose main purpose is to make you despise a group"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Why It Matters for Development"},

        {"type": "content", "label": "From Abstract to Urgent", "title": "This is not just an online problem",
         "blocks": [
             {"t": "body", "html": "Post-truth dynamics are sometimes dismissed as a distraction "
              "for the well-connected. In South Asia they shape <strong>whether children get "
              "vaccinated, whether riots ignite, and whether elections are trusted</strong>."},
             {"t": "hbox", "color": "red", "html": "For development practitioners, falsehood is "
              "not a media-studies topic. It is an operational risk to every programme that relies "
              "on public trust."},
         ]},

        {"type": "content", "label": "Public Health", "title": "Vaccine hesitancy and rumour",
         "blocks": [
             {"t": "body", "html": "Health programmes live or die on trust. Rumours &mdash; that a "
              "polio or COVID vaccine causes harm or infertility &mdash; have stalled campaigns and "
              "cost lives, sometimes triggering attacks on health workers."},
             {"t": "hbox", "color": "amber", "html": "A single viral falsehood can undo years of "
              "patient community work. Misinformation here is measured in preventable illness and "
              "death."},
         ]},

        {"type": "content", "label": "Rumour and Violence", "title": "When a forward becomes a mob",
         "blocks": [
             {"t": "body", "html": "Across South Asia, false rumours &mdash; of child-kidnappers, "
              "cattle theft or blasphemy &mdash; spread through messaging apps have led to "
              "<strong>mob lynchings of innocent people</strong>, often strangers in the wrong "
              "place."},
             {"t": "hbox", "color": "red", "html": "These are not edge cases. They are documented, "
              "recurring tragedies in which a smartphone forward was the spark. The stakes could "
              "not be more concrete."},
         ]},

        {"type": "content", "label": "Communal Tension", "title": "Disinformation as a weapon against minorities",
         "blocks": [
             {"t": "body", "html": "Coordinated falsehood &mdash; doctored clips, recaptioned "
              "images, fabricated 'crimes' &mdash; is repeatedly used to inflame communal and "
              "religious hatred and to <strong>scapegoat minorities</strong>."},
             {"t": "hbox", "color": "amber", "html": "Here malinformation and disinformation fuse: "
              "a real fear, a false target, a deliberate match. Recognising the pattern is the "
              "first defence."},
         ]},

        {"type": "content", "label": "Elections", "title": "Falsehood and the integrity of the vote",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Fabricated claims about candidates, seeded on polling eve",
                 "False 'voting day/place changed' messages to suppress turnout",
                 "Manufactured outrage to depress or mobilise particular communities",
                 "Pre-emptive lies that the count will be 'rigged', to delegitimise any result"]},
             {"t": "hbox", "color": "cyan", "html": "The damage is not only any single false vote. "
              "It is the slow erosion of faith that elections can be trusted at all."},
         ]},

        {"type": "content", "label": "Science &amp; Climate", "title": "Manufactured doubt about settled questions",
         "blocks": [
             {"t": "body", "html": "On climate, tobacco and pollution, a recurring playbook "
              "<strong>manufactures doubt</strong>: not denying outright, but amplifying "
              "uncertainty to delay action &mdash; 'the science isn't settled'."},
             {"t": "hbox", "color": "amber", "html": "Doubt is the product. As one tobacco memo "
              "put it decades ago, 'doubt is our product' &mdash; a strategy since reused against "
              "climate science."},
         ]},

        {"type": "content", "label": "Eroded Trust", "title": "The slow poison: nobody to believe",
         "blocks": [
             {"t": "body", "html": "The deepest cost is corrosive and cumulative: when people "
              "trust <strong>no</strong> institution &mdash; not science, not the courts, not the "
              "press &mdash; cooperation on any shared problem becomes almost impossible."},
             {"t": "hbox", "color": "red", "html": "Development is collective action. Post-truth "
              "attacks the trust that collective action requires. That is why it belongs on every "
              "practitioner's risk register."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Building Resilience"},

        {"type": "content", "label": "The Goal", "title": "Resilience, not perfect detection",
         "blocks": [
             {"t": "body", "html": "We will never catch every lie. The realistic aim is "
              "<strong>resilience</strong>: people and communities harder to fool, quicker to "
              "check, and slower to spread &mdash; a population with cognitive antibodies."},
             {"t": "hbox", "color": "cyan", "html": "Shift the question from 'how do we delete "
              "falsehood?' to 'how do we make people and systems resistant to it?'"},
         ]},

        {"type": "content", "label": "Fact-Checking", "title": "Necessary, but not sufficient",
         "blocks": [
             {"t": "body", "html": "Professional <strong>fact-checkers</strong> verify claims and "
              "publish corrections. South Asia has a strong, growing ecosystem of them &mdash; a "
              "vital public good."},
             {"t": "hbox", "color": "amber", "html": "But corrections are slower than falsehood and "
              "rarely reach the closed groups where lies live. Fact-checking is essential "
              "<em>and</em> insufficient on its own &mdash; hence everything that follows."},
         ]},

        {"type": "content", "label": "Lateral Reading", "title": "Read like a fact-checker",
         "blocks": [
             {"t": "term", "word": "Lateral reading",
              "def": "Instead of scrutinising a suspicious page itself, opening new tabs to check "
              "what <em>other</em> sources say about it &mdash; the technique professional "
              "fact-checkers actually use."},
             {"t": "body", "html": "Vertical reading (staying on the page, judging its slick "
              "design) is how the gullible are fooled. <strong>Leave the page</strong> to find out "
              "who is really behind it."},
         ]},

        {"type": "content", "label": "Prebunking", "title": "Inoculate before the lie arrives",
         "blocks": [
             {"t": "term", "word": "Prebunking",
              "def": "Forewarning and refuting a manipulation technique <em>before</em> people meet "
              "it &mdash; building mental resistance, like a vaccine builds immunity."},
             {"t": "hbox", "color": "green", "html": "Inoculation theory traces to psychologist "
              "<strong>William McGuire</strong> in the 1960s and has been revived for the digital "
              "age by Sander van der Linden and colleagues."},
         ]},

        {"type": "content", "label": "The Inoculation Model", "title": "How a mental vaccine works",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 560 170" width="560" height="160" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 '<rect x="10" y="55" width="150" height="60" rx="8" fill="#0EA5E9" fill-opacity="0.12" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="85" y="80" text-anchor="middle" fill="#0EA5E9" font-size="13" font-weight="700">WARN</text>'
                 '<text x="85" y="100" text-anchor="middle" fill="#94A3B8" font-size="11">a lie is coming</text>'
                 '<rect x="205" y="55" width="150" height="60" rx="8" fill="#F59E0B" fill-opacity="0.12" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="280" y="80" text-anchor="middle" fill="#F59E0B" font-size="13" font-weight="700">EXPOSE</text>'
                 '<text x="280" y="100" text-anchor="middle" fill="#94A3B8" font-size="11">a weakened example</text>'
                 '<rect x="400" y="55" width="150" height="60" rx="8" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-width="2"/>'
                 '<text x="475" y="80" text-anchor="middle" fill="#10B981" font-size="13" font-weight="700">REFUTE</text>'
                 '<text x="475" y="100" text-anchor="middle" fill="#94A3B8" font-size="11">show the trick</text>'
                 '<line x1="160" y1="85" x2="203" y2="85" stroke="#334155" stroke-width="2" marker-end="url(#ih)"/>'
                 '<line x1="355" y1="85" x2="398" y2="85" stroke="#334155" stroke-width="2" marker-end="url(#ih)"/>'
                 '<defs><marker id="ih" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
                 '<path d="M0,0 L6,3 L0,6 Z" fill="#334155"/></marker></defs>'
                 '</svg></div>'),},
             {"t": "hbox", "color": "cyan", "html": "Teach the <strong>technique</strong> (e.g. "
              "fake experts, emotional manipulation) and the immunity generalises to lies you've "
              "never seen &mdash; far more durable than debunking one claim at a time."},
         ]},

        {"type": "content", "label": "If You Must Debunk", "title": "How to correct without backfiring",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Lead with the <strong>truth</strong>, not the myth",
                 "Warn briefly before repeating the falsehood (if you must repeat it at all)",
                 "Explain <em>why</em> it's wrong and the <strong>motive</strong> behind it",
                 "Give a clear replacement explanation to fill the gap"]},
             {"t": "hbox", "color": "amber", "html": "The 'truth sandwich': truth &rarr; brief "
              "myth &rarr; truth again. Don't let the lie be the loudest thing you said."},
         ]},

        {"type": "content", "label": "Media &amp; Information Literacy", "title": "The long game: build the skill in everyone",
         "blocks": [
             {"t": "body", "html": "The most durable defence is widespread "
              "<strong>media and information literacy (MIL)</strong> &mdash; teaching people, from "
              "school age up, to source, verify, contextualise and question what they consume and "
              "share."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Who made this, and why?",
                 "What's the evidence, and where's it from?",
                 "What's missing or being left out?",
                 "How does it want me to feel &mdash; and act?"]},
         ]},

        {"type": "content", "label": "A Citizen's Checklist", "title": "Before you believe &mdash; or forward",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Pause</strong> &mdash; strong emotion is a flag, not a green light",
                 "<strong>Source</strong> &mdash; who is behind this, and read laterally",
                 "<strong>Date &amp; place</strong> &mdash; is it old, or from somewhere else?",
                 "<strong>Cross-check</strong> &mdash; do credible outlets report it too?",
                 "<strong>Image</strong> &mdash; reverse-search striking photos and clips",
                 "<strong>Don't be the spreader</strong> &mdash; if unsure, don't forward"]},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Go deeper",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Post-Truth</em> &mdash; Lee McIntyre (a concise primer)",
                 "<em>Manufacturing Consent</em> &mdash; Herman &amp; Chomsky",
                 "<em>The Filter Bubble</em> &mdash; Eli Pariser",
                 "<em>Foolproof</em> &mdash; Sander van der Linden (inoculation &amp; prebunking)",
                 "<em>Information Disorder</em> &mdash; Wardle &amp; Derakhshan (Council of Europe, 2017)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Media &amp; Communications</strong> and "
              "<strong>Digital Rights</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Post-truth is about emotion and identity</strong> beating facts &mdash; not facts vanishing",
                 "<strong>Falsehood spreads faster than truth</strong> &mdash; novelty and outrage are its fuel",
                 "<strong>Your own brain is complicit</strong> &mdash; humility before certainty",
                 "<strong>The incentive does the damage</strong> &mdash; attention, not truth, is what the feed rewards",
                 "<strong>Resilience beats detection</strong> &mdash; prebunk, read laterally, pause before you forward"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Post-Truth Politics 101 &middot; Complete",
         "headline": "Pause before<br>you forward.",
         "byline": "You can't catch every lie &mdash; but you can be harder to fool, quicker to "
                   "check and slower to spread. Carry that into every feed, group chat and "
                   "campaign. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
