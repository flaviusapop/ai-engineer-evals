# Perception Agents — Antje Barth, Amazon AGI Lab

Source: https://www.youtube.com/watch?v=2JX6JYyQG4Y

Upload date (publisher UTC): 2026-07-23

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/b5/b5f49fe6c1c1f6116f81271baea8f673a8db0929d51a6d693818e18e83f67b2e.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.22s] [upbeat music] Joining us on stage is a member of technical staff at Amazon AGI Lab, Antje Barth. [upbeat music]

[36.32s] Good morning. It's so great to be back here at the AI Engineer World's Fair.

[43.76s] Just a year ago, the hard problem was getting an agent to find a button and click it on a screen, especially screens it had never seen before.

[57.46s] Now, agents can drive browsers, and they're starting to also drive desktop apps.

[66.59s] But what we figured out, clicking, clicking, was actually the easy part.

[76.00s] What we didn't solve is the actual work.

[80.82s] And what do I mean with this? Let's take a very simple example. A new team member starts on Monday, and maybe your job is to set up their accounts, add them to a Slack channel, book intros with colleagues, order the laptops, et cetera.

[100.74s] And nobody really owns this end-to-end process in the company,

[106.32s] and it might be also touching five different systems.

[111.18s] Now, agents can most likely perform each single individual, individual step of this workflow.

[119.74s] But agents still struggle to do this end to end because the real work lives within the seams of all of those different applications, of all of those different steps you have to take.

[132.98s] And this is mostly where it all falls apart.

[137.52s] The agent can use every single tool you give it, but it still can't do the full work.

[146.88s] So why do we see this gap? Think about for a minute what we actually built.

[154.26s] We taught computers to use computers. So what do I mean with this? We started building out the basics. We taught them clicking, scrolling, typing, calling an API, filling out a form, and we got those stops-- these steps really reliable, and you can string them together in a workflow.

[177.32s] And agents these days are fairly good at, like, operating those workflows.

[183.78s] So why can you not just hand them more of your work and then literally just walk away and trust it to be completed?

[194.96s] So all the things I talked about, like using a tool, models itself, tool use, stringing agents together, this is all capabilities.

[207.72s] And we mostly figured out how to add capabilities to models. Now, the next hard part is really reliability.

[218.13s] And without reliability, we cannot really build up trust in those systems.

[225.30s] So here's a quick gut check, and maybe all of you can just think about an agent doing work in an end-to-end workflow. How often do you think that actually succeeds these days?

[239.54s] Maybe sixty, maybe eighty percent of the time?

[243.89s] And it sounds really fine. But if you look into this,

[249.92s] if your agent one in four times deletes a database, you will never touch that agent again, right?

[259.40s] So when you need this reliability, you really need to be it in the nines. You need to have the trust that it actually can do the work successfully.

[276.00s] Now, there's actually one place where we made enormous progress on reliability and trust, and this is coding, right? Think about how fast coding evolved.

[292.22s] I still remember the first time when it started auto-completing for you, right? You just tapped auto-complete, amazing. Then short time later, it started to write functions, and we thought, "That is amazing."

[307.32s] And now look at these days, coding agents write the code, they open up the pull request themselves, and we heard it earlier this week, code keeps flying by.

[319.26s] So once in a time, we were able to just every single line that it generated, we felt like the urge we need to really read it and make sure it's correct, right?

[329.28s] I think most in the audience here can still relate to that.

[333.38s] These days, I think hardly anyone is still doing that. Like, we cannot even do that, right? Code is generated at such a pace.

[343.40s] At the same time, coding made the jump, so why is that? Because we were able to bring it from just being capable, the coding agents, to actually be reliable and then trusted.

[359.72s] So why is that? Why was coding first solved?

[364.81s] It's because code is verifiable. You can run it, you can test it, you can check it, and you can be for sure that it worked.

[376.67s] So reliability showed up in the first place. You can actually verify the answer.

[387.95s] But here's the catch. Most of the work we do, if you look at the broader knowledge work areas, it's not like that.

[397.39s] Knowledge work is messy. And heck, the whole real world is really messy.

[404.85s] Did the report I created land? Is the design on brand?

[410.53s] Did it get it what I actually meant? So there is no unit test that can answer those questions.

[419.11s] So verification really hits the wall right where most of our work lives.

[425.67s] It's living in the seams of all of those applications we're using on a day-by-day basis. And nobody really has cracked this part yet.

[435.27s] How do you make an agent reliable when there's no way to verify the answer that easily? And that's a field that is still wide open.

[449.49s] So how can we solve this? Well, so how do humans handle messy work? I mean, we're successful at it, right? Each of us, like, every day, we work across different systems, we manage out how to onboard a new colleague.

[464.63s] We do this. Well, we're doing it by figuring things out together. You grab a colleague, you jump on a Zoom meeting, you're discussing things, you're looking at the problem to solve, you're discussing pa-pa-pointing at systems, and maybe two minutes later, you solved it.

[486.03s] You're done. But none of this work is actually directly verifiable.

[492.83s] And we do this all day. So one of the things is we're looking mostly at the same screen, right? If you're jumping on a meeting with a colleague, you see the same screen, both of you, and you can actually, like, figure out really quickly what needs to be done.

[511.17s] So this is what the agent these days is missing. You don't necessarily need a bigger brain. What you need is this shared context, because if we're looking, the agent and myself, at the same screen, I probably have much less explaining to do.

[533.65s] So what kind of agent do we really need to build to achieve this?

[539.63s] And today's agent, as I said, they can already see a screen, right? And they can click and take actions in it. That part works. But if they fire off actions, what they usually do, they move on.

[553.57s] They don't watch what happens or recover if one step didn't succeed or something goes sideways.

[562.17s] And we need an agent that can actually work like you do, like humans work.

[568.93s] And one example is robotics. If you just look for a moment as how robotics do it, a robot perceives what's around it, and it plans what to do and then acts.

[582.97s] So this loop here from perceiving to planning to acting, this is actually what we also would need on a screen.

[593.45s] And it starts here really with the first word, which is perceive. The agent has to take in the screen the way you do.

[604.19s] Not scrape the code behind the page, but what's actually rendered. The layout, the state, what just changed, the work, what we're doing, and then do it.

[620.43s] And it would also have to keep up in real time. Think about how we as humans work together. You jump in, you react to build on top of what each other you say.

[635.33s] And today, agents can still don't do it. What we're doing is we're sending a prompt, we're waiting, it goes away, and at one point the agent come back, and we might have to take a couple of turns, right?

[647.25s] Because what the agent come back with is not exactly what we might wanna do. So we're sending another prompt, say, "Hey, go back, do this, do this differently." And we have this long back and forth, which we got so used to from our chatbot experience and from this rhythm taking turns.

[665.31s] But what we actually would need, think about it, is an agent that can react while you're still working. Wouldn't that be really cool, right? Like at the same time you're working, it can also come up with suggestions, can help you, and there is no waiting time.

[685.59s] So basically an agent that perceives what you perceive and understands what you mean.

[696.37s] We call them perception agents. So why perception agents? Why do they matter? So first, they complete the loop on computer use.

[712.25s] Today's agents, again, they can act. They can click, they can type, they can scroll, but what they can't do well is looking at the results and whether it actually worked.

[726.30s] A perception agent can read the rendered screen, so it can confirm its own output instead of just firing off those actions and then hoping.

[739.56s] Second, it doesn't need an API or backend process,

[744.70s] and that's important because it works off the rendered interface. It sees the same pixels and the structure you see.

[752.86s] And most of today's software people use every day don't expose APIs at all.

[761.10s] And then third, the input also goes the other way here. Instead of writing a long paragraph to describe what you wanna change, let's say you're working on a website, and you wanna describe all the changes you wanna apply.

[776.92s] Instead of writing this really long description, wouldn't it be great if you can just point to it and say, "Hey, here, this heading needs to change. Hey, can you update this section?"

[789.48s] This is a much more precise signal and less lossy than text,

[795.62s] and the agent can act exactly on what you marked.

[803.62s] So this is where we started, and I'm happy to share that we just recently launched the first two pieces of our perception agent harness,

[815.96s] open source. There's two pieces. There is annotation, which you can use to tell it what you want.

[825.46s] And then the second piece, the verification part, gives the agent the capability to check its own work.

[836.78s] So let me show you the first one. So here's a very quick demo on our annotation tool.

[845.40s] This one is a Chrome extension, so it's super easy to use, and I'm gonna play here this quick video demo.

[853.52s] So you have the extension installed, and then you can just select different elements on a screen. So this example, we're just drawing around the heading there, marking the section, and maybe you wanna change it.

[866.68s] Why not? Let's change it to red. You could also select the elements on this page. You see how if I hover over, it finds the right element. You click it, you select it, and say something, maybe double the font size.

[881.12s] And you see also how the agent here captures on the screen exactly the feedback, the location, the style elements, and it creates this complete summary, which you can then use and then give your agent to implement.

[896.00s] So there is no back and forth anymore because you captured exactly what you saw on screen, and the agent can see the same thing.

[907.84s] Now, let's have a very brief look at the second one, at verification.

[914.52s] So the idea of verification is that you can describe, let's stay in this case of the web development. You can describe in a design.md file what your design rules are for this.

[929.12s] And then what happens if I play this video here, the ac- the agent can actually check its own work against those design specs.

[938.94s] So it will take what you defined, the colors, the components, your layout, and it turns it into those rules if you don't have it written before yet. And it does two kinds of checks then.

[951.58s] It does a visual check, which is really cool. So everything is on brand, for example. It's the right layout.

[960.74s] The other part is also checking user flows. So what it does there, it actually walks through this experience, through the app, for example. Depending on the tasks available, it might add a task, it might delete a task like a real user would.

[977.86s] So it helps you walk through those user flows as well in an automated fashion. And then once it's done, it's writing a report which you can review, and it's gonna call out which tests passed, and it's gonna tell you anything that didn't.

[994.90s] So ultimately, you're the one that doesn't have to click through this at midnight at the end of the day because, great work, the agent already did this job for you.

[1008.04s] Now, there might not always be a screen, right? So I talked a lot right now. I called it perception. I talked about the agent sees what you see on a screen.

[1020.92s] But there are times in your day where you don't have a screen. Maybe you're in the office, you're walking into a meeting with a colleague.

[1031.70s] So I did a fun experiment yesterday [chuckles] at the conference here. So I grabbed my colleague Giovanni, who's also here, and actually on the [REDACTED:location], there's a great, like, little meeting booth.

[1042.62s] We found that by coincidence. So we went in there, and we had our design meeting. And the goal here is to really kind of show you how perception is so much more than just the visual part.

[1055.42s] So in this example, what we wanna show you is perception can also be listening in the room to what you're discussing. And you can see here on the picture, both of us are wearing our Bee devices.

[1068.40s] Big shout out to Bee for [chuckles] sponsoring these. Um, so we're sitting there. We have our Bee devices that can do a transcript. They're listening to what we're saying. And then we have this design meeting, and I had a couple of great ideas how to change this website.

[1083.84s] Um, you will see them in a, in a second here. So let's have a quick look how this changed the same workflow on this website using this device.

[1095.96s] So we had the discussion, the Bee did the transcript, and you can see here on the right, we're pulling this meeting transcript right in. There is a whole detailed summary of the meeting.

[1109.52s] There is what we discussed, and then it basically captures those insights. We have them right here, and we can click Apply. So what this Apply button does is it sends it straight to the agent.

[1124.04s] And you can see here my crazy idea is to turn the background to yellow, turn the heading to red, and also change the emoji directly applied. And it also straight kicks off the verification right away.

[1136.96s] So it creates this report and, and luckily this color scheme was apparently into-- in the approved rules. Otherwise this would have flagged like you did some weird things here.

[1147.20s] But again, you could change those rules if you don't wanna have yellow backgrounds, and it will make sure, um, that we still adhere to those guidelines. It would flag anything that's off.

[1157.22s] So you have the judgment call if you wanna either update the design specs because you actually like yellow, or you take an action and say, "No, um, fix this violation."

[1170.16s] But this is really the very first step. These two pieces are the very first beginning, and we're building out the rest in the open because these patterns can only get better if more people are using them, building on top of them, breaking things.

[1188.72s] So my ask here to you is go and try them out. They're on our GitHub repos, open source. Tell us what we're missing. Give us the feedback, what you would like to see, where this should go next, because ultimately none of us get smart alone.

[1206.66s] And that's the whole point. We wanna build AI that makes all of us smarter together.

[1216.22s] Now, if you're interested in a little bit more on human-agent interactions and how we see those patterns changing, I would highly recommend this podcast by my colleague Danielle Perszyk.

[1229.94s] She is a cognitive scientist and runs our AGI-- HCI team at the lab and discusses a lot about human-computer interaction patterns with experts in the industry. You can find the podcast on, on a popular podcast platform.

[1246.74s] We also have more sessions this week, um, so check them out. We have a booth down there. We have expo talks. We also have another computer use track talk coming up with my colleague Gaurav Mishra at one thirty in the computer use track.

[1262.10s] Highly recommend checking out his talk, From RL to IRL.

[1268.52s] And then ultimately come find us. We have a huge presence down at the expo hall. We would love to continue the conversation with you all. If you're not here in person, you can also check out our code on our GitHub repo and check out our website.

[1284.64s] And with that, thank you very much. [clapping] [outro jingle]
