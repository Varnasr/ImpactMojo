/* =============================================================================
   ImpactMojo — Fundamentals: deriving a wheel position from questions
   -----------------------------------------------------------------------------
   Why this exists
   ---------------
   The wheel originally asked people to mark where they sat. Self-placement
   measures self-perception, and self-perception is itself patterned by power:
   people near the centre routinely place themselves further out. So the error
   was not random — it ran in the direction that mattered most.

   These questions ask about group membership as a matter of fact, and then
   apply the wheel's OWN published band definitions to the answer. That is the
   whole of what happens. The result is not a measurement of anyone's life; it
   is the wheel's classification, shown back with the definition it used, so a
   person can see the reasoning and disagree with it.

   Design rules this file follows
   ------------------------------
   1. Every question is answerable as a fact, not a judgment. No question asks
      how excluded someone feels.
   2. Every question can be skipped, and skipping is offered as a first-class
      answer rather than buried. Caste, sexual orientation, religion and
      disability are all here; nobody should have to declare any of them.
   3. Every option carries the plain group name from the wheel's own data, never
      "closer to power" or "pushed to the margin" — the band is revealed after,
      with its definition, not embedded in the question.
   4. Nothing is scored, summed or ranked. A wheel is not a league table.
   5. Answers never leave the browser. There is no endpoint, and the storage key
      is the same one the manual marks already used.

   The suggestion to derive placement from questions rather than self-marking
   came from Pallavi, who also proposed the material axes on the outer band.
   ============================================================================= */

window.FUNDAMENTALS_ASSESS = (function () {
  "use strict";

  /* Each option's `band` is the ring in js/fundamentals-data.js it maps to.
     `note` is shown on the reveal, and is the definition being applied. */
  var questions = [
    {
      axis: "caste",
      q: "Which of these describes the caste category your family is recorded under?",
      help: "India has not enumerated caste beyond SC and ST since 1931, so this uses the administrative categories that do exist.",
      options: [
        { band: "margin", label: "Scheduled Caste or Scheduled Tribe" },
        { band: "middle", label: "Other Backward Class, including Extremely Backward Class" },
        { band: "power",  label: "None of these — recorded as 'General' or 'Others'" }
      ]
    },
    {
      axis: "gender",
      q: "Does the gender you live in match the one you were assigned at birth?",
      options: [
        { band: "power",  label: "Yes, and I am a man" },
        { band: "middle", label: "Yes, and I am a woman" },
        { band: "margin", label: "No — I am transgender, non-binary or intersex" }
      ]
    },
    {
      axis: "sexuality",
      q: "Which of these is closest to your sexual orientation?",
      options: [
        { band: "power",  label: "Heterosexual" },
        { band: "middle", label: "Gay, lesbian or bisexual" },
        { band: "margin", label: "Asexual, aromantic, pansexual or questioning" }
      ]
    },
    {
      axis: "religion",
      q: "Which religion, if any, were you raised in or do you practise?",
      options: [
        { band: "power",  label: "Hindu" },
        { band: "middle", label: "Sikh, Jain, Buddhist, Parsi or Jewish" },
        { band: "margin", label: "Muslim, Christian, or an Indigenous faith such as Sarna" }
      ]
    },
    {
      axis: "economic",
      q: "Where does most of your household's income come from?",
      options: [
        { band: "power",  label: "Property, land, rent or returns on capital" },
        { band: "middle", label: "A salary or a stable business" },
        { band: "margin", label: "Daily or seasonal work, or we are living on debt" }
      ]
    },
    {
      axis: "education",
      q: "What is the highest level of formal education you completed?",
      options: [
        { band: "power",  label: "A college degree or higher" },
        { band: "middle", label: "Finished school, or the first in my family to study" },
        { band: "margin", label: "No formal schooling, or schooling that was interrupted" }
      ]
    },
    {
      axis: "ability",
      q: "Do you live with a disability, chronic illness or significant neurodivergence?",
      help: "India records disability at about 2.2% of the population against a global estimate nearer 16%, so a great many people who would answer yes here have no certificate.",
      options: [
        { band: "power",  label: "No" },
        { band: "middle", label: "Yes — mild, undiagnosed or without a certificate" },
        { band: "margin", label: "Yes — severe, multiple, or significant neurodivergence" }
      ]
    },
    {
      axis: "body",
      q: "Thinking about skin colour, build and how conventionally gendered your appearance reads — how are you usually treated?",
      help: "This is the one question here about how others read you rather than about a category you belong to.",
      options: [
        { band: "power",  label: "As fair-skinned and conventionally presenting" },
        { band: "middle", label: "Unremarkably — I am not usually singled out either way" },
        { band: "margin", label: "As dark-skinned, visibly different, disabled or gender-nonconforming" }
      ]
    },
    {
      axis: "language",
      q: "Which languages can you conduct official business in — a bank, a hospital, a government office?",
      options: [
        { band: "power",  label: "English, and the language of my state" },
        { band: "middle", label: "One Scheduled language only" },
        { band: "margin", label: "A non-Scheduled or Indigenous language" }
      ]
    },
    {
      axis: "age",
      q: "Which describes you now?",
      options: [
        { band: "power",  label: "A young adult in the labour market" },
        { band: "middle", label: "Middle-aged" },
        { band: "margin", label: "A child, or an elder who depends on others" }
      ]
    },
    {
      axis: "geography",
      q: "Where do you live, and is your citizenship ever questioned?",
      options: [
        { band: "power",  label: "In a metro, as a local, with citizenship never in question" },
        { band: "middle", label: "In a rural area, or as a migrant from another state" },
        { band: "margin", label: "In Kashmir, the North-East or the islands — or I am not a citizen" }
      ]
    },
    {
      axis: "relationship",
      q: "Which describes your relationship status, as your family and the law see it?",
      options: [
        { band: "power",  label: "Married, within caste and religion, with family approval" },
        { band: "middle", label: "Dating, engaged, or married under pressure" },
        { band: "margin", label: "Single, divorced, separated, widowed, or in a relationship the law does not recognise" }
      ]
    }
  ];

  return { questions: questions, SKIP: "__skip__" };
})();
