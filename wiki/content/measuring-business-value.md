A useful agent changes an outcome someone cares about, within an acceptable operating boundary. Calls made, drafts generated and users activated are evidence of activity, not the outcome itself. Measure the work before and after the intervention, including what happens to people and tasks downstream.

## Baseline the whole workflow

Before deployment, document the unaided process: its inputs, workload, handoffs, cycle time, quality, costs and final outcomes. Then specify exactly what changes. In an investment-research comparison, the analyst documents sources and conclusions for one investment name across an unaided earnings cycle, then repeats the research with AI tools and portfolio-manager participation. The speaker calls this a live A/B test, but does not describe random assignment, concurrent controls or protection against order and market effects. A baseline is essential context, not by itself causal proof. [cite:ZMZlAn6Pyfg:c01]

Separately, the speaker illustrates how to distinguish an agent conducting expert calls while a person synthesizes notes from an arrangement in which the agent also synthesizes them. These are different interventions; a combined before-and-after change cannot identify which part produced an effect. No numerical comparison or isolated causal effect is reported for the arrangements. [cite:ZMZlAn6Pyfg:c02]

Count workload alongside all induced human work: operating, reviewing, escalating and repairing, as well as licensing and compute. Time apparently freed is not yet realized value: establish whether it was actually redeployed and what that work accomplished. An acquisition-reporting scenario uses analyst time and reassignment to illustrate the distinction; its hours and savings are assumptions, not an observed return. [cite:gDRCpTMCqEU:c02] [cite:-a2oTS9J67U:c03]

Follow the entire pipeline. Faster early research need not accelerate a later clinical stage, and an investment thesis can take months to affect returns. While waiting, track whether information sourcing, model updates or other intermediate work improved, but label those as process measures rather than realized ROI. For cost per accepted task and cost-linked proxies, see [[decision-economics]]. [cite:-561cZmir5Q:c01] [cite:ZMZlAn6Pyfg:c03]

## Define the mandate and keep dimensions visible

Start with customer and stakeholder outcomes: product, operations, domain, engineering and security may care about different failures. For each task record the required context, desired result, permitted evidence and systems, budget and task-specific success criteria. A renewal event alone, for example, does not show that the individual contract met its intended conditions. Clarify field meanings with real cases: an injury date and a report-submission date can both be extracted correctly but answer different business questions. [[define-domain-success-and-expert-accountability]] addresses expert ownership of domain criteria. [cite:gv4w23xYj-0:c12] [cite:PwCSYy-oGsM:c09] [cite:W4pnzOURwHQ:c10]

Maintain separate measures for completion, correctness, tool reliability, availability, safety incidents, latency, cost, human escalation and recovery. Define each numerator, denominator, population and time window for the workflow rather than importing a universal threshold. A quick successful API call is not the same as a completed multi-call task: an intermediate timeout can invalidate the work. Accuracy remains important, but does not subsume operational reliability. [cite:vljxQZfJ9wY:c12] [cite:_naLJOqVOEI:c09]

Do not hide opposing dimensions in a single average. One product demonstration reported a 17-point safety improvement and a 17-point completion decline after adding confirmation before every action. The flat average obscures a substantive tradeoff; the example is not a controlled field trial or a universal effect of confirmation. [cite:v5tm5EAzsAs:c01]

A readiness assessment is also not an outcome score. Separate configured mandate, permissions and platform capabilities from observed runtime execution and outcomes; governance spans both. A mature-looking configuration does not demonstrate task accuracy, and the source framework's component count is inconsistently described. [cite:PwCSYy-oGsM:c02]

## Measure autonomy and the right handoff

Name the start and end of the workflow before calculating straight-through completion: a task completed from input through the named endpoint with no human intervention. State the eligible task denominator and count human edits, approvals and interventions separately. An autonomous draft rate cannot be relabeled an autonomous production-deployment rate. This is a proposed diligence definition, not a measured company-wide autonomy result. [cite:gDRCpTMCqEU:c03]

Nor should every handoff count as failure. In an illustrative banking scenario, an agent answers a mortgage question and passes refinancing context to a senior banker as intended. Evaluate whether the right case reaches the right person with useful context, rather than maximizing containment. A shared handoff service is one vendor's recommendation, not a proven superior implementation. [cite:PwCSYy-oGsM:c01] [cite:PwCSYy-oGsM:c08]

Measure decision-relevant time as well as production speed. In the acquisition-report scenario, a deck produced sooner does not guarantee that a real business slip reaches the steering committee sooner. Track the interval from the first sign in source data to decision-maker visibility separately from report turnaround. [cite:-a2oTS9J67U:c04]

## Find the constraint and account for downstream quality

Map discovery, implementation, review, administration and operations to find where work actually waits. Accelerating generation at a non-bottleneck may merely move the queue to review. A speaker describes agents producing requirements from legacy code and reducing administrative work as alternative targets; the reported savings lack complete measurement methods. Check whether the chosen intervention changes throughput at the constraint and what people do with any freed capacity. [cite:Se8jHLliLXE:c09] [cite:Se8jHLliLXE:c10] [cite:Se8jHLliLXE:c11]

For software work, retain delivery flow measures but pair them with defects, reverts, change failures, review, rework and maintenance over time. Compare adoption cohorts with these outcomes and costs, while recognizing that users and teams may differ before adoption. Observational trends and secondhand reports cannot establish that AI caused quality changes. Perceived ease of maintaining code and confidence in shipping it are distinct survey outcomes, neither a direct correctness measurement. [cite:Se8jHLliLXE:c01] [cite:Se8jHLliLXE:c06] [cite:Se8jHLliLXE:c03] [cite:VrpEyglYgeU:c03]

Measure the failure floor, not just the best demo: unwanted messages or destructive actions can matter more than an impressive occasional success. Include the supervision and recovery that remain with users; an agent can add work if every output must be checked and repaired. Anecdotal discussions of trust at particular reliability percentages are not universal acceptance thresholds. [cite:jHMiYtjoJfA:c04] [cite:Emo5FGGY-wM:c06]

## Test whether people can use and keep using it

Tell users which tasks are supported reliably, which are being improved and which are out of scope. An out-of-scope request can indicate a need to expand the product or clarify communication, not necessarily a model defect; a scope detector can itself be wrong. The claimed trust benefit of transparency is qualitative. [cite:Emo5FGGY-wM:c07] [cite:BOCjybvJYM4:c07]

Evaluate the actual operators' skills and interfaces. A mixed technical and nontechnical QA team prompted one vendor to add a nontechnical experience; another customer needed customization for varied downstream workflows. These cases identify requirements, not controlled usability or adoption gains. [cite:Emo5FGGY-wM:c09] [cite:Emo5FGGY-wM:c10]

Separate employees who never try the product from those who try it and do not return: the first suggests an activation investigation, the second a workflow-fit investigation, although the causes can overlap. Define retention cohorts, periods and denominators, track unmet requests, and assign ownership for demonstrations, sponsorship and continued enablement. One team recreated familiar subscriptions and folders as saved searches and collections before introducing broader agent uses; it attributed product fit to that transition without a causal comparison. Expectations can rise once a capability becomes ordinary, so early enthusiasm is not durable-value evidence. [cite:DrTdD-ttjCY:c05] [cite:DrTdD-ttjCY:c06] [cite:CLve4Nx_RwI:c09] [cite:DrTdD-ttjCY:c07]
