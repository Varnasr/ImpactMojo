/* =============================================================================
   ImpactMojo — Fundamentals: the Power Cube
   -----------------------------------------------------------------------------
   The cube is John Gaventa's, from "Finding the Spaces for Change: A Power
   Analysis", IDS Bulletin 37(6), 2006. The three dimensions and their nine
   categories are his, building on Steven Lukes' three dimensions of power
   (1974) and on VeneKlasen and Miller's forms of power (2002). The teaching
   resource lives at powercube.net, run by IDS.

   ImpactMojo adds the Indian evidence: for each category, and for a set of
   documented Indian cases plotted on all three dimensions at once.
   ============================================================================= */

window.CUBE = (function () {
  "use strict";

  var dims = [
    {
      id: "space", name: "Spaces", color: "#7c3aed",
      question: "Where does the decision get made, and who set the table?",
      cats: [
        { id: "closed", name: "Closed", color: "#4c1d95",
          gaventa: "Decisions are made by a set of actors behind closed doors, without any pretence of broadening the boundaries of who is involved.",
          evidence: [
            { stat: "Collegium", detail: "Judges of the Supreme Court and High Courts are selected by a collegium of senior judges. There is no application, no published criteria and no external participation. The 99th Amendment tried to replace it and was struck down in 2015.", source: "Supreme Court Advocates-on-Record Association v. Union of India", year: "2015" },
            { stat: "116", detail: "internet shutdown orders in one year, the sixth year running that India led the world. Orders are issued under the Telegraph Act by an executive officer and are frequently not published.", source: "Access Now, #KeepItOn", year: "2023" },
            { stat: "Ordinances", detail: "Union and state governments legislate by ordinance between sessions under Articles 123 and 213, which produces binding law with no debate and no hearing.", source: "Constitution of India", year: "1950" }
          ],
          complication: "A closed space is not always illegitimate. Judicial independence is a reason to keep some decisions away from popular pressure, and the collegium's defenders make exactly that argument. The cube asks who is inside the room, not whether the room should exist."
        },
        { id: "invited", name: "Invited", color: "#7c3aed",
          gaventa: "People are invited to participate by authorities, whether by government, supranational agencies or NGOs. The invitation, and its terms, come from the powerholder.",
          evidence: [
            { stat: "2.6 lakh", detail: "gram panchayats hold gram sabha meetings that state law requires, with quorum and notice rules. The agenda, timing and follow-up are set by the administration.", source: "Ministry of Panchayati Raj", year: "2024" },
            { stat: "§17", detail: "MGNREGA requires the gram sabha to conduct social audits of every work in its jurisdiction, with records read aloud in public.", source: "Mahatma Gandhi National Rural Employment Guarantee Act", year: "2005" },
            { stat: "2006", detail: "EIA public hearings give affected people a recorded chance to object before a project is cleared, on a notice period and format the regulator sets.", source: "Environment Impact Assessment Notification", year: "2006" }
          ],
          complication: "Invited spaces are where most participatory practice happens, and the invitation is also the limit. Gaventa's point is that entering one can legitimise a decision without changing it, which is why the cube asks people to look at the other two spaces before judging how much a seat is worth."
        },
        { id: "claimed", name: "Claimed", color: "#a78bfa",
          gaventa: "Spaces claimed by less powerful actors from or against the powerholders, or created more autonomously by them: social movements, community associations, places people come together on their own terms.",
          evidence: [
            { stat: "1990s", detail: "The Mazdoor Kisan Shakti Sangathan's public hearings in rural Rajasthan, where wage records were read aloud against what people were actually paid, ran with no statutory basis at all. The Right to Information Act followed a decade later.", source: "MKSS; Right to Information Act 2005", year: "1990s" },
            { stat: "1985", detail: "The Narmada Bachao Andolan organised against the Sardar Sarovar dam outside any official process, and forced the first World Bank independent review of a project it was funding.", source: "Morse Commission, World Bank", year: "1992" },
            { stat: "2012", detail: "Protests after the Delhi gang rape produced the Justice Verma Committee, which took 80,000 public submissions in 29 days, and then the Criminal Law (Amendment) Act.", source: "Justice J.S. Verma Committee Report; Criminal Law (Amendment) Act", year: "2013" }
          ],
          complication: "Claimed spaces are the ones that most often change the rules, and they are also the least durable. Each of these three was absorbed into official process afterwards, which is a victory and a domestication at the same time."
        }
      ]
    },
    {
      id: "level", name: "Levels", color: "#0f766e",
      question: "At which level is the decision actually taken?",
      cats: [
        { id: "local", name: "Local", color: "#134e4a",
          gaventa: "The level closest to where people live, where participation is most often invited and where the decisions available may already have been bounded from above.",
          evidence: [
            { stat: "29", detail: "subjects are listed in the Eleventh Schedule for devolution to panchayats. How many a state actually devolves, with funds and staff attached, is the state's choice.", source: "Constitution (73rd Amendment) Act", year: "1992" },
            { stat: "Untied", detail: "Finance Commission grants reach panchayats directly, but most local budgets remain tied to centrally designed schemes, which sets the menu before the gram sabha meets.", source: "Fifteenth Finance Commission", year: "2021-26" }
          ],
          complication: "Local is where participation is easiest to organise and where the least tends to be at stake. A gram sabha with real authority over a scheme it did not design, cannot alter and does not fund is participating at one level in a decision taken at another."
        },
        { id: "national", name: "National", color: "#0f766e",
          gaventa: "The level at which most binding law and budget is set, and where formal representation substitutes for direct participation.",
          evidence: [
            { stat: "16%", detail: "of Bills introduced in the 17th Lok Sabha were referred to a parliamentary committee, against 71% in the 15th. Pre-legislative consultation policy exists but is not binding.", source: "PRS Legislative Research", year: "2019-24" },
            { stat: "4.4% / 13.6%", detail: "of the 18th Lok Sabha are Muslim and women respectively, against 14.2% and roughly half of the population.", source: "Election Commission of India; Census 2011", year: "2024" }
          ],
          complication: "The cube's national level is where the wheel's axes bite hardest. Who sits in the room is itself patterned by caste, religion and gender, so a national space can be formally open and demographically closed at once."
        },
        { id: "global", name: "Global", color: "#14b8a6",
          gaventa: "The level of treaties, lenders and standard-setters, where decisions with domestic force are taken in rooms no domestic citizen can enter.",
          evidence: [
            { stat: "WTO", detail: "India's public stockholding for food security, which underpins the PDS, has been contested at the WTO since 2013 and runs under an interim peace clause rather than a settled rule.", source: "WTO Bali Ministerial Decision", year: "2013" },
            { stat: "TRIPS", detail: "India's patent law, including the Section 3(d) bar on evergreening upheld in the Novartis case, is written inside the space TRIPS leaves.", source: "Novartis AG v. Union of India", year: "2013" }
          ],
          complication: "Global decisions are the hardest to hold anyone accountable for, and also the ones where Indian negotiators have sometimes had more room than the framing suggests. Section 3(d) exists because that room was used."
        }
      ]
    },
    {
      id: "form", name: "Forms", color: "#b45309",
      question: "How is the power being exercised, and can you see it?",
      cats: [
        { id: "visible", name: "Visible", color: "#78350f",
          gaventa: "Observable decision-making: the formal rules, structures, authorities and procedures. Who makes the law, and who sits where.",
          evidence: [
            { stat: "Statute", detail: "Reservation in legislatures, education and public employment for SCs, STs and OBCs is written into the Constitution and is contested in the open, in Parliament and in court.", source: "Constitution of India, Arts. 15, 16, 330, 332", year: "1950 onward" },
            { stat: "Published", detail: "Budgets, Bills, judgments and gazette notifications are all published. Visible power is the layer India documents best, which is why most evidence on this page describes it.", source: "Parliament of India; eGazette", year: "current" }
          ],
          complication: "Visible power is the easiest to study and the easiest to overestimate. A law can be entirely public and still be irrelevant to what happens, which is what the other two forms are for."
        },
        { id: "hidden", name: "Hidden", color: "#b45309",
          gaventa: "Power exercised by setting the agenda: keeping certain issues and certain people away from the table, so that the decision never comes up for a decision.",
          evidence: [
            { stat: "1931", detail: "No Indian census has enumerated caste beyond SC and ST since 1931. Without a count there is no denominator, and a claim for proportional share cannot be argued in the terms policy uses.", source: "Census of India", year: "1931" },
            { stat: "Para 3", detail: "The 1950 Presidential Order bars Dalit Christians and Dalit Muslims from SC status. The Ranganath Misra Commission recommended removing the religious bar in 2007 and it has not been removed.", source: "Constitution (Scheduled Castes) Order; Ranganath Misra Commission", year: "1950, 2007" },
            { stat: "22.3%", detail: "of registered deaths in India carry a medically certified cause. What kills four in five Indians does not enter the record that health budgets are argued from.", source: "Medical Certification of Cause of Death, ORGI", year: "2022" }
          ],
          complication: "Hidden power is inferred rather than observed, which makes it the easiest claim to overreach on. The disciplined version names the specific issue kept off the table, and who benefits from its absence, rather than asserting a general conspiracy."
        },
        { id: "invisible", name: "Invisible", color: "#f59e0b",
          gaventa: "Power that shapes meaning and what people accept as normal, so that an arrangement is not experienced as a decision at all and grievance does not form.",
          evidence: [
            { stat: "~27%", detail: "of surveyed households said someone in the household practises untouchability. It persists as ordinary domestic conduct rather than as a policy anyone defends.", source: "India Human Development Survey-II", year: "2011-12" },
            { stat: "~95%", detail: "of Indian marriages are within caste. Endogamy at that rate is maintained by preference and family expectation, not by any rule that could be repealed.", source: "India Human Development Survey-II", year: "2011-12" },
            { stat: "299 vs 97", detail: "minutes a day of unpaid domestic work by women and men. The allocation is treated as a fact of life rather than as a distribution anyone chose, and no national account records it.", source: "Time Use Survey, NSO", year: "2019" }
          ],
          complication: "Invisible power is the level at which the cube is most useful and least testable. These three figures show a pattern consistent with internalised norms, and they cannot by themselves distinguish a norm someone accepts from a constraint they cannot escape."
        }
      ]
    }
  ];

  /* Documented Indian cases, plotted on all three dimensions at once. */
  var cases = [
    { name: "MKSS wage hearings, Rajasthan", space: "claimed", level: "local", form: "hidden",
      note: "Muster rolls read aloud against what people were actually paid. A claimed local space used to drag hidden power into view; the practice became statutory as the RTI Act a decade later.", year: "1990s" },
    { name: "Right to Information Act", space: "invited", level: "national", form: "hidden",
      note: "Turned an activist practice into a national entitlement, and converted a claimed space into an invited one. Its work is against hidden power: it makes the file available.", year: "2005" },
    { name: "MGNREGA social audit", space: "invited", level: "local", form: "visible",
      note: "The state invites the gram sabha to audit the state, on a schedule the state sets. Visible power made contestable in the village where the work happened.", year: "2005" },
    { name: "Niyamgiri gram sabha referendum", space: "invited", level: "local", form: "visible",
      note: "The Supreme Court created an invited local space and made its output binding. Twelve assemblies were convened and all twelve refused the mine.", year: "2013" },
    { name: "Narmada Bachao Andolan", space: "claimed", level: "global", form: "visible",
      note: "A claimed space that reached the global level, forcing the first independent review of a World Bank-funded project.", year: "1985 onward" },
    { name: "Judicial collegium", space: "closed", level: "national", form: "hidden",
      note: "Selection of judges by judges, with no application and no published criteria. Parliament's attempt to open it was struck down in 2015.", year: "1993 onward" },
    { name: "Caste not counted since 1931", space: "closed", level: "national", form: "hidden",
      note: "An absence rather than an act. Keeping the count off the table keeps the claim it would support out of policy argument.", year: "1931 onward" },
    { name: "Untouchability in the household", space: "closed", level: "local", form: "invisible",
      note: "No decision is taken and no rule is cited. Roughly a quarter of surveyed households reported the practice, sustained as ordinary conduct.", year: "2011-12" }
  ];

  return { dims: dims, cases: cases };
})();
