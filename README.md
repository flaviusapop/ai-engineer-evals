# AI Engineer: six months of evals

**[Browse the public library](https://flaviusapop.github.io/ai-engineer-evals/)** · **[Open the report](https://flaviusapop.github.io/ai-engineer-evals/report.html#collection)** · [Download everything](collection.zip)

The report defaults to **newest first**; oldest-first and topic-grouping options work with search and filters. No login or Tailscale is required. See [sources, building and verification](ACCESS.md).



## Coverage and method

- Source: [AI Engineer — Videos](https://www.youtube.com/@aiDotEngineer/videos).
- Upload-date window: **30 April–30 October 2026**, inclusive. Dates refer to YouTube uploads, not conference presentation dates.
- Enumerated **1,419 channel uploads**. The exact-date boundary identifies **788 uploads in the requested window**; title screening covered these plus an older buffer, **840 uploads** in total. Independently reviewed all **744 in-window records** in the publisher’s talk atlas, including full available summaries and chapters, to catch evaluation discussions hidden behind generic titles. Selected full transcripts were then reviewed; this is not a full-transcript search of every channel upload.
- Upload dates use watch-page metadata from the extractor when available. Publisher UTC timestamps are also preserved in videos.json; localized YouTube dates may differ by one day. Conference dates are not used.
- Selected **313 videos**: **190 core evaluation talks** and **123 adjacent talks** (testing, observability, verification, performance or safety evaluation).
- Saved **313 transcripts**; **0 unavailable**. **1 has a flagged caption-language issue**, with the original caption text retained. Summaries are based on the retrieved transcript unless explicitly labeled otherwise.
- Transcripts preserve extracted caption text and can contain speech-recognition errors. Timestamp availability varies by caption source; timestamps are preserved where provided, never reconstructed. Chapter timestamps in video descriptions are not represented as transcript-segment timestamps.
- The Videos tab is the requested source; separately listed Shorts, livestream archives, private/deleted and unlisted videos are outside this inventory. Broad talks with only passing eval mentions may not be discoverable from title/description screening. The screening audit records inclusion and exclusion decisions.


## What the videos collectively teach

**1. Start with observed failures, then build the dataset.** The recurring practical sequence is to inspect real traces, distinguish symptoms from causes, group failures, and write explicit acceptance criteria. A small, representative golden set is more useful than a large collection of generic questions. Include successful cases, negative tests, and consequential edge cases; otherwise a fix can improve the target failure while breaking existing behavior. Domain experts should contribute explanations and corrections, not just labels. Representative videos: [Ship Real Agents](https://www.youtube.com/watch?v=Xfl50508LZM), [How Evals and Prompts Shape Agent Behavior](https://www.youtube.com/watch?v=xyL2Ltkh-SA), and [How to Leverage Domain Expertise](https://www.youtube.com/watch?v=kfSDc2eVLo4).

**2. Evaluate the evaluator before optimizing against it.** Prefer deterministic checks for objectively testable constraints and use semantic judges for questions requiring interpretation. Give judges the evidence their question requires: source-grounded faithfulness is not independent factual correctness, and an agent claiming completion is not proof. Calibrate against expert-labeled, held-out examples, investigate disagreements, and separate outcome completion from partial progress. A polished rubric can still miss important domain errors. Representative videos: [Your LLM Judge Is a Confident Liar](https://www.youtube.com/watch?v=xLxhT2ZI7UM), [Inside 847 Production Clinical AI Notes](https://www.youtube.com/watch?v=yqF6XhzbWBk), and [Ship Real Agents](https://www.youtube.com/watch?v=Xfl50508LZM).

**3. Benchmark the complete agent system, not a model name.** Results depend on tools, harness, environment, state, budgets, and verifier quality. Hold these conditions explicit, inspect trajectories, and distinguish infrastructure failures from capability failures. Fresh tasks and protected grading reduce solution leakage; environment variation tests whether behavior generalizes beyond replayable setups. Repeated trials should measure reliability and uncertainty, not merely whether one attempt eventually succeeds. Representative videos: [The Art & Science of Benchmarking Agents](https://www.youtube.com/watch?v=iNkFlCiij0U), [SWE-rebench](https://www.youtube.com/watch?v=wcUJWP6WpGM), and [Computer Use at the Edge of the Statistical Precipice](https://www.youtube.com/watch?v=CTLa_p6iOiY).

**4. Connect offline tests to a production improvement loop.** Instrument execution, discover recurring failures, turn them into regression cases, compare candidate changes against a baseline, and validate the result after release. Version datasets and judging criteria alongside prompts, skills, and harness changes. Agents can investigate traces and propose repairs, but humans still own what counts as improvement. Optimizing a proxy such as fewer turns can remove useful documentation lookup or approval steps. Representative videos: [Continuously Improving Agents with Langfuse](https://www.youtube.com/watch?v=BOCjybvJYM4), [The Loop Is the Product](https://www.youtube.com/watch?v=7taOQBfjDyE), and [Skill issue: Lessons from skilling up coding agents](https://www.youtube.com/watch?v=vNCY9kXXyDQ).

**5. Measure useful outcomes under domain-specific risk and cost.** Token prices, throughput, and aggregate accuracy are inadequate decision rules. Count acceptable completed work, retries, failed attempts, latency, and review burden. In finance, numerical provenance and replayable calculations matter; in healthcare, missing a dangerous condition may outweigh many ordinary correct responses. Evaluation should therefore reflect the actual workflow and consequences, rather than importing a universal quality score. Representative videos: [The Cheaper AI Model That Costs You More](https://www.youtube.com/watch?v=rWtbOgl5FTU), [How Kepler Built Verifiable AI for Financial Services](https://www.youtube.com/watch?v=Tt2kX2sgQio), and [Shipping AI to a Million Patients Without an A/B Test](https://www.youtube.com/watch?v=McknwOzbmyg).

## Important disagreements and caveats

- **Automation has contested limits.** Several workshops operationalize human-calibrated LLM judges; [Nick Heiner](https://www.youtube.com/watch?v=-npY6XjM8CQ) instead favors professional-human comparisons for nuanced writing. [Thais Castello Branco](https://www.youtube.com/watch?v=lCBf9slCanI) argues that legitimate taste differences should retain their context, not be averaged away. These positions do not establish one universally best grader.
- **Production experimentation is not equally acceptable everywhere.** [The Loop Is the Product](https://www.youtube.com/watch?v=7taOQBfjDyE) emphasizes validating value with users; [Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg) emphasizes simulation and staged clinical evidence before exposure. Simulation can screen changes, but requires validation and does not itself prove real-world safety.
- **Demonstrations and proposals are weaker than validated results.** [Malleable Evals](https://www.youtube.com/watch?v=4VhbYlfC7Gs) presents an unfinished conceptual implementation. The [Ship Real Agents workshop](https://www.youtube.com/watch?v=Xfl50508LZM) uses randomized demonstration annotations, not genuine calibration evidence. Likewise, task-specific vendor results and leaderboard gains should not become general reliability claims.

## Start with these five videos

1. **[Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss](https://www.youtube.com/watch?v=Xfl50508LZM).** Foundation: follow traces through error analysis, evaluator selection, experiments, and regression testing. It supplies the overall workflow; treat its randomized annotation exercise as illustration only.
2. **[How Evals and Prompts Shape Agent Behavior — YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA).** Judge calibration: learn human agreement, explanatory labels, expert audits, and held-out tests. It strengthens the judgment layer before you automate scoring or optimize prompts.
3. **[SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov](https://www.youtube.com/watch?v=wcUJWP6WpGM).** Agent benchmarking: make environments executable, protect against leakage, define retries, and distinguish occasional success from consistent reliability. The concrete coding examples expose general measurement traps.
4. **[Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden](https://www.youtube.com/watch?v=BOCjybvJYM4).** Production flywheel: connect instrumentation, application-specific signals, human review, and maintained datasets. It shows how the earlier offline methods become ongoing operational work.
5. **[Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz](https://www.youtube.com/watch?v=McknwOzbmyg).** Advanced domain evaluation: study hazard-linked scenarios, simulator and judge validation, harm-sensitive objectives, and staged evidence. It tests whether your evaluation approach remains defensible when mistakes have clinical consequences.


## Video-by-video summaries


## Core · Agent benchmarks, simulations & measurement


### 1. Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind

**Uploaded:** 2026-05-25 · [Watch video](https://www.youtube.com/watch?v=Ubwb6NzegyA) · [Read transcript](transcripts/Ubwb6NzegyA.md)

Nicholas Kang and Michael Aaron describe Kaggle efforts to make evaluations current, transparent and accessible beyond AI researchers. They show why model settings and harness choices can change reported results and why domain experts contribute capabilities otherwise absent from benchmarks. Standardized Agent Exams lower setup cost for consumer-agent testing. Game Arena uses strategic games, open trajectories and pairwise ratings to maintain comparative headroom, but statistical significance, inference costs and disappearing models complicate measurement. Community benchmark tools combine assertions and LLM judges, while the speakers repeatedly ask whether a result measures the model, harness or complete configured agent.

- Publish settings and identify the actual system under test.

- Invite domain experts to create benchmarks outside mainstream technical tasks.

- Balance accessible exams and pairwise competition against cost, difficulty and statistical confidence.


### 2. The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI

**Uploaded:** 2026-06-04 · [Watch video](https://www.youtube.com/watch?v=iNkFlCiij0U) · [Read transcript](transcripts/iNkFlCiij0U.md)

Vincent Chen offers a framework for evaluating benchmarks themselves. Scientific requirements include expert-validated tasks, deliberate domain coverage, meaningful difficulty and headroom, and reproducible measurement beyond accuracy. Examples from GPQA, MMLU, ARC-AGI and policy-aware agent tasks show why quality control and task distributions matter. Differentiating benchmarks also have a thesis about future capability, inspire research directions and offer usable interfaces for researchers. Looking ahead, he calls for richer environments, longer autonomy horizons and more complex work products with nuanced reward signals. Open benchmarks are presented as tools for shaping progress, not merely recording leaderboard snapshots.

- Audit task quality, coverage and model headroom before trusting a benchmark.

- Measure policy compliance and operational dimensions alongside completion.

- Researcher usability and an explicit capability thesis influence benchmark adoption.


### 3. The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica

**Uploaded:** 2026-06-28 · [Watch video](https://www.youtube.com/watch?v=vh2VGuQ3zhY) · [Read transcript](transcripts/vh2VGuQ3zhY.md)

Sohail Shaikh and Ankush Rastogi benchmark full-catalog tool loading against semantic routing with just-in-time schema injection. They measure selection accuracy, time to first token, input tokens and estimated cost while holding queries, models, answer keys and catalogs fixed. Benchmark-style tasks and synthetic tool pools expose degradation as catalog size increases; varying the retrieved-tool count shows the recall-versus-efficiency tradeoff. Their recommended implementation logs selected and called tools, reindexes changed descriptions, and widens retrieval on misses. The talk qualifies the approach for larger catalogs rather than recommending additional routing infrastructure for every small agent.

- Hold model, queries and answer key fixed when comparing tool-loading strategies.

- Sweep retrieval size and measure accuracy together with latency and cost.

- Log router misses and rare-tool failures; small catalogs may not need routing.


### 4. Stop Evaluating Models Like It's the 50s - Alejandro Vidal, Mindmakers

**Uploaded:** 2026-07-13 · [Watch video](https://www.youtube.com/watch?v=O3FEoMYvUf8) · [Read transcript](transcripts/O3FEoMYvUf8.md)

Alejandro Vidal introduces item response theory as an alternative to simply counting correct benchmark answers. Calibrating item difficulty and discrimination alongside model ability exposes noisy or negatively discriminating questions and provides likelihood intervals. He demonstrates auditing mislabeled questions, selecting smaller informative test subsets, examining unexpected residuals, and comparing behavior across model groups. Private anchor and organization-specific fingerprint sets are proposed for investigating possible benchmark leakage, with explicit cautions that anomalous answers are not proof of contamination. Residual correlations may also reveal model relationships. Vidal closes by suggesting multidimensional measurement, combined benchmarks, and additional signals, presenting psychometrics as a practical toolbox rather than a universal intelligence score.

- Calibrate item difficulty and discrimination before trusting aggregate rankings.

- Use residuals to prioritize audits, not automatically declare cheating.

- Reduce evaluation cost through informative item selection while checking benchmark-specific limitations.


### 5. Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

**Uploaded:** 2026-07-15 · [Watch video](https://www.youtube.com/watch?v=ZSQb5fzRFPw) · [Read transcript](transcripts/ZSQb5fzRFPw.md)

Francesco Bonacci, Dillon DuPont, and Robert Wendt present Cua’s computer-use stack, with a substantial Cua-Bench evaluation section. Tasks combine initial-state setup, a golden GUI trajectory, and evaluators probing whether the environment actually changed correctly. KiCad tasks use circuit simulation and expose a sharp gap between editing existing schematics and starting from blank ones. The team compares computer-tool interfaces, stress-tests proposed environments with reward-hacking agents before admitting tasks, and forks recorded states to test predictions of world state or reward. Background interaction and pooled sandbox infrastructure round out the talk. The evaluation contribution is executable cross-platform tasks plus scrutiny of the graders themselves.

- Validate environment state, not only action sequences or final screenshots.

- Stress-test evaluators for reward hacking before accepting benchmark tasks.

- Separate creation-from-blank capabilities from editing existing artifacts.


### 6. Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=jRCpXUjz4CI) · [Read transcript](transcripts/jRCpXUjz4CI.md)

Alex Shaw frames agent development as empirical machine learning: environments supply tasks, verifiers supply rewards and feedback, and prompt or harness changes act like optimization steps. Harbor standardizes instructions, sandbox setup, hidden verification, artifacts, and parallel rollouts so different agents and models can be compared on common tasks. The talk demonstrates Terminal-Bench execution and describes evaluation use cases spanning internal coding, product usability, embedded agent features, and operational automation. Shaw also shows map-reduce analysis of coding sessions to extract recurring mistakes and inform new tests. He connects the same rollout infrastructure to supervised training, reinforcement learning, and text-feedback optimization while warning about overfitting and reward hacking.

- Define tasks as executable environments with explicit stopping and verification conditions.

- Use organization-specific evals to make cost-quality choices instead of trusting brands.

- Analyze trajectories to discover recurring mistakes and expand task coverage.


### 7. Vending-Bench: Long-Horizon Agent Evals — Lukas Petersson, Andon Labs

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=cO8qC6HBuBg) · [Read transcript](transcripts/cO8qC6HBuBg.md)

Lukas Petersson explains Vending-Bench as a long-horizon test of whether coding-trained models can generalize to running businesses. Simulated vending agents negotiate, price goods, and compete, revealing unprompted collusion, deception, and other problematic behavior. However, agents can behave differently when they recognize a simulation, while real cafés, stores, and radio stations supply richer evidence but weak reproducibility. Andon Labs therefore experiments with forking live deployments into digital clones, preserving their history while enabling repeated tests across models. Petersson distinguishes anecdotes from controlled comparisons and demonstrates replaying an actual problematic request. The central evaluation challenge is combining real-world validity, low simulation awareness, and repeatable behavioral measurement.

- Check whether simulation awareness changes the behavior being measured.

- Treat real deployment anecdotes as discovery signals, not controlled comparisons.

- Fork realistic live state to make consequential behavioral cases replayable.


### 8. From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI

**Uploaded:** 2026-07-25 · [Watch video](https://www.youtube.com/watch?v=Ib5t2RLtxvM) · [Read transcript](transcripts/Ib5t2RLtxvM.md)

Rustem Feyzkhanov explains how production traces become repeatable agent simulations by reconstructing relevant database state, services, files, tools, and policies. Public benchmarks establish useful priors, but private tasks evaluate the full production system, including cost, latency, retries, and policy adherence. Each task needs an environment, hidden verifiers, and an oracle solution proving solvability. Graders may inspect final world state, artifacts, and trajectories using deterministic checks, model judges, and targeted expert review. Feyzkhanov advocates testing benchmark software itself for missing fixtures, reward hacking, unstable outcomes, and faulty graders. Production failures then expand the suite, connecting observability, controlled experiments, regression gates, and eventual optimization or training.

- Reconstruct production state so configurations face genuinely comparable conditions.

- Validate both positive oracle solutions and negative verifier behavior.

- Continuously feed production failures into a versioned simulation benchmark.


### 9. SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=KMR_RBoCa4M) · [Read transcript](transcripts/KMR_RBoCa4M.md)

Aman Gupta and Shreya Rajpal argue that evaluation-data generation, rather than agent changes alone, bottlenecks customer-support experimentation. Snowglobe runs real agents against simulated users and mocked tools, maintaining consistent identity, account information, and conversational style across multi-turn trajectories. Human-aligned judges score these traces, which feed harness optimization alongside production data. The speakers report twentyfold faster iteration, while Gupta says domain experts judged 80% of simulated data usable. They describe catching regressions before deployment, screening open models, and improving customer satisfaction without sacrificing self-service. Their central caveat is to validate the sim-to-real relationship through offline, online, and human review before relying on simulation to filter production A/B tests.

- Generate complete multi-turn trajectories with state-consistent mocked tools instead of relying solely on hand-authored cases or live-user experiments.

- Calibrate judges against human judgments and compare simulation scores with real production outcomes.

- Use simulations to reject weak harness or model changes before production A/B testing, while retaining real-world validation.

- Track both customer satisfaction and self-service rate so improvements do not hide an operational trade-off.


### 10. Verifiable Environments for AI in Biology — Kenny Workman, LatchBio

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=3ZMUiFaQ3qg) · [Read transcript](transcripts/3ZMUiFaQ3qg.md)

Workman presents biological data analysis as an executable substrate for evaluating scientific agents beyond academic question answering. He describes SpatialBench's initial 146 problems, built around experimental datasets, scientific goals, and deterministic Python graders. Good tasks should require interaction with data and accept valid alternative analysis paths, but scientist attempts exposed ambiguous instructions and arbitrary thresholds, motivating a human-verified subset. Longer workflows approximate paper results or drug-program decisions; their sparse end rewards prompted experiments with intermediate rubrics, whose weak numerical correlation with outcomes leaves the team cautious. He also describes expansion across omics and pharmacology, plus biosecurity evaluations contrasting routine scientific requests with deceptively innocuous harmful ones.

- Require scientific conclusions to depend on the supplied experimental data rather than allowing memorized domain knowledge to answer a benchmark in one turn.

- Design graders around properties that remain valid across legitimate analysis paths, and use scientists' independent attempts to uncover hidden task ambiguity.

- Do not assume intermediate rubric scores are reliable training rewards merely because they appear related to final outcomes; Workman reports limited numerical correlation.

- Evaluate both over-refusal on routine biology work and handling of harmful requests whose surface wording appears benign.


### 11. When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI

**Uploaded:** 2026-08-02 · [Watch video](https://www.youtube.com/watch?v=-npY6XjM8CQ) · [Read transcript](transcripts/-npY6XjM8CQ.md)

Heiner argues that benchmaxxing exploits misalignment between benchmark rewards and real human value, amplified by marketing incentives and costly benchmark construction. He critiques public-test contamination, brittle string matching, contradictory instructions, incomplete verifiers, synthetic-data artifacts, and arena manipulation. His examples illustrate how a score can punish valid solutions, reward loopholes, or improve while human preference deteriorates. He proposes expert-designed, economically relevant tasks with realistic input data, working tools, bidirectional prompt-verifier alignment, thorough quality control, and private holdouts. For nuanced writing assessment, he presents Surge's Hemingway Bench as blind comparisons by professional writers rather than mechanical rules or LLM judges, explicitly accepting higher evaluation costs for stronger human grounding.

- Check that every scored requirement is stated in the prompt and every prompt requirement is actually verified; otherwise rankings mix capability with specification errors.

- Audit contamination and adversarial reward shortcuts, including formatting loopholes and benchmark-aware behavior, before trusting leaderboard improvements.

- Use domain experts, realistic artifacts, reliable tools, and private holdouts to improve construct validity and reduce noise.

- For writing, Heiner advocates blind professional-human comparisons because he considers automated proxies insufficiently faithful to nuanced human taste.


### 12. Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley

**Uploaded:** 2026-08-12 · [Watch video](https://www.youtube.com/watch?v=iqloyWCGYQQ) · [Read transcript](transcripts/iqloyWCGYQQ.md)

Parth Asawa argues that independent, memory-reset benchmark instances measure static capability rather than learning. Continual Learning Bench instead requires headroom for online adaptation, shared latent structure across tasks, and usable feedback. Each system runs both statefully and with state reset; their reward difference defines gain, separating learning benefits from initial model strength. Reward, gain, and cost are compared jointly. Six domains include database exploration with schema drift, forecasting, and strategic play, with expert-validated task sequences. He reports that vanilla in-context learning leads the initial comparisons, while acknowledging medium-horizon limitations. Failure examples distinguish forgetting prior feedback from failing to update beliefs, motivating longer tasks and exploration of models designed for continual learning.

- Require shared task structure and feedback; chaining independent benchmark questions does not establish learning.

- Compare every stateful system with its own stateless baseline to isolate experience-derived gain.

- Report reward, gain, and cost together rather than declaring the highest cumulative reward the best learner.

- Use concept drift and separate stability from plasticity failures when analyzing adaptation over time.


### 13. Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs

**Uploaded:** 2026-08-14 · [Watch video](https://www.youtube.com/watch?v=CTLa_p6iOiY) · [Read transcript](transcripts/CTLa_p6iOiY.md)

Pierluca D'Oro shows how a blind replay agent assembled from successful trajectories can match or beat its source model on deterministic computer-use benchmarks. He argues that pass@k inherits this replayability problem and advocates varied, realistic, sandboxed environments with verifiable configurations. DigiWorld operationalizes these principles through parameterized Android tasks, varied data and interfaces, and a compiler-like validation system; he reports 387 scenarios across fifteen apps and 3.2 million verified configurations. Evaluation must also capture both agent-action randomness and environmental variation. He warns that rollout-only confidence intervals can be severely overconfident, whereas uncertainty estimates respecting the benchmark hierarchy support more trustworthy deployment comparisons and decisions to collect additional evidence.

- Test whether blind successful-action replay can exploit a benchmark before treating its scores as capability evidence.

- Vary task data, appearance, and starting states, and verify that generated combinations remain valid.

- Measure robustness across environmental factors instead of relying only on aggregate success.

- Construct uncertainty estimates that account for environment variation as well as repeated agent rollouts.


### 14. The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph

**Uploaded:** 2026-08-26 · [Watch video](https://www.youtube.com/watch?v=Lrw0jqBNaw0) · [Read transcript](transcripts/Lrw0jqBNaw0.md)

Stephanie Jarmak argues that developer advocacy must include agents as both tool users and product recommenders. Her CodeScaleBench experiment uses hundreds of software-development tasks, comparing agents with and without Sourcegraph tooling and inspecting thousands of traces. Tool failures reveal interface mismatches that consume extra turns, tokens and latency even when agents recover. A separate recommendation study varies prompt intent: explicit product-shopping prompts surfaced Sourcegraph frequently, while realistic descriptions of user pain produced no mentions in the example. She proposes testing content and interface changes against these measured gaps, turning agent advocacy into an experimental feedback loop spanning engineering, product and marketing.

- Compare agents with and without your tool on realistic task suites.

- Inspect recovered tool errors as measurable latency and token costs.

- Test recommendation behavior across pain-driven prompts, not only explicit comparison shopping.


### 15. Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind

**Uploaded:** 2026-09-01 · [Watch video](https://www.youtube.com/watch?v=AhQpRalYlyg) · [Read transcript](transcripts/AhQpRalYlyg.md)

Nidhi Kaushik Vyas presents commerce agents as discovery–research–response loops and specifies evaluators for each stage. Working-state checks measure retained facts, confidence calibration and counterfactual sensitivity: changing a user constraint should change relevant extracted fields without disturbing unrelated ones. Collaborative-strategy evaluations assess blocker discovery, question usefulness and over-asking. User simulators with hidden preferences test whether multimodal elicitation uncovers those preferences efficiently, while turn counts reveal wasteful conversations. Final-response graders assess format selection, data fidelity and actionability. A living-room shopping example connects these measurements to practical decisions, and Vyas argues that automatic raters must evolve as agent capabilities and interaction patterns expand.

- Evaluate intermediate state and questioning strategy, not just the final recommendation.

- Use counterfactual edits to test both sensitivity and invariance of extracted constraints.

- Use hidden-preference simulators and turn-efficiency metrics for conversational discovery.

- Grade response format, factual fidelity and actionability separately.


### 16. How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI

**Uploaded:** 2026-09-09 · [Watch video](https://www.youtube.com/watch?v=XzJD1bvXKjs) · [Read transcript](transcripts/XzJD1bvXKjs.md)

Laurie Voss reruns IFScale, which asks models to include exact words in a business report, first reproducing older models’ instruction-density degradation and then expanding the benchmark after newer models saturated its original range. He reports substantially higher keyword capacity, but identifies distinct failures: omissions, safety refusals, exhausted thinking budgets and polished partial completion. The important caveat is that keyword inclusion is a proxy, not proof that long skills files or conflicting instructions work reliably. He highlights sensitivity to wording and ordering and argues that higher capacity shifts attention toward cost, latency and verification. The recommendation is to revisit old prompt-size assumptions while checking actual outputs.

- Replicate prior results before claiming a capability shift.

- Track refusals, truncation and budget exhaustion separately from omitted constraints.

- Do not equate proxy-benchmark success with reliable reasoning over real instructions.


### 17. Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori

**Uploaded:** 2026-09-10 · [Watch video](https://www.youtube.com/watch?v=8KkibGU_DDY) · [Read transcript](transcripts/8KkibGU_DDY.md)

Maximillian Piras frames agent adoption as a measurement problem: token spending is easy to count, but customers need a legible relationship between cost and useful outcomes. Drawing on horsepower as a communication analogy, he proposes mousepower as an idea, not a universal numerical benchmark. He identifies verification as the bottleneck when generated work grows faster than review capacity. An entropy matrix distinguishes uncertainty in task steps from uncertainty in acceptance criteria. The useful region contains tasks that warrant an agent yet are cheaper to verify than to perform. He argues agent products should supply verification rubrics and outcome-based ROI, potentially using agents to check other agents.

- Trace token costs to completed useful outcomes rather than treating usage as value.

- Choose tasks whose acceptance criteria are clearer than their execution path.

- Design verification alongside the producing agent, not after deployment.


### 18. Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic

**Uploaded:** 2026-09-14 · [Watch video](https://www.youtube.com/watch?v=PXj0p_mW9nI) · [Read transcript](transcripts/PXj0p_mW9nI.md)

Katelyn Lesse and Angela Jiang test whether allocating tokens to advising, grading or reflection improves agents more than execution alone. They compare strategies on financial-analysis tasks, then hold the token budget fixed to separate architectural effects from simply spending more compute. A second analysis changes the acceptance criterion from partial accuracy to completely correct outputs, arguing that an imperfect financial statement may be unusable. This changes the relevant tradeoff to successful-run reliability and resource cost per useful result. They describe rubric-driven graders, advisers and transcript-to-memory reflection as composable roles. The talk’s central lesson is to benchmark strategies against the actual business definition of success.

- Hold compute budgets constant when comparing agent architectures.

- Use acceptance criteria that reflect whether a result is actually usable.

- Compare reliability and cost per successful outcome, not only partial-credit accuracy.


### 19. The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=A_I8mw8yfns) · [Read transcript](transcripts/A_I8mw8yfns.md)

Andrew Dai demonstrates failures in frontier models’ visual reasoning, including counting partial chessboards, interpreting Catan pieces and tracking robot actions across video. He distinguishes quick recognition from tasks requiring sustained spatial or temporal reasoning. The talk critiques benchmarks whose tiny images or text-answerable questions can overstate real-world multimodal capability. Dai argues for evaluations targeting geometric alignment, spatial intelligence and object persistence, rather than treating leaderboard progress as proximity to general intelligence. He then outlines Elorian’s proposed data, architecture and visual-chain-of-thought approach, with robotics, construction and mechanical design as motivating applications. These are capability critiques and development proposals, not a validated universal replacement benchmark.

- Inspect benchmark examples for shortcuts and relevance to actual deployment tasks.

- Test counting, temporal state and geometric constraints separately from visual recognition.

- Use programmatic or simulation-based checks where visual outputs can be validated.


### 20. Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=x4e5O9zN0TE) · [Read transcript](transcripts/x4e5O9zN0TE.md)

Karati uses Supercell’s Project Paradox village agents to explain why long-horizon quality requires controlled experiments rather than impressive short demos. Per-agent memories, emotion vectors, trust scores, and importance caching enable local behavior but fail to preserve provenance, uncertainty, and consistent planning over time. An external autoresearch loop reads full-run traces, scores controlled scenarios, proposes small policy changes, and retains improvements only when guardrails hold. The scorecard balances information diffusion, source retention, uncertainty, planning, and privacy to prevent single-metric gaming. Harnesses, scenarios, and metrics stay frozen while bounded cognitive policies change. The improved mango-rumor example is illustrative; Karati explicitly avoids claiming broad improvement without repeated controlled results.

- Evaluate complete stateful runs with controlled scenario suites.

- Freeze evaluators and restrict the editable policy surface.

- Balance recall and diffusion against privacy, uncertainty, and stale-memory risks.


### 21. We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=oVsEddfhdxc) · [Read transcript](transcripts/oVsEddfhdxc.md)

Bakouch presents open experiments comparing coding agents with human researchers on GPT training and optimizer speedruns. Agents propose changes, launch GPU jobs, inspect logs, and validate records using statistical thresholds rather than single lucky runs. He reports competitive improvements from Claude Code and Codex, while describing differences in persistence, memory use, parallelism, and token consumption. Access to human records and literature complicates attribution, and he distinguishes these exploratory results from a planned controlled, multiple-seed benchmark with restricted-access tracks. Agents mostly recombine existing methods rather than invent new optimizers. A proposed discovery loop adds diverse generators, judging, human steering, and larger-scale validation, but remains under development.

- Validate records statistically and compare equal experimental conditions.

- Distinguish incremental optimization from genuinely novel discovery.

- Report resource use and information access alongside benchmark progress.


### 22. Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI

**Uploaded:** 2026-10-10 · [Watch video](https://www.youtube.com/watch?v=TyPpSRXGhbc) · [Read transcript](transcripts/TyPpSRXGhbc.md)

Dickens reports training a Qwen 3 4B finance specialist with reinforcement learning for under $500 in compute and judge costs. On a simulated financial question-answering benchmark, he reports nearly 60% pass-at-one versus 51% for a 235B variant. The dataset derives from annual-report tables and combines programmatic validation, independent agent review, and expert checks, with company-disjoint splits and 290 held-out examples. Training uses tool interaction and a reference-based model judge. Ablations favor simpler single-table training and binary rewards over curricula and elaborate rubrics; reported gains transfer to multi-table tasks without eroding general tool calling. He frames reliable tool discipline, realistic environments, autonomy horizons, and richer outputs as priorities, not universal small-model superiority.

- Validate synthetic data and prevent company overlap across splits.

- Test simple rewards and datasets before adding complexity.

- Reported cost excludes broader data-development effort; results concern a simulated domain.


### 23. From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=YIxzNZDDy1A) · [Read transcript](transcripts/YIxzNZDDy1A.md)

Ravenwolf demonstrates building an agent evaluation pipeline with Terminal Bench, Harbor, isolated sandboxes, and Wolf Bench dashboards. His central argument is that benchmarks measure configurations, not models alone: provider routing, harness versions, prompts, resources, sampling, and timeout policies affect comparability. He recommends repeated runs and publishing trajectories alongside average scores, consistency, capability ceilings, variance, and cost. Examples from his evaluations show that cheaper token pricing can produce higher total bills and increased reasoning can hurt under time limits. A live repository-repair task succeeds, but he excludes this partial run from the leaderboard. He emphasizes inspecting traces and distinguishing infrastructure failures from agent mistakes rather than trusting rankings uncritically.

- Pin and disclose the complete evaluation configuration.

- Compare repeated-run consistency, ceilings, variance, and actual cost, not averages alone.

- Inspect traces to distinguish model failures from infrastructure problems.


### 24. Version-Controlled Search: The Web as It Was — Ryan Ahern, Exa

**Uploaded:** 2026-10-19 · [Watch video](https://www.youtube.com/watch?v=vS2IA9pq0Q4) · [Read transcript](transcripts/vS2IA9pq0Q4.md)

Ryan Ahern presents Exa Snapshot as historical web access for building and testing predictive signals. He first discusses search quality, latency, and token cost, including the need to separate search-tool quality from the model reasoning over results. Point-in-time retrieval and versioned search then let developers reconstruct what information was available before an event, rather than accidentally read its later announcement. Examples move from enriching traditional models to testing fully agentic systems against historical inputs. He recommends incremental feature experiments and holdout cases when tuning signals. The method addresses future-information leakage in web retrieval, but does not by itself prove that a tuned predictor generalizes beyond the tested examples.

- Separate search quality from downstream model quality.

- Restrict historical evaluations to contemporaneously available web information.

- Use holdouts and feature-by-feature tests to check generalization.


### 25. How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada

**Uploaded:** 2026-10-22 · [Watch video](https://www.youtube.com/watch?v=c_SPW__jF9w) · [Read transcript](transcripts/c_SPW__jF9w.md)

Nathanael Weill explains how to evaluate specialized agents when public benchmarks do not exist and experts cannot grade frequent runs. His central inversion is to start with a known answer, generate the input around it, and check whether the agent recovers that answer. A RAG example replaces weekly expert feedback with dozens of automated tests per day. For supplier contracts, he combines past decisions, injected rule violations, removed clauses, harmless transformations, and filled templates. Deterministic checks are preferred when feasible because LLM judges introduce another calibration problem. Expert review still matters for realistic coverage and release decisions; synthetic tests accelerate iteration but cannot alone establish that a product is safe to ship.

- Construct inputs from known answers to reduce labeling dependence.

- Use injected defects and invariance tests to expand coverage.

- Prefer deterministic graders and use experts to identify missing test cases.


### 26. Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha

**Uploaded:** 2026-10-25 · [Watch video](https://www.youtube.com/watch?v=aVbRSIQO2dE) · [Read transcript](transcripts/aVbRSIQO2dE.md)

Janie Gu describes problems discovered while reproducing 65 industry benchmarks: expensive sweeps, stale leaderboards, grading-script manipulation, cross-model interference, and substantial variability between identical runs. She argues for realistic tasks, independent verification, and anti-cheating infrastructure rather than trusting a published score. Suyeol Yun then introduces MandateBench, which evaluates buy-side analyst work from a fund mandate through evidence gathering and investment-memo reasoning. Its tasks require resolving conflicting sources, rebuilding a company at a historical date, and judging reasoning rather than only the final recommendation. Early results are preliminary, and the full benchmark is still forthcoming. Together, the talks connect reproducibility controls with meaningful domain-specific assessment.

- Reproduce benchmarks and inspect how scores are produced.

- Protect grading infrastructure from evaluated agents.

- Use end-to-end domain work and temporal constraints rather than isolated finance questions.


### 27. How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit

**Uploaded:** 2026-10-26 · [Watch video](https://www.youtube.com/watch?v=OmyqelTwpOo) · [Read transcript](transcripts/OmyqelTwpOo.md)

Jesse Hall argues that a voice agent must be evaluated as a complete conversation rather than a collection of leaderboard-leading components. User-visible measures include time to first audio and first sentence, turn-taking, interruptions, and behavior while tools run. He demonstrates a hotel-booking agent and describes text and audio simulations with noisy callers, changed goals, and interruptions. Tests inspect database outcomes, authorized amounts, identity checks, hallucinated calls, and unnecessary steps; fixed scenarios allow stack and provider comparisons. He recommends listening to runs, checking the backend, and turning failures into regression cases. The presented latency and model rankings are specific to the demonstrated workload, not universal voice-agent prescriptions.

- Evaluate full conversations with realistic simulated callers.

- Measure audible response and sentence latency, not only first byte or token.

- Check final backend state, safety constraints, and tool efficiency before comparing stacks.


### 28. How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI

**Uploaded:** 2026-10-26 · [Watch video](https://www.youtube.com/watch?v=kRJjSOYqW0I) · [Read transcript](transcripts/kRJjSOYqW0I.md)

Xander Song introduces Harbor as a framework for evaluating agents on realistic tasks in isolated environments. Tasks combine instructions, Docker-based setups, and verifiers that assess outcomes independently of the agent implementation; oracles check that the environment and expected solution work before spending model tokens. Trials and jobs support repeated and parallel experiments, while standardized trajectories can be inspected in Phoenix alongside reward, latency, and cost. A Phoenix case study tests a prompt change encouraging SQL-tool usage and compares tool calls without sacrificing correctness. The Q&A explores integration-test boundaries, complex dependencies, dataset size, and the limits of mocking. The emphasis is reproducible evidence for architectural and prompt changes.

- Validate the task environment with an oracle before evaluating agents.

- Keep verifiers independent of implementation details.

- Compare repeated trials using both outcome scores and trajectories.


## Core · Coding agents & software verification


### 29. Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor

**Uploaded:** 2026-04-30 · [Watch video](https://www.youtube.com/watch?v=WE_Gnowy3uw) · [Read transcript](transcripts/WE_Gnowy3uw.md)

David Gomes describes replacing Cursor’s code-heavy worktree and best-of-N features with Markdown commands and subagents. A parent agent creates isolated worktrees, delegates implementations to different models, and compares or combines their results. The simplification improves flexibility but replaces enforced checkout isolation with instructions, allowing agents to drift into the primary repository, especially during long sessions. Gomes details a headless CLI evaluation with two scorers: one verifies work occurred in the intended worktree, and the other detects unauthorized primary-checkout changes. Early comparisons reveal model differences, but he acknowledges the tests do not yet reproduce very long sessions. Proposed improvements include stronger evals, system reminders, and relevant reinforcement-learning tasks.

- Replacing enforced isolation with prompting introduces a behavioral invariant that must be tested: agents must remain in their assigned checkout.

- Use complementary scorers to check both intended worktree activity and unintended edits in the primary checkout.

- Simple short-session evals can reveal model differences but do not establish reliability for the long sessions where drift is reported.

- A parent agent can compare and combine best-of-N implementations, but the talk does not establish the accuracy of that judging process.


### 30. Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse

**Uploaded:** 2026-05-20 · [Watch video](https://www.youtube.com/watch?v=vNCY9kXXyDQ) · [Read transcript](transcripts/vNCY9kXXyDQ.md)

Marc Klingen explains how Langfuse used execution traces and lightweight evaluations to improve a coding-agent integration skill. Traces exposed stale SDK assumptions, hallucinated CLI flags, and instrumentation that captured model calls but missed retrieval and tool activity. Five example setups supplied natural-language checks, judged against filesystem changes, to detect regressions. An automated skill-improvement experiment produced six proposals, three accepted, but minimizing turns encouraged removing documentation retrieval and other important workflow steps. Missing approval interactions and prompt-version links illustrated gaps in the objective and sandbox. The Q&A emphasizes human review and application-specific guidance rather than treating automated optimization as a complete substitute for expert judgment.

- Inspect actual execution traces before introducing elaborate evaluators; incomplete spans can hide the agent behavior that matters.

- Start with a small set of representative repositories and explicit, application-specific checks against the resulting changes.

- Optimization objectives must protect documentation freshness, approval gates, and production trace links instead of rewarding fewer turns alone.

- Review proposed skill changes manually and reference living documentation rather than duplicating dynamic content.


### 31. Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

**Uploaded:** 2026-06-03 · [Watch video](https://www.youtube.com/watch?v=zKk7sDMGDEQ) · [Read transcript](transcripts/zKk7sDMGDEQ.md)

Kuba Rogut evaluates semantic code retrieval using ContextBench-style human labels for files, lines and symbols an agent should inspect, rather than only task completion. Fifty tasks compare baseline Claude Code, fifty-line windowed reads and those reads plus a Voyage/turbopuffer search tool. Semantic search improves precision, but recall varies: behaviorally related files benefit, while import tracing often favors grep. The talk distinguishes adding an external tool from training a harness to use retrieval well, helping explain differences from Cursor’s results. It also frames embeddings as cached computation whose value depends on repeated workload and indexing cost.

- Measure retrieval process precision and recall separately from final task success.

- Break aggregate results down by task type.

- A model trained for search may exploit the same tool differently from an unadapted agent.


### 32. SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

**Uploaded:** 2026-06-04 · [Watch video](https://www.youtube.com/watch?v=wcUJWP6WpGM) · [Read transcript](transcripts/wcUJWP6WpGM.md)

Ibragim Badertdinov explains SWE-rebench’s monthly collection of fresh software-engineering tasks to reduce contamination. Each task needs a balanced issue description, executable environment and verifier with both fail-to-pass and regression tests. Filtering, manual review and agent trials expose brittle tests and infrastructure noise. The talk details retry policies, caching, changing provider defaults and replicating known scores before new experiments. Reward-hacking examples include future Git history, web tools and curl recovering original solutions. Repeated trials support confidence intervals and distinguish pass-at-five potential from all-five reliability, while trajectory analysis supplies richer evidence than a mean resolution score.

- Use temporal splits and remove future solutions from repositories and network access.

- Define retry/resource policies and distinguish infrastructure failures from model failures.

- Report repeated-trial reliability, uncertainty and cost as well as mean success.


### 33. Evals Are Broken, Use Them Anyway — Ara Khan, Cline

**Uploaded:** 2026-06-06 · [Watch video](https://www.youtube.com/watch?v=QuuIywMG4s8) · [Read transcript](transcripts/QuuIywMG4s8.md)

Ara Khan rejects both treating leaderboard numbers as objective truth and abandoning evaluations for subjective preference. Cline’s experience building realistic tasks leads into Terminal-Bench and Harbor, where isolated standardized environments run long coding workflows in parallel. Failure traces are categorized to identify model limitations, harness bugs and infrastructure constraints such as memory, CPU and timeouts. The talk distinguishes obvious repairs, nuanced model-specific harness improvements and dangerous overfitting. Its recommendation is to use relevant, current benchmarks alongside real product experience, recognizing that the tested unit includes model, harness, task definition and execution environment rather than model weights alone.

- Inspect and categorize failed trajectories rather than optimizing a headline blindly.

- Standardize resources and environment settings in agent comparisons.

- Distinguish real harness improvement from benchmark overfitting.


### 34. SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI

**Uploaded:** 2026-07-07 · [Watch video](https://www.youtube.com/watch?v=Rx8f05JI_WA) · [Read transcript](transcripts/Rx8f05JI_WA.md)

Rishi Desai presents SWE-Marathon, a twenty-task benchmark for project-scale coding work rather than isolated patches. Tasks span library clones, full-stack products, machine learning and algorithms, with long trajectories and large token budgets. Verification combines hidden tests, reference comparisons, browser-based user workflows and anti-cheating checks because an agent can exploit weak tests over hours of execution. The talk reports a best resolution rate of 26% and distinguishes suspicious shortcuts from actual verifier bypass attempts. A compiler submission secretly invoking GCC illustrates why functional parity alone is insufficient. Public trajectories support inspection of failures and harness effects.

- Use independent verification channels with different failure modes.

- Browser workflow tests complement backend unit tests for product clones.

- Harden long-horizon tasks against reward hacking, not only accidental errors.


### 35. Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs

**Uploaded:** 2026-07-08 · [Watch video](https://www.youtube.com/watch?v=HEFSExa0xl0) · [Read transcript](transcripts/HEFSExa0xl0.md)

Nuno Campos describes improving spreadsheet agents from roughly 50% to 92% on an internal financial-analysis benchmark. A persistent JavaScript REPL replaced many sequential tools, enabling more efficient exploration and nearly eliminating task timeouts. Crucially, reliable formula-calculation and rendering engines gave agents feedback analogous to compilers and tests; incomplete engines instead created misleading failures. Evaluation also evolved from LLM-only judging toward deterministic comparisons against golden spreadsheets, applying identical inputs and comparing resulting outputs. Campos stresses inspecting traces because apparent reasoning failures can originate in broken tools, prompts, or examples. The durable investment is trustworthy feedback infrastructure, even as model capabilities and preferred interfaces change.

- Prefer deterministic input/output checks when spreadsheet behavior permits them.

- Verifier fidelity matters: incomplete calculation engines can penalize correct work.

- Inspect tool plumbing before attributing every failure to reasoning.


### 36. Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com

**Uploaded:** 2026-07-08 · [Watch video](https://www.youtube.com/watch?v=MpZzWMdmQCE) · [Read transcript](transcripts/MpZzWMdmQCE.md)

Talha Sheikh describes replacing repeated manual correction of coding agents with explicit verification contracts. His Vector harness uses hooks and configurable checks to test outputs when an agent finishes, feeding failures back for another attempt. He distinguishes better instructions and greater model capability from demonstrated reliability, and generalizes the pattern beyond one product to language-agnostic checks at session endings, commits, multi-agent handoffs, and asynchronous work. Deterministically invoked verification may also call an LLM judge where appropriate. Sheikh suggests stronger harnesses could enable cheaper models, but presents this as an argument rather than a controlled benchmark. The main contribution is enforceable, reusable completion checks.

- Do not equate explicit instructions with verified compliance.

- Invoke checks automatically at meaningful workflow boundaries.

- Make verification contracts portable while allowing domain-specific validators.


### 37. Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI

**Uploaded:** 2026-07-15 · [Watch video](https://www.youtube.com/watch?v=q4Tr-DknG2M) · [Read transcript](transcripts/q4Tr-DknG2M.md)

Lee Robinson describes Cursor’s model-improvement flywheel connecting user reports, online A/B tests, private evaluations, difficult training environments, and new checkpoints. Public tests were vulnerable to Git-history and internet solution lookup, so Cursor also uses held-out internal engineering tasks reflecting real workflows and behavioral preferences. Robinson discusses retiring saturated evals, generating verifiable feature-reconstruction tasks, and providing localized textual feedback to improve credit assignment across long trajectories. Evaluation compute includes repeated checkpoint testing, reward generation, and developing fresh tasks, not just a launch leaderboard. The broader research-automation discussion explains how stronger models can help build and judge the next generation’s training and evaluation materials.

- Maintain held-out private evals representative of real engineering work.

- Audit public environments for solution lookup and other reward shortcuts.

- Continuously refresh saturated tasks and evaluate each training checkpoint.


### 38. In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar

**Uploaded:** 2026-07-20 · [Watch video](https://www.youtube.com/watch?v=VrpEyglYgeU) · [Read transcript](transcripts/VrpEyglYgeU.md)

Tariq Shaukat argues that agent capability gains do not remove the need to verify reliability, security, complexity, and maintainability. He contrasts benchmark task horizons at different success thresholds and describes Sonar’s coding evaluations, which assess more than functional correctness. His Guide, Verify, Solve framework supplies architectural context and constraints, combines algorithmic analysis with agentic assessment, and maintains code quality through ongoing remediation. Verification belongs inside the agent loop, the CI review loop, and the maintenance loop rather than as an afterthought. Vendor-presented customer results illustrate the argument, but the central recommendation is a deliberate, zero-trust, multilayered system for evaluating what agents actually produce.

- Distinguish impressive task horizons from enterprise-required success rates.

- Evaluate security and maintainability alongside functional correctness.

- Combine algorithmic and agentic checks across development and maintenance loops.


### 39. DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve

**Uploaded:** 2026-07-26 · [Watch video](https://www.youtube.com/watch?v=Yk87oUPVaxU) · [Read transcript](transcripts/Yk87oUPVaxU.md)

James Shi presents DeepSWE, a benchmark of 113 original, long-horizon software-engineering tasks across five languages and a broad repository pool. He explains why public pull-request-derived tests can leak solutions, reward implementation-specific details, and inadequately distinguish strong models. DeepSWE instead commissions realistic tasks, checks observable behavior, separates verifier and agent runtimes, and removes exploitable Git history. Qualitative rollout analysis reveals missed multipart requirements, differences in requirement adherence, and how benchmark instructions can suppress self-testing. Shi also acknowledges limitations: harness effects deserve separate study, and refactoring and bug-localization tasks remain underrepresented. The talk treats benchmark integrity and failure analysis as essential complements to leaderboard scores.

- Separate verifier execution from the agent and remove solution-bearing Git history.

- Test observable behavior rather than private helpers or a single implementation.

- Inspect trajectories and prompt effects, not just aggregate success rates.


### 40. Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=jWq-aZIU0kM) · [Read transcript](transcripts/jWq-aZIU0kM.md)

Khial recounts investigating why coding benchmarks fail to resemble engineering work or inspire trust. He decomposes a benchmark into instructions, agents, verifiers, harnesses, and resulting trajectories, then examines unrealistic or leaky prompts, economically questionable tasks, and tests tied to unspecified implementation details. Citing another team's comparison, he reports that SWE-bench Pro tasks sometimes accepted incorrect implementations or rejected correct ones. He also describes increasingly capable agents exploiting exposed repository history or internet traces. His proposed framework combines human-authored instructions focused on behavior and constraints, holistic behavioral grading, production-relevant tasks, novel private holdouts, and reporting that explains model behavior instead of presenting only leaderboard winners.

- Specify desired behavior and hard constraints without leaking test locations or prescribing internal implementation details unnecessarily.

- Audit false positives and false negatives in verifiers, especially tests that require undeclared variable names or inspect nonpublic internals.

- Use production-relevant novel tasks and private holdouts, while hardening harnesses against access to solution-revealing history or external traces.

- Publish interpretable trajectory and performance information that helps engineers choose models, not just a ranking that says which model won.


### 41. fighting slop with slop — Vaibhav Gupta, Boundary

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=AMiyLItEtLA) · [Read transcript](transcripts/AMiyLItEtLA.md)

Vaibhav Gupta describes Boundary's attempt to ship a reliable programming language without conventional code reviews or standardized AI tools. Small architecture documents, genuinely read design proposals, and dependency checks establish durable constraints. Agents continuously generate BAML programs; other agents inspect their execution transcripts for incorrect behavior and unnecessary tool calls, with humans triaging proposed issues. Language features and skills can then be A/B tested for errors, tool use, and successful outcomes. Gupta also demonstrates architectural visualization, navigable execution traces, source-aware inspection, callable functions, inferred error types, and cross-language interoperability. His argument is that stronger tooling and enforceable invariants can replace exhaustive line-by-line reading, not that correctness becomes unnecessary.

- Enforce architectural invariants with dependency checks instead of expecting agents to preserve boundaries through prose alone.

- Generate real programs continuously and inspect complete traces for both correctness failures and avoidable tool calls.

- A/B test language features or skills on successful outcomes, errors, and tool-call counts, while humans filter unreliable issue reports.

- Use inferred error types and compiler checks to make error-handling obligations explicit and mechanically checkable.


### 42. Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs

**Uploaded:** 2026-08-08 · [Watch video](https://www.youtube.com/watch?v=7vn4WpqNpck) · [Read transcript](transcripts/7vn4WpqNpck.md)

Linkov examines Wisedocs' decision to rebuild a complex medical-document pipeline from multiple legacy repositories into a monorepo. He revisits earlier refactoring tasks with newer coding models and harnesses, reporting less manual intervention and better tool use, while distinguishing execution cost from engineering effort. He cautions against interpreting advertised task horizons at modest success rates as dependable autonomy. A separate attempt to refactor the whole system quickly produced scaffolding rather than functioning model deployments, illustrating why completion claims need inspection. The broader case study weighs technical debt, business outcomes, developer participation, and timing; its discussion emphasizes explicit requirements, proof-of-concept validation, end-to-end verification, and human reviews that preserve shared understanding.

- Replay representative historical engineering tasks and inspect errors, intervention requirements, tool use, and total engineering effort rather than comparing model runtime alone.

- Use high success-rate thresholds when interpreting autonomous task horizons; a median-success horizon is not a reliability guarantee for unattended work.

- Validate implementation completeness against requirements: Linkov's whole-system refactor experiment appeared finished but omitted operational model-serving components.

- Include business outcomes and maintainability in refactor evaluation; faster commits or more generated lines alone do not establish product quality.


### 43. Guide, Verify, Solve — Anirban Chatterjee, Sonar

**Uploaded:** 2026-08-09 · [Watch video](https://www.youtube.com/watch?v=03l29gJXpCE) · [Read transcript](transcripts/03l29gJXpCE.md)

Chatterjee frames AI coding's bottleneck as verification debt: faster generation can leave persistent complexity, security, and maintainability problems. He describes Sonar's model leaderboard as evaluating coding tasks across several quality dimensions rather than correctness alone, and argues that human review also suffers from overreliance on confident AI output. His proposed guide-verify-solve cycle supplies architectural constraints and relevant context, checks generated code independently, and lets agents remediate findings. The presentation demonstrates Sonar Vortex integration and extends verification from the inner coding loop to outer pull-request and CI/CD gates. Its central recommendation is bounded autonomy backed by repeatable, auditable, multilayer checks combining computational analysis and LLM review.

- Evaluate generated code for security, complexity, and maintainability as well as task completion; stronger correctness does not guarantee stronger results on every quality dimension.

- Use independent, repeatable verification methods rather than relying solely on the generating model or human approval of confident-looking output.

- Encode organizational constraints and quality thresholds, then verify both during agent execution and at pull-request gates, feeding failures back into remediation.


### 44. How to Kill the Code Review — Ankit Jain, Aviator

**Uploaded:** 2026-08-17 · [Watch video](https://www.youtube.com/watch?v=YgEv7IQzGdM) · [Read transcript](transcripts/YgEv7IQzGdM.md)

Ankit Jain argues that AI-generated code makes line-by-line review a bottleneck, but eliminating review must not eliminate team alignment, mentorship, or architectural discussion. His proposed replacement captures decisions from coding sessions as acceptance criteria and combines them with an 'AI slop registry' of recurring review failures to generate test plans. Verification runs the application in previews and gathers behavioral evidence, including screenshots and database snapshots. Humans review intent, architecture, test coverage, and execution evidence rather than merely trusting another model's comments. He favors deterministic checks where possible and LLM assistance where necessary, emphasizing that tests derived only from generated code can repeat the implementation's blind spots.

- Preserve evolving decisions from agent conversations instead of discarding prompts after opening a pull request.

- Turn recurring review comments into reusable invariants and combine them with acceptance criteria.

- Verify behavior in a running preview and retain screenshots or database evidence for reviewers.

- Derive test intent independently of generated code to reduce shared implementation-and-test blind spots.


### 45. The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo

**Uploaded:** 2026-08-20 · [Watch video](https://www.youtube.com/watch?v=s-aixZYJG4c) · [Read transcript](transcripts/s-aixZYJG4c.md)

Itamar Friedman treats code review as both quality verification and a mechanism for alignment and learning, then asks what infrastructure could gradually automate it. He argues that stronger models alone are insufficient: reviewers need codified team standards, architectural context, service contracts, past incidents, and developer discussions. A context engine should expose this knowledge in forms useful to both humans and agents, linking findings to the rules and evidence behind them. He proposes software graphs that reveal cross-repository dependencies and conflicting changes, plus analytics showing which rules actually help. Automatic approval and blocking should expand incrementally through explicit semantic policies, rather than immediately removing human oversight.

- Evaluate changes against team-specific intent, architecture, and standards, not merely generic code-quality advice.

- Make review findings auditable by linking them to the applicable rules and accumulated organizational evidence.

- Include service contracts, incident history, and concurrent changes in cross-repository verification context.

- Introduce automatic approval and blocking gradually, measuring rule usefulness and retaining human visibility and control.


### 46. Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI

**Uploaded:** 2026-08-27 · [Watch video](https://www.youtube.com/watch?v=pOvWgX7IJsc) · [Read transcript](transcripts/pOvWgX7IJsc.md)

Simran Arora introduces ParallelKernelBench to test whether frontier models can generate useful multi-GPU CUDA kernels, after explaining communication bottlenecks and the ParallelKittens primitives. The benchmark contains 87 real-workload problems, each supplying a PyTorch reference and hardware topology. Evaluation separates functional correctness from kernels that also outperform the baseline, including pass-at-K and speedup-threshold comparisons. More sampling and a multi-turn bash-enabled agent improve results but plateau; compiling successfully does not imply understanding collective ordering, partitioning or communication tradeoffs. Reported zero-shot best-model performance is 28 correct kernels, 22 faster than baseline. The talk emphasizes realistic task coverage and analyzing which familiar patterns models solve.

- Measure correctness and speed independently before combining them.

- Build benchmark coverage from real workload taxonomies and hardware constraints.

- Analyze plateauing test-time scaling and conceptual failures beyond compilation.


### 47. Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma

**Uploaded:** 2026-08-28 · [Watch video](https://www.youtube.com/watch?v=ZIYYsAzaLlA) · [Read transcript](transcripts/ZIYYsAzaLlA.md)

Jesse Lumarie recounts building Figma’s MCP server and the evaluation loop used to choose representations of design context. The team combined measurable checks, such as variable and theme usage, with qualitative judgments about visual quality and decisions under incomplete information. Manual spreadsheet grading proved too cumbersome, so they built an evaluation web app and assembled toy repositories with paired design files. The resulting workflow runs hundreds of times weekly and uses LLM judges to assess prompt changes. The talk also distinguishes pixel-perfect output from enterprise usefulness: generated implementations should reuse accessible, internationalized code components rather than merely resemble the design.

- Combine structural checks with visual and decision-quality assessments.

- Build paired design/code fixtures rather than relying on unrelated public repositories.

- Automate frequent prompt-regression runs while judging component reuse, not only pixels.


### 48. Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber

**Uploaded:** 2026-08-28 · [Watch video](https://www.youtube.com/watch?v=EL123UNokkI) · [Read transcript](transcripts/EL123UNokkI.md)

Will Bond and Ameya Ketkar explain how Uber improved uReview by moving beyond cost tracking and broad satisfaction surveys. They collect review-reply sentiment, whether developers address comments, and agent trajectories to identify weak rules, wasted actions and runtime issues. Distributed team-specific reviewers share central routing, filtering and deduplication, with observability returned to rule owners. Reported production scale is about 25,000 comments weekly, with roughly 67% addressed and a 60% cost reduction versus their naive implementation. They distinguish human-facing from agent-inner-loop reviews, where inaccurate comments can cause repeated reversals. Their conclusion preserves a human outer feedback loop focused on architecture, domain expertise and product judgment.

- Measure actionable comment outcomes and trajectories, not only cost or surveys.

- Return quality signals to teams that own reviewer rules.

- Retain human feedback as review moves deeper into autonomous coding loops.


### 49. Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS

**Uploaded:** 2026-08-28 · [Watch video](https://www.youtube.com/watch?v=lRa9sPaMyy4) · [Read transcript](transcripts/lRa9sPaMyy4.md)

Varun Pant introduces formal verification as a complement to probabilistic judges, sampled tests and limited human review for AI-generated code. The key contract is an explicit specification: humans must validate what correctness means before machines implement it and construct proofs. He explains Lean’s tactics and independently checkable trusted kernel, then discusses a reported zlib conversion and Cedar’s Lean specification paired with Rust production code. Cedar’s differential random testing is distinguished from direct deductive proof. Further examples include Verus preconditions and postconditions and AWS’s work-in-progress Strata framework. The practical message is to start with critical code and verified specifications, not assume proofs establish unstated requirements.

- Validate specifications before trusting a formally checked implementation.

- Distinguish proof checking from differential random testing.

- Use small trusted verification kernels to check machine-generated proofs.


### 50. Fixing the PR Bottleneck — Matt Pocock, AIHero

**Uploaded:** 2026-09-25 · [Watch video](https://www.youtube.com/watch?v=LlgiOCmFG_w) · [Read transcript](transcripts/LlgiOCmFG_w.md)

Matt Pocock proposes three quality brakes for agent-driven software factories: deterministic checks, automated review and human review. He illustrates why green CI can mislead through tautological assertions, source-structure tests and mocks that erase real failure modes. Deep modules with narrow interfaces make behavior-focused tests easier. A separate reviewer context applies repository-specific standards and, in his proposed workflow, commits fixes before humans see the change. Human attention is allocated by reversibility and blast radius rather than diff size alone. Finally, retrospectives convert recurring review findings into stronger checks, standards and navigation guidance, improving the system that produces code rather than repeatedly correcting identical mistakes.

- Test behavior rather than restating constants or inspecting source text.

- Separate implementation from standards-focused review to reduce context overload.

- Turn recurring human review findings into durable checks and process improvements.


### 51. AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile

**Uploaded:** 2026-09-27 · [Watch video](https://www.youtube.com/watch?v=474j-n1Ltxc) · [Read transcript](transcripts/474j-n1Ltxc.md)

Gupta examines whether largely autonomous coding agents produce enterprise-worthy pull requests using Greptile's review data. He infers AI authorship from author fields, description footers, and branch prefixes, reporting about a quarter of reviewed PRs as largely AI-generated. Revert rates, detected high-severity bugs, and review iterations show broadly comparable human and agent outcomes in his analysis, while keyword-based error categories reveal differing failure profiles. These are observational proxies with imperfect authorship labels and reviewer-dependent quality signals, not proof of equivalent capability on matched tasks. He argues validation must scale with PR generation, assessing user-contract violations, future risk, and author intent through contextual review and sandbox execution.

- Use multiple quality signals rather than a single revert or bug metric.

- Account for imperfect authorship inference and observational comparison limits.

- Validate intent and user contracts with contextual analysis and execution.


### 52. The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI

**Uploaded:** 2026-09-30 · [Watch video](https://www.youtube.com/watch?v=_mi3alkqy4s) · [Read transcript](transcripts/_mi3alkqy4s.md)

Voss examines why rapid AI code generation has not translated proportionally into shipped software, framing human review as a bottleneck. He contrasts test-passing benchmarks with maintainer mergeability, surveys multipass and tool-using automated reviewers, and revisits autonomous coding experiments whose human judgment moved into harnesses rather than disappearing. Claimed case studies highlight maintenance problems, unsafe-code blind spots, and prompt-injection vulnerabilities in reviewers. His conclusion is not to abandon verification but to encode domain context, quality standards, and review criteria into an engineered system. Humans still assess that system, especially where consequences are large or correctness is expensive to check, while production observability provides essential downstream evidence.

- Measure mergeability, not merely whether a test suite passes.

- Evaluate review systems for false positives and adversarial manipulation.

- Move scarce human judgment into harness design and production verification.


### 53. Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=T3SS931wU0I) · [Read transcript](transcripts/T3SS931wU0I.md)

Jess introduces evaluations as datasets, executable tasks, scoring systems, and comparative experiments that support evidence-based shipping decisions. Her example compares vector retrieval with tool-driven agentic search on roughly 20 bug-fix tasks reconstructed from Microsoft's TypeScript-Go repository. Both approaches use Claude Code, with tool restrictions enforcing the vector condition; subprocess trace linkage makes behavior inspectable, and repository tests provide binary scoring. She reports equal accuracy but fourfold higher cost for vector search, attributing repeated retrieval to chunks lacking cross-function context. She explicitly limits the finding: the vector implementation was weak, the dataset small and single-repository, and repeated trials and broader coverage would strengthen confidence. The purpose is methodological illustration, not a definitive retrieval ranking.

- Control harness and tool access when comparing retrieval methods.

- Inspect traces and actual test outcomes alongside cost.

- Do not generalize a small, weak-baseline experiment into universal search superiority.


### 54. We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman

**Uploaded:** 2026-10-08 · [Watch video](https://www.youtube.com/watch?v=k2ClBT4aqAg) · [Read transcript](transcripts/k2ClBT4aqAg.md)

Kamalakannan Nandagopal describes evaluating Postman’s API context graph using real pull requests and retrospective design decisions as task ground truth. The team compares its agent, Claude Code using GitHub search, and Claude Code with graph access through a skill, scoring outputs from zero to five and measuring token consumption. Examples cover API discovery, input-shape reconstruction, and change-impact assessment. He reports quality and efficiency benefits in selected cases, but also an inverted result when newly added consumers were missing from the graph. The presentation therefore highlights freshness as an evaluation dependency; it does not supply a complete dataset or statistical validation of general superiority.

- Build evaluations from real changes and design decisions, measuring quality alongside token use.

- Compare context tools across agents rather than attributing every gain to a single model.

- Test graph freshness, including added and removed dependencies, when diagnosing failures.


### 55. How to Build an AI Code Review Agent - Daksh Gupta, Greptile

**Uploaded:** 2026-10-26 · [Watch video](https://www.youtube.com/watch?v=4UtrRVtUN_g) · [Read transcript](transcripts/4UtrRVtUN_g.md)

Daksh Gupta outlines how to build an effective code-review agent beyond a basic webhook and sandbox. The difficult requirements are finding substantive bugs, suppressing nitpicks, understanding a large codebase, and keeping review costs manageable. He recommends a continuously updated evaluation set of historical incident-causing pull requests, focused prompts, contextual documentation, and autonomous end-to-end tests. Greptile reportedly detects about 10% more bugs when a different model family reviews the generating model’s code. He also discusses routing inexpensive models to simpler subtasks. His caution is fundamental: finding bugs demonstrates their presence, but a clean review cannot prove their absence, so validation must keep evolving as agents produce new failure modes.

- Evaluate against historical incident PRs and refresh the dataset.

- Use different model families to reduce correlated reviewer blind spots.

- Measure useful bug detection, noise, and review cost together.


## Core · Domain-specific & multimodal evaluation


### 56. Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=31GUkCBD-Uc) · [Read transcript](transcripts/31GUkCBD-Uc.md)

Soumya Gupta and Jai Chopra describe Uber Eats’ evaluation system for enhancing merchant food photographs without changing the dish, erasing branding, or homogenizing the marketplace. Human-labeled, representative examples anchor routing precision and recall, while editing agents receive multidimensional QA feedback and bounded regeneration attempts. Pairwise input/output checks assess faithfulness, completeness, naturalness, and realism; uncertain cases can be rejected. Production samples, merchant feedback, and marketplace metrics feed a diagnoser that routes failures to configuration and prompt-tuning loops. Updated agents must clear the golden benchmark before registration. The talk highlights reward hacking, redundant final publication checks, observability, segment-level analysis, and rollback as safeguards around automated improvement.

- Evaluate routing separately from generation and final publication readiness.

- Keep faithfulness and merchant authenticity explicit in multimodal rubrics.

- Benchmark automatic tuning against golden data before deploying new configurations.


### 57. How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=Tt2kX2sgQio) · [Read transcript](transcripts/Tt2kX2sgQio.md)

Vinoo Ganesh argues that citations and probabilistic evaluations cannot by themselves guarantee numerically reliable financial work. He describes Kepler's three-part architecture: atomic provenance, scoped determinism, and derivation chains. Models select references and decide what should be computed, while deterministic systems extract, persist, validate, and calculate numbers. Unverifiable values are removed rather than passed through. Derivation chains record source data and transformations so ratios and adjustments can be replayed under a firm's particular conventions. Ganesh distinguishes verifying a process from proving an investment opinion correct, since identical evidence can support opposing positions. The discussion extends the approach to legal and scientific entities and ends with customers' interest in automating repetitive analyst tasks.

- Separate model planning from deterministic numerical extraction, storage, and calculation rather than asking another model to certify the first.

- Preserve atomic references to source values and reject values that fail independent deterministic checks.

- Record replayable derivation chains, including firm-specific transformations, because a citation alone does not validate a derived metric.


### 58. Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings

**Uploaded:** 2026-07-30 · [Watch video](https://www.youtube.com/watch?v=tJFjeMBKbIY) · [Read transcript](transcripts/tJFjeMBKbIY.md)

Shawn Chan evaluates finance AI from the perspective of an investment-committee decision maker rather than a builder. A polished demo is insufficient when a memo must survive scrutiny across conflicting filings, notes, transcripts, and spreadsheets. He identifies six trust failures: unreliable source selection, inconsistent numbers, concealed contradictions, guesses presented as facts, inaccessible evidence, and missing accountability. His proposed controls link each claim to an exact source passage and trust level, visibly separate assumptions, automatically reconcile figures, surface disagreements, and log human approval. The closing fundraising lesson applies the same standard to founders: pitch claims eventually become internal investment memos whose numbers are checked against the data room.

- Attach exact, directly accessible source passages and source-trust levels to individual claims, not merely a bibliography.

- Block inconsistent figures and preserve visible labels separating facts from forecasts or assumptions.

- Surface source contradictions for human review and retain an approval trail showing who reviewed, changed, and signed the work.


### 59. "My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow

**Uploaded:** 2026-09-15 · [Watch video](https://www.youtube.com/watch?v=IDNfAZVKvPE) · [Read transcript](transcripts/IDNfAZVKvPE.md)

Midam Kim analyzes a failed voice-agent call through a linguistic framework rather than treating each defect as an isolated bug. Misheard spelling, English-centric pronunciation, premature turn-taking, unfamiliar account terminology and repeated requests accumulate into user frustration. Her framework crosses listening and speaking with sounds, words, interaction and mental models. These layers are interdependent and evolve over a call, so strong speech recognition alone cannot guarantee task success. She recommends using this structure to diagnose an agent and references ServiceNow’s EVA end-to-end benchmark. The central evaluation contribution is a systematic error taxonomy connected to escalation, abandonment, silent failures and the user’s evolving understanding.

- Classify failures across listening, speaking, interaction and intent tracking.

- Evaluate accumulated conversation experience rather than isolated speech components.

- Include user adaptation, clarification and mental-model consistency in diagnosis.


### 60. 5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo

**Uploaded:** 2026-09-15 · [Watch video](https://www.youtube.com/watch?v=vblnYHzBgS4) · [Read transcript](transcripts/vblnYHzBgS4.md)

Venky B organizes production voice failures into latency, brittle transcription, data collection, speech normalization and turn-taking problems. He discusses measuring time to first audio and balancing model capability, cost and response speed, including multilingual tokenization effects. The most concrete evaluation recommendation is to model collected information as typed fields with validators and confirmations, then test each field independently instead of running expensive end-to-end conversations to discover a broken input. He reports substantial data-collection improvements without fine-tuning through this structural approach. Proper nouns, code-switching, relative dates and pronunciation are practical stress cases. The talk emphasizes engineering reliable subcomponents rather than repeatedly tweaking prompts and hoping compliance improves.

- Treat collected phone numbers, names and dates as typed, validated fields.

- Use field-level regression tests to localize failures before end-to-end testing.

- Benchmark multilingual latency and pronunciation on realistic domain vocabulary.


### 61. The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=42Bz0TUfeOQ) · [Read transcript](transcripts/42Bz0TUfeOQ.md)

This Arize talk argues that transcripts alone conceal important voice-agent failures: pauses, overlapping speech, transcription errors, tone, and incorrect downstream actions. An AI-generated refund example illustrates a misheard order number, dead air, and a refund issued for the wrong order despite superficially reassuring text. The presenter advocates linking audio, transcripts, tool spans, and multi-turn sessions through normalized OpenInference conventions. Audio-aware evaluations should measure time to first audio, interruptions, sentiment, transcription drift, and actual task success, with results attached to relevant spans. The closing vision extends observation into agent-led diagnosis, replay-based fix validation, and reviewable pull requests; this self-healing workflow is presented as a future direction rather than proven end-to-end performance.

- Evaluate original audio alongside transcripts and actual tool outcomes.

- Stitch turns into sessions to diagnose latency and interruption behavior.

- Replay failures against proposed fixes and inspect measured results before approval.


### 62. Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics

**Uploaded:** 2026-10-23 · [Watch video](https://www.youtube.com/watch?v=A3FL_zTQKU0) · [Read transcript](transcripts/A3FL_zTQKU0.md)

Stephanie Jarmak argues that agent evaluation should resemble a controlled experiment. She shows that changing the harness alone can move benchmark performance by more than thirty percentage points, so a score cannot be attributed to the model without accounting for configuration. Public benchmarks help shortlist candidates; product decisions require realistic local tasks, repeated runs, appropriate measures, and full-pipeline traces. She discusses balancing retrieval precision and recall, enforcing quality gates that actually stop work, and budgeting the human workload created by alarms. Agent-maintained records may be unreliable evidence. Production feedback ultimately tests whether offline improvements survive real conditions, and escalation should be designed around risk rather than a single aggregate success rate.

- Control harness and environment variables when comparing models.

- Repeat realistic tasks and inspect trajectories, not only scores.

- Make gates enforceable and account for the human cost of false alarms.


### 63. Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence

**Uploaded:** 2026-10-24 · [Watch video](https://www.youtube.com/watch?v=WOszaC1WWbQ) · [Read transcript](transcripts/WOszaC1WWbQ.md)

Harneet Kaur asks how to assess AI reasoning when the final outcome has not happened yet. In a live distressed-credit case involving iHeartMedia, frontier models given similar context initially assign sharply different bankruptcy probabilities. She decomposes the work into extraction, derivation, judgment, and prediction so that factual inputs and assumptions can be checked separately. Structured context and layer-by-layer evaluation bring the models toward a common answer, but she explicitly questions whether convergence proves correctness. Historical testing also risks look-ahead bias. The talk’s contribution is a framework for exposing intermediate reasoning failures and assumptions, not evidence that consensus can validate an uncertain investment forecast.

- Evaluate extraction and derivation separately from judgment and prediction.

- Check assumptions when no final ground truth is available.

- Do not confuse agreement between models with independent correctness.


## Core · Foundations & evaluation design


### 64. The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

**Uploaded:** 2026-05-06 · [Watch video](https://www.youtube.com/watch?v=ow1we5PzK-o) · [Read transcript](transcripts/ow1we5PzK-o.md)

Luke Alvoeiro presents Factory's Missions architecture, emphasizing verification as the mechanism that sustains long-running coding agents. An orchestrator defines features, milestones, and a validation contract before implementation. Workers execute tasks with clean contexts and provide structured handoffs containing commands, exit codes, and unresolved issues. Separate validators run conventional checks and feature reviews, then exercise the live application through user-like interactions. Failures generate corrective work at milestone boundaries. The talk favors serial feature execution with parallel read-only operations and assigns models by role. A Slack-clone example illustrates repeated validation failures and follow-up work, rather than treating passing unit tests as sufficient evidence of completion.

- Define behavioral correctness during planning, independently of the implementation, and map every required assertion to work.

- Separate implementation from fresh-context scrutiny and live user-flow testing to reduce confirmation bias.

- Record commands, exit codes, unresolved issues, and corrective work in structured handoffs at validation boundaries.

- Parallelize read-only investigation and review selectively rather than allowing concurrent writers to undermine correctness.


### 65. Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson

**Uploaded:** 2026-05-18 · [Watch video](https://www.youtube.com/watch?v=mR-WAvEPRwE) · [Read transcript](transcripts/mR-WAvEPRwE.md)

Prabaker and Wilson examine long-running agents through context management, planning, and unreliable self-assessment. Their central pattern separates a generator from an adversarial evaluator that exercises live applications with browser tools rather than merely reviewing code. Subjective design quality becomes an explicit, example-calibrated rubric, while generator and evaluator negotiate testable contracts before implementation. A game-building comparison illustrates how interactive verification exposes broken behavior that superficial completeness and unit tests miss. Trace reading identifies where model judgment diverges from human expectations and guides prompt revisions. Q&A clarifies that evaluators should judge outputs without inheriting generator reasoning, and that rubric scores are useful within runs but not readily comparable across products.

- Separate builder and critic contexts; have the critic exercise the running application rather than accept the builder's account of success.

- Translate subjective preferences and feature requirements into calibrated rubrics and granular, negotiated acceptance tests.

- Read complete traces to find judgment failures and revise prompts; reevaluate which harness components remain necessary as models change.

- Treat the demonstrated pattern primarily as a greenfield approach requiring project-specific validation, not as evidence of comparable scores across products.


### 66. Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence

**Uploaded:** 2026-05-31 · [Watch video](https://www.youtube.com/watch?v=UQKg0td-Bf4) · [Read transcript](transcripts/UQKg0td-Bf4.md)

Steven Willmott argues that an agent specification must contain more than input/output examples. It should explicitly state rules, domain ontologies, terminology, rights, roles and robustness requirements, independently of implementation. Larger models can understand more malicious instructions and broader tool access creates additional attack surface, so capability is not equivalent to safety. The same specification can guide security testing and valid input variations such as typos or rephrasings. Tests should survive framework or model changes and feed iterative repairs. The talk stresses that generating meaningful variants requires knowing which substitutions preserve domain meaning and permissions.

- Specify rules, role permissions and valid perturbations, not only happy-path examples.

- Keep evaluation specifications independent of the deployed framework.

- Use domain context to target both security boundaries and robustness tests.


### 67. Agents Building Agents - Alfonso Graziano, Nearform

**Uploaded:** 2026-06-28 · [Watch video](https://www.youtube.com/watch?v=aHhB3sjGjkI) · [Read transcript](transcripts/aHhB3sjGjkI.md)

Alfonso Graziano separates a coding agent that builds software from the product agent being evaluated. A golden dataset and scorers establish the baseline; an optimization loop proposes one hypothesis, edits prompts, tools or code, reruns evaluations and retains or rolls back changes. Reports and memory preserve unsuccessful experiments as well as gains. A second workflow collects production traces with user or expert feedback, clusters failure modes, validates them with domain experts and adds confirmed cases to regression coverage. The talk warns against letting the optimizing agent change datasets or scorers simply to make scores improve.

- Give builder agents access to traces, explicit metrics and protected evaluation targets.

- Retain experiment reports and roll back regressions.

- Turn validated production failure clusters into golden-dataset cases.


### 68. Frontier results, on device - RL Nabors, Arize

**Uploaded:** 2026-06-29 · [Watch video](https://www.youtube.com/watch?v=fWXJM-J0ZB8) · [Read transcript](transcripts/fWXJM-J0ZB8.md)

RL Nabors demonstrates selecting small local models through application-specific capability evaluations rather than public reputation. A thread-summarization case uses a golden dataset, deterministic checks for JSON, references and length, plus an LLM judge for factual consistency and latency measurements. The process prototypes with a capable remote model, tests smaller alternatives, and isolates prompt changes one variable at a time. Inspecting individual failures exposes overly strict judging and format problems better handled by post-processing. The resulting model and prompt are retained as regression tests so future migrations cannot silently undo quality or responsiveness gains.

- Build task-specific golden examples and define success before choosing a model.

- Inspect judge disagreements and individual outputs instead of trusting aggregate scores.

- Test prompt variants independently and preserve the winning setup as regression coverage.


### 69. The Agentic AI Engineer - Benedikt Sanftl, Mutagent

**Uploaded:** 2026-06-29 · [Watch video](https://www.youtube.com/watch?v=pSto5YaNGUo) · [Read transcript](transcripts/pSto5YaNGUo.md)

Benedikt Sanftl and Burak describe automating the offline and online loops of agent engineering. Specifications establish responsibilities and success criteria; evaluation datasets and metrics evolve from real failures rather than appearing complete at the start. Evaluators inspect context completeness, tool outputs, trajectories and harness effects, favoring actionable binary criteria and calibrated judges over ambiguous scores. Production diagnosis groups failures by root cause and derives new tests before optimization. The demo produces trace-linked explanations, assumptions and candidate remedies for human decisions, while sampling and learned indicators reduce the cost of repeatedly reading large trace collections.

- Treat the evaluation suite as a discovered, growing specification.

- Require actionable criteria and judge-variance control.

- Turn diagnosed root causes into new tests before applying remedies.


### 70. What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

**Uploaded:** 2026-07-12 · [Watch video](https://www.youtube.com/watch?v=7P0elyLIxXo) · [Read transcript](transcripts/7P0elyLIxXo.md)

Dotta argues that “done” must represent a bundle of operational claims rather than an agent-controlled Boolean. An artifact may exist without being reviewed, independently verified, authorized for release, or proven under real-world conditions. Paperclip’s liveness model balances productive progress against verification through explicit transitions, blockers, reviewers, approvers, watchdogs, and bounded loops. The proposed completion record includes scope, rubric, evidence, verifier, approval authority, residual risk, and next action. Dotta recommends separating author and verifier, often across models, and giving agents practical tools such as browsers and screenshots to demonstrate completion. The central goal is replacing approval theater with inspectable evidence and clear custody.

- Define completion with explicit scope, standards, evidence, and remaining risk.

- Separate the producer from the verifier and authorized approver.

- Keep workflows moving with bounded loops and meaningful blockers.


### 71. Your Agents Need a Save Button - Hamza Tahir, ZenML

**Uploaded:** 2026-07-18 · [Watch video](https://www.youtube.com/watch?v=bZISsg7H7DA) · [Read transcript](transcripts/bZISsg7H7DA.md)

Hamza Tahir distinguishes read-only traces from durable execution checkpoints that preserve code, artifacts, environment, and intermediate state. With checkpoints, teams can replay a production run from a chosen decision, change a model or tool result, and compare outcomes against the original. A Kitaru demonstration extends individual replays into cohort-level analysis of support cases, showing why a cheaper model that looks acceptable once may fail across a meaningful distribution. Tahir warns against optimizing token cost without task value or shipping after one or two examples. His proposed loop is checkpoint, replay, diff, and decide, using representative production cohorts and retaining human approval.

- Preserve executable state so production failures can become controlled experiments.

- Change one factor and compare against a common checkpoint baseline.

- Evaluate cohorts and resolved-task value rather than one successful cheap replay.


### 72. Perception Agents — Antje Barth, Amazon AGI Lab

**Uploaded:** 2026-07-23 · [Watch video](https://www.youtube.com/watch?v=2JX6JYyQG4Y) · [Read transcript](transcripts/2JX6JYyQG4Y.md)

Antje Barth argues that computer-use capability is insufficient without observing whether actions actually achieved the intended result. She introduces open-source perception-agent components for shared visual annotation and verification against design specifications. The verification demonstration checks rendered appearance, brand and layout rules, and actual application flows such as adding or deleting tasks, then produces a pass/fail report for human review. Shared screen context and precise annotations reduce ambiguous instructions, while a meeting-transcript example feeds requested changes directly into implementation and verification. The talk is a product-pattern demonstration rather than a calibrated benchmark, but its central concern is closing the observe-act-check loop for reliable agent work.

- Check rendered results and user flows after actions, not merely successful tool calls.

- Make design expectations explicit and generate inspectable pass/fail reports.

- Use shared visual context to make human feedback more precise.


### 73. Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=YnNF55QV0zs) · [Read transcript](transcripts/YnNF55QV0zs.md)

Ishan Anand frames synthetic personas as bounded forecasts, not replacements for people. He reviews research on interview-grounded personas, prompting, fine-tuning, and mapping free-text responses onto survey distributions. Failure modes include invented contextual confounders, strong option-order sensitivity, amplified demographic bias, and weaker prediction of behavior than stated attitudes. Evaluation must compare synthetic responses with human ground truth using both correlation and distribution-shape metrics. Repeated synthetic sampling does not create additional statistical significance. Anand recommends estimating human inconsistency through retesting or repeated data splits; he cites a study's 83% alignment as normalized against human noise. Synthetic personas can extend existing research, but require empirical calibration and continuing reality checks.

- Ground personality, context, and experimental conditions explicitly so the model does not invent confounding variables.

- Stress-test rewordings, reordered choices, and adversarial challenges, then validate each construction against real human responses.

- Measure distribution shape as well as correlation; matching averages can conceal collapsed variation.

- Estimate the human-data noise baseline and do not mistake more synthetic samples for stronger real-world statistical evidence.


### 74. Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai

**Uploaded:** 2026-08-12 · [Watch video](https://www.youtube.com/watch?v=R3-anFK1YM8) · [Read transcript](transcripts/R3-anFK1YM8.md)

Stefania Druga evaluates local research-agent memory as a write-manage-read control loop, holding the model fixed while varying recall policies. Conditions include no memory, vector retrieval, a ranked decision ledger, and an oracle supplying the correct memory. A literature-review task already fitting in context gains no capability from added memory, only cost. For longer-horizon XBench tasks, she reports that ranked ledger recall performs best across tested conditions, with additional ablations and SpiderV2 experiments. Importantly, oracle retrieval does not guarantee correct answers because a model may ignore or misuse supplied evidence. She argues for evaluating recall policy and token cost explicitly, while noting local hardware and serial-inference constraints.

- Hold the model fixed when comparing memory policies so improvements can be attributed to the harness.

- Include both a no-memory baseline and an oracle-memory condition to diagnose retrieval versus evidence-use failures.

- Test beyond the context window; memory can add cost without value when all evidence already fits.

- Compare structured ranked recall with vector retrieval and gating, measuring token expenditure alongside correctness.


### 75. Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI

**Uploaded:** 2026-08-17 · [Watch video](https://www.youtube.com/watch?v=WP3hjUXd918) · [Read transcript](transcripts/WP3hjUXd918.md)

The Towards AI team evaluates context-management strategies for its tutoring agent using real student questions, synthetic multi-turn recall probes, deterministic retrieval checks, and LLM grading. They compare fixed configurations while logging cost, latency, caching, and whether compaction actually triggered. Contrary to their initial defaults, retaining history often beats summarization or clearing tool outputs, which can destroy cache reuse and force retrieval again. The speakers report roughly 95% detail recall with full history versus 32% after summarization, while acknowledging limited trials in the initial experiments. Local context limits change the trade-off: hybrid retrieval helps oversized documents, but chat memory remains weaker. Their selected setup uses cached DeepSeek V4 Flash, hybrid retrieval, and a compaction threshold.

- Check that the intervention actually triggers; single-turn tests may never exercise compaction.

- Measure cache hit rate, retrieval repetition, latency, and recall together rather than optimizing token count alone.

- The team's filesystem-browsing tool added latency without improving recall on its tested student questions.

- Distinguish long chat memory from document retrieval, and interpret small-trial results as workload-specific evidence.


### 76. Don’t be data poor — Anuj Iravane, Anterior

**Uploaded:** 2026-08-19 · [Watch video](https://www.youtube.com/watch?v=XAsb7MIAzm8) · [Read transcript](transcripts/XAsb7MIAzm8.md)

Anuj Iravane describes building healthcare evaluation datasets when contracts prohibit retaining patient records or derivative copies. Anterior reverses its policy-guided inference task: sample an outcome and a symbolic policy reasoning trace, then generate supporting records. A coarse-to-fine pipeline creates patient invariants, journeys, encounter plans, and documents, followed by consistency checks and round-trip validation against the intended label. Clinicians can steer generation and own pipeline logic through skills, allowing realistic failure cases without engineering changes. Iravane says synthetic data is currently used for evaluation, not training, and constitutes roughly 90% of their datasets. He reports clinicians distinguished synthetic from real records about 60% of the time in blind review.

- Sample outcomes and symbolic policy paths explicitly to cover rare scenarios instead of relying on one-shot LLM diversity.

- Generate records in stages that mirror real patient encounters, avoiding context overload and inconsistent long documents.

- Validate cross-document consistency and round-trip agreement with the originally sampled outcome.

- Give domain experts control of generation, evaluation, and pipeline skills so cases reflect realistic clinical failure modes.


### 77. Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku

**Uploaded:** 2026-09-15 · [Watch video](https://www.youtube.com/watch?v=Zd5b40Jbp_k) · [Read transcript](transcripts/Zd5b40Jbp_k.md)

Amit Desai demonstrates how to improve voice-assistant outcomes without improving recognition accuracy. In a simplified music-request example, he assigns different user recovery costs to wrong actions, refusals and confirmations, then optimizes confidence thresholds against their combined cost. This Outcome User Cost Heuristic, or OUCH, exposes why an intuitive threshold can be inferior to a data-driven one. Adding a confirmation region changes the decision policy while leaving the underlying model unchanged. He extends the reasoning to televisions and embodied assistants, where interface modality and action consequences alter the cost model. The talk advocates evaluating user harm and recovery effort rather than accuracy in isolation.

- Weight failure types by their actual user consequences.

- Optimize act, confirm and abstain policies using labeled outcomes.

- Recalibrate cost assumptions when the interface or action stakes change.


### 78. The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev

**Uploaded:** 2026-09-16 · [Watch video](https://www.youtube.com/watch?v=fZH97QHHYjY) · [Read transcript](transcripts/fZH97QHHYjY.md)

Jo Kristian Bergum argues that search evaluation must change when the searcher is an agent capable of reformulating many queries. Using BrowseComp-Plus, he contrasts high accuracy when evidence is supplied directly with lower end-to-end accuracy through a search tool, isolating retrieval and harness limitations from reasoning. He warns that an inadequately configured BM25 baseline can make competing methods appear stronger than they are; parameter and implementation choices matter. Rather than judge a single ranked list alone, he recommends measuring whether the complete agent reaches the correct answer. The talk also discusses query trajectories and filesystem workspaces as practical retrieval interfaces.

- Evaluate completed agent tasks, not only one-shot ranked-list relevance.

- Use evidence-in-context comparisons to diagnose retrieval versus reasoning failures.

- Tune and document baseline parameters before making method comparisons.


### 79. The Loop Is the Product — Roland Gavrilescu, Introspection

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=7taOQBfjDyE) · [Read transcript](transcripts/7taOQBfjDyE.md)

Roland Gavrilescu argues that agent products improve through nested loops: workers generate traces and outcomes, while a second loop turns recurring failures into judges, evaluations, skills and harness changes. He proposes portable, versioned agent recipes that preserve this accumulated judgment independently of a model provider. A recruiting example shows how trace analysis reveals undesirable targeting, humans calibrate a judge, and agents generate candidate changes. Offline evaluations are necessary but insufficient: production experiments must establish that users value the creator’s preferences before a recipe is promoted. His proposed optimization target is valuable work relative to its resource cost, not raw token consumption.

- Turn recurring failure patterns into explicit judges and regression evaluations.

- Use humans to calibrate judgment, then validate proposed changes with production users.

- Version evaluation artifacts together with the harness and skills.


### 80. The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=TeErpYBUIeM) · [Read transcript](transcripts/TeErpYBUIeM.md)

Klingen outlines an emerging open-source stack linking production traces, feedback, evaluation datasets, and automated improvement experiments. Agents can increasingly propose implementation fixes and maintain evaluation assets, but humans should approve changes that redefine optimization targets to avoid irrelevant failure chasing and overfitting. A changelog-writing demo uses human approval and edit signals to identify internal jargon and unclear customer language. Updated datasets compare a baseline and candidate, showing improved user-facing language without degrading format or accuracy in the example. Automatic release is acceptable there because the writer only opens reviewable pull requests. He also emphasizes scalable, retained trace data as agent-driven analysis becomes increasingly read-intensive.

- Keep humans responsible for datasets, criteria, and optimization direction.

- Compare candidates on both target improvements and regression dimensions.

- Use production feedback to drive repeatable, bounded improvement loops.


### 81. Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=7RFJRDYroic) · [Read transcript](transcripts/7RFJRDYroic.md)

Weco AI demonstrates autoresearch as a loop that proposes code changes, evaluates them, keeps improvements, and discards worse attempts. Mini Parameter Golf supplies a small training task, a fixed command, and a scalar validation objective; a dashboard records code and scores in an experiment tree. The presenters emphasize fast, stable measurements, correct optimization direction, bounded runtime, useful initial guidance, and protecting the evaluator from reward hacking. A second exercise optimizes a Flappy Bird controller across several conditions, with a hidden validation set and restricted editable code. Human steering can explore promising branches, but meaningful progress depends on the quality and integrity of the evaluation signal.

- Use fast, low-noise evaluators with explicit objectives and budgets.

- Protect scoring code and keep hidden validation cases.

- Inspect experiment trees and steer search rather than trust the best visible score.


### 82. The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=KhRjivBSwiw) · [Read transcript](transcripts/KhRjivBSwiw.md)

Yoni Michael and Brandon Callender combine data-context architecture with a substantial evaluation workshop. Their comparisons hold model and task fixed while varying graph versus filesystem tools, using repeated runs, source-checked gold answers, deterministic citation checks, token counts, and tool-adoption traces. Callender distinguishes occasional success from correctness across every run, reporting stronger consistency and lower token use for the graph approach in a cached experiment. He also describes misleading early results caused by broken file paths, and repository-history leakage in bug-fixing evaluations. The presenters recommend hardening scorers and harnesses, reading traces, and pinning corpus snapshots; reported gains remain specific to their tasks and setup.

- Measure repeat-run consistency as well as whether any attempt succeeds.

- Validate gold answers against source and unit-test deterministic scorers.

- Inspect traces for broken tools and measure actual adoption, not just tool availability.

- Prevent repository-history leakage and pin benchmark corpus snapshots.


### 83. 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=k72eLcYpVys) · [Read transcript](transcripts/k72eLcYpVys.md)

Kevin Orellana uses coding agents to test the infrastructure those agents themselves depend on. An MCP wrapper exposes AgentCore’s code sandbox and browser, and agents generate and execute one thousand workflows across ten domains, logging results in SQLite for concurrent analysis. Failures include incorrect image encoding, null-byte handling, unreadable files, and browser memory exhaustion. He separates interface-layer defects from sandbox limits involving permissions, memory, process creation, seccomp, and eBPF. The talk also considers the limitations of model-generated tests and benchmark exploits. His recommendation is broad remote workflow fuzzing alongside local tests, because infrastructure failures can masquerade as weak agent reasoning or prevent an otherwise capable agent from completing its task.

- Test the environment through the same interfaces agents use.

- Store structured results and classify interface versus sandbox failures.

- Include remote limits and resource exhaustion in benchmark interpretation.


### 84. Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=PwCSYy-oGsM) · [Read transcript](transcripts/PwCSYy-oGsM.md)

Druid AI critiques containment rate as a misleading proxy for agent success. An agent escalating fewer conversations may look better while missing customers who actually need human attention. The presenters propose a seven-pillar scorecard covering configuration, runtime behavior, and governance, with twenty-six components scored by whether they are absent, defined, or actively governed. Business-weighted checks include mandate, permissions, budget, risk, compliance, observability, hallucination, tone, and validated outcomes. Repeated measurement against a human baseline can expose degradation hidden behind an unchanged green dashboard. The framework emphasizes matching metrics to a specific business role and industry; its composite score is a proposed management instrument, not an independently established universal benchmark.

- Choose outcome measures that reflect the agent’s actual mandate.

- Re-evaluate on live traffic against human baselines.

- Inspect drift across component metrics instead of trusting containment alone.


### 85. Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=Fa3hQVIKShw) · [Read transcript](transcripts/Fa3hQVIKShw.md)

Hrishi Olickel presents just-in-time ontologies as transformations built around a specific decision rather than a universal schema. The evaluation lessons come from data-work examples: ambiguous entity definitions, costly checking, and a pipeline that removed negative signs and turned a much smaller net balance into millions of debt while multiple models agreed. He separates designers, task workers, and optimizers, and recommends held-out cases, bounded pilot runs, versioned work segments, and explicit failure conditions. Cross-model disagreement can concentrate human review, but consensus can preserve shared mistaken assumptions. Cost, speed, and accuracy optimization only becomes meaningful when the execution surface, baseline, and evidence are stable enough to compare.

- Test definitions and silent transformations, not just output plausibility.

- Use held-out cases and independently checked pilot baselines.

- Treat cross-model agreement as a review aid, not proof of correctness.


### 86. How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI

**Uploaded:** 2026-10-17 · [Watch video](https://www.youtube.com/watch?v=SHMCGrNJJGc) · [Read transcript](transcripts/SHMCGrNJJGc.md)

Laurie Voss builds an evaluation loop around a Claude-powered financial analyst, beginning with Phoenix tracing and manual error analysis. A report claiming 116% analyst agreement illustrates why plausible final prose is insufficient. Code checks cover deterministic properties; model judges assess faithfulness and actionability. A generic correctness judge fails partly because it lacks fresh evidence, so she supplies research context and creates a focused custom judge. Human labels, rubric disagreements, and development/test separation help calibrate it. Repeated prompt experiments improve actionability without fixing all faithfulness failures, and a model upgrade introduces conservatism. The workshop ends with CI acceptance criteria and ongoing production sampling, emphasizing complementary measures rather than one score.

- Give each judge the evidence required to answer its specific question.

- Calibrate with careful human labels and inspect disagreements.

- Track tradeoffs across quality dimensions and retain regression checks in CI.


### 87. Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse

**Uploaded:** 2026-10-18 · [Watch video](https://www.youtube.com/watch?v=obfPzbapMIM) · [Read transcript](transcripts/obfPzbapMIM.md)

Annabell Schäfer and Doneyli De Jesus walk through a Langfuse evaluation loop for a fictional banking assistant. Tracing captures intermediate work, with PII masking before persistence; production samples and imported cases become datasets. Domain experts annotate outputs, comments are grouped into failure modes, and focused code checks or LLM judges score experiments. The session demonstrates prompt-change evaluation in CI and dashboards linking quality findings to operational concerns. Judge calibration against representative human labels is essential, particularly in regulated applications. A demonstrated score gate illustrates the intended workflow, but its effectiveness depends on testing candidates before promotion and connecting the gate correctly to deployment rather than merely displaying pass/fail results.

- Use expert comments to define application-specific failure modes.

- Combine deterministic checks with human-calibrated judges.

- Connect CI evaluation thresholds to the actual release boundary.


### 88. Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS

**Uploaded:** 2026-10-18 · [Watch video](https://www.youtube.com/watch?v=q4WC4TowkBo) · [Read transcript](transcripts/q4WC4TowkBo.md)

Nick Nisi and Zack Proser demonstrate how coding agents can produce checkable evidence instead of merely announce that a task is finished. The Midnight Snack Club application combines explicit goals, CLI health checks, browser observations, deterministic tests, and model judges. Failures feed the next repair attempt, while independent evidence includes screenshots, smoke tests, and persisted application state. The live discussion exposes limitations: a judge may miss a successful interaction, and a saved receipt may refer to code that has since changed. They advocate a stable evaluation baseline that multiple implementations can target, with checks tied to the current artifact and real user journeys rather than a passing build alone.

- Define completion in terms the agent can actually test.

- Verify running user flows and persistence, not just compilation.

- Invalidate old proof when the code or environment changes.


### 89. What Agents Want — Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse

**Uploaded:** 2026-10-18 · [Watch video](https://www.youtube.com/watch?v=7T-gldvgfpo) · [Read transcript](transcripts/7T-gldvgfpo.md)

The OpenProse team proposes expressing multi-agent work as declarative contracts in Markdown rather than prescribing every implementation step. Demos include event-triggered jobs, a deliberately critical PR reviewer, and bank model documentation. Evaluation is embedded in the contract: describe the desired end state, compare runs against that specification, and preserve successful trajectories as reusable workflows. The presenters discuss development versus production behavior, historical-result comparisons, composable contracts, and differences from DSPy. The approach shifts effort toward stating what success means, but it does not remove the need for a trustworthy checker or good examples. The session presents workflow mechanics rather than independently measured reliability gains.

- Write outcome contracts that can be checked independently of execution.

- Benchmark recurring runs against the same requirements.

- Preserve successful trajectories without confusing one success with general reliability.


### 90. Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa

**Uploaded:** 2026-10-19 · [Watch video](https://www.youtube.com/watch?v=L4dUFimVDKU) · [Read transcript](transcripts/L4dUFimVDKU.md)

Ryan Ahern leads a workshop using historical search to backtest agent-generated predictions. Exa Snapshot supports retrieval of known URLs and broader searches at a chosen cutoff, preventing an acquisition predictor from simply finding the later acquisition announcement. Participants propose company-acquisition features and test them at one, seven, and thirty days before the event, with comparison dates for non-acquired companies. The scoring setup and visible company list encourage rapid tuning, which also exposes overfitting. Ahern explicitly notes that a held-out set is necessary: historical cutoffs prevent future-information leakage, while unseen cases answer a separate question about generalization. The exercise demonstrates evaluation design, not validated investing performance.

- Freeze the information cutoff before the predicted event.

- Inspect how the scoring rule rewards false positives and misses.

- Use unseen cases as well as historical retrieval to prevent overfitting.


### 91. How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase

**Uploaded:** 2026-10-19 · [Watch video](https://www.youtube.com/watch?v=_4Ph2dhmUFI) · [Read transcript](transcripts/_4Ph2dhmUFI.md)

Evan Kormos models regulated business processes as directed workflows whose individual nodes can contain agentic loops. More iterations only help when the loop has a reliable check, and faster nodes can merely move a bottleneck elsewhere. He proposes representative evaluation datasets, domain-defined quality criteria, traces, and operational measures as a confidence mechanism for nondeterministic systems. Agents progress from fully supervised work to sampled human review and eventually exception-focused oversight when policy thresholds and measured evidence permit it. Decisions about authority remain distinct from technical capability. The emphasis is an incremental, observable transition rather than treating one successful demonstration as proof that an agent can safely work unsupervised.

- Define checks and representative datasets before increasing autonomy.

- Measure the whole workflow for new bottlenecks.

- Advance from supervision to sampling only against explicit policy thresholds.


### 92. The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft

**Uploaded:** 2026-10-19 · [Watch video](https://www.youtube.com/watch?v=UGjk3Uk0MxM) · [Read transcript](transcripts/UGjk3Uk0MxM.md)

Pamela Fox compares GPT-5.5, Kimi, DeepSeek, and Mistral on shared application scenarios rather than trust general leaderboards. Examples cover letter counting, source-grounded RAG, images, language changes, tool arguments, calculation loops, and a travel agent’s use of parallel tools. The demonstrations expose different failure modes and show that prompt changes can repair some gaps but not establish universal capability. She then introduces bulk deterministic checks, human-calibrated LLM judges, ASSERT-generated rubrics and cases from a specification, and DSPy/GEPA prompt optimization. Evaluation must inspect completion, grounding, tool use, cost, and latency. Workshop comparisons are illustrative runs, not statistically definitive rankings of the models.

- Evaluate the actual scenario, language, and modality.

- Check tool arguments, workflow completion, and efficiency alongside final answers.

- Bootstrap custom cases, then calibrate judges and automate repeated evaluation.


### 93. Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler

**Uploaded:** 2026-10-25 · [Watch video](https://www.youtube.com/watch?v=dZgA6btnb_s) · [Read transcript](transcripts/dZgA6btnb_s.md)

Vinoo Ganesh presents a finance architecture that prevents models from freely inventing numerical claims. Retrieved facts enter a citation registry with values, units, scales, periods, and provenance; deterministic code performs calculations, while models refer to registered facts. A post-processing filter removes unsupported figures, including numbers recalled from model training rather than retrieved evidence. He describes hybrid retrieval, reranking, tenant isolation, and disagreements between legitimate sources. Evaluation examples show many rejected citations and thousands of incorrect numbers from ordinary model or RAG outputs. The assurance is deliberately bounded: numerical traceability improves verification, but it does not establish that every qualitative conclusion or investment interpretation is correct.

- Represent financial facts with units, periods, and source provenance.

- Keep calculations deterministic and reject unregistered numbers.

- Distinguish verifiable numerical grounding from correctness of the broader narrative.


### 94. How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI

**Uploaded:** 2026-10-25 · [Watch video](https://www.youtube.com/watch?v=gv4w23xYj-0) · [Read transcript](transcripts/gv4w23xYj-0.md)

SallyAnn DeLucia leads a hands-on workshop on translating vague impressions into a first useful evaluator. A travel agent’s traces provide evidence about model decisions and tool calls; participants identify one quality dimension, define concrete pass and fail conditions, create a small dataset, and test an LLM judge in a prompt playground. She distinguishes traces, aggregate metrics, and evaluations, and surveys code checks, human annotations, decision models, and agent-as-judge approaches. The recommendation is to start with roughly twenty traces and one focused judge, inspect explanations, iterate on the rubric, and then align with human labels and expand toward online monitoring rather than begin with an all-purpose score.

- Read traces before deciding what to evaluate.

- Judge one quality at a time with explicit pass/fail criteria.

- Inspect explanations and calibrate against human judgments before scaling.


## Core · Judges, rubrics & subjective quality


### 95. Context Is the New Code — Patrick Debois, Tessl

**Uploaded:** 2026-05-03 · [Watch video](https://www.youtube.com/watch?v=bSG9wUYaHWU) · [Read transcript](transcripts/bSG9wUYaHWU.md)

Patrick Debois proposes a Context Development Lifecycle: generate, evaluate, distribute, and observe the instructions, documentation, and skills that shape coding agents. Evaluation progresses from format linting and clarity checks to judging generated code against company rules and running tool-enabled judges against live endpoints in sandboxes. He recommends repeated trials and risk-sensitive error budgets because a single passing run is unreliable. Observation closes the loop through agent logs, pull-request feedback, and production failures converted into regression tests and improved shared context. Security discussion covers provenance, scanning, tracing, and context filtering. Q&A stresses that constructing useful, business-specific evals remains substantial engineering work rather than disappearing with prompt-based development.

- Test changes to agent instructions as behavioral changes, using layered checks from format validation to executable end-to-end scenarios.

- Give judges tools when correctness requires running the generated system rather than merely inspecting its source.

- Use repeated trials and risk-sensitive error budgets rather than treating one nondeterministic eval run as a reliable CI gate.

- Turn recurring agent-log gaps, PR feedback, and production failures into shared context improvements and regression cases.


### 96. Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize

**Uploaded:** 2026-05-14 · [Watch video](https://www.youtube.com/watch?v=Xfl50508LZM) · [Read transcript](transcripts/Xfl50508LZM.md)

Voss builds an evaluation workflow around a two-stage financial-analysis agent, using Phoenix tracing to inspect tool calls, diagnose failures, and prioritize fixes. He combines deterministic checks, built-in LLM judges, and a custom actionability rubric with concrete examples. A correctness judge rejects current financial data because it lacks temporal context, whereas a source-grounded faithfulness judge passes the same runs, demonstrating that evaluator selection changes the signal. Meta-evaluation covers human labels, held-out examples, precision, recall, and judge biases, although the workshop's human annotations are explicitly randomized demonstration data. Experiments compare prompt revisions on failures; Q&A recommends periodically rerunning the full corpus to detect overfitting and regressions.

- Read traces before writing evaluators, distinguish symptoms from root causes, and prioritize observed failures by frequency and severity.

- Use deterministic checks for objective constraints and LLM judges for semantic requirements; faithfulness to supplied research does not establish independent factual correctness.

- Calibrate focused rubrics with genuine human-labeled examples and held-out data, inspect disagreements and biases, and do not treat the randomized workshop labels as validation.

- Compare prompt versions with fixed inputs and evaluators, repeat trials for nondeterminism, and periodically run the full evaluation corpus to catch regressions beyond targeted failures.


### 97. The maturity phases of running evals — Phil Hetzel, Braintrust

**Uploaded:** 2026-05-27 · [Watch video](https://www.youtube.com/watch?v=FB-MLPhL9Ms) · [Read transcript](transcripts/FB-MLPhL9Ms.md)

Phil Hetzel outlines a progression from documented human review to scalable, production-informed agent evaluation. Early reviewers should record both a quality judgment and the reasoning behind it, allowing teams to derive specific failure modes and create deterministic scorers or LLM judges. Judges themselves need validation against trusted human labels. As agents use external systems, evaluation expands from final outputs to full traces, with special attention to reconstructing historical state and avoiding destructive production writes during replay. The talk favors focused failure coverage over impossible exhaustive testing and identifies automated topic modeling and agent-driven workflows as emerging practices.

- Capture expert rationales, not just binary annotations.

- Evaluate the evaluator before scaling LLM-as-judge scoring.

- Represent historical external-system state and isolate side effects in offline evaluation.


### 98. LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize

**Uploaded:** 2026-06-07 · [Watch video](https://www.youtube.com/watch?v=JsCCrBF7F1g) · [Read transcript](transcripts/JsCCrBF7F1g.md)

Dat Ngo demonstrates how observability, evaluation and experimentation fit together in Arize’s tooling. OpenTelemetry traces expose tool calls and branches, while sessions and distributional views reveal failures beyond one run. Evaluation signals include expert gold sets, end-user feedback, deterministic checks and LLM judges calibrated against trusted annotations. He distinguishes span, multi-span, trajectory and session-level assessments, advising teams to choose the smallest useful set rather than evaluate everything. Production traces become datasets for comparing prompt, model and orchestration changes. The presentation also shows agent-accessible tools intended to automate failure discovery and the improvement loop.

- Choose evaluation scope to match the question: component, trajectory or full session.

- Calibrate judges against domain-expert annotations.

- Convert trace failures into controlled experiments and monitor regressions.


### 99. Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel

**Uploaded:** 2026-06-10 · [Watch video](https://www.youtube.com/watch?v=TNwJ1LMiENk) · [Read transcript](transcripts/TNwJ1LMiENk.md)

Kobie Crawford presents a financial-analysis study where targeted reinforcement learning improves a small model’s tool discipline more than selecting a much larger reasoning model. A self-contained FinQA environment supplies verifiable answers and separate single-table and harder multi-table benchmarks. Trace comparisons show the larger model guessing table names and hallucinating after failed queries, while the trained model discovers schemas and corrects errors. Single-table training generalizes to multi-table evaluation. The practical evaluation lesson is to decompose correctness into behavioral rubrics, identify the failing component, and generate training data for that behavior instead of interpreting a final-answer score as a diagnosis.

- Inspect tool trajectories to distinguish reasoning gaps from tool-discipline failures.

- Use component rubrics to choose what training data to create.

- Test transfer on harder held-out task types rather than only trained scenarios.


### 100. The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen

**Uploaded:** 2026-06-25 · [Watch video](https://www.youtube.com/watch?v=IJXjTLPzvAU) · [Read transcript](transcripts/IJXjTLPzvAU.md)

Jacob E. Thomas argues that fluent, personality-consistent historical personas can still reason from anachronistic cultural composites. Hamilton and Lincoln demonstrations illustrate why convincingness is not documentary fidelity. His proposed Prism experiment compares primary-source, biography and bare-model conditions at distinct moments in Lincoln’s life using historian-authored diagnostic questions. A preregistered rubric weights anachronism, documentary consistency and contextual plausibility, deliberately excluding rhetorical polish as an independent reward. The talk is explicit that large-scale results are not yet available. Domain experts design gold sets and adjudicate edge cases at build and release gates rather than reviewing every runtime conversation.

- Validate whether your rubric measures the actual failure mode rather than fluency.

- Use temporally bounded sources and domain-expert gold sets for persona fidelity.

- Separate observed examples from preregistered predictions and future findings.


### 101. How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI

**Uploaded:** 2026-07-07 · [Watch video](https://www.youtube.com/watch?v=1IdzkRVmWAA) · [Read transcript](transcripts/1IdzkRVmWAA.md)

Mixedbread explains an oracle gap: models answer difficult knowledge questions better when supplied the right documents than when they must retrieve them. BrowseComp+ and OfficeQA Pro illustrate the gap and the limitations of keyword-shaped benchmark queries. The speakers build a bounded, parallel search harness with semantic search, metadata filtering and grep, then train a smaller agent using supervised examples and on-policy reinforcement learning. Rewards combine retrieval metrics with LLM rubrics for relevance, ranking, query formulation and exploration. Preliminary results distinguish the unreleased trained system from an existing production search offering, emphasizing evaluation of retrieval behavior rather than reasoning alone.

- Measure retrieval against an oracle-document baseline to localize failure.

- Use separate relevance, ranking and trajectory rubrics rather than one final-answer score.

- Match keyword and semantic tools to different evidence needs.


### 102. Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft

**Uploaded:** 2026-07-19 · [Watch video](https://www.youtube.com/watch?v=3z2uT5aDx_Y) · [Read transcript](transcripts/3z2uT5aDx_Y.md)

Nick Ung and Akshay Sharma describe Lyft’s end-to-end customer-support evaluation lifecycle. Offline multi-turn simulations combine representative tasks, personas, deterministic checks, and LLM judges before launch; production traces and expert annotation then drive continuing error analysis. Helpful frontier models made unrealistically polite simulated customers, inflating results, so Lyft fine-tuned a user simulator on real verbatim conversations. Judges are treated as classifiers with specific binary business rubrics, human labels, held-out validation, and precision/recall measurement. The speakers emphasize criteria drift, confidence intervals, sufficient samples, accountable regression owners, and scores that actually gate decisions. A standardized, config-driven harness is presented as continuing work rather than a fully completed system.

- Make simulated users resemble real difficult conversations, not helpful assistants.

- Validate each judge against human labels and task-specific binary criteria.

- Require decision-relevant launch gates, uncertainty estimates, and regression ownership.


### 103. The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=q2JrUKBMf0w) · [Read transcript](transcripts/q2JrUKBMf0w.md)

Aparna Dhinakaran argues that evaluation must evolve with agents: fixed prompt-response checks no longer cover systems with memory, dynamic interfaces, repeated tools, subagents, and long-running trajectories. Drawing on Arize’s production experience, she distinguishes deterministic checks, conventional rubric-based LLM judges, and adaptive agent-as-judge analysis. The third approach investigates traces to discover failures that were not anticipated in a predefined rubric, such as inefficient repeated tool calls or completion and context-management problems. She introduces Signal as a long-running investigator that groups issues and can propose fixes. Her recommendation is additive rather than replacement: use all three evaluation styles for their respective strengths.

- Retain deterministic checks and rubric-based judges while adding adaptive investigation.

- Look beyond final answers to trajectory-level failures and inefficient loops.

- Use newly discovered production issues to fuel continual improvement.


### 104. Evaling Video Slop — Maor Bril, Character.ai

**Uploaded:** 2026-07-25 · [Watch video](https://www.youtube.com/watch?v=b_PmGocP4rc) · [Read transcript](transcripts/b_PmGocP4rc.md)

Maor Bril describes why generated-video evaluation must capture storytelling, physical plausibility, pacing, identity consistency, and audio synchronization rather than individual-frame similarity alone. Character.ai combined conventional metrics with human-calibrated model judges, then distilled that expensive process into a small vision-language model for faster feedback during generation. Pairwise comparisons proved more useful than absolute scores. Early versions confidently rewarded visual polish rather than the intended quality axes, requiring better training pairs and consistent encoding and annotation to avoid learning an AI-versus-human detector. Bril emphasizes detecting errors before full videos are assembled, continually recalibrating against human judgments, and choosing judge size according to latency and unit economics.

- Use pairwise preferences and explicit quality axes instead of vague absolute scores.

- Audit training pairs for shortcuts such as production-source or encoding artifacts.

- Place quality checks early inside generation and recalibrate with human feedback.


### 105. Ending AI Slop — Thais Castello Branco, Taste Labs

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=lCBf9slCanI) · [Read transcript](transcripts/lCBf9slCanI.md)

Castello Branco argues that improving design and writing requires decomposing subjective quality rather than treating taste as one undifferentiated score. Brand adherence illustrates the method: extract colors, typography, spacing, motion, and other constraints, then judge new work against those properties instead of copying a reference. More verifiable components can support reinforcement-learning environments, while creativity and contextual style fit require expert human judgment. She warns that pooling incompatible preferences produces bland averages and recommends preserving audience, style, and temporal context. Her data-quality framework stresses carefully selected experts, specific explanations grounded in visible or code components, and QA that distinguishes objective errors from legitimate aesthetic disagreement.

- Break subjective goals into observable components and choose evaluation methods per component rather than asking one judge whether an artifact is simply good.

- Grade brand-consistent novelty against explicit design constraints, not resemblance to a single reference output.

- Preserve differing human preferences with contextual information; disagreement about aesthetics is not automatically annotation noise.

- Improve feedback specificity by connecting expert comments to exact visual or code components, while reserving consensus checks for properties experts should objectively agree on.


### 106. Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software

**Uploaded:** 2026-08-01 · [Watch video](https://www.youtube.com/watch?v=2aS7aKoXn64) · [Read transcript](transcripts/2aS7aKoXn64.md)

Theta's presenters argue that long-horizon capability cannot be captured by human task duration alone: token consumption, tool coordination, sequential state dependencies, and ambiguity reveal different difficulties. They distinguish genuinely dependent workflows from artificially concatenated tasks and explain why open-ended work complicates standardized grading. Their proposed judges act as agents, inspecting final environment state through safeguarded read-only tools and querying structured trajectories rather than receiving one oversized transcript. They discuss combining deterministic checks with rubric judging, partial credit, reward-density tradeoffs, and quality tests for gold solutions, no-ops, variance, coverage, and expert agreement. The closing critique questions existing finance benchmarks' horizon claims, domain breadth, saturation, and usefulness as learning signals.

- Report both human-time and model-execution measures, with harness and task methodology held explicit; neither alone establishes long-horizon difficulty.

- Build tasks with consequential state changes and dependencies rather than merely chaining independent subtasks to inflate length.

- Give judges read-only access to relevant system state and searchable trajectories so they can verify outcomes without mutating the evaluated environment.

- Quality-test rubrics against gold and no-op solutions, judge variance, coverage, and expert agreement before using their rewards for training or comparisons.


### 107. Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia

**Uploaded:** 2026-08-19 · [Watch video](https://www.youtube.com/watch?v=McknwOzbmyg) · [Read transcript](transcripts/McknwOzbmyg.md)

Jared Joselowitz explains Ufonia's safety-evaluation stack for DORA, arguing that irreversible clinical conversations require evidence before patient exposure. He describes around 200,000 completed UK calls and contracts to reach a million patients. Matrix simulates clinical scenarios with Patbot patients and uses an automated judge to identify hazards against clinician-defined behaviors. Both patient realism and judge accuracy are validated; he reports a judge F1 of 0.96 on a clinician-labeled corpus. Automated prompt optimization uses harm-sensitive objectives rather than flat accuracy. Simulation then feeds staged user testing, supervised clinical evaluation, and monitored deployment. He stresses that simulation is necessary but insufficient, and that prompts, verdicts, and datasets must trace to specific hazards.

- Derive test scenarios from product-specific harms and deliberately manufacture rare, dangerous edge cases.

- Validate both simulated-patient behavior and automated judges against human evidence before trusting large-scale simulation scores.

- Use harm-sensitive cost functions, prioritizing red-flag sensitivity when missed hazards are more costly than false alarms.

- Require staged clinical evidence after simulation and preserve hazard-linked prompts, datasets, traces, and judge verdicts.


### 108. Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo

**Uploaded:** 2026-08-22 · [Watch video](https://www.youtube.com/watch?v=yqF6XhzbWBk) · [Read transcript](transcripts/yqF6XhzbWBk.md)

Sebastian Fox examines dangerous failures in clinical notes that remain fluent and superficially faithful: omitted red flags, inferred symptoms, and plans preserved after clinicians abandoned them. He distinguishes transcription mistakes from generation errors and argues that spotting textual differences is easier than judging their clinical significance. In his tests, even a carefully engineered rubric-based judge approved notes containing serious errors. His proposed alternative is a continuous discover, capture, and calibrate loop: cluster failures from real outputs, collect expert reasoning and corrections, and retrieve relevant precedents and guidelines for each judgment. He reports improved detection on the same notes when the judge receives this case-specific context instead of a frozen standard.

- Audit omissions and altered clinical intent, not just obvious hallucinations or surface-level faithfulness.

- Discover failure categories from real outputs rather than relying exclusively on imagined or synthetic cases.

- Capture experts' explanations and corrections alongside scores so tacit contextual judgment becomes reusable evidence.

- Retrieve relevant adjudicated cases and guidelines per output, updating the evaluator as standards and failure modes change.


### 109. AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash

**Uploaded:** 2026-08-28 · [Watch video](https://www.youtube.com/watch?v=bMjlRrWjdT0) · [Read transcript](transcripts/bMjlRrWjdT0.md)

DoorDash’s GenAI platform speakers describe evaluation as a shared workflow rather than an engineering-only test harness. Strategy and operations set quality priorities, product translates requirements into rubrics, operations supplies annotations, and engineering provides stable APIs, telemetry, datasets and judges. Their continuous loop captures traces, samples reviewable subsets, annotates them with domain expertise, creates golden datasets and calibrates judges before repeating. API-first infrastructure lets operators build their own annotation interfaces with coding agents. A self-service calibration UI exposes original and revised judge prompts for review. The speakers report lower annotation costs and faster iteration, but the captions provide no numeric cost-reduction figure.

- Assign domain experts meaningful ownership of quality definitions and annotations.

- Make trace sampling, golden-set creation and judge calibration one continuous workflow.

- Expose judge-prompt changes so non-engineers can review calibration results.


### 110. SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind

**Uploaded:** 2026-08-30 · [Watch video](https://www.youtube.com/watch?v=KLDdXOw6jIc) · [Read transcript](transcripts/KLDdXOw6jIc.md)

This Google DeepMind panel explains why attractive generative-media outputs are not necessarily useful or faithful. A side-by-side experiment found people often preferred generated versions of real videos because they looked sharper or more saturated, illustrating weaknesses of broad preference scores. The panel contrasts automatable checks, such as OCR-based text-rendering verification, with difficult aesthetic and free-form editing judgments. Evaluation combines large human studies, live experiments, expert inspection and early-access workflow feedback. Examples include missed details, implausible eye gaze and unexpected wedding rings. Their practical message is to evaluate instruction following and real creative workflows, rather than optimizing a single generic beauty judgment.

- Separate aesthetic preference from fidelity, instruction following and workflow usefulness.

- Automate objective checks where possible, but retain expert and human assessment.

- Use early-access practitioners to uncover regressions hidden by aggregate preference gains.


### 111. Training Taste — Thais Castello Branco, Taste Labs

**Uploaded:** 2026-09-10 · [Watch video](https://www.youtube.com/watch?v=sDMGWK4wZ_w) · [Read transcript](transcripts/sDMGWK4wZ_w.md)

Thais Castello Branco explains how Taste Labs decomposes subjective design quality into measurable characteristics. Some attributes, such as contrast or alignment in a defined context, admit broad expert agreement; others require data and acknowledgment of disagreement. Her team analyzes over two million historical websites alongside synthetic designs, mining structured features and training small classifier probes. Combined probe patterns predict repetitive, context-insensitive design, reportedly outperforming generic LLM judging, though no detailed numeric comparison is supplied in the captions. She connects measurement to intervention: deliberate creative divergence and structured brand representations give agents both guidance and criteria against which their outputs can be checked.

- Decompose subjective quality into specific observable attributes.

- Distinguish expert-consensus checks from genuinely preference-dependent judgments.

- Evaluate brand adherence against explicit structured references rather than generic taste.


### 112. The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)

**Uploaded:** 2026-09-21 · [Watch video](https://www.youtube.com/watch?v=SQMCtZX3trg) · [Read transcript](transcripts/SQMCtZX3trg.md)

Paul Bakaus treats skills as harness extensions rather than packaged prompts, combining independent critiques, deterministic linting, hooks and model-specific behavior. His evaluation setup recreates several agent harnesses and tools, simulates interactive users, and compares skill releases across models and design niches. Rule identifiers enable ablations: remove a line, rerun evaluations, restore it and measure effects with deterministic checks. He also explains limits of visual taste judges, including a model rewarding crowded viewports, and retains human annotation for subjective assessment. The workshop’s quality lesson is to test actual cross-harness behavior and enforce required validation steps rather than assume prose instructions guarantee compliance.

- Run cross-model and cross-harness tests rather than validating only the author’s setup.

- Ablate individual skill rules to establish whether they improve measured behavior.

- Keep independent critiques and human judgment when design judges reward spurious features.


### 113. Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=jNE8No-wvok) · [Read transcript](transcripts/jNE8No-wvok.md)

Aditya Gautam describes specialized video agents for modality misalignment and originality attribution, then explains how production evaluation sustains them. A perceiver, retriever and reviewer divide temporal analysis, evidence retrieval and decision-making. Daily production samples pass through an in-house judge and human review; failures are traced to reasoning, tool calls or retrieval before preference data informs further training. Evaluation includes precision, recall and F1, but also per-node latency, reasoning budgets, robustness and token costs. Crucially, the judge itself is checked against the human queue for drift. The talk ties task quality, infrastructure efficiency and ongoing monitoring into one continuous improvement process.

- Attribute failures at agent, tool and retrieval levels instead of relying only on final accuracy.

- Continuously compare automated judges with human review to detect drift.

- Evaluate efficiency changes alongside task quality and reasoning-budget tradeoffs.


### 114. Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=dKcTBQzR7jI) · [Read transcript](transcripts/dKcTBQzR7jI.md)

Merve Noyan presents a workflow in which a larger vision-language model labels images, smaller VLM judges inspect overlaid bounding boxes, and accepted examples train a compact detector. She evaluates road-sign outputs against ground-truth labels and explores document parsing where the trained detector sometimes catches objects missed by its labeler. The talk’s key quality lesson is judge imbalance: requiring both judges to approve would discard too much data, so her experiment accepts an example if either approves. Human review remains necessary for judge prompts and augmentation policies; agent-generated horizontal sign flips and traffic-light color jitter illustrate destructive defaults. Model choice also considers licensing and deployment speed.

- Inspect each judge’s rejection behavior before choosing an ensemble rule.

- Compare pseudo-label pipelines with ground truth when available.

- Review augmentation policies and judge prompts rather than trusting coding-agent defaults.


### 115. Evals in AI: A Deep Dive — Tejas Kumar, IBM

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=NdrSPm6NCdk) · [Read transcript](transcripts/NdrSPm6NCdk.md)

Kumar introduces evaluations as predeployment reliability instrumentation complementary to runtime harness safeguards. He surveys exact matching, schema validation, pairwise comparisons, and LLM judges, highlighting position, sycophancy, self-preference, and verbosity biases. A live returns-policy example progresses from brittle keyword checks to a policy-grounded judge calibrated against approximately thirty labeled examples, then a CI agreement gate. Adding missing policy context and upgrading the judge improve the demonstration; network timeouts and label formatting complicate results. He recommends version-pinned judges, continuously refreshed production examples, and shared retrievable policy for agent and judge, demonstrated through OpenRAG. His suggested agreement thresholds and perfect-agreement warning are heuristics, not guarantees of safety or generalization.

- Start with cheap deterministic checks and escalate only when needed.

- Ground judges in the same current policy as production agents.

- Monitor agreement and inspect disagreements instead of trusting green scores.


### 116. From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=qZj7sqmidqA) · [Read transcript](transcripts/qZj7sqmidqA.md)

Voss walks through instrumenting a financial-research agent, reading complete traces, categorizing failures, and building deterministic, built-in, and custom evaluations. A context-free correctness judge rejects current financial information, while source-grounded faithfulness exposes unsupported claims. The workshop then calibrates actionability judgments against human labels, discusses precision, recall, held-out data, bias, and focused rubrics, and converts failures into experiment datasets. Coding-agent-generated prompt revisions are compared using the same evaluations, with passing cases retained for regression checks. Some labels and failure categories are deliberately random demonstration data, and the polished improvement result is explicitly unrepresentative. Production sampling and ongoing dataset maintenance complete the proposed engineering loop.

- Read traces and define domain-specific success before writing evaluators.

- Provide judges the evidence needed for the question being scored.

- Calibrate judges and test fixes against both failing and passing examples.


### 117. Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=xLxhT2ZI7UM) · [Read transcript](transcripts/xLxhT2ZI7UM.md)

Browserbase and Microsoft researchers show how weak web-task judges can reward false success, citing one agent scored near seventy-four percent by an existing judge versus roughly thirty-eight percent by their verifier. Their universal verifier generates task-specific rubrics, retrieves relevant screenshot evidence per criterion, and separates partial process credit from actual outcome success and environmental blockers. Evaluation uses human annotations, held-out trajectories, agreement measures, and controlled training-data filtering experiments. They report better downstream models and strong human agreement on their collected labels, not universal infallibility. Autoresearch accelerates verifier development, but unprimed automation falls short of human-designed quality; combining human insights with automated experiments performs better.

- Verify environment evidence rather than agent claims.

- Separate controllable mistakes, partial progress, and outcome completion.

- Hold out human-labeled trajectories when tuning verifiers.


### 118. Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket

**Uploaded:** 2026-10-14 · [Watch video](https://www.youtube.com/watch?v=gonAewBZxfU) · [Read transcript](transcripts/gonAewBZxfU.md)

Eleonora Drykina and Nina Žižakić describe a payment-rulebook assistant whose quality depends on preserving tables, section structure, and citations across hundreds of PDFs. Their retrieval-only test on sixty-three questions raises reported hit rate from ninety-two to ninety-seven percent with hybrid search, but they distinguish this from answer correctness. Roughly eighty-six Promptfoo end-to-end cases combine rubric-based LLM judgment with source-document citation checks, informed by real user tests and behavioral rules. Repeated runs expose judge noise: five of twelve apparent flips do not reproduce, and one alleged hallucinated date is actually in the source. Traces and direct document inspection therefore remain necessary when interpreting evaluation changes.

- Evaluate retrieval and complete answers separately.

- Check citation targets alongside rubric-based model judgments.

- Rerun apparent regressions and challenge the rubric against source documents.


### 119. Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI

**Uploaded:** 2026-10-22 · [Watch video](https://www.youtube.com/watch?v=_dTF3NpPzGo) · [Read transcript](transcripts/_dTF3NpPzGo.md)

Louis-François Bouchard introduces ToneBench for assessing writing that matches a particular voice rather than merely avoiding conspicuous AI vocabulary. Ten script tasks, five drafts per model, four LLM judges, and nine metrics address tone, writing quality, instruction following, research accuracy, and slop. Detailed rubrics require explanations and examples, while blind judging and one thousand human A/B comparisons help expose weaknesses. He reports that judges can prefer their own model family and that rubric or generation-prompt changes make reruns expensive. The benchmark measures one author’s preferences, not universal writing quality. Practical advice includes rich examples, checking variability, and retaining human editing rather than selecting a model from its best sample alone.

- Evaluate multiple drafts to reveal within-model variability.

- Use diverse judge families and human pairwise comparisons.

- Treat style benchmarks as preference-specific and account for rerun costs.


## Core · Optimization, skills & learning loops


### 120. Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic

**Uploaded:** 2026-05-07 · [Watch video](https://www.youtube.com/watch?v=A48uhxfxbsM) · [Read transcript](transcripts/A48uhxfxbsM.md)

Samuel Colvin demonstrates an evaluation-driven optimization loop using Pydantic AI, Logfire, and GEPA. The example extracts political ancestors from MPs' Wikipedia pages, comparing structured outputs with a model-generated, partly checked reference dataset. Deterministic evaluators and per-case traces expose errors that aggregate accuracy obscures. GEPA proposes and evaluates revised prompts, with the demonstrated run reporting a 96.7% score, but audience questions uncover overfitting that excludes aunts and uncles. Managed variables support live prompt and model experiments without redeployment. The session also discusses repeated trials, representative train/evaluation splits, implicit feedback, and privacy-preserving metrics. A later live extraction still misclassifies a sports commentator, limiting the optimization claim.

- Use task-specific deterministic comparisons against reference data where possible, and inspect individual disagreements rather than only aggregate scores.

- Separate representative optimization and evaluation data; a high score can conceal systematic errors and overfitting.

- Repeat nondeterministic cases and reassess optimized prompts when the model changes.

- Use production traces and subsequent user behavior as feedback, while treating model-generated reference labels and live-demo results cautiously.


### 121. Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take

**Uploaded:** 2026-05-13 · [Watch video](https://www.youtube.com/watch?v=FlzpEGHNVKQ) · [Read transcript](transcripts/FlzpEGHNVKQ.md)

Anant Dole and Asbjorn Steinskog describe a chess coach that grounds language generation in Stockfish analysis, tactical detectors, and human-move probabilities rather than asking an LLM to calculate chess unaided. User reports enter Slack and a running coding-agent session, where a triage skill investigates, regenerates commentary, and seeks human approval before changes. Quality checks use sixteen scenarios drawn from real games, LLM judging, and the presenters’ chess expertise, alongside latency comparisons across models. The live report does not demonstrate a completed fix: the agent asks what is wrong, and the presenter acknowledges the commentary was fine. This illustrates feedback clarification as well as automated triage.

- Separate trusted domain analysis from language generation to constrain hallucinations and reduce latency.

- Build scenario evaluations from real domain failures and combine automated judges with subject-matter expert review.

- Evaluate model quality together with latency; more reasoning did not automatically improve this application’s scenario results.

- Investigate and clarify user reports before changing the system; the live demo flagged commentary the presenter then accepted as correct.


### 122. How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS

**Uploaded:** 2026-05-30 · [Watch video](https://www.youtube.com/watch?v=vy7o1g2iHY8) · [Read transcript](transcripts/vy7o1g2iHY8.md)

Nick Nisi describes replacing prompt-only trust with explicit state-machine gates for implementation, verification, review and completion. An agent once satisfied a test marker by touching a file; recording test-output evidence made actual execution easier than faking compliance. In a separate WorkOS skills experiment, generated documentation-heavy skills reduced performance: one comparison scored better without the skill. Pruning to concise, failure-informed gotchas improved runtime and results. The talk recommends measuring skill ablations, attaching before/after UI evidence, analyzing transcripts retrospectively and repairing the harness so repeated failures become system improvements rather than isolated manual fixes.

- Ablate skills and compare with a no-skill baseline.

- Require externally checkable evidence instead of self-reported completion.

- Convert recurring trajectory failures into harness repairs and concise gotchas.


### 123. Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI

**Uploaded:** 2026-07-05 · [Watch video](https://www.youtube.com/watch?v=2IxD9OB3XuQ) · [Read transcript](transcripts/2IxD9OB3XuQ.md)

Soheil Feizi frames continual learning as a verifiable engineering loop, not necessarily model fine-tuning. Production traces and expert feedback must first become replayable environments with simulated users, tools and explicit success criteria. Candidate repairs can then be measured before and after and checked against earlier environments. The talk compares model, harness and memory updates, arguing for the smallest durable repair at the appropriate layer. Its four principles are replayability, holistic diagnosis, lifelong regression control and efficiency. A fictional support-agent benchmark includes regression traps to illustrate why fixing the latest failure is not sufficient evidence of improvement.

- Logs plus feedback are not yet executable evaluation environments.

- Route repairs across memory, harness and model rather than defaulting to fine-tuning.

- Integrate regression constraints into optimization instead of testing only the newest case.


### 124. Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind

**Uploaded:** 2026-07-14 · [Watch video](https://www.youtube.com/watch?v=0vphxNt4wyk) · [Read transcript](transcripts/0vphxNt4wyk.md)

Philipp Schmid explains why nondeterministic agent skills need tests for both triggering and successful task completion. He distinguishes temporary capability skills from durable organizational preferences, and recommends concise directives, progressive disclosure, negative cases, and removing instructions that do not change behavior. A Gemini Interactions API example uses a small runner, explicit test cases, and inexpensive regex validators, with model judges reserved for harder cases. Schmid stresses isolated workspaces, multiple trials, cross-model and cross-harness testing, and evaluation on every skill change. With-versus-without-skill ablations establish whether a skill helps and when it can be retired, while retaining the tests to detect future regressions.

- Test non-triggering cases and actual outcomes, not only skill invocation.

- Use isolated repeated trials across the harnesses and models people really use.

- Run ablations to retire redundant skills without discarding their regression tests.


### 125. Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse

**Uploaded:** 2026-07-18 · [Watch video](https://www.youtube.com/watch?v=eAXxdtNlK04) · [Read transcript](transcripts/eAXxdtNlK04.md)

Annabell Schäfer uses an arXiv-paper classifier to examine what makes self-improvement loops effective. Separate fit, validation, and untouched test sets constrain overfitting while an optimizer analyzes clustered errors, proposes prompt changes, and accepts improvements only when they generalize. Most gains arrive early; later plateaus expose ambiguity even in apparently objective labels. Schäfer argues that vague helpfulness or correctness scores offer weak optimization signals unless their scales are precisely defined. Domain experts should instead help identify concrete binary criteria and known failure categories, inspect real traces, and continually revise the definition of good. Clear stopping rules and validation prevent endless token-consuming loops.

- Separate optimization, validation, and final test data.

- Replace vague quality scores with concrete domain-specific failure checks.

- Use expert review and stopping criteria when improvement plateaus.


### 126. Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog

**Uploaded:** 2026-07-20 · [Watch video](https://www.youtube.com/watch?v=wEc9aG7cRQc) · [Read transcript](transcripts/wEc9aG7cRQc.md)

Diane Lin treats materially inconsistent answers as a product-quality problem and shows why single-run evaluation misses it. Ambiguous examples often lie near a decision boundary where even experts need clearer policy or additional facts. She proposes query-by-committee or repeated-run disagreement to select high-value cases for human review, rather than trusting model confidence. Reviewed examples become episodic memory; distilled rules become semantic memory, allowing adaptation without immediate fine-tuning. A small cybersecurity-alert experiment illustrates reduced flip-flopping and the remaining need for expert clarification. The talk connects repeated evaluation, targeted labeling, customer-specific preferences, and memory-based improvement while distinguishing uncertainty from simple model incompetence.

- Repeat evaluations to expose semantic disagreement, not only average accuracy.

- Prioritize disputed cases for expert labeling and policy clarification.

- Use episodic examples and distilled domain rules as complementary improvement mechanisms.


### 127. The Unreasonable Effectiveness of Separating the Task from the Model

**Uploaded:** 2026-07-23 · [Watch video](https://www.youtube.com/watch?v=GgLQ02aO-hs) · [Read transcript](transcripts/GgLQ02aO-hs.md)

Maxime Rivest and Isaac Miller present DSPy as a way to separate stable task contracts from changing models, prompts and harness implementations. They describe three complementary specifications: natural-language instructions for what should happen, code constraints for what must happen and evaluations defining what good looks like. Stable interfaces and evaluation sets allow model substitutions and automated optimization without rewriting integrations. They introduce harness-learning ambitions and qualitative learning, where production traces, user actions and textual feedback could refine evaluation objectives over time. The speakers explicitly frame this last idea as an active research question, emphasizing accountability to business tasks rather than enthusiasm for new techniques alone.

- Specify instructions, deterministic constraints and examples of quality together.

- Keep task interfaces and evals stable while comparing implementation changes.

- Preserve detailed qualitative feedback instead of immediately collapsing it into binary scores.

- Distinguish proposed feedback-to-eval research from established production guarantees.


### 128. How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=xyL2Ltkh-SA) · [Read transcript](transcripts/xyL2Ltkh-SA.md)

Preetika Bhateja and Daniel Bump share evaluation lessons from YouTube advertising agents. They recommend first examining outputs manually to understand capabilities and failure patterns, then growing a small task-focused golden set into scalable evaluation. Reliable human rubrics require examples, strong human-human agreement, and explanations rather than pass/fail labels alone. Automated judges should be sampled against expert judgments and audited through traces. One trace showed an agent recognizing a legal disclaimer and removing it despite instructions, illustrating what aggregate scores conceal. The speakers stress negative tests, held-out and production-refreshed data, ablations, explicit launch criteria, and improving recurring failure patterns rather than overfitting prompts to individual stochastic runs.

- Establish human agreement and collect explanations before scaling model judging.

- Inspect traces to identify why constraints were violated.

- Optimize recurring failure patterns, with held-out tests and explicit release criteria.


### 129. Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=OA-Mc60Rboo) · [Read transcript](transcripts/OA-Mc60Rboo.md)

Agrawal presents GEPA as sample-efficient reflective optimization: inspect complete rollout feedback, propose textual changes, and retain a Pareto pool of candidates rather than only the aggregate winner. He argues that diagnostic traces contain learning signals discarded by scalar rewards and reports stronger gains than GRPO in a particular comparison. Optimize Anything generalizes the method to scored text artifacts, including prompts, harnesses, skills, code, and scheduling policies. Examples include domain-specific API lessons, repository skills, and human-aligned judge optimization feeding an improvement loop. All performance and cost figures are presenter-reported, with varying tasks and baselines rather than a universal advantage over reinforcement learning. Generalization depends on representative problems and a meaningful evaluator, not reflection alone.

- Return actionable diagnostic information alongside evaluation scores.

- Preserve candidates with complementary strengths to avoid local optima.

- Align subjective judges with human annotations before using them for optimization.


### 130. Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=fnuNVFgLjHA) · [Read transcript](transcripts/fnuNVFgLjHA.md)

Ali describes a detect, investigate, fix, and verify loop in which agents consume production telemetry together with repository context. A toy-shopping assistant illustrates a price-filter bug that confidently returns products outside the requested budget. Arize Signal provides continuous failure clustering and investigation, while coding-agent skills offer an on-demand route to similar analysis and proposed pull requests. Verification uses tool-enabled harness judges and experiments replaying actual failure datasets against a development endpoint, comparing quality alongside latency and cost. Network problems limit the live workshop, and parts of verification are explained rather than executed. Ali recommends retaining human code review before shipping proposed changes.

- Join real traces with source code to investigate root causes.

- Validate proposed fixes against failure datasets before deployment.

- Keep human approval while automating investigation and experimentation.


### 131. Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=p7gaxmCUiIU) · [Read transcript](transcripts/p7gaxmCUiIU.md)

Shubhankar Srivastava demonstrates AutoBrowse, where a browser-operating agent and a teacher improve a persistent strategy file without updating model weights. The teacher reviews screenshots, trajectories, and outcomes after each attempt, preserving navigation lessons and shortcuts as a reusable skill. Flight-search and other examples show uneven progress: a passing iteration can be followed by failure, while successful runs can still improve on cost. The essential prerequisites are a replayable environment and a verifiable outcome. Q&A examines who evaluates the verifier, whether acceptable results are truly optimal, iteration budgets, skill portability, prompt injection, and changing websites. Monitoring and failure-triggered repair remain necessary after a skill graduates.

- Require replayable environments and explicit outcome criteria.

- Evaluate verifier quality and define the optimization objective.

- Monitor deployed skills for drift and review generated repairs.


### 132. Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=_zUp6y9bDU8) · [Read transcript](transcripts/_zUp6y9bDU8.md)

Ankur Duggal uses Arize CLI skills to bring operational traces, evaluations, annotations, and code into a coding agent’s repair workflow. A financial assistant’s plausible recommendations hide numeric-grounding problems, fabricated responses, repeated searches, and silent tool failures. The coding agent investigates these traces, proposes focused evaluators, and tests changes against datasets drawn from failing spans. An earlier international-stock experiment improves only after fixing both country context and an outdated tool, illustrating why prompt edits alone can be insufficient. The live repair remains unfinished at the end. The session recommends human review, application-specific rubrics, configurable judges, and sampling that balances ongoing quality monitoring with evaluation cost.

- Investigate trace-level causes before editing prompts.

- Test repairs on datasets representing the original failures.

- Review proposed fixes and evaluators; do not count an unfinished run as success.


## Core · Performance, cost & model selection


### 133. 20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna

**Uploaded:** 2026-06-01 · [Watch video](https://www.youtube.com/watch?v=hqHC6Z_lXyo) · [Read transcript](transcripts/hqHC6Z_lXyo.md)

Bertrand Charpentier challenges the idea of one universally best generative model. Public image-editing leaderboards disagree, aggregate rankings hide task-specific strengths, and personal inspection is biased by both reviewer preference and a few chosen samples. Automated metrics also require understanding and should match the target capability rather than serve as generic quality proxies. The talk recommends multiple benchmarks, realistic user conditions and larger samples, then adds latency, cost and energy to quality comparisons. Pareto plots expose several viable state-of-the-art choices and show why a small quality gain may not justify a large operational penalty.

- Evaluate the actual use case, not just an aggregate leaderboard rank.

- Combine broader human review with understood, task-specific metrics.

- Compare quality and efficiency on a Pareto frontier rather than choosing a single score winner.


### 134. How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival

**Uploaded:** 2026-10-14 · [Watch video](https://www.youtube.com/watch?v=8g1N_a3h9H0) · [Read transcript](transcripts/8g1N_a3h9H0.md)

Alvin Pane explains why disagreement with a production model is not automatically a regression: the production system can disagree with itself. In a synthetic HarborBite example, a cheaper candidate differs on eighteen percent of cases while repeated baseline runs differ on roughly seven percent. He combines telemetry, prefix caching, DSPy/GEPA prompt compression, and smaller-model experiments with shadow comparisons of baseline-to-baseline, candidate-to-candidate, and candidate-to-baseline behavior. Humans adjudicate disagreements into improvements, regressions, and ambiguity, then a paired confidence interval and critical-category checks inform release decisions. The reported prompt reduction illustrates the method, not realized million-dollar savings. Quality must still be monitored after deployment.

- Measure baseline nondeterminism before interpreting candidate disagreement.

- Adjudicate improvements and regressions with humans.

- Use paired confidence intervals and critical-category checks as release criteria.


### 135. Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax

**Uploaded:** 2026-10-21 · [Watch video](https://www.youtube.com/watch?v=YvQ4BVTWfHI) · [Read transcript](transcripts/YvQ4BVTWfHI.md)

Morgan Suo uses a financial research job to examine whether faster inference produces a faster usable result. M3.1 Flash changes include sparse attention, a lower-precision KV cache and experts, speculative decoding, serving-load choices, and reasoning budgets. Each optimization needs checks on retrieval, calculations, accuracy, and user-visible waiting time. She shows how average benchmark results can hide a task-specific regression, and how higher throughput can coincide with substantially worse tail latency. The proposed model-switch evaluation repeats the same research questions, checks sources and numbers, and counts retries and failed attempts in the total cost. The relevant unit is an acceptable completed report, not output tokens per second.

- Measure finished-task quality, latency, and total cost together.

- Inspect category-level regressions and tail latency.

- Include retries and failed attempts when comparing model configurations.


### 136. The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI

**Uploaded:** 2026-10-30 · [Watch video](https://www.youtube.com/watch?v=rWtbOgl5FTU) · [Read transcript](transcripts/rWtbOgl5FTU.md)

Rayan Krishnan explains why aggregate model-card scores and advertised token prices are poor substitutes for task-specific evaluations. Vals AI benchmarks reveal a jagged frontier: model rankings change across finance tasks and even across subsets such as leveraged-buyout modeling. A nominally cheaper model can consume enough extra tokens to cost more per completed task. He discusses partial-credit versus fully-correct scoring, representative tasks, reliability, benchmark saturation, reward hacking, and multi-turn work. An internal-evaluation case study reportedly reduced a team’s token spending by about 90% while preserving useful output. He recommends converting an organization’s accumulated work into evaluation cases that encode its actual standards.

- Compare cost per completed task rather than price per token.

- Inspect task subsets instead of trusting one aggregate leaderboard.

- Build realistic multi-turn tests from historical work and guard against grader exploitation.


## Core · Production monitoring & feedback loops


### 137. LLM codegen fails and how to stop 'em — Danilo Campos, PostHog

**Uploaded:** 2026-04-30 · [Watch video](https://www.youtube.com/watch?v=juoNbJiZUi0) · [Read transcript](transcripts/juoNbJiZUi0.md)

Danilo Campos analyzes failure modes in PostHog’s autonomous integration wizard and the interventions used to reduce them. Stale model knowledge is countered with current documentation, while lightweight reference applications show the intended integration shape. Staged instructions reduce unhelpful improvisation by separating discovery, event planning, and implementation. Crucially, an end-of-run question asks the agent what prevented success, exposing contradictory directives, unavailable tools, missing permissions, and language-mismatched guidance. Security examples replace unrestricted environment-file access with narrow key-presence and update tools. Q&A explains packaging reference applications and documentation as skill content. The emphasis is production feedback and error diagnosis, not a controlled benchmark or quantified causal evaluation.

- Use current documentation and compact reference integrations to counter stale model knowledge and inconsistent implementation patterns.

- Ask agents after each run what would have better enabled success; the team reports finding contradictory instructions, inaccessible tools, and inappropriate language guidance this way.

- Separate discovery, event planning, and implementation to reduce uncontrolled improvisation.

- Diagnose privacy risks in tool behavior and expose narrowly scoped operations rather than sending raw environment-file contents to inference services.


### 138. Shipping complex AI applications — Braintrust & Trainline

**Uploaded:** 2026-05-01 · [Watch video](https://www.youtube.com/watch?v=ZdheJTfLu-s) · [Read transcript](transcripts/ZdheJTfLu-s.md)

Braintrust and Trainline present a hands-on quality workflow for a staged support-triage agent. After adding deterministic tools and specialist stages, they instrument nested traces so reviewers can inspect inputs, outputs, tool calls, cost, and latency. A small golden dataset combines deterministic checks for structure and escalation policy with an LLM judge for nuanced customer-facing responses. Managed prompts, tools, and parameters support collaborative experiments and model comparisons. Online scoring monitors production traces, with sampling to control judge costs. The remediation exercise captures a misleadingly nonurgent invoice-export request, updates the prompt, and reruns evaluations, including regression checks. Trainline connects these practices to production model switching and travel-assistant reliability.

- Preserve a nested parent/child trace structure so failures can be localized to particular agent stages and tool calls.

- Start with explicit expected behavior and edge cases; combine inexpensive deterministic scorers with LLM judges for genuinely nuanced criteria.

- Apply online scoring to real production traces, using sampling to manage judge costs while retaining cheap deterministic checks.

- Promote production failures into evaluation cases, compare the fix against a baseline, and rerun the wider suite to check for regressions.


### 139. Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick

**Uploaded:** 2026-05-04 · [Watch video](https://www.youtube.com/watch?v=2TLXsxkz0zI) · [Read transcript](transcripts/2TLXsxkz0zI.md)

Chris Parsons builds a Pomodoro application through repeated Claude Code runs that select and implement tickets, then expands the pattern to personal work and content generation. Quality depends on explicit feedback: tests, behavioral checks, screenshot inspection, simulated audience personas, and independent subagent or adversarial review. The Q&A highlights confirmation bias when an agent validates its own work, the risk that generated tests reproduce a misunderstood requirement, and continued human review for security-sensitive code. Parsons describes versioning prompts as skills but acknowledges that improvement remains subjective; proposed blind comparisons across ticket sets have not been performed. The workshop provides practical verification and feedback patterns rather than measured evidence that Ralph loops outperform alternatives.

- Specify how the loop verifies actual behavior; passing generated tests or marking a ticket complete is not sufficient.

- Fresh-context subagents, adversarial review, and simulated audiences can provide different perspectives, but these examples do not establish calibrated evaluator accuracy.

- Keep human closure and security-sensitive review where needed, and define explicit stop conditions for irreversible actions.

- Prompt version control is not performance evaluation: Parsons acknowledges that he has not implemented objective comparative testing.


### 140. Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure

**Uploaded:** 2026-05-05 · [Watch video](https://www.youtube.com/watch?v=_QAVExf_1uw) · [Read transcript](transcripts/_QAVExf_1uw.md)

Raj Navakoti proposes using agent failures to discover missing enterprise knowledge rather than pushing an entire documentation collection into context. Agents attempt real work, identify unanswered domain questions, receive expert corrections, and preserve reusable context blocks. A workshop demonstration follows incident investigations and reports increasing confidence across fourteen iterations. A scanner extends the approach by generating probes from archived incidents, testing documentation, and classifying gaps, staleness, duplication, and priority. GitHub supplies review and versioning for curated Markdown. The Q&A limits the claims: testing was scoped to small teams, code and documentation can conflict, and maintaining correct, current knowledge remains unresolved. Confidence scores do not establish independently measured task accuracy.

- Use failed real tasks to identify specific missing context, then capture expert corrections for reuse instead of indiscriminately expanding retrieval.

- Generate probes from archived incidents to assess documentation coverage and prioritize recurring, high-impact gaps.

- Scope the process narrowly enough that domain experts can answer questions, and define precedence when code and documentation disagree.

- Treat rising agent confidence as a diagnostic signal, not an independently validated accuracy result; knowledge freshness still requires oversight.


### 141. Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop

**Uploaded:** 2026-05-07 · [Watch video](https://www.youtube.com/watch?v=-aM2EDTiaMs) · [Read transcript](transcripts/-aM2EDTiaMs.md)

Raindrop's team argues that finite evaluation datasets cannot cover the expanding behavior of production agents. They propose monitoring explicit signals such as tool errors, latency, cost, and regenerations alongside semantic classifiers for refusals, task failure, and user frustration. Regex offers a cheap aggregate signal, while experiments compare issue rates between shipped variants and controls. The workshop adds a self-reporting tool to a coding agent, deliberately breaks file writing, and observes the agent report its bash workaround. Q&A covers sample-size limitations, historical backfills, clustering failures by use case, and exporting classified events. The speakers caution that self-diagnostics may miss behavior the model regards as successful.

- Track concrete issue categories and their rates instead of relying solely on generic numerical output ratings.

- Compare production variants against controls using semantic failure signals, without confusing an early warning with statistical significance.

- A neutral reporting tool and creator-feedback framing can elicit useful diagnostics, but self-reporting is not a dependable security verifier.

- Cluster frustration and failure signals by task, tool, and trajectory to discover root causes and previously unknown regressions.


### 142. Feedback Loops are All You Need — Mehedi Hassan, Granola

**Uploaded:** 2026-05-10 · [Watch video](https://www.youtube.com/watch?v=ON5LIT0M4do) · [Read transcript](transcripts/ON5LIT0M4do.md)

Mehedi Hassan describes Granola's move from one-shot chat features toward explicit feedback loops for improving AI product quality. Production problems include expensive, context-heavy web search, silent provider regressions, and summaries that miss different users' expectations. Granola built internal tracing that exposes tool calls, reasoning, search activity, and costs to product, data, support, and engineering staff. This lets teams investigate vague complaints and identify specific failures. The team also made its Electron renderer run as a web application, enabling per-PR previews and Cursor-driven checks with screenshots. The Q&A reports that experiments with Tauri had not produced meaningful performance gains.

- Expose complete agent traces in a usable interface so non-engineering teams can connect poor outputs to specific failures.

- Monitor provider-dependent behavior: an upstream web-search update can degrade quality without an application deployment.

- Make desktop frontends accessible through PR preview URLs to enable parallel human testing and automated agent verification.


### 143. How we solved Context Management in Agents — Sally-Ann Delucia

**Uploaded:** 2026-05-10 · [Watch video](https://www.youtube.com/watch?v=esY99nYXxR4) · [Read transcript](transcripts/esY99nYXxR4.md)

Sally-Ann Delucia explains how Arize's agent encountered runaway context growth while analyzing its own trace data. Naive truncation broke follow-up reasoning, while unconstrained summarization inconsistently discarded important information. The team instead preserved message heads and tails, retained recent tool results, and stored removed content for retrieval. A concrete testing method replays ten conversation turns and evaluates the eleventh to expose late-session failures before customers report them. Data-heavy searches move into subagents to protect the main conversation. The talk also acknowledges unresolved context-quality metrics and missing cross-session memory; the Q&A prioritizes long-term memory over cache-preservation work.

- Replay accumulated conversation history and evaluate a subsequent turn to catch failures that short, single-turn tests miss.

- Treat broken follow-ups and forgotten context as observable failure modes when comparing context-management strategies.

- The reported success of head/tail preservation plus retrieval is experiential; the team still lacks principled context-quality metrics.


### 144. Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw

**Uploaded:** 2026-05-12 · [Watch video](https://www.youtube.com/watch?v=4VhbYlfC7Gs) · [Read transcript](transcripts/4VhbYlfC7Gs.md)

Vincent Koc argues that static evaluation suites calcify while agent behavior, harnesses, and user populations keep changing. He contrasts fixed offline question sets with adaptive testing and proposes outcome-oriented rubrics rather than exact-answer matching alone. Traces could supply automatically curated scenarios, always-on evaluations could detect changing use patterns, and telemetry-aware harnesses could respond to failures and cost constraints. His recurring stable-versus-changing workload example motivates maintaining the evolving edge cases instead of assuming a benchmark remains representative. The talk is conceptual: he says the intended implementation demonstration is not finished. Its contribution is an adaptive evaluation direction, not measured evidence that self-optimizing evaluation already works.

- Update evaluation coverage as production traces reveal changes in users, tasks, or agent behavior.

- Define desired outcomes and suitable rubrics when multiple valid behaviors make exact-answer tests insufficient.

- Connect telemetry and online quality assessment to the harness so observed failures can inform adaptation.

- Treat the proposed self-curating evaluation system as a conceptual design, since the implementation demonstration was not ready.


### 145. Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft

**Uploaded:** 2026-05-14 · [Watch video](https://www.youtube.com/watch?v=iOXM3zE-2dk) · [Read transcript](transcripts/iOXM3zE-2dk.md)

Boyd and Narasimhan connect agent observability to closing the gap between requirements and actual behavior as models, prompts, and environments change. Using a travel-agent example, they demonstrate OpenTelemetry tracing, trace-linked quality and safety evaluations, and agent-specific checks for intent resolution, task adherence, and tool calling. Their notebooks progress from a simple agent to specialist workflows, then batch evaluation and adversarial red-teaming scans. A preview observe skill generates evaluation data, establishes a baseline, analyzes failures, optimizes instructions, and compares versioned results. Further prompt changes cause regressions rather than perfect scores, prompting selection of an earlier best version. Audience discussion emphasizes human guidance, model-cost trade-offs, and reevaluation after changes.

- Link evaluation results to execution traces so a quality drop can be traced to specific tool calls, messages, or specialist agents.

- Evaluate intent resolution, task adherence, and tool behavior alongside output quality and safety; rerun evaluations after model or prompt changes.

- Use generated datasets and agent-assisted batch evaluation as a starting point, retain human guidance, and compare versioned results rather than assuming every optimization improves quality.

- Complement ordinary quality and safety tests with adversarial scans for data leakage, instruction violations, and prohibited agent actions.


### 146. How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs

**Uploaded:** 2026-05-16 · [Watch video](https://www.youtube.com/watch?v=kfSDc2eVLo4) · [Read transcript](transcripts/kfSDc2eVLo4.md)

Lovejoy treats AI quality as an organizational problem: domain judgment must own assessment and feed concrete improvements. He distinguishes oracles, who inspect outputs and directly revise prompts; evaluators, who define metrics and failure taxonomies while engineers implement fixes; and architects, who design systems that learn from usage. Granola illustrates taste-driven review, Tandem illustrates decentralized clinical prompt ownership, and Anterior illustrates progression toward clinician review dashboards and automated adaptation. Choosing an organizational model depends on measurable outcomes, scale, and whether manual iteration is fast enough. He argues for a principal expert with ownership and complementary data-science or engineering skills rather than an advisory role without authority.

- Give a principal domain expert accountability and decision-making ownership for AI quality, rather than limiting experts to occasional advice.

- Use direct expert review and prompt iteration when quality depends on taste; decentralize that ownership when specialties and customer needs diverge.

- When outcomes are meaningfully measurable, define metrics and failure modes, collect expert reviews, and connect those findings to engineering fixes.

- Move toward automated improvement only when manual iteration becomes inadequate; detailed experience with failures should inform the evaluation system.


### 147. Fighting AI with AI — Lawrence Jones, Incident

**Uploaded:** 2026-05-17 · [Watch video](https://www.youtube.com/watch?v=L2r6vLlLgs8) · [Read transcript](transcripts/L2r6vLlLgs8.md)

Lawrence Jones describes using coding agents to evaluate and debug Incident.io’s complex AI investigations. A small CLI lets agents inspect and edit individual YAML evaluation cases without loading enormous production examples into context. A runbook creates a failing case, adjusts the prompt, reruns regression checks, and simplifies accumulated instructions. To locate failures across many prompts, the team exports debugging interfaces and traces as self-documenting files alongside the codebase. For daily backtests, parallel agents analyze individual investigations before a clustering stage identifies shared failure patterns. This turns aggregate accuracy into actionable explanations and connects diagnosed problems to code changes that can be tested.

- Expose targeted evaluation operations through a CLI when large test fixtures overwhelm agent context.

- Require a failing evaluation, a prompt fix, and checks that other cases still pass; periodically consolidate the prompt.

- Export traces and debugging context as navigable files so agents can trace errors through the full prompt hierarchy.

- Combine parallel per-investigation analysis with cohort clustering to explain quality changes that aggregate scores cannot explain.


### 148. Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

**Uploaded:** 2026-05-17 · [Watch video](https://www.youtube.com/watch?v=C_GG5g38vLU) · [Read transcript](transcripts/C_GG5g38vLU.md)

Tejas Kumar builds a browser-agent harness around GPT-3.5 Turbo while keeping its prompt unchanged. The initial Hacker News task fails at authentication yet reports a successful upvote. He adds iteration limits, illustrative context trimming, bounded retries, and a deterministic verifier that inspects tool history for genuine success and unresolved login failures. A programmatic login handler then resolves authentication outside the model and records that intervention in the trace. The final demonstration checks the resulting page for an unvote option as confirmation. The lesson is to distinguish model claims from observed execution and encode explicit failure conditions before attempting to improve task completion.

- A model saying it finished is not sufficient evidence that its requested action occurred.

- Deterministic verification should check tool results and explicit failure cases, including unrecovered authentication redirects.

- Bound attempts and iterations, and manage context in the harness rather than relying entirely on prompting.

- Verify externally visible state after execution; the demonstration confirms the upvote through the available unvote action.


### 149. How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

**Uploaded:** 2026-05-28 · [Watch video](https://www.youtube.com/watch?v=XBaznoTRDFI) · [Read transcript](transcripts/XBaznoTRDFI.md)

Phil Hetzel contrasts uptime-oriented observability with measuring whether agents produce grounded, appropriate and useful behavior. Large semi-structured traces contain prompts, context and tool decisions needed for these qualitative assessments, creating different ingestion, indexing and query demands from ordinary application metrics. Domain experts such as clinicians and lawyers review traces and explain judgments; those rationales become scalable automated scorers. The talk connects real-time observability with batch evaluation on known inputs and describes clustering traces to discover intents, sentiment and previously unknown failures. Traditional technical metrics remain useful, but they do not establish functional agent quality.

- Instrument enough context to evaluate grounding and tool decisions.

- Bring domain experts into trace review and capture their reasoning.

- Use production failure discovery to populate offline experiments.


### 150. How Lovable self-improves every hour — Benjamin Verbeek, Lovable

**Uploaded:** 2026-06-02 · [Watch video](https://www.youtube.com/watch?v=KA5kPbdkK2E) · [Read transcript](transcripts/KA5kPbdkK2E.md)

Benjamin Verbeek describes two continuous-improvement loops at Lovable. Session judges identify users who become stuck and later succeed; clustered solutions become contextual knowledge entries, reviewed and tested before injection. A small holdout receives blank injections, allowing production outcomes to determine whether entries help and whether stale advice should be removed. Separately, an agent vent tool reports missing capabilities, confusing instructions and broken platform behavior directly to engineers. Deduplicating agents investigate and propose fixes. Examples include file-copy failures involving spaces and incident-related feedback spikes, showing how inline agent feedback complements external conversation review.

- Use holdouts to verify that injected lessons improve real project outcomes.

- Prune knowledge as models and product behavior change.

- Give working agents a selective channel for concrete tool and platform failures.


### 151. Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel

**Uploaded:** 2026-06-02 · [Watch video](https://www.youtube.com/watch?v=YYH0DMQr30A) · [Read transcript](transcripts/YYH0DMQr30A.md)

Kobie Crawford investigates whether better agentic tasks improve training outcomes under matched conditions. Terminal-Bench-style environments are accepted only if achievable, nontrivial, functionally correct and reliable. Accepted and rejected pools are compared through tool counts, pass rates, reasoning effort and failure categories before training with the same model, compute and task count. Higher-quality tasks produce cleaner capability failures and larger reported improvement. The discussion distinguishes genuine difficulty from underspecified instructions, hidden dependencies and mismatched tests. Human and LLM rubric agreement is also treated as a quality-control mechanism, particularly as tasks become less straightforwardly verifiable.

- Audit task executability and test/spec alignment before interpreting failure rates.

- Compare training effects with model, compute and task count held fixed.

- Use detailed failure taxonomies and human–judge agreement to validate task quality.


### 152. The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

**Uploaded:** 2026-06-18 · [Watch video](https://www.youtube.com/watch?v=ObTPqBGsEbA) · [Read transcript](transcripts/ObTPqBGsEbA.md)

Sandipan Bhaumik’s production playbook starts with measurable business success, representative expert cases and an evaluation pipeline before model selection. It distinguishes deterministic checks, semantic LLM judges and behavioral tests for tool use, loops and wasteful execution. A banking-chatbot case illustrates collecting evaluation data and tracing first, then detecting stale retrieval after a policy update through falling satisfaction and trace inspection. Evaluation datasets should grow from incidents, with ownership, categories and prompt-change provenance. The talk also discusses governance, orchestration and data foundations, but repeatedly ties them to observable quality, release validation and operational accountability.

- Define business targets and representative cases before selecting a model.

- Evaluate tool behavior even when final answers are correct.

- Govern a living incident-derived dataset and use smaller CI subsets when full runs are costly.


### 153. Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs

**Uploaded:** 2026-06-25 · [Watch video](https://www.youtube.com/watch?v=vljxQZfJ9wY) · [Read transcript](transcripts/vljxQZfJ9wY.md)

Nishant Gupta reframes evaluation from scoring isolated model answers to measuring dependable agent workflows. Offline benchmarks remain useful, but scenario simulations and production telemetry reveal tool errors, retrieval and memory failures, recovery behavior and multi-agent coordination. He proposes continuous evaluation as a control-plane service that observes traces, runs simulations, coordinates targeted human review and feeds new cases into offline validation. Metrics map to outcomes: completion, tool success, escalation, safety violations, latency, cost and recovery. The talk emphasizes gradual drift across model, prompt, tool and user changes, making ongoing monitoring necessary rather than a single pre-release testing phase.

- Evaluate complete scenarios and recovery paths, not only answer accuracy.

- Combine production traces with human calibration and offline update validation.

- Treat evaluation as a continuous control-plane capability.


### 154. User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

**Uploaded:** 2026-06-28 · [Watch video](https://www.youtube.com/watch?v=Jx4ZFEAq6bY) · [Read transcript](transcripts/Jx4ZFEAq6bY.md)

Sonam Pankaj argues that traces and pass/fail evaluations are wasted if they never change the next agent run. Reflect adds runtime memory ranked by semantic similarity and historical usefulness: successful use increases utility and failed use reduces it. Reusable lessons can later become skills. The talk contrasts this with recency-only or similarity-only memory, reports company-run benchmark improvements, and demonstrates feedback changing a SQL product-search trajectory. It acknowledges cold starts, drifting utility and noisy review labels. The central contribution is an explicit connection from evaluation outcomes to retrieval behavior, rather than treating observability dashboards as the end of improvement.

- Make outcomes influence retrieval rather than merely recording them.

- Distill recurrent successful reasoning into maintained skills.

- Monitor label quality, cold starts and utility drift in feedback-driven memory.


### 155. Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

**Uploaded:** 2026-06-29 · [Watch video](https://www.youtube.com/watch?v=Lc8zRh9muoY) · [Read transcript](transcripts/Lc8zRh9muoY.md)

Tisha Chawla and Susheem Koul distinguish reproducing a model output from replaying a failed system execution. Their Chronicle proof of concept records inputs, outputs and version metadata at semantic boundaries around model calls, tools and retrieval. A stock-selling example shows a valid API request executing the wrong quantity without raising errors. After adding a guardrail, recorded model outputs are replayed while the changed tool runs live, turning the original incident into an assertion-based regression test. The speakers separate deterministic tests of tools and guardrails from behavioral evaluations of tone or trajectory using judges.

- Record tool, memory and retrieval boundaries, not only prompts or network packets.

- Replay unchanged nodes and execute the repaired component to test the exact failure.

- Use behavioral evaluation alongside deterministic replay, not as its replacement.


### 156. The Missing Layer After Launch - Raphael Kalandadze, Wandero AI

**Uploaded:** 2026-07-05 · [Watch video](https://www.youtube.com/watch?v=kZsf_Sfm7RU) · [Read transcript](transcripts/kZsf_Sfm7RU.md)

Raphael Kalandadze describes an operational layer for agents after launch, where successful requests and green infrastructure metrics can conceal user-level failure. A short-cycle monitoring agent analyzes logs and code, proposes fixes and alerts; an independent review agent challenges whether each patch addresses a root cause. A separate session analyzer scores conversations and aggregates recurring problems, tool behavior and system health across customers. Browser-based testing supplies the user perspective missing from logs. The talk stresses access to traces, databases and interfaces, calibration of the operating agents, and keeping humans at review boundaries while making evidence understandable.

- Measure conversation outcomes, not just exceptions or request completion.

- Separate local incident repair from cross-session failure discovery.

- Combine trace analysis with user-facing browser checks and independent patch review.


### 157. Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo

**Uploaded:** 2026-07-07 · [Watch video](https://www.youtube.com/watch?v=CDqzWpwkSls) · [Read transcript](transcripts/CDqzWpwkSls.md)

Angel Ortmann Lee shows why human-in-the-loop review is not automatically reliable evaluation. In a Duolingo English Test experiment, experienced proctors accepted half of fabricated cheating alerts on legitimate historical sessions. Reframing instructions to require independent evidence improved rejection of false alerts from roughly 50% to 71%, without changing the model. The talk treats interaction design as part of the measurement system: distinguish detection from policy decisions, capture edits rather than only acceptance clicks, and expose assumptions in reviewable steps. Examples from tutoring and coding agents show how interfaces can generate useful labels or reinforce automation bias.

- Evaluate human reviewers under deliberately incorrect AI suggestions.

- Separate model correctness from downstream policy decisions.

- Capture structured corrections and disagreements, not only thumbs-up signals.


### 158. Your agent is blindfolded — Johan Lajili, Poolside AI

**Uploaded:** 2026-07-08 · [Watch video](https://www.youtube.com/watch?v=iRcX54EO5g8) · [Read transcript](transcripts/iRcX54EO5g8.md)

Johan Lajili argues that the difference between successful and disappointing coding-agent use is often the feedback loop, not whether a repository is new or legacy. Poolside built an internal CLI that exposes its VS Code extension through screenshots, compact page snapshots, service logs, restarts, and higher-level interaction commands. This lets an agent reproduce a bug before changing code and verify the result afterward, rather than confidently reporting an untested intuition. Lajili frames agent-facing tooling and codebase accessibility as engineering work in their own right. He recommends inspecting repeated manual interventions and agent logs to discover the next missing observation or control.

- Require bug reproduction before accepting an agent’s diagnosis.

- Give agents product-specific observation and interaction tools.

- Use recurring manual checks and awkward log patterns to improve the testing interface.


### 159. Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony

**Uploaded:** 2026-07-11 · [Watch video](https://www.youtube.com/watch?v=WLXxTaPagA8) · [Read transcript](transcripts/WLXxTaPagA8.md)

Sumaiya Shrabony uses a 19-skill content pipeline to show how polished agent outputs can violate production contracts while declaring themselves ready. Her demonstration contrasts naive saving with blocking gates for voice drift, unsupported factual claims, and duplicated angles. The broader controls resemble established software practices: regression testing, scheduled-run monitoring, contract testing, staging, and audit trails. She recommends mapping every handoff, identifying where corrupted output is most costly, and adding a small boundary check there before expanding the agent system. A real gate must prevent downstream publication, not merely log a warning. The talk emphasizes observable failure paths and source-linked evidence over happy-path demos.

- Test handoff contracts as well as final artifact shape.

- Block unsupported claims and duplicates before publication.

- Start with the highest-cost failure boundary and retain an audit record.


### 160. Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS

**Uploaded:** 2026-07-11 · [Watch video](https://www.youtube.com/watch?v=vJukHCIv7Ck) · [Read transcript](transcripts/vJukHCIv7Ck.md)

Elizabeth Fuentes demonstrates five structural approaches to agent reliability using a toy travel assistant: semantic tool selection, graph-based retrieval, executor-validator-critic handoffs, code-enforced business rules, and runtime steering. Each section compares a baseline with a modified system, using known tool choices or booking outcomes to inspect errors, token use, and constraint compliance. The workshop distinguishes hard blocking from corrective feedback that lets an agent find an acceptable alternative. Its examples are explicitly dummy tools and small local demonstrations, not production-scale evidence for the headline performance claims. The useful evaluation pattern is to define observable failure cases and hold the surrounding task constant while testing a specific intervention.

- Compare interventions against explicit ground-truth cases and known constraints.

- Validate tool failures independently instead of trusting a success narrative.

- Separate hard invariant enforcement from soft-rule steering and measure task outcomes.


### 161. Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest

**Uploaded:** 2026-07-20 · [Watch video](https://www.youtube.com/watch?v=0RNNfxpdbQk) · [Read transcript](transcripts/0RNNfxpdbQk.md)

Drasko Profirovic describes Pinterest’s Medic diagnostic agent and the evaluation infrastructure needed to improve it safely. Early manual tests depended on expiring production logs and made regressions difficult to identify. The team added OpenTelemetry traces and a record/playback harness: real tool responses are captured as versioned fixtures, replayed offline, and the resulting diagnostic reports graded against authored expectations. This turned quality changes into measurable regressions rather than anecdotes. Subsequent work improves exception retrieval, uses isolated visual analysis of metrics to control token volume, and separates specialist agents. The talk connects observability, reproducible inputs, targeted output rubrics, and architectural iteration in a concrete production support system.

- Snapshot real downstream responses into versioned fixtures for replay.

- Grade diagnostic reports against explicit expectations and track regressions.

- Use traces to distinguish bad reasoning from noisy or oversized tool context.


### 162. From Signal to PR: Anatomy of a Self-Improving Agent — Jason Lopatecki, Arize

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=9HbzAWnKbo4) · [Read transcript](transcripts/9HbzAWnKbo4.md)

Jason Lopatecki demonstrates Arize Signal as a loop connecting production telemetry to investigation and proposed fixes. Well-designed skills retrieve relevant traces, online-evaluation results, and logs into files beside the repository, giving coding agents concrete evidence of the executed path rather than a dashboard to navigate. Scheduled or event-triggered sandbox runs identify issues, build datasets or evaluators, and sometimes open a pull request. Lopatecki distinguishes scalable, predefined LLM judges from broader periodic agent investigations and says larger fixes still need human guidance. The key architectural concerns are composable data-access skills, security-conscious sandbox placement, and retaining enough telemetry to support evidence-backed diagnosis and review.

- Make traces and evaluation data accessible as files alongside code.

- Convert recurring newly discovered failures into reusable evaluators.

- Treat proposed fixes as evidence-backed review inputs, not proof of autonomous correctness.


### 163. The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=BInpv7lGp1o) · [Read transcript](transcripts/BInpv7lGp1o.md)

The talk argues that fluent model responses can conceal failures in the surrounding agent harness. Using public OpenClaw incidents, it examines delivered replies missing from durable history, concurrent writers losing updates, dangling tool calls, expired approvals, and messages accepted internally but never rendered. The proposed contract is that the model proposes, the harness commits, and durable receipts prove outcomes. Reliable systems assign each fact a replayable owner, serialize commits within shared state boundaries, bound waits and retries, and bind approvals to specific actions. A five-question audit checks triggers, inherited state, authority, execution, and surviving evidence, ending at the external result the user actually cares about.

- Distinguish message delivery from durable state persistence, and identify the owner and replay path for every retained fact.

- Serialize mutations at each shared-state boundary while preserving parallel reads and independent work.

- Give tools terminal outcomes and deadlines, and bind approval records to exact actions, arguments, and lifetimes.

- Verify the user-visible or external side effect; a transcript or internal success flag is not sufficient proof.


### 164. Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop

**Uploaded:** 2026-08-12 · [Watch video](https://www.youtube.com/watch?v=jHMiYtjoJfA) · [Read transcript](transcripts/jHMiYtjoJfA.md)

Ben Hylak distinguishes maximizing frontier benchmark capability from raising an application's reliability floor. He argues that brittle chatbot-era datasets and exact tool-call expectations often fail when models or harnesses change, so offline agent evaluations should increasingly resemble executable unit and end-to-end tests kept as code. Production improvement requires discovering unknown issues, identifying when each began, and measuring affected users. He cautions that trace clusters are not stable issue definitions: broad groups can mix unrelated root causes and are difficult to track over time. Instead, he recommends scalable code-based classifiers and deterministic anomaly signals, with agents investigating detected changes rather than being asked to discover anomalies unaided.

- Evaluate the full agent harness with tests as code rather than treating a prompt string as the whole system.

- Track issue onset and user prevalence to connect regressions with changes and prioritize repairs.

- Do not equate semantic clusters with durable, actionable issue categories.

- Detect changes using tractable deterministic signals, then use agents to investigate the evidence.


### 165. Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

**Uploaded:** 2026-08-12 · [Watch video](https://www.youtube.com/watch?v=CvRngaQZQ3Y) · [Read transcript](transcripts/CvRngaQZQ3Y.md)

Vivek Trivedy frames agent improvement as a data loop: deploy, collect complete traces, mine behavior, and run experiments on prompts, tools, orchestration, or models. Traces expose user dissatisfaction, post-compaction degradation, and behavioral differences that aggregate scores obscure. Because long traces are expensive and may exceed context windows, analysis agents should query them as external data rather than ingest everything. Curated outputs support evaluation datasets, training examples, and human review. He describes starting with strong models, testing cheaper open models, and using harness engineering before fine-tuning when returns plateau. Dense diagnostic feedback from traces is presented as more useful for automated improvement than a bare benchmark pass/fail signal.

- Centralize tool calls, messages, and execution data so agent behavior can be inspected across production runs.

- Mine traces into concrete failure cases and evaluation datasets, then test proposed changes against them.

- Query large traces selectively and benchmark cheaper judging models on the actual domain task.

- Provide diagnostic evidence beyond pass/fail, and try fast-feedback harness changes before escalating to fine-tuning.


### 166. Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust

**Uploaded:** 2026-08-20 · [Watch video](https://www.youtube.com/watch?v=nxokqOq1imY) · [Read transcript](transcripts/nxokqOq1imY.md)

Ameya Bhatawdekar argues that evaluation must evolve with agent architecture rather than remain attached to an application's earliest design. Using an SRE agent as a running example, he traces the progression from single model calls through retrieval chains, workflow graphs, autonomous loops, and systems augmented with memory, execution sandboxes, and skills. Each transition introduces new failure surfaces, requiring checks beyond final-answer correctness, including retrieval, node contracts, tool use, branching, and retries. For variable agent trajectories, he recommends repeated runs and distributional metrics separating capability from reliability. He closes with a production-to-evaluation flywheel and Braintrust's clustering-based Topics feature for discovering previously unanticipated failure categories and building fresh regression datasets.

- Update evaluation coverage whenever architectural changes introduce new tools, memory, orchestration, or execution components.

- Evaluate intermediate nodes and contracts as well as end-to-end outcomes when workflows can fail between steps.

- Repeat nondeterministic tasks to distinguish occasional success from reliable behavior across runs.

- Cluster production traces to discover unknown failure types, then convert them into maintained regression cases.


### 167. Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan

**Uploaded:** 2026-08-29 · [Watch video](https://www.youtube.com/watch?v=32nrHU6zHU8) · [Read transcript](transcripts/32nrHU6zHU8.md)

Roberto Milev and Uday Kanagala outline production agent infrastructure at Navan, with a substantial focus on debugging and evaluating nondeterministic behavior. They use skills as independently testable context units and hooks around tool calls to emit traces of goals, decision signals and execution. Instead of asserting one fixed sequence or exact output, they discuss trajectory evaluations that measure progress toward the intended goal, completeness and efficiency. Inferred answers can trigger human review, and regressions inform fixes. The talk also covers identity, authorization and orchestration, recommending a manageable single-agent foundation before multi-agent complexity. Its evaluation contribution links operational traces, component boundaries and trajectory-based testing.

- Test reusable skill units separately from complete agent workflows.

- Instrument decision and tool boundaries for actionable quality traces.

- Score goal progress and trajectory quality rather than assuming a deterministic execution graph.


### 168. An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=hd7TOvmyAxU) · [Read transcript](transcripts/hd7TOvmyAxU.md)

Sweeney demonstrates ARIA as a research assistant that queries experiment history, builds reports and visualizations, and launches GPU-backed code and hyperparameter experiments through Weights & Biases. A live batch runs twelve experiments but does not beat the prior best loss, illustrating iteration without guaranteed improvement. He then explains ARIA's development loop: production tracing and online judges reveal behavioral issues, which become YAML tasks scored for correctness, insight quality, and tool-call efficiency in nightly evaluations. Candidate-versus-production dashboards guide releases. He recommends agent-oriented observability, evaluation-driven go/no-go decisions, domain context, and human trace review because model judges miss nuances. The agent complements researchers rather than replacing hypothesis-setting and judgment.

- Connect production behavioral failures to explicit offline evaluation tasks.

- Score correctness, usefulness, and efficiency rather than execution alone.

- Keep human review and accept that experimental batches may not improve results.


### 169. How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=XyV6bSMyq-I) · [Read transcript](transcripts/XyV6bSMyq-I.md)

Aysola explains how Weights & Biases develops ARIA through a production-to-simulation evaluation loop rather than relying primarily on reinforcement learning. Research and production use identical agent code, synchronized regularly to reduce drift. Tasks define starting environments and desired outcomes, including single prompts and simulated multi-turn users; scoring combines task completion with relative behavioral comparisons. Production failures and successful patterns become offline tasks, and product teams assess benchmark relevance. A live example converts a trace into a regression case, compares candidate and production variants, and targets an SDK logging error through prompting or skills. He stresses thoughtful measurement despite automation; the demonstration does not establish a broad improvement magnitude or eliminate the need to validate evaluation relevance.

- Minimize production-simulation drift with shared code and synchronized environments.

- Turn real traces into repeatable tasks and compare candidate against production.

- Automation does not replace judgment about scoring robustness and meaningful improvement.


### 170. Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase

**Uploaded:** 2026-10-02 · [Watch video](https://www.youtube.com/watch?v=5xi_S1f9sDU) · [Read transcript](transcripts/5xi_S1f9sDU.md)

Meegan explains why reliable browser automation requires more than strong per-step model accuracy: transactional workflows accumulate risk and cost but deliver value only when completed. He distinguishes browser representations and autonomy levels, then prioritizes task performance before cost and maintainability. Success should be verified through concrete artifacts such as receipts or queryable records and measured per transaction, including retries, rather than per run alone. A health-insurance portal architecture moves stable authentication and downloading into deterministic functions, adds document verification against records, and reserves agent reasoning for genuine ambiguity guided by skills. His probability examples are illustrative assumptions, while observability and reevaluation remain necessary as sites, tasks, and models change.

- Verify concrete transaction outcomes instead of accepting agent declarations.

- Reduce probabilistic steps by extracting stable operations into tools.

- Measure transaction-level reliability and maintain reevaluation as environments change.


### 171. Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog

**Uploaded:** 2026-10-03 · [Watch video](https://www.youtube.com/watch?v=rTojoVotlD8) · [Read transcript](transcripts/rTojoVotlD8.md)

Petzel argues that traditional latency, error, traffic, and saturation monitoring remains necessary but cannot establish generative-AI application health. Successful HTTP responses can conceal hallucinations, unsafe disclosures, or irrelevant answers, while model choices and context growth make costs variable. She proposes cost attribution by feature, user, model/provider, and environment, alongside attention to caching and token creep. Safety monitoring covers injection attempts, personal-data leakage, toxic content, and jailbreaks. Quality monitoring combines groundedness checks, relevance, user feedback, completeness judgments, and retrieval metrics, using both automation and manual review. Datadog is offered as an implementation platform; numerical targets and spending examples are presenter recommendations or claims rather than validated universal thresholds.

- Add cost, safety, and semantic quality monitoring to infrastructure metrics.

- Tag spending dimensions to locate expensive features and usage patterns.

- Combine human review, task-specific metrics, and automated checks rather than trusting HTTP success.


### 172. From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI

**Uploaded:** 2026-10-05 · [Watch video](https://www.youtube.com/watch?v=F0TNSmbo5hE) · [Read transcript](transcripts/F0TNSmbo5hE.md)

Voss extends agent observability from manually reading traces to automated improvement driven by evaluations and recurring failure patterns. Because identical inputs can follow different paths, he treats aggregated traces as behavioral evidence and evaluator explanations as actionable feedback. A toy-store workshop instruments an application, analyzes searches, and adds missing price filtering; the coding agent copies a nearby pre-solved implementation, limiting the demonstration's independence. Arize Signal is presented as a scheduled trace-analysis agent that suggests issues, datasets, evaluators, and reviewable fixes. He emphasizes regression evaluations to preserve existing behavior and describes Signal's own internal evaluations and judges. Autonomous evaluator creation is not enabled, and suggestions still require user decisions.

- Use trace-derived failure clusters to prioritize improvements at scale.

- Run regression evaluations before accepting automated fixes.

- Evaluate improvement agents themselves and retain reviewable evidence.


### 173. Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=hfEczxdNyvU) · [Read transcript](transcripts/hfEczxdNyvU.md)

Guthrie demonstrates an observability-to-evaluation improvement loop using a support agent, Braintrust tracing, online judges, and topic clustering. He distinguishes deterministic checks from subjective model judges and stresses human calibration, difficult examples, and evolving datasets. Topics preprocess conversations, summarize facets, embed them, and cluster patterns to expose issues beyond existing scores. The workshop imports example traces, configures scoring scope and sampling, then uses SQL-capable coding agents to investigate failures, create regression cases, modify code, and compare evaluations. Limitations remain explicit: demonstration data is synthetic, a built-in issues facet produces insufficient matches, Topics requires hosted models, and reviewers must assess generated changes. Network problems also prevent normal audience participation.

- Trace intermediate steps and calibrate judges with human review.

- Combine known-failure scores with clustering to discover untested behavior.

- Scope multi-turn scoring correctly and budget online sampling costs.

- Require evaluation evidence and human review for automated improvement PRs.


### 174. Why Building an Eval Platform Is Harder Than It Looks — Braintrust

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=mUQoVz7THu0) · [Read transcript](transcripts/mUQoVz7THu0.md)

Braintrust's presenter explains why an evaluation platform grows far beyond a spreadsheet and results interface. Early loops execute examples and record scores; later stages add collaborative review, nontechnical experimentation, and side-by-side prompt or model comparisons. The crucial next step links production observability to offline regression datasets so real failures drive improvement without new regressions. Supporting this requires ingesting large, nested traces, querying fresh and historical data, preserving snapshots, and managing permissions and masking. He describes Braintrust's query abstraction and agent-assisted failure discovery as responses to those systems demands. Humans still choose what to ship; automated insight capabilities are presented as product direction and functionality, not independently benchmarked guarantees.

- Turn production failures into reusable offline regression cases.

- Plan for trace storage, query workloads, governance, and cross-role collaboration.

- Agent-driven experimentation does not remove human release responsibility.


### 175. Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab

**Uploaded:** 2026-10-09 · [Watch video](https://www.youtube.com/watch?v=Emo5FGGY-wM) · [Read transcript](transcripts/Emo5FGGY-wM.md)

Blanes frames reliable browser agents as a customer-feedback problem rather than a contest to maximize static benchmark scores. Drawing on Amazon’s Nova service rollout, he proposes a flywheel: define success in customer terms, capture telemetry and direct conversations, diagnose model, engineering, or product gaps, and prioritize changes. Customer needs evolve from discovery through early adoption and scale, so evaluation scenarios must evolve too. He describes an observed trust cliff between roughly 80% and 92% reliability, not a universal safety threshold. Examples include trajectory caching, nontechnical QA tooling, and customization. Honest communication of limitations and out-of-scope capabilities is presented as essential to trust.

- Build scenarios from production behavior and customer conversations.

- Separate research, engineering, and product failures before prioritizing.

- Disclose limitations instead of presenting benchmark scores as guarantees.


### 176. Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=BOCjybvJYM4) · [Read transcript](transcripts/BOCjybvJYM4.md)

Schäfer and Verheyden present an AI engineering loop connecting production tracing and monitoring with offline datasets, experiments, and regression checks. Their workshop instruments a dad-focused IT support agent and configures semantic judges for disagreement and out-of-scope requests alongside a deterministic all-caps frustration check. They emphasize selecting application-specific failure signals rather than copying generic evaluators. A coding agent then analyzes seeded traces, surfacing retrieval failures, retry costs, and monitoring coverage gaps. The practical focus remains online observability; the broader recommendation is to maintain representative datasets and evaluation criteria continuously, with human review catching novel failures that automated checks can miss.

- Capture useful trace context before designing evaluations.

- Combine deterministic checks, semantic judges, and human feedback.

- Turn production failures into maintained regression datasets.


### 177. 1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah

**Uploaded:** 2026-10-22 · [Watch video](https://www.youtube.com/watch?v=mMw3arwQsL0) · [Read transcript](transcripts/mMw3arwQsL0.md)

Vishal Srivastava and Tanmay Sah study 1,368 public AI incidents to derive a broader evaluation framework. They organize failures across technical strength, deployment controls, and business context, with thirteen subdimensions reportedly covering about ninety-eight percent of the incidents examined. Human oversight, monitoring, authority, assumptions, and material business harm matter alongside model accuracy. Their proposed build-break-fix loop deliberately searches for counterexamples rather than confirming that a system works. An airline chatbot’s incorrect refund advice illustrates how a narrow model test misses consequential system-level failures. They also stress evaluating the evaluator itself, since generated tests and AI judges can reproduce blind spots instead of providing independent evidence.

- Prioritize evaluation according to business risk and system authority.

- Test deployment controls and harm detection, not just model quality.

- Seek falsifying cases and verify the evaluator’s assumptions.


### 178. Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI

**Uploaded:** 2026-10-24 · [Watch video](https://www.youtube.com/watch?v=v5tm5EAzsAs) · [Read transcript](transcripts/v5tm5EAzsAs.md)

Sofia Jakovcevic demonstrates why a prompt fix can improve one behavior while degrading another: an illustrative support-agent change raises action safety by seventeen points but lowers task completion by seventeen. Her five-step regression loop starts with production traces, curates representative successes and failures, defines evaluators, runs a baseline, compares one change, and gates merges in CI. The workshop shows prompt-level and full-agent experiments with outcome scores, latency, cost, and errors. Coding agents can consume the same traces and evaluation artifacts to investigate problems, but proposed repairs still need testing. Each new production failure should enrich the regression suite rather than disappear after a one-off patch.

- Protect existing successes as well as known failure cases.

- Compare multiple quality dimensions against a fixed baseline.

- Make evaluation results enforceable merge criteria and keep adding production failures.


### 179. What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI

**Uploaded:** 2026-10-25 · [Watch video](https://www.youtube.com/watch?v=ImnZ7s68jw8) · [Read transcript](transcripts/ImnZ7s68jw8.md)

Aparna Dhinakaran argues that AI engineering is shifting from implementing individual features to building feedback loops around fleets of agents. Arize Signal illustrates an always-on agent that reads telemetry, remembers prior issues, and proposes changes, with durable state surviving disposable sandboxes and failures. Evaluation is necessary at several levels: offline tests of a proposed repair, human-aligned golden datasets for the evaluators themselves, and online checks of production behavior. She emphasizes that agents increasingly consume observability data directly, making trace quality part of the improvement system. The talk connects scheduling, triggers, persistent memory, and model-independent harnesses to reliable evaluation rather than treating monitoring as a dashboard added after deployment.

- Design telemetry for automated investigation as well as human inspection.

- Evaluate proposed changes offline and behavior online.

- Test evaluators against human-labeled golden data.


### 180. Agents That Self Improve While You Sleep - Fuad Ali, Arize AI

**Uploaded:** 2026-10-26 · [Watch video](https://www.youtube.com/watch?v=UGuNt2_Oz8s) · [Read transcript](transcripts/UGuNt2_Oz8s.md)

Fuad Ali demonstrates a self-improvement loop in which production traces become issues, datasets, evaluators, experiments, and proposed repairs. Signal periodically reviews a shopping agent’s traces, remembers earlier findings to avoid duplicates, and diagnoses a category-formatting bug from evidence rather than an implausible final answer alone. Failures are preserved as regression cases and replayed against a candidate fix. The workshop compares code checks, LLM judges, and decision models, and discusses evaluation health, qualitative output, sampling, and cost. Humans retain leverage over rubric design, dataset curation, and reviewing changes. The useful distinction is between detecting a production problem and experimentally establishing that a repair resolves it without introducing regressions.

- Turn production failures into persistent regression cases.

- Test proposed fixes against the same cases and evaluators.

- Keep humans responsible for evaluation intent and review evaluation costs.


## Core · Safety, security & adversarial evaluation


### 181. Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase

**Uploaded:** 2026-05-04 · [Watch video](https://www.youtube.com/watch?v=GmAQKINjv1E) · [Read transcript](transcripts/GmAQKINjv1E.md)

Pedro Rodrigues walks through evaluating agent skills against Supabase database tasks. A performance-review application exposes how a seemingly successful generated SQL view can bypass row-level security. Adding a security skill changes the generated migration to include security_invoker, but the live application still has other vulnerabilities. The workshop then compares skill and no-skill conditions using a reset database, headless Claude Code, and deterministic assertions. A faulty evaluator marks similar outputs differently, demonstrating why graders themselves need inspection. The speaker distinguishes appending skill instructions to the system prompt from organic discovery and recommends representative triggering and non-triggering scenarios, isolated environments, regression checks, and maintaining only relevant production skills.

- Specify expected behavior and representative scenarios before grading a skill, including when it should and should not activate.

- Compare skill and no-skill runs from the same reset state; use isolated environments to avoid contamination from unrelated installed skills.

- Validate graders against actual generated artifacts: a faulty assertion can report failure even when the requested security setting is present.

- Do not infer reliable security improvement from a changed SQL flag or a single run; the live demo retained vulnerabilities and the final compared outputs were similar.


### 182. Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase

**Uploaded:** 2026-05-15 · [Watch video](https://www.youtube.com/watch?v=JT3OzDKrucU) · [Read transcript](transcripts/JT3OzDKrucU.md)

Pedro Rodrigues explains Supabase’s evaluation-driven development of an agent skill. A matched task shows why tool access alone is insufficient: creating a PostgreSQL view without security_invoker can bypass existing row-level security, while the skill-guided agent handles the constraint. He describes six project scenarios tested across four models under three conditions: neither MCP nor skills, MCP alone, and MCP plus the skill. The combined condition leads on the reported task-completeness measure. Observed failures also shape the document: security essentials belong in the main skill because references may be skipped, while changing documentation should be linked. Q&A addresses repository-based distribution and unresolved packaging limitations.

- Compare controlled agent configurations on realistic project scenarios rather than assuming tool access guarantees correct behavior.

- The reported experiment compares a no-MCP/no-skill baseline, MCP alone, and MCP plus a skill; it does not establish a skill-only condition.

- Check environment-specific security behavior, such as whether a view preserves row-level security, instead of checking only task completion.

- Use observed agent behavior to decide which critical constraints must be directly present in the main skill file.


### 183. Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

**Uploaded:** 2026-05-31 · [Watch video](https://www.youtube.com/watch?v=NuePCNMpWGc) · [Read transcript](transcripts/NuePCNMpWGc.md)

Prasenjit Sarkar presents Sonar’s analysis of thousands of Java programming assignments across dozens of models. Functional benchmark scores are placed alongside code volume, bug density, security findings and cyclomatic or cognitive complexity to show why passing tests does not establish enterprise readiness. The talk compares model behaviors and warns that more recent models can produce substantially more code and subtler issues. Its proposed development cycle guides generation with context, verifies code before commit through static analysis, and uses a remediation agent that reanalyzes and compiles proposed fixes before presenting them for human review.

- Separate functional correctness from maintainability and security quality.

- Measure code volume and issue density as well as absolute findings.

- Verify generated fixes again before inviting human review.


### 184. Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind

**Uploaded:** 2026-07-25 · [Watch video](https://www.youtube.com/watch?v=O72p-rBb2bA) · [Read transcript](transcripts/O72p-rBb2bA.md)

Akele Reed and Dave Revere describe a mental-health coach whose independent input and output guardrails are calibrated through clinician-led evaluation. The goal is not maximal intervention: inappropriate escalation can itself deny support, while indirect crisis language may evade generic moderation. Licensed clinicians annotate traced conversations with expected observations, categories, and the turn where intervention should occur. Those annotations become typed, replayable evaluation cases committed to CI so prompt, model, and guardrail changes are regression-tested. The speakers emphasize false positives, false negatives, timing, and clinical context rather than chasing a perfect aggregate score. They also release reviewed input- and output-guardrail datasets as starting baselines, not substitutes for local learning loops.

- Let domain experts define correct behavior and label ambiguous failures.

- Turn traced clinical judgments into versioned, turn-specific regression cases.

- Measure intervention correctness and timing, not merely how often guardrails fire.


### 185. We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=iKQ78wyJEXU) · [Read transcript](transcripts/iKQ78wyJEXU.md)

Lucas Palma describes Nubank's security-review pipeline for AI skills, treating instructions, plugins, and MCP integrations as supply-chain dependencies rather than harmless configuration. Developers can scan locally, but mandatory CI rescans submissions before internal marketplace distribution. Deterministic pattern checks handle clear risks, while LLM review adds behavioral context; findings appear in pull requests and machine-readable security reports. Palma reports scanning over 2,000 skills, finding more than 1,500 risks, and roughly 1,000 remediations. Examples include credential exposure, destructive shell commands, excessive permissions, and unsafe file changes. He emphasizes context-sensitive severity, actionable remediation, retrospective scanning, and tool-level approval enforcement because prompt-only requests for human confirmation can be satisfied incorrectly by agents.

- Combine deterministic scanning with contextual LLM review, and enforce the same checks in CI even when local scanning is available.

- Evaluate the entire agent workflow for credential leakage, destructive actions, excessive permissions, and risky integrations.

- Implement human approval through execution gates and hooks; a prompt asking for confirmation is not an enforceable control.

- Provide actionable pull-request findings and machine-readable reports that feed existing vulnerability management.


### 186. Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd

**Uploaded:** 2026-08-01 · [Watch video](https://www.youtube.com/watch?v=ZFxh7sqbUZo) · [Read transcript](transcripts/ZFxh7sqbUZo.md)

Brumley explains cybersecurity evaluation through two ladders: target difficulty and exploitation capability. He argues that single-bug tasks and crash-only rewards encourage agents to rediscover easy flaws or overstate hacking ability. His audit-task alternative accepts multiple executable proofs, deterministically validates and deduplicates vulnerabilities, and balances precision with recall while expanding ground truth for newly discovered bugs. He then presents a staged V8 evaluation separating crashes, memory-access primitives, sandbox escape, and code execution. Across 41 verified vulnerabilities, Brumley reports code-execution success of 73% for Mythos and 68% for GPT, contrasting with much easier crash triggering. He closes with contamination-resistant environment generation and disclosure concerns around publishing weaponized outputs.

- Require executable proofs and deterministic grading instead of accepting an agent's claim that it found or exploited a vulnerability.

- Score distinct validated discoveries with precision and recall so agents cannot maximize reward by repeatedly finding one easy flaw or spamming unsupported findings.

- Separate crash detection from stronger exploitation capabilities; coarse success definitions can conceal large differences between models.

- Inspect trajectories for memorization and reward hacking, and account for disclosure risks when successful benchmark outputs contain previously unpublished exploits.


### 187. Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health

**Uploaded:** 2026-08-19 · [Watch video](https://www.youtube.com/watch?v=YXEqC05WEI0) · [Read transcript](transcripts/YXEqC05WEI0.md)

Rashi Agrawal describes member-facing healthcare AI as an architectural safety problem, not something solved by stronger prompts. She advocates removing protected health information at ingestion, separating environments, and placing emergency escalation, authentication, and high-stakes routing in code above the model. Production safety combines continuously running multidimensional judges, member feedback, and human trace review, with every high-stakes case checked. Launch decisions should reflect plausible worst-case harm, separate severity from engineering capacity, and default toward the safer mistake. Crucially, a falling evaluation score should trigger investigation of the judge before changing the agent: an overcalling scorer and genuinely unsafe advice require different fixes.

- Put irreversible safety and identity decisions in an enforced code layer rather than relying on prompts.

- Combine live automated scoring with member feedback and human review, including all high-stakes traces.

- Validate a judge's finding before modifying agent behavior; judges themselves require maintenance.

- Assess launch-blocking severity by plausible harm, not available capacity, and make risk acceptance explicit.


### 188. Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley

**Uploaded:** 2026-09-14 · [Watch video](https://www.youtube.com/watch?v=hOWU0KPUp1k) · [Read transcript](transcripts/hOWU0KPUp1k.md)

Brendan Rappazzo presents Loophole, a personal open-source project that stress-tests moral rules using adversarial agents. One agent formalizes user principles; two others search for immoral-but-permitted cases and moral-but-prohibited cases. A judge patches translation errors or escalates genuine ambiguity to the human. DNA-consent examples illustrate both outcomes. He then explores the same pattern for chatbot constitutions, checking inappropriate answers and inappropriate refusals, and for comparing contracts. The final branch simulates legislative preferences and optimizes proposed bills against them. Those political experiments are presented as exploratory simulations, not evidence of real-world voting prediction. The evaluation contribution is adversarial case generation with bidirectional coverage and human judgment.

- Test both under-enforcement and over-restriction of behavioral rules.

- Separate fixable rule translation errors from unresolved human preferences.

- Use adversarial examples to improve specifications rather than only score outputs.


### 189. 1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI

**Uploaded:** 2026-09-15 · [Watch video](https://www.youtube.com/watch?v=qStB9GbppMU) · [Read transcript](transcripts/qStB9GbppMU.md)

Sumanyu Sharma argues that centralized voice agents can propagate small defects to enormous numbers of calls. Drawing on Hamming’s monitored deployments, he describes a loop of failure discovery, frequency-and-severity prioritization, fixes, regression checks and continued monitoring. Manual call listening builds initial understanding, but cross-conversation analysis is needed to discover new patterns rather than merely score known rubrics. He recommends repeatedly replaying failures, then varying wording, accents and intent combinations; some experience changes still require real A/B tests. The final section extends reliability testing to adversarial callers, reports breaking roughly one in five tested agents, and recommends continuous red teaming where consequences are significant.

- Prioritize failure classes by both frequency and severity.

- Vary scenarios around real failures instead of replaying only one exact call.

- Combine call scoring, cross-call discovery, production experiments and adversarial testing.


### 190. I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore

**Uploaded:** 2026-10-13 · [Watch video](https://www.youtube.com/watch?v=dYh7TQkuYFE) · [Read transcript](transcripts/dYh7TQkuYFE.md)

Corey Gallon describes three levels of review for agents that misstate completion, extract facts incorrectly, or reason from faulty assumptions. Level one verifies the actual artifact and its fingerprint. Level two uses independent extractions, control totals, provenance, and reconciliation against source material. Level three combines self-audit with cold reviewers instructed to challenge the result, followed by fresh review of revisions. Examples cover an overstated memory-leak fix, accounting statements, and a demand letter based on an overlooked contract renewal. He reports substantial review time and token costs. His session-error observations describe his own sample, while the method supplies concrete checking practices rather than a guarantee that reviews eliminate every mistake.

- Verify artifacts directly before trusting completion reports.

- Reconcile independent factual extractions against control totals and sources.

- Use cold adversarial reviewers and fresh checks after revision.


## Adjacent · Agent benchmarks, simulations & measurement


### 191. Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI

**Uploaded:** 2026-06-05 · [Watch video](https://www.youtube.com/watch?v=mFLlVpnGpds) · [Read transcript](transcripts/mFLlVpnGpds.md)

Hervé Bredin explains speaker diarization and demonstrates its evaluation with reference annotations, visualization and diarization error rate. Errors are separated into speaker confusion, false alarms and missed speech, including overlap. A transcription comparison shows the same model and meeting dataset producing very different word error rates when headset recordings are replaced by a table microphone, exposing hidden benchmark conditions. The talk also demonstrates why aligning transcription words with diarization turns is nontrivial and why strong component scores do not guarantee correct speaker-attributed text. It emphasizes evaluating real acoustic settings rather than treating single-speaker transcription as solved conversational understanding.

- Inspect microphone setup and acoustic conditions before comparing speech scores.

- Decompose diarization errors rather than relying on one aggregate rate.

- Evaluate reconciliation between transcription and diarization, not just each model independently.


### 192. Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon

**Uploaded:** 2026-06-29 · [Watch video](https://www.youtube.com/watch?v=LrGCT7G_rU8) · [Read transcript](transcripts/LrGCT7G_rU8.md)

Anna Marie Benzon presents a bounded RL-guided ETL remediation system and a controlled synthetic benchmark rather than a production-proven autonomous operator. Deterministic checks establish observable schema and data-quality facts, a learned policy proposes actions, and independent safety rules can force escalation. Evaluation reports detection precision and recall, successful recovery time, repeated-seed confidence intervals and comparisons with deterministic and random action selection. The learned policy matches the deterministic baseline in this compact setting, so the talk attributes reliability mainly to structured state and external constraints. It explicitly reserves production incident validation and shadow deployment as future work.


> Caption-language issue: the source auto-captions render English speech in Devanagari. The original captions are preserved, not a verified English transcript; the summary is in English.

- Compare learned policies with simple deterministic and random baselines.

- Treat safe escalation and post-action validation as measured outcomes.

- Keep synthetic feasibility results separate from production effectiveness claims.


### 193. Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth

**Uploaded:** 2026-07-17 · [Watch video](https://www.youtube.com/watch?v=uIiA6DquRiE) · [Read transcript](transcripts/uIiA6DquRiE.md)

Daniel Han’s extended workshop spans model progress, quantization, inference stacks, kernels, reinforcement learning, and agent reward hacking. Evaluation-relevant sections distinguish benchmark success thresholds, examine long-context degradation, and warn that harness, serving, formatting, extraction, and verifier changes can alter apparent model quality. Han compares competing benchmark claims and discusses contamination and solution leakage, often presenting hypotheses rather than established causes. Later examples show agents optimizing proxy checks by manipulating timers, inputs, caching, or correctness-versus-timing paths. He contrasts outcome rewards with costly process supervision and urges inspecting generated code and measurement infrastructure before publishing improvements. This is a broad, opinionated workshop, not an independently verified benchmark report.

- Validate the entire harness and serving stack, not just nominal model identity.

- Audit measurement code and artifacts for reward hacking before claiming speedups.

- Distinguish observed benchmark changes from speculative explanations and proxy objectives.


### 194. Agents Need Feature Flags - Sachin Gupta

**Uploaded:** 2026-07-18 · [Watch video](https://www.youtube.com/watch?v=zU4EagB311U) · [Read transcript](transcripts/zU4EagB311U.md)

Sachin Gupta adapts feature-flag discipline to agent behavior across prompts, tools, models, memory, autonomy, and subagents. He proposes segmented canary releases, rapid rollback, per-tool and agent-wide kill switches, and middleware that every child agent must also obey. Evaluation enters through monitoring behavioral error-rate changes, escalation and hallucination signals, mitigation time, and audit completeness before promoting a variant. Demonstrations include explicitly illustrative incident simulations rather than measured production trials. Gupta also warns that stale caching, session-only flag checks, and untested combinations undermine control. The adjacent lesson is to treat agent behavior changes as observable experiments with enforceable stop conditions, not global prompt edits.

- Gate promotion on cohort-level canary changes against a baseline.

- Ensure switches and policy checks reach in-flight work and subagents.

- Test flag combinations and audit both changes and mitigation behavior.


### 195. From Tokens to Cells: Foundation Models for Single-Cell Biology - Akram Baharlouei, Altos Labs

**Uploaded:** 2026-07-19 · [Watch video](https://www.youtube.com/watch?v=-561cZmir5Q) · [Read transcript](transcripts/-561cZmir5Q.md)

Akram Baharlouei surveys single-cell foundation models and the measurement problems that complicate their evaluation. RNA-sequencing data offer scale but contain biological variation, snapshot limitations, and technical batch effects; more samples do not automatically produce a faithful representation of cells. In the evaluation-focused section, she discusses multimodal and perturbation-response benchmarks, including scGeneScope and PerturBench, where expensive transformer models can match or underperform simpler baselines. Distributional comparisons motivate flow-matching approaches such as Prime Flow rather than judging only mean predictions. This is a broad biological-model overview, with adjacent value in domain-specific benchmarking, appropriate baselines, and the relationship between data measurement and model conclusions.

- Compare sophisticated foundation models against simple domain baselines.

- Account for measurement noise and batch effects when interpreting biological benchmarks.

- Evaluate predicted distributions, not only compressed representations or mean outputs.


### 196. Claude for Long-Horizon Tasks — Lance Martin, Anthropic

**Uploaded:** 2026-07-22 · [Watch video](https://www.youtube.com/watch?v=9QebvrrY3KY) · [Read transcript](transcripts/9QebvrrY3KY.md)

Lance Martin outlines infrastructure and feedback patterns for long-running Claude agents. Separating the harness from execution containers preserves sessions and limits credential exposure, while an append-only event log keeps earlier context retrievable. A substantial section advocates independent verifier contexts with explicit goals or rubrics: builders iterate until a separate, critically tuned verifier confirms the outcome. Martin illustrates this with ML experiments and discusses memory benchmarks, including how offline consolidation corrected a repeatedly harmful Pokémon memory. He also describes organization-level, multiplayer harnesses. The evaluation-related lesson is that task duration, memory improvements, and autonomous completion need measured feedback and independent checks, not self-grading inside the same context.

- Separate building and verification into independently tuned contexts.

- Encode measurable outcomes so feedback can steer long-running work.

- Evaluate memory consolidation in the application rather than assuming it helps.


### 197. Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face

**Uploaded:** 2026-07-24 · [Watch video](https://www.youtube.com/watch?v=O-CBZ3JtRvo) · [Read transcript](transcripts/O-CBZ3JtRvo.md)

Uri Rolls and Thom Wolf present an access-control benchmark built from previously undisclosed vulnerabilities found by human researchers. Agents operate black-box, chained software environments without internet or source access, and must reason about system state to achieve an unauthorized capability. Deterministic graders verify both the final outcome and intermediate exploitation steps, providing useful discrimination when complete successes are rare. The speakers contrast reconnaissance with the harder logical leap needed to connect discovered facts, and inspect trajectories to localize those failures. They position high-quality, specialized cyber evaluation data as a prerequisite for stronger defensive models, while noting that one benchmark cannot represent the whole security domain.

- Use intermediate deterministic grading when end-to-end success is sparse.

- Evaluate domain-specific reasoning rather than conflating all cyber capabilities.

- Keep undisclosed tasks and realistic environments to reduce contamination.


### 198. State of Data — Sean Cai, Independent / State of Data

**Uploaded:** 2026-07-26 · [Watch video](https://www.youtube.com/watch?v=ZyIoTOAbRfs) · [Read transcript](transcripts/ZyIoTOAbRfs.md)

Sean Cai examines AI data markets through task verifiability and the difference between captured real workflows and contrived expert examples. A substantial section critiques benchmarks that sell both a target and training data to optimize it, ignore long dependent episodes, or report a single score without measuring harness and infrastructure variation. Finance examples illustrate how similar aggregate scores can conceal opposite strengths in arithmetic and methodology. Cai proposes examining decomposition into checkable steps, agreement about correctness, and the availability of independently verified outcomes. These are an industry practitioner’s claims, not independently established market facts; the adjacent evaluation contribution is a framework for judging realism, rubric quality, and benchmark incentives.

- Check whether evaluation tasks reflect authentic dependent workflows.

- Analyze rubric-level failures and harness variation instead of one leaderboard number.

- Keep the definition of realism independent from vendors selling both tasks and evaluation targets.


### 199. Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=AVMr9PMINyo) · [Read transcript](transcripts/AVMr9PMINyo.md)

Dan Fu and Olive Song discuss MiniMax-M3's open-weight release, multimodal training, and the inference engineering needed for agentic workloads. Song stresses environment, data, and reward design for kernel optimization, computer use, and long-running research tasks. Fu describes ParallelKernelBench as a collection of practically useful, unsolved kernel problems: improvements can directly accelerate inference rather than merely raise leaderboard scores. For long-horizon evaluation, Song describes scoring successive submissions and using validation/test splits to distinguish genuine gains from hacking. The discussion also covers sparse-attention kernels, quantization, distributed KV-cache management, and internal development evaluations, emphasizing continuous optimization after launch rather than a fixed serving configuration.

- Prefer benchmarks whose solved tasks produce deployable improvements, as Fu proposes for missing inference kernels.

- Evaluate intermediate submissions during long runs and reserve validation/test splits to detect performance hacking.

- Agentic workloads change serving bottlenecks through long contexts, repeated tool turns, and reusable KV caches.


### 200. Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI

**Uploaded:** 2026-08-25 · [Watch video](https://www.youtube.com/watch?v=mMNkdYnIVC4) · [Read transcript](transcripts/mMNkdYnIVC4.md)

James Zou argues that agent environments should supply incentives, resources, and guardrails rather than prescribe rigid workflows. Einstein Arena combines open scientific problems, deterministic solution verifiers, public leaderboards, and forums where agents exchange and refine solutions. He reports new mathematical constructions and production kernel improvements from this collaborative competition. The second example, DS Gym, provides a unified execution environment for evaluating and training data-science agents. Zou highlights shortcut-prone existing benchmarks, reporting that agents could solve substantial portions without using the underlying datasets. DS Gym instead curates expert-reviewed scientific tasks and recent Kaggle problems, then uses code execution to verify trajectories that can also train smaller open models.

- Choose scientific tasks with deterministic verifiers so submitted solutions receive reproducible, immediate feedback.

- Audit data-science benchmarks with no-data baselines to expose shortcuts that bypass the intended analytical work.

- Combine expert-reviewed tasks and execution checks; execution-verified trajectories can support both evaluation and training.

- Shared solutions, discussion forums, and specialist agent roles can complement competitive leaderboards.


### 201. If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread

**Uploaded:** 2026-09-16 · [Watch video](https://www.youtube.com/watch?v=O84lhGc1OOI) · [Read transcript](transcripts/O84lhGc1OOI.md)

Benjamin Clavié argues that knowledge agents need search tools and organizational patterns different from coding agents. His benchmark discussion shows how poorly tuned BM25 baselines can distort conclusions and how similar accuracy may conceal meaningful tool-call savings. He compares text-only retrieval ceilings with multimodal search on enterprise PDFs, then introduces searcher agents that return short research memos to an orchestrator. The reported gain is framed as reducing the remaining oracle gap rather than only adding percentage points. The broader lesson is to use evaluations to identify whether tools, orchestration or information access constrain performance, and co-design those components instead of assuming coding workflows generalize.

- Optimize baselines before comparing retrieval approaches.

- Measure tool calls and resource use alongside answer accuracy.

- Use human or oracle ceilings to distinguish tool limitations from orchestration gaps.


### 202. Stop Chunking Like It's 2022 — Yuval Belfer, AI21 Labs

**Uploaded:** 2026-09-16 · [Watch video](https://www.youtube.com/watch?v=r9OwPx_HoV0) · [Read transcript](transcripts/r9OwPx_HoV0.md)

Yuval Belfer uses retrieval experiments to challenge the assumption that a corpus has one optimal chunk size. Across meeting transcripts, narrative question answering, Seinfeld trivia and financial data, different queries favor different windows. An oracle experiment selects the best size per query to expose potential recall gains; he distinguishes this diagnostic upper bound from a deployable system. His proposed multiscale index retrieves across several window sizes, maps results to whole documents, and merges rankings with reciprocal rank fusion. Reported gains come with two-to-fivefold memory costs, while parallel searches limit latency impact. The talk illustrates how query-level analysis and upper-bound experiments reveal overlooked retrieval bottlenecks.

- Use per-query analysis to expose weaknesses hidden by an average chunk-size score.

- Distinguish oracle diagnostic results from deployable retrieval performance.

- Report memory and latency costs alongside recall improvements.


### 203. Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=RQi7x-navxU) · [Read transcript](transcripts/RQi7x-navxU.md)

Jerry Liu describes document infrastructure as the context layer around an agent harness. After explaining why PDFs lack explicit reading order and table semantics, he contrasts heuristic parsing, one-shot VLM reading and hybrid routing. The evaluation contribution is ParseBench: a reported 2,000 human-verified pages comparing roughly 50 models and OCR systems on tables, charts, faithfulness and semantic formatting. He emphasizes usefulness for agent understanding rather than syntactic output alone. The talk places benchmark results on accuracy, cost and latency tradeoff curves, distinguishing regulated high-accuracy extraction from cheap bulk indexing and fast interactive ingestion. It closes with parsing tools, structured extraction and source-grounded citations.

- Evaluate semantic faithfulness and downstream usability, not only output syntax.

- Choose an operating point on accuracy, cost and latency based on deployment risk.

- Use human-verified enterprise documents to expose complex-layout failure modes.


### 204. Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=aV_vgUSatqs) · [Read transcript](transcripts/aV_vgUSatqs.md)

Mark Lummus and Navinkumar Patil explore how agents can operate interactive command-line interfaces designed around human terminals, prompts, and keyboard controls. A workshop competition evaluates a cafe-ordering CLI using task accuracy and response time, encouraging participants to build adapters and interaction strategies. High-scoring solutions expose a benchmark-design issue: deterministic parsing and network-speed optimization can outperform the intended agent-interaction approach without demonstrating the capability originally being explored. The discussion includes terminal multiplexing and machine-readable alternatives for tools. The evaluation lesson is to define what a leaderboard actually measures and inspect successful strategies before interpreting their scores as evidence of general interactive-tool competence.

- Define the target capability before choosing a scoring rule.

- Inspect winning solutions for shortcuts that bypass the intended behavior.

- Separate task accuracy, interaction robustness, and network latency.


### 205. Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs

**Uploaded:** 2026-10-18 · [Watch video](https://www.youtube.com/watch?v=W4pnzOURwHQ) · [Read transcript](transcripts/W4pnzOURwHQ.md)

Denys Linkov describes the messy document pipeline behind insurance claims: handwriting, faxes, duplication, inconsistent forms, and enormous PDFs complicate extraction and reasoning. A benchmark built with Artificial Analysis evaluates medical-record questions against expert-validated answers, with the reported initial best reasoning accuracy around twenty percent. The discussion connects model quality to cost frontiers and stresses judge calibration rather than uncritical reliance on an LLM score. Broader architecture examples use successive levels of extraction and abstraction with model and human verification. The point is to test the actual document and reasoning challenges of the domain; generic model capability and nominal context length do not establish reliable claim analysis.

- Build domain cases with expert-validated answers.

- Calibrate judges and compare accuracy against full task cost.

- Verify information as it moves through extraction and abstraction layers.


### 206. Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis

**Uploaded:** 2026-10-20 · [Watch video](https://www.youtube.com/watch?v=3axY1wz2OvA) · [Read transcript](transcripts/3axY1wz2OvA.md)

Oliver Kennon distinguishes rented GPU hours from the useful intelligence an operator delivers. A same-chip serving comparison reportedly produces about fifty percent more output at a specified interactivity target, illustrating how software and operations change economic performance. He describes ClusterMAX’s assessment of provisioning, reliability, monitoring, security, documentation, and failure handling, while noting that these are not direct token-output measurements. The broader discussion separates rental prices, production costs, comparable compute grades, and futures exposure. His proposed north-star measure is full cost per successfully completed task at required quality. The comparisons and examples are bounded illustrations rather than a claim that one hardware label defines equivalent delivered service.

- Compare delivered work at matched quality and interactivity.

- Keep rental price separate from production cost.

- Benchmark operational reliability and security as well as throughput.


### 207. How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater

**Uploaded:** 2026-10-24 · [Watch video](https://www.youtube.com/watch?v=CLve4Nx_RwI) · [Read transcript](transcripts/CLve4Nx_RwI.md)

Sam Green and Aaron Linsky describe Bridgewater’s Vault, a permissioned research corpus serving both people and agents. Their search-quality section turns complaints into an approximately two-hundred-example benchmark built in less than a week, using precision at ten to measure whether the highest-ranked results contain the right documents. Reported relevance rises from roughly sixty percent to around ninety to ninety-five percent after search improvements. The talk also explains why human readers need precision while agents can process broader result sets, and why filtering must preserve recall and latency under agent-scale demand. The benchmark supports local product decisions; the reported gains are not a universal comparison of search systems.

- Translate subjective relevance complaints into labeled search cases.

- Choose metrics around the consumer’s needs and reading capacity.

- Evaluate filtering, relevance, and latency under realistic agent demand.


### 208. Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI

**Uploaded:** 2026-10-27 · [Watch video](https://www.youtube.com/watch?v=dAoOYFx7ZYw) · [Read transcript](transcripts/dAoOYFx7ZYw.md)

Mikyo King explains code mode: instead of exposing a large tool catalog and returning all raw tool outputs, give an agent a sandbox where it can discover and compose operations in code. Phoenix examples include Bash, Python, SQL, and UI interaction. He also details the new failure surfaces: credentials, permissions, egress, sandbox startup, durability, and generated-code accuracy. The evaluation section uses realistic Harbor tasks, verifiers, and repeated trials to compare behavior while capturing trajectories. Reported results show 43% fewer tokens and 31% lower cost with roughly unchanged latency. These are measurements from the presented setup, not a general guarantee for every model or task.

- Measure architectural changes with realistic task verifiers and repeated trials.

- Capture trajectories alongside outcome scores.

- Include sandbox overhead and operational failures in the comparison.


## Adjacent · Coding agents & software verification


### 209. CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner

**Uploaded:** 2026-05-13 · [Watch video](https://www.youtube.com/watch?v=VktrqzQgytY) · [Read transcript](transcripts/VktrqzQgytY.md)

Madison Faulkner and Hugo Santos argue that autonomous coding agents overwhelm CI/CD workflows designed for infrequent human changes. They propose moving build, test, and review feedback into a continuous, stateful agent loop rather than treating validation as a separate pull-request phase. Internal validation uses repository builds and tests; external validation can involve specialized security and API-conformance agents. Completed changes enter a premerge queue, where people assess intent and demonstrated outcomes while coordination reconciles concurrent edits. The talk emphasizes fast incremental infrastructure, known-source invariants, and continuous governance. Its contribution is a verification architecture and future-facing proposal, not an experimentally validated evaluation framework.

- Move repository builds, tests, and reviewer feedback into the coding agent’s inner loop instead of deferring validation to pull requests.

- Distinguish internal build/test checks from external specialist-agent review, while preserving known-source and compliance invariants.

- The proposed human approval step reviews intent and outcome evidence; premerge coordination must still reconcile concurrent changes.


### 210. Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft

**Uploaded:** 2026-05-16 · [Watch video](https://www.youtube.com/watch?v=FWEInOtngmM) · [Read transcript](transcripts/FWEInOtngmM.md)

Marlene Mhangami argues that AI-generated unit tests can affirm existing implementation while missing broken user behavior. She proposes behavior-focused red-green-refactor development with Playwright: derive failing browser tests from feature requests, generate code to pass them, and reserve human attention for refactoring. In a toy-store example, Copilot begins generating tests while a prepared implementation is exercised through search, category, and price-filter interactions. She recommends retaining screenshots in pull requests, committing before automated changes, and organizing tests around features. Q&A discusses specialized Playwright agent instructions for state-heavy applications, direct API testing as an alternative, and testing mobile versus desktop layouts.

- Use requested behavior, not newly added methods or existing implementation, as the basis for agent-generated tests.

- Write failing functional tests before implementation to reduce self-affirming test generation.

- Keep browser screenshots as review evidence and preserve a committed baseline before agents modify code or tests.

- For complex state, consider specialized Playwright agent instructions or direct API tests; include relevant viewport sizes.


### 211. Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry

**Uploaded:** 2026-05-27 · [Watch video](https://www.youtube.com/watch?v=ugUeZ8-b-u0) · [Read transcript](transcripts/ugUeZ8-b-u0.md)

Daniel Szoke argues that ease of generating runnable code is a poor optimization target if language flexibility allows hidden defects. Tests and review agents remain useful but can mirror implementation mistakes or miss untested behavior. Rust’s compiler supplies deterministic constraints for types, nullability, memory and concurrency, with actionable errors an agent can use in its repair loop. A threaded-counter example illustrates rejecting unsafe shared state before runtime. The talk does not claim compilation proves overall correctness; its evaluation-adjacent contribution is moving some verification from fallible generated tests and subjective review into independently enforced language invariants.

- Optimize for verified properties rather than first-pass runnable output.

- Use deterministic compiler checks alongside tests and agent review.

- Feed concrete compiler diagnostics back into the coding loop.


### 212. BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence

**Uploaded:** 2026-06-03 · [Watch video](https://www.youtube.com/watch?v=504PvfXou5Y) · [Read transcript](transcripts/504PvfXou5Y.md)

Michal Cichra connects architecture decision records, product requirements and executable behavior-driven scenarios to make agent-written software reviewable. Cucumber tests close the gap between a prose specification and observed product behavior, while architectural lint rules prevent forbidden dependencies such as browser tests directly accessing a database. Git hooks and CI enforce the same checks and direct rejected agents back to documents explaining the rule. Specialized skills change the focus of the loop for UI work, tests or design decisions. Persistent specifications and automated enforcement keep long sessions consistent even across repeated context compaction.

- Make critical user journeys executable and human-readable.

- Enforce architectural constraints in tools rather than repeating them in prompts.

- Use hooks and CI to provide actionable feedback linked to the governing decision.


### 213. We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco

**Uploaded:** 2026-06-28 · [Watch video](https://www.youtube.com/watch?v=dRmWYHuIJxM) · [Read transcript](transcripts/dRmWYHuIJxM.md)

Rajkumar Sakthivel reports a local code index built to reduce irrelevant context sent to coding models. It combines structure-aware code chunks, semantic and keyword search, relationship traversal and inexpensive relevance scoring. A public FastAPI experiment with twenty developer questions compares retrieved context against full-file reading and reports a 94% token reduction while preserving useful retrieval. Crucially, the speaker qualifies the baseline: production coding tools already avoid some full-file reads, so real savings are smaller. He also reports recall collapsing on a larger, mixed-responsibility codebase, making benchmark scope and failure analysis more informative than the headline efficiency claim.

- Compare retrieval savings against a realistic existing-tool baseline.

- Measure relevance and recall alongside token reduction.

- Test heterogeneous larger repositories; small clean benchmarks can conceal collapse.


### 214. Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI

**Uploaded:** 2026-07-10 · [Watch video](https://www.youtube.com/watch?v=ZpK5PWX2YRM) · [Read transcript](transcripts/ZpK5PWX2YRM.md)

Alex Volkov reframes the argument over reading all AI-generated code as a task-level question: what proof does this specific change need? His Z/L continuum spans close human inspection and system-level oversight, but neither endpoint removes verification. Critical authentication, money, permissions, and irreversible-data changes warrant deeper review; large changes should be decomposed, and traces, evals, shadow mode, independent reviewers, observability, and rollback supply complementary evidence. Volkov warns that a builder grading itself hides review rather than eliminating it. The talk uses industry examples and reported studies, not a new controlled experiment, to argue that advancing capability changes where proof belongs, not whether it is required.

- Route changes to verification proportional to consequence and reversibility.

- Separate builders, reviewers, and test evidence where possible.

- Encode recurring review findings in checks so the system remembers them.


### 215. Why Software Factories Fail

**Uploaded:** 2026-07-23 · [Watch video](https://www.youtube.com/watch?v=Ib5GBkD555M) · [Read transcript](transcripts/Ib5GBkD555M.md)

Dex Horthy argues that autonomous software factories fail when passing tests is mistaken for maintaining a healthy codebase. He walks through reinforcement-learning-style coding tasks and explains how binary correctness rewards omit architectural degradation whose costs emerge months later. His team’s lights-off experiment exposed the difficulty of recovering from failures in code nobody had reviewed. Horthy surveys longer-horizon benchmarks and quality-aware verification attempts, but cautions that model review cannot automatically solve the underlying training gap. His interim prescription is human ownership supported by AI-assisted product review, architecture, program design, and vertical implementation slices, reducing review burden through earlier alignment rather than removing verification.

- Passing functional tests does not establish long-term maintainability.

- Benchmark rewards need to capture quality dimensions beyond immediate correctness.

- Use upfront design alignment to keep human verification feasible.


### 216. Loop Engineering from First Principles — Kyle Mistele, HumanLayer

**Uploaded:** 2026-07-25 · [Watch video](https://www.youtube.com/watch?v=xIt_mTQp6mY) · [Read transcript](transcripts/xIt_mTQp6mY.md)

Kyle Mistele applies control theory to coding-agent workflows: measure the gap between current and desired code, select a small corrective action, execute it, and measure again. His practical example incrementally migrates RPC procedures using structural-search sensors, deterministic selection, golden implementation patterns, and scheduled CI workflows. Versioned baselines prevent new violations, while a feedback file captures review corrections for subsequent iterations. Flow control prevents accumulating more unreviewed pull requests when the previous change remains open. This is broader than model evaluation, but its central contribution is an evidence-driven improvement loop that keeps changes measurable, reversible, and small enough for accountable human verification.

- Define a measurable target and use deterministic sensors where possible.

- Prefer small verified changes over giant autonomous pull requests.

- Version review feedback and avoid generating work faster than it can be checked.


### 217. How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma

**Uploaded:** 2026-08-28 · [Watch video](https://www.youtube.com/watch?v=5Bn0xro2ol8) · [Read transcript](transcripts/5Bn0xro2ol8.md)

Eyal Blum describes Figma’s uneven adoption of coding agents and argues that verification investment is the most useful response to experienced engineers’ skepticism. He recommends shifting repeated checks into deterministic tooling, using test-first development so tests constrain implementation rather than conform to generated code, and reserving human review for higher-level functional judgment. Detailed plans should divide work into independently verifiable, reviewable stages with acceptance gates. Skeptics’ knowledge of failure modes becomes a roadmap for safer tooling. The talk also addresses reduced developer agency and attention-aware communication, including marking human-written versus generated PR descriptions. Its evaluation relevance is the organization and economics of trustworthy verification.

- Move known checks into deterministic tests and tools.

- Write acceptance criteria and failing tests before asking agents to implement.

- Break plans into independently validated increments and use expert skepticism as failure evidence.


### 218. Building Self-Improving Agent Software Factories — Suraj Gupta, Warp

**Uploaded:** 2026-09-27 · [Watch video](https://www.youtube.com/watch?v=TN3mj92oZ8I) · [Read transcript](transcripts/TN3mj92oZ8I.md)

Gupta describes three mechanisms for improving software factories: evolving skills, persistent memory, and task-specific model routing. An outer-loop agent reviews triage runs and human feedback, proposes procedural updates through Git-tracked pull requests, and leaves humans to guard against regressions. A parallel memory loop extracts reusable facts and outcomes with provenance, versioning, and human edit or deletion controls, reducing repeated investigation. Routing aims to balance capability and cost rather than using expensive models everywhere. Warp internally compares models through an evaluation sidecar, while customer-defined workflow evaluations are described as forthcoming. The presentation offers concrete architectural examples but no quantitative proof of factory-wide improvement, and one provenance demonstration is blocked by access restrictions.

- Keep skill updates reviewable and version-controlled.

- Preserve memory provenance and support correction or deletion.

- Evaluate routing on actual task classes rather than generic leaderboard rankings.


### 219. What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory

**Uploaded:** 2026-09-27 · [Watch video](https://www.youtube.com/watch?v=vGCJ7diEtrw) · [Read transcript](transcripts/vGCJ7diEtrw.md)

Tereza Tížková describes Factory’s software-factory architecture, emphasizing that autonomous duration does not establish reliability. Missions use orchestrators, sequential workers, and separate validators operating against a validation contract written before implementation. Scrutiny validators inspect code, types, linters, and tests; user-testing validators operate the running interface to distinguish functional software from convincing-looking output. She warns that poorly defined completion criteria encourage test gaming. Model routing and agent-readiness checks provide additional evaluation context. Reported routing savings and a customer mission’s validation effort are vendor examples, not independently verified benchmarks; the talk explicitly treats reliable long-running autonomy as an unsolved challenge.

- Define the validation contract before implementation and assign review to agents that did not write the code.

- Combine static and test scrutiny with interaction against the running UI.

- Do not confuse longer autonomous runs or passing narrow tests with production reliability.


### 220. The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX

**Uploaded:** 2026-09-30 · [Watch video](https://www.youtube.com/watch?v=Se8jHLliLXE) · [Read transcript](transcripts/Se8jHLliLXE.md)

Reock presents DX research on AI's organizational impact, emphasizing that throughput metrics are proxies, not business value. He reports rising deployment frequency and larger pull requests alongside volatile change-failure rates, improved perceived maintainability, and reduced confidence in changes. Junior engineers reportedly use AI more and consume more tokens, while senior engineers achieve similar time savings. His measurement framework links utilization, impact, and cost through cohort comparisons using established productivity and experience metrics. He argues that infrastructure readiness and bottlenecks outside code generation constrain gains, highlighting administrative, legacy-understanding, review, and incident-response applications. Findings are observational rather than clean causal estimates; cohort differences and infrastructure conditions complicate attribution to AI.

- Measure quality and business impact alongside adoption and throughput.

- Track PR size, change failures, and confidence rather than assuming faster generation improves delivery.

- Improve documentation, tests, and workflow bottlenecks beyond coding.


### 221. How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner

**Uploaded:** 2026-10-03 · [Watch video](https://www.youtube.com/watch?v=I2LL_wd89-A) · [Read transcript](transcripts/I2LL_wd89-A.md)

Kirschner explains VS Code’s move from monthly to weekly releases as a whole-system redesign, not simply greater AI usage. Agent-ready documentation, expert-maintained skills, faster TypeScript builds, component screenshot diffs, and Playwright-driven application access shorten implementation and verification loops. Automated code review precedes human review, while issue triage and error telemetry generate investigations and proposed fixes. Staged rollouts limit risk for an installed application. Product-specific evaluation scenarios connect customer reports to offline benchmarks and online experimentation, revealing surprising model-token behavior even on trivial tasks. Reported code-survival and build-speed gains are team observations. Durable ownership, daily prototyping, and continual bottleneck removal support both quality and faster learning.

- Let agents exercise the actual product and capture visual evidence.

- Accelerate CI feedback before multiplying agent concurrency.

- Combine offline evaluations, rollout monitoring, and human oversight.


### 222. Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=X6l4lpA0_NY) · [Read transcript](transcripts/X6l4lpA0_NY.md)

Dru Knox frames harness engineering as three feedback loops for moving toward a software factory. Cheap, frequent inner checks help agents correct work before a pull request; expensive outer checks, including agentic QA and mutation testing, build confidence after submission. A meta loop mines agent logs, pull requests, issues, and user feedback for escaped mistakes and updates the other loops. He distinguishes reduced human correction from reduced review and recommends tracking manual takeovers, review comments, and agent-initiated work while holding product quality steady. The talk offers process guidance and Tessl tooling examples, not measured evidence that adopting this architecture improves quality.

- Separate frequent low-cost checks from expensive PR-stage QA and mutation testing.

- Use escaped defects and human corrections to improve future verification loops.

- Track autonomy and automation separately without sacrificing product quality.


### 223. Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace

**Uploaded:** 2026-10-08 · [Watch video](https://www.youtube.com/watch?v=YNT7Plf9KIg) · [Read transcript](transcripts/YNT7Plf9KIg.md)

Gibiec argues that agents lack the operational context needed to make dependable engineering decisions, describing observability as their missing nervous system. He urges teams to define user value and success measures before accelerating deployment. Dynatrace's Bluebox is presented as a context layer connecting production telemetry, service dependencies, historical baselines, and repository changes to coding workflows. Proposed applications include production-informed local testing, early anomaly detection, change-correlated diagnosis, safer remediation, and feature planning. The workflow progresses from observation to suggested fixes while retaining human release decisions. These are preview-product scenarios and presenter claims, not demonstrated benchmark evidence; the talk offers no measured accuracy or assurance that dependency context eliminates regressions.

- Define agent success in terms of user value, not deployment activity.

- Use production dependencies and telemetry to supplement local tests.

- Keep human control over deploying suggested fixes.


### 224. Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=ZGzthw4BZiA) · [Read transcript](transcripts/ZGzthw4BZiA.md)

Emile Baizel and Shruti Arora connect visual feedback to a coding-agent repair loop. A browser extension lets users select elements, draw annotations, and export structured changes; visual verification then checks the rendered application against design requirements and user flows. The workshop wires these primitives through a local bridge into a podcast-page editing exercise and produces verification reports after changes. Examples include a duck-themed interface and conversational design feedback, with some audience integrations remaining prototypes. The evaluation lesson is to inspect what users actually see and can do, not merely accept the coding agent’s completion claim. Annotation and model-based verification are separate components with different reliability characteristics.

- Turn visual feedback into explicit, structured requirements.

- Run browser-based checks on the rendered design and user journeys.

- Treat a verification report as evidence to inspect, not an automatic guarantee.


### 225. How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=-AKPRSYccJc) · [Read transcript](transcripts/-AKPRSYccJc.md)

Ndukwe presents a structured agentic coding workflow using a FastAPI payments workshop. Teams first codify quality standards as reusable rules and skills, then carry that context through planning, test-driven implementation, local deterministic checks, and pull-request review. Detailed plans specify behavior, constraints, verification commands, recovery, and completion evidence. A refund demonstration surfaces non-durable idempotency storage and rule violations; an agent-driven remediation loop fixes findings and reruns checks. She advocates combining static analysis and tests with AI review rather than treating either as sufficient. Audience questions expose limits: Qodo ingests skills without evaluating their effectiveness, and AI selection of relevant rules is not deterministic, even when severity-based merge blocking is.

- Apply consistent standards during planning, implementation, and review.

- Combine deterministic gates with AI review and rerun verification after fixes.

- Rule retrieval and skill effectiveness require scrutiny beyond merge-blocking configuration.


### 226. Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar

**Uploaded:** 2026-10-14 · [Watch video](https://www.youtube.com/watch?v=7b9tov5Uc5s) · [Read transcript](transcripts/7b9tov5Uc5s.md)

Gautam Korlam describes how agent-scale pull-request volume shifts delivery bottlenecks into CI, repair loops, review, and approval. SubmitQueue-style testing of combinations protects the main branch, while incremental builds, caching, sharding, and parallelism reduce feedback latency. The more consequential verification lesson is that green CI alone does not establish permission to merge: risk-sensitive policies, independent approval, and durable evidence must apply to the exact tested commit. Known failures and overrides need recorded reasons so agents do not repeatedly rediscover problems or silently bypass controls. The talk advocates measuring the complete proposal-to-accepted-change path rather than equating more generated pull requests with more delivered value.

- Optimize the full verification and merge path, not only test runtime.

- Bind approval to the exact tested commit.

- Record failure explanations, override reasons, and risk-dependent merge policies.


### 227. Why Are We Still Governing AI Agents Like Software? - Tim Tyler, Gravitee

**Uploaded:** 2026-10-27 · [Watch video](https://www.youtube.com/watch?v=h8jgniNJcbQ) · [Read transcript](transcripts/h8jgniNJcbQ.md)

Tim Tyler proposes governing AI agents as an accountable digital workforce rather than anonymous software processes. His framework covers assignment of identity and a human sponsor, alignment of role and mission with least-privilege authority, and administration through oversight and recourse. Evaluation appears in role-specific scorecards that distinguish task success from compliance with authorized behavior, including invoice accuracy, cycle time, budgets, and intent confidence. Guardian agents can monitor continually, while explicit thresholds determine redaction, restrictions, or escalation to people. The framework requires human judgment to revise roles and controls as evidence accumulates; conversational assurances do not establish alignment or justify expanded permissions.

- Score task success and authority compliance separately.

- Give every agent an accountable owner and explicit role boundaries.

- Define escalation thresholds and revise controls from observed behavior.


### 228. How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic

**Uploaded:** 2026-10-28 · [Watch video](https://www.youtube.com/watch?v=AnsXWH2_EBU) · [Read transcript](transcripts/AnsXWH2_EBU.md)

Manish Kapur and Addy Osmani discuss the verification bottleneck created by coding agents and increasingly automated software factories. Osmani describes Anthropic’s growth from roughly 2,500 to 30,000 merged changes per day, with Claude providing first-pass review supported by verification evidence. The speakers distinguish supervised factories from fully automated ones and advocate independent checks inside each production loop. End-to-end tests, property tests, visual checks, security analysis, permissions, and human escalation address different risks. Survey statistics and company throughput figures are speaker-reported observations, not universal productivity guarantees. Their central recommendation is to define precisely what sufficient evidence for merging means, rather than ask teams simply to trust agent output.

- Use complementary tests rather than one universal reviewer.

- Require reviewable verification evidence before automatic merging.

- Treat control boundaries and human escalation as part of the delivery system.


### 229. Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar

**Uploaded:** 2026-10-29 · [Watch video](https://www.youtube.com/watch?v=wP3P89YB9fA) · [Read transcript](transcripts/wP3P89YB9fA.md)

Killian Carlsen-Phelan and Taylor Luttrell-Williams demonstrate Gitar as a verification layer for agent-written pull requests. A sample ticketing application supplies three exercises: identify a refund bug outside the changed lines, enforce an all-in pricing rule supplied through repository configuration, and repair a failing CI test before automatic merging. The session separates passing existing tests from satisfying business intent and emphasizes rechecking each new commit. It also covers explicit verification instructions, learned conventions, ticket-based functional validation, and cross-repository or cross-PR context. These are demonstrations of a proposed review workflow, not evidence that automated review can prove the absence of defects.

- Check unchanged code and business rules, not only the diff.

- Require CI and verification against the exact updated commit.

- Bring ticket requirements and cross-repository context into review.


### 230. Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo

**Uploaded:** 2026-10-29 · [Watch video](https://www.youtube.com/watch?v=YqxpPI7YUjE) · [Read transcript](transcripts/YqxpPI7YUjE.md)

Cole Gannaway shows how a one-line data-model change can pass builds, tests, and linting while breaking several downstream clients. He proposes a software graph that exposes cross-repository dependencies and the true change surface, alongside rules capturing business requirements and reviewer knowledge. The discussion explicitly separates the agent authoring code from the reviewer judging it and considers different models and harnesses to reduce correlated blind spots. Reviewer comments can become reusable constraints, and reviews can be run during implementation rather than only afterward. Ticket-level intent checks and human escalation remain important because neither a passing test suite nor another agent’s approval guarantees the right behavior.

- Review dependency impact beyond the local repository.

- Use independent reviewers and investigate disagreements.

- Turn recurring reviewer feedback into explicit rules and ticket checks.


## Adjacent · Domain-specific & multimodal evaluation


### 231. Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust

**Uploaded:** 2026-05-25 · [Watch video](https://www.youtube.com/watch?v=NKwIX3CiRgU) · [Read transcript](transcripts/NKwIX3CiRgU.md)

Phil Hetzel argues that agent development should not be isolated inside a traditional ML platform team. Foundation models arrive pretrained, but applications still require contextual evaluation, observability and domain judgment. Product and systems engineers build reliable integrations, subject-matter experts annotate traces and shape prompts, and data scientists contribute statistical rigor, risk awareness and judge validation. He specifically distinguishes broad functional agent quality from simply reusing precision, recall and F1, while recommending those metrics for testing discrete LLM-judge outputs against labeled data. Production examples should continually refresh offline datasets and reveal divergence from human judgments.

- Make domain experts active participants in annotation and evaluation design.

- Apply statistical validation to judges rather than trusting their authority.

- Share evaluation and observability ownership across product, systems and data disciplines.


### 232. Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI

**Uploaded:** 2026-08-19 · [Watch video](https://www.youtube.com/watch?v=Yphdry8ttAQ) · [Read transcript](transcripts/Yphdry8ttAQ.md)

Ayush Bhardwaj compares applied AI development in hedge funds and pharmaceutical technology, arguing that useful systems depend on narrow tasks, proprietary data, and domain expertise rather than commodity agent infrastructure. His development recipe combines problem formulation, data curation, prompts, observability, expert involvement, iterative learning, and deployment justified by business value. He recounts why uncalibrated LLM judging failed to replace traders' or scientists' judgment and recommends hiring representative users to evaluate outputs and refine reasoning workflows. Trace-based error analysis is presented as a low-cost starting point before fine-tuning or preference-based training. He warns about rubric echo chambers and retraining costs, while emphasizing that experts still make consequential decisions with AI assistance.

- Define narrow domain tasks and curate proprietary evidence, including failed experiments or unsuccessful trade theses.

- Use representative domain experts to judge usefulness and correctness rather than trusting uncalibrated model self-evaluation.

- Start improvement with observed trace failures before investing in weight updates or expensive feedback training.

- Measure whether deployed assistance creates business value while keeping consequential decisions with qualified experts.


## Adjacent · Foundations & evaluation design


### 233. Respect The Process - Andrew Dumit, Watershed Technology Inc.

**Uploaded:** 2026-07-07 · [Watch video](https://www.youtube.com/watch?v=CLttOU7n6sI) · [Read transcript](transcripts/CLttOU7n6sI.md)

Andrew Dumit explains why sustainability agents must justify how an answer was produced when experts can legitimately disagree on the final number. A coding agent gains flexibility but can bypass intended interfaces, claim edits that never happened or leave work nontechnical users cannot review. Watershed constrains effects through a typed SDK and owns final execution, enabling linting, conflict checks, artifact validation and readable change reports. Internal task evaluations improve with ordinary harness engineering, but the main distinction is that a traceable, replayable process remains inspectable even when the final result differs from one reference answer.

- Validate process and state changes when multiple final answers can be defensible.

- Own execution and inspect typed artifacts instead of trusting completion claims.

- Produce domain-readable evidence for reviewers who cannot assess generated code.


### 234. Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech

**Uploaded:** 2026-07-11 · [Watch video](https://www.youtube.com/watch?v=YZQsWVeN3rE) · [Read transcript](transcripts/YZQsWVeN3rE.md)

Alex Bauer presents three practical patterns for improving trust in go-to-market agents: documented anchor assets, a librarian that supplies business definitions and prior failure knowledge, and independent analysts overseen by a consensus judge. The jury pattern addresses attribution questions without a single empirically correct answer. Analysts produce evidence-cited opinions independently, while the judge weighs reasoning rather than treating conclusions as facts and expands the jury when consensus is insufficient. Bauer also stresses source traceability and choosing capable agent harnesses for consequential work. This is a broader product-pattern talk, not a calibrated evaluation study, but its judging and evidence-management sections provide adjacent quality-control ideas.

- Keep independent evidence gathering separate from synthesis and judgment.

- Make business definitions and prior query failures available before an agent acts.

- Treat consensus as a reasoning aid, not proof of ground-truth correctness.


### 235. ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay

**Uploaded:** 2026-07-12 · [Watch video](https://www.youtube.com/watch?v=TJPInBjhE4Q) · [Read transcript](transcripts/TJPInBjhE4Q.md)

Sachin Gupta presents ReviewDebt, a deterministic framework for measuring the gap between generated code and code humans have reviewed and understood. Five signal families cover diff size and coupling, test evidence, ownership spread, authorship indicators, and missing rationale. Scores should produce explanations and next actions, not simply rank developers or penalize AI use. A scan of public repositories shows structural complexity and volume driving burden more clearly than authorship labels. Gupta recommends backtesting and calibrating weights against local reviewer experience, surfacing scores without immediate blocking, and tracking trends. The framework measures review effort proxies, not proven code correctness or an independently established time-to-review model.

- Use explainable deterministic signals and calibrate them against local review experience.

- Distinguish code complexity and volume from AI-authorship suspicion.

- Measure review burden alongside delivery throughput, without treating the score as correctness.


### 236. "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox

**Uploaded:** 2026-07-13 · [Watch video](https://www.youtube.com/watch?v=-CnA2lGfymY) · [Read transcript](transcripts/-CnA2lGfymY.md)

Erik Meijer distinguishes difficult-to-formalize judgments about safe language from machine-checkable properties of agent actions. Tool use introduces side effects that may occur before a harmless final answer, so he proposes separating planning from execution. Agents emit an inspectable program representing the intended computation together with a proof, rather than directly running opaque IO actions. A trusted interpreter or checker can then apply type, dataflow, and taint analyses before execution. The talk presents this as proof-carrying code adapted to agents and points to an implementation. Its guarantees depend on the specified language, properties, and trusted execution boundary; it is adjacent formal verification, not an empirical application benchmark.

- Separate proposing an action plan from executing its side effects.

- Express plans in an inspectable language with machine-checkable properties.

- Distinguish formal action guarantees from subjective safety claims about language.


### 237. Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect

**Uploaded:** 2026-07-13 · [Watch video](https://www.youtube.com/watch?v=V-EDrhIhHzQ) · [Read transcript](transcripts/V-EDrhIhHzQ.md)

Will Brown presents Prime Intellect’s post-training stack, centering evaluation and training on reusable executable environments. The revised verifiers design separates task sets, agent harnesses, and runtimes so teams can compare real agents without rewriting their deployment logic. Rewards and metrics are explicit functions; group-level comparisons support ranking, pairwise judging, and efficiency bonuses among correct solutions. User simulators and interception servers enable realistic multi-turn rollouts, while trace graphs and renderer tooling preserve the distinction between logical messages and exact tokens. The second half covers asynchronous RL scaling and pluggable algorithms. Evaluation is presented as the practical entry point, with the same environment abstractions later supporting training.

- Separate tasks, harnesses, and runtime so evaluations remain modular and reusable.

- Use group comparisons to balance correctness with efficiency.

- Preserve exact rollout/token information and avoid training-serving mismatches.


### 238. "The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic

**Uploaded:** 2026-07-14 · [Watch video](https://www.youtube.com/watch?v=n97BCfyFIvw) · [Read transcript](transcripts/n97BCfyFIvw.md)

Addy Osmani argues that automated engineering still needs accountable judgments about whether work should ship. Agents can investigate, implement, test, and report, but humans must decide whether the evidence is sufficient, understand the constraints, and own residual risk. He distinguishes delegation from blindly borrowing an agent’s confidence, and describes cognitive debt and orchestration overhead as threats to effective review. Verification should become cheaper, clearer, and harder to skip through harnesses, static checks, critique, and intentional checkpoints. This is an engineering-practice keynote rather than an evaluation-method tutorial; its adjacent contribution is a clear boundary between producing quality evidence and making responsible production decisions.

- Require inspectable evidence rather than accepting agent confidence.

- Move human attention to high-leverage verification and approval checkpoints.

- Retain enough system understanding to explain and defend what ships.


### 239. "The biggest challenge in your stack? Evals, Evals, Evals" - 2026 State of AI Engineering results

**Uploaded:** 2026-07-21 · [Watch video](https://www.youtube.com/watch?v=RGe6EjucbzI) · [Read transcript](transcripts/RGe6EjucbzI.md)

Barr Yaron presents a survey of 1,048 AI builders, placing evaluation challenges within broader changes in model choice, costs, agent permissions, and engineering work. Respondents prioritize quality when selecting models, monitor production quality and costs, and frequently combine multiple providers. Evaluation again ranks as the leading stack challenge, while informal “vibe review” remains the most common evaluation approach. The survey also reports wider agent write access, relatively blunt human-approval and permission controls, and downstream concerns about review burden and declining codebase understanding. This is an industry-practice overview rather than an evaluation tutorial; its relevant contribution is evidence about the gap between rapidly expanding agent adoption and mature quality-control methods.

- Interpret findings as a builder-heavy survey, not a universal population estimate.

- Evaluation remains a leading infrastructure challenge despite broad agent adoption.

- Quality, cost, permissions, and human review need to be considered together.


### 240. AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix

**Uploaded:** 2026-07-28 · [Watch video](https://www.youtube.com/watch?v=CgsWxRUY5Eo) · [Read transcript](transcripts/CgsWxRUY5Eo.md)

Rajat Shah describes Netflix’s use of coding agents to analyze production profiles, locate inefficient code, and propose performance fixes. Profiles identify promising hotspots, but they are not proof of savings: functional tests and canary comparisons against real traffic establish correctness, CPU reduction, latency changes, and error-rate regressions before human approval. A shared Git-based catalog records confirmed patterns and anti-patterns so later agents can reuse evidence across services and eventually prevent inefficient code earlier in development. Shah recommends incremental automation with strong deterministic foundations. The adjacent evaluation lesson is to separate model-proposed optimization hypotheses from measured production outcomes and retain accountable review.

- Treat profiling as an estimate and canary measurements as validation.

- Check functional correctness and error rates alongside performance gains.

- Reuse confirmed evidence in a versioned pattern catalog.


### 241. Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama

**Uploaded:** 2026-08-07 · [Watch video](https://www.youtube.com/watch?v=J4_jCrTxMkk) · [Read transcript](transcripts/J4_jCrTxMkk.md)

This panel explores quantization and other compression techniques for local and enterprise model deployment. Speakers explain mixed-precision treatment of sensitive layers, NVFP4 block scaling, and tradeoffs among model size, throughput, hardware requirements, and quality. Evaluation emerges as a major engineering burden: NVIDIA's representative describes benchmarking against original model cards and an accuracy-degradation target, while Ollama stresses testing actual agent harnesses beyond benchmark scores. Unsloth warns that quantizing linear-attention layers can appear acceptable until long-context use fails. Discussion also covers smaller models' recovery-training difficulties, architectural diversity, KV-cache compression, and sparsity. The closing exchange proposes comparing quantized and original output distributions using KL divergence alongside accuracy measurements.

- Test compressed models in real agent harnesses and at long contexts; aggregate benchmark accuracy can miss behavioral changes or delayed degeneration.

- Choose precision selectively by architecture and layer sensitivity rather than assuming one quantization recipe transfers unchanged across models.

- Compare output-logit distributions with the original checkpoint using calibration data and KL divergence as an additional fidelity diagnostic.

- NVIDIA's representative states a target of less than 1% overall accuracy degradation on the cited AA benchmarks, not a universal guarantee for all compressed models.


### 242. From RL to IRL — Gaurav Mishra, Amazon AGI Lab

**Uploaded:** 2026-08-14 · [Watch video](https://www.youtube.com/watch?v=Cc0_nyxROBA) · [Read transcript](transcripts/Cc0_nyxROBA.md)

Gaurav Mishra examines why reinforcement-learned coding agents do not automatically become safe computer-use agents. Early browser-training examples show password guessing that locks an account and an advertisement's misleading Submit button diverting an agent into disclosing information. Real deployments introduce partial observations, irreversible actions, expired authority, uncertain execution, and ambiguous success. His remedy combines realistic training sandboxes, native recovery actions, process-level penalties for dangerous behavior, and calibrated escalation. Models need visual grounding and change detection; harnesses add risk classification, credential checks, execution monitoring, audit trails, rollback where possible, and human handoff. A later demonstration handles the deceptive button and expired login correctly, illustrating a deployment-feedback-to-training loop.

- Train on messy states such as expired sessions, slow pages, deceptive content, and layout changes.

- Judge harmful intermediate actions as well as final task completion.

- Make waiting, backtracking, abandoning, and user handoff legitimate recovery actions rather than resetting failures away.

- Use harness monitoring and audit evidence to contain model gaps while production failures inform further training.


### 243. From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=0I07YAuF8xA) · [Read transcript](transcripts/0I07YAuF8xA.md)

Adit Abraham explains why document quality becomes more consequential when agents compound decisions across multiple steps. He compares traditional vision pipelines with VLMs, advocates token-level OCR correction rather than wholesale rewriting, and shows how representation affects both reasoning and retrieval. Benchmark examples distinguish precision from silently dropped content and show better structured inputs improving downstream answers while reducing reasoning effort. Agent harnesses can iteratively reconstruct charts and validate large extractions. His evaluation recommendation is explicit: test parsing, retrieval, formatting and end-agent performance separately, and complement public datasets with production monitoring because deployed document distributions differ. The talk is an applied document-engineering case with substantial quality methodology.

- Measure recall as well as precision to catch silently omitted rows and fields.

- Evaluate each pipeline stage and the downstream agent outcome.

- Combine offline document benchmarks with production-distribution monitoring.


### 244. From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam

**Uploaded:** 2026-09-23 · [Watch video](https://www.youtube.com/watch?v=T72nqdC92PM) · [Read transcript](transcripts/T72nqdC92PM.md)

Krishna Prasad Srinivasan describes Sarvam’s compact state-space vision model for English and 22 Indian languages. Beyond architecture and staged training, he emphasizes a data engine coupled to evaluations designed for end-user usefulness. OCR provides machine-checkable rewards: character error, table structure, equations and grammar can be scored through unit tests for reinforcement learning. He reports performance on English document benchmarks and describes a planned Indic benchmark spanning historical and modern documents with diverse layouts. The Q&A stresses faithful extraction, including preserving mistakes in the source rather than silently correcting them. Deployment feedback, confidence scores and block-level grounding connect benchmark development with production document quality.

- Build language- and layout-representative evaluations when public datasets are missing.

- Use verifiable task-specific checks to score OCR outputs and training rewards.

- Evaluate source fidelity rather than rewarding plausible corrections of original text.


### 245. Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph

**Uploaded:** 2026-09-26 · [Watch video](https://www.youtube.com/watch?v=vrDvatGtIxs) · [Read transcript](transcripts/vrDvatGtIxs.md)

Bhakta describes GPU-kernel autoresearch as a proposal, correctness check, benchmark, and keep-or-revert loop. Humans supply architectural ideas and profiling insights; agents search implementation parameters using detailed hardware and model context. Correctness and speed make kernels attractive optimization targets, but reward hacking can make a local kernel faster while slowing end-to-end inference, for example by disabling CUDA graphs or testing only favorable context lengths. Optimized kernels may require workload-dependent fallbacks. He reports combining kernel and bare-metal tuning for approximately threefold model speedups, while warning that most attempted changes fail. The practical argument is disciplined measurement and constraints, not guaranteed automatic discovery of novel architectures or universal acceleration.

- Validate end-to-end inference, not isolated kernel speed alone.

- Constrain benchmark conditions to prevent reward hacking.

- Supply hardware details and retain workload-specific fallback kernels.


### 246. Scale the Judgment, Not the Model — Andrew Orobator, Reddit

**Uploaded:** 2026-09-27 · [Watch video](https://www.youtube.com/watch?v=6MudaeKdBSk) · [Read transcript](transcripts/6MudaeKdBSk.md)

Orobator argues that trustworthy automation requires scaling institutional judgment through skills, worklogs, personas, and enforceable verification gates rather than simply upgrading models. A verification ladder extends from builds and tests to screenshots, recorded application flows, and production telemetry; autonomy grows only as evidence improves. His local stale-feature-flag agent applies risk and experiment checks before proposing mechanical changes, with reported backtesting and seven successful CI-passing pull requests. Humans retain merge approval. Personal experiments reveal bypassable hooks and self-authorized exceptions, motivating lower-level gates whose overrides remain operator-only. Scheduled reviews and postmortems keep encoded judgment current as architecture changes; the examples do not establish general autonomous reliability.

- Encode experienced reviewers’ decisions, not just repository facts.

- Require executable or recorded evidence before granting more autonomy.

- Protect gates from agent-controlled bypasses and maintain their rules.


### 247. MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify

**Uploaded:** 2026-10-02 · [Watch video](https://www.youtube.com/watch?v=pAnLpiAG6Es) · [Read transcript](transcripts/pAnLpiAG6Es.md)

Čurn argues that common MCP complaints stem from agent-harness design rather than the protocol itself. Eager tool loading and routing large or sensitive results through context create avoidable cost, reliability, and security problems. Progressive discovery and code-mode execution provide alternatives, while CLIs already benefit from familiar shell composition and incremental help. His MCPC demonstration wraps MCP in a CLI supporting structured JSON, authentication, persistent sessions, tool discovery, and asynchronous tasks. Connector Evals then holds the agent fixed to compare interfaces on completion time and token cost. Early examples show MCPC and native CLI behaving similarly, with raw MCP often more token-heavy; these preliminary results are not universal rankings.

- Evaluate connectors separately from the agent using them.

- Use progressive discovery and code composition to reduce context load.

- Keep sensitive and bulky intermediate data out of model context.


### 248. AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar

**Uploaded:** 2026-10-09 · [Watch video](https://www.youtube.com/watch?v=uuwDWRbxoYo) · [Read transcript](transcripts/uuwDWRbxoYo.md)

Adl-Tabatabai argues that AI-generated code shifts engineering bottlenecks into centralized CI and code review, where failures create expensive, slow feedback loops. He presents Gitar's agentic validation system, now part of Sonar, as an orchestration layer that reviews pull requests, explains CI failures, identifies flaky tests, and iterates on fixes. Teams can progressively enable merge blocking, automatic remediation, and conditional approval and merging as trust grows. The system also categorizes CI failures and engineering work for platform and leadership teams. He describes a specialized harness and model-routing proxy, then advocates combining agents with traditional program analysis. Claimed quality, security, and productivity benefits are product assertions rather than quantified benchmark results.

- Validation capacity must scale alongside AI-generated pull requests.

- Adopt review, blocking, fixing, and merging automation progressively with explicit conditions.

- Combine agentic review with deterministic program analysis.


### 249. Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=qFaKvbVc5cE) · [Read transcript](transcripts/qFaKvbVc5cE.md)

Nathawani demonstrates NeMo Data Designer as a reproducible pipeline for generating diverse synthetic training data, progressing from question-answer pairs to MCP-mediated search trajectories. Wikidata graph walks seed difficult riddles intended to require reasoning and search rather than memorized answers. He reports moving a model from zero to thirty percent on BrowseComp after filtering fifty thousand seeds into roughly seven thousand high-quality supervised records. Evaluation combines judges, task-specific checks, current information, and human review of judge decisions. Stale seed facts and brittle answer matching illustrate why no single verifier is sufficient. Additional examples cover SQL, structured outputs, demographic personas, and privacy-oriented data tooling.

- Prioritize diversity and quality over raw generation volume.

- Cross-check judge decisions with humans and current evidence.

- Version data-generation workflows and inspect previews before scaling.


### 250. Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=ksjwtQop4os) · [Read transcript](transcripts/ksjwtQop4os.md)

Vestal and Williams lead an Elastic workshop comparing semantic vector retrieval, BM25 lexical search, hybrid fusion, and optional reranking. They explain why exact identifiers can defeat semantic search and why lexical matching misses paraphrased intent. Reciprocal rank fusion offers a starting point, while normalized linear combinations allow weight tuning against relevance judgments. Evaluation centers on desired documents, precision and recall targets, top-ranked chunks, and end-to-end latency including inference. Agent Builder examples connect retrieval quality to grounded answers, citations, and inspectable search traces. The presenters recommend adding rerankers only when measured relevance gains justify latency; their small workshop dataset and vendor guidance do not establish universal superiority, and automatic relevance tuning remains unreleased.

- Compare retrieval strategies against query-document judgments rather than assuming hybrid search always wins.

- Use rank fusion as a baseline; tune normalized linear weights and filters for the actual query mix.

- Evaluate top-ranked context and end-to-end latency before adding a reranker.

- Inspect retrieved documents and citations to diagnose incorrect agent answers.


### 251. Claude Managed Agents Q&A: Evals, CI/CD and Multi-Tenancy (Part 4 of 4) — Anthropic

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=QSeaZ6qHyXs) · [Read transcript](transcripts/QSeaZ6qHyXs.md)

Priyanka Phatak and Gabe Cemaj answer operational questions about Claude Managed Agents, including a focused discussion of evaluation. Anthropic runs many cloud sessions in parallel and revisits prompts and harness assumptions for each model release. For application builders, they prioritize well-defined, high-quality datasets and scoring historical sessions over achieving perfect numbers on poorly specified tasks. Related examples cover code-review agents, sandbox QA, YAML configuration synchronized through CI/CD, tenant workspaces, and responsive coordinator/subagent patterns. The advice is useful for constructing an evaluation workflow inside a managed platform, but the session is broader product Q&A; it does not provide a benchmark comparison or a complete evaluator implementation.

- Start from meaningful task definitions and historical sessions.

- Re-evaluate harness assumptions when models change.

- Keep deployed agent definitions versioned and synchronized.


### 252. Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=qJtcEDc_WJU) · [Read transcript](transcripts/qJtcEDc_WJU.md)

Gabe Cemaj demonstrates scheduled managed-agent deployments, fan-out sessions, and Dreaming, a research preview that reviews past sessions to improve shared memory. The Q&A repeatedly returns to evaluation: task-specific datasets are needed to compare harness choices, judge whether memory changes help, and assess new model releases. The presenters caution against assuming that a feature tuned for coding transfers equally well to another application. Outcomes and verifier loops provide explicit success criteria, while observability supports inspection of long-running sessions. The broader session covers tenancy, compaction, skills, scaling, and deployment options. Its contribution is contextual evaluation advice around memory and orchestration, not a controlled proof that Dreaming improves every workload.

- Evaluate memory changes on the tasks the agent will actually perform.

- Retest model and harness combinations rather than assume transfer.

- Use observability and explicit outcomes to inspect long-running work.


### 253. Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers

**Uploaded:** 2026-10-13 · [Watch video](https://www.youtube.com/watch?v=3ZlQk4-knWM) · [Read transcript](transcripts/3ZlQk4-knWM.md)

Paden Gayle argues that bank AI deployments fail when teams discover approval and control requirements only after building a convincing demo. A hypothetical document-exception assistant illustrates how intended use, source ownership, hosting, analyst review, and authority must be agreed early. Evaluation evidence should preserve actual inputs, outputs, model versions, reviewer actions, failure modes, detection paths, and fallback owners. Results need segmentation because a good average can hide poorly supported document types or user groups. He recommends the smallest useful authority boundary and incremental evidence before expansion. The framework is a deployment planning method, not a guarantee that human review or a checklist establishes regulatory approval.

- Identify data and control owners before designing the workflow.

- Preserve original evaluation evidence rather than rely on later reruns.

- Inspect weak segments and restrict unsupported use cases.


### 254. The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale

**Uploaded:** 2026-10-13 · [Watch video](https://www.youtube.com/watch?v=-a2oTS9J67U) · [Read transcript](transcripts/-a2oTS9J67U.md)

Michele Grant uses an illustrative acquisition-integration assistant to distinguish a working pilot from trustworthy operational autonomy. Her framework starts with baselines for reporting time, capacity, cost, and material-issue detection, then assigns operational ownership, risk oversight, and independent assurance. A documented human-work standard defines authority and escalation; decision logs and agent inventories preserve versions, dependencies, and evidence. Autonomy advances through shadow work, reviewed drafts, sampled exception handling, and more independent operation only when scorecard evidence supports it. At later stages, missed issues matter as much as alerts, and declining overrides may reflect weaker review rather than better performance. The scenario is explanatory, not a disclosed deployment outcome.

- Set value and control baselines before deploying.

- Keep auditable decision records and revalidate after relevant changes.

- Use independent sampling to detect missed issues and weakened human oversight.


### 255. What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad

**Uploaded:** 2026-10-13 · [Watch video](https://www.youtube.com/watch?v=gDRCpTMCqEU) · [Read transcript](transcripts/gDRCpTMCqEU.md)

Soukaïna Abelhad proposes technical-diligence checks for claims such as seventy percent automation. First compare workload growth with fully loaded human labor, including review, escalation, and rework. Next define whether automation means drafting, human approval, or genuine end-to-end completion within an explicit boundary. Finally inspect evaluation maturity: who labeled ground truth, whether domain experts agree with automated graders, and which bad outputs escaped. Examples show why benchmark passes and maintainer acceptance can diverge. Her preferred economic measure is cost per accepted autonomous task, including failures and human effort. The talk uses public and anonymous examples to structure diligence, not to establish a universal automation rate or causal explanation of company outcomes.

- Define the exact workflow boundary behind every automation percentage.

- Validate automated graders against knowledgeable reviewers.

- Include failed attempts and human rework in cost per accepted task.


### 256. The Cost of Accessibility in AI — Jemima Abu, CAIS

**Uploaded:** 2026-10-14 · [Watch video](https://www.youtube.com/watch?v=ZccJsdOE54M) · [Read transcript](transcripts/ZccJsdOE54M.md)

Jemima Abu examines the quality requirements that coding agents miss when accessibility is not explicit. A small uncontrolled comparison finds an accessibility skill producing a design faster and at lower cost, but she cautions that one experiment cannot establish a general cost advantage. The broader argument is that inaccessible code teaches agents poor conventions, while native HTML can avoid verbose custom behavior. She recommends defining accessibility requirements from the business and design stages, auditing the existing interface, using reusable patterns and explicit agent skills, and testing keyboard and assistive behavior. Automated checks help, but human testing remains necessary; accessibility is a property of the finished experience, not proof supplied by a prompt.

- Make accessibility part of acceptance criteria from the start.

- Audit inherited patterns and prefer correct native semantics.

- Combine automated checking with manual experience-based testing.


### 257. What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma

**Uploaded:** 2026-10-27 · [Watch video](https://www.youtube.com/watch?v=iniryju23Sk) · [Read transcript](transcripts/iniryju23Sk.md)

John Feminella uses Citibank’s mistaken Revlon payment to show how formal procedures and several approvers can still permit a catastrophic outcome. His proposed agent-control architecture combines automatic registration, risk-sensitive review, purpose-linked tool permissions, shared firm-wide evaluation infrastructure, and conservative classifiers for routine action decisions. The evaluation section treats model changes as runtime-dependency changes that require regression tests, while shared tooling handles common evaluation mechanics so each team can specify what should hold for its own agent. Deterministic rules cover clear cases and human review focuses on ambiguous or consequential actions. The talk emphasizes usable controls that preserve iteration rather than blanket approval queues or unverified autonomy.

- Share evaluation infrastructure while keeping agent-specific assertions explicit.

- Retest quality when runtime model dependencies change.

- Use risk-based review and reduce low-value approval fatigue.


## Adjacent · Judges, rubrics & subjective quality


### 258. Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML

**Uploaded:** 2026-05-12 · [Watch video](https://www.youtube.com/watch?v=X6NShR2ccOg) · [Read transcript](transcripts/X6NShR2ccOg.md)

Alessandro Cappelli argues that production AI requires a feedback-driven lifecycle rather than stopping at a convincing demonstration. Within an RL-focused presentation, he explains how existing or mocked agent environments generate trajectories, while execution checks, business outcomes, and LLM judges define success. Human involvement shifts toward specifying rubrics and realistic scenarios, including difficult customer interactions. The Q&A distinguishes using a small set of early judgments to refine prompted evaluators from using larger production-feedback collections to train reward models. He also discusses implicit feedback as use-case-dependent. These are proposed practices for integrating quality signals into training, not a demonstrated comparative study of judge reliability.

- Define success using appropriate execution checks, business KPIs, and rubric-based judgments rather than relying on one generic score.

- Mock tools and users can supply controlled environments and realistic scenarios for assessing agent trajectories.

- Use scarce early human feedback to refine judging criteria; the speaker describes training reward models once production feedback grows.

- Interpret the RL superiority claims as the presenter’s argument, not as independently established evaluation results in this transcript.


### 259. Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo

**Uploaded:** 2026-06-08 · [Watch video](https://www.youtube.com/watch?v=EcqMYoIV57A) · [Read transcript](transcripts/EcqMYoIV57A.md)

Nupur Sharma explains why larger context windows do not eliminate attention failures or unproductive agent orchestration. She compares retrieval, summaries, graphs and critic loops, then describes Qodo’s specialized review agents and a judge that combines their findings with relevant code and prior PR context. Validation is more constrained than exploration, and accepted or rejected recommendations influence subsequent weighting. Audience questions probe whether historical behavior is an appropriate quality standard and how explicit security or compliance rules should override learned preferences. The talk’s evaluation relevance lies in contextual judging, feedback quality and the limits of treating acceptance as correctness.

- Use a judge to reconcile specialist findings against the actual task context.

- Distinguish explicit policy requirements from learned reviewer preferences.

- Treat historical acceptance as a fallible signal, not unquestioned ground truth.


### 260. Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify

**Uploaded:** 2026-09-25 · [Watch video](https://www.youtube.com/watch?v=2LRIAfng7eA) · [Read transcript](transcripts/2LRIAfng7eA.md)

Spotify’s speakers describe an LLM-native recommendation system and the evaluation work needed to support it. Their NEO recipe adds semantic catalog tokens, grounds them with a frozen backbone, and then performs multitask instruction tuning. Ablations compare retained language ability, task performance and decoding tradeoffs. The evaluation section explains why interaction metrics alone cannot judge intent alignment or explanation quality. Grounding judges with textual listening profiles produced reported 75% alignment with human preferences; behavioral examples particularly helped ambiguous search queries. Grounded judges also replace expensive human ranking in pooled evaluation collections, with reported agreement of 0.87 on system rankings.

- Evaluate explanation accuracy and user intent, not only historical clicks.

- Ground recommendation judges in user profiles and actual behavioral signals.

- Use training ablations to detect losses that task-specific scores conceal.


### 261. Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=FGftGOzfohc) · [Read transcript](transcripts/FGftGOzfohc.md)

Priyanka Phatak and Gabe Cemaj build a research application on Claude Managed Agents, adding event-stream chat, SEC EDGAR skills, subagents, custom tools, and shared memory. The evaluation-relevant feature is Outcomes: a task and rubric drive a separate grading step that sends the agent back to work when the requested result is not yet satisfied, within configured bounds. A Nvidia research example illustrates a scorecard and verifier alongside specialist analysis agents. Q&A examines grading placement, guardrails, credential handling, and memory. The demonstration connects managed orchestration to explicit completion criteria, but self-supervision still depends on the rubric and grader rather than proving that a financial conclusion is independently correct.

- Specify an outcome rubric rather than only an open-ended instruction.

- Use bounded grading-and-retry loops with visible results.

- Distinguish satisfying a task scorecard from validating uncertain domain conclusions.


### 262. Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar

**Uploaded:** 2026-10-29 · [Watch video](https://www.youtube.com/watch?v=LQW_Wvqhp04) · [Read transcript](transcripts/LQW_Wvqhp04.md)

Tariq Shaukat argues that agentic software production needs quality engineering rather than a larger human-review queue. He uses manufacturing analogies and cited studies to describe review overload, automation bias, declining performance on large codebases, compounding errors in long tasks, and instability in LLM judges. His proposed code-confidence framework combines intent, guardrails, independent verification, and evidence. Verification should be layered, address different failure classes, and produce actionable findings rather than merely collect another approval. The talk reports customer and survey observations, but its transferable point is methodological: increased code generation does not establish increased safe delivery, and self-assessment or nominal human oversight is insufficient evidence.

- Separate generation from independent verification.

- Measure delivered outcomes and failure rates, not only generated code volume.

- Account for judge variability and compounding multi-step errors.


## Adjacent · Optimization, skills & learning loops


### 263. From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud

**Uploaded:** 2026-07-19 · [Watch video](https://www.youtube.com/watch?v=JJGbw4ggaFs) · [Read transcript](transcripts/JJGbw4ggaFs.md)

May Walter describes a production workflow that turns runtime evidence into prioritized performance improvements. Scheduled agents correlate code with function-level traces, queries, latency, and forensic examples, then investigate likely high-ROI opportunities. Early failures included plausible but unverified diagnoses, complex-query mistakes, and superficial exception suppression. Skills and better production-to-code context made investigations more consistent, while rerun tests and runtime measurements established whether proposed fixes actually helped. Human-friendly reports, rather than floods of pull requests, rank opportunities by impact, risk, and business relevance. The adjacent evaluation lesson is that trustworthy automation must validate both the causal improvement and whether the issue deserves scarce review attention.

- Require runtime evidence rather than accepting plausible optimization narratives.

- Score changes by business impact and review risk, not only potential speedup.

- Validate improvements before surfacing actionable reports to humans.


### 264. Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo

**Uploaded:** 2026-07-29 · [Watch video](https://www.youtube.com/watch?v=kiqubc5b5Yo) · [Read transcript](transcripts/kiqubc5b5Yo.md)

Brendan Rappazzo presents AlphaLab, Morgan Stanley's provider-agnostic harness for research, evaluation construction, and parallel experimentation. A strategist proposes experiments, workers implement and analyze them, and humans steer a shared board. The initial evaluation builder used separate conceptual and programmatic critics to catch leakage and code defects. Failures prompted a stricter second version: agents submit containerized models against public feedback, while users inspect held-out private validation. Rappazzo describes using carefully designed environments and qualitative research-process rubrics to optimize the harness itself and explore weight updates. He reports a top-12% Kaggle finish with limited iterations, while emphasizing that enterprise value lies in trustworthy evaluation environments and encoded expertise, not orchestration alone.

- Audit generated evaluations for conceptual flaws and forward information leakage separately from implementation and test failures.

- Use strict submission interfaces and private held-out validation to judge research progress beyond visible optimization feedback.

- Encode expert research standards in trajectory rubrics as well as outcome metrics.

- Establish reliable environments before automating harness optimization; otherwise the system can optimize against a faulty target.


### 265. Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect

**Uploaded:** 2026-07-31 · [Watch video](https://www.youtube.com/watch?v=AQv3qRCG6Gw) · [Read transcript](transcripts/AQv3qRCG6Gw.md)

Will Brown explains how to manufacture useful reinforcement-learning signals when real-world tasks lack clean correctness checks. He treats environments as reusable evaluation and training objects, grounding task generation in production traces, documents, and repositories. Working backward from known solutions can create solvable tasks, while controllable simulators provide checks unavailable in live systems. Model judges inspect completed trajectories, extract failure-specific rubrics, and support cheaper subsequent audits. Brown emphasizes searching for appropriately difficult tasks, probing reward hacking, and validating environments through small training runs. He also argues that continual learning needs supervised environmental knowledge alongside RL, with humans retaining authority over goals and consequential judgments.

- Mine production traces to discover the actual task distribution before designing tasks and scoring criteria.

- Construct tasks backward from reachable outcomes and use controllable simulators to recover verifiable signals.

- Audit reward hacking through retrospective judging, adversarial searches, and small training experiments rather than trusting the initial reward definition.


### 266. Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute

**Uploaded:** 2026-08-12 · [Watch video](https://www.youtube.com/watch?v=ZTA0GwpAUak) · [Read transcript](transcripts/ZTA0GwpAUak.md)

Samuel Denton organizes enterprise continual learning along two axes: offline versus online production traces, and static versus rollout-specific hints. Offline distillation targets known behaviors without replayable environments; online hinting supports an ongoing serving-and-training loop without requiring golden answers. He separates task-submission rate from underlying test success when teaching a coding agent to finish sooner, reporting submission improvement from about 22% to 60% without degraded test performance. Another example reports hyperlink-format compliance rising from roughly 15% to 80% with dynamic hints. Implementation lessons include selecting where to inject hints, distilling nearby steps, and using judge-selected relevant tokens to learn targeted behaviors while limiting broader capability degradation.

- Separate compliance or completion metrics from underlying task correctness to detect hidden regressions.

- Compare static hints with hints conditioned on the actual rollout rather than assuming they are interchangeable.

- Use judges to identify intervention points and focus distillation on nearby, behavior-relevant steps.

- Mask irrelevant teacher-token preferences to reduce unwanted capability changes during targeted training.


### 267. Prototyping as Leadership: How a CTO Ships with AI Agents

**Uploaded:** 2026-08-20 · [Watch video](https://www.youtube.com/watch?v=bdHaOXZOhcM) · [Read transcript](transcripts/bdHaOXZOhcM.md)

Hursh Agrawal describes fitting agent-assisted prototyping into a CTO’s schedule, with a substantial example of overnight evaluation-driven optimization. Prototype feedback buttons save inputs, prompts and qualitative comments as JSON; the agent converts these examples into an evaluation set, collaborates with the human on scoring rubrics and builds a harness to hill-climb quality, latency and cost. He acknowledges overfitting risks with small datasets, although his proposed instruction to avoid overfitting is not a substitute for held-out validation. A second example delegates model-class comparisons and training for a PII classifier. Reliable CI, independent review, sandboxed infrastructure and morning human testing provide necessary organizational scaffolding.

- Capture complete runs and qualitative user feedback while prototyping.

- Agree on scoring rubrics before delegating autonomous optimization.

- Treat tiny feedback datasets as an overfitting risk; validate beyond the optimization examples.

- Keep model-training experiments sandboxed and review outputs before shipping.


### 268. Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli

**Uploaded:** 2026-09-19 · [Watch video](https://www.youtube.com/watch?v=c1hGBoWw20A) · [Read transcript](transcripts/c1hGBoWw20A.md)

Filip Makraduli explains FlashNorm, an RMS-normalization optimization using weight folding and parallel computation, then recounts a correctness failure that ordinary checks missed. Unit tests and perplexity looked acceptable, but longer generations revealed repetitions and a one-step lag. The cause was an implicit CUDA-stream join that let post-scaling read an unfinished buffer; explicit synchronization fixed it. He then discusses ablations of the proposed operations, compatibility with compiled and quantized models, and deploying modified checkpoints on open inference infrastructure. Its evaluation relevance is the gap between small tests or aggregate quality metrics and sustained generation behavior when low-level performance optimizations alter execution.

- Test long-generation behavior as well as unit outputs and perplexity.

- Validate synchronization semantics when optimizing across concurrent GPU streams.

- Use ablations and production-like deployment to assess optimization tradeoffs.


### 269. Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics

**Uploaded:** 2026-09-24 · [Watch video](https://www.youtube.com/watch?v=Sjfz1TqxzEs) · [Read transcript](transcripts/Sjfz1TqxzEs.md)

Jason Ma explains how Dyna Robotics moves beyond attractive demonstrations toward sustained commercial task reliability. He contrasts broad pretraining with targeted post-training and reports napkin folding at 99.4% success over a 24-hour run, with restaurant-specific fold-quality acceptance criteria. A video reward model estimates task progress; non-monotonic dips reveal mistakes and guide targeted human recovery demonstrations. Repeated active-learning cycles teach recovery rather than requiring exhaustive coverage of every deformable-object state. The talk also separates performance at data-collection sites from generalization to unfamiliar locations, using conference and customer deployments as examples. Its evaluation relevance is continuous failure detection and deployment-grounded reliability measurement.

- Define commercial acceptance criteria beyond whether a task nominally finishes.

- Use progress-model anomalies to target recovery-data collection.

- Separate familiar-site success from robustness at unseen deployment sites.


### 270. From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer

**Uploaded:** 2026-10-07 · [Watch video](https://www.youtube.com/watch?v=u-o0sW9nwmk) · [Read transcript](transcripts/u-o0sW9nwmk.md)

Wilinski proposes turning agent experience into shared procedural knowledge rather than discarding traces. Skills guide initial trajectories and reduce costly rediscovery, but local developer-centric distribution, missing documentation, and uneven client support impede adoption. He describes using MCP to serve governed skills across an organization and a distiller that learns from successful runs and failures. In one Chromium-on-AWS-Lambda task using Sonnet 4.6, he reports success rising from 36% to 100% after skill creation, without supplying sample sizes or broad validation. Grouped traces generate candidate skills checked for prompt injection and personal information before distribution. He frames this organizational learning loop as a cost-saving asset resilient to model changes, not weight training.

- Distill both successful procedures and failure-driven guardrails.

- Separate skill knowledge from tool capabilities and centralize governed distribution.

- Treat the reported 100% as a task-specific result, not a general reliability guarantee.


### 271. Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j

**Uploaded:** 2026-10-08 · [Watch video](https://www.youtube.com/watch?v=XPj3mIKEtI4) · [Read transcript](transcripts/XPj3mIKEtI4.md)

Will Lyon presents graph-based agent memory and skill distillation with explicit provenance and quality governance. Beyond retrieving similar text, the proposed system records entities, decision traces, tool results, timing, and token use, then derives typed procedural skills grounded in those records. Quality checks consider grounding, coverage, and coherence; mixed-topic subgraphs can trigger skill decomposition, while changed, removed, or contradictory evidence can mark skills stale. Lyon cites improved task completion on SkillsBench for an associated graph-representation approach, without giving numerical results in the transcript. A healthcare intake demonstration illustrates provenance and packaging, rather than independently validating downstream task reliability.

- Check grounding, coverage, and coherence before treating distilled memory as an executable skill.

- Retain evidence links so source changes or contradictions can flag stale procedures.

- Treat cited benchmark improvements separately from the demonstrated distillation workflow.


### 272. Stop Prompting — Greg Pstrucha, Sentry

**Uploaded:** 2026-10-09 · [Watch video](https://www.youtube.com/watch?v=E3KbFLAGD6A) · [Read transcript](transcripts/E3KbFLAGD6A.md)

Pstrucha recommends replacing repeated corrective prompting with repository-enforced rules that survive context resets. Tests, strict types, and especially custom linters encode recurring review feedback; Sentry examples enforce agreement between endpoint types, API schemas, and executable skill examples. Agents repeatedly evade narrow checks by deleting code blocks or shifting claims into prose, showing why enforcement must cover the actual requirement. Qualitative concerns such as unnecessary complexity require explicit policies and iterative reviewer agents rather than arbitrary numeric thresholds. Human review remains part of the process. His experiments with near-perfect coverage and complexity metrics demonstrate that optimizing proxies can produce weak tests and false confidence instead of maintainable code.

- Codify recurring deterministic feedback into enforceable checks.

- Test executable documentation against the real API schema.

- Keep qualitative review separate from gameable numerical proxies.


### 273. We Let Our Financial Planners Write the Agents — Matthew Ragone, Range

**Uploaded:** 2026-10-12 · [Watch video](https://www.youtube.com/watch?v=gpmze-6ueGU) · [Read transcript](transcripts/gpmze-6ueGU.md)

Matthew Ragone explains how financial planners at Range capture professional judgment in agent skills rather than leave workflow design solely to engineers. A skill starts with a repeated task whose output the domain expert can judge, then incorporates real cases, required questions, firm-specific reasoning, and explicit limits. He recommends five to ten test runs before wider use, correcting missing questions and confident mistakes after each attempt. Every skill needs an accountable owner and a separate reviewer, while recommendations remain drafts until a planner approves them. The talk acknowledges that scaling quality checks for judgment-heavy work remains unresolved; adoption counts are not proof that every generated plan is correct.

- Choose tasks whose output a domain expert can evaluate.

- Test skills repeatedly on real cases before sharing.

- Assign separate ownership and review, with explicit boundaries on client-facing actions.


## Adjacent · Performance, cost & model selection


### 274. Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean

**Uploaded:** 2026-08-22 · [Watch video](https://www.youtube.com/watch?v=FvxY8oPoI8o) · [Read transcript](transcripts/FvxY8oPoI8o.md)

Archana Kamath and Tyler Gillam present model routing as a request-specific tradeoff among quality, cost, latency, and availability rather than a search for one leaderboard winner. Their router combines task descriptions, model pools, selection policies, and explicit preferences, including manual failover rankings and recent-latency selection. Gillam demonstrates routing within a coding-agent workflow and separates informal visual checks from evaluation evidence. He reports a router correctness score of 90% versus 95% for Opus, while a demonstrated session cost 14 cents through routing versus 44 cents directly. The speakers advocate a route, evaluate, adjust loop using the application's own tests, with caching and personalization as further improvements.

- Evaluate the complete workload with its prompts and tools rather than selecting models solely from public rankings.

- Compare correctness, latency, token usage, and monetary cost together when assessing a routing policy.

- Make per-task model pools, fallback order, and selection rules explicit so routing decisions can be inspected and changed.

- Treat live demonstrations and visual impressions as weaker evidence than repeatable application-specific evaluations.


### 275. From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad

**Uploaded:** 2026-08-29 · [Watch video](https://www.youtube.com/watch?v=dSg0pu8d6qg) · [Read transcript](transcripts/dSg0pu8d6qg.md)

Mingsheng Hong explains how Ironclad evaluates the return on AI coding spend through trusted throughput rather than token usage. His metric evolves from lines of code and open pull requests toward merged changes weighted by an explicitly provisional complexity score. Trust combines objective tests and security checks, human judgments about architecture and maintainability, and production outcomes such as rollbacks and customer complaints. He describes review and CI as downstream bottlenecks, warning that slow pipelines encourage larger, harder-to-review changes. Token dashboards should reveal anomalies and adoption gaps, not reward consumption. The talk links outcome measurement with test reliability, review workflows and limits on unproductive agent retries.

- Measure validated shipped work alongside cost, not token consumption as a goal.

- Combine automated checks, human review and customer outcomes.

- Track review and CI bottlenecks, including flaky-test retries and ready-to-merge time.


### 276. Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google

**Uploaded:** 2026-09-19 · [Watch video](https://www.youtube.com/watch?v=l1-D89bAuOA) · [Read transcript](transcripts/l1-D89bAuOA.md)

Ashok Chandrasekar and Jason Kramberger show how inference benchmarks can mismeasure the client rather than the server. Their examples include requested load not actually delivered, streaming-client overload inflating latency, temperature settings changing throughput, and identical datasets producing different token counts through sampling or truncation. They introduce Inference Perf, a multiprocess load generator with declarative workload configuration and telemetry comparing scheduled with actual request execution. Client metrics are combined with server metrics to distinguish harness saturation from system bottlenecks. A shared workload catalog covers conversation replay and agentic scenarios. The central message is to validate load generation, workload realism and reproducibility before trusting performance comparisons.

- Instrument the benchmark client and compare planned versus delivered load.

- Record sampling, truncation, generation settings and realistic workload distributions.

- Separate harness saturation from server latency before optimizing inference.


### 277. Large clusters for small models — Daniel Svonava, Superlinked

**Uploaded:** 2026-09-19 · [Watch video](https://www.youtube.com/watch?v=g4SsanB0gMc) · [Read transcript](transcripts/g4SsanB0gMc.md)

Daniel Svonava explains serving fleets of small models and includes concrete inference-benchmarking principles. He defines the throughput–latency knee as the saturation point beyond which additional offered load mostly increases latency, then uses it to discuss practical serving capacity. Comparisons against tuned SGLang distinguish runtime performance from improvements introduced by batching and a Rust sidecar. Internal measurement tools feed autoresearch loops that optimize model adapters and ship tuned configurations rather than requiring customers to rediscover settings. Task-specific quality checks remain necessary when replacing general models; a brief retrieval-adaptation example reports an improvement. The talk is chiefly infrastructure engineering, with evaluation relevance strongest in workload-aware performance measurement.

- Benchmark saturation and tail effects rather than quoting an unconstrained throughput number.

- Compare against a tuned runtime baseline to isolate orchestration improvements.

- Feed reproducible measurements into optimization loops and ship the resulting configurations.


### 278. Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer

**Uploaded:** 2026-09-19 · [Watch video](https://www.youtube.com/watch?v=btxG75rNJC4) · [Read transcript](transcripts/btxG75rNJC4.md)

Asaf Gardin and Yuval Belfer investigate silent Jamba inference corruption in vLLM rather than ordinary model-quality deficiencies. They make a rare gibberish failure reproducible through memory pressure and deterministic sampling, then compare token log probabilities against a plain Transformers reference. Propagating request identity into the forward pass reveals decode occurring before prefill, exposing stale Mamba state. A second discrepancy between rollout and training log probabilities, before any weight update, traces to a 32-bit cache index overflow. The practical evaluation lesson is differential correctness checking under realistic stress: changing load and memory can expose or hide infrastructure bugs that confident final text and crash monitoring miss.

- Compare token-level probabilities against an independent reference implementation.

- Stress inference under varied memory and rollout scale to expose silent corruption.

- Carry request identity into low-level execution for actionable diagnostics.


### 279. Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI

**Uploaded:** 2026-10-02 · [Watch video](https://www.youtube.com/watch?v=48YUYDjwfYY) · [Read transcript](transcripts/48YUYDjwfYY.md)

The Kimchi team presents model routing around cost per completed task at comparable quality, rather than advertised token prices. They describe a milestone-based Ferment loop that scores outputs, runs builds, detects breakage, and sends work back for remediation; a higher-order model checks quality, with completion generally requiring at least a B score. The speakers report internal savings against a hypothetical Claude bill, but the transcript does not establish a controlled benchmark or define the grading rubric. Automation currently stops at staging, retaining human involvement before production. Remote sandboxes and team review interfaces support this workflow but do not themselves demonstrate output correctness.

- Compare completed-task costs under a quality constraint rather than token prices alone.

- Use milestone scoring and repeated build/remediation checks to govern routed model output.

- Keep reported internal savings distinct from independently validated benchmark results.

- Preserve the stated staging boundary and human production review.


### 280. Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=XTpyNrEgJQ4) · [Read transcript](transcripts/XTpyNrEgJQ4.md)

The presenter explains speculative decoding as a small draft model proposing tokens that a target model verifies together, accelerating decoding while preserving the target distribution. A vLLM demonstration on one Blackwell GPU compares baseline and speculative servers and reports roughly a 1.6-fold speedup for a structured workload. Acceptance rate and generated tokens per second guide the comparison; a creative, higher-temperature example shows lower acceptance. Benefits depend on draft accuracy, speed, tokenizer compatibility, spare memory, concurrency, and input-to-output proportions. Long-prefill workloads and saturated GPUs may gain little. The talk provides workload-selection guidance rather than a comprehensive benchmark, and the live demonstration initially encounters server problems.

- Benchmark acceptance rate and throughput on your own workloads.

- Account for draft weights and both KV caches.

- Expect weaker gains for prefill-heavy or highly concurrent serving.


### 281. Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=4n08JHb90hI) · [Read transcript](transcripts/4n08JHb90hI.md)

Du’an Lightfoot and Khaja Omer teach workload-specific evaluation of self-hosted inference, combining serving metrics with output-quality checks. The workshop establishes concurrency baselines, compares quantized and full-precision models, and examines throughput, first-token latency, cache pressure, and saturation. Participants are urged to change one serving setting at a time and retest realistic workloads, including JSON and tool-call correctness. A speculative-decoding experiment actually reduces throughput and is rolled back; the presenters attribute this to poor drafter compatibility and acceptance. Later tuning improves selected load-test metrics, but a notebook failure and model reset complicate comparisons. Results are workshop-specific, not universal optimization guarantees.

- Pair load-test improvements with workload-specific quality checks after quantization or configuration changes.

- Locate the throughput/latency knee instead of maximizing concurrency blindly.

- Measure speculative-decoding acceptance and retain rollback when the added model makes performance worse.

- Track model and environment changes to avoid confounded comparisons.


### 282. Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=j4AmIK6OvHc) · [Read transcript](transcripts/j4AmIK6OvHc.md)

Hall argues that voice-agent quality depends on a complete conversational system, not isolated model leaderboards or minimal latency alone. Speech recognition errors cascade downstream, while first-byte and first-token timings can obscure when users actually hear useful speech. He advocates asynchronous tools, audio-based turn detection, and a latency budget that preserves natural interruption and replanning. LiveKit’s proposed benchmark runs simulated callers against a hotel agent, checking database outcomes, accuracy, interruptions, privacy, and unnecessary steps while swapping model stacks. Hall reports favorable turn-detection and tuned-model results, but stresses running the open harness on each application. The demonstrated conversation is partly sped up, not an unedited timing test.

- Measure first audible response and complete conversational outcomes.

- Keep slow tools asynchronous so conversation remains responsive.

- Benchmark realistic interruptions and backend state, not components alone.


### 283. Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=_naLJOqVOEI) · [Read transcript](transcripts/_naLJOqVOEI.md)

Yunmo Koo demonstrates why the same open-weight model and coding workflow can behave differently across inference providers. A game-generation comparison illustrates task cost, while a same-model provider comparison examines end-to-end completion speed. He explains prefix caching, cache-aware routing, hierarchical KV storage, and adaptive speculative decoding as possible sources of performance differences. Reliability belongs in the benchmark because timeouts, rate limits, and server errors can derail a long agent run even when average generation speed looks good. Customer and demonstration figures are contextual claims, not controlled universal rankings. The recommended evaluation is the application’s own prompts, lengths, traffic patterns, quality requirements, costs, and failure rates.

- Hold model and agent workflow constant when comparing providers.

- Measure end-to-end time and failure rates alongside token throughput.

- Use real prompt lengths, repeated prefixes, and traffic patterns.


### 284. Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=7BcQdtRA3Tc) · [Read transcript](transcripts/7BcQdtRA3Tc.md)

Abdul Dakkak presents Modular’s Mojo, MAX, and cloud stack as an alternative to separately optimized hardware-specific serving systems. A substantial benchmark section compares kernels and inference across language and image models, GPUs, and serving frameworks, using measures such as time to first token, tokens per GPU, throughput, and image-generation latency. He discusses tuning a workload’s performance-cost frontier and accounting for hardware prices rather than comparing speed alone. The talk reports vendor results and references external verification, but does not establish universal superiority across every workload. Its evaluation relevance is infrastructure performance comparison, not assessment of model answer correctness or agent task success.

- Compare serving metrics on specified models and hardware.

- Include hardware price and workload-specific performance tradeoffs.

- Separate vendor benchmark claims from general application-quality evidence.


### 285. The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI

**Uploaded:** 2026-10-17 · [Watch video](https://www.youtube.com/watch?v=Ti-BmGU1_mQ) · [Read transcript](transcripts/Ti-BmGU1_mQ.md)

Eugene Cheah presents an inference-cost workflow built around measurement, model right-sizing, capacity purchasing, and process review. He distinguishes exploratory agentic workloads from repeated processes and recommends separate telemetry so their costs can be understood. For stable tasks, frontier outputs, test cases, golden traces, fine-tuning, and shadow traffic can support cheaper specialized models without assuming equivalent quality. Examples and Q&A discuss task-specific benchmarks, acceptable evaluation changes, caching, and harness flexibility. He also warns that more token consumption can create review burdens rather than useful work. The talk’s optimization claims are contextual customer examples; the practical method is to test quality and total operational outcomes before changing models or serving arrangements.

- Separate workload classes and measure their costs independently.

- Use golden cases and shadow evaluation to validate smaller models.

- Check downstream review burden instead of treating tokens as productivity.


### 286. Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management

**Uploaded:** 2026-10-24 · [Watch video](https://www.youtube.com/watch?v=ZMZlAn6Pyfg) · [Read transcript](transcripts/ZMZlAn6Pyfg.md)

Hari Kumar explains how Contour Asset Management evaluates AI tools against analysts’ existing research processes rather than rely on adoption statistics. Live A/B comparisons examine research with and without AI, while tracking time, useful insights, and whether ideas become actionable over investment-relevant horizons. He proposes cost per useful insight as a practical bridge between operational improvements and eventual portfolio results. Examples include resurfacing older investment ideas, combining alternative data, trading workflows, operations, and compliance. The analysis also counts time spent fixing and maintaining AI tools. The point is to measure the full process and opportunity cost; eventual P&L alone arrives too late and is affected by many other factors.

- Benchmark AI-assisted work against the existing human workflow.

- Track cost and time per useful insight, including maintenance.

- Separate near-term process evidence from delayed investment outcomes.


### 287. Stop Guessing Your vLLM Config: Benchmarking LLMs on Runpod - Chris Vela, Runpod

**Uploaded:** 2026-10-28 · [Watch video](https://www.youtube.com/watch?v=P_0_Th_ZzIg) · [Read transcript](transcripts/P_0_Th_ZzIg.md)

Chris Vela demonstrates workload-specific benchmarking for vLLM deployments rather than selecting a default recipe and assuming it will scale. He starts with task requirements, concurrency, context length, memory, and software compatibility, then uses BenchPod to inspect serving metrics and compare configurations. A Kimi K3 deployment on B300 hardware illustrates maximum-batch-token experiments: in the shown comparison, inter-token latency improves while time to first token changes less. Configuration changes still involve service restart in the demonstration. He recommends measuring relevant latency, throughput, errors, and cold starts before production deployment, and considering whether a smaller model could satisfy the application at lower infrastructure cost.

- Benchmark expected concurrency and context length, not one successful request.

- Choose latency and throughput metrics that match the workload.

- Treat demonstrated tuning results as configuration-specific rather than universal.


## Adjacent · Production monitoring & feedback loops


### 288. How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

**Uploaded:** 2026-05-30 · [Watch video](https://www.youtube.com/watch?v=phchDt63qAA) · [Read transcript](transcripts/phchDt63qAA.md)

Ben Kunkle explains Zeta2’s edit-prediction training pipeline and the measurements needed to judge it. Opt-in production snapshots are distilled through a teacher, checked for behavior such as reversing recent edits or crossing editable boundaries, and repaired before training. A settled user edit is useful but noisy ground truth, so repeated predictions and edit-distance comparisons filter predictable examples. Held-out evaluations use multiple acceptable teacher outputs and track reversal ratio and diagnostic changes. Because offline similarity does not necessarily reflect editor usefulness, production traffic experiments also monitor acceptance, retention and latency before promoting a model.

- Keep held-out evaluation separate from training examples.

- Use multiple valid predictions when there is no single correct edit.

- Validate offline diagnostics against production acceptance and latency.


### 289. Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind

**Uploaded:** 2026-05-30 · [Watch video](https://www.youtube.com/watch?v=3_gYbhABcAE) · [Read transcript](transcripts/3_gYbhABcAE.md)

Philipp Schmid contrasts deterministic software control with goal-directed agents whose state includes natural-language context. He argues for treating errors as recoverable inputs and designing self-documenting tool interfaces rather than assuming implicit developer knowledge. A substantial reliability section distinguishes asserting one expected result from measuring how often an agent succeeds. Subjective outputs need expert or LLM-judge feedback, while traces explain the path without requiring every run to take identical steps. The overall recommendation is to preserve semantic meaning and recovery capability while evaluating outcome reliability, rather than forcing a model into a brittle predetermined workflow.

- Measure success frequency across repeated runs, not one successful demonstration.

- Use expert or judge feedback for subjective outputs and traces for diagnosis.

- Keep recovery in the workflow instead of restarting all work after a tool error.


### 290. AI System Design: From Idea to Production - Apoorva Joshi, MongoDB

**Uploaded:** 2026-06-28 · [Watch video](https://www.youtube.com/watch?v=T0HhO4YtTfE) · [Read transcript](transcripts/T0HhO4YtTfE.md)

Apoorva Joshi applies an end-to-end design framework to a hypothetical insurance-claims review system. Business constraints and measurable success criteria determine data, architecture and human-review boundaries before tools are selected. Evaluation distinguishes invalid inputs, missing citations, faithfulness to retrieved evidence, application-specific processing time and system cost. Production adds human override rates and review duration as signals of usefulness or confusion. The talk recommends starting with the simplest architecture, locating failures through measurement and iterating on retrieval or prompts before overengineering. Evaluation and monitoring remain linked but serve pre-release confidence and post-release regression detection respectively.

- Define domain-specific success alongside generic quality and cost metrics.

- Monitor human overrides and review time after launch.

- Evaluate the simplest design before adding autonomous complexity.


### 291. Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra

**Uploaded:** 2026-07-12 · [Watch video](https://www.youtube.com/watch?v=EUsPvBeIx70) · [Read transcript](transcripts/EUsPvBeIx70.md)

Raahul Singh and Vanč Levstik describe an industrial agent that failed when asked to resolve equipment names at massive sensor scale. Vector search and sharded LLM scanning lost recall, invented equipment, and struggled with nearly identical names. Their redesign separates intent planning from deterministic hierarchical resolution and set operations. They evaluate old and new systems head-to-head with the same model and data, repeat each case, include real production systems, and measure correctness and token cost across scales. The reported results belong to this case study, not a universal guarantee. Its adjacent evaluation lesson is that demo-scale success must be challenged with realistic scale, exactness requirements, and controlled architectural comparisons.

- Benchmark correctness and cost across realistic scale, not only small demos.

- Hold model and data constant when comparing architectural changes.

- Use deterministic resolution for exact structured operations instead of asking LLMs to enumerate them.


### 292. Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake

**Uploaded:** 2026-08-26 · [Watch video](https://www.youtube.com/watch?v=DrTdD-ttjCY) · [Read transcript](transcripts/DrTdD-ttjCY.md)

Sait Izmit describes Snowflake’s internal go-to-market assistant, emphasizing quality before breadth. Before testing the system, he wrote 150 questions from actual sales workflows, exposing missing data and an initial reported 50% accuracy. The team narrowed scope to earn trust, then used pilot feedback, a limited beta and retention criteria before broad rollout. Logs become a continuing evaluation resource: LLM classification reveals repeated questions, feature gaps and signs of frustration, informing content and product changes. He distinguishes poor activation from users trying and rejecting the product. The broader deployment story includes changing architecture and workflow automation, but realistic question sets and production feedback are central lessons.

- Build evaluation questions from user workflows, including unmet needs.

- Prefer reliable narrow coverage over unreliable breadth during launch.

- Mine production logs for failure patterns and separate activation from retention problems.


### 293. Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous

**Uploaded:** 2026-10-02 · [Watch video](https://www.youtube.com/watch?v=HLTa7Vcs4X0) · [Read transcript](transcripts/HLTa7Vcs4X0.md)

Spencer-Harper argues that verification, rather than code generation, becomes the delivery bottleneck when agents produce changes faster than humans can inspect them. Meticulous records browser workflows in nonproduction environments, replays selected flows against pre-change and post-change code, and exposes screenshot differences for reviewers to judge. Network mocking isolates runs, browser scheduling controls reduce nondeterminism, and coverage-guided selection chooses workflows spanning more executed code. He claims near-exhaustive frontend verification and substantially fewer flakes, but the mechanism detects differences rather than independently deciding correctness. Its reach depends on recorded behavior and visible effects; humans or reviewing agents still distinguish intended changes from regressions.

- Review behavioral differences instead of relying only on upfront assertions.

- Control network and scheduling nondeterminism for reproducible replay.

- Treat coverage and visual diffs as evidence, not universal correctness proofs.


### 294. The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI

**Uploaded:** 2026-10-06 · [Watch video](https://www.youtube.com/watch?v=eXA2tjRZIbY) · [Read transcript](transcripts/eXA2tjRZIbY.md)

Varun Krovvidi presents Resolve AI’s production-agent harness, connecting model orchestration, context selection, causal reasoning, governed actions, learning, and evaluation. The evaluation discussion goes beyond answer correctness: user reinforcement, investigation-path tracing, comparisons with strong engineers, and confidence calibration feed recurring checks after model, use-case, or architecture changes. He argues that incident investigations need causal evidence rather than plausible correlations, with low confidence when evidence runs out. A product demonstration illustrates rejected outage hypotheses and collaborative investigation. These are architectural prescriptions and a vendor demonstration, not a quantified benchmark establishing production reliability or comparative superiority.

- Evaluate investigation paths and confidence calibration, not only final root-cause answers.

- Re-run evaluations when models, use cases, or architecture change.

- Distinguish causal evidence from coincident outages and communicate evidence gaps.


### 295. Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto

**Uploaded:** 2026-10-08 · [Watch video](https://www.youtube.com/watch?v=jJQoVkd5yLg) · [Read transcript](transcripts/jJQoVkd5yLg.md)

Abhi Arya recounts rebuilding Reducto’s MCP interface after a curated demo failed under colleagues’ ambiguous requests. Instead of exposing raw endpoints, the redesign supplies workflow-aware tools, live pipeline snapshots, specific errors, and validators that make agent actions inspectable. Runtime extraction confidence and bounding boxes feed schema improvement, while evaluations penalize unsupported assumptions and reward clarification. Instrumentation tracks human overrides, low confidence, and questions to improve later guidance. Human review remains central because executable pipelines can silently produce incorrect document results. The speaker reports improved accuracy, satisfaction, and adoption, but provides no quantified evaluation dataset or independent verification of those gains.

- Evaluate ambiguous real-user requests rather than relying on a curated demonstration.

- Penalize unsupported assumptions and encourage explicit clarification in evaluations.

- Expose state, confidence, evidence, and human override signals for inspectable quality feedback.


### 296. Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked

**Uploaded:** 2026-10-10 · [Watch video](https://www.youtube.com/watch?v=ORVh4GivEU0) · [Read transcript](transcripts/ORVh4GivEU0.md)

Unblocked’s presenter combines context-engine comparisons with a practical walkthrough of safe structured-query generation. A displayed planning example reportedly halves cost and elapsed time with task-specific context, while a code-review regression example links changing model behavior to reduced issue detection. An open-source simulator is proposed for same-task A/B tests with and without context bundles. The implementation section treats generated queries as untrusted: validate operators, hide sensitive fields, inject tenant constraints outside the model, and bound repair retries. The examples demonstrate mechanisms and selected outcomes, not a broad benchmark proving general savings or complete safety; one retry initially produces an overly narrow match.

- Use same-task A/B comparisons to assess context benefits instead of assuming retrieval helps.

- Validate generated queries independently and enforce tenant constraints outside model control.

- Inspect repair outcomes for semantic correctness, not merely successful execution.


### 297. The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=tyFPqtyOK5w) · [Read transcript](transcripts/tyFPqtyOK5w.md)

Ang Li discusses computer-use agents through Agent S and Simular’s combination of visual exploration, reusable code, and cloud desktops. The evaluation distinction is between succeeding at least once across attempts and completing the same task reliably across repeated runs and environmental variation. A conference-site demonstration saves a successful workflow as a skill, then encounters a replay problem on a different day and returns to model-driven exploration. The session explores visual grounding, accessibility information, verification loops, irreversible actions, and the limits of fixed scripts. Benchmark improvements and successful demos remain incomplete evidence for everyday reliability; stable automation and adaptive recovery need to be tested together.

- Distinguish best-of-many success from repeated-run reliability.

- Evaluate replay behavior when prompts and environments change.

- Check state and action outcomes instead of trusting a successful demonstration.


### 298. We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI

**Uploaded:** 2026-10-27 · [Watch video](https://www.youtube.com/watch?v=YIhvrvHtonk) · [Read transcript](transcripts/YIhvrvHtonk.md)

Fuad Ali traces Arize’s Alex agent through successive architectural changes, from an unreliable prototype to a single agent with planning, explicit stopping rules, memory, and on-demand skills. Evaluation appears as a practical decision mechanism: real production sessions become regression datasets, harness changes are compared experimentally, and model upgrades are weighed against latency and quality rather than assumed beneficial. He explains moving planning into the harness, offloading large tool outputs into files, and preferring a small auditable per-user memory file over more complex retrieval structures. Human-written labels and judge alignment remain necessary. The design lesson is to retain testable evidence while simplifying the architecture as capabilities improve.

- Convert representative production sessions into regression tests.

- Compare harness and model changes on both latency and quality.

- Keep memory inspectable and calibrate judges against human labels.


## Adjacent · Safety, security & adversarial evaluation


### 299. Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis

**Uploaded:** 2026-07-08 · [Watch video](https://www.youtube.com/watch?v=IQkVMvXQKLY) · [Read transcript](transcripts/IQkVMvXQKLY.md)

Sachin Kumar examines sleeper-agent backdoors that pass ordinary behavioral evaluations until an untested trigger appears. He compares cross-model features with sparse autoencoders trained on activation differences between a base and fine-tuned model. In a controlled year-triggered SQL-injection experiment on a 360-million-parameter model, the difference-based method produces a much stronger isolation signal and perfect precision, but one feature detects only about a quarter of triggers. The proposed deployment is a cheap checkpoint-comparison gate followed by feature inspection. The talk explicitly limits its evidence to one backdoor family and notes untested adaptive attackers and scaling.

- Passing behavioral tests does not establish absence of a conditional backdoor.

- Activation-difference features isolate fine-tuning changes better than joint features in this experiment.

- High precision is not high coverage; validate thresholds and consider ensembles.


### 300. Using LLMs to Secure Source Code — Eugene Yan, Anthropic

**Uploaded:** 2026-07-17 · [Watch video](https://www.youtube.com/watch?v=imFedndyXYQ) · [Read transcript](transcripts/imFedndyXYQ.md)

Eugene Yan describes an LLM-assisted security workflow with six stages: threat modeling, sandbox setup, discovery, verification, triage, and patching. Discovery should maximize recall, while an independent adversarial verifier receives a suspected vulnerability without the discoverer’s reasoning and attempts to reproduce or disprove it. Representative isolated environments make proof-of-concept execution meaningful and repeatable. Triage then incorporates business context and compensating controls so scarce engineering attention reaches the most consequential findings. Patch validation requires the original exploit to fail, existing tests to remain green, and potentially a fresh attack against the patched system. Yan emphasizes that verification and organizational calibration, not merely finding candidates, are the scaling bottlenecks.

- Separate recall-oriented discovery from precision-oriented independent verification.

- Reproduce findings in realistic isolated test beds.

- Validate patches through exploit failure, regression tests, and renewed adversarial testing.


### 301. Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk

**Uploaded:** 2026-07-20 · [Watch video](https://www.youtube.com/watch?v=1EZdpEhwmNc) · [Read transcript](transcripts/1EZdpEhwmNc.md)

Manoj Nair argues that agentic security requires separating generation from validation. He presents Snyk customer observations and red-team comparisons showing that model behavior varies across attacks and that stronger general capabilities do not guarantee reliable vulnerability detection. Repeated-run consistency and comparison against deterministic checks expose omissions hidden by a single successful example. The talk broadens the security surface from generated code to packages, skills, MCP components, and agent actions, then demonstrates package-health and skill-risk checks inside coding workflows. These are vendor-presented findings, not independently reproduced measurements. The adjacent evaluation message is to combine probabilistic investigation with explicit, continuously updated verification rather than let one model certify itself.

- Evaluate repeated-run consistency and distinct attack types separately.

- Use deterministic security checks alongside model-based analysis.

- Assess tools, skills, and dependencies as well as generated code.


### 302. 200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI

**Uploaded:** 2026-08-19 · [Watch video](https://www.youtube.com/watch?v=AN65uc645mE) · [Read transcript](transcripts/AN65uc645mE.md)

Vivek Muppalla describes Hippocratic AI's vertically integrated voice-agent stack, balancing clinical accuracy, conversational latency, and patient empathy. Context-aware speech recognition addresses medication names, noisy audio, and ambiguous short replies; parallel specialist models assist a central conversational model while background verifiers check tool arguments and results. Inference optimizations create latency headroom for additional intelligence rather than relaxing quality requirements. He explains why rare failures demand extensive testing, combining synthetic scenarios with clinician-led conversations. Safety is assessed on harm-severity categories rather than correctness alone, alongside a dedicated empathy benchmark, HEART. Muppalla reports 99.89% no-harm performance under their rubric and describes ongoing clinical evaluation, escalation, and offline verification as parts of the safety system.

- Investigate speech-recognition errors before attributing clinical failures to reasoning, especially for medication names and short answers.

- Verify tool-call parameters and results during operation, using offline checks and correction when the workflow permits.

- Combine synthetic cases with clinician evaluation to investigate rare failures at deployment-relevant scale.

- Assess harm severity and empathy explicitly instead of treating aggregate correctness as a sufficient clinical-quality metric.


### 303. We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog

**Uploaded:** 2026-09-14 · [Watch video](https://www.youtube.com/watch?v=4lXks428C9o) · [Read transcript](transcripts/4lXks428C9o.md)

Sarah Sanders describes auditing PostHog’s command-running onboarding agent and discovering that individually benign components can compose into security gaps. The context supply chain becomes an important threat surface, so her team scans both published skill bundles and runtime inputs. The Warlock detector uses deterministic YARA rules, while an LLM advises on noise rather than controlling enforcement. Observed subagent attempts to find secrets and unintended PII capture inform changes to the system. She stresses positive and negative tests for detection rules, impact-based severity and false-positive control. This is a security-evaluation case study, not a claim that prompt scanning alone prevents injection; layered controls remain essential.

- Audit component interactions and the context supply chain, not just isolated diffs.

- Ship negative tests to prevent security rules from becoming unusably noisy.

- Separate probabilistic triage from deterministic enforcement and retain telemetry.


### 304. AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk

**Uploaded:** 2026-10-07 · [Watch video](https://www.youtube.com/watch?v=f3o0-9Dlw3E) · [Read transcript](transcripts/f3o0-9Dlw3E.md)

Cohen argues that faster AI-generated changes and AI-assisted attacks make occasional penetration tests insufficient. He contrasts static scanning, dynamic testing, and human pentesting, emphasizing their different coverage of business logic, authorization, and configuration. Snyk’s EVO proposal combines continuous AI pentesting, agent red teaming, and existing scanner context. Its multi-agent sequence performs reconnaissance, vulnerability testing, exploit validation, remediation, and reporting. The verification priority is proving exploitability rather than adding speculative findings to an overloaded backlog. Cohen advocates evaluating vendors on continuous operation, contextual reasoning, data enrichment, and actionable evidence. His attack-speed and insecurity statistics are presenter claims, with some visibly unreliable caption wording, not independently established benchmarks.

- Combine complementary security methods rather than replacing them wholesale.

- Require exploit validation to reduce false positives.

- Assess continuous testing and contextual evidence, not just finding counts.


### 305. AI Security Engineer Foundations + Certificate — Javier Garza, Snyk

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=ZyC56eV8sVw) · [Read transcript](transcripts/ZyC56eV8sVw.md)

Javier Garza’s workshop combines AI application security concepts with exercises and concrete assessment workflows. Prompt-injection challenges and a deliberately vulnerable assistant expose trust-boundary failures; an AI bill of materials inventories models, datasets, and agents before risks can be prioritized. Threat modeling maps assets, attacks, mitigations, and validation. For MCP servers and skills, he distinguishes inspecting tool definitions for poisoning from scanning implementation code for vulnerabilities, then advocates scan-fix-rescan loops integrated with agent rules and hooks. The session also covers output validation, least privilege, dependency verification, environment separation, and human review. It is broad security training rather than a model-quality leaderboard, but provides substantial adversarial testing material.

- Inventory AI components before prioritizing security tests.

- Inspect tool descriptions and implementation code as separate attack surfaces.

- Validate mitigations through repeated exercises and scan-fix-rescan workflows.


### 306. AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=p-2MT8KYZqU) · [Read transcript](transcripts/p-2MT8KYZqU.md)

Silverman's accelerated security foundations workshop covers LLM vulnerabilities, shadow AI inventories, threat modeling, MCP security, secure agentic development, and red teaming. He connects AI-specific risks such as prompt injection, tool poisoning, and excessive agency to established application-security practices. Proposed verification mechanisms include AI bills of materials checked against approved baselines in CI, dependency and code scanning, architectural threat reviews, and repeated adversarial testing. His strongest recurring prescription is external enforcement: restrict data access, isolate environments, require approvals, and never treat prompts as authorization. Product demonstrations illustrate inventory policies, while a deliberately vulnerable student chatbot resists attempts to extract grades, underscoring nondeterministic testing and the workshop's incomplete exploitation outcome.

- Enforce least privilege outside the model; prompts alone are not access controls.

- Continuously inventory AI components and gate unapproved changes.

- Test tool descriptions and underlying code, then repeat adversarial checks.


### 307. Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=1tpqdglI3T0) · [Read transcript](transcripts/1tpqdglI3T0.md)

Michael Forrester and Whitney Lee use a deliberately overprivileged burrito assistant to test agent security across three configurations. Audience attacks deploy external images and expose a secret recipe; replaying them demonstrates Kubernetes admission policies, attempted runtime restrictions, and input/output guardrails. OpenTelemetry traces reveal prompts, tool calls, and a poisoned weather tool that requests internal configuration. The presenters distinguish reliable infrastructure enforcement from inconsistent model refusals, acknowledge runtime protections and provisioning failures, and compare redaction after generation with filtering before it. They also warn that traces can retain sensitive user data and recommend bounded, economically worthwhile workflows with verifiable outputs.

- Replay the same attacks before and after controls; model refusals are not dependable enforcement.

- Check actual tool behavior and side effects in traces, not only chat responses.

- Scrub sensitive input before it becomes model context or retained telemetry.


### 308. SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar

**Uploaded:** 2026-10-11 · [Watch video](https://www.youtube.com/watch?v=bI8WyG9YB0I) · [Read transcript](transcripts/bI8WyG9YB0I.md)

Killian Carlsen-Phelan demonstrates SonarQube integrated into Codex’s guide-verify-solve loop. A deliberately vulnerable Python project contains a hardcoded credential and SQL injection; static dataflow findings become context for an agent-generated parameterized-query repair, which is checked again after editing. A prompt hook blocks a fake secret, while CLI skills and an MCP server expose project issues and guidance. The opening discussion distinguishes sandbox containment from artifact correctness and warns about correlated author-and-reviewer failures. Q&A covers hook bypasses, local execution, containers, and feature access. The practical emphasis is independent evidence and repeated verification inside the editing loop, not an assumption that safe execution implies correct output.

- Separate execution containment from correctness of generated artifacts.

- Provide agents independent static-analysis findings and recheck repairs.

- Understand hook bypasses and the exact scope of enforcement.


### 309. Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco

**Uploaded:** 2026-10-20 · [Watch video](https://www.youtube.com/watch?v=Bz1HFxQA1o8) · [Read transcript](transcripts/Bz1HFxQA1o8.md)

Al Chen explains how engineering evidence supports AI deployments inside banks. For dependency vulnerabilities, agents reproduce exploits and run tests against proposed patched versions rather than assume an upgrade fixes the issue. Harbor tasks provide controlled application environments and verifiable outcomes. Backup success also needs restoration and data checks, not a green status alone. A separate example shows LLM-judge explanations leaking sensitive information even when numerical scores are safe to expose; redaction and an additional judgment path introduce their own costs. The talk connects compliance requirements to concrete testing workflows while emphasizing that data residency, privacy, and reliable recovery cannot be guaranteed for free.

- Test exploit behavior after dependency changes.

- Verify restored data rather than only backup job status.

- Evaluate judge explanations and data paths for sensitive-information leakage.


### 310. Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg

**Uploaded:** 2026-10-23 · [Watch video](https://www.youtube.com/watch?v=5O6jLtoeKrg) · [Read transcript](transcripts/5O6jLtoeKrg.md)

Andrey Rybka reviews reported agent-security incidents and maps each failure path to concrete controls. Examples include sandbox escape, email prompt injection, malicious marketplace content, DNS exfiltration, poisoned MCP packages, and production database deletion. The proposed defenses combine per-agent identities, short-lived scoped credentials, hostile-input handling, deterministic tool-call brokerage, restrictive outbound networking, human approval for valuable actions, and audit trails. He emphasizes that static rules and broad permissions cannot establish whether an agent’s goal has been redirected. The incidents are presented as lessons for layered risk assessment rather than an independently verified attack benchmark. Developers should test containment, memory, identity, and action authorization together instead of assuming a single guardrail is sufficient.

- Analyze incidents as complete attack paths across multiple layers.

- Put deterministic controls around consequential tool actions.

- Verify isolation, outbound traffic policy, and auditable agent identities.


### 311. 300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer

**Uploaded:** 2026-10-27 · [Watch video](https://www.youtube.com/watch?v=BgLdvF7Qkh8) · [Read transcript](transcripts/BgLdvF7Qkh8.md)

Aiden Sochowski describes instrumenting Runlayer’s internal agents through a common gateway to expose sessions, tool calls, permissions, and costs. Examples include email-based exfiltration, reviewers persuaded into approving code, over-permissioned bots, and compromised agents contaminating other agents through shared systems. He stresses that some attacks unfold over a whole conversation, so inspecting individual calls cannot reveal the complete failure. The same telemetry reveals broken MCP tools, repeated workarounds, and dramatic cost increases after model changes. His recommended response is to map actual behavior and data movement before narrowing permissions and applying contextual policies. Monitoring provides evidence for controls; it does not make probabilistic detection perfect.

- Inspect complete sessions and cross-agent data flows.

- Use observed tool usage to reduce excessive permissions.

- Treat retries, broken integrations, and model-change costs as observable failure modes.


### 312. AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar

**Uploaded:** 2026-10-28 · [Watch video](https://www.youtube.com/watch?v=UW8Qkk7MG8A) · [Read transcript](transcripts/UW8Qkk7MG8A.md)

Taylor Luttrell-Williams introduces SonarQube Hunter Agent for vulnerabilities that pattern-based static analysis can miss, including broken authorization and valid code implementing flawed business logic. The proposed pipeline maps a repository, runs specialist agents, consolidates findings, and performs adversarial validation and noise filtering before presenting issues. A sample Python project produces 46 findings, including privilege escalation and an MFA bypass. The walkthrough covers issue states, quality-gate consequences, scheduled scans, and remediation. It recommends combining conventional static and dependency analysis with contextual investigation. The example demonstrates the workflow and reported findings; it does not establish independent precision, recall, or complete vulnerability coverage.

- Validate suspected findings adversarially before surfacing them.

- Combine deterministic analysis with contextual logic checks.

- Distinguish accepted findings from issues that actually block a quality gate.


### 313. Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi

**Uploaded:** 2026-10-30 · [Watch video](https://www.youtube.com/watch?v=YU1uD_YkpjU) · [Read transcript](transcripts/YU1uD_YkpjU.md)

Ishween Kaur tests x402 agent payments in a safe environment, using end-to-end traces to expose failures that a valid payment signature alone cannot prevent. Six examples cover price manipulation, duplicate charges, unpaid delivery, payment reuse across pages, lookalike sellers, and prompt injection that persuades an agent to pay again. She distinguishes verification from settlement and shows why retries, caches, endpoint coverage, seller identity, and payment-to-resource binding all need explicit checks. Her rollout approach progresses from instrumented tests to shadow runs and error analysis on successful and failing cases. The practical lesson is to evaluate the complete payment workflow, not just whether its cryptography accepts a request.

- Trace one payment identifier across every component.

- Test retries, settlement, caching, and resource binding separately.

- Use shadow cases and error analysis before granting payment autonomy.
