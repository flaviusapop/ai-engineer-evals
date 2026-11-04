A production trace is evidence about what happened, not an automatic specification of what should happen next. A useful improvement loop moves from observed behavior to a reviewed hypothesis, a repeatable test, a candidate change and comparative evidence. It preserves uncertainty at each step: a cluster may be misleading, a regression suite is finite, and passing it is not the same as authorization to release.

## Construct repeatable behavioral evidence

Ask domain experts to create diagnostic cases, expected outcomes, a rubric and held-out references. Run candidates against the same instrument after a prompt, model or skill change, retaining individual outcomes as well as aggregates. Automated scoring can provide an initial pass; experts remain needed for disputed cases and interpretation. One team described a roughly 200-task nightly suite, but its reported aggregate comparison lacks uncertainty and per-task regression details. The expert-instrument proposal likewise does not establish judge calibration or deployment outcomes. [cite:IJXjTLPzvAU:c12] [cite:hd7TOvmyAxU:c07]

Make results available to the decision process rather than treating a favorable average as approval. The thresholds, exceptions and promotion authority belong to [[production-governance-and-release]]; continued observation after deployment is a different activity. No finite offline suite proves safety outside its coverage. [cite:3z2uT5aDx_Y:c01]

## Train recovery from observed disruptions

A training environment that silently resets after a tool or infrastructure error may never exercise the recovery behavior a user needs. Preserve the disruption in the task and evaluate whether the agent refreshes, backtracks, compares state, waits, abandons or escalates as appropriate. Gather failures under protective operation, then reconstruct representative tasks and decide what successful recovery and its reward should mean. For instance, an **illustrative** expired-session case could require the agent to stop and request reauthentication rather than repeatedly submitting the same action. [cite:Cc0_nyxROBA:c06] [cite:Cc0_nyxROBA:c11]

Turning user feedback into faithful environments and reward signals is still an open engineering and research problem; the cited approach does not isolate a reliability gain. A proposed thinner future harness is not evidence that safeguards can be removed. Live recovery limits and independent enforcement are covered by [[agent-sessions-and-long-running-work]] and [[agent-authority-isolation-and-runtime-controls]]. [cite:V-EDrhIhHzQ:c04]

## Discover patterns, then review what they mean

Known scores detect known failure categories; examining many interactions together can expose recurring frustrations or goals that the existing rubric never anticipated. A useful discovery pipeline selects trace material, applies a facet such as task or issue, summarizes it, embeds the summaries and groups similar representations. Each choice affects what can appear: if relevant tool metadata is omitted during preprocessing, an issue may disappear before clustering begins. Review representative underlying interactions before turning a cluster into a requirement or a new regression case. Clusters are leads, not proof of novelty or error. [cite:qStB9GbppMU:c05] [cite:hfEczxdNyvU:c06] [cite:hfEczxdNyvU:c07]

In a synthetic support workshop, a generic issues facet yielded no topic, while a custom support-workflow facet surfaced record-lookup failures. The product required at least 100 matching facet outputs at the time: too few matches and an ill-fitting representation were different possible explanations for an empty result. That cutoff was product-specific, not a general statistical rule; the workshop did not measure discovery recall. [cite:hfEczxdNyvU:c10]

Once reviewed, a failure can become a case with an explicit expected outcome and a suitable evaluation method. The complementary work of selecting and maintaining production-derived examples is detailed in [[build-and-maintain-production-grounded-evaluation-sets]].

### Maintain skills through reviewed changes

Separate the agent doing a task from a maintenance process that examines its outcomes and human corrections. In an issue-triage case, the maintenance agent gathered reactions and comments and proposed a versioned skill change for human review. A shared procedure should have a named owner and a reviewer other than its author, because rules and workflows change and one mistake can repeat across future work. Human review is a safeguard, not a measured guarantee; reactions can be noisy or contradictory. A proposal to consolidate experiences into skills also illustrates why stale SQL-column guidance needs revision, but its suggested consolidation counts were inconsistent and should not be treated as a threshold. [cite:TN3mj92oZ8I:c02] [cite:TN3mj92oZ8I:c03] [cite:TN3mj92oZ8I:c04] [cite:gpmze-6ueGU:c07] [cite:Jx4ZFEAq6bY:c06]

### Share experiments without losing history

Domain experts need appropriate access to inspect traces and try controlled changes, not an engineering export for every question. A demonstrated remote evaluation exposed selected prompt, tool-description and model parameters while execution stayed on the server and results returned to a playground. Keep source assets, versions, authorship and synchronization under change control even when a managed interface makes experiments accessible. The demonstration does not specify a complete authentication or promotion policy. [cite:hfEczxdNyvU:c14] [cite:ZdheJTfLu-s:c04] [cite:ZdheJTfLu-s:c10]

### Revisit the objective, not just the implementation

A candidate can improve a fixed score while missing what users value. Compare qualitative feedback, behavior and product outcomes with the rubric and ask whether the proxy needs a new dimension. Keep the existing evaluation stable for an apples-to-apples comparison of candidates, then version a revised objective separately so the reason for a changed score is visible. Automatically turning feedback into a faithful objective is proposed research, not a validated procedure. [cite:GgLQ02aO-hs:c10]

## Broaden and place tests deliberately

Keep behavioral specifications and unit, integration and penetration tests versioned independently of a particular agent framework. On migration, run the same obligations against the new implementation instead of redefining success to match it. This is a design recommendation; the source does not demonstrate a finished portable specification format. [cite:UQKg0td-Bf4:c10]

Generate domain-grounded synthetic edge cases before customer records are available, for example a difficult but plausible support-policy boundary reviewed by an expert. They accelerate iteration when real examples are sensitive or scarce, but cover only modeled scenarios; passing generated cases alone cannot establish real-world coverage or authorize shipping. [cite:XAsb7MIAzm8:c13] [cite:c_SPW__jF9w:c12]

Security testing adds a different evidence stream. A proposed process brings context-sensitive offensive checks closer to code changes, validates candidate exploits and gives developers actionable remediation guidance. More frequent scans or findings do not demonstrate coverage, and the source shows neither a completed automatic patch nor successful retest. Retest the fix rather than equating a report with remediation. [cite:f3o0-9Dlw3E:c03] [cite:f3o0-9Dlw3E:c07]

Execution and scoring can live in different places: a candidate might run locally and send outputs to a separate evaluation service. Record candidate execution failure separately from evaluator failure. In a demonstration a code evaluator failed and an LLM judge was used instead; that fallback was not shown to have equivalent validity. [cite:_zUp6y9bDU8:c11]

## Evaluate the whole task, not just the final sentence

Use different checks for different questions. Deterministic checks can validate syntax, counts and required fields; semantic evaluation addresses meaning and grounding; behavioral checks inspect tool selection, loops and repeated actions. Post-processing can enforce a length or reference-count rule, but neither a valid structure nor a good-looking answer establishes factual correctness. One small thread-summary experiment reported structural success after post-processing; its size and partly model-derived labels limit generalization. [cite:ObTPqBGsEbA:c03] [cite:fWXJM-J0ZB8:c08]

Also check completion against every requested deliverable. A polished response may stop halfway. If a research assignment requires both a user-facing scorecard and a durable memory update, inspect both artifacts and their substantive content rather than crediting a fluent opening. The cited financial demonstration did not independently verify the scorecard values or supply a complete rubric. [cite:XzJD1bvXKjs:c09] [cite:FGftGOzfohc:c06]

## Compare changes under realistic conditions

Running the same agent code in simulation and production reduces implementation drift; one team reported synchronizing the two environments. It does not make simulated users, data, external tools or failures realistic. Document those differences when interpreting offline results, and use customer-perspective checks as a complement: a browser-using agent can exercise the visible interface and reveal issues absent from code or logs, though computer use adds latency and token cost and the cited account does not establish broad coverage. [cite:XyV6bSMyq-I:c01] [cite:kZsf_Sfm7RU:c08]

A telemetry trace usually records emitted events, while an execution checkpoint aims to retain enough state—such as variables, files, code and environment—to resume. Tracing systems differ, so verify what your own record captures. A checkpoint can support a controlled branch: restore the same point, change one factor such as a model or policy lookup, then compare decisions and artifacts as well as cost. Confirm replay fidelity and avoid treating the branch as proof of what production would have done. [cite:bZISsg7H7DA:c01] [cite:bZISsg7H7DA:c02] [cite:bZISsg7H7DA:c03]

In a vendor demonstration, a cheaper-model replay looked equivalent on one case, but a subsequent cohort verdict was not to ship. The cohort size, grading and raw results were not given; the lesson is to challenge the attractive example with broader evidence, not to infer a population effect from the demo. [cite:bZISsg7H7DA:c08]

Finally, test whether injected knowledge helps rather than assuming more context is better. One team described withholding an otherwise relevant entry from a small comparison group and comparing downstream project success with the injected group. Use such evidence to reconsider or retire stale entries after model or product changes, but the account lacks effect sizes and a full assignment and analysis design, so it does not establish a causal effect. [cite:KA5kPbdkK2E:c04] [cite:KA5kPbdkK2E:c05]
