An agent can only use an interface it can find and understand. A long list of opaque API endpoints is not automatically a useful toolset: schemas consume context, names may hide the intended action, and the result of a call may not give the agent enough information to proceed. Design the individual operation, its discovery path and its invocation environment as separate choices.

## Discover capabilities progressively and tune schema selection

For a small, stable set of tools, loading every schema may be simpler than maintaining a router. When a large catalog makes context or selection costly, expose a search mechanism or concise capability descriptions first, then load complete definitions for relevant candidates. An embedding-based router can index descriptions and retrieve a shortlist for each request; test the smallest shortlist that meets your required recall, including uncommon tasks. A smaller shortlist costs less context but can omit the only suitable operation; wider retrieval or a second search costs more and may add a handshake. Suggested catalog sizes and shortlist lengths are starting heuristics, not universal thresholds. The reported catalog experiments have incomplete methods and conflicting counts, so they do not establish a portable accuracy or savings figure. [cite:dAoOYFx7ZYw:c02] [cite:vh2VGuQ3zhY:c04] [cite:vh2VGuQ3zhY:c07]

The same staged pattern applies differently to procedural skills and documents. A skill's name and trigger description help select a playbook; the body and specialized references are loaded when needed. A document interface might expose a short index description and then retrieve the relevant schema or passage. Test whether the agent actually selects the right skill and follows its references: merely making a reference available does not ensure it is read. A large database schema can be disclosed in chunks only if the extraction interface can return chunks; a prompt asking for partial results cannot create that capability. An experimental filesystem-shaped documentation interface and suggested semantic augmentation have no measured retrieval advantage in the source. [cite:JT3OzDKrucU:c02] [cite:GmAQKINjv1E:c08] [cite:JT3OzDKrucU:c09]

## Replace the per-turn active tool registry

Selection and registry maintenance are distinct. Once the current request's candidates are selected, replace the previous active shortlist rather than continually adding to it. Otherwise a conversation can eventually carry the whole catalog again. Check the framework's actual behavior and ensure the current task still has the tools it needs. The demonstrated replacement hook was described orally, not as a complete implementation. Crucially, removing old schemas does not remove chat history: history compaction and broader context economics are separate concerns in [[context-and-retrieval]]. [cite:vJukHCIv7Ck:c03]

## Compose calls and intermediate results in code

A program can run independent reads in parallel, wait for a result before issuing a dependent call, branch on that result and reduce structured intermediates before sending a concise answer to the model. For example, an **illustrative** inventory lookup could fetch stock for several warehouses concurrently, then request a reorder quote only for locations below their threshold. Check failures and partial results before treating the aggregate as complete. This avoids requiring a new model turn for every intermediate operation, but is not itself evidence of speed or safety. [cite:dAoOYFx7ZYw:c03]

Choose an execution language the intended model can use and test the generated program, including numerical behavior and error handling. Large images or binaries need not be serialized into model context: an appropriately access-controlled reference can identify an artifact for later use. The source's warnings about language arithmetic and smaller-model fit are qualitative, not a controlled comparison with native tool calls. Execution permissions and isolation are separate: see [[agent-authority-isolation-and-runtime-controls]]. [cite:dAoOYFx7ZYw:c11]

## Make individual tool meaning and first-call affordances legible

A tool description should answer what its identifiers identify, what the operation changes, and how failures appear. An experienced developer may know what a delete-item endpoint deletes; an agent seeing only a schema and docstring does not inherit that product history. State, for example, whether the identifier is an item or a collection ID, whether deletion is reversible, and what a not-found response means. These are illustrative contract fields, not claims about a specific endpoint. [cite:3_gYbhABcAE:c09]

Names, inputs and output shape also affect adoption. A practitioner observed agents falling back to familiar grep and file reads rather than using a graph tool; a search-like name, multi-keyword input and evidence-bearing grep-like results can make the first call easier to interpret. Test actual trajectories instead of assuming familiar formatting guarantees use. [cite:KhRjivBSwiw:c09]

## Encode known workflow steps in executable tools

If product rules already say which operations form a valid workflow, do not make the model rediscover every rule from generic CRUD calls. In one document-pipeline rebuild, a classify-to-extract operation replaced repeated generic step creation, with validators, contextual next-step guidance and occasional automatic chaining. This embeds a known valid path while leaving judgment where it is needed. The reported reliability improvement was qualitative, without a controlled prompt-versus-architecture comparison. A valid pipeline can still extract the wrong information; inspect [[agent-task-flow-and-action-evidence|action evidence]] as well as structure. [cite:jJQoVkd5yLg:c03]

## Maintain a discoverable catalog and diagnose contract drift

Give each catalog entry an owner and version alongside its name, intent-oriented description and schema. When a description or schema changes, refresh its search index. Record candidates retrieved, the eventual call, failures and fallback paths; inspect rare operations and use the terms users actually use. If the required operation is absent from the shortlist, widen the search, retry or fall back to a broader group, then improve the entry if its description caused the miss. [cite:vh2VGuQ3zhY:c05] [cite:vh2VGuQ3zhY:c06]

A retrieval miss is not the same as a permission or configuration mismatch. Separately compare instructions with the tools actually exposed and permitted. One speaker reported hundreds of runs requesting an unavailable tool; the case does not quantify comparative reliability. Finding a tool never grants authority to execute it. [cite:juoNbJiZUi0:c09]

## Select retrieval primitives and fit uneven clients

Teach the harness which retrieval primitive fits the information need: literal grep-like search finds exact strings; BM25 uses lexical term matching and ranking; semantic search can find conceptually related wording. They are different interfaces with different failure modes, not interchangeable labels. Supply concise index and field descriptions so the agent can formulate useful queries, and evaluate whether the returned evidence answers the task. General retrieval selection and context management are covered in [[context-and-retrieval]]. [cite:O84lhGc1OOI:c10] [cite:ksjwtQop4os:c13]

Connector compatibility is a separate issue. A team found uneven support for server-level instructions and repeated relevant guidance in tool calls. In another workaround, prompts asked permission to map unlinked design components and then requested candidate matches, imitating missing elicitation and sampling features. These are context-specific adaptations, not proof that prompts reproduce native protocol guarantees. [cite:ZIYYsAzaLlA:c07] [cite:ZIYYsAzaLlA:c08]

## Layer local access over remote connectors

A shell-friendly local client can provide familiar command discovery while a remote protocol handles connector interaction; CLI and MCP need not be mutually exclusive choices. A demonstration used browser authentication, OS-keychain storage and persistent sessions shared across agent invocations. It did not audit credential isolation, revocation or multi-user access. For long operations, submit, check progress and collect later only when both server and client support asynchronous tasks; the demonstration did not establish cancellation or failure recovery. See [[agent-sessions-and-long-running-work]] for the broader session lifecycle. [cite:pAnLpiAG6Es:c05] [cite:pAnLpiAG6Es:c06] [cite:pAnLpiAG6Es:c07]

## Choose interaction flow, state access and predictable behavior

Flags are often convenient for independent, single-pass inputs. If the next choice depends on a live response or an earlier answer, an interactive flow can preserve situational guidance and escalation, though flags can encode conditional logic too. For an existing terminal UI, a multiplexer can send keys and capture the screen, but the agent must interpret redraws. A structured side channel can instead expose machine-readable state, choices and inputs while retaining the human UI. In the workshop's low-inventory illustration, include the remaining quantity and whether the agent should ask for confirmation or select a backup, not just the displayed button text. The side channel is a proposal, not a controlled comparison. [cite:aV_vgUSatqs:c02] [cite:aV_vgUSatqs:c03] [cite:aV_vgUSatqs:c04] [cite:aV_vgUSatqs:c05]

Keep each tool's semantics predictable so the model can reason about its result rather than invoke another opaque decision-maker inside every call. Predictability does not mean identical output when external state has changed: a stock query may correctly return a different quantity later. [cite:aV_vgUSatqs:c07]

## Compose domain operations and revisit discovery with stateful scripting

Batching several operations in one script and preserving state across scripts solve different problems. A spreadsheet team exposed roughly fifteen operations as JavaScript functions in a REPL: one call could combine results, while retained variables let a later call inspect and extend an earlier investigation. TypeScript definitions described the model-facing methods while the domain engine remained in C#. The team had also found that a rigid, one-time discovery handoff blocked further investigation; planning was useful, but the agent needed to return to discovery as new facts emerged. [cite:HEFSExa0xl0:c02] [cite:HEFSExa0xl0:c04] [cite:HEFSExa0xl0:c05] [cite:HEFSExa0xl0:c06]

The stateful-versus-stateless observations were not a controlled comparison, and the source does not establish the sandbox's security properties. Test the interface with the actual workload and protect execution independently rather than treating the REPL as a security guarantee.
