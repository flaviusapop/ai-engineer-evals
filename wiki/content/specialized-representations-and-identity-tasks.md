A model's representation and its evaluation target are choices, not interchangeable abstractions. A sentence-like sequence of gene measurements, anonymous speaker IDs, and a list of exact words may all be processed by machine learning systems, but success on one tells us little about the others. In each case, identify what the representation preserves, what counts as the same answer, and what the test leaves out.

## Source context: language interoperability and adoption

One language-tooling speaker proposed exposing functions to existing languages through bindings rather than requiring a wholesale rewrite. The demonstration included Python calls and callbacks. This is **peripheral adoption context**, not an evaluation method: lower migration friction is the speaker's rationale, not a measured result, and the demonstration is not a broad compatibility study. For evaluating executable programs, see [[tests-oracles-and-verifier-validity]]. [cite:AMiyLItEtLA:c09]

## Specialized representations and identity tasks

### Language as an intermediate representation

One panelist explains language-based intermediate reasoning as a way to use capabilities already learned in language pretraining. That is a plausible rationale for a productive current approach, not a controlled comparison proving that latent, code, or visual representations cannot work. A different representation may be preferable when the task requires information that text does not readily convey. [cite:KLDdXOw6jIc:c03]

For example, a reference recording can convey prosody that a user struggles to describe in words. The panel disagreed about whether such limits are fundamental to language or reflect insufficient data and development; observed difficulties do not settle that question. Compare representations against the information and outputs the actual task requires, rather than assuming a single channel is universally best. [cite:KLDdXOw6jIc:c05]

### Cells as gene-related tokens

In one described single-cell modeling approach, a cell-by-gene expression matrix is represented with cells analogous to sentences and genes to tokens. A transformer learns by predicting masked genes or expression information using bidirectional attention. Its learned representations can then be used for tasks such as cell-type prediction or perturbation-response modeling. This is a modeling analogy and training objective, not evidence that cells share the statistical properties of language. The available account does not specify the exact objectives or tokenization of the named models, and its captions need review; it does not establish clinical benefit. [cite:-561cZmir5Q:c05]

### Anonymous identity is not a person's name

Diarization groups speech turns by speaker; it does not necessarily determine real names or know the true number of participants in advance. A meeting attendee list may help but does not establish who joined or shared a channel. Evaluation should allow a **consistent permutation** of anonymous labels. [cite:mFLlVpnGpds:c03]

**Illustrative example:** If the reference assigns three turns A, B, A and the system assigns 2, 1, 2, swapping the system's 1 and 2 yields the same grouping. Scoring literal label names as errors would be wrong. Conversely, 2, 1, 1 still incorrectly groups the final turn after any consistent swap. This scoring equivalence does not identify either person's real name.

## Testing instruction capacity and robustness

### What the word-inclusion proxy measures

A simple instruction-density experiment asks a model to write a synthetic business report containing a specified list of exact words. Vary the number of requested words and score the fraction present; this measures tracking of these simple lexical constraints, not quality of the business analysis or reliable compliance with an entire skill file. [cite:XzJD1bvXKjs:c01] [cite:XzJD1bvXKjs:c06]

The speaker reported sharp decline near 2,000 constraints for some tested models and up to 5,000 for the best. These are model-, version-, and task-specific observations, not safe general instruction limits; the word list was filtered for one model, the tested models varied, and the results were not independently verified in the supplied notes. Track *how* runs fail: omission, refusal, exhausted reasoning budget, or an incomplete but polished-looking response demand different remedies. A single fraction hides those differences. [cite:XzJD1bvXKjs:c03] [cite:XzJD1bvXKjs:c05]

If the intended application has interacting or conflicting instructions, test those separately. Adding more instructions may increase coverage but also consumes tokens and can add latency; a longer prompt is not automatically a better system. [cite:XzJD1bvXKjs:c06] [cite:XzJD1bvXKjs:c07]

### Probe presentation separately from capacity

Specify which variations should preserve acceptable behavior for the role, then test them: typos, paraphrases, and reordered equivalent instructions, for example. Keep the underlying requirement fixed while varying presentation so that a failure indicates sensitivity to the change rather than a different task. The reported effect of wording and order is secondhand in the source, without its full method or data; it motivates a probe, not a quantified reliability claim. [cite:UQKg0td-Bf4:c08] [cite:XzJD1bvXKjs:c08]

**Illustrative example:** A support agent's policy limits a discount. Compare a plainly worded request with a misspelled paraphrase and reorder the same policy instructions; record the response and whether the limit was respected. If the change alters the allowed discount, investigate the failure. Passing these finite variants cannot prove the rule will never be violated. Choose variants and their prevalence for the decision at hand, as discussed in [[design-evaluation-distributions-for-decisions]]. [cite:UQKg0td-Bf4:c04]
