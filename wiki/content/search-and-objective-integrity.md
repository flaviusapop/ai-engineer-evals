An optimization loop can get better at its score without getting better at the job. Before letting it try many changes, state the user outcome, the evidence that would count as success, and the boundaries a solution must respect. A reward or business KPI is a proposed representation of that intent, not proof that the representation is faithful. Domain experts should own the underlying success criteria: see [[define-domain-success-and-expert-accountability]]. [cite:4VhbYlfC7Gs:c09] [cite:obfPzbapMIM:c12]

A creative-editing case illustrates the gap: a rejection-driven loop overcorrected toward a generic ceramic bowl. The pixels changed, but the speakers regarded the result as commercially meaningless. This is an illustrated failure, not an estimate of how often it happens. Check the usefulness of accepted changes, not just whether they avoid explicit rejection. [cite:31GUkCBD-Uc:c11]

## Stable comparisons, evolving objectives and nonmonotonic search

For a comparison, hold the task, scenarios, scorecard and evaluation configuration stable while candidates change. Otherwise, a score increase may reflect a changed measuring stick rather than an improved implementation. Stability for a comparison does not mean the scorecard must never change: when production learning exposes a missing objective, review the change, version the new scorecard, and rerun the baseline and candidates under it. Report which version produced each result; scores across different versions are not automatically comparable. [cite:GgLQ02aO-hs:c06] [cite:TeErpYBUIeM:c02]

List the dimensions separately before combining them: task success, latency, cost, reliability, privacy or other relevant risks. If search requires a scalar, assign explicit weights, or set non-negotiable constraints and optimize one remaining dimension. A weight allows tradeoffs; a constraint excludes candidates outside its limit. Neither approach supplies the right weights or limits automatically. A cheaper or faster candidate can fail the task: in one selected demonstration a later iteration reduced latency and turn count but failed after an earlier iteration passed. This is not a convergence test. [cite:7RFJRDYroic:c06] [cite:p7gaxmCUiIU:c03]

The optimizer's chosen weights and constraints are a **decision policy**, not the empirical cost–quality frontier. The latter describes observed candidate tradeoffs under a particular workload and measurement setup; see [[decision-economics]]. Do not infer equivalent quality from a lower price, or from two similar-looking scores without the evidence needed to assess their difference.

Prioritize experiments using expected impact and frequency together with deployment risk and the human effort required to review them. A frequently used payment flow can warrant attention that an infrequent operation does not, while a risky migration can cost more review than a small change. This is a decision consideration, not a supplied ROI formula. [cite:JJGbw4ggaFs:c09]

Keep process validity separate from task accuracy. An inspectable, constrained process can leave useful evidence even when the answer fails or experts reasonably disagree over the ground truth. Conversely, a valid process does not make the answer correct. One team reported internal task-success gains while changing several components, but did not disclose enough to attribute the improvement to its harness alone. [cite:CLttOU7n6sI:c11]

## Search and objective integrity

### Protect the measurement surface

Freeze the cases, harness and metrics for the comparison; explicitly grant the optimizer access only to intended artifacts, such as selected prompts, memory policies or retrieval rules. Preserve a known version and a way to undo edits. A prompt telling an agent not to change the evaluator is not itself evidence of a hard access control; use an appropriate enforced boundary when the risk requires one. Even a protected scorecard can encode the wrong goal. [cite:x4e5O9zN0TE:c10] [cite:Fa3hQVIKShw:c11]

For example, an integration-skill optimizer rewarded fewer turns and proposed removing documentation-fetching instructions; other missing criteria allowed it to remove trace-linking guidance. The sandbox could not evaluate an approval gate for data leaving the machine. Humans accepted only three of six suggestions after review. A missing observable cannot be protected merely by assuming that a passing score covers it. [cite:vNCY9kXXyDQ:c07]

### Run a conditional keep-or-revert loop

1. Establish a baseline and a concrete failure surface: task examples and checks that can reject a fluent but wrong answer. Specify budget, time and access limits. [cite:Fa3hQVIKShw:c12] [cite:Fa3hQVIKShw:c11]
2. Propose a bounded change and record its parent version and diff. Rerun the same cases and complete scorecard, including correctness and guardrails.
3. Keep the candidate only if the decision rule is satisfied; otherwise revert to the known version. Inspect individual regressions and uncertain results rather than accepting a marginal aggregate improvement blindly. [cite:vrDvatGtIxs:c01] [cite:x4e5O9zN0TE:c12]
4. Preserve candidate versions and results as branches: extend promising alternatives, revisit earlier ones, and record why each was retained or rejected. In a prepared prompt-optimization walkthrough, the presenter selected version five after reaching version ten because later changes regressed; the small evaluation does not establish held-out generalization. [cite:7RFJRDYroic:c04] [cite:iOXM3zE-2dk:c14]

A local metric can hide an end-to-end regression: a kernel may look faster after a surrounding acceleration is disabled while the full inference path becomes slower. Retain the real operating conditions in the acceptance question. The correctness-and-speed loop is guidance, not a complete specification of tolerances, timing or statistical acceptance; selected winners still need independent validation. For verifier design and its limits, see [[tests-oracles-and-verifier-validity]] and [[protect-holdouts-and-historical-evidence]]. [cite:vrDvatGtIxs:c06] [cite:vrDvatGtIxs:c01]

### Govern search, feedback and decisions

Automation can explore parameters, analyze recurring failure patterns and propose patches; people retain responsibility for requirements, objective-defining data and evaluator changes, and promotion. Give an improvement agent the product requirements and recurring failure themes, not only instructions to make individual tests pass. A proposed fix or automatically generated evaluator is an artifact for review, not evidence that autonomous repair worked. In one speaker's experience, human structural ideas and agent parameter tuning played different roles; that anecdote is not a comparative benchmark. [cite:qZj7sqmidqA:c16] [cite:JsCCrBF7F1g:c11] [cite:vrDvatGtIxs:c02]

Separate the inner task execution from an outer improvement loop: capture trajectories, rewards and relevant artifacts; analyze failures; propose a change; then test it under the controlled scorecard. Rollouts can feed different learning or prompt-improvement methods, but reuse of infrastructure does not turn training material into independent held-out evaluation. Rewards themselves can be gamed. [cite:7taOQBfjDyE:c03] [cite:jRCpXUjz4CI:c12]

Finally, choose action, confirmation, stop or human-review thresholds using the relevant outcome distribution and the costs of mistakes and interruptions. A stop can prevent a wrong action but also delay someone whose request was understood correctly. The voice-assistant example in the source uses illustrative request and recovery-cost assumptions, so its preferred threshold is not a portable default. In a clinical example, a missed red flag is treated as more costly than an unnecessary follow-up question; clinicians must determine the applicable tradeoff, not a flat accuracy score. [cite:Zd5b40Jbp_k:c04] [cite:McknwOzbmyg:c08]
