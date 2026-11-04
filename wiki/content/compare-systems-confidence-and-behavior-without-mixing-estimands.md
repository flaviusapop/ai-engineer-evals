A system can agree with itself, disagree with an incumbent, be preferred in a pair, and be wrong—all at once. Before choosing a metric, name the estimand: the particular population-level quantity the comparison is intended to estimate. A reliability measure, a calibrated probability and a signed quality difference answer different questions.

## Use confidence only for the decision it supports

An agent's self-reported confidence or an “inferred answer” flag can help prioritize human review; neither proves the answer correct. A narrated incident demo reported increasing confidence after experts supplied context, but did not independently validate incident resolution or calibrate those scores. [cite:32nrHU6zHU8:c06] [cite:_QAVExf_1uw:c05]

For action gating, define the outcome and obtain representative labeled examples. If a score means probability of a correct action, compare predicted probabilities with observed correctness in score bands, including important subgroups and the proposed action region. Assess uncertainty and monitor shifts; good aggregate calibration need not guarantee every subgroup is calibrated. A voice-system example assumes a reasonably calibrated single score, even though a real cascade may have several signals. That assumption must be tested, not inferred from the model's confidence wording. [cite:Zd5b40Jbp_k:c02]

Choose between acting, asking for confirmation and human review using the costs of mistakes, delay, review capacity and the observed performance of each option. A low-score queue can help allocate review, but inspect high-confidence errors too, and measure both coverage and error among automatically handled cases. There is no universal threshold. Probability calibration is not the same as [[validate-judges-against-human-labels|agreement with human labels]] or precision and recall. [cite:UGuNt2_Oz8s:c09]

## Absolute acceptance and relative preference

Pointwise evaluation asks whether one response satisfies a criterion; pairwise evaluation asks which of two responses is better on a defined axis. Use the first for an absolute policy gate and the second, for example, to compare storytelling quality. The preferred answer can still fail policy, and a tie or an unsure judgment can be meaningful. Reverse or randomize presentation order to check position sensitivity rather than assuming the comparison is neutral. [cite:NdrSPm6NCdk:c05] [cite:b_PmGocP4rc:c05]

For image edits, a comparison can assess faithfulness, completeness and realism as well as visual appeal; stakeholders must define what improvement means. The proposed pairwise advantage in storytelling agreement was not measured in the cited account, and the image criteria are not fully disclosed. Relative preference does not automatically establish absolute validity. [cite:31GUkCBD-Uc:c10]

## Repeatability is not truth

Run the same version repeatedly on identical inputs, holding and recording the judge model, prompt, inference engine and settings fixed. Also test sensitivity to a mild challenge separately: a verdict changing under pressure is a different observation from changing on an exact rerun. Consistency does not establish correctness; inspecting the source and rubric matters too. In one project five of twelve apparent evaluation flips failed to reproduce, and a supposedly hallucinated date was present in the source. The project did not report a formal variance estimate. [cite:uIiA6DquRiE:c07] [cite:LQW_Wvqhp04:c06] [cite:gonAewBZxfU:c13]

In a separate speaker-reported case, an incumbent disagreed with itself about 7% of the time across repeated runs, while a candidate differed from historical production answers about 18% of the time. The former is a repeatability baseline, not a mathematical ceiling on candidate accuracy; neither number alone says how often the candidate is worse. Sampling, configuration and uncertainty were not supplied. [cite:8g1N_a3h9H0:c03]

## Behavioral drift versus paired quality gain

Measure cross-version disagreement on the same inputs alongside within-version disagreement. One proposed diagnostic subtracts the average within-version disagreement from cross-version disagreement to highlight changes beyond baseline variability. Its statistical assumptions and derivation were not supplied: do not treat it as a universal correction, an accuracy estimate, or a signed gain. Behavior can change for better, worse, or into another acceptable response. [cite:8g1N_a3h9H0:c09] [cite:8g1N_a3h9H0:c10]

To estimate *quality gain*, review paired incumbent and candidate outputs for each request against the relevant outcome criteria, classifying improvements, regressions and acceptable alternatives. Define the target population and sampling procedure. A signed net gain can be the population share of improvements minus the share of regressions, with acceptable alternatives contributing zero under that definition. If only disagreements are reviewed, their sampling probabilities and the unreviewed population must be accounted for before making a population-wide claim. Pair each comparison by request and keep repeated runs from one conversation grouped when estimating uncertainty; correlated repeats are not independent conversations. The source recommends this design but does not specify a confidence-interval estimator or reviewer sampling protocol. Inspect high-risk slices as well as the overall difference, and make a release decision against a prespecified tolerance rather than a positive point estimate alone. [cite:8g1N_a3h9H0:c10] [cite:8g1N_a3h9H0:c11]

These comparisons are not automatically causal evidence about a single change: if models, prompts, tools or traffic differ together, the observed difference is a system-level comparison under that protocol. See [[comparing-agents-without-confounding-the-result]] for controlled comparisons, and [[agreement-truth-and-the-limits-of-evaluator-proxies]] for why agreement alone is not truth.

## Fidelity to a reference distribution

For quantization, compare output distributions of the compressed model and its original reference on specified calibration inputs; KL divergence is one proposed measure. This asks how closely one model follows a particular reference, not whether either is correct on the application. Report the input distribution, divergence direction and aggregation, and choose an acceptance threshold for the purpose. The source does not specify those choices, so no universal cutoff follows. Pair fidelity checks with independent task evaluation rather than substituting them for it. [cite:J4_jCrTxMkk:c11]
