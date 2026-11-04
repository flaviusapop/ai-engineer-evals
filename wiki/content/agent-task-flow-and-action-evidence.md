Agent work is not finished merely because a model says it is done. A useful workflow makes it possible to tell who owns the next step, whether the receiving step can use the output, what actually happened at an external boundary, and what evidence supports the outcome. Those are related but distinct questions.

## Separate required gates from adaptive repair

Map the dependencies that must hold before work advances. A proposed design puts those forward dependencies and required gates in an outer workflow, while allowing iteration inside a node: a code-review step can request changes and review again without skipping the later required check. Independent reviews can run in parallel, then join before a dependent decision. In the illustrative lending workflow, some verification and financial work can proceed alongside each other even though later steps remain ordered. This is an architectural proposal, not a proven compiler or measured speedup. [cite:_4Ph2dhmUFI:c02] [cite:_4Ph2dhmUFI:c03]

A workflow diagram states the intended progression; it does not by itself enforce access restrictions. Policy intent and the running system are different things, and runtime restrictions must actually be implemented. See [[agent-authority-isolation-and-runtime-controls]] for enforcement. [cite:_4Ph2dhmUFI:c01]

## Advance work without losing custody or shared updates

Choose the next task from current state and record its dependencies, allowed transitions, blocker, current owner and next action. When the producer finishes, name the reviewer or other recipient and what they must do; stopping the producer is not the same as transferring custody. One coding-loop practitioner recommends selecting the next important ticket afresh after each change, and, when workers share a backlog, claiming a ticket and checking for contention before starting. His failed parallel attempt is not proof that parallel work is generally impossible. Ticket claims alone are not atomic locks. [cite:2TLXsxkz0zI:c02] [cite:2TLXsxkz0zI:c15] [cite:7P0elyLIxXo:c05] [cite:7P0elyLIxXo:c09]

A watchdog can notice stalled progress and prompt further work, but it must respect genuine blockers and a bounded stopping rule: activity is not evidence of completion. The described watchdog and liveness invariants are proposals, not guarantees of termination. [cite:7P0elyLIxXo:c04] [cite:7P0elyLIxXo:c06]

Coordination also applies to data, not only tickets. Two workers can read the same old state, independently edit it, and have the second save erase the first. Order commits at each shared mutable boundary with a suitable transaction, queue or lock; independent reads and unrelated work need not be serialized. This is a proposed invariant, not a tested universal locking implementation. [cite:BInpv7lGp1o:c03] For topology choices, see [[agent-delegation-and-coordination]].

## Accept the artifact, not just the handoff

Custody says who acts next. An artifact contract says what the receiver needs. Check required fields and structure at the producer-consumer boundary, then check substantive domain requirements before promotion. After changing a prompt or skill, rerun representative downstream checks: a locally plausible artifact may break several consumers. This delivery-control inventory comes from one practitioner's workflow, not a framework comparison. [cite:WLXxTaPagA8:c01] [cite:WLXxTaPagA8:c02] [cite:WLXxTaPagA8:c04]

A content demonstration makes the distinction concrete: a complete, ready-marked package can still have an opening hook that repeats a previous angle. Compare that meaningful unit against relevant history rather than merely checking that the file is new. The demonstration does not disclose a similarity algorithm or threshold; novelty is one domain gate, not a substitute for the rest of the contract. [cite:WLXxTaPagA8:c08]

## Observe current state and validate recovery

Before choosing an action, refresh the facts the step can actually access: workflow position, current components and errors, and relevant operational measurements. One reported pipeline snapshot returns flow context and specific error codes, helping an agent refer to present components rather than remembered names. It comes with no stated consistency or concurrent-edit guarantee. Check for missing or inaccessible context rather than assuming the snapshot is complete; keep a human-readable operational view as well as programmatic access. Dynamic feedback can guide the next step, but changing output is different from cacheable static instructions. [cite:jJQoVkd5yLg:c04] [cite:YNT7Plf9KIg:c02] [cite:P_0_Th_ZzIg:c06] [cite:SQMCtZX3trg:c06]

For remediation, distinguish **proposal → permission → executor capability → attempt → verified recovery**. A bounded set of actions makes a decision inspectable, but a safe proposed action is not necessarily available, and an available action is not necessarily successful. In a synthetic incident capstone, a datetime conversion is reportedly permitted but unavailable in the executor; the incident is recorded and sent for manual review rather than called fixed. The captions are corrupted, so this interpretation is provisional; it is not evidence of live recovery. If an action is attempted, check the actual downstream result, such as a successful rerun and the resulting data, before reporting recovery. A fixed decision threshold is a teaching simplification, not an established production policy. [cite:LrGCT7G_rU8:c03] [cite:LrGCT7G_rU8:c06] [cite:LrGCT7G_rU8:c01] [cite:Zd5b40Jbp_k:c07]

## Time checks to the recovery window

Inspect arguments and results before or during consequential actions when waiting would make errors unsafe or hard to reverse. A vendor describes selected appointment checks that can run after a call if an error can still be corrected or a patient called back. That example does not make urgent clinical risks deferrable, nor does a later check guarantee correctness. [cite:AN65uc645mE:c08]

For replayed actions, verify expected intermediate interface state at each relevant step. If it differs, stop the replay and fall back to adaptive reasoning rather than continuing a stale macro. In an experimental conference-schedule replay, a filtering hiccup led to fallback; the predicates and missed-error rate were not specified. Repeatability and adaptation remain a tradeoff, not a solved reliability guarantee. [cite:tyFPqtyOK5w:c09]

## Record gates and the historical action chain

Ask for a separate result for each instructed gate, rather than accepting one compressed checklist claim. This can expose omissions, especially with weaker instruction followers, but prompt-level logging is neither independent enforcement nor tamper-proof evidence. [cite:SQMCtZX3trg:c12]

An action receipt answers a broader historical question. Record the trigger and its identity, inherited state, proposal, applicable authority decision, actual arguments and attempts, and the external result or failure to confirm it. Preserve the actual inputs, model and configuration, output and reviewer action: a later rerun is not what happened then. An internal message tool accepting a request, for example, does not establish that a user saw the message; delivery and persistence can fail separately. The receipt is a proposed architectural contract, not a standard format or cryptographic proof. [cite:BInpv7lGp1o:c08] [cite:BInpv7lGp1o:c07] [cite:BInpv7lGp1o:c06] [cite:3ZlQk4-knWM:c11]

Start an audit with one real path: identify its trigger, inherited state, authority, execution and surviving evidence. Trace each side effect through attempts and any idempotency information to the boundary the user cares about. This is an inspectable starting point, not a reliability assessment of the whole deployment. [cite:BInpv7lGp1o:c09]

## Bound triggers, recovery and changing goals

Specify when an unattended agent wakes—on an event or schedule—and the evidence window it should inspect. Monitor expected runs and silent failures separately from the quality of produced artifacts; a trigger is not completion. Three- or six-hour sweeps are examples, not optimal intervals. [cite:ImnZ7s68jw8:c03] [cite:WLXxTaPagA8:c03]

Give external calls deadlines, cancellation and explicit terminal outcomes, and let recovery commands bypass the lane blocked by the operation they repair. Feed errors back into the workflow, cap retries and exploratory investigation by count or time, then validate, report or escalate. Select limits for the operation and its risks; a cited three-retry example is not a universal optimum. The incident motivating the blocked-lane proposal had no established exact cause. [cite:BInpv7lGp1o:c04] [cite:3_gYbhABcAE:c05] [cite:ObTPqBGsEbA:c05] [cite:EcqMYoIV57A:c04]

After interruption, inspect existing work before starting over: a dirty working tree and passing tests are clues, not proof of completion. Saving progress outside a disposable runtime can enable resumption, but neither saved state nor retries establish exactly-once external effects. In the discussed generated-code setup, resuming inside a failed program remained an open problem. See [[agent-sessions-and-long-running-work]] for session lifecycle. [cite:2TLXsxkz0zI:c05] [cite:ImnZ7s68jw8:c07] [cite:dAoOYFx7ZYw:c10]

Finally, allow the route to change when the user changes their goal: a cancellation conversation need not remain locked in its original branch. Re-establish the intended outcome and apply the same relevant controls and verification to the new route. This is a design argument, not a demonstrated improvement in satisfaction or safety. [cite:3_gYbhABcAE:c04]
