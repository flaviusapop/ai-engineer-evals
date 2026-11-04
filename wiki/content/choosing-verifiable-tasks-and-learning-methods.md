A task is not a good agent candidate merely because a model can produce an answer. The work needs boundaries, a way to tell whether the result is acceptable and an economic reason to use the system. The same properties affect learning: an available outcome check can make a task attractive for reinforcement learning, but does not by itself make the agent’s path safe.

## Separate uncertainty about steps from uncertainty about acceptance

Ask two different questions. How variable is the route to completion? And how clear are the criteria for accepting the result? Booking a flight requires recognizable information and actions, although choices can vary; creating a masterpiece has a less predictable route and a less settled standard of success. The contrast is a thought-starter for task selection, not a validated numerical measure of uncertainty. [cite:8KkibGU_DDY:c07]

When the steps are predictable, a conventional script may be preferable to an agent: flexibility has a cost and should address real variability. At the other extreme, when acceptance criteria are so unclear that a reviewer must effectively redo the work, the checking burden can consume the apparent benefit. This does not mean subjective work cannot be assisted; it means that value and review effort need to be assessed, not inferred from output volume. [cite:8KkibGU_DDY:c08] [cite:8KkibGU_DDY:c09]

A promising candidate has enough execution variability to benefit from flexible behavior but a repeatable, comparatively inexpensive way to check results. Treat this as a hypothesis to evaluate, not a guaranteed return on investment. An agent might help with checking too, but that does not automatically make its judgment reliable. Specify the system’s interfaces and limits, the observable result, and the costs of execution and review before choosing the workflow. [cite:8KkibGU_DDY:c10] [cite:1tpqdglI3T0:c12]

## Inspect what makes a result verifiable

One heuristic separates three properties: whether work can be decomposed into checkable pieces, whether people agree on correctness, and whether verified examples occur often enough to learn from. These dimensions need not move together. A task may have many examples but disputed acceptance criteria, or clear criteria but too few verified examples for the intended learning process. The framework is a way to organize investigation, not a validated prediction of which market or domain will mature first. [cite:ZyIoTOAbRfs:c03]

Code illustrates the affordance: parts can often be decomposed and executed, making some outcomes easier to observe than an overall judgment of design or writing. Look for observable components of a subjective task without pretending they capture the entire quality target. The claim that measurability explains differences in model capability is a conceptual argument, not an isolated causal finding. [cite:lCBf9slCanI:c01]

## Match learning to available evidence and risk

Reinforcement learning is worth considering when tasks are available or can be generated, expert demonstrations are expensive, several action paths can reach acceptable results, and outcomes can be checked. A reward tied to the outcome can in principle recognize different successful routes rather than requiring every trajectory to imitate a small set of demonstrations. That is a task-fit argument, not evidence that reinforcement learning generally outperforms supervised fine-tuning; the cited account gives no comparative experiment. [cite:Cc0_nyxROBA:c01]

A final-state reward can miss harmful intermediate actions. A browser agent might eventually complete its intended task after taking a dangerous or unauthorized action along the way; checking the final result alone would not expose that failure. The speaker therefore advocates tracking and penalizing risky actions throughout the trajectory, not just failed outcomes. The account does not specify a reward formula or quantify how well this approach prevents harm. **Illustrative example:** reaching the correct record after changing an unrelated account setting is not an acceptable route merely because the record is correct. [cite:Cc0_nyxROBA:c07]

Before adopting a learning method, examine whether the available checks represent the desired outcome and whether unsafe routes are observable. Verifiability is a useful affordance, not a substitute for validating the evaluator or deciding what evidence an evaluation can establish. See [[what-an-ai-evaluation-can-and-cannot-establish]] and [[tests-oracles-and-verifier-validity]].
