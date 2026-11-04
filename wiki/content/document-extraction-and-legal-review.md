A document system can return accurate-looking statements while omitting a critical page, transcribing a table incorrectly or reviewing the wrong person’s file. Evaluate the path from source document to extracted representation to decision: success at one stage does not establish success at the next, and faithful extraction alone does not establish legal correctness.

## Find missing information, not only incorrect statements

Check both whether emitted facts are supported and whether consequential facts are absent. In a speaker’s clinical illustration, a plausible headache note omitted jaw pain on chewing, a detail the speaker regarded as changing urgency. This is an illustration of omission severity, not independently validated clinical advice. A claims-review account similarly scores correctness, completeness and conciseness separately; its provider comparisons are snapshots without a complete numerical table or model settings. [cite:yqF6XhzbWBk:c01] [cite:W4pnzOURwHQ:c06]

A missing source document is a different problem from a missing fact in an available document. Cross-reference notes, scheduled procedures, reports and billing: if a note references a scheduled X-ray but the report is absent, flag the gap for follow-up rather than inventing why it is missing or assuming the procedure occurred. [cite:W4pnzOURwHQ:c04]

For legal review, test missing expected clauses explicitly. The requirement must be conditional on the applicable template and supplier type. A team described removing clauses from signed contracts and mixing these mutations with intact contracts that should receive no flag. The agents reportedly missed most removals; the account supplies no denominator, full omission taxonomy or final recovered performance. Intact controls reveal indiscriminate flagging, while deleted cases test detection—not the legal sufficiency of every contract. [cite:c_SPW__jF9w:c06]

## Establish record integrity before aggregation

Deduplicating pages and identifying records belonging to the wrong person are separate checks. Similar names can result in an unrelated person’s record being included in a claim, contaminating the analysis and potentially exposing private information. Verify identity and per-claim extraction before combining claims, and establish permission for the intended cross-record use. The case account does not measure how often contamination occurs. [cite:W4pnzOURwHQ:c02]

Once those prerequisites hold, aggregated records may help inspect provider networks or costs. Even then, price differences alone do not prove waste: a higher-priced provider might require fewer treatments, and patient outcomes matter. The described network visualization used a redacted subset; proposed savings were not established causal effects. [cite:W4pnzOURwHQ:c09]

## Diagnose the document pipeline

A structurally valid pipeline can silently miss a scan, segment the page incorrectly, read a block incorrectly or join blocks in the wrong order. One reported architecture separates layout and reading modules around block-level OCR, making segmentation and order distinct things to inspect; no ablation isolates the benefit of any component. Another account describes extraction confidence, bounding boxes and failures being returned to tools to help refine a schema. A bounding box helps a reviewer locate evidence, but a confidence number is not calibrated merely because it is available, nor do diagnostics detect every error. [cite:T72nqdC92PM:c02] [cite:jJQoVkd5yLg:c05]

State where the evaluation begins. A synthetic pipeline generating text and Markdown tests downstream reasoning over already parsed content; it does not test conversion from degraded scans, handwriting or visual checkboxes. Its speaker’s confidence in available parsers is an opinion, not a parser benchmark. Include source-image cases when those ingestion failures matter. [cite:XAsb7MIAzm8:c09]

## Select and test representations for the task

Plain OCR text may lose the row-column relationships, charts, formatting or reading order on which an answer depends. Compare representations using the same task and source documents: test both whether the representation preserves those features and whether downstream answers use them correctly. A vendor-affiliated account reported better PDF retrieval with a multimodal approach but did not provide the visual leaderboard details or implementation; another reported improved answers with structured parses, without full numerical methods and with one comparison model omitted. Neither establishes a universally superior representation. [cite:O84lhGc1OOI:c08] [cite:0I07YAuF8xA:c05]

Include varied, complex real document types when they reflect the deployment distribution. A speaker recommended character error rate, table structure, equations and language-specific grammar as possible OCR rewards, alongside synthetic documents; exact reward weights and document selection were not supplied. Such component measures need downstream task checks as well. [cite:T72nqdC92PM:c07] [cite:RQi7x-navxU:c05]

## Preserve source errors; measure extraction coverage

If the objective is faithful transcription, correct a recognition mistake without silently correcting the source itself. For example, a source table may contain an arithmetically wrong total. A model that recalculates it may produce a plausible number but an unfaithful transcription. Preserve the printed value, then surface any suspected arithmetic issue separately for review. A proposed correction layer for OCR errors was not independently measured; translation or transliteration are distinct objectives. [cite:0I07YAuF8xA:c03] [cite:T72nqdC92PM:c08]

For structured rows, measure **precision** as correctly emitted rows divided by emitted rows, and **recall** as correctly recovered expected rows divided by expected rows, using a defined matching rule and reference set. High precision can coexist with low recall when an extractor outputs only a few easy rows and silently drops the rest. Inspect missed rows and their importance, not just the correctness of returned rows. The reported model and harness comparison lacks detailed numbers. [cite:0I07YAuF8xA:c08]

## Test contract invariance and policy controls

When a complete gold answer is expensive, metamorphic tests compare outputs under changes that should preserve a particular rule. Reorder independent clauses, rerun the same contract, or change a supplier name or address only where that field genuinely has no bearing on the rule. Unexpected flag changes reveal instability. Passing such tests establishes neither complete coverage nor legal correctness: the same wrong answer can be consistent across variants. [cite:c_SPW__jF9w:c07]

Policy advice needs a separate control test. Define the approved policy, construct cases where an answer could conflict with it, and check the advice a customer would actually receive. Add a policy check or escalation where appropriate, then rerun those cases through the full path to see whether the control intercepts the error. A speaker-retold airline incident involving alleged incorrect post-purchase discount advice motivated such a proposal; the legal account was not independently checked and the proposed controls were counterfactual, not demonstrated prevention. [cite:mMw3arwQsL0:c10]

A related exploratory proposal compares a user’s privacy preferences with contract terms through concrete scenarios, surfacing possible conflicts. This can inform review, but a generated conflict is not a legal determination and does not give the user power to negotiate the terms. [cite:hOWU0KPUp1k:c06]