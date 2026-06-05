# -*- coding: utf-8 -*-
"""
Visual Ethnography 101 — ImpactMojo 101 Series (native deck spec)
Understanding culture and social life through images, for South Asian
development researchers and communicators doing qualitative field work.
Build: python3 scripts/deck-builder/build.py visual_eth
"""

DECK = {
    "slug": "visual-eth",
    "title": "Visual Ethnography 101",
    "description": ("Visual Ethnography 101 — a free foundational course for development "
                    "researchers and communicators in South Asia. Read, make and analyse "
                    "images responsibly: photo-elicitation, photovoice, video methods, the "
                    "ethics of the gaze, and dignified representation in field work. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Visual<br>Ethnography<br>101",
         "sub": "Understanding Culture &amp; Social Life Through Images &mdash; a Foundational "
                "Course for Development Researchers &amp; Communicators in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Is Visual Ethnography?"},
             {"name": "A Short History"},
             {"name": "The Methods Map"},
             {"name": "Photo-Elicitation"},
             {"name": "Photovoice"},
             {"name": "Video &amp; Film Methods"},
             {"name": "Working With Images in the Field"},
             {"name": "Analysing Visual Data"},
             {"name": "The Ethics of the Image"},
             {"name": "Representation &amp; Dignity"},
             {"name": "Presenting Visual Research"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Is Visual Ethnography?"},

        {"type": "content", "label": "Definition", "title": "Seeing culture, not just describing it",
         "blocks": [
             {"t": "body", "html": "Ethnography is the close study of a culture or social world "
              "from the inside. <strong>Visual ethnography</strong> does that work with and "
              "through images &mdash; photographs, video, objects, drawings, the whole visual "
              "fabric of everyday life &mdash; both as data and as a way of knowing."},
             {"t": "term", "word": "Visual ethnography",
              "def": "The study of culture and social life in which images are central to "
              "producing, analysing and communicating knowledge &mdash; not mere illustration "
              "of words, but a method in their own right."},
             {"t": "hbox", "color": "cyan", "html": "The camera is not a neutral recorder. It is "
              "a research instrument &mdash; and a social act &mdash; that you must learn to use "
              "with the same care as an interview guide."},
         ]},

        {"type": "content", "label": "Why Images", "title": "What images do that words cannot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Images capture", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "The texture of a place &mdash; light, density, wear",
                      "Bodies, gesture, dress, spatial arrangement",
                      "What people take for granted and never say",
                      "Material culture: tools, objects, thresholds"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Words capture", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Meaning, motive, interpretation",
                      "Sequence, cause, history",
                      "Abstraction and generalisation",
                      "What an image cannot show on its own"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Visual ethnography works best when images "
              "and words travel together &mdash; the photograph raises questions the interview "
              "then answers."},
         ]},

        {"type": "content", "label": "Three Uses", "title": "Images as data, as method, as output",
         "blocks": [
             {"t": "flow", "steps": [
                 "AS DATA: the image is evidence to be read and analysed",
                 "AS METHOD: making images is how you generate knowledge",
                 "AS OUTPUT: images communicate findings to others"]},
             {"t": "hbox", "color": "green", "html": "A single project often uses all three &mdash; "
              "you photograph a market (data), ask vendors to photograph their day (method), and "
              "build a photo-essay for a report (output)."},
         ]},

        {"type": "content", "label": "Not This", "title": "What visual ethnography is not",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Not stock photos dropped into a report to fill space",
                 "Not 'a nice picture' chosen for beauty over meaning",
                 "Not surveillance &mdash; watching people without their knowledge",
                 "Not a shortcut that skips consent, context or analysis"]},
             {"t": "hbox", "color": "amber", "html": "The discipline is in the method: systematic, "
              "reflexive, consented, and analysed &mdash; not just photogenic."},
         ]},

        {"type": "content", "label": "The Visual World", "title": "More than photographs",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Made", "label": "Photographs, video, film, drawings, maps you or "
                  "participants create", "color": "cyan"},
                 {"num": "Found", "label": "Archives, family albums, posters, signage, social "
                  "media already out there", "color": "indigo"},
                 {"num": "Lived", "label": "Dress, objects, architecture, ritual &mdash; the "
                  "visible texture of culture itself", "color": "amber"}]},
             {"t": "body", "html": "Visual ethnography attends to all of these &mdash; the images "
              "people make, the images they keep, and the visual world they live inside."},
         ]},

        {"type": "content", "label": "South Asia", "title": "A deeply visual region",
         "blocks": [
             {"t": "body", "html": "South Asia is saturated with images &mdash; cinema hoardings, "
              "calendar gods, wedding photography, wall murals, WhatsApp forwards, NREGA muster "
              "boards, ration-shop signage. The visual is where much social meaning already lives."},
             {"t": "hbox", "color": "cyan", "html": "For a development researcher this is an "
              "opportunity: you are studying people who are already skilled makers and readers of "
              "images. Visual methods meet them on familiar ground."},
         ]},

        {"type": "content", "label": "The Image Flood", "title": "We live in an age of images",
         "blocks": [
             {"t": "chart", "canvas": "imageFloodChart",
              "title": "Camera-phone ownership is reshaping who makes images (illustrative)",
              "source": "Illustrative, patterned on rising smartphone adoption in South Asia",
              "type": "line",
              "data": {"labels": ["2010", "2013", "2016", "2019", "2022", "2025"],
                       "datasets": [{"label": "Share of adults with a camera-phone (%)",
                                     "data": [6, 14, 28, 45, 62, 74],
                                     "borderColor": "#0EA5E9",
                                     "backgroundColor": "rgba(14,165,233,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of adults'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Figures illustrative. The trend is real: the "
              "people you study increasingly carry cameras too. Visual ethnography is no longer "
              "the researcher's monopoly &mdash; which is precisely its participatory opportunity."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The methods", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "History and the methods map",
                      "Photo-elicitation and photovoice",
                      "Video, film and field practice"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "The judgement", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Analysing what an image shows and hides",
                      "Consent, ownership and the gaze",
                      "Dignity, representation and presenting"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Throughout, examples are drawn from "
              "fieldwork in India and the wider region &mdash; the situations you will actually "
              "meet with a camera in hand."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "A Short History"},

        {"type": "content", "label": "Origins", "title": "Photography and anthropology grew up together",
         "blocks": [
             {"t": "body", "html": "Photography (1839) and modern anthropology emerged in the same "
              "century, and were entangled from the start. Early ethnographers carried cameras "
              "into the field believing the photograph offered objective, scientific record."},
             {"t": "hbox", "color": "amber", "html": "That belief &mdash; that the camera simply "
              "captures truth &mdash; is exactly what the rest of this course will dismantle. The "
              "image is always made by someone, for someone."},
         ]},

        {"type": "content", "label": "The Colonial Gaze", "title": "Photography as an instrument of empire",
         "blocks": [
             {"t": "body", "html": "In colonial South Asia, the camera was used to classify, "
              "measure and control. Projects like <em>The People of India</em> (1868&ndash;75) "
              "catalogued communities as 'types' &mdash; bodies arranged for the imperial eye."},
             {"t": "bullets", "color": "red", "items": [
                 "People posed as specimens, stripped of name and voice",
                 "Anthropometric photographs to rank and racialise",
                 "Images made <em>about</em> people, never <em>with</em> them",
                 "The subject had no say in how they were seen or used"]},
         ]},

        {"type": "content", "label": "Salvage", "title": "The 'salvage' paradigm",
         "blocks": [
             {"t": "term", "word": "Salvage ethnography",
              "def": "The early-20th-century drive to photograph and record 'vanishing' cultures "
              "before they disappeared &mdash; freezing living peoples as relics of a dying past."},
             {"t": "hbox", "color": "red", "html": "The salvage gaze treated communities as "
              "already-dead museums rather than living, changing societies. It denied people a "
              "present and a future &mdash; a politics hiding inside an apparently caring impulse."},
         ]},

        {"type": "content", "label": "Turning Point", "title": "Bateson and Mead: the systematic turn",
         "blocks": [
             {"t": "body", "html": "Gregory Bateson and Margaret Mead's <em>Balinese Character</em> "
              "(1942) used 759 photographs analysed systematically &mdash; an early attempt to "
              "treat images as rigorous data rather than decorative illustration."},
             {"t": "hbox", "color": "cyan", "html": "A landmark, but still firmly in the "
              "observational tradition: the anthropologists made and arranged the images; the "
              "Balinese were studied, not collaborators."},
         ]},

        {"type": "content", "label": "Founding Texts", "title": "Collier and the method takes shape",
         "blocks": [
             {"t": "body", "html": "John Collier Jr.'s <em>Visual Anthropology: Photography as a "
              "Research Method</em> (1967) made the case that the camera could be a disciplined "
              "research tool &mdash; and introduced <strong>photo-elicitation</strong>, using "
              "photographs to prompt interviews."},
             {"t": "hbox", "color": "green", "html": "Collier moved the field from 'photographs of "
              "people' towards 'photographs as a way of talking with people' &mdash; the seed of "
              "today's participatory methods."},
         ]},

        {"type": "content", "label": "The Shift", "title": "From objectifying to collaborating",
         "blocks": [
             {"t": "table",
              "head": ["", "Old gaze", "Collaborative turn"],
              "rows": [
                  ["Who holds the camera", "The researcher / coloniser", "Increasingly the community"],
                  ["The subject is", "A specimen, a 'type'", "A partner with a voice"],
                  ["Image is", "Objective record", "A co-made interpretation"],
                  ["Power flows", "Outward, extractive", "Shared, negotiated"],
                  ["Goal", "Classify and control", "Understand and advocate"]]},
             {"t": "hbox", "color": "cyan", "html": "This shift &mdash; from camera-as-weapon to "
              "camera-as-dialogue &mdash; is the moral spine of the whole field."},
         ]},

        {"type": "content", "label": "The Critique", "title": "Sontag and Berger name the power",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Susan Sontag", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<em>On Photography</em> (1977): to photograph "
                   "is to appropriate &mdash; an act with the logic of acquisition and even "
                   "aggression. The camera does something <em>to</em> its subject."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "John Berger", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<em>Ways of Seeing</em> (1972): seeing is "
                   "never innocent. How we look is shaped by power, gender and convention &mdash; "
                   "the image carries an ideology."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Keep both voices in your head whenever you "
              "raise a camera in the field. Making an image is never a neutral act."},
         ]},

        {"type": "content", "label": "The Inheritance", "title": "Why this history matters to you",
         "blocks": [
             {"t": "body", "html": "When an NGO photographs 'beneficiaries' for a donor report, "
              "it can unknowingly repeat the colonial gaze &mdash; people posed, unnamed, used to "
              "tell someone else's story."},
             {"t": "hbox", "color": "red", "html": "Knowing this history is not academic. It is "
              "how you avoid reproducing extraction with a modern camera and a development budget."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Methods Map"},

        {"type": "content", "label": "Big Picture", "title": "Three questions organise every method",
         "blocks": [
             {"t": "flow", "steps": [
                 "WHO MAKES the image? &mdash; researcher, participant, or already exists",
                 "WHAT MEDIUM? &mdash; photograph, video, object, drawing",
                 "WHAT FOR? &mdash; to elicit talk, to advocate, to record"]},
             {"t": "body", "html": "Almost every visual method is a combination of answers to "
              "these three questions. The next slide maps the main families."},
         ]},

        {"type": "content", "label": "The Map", "title": "A map of visual ethnographic methods",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 900 360" width="900" style="max-width:100%;font-family:inherit;">'
                 '<text x="450" y="26" text-anchor="middle" fill="#cbd5e1" font-size="16" font-weight="700">'
                 'Who produces the image?</text>'
                 # three top buckets
                 '<rect x="40" y="50" width="240" height="46" rx="8" fill="rgba(14,165,233,.15)" stroke="#0EA5E9" stroke-width="1.5"/>'
                 '<text x="160" y="79" text-anchor="middle" fill="#0EA5E9" font-size="15" font-weight="700">Researcher-produced</text>'
                 '<rect x="330" y="50" width="240" height="46" rx="8" fill="rgba(16,185,129,.15)" stroke="#10B981" stroke-width="1.5"/>'
                 '<text x="450" y="79" text-anchor="middle" fill="#10B981" font-size="15" font-weight="700">Participant-produced</text>'
                 '<rect x="620" y="50" width="240" height="46" rx="8" fill="rgba(245,158,11,.15)" stroke="#F59E0B" stroke-width="1.5"/>'
                 '<text x="740" y="79" text-anchor="middle" fill="#F59E0B" font-size="15" font-weight="700">Found / archival</text>'
                 # connectors
                 '<line x1="160" y1="96" x2="160" y2="130" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="450" y1="96" x2="450" y2="130" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="740" y1="96" x2="740" y2="130" stroke="#334155" stroke-width="1.5"/>'
                 # leaf cards row 1
                 '<rect x="40" y="130" width="240" height="40" rx="6" fill="#1C1917" stroke="#0EA5E9" stroke-width="1"/>'
                 '<text x="160" y="155" text-anchor="middle" fill="#cbd5e1" font-size="13">Observational photography</text>'
                 '<rect x="330" y="130" width="240" height="40" rx="6" fill="#1C1917" stroke="#10B981" stroke-width="1"/>'
                 '<text x="450" y="155" text-anchor="middle" fill="#cbd5e1" font-size="13">Photovoice</text>'
                 '<rect x="620" y="130" width="240" height="40" rx="6" fill="#1C1917" stroke="#F59E0B" stroke-width="1"/>'
                 '<text x="740" y="155" text-anchor="middle" fill="#cbd5e1" font-size="13">Archives &amp; albums</text>'
                 # leaf cards row 2
                 '<rect x="40" y="180" width="240" height="40" rx="6" fill="#1C1917" stroke="#0EA5E9" stroke-width="1"/>'
                 '<text x="160" y="205" text-anchor="middle" fill="#cbd5e1" font-size="13">Observational video</text>'
                 '<rect x="330" y="180" width="240" height="40" rx="6" fill="#1C1917" stroke="#10B981" stroke-width="1"/>'
                 '<text x="450" y="205" text-anchor="middle" fill="#cbd5e1" font-size="13">Participatory video</text>'
                 '<rect x="620" y="180" width="240" height="40" rx="6" fill="#1C1917" stroke="#F59E0B" stroke-width="1"/>'
                 '<text x="740" y="205" text-anchor="middle" fill="#cbd5e1" font-size="13">Found posters &amp; media</text>'
                 # photo-elicitation spans
                 '<rect x="180" y="250" width="540" height="48" rx="8" fill="rgba(99,102,241,.15)" stroke="#6366F1" stroke-width="1.5"/>'
                 '<text x="450" y="272" text-anchor="middle" fill="#6366F1" font-size="14" font-weight="700">Photo-elicitation</text>'
                 '<text x="450" y="290" text-anchor="middle" fill="#94a3b8" font-size="11">uses ANY of the above to prompt talk</text>'
                 '<line x1="160" y1="220" x2="280" y2="250" stroke="#334155" stroke-width="1"/>'
                 '<line x1="450" y1="220" x2="450" y2="250" stroke="#334155" stroke-width="1"/>'
                 '<line x1="740" y1="220" x2="620" y2="250" stroke="#334155" stroke-width="1"/>'
                 '<text x="450" y="338" text-anchor="middle" fill="#64748b" font-size="11">Most projects mix several of these families.</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Family 1", "title": "Researcher-produced images",
         "blocks": [
             {"t": "body", "html": "The researcher holds the camera, choosing what to frame. "
              "Useful for systematic documentation &mdash; spatial layouts, work processes, "
              "material culture, change over time."},
             {"t": "hbox", "color": "amber", "html": "Strength: control and consistency. Weakness: "
              "the frame is <em>yours</em> &mdash; it encodes your assumptions about what matters. "
              "Whose eye is choosing, and what does that eye miss?"},
         ]},

        {"type": "content", "label": "Family 2", "title": "Participant-produced images",
         "blocks": [
             {"t": "body", "html": "You hand the camera to the people you are studying. They "
              "decide what is worth photographing &mdash; revealing priorities and meanings an "
              "outsider would never have framed."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Insider eye", "label": "Captures what matters to <em>them</em>, not you",
                  "color": "green"},
                 {"num": "Shifts power", "label": "Author of the image is the community member",
                  "color": "cyan"}]},
             {"t": "hbox", "color": "green", "html": "Photovoice (Section 5) is the most "
              "developed form of this family."},
         ]},

        {"type": "content", "label": "Family 3", "title": "Found and archival images",
         "blocks": [
             {"t": "body", "html": "Images that already exist &mdash; family albums, NGO archives, "
              "old government photographs, calendar art, social-media posts, wall paintings. The "
              "researcher analyses rather than makes."},
             {"t": "bullets", "items": [
                 "Reveal how a community sees and remembers itself",
                 "Trace change across decades through old photographs",
                 "Surface official or commercial ways of seeing",
                 "Carry their own consent and copyright questions (Section 9)"]},
         ]},

        {"type": "content", "label": "Cross-Cutting", "title": "Photo-elicitation: a method that uses any image",
         "blocks": [
             {"t": "body", "html": "Photo-elicitation is not a fourth family but a <em>technique</em> "
              "&mdash; it takes images from any source and puts them at the centre of an interview "
              "to prompt deeper, richer talk. We unpack it next, in Section 4."},
             {"t": "hbox", "color": "indigo", "html": "Likewise <strong>video</strong> cuts across "
              "all three families &mdash; researcher-shot, participant-shot, or found footage. "
              "Section 6 gives it its own treatment."},
         ]},

        {"type": "content", "label": "Choosing", "title": "Match the method to the question",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["If you want to&hellip;", "Reach for"],
              "rows": [
                  ["Document a place or process systematically", "Researcher photography / video"],
                  ["See a community's own priorities", "Photovoice / participant cameras"],
                  ["Unlock memory and emotion in interviews", "Photo-elicitation"],
                  ["Support advocacy led by the community", "Photovoice + exhibition"],
                  ["Understand self-representation over time", "Found / archival images"],
                  ["Show practice, movement, interaction", "Video methods"]]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Photo-Elicitation"},

        {"type": "content", "label": "Definition", "title": "Interviewing with images on the table",
         "blocks": [
             {"t": "term", "word": "Photo-elicitation",
              "def": "An interview technique in which photographs are introduced into the "
              "conversation to evoke responses &mdash; the participant and researcher talk "
              "about and through the images together."},
             {"t": "body", "html": "Introduced by John Collier Jr. in the 1950s&ndash;60s, it is "
              "now one of the most widely used visual methods &mdash; simple, powerful, and "
              "gentle on the participant."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Images unlock memory and emotion",
         "blocks": [
             {"t": "body", "html": "A photograph in front of someone does something a bare "
              "question cannot. Collier observed that images sharpened memory and lengthened "
              "interviews while easing fatigue &mdash; people talk longer, and differently."},
             {"t": "bullets", "color": "green", "items": [
                 "Triggers concrete, detailed memory ('that is the well we lost')",
                 "Opens emotion that abstract questions keep at bay",
                 "Gives shy participants something to look at, not just answer",
                 "Surfaces details the researcher did not know to ask about"]},
         ]},

        {"type": "content", "label": "The Effect", "title": "Why interviewers reach for photographs",
         "blocks": [
             {"t": "chart", "canvas": "elicitChart",
              "title": "Photo-prompted interviews tend to run longer and richer (illustrative)",
              "source": "Illustrative, in the spirit of Collier's observations",
              "type": "bar",
              "data": {"labels": ["Interview length", "Concrete detail", "Emotional depth", "Topics raised"],
                       "datasets": [
                           {"label": "Words-only interview", "data": [40, 35, 30, 45],
                            "backgroundColor": "#94a3b8"},
                           {"label": "Photo-elicitation", "data": [70, 75, 72, 80],
                            "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:100, title:{display:true,text:'relative index'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Indices are illustrative, not measured "
              "constants &mdash; but they capture the consistent finding that an image on the "
              "table opens up talk a bare question cannot."},
         ]},

        {"type": "content", "label": "Two Modes", "title": "Whose photographs are on the table?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Researcher's images", "blocks": [
                  {"t": "body", "cls": "sm", "html": "You bring photographs &mdash; of the place, "
                   "of historical scenes, of types of work &mdash; and ask people to react. Good "
                   "for shared reference and comparison."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Participant's images", "blocks": [
                  {"t": "body", "cls": "sm", "html": "People discuss photographs <em>they</em> "
                   "made or own &mdash; family albums or photovoice shots. The agenda is theirs; "
                   "the talk goes where they take it."}]}]},
             {"t": "hbox", "color": "amber", "html": "Participant-led elicitation shifts authority "
              "to the interviewee &mdash; often the richer and more equitable choice."},
         ]},

        {"type": "content", "label": "The Flow", "title": "How a photo-elicitation interview runs",
         "blocks": [
             {"t": "flow", "steps": [
                 "SELECT: choose or gather the images together",
                 "OPEN: 'Tell me about this one' &mdash; let them lead",
                 "PROBE: follow their meanings, not your checklist",
                 "CONNECT: ask how images relate to each other",
                 "CLOSE: which image matters most, and why?"]},
             {"t": "hbox", "color": "cyan", "html": "The golden rule: the participant interprets "
              "the image. You ask; you do not tell them what their photo means."},
         ]},

        {"type": "content", "label": "Field Example", "title": "A water photo opens a wider story",
         "blocks": [
             {"t": "body", "html": "A researcher asks women in a Rajasthan village to discuss "
              "photographs of their daily water collection. The images of a distant handpump "
              "elicit talk not just about water, but about time, safety, girls' schooling and "
              "caste access to the well."},
             {"t": "hbox", "color": "green", "html": "Illustrative, but typical: one concrete "
              "image becomes a doorway into an entire web of social relations &mdash; exactly "
              "what a direct survey question would have flattened."},
         ]},

        {"type": "content", "label": "Doing It Well", "title": "Practical craft",
         "blocks": [
             {"t": "bullets", "items": [
                 "Use a manageable set &mdash; a dozen images, not a hundred",
                 "Start broad and open; resist steering early",
                 "Record the talk, and note which image prompted what",
                 "Let silences sit &mdash; people are looking and remembering",
                 "Treat the participant as the expert on their own image"]},
         ]},

        {"type": "content", "label": "Watch-Outs", "title": "Where photo-elicitation can go wrong",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Leading images that plant your interpretation",
                 "Photographs that expose or embarrass the participant",
                 "Assuming an image means the same to them as to you",
                 "Forgetting that <em>you</em> chose the set, framing the talk"]},
             {"t": "hbox", "color": "amber", "html": "Reflexivity again: an elicitation interview "
              "is co-produced. The images you bring shape the story you hear."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Photovoice"},

        {"type": "content", "label": "Definition", "title": "The community photographs its own reality",
         "blocks": [
             {"t": "term", "word": "Photovoice",
              "def": "A participatory action-research method in which community members use "
              "cameras to document their own lives and concerns, then discuss the images "
              "collectively to inform change and reach decision-makers."},
             {"t": "body", "html": "It is explicitly about <strong>voice</strong> &mdash; putting "
              "the means of representation into the hands of those usually represented by others."},
         ]},

        {"type": "content", "label": "Origins", "title": "Wang and Burris, 1997",
         "blocks": [
             {"t": "body", "html": "Photovoice was developed by <strong>Caroline Wang and Mary "
              "Ann Burris</strong> and formalised in 1997, growing from their work with rural "
              "women in Yunnan, China. It draws on feminist theory, documentary photography and "
              "the empowerment education of Paulo Freire."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "1997", "label": "method formalised by Wang &amp; Burris", "color": "cyan",
                  "source": "Wang &amp; Burris, Health Educ &amp; Behavior"},
                 {"num": "Yunnan", "label": "rural women's reproductive-health project", "color": "indigo"},
                 {"num": "Freire", "label": "rooted in critical, empowering pedagogy", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Three Goals", "title": "What photovoice is for",
         "blocks": [
             {"t": "flow", "steps": [
                 "RECORD: let people document community strengths and concerns",
                 "DIALOGUE: promote critical discussion through group reflection",
                 "REACH: bring grassroots knowledge to policymakers"]},
             {"t": "hbox", "color": "green", "html": "Photovoice is not just data collection &mdash; "
              "it is designed to <em>change something</em>. Advocacy is built into the method."},
         ]},

        {"type": "content", "label": "Framework", "title": "SHOWeD: the discussion framework",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 880 320" width="880" style="max-width:100%;font-family:inherit;">'
                 '<text x="440" y="24" text-anchor="middle" fill="#cbd5e1" font-size="15" font-weight="700">'
                 'SHOWeD &mdash; questions asked of each chosen photograph</text>'
                 # rows
                 '<rect x="40" y="44" width="800" height="38" rx="6" fill="rgba(14,165,233,.12)" stroke="#0EA5E9" stroke-width="1"/>'
                 '<text x="60" y="68" fill="#0EA5E9" font-size="18" font-weight="800">S</text>'
                 '<text x="100" y="68" fill="#cbd5e1" font-size="14">What do you <tspan font-weight="700">See</tspan> here?</text>'
                 '<rect x="40" y="88" width="800" height="38" rx="6" fill="rgba(99,102,241,.12)" stroke="#6366F1" stroke-width="1"/>'
                 '<text x="60" y="112" fill="#6366F1" font-size="18" font-weight="800">H</text>'
                 '<text x="100" y="112" fill="#cbd5e1" font-size="14">What is really <tspan font-weight="700">Happening</tspan>?</text>'
                 '<rect x="40" y="132" width="800" height="38" rx="6" fill="rgba(16,185,129,.12)" stroke="#10B981" stroke-width="1"/>'
                 '<text x="60" y="156" fill="#10B981" font-size="18" font-weight="800">O</text>'
                 '<text x="100" y="156" fill="#cbd5e1" font-size="14">How does this relate to <tspan font-weight="700">Our</tspan> lives?</text>'
                 '<rect x="40" y="176" width="800" height="38" rx="6" fill="rgba(245,158,11,.12)" stroke="#F59E0B" stroke-width="1"/>'
                 '<text x="60" y="200" fill="#F59E0B" font-size="18" font-weight="800">W</text>'
                 '<text x="100" y="200" fill="#cbd5e1" font-size="14"><tspan font-weight="700">Why</tspan> does this situation exist?</text>'
                 '<rect x="40" y="220" width="800" height="38" rx="6" fill="rgba(99,102,241,.12)" stroke="#6366F1" stroke-width="1"/>'
                 '<text x="60" y="244" fill="#6366F1" font-size="16" font-weight="800">e</text>'
                 '<text x="100" y="244" fill="#cbd5e1" font-size="14">How could we become <tspan font-weight="700">Educated</tspan> / empowered about it?</text>'
                 '<rect x="40" y="264" width="800" height="38" rx="6" fill="rgba(239,68,68,.12)" stroke="#EF4444" stroke-width="1"/>'
                 '<text x="60" y="288" fill="#EF4444" font-size="18" font-weight="800">D</text>'
                 '<text x="100" y="288" fill="#cbd5e1" font-size="14">What can we <tspan font-weight="700">Do</tspan> about it?</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "SHOWeD", "title": "Why the framework matters",
         "blocks": [
             {"t": "body", "html": "SHOWeD moves a group from simply describing a photograph "
              "(<em>See</em>) to analysing causes (<em>Why</em>) and planning action (<em>Do</em>) "
              "&mdash; turning images into a tool for collective critical consciousness."},
             {"t": "hbox", "color": "cyan", "html": "The arc from 'what do you see' to 'what can "
              "we do' is the whole politics of photovoice in five questions."},
         ]},

        {"type": "content", "label": "The Process", "title": "Running a photovoice project",
         "blocks": [
             {"t": "flow", "steps": [
                 "RECRUIT &amp; train participants; cover ethics of shooting",
                 "PROMPT: agree a question ('What is health here?')",
                 "SHOOT: participants photograph over days or weeks",
                 "SELECT &amp; tell: each picks images and narrates them",
                 "CODIFY with SHOWeD; surface shared themes",
                 "ACT: exhibit, present to officials, advocate"]},
             {"t": "hbox", "color": "amber", "html": "The training step is non-negotiable: "
              "participants become photographers <em>and</em> ethical fieldworkers who must seek "
              "consent from anyone they photograph."},
         ]},

        {"type": "content", "label": "Ethics First", "title": "Photovoice has its own ethics",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Participants need consent from people <em>they</em> photograph",
                 "'No portraits of identifiable strangers without permission'",
                 "Discuss risk &mdash; photographing power can endanger the photographer",
                 "Agree who owns and controls the images from the start"]},
             {"t": "hbox", "color": "amber", "html": "Wang and Burris stressed safety and ethics "
              "training as the first session, before any camera is handed out."},
         ]},

        {"type": "content", "label": "Strengths &amp; Limits", "title": "What photovoice does and does not do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Centres marginalised voices",
                      "Builds skills and confidence",
                      "Powerful advocacy material",
                      "Findings owned by the community"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Limits", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Time- and resource-intensive",
                      "Raises expectations of change",
                      "Risk of tokenism if not genuine",
                      "Group dynamics can silence some"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Done well it transfers power. Done as a box-"
              "ticking exercise it merely extracts prettier images. The difference is intent and "
              "follow-through."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Video &amp; Film Methods"},

        {"type": "content", "label": "Why Video", "title": "What moving images add",
         "blocks": [
             {"t": "body", "html": "Video captures what a still cannot: time, movement, sound, "
              "speech, the unfolding of an event or a practice. It is uniquely suited to ritual, "
              "work processes, interaction and embodied skill."},
             {"t": "hbox", "color": "amber", "html": "But video is heavier &mdash; more "
              "intrusive, more labour to make and analyse, and far harder to anonymise. Reach for "
              "it when motion and sequence are the point, not by default."},
         ]},

        {"type": "content", "label": "Two Traditions", "title": "Observational vs participatory video",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Observational", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The filmmaker records events as they "
                   "unfold, aiming to intrude minimally &mdash; the 'fly on the wall'. The "
                   "researcher still chooses where to point the lens."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Participatory", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Community members shape and often shoot the "
                   "film themselves, deciding what is recorded and how their story is told. "
                   "Authorship is shared or handed over."}]}]},
             {"t": "hbox", "color": "indigo", "html": "These are ends of a spectrum, not a binary. "
              "Most projects sit somewhere in between &mdash; and should be honest about where."},
         ]},

        {"type": "content", "label": "PV", "title": "Participatory Video (PV) in practice",
         "blocks": [
             {"t": "body", "html": "In participatory video, a facilitator trains a group to plan, "
              "shoot and screen their own short films. Used widely in South Asian development &mdash; "
              "from community forest rights to sanitation campaigns &mdash; it builds confidence "
              "and a tool the community keeps."},
             {"t": "flow", "steps": [
                 "Games &amp; camera training build comfort",
                 "Group storyboards the issue together",
                 "Members film and review their own footage",
                 "Community screening sparks discussion &amp; action"]},
         ]},

        {"type": "content", "label": "Labour", "title": "The hidden labour of filming",
         "blocks": [
             {"t": "body", "html": "Filming is not a casual act. It demands planning, equipment, "
              "permissions, hours of capture and far more hours of logging and editing. A minute "
              "of usable film can cost a day of work."},
             {"t": "hbox", "color": "amber", "html": "Budget the labour honestly &mdash; "
              "including the time of community members. Their hours in front of and behind the "
              "camera are real work, and should be respected as such."},
         ]},

        {"type": "content", "label": "The Edit", "title": "Editing is interpretation",
         "blocks": [
             {"t": "body", "html": "Every cut is a choice. What you keep, drop and sequence builds "
              "an argument &mdash; the edit, not the raw footage, makes the meaning. Power "
              "concentrates in the edit suite."},
             {"t": "hbox", "color": "cyan", "html": "<strong>Collaborative editing</strong> shares "
              "that power: show participants the rough cut, let them object, correct and shape the "
              "final story. The people on screen should recognise themselves in it."},
         ]},

        {"type": "content", "label": "Ethics of Film", "title": "Video raises the ethical stakes",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Faces and voices are almost impossible to anonymise",
                 "Footage can circulate forever, far beyond the original purpose",
                 "Consent must cover <em>how and where</em> the film will be shown",
                 "Filming the powerful can expose participants to real risk"]},
             {"t": "hbox", "color": "amber", "html": "Treat video consent as ongoing, not a "
              "one-time signature &mdash; people should be able to see the cut and withdraw."},
         ]},

        {"type": "content", "label": "Analysis", "title": "Analysing video data",
         "blocks": [
             {"t": "body", "html": "Video analysis is slow and systematic: log footage with "
              "timecodes, transcribe speech, note gesture, gaze and interaction, then code as you "
              "would any qualitative data &mdash; watching repeatedly for what you missed."},
             {"t": "hbox", "color": "cyan", "html": "The same reflexivity applies: your camera "
              "position and presence shaped the event. Note where you stood and what you could "
              "not see."},
         ]},

        {"type": "content", "label": "The Screening", "title": "The community screening is part of the method",
         "blocks": [
             {"t": "body", "html": "In participatory video, showing the film back to the community "
              "is not a launch event &mdash; it is data and action at once. Reactions, arguments "
              "and corrections at the screening often matter more than the footage itself."},
             {"t": "hbox", "color": "green", "html": "The screening can also reach officials and "
              "duty-bearers directly, turning the community's own images into advocacy in the room "
              "where decisions are made."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Working With Images in the Field"},

        {"type": "content", "label": "Before You Shoot", "title": "Preparation in the field",
         "blocks": [
             {"t": "bullets", "items": [
                 "Clarify your <strong>research question</strong> &mdash; what are images <em>for</em>?",
                 "Secure permissions &mdash; community, gatekeepers, individuals",
                 "Plan consent in the local language, before the camera appears",
                 "Decide storage, backup and who will see the images"]},
             {"t": "hbox", "color": "amber", "html": "An image you cannot ethically use is worse "
              "than no image. Settle consent and purpose <em>before</em> you press the shutter."},
         ]},

        {"type": "content", "label": "Visual Consent", "title": "Informed visual consent",
         "blocks": [
             {"t": "term", "word": "Informed visual consent",
              "def": "Agreement, freely given and properly understood, to be photographed or "
              "filmed &mdash; covering what is captured, how it will be used, where it may "
              "appear, and the right to refuse or withdraw."},
             {"t": "hbox", "color": "red", "html": "Crucial distinction: consent to be "
              "<em>photographed</em> is not the same as consent to <em>publish</em>. Ask for "
              "both, separately, and explain the difference."},
         ]},

        {"type": "content", "label": "Composition", "title": "Composition carries meaning",
         "blocks": [
             {"t": "body", "html": "How you frame is an interpretive choice. Angle, distance, "
              "what is in or out of frame, what is foregrounded &mdash; all shape the story the "
              "image tells before a word is spoken."},
             {"t": "bullets", "items": [
                 "Low angle can ennoble; high angle can diminish",
                 "Tight crops strip context; wide shots restore it",
                 "What you leave <em>out</em> of frame is also a choice",
                 "Eye-level, with the subject, signals respect"]},
         ]},

        {"type": "content", "label": "Context", "title": "An image without context is a riddle",
         "blocks": [
             {"t": "body", "html": "A photograph alone is ambiguous. The same image can mean "
              "opposite things depending on where, when and why it was made. Context is what "
              "makes an image usable as data."},
             {"t": "hbox", "color": "cyan", "html": "Record context as you shoot: who, what, "
              "where, when, and what was happening just before and after. The picture is half "
              "the data; the context is the other half."},
         ]},

        {"type": "content", "label": "Metadata", "title": "Capture the metadata",
         "blocks": [
             {"t": "term", "word": "Metadata",
              "def": "Data about the image &mdash; date, location, who is shown, consent status, "
              "the prompt or event, and any restrictions on use. Without it, an image is an "
              "orphan."},
             {"t": "hbox", "color": "amber", "html": "Build a simple log: file name, date, place, "
              "people, consent reference, caption notes. Six months on, you will not remember "
              "which blurred face belongs to which interview."},
         ]},

        {"type": "content", "label": "Fieldnotes", "title": "Fieldnotes alongside images",
         "blocks": [
             {"t": "body", "html": "Images do not replace written fieldnotes &mdash; they sit "
              "beside them. Note why you took each shot, what you could <em>not</em> photograph, "
              "and how people reacted to the camera."},
             {"t": "hbox", "color": "green", "html": "The reaction to the camera is itself data: "
              "who avoided it, who performed for it, who asked to be in it. Write it down."},
         ]},

        {"type": "content", "label": "The Observer Effect", "title": "The camera changes the scene",
         "blocks": [
             {"t": "body", "html": "People behave differently when a lens is present &mdash; they "
              "tidy, pose, perform or withdraw. The camera does not record an untouched reality; "
              "it co-creates the moment it captures."},
             {"t": "hbox", "color": "cyan", "html": "Do not pretend this away. Acknowledge it, "
              "spend time until the camera becomes ordinary, and treat the performance itself as "
              "something worth understanding."},
         ]},

        {"type": "content", "label": "Care", "title": "Storage, security and respect",
         "blocks": [
             {"t": "bullets", "items": [
                 "Back up images securely; restrict who can access them",
                 "Store consent records with the images they cover",
                 "Honour any agreement to share photographs back with people",
                 "Have a plan to delete on request &mdash; and mean it"]},
             {"t": "hbox", "color": "amber", "html": "A photograph of a person is a piece of "
              "their life. Custody of it is a responsibility, not a trophy."},
         ]},

        {"type": "content", "label": "Saturation", "title": "How many images is enough?",
         "blocks": [
             {"t": "body", "html": "There is no magic number. As with interviews, you keep "
              "collecting until new images stop revealing new themes &mdash; the point of "
              "<strong>saturation</strong>. Depth and consent matter more than volume."},
             {"t": "hbox", "color": "amber", "html": "A thousand unconsented snapshots are worth "
              "less than thirty images made with care, context and permission. Resist the urge "
              "to hoard pictures."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Analysing Visual Data"},

        {"type": "content", "label": "The Task", "title": "From images to understanding",
         "blocks": [
             {"t": "body", "html": "Collecting images is the easy part. Analysis means reading "
              "them systematically &mdash; what they show, what they mean, what they leave out, "
              "and how your own gaze shaped what you see."},
             {"t": "flow", "steps": [
                 "WHAT is in the image? (content)",
                 "WHAT does it mean? (semiotics)",
                 "WHAT is absent? (the unseen)",
                 "HOW does my position shape this reading? (reflexivity)"]},
         ]},

        {"type": "content", "label": "Two Approaches", "title": "Content vs semiotic analysis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Content analysis", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Systematic counting of what appears &mdash; "
                   "how many images show women, how often a tap is present. Good for patterns "
                   "across many images; answers <em>what</em> and <em>how often</em>."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Semiotic analysis", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Interpreting <em>meaning</em> &mdash; what "
                   "the image signifies, what it connotes, what cultural codes it draws on. Deep "
                   "reading of few images; answers <em>what does it mean</em>."}]}]},
             {"t": "hbox", "color": "amber", "html": "Content analysis is broad and countable; "
              "semiotic analysis is deep and interpretive. Many projects use both."},
         ]},

        {"type": "content", "label": "Barthes", "title": "Denotation and connotation",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 860 300" width="860" style="max-width:100%;font-family:inherit;">'
                 '<text x="430" y="24" text-anchor="middle" fill="#cbd5e1" font-size="15" font-weight="700">'
                 'Two layers of meaning in one photograph (after Roland Barthes)</text>'
                 # the image box
                 '<rect x="40" y="60" width="220" height="160" rx="10" fill="#1C1917" stroke="#64748b" stroke-width="1.5"/>'
                 '<text x="150" y="135" text-anchor="middle" fill="#94a3b8" font-size="13">A photograph of</text>'
                 '<text x="150" y="158" text-anchor="middle" fill="#cbd5e1" font-size="14" font-weight="700">a child &amp; a water pot</text>'
                 # denotation
                 '<rect x="320" y="60" width="500" height="66" rx="10" fill="rgba(14,165,233,.12)" stroke="#0EA5E9" stroke-width="1.5"/>'
                 '<text x="340" y="86" fill="#0EA5E9" font-size="14" font-weight="700">DENOTATION &mdash; what is literally shown</text>'
                 '<text x="340" y="110" fill="#cbd5e1" font-size="13">A child carrying a metal pot on a dirt path.</text>'
                 # connotation
                 '<rect x="320" y="150" width="500" height="80" rx="10" fill="rgba(245,158,11,.12)" stroke="#F59E0B" stroke-width="1.5"/>'
                 '<text x="340" y="176" fill="#F59E0B" font-size="14" font-weight="700">CONNOTATION &mdash; what it is taken to mean</text>'
                 '<text x="340" y="200" fill="#cbd5e1" font-size="13">&ldquo;Poverty,&rdquo; &ldquo;lost childhood,&rdquo; &ldquo;the burden of</text>'
                 '<text x="340" y="218" fill="#cbd5e1" font-size="13">water&rdquo; &mdash; cultural meanings the viewer adds.</text>'
                 # arrow
                 '<line x1="260" y1="140" x2="318" y2="100" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="260" y1="150" x2="318" y2="185" stroke="#334155" stroke-width="1.5"/>'
                 '<text x="430" y="280" text-anchor="middle" fill="#64748b" font-size="11">The danger: presenting connotation as if it were simply &ldquo;what the photo shows.&rdquo;</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "The Layers", "title": "Why the two layers matter",
         "blocks": [
             {"t": "body", "html": "Roland Barthes distinguished <strong>denotation</strong> (the "
              "literal content) from <strong>connotation</strong> (the cultural meanings layered "
              "on top). A photograph never just 'shows' &mdash; it always also 'says'."},
             {"t": "hbox", "color": "red", "html": "Much misleading development imagery works "
              "exactly here: it presents a loaded <em>connotation</em> &mdash; helplessness, "
              "exotic poverty &mdash; as if it were neutral fact."},
         ]},

        {"type": "content", "label": "The Unseen", "title": "Read what the image excludes",
         "blocks": [
             {"t": "body", "html": "Analysis is not only about what is in the frame. Ask what has "
              "been cropped out, who is absent, what the photographer chose <em>not</em> to "
              "record. The edges of an image are full of meaning."},
             {"t": "bullets", "color": "amber", "items": [
                 "Who is never photographed in this archive?",
                 "What is just outside the frame &mdash; and why?",
                 "Which moments were not considered worth a shot?",
                 "Whose perspective does the framing assume?"]},
         ]},

        {"type": "content", "label": "The Gaze", "title": "The triangle of looking",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 700 330" width="700" style="max-width:100%;font-family:inherit;">'
                 '<text x="350" y="24" text-anchor="middle" fill="#cbd5e1" font-size="15" font-weight="700">'
                 'Every image sits inside three gazes</text>'
                 # triangle edges
                 '<line x1="350" y1="70" x2="120" y2="260" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="350" y1="70" x2="580" y2="260" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="120" y1="260" x2="580" y2="260" stroke="#334155" stroke-width="1.5"/>'
                 # nodes
                 '<circle cx="350" cy="70" r="52" fill="rgba(14,165,233,.15)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="350" y="66" text-anchor="middle" fill="#0EA5E9" font-size="14" font-weight="700">Photographer</text>'
                 '<text x="350" y="84" text-anchor="middle" fill="#94a3b8" font-size="11">chooses the frame</text>'
                 '<circle cx="120" cy="260" r="52" fill="rgba(16,185,129,.15)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="120" y="256" text-anchor="middle" fill="#10B981" font-size="14" font-weight="700">Subject</text>'
                 '<text x="120" y="274" text-anchor="middle" fill="#94a3b8" font-size="11">is looked at</text>'
                 '<circle cx="580" cy="260" r="52" fill="rgba(245,158,11,.15)" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="580" y="256" text-anchor="middle" fill="#F59E0B" font-size="14" font-weight="700">Viewer</text>'
                 '<text x="580" y="274" text-anchor="middle" fill="#94a3b8" font-size="11">interprets later</text>'
                 # edge labels
                 '<text x="205" y="160" text-anchor="middle" fill="#64748b" font-size="11" transform="rotate(40 205,160)">power to frame</text>'
                 '<text x="495" y="160" text-anchor="middle" fill="#64748b" font-size="11" transform="rotate(-40 495,160)">power to read</text>'
                 '<text x="350" y="300" text-anchor="middle" fill="#64748b" font-size="11">power of circulation</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Reflexivity", "title": "You are part of the picture",
         "blocks": [
             {"t": "term", "word": "Reflexivity",
              "def": "Critical awareness of how your own position &mdash; identity, assumptions, "
              "presence and power &mdash; shapes the images you make and the meanings you read "
              "from them."},
             {"t": "hbox", "color": "cyan", "html": "There is no view from nowhere. A reflexive "
              "analyst states who they are, why they framed as they did, and how that colours "
              "the findings &mdash; rather than hiding behind the camera's apparent objectivity."},
         ]},

        {"type": "content", "label": "Triangulate", "title": "Don't let the image testify alone",
         "blocks": [
             {"t": "body", "html": "An image is one source among many. Read it against your "
              "fieldnotes, interviews, the maker's intent and the wider context. A photograph "
              "confirms, complicates or contradicts &mdash; it rarely proves on its own."},
             {"t": "hbox", "color": "cyan", "html": "Ask the people in the picture what it means "
              "to them. Member-checking your reading guards against imposing an outsider's "
              "interpretation on their lives."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "The Ethics of the Image"},

        {"type": "content", "label": "The Core", "title": "The camera is a form of power",
         "blocks": [
             {"t": "body", "html": "To photograph someone is to take something and to hold "
              "power over how they appear to others. In development settings &mdash; researcher "
              "with resources, subject often without &mdash; that power is sharply unequal."},
             {"t": "quote", "text": "To photograph people is to violate them, by seeing them as "
              "they never see themselves.",
              "attr": "&mdash; Susan Sontag, On Photography (1977)"},
         ]},

        {"type": "content", "label": "Two Consents", "title": "Consent to photograph &ne; consent to publish",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "To be photographed", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Agreement that an image may be made in the "
                   "moment. Necessary &mdash; but it does not license any later use."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "To publish / share", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Separate agreement to show the image in a "
                   "report, online, in a campaign. People may say yes to one and no to the other."}]}]},
             {"t": "hbox", "color": "red", "html": "Get both, in language people understand, and "
              "explain where the image could end up &mdash; including 'forever, on the internet'."},
         ]},

        {"type": "content", "label": "Ownership", "title": "Who owns the image?",
         "blocks": [
             {"t": "body", "html": "By default, copyright usually rests with whoever pressed the "
              "shutter &mdash; not the person depicted. In participatory work this is ethically "
              "fraught: the community's images may legally belong to the project."},
             {"t": "bullets", "items": [
                 "Agree ownership and licensing <em>before</em> shooting",
                 "Consider giving participants rights over their own images",
                 "Distinguish the photographer's copyright from the subject's rights",
                 "Be explicit about reuse, sale and archiving"]},
         ]},

        {"type": "content", "label": "The Gaze", "title": "Whose way of seeing is encoded?",
         "blocks": [
             {"t": "body", "html": "Every image embeds a <strong>gaze</strong> &mdash; a position "
              "of looking shaped by power, gender, class and history. The colonial gaze, the male "
              "gaze, the donor gaze: each frames the subject for a particular viewer."},
             {"t": "hbox", "color": "amber", "html": "Ask of any field image: who is this made "
              "<em>for</em>? If the answer is 'a distant donor' rather than 'the people in it', "
              "examine the gaze you are reproducing."},
         ]},

        {"type": "content", "label": "Children", "title": "Children and vulnerable subjects",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Children cannot give full legal consent &mdash; seek guardian consent <em>and</em> the child's assent",
                 "Never publish images that could endanger or shame a child",
                 "Extra care for survivors of violence, trafficking, illness, stigma",
                 "When in doubt, do not photograph &mdash; or anonymise thoroughly"]},
             {"t": "hbox", "color": "amber", "html": "Many organisations bar identifiable images "
              "of children in vulnerable situations entirely. A safeguarding policy should govern "
              "this, not a deadline or a donor's appetite for a 'strong image'."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "Anticipate downstream harm",
         "blocks": [
             {"t": "body", "html": "An image that seems harmless to you may endanger its subject: "
              "a photo identifying an undocumented migrant, a protester, a survivor, a person "
              "whose community would punish what the picture reveals."},
             {"t": "hbox", "color": "red", "html": "Think one step ahead: who might see this, and "
              "what could they do with it? The 'right to be seen' must always be balanced against "
              "the right to safety."},
         ]},

        {"type": "content", "label": "Codes", "title": "Ethics is ongoing, not a signature",
         "blocks": [
             {"t": "body", "html": "Formal ethics review and consent forms are a floor, not a "
              "ceiling. Visual ethics is a continuing relationship &mdash; revisited as the "
              "project, the images and their uses evolve."},
             {"t": "bullets", "color": "green", "items": [
                 "Let people see how their image will be used &mdash; and object",
                 "Honour withdrawal of consent, even later",
                 "Follow your organisation's safeguarding and data-protection rules",
                 "Treat dignity, not the image, as the deliverable"]},
         ]},

        {"type": "content", "label": "Found Images", "title": "Ethics of images you did not make",
         "blocks": [
             {"t": "body", "html": "Archival and social-media images carry their own consent and "
              "copyright burdens. A photograph posted publicly was not posted for <em>your</em> "
              "study &mdash; and the people in it never agreed to be your data."},
             {"t": "hbox", "color": "red", "html": "Public availability is not consent. Treat "
              "found images with the same care as ones you make: check rights, weigh harm, and "
              "anonymise where reuse could expose someone."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Representation &amp; Dignity"},

        {"type": "content", "label": "The Problem", "title": "Poverty porn",
         "blocks": [
             {"t": "term", "word": "Poverty porn",
              "def": "Imagery that exploits the suffering or destitution of subjects to provoke "
              "pity and donations &mdash; stripping people of agency, context and dignity for "
              "emotional effect."},
             {"t": "hbox", "color": "red", "html": "The flies-on-the-face, hand-outstretched, "
              "nameless-child photograph is the archetype. It raises money in the short term and "
              "corrodes dignity and truth in the long term."},
         ]},

        {"type": "content", "label": "Stereotype", "title": "How harmful images work",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Reduce a whole community to a single image of lack",
                 "Erase agency &mdash; people as passive victims, never actors",
                 "Strip context &mdash; no history, no cause, no structure",
                 "Flatten difference &mdash; 'the poor', 'the village', undifferentiated"]},
             {"t": "hbox", "color": "amber", "html": "Stereotyped images do not just misrepresent; "
              "they shape policy and public attitudes towards the people depicted."},
         ]},

        {"type": "content", "label": "Two Framings", "title": "The same person, two ways to show them",
         "blocks": [
             {"t": "table",
              "head": ["", "Undignified framing", "Dignified framing"],
              "rows": [
                  ["Posture", "Helpless, hand out", "Active, at work or speaking"],
                  ["Name", "Anonymous 'victim'", "Named, with their words"],
                  ["Context", "Stripped, decontextualised", "Situated in their world"],
                  ["Agency", "Acted upon", "Acting, deciding"],
                  ["Purpose", "Provoke pity in donors", "Convey reality &amp; voice"]]},
             {"t": "hbox", "color": "green", "html": "Dignity is not about hiding hardship. It is "
              "about showing people as full human beings who happen to face hardship."},
         ]},

        {"type": "content", "label": "Agency", "title": "Show agency and voice",
         "blocks": [
             {"t": "body", "html": "Dignified representation centres what people <em>do</em> and "
              "<em>say</em>, not only what they lack. Name them (where safe), quote them, show "
              "them acting, and let their account frame the image."},
             {"t": "quote", "text": "Nothing about us without us.",
              "attr": "&mdash; disability-rights principle, widely adopted in participatory practice"},
         ]},

        {"type": "content", "label": "Ethical Codes", "title": "Guidance NGOs already have",
         "blocks": [
             {"t": "body", "html": "Sector codes &mdash; such as Dóchas / the international "
              "<em>Code of Conduct on Images and Messages</em> &mdash; set out principles for "
              "respectful imagery: consent, accuracy, dignity, and showing people as equals."},
             {"t": "bullets", "color": "green", "items": [
                 "Respect the dignity of the people portrayed",
                 "Represent fairly, in context, without stereotype",
                 "Obtain informed consent for image and use",
                 "Give people a say in how they are shown"]},
         ]},

        {"type": "content", "label": "For Communicators", "title": "How NGOs should use field images",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Do", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Caption with name (if safe) &amp; context",
                      "Use the subject's own words",
                      "Show strength, work, ordinary life",
                      "Share images back with the community"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Don't", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Use shock to extract donations",
                      "Recycle images out of context",
                      "Caption with invented or generic stories",
                      "Show what could endanger or shame"]}]}]},
         ]},

        {"type": "content", "label": "The Test", "title": "The dignity test",
         "blocks": [
             {"t": "body", "html": "A simple check before publishing any field image: would the "
              "person in it be content to see this picture, this caption, in this place &mdash; "
              "and would you be comfortable if it were you, or someone you love?"},
             {"t": "hbox", "color": "cyan", "html": "If the honest answer is no, the image fails "
              "&mdash; however powerful, however much it might raise. Dignity is the deliverable."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Presenting Visual Research"},

        {"type": "content", "label": "Outputs", "title": "Many ways to show visual research",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Exhibition", "label": "Prints, community screenings, public displays",
                  "color": "cyan"},
                 {"num": "Photo-essay", "label": "Sequenced images + text that build an argument",
                  "color": "indigo"},
                 {"num": "Multimodal", "label": "Web, audio-slideshow, film, interactive pieces",
                  "color": "amber"}]},
             {"t": "body", "html": "Choose the form that reaches your audience and honours your "
              "participants &mdash; an exhibition in the community may matter more than a report "
              "to a distant funder."},
         ]},

        {"type": "content", "label": "The Photo-Essay", "title": "Sequencing tells the story",
         "blocks": [
             {"t": "body", "html": "A photo-essay is not a gallery of best shots; it is an "
              "<strong>argument made in sequence</strong>. Order, pacing, and the relation "
              "between images carry meaning as much as any single frame."},
             {"t": "flow", "steps": [
                 "OPEN: establish place and people",
                 "DEVELOP: build the theme image by image",
                 "TURN: complicate or deepen",
                 "CLOSE: resolve, or leave a deliberate question"]},
         ]},

        {"type": "content", "label": "Captions", "title": "The caption does heavy lifting",
         "blocks": [
             {"t": "body", "html": "A caption anchors meaning. The same photograph, captioned two "
              "ways, tells two different truths. Honest captions give context, attribute voice, "
              "and resist putting words in the subject's mouth."},
             {"t": "bullets", "color": "amber", "items": [
                 "State who, where, when &mdash; the verifiable facts",
                 "Use the subject's own words where you can",
                 "Avoid loaded adjectives that supply your verdict",
                 "Never caption a generic image with a specific false story"]},
         ]},

        {"type": "content", "label": "Give It Back", "title": "Return the work to the community",
         "blocks": [
             {"t": "body", "html": "Visual research too often extracts: images flow out to "
              "reports and donors, and nothing flows back. Ethical practice closes the loop."},
             {"t": "hbox", "color": "green", "html": "Hold the exhibition <em>in</em> the "
              "community first. Give people prints of themselves. Let participants present their "
              "own images. The audience that matters most is the one in the photographs."},
         ]},

        {"type": "content", "label": "Tools", "title": "Practical tools to grow into",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["A decent phone camera", "Most field photography", "The best camera is the one you have"],
                  ["KoboToolbox / ODK", "Linking images to survey records", "Free, offline, captures metadata"],
                  ["Audacity / phone recorder", "Audio for elicitation &amp; video", "Free; back up everything"],
                  ["Shotcut / DaVinci Resolve", "Editing participatory video", "Free, capable editors"],
                  ["A simple image log (sheet)", "Metadata &amp; consent tracking", "Low-tech beats no record"],
                  ["Exhibition prints / projector", "Community screenings", "Reach people offline"]]},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Doing Visual Ethnography</em> &mdash; Sarah Pink (the modern standard)",
                 "<em>Visual Anthropology: Photography as a Research Method</em> &mdash; John Collier Jr.",
                 "<em>On Photography</em> &mdash; Susan Sontag (the camera &amp; power)",
                 "<em>Ways of Seeing</em> &mdash; John Berger (how we look)",
                 "Wang &amp; Burris (1997) &mdash; the founding photovoice paper"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Qualitative Methods</strong>, <strong>Research Ethics</strong> and "
              "<strong>Data Feminism</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>The camera is never neutral</strong> &mdash; it carries power and a gaze",
                 "<strong>Hand over the camera</strong> when you can &mdash; let people frame their own lives",
                 "<strong>Consent to photograph is not consent to publish</strong> &mdash; ask for both",
                 "<strong>Read what the image hides</strong> as well as what it shows",
                 "<strong>Dignity is the deliverable</strong> &mdash; never trade it for a 'strong image'"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Visual Ethnography 101 &middot; Complete",
         "headline": "Now go look<br>more carefully.",
         "byline": "A camera in the field is a relationship, not just a tool. Make images "
                   "<em>with</em> people, read them critically, and let dignity govern every "
                   "frame. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
