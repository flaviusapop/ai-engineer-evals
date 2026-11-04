Evaluation is both a shared technical capability and a set of decisions someone must own. A platform can make runs and evidence accessible, but it cannot decide what a particular product should do, supply domain judgment by itself, or make an ambiguous owner accountable.

## Register agent purpose and accountable ownership

Maintain a discoverable inventory recording each agent's product, purpose, accountable owner, tools and endpoints. Someone investigating an unexpected action can then find the responsible team and understand the intended use; another team can discover an existing capability before rebuilding it. Approved development frameworks can populate the registry automatically, with manual registration for agents outside that path. The proposal favors low-friction visibility rather than making every experiment wait in a universal central approval queue, which can encourage invisible shadow IT. It does not provide measured governance outcomes or a risk-scoring formula. [cite:iniryju23Sk:c02] [cite:iniryju23Sk:c07]

A registry is an inventory, not a permission grant or evidence of compliance. Runtime enforcement and risk-sensitive human review are separate responsibilities: see [[agent-authority-isolation-and-runtime-controls]] and [[human-review-and-agent-governance]].

## Share quality work across disciplines

Organize around the user problem rather than assigning an entire agent product to a model team merely because it uses AI. Data scientists contribute testing and risk expertise; product and domain specialists understand the desired behavior; application and systems engineers connect tools, services and interfaces. A supervisor invoking child agents across infrastructure illustrates why model knowledge alone does not specify the surrounding system. This is organizational guidance and an architectural example, not a measured staffing formula. [cite:NKwIX3CiRgU:c01] [cite:NKwIX3CiRgU:c07]

One practical division is for product managers to frame success hypotheses, domain experts to define and label consequential cases, analysts to interpret results, and engineers to implement data integration and automated runs. In DoorDash's account, strategy and operations set priorities and quality bars, product teams develop rubrics and workflows, operations annotate, and engineering supplies APIs and telemetry. These are local choices, not a mandatory organizational chart. Judge-prompt ownership can sit with operations, product or engineering in different teams; the key is to name an owner and make changes reviewable. [cite:T3SS931wU0I:c04] [cite:bMjlRrWjdT0:c02] [cite:bMjlRrWjdT0:c09]

**Illustrative handoff:** for an insurance assistant, the product owner identifies a disputed-claim workflow, an insurance expert labels what an acceptable answer must include, and an engineer turns those cases into repeatable runs. The owner reviews disagreements with the expert before changing the rubric. The tooling carries the evidence; the participants remain responsible for its interpretation. Domain participation should not depend on every expert being able to code. [cite:JsCCrBF7F1g:c06]

## Share primitives, keep local decisions close to the work

A central platform team can provide stable APIs for traces, scores and datasets, plus workflow primitives for annotation and judge calibration. Domain teams can then build or use interfaces suited to their own tasks without waiting for a centrally built custom screen for every change. DoorDash describes telemetry and human-workflow surfaces backed by shared APIs, and a self-service calibration interface where product managers or operators can configure a run and choose a judge model. The architecture is a reported case, not a published endpoint contract or a reliability measurement; the ability to run a calibration does not guarantee that an unsupported user has produced a valid judge. [cite:bMjlRrWjdT0:c04] [cite:bMjlRrWjdT0:c07]

A spreadsheet can be a useful starting point. A polished results screen improves access but remains a reporting tool if users cannot change a prompt, model or parameter and compare persisted runs. The next useful capability is to retain configurations and evidence so stakeholders can inspect side-by-side experiments over time. Shared infrastructure need not mean central sign-off for every iteration; conversely, local autonomy does not remove the need for an accountable quality owner. The recommended progression is a design proposal, not a required sequence for every organization. [cite:mUQoVz7THu0:c03] [cite:iniryju23Sk:c07]

Offline experiment interfaces also do not show what happens after deployment by themselves. For that distinct operational loop, see [[production-evaluation-and-monitoring]].

## Organize accountable development and architecture evolution

Give domain quality a named decision-maker with authority to participate, rather than making experts advisory while no one can resolve a disagreement. One speaker advocates a principal domain expert; this is an opinion informed by a case, not evidence that one reporting structure always wins. Make plans and review requests visible to engineers and product stakeholders so requirements can be corrected before execution finishes. A shared board is a demonstrated collaboration design, not a measured improvement in outcomes. [cite:kfSDc2eVLo4:c07] [cite:48YUYDjwfYY:c09]

Leaders can prototype, but an interruptible leader should avoid becoming the sole critical-path dependency: meetings and incidents can leave the rest of the team blocked. Assign delivery and review ownership to people with capacity to follow through. [cite:bdHaOXZOhcM:c02]

Start with an architecture proportionate to the risk and reserve capacity to replace parts as needs become clear. One internal assistant reportedly began with long instructions and a simple tool stack, adding CI/CD, evaluation infrastructure and a skill library later. That retrospective is not proof that delaying evaluations or controls is appropriate in a high-risk deployment; a workable early stack still needs risk-appropriate quality gates. [cite:DrTdD-ttjCY:c08]
