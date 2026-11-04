A long-running agent is not just a slow request. The client may disconnect, an execution container may fail, a tool may wait, and a later worker may need to continue. Design where the session’s state is held and who can recover it independently of where a model call happens.

## Separate session persistence from execution failure

If the harness and its execution sandbox share a container, losing that container can lose the session with it. One proposed design separates a stateless harness and sandboxed execution from an append-only session log, with credentials stored separately. A replacement harness can consult durable records rather than relying on the dead container’s memory. This is a vendor architecture proposal, not evidence of an independently verified security boundary or complete recovery. Access enforcement belongs to [[agent-authority-isolation-and-runtime-controls]]. [cite:9QebvrrY3KY:c01]

## Specify what survives interruption

Decide what identifies a session, what records its history and outstanding work, where that state is held, and how a replacement worker rehydrates it after interruption or inactivity. A managed runtime may provide compute without supplying every persistence and rehydration behavior an application needs: one team reports adding those pieces itself. Long-running evaluation workers face the same requirement to resume or respawn while preserving a consistent run, but the cited account provides no checkpoint format or recovery benchmark. [cite:32nrHU6zHU8:c01] [cite:rWtbOgl5FTU:c08]

A log of events is not automatically an executable checkpoint: it may document what happened without preserving enough state to continue safely. Nor does a resumed worker imply that external actions were reversed. Specify and test the actual recovery contract; use [[agent-task-flow-and-action-evidence]] for action evidence and operational recovery rather than treating session persistence as proof of either.

## Exchange events without making the client the worker

An event interface lets a client send user-message events and listen for agent events while execution has its own lifecycle. In a workshop chat application, the backend relays a server-sent event stream to the browser. Separating event storage from session mechanics also allows new recorded event types without tying all persistence changes to execution. Filter model and tool events for observation, but do not confuse an event feed with resumable state; the workshop’s longer-duration capability claims were not demonstrated as elapsed runs. [cite:FGftGOzfohc:c01] [cite:FGftGOzfohc:c03] [cite:qJtcEDc_WJU:c03]

For shared chat, one proposed mapping assigns a session to each thread, identifies the sender in injected messages and provides an explicit reply tool. Separate agents and memory per channel may help when channel boundaries matter. Thread mapping is routing, not proof of authorization or tenant isolation; assess access separately. [cite:QSeaZ6qHyXs:c09]

## Preserve useful working context

An unattended run needs the task goal, prior attempts and relevant tradeoffs, but indiscriminately adding telemetry can leave both noise and critical evidence gaps. One practitioner prepares an overnight run with business context and clarification before leaving it unattended; another describes investigations with too much low-value context and missing essential logs. Choose context by relevance and identify what is unavailable, rather than simply maximizing or minimizing its size. [cite:bdHaOXZOhcM:c03] [cite:JJGbw4ggaFs:c05]

Compaction makes room in the model’s working window but can discard details needed later. A deliberately naive demonstration retained the system prompt, task and last two messages while dropping intervening history; that does not establish preservation of working state. An append-only original log offers a possible way to retrieve earlier events after compaction, provided retrieval, selection and access controls work. A provider reports ten-hour sessions using compaction but gives no compaction-quality measurement or evidence of year-long continuous operation. [cite:C_GG5g38vLU:c05] [cite:9QebvrrY3KY:c02] [cite:qJtcEDc_WJU:c04]

Working context is selected material for this session; a retained event log is its historical record; an executable checkpoint must support continuation; curated organizational memory serves later work. These are different forms of custody and cannot be substituted merely because each contains text. For curation see [[reliable-agent-context-and-memory]].

## Steer a waiting session without assuming rewind

A corrective user-message event can be queued to influence future work; it does not undo earlier actions or roll execution back. In one discussed product, ordinary messages can queue while a model works, but a custom-tool wait blocks message injection and returns HTTP 400 to preserve ordering. A proposed coordinator delegates that blocking work to a subagent so the main thread stays responsive; the discussion does not validate all races. Forking or rewind was a requested roadmap feature, not demonstrated recovery. Clients need to represent the waiting state and handle the product’s actual ordering semantics. [cite:FGftGOzfohc:c10] [cite:QSeaZ6qHyXs:c02] [cite:QSeaZ6qHyXs:c10]

## Queue compute separately from choosing execution placement

For hours-long training, an agent can prepare code and parameters, submit the actual run to a separate compute queue, poll for results and resume analysis when it finishes. This avoids holding one conversational turn open for the whole job. The demonstrated queue does not establish scheduling guarantees, fault tolerance or recovery; the session still needs a way to remember the job and interpret its eventual result. [cite:hd7TOvmyAxU:c01]

A remote sandbox answers a different question: where should the agent workflow execute? A speaker recommends getting a debugging loop working locally before moving it to scheduled or event-triggered sandbox execution. Remote placement can let work continue after a laptop closes and permits different resource choices, but it does not itself provide durable session state. Hosted or on-premises security, synchronization and portability claims in these accounts are not independent validation. [cite:9HbzAWnKbo4:c05] [cite:48YUYDjwfYY:c08] [cite:JJGbw4ggaFs:c02]

## Schedule invocations and version their resources

In one product, a deployment combines an agent definition, schedule, initial messages and optional resources such as repositories or memory stores. Each scheduled invocation starts a session; an on-demand invocation is also possible. This differs from keeping one session open indefinitely, and the deployment is not a frozen snapshot of every referenced agent. Some workshop runs failed, so scheduling does not guarantee execution. [cite:qJtcEDc_WJU:c01]

The same speakers describe storing durable agent resource definitions as versioned YAML and using a CLI and API from CI/CD to update them. Versioned configuration helps reconstruct intended changes, but does not preserve a running session or prove which mutable referenced resources were used at invocation. The workshop does not verify all resource types or provide a complete deployment recipe. [cite:QSeaZ6qHyXs:c01]

For selecting triggers, evidence windows and monitoring missing runs, see [[agent-task-flow-and-action-evidence]].
