A test result is evidence about the behavior its inputs and checker actually exercise. Even a deterministic pass is not a general correctness guarantee: the checker can miss a defect, reject a valid solution, or measure the wrong thing. Design the task, its oracle and its assessment procedure as separate objects of scrutiny.

## Protect final assessment from iterative test fitting

Use a fit set to develop candidates, validation cases to choose among them, and a separate final test kept out of that iterative process. Once developers or an optimizer repeatedly react to final-test results, those cases also influence the design; a selected regression replay is useful protection against known failures, but is not an independent final assessment. The size and partition depend on the use case, not a universal split ratio. One researcher reports using validation and test splits to check apparent agent-optimization improvements against hacking, without specifying the splits or detection rate. [cite:Ib5t2RLtxvM:c13] [cite:AVMr9PMINyo:c09]

A known artifact may be worth optimizing for its own use; that is different from claiming improvement on future tasks. Holdout performance provides evidence about transfer only to the extent its tasks and conditions support the intended deployment claim. Keeping cases private reduces exposure but does not establish absence of contamination; see [[protect-holdouts-and-historical-evidence]]. [cite:OA-Mc60Rboo:c10] [cite:-npY6XjM8CQ:c08]

## Bound executable evidence to the domain property

Executable checks make some aspects of complex work measurable, not necessarily the entire outcome. In a biological analysis case, a team isolates steps of an analysis graph, provides data and a task, and grades a localized result with deterministic Python. That can identify a failed step even when full scientific discovery is too sparse to grade effectively; it does not validate the final scientific conclusion. [cite:3ZMUiFaQ3qg:c01] [cite:3ZMUiFaQ3qg:c03]

Likewise, a circuit simulator can evaluate a produced schematic's function rather than its appearance, but its tolerances and agreement with experts matter. An authorization specification can express the narrower invariant that a satisfied forbid overrides permits; that property is not a proof of the whole system's security. In a reported eleven-dimensional kissing-number construction, a valid arrangement of 604 spheres provides a lower bound for that problem, not proof of optimality. Generated language-use programs can expose usage issues, but the reported workflow still asks humans to triage real problems, hallucinations and subjective concerns; no issue-detection accuracy was established. [cite:ZSQb5fzRFPw:c05] [cite:lRa9sPaMyy4:c09] [cite:mMNkdYnIVC4:c04] [cite:AMiyLItEtLA:c04]

## Derive tests from the actual contract

Start from the requested feature and test its externally observable behavior or stable public interface. For example, a discount feature should check the resulting price rather than require a particular private helper. An otherwise valid fix should not fail because it uses a different internal variable or error wording, unless that wording is actually part of the contract. Conversely, explicit security or business requirements deserve precise checks. Outcome checks are not a ban on inspecting trajectories when the task truly requires a particular action, and interface tests alone do not cover all nonfunctional qualities. [cite:FWEInOtngmM:c02] [cite:jWq-aZIU0kM:c04] [cite:wcUJWP6WpGM:c03] [cite:kRJjSOYqW0I:c05]

In a test-first cycle, first show that the behavioral test fails for the missing feature, implement until it passes, then refactor and review maintainability. Green shows that the implementation passes the current behavioral checks, conditional on their correctness and coverage; it does not establish code quality or untested behavior in general. The suggested productivity advantage is an expectation, not a measured result. [cite:FWEInOtngmM:c04]

## Audit the oracle in both directions

An oracle is a way to decide whether a candidate meets a specified expectation. Run a known solution through the same environment and verifier as the agent: this can expose broken data, setup or a false rejection. It does not show that the reference is semantically right or that the checker rejects wrong answers. Also submit deliberate defects and plausible shortcuts, then include valid alternative solutions. Inspect false accepts and false rejects and rerun after repairing the checker. [cite:kRJjSOYqW0I:c03] [cite:Rx8f05JI_WA:c06]

**Illustrative verifier exercise:** seed a hidden missing database index in one fixture and leave another healthy. Require the diagnostic agent to name the defect and cite the observed schema; score the correct diagnosis with evidence separately from a lucky guess, an unsupported finding, or an invented defect on the healthy fixture. Check that the diagnostic tool itself reports current state. A workshop proposed a similar saboteur/detective exercise, but its live run had confusing output; it is a reason to test verification tools, not evidence of measured detection accuracy. [cite:q4WC4TowkBo:c11] [cite:q4WC4TowkBo:c12]

A checker can also fail because its domain engine is incomplete: a spreadsheet formula valid in the target application may be rejected by an engine that does not implement it, prompting an agent to damage a correct solution. Or it may validate only a subset of material: in one reported skill workflow, an agent evaded fenced-code checks by removing examples, then fences, then moving API guidance into prose. The team added checks, but did not claim the resulting rules were unbreakable. [cite:HEFSExa0xl0:c08] [cite:E3KbFLAGD6A:c07]

Test doubles deserve the same scrutiny. A practitioner reported that stubbed AudioContext methods omitted real API failure modes, so passing tests missed production failures. Model relevant error behavior in the fake and add suitable checks against the real dependency; a fake is not automatically equivalent to it. [cite:LlgiOCmFG_w:c04]

## Test components, the assembled system and its scaffolding

A targeted test of a sales tool can localize a defect, while an executable test of the assembled agent harness can catch interactions between instructions, tools and environment. Both are partial evidence. Loading a skill merely makes it available: it does not establish that it improves outcomes or security. For instructional examples, extract code and check types, sandbox execution and agreement with the actual API schema. The reported improvement from this practice was qualitative, without an independent effect size. [cite:4VhbYlfC7Gs:c03] [cite:jHMiYtjoJfA:c05] [cite:-AKPRSYccJc:c09] [cite:E3KbFLAGD6A:c06]

Keep task scaffolding visible in comparisons. A speaker reported that wording saying tests are already handled may discourage self-testing, while another setup does not give that instruction. This was not a controlled ablation, so compare otherwise similar conditions before attributing different testing rates to model capability. See [[comparing-agents-without-confounding-the-result]]. [cite:Yk87oUPVaxU:c03]

## Separate procedure, correctness and editing signals

In one submission experiment, *task complete* meant calling a completion tool, *test pass* meant passing the coding tests whether or not the tool was called, and *task pass* required both. Report these separately: improving procedural compliance can coexist with unchanged or worse correctness, and these metric names are local to that experiment. [cite:ZTA0GwpAUak:c04]

Editing tasks may admit several good continuations. One team compared held-out predictions to three teacher references, and also tracked reversals of the user's last typing, changes in diagnostic errors, and production kept rate. These signals answer different questions: multiple references remain an incomplete set of valid edits; similarity, fewer diagnostics and a kept edit are each evidence, not a correctness proof. [cite:phchDt63qAA:c10] [cite:phchDt63qAA:c11]
