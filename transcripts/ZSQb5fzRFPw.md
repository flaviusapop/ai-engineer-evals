# Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

Source: https://www.youtube.com/watch?v=ZSQb5fzRFPw

Upload date (publisher UTC): 2026-07-15

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/6d/6d64e8ed917963311dc5c0bc1800ca1c4605c5e1383735b46f6d77160b724a22.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.22s] [upbeat music] Thank you for taking the time for coming over here.

[17.08s] Um, I'm Francesco. I'm the CEO of the company. Uh, alongside me, a couple of other folks, um, my CTO, Dillon, and my chief of infra, Rob. They're gonna walk on the stage in a while.

[27.22s] Uh, but before we do that, who's excited for some computer-using agent talk happening now? Are you guys excited? Lovely. Um, if I were to ask, like, what, what was a computer-using agent like one year ago?

[39.36s] Probably half the crowd would say, "I don't have any idea what really computer use mean." Um, so, um, today I'm gonna take you to a journey, um, basically like from our vision where, um, we come from so far on computer use, um, like this new shape of like agents that are talking, um, and, uh, up to

[64.30s] model intelligence. Um, so we're gonna start like with the vision of, uh, Cua Driver, where we're coming from. And, uh,

[75.62s] if you-- How many of you guys have been work- have been working with computer use for one year?

[82.46s] How about like three years? Lovely. Okay. So our team has plenty of experience. Like we go all the way back, uh, our time on Microsoft. We were working on this type of GUI agents we were calling them, uh, back in the days.

[96.78s] Um, and, uh, there is a, um, there is an example of like old-fashioned human, uh, agent loop. Um, we basically refer, um, refer this as, uh, human, uh, loop, where you will have like an agent loop.

[115.22s] You will have a, um, uh, you will take a screenshot that the agents will have to reason and plan through, and then, uh, um, you will basically work with an action space, uh, in terms of like clicking, typing, scrolling around.

[127.40s] So this is what we refer as, uh, as, um, um, the old-fashioned like computer use 1.0 just to set the tone for, for, um, for this talk. And, uh, we come like a long, um, a long like way since, uh, this type of like, um, computer-using agents.

[147.24s] 'Cause this is, this is again, like I'm gonna skim over these slides, but that's like the old-fashioned way of like representing this agents loop as a human would do.

[154.70s] Um, we, um... Here we go. Um, over like two months ago, we released a project in open source. It's called Cua Driver. And, uh,

[171.64s] um, we, we, um, we made it working like in the background. That means that your computer user will ta- will not take over your, uh, screen as like the computer use p- 1.0, um, kind of like agent loop was doing back in the days.

[187.56s] And, uh, um, it all like started from, uh, um, from like a, um, from Codex rel-releasing their computer-use, um, model, uh, two months ago. So we kind of like take the challenge because we were really like working with, uh, these, uh, this type of background computer use.

[206.69s] So over one weekend, uh, we hack something together, and, uh, the trick here is really, um, not like having your agents like take over your screen. So there is a lot of like dark magic like happening behind the hood.

[220.18s] Just to, uh, give you some context, uh, there are like some undocumented API, um, living in, uh, um, in the Apple framework and basically ships with your laptop. And as you can see here, like is in the demo, you have like an AI agent, uh, that is not taking over, uh, control of your, over your laptop.

[238.82s] Um, we made it working not only for macOS but also spanning like across Windows and Linux. We were-- Uh, this is like the very first like driver that is, uh, living on your, um, laptop and, uh, it lets, uh, really any AI agents connect to the underlying operating system, uh, either like using accessibility trees or like a

[260.84s] screenshot-level approach. We kind of like take all both.

[266.68s] Um, this is what really the agent sees for what it concerns. Um, you will have to install Cua Driver. Um, the agents will, uh, will take a snapshot of the window state, and, uh, you will have to observe.

[280.06s] Um, and, uh, we really like take, take like one, uh, like different like a, action path to really make background computer use happening. So you really, um, have, uh, to observe the space.

[294.84s] Uh, in this case, uh, just by calling like getWindowState, you get, uh, an accessibility tree representation plus a screenshot. And then, uh, you will go and, uh, um, try a background execution using accessibility tree, and if that doesn't work, we go all the way and, uh, make the heavy lifting for you and just try a pixel background

[316.30s] click. This is like, uh, kinda like best step for background at this stage. It's not like behaving the same way on macOS, Windows and Linux. So, uh, we, we do like some of the heavy lifting for you so that your AI agent can, uh, can run undisturbed on your, uh, on your MacBook.

[334.98s] Um, how we manage like to not break anything between like release cycles. We have ex- We have like a lot of investment happening, uh, behind the scene, uh, when we test like new releases.

[349.06s] Uh, we have about like eight different f- uh, application harnesses that, uh, are, um, that, that, that we, that we use for making sure that we don't break anything, uh, among different releases.

[365.66s] Um, among our early adopters, you can see, like, Cliqi, Hermes, Quancode, H Company, and, uh, DroidFactory. Uh, like, huge thanks to them for using Cua Driver and, like, um, basically releasing a lot of, like, upstream contribution, like, in, uh, in our framework.

[382.46s] Um, without further ado, I'm just gonna move to the next part of the presentation, which is gonna be intelligence. Um, and I'm gonna have our CTO, Dillon, uh, cover that.

[394.84s] Hello. So thank you, Francesco. Um, with Cua Driver, we gave an agent hands. But then the question becomes: How can you trust the agent to use those hands correctly and not leave anything broken behind?

[406.53s] And to answer that, we had to build Cua-Bench.

[409.88s] So for a show of hands, who here has heard of Terminal-Bench or Harbor?

[414.96s] Yeah, so a few of y- few of you have, have heard of it. And, uh, if you've ever authored a task for Terminal-Bench, then this might look familiar.

[423.06s] But in Cua-Bench, a task is made of three pieces: The setup function, which sets up the machine into initial state; the oracle function, which provides a golden trajectory for the task; and the evaluator, which probes the environment to check if the agent successfully completed the task.

[441.80s] Uh, unlike Terminal-Bench, the oracle here is, uh, GUI actions, so it looks kind of like PyAutoGUI when you write that.

[451.20s] And writing environments takes skill and expertise. On desktop, there's more than, uh, five platforms that we target, and, um, we try to collapse that into a single Python file.

[463.32s] So using the Cua-Bench SDK, you can write a GUI that works across every desktop platform in a single Python file and use the same SDK to probe that GUI to get usable agent data.

[475.52s] Anyone or any agent can author one of these tasks.

[479.64s] And when you put that to work, you get a real catalog. We have currently over 130 verifiable tasks, 42 environments, and across five platforms, and each of these are easily reproducible using our CLI.

[493.30s] And the latest addition to our datasets is one that we're proud of. Uh, with collaboration with Snorkel AI, we built Cua-Bench KiCad, which tests computer-use agents on electrical engineering tasks using software by real professionals and evaluator functions that actually simulate the circuits.

[514.02s] But the results are humbling. The top agent that we tested only got a full pass on six out of 25 of these tasks. Of those six, 100% of them involved editing an existing schematic.

[526.72s] And when we start the task from a blank schematic, the success rate drops to 0%.

[534.38s] And across all the models that we tested, the leaderboard is flat. No model has achieved more than 30% reward.

[544.96s] But once you can score something, you can improve it. If we take a look at the Cua-Bench basic dataset, scale it up to 4K resolution, uh, testing an agent, they typically get around 62% pass rate.

[558.14s] But when you switch the agent computer tool from the built-in one to Cua Driver, the pass rate jumps from 62% to 80% using 34% less tokens. And this is primarily because Cua Driver focuses on a window rather than the entire desktop.

[574.96s] But our evals might say you can trust model XYZ at task whatever. But how can you know that the task-- How can you know that the eval can be trusted?

[584.44s] So before we test a task against any agent, we first try to break the environment ourselves. We have a matrix of agents attempt to do reward hacking and attempting to break the environment, and we take all that data and we compile it into a nice CodeRabbit-style code review.

[602.22s] And only tasks that survive our pipeline can enter the dataset. And if you ask us how we trust that agent, the answer is that it's just evals all the way down.

[612.68s] But to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions. You also have to measure its ability to understand the world that it's operating in.

[622.90s] Every run that we record can be forked through any moment in its trajectory to give you the state of the computer at that moment. From there, we can probe a model asking to predict the reward, the internal state, or any other observation of the computer and compare it against the fork.

[641.50s] And that prediction is the world model of the agent made measurable. And with that, um, I'll let Robert take the stage.

[650.62s] Thank you, Dillon. Uh, hello, everybody. Uh, I am the chief infra officer at Cua, and I'm here to talk to you about, um, how you're probably leaving a lot of money on the table, uh, with idle GPUs if you do RL training, uh, for computer-use agents.

[667.86s] So I kinda wanna introduce this, uh, diagram to y'all. Uh, can I get like... Is, is there, like, general familiarity with this diagram, or is this, like, something that most of us haven't seen before?

[678.91s] Like, any- anyone? Awesome. Very niche. Um, almost everything on this is not really important for what we're talking about, but the blue portions are. Um, and what those basically represent are GPUs, uh, generating tokens for, um, RL, uh, training.

[697.30s] And if you zoom in on this a little bit, you can kinda see, like, how this typically looks, like, with a sandbox environment, is you're gonna be generating some tokens, um, and then you finish your task on a sandbox, and then you're waiting for either, like, a new sandbox to spin up or for your existing one to

[717.12s] reset. Uh, the problem here is that, like, this is just pure cost. Um, your GPU really isn't doing anything useful here. And, you know, I don't know if you've heard, but GPU time is pretty expensive right now.

[730.07s] So, um, as you're scaling, this cost really compounds a lot, and you really wanna focus on minimizing this if possible. So one thing that you might try to do is, uh, minimize the startup time of your sandbox, and I mean, you should do that.

[747.35s] Like, that's a great thing to do, but, uh, you know, especially for computer use style environments, sometimes this can be a little bit impractical. Um, you know, your researchers might give you like a forty-gigabyte environment, and that might just be necessary, and it takes a long time to pull that down and start it up.

[763.97s] So, you know, how do you, how do you design your training infrastructure so that you can minimize the GPU startup or the minimize the startup time of the sandbox, uh, even when the sandbox is like not well designed to be start up quickly?

[780.37s] Um, so the way we do that... Ah, man, is it not?

[786.07s] So the way we do this is a p-pool, and this is supposed to be animated, but it's not animating. So, um, I guess I'll just explain it to you orally.

[796.17s] And what, what that is is, uh, so we have like a, a set of GPUs here which all want to use a sandbox. And what we will do is that we use a demand-based autoscaler to detect, um, how many GPUs, like, currently need a sandbox, and we can grow the pool to be that size, uh, on demand.

[818.85s] And what that means is that, uh, if you have... Let's say like you have a warm pool that you wanna allocate to your GPU cluster, you don't actually need to know upfront what that warm pool size is.

[830.07s] We can figure out what that warm pool size should be for you, um, on demand. And that might even change over the course of your multi-day training run. Uh, you might start needing a lot of sandboxes, but then as your generations get longer, you might need less.

[845.55s] So these also could be like, you know, easily, uh, two to f-four times cheaper than your GPUs. So having a little bit of redundancy here, uh, you still wind up saving money because you're maximizing the use of your GPU time.

[861.69s] Um, yeah, come see me after if you wanna see the animation 'cause it's, it's cool. Um, so yeah. So now when you have like this like, uh, redundancy in your pool, you're paying the cost of that startup time on the infrastructure side, not on the GPU side.

[878.68s] So your GPU workers have full utilization. Um, yeah. And then because we use this, we can give you instant sandboxes for your GPUs for Windows, Windows, Linux, Android, uh, and macOS is coming up.

[895.53s] Um, and I'm gonna hand it back to Francesco to, uh, close it out for us.

[902.93s] Lovely. Uh, thank you, Dillon. Thank you, Rob, for taking this over. Um, we do have like plenty of time for Q&A, so if you guys like have any questions, like happy to, um, take them either for Cua Driver, Cua-Bench, basically what Dillon presented, or Cua Fleet, uh, which is like what, uh, Robert covered.

[930.37s] Any questions? Otherwise, we can wrap this up. Oh, I see.

[935.15s] Would it be possible to operate like, uh, computer-use agents in the background? I know you do this for Mac-

[941.23s] Mm-hmm

[941.55s] ... but like in something like, uh, uh, mobile?

[944.55s] Um, so the story for mobile, Android, there is very far you can go. Um, we are talking with the Hermes team 'cause they do have like an harness that runs on Android.

[955.87s] I guess like if you're talking about background, there is some level of like background that can happen if you containerize a workload and basically on Android you can even like run your own container or like sort of like Ubuntu or like GUI Docker container, uh, within An-Android.

[974.11s] Um, but yeah, the Android ecosystem, especially compared to iOS, is more inclined to that form of like background, uh, computer use, but it's more towards like tool use than really like controlling GUI interface.

[987.83s] Um, we work with the activity framework and, uh, do tool use, uh, in the background.

[998.03s] Thank you.

[998.59s] Cool. Thank you, guys. [audience applauding]
