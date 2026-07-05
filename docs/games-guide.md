# Games Guide

## What Are the ImpactMojo Games?

ImpactMojo offers **interactive games** that teach development-relevant concepts through strategic decision-making and simulation. Each game takes 10–20 minutes to play and covers a specific concept — from game theory and market failures to climate action, gender equity, public health, and digital ethics.

These aren't quizzes or flashcards. They're interactive simulations where your decisions have consequences, and the concepts become clear through play rather than lecture.

All games are **free, browser-based, and require no login**. They are self-hosted at `/Games/` on impactmojo.in.

### MiroFish AI Agents

The economics games feature **MiroFish AI agents** — AI-powered opponents with distinct South Asian identities, backstories, and strategic personalities. Each agent has calibrated personality traits (cooperation bias, risk tolerance, memory weight) that shape their decisions. You're not playing against a random number generator — you're negotiating with Meera the pragmatic NGO director, debating Arjun the idealistic researcher, or competing against Nandini the shrewd procurement officer.

The AI system uses a **multi-provider LLM fallback chain** (DeepSeek → Groq → Gemini → Together → OpenAI) via a Supabase Edge Function. When LLM providers are unavailable, a local personality engine generates decisions using weighted heuristics — so games always work, even offline.

See [Game Agents documentation](game-agents.md) for technical details on the AI system.

### Indian Folk Art Story Illustrations

Every game features **original Indian folk art** rendered as inline SVGs in six traditional styles:

| Art Style | Origin | Games |
|-----------|--------|-------|
| **Warli** | Maharashtra — white line art on terracotta | Climate Action, Cooperation Paradox, Network Effects, Counterfactual |
| **Madhubani** | Bihar — bold outlines, bright fills, nature motifs | Gender Equity, Econ Concepts, Real Middle India |
| **Gond** | Madhya Pradesh — dot patterns, vibrant nature-tech fusion | Prisoners' Dilemma, Digital Ethics |
| **Kalamkari** | Andhra Pradesh — pen-drawn narrative scrolls | Opportunity Cost, Risk & Reward |
| **Pichwai** | Rajasthan — devotional temple art, rich detail | Bidding Wars, Public Good |
| **Pattachitra** | Odisha — scrollwork narrative art, bold outlines | Information Asymmetry, Public Health |

Each game includes:
- **Story intro screen** — a full-screen folk art scene setting the narrative context
- **Mid-game interludes** — art and narrative that respond to your choices between rounds
- **Adaptive ending art** — different illustrations based on your overall performance

The art grounds each game in South Asian visual culture while making abstract concepts tangible through storytelling.

---

## The Games

### Collective Action & Cooperation

| Game | Concept | What You Learn | AI Agents |
|------|---------|---------------|-----------|
| **Public Good Game** | Free-rider problem | Why people under-contribute to shared resources, and what mechanisms sustain cooperation | Meera, Arjun, Fatima, Ravi |
| **Commons Crisis Game** | Tragedy of the commons | How communication, monitoring, and sanctions help communities manage shared resources like water, forests, or fisheries | Priya, Raj, Ananya, Karthik |
| **Cooperation Paradox** | Game theory | Why cooperation yields better outcomes but individual incentives push toward competition — Nash equilibrium and Pareto efficiency in action | Imran, Reshma |
| **Prisoners' Dilemma Game** | Strategic interdependence | How trust, reputation, and repeated interactions overcome cooperation failures | Sunita, Vikram, Lakshmi, Deepak |

### Markets & Decision-Making

| Game | Concept | What You Learn | AI Agents |
|------|---------|---------------|-----------|
| **Opportunity Cost Game** | Tradeoffs | How every choice has a cost — the next-best alternative you gave up — and how this shapes policy decisions | Pallavi, Suresh |
| **Risk & Reward Explorer** | Behavioural economics | Risk preferences, expected utility, prospect theory — why people make seemingly irrational choices under uncertainty | Sanjay, Pooja, Arun |
| **Bidding Wars Game** | Auction theory | How different auction formats affect prices, why winners sometimes overpay (winner's curse), and how procurement works | Nandini, Sameer, Zara |
| **Information Asymmetry Game** | Asymmetric information | Adverse selection, moral hazard, and signalling — what happens when buyers and sellers know different things | Kavitha, Mohan, Aisha |

### Systems & Scale

| Game | Concept | What You Learn | AI Agents |
|------|---------|---------------|-----------|
| **Network Effects Game** | Network economics | How value multiplies as more people join, critical mass dynamics, and why some platforms dominate | Tanvi, Harish, Divya |
| **Externality Game** | Market failures | Hidden social costs and benefits — pollution, education spillovers — and why markets alone don't solve them | Ashok, Nalini, Bina |
| **The Real Middle** | Inequality dynamics | Wealth distribution, income mobility, and the precarity of middle-class status in India | 5 simulated households |
| **Econ Concepts Puzzle** | Mixed economics | Economic reasoning through puzzles and brain-teasers covering supply/demand, game theory, and market structure | — |

### Beyond Economics

| Game | Concept | What You Learn | AI Agents |
|------|---------|---------------|-----------|
| **Climate Action Challenge** | Climate science | Allocate resources between mitigation and adaptation across decades — the lesson that both are needed together | — |
| **Care Economy Challenge** | Gender equity | Experience the invisible burden of unpaid care work and how policy choices affect equity outcomes | — |
| **Epidemic Response** | Public health | Manage a disease outbreak across surveillance, treatment, prevention, community health workers, and communication | — |
| **Counterfactual: The Evaluation Game** | Causal inference | Eight impact claims from Indian programmes, each hiding a classic trap — regression to the mean, self-selection, survivorship bias, spillovers, the observer effect. Pick the evaluation design that finds what would have happened anyway | — |

---

## How Educators Can Use the Games

### As Workshop Openers

Play a game at the start of a session to introduce a concept experientially. Participants engage with the idea *before* you explain the theory — this creates curiosity and gives them a shared reference point for discussion.

**Example flow:**
1. Play the Public Good Game (10 minutes)
2. Debrief: "What happened? Why did contributions drop?" (10 minutes)
3. Introduce the formal concept of public goods and free-riding (15 minutes)
4. Discuss real-world applications in their programmes (15 minutes)

### As Classroom Activities

Games work well projected on a screen for group play. Have the class vote on decisions together, or split into teams and compare outcomes.

**Good pairings:**
- Public Good Game + Commons Crisis = comprehensive view of collective action
- Information Asymmetry + Externality = understanding market failures together
- Prisoners' Dilemma + Cooperation Paradox = deep dive into strategic thinking

### As Self-Study Assignments

Assign 2–3 games as pre-work before a workshop. Ask participants to write a one-paragraph reflection: "What surprised you? How does this concept show up in your work?"

### For Debrief Discussions

After any game, these questions work well:
- What strategy did you use? Did it change over rounds?
- What surprised you about the outcome?
- Where do you see this dynamic in your development work?
- What mechanisms could change the outcome?

---

## Getting Started

1. **Visit the Games section** on [impactmojo.in](https://www.impactmojo.in) — scroll to the Games showcase or find them in the catalog
2. **Start with Public Good Game or Prisoners' Dilemma** — these are the most intuitive entry points
3. **Play each game yourself first** before using it in a workshop, so you can anticipate participant questions
4. **No login or download required** — games run in any modern browser on desktop or mobile

---

## Tips

- **Games are designed for adults, not children.** The framing, language, and complexity are pitched at development practitioners and university students.
- **Debrief is where learning happens.** The game itself creates the experience; the discussion afterward creates the understanding. Always budget time for debrief.
- **Play multiple rounds.** Most games reveal deeper dynamics on second and third plays as participants adjust their strategies.
- **Connect to real programmes.** After playing the Commons Crisis Game, ask: "Where in your WASH programme do you see a commons dilemma?" This transfer step is essential.
