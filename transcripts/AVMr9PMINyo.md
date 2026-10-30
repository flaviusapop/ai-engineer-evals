# Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It — Dan Fu and Olive Song

Source: https://www.youtube.com/watch?v=AVMr9PMINyo

Uploaded: 2026-07-31

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/40/405a8260d9c0eb2c0b9891a7aa3a95272786bed29ff958c00d4903621a5dc931.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/AVMr9PMINyo.json.

## Transcript

[upbeat music] This is a discussion that I'm particularly excited about because the field is moving so fast, and we have two people that, that kind of have this unique vantage point on the field.

And what I wanna do is kind of ask questions to see if we can learn from that. So, uh, I wanna start off with intros. Talk a little bit about your role, what you're thinking about, what you're working on.

Maybe Dan, if you can go first.

Yeah. Uh, hey everyone. Uh, I'm Dan. I'm the VP of Kernels at Together AI. Uh, I lead inference, uh, GPU optimization. I'm trying to figure out how to use GPUs most effectively to serve AI models.

Yeah. So one of the things that I wanted to dive, uh, in, uh, with, with Dan about is like new model drops. What are... What is everything that goes on behind the scenes to serve it so that everybody here, there's a lot of builders here that can use it.

Um, Olive, I want to throw it over to you to talk about your role and what you're focusing on.

Yeah. Um, I'm Olive, and I am the research lead of RL at MiniMax. And I'm responsible for the final training of the model and the shipping of the model.

So basically, everything before the inference, right?

Okay. Awesome. Um, so maybe I want to start off, this panel is focusing on open source. I wanted to start off, uh, with this is your strongest model yet, MiniMax-M3.

Um, why open source it? What's the kind of the, the idea behind that as a company, uh, as you're releasing these models?

We do believe that, um, the open source community as a whole is very str- strong and powerful. While we open source the model, everyone can use it, so it aligns with our mission that we want to have intelligence with everyone.

And also different developers can contribute to the model through feedback, through their own PRs, and we can build the models even stronger. And also like, for example, Dan, you, you will be able to optimize on our open-weight model and make it inference faster and then serve better for everyone.

Yeah. Yeah, we're, we're big believers in open source at Together-

Yeah

... and, um, yeah, I think when we, we've been, you know, following you guys for, for a while, I think from way o- old, older MiniMax models. So seeing M3 and seeing how far it's come is, is really impressive and really great.

Mm-hmm.

Yeah, so I wanted to kind of pick on, uh, this a little bit more. Can you explain... So we've got the model creators themselves, MiniMax. We've got, um, experts on the inference side of things.

How did this partnership come to be? So they launch an open source model, uh, and we're now distributing it. I, I checked this morning. We have the lion's share of, uh, token usage for MiniMax-M3.

Um, w- how does this partnership come to be, and how do we serve a model like this at scale?

Yeah, yeah, great question. So at Together, I think one of the things that, that we're really interested in is how do you, um, make intelligence abundant. So how do you get more tokens for more people to do, um, more useful things and, and, and get, uh, get all these capabilities into more people's hands.

So, uh, we follow all the open models very closely. Um, I, I don't remember when exactly we, we started part... Oh, actually, I think I do know this. Um, we had a car event in Las Vegas sometime last year and w- someone from MiniMax came.

And there he was like, "Guys, you really gotta serve our next model. It's gonna be really, really great." Um, so I think from there we, we started talking. We were serving MiniMax 2.5-

Mm-hmm

... um, and I think 2.7 for, for a while. Uh, and then when leading up to the launch of, of M3, uh, we were, uh, we were quite excited about it.

I think we, we were seeing the, the usage and what people were, were doing with it. It was, it was really quite exciting. Um, and, and so from there, uh, that's really where we partner.

We start working on the model, the architecture, optimizing it, uh, figuring out, you know, what's the best way to serve inference on it, um, and, and all those great pieces.

Yeah. I wanted to actually get into more on the model side of things. And so as the creator of a model, as, as somebody who's like post-training this thing, the model lands and all the builders that are here start using it.

From your perspective, um, what are the kinda the unique capabilities that you, you love to see people use it for? And what are maybe some of the hidden gems that you haven't...

You thought, "Oh, people would love to build this," but you haven't seen a little bit. Could you shed more light on that?

Mm-hmm. Mm-hmm. So MiniMax-M3, which was different from the M2 series, was that it was actually multimodal.

Yeah.

So it not only understands text and it not only writes code, it also understands videos and images. So we did see a lot of applications on agentic, uh, multimodal agents, which is very cool.

Um, and I would say there are a couple that we can highlight, right? For example, computer use. The model can-- is able to navigate through a computer and then do some pretty good creations with, uh, the tools that they, they can, uh, utilize.

And also, um, you can develop games with the model. Um, it's very fun that, uh, I, I don't... I think that's one of the hidden gems is that we actually worked on, um, game development.

So the model can help you develop, uh, real cool games. Um, yeah.

Yeah. One, uh, so when the, when the blog dropped and then, uh, the paper dropped, one of the things I noticed was that you guys highlighted, uh, SVG-Bench, you guys highlighted KernelBench.

You also touched on OSWorld.

Yeah.

So can you talk more about, like, what does it take to post-train, especially for those particular domains?

Mm-hmm. Mm-hmm. Uh, I would say is, uh, the very important thing is the data and how we define the problems.

Yeah.

Um, and it could be very different from different tasks. For example, uh, let's say the kernel one, right? The, it would be very important to design the environments of the data so that we can deliberately train reinforcement learning in those very complex environments and to let the model to optimize the kernels themselves and iteratively improve the performance.

And, uh, one, one aspect that I wanted to talk to you about on, on the kernel development side of things-

Mm

... um, where are you seeing open models, uh, wh- when it comes to kernel development? You recently released, um, a benchmark specifically for this. So I was wondering if you could talk on that a little bit as well.

Yeah. Yeah. It's a, it's a great question. So I think, uh, we're seeing all sorts of models. So the closed frontier models and the open models, um, get increasingly better at, at writing kernels.

So we use, uh, models all the time when we are developing kernels and, and, and writing the, the optimization frameworks. Um, I think the, the interesting thing that we are starting to look at is...

So this benchmark that, that we recently released called, um, ParallelKernelBench. So it actually has a bunch of, uh, unsolved problems in it. So we went around, surveyed all the different, uh, ways they can serve model inference.

Um, and one of the interesting things that we found is that there's a lot of things that we can think of that would actually speed models up that there don't exist good kernels for.

Um, so one of the reasons that we put that benchmark out was, you know, one thing that people worry about is, like, benchmaxxing or, or overfitting to particular benchmarks.

Um, one of our intentions with this benchmark was if you overfit to it, that's great, 'cause we'll go take those kernels and use them to, to, to accelerate the, um, the, the, the inference and the development.

Yeah. This is a really interesting point. A lot of people have problems with benchmaxxing. But the, the way I think about it is if researchers like you put all the really useful benchmarks out and we benchmark on all of them and everything is in distribution, then that's a perfect world, right?

Exactly, yeah.

That's a very useful model that we can then use. Um-

Yeah.

Okay. Cool. So I, I wanted to touch on, um, the inference side of things now as well.

Mm.

So, like, a new model drops like this, what does it take... C- could you take me, like, behind the scenes at the inference stack, and what does it take to go from day zero launch to then optimizing it week over week, month over month?

Yeah, yeah. Great question. So when we partner with someone like MiniMax, we will get some early model details. So, uh, for M3, for example, there are things like the MiniMax Sparse Attention, um, and, and some of those choices that were a little bit different from any model that's out there.

And I think if you look at any of the open models now, they're all quite different from each other in different ways. So there's different attention, different MoE choices, um, differences in quantization and, and all these pieces.

So as soon as we get those details, we start writing kernels, benchmarking, figuring out is there existing kernels that work for it, uh, do we need to modify something, do we need to write something from scratch.

Um, and then so day zero we're d- trying to think about things like quality. So, um, when this model launches, is it gonna have the quality that we all expect?

Uh, are we gonna be able to provide the right, um, the, the right user experience? Um, and then from there, uh, as soon as it launches that day zero, we have a long list of things that we know, hey, we have to do this with the KV cache, we have to do this with the attention kernels, we

have to do... Uh, we're gonna look at this part of the quantization, um, and things like that. So we, uh, we, we have that list and then we start working on it and start, uh, optimizing over the course of weeks so that when you use these models, they actually get faster, um, between day zero and day seven

and day 14 and, um, et cetera.

Yeah. I was just talking to Ingrid actually yesterday and I, and I asked her, "Have we been improving the performance of M3?" Um, and I meant over the last month and she said, "Oh, did you mean from last night?" [laughs]

And this is the pace at which these guys work, so, um, it's very real. Um, one aspect that I wanted to touch on with this is we're seeing the workloads shift.

We're going from kind of predominantly chat workloads where you have turns, uh, coming in now to agentic workloads where you've got this thing sitting inside a harness and you're doing hundreds and hundreds of multi-turn tool calls.

Yeah.

Does that change the way you build the inference stack?

Yeah, it definitely does. So these agentic turn-based workloads, uh, they go into everything from informing your KV cache, um, your prompting, your, um, pieces like that. So it, it, it informs what part of the stack you want to go optimize, um, because now I think when we're in the chat, chat, chat world you have a system prompt

of a few thousand, um, and then you just have the, the chat logs. Now with the coding-based agentic workflows, you upload your whole code base to the model, um, and that's a very different optimization and routing and kernel challenge, um, than, than just the, the chat-based workload.

So yeah, we're, we, we follow these workloads very closely. It's really interesting to see how they evolve and, and how to adapt the inference stack and the inference engines to, to really take- uh, to really serve them well.

Not only do you have agentic workloads, but you've also got multimodal workloads in there. So what I like to do often with these coding agents is, um, get them to optimize a, a web app and then get it to use it and then do a feedback loop.

So one thing that I wanted to come to you, uh, uh, Olive, for is, uh, MiniMax-M3 is multimodal, M2.7, all, all the ones before that were not multimodal.

And, uh, like, can you talk a little bit about the optimizations and, uh, how you trained it for that aspect? And then also I wanna get into the architecture of it a- afterwards as well.

Right. Uh, definitely. So what's different from before was that it was trained multimodal from scratch.

Yeah.

So from step zero we train not only text data, we also train image data. And it was normal for many other labs that the model would collapse after training a little bit and we managed to solve that problem.

And, uh, what we find was actually that with this kind of training from scratch, if you look at the attention map, it actually the visual... Uh, the, the text tokens would attend to the visual tokens so that they're naturally combined together to naturally understand each other.

So for example, we are developing, for example, uh, we- websites, right?

Yeah.

Um, it is better if we train with m- uh, both multi- modalities. Also like for example it can look at the website, it can understand how it looks and then better optimize for it, like for example during reinforcement learning.

Um, so yeah, I think that is pretty cool.

One, one thing that kind of stuck out with this model for me was the fact that it introduced a lot of new things. The multimodality, the increase of context to one million-

Yes

... um, the fact that you have a sparse attention now.

Right.

Um, so if you go to the inference side, it's almost a, a nightmare, isn't it? You get, you get this new model, and there's so many things that you could optimize to speed up inference.

Um, practically, what are the things that you focus on? There's like 1,000 things that you could optimize, but where do you get the most bang for your buck?

I mean, you focus on 1,001 things.

Yeah.

Like, you just, you just go, and you keep, you keep doing it. You find every edge that you can, um, and, and you go and, and you push on it.

Um, so yeah, I think there, there's, there's no stir-

Yeah

... there's no stone that you leave unturned-

Uh-huh

... and you just, uh, ke- keep going at it. If someone tells me you can't do the 1,001st thing-

Yeah

... like, I don't know, try harder.

Yeah.

And then up a little later.

Oh, go ahead.

No, no, that's it.

Yeah. So the other thing that I wanted to ask is there, there's a whole kind of, um, zoo of open source models.

Mm.

Uh, as you're talking about speeding up inference, are there things that ... Are there lessons that you can take from one model and apply it to MiniMax-M3? Um, or, or do you have to, like, restart from scratch as you're thinking about the inference engine, the kernels?

Like, how, how does that work?

Right. Um, yeah, so there, there's definitely things that you learn from optimizing one model that you take to another. Um, so I think sparse attentions are something that have become quite popular now.

So the MiniMax Sparse Attention is a little bit different from the, uh, from the DeepSeek and the, and, and, and those, and the, and the ones that you find in GLM.

Um, but the, there's still similar lessons that you can take from that optimization process and that kernel writing process that you can then bring to, to the new sparse attentions.

Um, and you know, we've been, uh, in, in some form anoth- and, or another, have been thinking about this problem for, for many years, um, so going all the way back to my PhD.

So it's, it's, it's great to see some validation that, that folks can now train it at scale, um, and people are using it and, and it's, uh, and it's, uh, it's going pretty well.

Yeah. Yeah, one of the interesting things, uh, especially about open source is you've got all these labs that are learning from each other-

Mm-hmm. Mm-hmm

... kind of, uh, taking the wins from each other, right? So if, if, uh, if one lab figures out that MiniMax does this really well-

Yeah

... then that gets, becomes the golden standard. Um, o- one of the things o- on model launch that I, uh, in the blog post that you guys go into is that this model was actually able to replicate a 12-hour run where it could reproduce an ICLR paper.

Um, and so somebody who's training this model to do this thing, how do you actually go about that? 'Cause that seems like a pretty ludicrous task.

Right. So letting the model to do cool stuff like replicating papers-

Yeah

... uh, optimizing kernel frameworks and stuff like that is always exciting for us researchers because it's, like, very related to our job.

Yeah.

But training it can be very tricky because it's very long horizon-

Mm-hmm

... and, like, the, the task itself would require GPUs. Um, it has hardware constraints. So it's very interesting to train tasks like that. And I would say the key there is still the environments and the data and how you formulate the problem, how you formulate the rewards, how you formulate the environment, and how you change the reinforcement

learning algorithm a little bit so that it's trained more efficiently, um, so that you can see cool things emerging through the, the iterations of RL runs.

Mm-hmm. Can you talk, maybe if I keep pulling on this thread a little bit, how do you do evaluation over these longer, longer scale runs? So if you're, if you want the thing to do a 12-hour task-

Mm-hmm

... yes, it might or might not do it at the end, but are there, like, uh, spar- intermediate things that you can also look at?

Yes, we do. For these tasks, uh, there are, there are iterations, right?

Yeah.

So the model can submit several times, and we would evaluate each of them.

Okay.

Some of them, some of the times, the models would hack, and we do, uh, do, like, validation and test split for it to test if it's really improving on the performance or it's hacking.

Uh, and also we design our internal evaluations. So for example, for the release of 2 point, M2.7, we touched a bit on self-evolution, right?

Mm.

So we're actively using the model to improve the speed of development internally, which, um, like, out of it, out of it, we can build our own evaluations that are closely related to our own work that we can evaluate the models on.

Yeah. When, so when we start talking about these long-horizon tasks that are 12 hours long, uh, we gave an entire workshop on this on Monday, but what I wanted to come to you, Dan, for is, um, KV cache.

So if let's say you-

Mm

... you have concurrent requests that are 500 to a million, uh, uh, thousand context length long, how do you deal with the KV cache that just keeps on growing?

And how does the inference engine deal with that?

Yeah. So there, there's a lot of different pieces that, that you put there. Um, like in, in some sense it's like recreating a distributed file system. Um, so we were in some sense building something like that, uh, or a, or a very big database.

Um, it's, it's pretty simple in theory. It's like the type of thing that you should have done in your third year of undergrad or something like that. Um, but most of us actually skipped that class, so now we're rediscovering it, um, live in, in industry.

But it's, it's all about where do you store that cache? Uh, how do you know? Have you, have you seen this before? How do you fetch it? How do, how do you send it from one place to another?

Um, so yeah, it's, it's, uh, it's, it's not that complicated. Um, but, uh, you, you do have to make sure that, that you do a good job.

Yeah. One thing I noticed, you, you gave a, a, um, a lecture at Stanford recently, and one thing that stood out was that if you fast-forward like two, three years, two, three years is, is, is a long time in AI, and if you look back, you said that we'll realize that how, um, how early we are right

now.

Yeah.

So from your vantage point, we're three years out. What do you think we'll look back on and be like, "Why were we doing it this way?"

Great question. Um, uh, some things that I hope for. So I think we underutilize our GPUs a lot right now. Um, you know, SpaceX said they would have, like, 10% FLOP utilization or something like that.

I hope in three years ... Well, they, they should already be embarrassed by it, but I hope in three years they're extra embarrassed by it. Um, so certainly training should be, should be pretty, um, should be pretty good.

I think at inference we can do a lot better with the hardware that we're using, uh, that we have today. So I hope, uh, in a few years we'll, we'll say, uh, we'll, we'll have seen the light on, on some of those pieces.

Um, and I think there will be a lot more models, there'll be a lot better ... Um, I, I hope finally by then we've put to, put to bed this question about the open models.

You know, there's ev- every few months there's someone like, "Oh, Anthropic, OpenAI, they're so ahead," yada, yada. Um, but I think, uh, we're, we're seeing with models like M3 and GLM and Kimi and, and all those models that, um, the open source frontier really can catch up.

Um, and uh, and it's, it's not even that far behind. So, so I think that that's quite exciting.

Yeah. I, I wanted to throw that same question over to you, Olive. But you mentioned that you, uh, for, for the M2 series and the M3 series, you're using this idea of self-evolution where the model is building its own harness and then it's training inside of that, and then you get the next checkpoint.

Um, if you look back three years, uh, out and then you say, like what in RL or post-training, um, do you think, uh, made the biggest difference? What do you think that is from this vantage point?

Um, great question. But three years ago I was still in school. Um [laughs] [laughs]

I actually didn't start this industry yet.

Yeah.

So I wouldn't have imagined what's happening right now today, so it's really exciting. But I can see how, uh, models that were developed are, were already, um, improving the speed of development-

Yeah

... maybe a year ago or even further than a year ago.

Yeah.

So I could see how the speed is actually accelerating, um, how the development is accelerating. And that's how, like, open-weight models can really catch up with frontier labs.

Yeah.

And yeah, it's, that's how we think we are on a mission to bring this model to everyone, um, so that everyone can use it. Yeah.

Awesome. Thank you, guys. Thank you, Dan. Thank you, D- uh, thank you, Olive. Um, thank you guys so much. Have a great day.

Very cool. Thanks so much.

Thank you. [clapping] [outro music]
