An evaluation set is not representative merely because it contains many examples. First state the decision: estimating ordinary user experience, finding severe failures, choosing a model for a particular task, and checking a proposed change each require a different population or case mix. The score is meaningful only for the distribution and conditions it actually covers.

## Ground scenarios in the work users need

Work with users and domain experts to describe expected behavior, then collect realistic workflows, ambiguous requests, ordinary successes and consequential failures. Do not restrict the test to what current connectors happen to support: one sales team wrote questions from the sales process before testing its assistant, including questions for which data was missing. Its reported accuracy lacked a disclosed rubric, but the design made unsupported demand visible. [cite:DrTdD-ttjCY:c01] [cite:ObTPqBGsEbA:c02]

For a financial research assistant, task variation might include unfamiliar companies, comparative and multipart requests, invalid identifiers and informal wording. A workshop's generated examples illustrate breadth, not live-user representativeness or release readiness. Likewise, experts authoring plausible repository tasks improve relevance without proving that the resulting collection mirrors all engineering work. Include common workflows and dependency failures, and disclose important absences. See [[from-business-problem-to-meaningful-success-criteria]] for defining success and [[specify-and-audit-meaningful-benchmark-tasks]] for task-level validity. [cite:Xfl50508LZM:c04] [cite:Yk87oUPVaxU:c04] [cite:Ib5t2RLtxvM:c14]

## Choose the distribution for the estimand

Build a taxonomy of user intents, task families, populations, environments and risk conditions. Then allocate cases deliberately:

- **Production-frequency evaluation** targets performance for the traffic population represented by the sample. Estimate or document how cases were selected, the relevant period and any missing groups.
- **Risk-enriched evaluation** deliberately oversamples rare but consequential events, such as tool failure or sensitive escalation. Its unweighted failure fraction describes that enriched test mix, not the prevalence of failures in ordinary traffic.
- **Slice results** describe performance within a defined group or condition. Report its denominator and uncertainty rather than assuming the overall average protects it.

If population rates are needed from an enriched sample, use justified population weights and sampling assumptions; absent those, keep the results separate. More cases cannot repair an unidentified population or an omitted risk category. [cite:iNkFlCiij0U:c02]

An informal product-discovery pilot illustrates why prompt intent matters: the product was reportedly mentioned around 65% of the time in explicitly comparative prompts but not in a pain-focused scenario. Sample sizes and prompt distribution were not fully specified, so these are not deployment rates. A long-horizon coding benchmark likewise acknowledged underrepresenting bug localization and refactoring, while one worktree evaluation had not simulated the very long sessions of concern. State such gaps rather than generalizing beyond the observed setting. [cite:Lrw0jqBNaw0:c04] [cite:Yk87oUPVaxU:c09] [cite:WE_Gnowy3uw:c05]

Cross relevant dimensions where interactions matter: a document system may need multiple languages, historical periods, layouts and genres; a visual task can behave differently when the question language changes. One proposed Indic benchmark described such breadth, but its release, per-language counts and scoring were not established. A few multilingual visual examples are similarly not a systematic coverage study. [cite:T72nqdC92PM:c09] [cite:UGjk3Uk0MxM:c03]

## Select models on the local slice

Public benchmarks are useful screening evidence and may be directly relevant when their tasks and conditions match deployment. They are not automatic certification for a different workflow. Compare actual candidate variants on the organization's task families, prompts, harness, latency and cost constraints. An image-editing aggregate can conceal different performance on object removal versus text editing; the cited vendor presentation did not provide full plotted data to verify every ranking. A modified checkpoint also needs evidence for that variant, not just the base model. [cite:A3FL_zTQKU0:c03] [cite:hqHC6Z_lXyo:c02] [cite:J4_jCrTxMkk:c12]

Record achieved task quality and realized cost per task, not only token tariffs: a cheaper token price can still yield more expensive work when an agent uses more tokens. Prompt and harness interactions can change the observed result; a small counting demonstration improved after a decomposition instruction, but cannot establish a stable model ranking. For controlled comparisons, see [[comparing-agents-without-confounding-the-result]]. [cite:rWtbOgl5FTU:c02] [cite:UGjk3Uk0MxM:c01]

## Replay cohorts, not anecdotes

For a proposed model or tool change, select a meaningful cohort of existing executions, replay the change and compare outcomes across cases. An expensive-case cohort answers what happens to expensive cases, not what happens to all traffic. Segment by cost, latency or risk where useful, and repeat stochastic attempts to expose within-case variability. One replay can be a valuable example but is not a reliability estimate; replay at scale costs resources, and the cited demonstration does not specify sampling, grading or fidelity. [cite:bZISsg7H7DA:c04] [cite:bZISsg7H7DA:c06]

## Quantify uncertainty for a release decision

A defect estimate below a release threshold is not enough when its uncertainty still crosses that threshold. A workshop describes an observed 3% defect rate against a 5% limit and contrasts different sample sizes; its intervals and sample-size suggestions are approximate, with no interval method or sampling design supplied. They are not universal release rules. Choose sample size and uncertainty analysis for the target population, sampling design, dependence between cases, risk tolerance and decision cost; seek more evidence or narrow deployment when the interval does not support the decision. This population-rate question is different from asking whether a deliberately enriched edge-case suite found a serious failure. [cite:Xfl50508LZM:c15]

## Account for combinations and provenance

Count authored base scenarios separately from configurations formed by varying profile, theme or starting state. A speaker described DigiWorld as 15 apps, 387 verified scenarios and 3.2 million configurations; these are speaker-reported counts without per-axis distribution details. Millions of combinations should not be presented as millions of independent authored tasks. [cite:CTLa_p6iOiY:c05]

Record where each dataset came from, what was excluded, and how labels were obtained. One tutoring study cleaned real staff-answered questions into 60 single-turn pairs, while using generated facts and filler for a different multi-turn memory probe. The former tests current question answering; the latter probes retention of planted facts. Similarly, PR descriptions and branch prefixes can suggest agent authorship, but they are proxy labels, not direct observation of autonomous work; their accuracy was not audited. Real-work capture can preserve context but may be biased or unsafe, while manufactured cases can deliberately cover missing conditions. Neither origin guarantees truth or representativeness. [cite:WP3hjUXd918:c09] [cite:474j-n1Ltxc:c01] [cite:ZyIoTOAbRfs:c02]
