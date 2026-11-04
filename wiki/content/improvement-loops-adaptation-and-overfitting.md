An agent can improve its score without improving the work people actually need. Treat the development loop itself as an optimization process: specify the desired behavior, seek evidence against it, and keep the feedback used to make changes distinct from evidence used to assess them.

## Discover the target separately from optimizing it

An outer loop learns what users need from feedback and online evidence, then revises tasks and measures. An inner loop changes the model or system to perform better against those targets. If a task is easy to score but misses the user's real problem, more inner-loop optimization may simply make the wrong target easier to hit. This separation is a described organizational framework, not proof that either loop caused a particular outcome. [cite:q4Tr-DknG2M:c01]

For an automated change loop, name the target, the sensor that observes the current state, the controller choosing a change, the actuator applying it, and the feedback after the change. For an illustrative example, a code-quality sensor might detect a specified undesirable pattern, while a proposed edit must be checked against that target and other relevant constraints. If the property cannot be observed or an edit cannot be checked, repeating prompts is not a closed control loop. The control analogy does not prove stability for a stochastic agent. [cite:xIt_mTQp6mY:c01]

## Optimize without teaching to the test

Changing a prompt, tool or harness after inspecting scores resembles training, even with frozen model weights: the suite guides successive choices. Repeated use can fit particular cases, or reward a shortcut that raises the verifier's score without achieving the task. This is an analogy and a risk, not evidence that every score improvement is overfitting. Inspect both outcome and traces to see what actually changed; a pass/fail result tells you much less about the failure mechanism than an execution trace can. [cite:jRCpXUjz4CI:c02] [cite:CvRngaQZQ3Y:c08] [cite:CvRngaQZQ3Y:c11]

Use development feedback to formulate a change and keep independent evidence for evaluating it. Rollout trajectories can feed supervised training, rewards can support reinforcement learning, and textual feedback can guide prompt or harness revisions, but a rollout used to optimize is not thereby a held-out test. Protect independent cases from iterative tuning and investigate when a gain is confined to the familiar suite. For practical set maintenance see [[build-and-maintain-production-grounded-evaluation-sets]]; for holdout protection see [[protect-holdouts-and-historical-evidence]]. [cite:jRCpXUjz4CI:c12]

## Make claims falsifiable

Write down a claim that could fail, then deliberately seek a counterexample rather than only demonstrating favorable cases. One answer-first strategy chooses a known expected result, constructs an input intended to require it, and checks whether the system recovers it. A tool workflow can similarly have an expected endpoint order. Sometimes the solution must be redesigned to make these checks possible, and not every task admits a known-answer construction. [cite:mMw3arwQsL0:c08] [cite:c_SPW__jF9w:c10]

A planted case tests the chosen rule, not the entire problem. A green synthetic suite is useful development evidence but not sufficient release authorization; retain real-world and independent evidence for cases the construction did not anticipate. There is no universal stopping rule in the cited challenge loop. [cite:c_SPW__jF9w:c12]

## Choose where to adapt and where to repeat

A fixed executable workflow can repeat a known procedure, but an interface change may break it; a model-driven agent can adapt to an altered interface but may make different decisions on identical runs. Choose the stable path where repeatability matters and adaptive handling where variation is unavoidable. Determinism does not guarantee correct results in a changed environment. [cite:tyFPqtyOK5w:c07]

One experimental hybrid records a successful trajectory as code and tries replay on a similar request, checking intermediate state and stopping or invoking adaptive repair on a mismatch. A live demonstration needed fallback after a replay hiccup; its verification predicates and miss rate were not specified. Treat this as a design option to test, not a solved reliability or safety guarantee. [cite:tyFPqtyOK5w:c08] [cite:tyFPqtyOK5w:c09]

## Evaluate learning across time, not only recall

Continual learning asks whether a system can use ongoing experience efficiently while retaining still-useful knowledge and updating when facts change. A meaningful sequence includes a stable period to test retention, then a change such as renamed database columns to test whether stale knowledge is discarded without losing valid schema knowledge. Measure performance as experience accumulates, not only whether a note was saved. [cite:iqloyWCGYQQ:c01] [cite:iqloyWCGYQQ:c08]

Two narrated traces illustrate different failures: a forecast returned to an already rejected high value after feedback said a later forecast was too low; elsewhere, relevant cohort definitions were stored but dismissed as belonging to another study. These individual traces do not establish prevalence or prove a repair. They show why preservation and willingness to update must both be tested. [cite:iqloyWCGYQQ:c10] [cite:iqloyWCGYQQ:c11]

Use a simple retained-context baseline before crediting a more elaborate memory system. In initial speaker-reported medium-horizon comparisons, vanilla context led aggregate reward and the reported reward-to-cost or gain-to-cost frontiers; exact scores and uncertainty were not given, and longer horizons may change the comparison. Designing architecture and training explicitly for ongoing learning is a research hypothesis, not a demonstrated universal winner over contextual methods. [cite:iqloyWCGYQQ:c09] [cite:iqloyWCGYQQ:c12]
