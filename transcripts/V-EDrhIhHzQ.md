# Modern Post-Training: A Deep Dive  — Will Brown, Prime Intellect

Source: https://www.youtube.com/watch?v=V-EDrhIhHzQ

Upload date (publisher UTC): 2026-07-13

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/9f/9ff3a7e7dbf4dc9afbd080337cc57101bea9fc612dc53e861567649583e1f145.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.10s] [upbeat music] Hey guys, how's it going? Thanks for showing up. This was a little bit of a last-minute assembly.

[17.32s] I, uh, you know, a few days ago, I was, like, talking to swyx. I was like, "Hey, can I still do a workshop?" And he's like, "We got one slot left.

[23.88s] It's Monday at four thirty," and I was like, "I'll take it." Um, and, uh, then yeah. Um, I wanted to kind of just do a bit of an update on, uh, some of the stuff we've been building at Prime Intellect.

[34.88s] So if you don't, uh, know me, hi, I'm Will Brown. I lead applied research at Prime Intellect. Uh, we do a lot of stuff around, uh, every part of the kind of AI research infrastructure stack.

[44.86s] Uh, today is gonna be about post-training, which is where I spend a lot of my time thinking and building. Um, and especially wanna be talking about, uh, the post-training tools that we build, uh, that are fully open source, uh, the verifiers and PrimeRL libraries, uh, which kind of go hand in hand, um, both on the environment side

[59.80s] and the training inference side. Um, and show off some things we've been cooking over the past few months that I think is, uh, kind of the way that things have evolved as the agent use cases have gotten more complex, but also kind of clearer in terms of what people want out of agents and the sorts of things

[75.80s] that are needed to, like, do the sort of post-training that is needed to, uh, power, like, the real-world applications people are building nowadays. And so broadly at Prime Intellect, we are-- our goal is to make doing large-scale open source AI research easier, and to enable companies to train their own models and deploy them and have them improve

[96.18s] based on the scenarios that they actually see in production in terms of use cases for applications and products and internal tasks and workflows. Um, and to give people an option to not just use the open source models that are getting quite good, but to take them and make them even better on their own use cases.

[113.06s] Um, and so we use the phrase the open superintelligence stack to describe what we mean by this. And I think when we said this phrase like a year ago, it felt a little more like marketing, and now it feels a little bit more like, oh, yeah, that's, that's kinda what it is.

[126.84s] Like, the models are getting very, very good. They are superhuman in many ways at lots of things. Um, and what we want to do is give people an open toolkit that they can use to do real training with them, and to have the control that they need to deploy it where they need to deploy it, and customize

[143.76s] it as much as they need to to kind of get the job done. And so this is the stack that we built, and it all kind of sits on top of compute.

[150.04s] So we, uh, operate a global, uh, marketplace of data centers around the world. A lot of these are, like, quite large data centers. Um, we currently operate, uh, over ten thousand GPUs, um, many in, like, uh, hundreds or thousands within a cluster.

[163.48s] Um, we have our PrimeRL training framework. Uh, we have environments built with the verifiers library in our Environments Hub platform. We have our, uh, tr-- platform for research workflows that we're now calling Lab, which is, uh, an assembly of many pieces, including the Environments Hub, hosted training evaluations, as well as inference and sandboxes.

[180.90s] And all of this is in service of empowering and u-unlocking frontier model training. And so, uh, we do this ourselves. We have our Intellect model series with some exciting things there coming soon.

[190.76s] Um, and we also train models with our customers, where we have lots of people we work with who their goal is to do large-scale model training on their own workflows.

[199.30s] Um, and so to do all of this, we need to give people the tools that they can assemble into the, the, the pipelines, the workflows, the research that allows them to actually get the results that they need at scale with everything that they need to do it.

[211.36s] Uh, and so this talk is gonna be about going deep into verifiers and PrimeRL, uh, and showing off some of these new things, but all under the umbrella of what does modern post-training look like.

[221.44s] What does it mean to kind of take a model and train it to be better at your task? What are all the parts? What are all the kind of gotchas?

[228.56s] Uh, and how do you orchestrate this into a system that is actually easy for people to use without needing to go build a massive research team, uh, and to be able to kind of have it be accessible, and sorts of things that anyone who's an AI engineer at, uh, any, like, startup or enterprise that wants to invest

[243.76s] in post-training can actually do. Um, and so there's a cookbook repo that is-- It's kinda like in alpha release right now. It's still changing a bit, but it's a, a preview of kind of all the stuff we've been building over the past several months.

[254.22s] And so today we'll be kinda following along, uh, that framing a good bit. And so, uh, I think the first thing we'll talk about is just kind of what is an environment.

[263.34s] People talk about environment in the context of RL, and think of, like, RL environments, but environments are more than just for RL. They're for all sorts of things in post-training and evaluation.

[272.45s] Um, we're gonna talk about what we're gonna call the, the V1 version of the verifiers library, which is a full overhaul. Everything else still-- from before still works, but we're kind of re-- we kind of wanted to redo it all.

[281.33s] And so we have a new way of doing everything that we think is gonna make a lot more sense and be a lot more powerful for what people are looking to do going forward, as well as kinda talk about how PrimeRL has evolved as a library.

[291.20s] And so PrimeRL is our, uh, like, full stack, uh, open source training framework, uh, to support asynchronous reinforcement learning. Um, and we've got a lot of fun new bells and whistles to show off, um, in terms of both scale and features.

[303.24s] Uh, a lot of this is in service of custom algorithms, so making it much easier to, um, do the kinds of things that people are interested in for modern post-training.

[310.67s] If you have been following the news on on-policy distillation or self-distillation or all these other fun new algorithms that people are coming out with, it is the, the age of research indeed.

[319.34s] Um, and we don't wanna just, like, train small models. We wanna train big models, and we wanna train them really efficiently because as models get bigger, uh, the compute starts adding up.

[329.52s] And if you want to make this accessible to people, especially if you want to be able to iterate on it, it has to be fast. It has to be cheap, it has to be affordable and, uh, reliable.

[339.24s] Um, and all of these kind of funnel into our Lab platform, and we'll talk about both some of the things that we've already released there, as well as some things that are coming soon.

[347.06s] Um, and so the post-training loop, in my mind, kind of revolves around environments in the sense of environments are a language for specifying what you want your model to do.

[357.42s] Um, they are an encapsulation of- The data you might have, the scenario you might want your agent to be in, uh, the way it'll interact with that environment, uh, as well as how to, to score what good looks like to determine what was good and bad.

[371.34s] Um, and often this is-- the first thing you'll want to do with an environment is just evals. And so I think a lot of people are maybe nervous about getting into post-training.

[381.56s] They're like, "Oh, it seems like a lot of work. There's a whole new tool chain. Um, what if I'm already using, like, the frontier models and I want good results out of them?

[389.74s] Uh, or I'm getting good results out of them, or I wanna, like, see what I can do at the harness level first or prompt optimization." And that's all good.

[395.52s] Like, we're not necessarily asking people to just, like, throw everything away. I think in many cases, what people find and what we see with our customers is that, um, the systems that work best for them involve using both, and you kind of want to be able to make these decisions about what is the right-- wh-where is the

[409.70s] right place to train, uh, where is the right place to use a frontier model that is available via some API. Um, and so evaluations are kinda very key to this.

[417.28s] And so, like, evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing. Um, but once you have evals, now this is the same kind of unit of, uh, like, logic that you actually need to do post-training anyways.

[432.02s] And so, uh, building evals is, like, just good for your product hygiene no matter what you're doing. If you want to kind of decide whether to use GPT or Claude or decide do you need Opus or, uh, Sonnet or Mythos for a task.

[444.38s] Like, if you want a min-max on, like, intelligence versus dollars, um, evals are a very good way to do this. But evals also then unlock this, this flywheel. And in terms of modern post-training, I think historically people have done SFT then RL.

[457.50s] It's, like, the main, uh, frontier model recipe, although on-policy distillation has certainly found its way into a lot of workflows. Um, and I think some people are also very eager about algorithms like self-distillation.

[466.90s] We can talk a bit about that and when it makes sense and when it doesn't. But, uh, in particular, one area where it does make sense to do, like, the whole on-policy distillation thing is when you're training experts where you have multiple different things you want your model to be good at.

[479.22s] And people have found that if you have a bunch of different environments that are all different things and you want to have one model be really good at them, a nice way to do this is train individual RL experts on top of the same base model and then do distillation from those teachers into the same, uh, checkpoint.

[494.31s] Uh, that just gen-generally ends up being more reliable. Um, and then once you have this, you want to deploy the trained model, which could be a full, uh, base model with a full weight training, or it could be a LoRA adapter, and you want to serve this at scale.

[505.94s] And ultimately, what is useful about this whole process is it's not just a thing you do once. Like, I think some people also say, like, "Oh, why should I do post-training if the, the frontier models are gonna get better?"

[516.68s] Well, your model should get better too. Like, it's not-- It-- Like, everything's gonna get better. Uh, the point of this is to have flywheels that make everything get better.

[523.26s] And so what you really want is to be able to not just post-train, like, today, but to be able to, uh, have this be an iterative process of model refinement and the sort of thing where you can kind of have the training compute end up be a pretty small fraction of your overall inference budget that you amortize

[537.82s] out such that your model is always getting better and better, um, as you are getting more signal from the real world. And getting the signal from the real world isn't trivial.

[545.80s] Like, that's kind of largely an open question as to, like, how you go about, um, getting information from real-world feedback into your environments. It's an engineering problem, it's a research problem, but it's the sort of thing we're all here at this conference to kind of think about and learn about.

[560.19s] And so I'll, I'll touch on that a little bit, uh, in the talk as to kind of how we, we think about this. But, but really the goal is going to be thinking about what do these tools look like?

[568.58s] How do you actually do this? What are the parts, um, and how do we build it? Um, and so environments as evals, uh, what is an environment? Um, I think it's useful to decompose environments into tasks and a harness.

[582.64s] Um, and this is foreshadowing some of the, the refactoring we've done in verifiers over the past months. Uh, if any of you have used the verifiers library before, you may be familiar with the, the multi-turn environment pattern, uh, tool environment pattern where there's kind of one loop that is owned by the environment that you can plug in

[598.90s] various tools into. And that was really great for a very long time for getting started for people, especially back in the day when people were mostly just trying to graduate from single turn into multi-turn tool, tool use.

[609.34s] Uh, but what we found, and as we kind of iterated on different patterns and extended it in various different ways, we found ourselves repeating a lot of work of, like, adding patterns for a CLI agent or adding patterns for MCP.

[621.20s] Um, and we wanted to be able to, like, step back and rethink, like, how should an environment work. Um, and what it really is, is there's a notion of a harness.

[629.54s] And so, uh, well-- And you-- There's also a notion of a task. And I think one of the reasons that this is kind of subtle and tricky and was a, a design problem that we went over many iterations over the past six months really is, um, certain things, it's not clear where they live.

[642.86s] Like, there's certain things that might belong to the harness and might belong to the task. There are certain tools that, uh, in some cases, it's I want this, uh, task I'm gonna do to use a certain tool.

[652.44s] In some case, the harness has certain tools, same with skills or system prompts or many other pieces of the puzzle in assembling, like, the full world that your agent is going to be operating in or your model is going to be operating in.

[662.80s] Um, but ultimately, the-- we're gonna call all of these parts of the environment. Um, and the goal of this is to have some notion of verification, where you plug in a model, uh, into the environment, which includes a harness.

[674.40s] You give it a task, it does a rollout, and then you verify what it did. Um, and this same process works both for evaluation offline, just understanding which model is better, as well as for doing reinforcement learning, RL, uh, as well as for generating data for SFT.

[690.72s] Uh, I think in many cases, people think of SFT as this thing where they wanna, like, upload a dataset. But really often what they're doing there is they're essentially cobbling together something that's essentially an environment, and they're doing rollouts in it and saving it offline and putting it in one format and uploading it, and then changing it

[706.92s] to another format and then plugging it into a trainer. And the way we've kind of approached this is saying, well, you can just kinda cut all that out and just, like, treat it like a, a, a problem where you're doing rollouts in an environment.

[717.89s] Just in this case, there's a teacher, and the teacher can be another model. It could be replaying from another dataset. Um, but ultimately, it's about collecting rollouts and training on those rollouts.

[727.36s] Uh, and then- On policy distillation, again, takes the same form where you are doing rollouts in an environment just as you would for RL, but the scoring is from a teacher and the, the log probs of the teacher, the likelihood of the teacher rather than, um, the, uh, the reward signal itself.

[742.62s] Um, and so these all in our framework are Python packages. So you can have any dependencies you want. You can, uh, pull data from anywhere you want. Uh, there's a lot of flexibility that we've, uh, unlocked in terms of what these tasks can look like, what these harnesses can look like.

[756.88s] Um, and our goal is to just make this a really flexible toolkit for all the kinds of evaluation things people want to do, both for API models as well as for post-training.

[765.82s] Um, and so verifiers v1 is what we're calling it, which is-- it's not actually released as v1 yet, but, uh, we took inspiration from vLLM doing this, um, and decided that we were gonna kind of have this be the, uh, new pattern that we want to have everything kind of, uh, be centered around.

[782.78s] And the, the key pieces we broke things down into were a task set, a harness, and a runtime. And so these are all composable. You can mix and match them, um, and they're all individually loadable in different ways.

[796.34s] Um, but the way to think about it is that, uh, task sets are the data and the rules of what should be done that are agent agnostic. So they're the sort of thing you could plug an agent into.

[808.42s] Um, and we wanted to take a very general approach in supporting a lot of the great work being done throughout the ecosystem, so we integrate natively with Hugging Face datasets, with Harbor, uh, with NeMo Gym, and OpenEnv.

[820.11s] And most other tools that you see out in the wild that are kind of under the umbrella of, uh, an RL environment, we would call these a task set.

[828.32s] Um, we generally have found that it's useful to have these be harness agnostic, where they represent the, the back end or the server or some state that you're interacting with, but they don't own everything about what the model is doing.

[841.62s] And so it doesn't-- in some cases, it doesn't make sense to plug a model into a task set, especially because we're kind of gravitating towards an agent world where everything is running in a terminal, or it has skills, or it, uh, is using CLI tools.

[854.34s] Um, and these things like often look more complex than just basic loops. Um, but we also want to support basic loops. So we want to kind of allow both the old way of doing things and the new way of doing things.

[865.67s] And so, uh, everything that was the old way is now the default harness, where it's system prompt and tools in a loop. Um, but the harness pattern also supports much more flexible execution of things like recursive language models or CLI agents like Codex, Claude Code, OpenCode, or classics from the research literature like mini-SWE-agent, or building your

[884.20s] own with arbitrary Python libraries like LangChain or DSPy. Um, and so we've been able to decouple these into a pattern where you get to write your harness independently of your task set.

[894.70s] Uh, there are kind of some basic sanity checks about properties that like harnesses either do or don't support and task sets do or don't require, uh, and these kind of click together.

[903.24s] And the runtime is where this executes. And so we've, uh, still been embracing a lot of the asyncio patterns from before, but we've leaned a little more into having things be subprocesses, uh, where you can still run everything locally.

[916.92s] You don't have to use sandboxes, but you can use local Docker, or you can use our own Prime sandboxes layer. You can use any other sandbox layer you'd like or kind of build from scratch.

[926.96s] Uh, and so the harness, uh, the runtime back end, uh, just is a place where the harness can run its code. And so the harness just needs to be able to run code somewhere as a script, essentially.

[936.62s] Um, we've used a lot of the uv tooling, where uv script is a very powerful pattern, uh, to be able to kind of mix and match and kind of contain dependencies.

[944.12s] Um, but what happens is once you plug these together, you run a rollout on a task from a task set, and you get a trace. Um, this is live on the verifiers main branch, uh, for PrimeIntellect-ai/verifiers on GitHub, as well as its release as a dev release.

[958.18s] The stable main release will be kind of coming to PyPI, uh, any minute now, but you can install the dev and play around with it if you want. Um, and so what do these look like?

[966.32s] So tasks are just like a row of a data set. Um, and the very basic version of it is, uh, you just start loading a data set from Hugging Face or anywhere else.

[975.54s] Um, and so the new pattern here is y- from verifiers.v1, uh, just to keep the old stuff separate. The old stuff still works just fine, but this is how we have been able to kind of decouple and iterate o- on the new version.

[987.40s] Um, as well as we've really embraced this decorator pattern. Um, we found it to very-- be very useful, but we also-- if you were a Rubric fan, we killed Rubric.

[994.84s] Um, didn't make sense anymore if you were using old verifiers Rubric patterns. Um, but still it's, uh, you have functions and loaders. Um, we are very heavy on Pydantic, so everything is super typed.

[1006.63s] Uh, we have lots of powerful config features where you can have everything in a TOML file, you can override it in the CLI, um, and everything is kind of clean and guaranteed to kind of type check at, uh, like, uh, a validation time rather than waiting for something to fail later down the road.

[1020.78s] Um, and so examples of this are things like SWE-grep, where you can do agentic code search. You can do the classic games like Wordle. You can do, uh, search over documents with judges.

[1029.50s] Uh, you can do, uh, complex things like Harbor that support, uh, a lot of popular benchmarks now that need, uh, agents running in a terminal. Uh, and all of these are gonna be combinations of the, the, the task set pattern with, uh, pick your own runtime and pick your own harness.

[1044.54s] Um, and so rewards and metrics, I think, are also kind of, uh, just functions that take in the kind of records, uh, of what's happened in a rollout and return numbers.

[1053.00s] Uh, so rewards are the main thing that'll drive progress in RL. Um, metrics are just kind of like logging, uh, what has happened, so counting tool use and counting errors.

[1062.26s] Um, these sorts of things are very useful to be able to expose in your dashboards. Um, and then group rewards. I think this is something that we have fought hard to kind of make sure still is first class because we see it as very important to, um, a lot of the research pattern people want to do, but

[1077.00s] I think is also ignored in a lot of like, uh, tooling out there where in s- in many RL frameworks, it's actually quite hard to do group rewards because things are very decoupled, and things kind of assume that all rollouts are gonna live independently and that they don't need to talk to each other.

[1089.64s] But there's a lot of things where you really want to do pairwise judging, or you want to do ranking, or you want to give a bonus to the, uh, the shortest correct answer, uh, in terms of tokens used.

[1101.21s] Um, and so these sorts of things are really flexible, uh, in terms of the-- W- we've really designed for flexibility in supporting the, the things that we see as like the most exciting papers we've read or all the algorithms that we think people may want to innovate on, um, while still allowing people to have like the core

[1115.20s] primitives that they kind of expect out of an RL framework. Um, and so like in group rewards, I think this concise-- this pattern is one that I find very useful a lot.

[1123.23s] I think, um, like a big pattern that comes up a lot when people are doing post-training is, uh, models will love to like think and think and think if you let them.

[1132.09s] Um, and if you don't give them some kind of pressure to like be more efficient, uh, I think a lot of people will notice that like open models often have really, really long chains of thought because on one hand, it's like this is a useful strategy for a model, but it's also the sort of thing that will

[1147.81s] grow like out of control if you don't counteract it. Um, and so in reward design, like one of the big things people will want to do is a-- something like a length penalty, um, or a conciseness bonus.

[1159.39s] Um, and so one of the reasons this is tricky is because you don't know the optimal length for a problem. Like if I give you a math problem, I could say, "Oh, solve it in less than N tokens," but also like who knows what the right N is.

[1170.59s] It's also gonna change as the model gets smarter over time. It's gonna be different for every problem. And so you kind of can't know this upfront, and the only way you can do it is take advantage of variance.

[1179.97s] And so one of the nice things about RL is you have multiple samples typically, um, and this allows you to use the fact that you have multiple samples to shape the reward.

[1189.81s] Um, and so if you have multiple rewards in a group, what you could do is, uh, look at all the ones that were the correct answer or just all the ones in general and give a bonus to the ones that are the most concise.

[1201.05s] Where if you also have a, uh, a correctness reward like these are going to, uh, ensure that, um, you're both incentivizing correctness as well as incentivizing efficiency. And so juggling multiple objectives simultaneously is kind of one of the hard challenges in RL and reward design.

[1217.59s] Um, but doing things like group level comparisons and kind of these sorts of bonuses are, are quite useful in many cases. Um, I also want to talk about like tools and user simulators, which I think have been, uh, becoming more important, uh, in a lot of complex applications where you have models that are-- in many cases, there's

[1234.29s] like a core agent harness. But there's also, in many cases, you are putting a model in a setting where it's gonna be in some task where a user is giving it additional tools, whether these are-- in some cases, you might want to model these as skills.

[1245.71s] In some cases, you might want to model them as MCP servers. We use MCP as a kind of a, a backend framework, um, that can interact with the runtime, uh, both for tools and for user simulators.

[1255.11s] So user simulators, especially if you want to do training where there's a, a user in the loop, um, you don't want just your agent to go do some tasks, but you want to be able to do some tasks that involves understanding how a user will interact.

[1265.87s] You can essentially have this user be an MCP as well, where we make it so the model sees it as a user, not as a tool. Um, but behind the scenes, it is a server that has some script or something, and it has some LLM that is gonna get some context, and it's gonna be able to be

[1281.83s] like a user in the context of a rollout. Uh, in many cases, benchmarks have found that this is very useful for simulating the realism of like having a multi-turn setting where there are users in the loop, especially given that people are building products now where there are these users in the loop.

[1295.20s] And so you want kind of a first-class way to incorporate this into, um, your, uh, your RL environments. And so we've found that it's useful to have all of these things be kind of modular and pluggable.

[1306.49s] And so, um, the harness can connect to each of these, which run as a, as a uv script. Um, we also have uv script support for grading in addition to the basic reward function patterns.

[1317.42s] Um, and we also are using this idea called an interception server. So the harness, we want people to be able to use real harnesses and not have to like break the harness and like retrofit it into like an RL harness.

[1328.93s] And so ideally, we don't know anything about the harness code. And so the pattern that we use with the interception server is that, um, w-we are responsible for giving each harness rollout a fake base URL, which could be OpenAI compatible or Anthropic compatible.

[1343.17s] The harness just thinks it's talking to some endpoint. So any harness that can just talk to some endpoint, we're good to go, and then we intercept each request. Uh, we can do some, some backend maneuvering to make sure that we're getting the log probs and setting the right temperature.

[1356.67s] Um, and then we send this to our, uh, inference server for-- with the RL trainer. Uh, and then as it completes, we send back the request. And so the, the harness doesn't know that it's doing RL.

[1366.85s] The harness just is a harness running as if it would be running in a real-world environment. And so you can kind of very easily move between the RL setting and the deployment setting where your harness is just code.

[1377.45s] It doesn't need to be anything specialized to verifiers or RL. We also have found it really use-useful to be able to kind of go from this like local to global and like have this hot swap pattern.

[1388.17s] Um, so we have this new like, uh, eval CLI where, um, you can just like choose the harness you want. You can have a task set where you're saying, "I'm gonna run an eval on this set of tasks.

[1398.45s] Okay, I wanna use recursive language models in RLM. I wanna use Codex. I wanna run it locally. I wanna run it in sandboxes. Uh, I wanna run it in Docker."

[1405.67s] These are all just like interchangeable. Um, and so we found that this is super useful in the iteration loop as you go from testing something out at a small scale towards scaling it up, towards being able to understand questions like what's the best harness for this model?

[1419.25s] Um, does this harness generalize across tasks? Um, as well as being able to both have the convenience of like local prototyping, where you can kind of run things fast on your MacBook, um, without having to like wait for a cloud job to finish.

[1431.77s] But also you can like go right to the cloud when you need to. And so there's been a lot of fun patterns we've had to kind of innovate on, um, as we've done this overhaul, and we-we're quite happy with how it's turned out.

[1441.79s] It's made our lives a lot easier for both client projects and research and just, uh, being able to have a lot more flexibility and power and control over the, the kinds of agents we want to be training.

[1452.21s] Um, and so one of the fun things behind the scenes, uh, is what we call the trace graph. And so we had kind of been having this grow out of control in terms of the old way of doing things, and we decided this was another opportunity to like really overhaul our system to like have really good support

[1467.71s] for sub-agents and parallel branching trees, while also still preserving the kind of linear sequential dependencies that you need for RL with, uh, careful token control. Um, and so here, uh, there's a, a notion of a, of branches that are kind of like at the message level.

[1484.25s] So conceptually, um, the things that matter logically in environment space and in harness space are messages, which are just text. Uh, the harnesses don't think about tokens. Uh, but if you've done any RL experimentation, you may have, uh, encountered issues where, uh, re-tokenization or, like, some messages-- If a model will say something and you turn it into

[1503.25s] text and you put it back through a tokenizer, it can change a little bit. The re-- 'cause tokenization is, is many to one. Um, and so this causes lots of very subtle numerical problems, especially late in large-scale training runs.

[1515.63s] And so you want a really nice back and forth between, uh, messages and tokens. Um, and so the trace data structure that we created here partly is to enable this, where we can, uh, store things both at trace level and then map them back into token level in the right sequences as needed.

[1532.94s] Um, and we also released a library called Renderers recently, um, which is a standalone toolkit that p- anyone can use, uh, that we have found the sort of thing that we're working with some of the inference tooling to, uh, support.

[1546.09s] So renderers are really all about, like, essentially rethinking tokenizers and chat templates, where behind the scenes, it's just making calls to the tokenizer. Um, but chat templates, if people have spent time debugging with them, it sucks.

[1560.25s] Jinja is awful. Um, it's very, very painful, and there's so many subtle things that we kept running into where, like, uh, a model would sometimes have an extra new line, and the chat template would strip it out, and this would, like, cause a mismatch in your trainer and inference that would either force you to go off policy

[1575.93s] because you now have a trainer inference mismatch, or it would cause a, a logical branch where a thing that is a branch in, like, uh... It becomes a branch in token space, even though it shouldn't be in logic space, um, because of tokenizer subtleties.

[1590.51s] Um, and so re-renderers as a, as an abstraction, it was kinda pioneered by, um, OpenAI's Harmony with the gpt-oss release and used, uh, prominently in Thinking Machines cookbooks as well for Tinker.

[1600.93s] Um, but we found it was useful to just kind of make it a standalone thing. And so this is just a Python library that doesn't depend on any other Prime stuff.

[1607.40s] Uh, you could use it with any inference engine you want, um, uh, just as a standalone thing that is really designed for being able to manage this token in, token out concatenation, uh, without thinking about it too much yourself, uh, because we kind of turn each of these chat templates for these-- the popular models into programmable artifacts.

[1627.83s] Um, where you can do things like, uh, look up a history of sequ-- uh, you can use the kind of history of a trace, um, to be able to understand, like, what is the right tokenization?

[1638.39s] Like, do I essentially have, like, a logical prefix hit in message space, even if I don't in tokenization space after re-tokenizing? And so this is the sort of thing where I think people have gone back and forth on, like, whether they want LLM APIs to be stateful in general.

[1652.39s] Um, I think a lot of people were hoping that, like, we could just have every model API be stateless. I think maybe people are less concerned about this now because we're moving towards this agent world where agents themselves are gonna be stateful APIs.

[1664.79s] Um, but I think this has revealed to us, like, going through all the, the things here, like why OpenAI Responses decided to be stateful. Uh, there are some kind of, like, unavoidable issues that kind of come up when you're doing, uh, large-scale agentic rollouts, uh, where you, you do need to kind of manage this very carefully, and

[1683.51s] it's kind of un-unavoidable just because of how tokenizers work. Um, and so you want to be able to maintain these dual streams of the logical text and the, the, the tokens.

[1692.67s] And you kind of want these to be cleanly interoperable, where users don't have to think about the tokens very much, uh, but the trainer gets to see everything nicely in token space, um, as well as the inference engine.

[1703.23s] Um, and so from the harness interception server, uh, we have clients that can be used both for training and inference. And so you can kind of like, uh, swap between these modes without thinking about it because, uh, certain models, like, don't need to...

[1716.77s] In, in a training setting, you need to be able to get log probs and set a temperature. Some model APIs won't let you do this. They won't return log probs because, like, OpenAI models with reasoning, like, won't show you the reasoning trace, so there's no way they can give you the log probs for everything.

[1729.05s] And so, like, that's fine. It's just eval only, and so we have this, this client layer where you can go between eval and train to be able to support all these models.

[1736.23s] But we still use the interception server pattern either way because it allows us to have, like, uh, this notion of a dialect where, like, you can choose, uh, OpenAI Chat Completions or Responses or Anthropic, and all of these are kind of easily supportable as just, like, translation layers between a raw request into something that'll get passed through

[1753.53s] a renderer, potentially, if you're on the training client side, and formatted into a, a message via tokens. Um, and so this brings us to PrimeRL. So PrimeRL is our training framework that is-- consumes the environment.

[1764.88s] So once you have an environment with your task set and your harness and your interception server and your runtime and your renderer and all those things, this plugs into what we call the orchestrator.

[1774.39s] And so PrimeRL has been async from the ground up. Uh, so I think async RL was one of those things that I think people were kind of one foot in, one foot out.

[1783.25s] And a lot of training frameworks, if you see them, uh, will still kind of support synchronous training. Um, some people, I think, have their reasons for wanting to do synchronous training.

[1791.05s] I don't agree with them. Um, uh, I think, uh, you kind of wanna bite the bullet of the off-policiness anyways for reasons that come up with agents, um, in terms of you want to be able to overlap long rollouts and not always be waiting on your slowest rollout.

[1805.50s] And this kind of means you can't be fully on policy unless you want to kind of accept always waiting on your slowest rollout. Um, and so this is really why we went all in on async.

[1814.38s] And so the orchestrator's job is to allow the inference and trainer to just be separate processes, separate servers. Uh, they don't share GPUs. They don't really know about each other all that much.

[1824.31s] They just consume from each other. Um, the-- But the orchestrator's job is to really, like, manage the run. And so the orchestrator, uh, will make sure that the environment is running with the endpoint mapping to the inference server.

[1835.15s] It'll do rollouts. Uh, it'll package these up into a batch. It'll send this back to the trainer, and it'll be up to the trainer to figure out what to do with the batch, uh, which will be kind of printing some, uh, sequence to feed into a loss function, um, based on the, the specification.

[1850.99s] Um, and so the, the server pattern we use for environments is just an engine that can, like, send requests to the inference and, like, send batches back to the orchestrators.

[1857.75s] It's very client-server. Um, and we found that this is just a really useful way to, uh, allow scaling concerns to be decoupled as well. And so, like, for example, you can have a lot of environments running, or you can have one environment running.

[1869.07s] You can have, um, a bunch of inference replicas. You can have one inference replica. Um, you can have- Sandboxes or no sandboxes. Uh, and the trainer doesn't care about this, the inference doesn't care about this.

[1879.23s] It's just separation of concerns at a system level, uh, allows you to kind of not really worry about these things as, uh, like, combined units versus like, in some cases, uh, people will want to, like, have training and inference on the same stack, where it's like, especially the, the closer that you kind of fold in your logic

[1895.33s] all-in-one, then it's like sometimes you can't even run your environments if you're not doing RL, but that means then you can't really experiment. You also can't use them as evals.

[1901.89s] There's a lot of reasons why just, like, pulling everything apart into these pieces and just, like, having nice APIs for them to talk to each other, uh, makes your life way easier.

[1909.49s] Um, and we've also just been, like, really scaling it. Um, and so we've been doing a lot of work on, uh, like GLM-5 series and Kimi K2.5, K2.6 series just to make sure that we can do, like, really good large scale RL efficiently.

[1923.57s] And so some results we found rec- we have recently, this was, uh, the run was on GLM-5 before the 5.2 one came out. It supports 5.2 as well.

[1931.53s] But, um, on the latest PrimeRL version, we can do, um, a GLM-5 step on twenty-eight nodes in less than five minutes for long horizon coding tasks with 131K context.

[1945.09s] Um, which means you can do a thousand-step run in three days, and that costs, for rental prices, about fifty K. And so fifty K is not cheap, but it's like if you're doing a full run on a frontier-sized model on, like, a proper real world agent environment, like, it's a lot cheaper than what OpenAI is raising for

[1965.83s] it. Um, it's a lot cheaper than, like, some of the clusters people are, are, uh, selling. And it's the sort of thing that, like, just starts making sense for a lot more enterprises if you can, like, actually do this.

[1974.77s] It becomes pretty justifiable if you can kind of get to the point where, uh, you have the, the tooling chain to be able to, like, build ready evals and, like, uh, do all this stuff.

[1983.45s] Um, and so this is like the sort of thing where it's like, let's say you do-- wanted to, like, you have a bunch of tasks that are, like, representative of, like, your coding workflows, and you wanna, like, do a big RL run.

[1991.47s] Like, this is a pretty big RL run, but it's also the sort of thing that, like, you could-- People spend this much on tokens in a month sometimes. Um, and so you can, uh, start finding a lot of savings if you kind of think about doing large scale post-training, and that's kind of what we're, we're here to

[2006.53s] help people do. Um, I guess more on the async side, uh, one of the reasons why you really wanna do async is that, um, there's a long tail of how long your coding agents take.

[2017.37s] Like, if you fire up a coding agent task, just like think your Claude Code or Codex tasks, like how many minutes is it gonna take you? Sometimes it'll be thirty seconds, sometimes it'll be like two minutes, sometimes it'll be a goal that goes for like f- three hours.

[2029.01s] Um, and these can all be rollouts. And so one of the goals of Async RL is to have your, like, forward progress speed not be tied to the speed of your individual rollout.

[2039.79s] And so this means you can kind of allow your rollouts to finish long after they start and just go into the first batch that they can accept them, even if that is from a much different copy of the model.

[2050.97s] Um, and so then the, the inference server is just always taking the latest version of the model. And so, um, what people have generally found and what we've done with our experimentation and found as well is that you can go reasonably far off policy.

[2061.71s] Like, I think sixteen is where we typically are often operating as like an average. Um, but this means that you just also can have a lot more room to not worry about certain things about speed.

[2072.41s] Like, you don't need to worry about the boot up time of your sandboxes as much, or the weight sync time, or like the time of any environment or your, or your grading.

[2078.81s] Like, it's, it's fine if you have these things that take time, 'cause you can't-- If you're doing, like, grading with a judge, you can't, like, force your judge to be super fast all the time.

[2086.84s] And so you want to have a system where it's okay if there are pockets of your life cycle that don't use GPU time, but do use time. Um, and you can kind of overlap these without kind of wasting GPU cycles.

[2098.69s] And so that's really the, the key benefit of, of Async RL in our eyes. Um, and we've done a lot of work on the loss function side. The DPPO paper is one that I think has gotten popular that we've been using a lot as well, of like, how do you make sure that this, like, stuff stays stable?

[2112.17s] Um, we found that it's very stable up to thousands of, uh, steps. Um, we're pushing towards ten thousand in kind of current experiments, um, in terms of the, the scale that we're trying to kind of get this stuff to reliably.

[2122.53s] Um, as well as doing this at big batch sizes where you kind of need to pull out all the bells and whistles on parallelisms. And so what we found is that, I guess I can go back to, uh, like doing like this, uh, expert parallel on the trainer as well as context parallel, um, and then on inference

[2140.01s] doing, uh, wide expert parallel for the big MoEs, uh, meaning multi-node, uh, experts across multiple nodes as well as de-disaggregated prefill. Um, and you can kind of throw all the inference bells and whistles that people would do for normal serving into your RL stack and get same wins there as well.

[2155.17s] Um, so here to kind of fully kind of recap all the, the advancements we've been pushing into the, the stack. We've been leaning in towards FP8, um, wide expert, wide DP, um, disagg prefill, lots of stuff at the routing and KV offloading and management of just kind of where things live, especially things like router replays.

[2173.23s] So router replays is actually a really nasty systems problem because it requires tracking a lot of metadata per rollout because you have this for every single layer. Um, so it's like, it's a big multiple over just the, like, tokens and log probs, uh, that you actually have to store, um, because especially with your mult- routing to multiple

[2189.65s] experts per layer. Um, and so the storage concerns for these as well as like for multimodal, um, if you have like images that you need to store, like there's a lot of stuff where you want to kind of offload the heavier artifacts onto some like object storage system or other file system, um, and not just have it

[2205.23s] floating around in memory. Um, and so we've rebuilt a lot of our systems to support this as well as just really pushing, uh... There's a lot of kind of like special cases that you need to worry about, where it's like certain models will want certain types of context parallelism, which have different considerations about what you can do,

[2220.19s] uh, in terms of like other aspects of the system. Um, and so we've just been trying to really refine the recipes for making sure that this works really well, especially for models like GLM.

[2230.45s] Um, and we've done this all on top of a TorchTitan base. I think a lot of people are like, "Why do you use TorchTitan and n- not Megatron?" Um, and it's because TorchTitan's just like really easy to like hack- And Megatron is kind of this monolith, um, that I think some people will hack it, but it's-- I

[2243.23s] think, uh, we just started with TorchTitan a long time ago and kind of find the pieces we wanna bring in, and especially when a new model comes out, it's like, well, you wanna train on it or you wanna-- Let's say you wanna-- There's some new paper that you read that, like, has some new idea.

[2255.15s] You wanna be able to, like, make everything really hackable and modular. And so, like, our, our team is not that big. Like, our whole research team that maintains PrimeRL is, like, less than ten people.

[2264.65s] Um, and the company is less than forty people. Um, and so there's a lot of work that we want to make sure people can parallelize, but also move quickly.

[2272.97s] Um, and so, uh, this is all stuff that we've kind of been able to, to figure out over the past few months as we've really been pushing it for scale.

[2281.47s] Um, another thing that's, I think, fun is algorithms. So I think a lot of what researchers care about-- I think researchers, some people will love thinking about the system problems of scale.

[2290.13s] Um, if you do, talk to us. Um, but if you don't, I think what a lot of people wanna spend their time thinking about is algorithms in terms of the on-policy distillation stuff or, like, OPSD or, uh, if you saw the Echo paper, I think that got a lot of people excited of, like, thinking about how you

[2303.27s] do world modeling with RL, um, and folding these in, as well as just basic stuff like SFT. Um, there's also this MaxRL paper from a while back that was super cool.

[2311.20s] And so we were just-- We were seeing all these papers, and we were like, we just wanna do all of these. We want it to be much easier to kind of, like, mix and match these and not have to, like, add another if statement buried super deep in the code, um, and, like, pipe a bunch of stuff

[2322.63s] all the way through. And so we kind of decompose things into the loss, which is, like, the thing that is taking the gradient, as well as the algorithm, which we say is the thing that's kind of, like, preparing the data.

[2332.53s] Um, and so we have different losses we can kind of, like, pipe things to, um, in terms of, like, the signal and the masking. Uh, and you can use these to kind of assemble, uh, different algorithms.

[2342.66s] Um, and so an algorithm's just like a class where you have-- You can have a class that does different things in terms of scoring or, uh, the groups. Um, and, and you kind of pick which loss you wanna target with it.

[2352.03s] Um, and so we support all of these, all the popular ones, and you can kind of add your own that look like adding in a function to, like, assign advantages, uh, to a rollout.

[2361.31s] Um, uh, yeah. And so then, then from your algor- then from your configs, you can just kinda say, "Hey, I want, like, this algorithm." And it's just going to pick one from the registry.

[2373.35s] You can add your own to the registry if you want. Um, and then this will be the algorithm used for your training run. Um, and you can do this on a per environment basis if you want.

[2382.11s] Um, but all of these algorithms that people are looking at kind of fall into this, like, table where there's questions about, like, what are your-- where are your rollouts coming from?

[2391.23s] Are they coming from your current policy model, or are they coming from some other source, like a teacher? Um, and so any p- algorithm people call, like, on-policy or, like, slightly off-policy in terms of the Async RL stuff, this is one where, like, your, your actor in RL sense is going to be the model you're training, your

[2406.14s] policy. Your policy is your actor. Um, in other cases, you're doing stuff where your, your actor is some other model. So if you're doing context distillation or you're doing SFT, like, these are ones where you are, uh, gonna have some other, like, model or a prompt potentially be the teacher that is generating the data that you're gonna

[2424.51s] be training on. Um, and so all of these kind of fit within this family. But then the other thing is the advantage. And so the advantage is just, like, if you generalize it to, like, a score, like, you can now call, like, just cross-entropy loss or negative log likelihood is, like, everything is, like, advantage one.

[2437.59s] Um, there's a lot of, uh, all of the, like, OPD algorithms can kind of-- You can kind of think of it as the log prob ratio as being the advantage.

[2444.75s] Um, and with RL, like, your, uh, your reward minus some baseline, usually group mean or something like it, is your advantage. Um, and so we just kind of, like, took a step back and looked at all these things, and we were like, "Oh, we can just kind of, like, factor this all out pretty nicely, um, and have

[2459.63s] almost everything else be shared." But these things get kinda swapped, and so your infra doesn't need to change just because your loss function needs to change. Um,

[2469.25s] and so for on-policy distillation, like, it's just plugging in with a different loss target, and it's, like, talking to the teacher and being like, "Okay, the thing I need to get is reference log probs from some teacher, and I already have my, like, sequences, so I just need to send these to a teacher as pre-fill in terms

[2484.35s] of, like, a-- Like, you can get pre-fill by just, like, asking for, like, a one-token response. Now I, I get my sequences, and I can just, like, stick these in as my reference log probs."

[2491.55s] Um, for self-distillation, you can have, like, a hint that you're kind of putting in before your, um, your, uh, like, this teacher. So you're not saying the same prompt.

[2499.61s] You're saying a different prompt, uh, using renderers to kind of, uh, pack these together. Um, and then you get back the same, like, sequence that you can then slice out, uh, into the original form, um, so that you can kind of add these as your reference log probs there.

[2511.43s] Um, you could do Echo, where you have, like, two different algorithm components. You could have one that is targeting the, uh, the doing cross-entropy on your environment tokens while doing, like, an RL objective on your, your action tokens.

[2523.77s] Um, and you can mix and match these. So you can have, um, uh, like, different, uh-- Like, you can ch- decide which teacher is gonna be do- your-- whether you're gonna be sampling from your student or your teacher.

[2534.21s] Um, you can, like, decide which algorithm you're gonna be using on a per environment basis. Um, and you can have, like, this one, we have, like, both, um, a normal, like, OPD as well as GRPO.

[2545.35s] Um, a-and then, ah, yes. So, like, this whole family we now support within PrimeRL natively. Um, and one thing you may also have poked around at or seen or tried is, uh, we have our hosted training platform, uh, which means you don't have to worry about GPUs at all.

[2561.87s] Um, and so this is just hosted PrimeRL. The version we have that is kind of the, the broad, uh, self-serve version today is multi-tenant LoRA, um, which is focused mostly on RL.

[2572.07s] Um, what we have coming quite soon that we'll be rolling out is full fine-tuning, um, which supports changing as much as you want in PrimeRL in terms of the model and everything else, where we still give you all the same abstractions for, uh, not needing to think about the GPUs and kind of auto-scaling and, uh, magic restarts

[2590.23s] and, uh, having a dashboard where you can log everything and have unified billing for sandboxes and judges and all these things. Um, but also you get to develop your environments on CPU, on your laptop, push them to the platform as environment packages, and specify them in your configs.

[2604.97s] Um, and then this allows you to, uh- Um, have a lot of flexibility in, like, deciding when you want to go to different levels of the stack. So in many cases, you don't actually want to change anything in the trainer.

[2617.35s] You just want to change your reward function, and you can do this in environment space. Maybe you want to configure the trainer but not change it, in which case you want to kind of poke into s- like, slightly more complex knobs for, uh, things like different loss functions or, or learning rates.

[2630.34s] Um, additionally, you may want to, like, actually go deeper into the trainer and like, uh, do new algorithms at the environment level, or the algorithm class level, or at the loss function level, or maybe something else entirely that needs going even deeper.

[2640.75s] And so we, we support all of this with the, the, um, the full fine-tuning as well. And so, uh, multi-tenant LoRA, if you're unfamiliar, is a, a very useful pattern for allowing multiple people to do training runs on the same architecture, um, on the same, uh, model weight copy.

[2653.92s] And so you have a base model that's kind of-- This is how all inference for, like, token-based pricing usually works, is you're doing multi-tenant inference where you have one big copy of Claude, uh, that is just getting everyone's requests and hitting a shared, uh, like, KV pool, uh, that is managed.

[2668.12s] Um, with-- This is really nice with LoRA because you can just have multiple LoRAs available that you can hot swap, and each person can have their own LoRA without needing to replace the base model.

[2677.06s] Uh, and you get one kind of inference pool that serves everybody at once, even if they're using different models. This allows you to do things like token-based pricing, uh, and not need to reserve GPUs.

[2685.22s] Um, for full fine-tuning, it kind of does have to be GPU-based, um, but we've been getting a lot more GPUs, and so we have the ability to let people run stuff on their GPUs.

[2695.26s] Um, and, uh, this allows going, like pretty-- like, going to full parameter training, where especially for algorithms like large-scale SFT or mid-training, um, you will want to kind of have more than just a LoRA adapter, um, as well as the ability to kind of really customize at, at every layer you might want, um, like how your algorithm

[2713.24s] is going to work. Um, but so we-- The multi-tenant LoRA one is already live, and you can go use it today. Um, full fine-tuning is coming out in the next coming, next couple weeks.

[2721.20s] Um, the V1 stuff from before is already, uh, out, uh, as a kind of a alpha feature that is a stable release coming in the next, I don't know, quite soon, hopefully.

[2730.68s] Um, and then the cookbook I mentioned earlier is also out. Um, and that's mostly what I want to talk about. Um, it's a bit informal, and I can-- if people have questions, I can, uh, dig into any individual parts people think are curious.

[2742.76s] We're also, uh, we're hiring. Uh, we are a small team based in mostly San Francisco, um, becoming a much larger team quickly. Um, and, uh, we'll have some other exciting news about that coming later this week, uh, to, I don't know, uh, demonstrate our commitment to scaling the team.

[2761.56s] Um, but yeah, we're, we're growing and we're, uh, I think in a unique position of, like, we do very open research work. Like, all this code is on GitHub if you wanna go play with it, but we also, like, are a real company that trains big models and makes money.

[2777.20s] Um, and so, yeah, I think we figured out a good business model to do real open research, and it's been an incredible journey thus far, and we'd love to have, uh, excited, passionate, talented people join the team. [audience applauding] [upbeat music]
