A rubric turns “this answer should be good” into a standard someone can apply, explain and revise. It identifies the task, the artifact being judged, the conditions that matter and what a failure means. A clear rubric defines the intended target; it does not by itself prove that a human or model applies the target reliably, or that the target captures the real-world outcome.

## Write a criterion someone can act on

Begin with the user’s task and ask a domain owner what successful work must do, what unacceptable work looks like and which exceptions matter. Replace a generic helpfulness score with observable conditions. For a travel planner, a workshop describes checking the requested number of days, budget and use of trip details in follow-up answers. A different team illustrates a possible offline check that would penalize reports with more than three suggested fixes to control verbosity; that limit is a local presentation choice, not a general rule or a measure of diagnostic correctness. [cite:gv4w23xYj-0:c04] [cite:0RNNfxpdbQk:c04]

**Illustrative rubric excerpt: travel follow-up.** The task is to answer a user's question about an existing itinerary. Judge whether the answer uses the trip details relevant to that question.

- **Pass:** addresses the follow-up using the relevant itinerary constraint, or explicitly says the needed detail is unavailable.
- **Fail:** gives generic advice while ignoring an available, relevant trip constraint, or invents the missing detail.
- **Not applicable:** the follow-up does not depend on the itinerary.
- **Failure reason:** identify the ignored or invented constraint and the relevant passage, so the team knows what to investigate.

This excerpt is a proposed local standard, not a validated travel evaluator. The owner must decide, for instance, whether acknowledging missing information is acceptable for the actual task. Lyft’s described support rubric distinguishes excessive repeated education from escalating too early: both can be wrong, but fixing one by always doing the other would miss the goal. In a clinical case, clinicians defined expected behaviors and hazards, and a judge returned pass/fail, triggered hazard and reason; structured reasons help inspection but do not independently prove clinical correctness. [cite:3z2uT5aDx_Y:c05] [cite:McknwOzbmyg:c05]

Maintain rubric text as evaluation logic: version criteria and examples, review changes with the domain owner, and test their effects. Separating instructions, candidate material and examples makes their roles legible, but delimiters such as XML are not established prompt-injection protection. Detailed failures can also inform what behavior-specific training data to collect even when a separate scalar reward is used for training. Mapping the right evidence into a judge is a separate prerequisite: [[give-judges-the-evidence-and-context-they-need]]. [cite:SHMCGrNJJGc:c08] [cite:TNwJ1LMiENk:c09]

## Separate dimensions without making every clue mandatory

A single overall rating can conceal distinct problems. A response may be fluent but use the wrong year, as in a prepared travel-agent example; relevance to a question is also different from covering every part of it. A visually attractive video may contain inconsistent events. These are separate properties because a pass on one does not entail a pass on another. [cite:iOXM3zE-2dk:c09] [cite:rTojoVotlD8:c10] [cite:KLDdXOw6jIc:c13]

Separate hard constraints from informative measures: a safety requirement may block release, while a style preference informs improvement. Separate genuinely independent outcomes so a failure is diagnosable, but do not turn every helpful signal into a required criterion. For an investment report, a valuation ratio might support a useful recommendation without being mandatory for every good recommendation. Ask the stakeholder whether the signal defines success or is only one possible route to it. [cite:Xfl50508LZM:c09]

More granular criteria can point to specific repairs and training needs. They also make consistent application harder as the list grows, especially for difficult tasks; proposed checks for coverage, no-op behavior, variability and expert agreement are not themselves evidence of reliability. Choose enough detail to identify a meaningful failure, not a fixed number of bullets. [cite:mR-WAvEPRwE:c09] [cite:2aS7aKoXn64:c09]

## Choose labels for the decision

Use a binary issue label when the question is a concrete occurrence, such as whether a required constraint was violated, and define which label is the problem. Binary wording alone does not make the criterion sound. If partial success changes the decision, define anchored labels such as correct, partially correct and incorrect; use **not applicable** when the condition genuinely does not arise rather than silently counting it as pass or fail. State what improvement means and request a reason tied to the artifact. [cite:-aM2EDTiaMs:c03] [cite:pSto5YaNGUo:c05] [cite:gv4w23xYj-0:c09]

For qualitative tone, one practitioner reports using a category first and then a finer rating with examples and textual justification. That may preserve distinctions a binary label would lose, but the report does not establish that the staged format is universally more reliable. Score format is a design choice, not a substitute for defining quality. [cite:_dTF3NpPzGo:c06]

## Use examples to clarify boundaries, not dictate a template

Positive, negative and borderline examples can show how a criterion applies. Vary their surface form so an evaluator does not learn that one writing style or layout is the only acceptable answer; label the examples clearly apart from the candidate. Compare a rubric with and without examples on separate held-out cases, then inspect disagreements rather than assuming either version wins. Examples embedded in a prompt are not independent validation cases. [cite:qZj7sqmidqA:c10]

In a small 16-report workshop, removing examples slightly increased agreement with the presenter, but inspection revealed that the presenter had accepted a report without risks while the examples demanded them. The discrepancy was partly about the standard itself, not simply the judge: the team had to decide whether risks were required and reconcile the labels and rubric. This small experiment cannot establish that examples are generally helpful or harmful. [cite:SHMCGrNJJGc:c09]

For independent assessment of whether a judge applies the intended standard, see [[validate-judges-against-human-labels]]; for how reference judgments are collected and interpreted, see [[collect-and-interpret-human-judgments]]. A well-worded criterion and a reliable evaluator are different accomplishments.

## Make ownership of subjective standards explicit

Taste can be specified without pretending it is universal. Ask the owner for strong and weak examples, the differences that matter, and reasons behind tradeoffs; translate those into named dimensions and any deliberately chosen weights. One team’s design critic used design, originality, craft and functionality, weighted weaknesses more heavily and used reference sites to express its own taste. Those choices are local to that team, not objective proof of universal aesthetic quality or safety. [cite:mR-WAvEPRwE:c05]

An agent may draft the rubric or evaluator, but the responsible person should decide whether its distinctions actually express the intended standard. A recruiting example proposes judging whether sourcing overemphasizes well-known employers rather than less-visible candidates; generating such a judge does not demonstrate that it is correct or that the preference produces better recruiting outcomes. Likewise, simulated newsletter audience reactions can suggest edits but are exploratory, not observations of the real audience. Retain human editorial judgment and test downstream outcomes separately. [cite:7taOQBfjDyE:c08] [cite:2TLXsxkz0zI:c07]
