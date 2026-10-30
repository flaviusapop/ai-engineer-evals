# SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)

Source: https://www.youtube.com/watch?v=KMR_RBoCa4M

Uploaded: 2026-07-29

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/ff/ffc9b8b840748c80864a0ff28117ec283616d2014bbc3b1ebd5b7311e71d9cbf.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/KMR_RBoCa4M.json.

## Transcript

[on-hold music] Hi, everybody. My name is Shreya. I am the CEO of Snowglobe, and we have with us Aman, who is a principal machine learning engineer at Nu.

And this talk is gonna be about simulation maxxing and how you can ship or, or how Nubank ships, uh, agents twenty X faster using simulations.

Hey, everyone, I'm Aman. Uh, so let me talk about Nubank at a glance. We are the lead, leading digital bank in Latin America. We have a hundred and thirty-five million customers, uh, in Brazil, Mexico, and Colombia, and we are launching in the US real soon.

Uh, our quarterly revenue crossed five billion in Q1 2026. Our NPS, our customer love is very high. And we are the perfect company for using AI agents for customer support, where human experts are fanatical customer care people and AI agents together solve customer issues in a fast, empathetic, and correct manner.

AI handles, uh, a lot of routines end to end. Uh, humans focus on the hardest and long-tail cases, and together, we aim to delight our customers.

So as Shreya said, this talk is only about, uh, one thing really. If you generate your eval data in sim instead of waiting on production data, you can ship agents twenty X faster, and we'll give you evidence for that.

So let's start with the results directly. Uh, uh, so th-this is, you know, the average of TNPS, which is a measure of customer satisfaction for five of our AI agents in production.

And at the beginning, uh, they were not so great, but now, you know, with a few months of, uh, of work and a few quarters worth of effort, we've been able to massively increase the TNPS and customer, uh, love for our AI agents, and many of them are approaching human quality, and this data is a bit stale,

as many of them are exceeding human quality. So we are at the stage where we are actually able to show proof that this actually works in production. Uh, here is a QR code for our KDD paper in case you wanna check it out.

It's gonna be presented, uh, in Korea, uh, in August.

Uh, awesome. So we opened with results, and, you know, it's really about this journey of how do you implement the right systems, uh, for evaluation in order, you know, be able to achieve those results.

So in this talk, we basically split it up into these three sections. The first is why evals are so important and essential, but why they're also the bottleneck from being able to, you know, do a lot of high-throughput experimentation to get the results that Aman was showing earlier.

And then why s-- The second part of this talk is about why simulated data, uh, works as well as collected data and helps you circumvent a lot of this bottleneck that we're gonna talk about.

And then the third part is really digging deep into the systems and the findings that we had by implementing, uh, you know, this framework at scale in Nubank.

Uh, awesome. So evals, we know this. There's, there's like a whole talk track dedicated at this conference to evals. Evals are absolutely critical for building good agents, and evals are really only about two things, right?

There's metrics, and there's data. Uh, metrics, again, I hope you attended many of the amazing talks yesterday on the evals track, but metrics are really... W-while they're challenging, we have a playbook for how to build metrics that are really well aligned with, you know, the rubrics that we care about, right?

Which is you essentially use, um, you know, LLM-as-a-judge style, uh, you know, classifiers, and you align it with human judgment and, and getting human data, and you can iteratively build on it using, you know, auto optimization and auto prompt tuning, uh, techniques.

The thing that's a bottleneck and that still remains very challenging and unsolved is what is the data that you're actually computing these metrics on? And that process is very time-consuming and very expensive, specifically so for agents.

So once again, people have been talking about, you know, uh, if, if you're around, like, machine learning era circa, you know, twenty eighteen, it would be like ML work is eighty-five percent data work, right?

So data has always been challenging, but with agents, the level of sophistication that data requires is just so much more expensive. So here's examples, you know, of what structured ML data look like, uh, and what even early era of AI, uh, data for, you know, chatbots or single-turn QA, which was, you know, much more manageable and tractable,

and you could still think of it as these structured rows. Uh, but now for multi-turn agents, each data point is a trajectory with a lot of internal tool calls that all need state, et cetera, and that becomes very...

Even one data point is expensive to generate and annotate, right? But scaling it up on a sample set becomes even harder.

Um, so how teams primarily get eval data today is two methods. Uh, one is either manual, or the second is production traces, and both of those are painful, but for different reasons, right?

Manual authoring, I mean, this one's obvious. It is so time-consuming, especially the kind of data that I was showing you on the previous slide. You have to hand plan, you know, state updates.

You have to hand plan the trajectory that you wanna take this, uh, you know, agent data point in. And synthetic, uh, the, the state for these data points has to stay consistent across all tool calls, et cetera, that you make, right?

Production traces, in comparison, are almost free. You don't have to pay for them. You're gonna get them anyway. But the cost is that you're testing on real live users every time you're testing it.

So for example, if you wanna run, you know, many parallel experiments at scale, which is often something you wanna do in a machine learning settings, is it becomes very hard to do that in prod.

So for those of you who build agents, you know how difficult building a new agent and maintaining, uh, an existing agent is. So if you wanna change the agent harness, you wanna change the prompt, the tools, anything around the, uh, the LLM that powers your agent, that can take a few hours in, in, in the best case.

But as Shreya mentioned, running offline evals on hand-curated data can take a few days. And then the, the worst part is if you've done an A/B test in production and monitor regressions, see if you get a statistically significant improvement of, over a previous version, that can take forever because customer feedback is, uh, through some kind of a

feedback form, and it can be sparse, it can be noisy, and can take forever to know, am I moving in the right direction or not? So I'm here to tell you that, uh, we have verified in production that, yes, simulation circuit this timeline, short-circuit this timeline.

From a few weeks, you can go to less than a day, sometimes even a few hours, a few minutes.

And, uh, as I mentioned earlier, uh, you know, with simulations, it takes a few hours. Uh, uh, without simulation, it takes a few hours to change the harness and offline evals, and all of this becomes super fast.

Now, with simulation, the agent harness change still takes a few hours. Running offline evals becomes a lot easier because you have a simulated user to fall back on. You're not waiting on hand-curated data.

You're not waiting on, you know, people to create data for you. And the best part, if you wanna know, uh, that am I doing well in production? Is this version gonna do well?

That can take just a few hours. So this has been a real game changer for us at Nubank.

Um, all right. So we talked about, you know, like, simulation shortening the release cycle, but what is mechanically a simulation? You know, it's existed in robotics, it's existed in, you know, a lot of different domains.

But simulations for agent evals, you know, mean a specific thing, and this is really where Snowglobe enters and, you know, sets up a lot of that core infrastructure for you.

So simulations are essentially, you know, it works by first, like, wrapping your agent, you know, using a, um, a... Like, pointing the, uh, Snowglobe SDK at your agent without requiring any code changes.

And, you know, you can grok what are the tools that you really need and, uh, to mock in order to make the simulation really work. The second input is about how you wanna drive or steer your s- your simulation.

So, you know, who are the personas? What are the use cases? What are the data points that we're really simulating? Once you have those inputs ready, Snowglobe essentially runs the simulation, and on the output, you end up getting, you know, first, just a dataset.

So you get, like, thousands of multi-turn conversations against your real agents. These conversations have, you know, tools, mocked, et cetera, have all of the bells and whistles needed to be actually, you know, useful for evaluating your agent already ready.

And then you run, like, judges on top of it, so that on this dataset you get, you know, per turn information about how your agent is really behaving. And it then, like, pipes directly into, you know, your evaluation pipeline so that you can really get data on demand.

Um, this is an example of what a si- what the, what, what a concrete output of simulation is like, right? So this is, as an example, like, one simulated persona, and then the corresponding conversation or data point for that simulated persona.

So here, for example, this is totally synthetic, a user named Maria Souza. Uh, you know, she wants to order a credit card. This is who she is. She's [REDACTED:age], a designer, first-time credit card customer.

In addition to, you know, this basic information about this synthetic user, we also generate, you know, this essential grounding data. As an example, this fake address, a fake credit card, et cetera, that stays consistent across your agent execution so that, you know, your agent can actually be evaluated against that.

And then you also have things like tone, voice, how do they really interact? And then... Oops. And then when you actually run this persona through the con- through the agent, you end up getting, you know, this, uh, conversation that's consistent with the simulated intent, right?

So you see, for example, that this user has very curt one-line messages in terms of how they interact because this is how the persona was set up. Or that, you know, when the agent wants to...

When the agent runs its tool, when Maria enters the chat, the agent is actually able to get a valid output mocked by the simulator that, you know, is able to identify who the user is, where the address is, the address can be verified, et cetera.

Um, and then finally, all of this is also grounded in, like, account data as well.

So for those of us building real agents, you know how hard things are. Uh, you don't know if your agent is good. You don't know if your evals are good.

You have no idea what's happening, and that was me a few quarters ago. Uh, since the theme of, uh, this year's conference is self-improving agents, so we are also kind of jumping on the bandwagon.

So this is our, uh, self-impr-improvement loop. You ship your agent, you observe, you create robust evals. We have spent a lot of time creating robust evals using automated prompt optimization with algorithms like GEPA.

And then you also do simulation. You run simulation, and you pipe the simulation data and real data through your evals, and that gives you rich signal to then optimize your agent harness.

And once you verify that agent harness, uh, optimization is good, you ship. And this has enabled us to do many, many, many A/B tests for a given agent, and we have many, many such agents across the company.

So this has been a real game changer for us in terms of improving our agents. And the proof, as I already showed you, is that, you know, the quality of our agents is going up, uh, pretty dramatically.

This is some data on how simulation really tracks real production data. So when you run, uh, simulations, you want to compare, is my simulation comparable to production data? So we looked at sim quality, uh, via evals.

So for, uh, you know, quality of, uh, with evals from sim and real data, the correlation is pretty high. And we had human review done, where eighty percent of our domain expert labels confirmed that sims give us usable data, not just for, uh, mature agents, but also for greenfield agents.

So this has been, uh, pretty useful for us in bringing up a new agent from scratch and also taking an existing agent and, and massively improving it.

And as, as we, as I mentioned, you know, simulation is not just about improving, uh, and Shreya also talked about this. We are de-risking a lot of things that could have made to production.

For instance, we caught a regression, uh, with simulation that could have made it to production, but simulation caught it. And at the same time, we also caught, uh, in another agent an issue, uh, which could have lowered our self-service rate, making it less efficient.

And all of this has resulted in pretty large improvements. Uh, for instance, one of our agents, the TNPS, has two xed, uh, thanks to simulation, robust evals, and investing in something super principled rather than, you know, throwing something at the wall and see what sticks.

Um, it's been pretty awesome to see simulation saving us so much time. So now the team uses Snowglobe and tries different ideas, and they're able to short-circuit launching A/B test.

They don't launch until they're happy with sim output. So imagine if you're running ten A/B tests a quarter for your agent, or probably more if you have more data.

Now you can just run a bunch of stuff through sim and launch just one A/B test, which kind of short-circuits launching the first five or six. And at the same time, uh, this, this is often discussed in, uh, customer service circles, that TNPS can come at the cost of self-service rate.

Sometimes there's a trade-off. But I'm happy to report that we are not compromising on self-service rate. With sim, we are also able to pretty dramatically improve SSR across the board.

But in one particular case, we were able to improve it by four percent. All of this makes us a much more efficient company and makes sure that we keep our customers really happy, and we keep our SSR rates and TNPS rates very, very high.

This is one example that I am most excited about. As, uh, you know, you, all of you know, open source models have been on a tear recently. So many of them have come out.

So we've been trying to test various open source models in our agent harnesses and see which ones are the best. And with sim, we have the perfect recipe to just throw a bunch of ideas, open source models at our agent harness and eval and sim setup and see which model versions, uh, you know, really, really work for

us. Uh, this has saved us multiple weeks of effort. I'm probably underselling it. It's, it's been, it's been pretty awesome. And, uh, we have A/B test running, uh, as I speak, uh, figuring out are these open source models as good as, you know, uh, the, the frontier models.

So sim is, is, has been super, super helpful in helping us figure out, uh, kind of, you know, uh, spreading our cards, uh, a bit.

Um, awesome. So, um, the core three takeaways from this talk, right, is about, um, where eval is today and how you can really remove a lot of bottlenecks to it.

So we lied [laughs] when we said earlier that there's just one thing you should take away from it. That one thing is still essential, but there's a, a few key downstream things that you can unlock if you know you adopt it, which is, the first is if you generate your evaluation data in simulation rather than solely relying on

production to get signal on how, you know, different agents are performing, uh, you'll be able to undercut or you'll be able to short-circuit a lot of the, uh, bottleneck in, in releasing, you know, uh, versions of your agents much faster.

The second is, in order for any of these gains to really be unlocked, uh, you know, you really need to close out the sim-to-real gap. So you need to s- you know, set up like offline, online human review kind of metrics to really understand how sim performs vis-a-vis real production da-data that you've seen, uh, so that you,

you, you are able to kind of like trust the results of these simulations. Um, and the third is, again, there's so much excitement around, you know, like auto research, self-improving agents, RSI, et cetera.

Uh, in an enterprise setting when you're building an agent, it really does come down to two things, data and metrics. If you have aligned metrics that are able to really catch the signals you care about, and you have a reliable way of generating data that th-those metrics can give you signal on, it's then very easy to put

together a loop of an agent that, you know, continuously improves itself from, like, feedback it receives from all of these places, uh, which, you know, again, is, like, where the future of this field is heading.

Um, awesome. That's, that's us. Uh, thank you for coming for the talk. Uh, there's a few, like, contact links and details for us, you know, if you guys wanna get in touch, and otherwise we'll be around here if you guys wanna ask us any questions. [outro music]
