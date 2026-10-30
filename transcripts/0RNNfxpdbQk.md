# Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest

Source: https://www.youtube.com/watch?v=0RNNfxpdbQk

Upload date (publisher UTC): 2026-07-20

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/ed/ed48b51695a2f81a88ac6be87f8fa70384ed8778297cf45646e08731863f64f7.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[1.66s] Hi, my name is Drasko Profirovic. I'm a staff engineer at Pinterest. Today, I'll cover Medic for Apache Spark, which is our agentic diagnostics tool built to troubleshoot Spark failures.

[16.10s] We'll dive into why we built the Medic, the journey from prototype to the current architecture, lessons learned along the way, and what's next.

[26.34s] A bit of background about myself. I had the opportunity to work at a few companies under the data platform org. Despite many differences between those companies, there's at least one similarity, the high bar for providing quality support to partner teams who rely on the infrastructure owned by the data platform org.

[46.62s] I'm sure I'm not alone when I say that the support rotation feels like a never-ending stream of questions or problems to resolve.

[55.08s] Moreover, it's easy to forget how difficult it is to troubleshoot Spark or any distributed system for that matter. This is particularly true for anyone just getting started with the framework.

[67.82s] The other challenge with supporting a load-bearing system comes down to ambiguous priorities. Do you focus on helping one team with their failing job, or do you unblock another team with a looming deadline?

[80.38s] It's not always straightforward to rank these asks, but as humans, we often have to decide how we'll spend our time. The same is not true for LLMs. We can easily scale out knowledge and capabilities on demand.

[96.14s] Our vision for a diagnostics agent was to ask it simply, "Why did a job fail?" And get back a deep research document which provides evidence on the root cause of the failure.

[107.82s] The agent would also need to provide suggested fixes that are grounded in the context of the job.

[114.20s] Needless to say, this agent would need to be available on all the surfaces where our users operate today, like Slack or the Airflow UI, to name a few.

[125.66s] We started by exposing our data resources by way of the Model Context Protocol as a way to connect them to the LLMs. At this point, we could start an LLM conversation with the MCP tools enabled and ask the model to reason about our Spark job.

[142.56s] This worked in practice, but it required a lot of careful prompting from the human operator.

[149.56s] We extended our prototype by creating a single reasoning and acting agent, ReAct for short.

[156.33s] The agent was given a single prompt which embodied the problem-solving approach it would take, how to structure the responses as a report, and specific examples to common failure patterns.

[169.20s] At this point, we had enough capabilities to start trialing the solution with our beta users.

[175.54s] From those early trials, we found a lot of shortcomings with our solution.

[181.00s] Prompt tuning became unsustainable. One prompt had to do everything, and adding detail in one area degraded the behavior in another.

[190.96s] Response quality was inconsistent. Sometimes analysis was shallow or other times too verbose. We lacked controls to keep the agent on track,

[202.08s] and we often hit context window issues for production jobs. As an example, large tool outputs from logs would click... quickly consume tokens and brought a halt to the agent's reasoning.

[215.52s] Lastly, our end-to-end testing strategy up to this point relied on manual tests from production.

[222.34s] This felt anecdotal since production data would be retentioned away. Overall, it was hard to know if changes broke earlier wins.

[233.18s] To improve the system, we invested in observability and testability. We used OpenTelemetry to publish traces to Langfuse, and by viewing the agent's execution as a waterfall diagram of steps, we could better understand the cause of lower quality responses.

[251.50s] The reliance on manual end-to-end testing highlighted the need for a more reliable and scalable solution. We built an end-to-end test harness to snapshot production state,

[263.64s] and we could codify expectations as offline evaluations.

[268.88s] Lastly, this allowed us to tune our prompt based on the results.

[274.38s] In practice, the end-to-end test harness is simple. In record mode, the agent calls real downstream systems, and tool responses are captured as fixtures. These are then saved to the file system and checked in as code.

[289.86s] Playback mode, the agent runs against fixtures instead of production data, but this time performs the analysis and generates the report. The test suite then grades the report based on the offline evals we have authored.

[305.34s] For example, an offline eval might check for a limit of three suggested fixes. The eval would score lower if the agent provided too many fixes towards managing the verbosity of the final report.

[319.50s] Our end-to-end tests allowed us to quantify quality instead of relying on intuition, and as we grew our test coverage, we gained confidence that improvements do not introduce regressions.

[332.36s] Once we had the testing coverage in place, we invested deeper in our handling of logs.

[339.52s] Logs are noisy, and many exceptions we see in logs are benign, so simply focusing the last exception may not always be suitable.

[349.44s] Initially, we kept it simple with a heuristics-based approach using regex to filter out certain exceptions, but this didn't scale well. Instead, we built the exception classifier pipeline. The core idea was we would learn which exceptions commonly appear in successful jobs, treat those as likely red herrings, and filter them out in the future analysis.

[373.25s] The agent would fingerprint and cluster exceptions, then rank them based on content relevance and how recently they occurred compared to the termination of the job.

[383.59s] The agent stopped consuming logs directly and instead was given two MCP tools: get the top-K truncated exceptions or get full log details for a specific exception.

[396.68s] This resulted in an improvement to our signal-to-noise ratio and reduced the chance of the LLM to anchor its investigation with a misleading exception.

[407.92s] Like logs, we found that we could improve the overall quality by investing in how we handle metrics.

[414.34s] Raw time-series metrics are not context window friendly. Simply feeding the raw data to an LLM works in the small scale but fails for long-running jobs in production. Not to mention, it's horribly token inefficient.

[429.97s] The approach we took was to perform metrics analysis in a quarantine sub-agent. We would convert the raw time-series data into graphs, which are then collaged into an final image, the appearance of which isn't much different than a Grafana dashboard, albeit with annotations that we found useful, like calling out the min and max values.

[453.54s] The image is then attached to the LLM conversation, and we would prompt the model to reason about patterns in the data. Images worked better because we could guarantee how many input tokens would be used for analyzing any given Spark job, irrespective of its duration.

[472.36s] Examples of useful signals we would be able to get included executors dropping down to zero or near zero, long plateaus or bottlenecks, effectively any resource behavior inconsistent with healthy progress.

[487.28s] Our sub-agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy.

[497.78s] Lastly, we overhauled our agent harness. We went from a single ReAct agent to a multi-agent architecture.

[507.07s] This was accomplished by building on top of LangGraph's Deep Agent library. Each agent now had a dedicated prompt and a subset of MCP tools. Meanwhile, the Deep Agent library itself provided built-in tools to keep the agent on track, like a to-do list or a virtual filesystem.

[526.00s] This approach mirrors what we've come to expect from our coding tools like Claude Code or Codex, to name a few.

[533.10s] We could finally decompose our single prompt into specialized roles. This refactor provided clearer separation of each agent, and it made it easier for developers to maintain each prompt separately while performing focus testing on the system using our end-to-end test harness.

[550.94s] A pleasant consequence of this architecture was that the effort to expand the scope of the project was as simple as adding a new prompt, and this is how we were able to extend the Medic to also help users optimize their Spark SQL jobs.

[568.14s] Our workflow started... starts with the user's request entering the system, whereupon intent is classified as either requiring a simple answer to a question or a deep diagnostic session. If it's the latter, the triage agent determines the Spark job's lifecycle state, and if it's failed, it'll use a subset of tools to generate a set of failure hypotheses.

[592.78s] Each hypothesis is researched in parallel, where we gather evidence to validate it.

[599.28s] These research agents then return a score and a root cause. The supervisor selects the highest confidence root cause and invokes the healer agent to offer remediations based on runbooks ingested into our vector database.

[615.18s] Lastly, the supervisor agent would assemble the final report, ensuring proper formatting.

[623.76s] The multi-agent architecture proved very effective, offering us the greatest control over the system's behavior.

[632.04s] Enhancements to log handling led to substantial reduction in inaccurate root causes.

[640.34s] We trialed using LangGraph's workflows to make the agent more deterministic, but this approach proved to be brittle compared to the reasoning and acting agent paradigm.

[650.92s] What we're experimenting with now is incorporating user feedback from prior sessions to automatically improve the agent.

[659.30s] Lastly, we see a broader opportunity to apply this pattern to other distributed systems like Flink and Trino.

[668.16s] Medic for Apache Spark project was made possible by the hard work from these contributors. Thank you for your time.
