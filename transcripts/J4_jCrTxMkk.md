# Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama

Source: https://www.youtube.com/watch?v=J4_jCrTxMkk

Uploaded: 2026-08-07

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/29/29095fdc6888af15d7893e33ca8ad0884a0148d9c389353d1c7b676e7f6d39ce.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/J4_jCrTxMkk.json.

## Transcript

[upbeat music] Okay. Hello, everybody. Welcome to, uh, Compression at the Edge, the panel that we'll be conducting for the next bit here.

Uh, very nice to meet you all, I'll be your trusty moderator today. Uh, my name is Chris Alexiuk. I'm a product research engineer at NVIDIA. I work on Nemotron.

Let's go. Okay. We are joined by...

Daniel. Yes. Hello, everyone. I'm from Unsloth. Um, yeah, thanks for coming, everyone.

Excellent. And...

Hello. Hi, I'm Asma. I build Mo- NVIDIA Model Optimizer, and we quantize a lot of models.

Let's go.

I'm Merve. I work as a machine learning engineer at Hugging Face.

Awesome. I'm Parth. I work at Ollama.

So compression, uh, a big topic. We're gonna, we're gonna set some, some context, hopefully, uh, i- in order to, to kinda launch into this. So may- maybe just in each of your own words, if you wanna kind of define what you think about compression, let us know like how you engage with, uh, with technology that ultimately is

designed to make models that are bigger, be a little bit smaller, right? Like, that's the, that's the general idea. So, uh, may- maybe we'll just go in reverse order.

Parth, if you wanna kick us off, and what, what is compression to you?

Yeah. I think honestly, with Ollama... And for those of you who are not familiar, Ollama, one of the easiest ways to run local models. Um, and for us, what honestly like rose us to popularity was being able to run a larger model on a relatively small machine through quantization, which I'm sure we'll talk a lot about today.

Um, and to me, compression is so, so important because it actually makes these giant models viable for most people.

I think for me it's just, um, shrinking something without losing information, but there's absolutely zero free lunch, so at the end of the day, you still spend on something, whether it's latency or, uh, quality, uh, at the short.

Um, and I kind of agree, I feel like compression is much more than that definition because it democratizes the models for everyone at edge devices at your computer. I'm sure you are all running some, uh, Gemma 4 quant at the moment, or Qwen 3.6.

Those are the hot ones these days, and like, it's, it just works so well. Um, so yeah. Uh, this is my definition, that is it democratizes things.

Cool. So the way I think about is same cost, more intelligence. So compression accelerates and enables. To give like, um, like a quick example, originally we started with training in FP32, right?

And now we are talking about FP4. So that is eight x, uh, more compression and, um, same-- almost same intelligence without not much degradation. Yeah. Same cost, more intelligence.

Yeah. Like how we see quantization is like, you know, you take like a big model like GLM 5.2, it's 1.5 terabytes, which is definitely ginormous. Um, but then the trick is you can actually quantize it and shrink it to 250 GB.

Um, so you can make it 86% smaller. Um, but with tricks of quantization, it will not become 86%... So it's not 86% dumber, right? If you compress it by 86%, it doesn't become like, you know, terrible, useless.

Um, and so what we show with dynamic quantization, if you quantize some layers to, you know, higher precision, and you leave most of the layers in like one bit or two bit, and some, you know, very important layers as 16 bit, you can still recover 76% of all accuracy.

Um, so you... So the trick for quantization is if you quantize the correct layers, you will not make the model, you know, literally useless. Um, and compression, I guess, is very important for you to run on your local computers, um, you know, make democratization of AI.

Um, yeah.

So like, okay. We, we, we, we've been talking today about like there, this inflection point, right? Recent moments that like, uh, kind of, uh, uh, led to this, uh, this more, th- this resurgence of the importance of local AI and, and, uh, you know, op- open models, right?

Uh, ow- own your own intelligence. W- y- you guys were like ahead of the curve though, right? [laughs] Like, I mean, uh, y- you guys were thinking about this before it was, it was cool to think about it, right?

So I'd love to hear from each of you, like, w- when was the moment that you knew that like quantization or compression like is the path forward for... It, it, and, and we're gonna talk a lot today about like consumer, right, uh, hardware.

That means like your RTX cards, your, your, your Macs, things like that, right? But, uh, it, it go- goes well beyond that. What, what was the moment you kind of first like got the quantization or compression bug, you know, that made you say like, "Oh, shit, this is gonna be big, man"?

And we'll just go right back down the line. Daniel, take us away.

Yeah. Um, so I think like the biggest moment was DeepSeek-R1, definitely. When it got released, it was quite dramatic for the world because we finally have some sort of like reasoning model that worked very well, um, and it was open source.

Um, and the biggest problem though, it was very big. Um, and you know, running it locally was extremely complex. Um, and so, you know, we... When we started off, like, you know, we decided, "Okay, let's do some tricks.

Let's quantize some layers to higher precision." Um, and it randomly worked. Um, and so like we were quite surprised, like, you know, 1.58 bit quant worked well. Um, and we were...

Yeah, we just posted about this, and we were quite surprised. "Okay, local models seem to be working well." Um, and obviously over time we had, you know, Qwen 3.6, 3.5, Gemma 4, you know.

Every single time there's a new... Even NVIDIA's, you know, open source models, Nemotron, they just keep getting better and better and better. Um, the only problem sometimes is they get bigger and bigger and bigger. [laughs]

So that's the only problem. And so you need to focus more on like, you know, how to make the model smaller and smaller and smaller. And so like, you know, recently with GLM 5.2, you know, it was quite, you know...

It's a very good local model, and-

Although it's ginormous-

Although

... and so making it work very well on the, the local device is complicated. Um, but I think like, you know, I guess it's a long history of these models.

Um, but we're expecting more. You know, whatever the next Nemotron model is, the next Gemma, the next any model, um, we're very excited for the future. Um-

Yeah, it's like a ongoing arms race between how big can we make the models versus how small can we make them and they still work, right? Uh, uh,

maybe some thoughts for, for, from you. Like what, when did you think like, "Ah, man, quantization is, is it?"

So I originally started working on pruning. Uh, so okay, so that was maybe three years back. That was when CV models were all the rage. Then ChatGPT happened. Um, yeah, so pruning, typically...

You typically lose, uh, quality, so you need to fine-tune it a little bit. And then we, LLMs came out, and quantization was a easy compression, uh, thing y- y- you could do.

You don't, uh, lose a lot of accuracy. The model, it pr- So what I learned was some kind of compressions are really good. You can architect techniques so that, um, you can chop it down a lot without, uh, losing quality.

So quantization is really good. Uh, sparsity is really good, but not as much as quantization. So I did not have like a exact moment of like, you know, where I got this numeric bug.

It, uh, slowly grew on me. And, uh, so for example, NVFP4, right? I was fortunate to work on NVFP4 experiment math when I joined NVIDIA. And the NVFP4 is very genius.

Uh, it, uh, we have been doing like a lot of research and experiments to, uh, make NVFP4 better, but it is like a really solid, uh, numeric format. So yeah, so that was...

Yeah, so basically like, you know, uh, some compressions are really good, and you can cleverly architect, uh, understanding things better and, uh, not lose quality. Like, like, you know, Dan said, uh, mixed precision, uh, quantization, uh, you can compress it a ton, chop it a ton without losing much quality.

Yeah. So that was a slowly growth for me.

Should I? [laughs]

Yes, please.

So, um, I think for me, the biggest wow moment of quantization was back in the day, there was something called QLoRA.

Oh. [laughs]

And, [laughs] and the fact that we could actually fine-tune stuff on a toaster, essentially, that is the Colab Free tier T4. For me, that was like a big wow. Although i- it's super slow, it's, it's okay.

Um, but on top of it, um, for instance, like we have libraries called TRL and bitsandbytes and PEFT that enables all of this. And like, you can even do this with the very advanced techniques like GRPO, for instance.

Actually, you can train stuff on the, um... I mean, you need to collocate and stuff, but like with, with very small amounts of VRAM. And then recently we, uh, in case you missed it, we have acquired llama.cpp, kind of acqui-hired llama.cpp.

And then I kinda pivoted to the llama.cpp world, and I was like, "Wow." Because like the second wow moment for me was the fact that I could run OpenClaw and Hermes Agent on like very long-horizon tasks with a Qwen 3.6 quants, which wouldn't be able to...

Which wouldn't be possible before. Um, I just know. Uh, I tried many models actually with that, and then Qwen 3.5 was like, wow, it can do a lot of coding.

It can fix its own harness and stuff. So yeah, that was the two big moments for me, actually.

Yeah. Um, I think I'll speak to it more from like a, a consumer point of view. Um, I... This is back in like 2023. Uh, I was kind of hacking around my own stuff.

This is prior to me being at Ollama. Um, but one of the coolest things was I wanted to run kinda my AI on my computer. And I was still in school at the time, broke, did not have a lot of money.

And so I was like, "Okay, I need to run this for free somehow, so what's like the best option?" Um, and so I came across Ollama at the time, and I ran the model kinda locally at, on my computer, and I think it was Llama 3 at the time as well, a very long time ago.

Um, and honestly, for me, that's kinda how I got into the whole world of local models is like, okay, this is actually workable. I can like make it do things.

It's able to output something. And, you know, back then it wasn't as good as it is, you know, outputting now. As Merve said, Qwen 3.6 is insane and Gemma 4 and all.

There's all these new models which can have so much more capability baked into them. But for me, it was honestly the idea of like being able to even just run something locally.

Um, and it started with like Llama 3 with Ollama and being able to actually have it run and like complete tasks. Um, and prior to that, you know, I'd done, built a lot of models before, um, and I knew like how much work it goes, right, is, like goes into building them.

Um, and running them has always been hard. So to me, quantization like really makes that happen for a lot of people.

Yeah, I mean, I think everyone's experience is the same, right? Like, uh, probably most of the people in this room, the first time that you run one of these models that like, you know, only exists in behind an API or, or a host environment on, on some cloud GPU somewhere, uh, on, on your, on your computer or

on your, you know, your, your, your gaming laptop or your, your gaming, your whatever it is. I mean, it's just, uh... I, I think from that moment on, you're like, "All right, making these things small is pretty cool."

There, there is, though, a, a, a something that we have to discuss, right? And, and, and, and anyone can jump in to, to follow up to this. Well, I'll pose it first to you, Daniel.

Uh, you said like models are 86% smaller, right? But like, they're not 86% dumber. Uh, how? That sounds absurd, right? Like, uh, and, and, and beyond how, like how do you actually like verify or think about verifying that like this model is, uh, you know, gone through the process of some, some form of compression, right, whatever it

happens to be. How do I now like determine that that model is, is not garbage, right? Like, uh, that, that, that we haven't chopped out 86% of its brain.

Yeah, that's a great question. Um, so I think generally speaking, if you compress a model down by 86%, you would assume, you know, if you randomly select parts of the model to compress, like delete or something like that, or set, set them to be like if you round it to like the closest number, you would, uh, most

likely it will be not 86% dumber. It will be 100% dumber. So if you do that methodology, that will not work. Um, and so the main trick of language models is you should leverage the architecture of the language model itself.

So language models generally have like, you know, 36 layers, you know, 50 layers, many, many layers. Each of the layers have different importance. Um, and so like, you know, for example, the most...

The first layer is actually very important, and then the last layer is also very important, but then the middle layers are kind of useless. Um, and so the main reason why they're not that useful, um, is because when you train a language model, um, with like, you know, let's say one trillion parameters, um, you have to use

many, many tokens, right? So like a language model can be trained with like 30 trillion tokens. Um, but we're still not there yet in terms of saturating all of the weights.

Um, so once you... Okay, maybe in the future once we train to 300 trillion tokens, okay, maybe you can't do compression anymore. Okay, maybe that's another topic. But at the current stage, the trick is, um, 86% of the weights do not need to be there in the model.

Um, because of the training algorithm, because of, you know, back propagation, some of the weights are very close to zero, and you can literally just set them to zero.

Um, and so that's one of the tricks. Um, and also you have to do, you know, layer-by-layer analysis. You know, if you quantize layer one, what will happen to accuracy?

If you quantize layer two, what will happen to accuracy? And so on, so on, so on. Um, and so you can also think of this as like a combinatorial optimization problem.

Um, you don't just do, okay, layer one and then do layer two. You also have to do like, you know, 32 choose two layers or choose three layers. So it, it becomes very complicated.

Um, and so like, you know, it's a very... Then you get some combinatorial explosion problem. You know, it's not just layer by layer. You know, within the layer, which number of this specific tensor is not quantizable or not?

Um, for example, there is something called a, um, super weights p- there is a super weights paper which shows that if you quantize one number, just one of the entire model, your model becomes 20% dumber.

Um, and so you need to find this specific one number, and then you cannot quantize this. Um, so there is like very s- weird mechanisms of language models during training.

Um, and yeah, there's a lot of whole research going into like quantizing models correctly. Um, yeah.

A-a-anyone else with thoughts to add here?

Uh, yeah. So, uh, okay. So f- particularly your question was about how we evaluate the-

Yeah, like how... E-exactly. Like how-

Okay

... beyond just how do we make the mo- models smaller, like how do we know that it's not dumbed down?

We have our answer. We just run all the benchmarks, mostly the AA benchmarks. So, uh, model optimizer team, we publish lot of check quantized checkpoints on Hugging Face Hub.

You can check the NVIDIA Model Optimizer space. Uh, so we, with FP4, we target for less than 1% accuracy degradation overall on all AA benchmarks. Yeah. So, uh, yeah, yeah.

So that is, um... And, and, um, they're like, you know, w- uh, we, we, uh, we, we try to use simple, uh, strategies because that way we can, um, push out, uh, models faster.

Um, on top of that, uh, learning is that, um, s- s- the strong, like, like, you know, um, the simple and strong nicely designed number formats like FP4 preserve like lot of accuracy.

And then, um, we also see this, um, disproportionate sensitivity to some layers. For example, uh, linear, uh, attention projection layers are very sensitive. Uh, the, the, uh, KV, QKV layers are sensitive, whereas MoE, we, we by default, uh, keep them in, uh, FP4, while we put, say like, you know, other, uh, layers in FP8 or BF16.

We use this, uh, gradient-based sensitivity analysis. It runs like a linear programming solver. But yeah, um, m- m- my main, um, learning has been, um, that, uh, FP4, um, or like, like, you know, really nicely designed, uh, number formats help a, uh, lot, and we, yeah, and then a lot of benchmarking, the boring stuff i- in which

we spent a lot of time, yeah.

Maybe ju- maybe just for everyone here who is like, uh, you know, I, I mean, I, I think w- w- w- hopefully most of us understand like BF16 and like, you know, uh, uh, FP8.

Like what, what the hell is NVFP4?

Oh, cool. Okay. So FP4, um, the number is there. It's a floating point 4-bit number, but the genius is in it is a micro block scaled, uh, number. So micro block scaling means, uh, every, uh, you choose a group.

So in, in the case of FP4, you choose 16 elements, and you can share one scaling factor, one, one extra, um, FP8 number between these 16 elements. So this was originally, uh, invented by, uh, uh, uh, bitsandbytes, uh, Tim Dettmers, and yeah.

So, uh, NVIDIA adopted like a similar but different design of, uh, 4 bits, but every, uh, 16 bits share one, uh, 8-bit value, uh, to scale them, and yeah, that has been s- like, uh, that has been tremendous.

It, uh, gives s- significant improvements o- over like other f- f- formats, yeah, of, of 4-bit. Yeah.

Yeah. So it's, it's, it's not as simple as like, uh, we just make the numbers smaller. [laughs] You know? [laughs] It's a lot more going into it than that. I mean, interesting to hear from you guys.

Uh, like w- I think w- w- w- a lot of the time when we talk about compression or quantization or a- any technique that makes the model more accessible, right?

We're talking about it through the lens of like, uh, so that I can run it on my, on my toaster, like you said, right? Uh, but like i- is there any value to compression or these techniques that exist for like a business that presumably has access to, I would hope more, more than a toaster? [laughs]

Parth, Parth, maybe you wanna...

Yeah. I think- For sure. Like, you have a variance in kind of just, you know, hardware that a employee has versus hardware which, uh, scales up and, you know, they're running their own clusters.

Um, and the way that at least we look at it from is you're-- you should be able to run whatever model you want locally on kind of that individual's computer as well.

Um, and you know, with compression in particular, you run through a lot of different challenges. So accuracy is for sure one of them. Um, but, you know, actually making use of it through a harness, um, seeing, you know, what the end result is when you actually try it out.

You know, there's so many things that I feel can't be captured by a, a model optimizer or after quantizing it or, you know, certain benchmarks. And it's literally me, you know, running through-- putting in Claude Code or something and running the model.

It's like, "No, it doesn't feel just right."

Mm.

Um, so I think, you know, the benchmarks are a great indicator of pointing in the right direction, um, but having the model behavior kind of stay in line with that, I think is still kind of being worked on.

And when it comes to businesses, you want to be able to give them the option to not just, you know, deploy their own models on like their own infrastructure, but also empower them to be able to run it on, you know, individual machines.

I think benchmarking oftentimes only work for the verifiable tasks rather than the, you know, the vibe itself. And like, I now that I think about it, actually it could have been cool to have like a quant arena or something.

But unfortunately, like there was a paper last year by, um, Singh et al., I think, yeah, from Cohere, uh, that showed that a-a-arenas are very much hacked. [laughs] Uh, so that-that's also not the way.

But anyway, I feel like most of the jobs still do not require, uh, like a fable level thing. Like we are kind of in a bubble as a software developers, right?

So we are like, "Wow, fable." But at the same time, mo-- really, most of the jobs do not require that. And on top of it, like for the businesses of, of-- Some of the things that we are saying, I feel like because I'm very open source pilled, it's like super obvious, but at the same time, many people

don't know about it. Like you can just serve a lot of like, you can have much more concurrency. Uh, at the same time you can do like in-house deployment and stuff.

So like, um, increasing concurrency cuts the compute and then... Yeah, like most of the time people just don't need that. But like for instance, like I've been hearing a lot from Hugging Face users and stuff and like it's not only the quantization, but I know companies that actually distill mid-size models to like very small ones for like

re-ranking or whatever that doesn't require like LLM outputs, uh, cutting like millions of costs. So like it's not only quantization, but like there is so much more that is out there for compression in my opinion.

Mm.

And it just creates a ton of value for businesses and people aren't aware of it. Like, because people in this room are like, you know, you are interested, you, you read about it, you just assume that people know a lot about it, but actually they don't and it's kind of shocking to me.

But yeah. [laughs]

Uh, I, another question that comes up all the time, right? We're talking about model compression. Uh, you, you were talking about like GLM-5.2, right? And let's, let's shrink it down as much as we can.

Uh, back there on the, the station we're running, uh, you know, a REAP quant of, uh-- well compress of, uh, of GLM. But like why would I do that when like, uh, Nemotron-3-Nano exists or Gemma Small exists or Qwen Tiny, you know, exists?

Like w-w-why, why should I care about compression when a lot of these model shops are kind of putting out like, uh, small enough models that you can run them in kind of their native precision or, or very close to their native precision?

So there is a paper showing that if you wanna do compression, um, it's actually most likely better use of resources if you train a ginormous model, then you quantize it down.

Um, and so there is this like formula where they show, um, comparing for example a very small model like a thirty-five billion, um, you know, thirty-five billion bfloat16, so 16-bit versus say like, um, four times bigger like one hundred and twenty billion at 4-bit.

Um, and which one's better? Um, right. So essentially they're the same size in terms of disk space, but which one intelligence-wise is better? And from those experiments they show that the bigger model quantized to 4-bit is actually much better, um, than a thirty-five billion 16-bit.

So in general, most likely what will happen is we get bigger and bigger and bigger and bigger models. Um, and you know like, okay, currently now, you know, GLM, you know, one point five terabytes, you know, oh, okay, it's not that big.

Um, but what happens if it's fifteen terabytes? Then okay, we must do quantization. We must do compression. This will not fit in anyone's-- not, not even enterprises can now serve this.

And so like local models, you know, you must do compression if they're getting bigger and bigger and bigger, um, and you know, to extract any value out of it and you know...

Okay, I guess the DGX station has a lot of memory. I guess that's very useful. Um, but you know, once we have ten trillion parameter models, that will also not fit.

And so like, you know, we need to do compression, you know, I guess quantization for that. Um, but in general the small ones are very useful. Um, but I think the bigger ones compressed down, um, is slightly more useful.

Um, but there's also another trick. You can do model routing, for example, for the small ones. You can do it for the-- For example, you can use the big ones for planning and then do execution with the small ones.

Um, but the small ones are still better because they're much faster. So even if you have a big one and you compress it down, uh, you probably get like five tokens to ten tokens per second if you don't have enough GPU power.

Um, and for the small ones you can get two hundred tokens per second. Um, so I guess like depending on your use case, um, you also have to consider speed, throughput, you know, what is the GPU that you have and stuff like that.

Um, yeah, I guess.

I mean, very cool. Very cool, obviously. Uh, y- so Parth, you're with Ollama I, I, I imagine m- most of the people here know Ollama. Uh, if, if you're, if you're not using it, give it a try.

Uh, you know, this is one of those topics where, you- is Ollama useful in a world where we don't have this kind of compression, right? Like, how, how much, uh, is the fact that we can compress intelligence to kind of run on, like my Mac or my, uh, you know, my, my, my home workstation, right?

Like, how much is that, uh, ecosystem important to, to, you know, people or businesses or organizations like Ollama?

Yeah. I think, uh, it's pivotal, obviously, for... In or- in order to have, like, these models be so viable running on your personal computers and being able to actually make work of them, as Merve was saying, you know, Qwen 3.6 just running on computer, running OpenClaw, being able to fix its own harness, that's really possible through some

level of compression. Now, there are, you know, other techniques which kind of some of the model labs will do, especially while releasing smaller-sized models, um, things like QAT or, you know, with GPT-OSS, it was MXFP4, which is a different format.

So I do think as long as there's a demand for being able to run kind of personal language models, even if compression didn't exist, there would be analogous techniques or, you know, maybe model training would look a little bit different.

Um, obviously that comes... everything comes at a trade-off, um, as Daniel was mentioning. You know, you can have a really large model being condensed down into something smaller, so you can run it, versus even just having, um, a full-precision model but smaller in parameter size, and they both come with different trade-offs.

It, it, Merve, like, how, how do you see the open source community help drive this, right? Like, uh, I, I think quantization... I mean, we all remember Tim Dettmers.

We all remember, uh, QLoRA, uh, you know, is like, uh, that, that, that, that image, right, where there's a big stack of things that would fall over if it weren't for bitsandbytes holding it all up.

Like, like, how have you seen the open source community flourish or grow around, uh, not just quantization, but compression more generally?

I wanted to add something to what Daniel says. By the way, if you don't know about their work, they have, like, immense pipelines to actually do the quants and then verify them and stuff.

So, like, I highly recommend you to check out Unsloth, which is, like, in my opinion, the best quants you will find over there. Yes.

Oh, thank you.

Um, I wanted to say, for instance, like, to add to your point, like, two years ago, I think two years ago, we trained, like, SmolVLM where there were no small vision language models.

There was LLaVA, and then there was a jump to big models, and then nobody was training, like, smaller ones. Um, we figured out that, like, um, training, like, we trained, like, 1B 500M and 260, f- uh, 56M, and, like, 256M was not good, and, like, 500M was actually somewhat good, and it was actually able to run on

your iPhone, which was, like, shocking to me. [laughs]

And, um, I noticed that over time, it feels like, uh, people have been releasing, like, smaller models, which is great, but, like, if you have, like, advanced models, and then everybody's just releasing midsize models, you can quantize them, and I feel like that's the biggest value that quantization somewhat offers.

And for instance, like, to coming to your question about the community and stuff, for instance, this year, what happened was that for the Qwen 3.6 release, Qwen team asked the people, "Okay, we are going to release only one checkpoint," which is kind of heartbreaking, and everybody said the mid-sized ones.

And this kind of goes to show the value of, like, how quantization is adopted, and everybody's, uh, using those checkpoints and then quantizing them instead of asking for smaller models.

I feel like you get more and more and more intelligence, and then over time, you shrink them, and then suddenly it-- the, the, the bigger models make the bigger shifts in terms of, like, um, how much you can quantize them and still you do not lose the information.

And the quants become smaller than the bigger models of yesterday, which to me is, like, phenomenal. Um, as for the community, can you rephrase your question again? [laughs] [laughs]

I think you answered it, actually.

Yeah. Yeah.

It's a great job. You, uh, yeah.

Thank you.

I mean, you know, I, I gotta ask this question, uh, since you're, you're on the... you're up here with us. So we, uh, NVIDIA Nemotron releases NVFP4 with every, uh, release.

NVFP4 is, uh, a- as described, uh, basically a numeric f- format, right? Uh, but the idea is that it's, like, a smaller version of the model, and it retains a lot of accuracy, right?

Uh, which is the whole idea of, of compression and quantization. Uh, I, I'd just like to hear, like, how hard is it to do that, right? Like, so we, we kind of heard Daniel talk about it from this dynamic, uh, quantization strategy, right?

Uh, it, it already sounds very difficult. Uh, like, how difficult as an engineering challenge is it to, like, make the model small without it shitting the bed?

Uh, I see. Okay. So if you're doing post-training quantization, which is, uh, you take the model that, uh, the, uh, like, the release model, the BF16 model, and do, uh, post-training quantization on it, it is fairly, uh, like, you know, easy to do.

Uh, um, so we q- quantize to FP4 models like, uh, a, uh, large, uh, GLM or, like, you know, those, like, trillion-size models. Uh, you need, uh, like, um, a...

We have Blackwell nodes, so we put it on Blackwell. Uh, in, in a couple of hours, uh, the quantized checkpoint is ready. But then our pain starts there because now we have to evaluate these models, match the model card.

Uh, actually, that is where we spend a lot of our time. Now, coming to, uh, uh, training-based methods, okay, so for large models and medium-sized models, uh, I would say, like, you know, 20 billion parameters plus or 30 billion parameter plus dense size- Uh, this PTQ usually works out of the, uh, box, uh, with, uh, some selective

quantization like the heuristics, like h- Dan mentioned, right? Like we use some heuristics such as, uh, s- sparse MoEs, uh, can be aggressively quantized. Uh, like, yeah. And we also have this auto quantize which uses this automatic sensitivity analysis and, uh, knapsack solver.

Yeah. Yeah, so all those, right? So for medium and large models, PTQ works out of the box very easy... Relatively super easy to do. Uh, then if it is smaller model, say like, you know, s- less than 20B-size model, we have to do some, uh, quantization-aware distillation, et cetera, to recover accuracy.

That is... Yeah, uh, so training-based methods are a little bit more painful. They're becoming more painful, especially with these reasoning models. So you need to have the original dataset.

And it's not just about the original dataset. Internally, we have the original Nemotron dataset. But even then it is a pain because these are multi-trained, uh, multi-stage trained RL models, uh, like for...

Done with... Now models are being trained with, uh, multiple teacher distillation where each teacher is like an expert in coding or reasoning or something. So it becomes really difficult to, uh, get, uh, good, uh, training data to, uh, train the model with, with QAD, uh, yeah, to recover accuracy.

If we, if we train, if we do QAD with the wrong data, it, uh, m- it most commonly breaks the model rather than helping it. Yeah.

Yeah. So again, it sounds hard. Uh, [laughs] I mean, it's still an engineering challenge.

No, I want to... No, I want to stay corrected. I want, uh, to encourage people to like, you know, use quantized model. Mostly PTQ will, uh, work, like, you know, if you are like looking at like 30B, yeah, it should work out of the box.

There are so many tools right now, like ModelOpt, like U- Unsloth has tools.

Mm-hmm.

Uh, Hug- Hugging Face in the ecosystem. Tons of tools, right, to, to make these big, these big models small. Uh, y- you know, something that I, I wanna pick your guys' brains about is ar- architecture for models in like the Llama era of, let's call it open AI, right?

Which is like, uh, every model was like the same. You know, the architecture was basically the same. The kinds of things that you saw in the guts of the model were the same.

And now we're entering like a very cursed era of technology, right? Where, uh, you know, e- everyone's doing the architecture just a little bit differently.

Yeah.

We're using this hybrid attention. Uh, they're using this, uh, you know, linear attention, uh, you know, you know, variant. Uh, you know, uh, uh, we're, we're be- we're exploring a lot and we're trying a bunch of new things.

How has that like shifted the difficulty of quantization now that it's not just like one problem repeated with different, uh, you know, you know, numbers of layers? Like i- is that something that is...

Makes it difficult to keep up with? Maybe, maybe Parth, uh, you know, from, from Ollama's perspective, like how hard is it to keep up with this?

Yeah. Um, there's kind of two facets to it, I'd say. Uh, the first is actually just the model implementation itself. Um, there's, you know, been times where a model lab would come to us early and we're kind of working with them to implement the model, uh, beforehand.

And we do this except, you know, they come and sometimes there's like five different variations of a model and, you know, we need to have them all working. So the implementation's one side of it.

Um, and I'm sure other people also have to put a lot of work in it. But the other kind of, uh, other side is you kind of have to run through the quantization bit and seeing, you know, kind of which one works best.

And at Ollama, we kind of do a UX thing of like giving a default, uh, model quantization for most things, uh, for most models. Um, and a big part of that is actually, you know, us spending the time, one, quantizing it, but then seeing if it actually works well with like different harnesses and, you know, is it

actually usable after. And so we find that sometimes when you have a very small parameter size model, um, you don't get like great quantization after that. Um, so we sometimes leave it in higher precision, um, as a default just because we actually want people to have a better experience, uh, versus, you know, quantizing it down...

Quantizi- yeah, quantizing it down to too little of a precision, um, and not having the model actually work well. So it's always a challenge, um, both from like the implementation perspective, but then actually, you know, you running into the quantization bit and making sure it still works correctly.

And, and Daniel, like is it harder to do quantization now that like everything is some hybrid or-

No.

-linear variant-

No

... or, a- and it's also all like sparse or variations on sparse MoE? Like how much harder is it today than it was when it was everything was just Llama all the way down?

Yeah. Like in the olden days, you know, every model was dense.

Yep.

The Transformer++. So it's called Transformer++ architecture. You know, it's an old Transformer, okay, plus RMS Layer Norm, plus some extra tricks. That's called Transformer++. And then now it's like, "Oh my, it's like Transformer+++, and then plus this thing, plus that thing, minus this thing, minus that thing, a different activation function, linear attention here, sliding wind- window attention."

You know, how many layers are sliding window? How many layers are global? Or let's delete global, do something else.

That's-

Blah, blah, blah, blah, blah. Um, you know, everyone likes to do their own thing and, you know, they like to compare, you know, like, "Okay, this one does better for long context.

You know, this one does worse for long context," or something like this. So there, there's always like reasons why they like to change the architecture. Um, you know, some folks even change some of the, you know, Layer Norm epsilons.

Like, you know, change one E minus five to one E minus six. Okay, which one's better? And so on. So they do a lot of ablations. You know, they do a lot of testing.

You know, this one seems to be better than this one. Um, and yes, it has complicated-

Compression and quantization dramatically. Um, you know, you have your old heuristics. Okay, this works well for, for this model. But then when you go to the MoE world, oh, you can quantize the MoE layers to, like, one bit, and it doesn't break.

Um, but then, you know, when you go to the linear attention world, you cannot quantize the linear attention layers. So if you quantize the linear-- we found that if you quantize the linear attention layers, okay, it looks like it's doing good, but then when you do long context benchmarks, you know, when you actually use the model in

real production, it becomes gibberish. Um, and so, like, there are some layers you cannot quantize with these new architectures. Some layers you can s- you know, quantize very low to, like, one bit.

You know, you can even delete some layers if you like. Um, and so it's like these new architectures complicate the process. Um, but to be honest, very happy with this because we need more different architectures.

We don't want everyone to be, like, thinking the same way. And, you know, open source has been ve-- you know, the open model er-era has been, like, there's so many different architectures, and it's very good to have, like, you know, a variety of different opinions and architectures.

Yeah.

I mean, that's, that's dope. Yeah. Hell yeah. Uh, I, we, we got about five minutes left.

Question.

Question.

Can we ask questions?

Uh, I g- I, I wanna get one more question with these guys, and then yes. Uh, okay, so compression's an art, not a science right now. Uh, w-well, it's a, it's an, it's an artisanal science, let's say.

Uh, but where is it going? Uh, you know, what, what does, what does compression look like, uh, in six months, in 18 months? May- We'll just go-- we'll start with Merve, and then we'll, we'll, we'll do a loop around.

Can we start from someone else? [laughs]

Yeah, sure. We'll, we'll start... [laughs]

Then you would you like to go?

Okay. Yeah, sure. Um, so-

Curious

... I think the way-- what we've seen so far is compression being so critical for any model launch that comes around. So it seems that model labs are starting to think more about it as well.

Um, the Unsl- folks at Unsloth do a phenomenal job. Fingers crossed they keep putting some great stuff out. Um, but more than that, I think because of, you know, the model architectures changing and kind of this awareness that model labs are having, we're starting to see more things like QAT, uh, come out from the labs themselves.

And I'm sure, like, there's ways to push even that further, but I think it's gonna be a mix of the labs kind of becoming a little bit more interested, but also the community kind of doing the great work they already have been and pushing that further.

So, Otan.

Can go now that I thought about the question. [laughs] So bas- um, what I think is most of... So previously, we were just running models on servers and stuff, but I think we can just finally push the edge because, like, there was this increasing demand for privacy and everything, especially for, like, sensitive data, personal data, and so on.

So, like, I see compression being a super hot topic, and, um, we are developing a lot of cool stuff with llama.cpp, so I would like, I would like it if you could stay tuned for that, um, so that it runs, like, everywhere.

Um, so I think I see the, the... So previously, I saw that the-- we were constantly scaling the model s- model parameters and then the data diversity, and then going down.

I see it as, like, going even further to the phones and stuff because it wasn't working. Like, we tried a lot, and then it wasn't working. I see intelligence going to phones thanks to the quants and everything.

So yeah.

Going to phones. Let's go. [laughs]

Yeah. Okay. So the way I think about compression, uh, the whole space is going to go more broader. So we've focused this discussion mostly on weight compression. So, uh, okay, going back to FP4 once again, uh, so it also do weight compression and, uh, math acceleration because it, it do the, uh, gem in four bit.

So, uh, yeah. So for-- in terms of weight compression, we might be able to go to, like, one, maybe two or three bit more. But w-w-in terms of, uh, quantization alone, we might be, like, close, like, close to the Pareto optimality.

Uh, yeah, let's, let's see. Uh, then there are more, like, you know, c- more type of compressions. So KV cache compression, right? So yeah. So people are still mostly using eight bit, uh, four bit mo- Large models retain that quality very well, but smaller models, we see some drop.

So yeah. So looking forward to KV cache, uh, maybe compaction plus quantization, uh, like pushing, uh, the long, uh, horizon reasoning, uh, broader, then sparsity. So, uh, so, so okay, so by the way, sparsity is, uh, has been part of NVIDIA hardware, but it has not been, uh, like, broadly adopted.

Uh, that is because, um, quantization does not degrade accuracy that much, but spa- sparsity causes accuracy degradation a bit more. So in Rubin, there is this cool feature called dynamic activation sparsity, so it can, uh, improve attention math, et cetera.

So yeah. So looking forward to that. And then coming back to, like, you know, all these heterogeneous architectures, right? So with each release, the, uh, particularly the attention architecture is getting more and more complex.

DeepSeek started it. I blame them. They started with MLA. Now, like, you know, sparse attention, index attention, like, you know, lot of skips, uh, softmax. Yeah. So it's getting broader, and yeah.

So it is part of this process where we make models cheaper and it, and they are, they are having compounding effects, right?

Perfect. So it's, so we're gonna quantize more things, uh, more is basically the idea.

Yeah.

That's, that's pretty dope. I, I don't, I don't mind that. Take us home.

Yeah. So I think, like, the world, we're gonna get more and more bigger models. Um, and you know, it would be very cool if we can run them locally on our phones, you know, on your laptops with your GPUs.

Um, and you, like, imagine in a world where, you know, the best frontier models will be able to run on your computers. You know, that would be so cool.

Um, you know, now you can control your own destiny. You do not need to be, you know, controlled by some model labs, and now you can do whatever you like on your computer, right?

You can do your own fine-tuning. You can customize it. Um, you can, you know, everything becomes yourself. You, you own it. Um, and so, like, you know, I see a world where the world in the future- All of the intelligence will be fully democratized, you know, via GPUs, via the phone, you know, any single hardware.

And you will, you will have, you know, very capable AIs on your laptop, on your local devices running, you know. And it's also gonna be efficient, right? You don't want your computer to like, you know, lose battery and die.

Um, but I feel like, you know, with all these techniques, um, you know, we can have a future where AI is fully democratized, and that's, yeah, that's where I see it.

Yeah.

Not a bad future. Uh- [audience applauding] Again, we can't do it without any, all of you in the room, so big round of applause for the, the, the panel here. [audience applauding]

Thank you so much, guys. We, we have one question. We'll do one question.

All right. So you talked about all the different permutations of craziness that are happening in the model space and the proliferation of various techniques to compress, right? Um, but we often...

You s- you find some weird Frankenstein model out there that you wanna try out, but you have no clue how well it actually performs on the original benchmarks of the model before all the modifications occurred.

So I'm just curious, like, is there any good resource out there-- Maybe this is a job for Hugging Face. Maybe this is a place they're gonna go into. But like, is there a good resource out there that maybe runs all these benchmarks again on these models again to see how well they perform after all the freakish things

were done to them to see how well they're going? And is there a place where we can find like matrices or summaries of like what the best modified model is for this or for that, and, and et cetera, et cetera, right?

I would love a resource like that. I'm just curious. Is anybody doing that?

Yeah, if you find so- something like that, let me know. Yeah. [laughs]

Yeah. I, I think, I think that's it. Basically, the question is: What is the resource I could look at to find out what is, you know, the-- of the suite of crazy quants or compressors that exist for a model, how do I find the ones that are good at the things that I care about?

Uh, is anyone doing that? I think right now it is not being done comprehensively. Uh-

We, we do have some-- So for some models, when we do our dynamic quantizations, we do release benchmarks, um, and we do not do-- So generally, what our view is accuracy benchmarks can be very complicated because you have to do sampling, how many trials do you need to do, and you have to average.

So there is another better method in our view, um, KL divergence. So KL D is the distance between the unquantized version, which is bfloat16, and your quantized version. And you can calculate some sort of distance between the quantized version and the unquantized version, and your goal is to make the distance zero and the size smaller.

Do you do it over ou- output logits?

Yes. So you check the output logits. You pass some sort of calibration data, you shove it in-

Oh

... and then you have some-- You check the output logits between the bfloat16 and then the main, you know, the quantized version.

The quant-

And then the goal is make this distance zero-

KL D

... um, and you make the model smaller.

That's KL D. Yeah, yeah.

Yeah, that's KL D. Um, and so-

KL D. Uh-

Mm-hmm

... you can check out the paper, Accuracy is Not All You Need, if you wanna learn more about that one. [laughs] That's it for us, guys. Thank you so much again to our excellent panel.

Thank you. [audience applauding]

Thank you. [upbeat music]
