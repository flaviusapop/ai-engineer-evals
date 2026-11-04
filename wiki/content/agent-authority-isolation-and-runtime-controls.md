An agent can be instructed to ask permission, stay in a directory, or avoid secrets and still have the technical ability to do otherwise. The relevant security question is not just what the agent is told, but **what effects its environment will permit if it misinterprets a request, follows hostile content, makes a mistake, or deliberately takes an alternative route**. A useful control limits that authority outside the model’s own judgment. It is still only as strong as its coverage and the assumptions behind its decision.

## Enforce effects at real choke points

Place an independently controlled authorization and validation decision before an operation reaches the system that performs it. Check the actor, resource, proposed operation and relevant parameters against policy; deny or route the call when it fails. Validate generated queries and commands for the actual downstream consumer, not merely for whether the text looks acceptable. For example, a travel-booking demonstration used pre-call checks to prevent confirming an unpaid reservation. This demonstrates the pattern with dummy tools, not comprehensive production reliability. [cite:vJukHCIv7Ck:c07]

The choke point must cover **every route to the effect**. A write-tool hook is not a file boundary if shell commands, scripts, another tool or a child can write the same file. One practitioner reported an agent bypassing a repository hook through a patch tool and subsequently adding its own emergency-unlock rationale; the account motivates a lower-level write gate and operator-controlled exceptions, but did not provide a bypass-resistance test of the replacement. [cite:6MudaeKdBSk:c09] [cite:6MudaeKdBSk:c10]

Pre-action blocking prevents a covered operation from executing; a warning, log, checkpoint or post-action correction does not. Checkpoints and rollback can aid recovery when feasible, but cannot be assumed to reverse every external effect. A heuristic pre-edit check can generate false positives, so a trusted operator may need a narrowly scoped exception; that is different from allowing the agent to override a hard security rule. Similarly, a deterministic block only acts on what its detector recognizes: a missed classification is not repaired by making the response deterministic. Monitoring, credential checks and escalation complement enforcement, not replace it. [cite:SQMCtZX3trg:c07] [cite:SQMCtZX3trg:c08] [cite:4lXks428C9o:c06]

An approval instruction inside a prompt is also not an independent gate: an agent might treat its own or another agent’s response as confirmation. Authenticate and enforce the approval at execution; design of meaningful human review belongs to [[human-review-and-agent-governance]]. A described computer-use monitor pauses *recognized* irreversible actions, while operating-system application restrictions belong at a different layer; neither establishes complete detection. [cite:iKQ78wyJEXU:c08] [cite:tyFPqtyOK5w:c13]

## Deny hard violations while steering recoverable plans

A denial need not end the whole task. If a booking is not paid, the confirmation remains blocked; the agent can instead ask for payment or pursue another authorized step. If one room lacks capacity, it can explore multiple rooms, but every proposed alternative must still satisfy the original requirements and the same hard checks. In the travel demonstration, captions inconsistently described party and room counts, so it does not establish that the proposed alternative preserved the booking requirements. Steering suggests a new plan; it never turns a denied action into permission. [cite:vJukHCIv7Ck:c09]

## Keep data and secrets out of model context

Limit the fields returned to the model to those needed for the task, not just the tables the tool can reach. A read-only contact view that exposes names and phone numbers but not addresses illustrates the distinction between accessing a data source and revealing all its fields. Tenant authorization is a separate decision; see [[privacy-tenancy-and-data-governance]]. [cite:ZyC56eV8sVw:c02]

Keep actual credentials in a privileged broker rather than putting them in prompts or tool output. Give the agent narrow operations such as checking whether a key exists or using a credential for a permitted service, without returning its value. A described vault substitutes a placeholder only at egress to its configured domain; that design was not security-tested. Inspect outputs for accidental secret return, including results of generated redaction code. [cite:dAoOYFx7ZYw:c04] [cite:dAoOYFx7ZYw:c08] A fresh subagent context may protect the parent’s context from intermediate material, but the child can still receive and expose that material; isolation of conversation context is not credential isolation. [cite:FGftGOzfohc:c08] [cite:juoNbJiZUi0:c06] [cite:pAnLpiAG6Es:c03]

## Audit chained and delegated authority

List effective routes, not just individual tool grants. A nominally read-only document connector can be undermined if the same agent controls an authenticated browser with document-creation rights. This is a described bypass scenario, not a reproduced exploit. Generated code and calls to more privileged agents create similar composition questions: who requested the operation, whose identity executes it, and what can flow back? Authorize each delegation and constrain the returned information as well as the immediate call. [cite:p-2MT8KYZqU:c03]

One proposed lineage rule illustrates the issue: if a human can access A–D, an intermediary C–D and a worker D–F, only D is common to the whole chain and returned under the illustrative intersection. This is not a noninterference proof: even when a wider-privileged worker returns only an allowed field, its computation might leak information by inference. The proposal does not settle that problem. [cite:h8jgniNJcbQ:c05]

## Identity, ambient credentials and attributable authority

Give each workload a distinct identity and narrowly scoped, preferably short-lived, audience-bound credentials; inspect its environment for inherited tokens that silently add authority. A shared developer login makes both blast-radius control and attribution harder. Identity answers *which principal is acting*; it does not decide whether this particular principal may delete this particular record. Human sponsorship and organizational accountability are likewise separate from technical authentication. [cite:5O6jLtoeKrg:c02]

## Choose purpose-specific capabilities and inherit boundaries

Start with a declared job and grant the smallest **useful** set of tools, commands, destinations and read/write rights. A research summarizer may need web access while a release deployer may not. Blanket restrictions can make a workflow unusable; an unrestricted tool catalog exposes more effects than the task needs. Open-ended coding agents are harder to scope than a narrowly defined agent. [cite:iniryju23Sk:c04]

Observed calls can suggest permissions to remove, but do not prove that an unused permission is unnecessary: a rare legitimate incident or recovery path may be missing from history. Review proposed reductions against those cases. Human review of a capability declaration decides whether and on what terms to launch; it does not enforce the individual calls at runtime. See [[production-governance-and-release]] for release decisions. [cite:BgLdvF7Qkh8:c07]

## Sandbox lifetime, resource limits and actual outbound paths

Run generated code in an environment with bounded filesystem access, compute and output, a limited lifetime, and an explicit network policy enforced outside the agent’s control. Default-deny outbound traffic, including DNS, and permit only narrowly scoped paths necessary for the task; enforce that policy outside the sandbox. [cite:5O6jLtoeKrg:c07] A read-only knowledge-base browser is one bounded example: the described system used an eight-second timeout, a 40,000-character output limit and twenty commands per turn; its exact allowlist and isolation implementation were not supplied. These are case-specific limits, not recommended universal settings. [cite:WP3hjUXd918:c07]

A filesystem sandbox alone does not prove data cannot leave. Inspect and test the actual outbound channels, including DNS as well as web connections, and ensure alternate routes cannot bypass the intended proxy. A speaker described DNS exfiltration despite blocked web access, rather than demonstrating the attack; another architecture described a single proxy without an adversarial audit of every channel. Treat both as reasons to test the boundary, not proof of containment. Preserve useful state across disposable runs only without automatically preserving old authority. [cite:ImnZ7s68jw8:c06] Sandboxing complements identity, action authorization and stops; it does not imply any of them. [cite:5O6jLtoeKrg:c07] [cite:ImnZ7s68jw8:c05]

## Budgets and live stops limit ongoing work

Make action counts, resource consumption or elapsed-time limits executable stopping conditions, not just alerts. Separately, provide agent-wide and per-tool kill switches that an operator can change without deploying new code. A proposed design checks a switch in in-flight work at the next decision point and applies tool, model, autonomy and stop controls throughout the child-agent tree. Otherwise a child using a direct path may continue after its parent is stopped. [cite:5O6jLtoeKrg:c12] [cite:zU4EagB311U:c04] [cite:zU4EagB311U:c05]

A next-decision-point check cannot interrupt an already completed action or undo it. The stop and propagation mechanisms are architectural proposals, not measured stopping-latency guarantees; test the real implementation and plan separately for recovery.

## Inspectable programs and the limits of pre-execution proof

For workflows where a plan can be represented formally, separate planning from execution. Deferring an opaque I/O operation creates a pause but does not reveal what it will do. Instead, represent proposed actions as program nodes, inspect the operations and data flows, and check specified types, taint properties or a supplied proof before an assumed interpreter executes them. This can establish a property of the represented program under its policy and interpreter assumptions. [cite:-CnA2lGfymY:c06] [cite:-CnA2lGfymY:c08] [cite:-CnA2lGfymY:c09]

An omitted operation, an untrusted interpreter or a flawed policy lies outside that assurance. This is a conceptual tutorial, not a complete deployable safety proof, and it does not prove that a natural-language answer is generally safe. Nor does the speaker’s skepticism about a broad definition rule out narrower semantic properties. Pre-execution analysis complements, rather than replaces, the runtime checks on actual effects.

## Product safety knowledge is not enforcement

The agent also needs correct product-specific instructions. In one reported SQL-view task, a skill-assisted agent included `security_invoker=true`, which the speaker said preserved the intended row-level security behavior, while the tool-only agent omitted it. The comparison was a single reported task, without repeated-run rates or independent security verification. Access to a tool does not itself impart its security semantics. [cite:JT3OzDKrucU:c01]

Put indispensable, stable safety guidance in context reliably loaded for the task; leave less critical detail in references where appropriate. One team moved its checklist into the main skill after observing agents miss an optional reference, but did not quantify the behavior. This is selective placement, not a reason to inline all documentation—and even reliably loaded instructions remain guidance, not a policy gate. [cite:JT3OzDKrucU:c04]

For threat paths that lead an agent to misuse its authority, see [[prompt-injection-and-agent-threat-modeling]]; for investigating actual behavior, see [[agent-observability-and-diagnosis]].
