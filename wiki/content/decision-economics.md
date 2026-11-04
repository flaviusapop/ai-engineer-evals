A cheap model call is not necessarily a cheap completed job. It may produce an answer that needs more retrieval, retries or human correction, and a faster response may still take longer to turn into usable work. Compare systems at the boundary where a defined task is accepted, while keeping quality, money and time visible as separate outcomes. [cite:48YUYDjwfYY:c01] [cite:YvQ4BVTWfHI:c01]

## Observe the workflow to usable work

Trace a task from request through retrieval, model and tool calls, retries, review and correction. Record which configured system ran, token use, expenditure, elapsed time and the human effort needed to reach a usable result. Keep request latency, total elapsed time and reviewer time distinct: each answers a different question. Context can grow and a model can change even when request volume is stable, so record those changes with the traces. [cite:ZdheJTfLu-s:c07] [cite:rTojoVotlD8:c02] [cite:rTojoVotlD8:c03]

For example, a speaker reported that a code-mode change used 43% fewer tokens and cost 31% less, while latency stayed roughly constant because of sandbox overhead. The comparison lacks the full task set, trial counts and raw data; it illustrates why the axes can move differently, not a general expected saving. Another retrospective coding account estimated a roughly fivefold speedup only after including planning, coordination and review; it was not a controlled productivity study. [cite:dAoOYFx7ZYw:c13] [cite:5Bn0xro2ol8:c07]

## Attribute avoided input to an explicit alternative

A counterfactual saving compares what was actually sent with what a specified alternative policy would have sent. Name that alternative, the workload and the assumed prices, including whether caching applies. If you assign the difference to retrieval or compression, explain the accounting order and assumptions. Priced avoided input is an estimate against that policy, not an observed reduction on an invoice or proof of a better end-to-end workflow.

In one speaker-run test, 20 questions on a 53-file FastAPI project were compared with repeatedly sending all files: approximately 83,000 input tokens versus 4,900 retrieved and 523 compressed. That baseline makes the comparison interpretable but is weaker than a capable modern coding agent; code-finding accuracy is not correctness of a generated patch. A separate 247-query savings attribution lacks enough billing, cache and pricing detail to establish realized savings. [cite:dRmWYHuIJxM:c06] [cite:dRmWYHuIJxM:c09]

## Control attribution when comparing interventions

Choose the question before running the comparison. Holding total resources fixed asks which strategy uses a given budget better; sweeping budgets asks how quality changes as spending changes. Use comparable tasks and acceptance rules, repeat runs, and record model, harness, reasoning effort, generation settings, precision and runtime environment. Report meaningful changes rather than attributing every observed difference to the intervention. For detailed experimental design, see [[comparing-agents-without-confounding-the-result]].

In a reported financial-task comparison, an initial strategy used roughly 39,000 tokens while another used roughly 600,000. When strategies received the larger budget, reported scores were 76 and 89 for two approaches. The example motivates budget control, but the available account does not supply sufficient uncertainty or replication to establish a general ranking. In a separate serving comparison, a temperature-zero default rather than the intended roughly 0.7 workload explained an apparent throughput advantage; matching configuration matters even when the metric is speed rather than quality. [cite:PXj0p_mW9nI:c05] [cite:l1-D89bAuOA:c06]

## Full lifecycle cost per accepted task versus first-attempt reliability

For a defined workload, period and acceptance rule, calculate:

**Cost per accepted task = total lifecycle expenditure in the period / verified acceptable tasks completed in that period.**

The numerator includes failed runs, retries, escalation and human supervision or repair, plus allocated infrastructure, integration, maintenance and optimization labor. The denominator is not requests, generated answers or tokens: it is accepted work. Apply comparable task mix and quality standards across alternatives. If no tasks are accepted, report the cost and zero accepted outcomes rather than a finite ratio. GPU rent and token tariffs are inputs, not the full price of delivered work; additional serving output can spread fixed costs but the people and software required to achieve it also cost money. [cite:3axY1wz2OvA:c06] [cite:3axY1wz2OvA:c07] [cite:5xi_S1f9sDU:c06]

**Illustrative accounting example:** over the same period, system A costs $1,200 across all work and produces 80 accepted tasks; system B costs $1,000 and produces 50. Their computed costs per accepted task are $15 and $20, respectively. This does not show either system has positive business value, and it is comparable only if the workloads and acceptance standards match. It also does not establish how much of the cost was caused by the AI change.

Report first-attempt success separately: accepted first attempts divided by eligible first attempts. It matters when a user cannot wait for retries or a mistake has consequences; the cheapest eventual accepted result need not be the most reliable first result. Retry expense depends on the actual retry policy, dependence between attempts and whether success can be recognized—not an assumed fixed number of attempts. For autonomous benefits, also track which work is eligible, whether people adopt the system, straight-through completion and accepted quality; do not multiply rates as independent or infer financial value without a defensible model. [cite:PXj0p_mW9nI:c07] [cite:PXj0p_mW9nI:c08] [cite:gDRCpTMCqEU:c07]

## Task-specific cost–quality frontiers and quality gates

Treat each model, harness and reasoning configuration as a separate candidate. Measure task-appropriate quality, actual task cost and latency, along with relevant constraints such as licensing. A candidate is dominated if another is at least as good on the dimensions being compared and strictly better on one. Among candidates that satisfy the application's requirements, a nondominated choice may be preferable to either the largest model or the lowest token tariff. Local inference avoids provider fees but still consumes hardware and energy. [cite:fWXJM-J0ZB8:c01] [cite:fWXJM-J0ZB8:c04] [cite:rWtbOgl5FTU:c02]

Repeat the comparison for important slices: a reported spreadsheet benchmark found that the leveraged-buyout subset changed which model was on the frontier, although the underlying plotted data and uncertainty were not supplied. Preference scores and accuracy also measure different things; do not substitute one for the other without justification. For systems that learn across tasks, report absolute reward, gain relative to a reset baseline, and cost separately: a strong starting model can score well without learning much. [cite:rWtbOgl5FTU:c03] [cite:uIiA6DquRiE:c04] [cite:iqloyWCGYQQ:c06]

Before replacing an incumbent, inspect critical categories and uncertainty rather than treating a point estimate or lower bill as equivalence. One proposed release workflow uses repeated comparison, disagreement review and a positive lower confidence bound for net gain, with critical categories holding up; that is guidance, not proof of production savings. Check the replacement after deployment as well. The details of choosing and allocating capabilities belong in [[routing-and-deployment]]; hard optimizer constraints belong in [[search-and-objective-integrity]]. [cite:8g1N_a3h9H0:c14] [cite:ZdheJTfLu-s:c02]

## Interpret workload spending and adoption

Attribute shared spend by team and use case so an unusual bill can be investigated against task mix and results. Long-context, multi-turn agents can have a very different consumption profile from isolated short automation. Review anomalies and use budgets or quotas appropriate to the stage of adoption, but do not turn either high or low token consumption into a productivity leaderboard. A higher bill may purchase trusted work; very low usage may expose an adoption problem. Early exploration still needs safeguards. [cite:Ti-BmGU1_mQ:c01] [cite:Ti-BmGU1_mQ:c02] [cite:dSg0pu8d6qg:c02] [cite:dSg0pu8d6qg:c04]

An adequate cheaper option may be more attractive if it is fast enough for the workflow, but the reported adoption pattern is observational. Compare people or teams cautiously: differences in tasks and experience confound raw usage, and the sources do not provide a validated normalization formula. [cite:Ti-BmGU1_mQ:c05] [cite:Se8jHLliLXE:c05]

## Intermediate value proxies and trusted throughput

Some outcomes, such as financial performance, arrive too late or are too entangled with other factors to guide every iteration. Define an intermediate proxy that can be checked now: for example, what counts as a useful insight, useful insights per analyst-day, and the cost per useful insight. Specify the observation window and assess whether reviewers agree. These measures can guide learning, but a faster research process or more counted insights does not establish realized ROI. [cite:ZMZlAn6Pyfg:c07]

Similarly, a merged change is not automatically valuable. Complexity-weighted merged work may capture effort that line counts miss, but the proposed scoring is not validated as a measure of customer value. Keep objective checks, human maintainability review and production outcomes as distinct evidence of trusted throughput, rather than silently treating them as a validated composite score. Use [[measuring-business-value]] for whole-workflow baselines and eventual outcome attribution, and [[evaluation-infrastructure]] for the separate cost of evaluation itself. [cite:dSg0pu8d6qg:c05] [cite:dSg0pu8d6qg:c06]
