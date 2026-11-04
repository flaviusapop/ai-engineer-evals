A retrieval system must do more than find plausible text. It must make the right evidence available, preserve where each assertion came from, and distinguish search results from complete, current records. These are different responsibilities: an auditable citation or deterministic query does not by itself prove that a source or answer is correct.

## Prepare and maintain candidate indexes

Different signals call for different indexes. An illustrative video corpus might maintain an inverted topic index, a graph of entities and a vector index for visual similarity. Offline processing extracts and clusters content; refresh jobs update those representations as the corpus changes. Online, query metadata chooses candidate types, quality filters remove obvious spam, and a ranking stage selects what to inspect. This is an architecture example, not evidence for a particular refresh interval or performance gain. For how lexical and semantic result lists are combined, see [[retrieval-and-query-optimization]]. [cite:jNE8No-wvok:c04]

Bind an embedding model and its configuration to the indexed field so document ingestion and query embedding use the same model rather than relying on every caller to remember it. A change of model needs a coordinated index migration; the cited guidance does not establish a method for aligning different models or require inference inside the database. [cite:ksjwtQop4os:c03]

Static routing selects a predefined search template for a query. It is not the same as a feedback system that changes weights or filters based on clicks, ratings and business outcomes. One workshop described the latter as a possible future capability and explicitly said it had not been released. [cite:ksjwtQop4os:c10]

## Select evidence and make it inspectable

If the answer model sees only a few chunks, evaluate the actual window it receives: the relevant passage at rank 20 cannot help if only three are passed through. Adding many plausible but conflicting passages can also make selection harder. An alternative proposal stages titles and snippets in a workspace and lets an agent open selected documents; it is not an independently validated optimal context strategy. [cite:ksjwtQop4os:c15] [cite:fZH97QHHYjY:c08]

Pass source URLs and document metadata with retrieved text rather than asking the generator to invent links. For numerical work, a stronger design registers stable fact identities and preserves the source, transformation and displayed value separately. A number displayed in thousands can then be traced back to its underlying fact and calculation. One financial platform reports such a registry and clickable calculations; its repeatability and universal clickability are speaker-reported, not independently tested. A basic URL-bearing demonstration is a different, weaker mechanism. Neither verifies that the cited passage entails the claim or that the source itself is true. [cite:ksjwtQop4os:c12] [cite:dZgA6btnb_s:c04]

When a number cannot be matched to a registered fact, remove or abstain from the unsupported claim, or attempt a separately checked repair before accepting it. The cited platform describes selective repair but does not disclose its acceptance criteria or accuracy; it is not evidence that an arbitrary repair is trustworthy. [cite:dZgA6btnb_s:c06]

Relevance is not authority. A filing and an earnings call can disagree about a metric; compare reporting period, definition and restatement before deciding which source answers the question, and expose unresolved conflict. For implemented software behavior, code may outrank stale documentation, while documentation can explain intended behavior. That ranking is task-specific, not a universal rule; a reported code/document integration was still being fixed. [cite:dZgA6btnb_s:c07] [cite:_QAVExf_1uw:c10]

## Navigate documents and query exact state

Search snippets are a starting point, not proof of completeness. For linked rulebooks, provide ordered-section access, a bounded whole-document read and a list of available documents so the agent can follow cross-references or investigate an exhaustive fee request. If a document is too large or a section name invalid, return available sections rather than silently truncating. One deployment used an approximately 100,000-token whole-document limit; that is its guardrail, not a general optimum, and these tools alone do not prove every fee was found. [cite:gonAewBZxfU:c07] [cite:gonAewBZxfU:c08]

Separate volatile state from relatively stable preferences. Refresh inventory before recommending an item whose availability matters; the source does not give a universal freshness window. [cite:AhQpRalYlyg:c03]

For exhaustive structured inventory, let the model interpret the request and let code enumerate records. In the reported example, “hot GPUs in data hall 11” becomes an entity type, a location subtree and a temperature predicate; the backend intersects the matching sets. A naming pattern can similarly be generated and executed against actual identifiers. Sharding a list across model calls had produced both missing and invented equipment. Exact set operations still depend on the correct interpretation, complete inventory and correctly specified “hot” filter; reported zero failures on 66 cases do not establish universal end-to-end reliability. [cite:EUsPvBeIx70:c02] [cite:EUsPvBeIx70:c04] [cite:EUsPvBeIx70:c05] [cite:EUsPvBeIx70:c06] [cite:EUsPvBeIx70:c09]

## Preserve lineage in domain workflows

A provenance chain should connect external and internal documents, extracted facts, derived values and model-directed input/output operations. For example, an *illustrative* business ratio should link both input versions and the calculation to the result, not merely link a public filing. This makes reconstruction possible; it does not certify the inputs or arithmetic. The cited account does not supply a complete ledger schema or retention policy. [cite:Tt2kX2sgQio:c09]

At intake, detect repeat submissions without erasing their individual histories. Delays can cause follow-ups that increase review load and falsely look like independent corroboration; an altered date may instead warrant separate investigation. Duplicate rates in the example are illustrative. [cite:W4pnzOURwHQ:c03]

Research workflows can combine analyst notes, expert-call material and alternative datasets, then surface a shelved thesis when market conditions change. A proposed workbench presents recommendations with exact evidence and saves the human–agent synthesis back into the research corpus. Treat saved synthesis as another reviewable claim, not an authoritative source merely because it is retained. Neither proposal establishes better investment performance. [cite:ZMZlAn6Pyfg:c05] [cite:ZMZlAn6Pyfg:c06] [cite:CLve4Nx_RwI:c10]

Similarly, attach error rates and instrumentation gaps to a software migration target so an agent can address why the migration was undertaken, not just translate syntax. Measure the stated operational goal alongside conversion; the telemetry-enriched migration is a proposed extension, not a demonstrated improvement. [cite:xIt_mTQp6mY:c06]

## Operate trace and document data

Treat traces as governed, text-rich data: define a shared schema and access for audit, operational monitoring, interactive reading and programmatic analysis across frameworks. Text indexing can support searches across spans; choose storage for actual workload and access constraints rather than assuming a custom database is required. The large span sizes described by a vendor are examples, not typical measurements. For interpreting traces, see [[agent-observability-and-diagnosis]]. [cite:ObTPqBGsEbA:c06] [cite:XBaznoTRDFI:c03] [cite:XBaznoTRDFI:c05]

For recurring document work, a specialized pipeline may be appropriate: classify and split mixed packets, parse, retrieve, extract fields and format outputs. Check each stage and the end-to-end result against representative live inputs: a split that hides a page can undermine otherwise accurate extraction. Attach field-level source references and uncertainty flags for review; a confidence score is not necessarily calibrated. The sources offer operational guidance, not quantified improvements. [cite:RQi7x-navxU:c02] [cite:0I07YAuF8xA:c06] [cite:0I07YAuF8xA:c09] [cite:RQi7x-navxU:c08]

Connected dependency data can also support ecosystem review: a demonstration generated an architecture report flagging cycles, migration issues, single points of failure and telemetry gaps. Treat those findings as leads to verify, not an independently validated audit; no precision measurement was given. [cite:k2ClBT4aqAg:c09]
