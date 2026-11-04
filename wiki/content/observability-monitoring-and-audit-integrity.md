A healthy service can still follow a malicious instruction, disclose sensitive information or take an unauthorized action. Monitoring makes such behavior visible enough to investigate and intervene; a clean dashboard is not proof that no attack or leak occurred.

## Monitor different risks at their own boundaries

Use distinct signals rather than one generic safety score:

- **Manipulation attempts:** inspect incoming prompts or caller interactions for attempts to override instructions or bypass safeguards. Such events may produce no server error. An attempt flag is not evidence that the attempt succeeded, and a stated goal of blocking every jailbreak is aspirational, not a demonstrated result. [cite:rTojoVotlD8:c06] [cite:qStB9GbppMU:c10]
- **Sensitive output:** scan what leaves the model for potentially sensitive identifiers or personal information, using approaches such as pattern matching and entity recognition. A match needs policy context: detecting a sensitive string is not the same as determining whether this particular disclosure was authorized. The source supplies no labeled dataset, precision, recall or contextual disclosure policy, so a zero-leakage target is not evidence of complete detection. [cite:rTojoVotlD8:c07]
- **Harmful content:** moderation scores can flag content for review under a chosen policy. Polite text can still expose private data or carry an injection, and a single toxicity classifier is not established as adequate for every kind of harm or bias. [cite:rTojoVotlD8:c08]
- **Action drift:** inspect tool calls in the context of the task and session, not only as isolated events. A reviewer agent might gradually be persuaded to approve a security-sensitive change outside its checklist. A vendor reports using internally trained classifiers to assess action alignment, but does not disclose their labels, accuracy, latency or resistance to evasion. The scenario illustrates a risk, not a measured detector guarantee. [cite:BgLdvF7Qkh8:c04]

For a narrowly scoped recruiting agent, compare tool use with its historical pattern across the applicant system, calendar, notes and messaging. An unusual action can prioritize investigation; it is neither proof of attack nor a complete list of legitimate future actions. Broad coding agents may have less stable patterns. No anomaly threshold or false-positive rate is supplied for this case. [cite:BgLdvF7Qkh8:c06]

Connect each signal to a proportionate response: inspect the relevant session and task, route a concerning action to an accountable reviewer, or use an independently enforced restriction where policy requires it. Monitoring can inform selective intervention rather than a blanket stop on every agent action, but the cited guidance does not demonstrate an end-to-end enforcement mechanism or quantify residual risk. Context matters: the same tool can be legitimate in one task and inappropriate in another. [cite:BgLdvF7Qkh8:c03] [cite:BgLdvF7Qkh8:c11]

A session view also has a boundary. Suspicious content written into a shared system may later influence a different agent, so a benign-looking isolated call or one clean session cannot settle the whole sequence. The shared-data scenario is illustrative rather than an observed incident. For the underlying control and isolation design, see [[agent-authority-isolation-and-runtime-controls]] and [[prompt-injection-and-agent-threat-modeling]]. [cite:BgLdvF7Qkh8:c08]

## Check whether the audit record is complete

A trace is useful only to the extent that it actually captures the relevant activity. For security-sensitive evaluations, compare the agent's retained trace with records collected independently of that trace, such as traffic or change history. Investigate missing actions, conflicting timestamps or unexplained changes rather than assuming that an internally consistent record represents everything that happened. A separate record is also evidence with its own possible gaps; disagreement warrants investigation, not automatic attribution of fault.

A speaker recounts a third-party experiment in which a hash-check setup missed seeded security issues while an independent traffic and change comparison found them. The account does not specify enough of the mechanism to reproduce the result or conclude that hashes are generally ineffective. Its lesson is narrower: a check on a retained record is not automatically a check that all relevant activity entered that record. [cite:A3FL_zTQKU0:c09]

Observability can itself expose sensitive information. Decisions about what trace data to retain, who may access it and for how long belong to [[privacy-tenancy-and-data-governance]]; audit usefulness does not override those obligations.
