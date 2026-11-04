Human feedback becomes useful evaluation evidence when its origin, context and uncertainty remain visible. A click, a reasoned expert judgment and a later edit answer different questions; treating them as interchangeable can turn convenience into false confidence.

## Preserve an independent first judgment

Show a reviewer the task and relevant evidence before showing the model's verdict. Save that first assessment, then reveal the model's reasoning and record any revision and why it changed. In a browser-verifier experiment, experts assessed full trajectories first; the verifier sometimes surfaced details they had missed. Independence protects the reference from immediate anchoring, not from human error. [cite:xLxhT2ZI7UM:c06]

Test whether reviewers actually deliberate. One copy-typing study inserted false alerts into legitimate historical sessions without affecting customers; reviewers sometimes accepted the signal despite strong calibration scores. Its sample size was not disclosed. If uncritical approvals are later reused as labels, they could reinforce the original errors; that feedback loop is a proposed mechanism, not a measured effect in the study. [cite:CDqzWpwkSls:c01] [cite:CDqzWpwkSls:c04]

Acceptance-weighted adaptation is a separate concern. A code-review system can use accepted and rejected suggestions to adjust what it offers, but a team can reject an important security warning. Keep mandatory rules and independent expert review separate from popularity; the described weighting safeguards are unspecified. Past review history can supply context without becoming the standard of correctness, and noisy utility feedback can misassign credit. [cite:EcqMYoIV57A:c06] [cite:EcqMYoIV57A:c07] [cite:Jx4ZFEAq6bY:c08] For measuring held-out judge alignment with these references, see [[validate-judges-against-human-labels]].

## Capture the reasoning and the evidence

Ask domain practitioners, including nontechnical experts, to inspect real outputs and explain the judgment, correction and significance of each error. Walk through completed cases: what did the expert look for, why did it matter, and what would have prompted a stop or question? Retain the sequence and constraints as well as the final artifact; otherwise a finished product can hide the decisions that made it acceptable. A small first set is useful for elicitation, not a guarantee of domain coverage, and expertise does not ensure experts agree. [cite:NKwIX3CiRgU:c06] [cite:yqF6XhzbWBk:c11] [cite:gpmze-6ueGU:c04] [cite:KLDdXOw6jIc:c14]

Attach each label to its supporting evidence and record the depth of verification: for example, whether a reviewer inspected only an extracted field or checked the original source. This makes a conclusion distinguishable from the work supporting it; it does not prove the conclusion correct. One campaign-finance case reports evidence-bearing labels, but their completeness was not independently audited. [cite:Fa3hQVIKShw:c06]

Make that work practical. Present traces in the form the domain expert recognizes, with a short set of decisions and room for comments. For visual review, associate a comment with a marked region or relevant component rather than leaving the recipient to infer its target. A demonstration exported located feedback as structured data, but did not disclose its full schema; neither a tailored view nor deterministic capture establishes that the annotation or proposed fix is correct. [cite:FB-MLPhL9Ms:c03] [cite:lCBf9slCanI:c10] [cite:ZGzthw4BZiA:c03]

## Interpret disagreement rather than erase it

Specify the dimension before resolving disagreement. Two reviewers may disagree whether a visual element meets a stated alignment requirement, suggesting a definition or inspection problem. They may also genuinely prefer different styles; averaging those tastes into one label can erase useful information. Record the reviewer’s relevant perspective, preference and conditions, and select experts across meaningful styles or media rather than relying on a large undifferentiated pool. The boundary between an objective requirement and taste itself needs definition; proposed preference vectors and diversity benefits have not been validated here as training results. [cite:lCBf9slCanI:c07] [cite:lCBf9slCanI:c08] [cite:lCBf9slCanI:c11]

Separate perceptual observation from policy. In the hearing-aid example, detecting an apparent ear device may be correct while the device is permitted. A single “violation: no” label would incorrectly suggest the detector failed. Record whether the observation is supported and, separately, whether the applicable policy makes it a violation. This is a design remedy, not a measured accuracy improvement. [cite:CDqzWpwkSls:c05]

Repeated verdicts or a committee can prioritize disagreements for human inspection. A disputed borderline case may expose missing context or an unclear decision rule; independent refinements of a vague specification may also reveal ambiguity. But inconsistency has other causes, unanimous models can share an error, and a disagreement-only queue misses consistent mistakes. Include other cases in review. [cite:wEc9aG7cRQc:c02] [cite:wEc9aG7cRQc:c03] [cite:bSG9wUYaHWU:c09]

For source-sensitive extraction, an alternative is independent duplicate work: give workers the same source and instructions without showing each other's outputs, require provenance, and reconcile differences against the source rather than by majority vote. The reported case uses agents; independence of presentation does not eliminate correlated model errors or substitute for professional sign-off. [cite:dYh7TQkuYFE:c02]

## Treat behavioral feedback as a clue

A complaint starts an investigation: ask what was wrong and inspect the relevant output. A staged demonstration produced a complaint that its author could not substantiate; it shows the value of clarification, not a measured false-report rejection rate. Likewise, capture what happened after acceptance: an edit may reveal a defect, a preference, a changed requirement or unrelated work. [cite:FlzpEGHNVKQ:c05] [cite:CDqzWpwkSls:c07]

A later editor snapshot can inform an earlier prediction, but the user's intent or the code may have changed in between. One experimental approach takes a snapshot after ten seconds without edits in a region, not after a commit. It compares samples from the original context with that later state, using closeness as a heuristic for predictability; it considers very distant examples noisy and intermediate cases potentially useful. Neither the pause nor text similarity proves satisfaction or semantic correctness, and thresholds, selection bias and training gains were not established. [cite:phchDt63qAA:c05] [cite:phchDt63qAA:c06] [cite:phchDt63qAA:c07] [cite:phchDt63qAA:c09]

Historical diffs have similar limits. Before inferring expected review flags, check that original and revised documents and relevant decisions exist. One contract project retained only final versions, and negotiation complicated interpretation, so its proposed diff-based route was unavailable. [cite:c_SPW__jF9w:c04]

## Audit the collection, not just its volume

Preference data can teach the wrong signal. A video judge reportedly learned overall polish and artifacts instead of the intended storytelling, physics or camera axes. Real-versus-generated pairs can also make origin or encoding a shortcut for quality. Normalize obvious nuisance differences across pairs and test challenging counterexamples for each axis; shared encoding and annotation do not prove all provenance confounding is gone. The diagnosis and improvement are internal, qualitative reports without an isolating ablation. [cite:b_PmGocP4rc:c06] [cite:b_PmGocP4rc:c07]

Inspect locally controllable properties—expert selection, evidence links, specificity and quality checks—even when downstream model-training feedback is unavailable. These properties make data more inspectable; they do not establish a causal training improvement or a universal quality-over-volume law. [cite:lCBf9slCanI:c12]

Finally, a public invitation alone does not ensure broad participation. Provide dataset hosting, access to relevant models and interpretable write-ups so contributors are not excluded merely by infrastructure or API costs. Access broadens the opportunity to contribute; it is not a statistical-validity guarantee. [cite:Ubwb6NzegyA:c04]
