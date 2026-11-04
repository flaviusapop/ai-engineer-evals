A financial memo is reviewable when an analyst can trace material claims to appropriate evidence, reproduce the calculations and see what could change the conclusion. Fluent prose and abundant citations are not enough. The standard applies to the work supporting a decision, not a promise that the decision will make money.

## Verify what the source actually supports

For each important figure, open the underlying source and check the entity, reporting period, metric, units and extraction. An audited filing and an informal estimate do not have the same evidential status, although even an authoritative filing can be wrong or unsuitable for the question. One reviewer described a tool preferring an informal guess over an available audited figure; the anonymized anecdote does not establish why retrieval ranked it that way. A model's remembered number may be correct, but memory alone does not provide an auditable source trail. [cite:tJFjeMBKbIY:c02] [cite:Tt2kX2sgQio:c02] [cite:dZgA6btnb_s:c09]

Check the time window and the sources actually used, not just the number retrieved. In one investing demonstration, an answer used one or two of fifteen candidates; a date-filtered answer used seven of fifty-two. The latter count proves neither consensus nor correctness. A months-old note may be stale for a fast-changing market question but useful for another question; set freshness from the decision, not a universal age limit. [cite:CLve4Nx_RwI:c02] [cite:CLve4Nx_RwI:c03]

## Reconstruct the financial perimeter and the workbook

A matching number can describe the wrong company or period. Before comparing figures, identify acquisitions, divestitures and partial-year contributions. In an illustrative benchmark case, the task was to reconstruct Sonoco as of May 2025 with a full year of Eviosys and without TFP. Different reported sales can reflect different perimeters rather than simple arithmetic error. This example is a benchmark design, not independently verified investment advice. [cite:aVbRSIQO2dE:c09]

For spreadsheets, distinguish gross from net, company from segment, quarter from year, and inputs from formulas. A tabular range helps inspect cells, a structural view exposes formulas and relationships, and a rendered sheet can reveal layout and headings. One practitioner found no single representation adequate; that is qualitative experience, not a quantified comparison. Combining views helps select the right figure but does not establish that the underlying figure is true. [cite:HEFSExa0xl0:c01] [cite:HEFSExa0xl0:c03]

## Make derivations reproducible and check independent controls

Separate selecting evidence and explaining it from calculating with it. A proposed architecture lets a model refer to a canonical numeric value while a computation layer preserves the payload and executes the calculation. Record each input's source and the rules and adjustments used, so a reviewer can replay, for example, a firm-specific margin or leverage calculation. Deterministic code makes the operation repeatable, not necessarily correct: parsers, chosen inputs, accounting rules and the generated explanation can all fail. The vendor's implementation was not independently audited. [cite:Tt2kX2sgQio:c04] [cite:Tt2kX2sgQio:c07] [cite:-a2oTS9J67U:c08]

Use an independently sourced control where available. A reported statement-extraction case checked each month's records against printed balances, then reconciled individual dates, descriptions and notes. The year reportedly balanced to the penny and 56 differences were reconciled, but this is one case, not an estimated error rate. A balanced total can hide offsetting mistakes; check the transaction details too. Similarly, comparison to a system of record can catch mismatches without proving that OCR, the record or the checker covers every relevant field. [cite:dYh7TQkuYFE:c03] [cite:5xi_S1f9sDU:c10]

## Preserve disagreements and uncertainty

Repeated figures should agree where they refer to the same definition and period; investigate differences rather than blindly demanding identical strings where rounding or scope differs. More importantly, if a filing and an earnings call make conflicting claims, show both with their sources and ask a reviewer to resolve the material difference. A smooth synthesis that silently chooses one can conceal the very issue diligence should expose. [cite:tJFjeMBKbIY:c03] [cite:tJFjeMBKbIY:c04]

Keep an estimate, forecast or disputed claim labeled through subsequent drafts and slides. A practitioner describes an expected approval becoming a received approval after successive rewrites: the failure is a change in evidential status, not merely an awkward sentence. Test the final artifact against the original source, not only the first draft. The anecdote does not measure how often this occurs. [cite:tJFjeMBKbIY:c05]

## Evaluate the whole decision, not only a plausible answer

Define the assignment from mandate to deliverable. A benchmark example asks for a fund's strategy and holding period, then an evidence-backed long, short or pass memo. Inspect the material sources, historical comparators, calculations, judgment and evidence that could overturn the thesis. Ask experts to review the work against the mandate; several conclusions can be defensible without treating every factual claim as correct. Agreement with a firm's process does not prove a profitable trade. [cite:aVbRSIQO2dE:c08] [cite:aVbRSIQO2dE:c12] [cite:Tt2kX2sgQio:c03] [cite:YvQ4BVTWfHI:c02]

Stress a material assumption and examine the reasoning, not just whether the label changes. In the benchmark's acquisition example, the reviewer asks what happens if projected savings are zero: does the memo explain the effect on the recommendation? This is a sensitivity test, not evidence that either recommendation will succeed. For generated model documentation, historical comparisons and working-quant ratings can assess the artifact; they do not constitute auditor or regulatory approval. [cite:aVbRSIQO2dE:c11] [cite:7T-gldvgfpo:c12]

## Define the forecast before judging it

Answering questions about debt or liquidity is different from predicting a future credit path. Distress can lead to bankruptcy, liability management, an exchange or restructuring; a binary default label may miss the decision-relevant outcome. Define a forecast date, horizon and an operationally clear set of outcomes before scoring probabilities against resolved cases. The cited exploratory case did not supply a mutually exclusive taxonomy, horizon, scoring rule or validated outcome. A critique that static scores can miss changing circumstances is a qualitative argument, not proof that such scores are obsolete. [cite:WOszaC1WWbQ:c01] [cite:WOszaC1WWbQ:c02] [cite:WOszaC1WWbQ:c03]

While the future is unresolved, check layers separately: was EBITDA extracted correctly, was leverage derived using the intended debt and adjustment definitions, and is the distress judgment defensible? The example is not a complete leverage specification. Model forecasts may converge and still be wrong; a market-price analogy does not turn agreement into a validated price, calibrated prediction or investment return. [cite:WOszaC1WWbQ:c04] [cite:WOszaC1WWbQ:c06] [cite:WOszaC1WWbQ:c09]

## Backtest with information available at the time

For each historical decision date, reconstruct the information actually available then, generate the feature or forecast, and compare it with the existing process on later-resolved outcomes. A proposed acquisition test searches at intervals before the announcement rather than letting today's search reveal the deal. Historical pricing pages or adverse-media reports can be transformed into structured features for a conventional model; test whether those features add value rather than assuming more searches help. [cite:vS2IA9pq0Q4:c04] [cite:vS2IA9pq0Q4:c06] [cite:vS2IA9pq0Q4:c07]

Historical replay may shorten feedback when outcomes take months, but a date-filtered web tool alone cannot remove future knowledge from model weights, internal feeds or other tools. Check snapshot coverage and availability dates, retain out-of-sample holdouts, and follow with live validation. The source proposes this workflow without validated snapshot coverage or out-of-sample performance results; it does not establish investment gains. For the broader integrity of historical tests, see [[protect-holdouts-and-historical-evidence]]. [cite:vS2IA9pq0Q4:c10]
