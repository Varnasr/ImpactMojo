# -*- coding: utf-8 -*-
"""
English for Development 101 — ImpactMojo 101 Series (native deck spec)
Practical professional communication — clear writing & speaking — for the
development sector in South Asia, written for English-as-a-second/third-language
practitioners. Build: python3 scripts/deck-builder/build.py eng_dev
"""

DECK = {
    "slug": "eng-dev",
    "title": "English for Development 101",
    "description": ("English for Development 101 — a free, practical communication course for "
                    "NGO staff, researchers and grant writers across South Asia working in "
                    "English as a second or third language: plain writing, killing jargon, "
                    "structuring reports, communicating data and speaking with confidence. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "English<br>for<br>Development<br>101",
         "sub": "Clear, Confident Professional Communication for the Development Sector "
                "&mdash; Written for Practitioners Who Work in English as a Second or "
                "Third Language",
         "tags": ["Plain Language", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Communication Matters"},
             {"name": "The Plain-Language Revolution"},
             {"name": "Killing Development Jargon"},
             {"name": "Know Your Audience"},
             {"name": "Structure That Carries Meaning"},
             {"name": "Everyday Professional Writing"},
             {"name": "Grammar That Trips People Up"},
             {"name": "Writing Reports &amp; Briefs"},
             {"name": "Communicating Data in Words"},
             {"name": "Storytelling &amp; Ethical Representation"},
             {"name": "Speaking, Presenting &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Communication Matters in Development"},

        {"type": "content", "label": "The Core Truth", "title": "Good work fails when it can't be explained",
         "blocks": [
             {"t": "body", "html": "A brilliant programme that nobody can describe clearly will "
              "lose the grant, miss the policy window, and confuse the community it serves. In "
              "development, <strong>communication is not a soft add-on</strong> &mdash; it is how "
              "evidence travels, how money moves, and how people are heard."},
             {"t": "hbox", "color": "cyan", "html": "Your impact is capped by your clearest "
              "sentence. If the reader does not understand it, the work might as well not exist."},
         ]},

        {"type": "content", "label": "The Stakes", "title": "Where unclear writing costs you",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "What goes wrong", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "A confusing proposal loses the grant",
                      "A dense report nobody reads or acts on",
                      "A vague email triggers three more emails",
                      "A muddled brief misleads a busy minister"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "What clarity buys", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Funders trust you and say yes",
                      "Decisions get made on your evidence",
                      "Colleagues act without re-asking",
                      "Communities understand their own data"]}]}]},
         ]},

        {"type": "content", "label": "The Working Language", "title": "English as the sector's lingua franca",
         "blocks": [
             {"t": "body", "html": "Across South Asia, development work runs on English &mdash; "
              "donor proposals, journal articles, MoUs, global conferences. It is the language "
              "that connects a field office in Bihar to a funder in Geneva. That gives English "
              "real reach &mdash; and real <strong>power</strong>."},
             {"t": "hbox", "color": "amber", "html": "This is a fact to use, not a hierarchy to "
              "accept. English opens doors; it should never be a gate that keeps good people out."},
         ]},

        {"type": "content", "label": "Power &amp; Politics", "title": "English carries power dynamics",
         "blocks": [
             {"t": "bullets", "items": [
                 "It can <strong>exclude</strong> brilliant field staff who think in other languages",
                 "It can make jargon a <strong>gatekeeping</strong> ritual that signals status",
                 "It can privilege the <strong>articulate</strong> over the <strong>right</strong>",
                 "It can silence the communities whose lives the data describes"]},
             {"t": "hbox", "color": "cyan", "html": "Good development communication uses English "
              "to <em>include</em> &mdash; plain, generous, translatable &mdash; never to perform "
              "expertise or to keep others out."},
         ]},

        {"type": "content", "label": "Reframe", "title": "Writing in your second or third language",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "The hidden advantage", "blocks": [
                  {"t": "body", "cls": "sm", "html": "ESL writers often write <em>plainer</em> "
                   "English than native speakers, because you reach for the simple, direct word. "
                   "Plain English is exactly what the sector needs."}]}],
              "right": [{"t": "panel", "color": "green", "title": "The mindset", "blocks": [
                  {"t": "body", "cls": "sm", "html": "You are not writing a literature exam. You "
                   "are getting a job done. Clarity beats fluency. A short, correct sentence "
                   "always beats a long, impressive, broken one."}]}]},
             {"t": "hbox", "color": "amber", "html": "Confidence comes from a method, not from "
              "vocabulary. This course gives you the method."},
         ]},

        {"type": "content", "label": "What This Deck Is Not", "title": "Not a grammar exam &mdash; a working toolkit",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "This deck is not", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "An academic grammar course",
                      "A test of &lsquo;correct&rsquo; English",
                      "A judgement of how you speak"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "This deck is", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "A practical writing &amp; speaking toolkit",
                      "Habits you can use on Monday",
                      "Confidence built from method"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Skills, not rules. Everything here is "
              "something you <em>do</em>, not something you are graded on."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "flow", "steps": [
                 "WRITE PLAIN: clarity, jargon, audience",
                 "STRUCTURE: emails, reports, briefs",
                 "GET IT RIGHT: grammar that matters",
                 "COMMUNICATE: data, stories, speaking"]},
             {"t": "hbox", "color": "cyan", "html": "Every example is drawn from real development "
              "writing &mdash; proposals, reports, emails and briefs you will actually produce."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Plain-Language Revolution"},

        {"type": "content", "label": "The Movement", "title": "Plain language is a global standard",
         "blocks": [
             {"t": "body", "html": "The <strong>plain-language movement</strong> &mdash; from the "
              "UK's Plain English Campaign (founded 1979) to plain-writing laws in the US and "
              "international standards &mdash; holds a simple idea: a document works if its "
              "intended reader can find what they need, understand it, and use it, the first time."},
             {"t": "term", "word": "Plain language",
              "def": "Writing the reader can understand the first time they read it. Not "
              "dumbed-down or childish &mdash; clear, direct and respectful of the reader's time."},
         ]},

        {"type": "content", "label": "The Principle", "title": "Clarity over complexity",
         "blocks": [
             {"t": "quote",
              "text": "If it is possible to cut a word out, always cut it out.",
              "attr": "&mdash; George Orwell, &ldquo;Politics and the English Language&rdquo; (1946)"},
             {"t": "body", "html": "Complex writing rarely signals a complex mind. It usually "
              "signals that the writer has not finished thinking. Clear writing is the final, "
              "hardest draft &mdash; not the first."},
         ]},

        {"type": "content", "label": "The Trap", "title": "The curse of knowledge",
         "blocks": [
             {"t": "term", "word": "The curse of knowledge",
              "def": "Once you understand something deeply, you forget what it is like not to "
              "understand it &mdash; so you skip the steps and the definitions the reader needs."},
             {"t": "hbox", "color": "red", "html": "You know what &lsquo;the intervention&rsquo;, "
              "&lsquo;the framework&rsquo; and &lsquo;the modality&rsquo; mean. Your reader, "
              "opening cold, does not. Write for the reader you had a year ago."},
         ]},

        {"type": "content", "label": "Readability", "title": "What makes writing readable",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Short sentences</strong> &mdash; one main idea each",
                 "<strong>Short, common words</strong> &mdash; the word you would say out loud",
                 "<strong>Active voice</strong> &mdash; say who does what",
                 "<strong>Concrete nouns</strong> &mdash; &lsquo;farmers&rsquo;, not &lsquo;stakeholders&rsquo;",
                 "<strong>Clear structure</strong> &mdash; headings and white space"]},
             {"t": "hbox", "color": "cyan", "html": "Readability is not about a low reading age. "
              "It is about respecting a busy reader who has forty other documents to get through."},
         ]},

        {"type": "content", "label": "The Evidence", "title": "Readers understand short words better",
         "blocks": [
             {"t": "chart", "canvas": "wordLenChart",
              "title": "Reader comprehension by word and sentence length (illustrative)",
              "source": "Illustrative &mdash; pattern, not exact figures",
              "type": "bar",
              "data": {"labels": ["Short words,\nshort sentences", "Mixed", "Long words,\nlong sentences"],
                       "datasets": [{"label": "Readers who understand first time",
                                     "data": [90, 65, 35],
                                     "backgroundColor": ["#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% who understand first time'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative, but the direction is real and "
              "well established: longer words and sentences steadily lower first-read comprehension."},
         ]},

        {"type": "content", "label": "Sentence Length", "title": "Aim for short, vary the rhythm",
         "blocks": [
             {"t": "body", "html": "A useful target for professional writing: an <strong>average "
              "of 15&ndash;20 words</strong> a sentence. Not every sentence &mdash; an average. "
              "Mix short punchy lines with the occasional longer one for rhythm."},
             {"t": "table",
              "head": ["Sentence length", "Reader experience"],
              "rows": [
                  ["Under 15 words", "Easy &mdash; crisp and clear"],
                  ["15&ndash;25 words", "Fine if well structured"],
                  ["Over 30 words", "Reader gets lost; re-reads or gives up"],
                  ["Over 40 words", "Almost always two or three sentences hiding as one"]]},
         ]},

        {"type": "content", "label": "Active Voice", "title": "Active voice: say who does what",
         "blocks": [
             {"t": "table",
              "head": ["Passive (vague)", "Active (clear)"],
              "rows": [
                  ["It was decided that funds would be reallocated.",
                   "The board reallocated the funds."],
                  ["Mistakes were made in the survey.",
                   "Our field team mis-coded 40 forms."],
                  ["The training was attended by 60 women.",
                   "Sixty women attended the training."]]},
             {"t": "hbox", "color": "green", "html": "Active voice names the actor. It is shorter, "
              "clearer and more honest &mdash; passive voice is often used to hide who did what."},
         ]},

        {"type": "content", "label": "When Passive Is Fine", "title": "Passive has its place",
         "blocks": [
             {"t": "body", "html": "Passive voice is not a crime. Use it deliberately when the "
              "<em>doer</em> is unknown, unimportant, or obvious &mdash; or when you want to keep "
              "the focus on the thing acted upon."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "&ldquo;The wells were contaminated&rdquo; &mdash; the cause is what matters, not who",
                 "&ldquo;Samples were collected weekly&rdquo; &mdash; in a methods section, fine",
                 "Default to active; choose passive on purpose, not by habit"]},
         ]},

        {"type": "content", "label": "Before &rarr; After", "title": "Plain language in action",
         "blocks": [
             {"t": "panel", "color": "red", "title": "Before", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;In order to facilitate the "
                  "optimisation of beneficiary outcomes, a multi-pronged approach was utilised "
                  "for the purpose of enhancing service delivery modalities.&rdquo;"}]},
             {"t": "panel", "color": "green", "title": "After", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;We changed how we deliver services so "
                  "they help people more.&rdquo;"}]},
             {"t": "hbox", "color": "cyan", "html": "26 words become 12, and the meaning finally "
              "appears. The plain version says something; the original only sounds like it does."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Killing Development Jargon"},

        {"type": "content", "label": "The Problem", "title": "NGO-speak: a dialect nobody loves",
         "blocks": [
             {"t": "body", "html": "Every sector grows its own jargon, and development has a "
              "famously thick one. Used inside the team, shorthand saves time. Used with a donor, "
              "a journalist or a community, it becomes a <strong>fog</strong> that hides meaning "
              "and excludes outsiders."},
             {"t": "hbox", "color": "amber", "html": "Test: would the woman in your case study "
              "recognise the words you use to describe her life? If not, rewrite."},
         ]},

        {"type": "content", "label": "Acronym Soup", "title": "Drowning in abbreviations",
         "blocks": [
             {"t": "body", "html": "&ldquo;The CSO submitted the DPR to the PMU for the WASH "
              "intervention under the CSR-funded SHG programme.&rdquo; A reader outside your "
              "office is now completely lost."},
             {"t": "bullets", "color": "green", "items": [
                 "Spell out every acronym on <strong>first use</strong> &mdash; every document",
                 "If you use a term once, do not abbreviate it at all",
                 "Cut acronyms the reader does not need; keep only the load-bearing ones",
                 "A page with five acronyms a sentence is a page nobody finishes"]},
         ]},

        {"type": "content", "label": "Abstraction", "title": "Abstraction hides the real thing",
         "blocks": [
             {"t": "table",
              "head": ["Abstract", "Concrete"],
              "rows": [
                  ["beneficiaries / stakeholders", "farmers, mothers, students, the village council"],
                  ["interventions", "the training, the clinic, the loans"],
                  ["capacity-building activities", "we trained 30 nurses"],
                  ["service-delivery modalities", "how we run the clinics"]]},
             {"t": "hbox", "color": "cyan", "html": "Concrete nouns let the reader <em>see</em> "
              "people and actions. Abstraction turns a living programme into grey vapour."},
         ]},

        {"type": "content", "label": "Nominalisation", "title": "Nominalisation: verbs hiding as nouns",
         "blocks": [
             {"t": "term", "word": "Nominalisation",
              "def": "Turning a strong verb into a heavy noun &mdash; &lsquo;implement&rsquo; "
              "becomes &lsquo;implementation&rsquo;, &lsquo;decide&rsquo; becomes "
              "&lsquo;decision-making&rsquo;. It drains energy and adds words."},
             {"t": "table",
              "head": ["Nominalised (heavy)", "Verb (light)"],
              "rows": [
                  ["We undertook the implementation of the plan.", "We carried out the plan."],
                  ["The utilisation of resources was poor.", "We used resources poorly."],
                  ["A decision was reached regarding closure.", "We decided to close it."]]},
         ]},

        {"type": "content", "label": "Buzzwords", "title": "The buzzword graveyard",
         "blocks": [
             {"t": "table",
              "head": ["Buzzword", "What it often hides", "Say instead"],
              "rows": [
                  ["leverage", "use", "use, draw on"],
                  ["synergy", "working together", "work together"],
                  ["capacity-build", "train, support", "train, mentor, fund"],
                  ["mainstream", "include routinely", "build into our normal work"],
                  ["paradigm shift", "a big change", "a big change"],
                  ["low-hanging fruit", "easy wins", "the easy wins"]]},
             {"t": "hbox", "color": "red", "html": "Buzzwords feel professional and say almost "
              "nothing. Each one is a place where you avoided choosing a precise word."},
         ]},

        {"type": "content", "label": "The Worst Offenders", "title": "Empty intensifiers &amp; filler",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "&ldquo;In order to&rdquo; &rarr; <strong>to</strong>",
                 "&ldquo;Due to the fact that&rdquo; &rarr; <strong>because</strong>",
                 "&ldquo;A large number of&rdquo; &rarr; <strong>many</strong>",
                 "&ldquo;At this point in time&rdquo; &rarr; <strong>now</strong>",
                 "&ldquo;In the event that&rdquo; &rarr; <strong>if</strong>"]},
             {"t": "hbox", "color": "green", "html": "Each replacement saves words and adds "
              "clarity. Do this once and your writing instantly sounds more confident."},
         ]},

        {"type": "content", "label": "Before &rarr; After", "title": "De-jargoning a real sentence",
         "blocks": [
             {"t": "panel", "color": "red", "title": "Before (jargon)", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;Our organisation leverages "
                  "multi-stakeholder synergies to mainstream capacity-building interventions "
                  "that empower beneficiaries at the grassroots level.&rdquo;"}]},
             {"t": "panel", "color": "green", "title": "After (plain)", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;We work with local groups to train "
                  "farmers so they can run their own services.&rdquo;"}]},
             {"t": "hbox", "color": "cyan", "html": "The plain version is shorter, true, and "
              "something a real person could repeat. The jargon version means whatever the reader "
              "wants it to."},
         ]},

        {"type": "content", "label": "A Working Method", "title": "Three passes to cut jargon",
         "blocks": [
             {"t": "flow", "steps": [
                 "READ ALOUD: any phrase you'd never say, rewrite",
                 "CIRCLE: every -ation, -ment, buzzword, acronym",
                 "REPLACE: with the plain word a friend would use"]},
             {"t": "hbox", "color": "amber", "html": "If you would not say it to a colleague over "
              "tea, do not write it in a report. Speech is your best plain-language test."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Know Your Audience"},

        {"type": "content", "label": "The First Question", "title": "Who is reading, and what do they want?",
         "blocks": [
             {"t": "body", "html": "Before writing a single line, name your reader. A donor, a "
              "village committee, a government officer and a journalist want different things from "
              "the same project &mdash; and reward completely different writing."},
             {"t": "hbox", "color": "cyan", "html": "There is no &lsquo;good writing&rsquo; in the "
              "abstract &mdash; only writing that is right for <em>this</em> reader, doing "
              "<em>this</em> job."},
         ]},

        {"type": "content", "label": "The Audience Map", "title": "Four readers, four hungers",
         "blocks": [
             {"t": "table",
              "head": ["Reader", "Wants", "Watch out for"],
              "rows": [
                  ["Donor", "Results, value for money, low risk", "Over-claiming; vague outcomes"],
                  ["Community", "Respect, plain words, usefulness", "Jargon; talking down"],
                  ["Government", "Alignment with policy, data, protocol", "Informality; ignoring their schemes"],
                  ["Media", "A clear story, a human angle, a number", "Dense detail; no headline"]]},
         ]},

        {"type": "content", "label": "Register", "title": "Register: matching the formality",
         "blocks": [
             {"t": "term", "word": "Register",
              "def": "The level of formality and tone you choose for a reader and a situation "
              "&mdash; from a quick WhatsApp to a formal MoU. Getting it wrong feels jarring."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Formal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Proposals, MoUs, policy briefs, journal "
                   "articles. Full sentences, no slang, careful claims."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Informal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Team chat, quick updates, field notes. "
                   "Warm, brief, direct. Still clear and respectful."}]}]},
         ]},

        {"type": "content", "label": "Tone", "title": "Tone is how the reader feels reading you",
         "blocks": [
             {"t": "body", "html": "Tone is separate from formality. You can be formal and warm, "
              "or informal and cold. Development writing should usually be <strong>confident, "
              "honest and human</strong> &mdash; never boastful, never apologetic, never "
              "bureaucratic for its own sake."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Confident: state findings plainly, own the limits",
                 "Honest: report what failed, not only what worked",
                 "Human: there are people behind every number"]},
         ]},

        {"type": "content", "label": "One Message, Many Forms", "title": "Rewrite the same fact for each reader",
         "blocks": [
             {"t": "table",
              "head": ["Reader", "Same finding, their version"],
              "rows": [
                  ["Donor", "Enrolment rose 22% against a 15% target, within budget."],
                  ["Community", "More of our children are now in school than last year."],
                  ["Government", "Enrolment rose 22%, in line with the SSA targets for the block."],
                  ["Media", "A village school doubled its girls' enrolment in one year."]]},
             {"t": "hbox", "color": "amber", "html": "One truth, four framings. None is dishonest "
              "&mdash; each leads with what that reader most needs to hear."},
         ]},

        {"type": "content", "label": "Reader's Time", "title": "Respect is measured in minutes",
         "blocks": [
             {"t": "body", "html": "Assume your reader is overworked and skim-reading on a phone "
              "between meetings. Front-load the point. Use headings. Keep paragraphs short. Make "
              "it <strong>scannable</strong>."},
             {"t": "hbox", "color": "green", "html": "If a busy reader can grasp your main message "
              "from the headings and first lines alone, you have done your job."},
         ]},

        {"type": "content", "label": "Jargon Cuts Both Ways", "title": "The same word fits one reader, fails another",
         "blocks": [
             {"t": "body", "html": "&lsquo;Disaggregated baseline&rsquo; is precise and welcome in "
              "a donor report; it is a wall in a village meeting. Audience does not just change "
              "your <em>tone</em> &mdash; it changes which <strong>words</strong> are clear and "
              "which exclude."},
             {"t": "hbox", "color": "cyan", "html": "There are no universally &lsquo;good&rsquo; "
              "words &mdash; only words that fit the reader in front of you. Choose them for that "
              "reader, every time."},
         ]},

        {"type": "content", "label": "The Empathy Test", "title": "Read it as your reader would",
         "blocks": [
             {"t": "flow", "steps": [
                 "ASK: who opens this, and why?",
                 "ASK: what do they need in 30 seconds?",
                 "ASK: what word would confuse them?",
                 "CUT: everything that does not serve them"]},
             {"t": "hbox", "color": "cyan", "html": "Audience-first writing is generous writing. "
              "You carry the effort so the reader does not have to."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Structure That Carries Meaning"},

        {"type": "content", "label": "The Big Idea", "title": "Structure is half the clarity",
         "blocks": [
             {"t": "body", "html": "Even plain sentences fail if they arrive in the wrong order. "
              "How you <strong>sequence</strong> information decides whether a busy reader finds "
              "the point &mdash; or gives up looking for it."},
             {"t": "hbox", "color": "cyan", "html": "Order is an act of kindness. Put the most "
              "important thing where the reader will actually see it: the top."},
         ]},

        {"type": "content", "label": "The Inverted Pyramid", "title": "Most important first",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:10px 0">'
                 '<svg viewBox="0 0 460 250" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:560px;max-width:100%;height:auto">'
                 '<polygon points="40,20 420,20 300,110 160,110" fill="#0EA5E9" opacity="0.92"/>'
                 '<polygon points="160,112 300,112 250,180 210,180" fill="#6366F1" opacity="0.92"/>'
                 '<polygon points="210,182 250,182 235,235 225,235" fill="#10B981" opacity="0.92"/>'
                 '<text x="230" y="72" fill="#fff" font-size="20" font-weight="700" '
                 'text-anchor="middle" font-family="sans-serif">THE BOTTOM LINE</text>'
                 '<text x="230" y="152" fill="#fff" font-size="14" font-weight="600" '
                 'text-anchor="middle" font-family="sans-serif">Key details</text>'
                 '<text x="232" y="215" fill="#fff" font-size="10" font-weight="600" '
                 'text-anchor="middle" font-family="sans-serif">Background</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "amber", "html": "Borrowed from journalism: lead with the "
              "conclusion, then the key facts, then the background. The reader can stop at any "
              "point and still have the essentials."},
         ]},

        {"type": "content", "label": "BLUF", "title": "Bottom line up front",
         "blocks": [
             {"t": "term", "word": "BLUF",
              "def": "&lsquo;Bottom Line Up Front&rsquo; &mdash; state your conclusion or ask in "
              "the first sentence, before the explanation. The reader learns what you want before "
              "deciding how much to read."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Buried", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Three paragraphs of context&hellip; and only "
                   "at the end: &lsquo;so we need ₹2 lakh by Friday.&rsquo;"}]}],
              "right": [{"t": "panel", "color": "green", "title": "BLUF", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&lsquo;We need ₹2 lakh by Friday to keep the "
                   "clinic open. Here is why&hellip;&rsquo;"}]}]},
         ]},

        {"type": "content", "label": "Topic Sentences", "title": "Each paragraph starts with its point",
         "blocks": [
             {"t": "body", "html": "A <strong>topic sentence</strong> opens each paragraph with "
              "its main idea; the rest of the paragraph supports it. A reader skimming only the "
              "first line of every paragraph should still follow your argument."},
             {"t": "hbox", "color": "cyan", "html": "One paragraph, one idea. If a paragraph "
              "needs two topic sentences, it is two paragraphs."},
         ]},

        {"type": "content", "label": "Executive Summary", "title": "The one page that gets read",
         "blocks": [
             {"t": "body", "html": "For many reports, the <strong>executive summary</strong> is "
              "the only part a senior reader opens. Write it last, but make it stand alone: the "
              "problem, what you did, what you found, what you recommend."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "One page, no jargon, no new information not in the report",
                 "Lead with findings and recommendations, not method",
                 "Someone reading <em>only</em> this should still get the message"]},
         ]},

        {"type": "content", "label": "Signposting", "title": "Headings and signposts guide the eye",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Headings</strong> that state content, not labels (&lsquo;What we found&rsquo;, not &lsquo;Section 3&rsquo;)",
                 "<strong>Signpost phrases:</strong> &lsquo;First&hellip;&rsquo;, &lsquo;In short&hellip;&rsquo;, &lsquo;The key risk is&hellip;&rsquo;",
                 "<strong>Bullet lists</strong> for parallel items &mdash; not for everything",
                 "<strong>White space</strong> &mdash; a wall of text repels the eye"]},
             {"t": "hbox", "color": "amber", "html": "A reader should be able to navigate your "
              "document by headings alone, like a map. Make the map honest."},
         ]},

        {"type": "content", "label": "Flow", "title": "Connect ideas, don't just stack them",
         "blocks": [
             {"t": "body", "html": "Good structure also links sentences. Each sentence should pick "
              "up a thread from the last &mdash; old information first, new information at the end. "
              "That &lsquo;known &rarr; new&rsquo; flow is what makes prose feel smooth."},
             {"t": "hbox", "color": "cyan", "html": "Transitions are cheap and powerful: "
              "&lsquo;but&rsquo;, &lsquo;so&rsquo;, &lsquo;because&rsquo;, &lsquo;for example&rsquo; "
              "tell the reader how ideas relate."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Everyday Professional Writing"},

        {"type": "content", "label": "Email Reality", "title": "Email is most of your writing",
         "blocks": [
             {"t": "body", "html": "You will write more emails than reports in your career, and "
              "your reputation is built on them, one message at a time. A clear, courteous, "
              "well-structured email marks you as someone reliable to work with."},
             {"t": "hbox", "color": "cyan", "html": "Treat every email as a small piece of "
              "professional writing &mdash; because that is exactly what it is."},
         ]},

        {"type": "content", "label": "Subject Lines", "title": "The subject line does the work",
         "blocks": [
             {"t": "table",
              "head": ["Weak subject", "Strong subject"],
              "rows": [
                  ["Update", "Field report submitted &mdash; review by Fri 12 June"],
                  ["Important!!", "Action needed: sign MoU before 10 June"],
                  ["Meeting", "Confirm: budget call moved to Tue 3pm"],
                  ["Hi", "Question on NFHS data for the WASH section"]]},
             {"t": "hbox", "color": "green", "html": "A good subject line says <em>what it is</em> "
              "and <em>what you want</em>. The reader should know whether to act before opening it."},
         ]},

        {"type": "content", "label": "Email Etiquette", "title": "A clean, courteous email",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Greeting</strong> &mdash; use the name; match the relationship",
                 "<strong>Purpose first</strong> &mdash; why you are writing, in line one",
                 "<strong>One ask</strong> &mdash; make the action obvious",
                 "<strong>Deadline</strong> &mdash; say <em>when</em>, not &lsquo;ASAP&rsquo;",
                 "<strong>Sign off</strong> &mdash; warm, short, with your name and role"]},
             {"t": "hbox", "color": "amber", "html": "Re-read once before sending. Most email "
              "regret is a five-second fix."},
         ]},

        {"type": "content", "label": "Requests &amp; Follow-ups", "title": "Asking clearly &mdash; and chasing politely",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Making a request", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Say exactly what you need and by when",
                      "Make it easy to say yes &mdash; attach, pre-fill",
                      "Give a reason; people help when they see why"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Following up", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Wait a reasonable time; assume goodwill",
                      "&lsquo;Just checking in on this&rsquo; &mdash; brief, warm",
                      "Re-state the ask and deadline; don't make them scroll"]}]}]},
         ]},

        {"type": "content", "label": "Meeting Notes", "title": "Notes people can actually use",
         "blocks": [
             {"t": "body", "html": "Good minutes are not a transcript. Capture <strong>decisions, "
              "actions and owners</strong> &mdash; who will do what, by when. Everything else is "
              "usually noise."},
             {"t": "table",
              "head": ["Decision / Action", "Owner", "By when"],
              "rows": [
                  ["Finalise budget revision", "Priya", "12 June"],
                  ["Share NFHS extract with team", "Arif", "8 June"],
                  ["Draft donor update", "Meena", "15 June"]]},
         ]},

        {"type": "content", "label": "Channel Choice", "title": "WhatsApp vs email: pick the right pipe",
         "blocks": [
             {"t": "table",
              "head": ["Use WhatsApp for", "Use email for"],
              "rows": [
                  ["Quick yes/no, urgent ping", "Anything that needs a record"],
                  ["Field coordination, photos", "Decisions, approvals, money"],
                  ["Informal team chat", "Donors, government, formal asks"],
                  ["&lsquo;Running late&rsquo;", "Attachments and long detail"]]},
             {"t": "hbox", "color": "red", "html": "Rule of thumb: if you might need to "
              "<em>prove</em> it later, or it has an attachment, it belongs in email."},
         ]},

        {"type": "content", "label": "Before &rarr; After", "title": "Rewriting a foggy email",
         "blocks": [
             {"t": "panel", "color": "red", "title": "Before", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;Hi, just wanted to touch base "
                  "regarding the thing we discussed, it would be great if you could possibly look "
                  "into it whenever you get a chance, no rush but kind of urgent. Thanks!&rdquo;"}]},
             {"t": "panel", "color": "green", "title": "After", "blocks": [
                 {"t": "body", "cls": "sm", "html": "&ldquo;Hi Ravi &mdash; could you approve the "
                  "revised budget (attached) by Friday 12 June? We cannot release funds without "
                  "it. Thanks!&rdquo;"}]},
             {"t": "hbox", "color": "cyan", "html": "Name the person, the ask, the file and the "
              "deadline. &lsquo;No rush but urgent&rsquo; tells the reader nothing &mdash; a date does."},
         ]},

        {"type": "content", "label": "Tone in Short Messages", "title": "Brevity without coldness",
         "blocks": [
             {"t": "body", "html": "Short messages can read as curt. A single warm word &mdash; "
              "&lsquo;Thanks!&rsquo;, &lsquo;Got it&rsquo;, &lsquo;Hope you're well&rsquo; &mdash; "
              "costs nothing and keeps a working relationship human, especially across cultures "
              "and languages."},
             {"t": "hbox", "color": "cyan", "html": "Clarity and warmth are not a trade-off. Be "
              "brief <em>and</em> kind."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Grammar That Actually Trips People Up"},

        {"type": "content", "label": "First, A Reframe", "title": "Indian English is not broken English",
         "blocks": [
             {"t": "body", "html": "Indian English is a <strong>legitimate, fully grown variety</strong> "
              "of English, with its own valid conventions &mdash; like American, British or "
              "Australian English. &lsquo;Prepone&rsquo;, &lsquo;do the needful&rsquo;, "
              "&lsquo;kindly revert&rsquo; are perfectly correct in their context."},
             {"t": "hbox", "color": "green", "html": "This section is about <em>audience fit</em>, "
              "not about &lsquo;errors of shame&rsquo;. When writing for an international donor, "
              "you may choose international conventions &mdash; a choice, not a correction."},
         ]},

        {"type": "content", "label": "Subject&ndash;Verb", "title": "Subject&ndash;verb agreement",
         "blocks": [
             {"t": "table",
              "head": ["Tripping point", "Fits international convention"],
              "rows": [
                  ["The team are submitting&hellip; (group)", "The team is submitting&hellip; (US/intl: singular)"],
                  ["The data is clear", "The data are clear (formal/academic: plural)"],
                  ["Each of the women have&hellip;", "Each of the women has&hellip;"],
                  ["One of the reports were late", "One of the reports was late"]]},
             {"t": "hbox", "color": "amber", "html": "&lsquo;Data&rsquo; as singular is now widely "
              "accepted; in academic writing, many journals still want the plural. Match the house "
              "style of where you are sending it."},
         ]},

        {"type": "content", "label": "Articles", "title": "Articles: a, an, the",
         "blocks": [
             {"t": "body", "html": "Articles are famously tricky if your first language has none. "
              "A quick guide: <strong>a/an</strong> for one of many (not yet known to the reader); "
              "<strong>the</strong> for a specific one the reader can identify; <strong>no "
              "article</strong> for general plurals and uncountables."},
             {"t": "table",
              "head": ["Use", "Example"],
              "rows": [
                  ["a / an (one, new)", "We ran a training in Patna."],
                  ["the (specific, known)", "The training we ran went well."],
                  ["no article (general)", "Training improves outcomes."]]},
         ]},

        {"type": "content", "label": "A vs An", "title": "&lsquo;A&rsquo; or &lsquo;an&rsquo; goes by sound",
         "blocks": [
             {"t": "bullets", "items": [
                 "Use <strong>an</strong> before a vowel <em>sound</em>: an NGO, an hour, an MoU",
                 "Use <strong>a</strong> before a consonant <em>sound</em>: a university, a one-day event",
                 "It is the sound, not the letter &mdash; &lsquo;an honest&rsquo;, &lsquo;a useful&rsquo;"]},
             {"t": "hbox", "color": "cyan", "html": "Say it aloud. &lsquo;An NGO&rsquo; sounds right "
              "because &lsquo;N&rsquo; begins with a vowel sound (&lsquo;en&rsquo;)."},
         ]},

        {"type": "content", "label": "Tenses", "title": "Tenses for reports",
         "blocks": [
             {"t": "table",
              "head": ["For&hellip;", "Use", "Example"],
              "rows": [
                  ["What you did", "Past simple", "We trained 30 nurses."],
                  ["What the data shows", "Present simple", "The data show a 22% rise."],
                  ["Ongoing work", "Present continuous", "We are scaling to four blocks."],
                  ["Findings that still hold", "Present simple", "Female literacy lowers fertility."]]},
             {"t": "hbox", "color": "green", "html": "Most report confusion comes from drifting "
              "between tenses. Pick the right one for each job and stay consistent within a section."},
         ]},

        {"type": "content", "label": "Prepositions", "title": "Prepositions: small words, big traps",
         "blocks": [
             {"t": "table",
              "head": ["Common slip", "International convention"],
              "rows": [
                  ["discuss about the plan", "discuss the plan"],
                  ["comprise of three parts", "comprise three parts"],
                  ["cope up with the load", "cope with the load"],
                  ["different than last year", "different from last year"]]},
             {"t": "hbox", "color": "amber", "html": "Prepositions rarely follow logic &mdash; "
              "they are learned by ear, phrase by phrase. Keep a personal list of the ones that "
              "catch you."},
         ]},

        {"type": "content", "label": "Indian vs International", "title": "Variety differences, framed as choices",
         "blocks": [
             {"t": "table",
              "head": ["Indian English", "International (donor) English", "Both are valid"],
              "rows": [
                  ["kindly revert", "please reply", "context decides"],
                  ["do the needful", "please take the necessary action", "context decides"],
                  ["prepone the meeting", "move the meeting earlier", "context decides"],
                  ["intimate the team", "inform / notify the team", "context decides"]]},
             {"t": "hbox", "color": "cyan", "html": "When the reader is an international funder, "
              "the right-hand column avoids confusion. That is a deliberate, professional choice "
              "&mdash; not a verdict that you were wrong."},
         ]},

        {"type": "content", "label": "Punctuation", "title": "Three marks worth getting right",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Comma splice:</strong> don't join two sentences with a comma &mdash; "
                 "use a full stop or &lsquo;and/but&rsquo;",
                 "<strong>Apostrophes:</strong> &lsquo;its&rsquo; = belonging; &lsquo;it's&rsquo; = it is",
                 "<strong>Semicolons:</strong> link two closely related full sentences &mdash; "
                 "use sparingly"]},
             {"t": "hbox", "color": "green", "html": "When unsure, a full stop is almost always "
              "safe. Short sentences need less punctuation &mdash; another reason to keep them short."},
         ]},

        {"type": "content", "label": "Self-Editing", "title": "Catch your own slips",
         "blocks": [
             {"t": "flow", "steps": [
                 "READ ALOUD: the ear catches what the eye misses",
                 "ONE PASS PER ISSUE: articles, then tenses, then commas",
                 "USE A CHECKER: but never trust it blindly",
                 "ASK A COLLEAGUE: a second reader is gold"]},
             {"t": "hbox", "color": "cyan", "html": "Grammar is a skill, not a character trait. "
              "Everyone &mdash; including native speakers &mdash; edits. The shame is misplaced; "
              "the practice is universal."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Writing Reports &amp; Briefs"},

        {"type": "content", "label": "The Project Report", "title": "The anatomy of a project report",
         "blocks": [
             {"t": "table",
              "head": ["Section", "Answers", "Keep it"],
              "rows": [
                  ["Executive summary", "What should I know?", "1 page, standalone"],
                  ["Context / problem", "Why this work?", "Short, sourced"],
                  ["What we did", "The activities", "Concrete, past tense"],
                  ["Findings", "What happened?", "Evidence, with numbers"],
                  ["Recommendations", "So what now?", "Specific, actionable"]]},
             {"t": "hbox", "color": "cyan", "html": "Lead with findings and recommendations. "
              "Method and context support the story &mdash; they are not the story."},
         ]},

        {"type": "content", "label": "The Policy Brief", "title": "The policy brief: short, sharp, actionable",
         "blocks": [
             {"t": "body", "html": "A <strong>policy brief</strong> is two to four pages aimed at "
              "a decision-maker who has minutes, not hours. It states a problem, gives the "
              "evidence, and recommends specific, feasible action."},
             {"t": "flow", "steps": [
                 "THE PROBLEM: stated in one line",
                 "THE EVIDENCE: 2&ndash;3 key findings",
                 "THE OPTIONS: what could be done",
                 "THE ASK: one clear recommendation"]},
         ]},

        {"type": "content", "label": "Brief vs Report", "title": "Two formats, two jobs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Report", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The full record &mdash; method, detail, "
                   "evidence, annexes. Written so the work can be checked and repeated."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Brief", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The persuasion &mdash; one problem, the key "
                   "evidence, a clear recommendation. Written so action can be taken."}]}]},
             {"t": "hbox", "color": "amber", "html": "A brief is not a shorter report. It is a "
              "different document with a different goal: not to inform fully, but to move a decision."},
         ]},

        {"type": "content", "label": "Paragraph Engine", "title": "Topic &rarr; evidence &rarr; takeaway",
         "blocks": [
             {"t": "body", "html": "A strong analytical paragraph has a simple engine: a "
              "<strong>topic sentence</strong> stating the point, <strong>evidence</strong> that "
              "supports it, and a <strong>takeaway</strong> that says why it matters."},
             {"t": "flow", "steps": [
                 "TOPIC: state the claim",
                 "EVIDENCE: the number or example",
                 "TAKEAWAY: so what it means"]},
         ]},

        {"type": "content", "label": "Worked Paragraph", "title": "The engine in one paragraph",
         "blocks": [
             {"t": "panel", "color": "green", "title": "Topic &rarr; Evidence &rarr; Takeaway", "blocks": [
                 {"t": "body", "cls": "sm", "html": "<strong>(Topic)</strong> Girls' enrolment "
                  "rose sharply this year. <strong>(Evidence)</strong> It climbed 22%, from 180 "
                  "to 220 girls, against a 15% target. <strong>(Takeaway)</strong> The "
                  "after-school transport scheme appears to be the main driver, and is worth "
                  "scaling to neighbouring blocks."}]},
             {"t": "hbox", "color": "cyan", "html": "Three sentences, one idea, fully argued. Most "
              "good report paragraphs are this shape."},
         ]},

        {"type": "content", "label": "Concision", "title": "Cut until it bleeds, then stop",
         "blocks": [
             {"t": "twocol", "ratio": "a23",
              "left": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Delete the first sentence &mdash; usually a warm-up",
                      "One idea per paragraph",
                      "If it only sounds clever, cut it",
                      "Ask each sentence: what are you <em>for</em>?"]}],
              "right": [
                  {"t": "chart", "canvas": "draftCutChart",
                   "title": "Word count falls draft by draft (illustrative)",
                   "source": "Illustrative",
                   "type": "bar",
                   "data": {"labels": ["Draft 1", "Draft 2", "Draft 3", "Final"],
                            "datasets": [{"label": "Words",
                                          "data": [420, 310, 240, 180],
                                          "backgroundColor": ["#EF4444", "#F59E0B", "#6366F1", "#10B981"]}]},
                   "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'words, same content'} } } }"}}]},
             {"t": "hbox", "color": "green", "html": "Illustrative, but the habit is real: a "
              "finished report is one you have cut, not one you kept adding to. Same meaning, "
              "fewer words."},
         ]},

        {"type": "content", "label": "Recommendations", "title": "Make recommendations someone can act on",
         "blocks": [
             {"t": "table",
              "head": ["Weak (vague)", "Strong (actionable)"],
              "rows": [
                  ["Strengthen the system.", "Add a second nurse to each of the 4 clinics by Q3."],
                  ["Raise awareness.", "Run 12 village meetings before the monsoon."],
                  ["Improve coordination.", "Hold a monthly review with the block officer."]]},
             {"t": "hbox", "color": "amber", "html": "A recommendation a reader cannot picture "
              "doing is not a recommendation. Name the action, the owner and the timeline."},
         ]},

        {"type": "content", "label": "Report Checklist", "title": "Before you submit, ask&hellip;",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Does the summary stand alone and lead with findings?",
                 "Is every acronym spelled out on first use?",
                 "Does each paragraph have one clear point?",
                 "Are recommendations specific, owned and timed?",
                 "Have I cut every sentence that earns nothing?",
                 "Could my target reader skim it in five minutes?"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Communicating Data &amp; Evidence in Words"},

        {"type": "content", "label": "The Skill", "title": "Turn statistics into sentences people feel",
         "blocks": [
             {"t": "body", "html": "Numbers do not speak for themselves; you translate them. The "
              "skill is to carry a statistic into a plain sentence that a non-specialist reader "
              "can picture &mdash; without distorting it."},
             {"t": "table",
              "head": ["Raw statistic", "Plain sentence"],
              "rows": [
                  ["TFR fell from 2.7 to 2.0", "Families are having fewer children than a decade ago."],
                  ["62% vs 38% completion", "Boys finish school far more often than girls here."],
                  ["n=636,000 households", "One of the largest health surveys in the world."]]},
         ]},

        {"type": "content", "label": "Describing a Chart", "title": "Put a chart into words",
         "blocks": [
             {"t": "body", "html": "When you describe a chart in text, do not narrate every "
              "number. State the <strong>pattern</strong>, then the <strong>most important "
              "point</strong>, then the <strong>exception</strong> if there is one."},
             {"t": "flow", "steps": [
                 "PATTERN: overall, enrolment rose",
                 "PEAK / KEY POINT: most in the last year",
                 "EXCEPTION: except in two drought blocks"]},
         ]},

        {"type": "content", "label": "Reader-Friendly Numbers", "title": "Round, compare, anchor",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Round</strong> for prose: &lsquo;about a third&rsquo; beats &lsquo;32.7%&rsquo;",
                 "<strong>Compare:</strong> &lsquo;twice the state average&rsquo; means more than a bare number",
                 "<strong>Anchor:</strong> &lsquo;1 in 5 children&rsquo; is more vivid than &lsquo;20%&rsquo;",
                 "<strong>One number at a time</strong> &mdash; never a sentence stuffed with five"]},
             {"t": "hbox", "color": "cyan", "html": "In a report table, keep the precise figure. "
              "In a sentence, give the reader a number they can hold in their head."},
         ]},

        {"type": "content", "label": "False Precision", "title": "Don't fake an accuracy you don't have",
         "blocks": [
             {"t": "body", "html": "Writing &lsquo;47.3% of beneficiaries&rsquo; from a sample of "
              "60 people pretends to a precision the data cannot support. The decimal is "
              "<strong>false precision</strong> &mdash; it misleads by looking exact."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "False precision", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;47.3% of the 60 respondents&hellip;&rdquo; "
                   "&mdash; that is about 28 people. The decimal is noise."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Honest", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Roughly half (28 of 60) "
                   "respondents&hellip;&rdquo; &mdash; precise about the count, honest about the share."}]}]},
         ]},

        {"type": "content", "label": "Honest Qualifiers", "title": "The words that keep you honest",
         "blocks": [
             {"t": "body", "html": "Good data writing carries its own uncertainty. Qualifiers are "
              "not weakness &mdash; they are accuracy. They tell the reader how far to trust the "
              "number."},
             {"t": "bullets", "sm": True, "color": "amber", "items": [
                 "&lsquo;about&rsquo;, &lsquo;roughly&rsquo;, &lsquo;around&rsquo; &mdash; for estimates",
                 "&lsquo;in this sample&rsquo;, &lsquo;in these 5 villages&rsquo; &mdash; scope of the claim",
                 "&lsquo;suggests&rsquo;, &lsquo;is associated with&rsquo; &mdash; not &lsquo;proves&rsquo; or &lsquo;causes&rsquo;",
                 "&lsquo;preliminary&rsquo;, &lsquo;early data&rsquo; &mdash; when the work is unfinished"]},
         ]},

        {"type": "content", "label": "Correlation in Words", "title": "Don't let language claim causation",
         "blocks": [
             {"t": "table",
              "head": ["Overclaims cause", "Honest wording"],
              "rows": [
                  ["The training raised incomes.", "Incomes rose among those trained."],
                  ["Literacy reduces fertility.", "Higher literacy is linked with lower fertility."],
                  ["Our clinic cut mortality.", "Mortality fell after the clinic opened."]]},
             {"t": "hbox", "color": "red", "html": "Unless you ran a proper evaluation with a "
              "comparison group, write &lsquo;is linked with&rsquo; or &lsquo;followed&rsquo; "
              "&mdash; not &lsquo;caused&rsquo;. The verb is where overclaiming hides."},
         ]},

        {"type": "content", "label": "Sourcing", "title": "Always name the source and the date",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Name the source: &lsquo;(NFHS-5, 2019&ndash;21)&rsquo;, not &lsquo;studies show&rsquo;",
                 "Give the date &mdash; a 2011 figure may be a different country now",
                 "State the denominator: per 1,000? of eligible children?",
                 "Flag your own estimates as <em>illustrative</em> or <em>approximate</em>"]},
             {"t": "hbox", "color": "cyan", "html": "A sourced number is trusted; an unsourced one "
              "invites doubt about everything around it. Citation is credibility."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Storytelling &amp; Ethical Representation"},

        {"type": "content", "label": "Why Stories", "title": "A story carries what a number cannot",
         "blocks": [
             {"t": "body", "html": "Numbers prove scale; stories create understanding. A single, "
              "well-told human story lets a reader feel why the work matters &mdash; and people "
              "act on what they feel. The best communication pairs the two."},
             {"t": "quote", "text": "The death of one person is a tragedy; the death of millions "
              "is a statistic.",
              "attr": "&mdash; a grim adage on why one story moves us more than a number"},
         ]},

        {"type": "content", "label": "The Case Study", "title": "Anatomy of a good case study",
         "blocks": [
             {"t": "flow", "steps": [
                 "PERSON: a real individual, named (with consent)",
                 "SITUATION: their life before",
                 "CHANGE: what happened, concretely",
                 "MEANING: what it shows &mdash; honestly, not heroically"]},
             {"t": "hbox", "color": "cyan", "html": "A case study illustrates a pattern; it does "
              "not prove one. Use it to make the data human, never to replace the data."},
         ]},

        {"type": "content", "label": "The Red Line", "title": "Dignity, not &lsquo;poverty porn&rsquo;",
         "blocks": [
             {"t": "term", "word": "Poverty porn",
              "def": "Imagery or writing that exaggerates suffering to provoke pity and donations, "
              "stripping people of dignity and agency and reducing them to their hardship."},
             {"t": "hbox", "color": "red", "html": "If a story makes the reader pity rather than "
              "respect the person &mdash; or erases everything they do for themselves &mdash; it "
              "has crossed the line. Show strength, choices and context, not only need."},
         ]},

        {"type": "content", "label": "Consent", "title": "Consent in storytelling is non-negotiable",
         "blocks": [
             {"t": "bullets", "items": [
                 "Ask permission to tell the story &mdash; <strong>and</strong> to use the name and photo",
                 "Explain where it will appear and for how long",
                 "Let people say no, or change their mind, without penalty",
                 "Take special care with children, survivors and vulnerable groups"]},
             {"t": "hbox", "color": "amber", "html": "Consent to <em>receive a service</em> is not "
              "consent to <em>star in a fundraising video</em>. Ask separately, ask clearly."},
         ]},

        {"type": "content", "label": "People-First Language", "title": "Words that respect, not label",
         "blocks": [
             {"t": "table",
              "head": ["Labelling", "People-first"],
              "rows": [
                  ["the poor / the disabled", "people living in poverty / with disabilities"],
                  ["AIDS victims", "people living with HIV"],
                  ["illiterate women", "women who have not had schooling"],
                  ["slum-dwellers", "residents of informal settlements"]]},
             {"t": "hbox", "color": "green", "html": "Lead with the person, not the condition. "
              "Language that defines people by their hardship quietly takes their dignity."},
         ]},

        {"type": "content", "label": "Non-Extractive", "title": "Tell stories <em>with</em>, not <em>about</em>",
         "blocks": [
             {"t": "body", "html": "Extractive storytelling takes a community's pain, packages it "
              "for distant audiences, and gives nothing back. Non-extractive practice shares "
              "power: people help shape how they are shown."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Let people review how their story is told before it is published",
                 "Use their own words where you can; quote, don't paraphrase away",
                 "Show the story to the community, in a form they can use"]},
         ]},

        {"type": "content", "label": "Representation Check", "title": "Before you publish a story, ask&hellip;",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Did this person freely consent to <em>this</em> use?",
                 "Does it show their dignity and agency, not only their need?",
                 "Would they recognise and approve of how they appear?",
                 "Am I telling this <em>with</em> them, or extracting it <em>from</em> them?",
                 "Does the community get anything back from this story?"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Speaking, Presenting &amp; Further Reading"},

        {"type": "content", "label": "Speaking Counts Too", "title": "You will be heard as much as read",
         "blocks": [
             {"t": "body", "html": "Communication is not only on the page. You will pitch to "
              "funders, brief officials, present at workshops and answer hard questions live. The "
              "same principles apply: <strong>know your audience, lead with the point, keep it "
              "plain</strong>."},
             {"t": "hbox", "color": "cyan", "html": "A clear speaker who pauses and breathes "
              "always beats a fast one who never stops. Slow is clear; clear is confident."},
         ]},

        {"type": "content", "label": "Presentations", "title": "Slides support you &mdash; they are not the talk",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>One idea per slide</strong> &mdash; you are the presentation, not the deck",
                 "Few words, large type; never read your slides aloud",
                 "Open with the bottom line, then the evidence (BLUF on stage too)",
                 "End with one clear ask or message, not &lsquo;any questions?&rsquo;"]},
             {"t": "hbox", "color": "amber", "html": "If your slides could be emailed and fully "
              "understood without you, you are not needed in the room. Make yourself necessary."},
         ]},

        {"type": "content", "label": "The Elevator Pitch", "title": "Your work in 30 seconds",
         "blocks": [
             {"t": "body", "html": "An <strong>elevator pitch</strong> explains who you help, "
              "what you do and why it matters &mdash; in the time of a short lift ride. Prepare "
              "and practise it; the chance comes without warning."},
             {"t": "flow", "steps": [
                 "WHO: the problem and whom it hits",
                 "WHAT: what you do about it",
                 "PROOF: one number or result",
                 "ASK: what you want from this person"]},
         ]},

        {"type": "content", "label": "Handling Q&amp;A", "title": "Answering questions under pressure",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Pause</strong> before answering &mdash; a breath is not weakness",
                 "Restate the question briefly &mdash; buys time, confirms you heard it",
                 "Answer the question asked; if you don't know, say so and offer to follow up",
                 "Keep answers short; a long answer hides the point"]},
             {"t": "hbox", "color": "green", "html": "&lsquo;That's a good question &mdash; let me "
              "check and get back to you&rsquo; is a strong answer, not a failure. Honesty builds "
              "trust."},
         ]},

        {"type": "content", "label": "Speaking as ESL", "title": "Presenting clearly in your second language",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "<strong>Slow down</strong> &mdash; nerves speed you up; the audience needs time",
                 "Short sentences are easier to <em>say</em> and to <em>follow</em>",
                 "Practise the opening and closing word-for-word; improvise the middle",
                 "Your accent is fine &mdash; clarity and structure matter far more than sounding native"]},
             {"t": "hbox", "color": "amber", "html": "The audience wants your ideas, not a "
              "performance of perfect English. Speak to be understood, and you will be."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "The shelf every writer should know",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>The Elements of Style</em> &mdash; Strunk &amp; White (the classic brevity manual)",
                 "<em>&ldquo;Politics and the English Language&rdquo;</em> &mdash; George Orwell, 1946 (read the six rules)",
                 "<strong>Plain English Campaign</strong> (plainenglish.co.uk) &mdash; free guides &amp; the &lsquo;Crystal Mark&rsquo;",
                 "<em>On Writing Well</em> &mdash; William Zinsser (warm, practical)",
                 "<em>Style: Lessons in Clarity and Grace</em> &mdash; Joseph Williams"]},
         ]},

        {"type": "content", "label": "Orwell's Six Rules", "title": "Orwell's six rules for clear writing",
         "blocks": [
             {"t": "bullets", "sm": True, "items": [
                 "Never use a metaphor, simile or figure of speech you are used to seeing in print",
                 "Never use a long word where a short one will do",
                 "If it is possible to cut a word out, cut it out",
                 "Never use the passive where you can use the active",
                 "Never use a foreign phrase or jargon word if there is an everyday English equivalent",
                 "Break any of these rules sooner than say anything outright barbarous"]},
             {"t": "hbox", "color": "cyan", "html": "From &lsquo;Politics and the English "
              "Language&rsquo; (1946). Eighty years on, still the best one-page writing course."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Clarity over cleverness</strong> &mdash; plain words win",
                 "<strong>Cut the jargon</strong> &mdash; say it as you would over tea",
                 "<strong>Bottom line up front</strong> &mdash; respect the reader's time",
                 "<strong>Your variety of English is valid</strong> &mdash; fit the audience by choice",
                 "<strong>Behind every story is a person</strong> &mdash; consent and dignity first"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Grant Writing</strong>, <strong>Data Literacy</strong> and "
              "<strong>Research Communication</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "English for Development 101 &middot; Complete",
         "headline": "Write to be<br>understood.",
         "byline": "You do not need perfect English &mdash; you need clear English that gets the "
                   "work done, includes the reader, and respects the people behind every number "
                   "and story. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Resources", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
