/* =============================================================================
   ImpactMojo — Fundamentals: the Ladder of Citizen Participation
   -----------------------------------------------------------------------------
   The ladder is Sherry R. Arnstein's, from "A Ladder of Citizen Participation",
   Journal of the American Institute of Planners 35(4), July 1969. The eight
   rungs and the three bands are hers. What ImpactMojo adds is an Indian
   evidence layer: for each rung, the law, scheme or judgment that puts a real
   Indian practice on it, with the source and year named.

   Same rule as the wheel: every entry carries a named source and a year, and
   where the placement rests on a pattern rather than a statistic, the entry
   says so instead of inventing precision.
   ============================================================================= */

window.LADDER = (function () {
  "use strict";

  var BANDS = {
    power:   { label: "Citizen power",   note: "Citizens hold decision-making authority." },
    token:   { label: "Tokenism",        note: "Citizens are heard. Nothing obliges anyone to act on what they say." },
    nonpart: { label: "Non-participation", note: "The exercise stands in for taking part." }
  };

  var rungs = [
    {
      n: 8, id: "citizen-control", name: "Citizen control", band: "power", color: "#166534",
      arnstein: "Participants govern the programme outright, with full charge of policy and management and no intermediaries between them and the source of funds.",
      india: "Village assemblies make a decision the state is legally bound to accept.",
      evidence: [
        { stat: "2013", detail: "The Supreme Court held that the gram sabhas of Niyamgiri, not the state government, would decide whether bauxite mining could proceed on their hills. Twelve village assemblies were convened and all twelve refused. The environment ministry cancelled the clearance in January 2014.", source: "Orissa Mining Corporation v. Ministry of Environment & Forests", year: "2013" },
        { stat: "§3(1)(i)", detail: "The Forest Rights Act gives the gram sabha the right to protect, regenerate and manage community forest resources. It is the strongest transfer of control to a village assembly anywhere in Indian statute.", source: "Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act", year: "2006" },
        { stat: "1996", detail: "PESA extends gram sabha authority across Fifth Schedule areas, including a mandatory consultation before land acquisition and ownership of minor forest produce.", source: "Panchayats (Extension to the Scheduled Areas) Act", year: "1996" }
      ],
      complication: "The law here runs well ahead of the practice. Rights and Resources Initiative assessed in 2015 that forest-dwelling communities hold legal title to under 5% of the land they customarily use, and states had rejected an average of 54% of the claims decided since 2008. Niyamgiri was also narrower than it looks: the state picked 12 villages to vote, out of 112 in the affected area."
    },
    {
      n: 7, id: "delegated-power", name: "Delegated power", band: "power", color: "#15803d",
      arnstein: "Citizens hold a clear majority on a body, or real delegated authority, so that officials must negotiate rather than instruct.",
      india: "Elected local bodies control budgets and subjects in their own right.",
      evidence: [
        { stat: "1992", detail: "The 73rd and 74th Amendments made panchayats and municipalities constitutional bodies, with 29 subjects listed in the Eleventh Schedule available for devolution to them.", source: "Constitution (73rd and 74th Amendment) Acts", year: "1992" },
        { stat: "35–40%", detail: "of Kerala's annual state plan budget was devolved to local governments in the first years of the People's Plan Campaign, with gram sabhas and development seminars setting local priorities.", source: "People's Plan Campaign, Government of Kerala", year: "1996 onward" },
        { stat: "1/3 → 1/2", detail: "of panchayat seats reserved for women by the 73rd Amendment, raised to half by more than twenty states. India has more elected women in local government than any other country.", source: "Constitution (73rd Amendment) Act; Ministry of Panchayati Raj", year: "1992 onward" }
      ],
      complication: "Devolution is a state subject, so the rung a panchayat stands on varies by state. Most devolved functions without the funds or the staff to discharge them, leaving an elected body with authority on paper and a budget it does not control. Kerala gets cited constantly because few states went as far."
    },
    {
      n: 6, id: "partnership", name: "Partnership", band: "power", color: "#4d7c0f",
      arnstein: "Power is redistributed through negotiation. Planning and decision-making are shared through joint committees, and neither side can act alone.",
      india: "The state and the community manage a resource jointly, under rules the state writes.",
      evidence: [
        { stat: "1990", detail: "The Joint Forest Management circular invited village committees to co-manage degraded forest in return for a share of the produce.", source: "Ministry of Environment & Forests circular", year: "1990" },
        { stat: "106,482", detail: "JFM committees across 28 states were managing about 22 million hectares of forest by 2006, involving roughly 14.5 million families.", source: "Ministry of Environment & Forests / Forest Survey of India", year: "2006" }
      ],
      complication: "JFM committees are created by executive circular rather than statute, and the forest department can wind one up. A partnership that one side can dissolve sits below rung 8 for that reason, and it is why the Forest Rights Act was argued for as a statutory replacement."
    },
    {
      n: 5, id: "placation", name: "Placation", band: "token", color: "#b45309",
      arnstein: "A few hand-picked citizens are placed on a board where they can be outvoted, which lets the powerholders say the community was represented.",
      india: "Community members sit on a committee that advises rather than decides.",
      evidence: [
        { stat: "75%", detail: "of a School Management Committee must be parents and guardians under the Right to Education Act, and the committee is to monitor the school and prepare its development plan.", source: "Right of Children to Free and Compulsory Education Act, §21", year: "2009" },
        { stat: "Advisory", detail: "In most states the SMC's development plan is a recommendation. The committee has no authority over teacher deployment, transfers or the school budget, which are the decisions that determine whether the school works.", source: "RTE §21–22 and state rules", year: "2009 onward" }
      ],
      complication: "On an organisation chart this rung looks the same as partnership, which makes it hard to spot from outside. Arnstein's test: count who can be outvoted, then check whether the body's output binds anyone."
    },
    {
      n: 4, id: "consultation", name: "Consultation", band: "token", color: "#c2410c",
      arnstein: "People are invited to give their views, with no assurance those views will count. Participation is measured by how many turned up, not by what changed.",
      india: "A hearing is held, minuted, and the decision proceeds.",
      evidence: [
        { stat: "2006", detail: "The EIA Notification made a public hearing compulsory for most large projects, giving affected people a recorded opportunity to object before clearance.", source: "Environment Impact Assessment Notification", year: "2006" },
        { stat: "30 → 20", detail: "days of public notice for those hearings, as proposed in the 2020 draft EIA notification. The proposal drew over 1.7 million public responses and was not finalised.", source: "Draft EIA Notification 2020, Ministry of Environment", year: "2020" },
        { stat: "Quorum", detail: "Gram sabha meetings require quorum and notice under state panchayat Acts. Where either fails, the meeting is still commonly recorded as held.", source: "State Panchayati Raj Acts", year: "various" }
      ],
      complication: "Consultation suits a technical decision with one defensible answer, and treating it as failure there wastes everyone's time. It becomes tokenism when the decision had real alternatives and those were closed before the hearing."
    },
    {
      n: 3, id: "informing", name: "Informing", band: "token", color: "#d97706",
      arnstein: "A one-way flow of information from officials to citizens, with no channel for feedback and no power to negotiate.",
      india: "The state publishes what it has decided and what it has spent.",
      evidence: [
        { stat: "§4(1)(b)", detail: "The Right to Information Act requires every public authority to publish 17 categories of information on its own initiative, without anyone having to ask.", source: "Right to Information Act", year: "2005" },
        { stat: "Muster rolls", detail: "MGNREGA requires job cards, muster rolls and payment records to be publicly displayed and read out at social audits, making the paper trail contestable in the village where the work happened.", source: "Mahatma Gandhi National Rural Employment Guarantee Act, §17", year: "2005" }
      ],
      complication: "Arnstein placed informing on the tokenism band, which fits one-way disclosure. India's version sits awkwardly there: MGNREGA's social audit gives the information a return channel, and disclosure with a forum to contest it behaves more like the rungs above."
    },
    {
      n: 2, id: "therapy", name: "Therapy", band: "nonpart", color: "#9f1239",
      arnstein: "Powerlessness is treated as the citizens' own condition. The programme sets out to change them rather than the thing they are objecting to.",
      india: "The deficit is located in the community's behaviour rather than in the service.",
      evidence: [
        { stat: "Pattern", detail: "Behaviour-change campaigns that frame a shortfall as attitude while the underlying access gap persists. No Indian statistic isolates this rung; it is identified by what a programme's theory of change blames, so it is described here rather than counted.", source: "Characterisation, not a measurement", year: "2026" }
      ],
      complication: "Critics reach for this rung too readily. Behaviour does matter for some outcomes, and calling every demand-side programme therapy is lazy. Arnstein's distinction was whether the citizen is engaged as a person with a grievance or as a problem to be treated."
    },
    {
      n: 1, id: "manipulation", name: "Manipulation", band: "nonpart", color: "#881337",
      arnstein: "People are placed on advisory bodies for the purpose of engineering their support. Participation becomes a public relations exercise for a decision already taken.",
      india: "The consultation is held because the file requires one.",
      evidence: [
        { stat: "Sequence", detail: "What marks this rung is order. The hearing follows the decision rather than preceding it, and the record exists to satisfy a procedural requirement. Identified by sequence, not by a statistic.", source: "Characterisation, not a measurement", year: "2026" }
      ],
      complication: "The bottom rung is an accusation, so it needs evidence about a specific decision rather than a general posture. The answerable question is narrow: what could this consultation have changed, and was that still open when it was held?"
    }
  ];

  return { rungs: rungs, BANDS: BANDS };
})();
