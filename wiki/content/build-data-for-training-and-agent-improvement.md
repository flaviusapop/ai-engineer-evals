Training data is not just a collection of inputs. It embodies decisions about which situations are generated, which outcomes count as desirable, which targets are trusted, and what the student should learn. Those decisions can improve the training signal while also introducing biases that a separate evaluation must detect.

## Generate and filter synthetic interaction trajectories

A proposed approach runs an agent in a simulated environment, generates candidate interaction trajectories, scores them with a reward, and rejection-samples the apparently desirable trajectories for training. Real customer conversations may inform the simulated user. The reward determines which behavior is selected; the simulator determines which situations the agent can encounter. Consequently, both shape the resulting data, including their blind spots. [cite:X6NShR2ccOg:c06]

**Illustrative example:** If a support simulator rewards ending conversations without human handoff, it may select a trajectory that keeps a distressed caller talking when escalation would have been appropriate. A high reward would then certify the proxy, not the user's welfare. Review the reward and selected examples against the intended outcome, including cases that deserve escalation. This is a vendor proposal, not independently validated evidence of improved real-user outcomes. For designing and checking the simulated world itself, see [[build-and-validate-simulated-agent-worlds]].

## Curate teacher targets and behavioral hints

A teacher can label realistic task contexts, but a stronger model is not an infallible labeler. One editor team described collecting opt-in production snapshots containing the context available at an edit request and asking a frontier teacher for a prediction. Snapshot inputs connect training to actual tasks, but opt-in alone does not establish representativeness or describe all privacy handling. [cite:phchDt63qAA:c02]

The team checks predictions for concrete violations, such as undoing what the user just typed or changing text outside the editable region. A failing prediction goes to another model with the failure explanation for repair before use as a training target. This controls identifiable failure modes, but the account gives neither repair accuracy nor remaining error rates; checks can miss bad labels and repairs can be wrong. Inspect targets and measure downstream student behavior rather than treating the repair step as a guarantee. [cite:phchDt63qAA:c03]

When trustworthy traces are scarce, one speaker recommends keeping a smaller, human-inspected golden subset and testing a higher training weight for it. The same speaker suggests that some failed reasoning traces might sometimes help smaller students. Those are conditional hypotheses to test through mixtures and student measurements, not a general instruction to discard every failure or train on all errors. No supporting experiment for the alleged benefit of failed traces is supplied. [cite:Ti-BmGU1_mQ:c10]

A complete ideal answer is not always available. Another proposed distillation approach gives the teacher privileged information about a specific behavior to improve, such as an undesirable formatting pattern or a tendency to continue rather than wrap up. The hint narrows supervision without supplying a perfect response for every task. It still needs validation: hints may be unreliable, downstream quality can regress, and the approach is not guaranteed to work for every enterprise task. [cite:ZTA0GwpAUak:c03]

## Select the skill, difficulty and verifier

Start with the intended skill, then select tasks that exercise it and can be executed safely. For reinforcement learning, tasks that are always trivial or impossible provide little useful learning signal; seek a productive difficulty range for the current agent and revise it as capability changes. The source gives qualitative guidance, not a universal success-rate target or selection algorithm. Match the verifier to the outcome: an equality check, compiler, unit test, database lookup, or rubric-guided judge may fit different tasks, but each creates its own training signal and can reward the wrong thing. See [[tests-oracles-and-verifier-validity]] for verifier validity. [cite:Cc0_nyxROBA:c02]

A visual reasoning company described purpose-built multimodal data and a loop involving evaluations, agents, supervised fine-tuning and reinforcement learning. The transferable decision is to target the missing visual skill rather than presume a generic image-text corpus covers it. The company did not disclose the dataset composition, recipe, filtering, or measured gains, so this is not proof that its flywheel works. [cite:A_I8mw8yfns:c08]

## Feed observed gaps back into the data

An OCR team described using evaluation results to update training inputs, combining synthetic examples and real documents when labels are scarce. The operational loop is: inspect a failure, identify the missing training pattern, add or improve relevant examples, then measure the changed model. Annotation quality and contamination safeguards were not described in the account, so the loop is not itself evidence of generalization. Keep independent assessment separate from data used to tune the system; see [[protect-holdouts-and-historical-evidence]]. [cite:T72nqdC92PM:c05]

Internal records may also contain knowledge absent from public data: failed experiments, trade theses and explanations of why a decision did or did not work. Preserve the context and outcome rather than training only on apparently successful decisions. A speaker proposed such proprietary negative data as a differentiator; neither the business advantage nor the claimed ease of quickly structuring it was demonstrated. [cite:Yphdry8ttAQ:c02]

## Keep execution receipts and bootstrap flow specifications

Retain the journey as well as the final status: actions, errors, timings and final state can help reviewers diagnose a run and curate future examples. A reported e-commerce journey, for instance, includes login, catalog loading, cart actions and abandonment. A receipt records what happened; it does not by itself define a correct outcome or become an executable test. Proposed overnight aggregation and autonomous fixes were not demonstrated results. [cite:q4WC4TowkBo:c09]

A related proposal would enrich nontechnical UI feedback with recordings, console logs and network requests. Its live integration did not run and only initial mocked tests were reported. Treat the added context as potentially useful evidence, not a verified automated improvement pipeline. [cite:ZGzthw4BZiA:c12]

Where written flows are missing, one described tool performs a one-level surface crawl of the current website and generates Gherkin user flows. This is a starting point for human review: a shallow crawl observes existing behavior and visible links, not the intended requirements, hidden paths, or complete acceptance criteria. A current defect can be reproduced as if it were a requirement unless someone checks it. [cite:ZGzthw4BZiA:c05]
