A successful AI system is not defined by selecting a model or producing an impressive demo. Define the work that needs to improve, who experiences the pain and what an acceptable outcome looks like; only then decide which measurements can tell you whether a proposed solution helps.

## Frame the problem without prescribing the solution

Describe the user, current process, measurable pain and desired outcome in terms that would still make sense if no agent were built. For example, an illustrative insurance-claims problem is that reviewers take too long to process claims, delaying care. The objective might be a shorter decision cycle while retaining required human review and respecting data and model restrictions. These are hypothetical design conditions, not measured results. [cite:T0HhO4YtTfE:c01]

Turn the problem into a specification before selecting models: which cases should be handled, what counts as a correct resolution, which errors or actions are unacceptable, and what operating constraints must hold? For support, the share of eligible simple queries resolved without a human can be a target, but deflection alone is not success if answers are wrong or customers need to return. An enterprise banking case describes setting handling and accuracy targets before model selection; its targets should not be read as achieved outcomes. [cite:ObTPqBGsEbA:c01]

Agree on the criteria with domain, customer-facing, product and technical stakeholders. Data scientists' statistical expertise is valuable alongside operational knowledge; neither a model team alone nor a product aspiration replaces both. This is organizational guidance, not evidence that a particular staffing pattern causes better outcomes. [cite:NKwIX3CiRgU:c01] [cite:NKwIX3CiRgU:c10]

## Choose metrics for the actual decision

Name the thing each metric measures, its denominator, and the action it should inform. For the claims example, elapsed time from receipt to reviewed decision addresses the delay; a separately assessed decision-quality measure addresses whether the recommendation was usable. Reviewer override rate and review duration can flag investigation: long reviews might indicate confusing output, but that explanation is a hypothesis, and an override is not automatically a model error. These are workflow proxies, not accuracy itself. [cite:T0HhO4YtTfE:c08]

Activity is especially easy to mistake for value. One demonstration found an agent run was reportedly 28% cheaper even though it still did not use the tool the experiment intended to assess; the speaker said cost variance needed investigation, so the number is not an established causal saving. Similarly, cursor movement is not a universal measure of useful information work: the proposed “mousepower” device was a metaphor ultimately rejected as a metric. [cite:A3FL_zTQKU0:c01] [cite:8KkibGU_DDY:c06]

Choose technical metrics at the layer where they answer a real question. Precision, recall and F1 can help assess a judge against human labels, but they do not alone describe whether an agent completes the user's job. For image generation, a generic image score may not measure the text-rendering capability the product needs; the cited presentation describes larger separation on text-specific measures but supplies no uncertainty or proof of construct validity. Use complementary measures and understand what each omits. Human inspection also depends on who rates and which examples they see. [cite:NKwIX3CiRgU:c04] [cite:NKwIX3CiRgU:c05] [cite:hqHC6Z_lXyo:c05] [cite:hqHC6Z_lXyo:c04]

## Separate useful progress from complete delivery

A partial-credit score summarizes the fraction of criteria satisfied; a fully correct rate asks how often the *entire* deliverable meets every requirement. These are different estimands, not alternative names for the same quality number. A draft with most criteria satisfied may save a reviewer time, while the same result may be unacceptable for unreviewed client delivery. Report both if both uses matter, and measure the human correction burden for the draft workflow. There is no universal conversion from average partial credit to whole-task success. [cite:rWtbOgl5FTU:c04]

## Measure policy choices, not recognition alone

Even if the underlying recognition hypotheses do not change, an assistant can act, reject or ask for confirmation. These choices change the errors and recovery effort experienced by users. In a speaker's illustrative music-assistant scenario, wrong playback takes effort to notice, interrupt and retry; rejection also delays a user, including one whose original hypothesis was correct. Confirmation has two distinct branches: a correct suggestion may receive a quick yes, while an incorrect one requires correction. [cite:Zd5b40Jbp_k:c01] [cite:Zd5b40Jbp_k:c03] [cite:Zd5b40Jbp_k:c05]

Compare policies using observed action outcomes and context-appropriate costs, including the burden of unnecessary confirmation as well as prevented mistakes. A simple low-confidence reject, middle-confidence confirm and high-confidence act policy can clarify the choice, but two thresholds are not a required architecture. It assumes useful calibration of confidence; the source's recovery times are illustrative, and lower estimated recovery cost is not a measured improvement in user satisfaction.

## Keep authority and outcome separate

An agent may obey every restriction and still fail its assigned job; it may also produce a useful-looking answer by taking an unauthorized action. Track authorized behavior and role success as separate dimensions rather than averaging them into a single correctness label. In an illustrative invoice workflow, a ceiling on approvals is an authority constraint; correct purchase-order matching and timely reconciliation describe the work. A conceptual scorecard can check clear rules and separately judge whether the intended outcome was achieved, without implying that the proposed governance framework has demonstrated effectiveness. [cite:h8jgniNJcbQ:c07] [cite:h8jgniNJcbQ:c08]

## Explain results in the customer's terms

Compare outcomes against a familiar baseline, such as the existing human review process, with the same task boundaries and required quality. A token count can explain a cost component but not by itself whether the work was worth doing. Early adopters who enjoy experimenting may tolerate workflows that ordinary customers cannot use; involve the intended population rather than treating builder enthusiasm as customer value. The familiar-baseline analogy is a communication aid, not a validated universal efficiency metric. [cite:8KkibGU_DDY:c02] [cite:8KkibGU_DDY:c03]

Once criteria are explicit, [[design-evaluation-distributions-for-decisions]] helps determine which cases and populations the measurements must cover; [[agent-contracts-completion-and-oversight]] develops the adjacent authority and oversight design.
