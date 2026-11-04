An agent may legitimately read an email, repository or tool description and then mistake an instruction embedded there for authority to change its task. The danger is not just an undesirable answer: the same agent may be able to read private records, write shared memory or call tools. Threat modeling follows that path from attacker-controlled input to the actual consequence.

## Map reach, assets and trust boundaries

Start with the agent's legitimate purpose and the assets it can affect. Diagram inputs, context assembly, model, memory, tool endpoints, connected applications and outputs that trigger operations. For each crossing, ask who controls the material, what the agent can read or write, whose identity it uses and what a successful attacker would gain. A support agent with access to customer records and messaging has a different blast radius from one that only answers from a public manual, even if both are called support bots. Revisit the map when tools, data, models or workflows change. [cite:p-2MT8KYZqU:c06] [cite:BgLdvF7Qkh8:c02] [cite:ZyC56eV8sVw:c07]

Ordinary success with cooperative users is not an adversarial assessment. Use the role and its real privileges to identify high-consequence probes, while remembering that attacks can also arise outside the nominal task. More capable systems may both do useful work and interpret attacks that weaker systems miss; the poem-wrapped instruction example is illustrative, not a measured model comparison. [cite:UQKg0td-Bf4:c09] [cite:UQKg0td-Bf4:c01] [cite:qStB9GbppMU:c09]

## When source content claims authority

Indirect injection enters through material the agent was authorized to read, rather than necessarily through the user's own request. An email summary can include hidden text telling the agent to perform an unrelated action. The boundary is crossed when source content is promoted from evidence about the task to an instruction governing the agent. Human visibility is not a reliable indicator of what a parser or model receives. The hidden-email examples are illustrative or briefly reported incidents, not measurements of defense effectiveness. [cite:p-2MT8KYZqU:c01] [cite:5O6jLtoeKrg:c04]

Record origin and trust level, and treat retrieved material, repository comments and reviewer inputs as data even when they contain imperative language. Internal-looking material can also be poisoned. A locally reviewed skill can load instructions from a mutable remote file, changing effective behavior without a local edit. A sandbox or a prompt saying to ignore embedded commands is not a complete defense; consequential actions require independent authorization. See [[agent-authority-isolation-and-runtime-controls]] and [[agent-and-dependency-supply-chain-security]]. [cite:4lXks428C9o:c04] [cite:1EZdpEhwmNc:c07] [cite:bSG9wUYaHWU:c08]

## Tool metadata can manufacture a dependency

Tool descriptions are themselves input to the model. A malicious description can make a privileged call appear necessary to complete a harmless request. In a demonstrated weather-tool trap, the description said the agent needed an internal-configuration call and its output to answer; the trace showed the internal call. That run did not establish external exfiltration. Inspect descriptions and actual cross-tool calls, not just protocol conformance: a properly formatted integration can still carry hostile instructions. Implementation vulnerabilities in the server are a separate surface. [cite:1tpqdglI3T0:c10] [cite:p-2MT8KYZqU:c09] [cite:ZyC56eV8sVw:c10]

## Memory makes an attack durable

An instruction need not act immediately. A poisoned document can ask to be remembered and triggered later, when a secret becomes available; shared notes or learned skills can carry the instruction into another run or to another agent. One described sleeper-memory scenario combines persistence with a later outbound channel; another cross-agent resume scenario is illustrative, not an observed propagation or containment experiment. [cite:5O6jLtoeKrg:c09] [cite:BgLdvF7Qkh8:c08]

Map not only who can read a store but also who can write it and which future agents will ingest it. Review learned artifacts and consider isolating memory or using fresh runs for sensitive work. That trades useful continuity for a smaller persistence surface; neither a review nor a memory-free run proves safety. Suggested screening and skill-review layers have not been shown to stop all attacks. [cite:p7gaxmCUiIU:c12]

## Review capability combinations, not just components

The consequential path often combines three ingredients: untrusted input can influence an agent that has private data and a tool capable of external action. For example, a malicious support message could redirect a broadly connected agent toward collecting and sending customer information. A proposed rule of two calls for human sign-off when all three are needed together. Treat this as a review trigger, not proof that any pair is safe or that approval alone prevents compromise. Examine the actual end-to-end path and reachable destinations. [cite:-CnA2lGfymY:c04] [cite:5O6jLtoeKrg:c05] [cite:BgLdvF7Qkh8:c02]

## Maintain an inventory, then test the paths

An AI bill of materials should include models, datasets, prompt templates, agents, memory stores, tools, dependencies and connected applications, as well as generated outputs and observable behavior. It helps identify affected systems when a component changes or is found vulnerable. It is not proof that discovery is complete or that an inventoried component is safe; a vendor inventory demonstration did not evaluate discovery completeness or incident-response performance. [cite:ZyC56eV8sVw:c06] [cite:1EZdpEhwmNc:c03]

Use the inventory to choose realistic attack paths and probe whether the agent follows malicious content, stores it, or invokes an unrelated tool. A passed probe is evidence only about the tested cases—not containment. Isolation, independent action and egress controls, and stopping mechanisms need their own verification; see [[safety-evaluation-and-adversarial-probing]] and [[agent-authority-isolation-and-runtime-controls]].
