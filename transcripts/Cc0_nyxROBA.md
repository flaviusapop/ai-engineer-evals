# From RL to IRL — Gaurav Mishra, Amazon AGI Lab

Source: https://www.youtube.com/watch?v=Cc0_nyxROBA

Uploaded: 2026-08-14

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/74/74dcbcf14eb6ce5e44daa7cfb3e8535f12496d22696f7ad4494260e91e803d75.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/Cc0_nyxROBA.json.

## Transcript

[on-hold music]

Let's begin. Um, the topic for this talk is RL to IRL, and for those of you who didn't get the clever wordplay here, I'm gonna talk about what breaks when agents trained with, uh, reinforcement learning are deployed in real life.

This is me. Uh, I'm a researcher at the Amazon AGI Lab. Uh, I work on training agents that can do anything a computer can-- uh, anything a human can on a computer.

Uh, before this, I've spent more than ten years at Google, the last six of them at, uh, Deep, uh, Brain and DeepMind training language models and agents.

Let's start by talking about RL. Lightning review of what RL is and how we use it in the context of training agents. So when we train, uh, a, uh, an agent with RL, the agent is our policy.

We give it a task, we sample generations, and then we, uh, compute a reward on the whole generation, and that's how it differs from SFT and pre-training, where you're, uh, assigning loss to every, uh, token prediction.

And then we have different algorithms to apply that, um, uh, reward and update the model weights. We have PPO, GRPO, but many, many other variants. When is RL effective versus SFT?

Uh, three characteristics. One, when domains where, uh, you can collect or generate tasks fairly easily, but it's very hard to collect demonstration data for SFT. That's one where RL is very effective.

Uh, when tasks have multiple correct solutions or many ways to get to the correct solution and the outcome is verifiable, but if you try to collect SFT data for all the different paths, you might not be able to, or you might, um, narrow down the model to following a few patterns only, which is not good.

And third is, uh, reasoning-heavy domains, where again, it's very subjective. You want to, uh, let the model learn how to think and only judge it based on the outcome.

So if you think about it, coding fits this paradigm perfectly. That's why we've, uh, been able to train really compelling coding agents, uh, using RL.

Um, what are the key components of RL? Three in my mind. The first one is the task. This is the problem that we give to the model to generate samples on.

The task has to have a verifiable outcome. The task has to be really targeted to the skills that the, uh, that we are trying to, uh, teach the model, and it also has to be in the right difficulty window.

If the task is very easy or very difficult, then we're not gonna get much training signal out of the model. Second part is the environment. Now we are asking agents to produce code, to produce actions, and we need to be able to have safe environments where the actions and code can be executed.

And so code sandboxes are a big part of this, uh, system. And then the last part is the verifi-verifier, which, you know, produces the training signal. So taking model responses and judging them.

The judge can be something as simple as a string equality, uh, to compiler, linter, running unit tests, database lookups to, uh, also, uh, agents which are given a set of rubrics and then are asked to grade the model responses.

So when we got really good coding agents out of RL, what people started realizing is that you can actually deploy coding agents in the real world and ask them to st-- do stuff beyond coding, like reading emails or sending chats or filing receipts for you, or doing, uh, research on a topic, you know, surfing and searching the

web. Uh, and that's because, uh, all of these tasks can be represented as code, as coding tasks. So chat, email, docs can all be, uh, accessed through MCP or API calls.

You can interact with the browser using Playwright, JavaScript, WebMCP. You can surf and search the web using, uh, web search APIs. So in theory, coding agents can be really good at computer use.

So what's the catch? Uh, this is where real life kicks in. Uh, so let's see what breaks when the reward function meets a real login screen. I'm gonna show you a couple of demos.

Uh, to give you a bit of context, these are, um, these are trajectories from our web browser use training runs. Um, these are from the early stages, so we will see some common traps that our agents fall into.

Uh, there is the prompt at the top. The verifiable outcome is over here. Uh, here's an excerpt from the model thinking, and this is the browser window that the model sees.

And here, uh, we have, uh, we have a very simple task where the model is asked to enter, uh, and submit an expense. Um, let's see what happens.

Okay, it enters the amount successfully. It clicks the button, but we are actually signed out now, so it needs to sign in. Um,

let's see what it does. Okay, it says, "Credential expired, but I can infer the account password." So it doesn't really know the password, but it's trying to guess now.

Okay, it entered something. Didn't work. Uh, password was likely close. I will generate another password. Not going in a good direction.

Okay, still it failed again. I will resolve this without handoff. Let me try another one.

Uh-oh, the account is now blocked. Okay, let's take a look at another example.

Uh, same situation, uh, small difference. There's, uh, a, uh, an ad over here with a Submit button that looks very similar to the actual Submit button. Very common scenario that we have seen probably every day.

Let's see what the model does. I think you already know what will happen here.

Model enters the right amount. It, it looks and just clicks the wrong button. Now we are in a different website, and it starts filling personal details. Now, one can only hope that it is now hallucinating these details, but very dangerous, uh, behavior, and we don't want this.

Okay, so what went wrong? Uh, a big realization has been that RL worked when the world was a game, and IRL starts when the game fights back. So let's-- We saw a few, uh, challenges.

Let's talk about them and a few more challenges when you actually deploy, uh, agents in real-world a-applications. The first one is partial observability. So in the, in the demo, the agent has access to the screenshot and the DOM, uh, but neither of them are actually complete sources of information.

The DOM has some info, but it doesn't have, uh, content that is dynamically generated. It didn't have the, uh, sponsored content for the ad because it was embedded into the image.

The screenshot has it, but the screenshot might be partial. There might be content that is-- that you need to scroll to reveal. And so the model is, uh, being fed all these sources of information and doesn't really know what to expect from each and what to pay attention to.

That's a big problem. Uh, irreversibility. Once you submit a form, once you delete a file, once you lock an account, it's often irreversible for the time being. Non-determinism. When you click a button, um, you don't really know what happens.

It might work, but it might, um, take a long time to load. Your internet might be flaky. Your computer might restart for an up-up-upgrade. Uh, so many things can go wrong.

Ephemeral authority, uh, this-- the thing that we saw, the session expired. Very, very common. Uh, credentials expire very often. You have to be able to handle, uh, those navigat-- um, those, uh, those edge cas-cases.

Ambiguous success. Um, done often doesn't mean successful. If the agent filed a s- uh, uh, expense report for me but also sent a resignation letter on my behalf to the CEO, it is done, but not what I wanted it to do, right?

Um, adversarial content. This is-- Everything we see around us is designed to grab our attention, and we are-- we have to train ourselves to navigate that, and the model that is now working on our behalf also needs to be able to navigate that.

So these are just a few challenges. How do we, how do we, how do we adapt to this? Uh, our big learning has been, uh, that, um, for computer-use agents and to use a, uh, a helpful analogy here, we need flight school, not just exams.

So the, uh, the agent has to be able to give in all these edge cases. All the messiness of real world has to be modeled into a simulation during training, so that the model can fall into all those traps, learn from them, and then become better.

So it's not just producing a generation that is, uh, rewarded by a reward model, but it's actually the environment and all of the training setup has to reflect the messiness and all the edge cases of the real world.

And it also means upgrading the pilot and the cockpit. So let's talk about each of those components. The first one is a flight simulator. As we talked about, the first and biggest requirement is that we need high-fidelity digital sandboxes.

So we have to train with all the messiness, train with the layout shift, the slow loads, the missing labels, pop-ups, focus stealing, a- random account states, stale tabs. And then recovery also has to be a n-native model action.

So a lot of, uh... Often, during traditional RL, what we do is when there's a infra error, we, we just reset the state or ask the model to just restart.

But that's not an option in real life. So what we do is we, uh, whenever we have an infra error, we pass it to the model, and we expect the model to recover from it using native tool use, native actions like, you know, refresh, backtrack, compare, wait, abandon, escalate to the user.

Uh, third part is the process reward model. So as, as we talked about, the outcome is very important, but the path the model takes and the impact it has throughout the trajectory is very important as well.

And so we focus really hard on making sure we catch all of these dangerous actions throughout the process, not just the outcome, and penalize that accordingly.

One o- one other really important part is calibrated confi-- uh, confidence. So the-- we need to teach the agent to know how actions, uh, are risky and when it is, uh, supposed to escalate to the user.

So based on if the action is authorized, if it is irreversible, is it visible to the user, what impact it has, we need to teach the model to know when to go for it or when to step back and escalate to the user.

And the last part is adversarial tasks. So we saw a couple of very simple ad-adversarial tasks in the demo where the, the training environment, uh, tests the model in two particular ways, um, that, that models can make mistakes, and this has to be part of the mainstream training.

It, it cannot be something that's a byproduct. You have to actually test the model during training to, uh, make mistakes and then learn, learn from them so that it does well in production.

Let's talk about the pilot, the model. What needs to change? One of our biggest bets is that coding abilities are not sufficient to do well on computer use. Uh, the model needs to be able to s- look at the screen the way we humans look at a screen and then make sense from it, and that, that means

a few things. Uh, computer, computer screens are very dense, so grounding is really important for the agent to be able to understand what is the layout, what, what, what-- where are the buttons, where are the text, what does all of it mean?

And then the semantic understanding of it, like what is the purpose of the different things, what to pay attention to for the task that it's trying to do. Uh, change detection is also important.

So what we do is, after every, uh, action, we take screenshots, and we keep putting it in the model context. So the model has access to all these screenshots, but it need-needs to understand what are the changes that are happening.

Are they desirable? Uh, what needs to change? And then what is-- what's the, uh, plan, and what are the actions the model has to take going forward? And then the multi-source observation part.

So m- Having all these incomplete sources of information, but then learning to know what to expect from each of those, and then figuring out what to pay attention to for the task at hand is a important step.

So all of these capabilities need to be baked into the model.

The third part is the cockpit. Um, this is the harness. Uh, harness is a very overloaded term, but I think of the harness as ev- the interface between the model and the world.

Uh, so all the context management, all the tools, uh, that are available to the model, all the, uh, tool execution, everything is handled by the harness. And we can put an additional layer of guardrails in the harness to, uh, prevent the model from doing something bad, and then also nudge it in the right direction when needed.

A few things that we have baked into our harness are checkpointing and rollback when possible. So if there is a risky state, uh, risky action checkpoint, and maybe come back to it if possible if there's a bad action.

Uh, action risk classifier, this is another layer of, uh, protection. So if [clears throat]

looking at the proposed actions from the models and then figuring out if they're actually safe or if they're, uh, risky. Credential guardrails, again, s- like, it's easy to detect if the credentials are active, if we have been signed out, and then nudge the model in the right direction based on that.

Uh, similarly, execution monitor, looking out for any bad patterns from the model, loops or repeated clicks or un-unproductive behavior, and then nudging it in the right direction. Uh, audit logs, so maintaining evidence of all the actions and effects so that we can always go back and see what was the trail, what happened, and what, what was the

effect. And then human handoff. So wherever the confidence calibration of the model is not correct, we let the harness override the model and force it to give control back to the user. [coughs]

All right, so quickly summarizing the, some of the assumptions of, uh, traditional RL, how reality differs, and what we have done to adapt to it. So the assumption is that state is observable.

The reality is that UI is partial and messy. Uh, we've introduced per-perception primitives to deal with that. The assumption is that actions are cheap. Uh, reality is that actions are-- can be irreversible, and so we have to b- focus on risk-aware execution.

The assumption is that reward is clear. Uh, reality is that success is often ambiguous, so we have to focus on audit and verification. Uh, the assumption is that failure resets.

Uh, the reality is that failure is often persistent, so we have to focus on recovery policies. The assumption is that environment is passive. In reality is that content can be really ad-adversarial, so we have to set the right, uh, trust boundaries.

And the assumption is that autonomy is always good. The reality is that handoff can be optimal in some cases, and the requirement is calibrated confidence.

Okay, with all of this baked in, I want to show you a trajectory on a s- on the same, same task, uh, few steps down the RL training loop.

So same task. You have to enter the final amount and click Submit. Uh, now you'll see that the model, uh, I see two Submit buttons. One is sponsored, so the model is now able to distinguish between the two buttons.

That's great. So it clicks the right thing. Now we sign out. We see the sign-in screen. Now it says, "I see a sign-in screen. Credentials expired, so the task data should not go here.

Next, I'll hand off to the user." So now it's giving up control to the user to f- uh, enter the password, sign in again, and then give the control back to the agent.

So now [coughs] we have a user simulator agent that is gonna enter the right password and then sign in, and now it gives control back to the agent. The agent says that we-we're back on the expense screen, uh, with the amount preserved.

Sign-in is complete. Next, I'll submit the expense.

Okay, amazing. The last message I want to leave you with is that the difference between a demo and a product is what happens after the first click, first failed click.

So all of the things that we talked about today is essentially boils down to simulating reality in your training setup, and that can only happen when you actually deploy the product and let it fail.

Uh, so what we do is we work really closely with our design partners and internal customers, uh, to get them to use our pro-- uh, use our model and see what fails, and then, you know, complete the loop and fill in those capabilities.

And early on, our harness is really strong. So harness has to detect all the gaps in the model and make it fail gracefully so that we are able to capture the, the failure modes and train on them, but we also are not, uh, causing any harm to the users that are actually using the models.

And over time, the model becomes better and better, and the harness becomes thinner and thinner.

Okay, that's all I have. Uh, I'll hang around outside if you have questions for me, or, uh, if you'd like, please come by the booth, uh, the Amazon AGI booth to meet me and my awesome teammates, uh, will be there, uh, today.

Great. Thank you. [audience applauding] [upbeat music]
