# Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI

Source: https://www.youtube.com/watch?v=48YUYDjwfYY

Uploaded: 2026-10-02 (publisher uploadedAt UTC)

Transcript source: Full corrected publisher transcript at https://ai.engineer/talks/48YUYDjwfYY-stop-rationing-tokens-let-harness-pick-model. All 54 source segments preserved with timestamps; machine-source-reviewed corrections may contain errors.

## Transcript

[0:13] All right, guys. Very nice to meet you all. My name is Laurent. I'm the co-founder and president of Cast AI, who is the inventor of Kimchi, which I'm going to show you in a few seconds. Um, the talk is going to be about proprietary models for edge case, but use open source for the rest, and you're going to see some great result we have with that with the coding agent called Kimchi. I have the pleasure to be here with Žilvinas.

[0:38] Hey, guys. I'm Žilvinas. I am leading engineering for, uh, Kimchi coding platform.

[0:42] So you have Žilvinas who run the entire engineering team for Kimchi. I'm so excited to be here with you. All right, let's go. So, um, you ha- you may have seen this in the news, uh, two, two piece of information that came up in the last few weeks. The first one is there's a company in India that spent five hundred million dollars on Anthropic alone in one month, which is again of a good example of tokens that are completely out of control. The other example is a famous tweet from Uber, the CTO of Uber,

[1:12] who say that in the last four months he actually used the entire budget of Anthropic for the entire year. And this is how much the token, um, the token maxing or the token cost is a thing for the enterprises. And you're gonna see how we fix this. Companies responded this by limiting the use of token. You may have heard this many, many times with our friends, developers. And as a developer, when you limit the amount of

[1:42] token, it feels like this. It's like, "Hey, you can use your laptop. You have an hour battery, and you can only charge once a, once a, once a day." That's how it feels to limit the amount of token for a developer. We at Kimchi think this is wrong.

[2:04] Our jobs as manager is to do the opposite, is to ensure that we want to make the tokens unlimited and inexpensive. Our job is not to prevent the developer to use coding agent. Our job is to make sure they can use it as much as they want for as long as they want in a completely unlimited fashion. This is why we started Kimchi. At Kimchi, we have three hundred developers.

[2:35] Oh, sorry, three hundred employees.  Two third of those are developers that Žilvinas run that, and we've been using this coding agent for the last three months. I'm going to show you what we built, how we built it, and the result of it, and then Žilvinas will show you a few more things that make the coding agent really, really cool.

[3:00] It's coming now. We built an entire token optimization based on this idea. What you see on screen is the true cost of LLM model for the same task. It was made by the famous white paper in a university. And here's what they say. On one side you see the cost per token. On the other side you see the cost per task for the same task

[3:30] with the same quality. That is the important thing. Otherwise you cannot compare apple with apple. And here's what is written here. First, they are all different, but also look at Gemini 3 Flash, our, our friends at Google. What it seems to be a relatively inexpensive model at three point five dollar per million token. It's a blended average at the time this study was made. But actually the task to complete with Gemini 3 was three hundred and five...

[4:00] Sorry, seven hundred and five dollars. And look at the others. MiniMax M2.7 is one of my favorite. The cost per token is one point five and the task-- the ta-- the cost for the task is one hundred and forty-eight dollars. It means the models are not the same. They don't cost the same, but they're also not the same per task. And that's why we built our coding agent. Would it be nice that you have an automated

[4:30] fashion, automated engine, automated harness that will select the right model for the task at the right time based on the outcome of the task? That is what we did with Kimchi coding. That is what Žilvinas did with his team. And here is the result. We've been using it for three months. Two point five times is the amount of savings we have over Claude for the period. This is a graph of what would

[5:00] have been our Claude bill by day. The purple one on top is what would have been Claude cost over time. The blue line is what we paid.

[5:17] Same outcome. But look at this. The number of tokens increased by one point five times. Okay, we all experienced that. The cost to Claude decreased by one point five times. This is our job as managers. We provide to our team a coding agent that is essentially unlimited because of that coding agent is growing three X less, two point five times less

[5:47] than the growth of token for the task. There's another result. The multi-model I showed you before. I'm going to show you the evolution of the selection of the model over time by the harness. And here it looks like. You see there is a lot of orange early June, and there is a lot of yellow late June. There's a complete shift, meaning the harness is

[6:17] selecting a very different model. It happens the 12th of June,

[6:23] and this is what happened the 12th of June. The fir- 3rd of June, Kimi, Kimi K2.6 is winning by far the most popular of the harness. 21st of June, the one winning is MiniMax M3. Us as human, probably we can find and understand and test and be comfortable with a new model coming in. Do you think we look at this as human? Absolutely not. But an autonomous harness, an

[6:53] automated coding agent that is obsessed with token cost, is going to do just that.

[7:03] That is what I mean when I say our responsibility is to think about providing our developers with the right cost per token for the same outcome. It is our responsibility to do it. Žilvinas is going to tell you a little bit more of how it works. Because whatever you're going to see, it's open source. Go, Žilvinas.

[7:30] Okay, so one more thing to mention. So Laurent mentioned that, uh, token maxing is no longer an option for everyone, and, uh, as a manager at the company, as, uh, most of you guys probably heard, uh, having unlimited amount of tokens to spend is no longer looking to be, like, a case. And, uh, we had to build this, uh, harness for ourselves. So meaning, like, we ended up spending too much on Claude Code. Like, half a year ago, we saw this, uh, cloud bill skyrocketing, and we started working on our own harness. Behind the scenes, it's using,

[8:00] like, pi-mono as SDK, but, uh, the goal of that is, like, to take the open source experience, still contribute back to open source by providing, uh, our own harness as open source. Building constructs c- like, uh, Ferment, which fits into the Kimchi theme, which is meant for long-running tasks, where on average, we estimate the human-in-the-loop for these tasks is, uh, typically happening only, like, every two hours, every th- three hours, and et cetera. So the goal is, uh, you use Kimchi harness, you run the a Ferment process, uh, it asks you a bunch

[8:30] of questions, and autonomously runs a coding task for, like, more than two hours. The goal of that is that because it breaks it into milestones, it knows how to implement it, and at the end of the cycle, you would get scoring for your output, so you would actually know what's happening. And going back to previously discussed, like, the amount of, uh, models used with, uh, Kimchi harness, uh, the scoring is there to prove you that, uh, whatever model we will pick for you, you will always have, like, a good enough scoring for the output on the task you're implementing.

[9:01] The way whole Kimchi platform works, uh, the goal is, like, uh, we are not just providing you the coding harness, we want to provide you the full co- software development life cycle solution. So you do a change, it runs a build for you, it checks if something broke. If something broke, it will go back, uh, do a change again, rebuild again, and that's, uh, how this fermentation process looks. If everything is complete, uh, there is no extra remediation needs to be done, the changes will be deployed to the staging environment.

[9:31] You see, what, what I like with, uh, the way Žilvinas explain it, is the harness select the model, Ferment is constantly checking the quality of the code and going back, meaning there is a, a higher order model that is checking the quality and thinking, "The quality is not good enough. Please do it again." This is what I was saying earlier by it looks at the outcome, and it's optimizing the token based on the quality of the

[10:01] outcome. That is what is super cool with Ferment.

[10:04] Yep. And artifact is only considered complete once, like, the output of the scoring are likely at least a B as a score. And even for that, like, if you don't like the score, you can ask agent to go back, fix it up, and, like, it will try to achieve a A as a scoring.

[10:21] The intention of stopping at the staging is currently by design. We still believe there is, like, some little human that needs to be in the loop before going to the production, at least at this point. We all know that the ultimate fu- future is to avoid that. You go to production, you look at the metrics, you look at the observability data, the SLO metrics you have in your environment. If you're running on Kubernetes, you want to check if the pods are not crashing, if application health checks are passing. So all of these things need to be done, uh, before it ship it- ship to production

[10:50] automatically. So this is, like, one of the things that are coming. So the current limitation, we stop at staging, but, uh, they'll go to production and, and further when that...

[11:01] What we believe is that reading code is not enough anymore. So, like, uh, probably most of you noticed, like, across this year, like, uh, the more wide engineering or agentic engineering we do in our coding environments, the more code changes we get on our change sets, and it kind of becomes unbearable to read, especially as you keep bringing, like, a little bit of a less technical personnel into your pipelines. So imagine, like, product manager doing the coding or my dear colleague Laurent starting to do some coding, and suddenly he comes up with

[11:31] a PR which is, like, uh-  ... 2,000 lines long, and, uh, you need to actually review not just the differences, but the actual intent which he wanted to achieve and the specifications wh- which he provided to the coding agent. So yeah. Moving on. Uh, one thing we built more on top of that is, uh, the thing we called Kimchi Teleport. So Kimchi Teleport allows you to close your laptop. It spins up sandbox in the remote environment. It's a secure sandbox where you don't need to care about anything. We can do that both

[12:01] on our SaaS platform. We can ship it to your on-premise deployment if you're, like, a financial technology company and, uh, things like that. So we will manage agent sessions for you. We will make sure they are running, they are accessible both from your laptop, from mobile device, if they are running in the background. So it goes back and ties to the story where I mentioned that the human-in-the-loop is only appearing, like, every two or three hours. So Teleport emphasizes that. You run your process, you teleport it to the remote environment, VM spins up

[12:31] in the background. You don't need to care about it. We will make sure it's the right size, it's the right security requirements, and everything else, and it will keep on running until the task is done or until the human in the loop, uh, needs to be involved, get notifications for some clarification of specs and, uh, things like that.

[12:48] Guys, I really like this idea. Look at the... This. This is a screenshot of Teleport. I am puzzled that sometimes innovations are always the simplest one. Like, this was born out of the idea that one of us was in the plane coding, and then Wi-Fi breaks. And what do you do when Wi-Fi breaks? It breaks the coding because it lives inside your thing. No, I thi- I think it was not the Wi-Fi, it was the battery that broke.

[13:19] Not the Wi-Fi. So you lost... So y- that's it, the guy was stopped there. What Teleport does, it detects all your environment, it synchronizes with a container that live inside one of the hyperscaler, in our case it's Google. And locally on your laptop, it feels exactly the same. It just doesn't run inside your laptop. It feels like it. It runs somewhere else, in your environment, in a

[13:49] container, in a community's cluster inside the place at Google, that will continue running even if you close your laptop. How simple that is, and yet our favorite tool is this one. I think the, the last one I, I, I looked at, it's 62% of our engineers are only using Teleport when they are coding now for that problem. They go home, it continues. They're in transit, it continues. They're on holiday, they don't look at

[14:19] it anymore, it continues. That's so cool, huh?

[14:23] Yep. So there is more to that. So we built another to- tool called Kimchi Studio. If the Teleport is something, uh, typically individual uses, Studio is kind of like a Teleport for teams and enterprises. The goal behind the Studio is, uh, that you have this kind of like board on your environment. It again runs in the Teleport sandboxes in the secure environment. The thing here is, like, you're supposed to share your tasks and work in progress, and plans which are made by the Kimchi coding harness with open source or

[14:53] proprietary models with your teams. So for example, imagine you as an engineer, you are, like, working on a task. Uh, you started implementing, uh, asking for a plan. The plan can be easily reviewed by your colleagues, like by your peer engineer, by your product manager, or someone else who cares what's happening. And this is how you kind of work with your whole team on collaborating on this agentic engineering journey, instead of like saying, "Oh, I'm gonna type this prompt. I'm gonna try to execute it to the production," only later on to learn that the specification and requirements were

[15:22] incorrect, uh, the output is not what was actually wanted by the task, and things like that.

[15:28] And this is yet another thing we built for ourself. We find it so cool, we decided to make it a product. How do you work with your colleague if what you have is a c- is a, is a terminal, a CLI? How do you share that with the others? Well, first it has to live somewhere else, so Teleport is the base of what we call Studio, and Studio is a very nice way to visualize all the sessions that are

[15:58] running, including those that are asking for a review. And then someone in the teams can say, "I take it," and I answer the, uh, I, I answer the question that is for review. Then you answer it, it goes back to in progress until the next one goes into review. And you can have many, many of those in a team, in a pizza team, a team of 5 to 10 guys. Think about it, a yet, yet a very simple innovation

[16:28] that is so essential in how our engineers are coding. They can now share in a very simple way, right? It's a, it's a browser. It's graphical. They can share, and they can take over the task according to the Kanban style of what is in review, what is in progress. They can start new ones with backlog. And you know what? If they close the laptop-

[16:53] It still works

[16:53] ... it continues. This is so cool.

[16:57] Yep.

[16:58] This is really cool. Thank you. Uh-

[17:01] Yeah. You forgot to show this-

[17:03] Another, oh, this is-

[17:03] ... Kimchi.

[17:04] This is the one that we took over, right?

[17:05] Yeah.

[17:06] That's the one. Guys, you can see this at our booth if you want to, uh, to see more of it. We are in UG4. It's exactly this way across a few streets. But have a look at it. It's really good. It is open source, most of it, at least. The harness is entirely open source.

[17:23] Yep.

[17:24] Uh, Studio and Teleport, you need a Google account, so it's a little bit more comm- uh, m- more complicated, but it's a, a five-minute install. And then you get your Teleport set up, as many sessions as you want inside your Google account, and then you can share with, share it with your colleagues with Kimchi Studio. So come see us. We'd be delighted to speak to you. Thank you, guys.

[17:48] Thank you, guys.
