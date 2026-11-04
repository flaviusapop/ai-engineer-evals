A successful query, a reconciled total, or a large dataset can still answer the wrong question. Interpret a measurement by tracing what was observed, how it was transformed, and which decision the result is meant to support.

## Protect business and label semantics

Before changing a transformation, state what one row represents and which business predicates define the metric. Then trace downstream consumers: changing a customer-month table to customer-week can repeat a monthly revenue value across weeks, so a downstream sum may inflate revenue even though the SQL runs. Removing a paid-customer filter may similarly turn paid churn into a metric that includes trials. These are illustrative failure modes, not measured incident rates; map lineage and check consumer assumptions before the change, rather than waiting for a successful build. [cite:KhRjivBSwiw:c01] [cite:KhRjivBSwiw:c04] [cite:KhRjivBSwiw:c05]

The same rule applies to test and training transformations. Gross profit and gross sales are not interchangeable paraphrases, and a horizontal flip of a directional traffic sign or a color change to a traffic light may change the label. Whether a transformation preserves meaning depends on the task and domain, not on its mechanical validity. Consult domain owners about the permissible variations; executable checks alone do not establish the intended semantics. See [[tests-oracles-and-verifier-validity]] for executable verification. [cite:UQKg0td-Bf4:c06] [cite:dKcTBQzR7jI:c06]

## Model the decision, not just the field

A useful conceptual framing distinguishes four things: what the source can observe, what storage preserves, what the decision needs, and what the model assumes. Billing may mean the payer by “customer,” while support means the caller; one universal entity definition can erase a distinction relevant to either decision. This four-part schema is a proposal for reasoning, not a validated taxonomy. Explicitly record the decision and entity definition before mapping fields. [cite:Fa3hQVIKShw:c01] [cite:Fa3hQVIKShw:c02]

A financial numeral also needs a type: value, unit, magnitude scale, reporting period and document location. A prior-year revenue figure in a later filing is not automatically revenue for the filing year, and a table-wide billions annotation can sit far from the number. Preserve those associations before comparing or calculating. [cite:dZgA6btnb_s:c02]

Reconciliation is necessary but not sufficient. In one speaker-reported debugging case, row counts and dollar totals matched while date parsing left nearly all dates empty. Other cases involved missed categories or changed signs. Check missingness by field, category coverage, sign conventions and representative source-to-output records as well as aggregates. Those cases illustrate a mechanism, not an estimated error rate. [cite:Fa3hQVIKShw:c08]

A zero result has a boundary too. A demonstrated query found no hotels listed in its Antarctica database; that supports “none listed in this database,” not “none exist anywhere.” State the dataset, query scope and any known completeness limits when reporting absence. [cite:vJukHCIv7Ck:c05]

## Ask what the measurement channel can see

In cell modeling, DNA, RNA expression, proteins and morphology or spatial measurements describe different aspects of biology. RNA sequencing is relatively scalable; protein measurements can be closer to functional activity but are described as lower throughput. Abundance makes a modality convenient, not sufficient for every biological question. Improving measurement fidelity alongside scale is a research direction, not a demonstrated out-of-distribution guarantee or a quantified cross-modality ranking. [cite:-561cZmir5Q:c02] [cite:-561cZmir5Q:c09]

A single-cell profile is also a snapshot of a changing system: cell cycle and bursts of expression can create genuine differences. Labs and instruments add technical variation. Record time, preparation, laboratory and instrument context where available, and consider both explanations before treating all variation as error or all of it as biology. The cited account does not supply a method for partitioning or correcting those effects. [cite:-561cZmir5Q:c03] [cite:-561cZmir5Q:c04]

## Specify the workload, not only its name

A serving benchmark needs its request-generation protocol. Record sampling and truncation, input and output length distributions, termination behavior, cache reuse and multi-turn structure. Specify whether requests arrive at a constant rate, via a stated stochastic process, or under a constant concurrency target, and verify the actual schedule. Two harnesses in a reported experiment produced different input-token workloads from the same named dataset because of sampling and truncation. A shared catalog can make scenarios reproducible, but does not by itself prove they represent a deployment. [cite:l1-D89bAuOA:c05] [cite:l1-D89bAuOA:c07] [cite:l1-D89bAuOA:c08] [cite:l1-D89bAuOA:c09]

Channels matter outside serving too. One speaker reported word error rates of 11.4% for a headset-oriented speech benchmark and 26% for the same model on a central room microphone, with different distance and speaker conditions. Full replication details were not supplied. Compare channel and recording conditions before attributing a score difference to the model. [cite:mFLlVpnGpds:c07]
