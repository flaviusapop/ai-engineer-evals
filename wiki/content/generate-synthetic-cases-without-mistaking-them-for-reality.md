Synthetic cases let a team exercise a behavior before real examples are available, or target rare failures that ordinary samples may miss. They answer a coverage question: “Does the system handle these constructed conditions?” They do not by themselves answer how often those conditions occur, or how well the system will perform on real users.

## Start from failures and a specification

List the behavior being tested, plausible failure modes, and the evidence needed for the expected answer. Author or generate cases across those conditions, then have a reviewer check that each case actually supports its intended label. A small diverse financial-query workshop set illustrates a useful starting point, not a representative sample of financial users. When allowed, supplement imagined cases with real-world evidence and revise the suite as usage reveals surprises. [cite:qZj7sqmidqA:c07] [cite:vljxQZfJ9wY:c07]

Retention constraints can make synthetic cases particularly useful, but they are not a blanket privacy or legal guarantee. One healthcare team described contractual restrictions on retaining real records and derivatives while clinicians contributed production-inspired ideas; the permitted boundary was not resolved in the account. Establish the applicable permissions rather than assuming synthetic output makes any source use permissible. [cite:XAsb7MIAzm8:c01] [cite:XAsb7MIAzm8:c10]

## Build a staged recipe instead of one giant prompt

Record seeds, generation settings, dependencies and checks so a case can be traced and regenerated. Preview a small batch before scaling; inspect variety and whether later fields actually follow earlier choices. For long records, fix invariants first, generate a chronological history, plan encounters, then produce individual documents with relevant prior context. Parallel document generation can introduce contradictions, so check dates, identity and clinical facts across documents rather than assuming that shared prompts guarantee consistency. This is a reported generation design, not a measured guarantee of realistic clinical records. [cite:qFaKvbVc5cE:c01] [cite:qFaKvbVc5cE:c03] [cite:XAsb7MIAzm8:c06] [cite:XAsb7MIAzm8:c08]

Another recipe walks a knowledge graph to make multi-hop search riddles: select a seed, follow a bounded sequence of relations, and formulate a question whose answer depends on the path. Longer walks can drift away from a useful subject; the source gives inconsistent hop ranges, not an established optimum. Validate the relations and answerability rather than treating path length as difficulty proof. [cite:qFaKvbVc5cE:c06]

## Construct cases backward from a check

**Illustrative example:** suppose an invented return policy accepts an unused item within 30 days and rejects it after that period. Select the intended path first: an unused item returned on day 29 should be accepted; an otherwise similar day-31 case should be rejected. Generate the surrounding customer messages and order records, then independently check that their dates, item condition and intended outcome agree. Vary templates so the answer cannot be inferred from a repeated phrase. This tests only the invented rule, not every real return-policy exception.

The same principle supports richer policy paths: a healthcare team described sampling approval and rejection reasoning paths before generating supporting records. Uniformly sampling paths can deliberately emphasize rare branches, but the resulting pass rate is not a deployment-average accuracy estimate. A contract-review practitioner described planting known problems and combining template values into code-gradable tests; their stated shorter feedback cycle was a practitioner account, not evidence of production readiness, and the source's wording about initial clause compliance is inconsistent. [cite:XAsb7MIAzm8:c03] [cite:XAsb7MIAzm8:c04] [cite:c_SPW__jF9w:c05] [cite:c_SPW__jF9w:c08]

Mechanically verifiable tasks are useful where requirements can be stated precisely. A proposed poem task, for example, checks word count and the presence of a chosen word; passing says nothing by itself about poetic quality. Varying constraints creates more cases, not proof that shortcuts or contamination are impossible. [cite:uIiA6DquRiE:c11]

## Expand failures without changing their meaning

From a known failure, generate neighbors that vary delivery while retaining the intent and expected decision: for a voice booking request, change speaking speed or background noise, but verify the request remains intelligible and means the same thing. Domain substitutions must also preserve meaning: gross profit and gross sales are not interchangeable just because both are financial terms. Ask experts to review questionable variants and feed identified mistakes back into the generator. Proposed voice and adversarial variations were not accompanied by a simulation-validity study or measured adversarial success rate. [cite:qStB9GbppMU:c07] [cite:UQKg0td-Bf4:c05] [cite:NdrSPm6NCdk:c17] [cite:c_SPW__jF9w:c11]

## Validate examples and labels in layers

Check structure and invariants first, then test whether the content supports the label. Round-trip the generated record through an independent rule implementation where possible, review disagreements, and use domain experts to inspect a sample and hard cases. A separate model can help find issues, but may share the generator's errors; a cheap local model's label is a hypothesis, not ground truth. One financial data pipeline combined programmatic checks, an independent agent and human review; the account does not provide reviewer agreement, rejection rates or an independent audit of final labels. [cite:TyPpSRXGhbc:c02] [cite:A48uhxfxbsM:c03] [cite:XAsb7MIAzm8:c08] [cite:g4SsanB0gMc:c09]

For retrieval training, another proposed backward construction generates questions and answers from documents, checks answerability using other grounded models, then removes the initial retrieval support so the learner must find the evidence. Checking the easy, grounded version helps construct supervision; it does not independently prove the resulting harder task or every label is valid. [cite:AQv3qRCG6Gw:c05]

For training data, budget for a funnel: generate more candidates than needed, filter invalid or unhelpful examples, record generated and retained counts, and evaluate the trained model on separate relevant evidence. A speaker reported 50,000 seeds yielding roughly 7,000 retained records and a search-benchmark change from zero to 30% after training. The model setup, baseline protocol and ablations were not supplied, so the report neither isolates the cause nor proves transfer to production. [cite:qFaKvbVc5cE:c08]

## Ground personas without claiming new human evidence

If personas are meant to resemble a population, use aggregate data and conditional relationships rather than sampling every attribute independently. For example, an age–income joint distribution can keep combinations in plausible proportions where the source data supports them. This does not establish individual realism, predictive validity or a formal privacy guarantee; the proposed method did not report distribution-fit or disclosure-risk measurements. [cite:qFaKvbVc5cE:c13]

Repeatedly asking an unchanged synthetic persona the same question can estimate that model's response distribution more precisely, but it creates no new independent human observations. A tighter Monte Carlo estimate is not evidence that the model predicts the population more accurately. This caution concerns reruns without new real-world input, not every kind of data augmentation. [cite:YnNF55QV0zs:c09]

For ongoing use, connect synthetic stress tests with [[build-and-maintain-production-grounded-evaluation-sets|permitted production-grounded evidence]]; keep the two purposes and their limitations visible when reporting results.
