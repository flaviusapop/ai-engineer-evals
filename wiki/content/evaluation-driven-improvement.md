An evaluation becomes useful for improvement when it does more than announce a score: it identifies a failure, helps locate a repair, and tests whether that repair preserves what already worked. Even then, a passing set establishes behavior only on the cases and conditions examined. The aim is a disciplined cycle of focused learning and broader verification, not a claim that repeated testing makes an agent generally correct.

## Turn a new capability into a protected behavior

Start with a behavior the system cannot yet perform reliably. Keep examples that expose that failure together with examples it already handles correctly. Work on the new capability, then retain its checks as regression tests when the behavior is sufficiently reliable for the intended use. The point of the transition is to keep a subsequent improvement from silently undoing an earlier one; a workshop's suggestion of a 100% transition is a teaching model, not a validated production threshold. [cite:Xfl50508LZM:c03]

Use the failure subset for inexpensive iterations, but periodically run the broader corpus and do so before a release decision. A financial-agent workshop reported that six selected failures passed after a prompt revision; it did not show repeated trials or freeze live search results, and this selected-case result did not establish broad improvement. A candidate can fit those six cases while damaging others. [cite:Xfl50508LZM:c13]

## Diagnose before choosing the repair

A final wrong answer is a symptom, not a diagnosis. Read the input, retrieved evidence, intermediate decisions, tool requests and outputs around representative failures. Compare cases that changed between candidates, not just their aggregate scores. Traces provide a denser explanation of a failure than pass/fail alone, while the outcome still matters: a convincing trajectory is not a substitute for completing the task. [cite:CvRngaQZQ3Y:c11] [cite:A48uhxfxbsM:c04]

For example, an agent citing a stale policy and skipping escalation might have outdated memory, a weak instruction, malformed tool data, a missing workflow gate or a reasoning problem. That scenario is illustrative, not a validated root-cause classifier. Investigate the evidence and repair the responsible layer: update the source when it is stale; fix the harness for context overload; enforce a schema at the interface when structure is the defect. A prompt prohibition is not automatically the right remedy. [cite:2IxD9OB3XuQ:c09] [cite:Ib5t2RLtxvM:c11]

Causes can combine. In a selected international-stock demonstration, adding country information did not resolve failures until the outdated tool was also updated. The reported final success rate is bounded by an unspecified dataset size and judge calibration; the failed intermediate attempt is the more useful lesson than the headline gain. Prioritize recurring defects by consequence as well as frequency, while keeping enough contextual evidence to investigate them responsibly. For instrumentation details, see [[agent-observability-and-diagnosis]]. [cite:_zUp6y9bDU8:c05] [cite:Xfl50508LZM:c05]

## Compare candidates under controlled conditions

Save the baseline configuration and compare it with the candidate on the same inputs, evaluator and, where possible, environment and retrieved data. Change a bounded component when the question is causal: if the model, prompt and tools all change at once, a whole-system comparison can show which configuration performed better on the test, but not which change produced the difference. Repeating stochastic cases helps estimate typical behavior, at a compute cost; one favorable run is weak evidence of a small improvement. Fixed inputs and a fixed judge do not eliminate sampling or live-retrieval variation. [cite:Ib5t2RLtxvM:c03] [cite:YvQ4BVTWfHI:c05] [cite:A48uhxfxbsM:c07]

Version history and an attractive new prompt establish what changed, not that it improved outcomes. Check the actual outputs and disagreements as well as the metric, and use a broader or held-out set that has not guided every iteration when making a generalization claim. Even an optimized aggregate can leave the original failure intact: in one workshop a selected political-relation extraction still misclassified a sports commentator after optimization. That was a demonstration, not an independently validated production result. [cite:2TLXsxkz0zI:c13] [cite:A48uhxfxbsM:c13]

## Protect more than the headline score

Define the dimensions that must not be traded away: task completion, factual grounding, critical slices, tool behavior, cost or latency, and any relevant safety requirements. An overall average can conceal a regression in a capability that a particular user needs. Likewise, adaptation for a specialist task should be checked against relevant general capabilities, rather than assuming they survive. [cite:YvQ4BVTWfHI:c04] [cite:2LRIAfng7eA:c06]

One small financial-report workshop illustrates why separate checks matter. Adding explicit recommendation instructions improved measured actionability across repeated outputs, yet faithfulness remained poor. An actionable form is not a sound recommendation, and the demonstration's small, nondeterministic experiments are not evidence of financial usefulness. Keep the unresolved grounding failure visible rather than averaging it away. [cite:SHMCGrNJJGc:c12]

## Make iteration fast without weakening the release decision

Fast, inexpensive, low-noise checks allow more useful experiments. Run a compact, representative regression subset and the current failure set during development; use reusable cases and structured feedback to reduce setup and diagnosis time. Compression saves effort but may omit an important failure, so periodically restore broader checks and investigate whether the fast suite still represents the behaviors it is meant to protect. An agent may exploit gaps in an evaluator; inspect the outputs behind a rising number. [cite:7RFJRDYroic:c02] [cite:Xfl50508LZM:c03]

A release gate should combine evidence that the targeted defect improved with checks for previously passing behavior and critical dimensions. Thresholds must be chosen for the application and its risk; a workshop's replay threshold is a local decision, not a universal safety guarantee. After release, continue evaluating real interactions and add coverage for newly discovered failure classes: a detector can help find recurrence, but does not itself prevent it. [cite:UGuNt2_Oz8s:c08] [cite:YXEqC05WEI0:c07]

For how candidates are constructed rather than compared, see [[prompt-and-harness-optimization]]; for the integrity of the objective being optimized, see [[search-and-objective-integrity]].
