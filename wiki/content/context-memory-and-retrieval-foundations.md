An agent needs more than general language ability: it needs the facts, constraints and relationships relevant to the work in front of it. **Context** is what the model sees on a particular call; **retrieval** finds potentially useful information; **memory** includes policies for writing, managing and bringing information back over time. A connected database is not the same thing as useful context.

## Begin with the decision and the evidence

Knowledge work turns information into a decision or finding. A legal research workflow, for example, may require a different organization of sources and intermediate work from a coding task. Design around the actual question and how its answer will be used, rather than assuming one search pattern suits every domain. Tools and work organization can evolve together; that is a design proposal, not evidence of a universal architecture. [cite:O84lhGc1OOI:c01] [cite:O84lhGc1OOI:c03]

Before writing a query, state what evidence would resolve the question. If the question concerns a thirty-day rule, identify whether the relevant evidence is a deadline, grace period or retention requirement: the same phrase can describe different concepts. Then choose queries for the needed evidence rather than guessing overlapping words. This ambiguity is not unique to noncoding work, nor is code always unambiguous. [cite:1IdzkRVmWAA:c07] [cite:O84lhGc1OOI:c02]

A capable model may still lack an organization's current rules, relationships and expectations. Connecting a search tool does not fix a missing, stale or contradictory knowledge base. Identify and maintain authoritative, task-useful information as well as the route to it. [cite:GgLQ02aO-hs:c11] [cite:_QAVExf_1uw:c01]

## Choose how to find and represent information

Lexical search matches words or identifiers; it can be useful for exact product IDs or named symbols. Semantic search can match related meaning despite different wording. Neither mechanism always wins: test both identifier-heavy and paraphrased questions. One workshop favors combining lexical and semantic search, while acknowledging that either alone may suffice and that others prefer starting lexical-first. Choose the simplest approach that meets the task's needs rather than adopting a universal ordering. [cite:ksjwtQop4os:c04] [cite:ksjwtQop4os:c11]

The size of the pieces indexed matters too. A small chunk can preserve a local detail but omit the context that explains it; a large chunk can carry that context while diluting the detail in its representation. Test granularity against different questions. An agent that searches iteratively still pays for poorly organized, widely dispersed evidence. For deeper design choices see [[retrieval-and-query-optimization]] and [[evaluate-and-represent-retrieval-corpora]]. [cite:r9OwPx_HoV0:c02] [cite:r9OwPx_HoV0:c01]

A domain map or typed knowledge graph offers a different representation: resolve aliases to a canonical entity and record relationships among people, systems or processes. This can make navigation and disambiguation explicit, but the proposed healthcare architecture did not establish entity-resolution accuracy or a general advantage over vector retrieval. [cite:XPj3mIKEtI4:c01]

Do not confuse retrieved examples with a complete population. To answer a count or mean over all records, a handful of top-ranked chunks is not a reliable denominator. If a suitable structured dataset exists, execute an aggregate or relationship query over the intended population, and verify both the data and query. A travel demonstration compared this approach with a simple top-k vector workflow; it was not a comparison against every retrieval architecture. [cite:vJukHCIv7Ck:c04]

## Keep the meaning, not just the flag

State should retain qualifications that change behavior. Approving a research plan while restricting it to the US and excluding California is not equivalent to a bare approval flag. Similarly, a preference for Celsius generally but Fahrenheit while cooking has a condition that a single global unit value loses. These are conceptual examples, not evidence that an unstructured memory architecture has been validated; structured fields can preserve conditions too. [cite:3_gYbhABcAE:c02] [cite:3_gYbhABcAE:c03]

## Select context and manage memory over time

A model's window is a capacity limit, not a promise that everything within it will be used. Select and rank the instructions, history and evidence relevant to the current decision. Compression can discard detail; preserving every token can also impose cost or obscure what matters. A speaker-reported study found distinctive facts easier to recover than ambiguous ones, but its incomplete follow-up protocol does not establish general long-context competence. Its recommendation against compaction by default also coexisted with an announced 30,000-token compaction policy without an explained reconciliation: the number is not a universal threshold. [cite:esY99nYXxR4:c01] [cite:WP3hjUXd918:c14] [cite:WP3hjUXd918:c18]

Memory is a **write–manage–read** loop: decide what to save, maintain or revise it, and retrieve it when useful. Distinguish what is always visible in the current session from a recall block and a persistent archive across sessions. A stored item that is never selected does not help the next decision, and an old item may need correction. The layered arrangement is an organizing model, not proof that a particular backend is best. [cite:R3-anFK1YM8:c01] [cite:R3-anFK1YM8:c02] [cite:WP3hjUXd918:c01]

To test whether these choices work, including delayed recall and whether retrieved evidence is actually used, continue to [[evaluate-retrieval-memory-and-learning-in-agent-loops]]. For operational context and persistence decisions, see [[reliable-agent-context-and-memory]] and [[context-and-retrieval]].
