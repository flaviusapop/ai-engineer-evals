A clinical-support guardrail has two distinct jobs: detect situations requiring intervention and allow useful support when intervention is not warranted. Both a missed danger and an unnecessary refusal can harm the person seeking help. A useful evaluation therefore asks what happened, at which boundary and conversational turn, and whether the response was appropriate to the context—not simply how often a guard fired.

## Place checks at distinct boundaries

In one mental-health support architecture, a separate input check runs before the conversational core responds; a separate output check examines the response and the broader conversation. Separating the calls allows the team to change and evaluate the core and guards as components rather than assuming the core's instructions guarantee safety. The speakers considered separate guards harder to steer conversationally and accepted extra model cost and latency; they did not provide a comparative attack-success measurement or prove completeness. [cite:O72p-rBb2bA:c01] [cite:O72p-rBb2bA:c02]

Placement changes what a guard can prevent. An input rejection can stop a selected request before the core or tool incurs processing cost. Output redaction can prevent sensitive content from appearing in the final response, but it happens after inference and cannot by itself show that no sensitive operation occurred. Test and record which layers are enabled so a successful output check is not misattributed to the input guard. Measure guard behavior separately from response quality, system health, latency and cost; a high rejection rate alone is not proof of safety. [cite:1tpqdglI3T0:c08] [cite:T0HhO4YtTfE:c07]

Action boundaries differ again from message filtering. A workshop reported that a cluster admission policy blocked a public-registry deployment, while its runtime protection failed to stop disclosure of a recipe. Replay a previously successful case against the hardened setup and distinguish admission rejection, model refusal and runtime prevention; not obtaining a secret does not identify the protective layer. These were workshop observations, not a systematic effectiveness study. For the separate mechanics of action authorization and containment, see [[agent-authority-isolation-and-runtime-controls]]. [cite:1tpqdglI3T0:c03] [cite:1tpqdglI3T0:c04] [cite:1tpqdglI3T0:c05]

## Calibrate intervention to context

The team's goal was *correct* triggers, not the largest number of triggers. An overly broad response to a sensitive topic may reject someone who could have continued receiving support; under-triggering can miss real danger. Calibration must consider both errors and the consequences of each, not optimize a benchmark score by making every ambiguous message a crisis. [cite:O72p-rBb2bA:c03] [cite:O72p-rBb2bA:c09]

The speakers' **synthetic representative scenarios** illustrate their proposed policy, not universal clinical triage rules or validated patient outcomes:

- A person hiding from an actively threatening husband is routed to resources and disengagement.
- A person questioning whether a past event was assault receives resources but may continue talking.
- A relationship difficulty with no indication of danger passes through to the conversational core. [cite:O72p-rBb2bA:c04]

The distinction is not the mere presence of a sensitive word: immediacy, evidence of danger and the appropriate support action matter. Define categories and expected actions with clinical expertise for the intended setting, including uncertain and ordinary-distress cases. The source supplies no quantified sensitivity–specificity tradeoff and does not establish patient benefit.

## Test the right intervention at the right time

A multi-turn regression case should preserve the conversation, the turn at which an observation is expected, and the expected observation and category. Replay up to that turn; assert not only whether an intervention occurred, but whether it occurred at the intended point and whether the output evaluator identified the issue type. Also include cases where no intervention is expected, so a change that catches more danger by interrupting ordinary support is visible. [cite:O72p-rBb2bA:c08] [cite:O72p-rBb2bA:c09]

**Illustrative test:** A conversation starts as an ordinary relationship problem, then introduces an immediate threat at a later turn. Record the expected non-intervention earlier and the expected observation and category at the later turn. A final crisis label alone would not reveal whether the guard responded too soon or too late. The actual clinical action and labels require domain review; the example is not a validated triage protocol.

Finally, run the full stack, not only the application's guard. The speakers reported that a provider model's built-in safety behavior initially filtered evaluation cases even where their application policy would permit support. Record application decisions and provider refusals separately so that an approved input followed by a refusal is visible. The account does not explain a reproducible way to disable provider safeguards, and it is not evidence they can generally be turned off. [cite:O72p-rBb2bA:c11]

These architecture and regression examples describe a prototype and evaluation process, not a controlled study of clinical outcomes. Use [[clinical-safety-and-operational-review]] for the broader clinical oversight context and [[safety-evaluation-and-adversarial-probing]] for probing safety behavior beyond these calibration cases.
