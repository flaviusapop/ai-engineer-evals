A plausible final answer does not reveal whether an agent retrieved the right information, failed a tool call or ignored a user’s constraint. A trace gives you evidence of execution; an evaluation asks a quality question about that evidence. Neither a trace nor a passing check, by itself, proves the whole task was done correctly. [cite:qZj7sqmidqA:c01]

## Trace tree and evidence boundary

A **span** represents a unit of work, such as a model call or tool invocation, and can record inputs, outputs, timing, token use and model metadata. Spans can nest: a child belongs to a parent operation; a root span has no parent and can represent the whole task. In one workshop, separate research and writing turns would otherwise have appeared as separate traces, so a parent wrapped both. The same demonstration suppressed instrumentation for judge calls to avoid mixing them into application traces; it did not measure production buffering performance. [cite:Xfl50508LZM:c01]

Choose the observation boundary for the question:

- **Single span:** did this tool call receive and return the expected kind of data?
- **Multiple spans:** did one agent pass the needed information to another? Both sides of the handoff matter.
- **Trajectory:** what sequence of actions and intermediate results led to the outcome, including a loop or failed write?
- **Root task or session:** was the overall task completed, or were the user’s questions resolved across the conversation?

A locally acceptable call cannot establish a successful handoff or a satisfactory session. These scopes describe the evidence needed, independently of whether code, a model or a person judges it. Instrumentation may omit events, and observed behavior is not automatically a quality verdict. For the evaluator’s concrete input contract and field mapping, see [[give-judges-the-evidence-and-context-they-need]]. [cite:JsCCrBF7F1g:c07] [cite:JsCCrBF7F1g:c08]

## From observations to provisional failure categories

Read available traces end to end before imposing a taxonomy. Record what happened in ordinary language: the request, relevant intermediate outputs, actions and final answer. Then group recurring observations into provisional categories. For example, “wrong answer” is a symptom; possibilities include a parser dropping a constraint, retrieval returning irrelevant material, reasoning misusing good material, a plan stopping early, or self-review declaring incomplete work finished. Inspect the intermediates that could distinguish these explanations. [cite:SHMCGrNJJGc:c01] [cite:nxokqOq1imY:c03]

**Illustrative example:** a weather assistant answers for the wrong city. If the trace shows the user’s city was parsed incorrectly, the likely investigation differs from a case where the right city reached the weather tool but the final response ignored its result. Record the evidence and uncertainty rather than announcing a root cause from the final answer alone. Stage-level checks for intent, tool selection and completion can help localize a failure without implying that every valid run must use the same path. [cite:iOXM3zE-2dk:c02]

Across traces, group similar observations and retain examples that challenge the grouping. Expert comments or model-assisted clustering can suggest recurring patterns, but the taxonomy remains provisional: selected examples do not establish prevalence or causation. Continue human sampling after automation to find missed categories. One workshop’s displayed category frequencies used random codes, so they are not evidence of actual failure rates. [cite:qZj7sqmidqA:c02] [cite:obfPzbapMIM:c08]

## Match rigor to maturity and consequence

Early in development, direct inspection can produce directional feedback while the architecture and capabilities are changing rapidly. Focus expert attention on consequential failures rather than trying to enumerate everything immediately. A team reported that this unscalable exploratory phase helped it understand what to evaluate; that is experience, not a controlled comparison. [cite:xyL2Ltkh-SA:c02] [cite:FB-MLPhL9Ms:c01]

As use and consequences grow, maintain explicit tests and measurable standards for consequential decisions. Maturity is a continuum, not a requirement to wait for a particular stage before checking serious risks. Informal impressions alone are not launch evidence, and a model judge used for such decisions needs its own [[validate-judges-against-human-labels|independent validation against human judgments]]. Release thresholds and promotion decisions belong to [[production-governance-and-release]]. [cite:xyL2Ltkh-SA:c10] [cite:FB-MLPhL9Ms:c05]

## Distill incidents and expert rationales into candidate checks

An expert’s explanation of *why* an answer failed can yield a more reusable question than a thumbs-down alone. Review rationales and recurring incidents for a candidate property, then ask a domain owner whether it actually reflects the task. Hindsight analysis or a model can help propose cheaper repeated checks, but a plausible generated criterion is not yet a validated evaluator. [cite:XBaznoTRDFI:c07] [cite:AQv3qRCG6Gw:c08]

A shopping workshop deliberately seeded an over-budget result. Its proposed candidate rule was that every returned product must fall within the requested price range. That is more actionable than “shopping quality is poor,” but the workshop’s verification path was not fully executed; it is not production proof. [cite:fnuNVFgLjHA:c09] A persistent agent reading many traces for patterns is another proposed discovery mechanism, not a demonstrated exhaustive detector. [cite:q2JrUKBMf0w:c06]

Discovery, criterion validation and regression promotion are separate handoffs. Use [[turn-task-quality-into-actionable-evaluation-rubrics|rubric design]] to make a candidate operational, [[validate-judges-against-human-labels|judge validation]] to assess alignment, and [[build-and-maintain-production-grounded-evaluation-sets|dataset maintenance]] to select and maintain regression cases. These quality signals complement rather than replace availability and latency monitoring.

## Use complementary evaluator layers

A useful layered evaluation keeps failures interpretable. Code can check reproducible format or inspectable state; a semantic judge can assess a meaning-dependent property; humans can examine unfamiliar failures and provide domain judgments. A model judge adds cost and can be wrong; an explanation helps inspect a verdict but does not prove it. A decision model may emit a label or probability without a comparable explanation; claimed speed and cost advantages in the workshop were not benchmarked. [cite:Xfl50508LZM:c02] [cite:gv4w23xYj-0:c02]

Keep different properties, such as faithfulness and actionability, distinct instead of relying on one opaque overall score. A ticker appearing in a financial report, for example, is a narrow reproducible proxy—not proof that the analysis is accurate. No stack of finite checks guarantees complete coverage. For deeper architectural choices, see [[choose-and-combine-judge-methods]]. [cite:SHMCGrNJJGc:c02] [cite:qZj7sqmidqA:c04]

## Make qualitative judgment teachable

Where no complete objective metric exists, an expert can explain a preference with a concrete critique and contrasting examples rather than simply saying an answer has good or bad taste. **Illustrative example:** a reviewer might prefer one explanation because it states the decision before the background, and show another that buries the decision. Colleagues can then discuss the tradeoff and learn what the reviewer values. This is conceptual guidance, not a measured improvement or a universal taste metric; other audiences may legitimately prefer a different ordering. [cite:n97BCfyFIvw:c05]

## Feedback is not acceptance

A repair loop can get a better feedback score while exploiting a weak proxy. **Illustrative example:** if the only check for a useful report is that it contains a ticker, adding the ticker makes the check pass without improving the analysis. Define the actual acceptance criterion and assess whether the verifier distinguishes genuine success from such shortcuts. More attempts cannot repair a defective acceptance test. [cite:_4Ph2dhmUFI:c06] [cite:7taOQBfjDyE:c02]

One architectural proposal allows adaptive revision inside a work step while an external deterministic gate controls progression. That can preserve a required boundary without prescribing every revision, but its usefulness still depends on the gate’s inputs, implementation and coverage. A deterministic pass is not comprehensive correctness, and the proposal is not a controlled production result. [cite:_4Ph2dhmUFI:c02]
