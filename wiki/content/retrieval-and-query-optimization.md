Optimize retrieval for the question and decision, not for a single impressive search score. Exact identifiers, paraphrased concepts, broad documentary evidence and structured counts have different failure modes. Compare candidate strategies on representative tasks and include the quality and cost of the answer that uses them.

## Combine complementary searches

Lexical search can find an exact error code or function name but miss a synonym; semantic search can find the synonym but confuse similarly described functions. Run both when both failure modes matter. Their raw scores need not share a scale, so adding them directly can give one retriever arbitrary dominance. [cite:dRmWYHuIJxM:c03] [cite:ksjwtQop4os:c06]

Reciprocal rank fusion (RRF) combines ranked positions instead of the original score magnitudes, with a tunable rank constant. This lets the two searches contribute without assuming their raw scores are directly comparable. Alternatively, normalize scores and tune weighted combinations against query–document relevance judgments. This retains score information but depends on the normalization, weights and labels. Tune on the intended query mix; RRF is a starting point, not a universal winner, and automatically generated relevance labels are not automatically trustworthy. [cite:ksjwtQop4os:c06] [cite:ksjwtQop4os:c07]

## Choose query strategy, filters and reranking

Use a natural description for semantic search when the intended meaning is broad, but use a literal pattern or keyword for an exact identifier. Route recognized query types to explicit templates—for instance, a hybrid search or a hybrid search followed by reranking. A real date, location or category constraint can filter the candidate pool before ranking; an inferred but incorrect constraint may exclude the answer. The template architecture is not evidence of continuously learned autotuning. [cite:1IdzkRVmWAA:c02] [cite:ksjwtQop4os:c08] [cite:ksjwtQop4os:c09]

After candidate generation, thresholds decide which weak matches survive. A single fixed cutoff can reject a relevant result for a short or unusual query, while a permissive cutoff sends noise onward. One search tool used a query-sensitive heuristic instead of a slower model judge; its reported timings and quality are setting-specific and its threshold method is not fully specified. Tune against both missed evidence and irrelevant context. [cite:dRmWYHuIJxM:c04]

A reranker can compare candidates more carefully. Pointwise scoring examines each query–candidate pair separately; listwise comparison considers competing candidates together, potentially useful when near-duplicates differ in one decisive detail. Joint comparison costs resources and time, and the cited workshop gives no comparative benchmark proving it is always superior. [cite:ksjwtQop4os:c16]

## Vary evidence granularity

A small passage may answer a focused fact question; a broader question may need context spread across a document. A fixed chunk size selected for average corpus performance can conceal those differences. In one research design the same corpus was indexed at several scales, each query searched all copies, and chunk hits were mapped to shared document identities before their document rankings were fused. This avoids comparing unlike chunk identities, but multiple copies and searches cost storage and work, and whole-document context has its own cost. [cite:r9OwPx_HoV0:c03] [cite:r9OwPx_HoV0:c06] [cite:r9OwPx_HoV0:c07] [cite:r9OwPx_HoV0:c08]

A hindsight oracle that picks the best scale using known answers measures potential headroom, not a deployable selection policy. The reported multi-scale recall gains are benchmark-specific; incomplete protocols and ambiguous percentage definitions prevent a clean universal effect size. Number of scales and fusion choices remain open. For production index lifecycle and provenance, see [[retrieval-evidence-and-provenance]]. [cite:r9OwPx_HoV0:c09] [cite:r9OwPx_HoV0:c11]

## Demand task-level benefit

Compare additions to a simpler baseline on the same representative questions, including exact-detail probes and final answer quality, latency and cost. A tutoring case found that adding filesystem browsing to its hybrid retriever increased latency by roughly half without improving relevant-page recall on its student questions; that does not rule out browsing for tasks with more cross-document dependencies. A separate reported long-context probe found lexical retrieval retained buried exact facts that its dense setup missed, but omitted the details needed to generalize the comparison. [cite:WP3hjUXd918:c08] [cite:WP3hjUXd918:c17]

Define target documents and relevance measures with [[evaluate-and-represent-retrieval-corpora]]; retrieval recall is not itself proof of a correct final answer. A narrow adaptation can be tested too, but a reported German legal retrieval improvement lacks the metric and protocol needed to transfer its numerical claim. [cite:g4SsanB0gMc:c10]

## Select useful memories and executable resources

Semantic similarity alone does not mean a prior memory helps. Consider ranking candidate memories by both task relevance and observed usefulness, while recognizing that credit assignment can be noisy and new memories lack outcome history. In a reported 68-question experiment, a ranked decision ledger outperformed a policy that first gated whether to recall; exact scores, ranking and uncertainty were not supplied. Compare these choices on outcomes and cost rather than assuming either policy always wins. When all evidence already fits in context, retrieval may add overhead without benefit; availability of the right memory does not ensure the model uses it correctly. [cite:Jx4ZFEAq6bY:c02] [cite:R3-anFK1YM8:c06]

Use structured queries, rather than vector similarity alone, for counts, relationships and time constraints. An *illustrative* request for “my merged pull requests last week” requires a caller identity, a time window and an executable filter; discover relevant fields and types, resolve names to system IDs and validate the query under the caller's permissions. Sampling a schemaless database can miss uncommon shapes, and unresolved identity ambiguity should not silently become a guess. A bounded retry can repair an execution error, but a syntactically valid query may still answer the wrong question. [cite:ORVh4GivEU0:c03] [cite:ORVh4GivEU0:c04] [cite:ORVh4GivEU0:c05] [cite:ORVh4GivEU0:c06] [cite:ORVh4GivEU0:c09]

Large tool catalogs present a separate selection problem: retrieve a small shortlist from tool descriptions before presenting schemas to the agent, then test whether the needed tool remains available. A synthetic travel demonstration used 90 queries, 29 tools and a top-three shortlist; it does not establish production accuracy or a reproducible improvement. [cite:vJukHCIv7Ck:c02]
