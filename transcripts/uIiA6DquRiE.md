# Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth

Source: https://www.youtube.com/watch?v=uIiA6DquRiE

Upload date (publisher UTC): 2026-07-17

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/71/7115eba117e745a156f9d47b3c61b8fcf27ff4ea6680b8487a146dcc50031f00.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.20s] [upbeat music] Hello, everyone. Um, yeah, thanks so much for coming today.

[16.85s] Much appreciated. Um, yes, I'm Daniel. I'm from Unsloth. Uh, my brother is also here today. Um, but yeah, like, you know, thanks for coming. Um,

[26.72s] so for you folks who don't know us, um, so we actually, you know, we're one of the largest distributors of language models and diffusion models as well. So we don't just do language models.

[35.16s] We upload our models to Hugging Face. Um, and you know, we're on the-- I think we're number ten or something on the... I don't know. I don't, I don't remember.

[42.84s] But anyways, we're on the list of the top organizations on Hugging Face. Um, we have over three hundred million total downloads. Um, so definitely check us out on that.

[50.42s] Um, you can run like, you know, DeepSeek, GLM, many other models, and we quantize them down using dynamic quantization. Um, so you can run them on your local computer.

[60.54s] Um, we also do many bug fixes for open source models. Um, so, you know, we, you know, fix many bugs in, you know, OpenAI's, gpt-oss, um, you know, Meta's models, um, Google's models, DeepSeek's, um, many other models, we fix bugs in them.

[74.24s] Um, and so, like, you know, they have many issues sometimes, and then we post about them on Twitter. Um, you know, we post about our findings. Um, so, you know, m-most of the open source models that you probably guys have used, um, are most likely fixed by us.

[87.99s] Um, and yeah, like we collaborate with everyone in the entire world, um, on, you know, model releases. Um, yeah, we also collaborate with hardware providers and, you know, we really appreciate the collaborations with everyone.

[100.16s] We also don't just do model fixes and bug, you know, bugs. We also introduce new features, and we also like, you know, do fixes for the entire training stack.

[108.78s] Um, for example, we introduced something called Async Gradient Checkpointing, which is used by many organizations. Um, we also introduced Flex Attention, which is used by many folks. Um, and we also fixed a gradient accumulation bug fix, um, which increased accuracy by one to three percent, um, across the entire training stack.

[125.20s] Um, so we don't just like, you know, do bug fixes for models. Um, it's also like, you know, whole training stack, um, fixes and stuff like that.

[134.84s] So today, you know, the workshop is quite long, um, so there will be multiple sections in the workshop. Um, and so after each section, anyone can ask a question.

[143.16s] Um, and so, you know, please, I guess if... I'm not sure if there's a microphone, but if you can raise your voice and you're gonna ask a question, you know, I'm more than happy to answer them.

[151.12s] Um, but you know, the first section we're gonna be talking about is the state of AI. So where is currently language models, AI models, where are they at currently?

[160.34s] Um, so I'm not sure if everyone knows the METR plot. Um, so this METR plot shows the time horizon of, uh, models. Um, if you can-- You know, every single task if it takes a human sixteen hours, can a model, you know, finish that task?

[176.40s] Um, and you can see on this plot, you know, Claude Mythos, you know, preview is very good. It can do t-tasks that humans can do that take, you know, humans sixteen hours.

[186.50s] Um, you know, Opus 4.6 is also there. You know, all the other models are also there. And so, you know, this plot is very good because it symbolizes the AI models are getting better and better and better over time.

[198.98s] You know, recently with the launch of, you know, GPT 5.6, um, you know, just, well, their preview model, um, you know, just on Friday, um, you know, I put the plot.

[208.34s] So they didn't-- So METR didn't actually update their plot, um, because they said that the results were not trustworthy enough. Um, but you know, I just put it on the plot.

[216.44s] Um, and so you can see that GPT 5.6, you know, is around, you know, Opus 4.6 level, I guess, with large confidence bounds. Um, so it's very, you know, uncertain about the capabilities of the model.

[228.90s] Um, however, if you include cheating, so if you include that the model sometimes likes to cheat on some of the tasks, then it actually goes to two hundred and seventy hours.

[237.84s] Um, so it directly-- And you know, i-if you look at the Y-axis, I actually did a disjoint graph. Um, so the Y-axis is fifty hours skipped to two hundred and fifty hours.

[248.34s] Um, so if you can imagine, the graph is actually very skewed. Um, at-- W-when I, like, made the graph, um, GPT 5.6 was, like, a very big outlier. Um, so I had to, like, compress the graph.

[257.42s] Um, but this only, you know, this graph only works if you consider that GPT 5.6 cheated on some of the tasks. Um, and so we'll be talking about, you know, why AI models cheat and how do we like, you know, solve these issues.

[269.90s] Um, but yeah, this plot is very useful to showcase the capabilities of these models.

[275.70s] So previously, this is fifty percent, you know, if you c- if a model can complete the task with fifty percent of the ch-- you know, of the time, so a fifty percent accuracy.

[284.28s] If you want to actually one-shot the model, so you just ask the model, you know, implement X or implement Y, um, and you want the model to do very well, then you want to look at the eighty percent success rate.

[294.78s] If you look at the eighty percent success rate, it kind of drops quite a lot. Um, so you can see that previously, Mythos is around sixteen, seventeen hours. Um, now it only can do three hours.

[306.84s] So if you prompt a model and you want to have like a one-shot example, you know, you just trust the model by just o-- asking it, you know, implement, I don't know, PageRank or something.

[316.48s] You know, implement some sort of RAG system. You know, fine-tune a model or something like that. Um, it can only do a task that will take a human three hours to do.

[323.64s] Um, and so th- so that is a problem with AI models. Um, generally speaking, if you wanna use AI models very well, you need to prompt it at least like, you know, five times or something.

[332.60s] Um, and each of those times, assuming they're independent, um, the success rate is much higher if you prompt it many, many times. But you can't just call the model once and expect it to do wor-- to do well.

[343.22s] Um, you need to call it multiple times. Um, and you can also work out the probability of it, like, succeeding. You know, if the model is fifty percent accurate, um, then it will be fifty percent failure.

[353.50s] Then it's one minus zero point five to the power of five or something like that, you know, if you do five turns, and then your success rate jumps to like ninety-seven percent or something.

[361.38s] Um, so you need to call the model at least five times for it to be very effective.

[368.22s] So previously, these are linear, you know, this is a linear trend. You know, on the Y-axis, it's just-- it's not, you know, it's just linear. Um, if we log it, you know, if we log the Y-axis, you can see that it's more exponential progress.

[384.46s] Um, so it's actually a straight line fit to the entire progress of AI models on the METR Time Horizon, um, you know, benchmark. You can see that, you know, it's very clear the AI models are getting better and better over time.

[395.86s] Um, I also added, you know, GPT 5.6 with the cheating and no cheating, and also Claude Mythos are, you know, accentuated that. And you can see, I-- you don't need-- now you don't need to like, you know, fake the Y-axis.

[406.90s] You know, you don't need to do like a disjoint Y-axis. Um, if you do that, you can see that, you know, models are getting better over time. Um, and supposedly, you know, if this trend continues, these models will get better and better and better, better, and much better.

[421.18s] Um, yeah. So, so the question is, if the trend continues, you know, that's the fundamental question.

[426.98s] Um, and it's not just, you know, one specific task for this benchmark that you can see that models are getting better over time. Across all benchmarks, models are getting better over time, right?

[437.36s] So like, you know, GPQA Diamond, you know, it's kind of plateau-- you know, it's kind of already saturated as a benchmark. But o-over time, you know, it does very well.

[444.54s] You know, every single benchmark you see, models are getting better, right? LiveCodeBench, you know, maths algorithm-- uh, maths tests. Um, you know, even Tesla's, you know, you know, self-driving, I guess, is also has like a doubling time of seventeen months.

[458.01s] Um, so every single seventeen months, the models will get better and better. Um, you know, double, double their capabilities. Um, so over time, all these models in every single subject, you know, every single

[470.36s] area, it will get better. Um, so I guess the main question is, you know, if we assume every single subject, every single area, the models get one hundred percent-- like, you know, approaching one hundred percent accuracy, is this AGI?

[483.72s] Um, so that is one of the fundamental questions that people ask. You know, if we just get better on benchmarks, um, is this AGI? Um, what happens if it get better on all benchmarks?

[493.32s] You know, every single benchmark that huma-humanity has created, it just gets better on all of them. Um, yeah. But so this is a, you know, very good plot sh-- well, I guess, chart showing all of the different types of benchmarks, and they all get better over time.

[509.02s] Everyone's favorite, I guess, artificial intelli-- uh, you know, Artificial Analysis benchmark showing, you know, artificial intelligence getting much, much better over time as well. You know, Fable, I guess, is, I guess the best for now.

[519.58s] Um, ah, although not everyone can access it currently. But anyways, it's for now, it's the best. Um, and you can see over time that, you know, these models are getting better over time as well.

[529.20s] Um, and you know, like this plot showcases, um, a very useful indication, you know, like how do we like, you know, benchmark-- you know, is this benchmark actually good, um, in terms of like, you know, showcasing the capabilities of models as well?

[541.54s] Um, and we'll be also discussing about that as well. Um, on the other hand, yes, models are getting better over time. Um, but there are some things which models are not very good at still.

[552.10s] For example, long context is not doing very well. Um, so you know, most models you might say, okay, Gemini has one million context length, you know, GPT has one million context length, Claude has one million context length.

[562.38s] But should you actually use all of the one million context length? Um, so there are actually benchmarks to showcase that if you use, for example, GPT 5.5, um, you know, if you use five hundred and twelve K context, your accuracy reduces to fifty percent.

[576.42s] Um, so if you use, you know, five hundred and twelve K context, you will only remember fifty percent of the facts that you wrote in the previous context. Um, so maybe that's not a good idea to use the full context.

[586.76s] Um, you can see Opus 4.7, um, 4.6-- uh, 4.7 is the very last orange line. Um, so at the context length of two hundred and fifty-six K, it goes to zero percent.

[597.44s] Um, so this might be a benchmark flaw. Um, so maybe don't trust the benchmark too much. Um, but it's good to look at the benchmark overall. You know, where is the model's capabilities for long context?

[607.84s] Um, the blue lines are highlighted are open source models. You know, DeepSeek, GLM 5.1, other models. Green is Google's models. Um, but you can see in general, you know, models are-- models definitely do degrade over long context.

[622.36s] Um, so if you, you know, for example, if you set like a, you know, automatic compaction area, I would not suggest you to use all one million context length.

[630.70s] Maybe maximum six hundred K or something. Um, and then compact it and then continue your, you know, coding session. Um, but I would-- yeah. But in general, you know, this plot shows that long context still has a very long way to go.

[643.20s] Um, and if we want to have long context, you know, capabilities, um, labs, I guess, will have a lot of time to fix this problem.

[653.96s] Yeah. So another plot is, you know, just showing open source versus closed source. So open source still has some way to go for this, you know, long context. Um, so open source is blue line, and the black lines are like, you know, closed source models.

[666.88s] Um, and you can see in general, open source does okay, but there's definitely much more room for improvement. Um, I guess compared to Opus 4.7, it's better. Um, but you know, maybe this benchmark does need-- maybe there are some flaws in the benchmark as well.

[679.72s] Um, yeah. But overall, you know, this plot shows that long context definitely still has more room for improvement.

[688.56s] And also, you know, like if you looked at the plot previously, you know, this METR plot, um, I'm not sure if you can see that before o1-preview, there is actually a plateau of performance.

[699.80s] Um, and so if you can see, you know, GPT-4 to GPT-4o, there's not that much performance improvement. Um, and so this timeframe around one year, um, was when, you know, the labs were confused on what is next.

[713.32s] Um, you know, before o1-preview, which showed that reasoning was very important, they didn't actually know what to pursue next. Um, and so for one year, the models kinda plateaued.

[722.66s] Um, and so I call this the intelligence plateau, the hypothesis that, you know, you know, assume that we ne-have never have discovered reasoning. Then maybe AI models would have, like, plateaued.

[733.96s] Um, but because we have discovered reasoning, you know, we have shown that models can do reasoning capabilities, we have continued the trend continuously. Um, and so normally, I don't know if this is, like, luck, um, or if this is a self-ful-fulfilling prophecy.

[747.20s] Um, so I don't know if you guys, you know, the Moore's Law. Um, you know, Moore's Law has continued, um, not because of the law, but because people know that it must continue, and so people invest money into the resources to make the law continue.

[760.18s] Um, and so this kind of, like, shows that, you know, we might have been in a world where models have stopped improving. Um, but you know, with the launch of o1-preview, you know, I guess models have went back to trend.

[774.00s] In fact, I made a plot showcasing, you know, assuming we did not discover reasoning or o1-preview, um, then the black line was the supposed, you know, capabilities of the, the models.

[786.42s] You can see I made it into a S shape, um, like a, you know, um, a sigmoid-type shape. Um, and if, you know, if we didn't discover reasoning, then models definitely would taper off in terms of capabilities, right?

[797.26s] We'll only have a model that's as capable as Claude 3.7 Sonnet, I guess, or o1 or something like that. Um, but you know, luckily, because of reasoning and this new paradigm of scaling, you know, the green line is the new scaling law.

[810.20s] Um, and you can see previously the black line, the doubling time was actually around seven months. So every single seven months, the capabilities of the models double. Um, but now it has shrunk to three point five months.

[822.00s] So every single three point five months, you just need to wait three point five months, and the models will get double better, right? Better by two times. Um, and that's quite striking, I guess.

[831.56s] Um, so the main question, though, is will the green line continue as a straight line? Um, that is the fundamental question that labs are still struggling on. You know, what happens if the green line again, you know, the green line again goes as a S shape?

[845.20s] You know, that's possible, um, but you know, we don't actually know if this will happen. You know, if the green line will continue scaling, you know, going all the way up to infinity, I guess, or would it be like an S shape?

[856.72s] Um, and this is, you know, many researchers are, you know, I guess, have sleepless nights. You know, what is the next-- you know, what is the next thing afterwards, after reasoning, after o1?

[866.24s] You know, what is the next thing afterwards? Um, and you know, many researchers will need to, like, you know, I guess, think about this. Um, yeah. But you know, this plot is very-- you know, this is one of my favorite plots because it shows that, you know, AI progress can continue over time with new ideas and innovation.

[883.92s] Oh, yes. So does anyone have any questions for the first section? Um, yes.

[888.58s] So we came all the way to one trillion, right? Do you think the next jump, if we need-- Do we need like ten trillion parameters when we will see the jump, or hardware will be the limitation at that point?

[900.38s] Yes, that's a great question. So the question was, you know, models were currently at one trillion parameters. Do we need to go to ten trillion parameters or more for models to be even more capable?

[909.70s] Um, so the scaling laws does say that, you know, if you multiply the parameters and the data size, um, generally speaking, this number, if you increase the number, you will get-- the models become more capable.

[920.74s] So yes, you can increase the parameters by ten times and in general, your performance will increase. Um, however, the view is there is gonna be diminishing returns. Um, I feel like, you know, it's not just the model size times the dataset size.

[935.66s] It's actually a ratio, um, some sort of like power law when you multiply them. So you actually get diminishing returns over time. So yes, you're right. If you wanna have actually-- I'm not sure the exact law, but if you wanna have double capabilities, you do need to ten times the parameters.

[948.92s] Um, and then if you want another double, you have to ten times it again. So it's one to ten to one hundred trillion parameters. Um, if you want-- Maybe that's not a good way to scale.

[959.92s] Um, maybe instead, you know, instead of making a one hundred trillion parameters, some sort of new algorithm or new architecture could solve that problem. Um, but you're right. Like, if you're a lab, you want to do something easy.

[974.06s] And so the easiest path is to just make a ten trillion parameters. Um, but I would say, like, you know, maybe a new algorithm would be better. Um, yeah.

[984.28s] Yes.

[985.50s] Any other questions? Yes.

[987.80s] So do you do think that we are approaching the limitation of next token prediction?

[993.70s] That is a good question. I would say that for next per, next token prediction, it's very powerful because you can essentially--

[1001.98s] The human language is extremely powerful, and it doesn't have to be human language. It can be, you know, maths, coding. You can just predict the next word. And in order to predict the next word or token, you need to know everything about that token or that word, right?

[1015.00s] So like, I think Ilya was talking about like, you know, Ilya Sutskever, he was saying like, you know, you need to have-- you need to make a world model in the model in order to, like, predict the next word.

[1023.86s] Um, so I still think next word prediction still has a lot of way to go. For example, if you see this plot, you know, if we didn't have reasoning,

[1031.86s] I guess, okay, maybe it would, it would have plateaued. But because we have discovered this new methodology, you know, reasoning and trying to, like, scale even more on next word to, you know, next word prediction, we have, you know, went back to trend.

[1043.22s] Um, I feel like-- So the main question is, if we don't have next word prediction, what is next? Um, that is a fundamental question. Most...

[1052.06s] I mean, I'm not sure, like, you know, I'm not certain what's the, what's the next thing. I feel like next word prediction is just extremely powerful because it's very easy to formulate and you can just like, you know, you can have like, you know-- Because attention is very powerful as well, you can have, you know, this special

[1066.92s] causal attention mechanism, and it's very efficient to train. So I'm not sure. I think the main question is, I'm not sure what's next. Um, I guess researchers will like, you know, they're trying to scratch their heads, you know, w-what is next afterwards?

[1078.68s] Um, yeah. I, I, yeah. Yes.

[1082.18s] Just a follow-up on it. Do you feel like we are in the same era, like how we were in with the LSTM and when attention came out?

[1088.78s] Mm.

[1089.40s] Right? So attention, like we don't know-

[1096.67s] Yes, that's a fair follow-up. So, um, you were mentioning how it's kind of like LSTMs or in the old AI world, we don't know what's next afterwards. Um, that's a fair point.

[1104.91s] I feel like-- So like, you know, previously, this example, right? So after GPT-4, it was just pre-training, some s- you know, supervised fine-tuning, some RLHF, you know, some RL.

[1116.59s] Um, and they waited one year until o1-preview. So in this one year of fog, you know, the fog of war, we don't know what, what was next. And so researchers, you know, were scrambling, you know.

[1127.29s] Do we do the reasoning process? Do we make pre-training better? Do we make the model bigger and bigger and bigger? You know, they tried all these experiments. Um, and

[1137.05s] reasoning was the one that won, I guess. Um, but I think, like, I think the main question is: Is the green trend going to continue? At the current time, it looks like it's continuing.

[1147.53s] Once we see models starting to taper out in intelligence, you know, in capabilities, then we'll go back to the, you know, olden days of, like, you know, this one-year waiting period.

[1156.63s] But I think for now, these models seem very powerful. Um,

[1160.91s] yeah. So, like, I'm not sure if this will-- I mean, if you look-- Okay, if you squint at the plot, I guess maybe we're tapering out. Maybe. Um, I-- let's not consider the GPT 5.6 cheating example, right?

[1170.55s] Let's remove that from the plot. Um, but you can see the GPT 5.6, Mythos, you know, 4.6, they're kind of all--

[1178.09s] I guess they're kind of tapering. Um, so maybe as a-- I mean, I don't know if we-- someone wants to bet on this, but, you know, maybe models have tapered out.

[1185.82s] But we're not sure. So we shall wait a few more months and see. So let's wait three point five months. If we wait three point five months and see the models do not improve, then we have tapered out.

[1195.17s] Um, but remember, we only need to wait three point five months, um, so then this law will fail. In fact, if you wait seven months, if you wait seven months, so double of the time, and models have, you know, just assume, you know that dotted line?

[1206.89s] The-- If, if the models just follow the dotted line, okay, then we have tapered out. And I would agree that, you know, we'll have to design something new in v-- you know, make some new invention or something like that.

[1215.99s] Um, but for now, you know, for now, it looks like it's doing fine. Um, yeah. Okay, next section. Um, so every single section we, we can have questions, so you can ask as many questions as you like.

[1226.29s] Um, the next section I'm gonna talk about is open versus closed models. Um, so Artificial Analysis has this very cool plot showcasing the performance of open source. So open source is the blue line.

[1237.79s] Um, so open source is the blue line, and closed source models is the black line. Um, and you can see that open source does lag. You know, open source definitely lags over time.

[1247.89s] Um, another very good benchmark is called the Weird ML Benchmark. Um, this also shows that open source models lag closed source models, right? The blue line is open source models.

[1257.71s] The green line is closed source models. Um, and you can see over time, you know, the x-axis is release date of the model, and the y-axis is, is performance.

[1267.48s] And you can see that open source models kind of lag closed source models.

[1272.59s] And why the Weird ML Benchmark? I'm not sure if you folks actually know about this. Why the Weird ML Benchmark? Um, it seems like the Weird ML Benchmark is a very good indicator, better than other benchmarks.

[1283.39s] And the reason, the reason why is, you know, previously I mentioned, you know, previously this graph, right? Reasoning-- the reasoning models are the green line, and then the black models are the non-reasoning models.

[1293.98s] And you can see that reasoning models double, you know, reduce the time of doubling time to three point five months. Previously, it was seven months. Um, interestingly, on the Weird ML Benchmark, these reasoning models didn't actually do better.

[1307.33s] It didn't actually change the trend. Um, all it did was make it slightly better. Um, and so this Weird ML Benchmark seems to be more robust. Um, and that is why, you know, this benchmark is very useful.

[1318.87s] Um, in fact, if you go on the Twitterverse, um, before GLM 5.2 got released, um, most, you know, most of the Twitter people said, "Oh, you know, DeepSeek, you know, Deep-- if you see very-- if you squint..."

[1330.03s] Okay, I, I think I have a plot. Oh, yes. If you squint, DeepSeek and Kimi are in that little corner over there. Um, you know, DeepSeek, those three models, the three whales are DeepSeek, you know, Flash, DeepSeek Pro, I think one of them's Max Mode or something like that.

[1344.27s] Um, and also Kimi's over there as well. So before GLM 5.2 got released, you know, on the Twitterverse, everyone kept saying that open source models are much worse than closed source models, right?

[1353.69s] They're not lagging. You know, they're not just lagging. They're much worse because of this benchmark. Um,

[1360.91s] in fact, if you look very closely of the Weird ML Benchmark, all of the top models are closed source labs. You know, like Fable, you know, GPT 5.5, whatever.

[1370.25s] You know, all of these are just very-- You know, it shows very clear that open source models are not doing very well in terms of this benchmark. Um, until GLM 5.2 came along.

[1379.99s] Um, you know, number fifteen is GLM 5.2, and it shows that actually open source has came back. Um, and GLM 5.2 kind of shocked the world, um, that, you know, I guess open source has not died.

[1391.77s] Um, and you know, DeepS-- Yeah. So in general, this worked very well. You know, DeepSeek-- You know, GLM 5.2 showed that, you know, open source does very well still.

[1403.25s] You can also filter out by country. So by country, you can see that the black line is United States, you know, the US, uh, models. Um, the dark red line is the Chinese labs.

[1414.43s] Um, and you know, there's other labs as well, um, you know, French, South Korean labs, and stuff like that. Um, but you know, over time, it shows that these models, um, you know, the US labs seem to do very well over time.

[1425.55s] You know, they're, they're always at the frontier. And then the Chinese labs like to catch up over time.

[1432.33s] Previously, you know, I mentioned, you know, the, um, you know, the plateau before, you know, before o1-preview got released. If you actually look at this plot, um,

[1441.49s] there is something called the open source drought. Um, so after o1-preview got released, open source labs did not know how to replicate o1-preview. They have never-- You know, they don't know what is reasoning.

[1454.07s] So I'm not sure if you-- Okay, this is a few years back. Um, but on Twitter, you know, OpenAI kept talking about, "Oh, you know, o1-preview was extremely powerful."

[1461.59s] Um, you know, every single tweet you see every single day, you know, they show that o1-preview was very powerful. Um, and so for one, I think it was six months to eight months, um, open source models, open source labs- They got confused on what to do next.

[1475.16s] Um, but then as everyone knows, DeepSeek-R1 came along. Um, and they showed that even for open source models, you can train these models to do reasoning, GRPO, um, reinforcement learning, and it does very, very well.

[1488.96s] In fact, if you take this plot, you know, the, the black line minus the blue line, if you just minus it, you get this plot. Um, and you can see this is how many months behind open source is.

[1499.28s] Um, and, you know, over time, um, you can see like, you know, after o1-preview got released, um, you know, it kind of skyrocketed. Um, you know, the, the open source models were very, very lagging in terms of, you know, behind closed source models.

[1513.90s] Um, and so like when DeepSeek-R1 got released, then the open source labs knew, okay, we can also do, uh, o1-type reasoning. Um, and that is why recently, you know, the pa-- the time between closed source labs and open source labs have started decreasing again.

[1529.64s] Um, yeah. So this is slightly outdated. This is like May. Um, so I think now it's actually four months with the release of GLM 5.2. It's around four months now.

[1538.90s] Um, so open source labs lag behind closed source labs by around four months.

[1545.22s] There is actually a very nice plot, you know, doing some sort of regression, so some sort of like trend extrapolation. Um, according to this plot, um, if you extrapolate the trend, by December this year, open source models will one hundred percent catch up to closed source models by this year, December.

[1560.54s] Um, but you know, who knows? I guess maybe, maybe open sou-- maybe we can have an open source model as powerful as the best closed source model by December, um, you know, if this trend continues.

[1573.92s] Um, so I guess the question is: Will the trend continue? Um, it's always about will the trend continue? Um,

[1581.80s] and you know, may-m-maybe-- most of you maybe may know that, you know, open source-- some of the open source improvements in technology, you know, improvements in capabilities are via distillation, you know?

[1592.06s] So some of the open source labs, what they like to do is they like to call the models, you know, call the frontier models like Opus or GPT and then use the traces to train your model.

[1601.12s] Um, so this is a common methodology that labs like to do. Um, I wouldn't say this is a bad method, um, but it is a method that, you know, some closed source labs like to look down upon.

[1611.56s] You know, they like to stop... You know, their view is, you know, we should not allow these open source labs to like, do this training, um, and, you know, get away for free, I guess, in terms of training cost.

[1621.60s] Um, but you don't actually have to do this approach. Um, so most labs, when you do distillation, there are two different types of approaches. Um, the first approach is you need to have the logits.

[1631.58s] You need to actually have access to the full logits. Um, and unfortunately, most labs do not actually have that, right? So, like, labs will not give you the full logits.

[1640.40s] Um, instead you only get the reasoning traces that are summarized, um, and the final output. Um, and so these, you know, these open source labs are not just, you know, they're not just training on the, you know, Opus output, right?

[1652.84s] That's just-- that's silly. What they do is they use GRPO or reinforcement learning to recreate the traces. Um, and so because you ha- you have the final output, which is the answer, all you need to do is use GRPO and RL to create the reasoning trace automatically.

[1667.70s] Um, and so that's kind of how they train these models. Um, and so you don't actually need to like, access the logits or the weights of the model. Um, that's not necessary.

[1676.74s] Um, yeah. And you know, one of the most important factors of, you know, these large models is, you know, as the models get bigger and bigger and bigger, you can't run them on your local device anymore.

[1689.22s] Um, it's extremely complicated to run. Um, and so we do something called dynamic quantization, where essentially you take a model, you quantize them down to one bit. Um, a- but the trick is you don't quantize every single layer to one bit.

[1702.42s] You quantize some important layers to a sixteen-bit or eight-bit or something like that. Um, and so if you quantize the whole model down to one bit, you will get zero percent accuracy, right?

[1713.50s] Zero percent. Um, but the trick is if you do dynamic quantization, so if you look on the, you know, this is a three-bit DeepSeek model, um, a three-bit one.

[1721.42s] You get seventy-five point six percent, percent accuracy, a three-bit one. In fact, if you do dynamic one bit, um, you get fifty-seven percent accuracy. Um, so we show that, you know, if you do something called dynamic quantization, where you quantize the model down smartly, you can recover accuracy.

[1737.28s] Um, and this methodology will become even more important when models get larger and larger and larger and larger.

[1744.62s] If you plot the Pareto, you know, efficiency, um, there-- If you don't do dynamic quan-- If you do s-- you know, some other dynamic quantization methods, it does okay.

[1753.44s] Um, but we show that if you smartly choose the layers, it does even better.

[1757.44s] Um, I'm not sure if you folks have followed, but GLM 5.2, we also released dynamic quantizations for that. We showed that GLM 5.2 can quantize very well. So if you look-- I think this is-- Oh, this is an animation.

[1768.90s] Oh, it works. Um, but yes, you can show the animation. You know, you can see the animation, a one-bit GLM 5.2 model. Um, this is one bit. Um, and the one-bit model is literally eighty-six percent smaller.

[1782.30s] Um, so it's eighty-six percent smaller than the full one point five terabytes. Um, and it still managed to do very well on one of the prompts. Um, so it shows that the models are not dumb, right?

[1793.20s] If you make the model eighty-six percent smaller, it does not get eighty-six percent dumber. Um, it only gets fourteen percent less dumb. Um, and so it shows that, you know, if you do special tricks to compress the model, the model still works very well.

[1808.16s] Um, and we also compare to Opus, you know, we compare to Opus 4.8. We compare to GPT 5.5. And also, you have to notice that for GLM 5.2, I use high reasoning mode.

[1820.56s] You know, for Opus, it's extra high, and for, you know, GPT 5.5, it's also extra high. Um, and so like, you know, there are different reasoning modes as well, which we can also s-- um, see.

[1830.22s] Um, and all of these are one shot. Um, so we do not like prompt the model like, you know, fifty times or something. Um, this is just one shot directly.

[1839.82s] Okay. So the next, I guess the open source versus closed source section is done, I guess. Any other questions? Yes. Um, so the question was which parts of the model do we quantize to lower bits versus higher precision?

[1853.10s] Um, so in general, um, we did actually a lot of research on this. So if you look at the Qwen, the Qwen3.5 architecture, there are some layers which is the linear attention layers.

[1863.72s] Um, the linear attention layers should never be quantized. If you quantize the linear attention layers down, you will definitely suffer in long context. Um, so in general, the linear attention layers need to be left in eight-bit or sixteen-bit.

[1878.36s] Um, that's for example. Um, another, like if you look at the model layers, um, some layers can be quantized down heavily to one bit. Um, and the reason why is because these layers are kind of like filler layers.

[1891.46s] Um, and so they don't actually do anything. Um, and in order to check whether a layer does something or not, you do need some sort of calibration dataset. So you need, you need to have some sort of like representative data and pass it into the model.

[1905.46s] Um, and you can get, you can get the, um, outputs after each layer, and then you can see, okay, does this model at this specific layer, you know, does it change that much?

[1915.88s] Um, and if it doesn't change that much, okay, maybe just quantize the layer to one bit. Um, but if it does change dramatically, then you need to be careful.

[1923.02s] Um, you, you cannot quantize that down to like one bit or whatever. Um, so th- there are actually many-- We actually publish a lot of like blogs, research on this.

[1931.34s] Um, we show-- I think there was-- We also show, for example, you cannot quantize the vision layers down. If you quantize the vision layers down, you will make the model really bad.

[1941.16s] Um, if you give it a, you know, if you give it a picture of a train, it will say it looks like a beach, for example. Um, and so it's-- you should never quantize the vision layers, the audio layers, um, and only the language, the language model layers you can like quantize.

[1956.46s] Um, but there are many tricks in order to do that. Um, yeah. [muffled]

[1961.08s] Correct. So the question was, if you do distillation, um, you, you might have done worse on other topics, um, but you know only-- if you-- for example, if you just do coding, it will just do good in coding, and then the rest gets very dumb.

[1974.10s] Um, so that's a fair point. Um, so I think the, the main trick is you will need to do many, many, many examples. You call the model like, you know, ten million times.

[1983.40s] Um, and so like the trick is once you call the middle-- model ten million times with high diversity of questions, in general, um, by using the pre-training argument, um, the model will do well on other tasks.

[1996.30s] Um, so the reason why pre-training does very well, um, is because it has learned so many tasks that it can interpolate the missing holes. Um, for example, if you just tr-- if you just pre-train a model with just maths questions, um, assume you do only maths.

[2012.50s] Okay, maybe it's not gonna do very well, right? And it's not gonna do very well on every other task. But the trick of pre-training is it does maths, coding, law, you know, every single imag-- you know, every single topic you can imagine.

[2024.78s] And the trick is because it has so much knowledge, it fills the holes of the things that it doesn't know. Um, and so for distillation, you also need to do the same approach.

[2033.58s] You need to sample, you need to sample well. Um, so for example, instead of doing ten trillion tokens, sample, you know, like one percent, um, and then call the model.

[2043.56s] Um, yeah, so that's kind of how the labs are doing that. Um, that is a very good question. So instead of doing one-bit quantization, can you instead prune the model, like, you know, delete some layers entirely?

[2054.00s] Um, so in general, from our research, pruning does work. There is a very big problem, though. You need to retrain the model. You need to continuously train the model after pruning because you have deleted an entire layer.

[2067.78s] Um, and so if you delete an entire layer, you will need to do like, you know, QAT or further fine-tuning to push the other, to push the other weights to have more knowledge.

[2078.44s] So that is the only problem where if you delete layers. Um, if you don't delete layers, when you do, you know, dyna-dynamic quantization, it's called post-training quantization, so PTQ.

[2089.16s] You do not need to do any training at all if you do, you know, quantization. Um, but if you do prune the layers, you do need to train. Um, so that is one of the problems.

[2098.30s] Um, yeah. Yes, that's, that's a great question. So the question was, you know, because open source labs, you know, they use closed source models, the gap will never actually go to zero.

[2109.30s] Um, and so I partially agree. And so the main argument was labs, open source labs, the easiest way is to do distillation. However, you know, if you-- for example, if you were an open source lab, you would only use that approach to firstly enter the market.

[2125.34s] But as long term, you know, as long-term safety, as a long-term safety net, you will not do this approach. Um, instead as a, you know-- Instead, you will do, you know, for example, generate the answer, get the question, for example.

[2137.38s] You know, you will get data from Mercor or Scale or whatever, you know, have some sort of like large data labeling army or something. I don't know. Um, and so like in general, because currently some of the labs-- So they don't just do distillation, right?

[2150.14s] So they're not just gonna call the model ten trillion times, you know, and just do distillation. They also augment the training data with their own approach. So if-- I will be talking about the GLM approach maybe like later.

[2160.82s] Um, but they did invent some new approaches to do very good reinforcement learning and GRPO. Um, and because GRPO and reinforcement learning, um, you know, is open source, these labs just use these methodologies to make the models better.

[2174.66s] So you don't-- So distillation is only one part of the training system. Um, and it's not-- I would say that assume distillation disappear, okay, maybe open source labs maybe increase, you know, it's not four, four months, maybe eight months.

[2188.24s] Um, but, but that's fine because, you know, we always have some sort of innovative and new approach. You know, DeepSeek might invent something new. Um, and so like, you know, GLM, Kimi, all of them, Google, you know, even the American open source lab, they'll have some new innovation.

[2203.62s] Um, and so like, I think like, yes, if you stop distillation- It will increase, you know, the, you know, four months to eight months, but I still think that is fine.

[2212.80s] Um, it's just a delay, you know, and then the delay will go back to, like, four months. Um, yeah. Yes.

[2220.12s] Good question. So the question is, if dynamic quantization is always better, why do people not always do dynamic quantization? Um, so

[2228.30s] it depends on the definition of dynamic quantization. So for every single lab, they will have different approaches to dynamic quantization. In fact, I'm actually gonna talk about that. Um, I was gonna talk about that in the benchmarking and accuracy minimizing [laughs] session.

[2243.10s] So I'll be talking about that. Um, so I will-- the-- your question will be answered later. Um, yes. Okay, one more question. Yes. Yes. So the question was, for consumer-grade GPUs, you know, what are the open source models in terms of like, you know, the parameter size, capabilities, and stuff like that?

[2259.72s] Um, so for the open source community, you know, the most popular models are probably Qwen3.6, thirty-five billion, um, twenty-seven billion, Gemma, you know, Gemma's twenty-six billion, um, GLM four point seven flash, the smallish type models.

[2273.98s] Um, and I feel like these small models are act-actually very powerful. Um, so-- Okay, I don't have-- Wait, I don't think I have a plot. Um, but essen-essentially, these small models, the biggest problem-- Oh, actually, I'm gonna talk about this as well.

[2286.90s] The biggest problem of these small models are they fail very bad at tool calling because they have tool calling issues, um, they loop continuously, um, and the biggest problem is because they're small, and that is why they have these problems.

[2300.32s] Um, but we can counteract this. Um, and so one of the things I'm gonna talk about later is the model becomes not important anymore. It's the harness or the tool that is actually the most important thing.

[2311.26s] Um, how do you actually call the model, um, that actually affects the most accuracy of the model. Um, so not actually the model itself. Um, but I'll be talking about that as well.

[2320.06s] Um, yeah. Okay. I will continue on. Um, there are always questions after each section. Um,

[2329.24s] uh, yes. Oh, yes, the next section, the fun section. Throughput maxxing. Oh, actually, I think I did-- It's supposed to be two X. I don't know. Whatever. Throughput maxxing and, a-and accuracy minimizing.

[2339.92s] I thought it was like accuracy mining, but there's no such thing. So it's called accuracy minimizing for now. Um, yes.

[2348.52s] So this part actually I really like. Okay, I'm not sure if you guys can see. It's a bit... Oh, whatever. Um, this shows the Pareto efficiency of cost-- of the cost of the model.

[2359.08s] So cost is, um, cost is the X-axis, um, and the Y-axis is the Arena score. So this is like an LM Arena's Arena score. Um, and this part I really like.

[2370.46s] So I don't really-- you know, maybe you see, like, Arena's scores, you know, LM Arena scores between each model. I don't really like that. It's not, it's not very easy to see.

[2378.66s] Instead, the better approach is to plot every single model on two axes, cost versus accuracy. Um, and you can see Fable does very well, right? So Fable does very, very well on that plot.

[2390.86s] Um, but you can see there is a Pareto trend, you know, like Gemini three point one preview is over here, you know, Opus four point six is over there as well.

[2399.02s] There are some other models as well. When Fable got released-- Okay, and well, now it's banned. But anyways, when Fable was released, when, you know, when people tried it, they noticed that it's not that much better in terms of actual capabilities.

[2415.34s] Um, you can see, you can see. But however, people really liked the front-end design. You know, they said if you called Fable, it was very, very good for UI, UX front-end.

[2428.42s] Um, and in fact, if you look at the LM Arena's chart, you can see it wa- it was a very big shift in terms of front-end design. Um, GLM Fabric is also there.

[2437.26s] If you can see, you know, it was part of the Pare-Pareto, Pareto trend. Um, but in general, for these large models, they seem to have-- they're not gonna be do-- they're not gonna be doing that much better on general tasks.

[2449.56s] Um, however, for UI and designing, Fable seems to have done very, very well. Um, and so you should use Fable for your designing. You know, you should use Fable for designing for UI, for UX, whatever, HTML, JavaScript.

[2463.60s] But you should probably not use Fable for the rest of the tasks because it is very expensive. Um, so, you know, use some other models instead.

[2472.62s] Um, and you know, however, yes, okay, you know, some of the models, you know, like, okay, this mo-- you know, this shows that Fable does very well on UI and UX.

[2483.38s] Um, but how about over time? Um, you know, how-- what do-- you know, Anthropic, their view is we need to maximize throughput, right? Maximize throughput, but also maximize accuracy.

[2495.30s] Um, you know, they want to like, you know, serve more people. Um, but sometimes it doesn't actually work. Um, sometimes they actually reduce accuracy. Um, and so you can see there is a-- I don't know if you folks know, um, MarginLab.

[2507.64s] Um, they have this very cool-- They do, they do SWE-bench. They benchmark Codex. They benchmark Codex and Claude Code with the models. Um, and this is accuracy over time for these models.

[2520.59s] Um, and the dotted lines are the release of the new models. Um, so there's actually another, um, there was actually a dip in-- Wait, can you-- Is there-- Oh, okay, the mouse is there.

[2529.04s] Um, I, I think it was over here, um, I think it was over here that Fable got released, um, so there was actually another dotted line. Um, there was actually very interesting trends you can see.

[2538.04s] The first one is, um, every single time there is a new model release, this, this, you know, daily tracker seems to decrease in accuracy. Um, and so if you wanna predict when a model gets released from Anthropic, you can use this as a indicator, um, of when the model gets released.

[2558.72s] It works very, very well, right? So, like, essentially, if you were over here, the dip in accuracy over a very long period of time was because Fable got released.

[2565.92s] Um, and over here, I think that's Opus four point eight, I think. Um, I think-- Yeah, I think that's Opus four point eight. This is Opus four point si- uh, seven, and so on.

[2575.61s] That's four point six, I think. Uh, uh, whatever. Um, I don't remember exactly, but, um, but you can also see that there is ginormous dips of accuracy. Um- And it's not just like one day or two days, it's for a very long period of time.

[2592.56s] This is also Codex. Um, so they also do Codex benchmarks. Um, and you, you can also see that over time-- I don't know if you can squint, but you can see that actually Codex has been getting worse if you plot the trend, right?

[2604.51s] If you can-- I don't know if you can squint, but if you draw a line, it seems to be getting worse. Um, so I'm, I'm assuming OpenAI is investigating this as well.

[2611.54s] Um, okay.

[2612.50s] Wait, wait. So this is a different model. So this is like-

[2614.38s] This is Codex

[2615.06s] ... Codex is gonna be worse than five point four.

[2617.64s] So this is using five point five.

[2619.69s] Okay.

[2619.70s] This is using-

[2621.66s] It's the same model every-- It's the same model every day.

[2623.68s] Correct. It's the same-- So what this benchmark does is you randomly sample fifty SWE-bench questions. SWE-bench is very large. So you just sample fifty of them, and then you call the model to answer it.

[2635.84s] Um, and then you record accuracy. Um, and so obviously, you know, every single day, there's like, you know, dai-daily variations. Uh, it's not, it's not that useful because you're only calling fifty questions.

[2645.58s] Um, so the trick is to look at the trend. Um, and the trend, uh, uh, maybe OpenAI should investigate this. Um, and you can see the trend for Claude.

[2654.64s] You know, Anthropic is also not very good. Um, in general-- Uh, so sorry, this is not the same model. Um, these models change. My bad. Um, so it's the same harness, but the model changes.

[2666.12s] Um, so this dotted line is GPT five point five. Um, so everything over here is GPT five point five. Everything over here is GPT five point four. Um, I think this is five point three, um, and so on.

[2677.20s] Um, but it seems like the model is getting worse. [laughs] So I don't know. Um, this is probably just on this benchmark, right? On the SWE-bench Pro benchmark, it's getting worse.

[2687.58s] Um, but, you know, I wouldn't really trust these benchmarks. The best way is to look at the degradation, you know, the sudden drops. You know, for example, Co-Codex dramatically dropped over here.

[2698.06s] I don't know why. Um, and you know, Claude, you know, Claude Code was very bad for a few weeks over here or over here, right?

[2708.76s] Okay. Yes.

[2711.24s] Is there a confidence interval? Is it one time-

[2712.14s] Yes. There is a confidence interval. I do not plot it, but this is fifty tasks. So every single day, they call a fifty tasks randomly. So they will sample fifty tasks.

[2722.16s] Um, and so you, you should not look at this daily. This is daily. So every single day is fifty questions, another fifty questions, another fifty questions, and so on.

[2729.40s] Instead, you should do like a rolling average. You know, some sort of rolling, you know, seven-day average. Um, that's a better number. Yeah.

[2737.14s] Is it-

[2737.56s] I don't see any pattern there.

[2740.86s] Really? I can see it from here. It's like decreasing.

[2744.10s] I, I, I see no pattern.

[2746.28s] It's, it's-

[2748.28s] But that's the next, the moving average.

[2750.13s] Hmm.

[2752.12s] It has a moving average.

[2753.12s] If you look at the-- If you do the seven moving average, I, I'll probably get the plot later. It actually is decreasing. You can see it. Um...

[2759.40s] I see it.

[2759.41s] If you can see-- I don't know. If you look at the top peaks of the-- You look at the top peaks, and the peaks are decreasing.

[2765.56s] Uh, no, it's just random. So you have a top peak, and then it goes down.

[2769.94s] Okay, how about the bottom peaks?

[2772.38s] You can only bottom down because it has a random noise. It has a Gaussian noise, and it has a random noise.

[2777.53s] Okay, I agree there is random noise. So the trick is you need to do moving average. And if you look at the moving average, you can actually see it's decreasing.

[2783.32s] I, I'll probably-- I'll get the plot later. Um, you can, you can search it. It's Mar-- So go to MarginLab. Search in MarginLab, Codex, Claude Code benchmarks, and they do show weekly, the weekly trend.

[2795.72s] But I'm just saying this is not, this is not to say that the model is getting worse. This is just to show that accuracy, that, you know, the sudden dips, the accuracy of these models can decrease.

[2807.46s] Um, and the question is why? You know, for example, why did Claude Code over a few weeks, why did the performance decrease? Like why? That's the fundamental question.

[2818.88s] Did they change the weights that-- on those dips? Did they change the weights?

[2823.82s] So that is one theory. A theory is they might have acci-- you know, that before the model release, they are doing testing.

[2832.10s] Exactly.

[2832.14s] And so they might have like, you know, act-- you know, some of the, some of the queries they route to Opus four point eight-

[2838.16s] Yes

[2838.58s] ... or Fable or whatever. And the problem is they did not--

[2843.60s] So the main question is, if you do route to another model, why did the accuracy decrease? It should actually get better. And so one of the theories is, theory one, they forgot to edit the system prompt.

[2854.42s] And so the system prompt for Fable was different, but then they used the wrong system prompt for, you know, for Opus four point eight, and that is why the accuracy decreased.

[2863.46s] Um, and then after the model got released, the accuracy went back up because they used the correct system prompt. That is one theory. Um, the other theory is, the other theory is-- Okay, we're actually gonna talk about this, is it's actually they're doing tricks.

[2878.42s] You know, they did quantization, but they didn't do dynamic quantization. They did some dumb quantization. Um, you know, they-- Some GPUs are broken, for example. You know, they use the wrong GPUs.

[2888.82s] Some of them have like, you know, bit flips or something. I don't know. Um, they have like a new data center, and then that data center, just by chance, has lower accuracy.

[2897.60s] Um, in fact, there is actually-- Okay, I'm gonna talk about this, actually. Um...

[2902.57s] In this slide.

[2904.16s] Yeah, but there are many, many theories like, you know, possibilities why this could reduce an accuracy. Um, actually, I, I think it's the next plot. Yes, the next plot.

[2911.92s] Um, or, well, the next slides. Um, so actually, when was this? I don't remember. Um, it was a few months ago. Someone from AMD actually made an issue on Claude Code, you know, during this dip.

[2925.52s] I think it was during the, before, um, a very large dips in accuracy. And they actually asked Claude, you know, they asked the Claude team, "Why is there a noticeable dip in accuracy?"

[2934.72s] You know, why, why is that? And Claude actually wrote a-- In April 23, they actually provided details on why they had reduced in accuracy, right? So they did a postmortem on what happened with Claude.

[2949.64s] Um, and- So why? It's because the thinking trace got deleted after the sec-- you know, when you, when you ask Claude the second time, the thinking trace got deleted, um, and it had a bad system prompt.

[2962.02s] Um, and they found out that that was why the accuracy got delete- got reduced. Um, so somehow in Claude Code,

[2970.66s] the second time you ask a question, the previous thinking trace got erased. Um, and I don't know. I don't even know how they did not find this, but oh well.

[2980.08s] Um, according to them now is Claude now has this internal benchmark, so they will use more internal investigations to test, okay, next time if there's a new model, this won't happen ever again.

[2989.98s] Um, and you know, like these things do happen over time. Um, and so like for this specific example, Cla- you know, Claude Code, the harness, the harness itself was the problem, not the actual model, right?

[3001.28s] The harness, the thinking trace got deleted, and they had a very-- not a very good system prompt. Um, and that is why the accuracy actually degrade, um, degraded. So that-- Okay.

[3011.90s] So we found one answer why these models got worse.

[3019.30s] They also released in September two thousand and twenty-five, right? In September two thousand and twenty-five, they showed that it was due to-- Okay, I didn't-- Okay, I didn't put the slide.

[3027.94s] But anyways, they showed it was actually due to a hardware problem. Um, so in their compiler, um, they used TPUs. So, so Anthropic likes to use TPUs and GPUs.

[3038.42s] Um, they showed that the same software stack for GPUs and TPUs, um, actually produced different results. Um, and so for the TPUs, it actually was different sampling. Um, and for the GPUs, it was a different sampling mechanism.

[3052.24s] Um, and so that is actually why they had decrease in accuracy during September sometime, um, because they actually had different hardware. And so you need to like-- Yeah. So like once you have different hardware, accuracy also changes.

[3066.94s] So I think the main point is the harness, the implementation, the tool is now the most important. It's not the model, right? The model is useless. Most models, you know, if you look at the model of, you know, open source versus closed source, models are generally the same.

[3083.04s] The difference is how Claude Code is made, you know, how Codex is made and used. Um, and so that is actually the most important factor. It's not the model anymore.

[3093.26s] Um, and so like, you know, as we have seen, if they have accidentally botched, you know, if they accidentally botched the harness, you will get reduced accuracy. Um, and so like, you know, definitely, you know, for large labs as, you know, I'm sure they ha-- they know these problems, and they're working on it.

[3111.10s] Um, but I feel like, you know, these are probably, you know, these are still very hard to fix. Um, yeah. So hopefully I answered some of people's questions on the harness, you know, the accuracy.

[3120.54s] Um, so there is actually reasons why accuracy got degraded.

[3125.68s] But, you know, it's not just closed source labs doing bad.

[3130.40s] Across open source model providers, the accuracy changes. So if you look at this plot, so this is from OpenRouter. Um, this is DeepSeek V4 Pro. Um, so most labs, what they want to do, most inference providers, what they want to do is they want to serve you the highest throughput, right, with the cheapest price.

[3149.86s] They want to give you, you know, sixty tokens, one hundred and twenty tokens, one thousand tokens per second, right? They wanna give you the fastest. Um, but did you ac-- But did people actually bother to check accuracy?

[3162.12s] So that is the fundamental question. You know, you might be getting ten thousand tokens per second, and there is no model. Um, so the main question is you need to be careful of what you use from these inference providers.

[3173.80s] Um, and so for DeepSeek V4, you know, there are two benchmarks which OpenRouter ran, you know.

[3181.58s] Yeah. It's like sorted. It's sorted I think on the gray. I think it's sorted on TauBench. Um, so it's sorted on TauBench. Um, and the green one is GPQA, and you can see that in general, some of the labs are not, you know, some of the-- Sorry, not labs.

[3193.82s] Some of the inference providers are not doing [chuckles] very well. Um, so you need to like, before you, before you use a open source model, please check the accuracy before you use a open source model.

[3204.86s] Um, and also one of the biggest problems of this is every single time, you know, for example, like Claude Code, you know, Claude Code and Codex, you can benchmark accuracy over time.

[3216.64s] Um, and the good thing about closed source labs is they control the supply chain. Um, the biggest problem of open source is there are so many suppliers and providers of these models, um, that sometimes what happens is people get turned off, and they get very annoyed that the open source models do not work very well.

[3236.34s] Um, so everyone, you know, in the, in the ecosystem, people keep saying that closed source labs do much better than open source. But it's not because of the model, it's because of the inference provider, right?

[3247.02s] The inference provider is to blame that they are causing the downfall of open source because they're giving a bad name for open source. Um, so I would like check, you know,

[3257.88s] whatever favorite inference, inference provider you have. Um, so this, this benchmark was run, I think, yesterday, um, by OpenRouter. So this is, this is daily data by OpenRouter. Um, so whatever favorite inference provider you have, please tell them not to, you know, reduce accuracy that much.

[3276.48s] Um, this is GLM five point two. Um, so, you know, GLM five point two as well shows different accuracies. Um, you can see-- So the plot on the right shows most model, you know, most inference provi-- Okay, I keep saying model labs.

[3290.62s] Most inference providers are throughput maxxing, but they are accuracy minimizing. That's where the phrase comes from, okay? So they do not care about ac-- In fact, look, look like, you know, the highest accuracy is seventy-six point four percent, and the lowest is sixty-two point four percent.

[3304.80s] So there is a ten percent gap between the be-- you know, between the highest accuracy and the, you know, lowest accuracy. Um, and so like you need to, you know, as a- As a, you know, as a call-out to inference providers, you know, please increase accuracy, you know, before trying to make things faster, right?

[3322.54s] You do not want a model to be very dumb, um, and it's like, you know, ten thousand tokens per second, right? We can make it one million tokens per second, and there is no model.

[3330.74s] Um, you know, just call a human or something. You know, make a fake or something. So yeah. So the main point is we need inference providers to do good in terms of accuracy.

[3341.90s] Otherwise, this will make open source have a very bad look. Um, yeah. Oh, okay. That's the end of the, [chuckles] the second section. I guess that was a bit of a rant.

[3351.74s] Um, any other questions for this? Yes.

[3354.20s] Yeah. So for a new organization that's-- that wants to use, like, a open source, uh, model, do you suggest using a, you know, inference service provider, or do you suggest downloading from Hugging Face and then using, like, model or, you know, some kind of server to, you know, implement, uh, yourself?

[3373.16s] Like, what do you suggest if any new organization comes and asks you, like, how do you use open source model?

[3378.66s] That's a great question. So when a open source model gets released, you know, how should you use it in terms of accuracy, throughput or whatever? Um, so in general, um,

[3388.90s] in general, open source has come a long way. So for example, we did report bugs in Gemma one, Gemma two, Llama, Mistral, you know, OpenAI, gpt-oss. Every single of, of those models had bugs.

[3398.96s] Um, and so the good thing is, you know, as Unsloth, we will help the labs before they release a model to fix some of the issues. So every single model you now have has some of our fixes.

[3410.16s] So that's a good thing. Um, but in general, if you have a open source model, I would use llama.cpp, for example. I think llama.cpp and llama-server is probably the most bug-free system.

[3423.16s] So y-- I would like suggest, yes, you should download from Hugging Face, use llama-server, use Llama, you know, CLI. I don't know, you can use Unsloth Studio, whatever.

[3431.80s] Whatever's your favorite tool. But you should... Yes, you should download from Hugging Face. Um, in terms of like, you know, if you're a large enterprise, generally speaking, what they like to do is they like to wait one week.

[3443.64s] So most enterprises, they'll wait one week for all the problems to be fixed. Um, and then, you know, then they'll use the model. But in my view, that is not a good approach.

[3453.66s] I would say if you-- Okay, if everyone waits one week, then, like, how do we fix the bugs? Um, because only at scale, only at scale, then we can see the bugs.

[3463.92s] Um, and so like in general, we need everyone to start trying these models earlier, um, and not like, you know, wait one week, wait one month. You know, don't do, don't do the waiting approach.

[3474.62s] Um, but I would say like in general, the enterprises, what they like to do is just wait. Wait one week. Um, yeah, that's like common practice. Um, yes.

[3483.84s] Do you-- Would you mind-- Can you go over the, um, theories and reasons again, like a bit more about why the performance degrades before a model release usually relates to Anthropic?

[3494.68s] So, okay, the question was why would the model performance degrade before a model release? Um,

[3502.62s] these are just hypothetical quest-- hypothetical theories. So every single model has a different system prompt. So Opus 4.8. Opus 4.8 system prompt is very short. Um, but Opus 4.7 system prompt was extremely long.

[3517.04s] Um, so the theory was, this is just a theory, that Anthropic via Claude Code accidentally routed some of the models to Opus 4.8, right? They use Opus 4.8 as testing, right?

[3529.10s] They need to test Opus 4.8. But they used Opus 4.7 system prompt. So they used the wrong system prompt, and that is why accuracy degraded. Um, that's one theory.

[3539.26s] Um, another theory is... Actually, I think that's the-- Actually, I thought about it. That's probably the only theory I had. [chuckles] I'm like thinking, "Hm, is there another theory?" Um.

[3552.10s] Yeah.

[3552.58s] I guess the harness itself, like, you know, sometimes the harness itself-- The harness was, was designed for Opus 4.7. Um, and during-- When they were going to release 4.8, they need to calibrate the harness, right?

[3568.30s] They need to change the harness, um, for, for 4.8 to make it work. But the problem is

[3574.42s] you're not allowed to publish it, right? You're not allowed to publish it and give it to people because otherwise people will, like, you know, go on Twitter, on LinkedIn, you know, everywhere.

[3582.14s] "Ooh, I can see O-- 4.8 is gonna be released." You know, everyone's gonna be screaming, you know, "4.8's coming, 4.8's, you know, re-getting released." And so maybe that's why accuracy deg-decreased.

[3591.88s] It's they update-- They did not update the harness. Um, or the other option is they up-- they already up-- they silently, they silently updated the harness before the new model got released, and it regressed, you know, it reduced accuracy.

[3605.56s] Um, I don't know. Like, to be honest, I-- you should probably ask Anthropic that question. Um, or... But I think in general, in general, the dips, the dips don't always correspond to, like, new model releases.

[3616.66s] Some of the dips are actual issues. Like, you know, the, the thinking trace got deleted. Um, the system prompt they wrote are wrong. I think for the system-- It's funny.

[3625.32s] I think for the system prompt, they said, um,

[3629.12s] they tried to reduce verbosity, so they tried to make the model less talkative, um, and it actually made the model dumber. Um, and so I think it was just one word.

[3638.98s] They added one word-- No, one sentence, I think. One sentence in the system prompt that made the model dumber. Um,

[3646.44s] yeah. I don't know if that helps, but... I don't know if ever anyone else has any i-- like theory. I don't, I don't think so anyone even has that many theories on this.

[3653.36s] Um, obviously, the Anthropic engineers will know. Um, but, you know, they're not gonna tell. So it's just based on hypotheticals. Something to do with the system prompt, something to do with the harness.

[3663.62s] Yeah. But I think in general, you can also use this plot. You know, if the performance decreases, most likely a new model's gonna be coming. Um, yeah. Any other que-- Yes.

[3671.96s] Just to add upon that, uh, they are opening up-- not opening, uh, Anthropic actually released the prompts-

[3684.37s] Before they get released, they drop the guardrails Correct. And then they again add new guardrails because they've been figured out that they are basically exploit. So that- Yes, exactly.

[3693.27s] Yeah. Exactly. So before a model release, they use a different system prompt for that new model for the old model. And so that is probably why there are some decrease in accuracy.

[3702.81s] They switch the system prompts around or something like that. Um, and also, you know, the model itself, you know, th-- I think 4.8 system prompt is very short. Um, it's-- Yeah, I think it's, like, very, very short.

[3713.77s] And 4.7 was ginormous. Um, and the reason is 4.7 was like, you know, I don't know what, I don't know what happened, but they have this ginormous system prompt, and the 4.8 just shrunk it a lot.

[3722.73s] Um, so maybe, maybe they used the 4.7 system prompt, I don't know, or 4.8 system, the short system prompt for 4.8, and then they use it for 4.7, and that's why it decreased accuracy.

[3734.11s] I don't know. Um, but yeah, sure, correct. Um, they do release-- Although I think the system prompt they released on the website is for Claude.ai, so the online chat system.

[3743.47s] Um, the Claude Code system prompt is actually different. Yeah. So I think you need to actually call-- You need to call Claude Code, you know, "What is my system prompt?"

[3753.03s] And then you print it to, like, a text file, um, and then you can, like, ins-- investigate what the system prompt is. And then you can also override it if you want.

[3761.49s] Um, yes, but it's a different system prompt, most likely. Um, yeah.

[3767.13s] Last question, if anyone... No? Okay. Continue on then.

[3778.89s] Okay. The next section we're gonna be talking about is benchmaxxing and cheating. Um,

[3786.87s] I'm not sure if you folks have seen the DeepSWE Benchmark. Um, the DeepSWE Benchmark is a very popular recent benchmark that shows, you know, the cost is on the X-axis, and the Y-axis it is a DeepSWE Benchmark.

[3801.05s] It's a new benchmark based on like, you know, a better uncontaminated version of SWE-bench Pro. Um, and in general, you can see that, you know, GPT 5.5 does very well with Fable, um, you know, GLM, Opus 4.8 in general, right?

[3813.77s] It shows, you know-- This part shows that models are getting, you know, um, uh, these-- The dots are different reasoning modes. Um, I think this is maximum reasoning, I think.

[3825.43s] Um, high, extra high. You know, these are actually different reasoning, um, reasoning times as well. Um, but in general, you can see that there is a Pareto efficiency trend, right?

[3836.02s] The best model is the one, you know, to the right to the top, right? The better the model to the right to the top is, the better the model.

[3843.08s] Um, so you want models to do better and better over time to that, to the top right corner.

[3849.33s] And, you know, I just learnt, I didn't actually know this. I just learnt that SWE-bench Pro, when you run this benchmark, you use LLM-- you use language models as the verifier.

[3861.41s] Um, and I was, like, confused because, like, for most benchmarks, for most benchmarks, you should never call another language model to check whether your answer is right or wrong.

[3874.03s] And so for SWE-bench Pro, you actually call a language model to verify if your language model was right. Um, and so that is why SWE-bench Pro is not a very good benchmark.

[3885.27s] Um, one of the problems is, is do we need to do sampling? Like, how many verification runs do you need to run to verify if your answer is correct?

[3896.25s] Do you run it one time? Do you run it five times? Do you run it one hundred times and take, like, an average? Um, so, like, I was actually quite shocked that this is actually what happens.

[3905.43s] Um, I was quite surprised, actually. Um, the next question is, which model is the verifier? You know, you ask-- For example, you ask Opus, you know, you, you benchmark Opus 4.8 on SWE-bench Pro.

[3917.87s] But which-- what do you use as the verifier? Do you use Opus 4.8 as the verifier? So you're using the same model itself to verify itself. Um, and so like this-- I was, like, quite surprised, actually, that this is how benchmarks work, um, [chuckles] and actually quite disappointed.

[3933.37s] Um, but anyways, obviously, you can go with the other approach. You can do human verification. Um, you know, everyone in the room, I'll give you the SWE-bench, you know, and just tell you guys to verify it.

[3945.87s] Um, you could do that, I guess. Um, and also, what happens if the verification changes every day? Um, you know, remember previously models, you know, every single day models get better or worse.

[3957.15s] Um, what happens, what happens if you run, what happens if you run the verification when the model was doing very bad, right? You will actually have different SWE-bench numbers.

[3967.19s] Um, and so, like, I'm actually quite surprised this is what the industry does. Um, you know, run SWE-bench Pro, but using LLMs as verifiers. That is definitely not a good idea.

[3977.11s] Um, but anyways, people do it, whatever. Um,

[3980.91s] in fact, according to DeepSWE, um, if you do, if you do verification using language models, SWE-bench Pro has a eight point five percent false positive rate. Um, and a false positive rate means that the LLM verifier said that the model was correct, but it was actually wrong.

[3999.41s] Um, and so eight point five percent of the time, it will do this. Um, the false negative rate is even worse at twenty-four percent. Um, this means that the verifier said that the model was wrong, but it was actually right.

[4014.57s] Um, and so you can see that SWE-bench Pro is a very bad benchmark. Um, and so DeepSWE showed that they have in-- you know, they fixed the problem, you know, um, by reducing the false positive rate and the false negative rate to, you know, one percent.

[4030.33s] Um, in fact, some examples of cheating, um, I-- You know, this is actually quite sh-surprising, um, but in the SWE-bench Pro benchmark, you get, you get, like, a GitHub question, you know, a GitHub issue.

[4045.43s] You call the model to solve that GitHub issue.

[4049.93s] But did you know that in SWE-bench Pro you get the full Git history? So you get the, you get the actual answer as well. Um, so I'm like, I'm actually quite-- I was actually quite shocked to learn this, um, that during these models, you give the answer and the question, like obviously the model will cheat.

[4067.97s] Um, and so like this is definitely a very bad benchmark. Um, you know, you should never, ever, ever, ever give the model the answer. Um, and so very silly.

[4079.57s] Um, but yes, this happens a lot. Um, and you do not want the model to literally see the solution. Right? That is a terrible approach. Um, the other problems that you get gaps, like false positives is, you know,

[4092.07s] the PR tests, you know, the, the GitHub, the GitHub issue tests are very weak. Um, so, you know, at the final conclusion, you know, when the GitHub, when the GitHub issue is closed with a pull request, the tests that the maintainer wrote are not very good.

[4106.89s] Um, and so the problem of that is, you know, if you have tests which are very weak, then you know, the model does very well-- uh, not very good.

[4114.20s] Um, and obviously the worst part is the model will like bypass some tests. It will skip some. Um, and that is not a very good approach.

[4122.11s] In fact, um, DeepSWE actually showed how many times a model cheats by looking at the full Git history, you know, directly going to the answer. Um, you can see Opus four point seven.

[4135.89s] So the purple bars show cheating by models. Um, uh, it looks like GPT five point five never cheats. It looks like it. Um, uh, okay, maybe we should use GPT five point five.

[4146.73s] Um, you know, so actually this is actually very interesting. There are some people which think that if you cheat, that's actually good. Um, and the reason why it's good is it means that Opus four point seven already knows-- like if you give it the full Git history, you should be able to-- like, you, you gave it to

[4163.47s] them, right? You gave Opus the full Git history. It should find the solution there, right? It should just directly skip over to the solution. So it's-- that's what people think.

[4171.51s] You know, people have a view that the humans gave Opus four point seven the full Git history, so it should cheat, right? You, you, you designed it to cheat.

[4181.53s] Um, so in general, Claude models seem to cheat more, um, and OpenAI models seem to cheat less in general. Um, so it depends on you, you know, if you want a model to cheat or not.

[4194.57s] Um, and the definition of the word cheat is also very, you know, charged. So I guess it depends on what the word cheating means.

[4202.01s] Um, you know, for false negatives, remember, SWE-bench Pro calls a language model to verify if your answer is correct. Um, and so sometimes it's not very good. You know, sometimes you have unrelated tests that fail.

[4216.77s] Um, you forgot-- you know, sometimes when you write tests, you forgot about the tests which have helpers, you know, helper functions, and you just skip that. Um, so there are many issues and this-- I think this was twenty-- yeah, so twenty-four percent of the time, twenty-four percent of the time the model says-- the verifier says your model

[4234.15s] was wrong, but it was actually correct. So this is another problem.

[4240.77s] And even worse, the harness itself can change accuracy. So when you benchmark using SWE-bench Pro, like you need to have one agent or one harness for all models, right?

[4253.89s] How do you create a generalized control environment for these models? Um, and so you can see, like, you know, for example, DeepSWE showed if you use Claude Code, you get forty percent accuracy.

[4265.41s] But then if you use their own, so it's a special harness, you can get fifty percent accuracy. Um, Gemini, for example, right? If you use Gemini CLI, you get twenty percent accuracy.

[4275.89s] But if you use their one, you know, the, the control environment, you can get forty percent accuracy. Um, and so in general,

[4285.21s] for these benchmarks, you also need to have a controlled environment. Um, and that is also another problem.

[4292.85s] And with DeepSWE, they showed by using this benchmark, by solving, you know, by stopping cheating, you know, by, you know, if we remove cheating, if we remove, you know, these other issues, you can see the models, you know, the models are not saturated anymore, right?

[4309.55s] You can see the models are very different in terms of the capabilities. According to this benchmark, GPT five point five is the best, according to this one. Um, are you-- Oh, this is not updated.

[4318.27s] Um, four, four point eight I think is over here or something. Um, but yes, this benchmark shows Claude Haiku is zero percent, um, accuracy, right? It's terrible, I guess.

[4329.65s] Um, but yeah, this benchmark just show-- Okay, the main question is do you trust this benchmark? That is another question. Um,

[4336.77s] there is other benchmarks, right? So Cognition released a Frontier Code benchmark, which also tries to solve the same questions for benchmark-- you know, for cheating and benchmarks. Um, and what they showed is you can fix contamination.

[4349.39s] And how do you fix contamination? You ask, you know, you ask Cognition's team, which is full of like, you know, national Olympiads and, you know, international Olympiads. They manually checked every single question, um, themselves, you know, and removed bad questions, you know, bad examples.

[4366.69s] Um, and they also showed that their questions are much more diverse, right? So Frontier Code has many different other languages. Um, and they showed with diversity, you know, with more diverse programming languages, um, and by reducing contamination, they also have a benchmark.

[4383.81s] Um, and according to their benchmark, Opus four point eight is the best, right? With a fourteen point five percent accuracy. GPT five point five is seven point two accuracy.

[4393.91s] Um, and this is the diamond one, right? So this is the fifty, the fifty hardest questions. Um, the main benchmark is one hundred questions, and the extended is one hundred and fifty.

[4404.75s] Um, and so according to them, you know, Claude does the best, according to them.

[4412.70s] But also according to them, Frontier Code seems to be better than DeepSWE, right? The benchmark that I showed previously, DeepSWE, this one, um, you know, according to Frontier Code, so the Cognition team, their benchmark is better than DeepSWE, right?

[4428.20s] According to them, according to them, DeepSWE's false positive rate is forty-four point nine percent. But remember, what did DeepSWE say? They said the false positive rate was...

[4439.30s] I don't remember. What, what did they say? Um, they said that it was zero point three percent, right? So DeepSWE said, DeepSWE said their false positive rate is zero point three percent, but Frontier Code said that DeepSWE's false positive rate was forty-four point nine percent.

[4456.70s] Um, so you know, there are some competition, [laughs] I guess, between benchmarking labs. Um, well, uh, uh, Cognition's not a benchmarking lab. But like, you know, between companies. Um, so the main question is who do we trust?

[4470.00s] You know, do we trust Frontier Code's benchmarks? Do we trust DeepSWE's benchmarks? Do we trust SWE-bench? You know, who do we trust? And that is a very important question.

[4482.26s] Um, you know, my take is like, you know, I guess just take an average of everyone. Take an average of everyone, and you'll probably get the best answer. You know, who is actually doing the best.

[4491.72s] Um, yeah. But this is actually very interesting. Um, you know, it sh-- Okay, so according to them, the false negative rate for DeepSWE is correct, you know, one point two percent.

[4499.66s] But my interest-- You know, I probably, uh, you know, my main question is why is the false positive rate so high for Deep-- According to, according to Frontier Code, DeepSWE is even worse than SWE-bench Pro.

[4512.96s] That's what they're trying to say, I guess, for, for the false positive rate. Um, yeah.

[4519.80s] And even worse, there is another benchmark called FrontierMath. Um, so FrontierMath is by Epoch AI. Um, so they, they have this math benchmark with different tiers. You know, tier one, tier two, tier three, tier four.

[4534.06s] So tier four is the hardest. Um, but the benchmark itself was botched, um, [laughs] and so they actually had to release a corrected version of their benchmark. Um, I think this was one month ago, um, or something.

[4549.06s] Um, so they showed that their benchmark questions were fully wrong. Um, and you can see that if you correct the benchmark, if you correct the benchmark, the accuracy for GPT five point five jumps from fifty percent to eighty percent or something.

[4562.88s] Um, and so now you can't even trust the benchmark. And they showed in a tweet-- Oh, it's June twelve. Oh, it's only two weeks ago. Um, so in June twelve, they showed that the reason why they did bad on the benchmarks is they, they did the answer extraction incorrectly.

[4578.92s] For example, they did un-- you know, they had unclear questions. They had the incorrect sign. So for example, they said the model said twelve, but it should be actually minus twelve, and they forgot to get the minus sign.

[4590.06s] Um, they have one-off errors. Um, yeah. There's many problems with the benchmark. Um, [laughs] and so they fixed their benchmark, um, just recently.

[4601.76s] In fact, you know, it's actually quite funny. This was just two weeks ago.

[4607.20s] Have you guys heard of Hugging Face's Math-Verify, which was one year ago? Um, and the Hugging Face showed that, in fact, these benchmarks, when you do maths questions, they always do bad.

[4619.46s] And the reason why is because there's many problems, right? The formatting is incorrect. Um, you know, the extraction of the fraction is wrong. Um, you know, the sign is failed extraction.

[4629.82s] There's many, many, many problems of mathematical extraction. And to be honest, I feel like it's like kind of reinventing the wheel or, you know, the rediscovery. Um, but Hugging Face actually published this one year ago, and Epoch just fixed it two weeks ago.

[4643.66s] Um, so you know, benchmarking labs definitely need more, you know, they need to investigate literature more, I think. Um, in fact, according to Hugging Face Math-Verify, you know, if you use-- if you-- The green bar, the green bar is if you do not use Hugging Face's verification system, you know, to fix the benchmark.

[4665.50s] If you do fix the benchmark, you can see accuracy dramatically increases, right? For example, for Qwen, for Qwen, the accuracy was ten percent. Now it's twenty-five percent. Um, and so you need to-- So that means that open source models are not dumb.

[4678.52s] They just have different-- They output a different format. Um, and so one of the problems is how do we actually, actually, like, you know, parse these different formats?

[4688.86s] In fact, it's even worse. Um, you know, I think I tweeted-- Oh, I tweeted this in August two thousand and twenty-four, um, that if you ca-- if you use different tokenization, you can also have different accuracy.

[4700.10s] Um, in fact, for MMLU, if you use spaces, you increase accuracy by zero point four percent. Um, it might not sound like a lot, but the point is by these very dumb things like, you know, using spaces or, you know, minus twelve becomes twelve, um, and all of these like dumb little small things, the accuracy of these

[4721.80s] benchmarks can change over time. Um, and so like the main question is, you know, how do we make benchmarking labs and benchmarking companies, you know, how do we make them more reliable, um, and you know, tr- more trustworthy?

[4737.36s] Oh, okay. That's I guess the section for the benchmarking ques- part. Any other questions for that section? Um,

[4744.98s] questions? Yes.

[4747.74s] So I think with, with all these kind of, uh, you know, issues with the benchmark, uh, like, do you have any specific suggestion on how to trust them? And like for somebody who are enterprise customers, how, how they should kind of, you know, build their own benchmark?

[4765.84s] Because it's, it's clearly like, you know, if you're talking from customers' point of view, customers probably, uh... I mean, it is-

[4781.05s] That's a great question. So the question is, how do we-- how can we trust these benchmarking companies? Or like what other types of benchmarks can we do to make it trustworthy?

[4790.50s] Um, so that is actually a very good question. The main question for benchmarks is you need to satisfy two conditions. The first condition is the benchmark must not, must not be benchmarkable, right?

[4801.45s] How do you make a benchmark that is extremely hard to benchmark, right? How do we like not get one hundred percent accuracy? And the second question is, how do we make the benchmark, um, verifiable, right?

[4813.09s] So how do we make the benchmark you can, you can also verify that the answer is in fact correct, right? You-- Remember, SWE-bench Pro is dumb because you call the language model itself to verify itself.

[4825.53s] Um, so that is not good. Um, so the main question is those two questions. Um, and so one good example, this is just a dumb example.

[4836.25s] Randomly create maths questions. Sample-- For example, okay, this is-- Okay, this is probably not a good benchmark.

[4844.37s] You automatically create maths questions. Um, we can sample infinity, right? We can sample infinite maths questions, right? Two plus two, four plus four, you know, any single number added together.

[4856.51s] That's one question. Can you verify this? Yes, you can, right? You can call a calculator to verify what is two plus two. Can this be benchmarkable? Hard. And the reason why hard is because the sampling space is infinity, right?

[4871.83s] It can be two plus two, one thousand plus one hundred and one, right? It can-- You, you don't have to do plus, right? You can do one thousand times one thousand.

[4879.44s] And so that's one way. Make a benchmark which is very hard to cheat, but also easy to verify. So some sort of maths question. Um, the other one, for example, is, um...

[4892.07s] Okay, maybe this is not a good example. I'm just making this one up on the spot.

[4896.03s] Tell the model to create a poem in seventy words, and you must use the word happy. Can you verify this? Yes, you can. Is happy in the, you know, generation?

[4909.65s] If yes, plus one. Also, you can count how many words, right? You can count, okay, is there seventy words? Um, so you can do these type of approaches. And is this benchmarkable?

[4919.95s] No, it's, it's very hard to benchmark because you can say seventy words, sixty-nine words, sixty-eight words, one hundred and two words, one thousand words, right? It doesn't have to be happy.

[4930.49s] It can be you must have two words, you must have three words. Um, so some, some sort of benchmark where it's very hard to benchmark. Um,

[4941.39s] yeah, in my view, I think that's, that's probably gonna be the most important benchmark. And I don't, I don't think so anyone has actually made this yet. Um, I don't know, maybe someone in the audience or, you know, you guys can go as teams, I don't know, make a startup or something.

[4953.57s] You know? Do that. Um, and I feel like that benchmark will be very, very important. Um, yeah. Yes.

[4960.55s] Um, what, in your opinion, are benchmarks we can trust today?

[4965.39s] Benchmarks we can trust today. None of them. [laughs] Take an average of all of them. To be honest, probably the best approach is just vibe, uh, vibe checking. T-try all of them and see which one you like the best.

[4977.69s] Um, to be completely honest, I just... You know, like these benchmarks, eh. Like the main o-- the main issue I have with benchmarks is, for example, um, you know...

[4989.35s] I mean, like this one, right? This one. I mean, even every single day the benchmark can change, so we can't trust the benchmarks anymore. So my fundamental view is do not trust any benchmarks.

[5002.15s] Take an average. And then, okay, then main question is who's taking the average? I guess artificial, Artificial Analysis has some a-average. The only problem is they have some weightings for the weight.

[5011.27s] Um, you know, each benchmark has a weight. So now the question is, you know, what is the weighting of each benchmark? You know, you can't just take like a dumb average.

[5019.29s] Um, you know, you can't just say, you know,

[5022.73s] ten benchmarks divided by ten. Um, that's probably not gonna work. So the main question is how do you even do the weighting? That's another problem. Um, so I think in general, it's based on vibe checking, I guess.

[5033.57s] Yeah. [laughs] I guess I don't have an answer for that. Um,

[5037.93s] any other questions? Yes.

[5040.17s] So, um, the SWE benchmark that you're saying, um, is comparing against its own model, um,

[5048.53s] there, there's one of the thing is all this benchmark, even if the benchmark was good by art-- by manually validating or, yeah, deterministic validation. These are the input questions.

[5060.01s] These are the output standard answer should match to. But when it goes to complex reasoning and dependent, dependent reasoning like, you know, the answer for this, this based on this answer are correct, right?

[5072.71s] When it-- reasoning goes on, it, it becomes very challenging because even if this is a, uh, DeepSeek or any of the benchmarks

[5094.24s] Yes.

[5095.51s] So that way, um, if it is good or bad, doesn't matter, but it's relevant for me, right?

[5103.77s] You're correct. So the question was in terms of-- because SWE-bench Pro, for example, you call a model. The question is what model? Could it be four point eight? Could it be GPT five point five?

[5113.81s] And you call this model to verify the benchmark. Um, you-- And so the question was, can you use an open source model instead so that now you, you have a controlled environment?

[5124.55s] So yes, you can. But remember, there is a problem because even open source models itself have bugs. Times, you know, the inference engines have bugs. Times the inference providers have bugs and accuracy degradation.

[5138.71s] So it's-- You're correct. Um, so the main question is we need to have someone or some organization, you know, some person or some whatever committee

[5150.36s] That we can investigate, you know, which engine did you use? Do not update the engine. You know, the engine must be the same. You know, the weights must have not changed.

[5158.36s] So there's many, many, many problems with this approach. Um, but I do agree as open-- You can use an open source model, but it's not-- it doesn't solve the other problems.

[5167.26s] Um, yeah. Does that-- Okay. Um, so the next section I'm gonna be talking about is cybersecurity and regulation. Um, this is a interesting topic. Um, so I'm not sure if you have-- all folks have seen this plot.

[5180.15s] It shows the AI Security Institute's, um, I think this is from the UK. Um, they show the performance of models based on some, some cybersecurity task. Um, and they show that Mythos Preview seems to be the best, um, you know, with GPT 5.5 Cyber, you know, Preview and so, so on.

[5197.38s] Um, they show this benchmark. Uh, and again, previously, as I mentioned, Weird ML is a better be-- in my view, okay, this is just my take, Weird ML is a better benchmark in general for benchmarking intelligence of models.

[5213.28s] And the reason why is because it doesn't actually, it doesn't actually follow the trend of reasoning versus non-reasoning. Remember reasoning, reasoning previously-- I think I have-- Okay, I don't have it.

[5222.80s] Um, reasoning, um, the reasoning models doubling time reduced by half to three point five months. So remember, you just need to wait three point five months, and the model's capabilities will double.

[5233.28s] Um, and the non-reasoning was seven months. Um, so you need to wait seven months for the models to double in capability. Um, but Weird ML did not actually have this trend.

[5242.88s] Um, the Weird ML benchmark showed that actually the trend was like, there is no trend. Um,

[5249.74s] and I think I'll just talk about this. You know, like one of the biggest problems of benchmarks is you need to constantly reinvent yourself and do reweightings of combinations of benchmarks.

[5260.44s] For example, Artificial Analysis just recently released, you know, their new V four point one benchmark, and they showed the weighting of the benchmarks. Um, you know, GDPval is twenty%, Terminal-Bench is sixteen%, and so on.

[5272.68s] Um, and so they, they designed these numbers as weightings for each of those benchmarks, and then they've averaged it up together. Um, so the main question is: How do you actually determine these numbers?

[5282.72s] Um, and so this is more like a human approach. You know, you have to determine these numbers. Um, you know, Arc AGI kind of saturated on ARC-AGI-1, and so that's why we have ARC-AGI-2, and that is also why we have ARC-AGI-3.

[5296.56s] And my, you know-- Though, I guess once ARC-AGI-3 is saturated, then we have ARC-AGI-4, five, six, seven, whatever. Um, and the main point is once you have benchmarks-- Is it called Goodhart's law?

[5306.86s] I don't remember. Um, the goo-- the benchmark itself becomes useless because, you know, models will start benchmarking on this.

[5315.04s] So one of the biggest problems of these larger models for cybersecurity, for example, um, is Mythos actually dramatically went out of the trend. Um, and that is why, you know, many people are afraid of these, you know, Mythos, you know, GPT five points-- five point six.

[5331.16s] You know, they're afraid of these models because it went out of trend. Um, you can see that Mythos dramatically went out of trend. Um, and, you know, even, you know, OP-- you know, GPT 5.6 didn't really release that many benchmarks because it was in preview mode.

[5344.64s] Um, so this is from their system card. They showed for cybersecurity that GPT 5.6 does very, very well.

[5350.78s] Um, in fact, because GPT f-- because GPT 5.6, they-- I think they only did Terminal-Bench as their benchmark. They did not benchmark on anything else. Um, they did have in their system card, they did have one benchmark, which is very important.

[5365.28s] Um, and this is called the internal research debugging evaluation. Um, and this is OpenAI's own set of, set of questions. So, you know, the custom open source, you know, if you wanna-- It's their own set of ten questions or whatever that they benchmarked GPT 5.6 on.

[5381.61s] Um, and according to them, it does very, very, you know-- it does better. Okay, I was gonna say very, very well, but it's not. Um, it does better. Um, and you can see that GPT-- It's actually kind of interesting.

[5391.50s] GPT 5.5 did worse than GPT 5.5 before, um, for OpenAI's own internal, um, research evaluation. Um, and, you know, GPT 5.6 definitely does much better, right? You can see that the G-GPT 5.6 Sol, you know, if you extend it, it does much better.

[5408.32s] Um, but interestingly, Terra does better, um, somewhat sometimes. Um, yeah.

[5418.10s] And, you know, one of the biggest problems of these models that are get-be-getting better and better and better is, I don't know if you guys know that, you know, open source exploits are getting worse and worse and worse.

[5428.70s] Um, and so the high exploit ratio, you know, number of critical vulnerabilities that were discovered has skyrocketed, you know, recently. You know, every single week or day, some sort of open source package gets compromised.

[5441.96s] Um, and they actually-- You know, this plot shows that it's getting very problematic. Um, and so, you know, Claude Mythos was released at this dotted line, where-- You know, most people, they're not sure if it's because of Claude Mythos that these vulnerabilities are increasing.

[5457.42s] Most likely, it's just because open source, you know, we use lots of models, call them many, many, many, many times, and we can, you know, automatically find exploits in these models.

[5468.68s] But, you know, there is actually another point. So in Hacker News, someone posted about this. Um,

[5474.18s] is it just Mythos and GPT 5.6 that do good on finding cybersecurity issues? It's not. Actually, open source models also do very well. Um, open source models do extremely well in finding cybersecurity threats and issues.

[5490.80s] Um, you know, there is some discussion on Hacker News, you know, is this actually true or false? Um, but, you know, according to some, you know, some researchers and cybersecurity people, the main reason why, you know, Mythos looked like it was very good on cybersecurity is because they bothered to actually check the open source code.

[5508.46s] Um, and so if you actually give the open source models the full code base of these open source libraries- They will find the bugs. You know, they will find cybersecurity issues.

[5518.82s] Um, and all you need to do is call the model. Um, and so I feel like, you know, that's the fundamental problem, is Mythos seems very powerful, not because the model is powerful, but because they actually bothered to test on all open source repos.

[5532.30s] Um, and so if you do... You know, if you call all these open source models to detect for bugs, for cybersecurity issues, you will find bugs.

[5543.26s] And you know, as, as, you know, recently, you know, as everyone knows, Fable is still banned for the majority [laughs] of everyone. Um, and GPT 5.6, you know, is delayed a staggered release, right?

[5554.78s] So, like, GPT 5.6 preview was on Friday, right? So, like, a few days ago, and they said they're not gonna be releasing to everyone. Um, and the main questions are, you know, in the open source world, in the closed source world, people are asking, do we need a license to use these AI models for everyone?

[5572.90s] You know, like, everyone in this room, now we have to have a license to use the models, like a driver's license. Um, do we need to get that? Um, is there going to be a delay in all of these releases?

[5583.10s] So every single time when a new model gets released, only the trusted providers get these models. Um,

[5590.30s] the next most important question. How about open source models? You know, okay, the government-- the US government currently is like tr- you know, trying to, like, control Fable, GPT 5.6.

[5601.82s] The main question now is what do we do about open source models? You know, open models, open weight models. What will the government do to control the open source space?

[5612.30s] To be completely honest, I was quite surprised the government acted this early, um, in doing GPT 5.6 and Fable control, right? I thought it was, like, maybe the end of the year or next year, but it seems like it's now.

[5622.84s] Um, so the next question is, what will happen to open source models? Will the government start controlling open source models? Um, and the fundamental question is what defines frontier intelligence?

[5634.96s] Like, the reason why the government is-- you know, they're controlling these models is because they're very, very powerful. Um, so the main question is what actually defines intelligence? You know, which benchmark do we use?

[5646.80s] Is it just based on one trillion parameters? Like, you know, how do we define whether a model can be banned or unbanned? Um, and that is a very, very important question.

[5654.72s] Um, and will we have a dark web of open models now? You know, do we need to torrent open models? Um, and the most important question, what is inference-- what are inference providers going to do now?

[5667.40s] You know, assuming, assuming that the government has some sort of regulation on, on even open models, um, what is the inference provi- what are they going to do? You know, what are the inference providers going to do?

[5677.60s] Do they need to have licen-- Do they need to check that ev- everyone has a license before you can use the model, um, or something like that? Um, and so, like, you know, these are very important questions that, you know, the government is currently, like, you know...

[5690.62s] And the industry, you know. The entire AI ecosystem and industry, we are trying to, like, you know, what are the answers to these questions? Um, and obviously, you know, if you were the government, if I was the government, it makes sense.

[5701.16s] You know, they do not want their critical infrastructure to be hacked. You know, remember, open source exploits are skyrocketing. If you change the y-axis, you know, not open source exploits, but, like, critical infrastructure exploits, you know, obviously the government's scared.

[5715.70s] Um, so it makes sense for them to, like, stagger the release. Um, but the main question is, you know, we're still in this, we're still in this fog of war type approach.

[5724.62s] You know? Okay, not fog of war, just fog. A foggy... You know, we don't know what will happen for regulation. Um, yeah. That's very problematic. Um, yeah. Oh, okay.

[5735.38s] Anyone have any questions for cybersecurity regulation, policy, whatever? Um, or any takes as well.

[5744.12s] Questions. Yes.

[5747.76s] I mean, given open source models are also very similar in performance to the source, is it-- are these, are these fears just overblown and FANG PR and, and Anthropic PR from, from Anthropic or some big player, some player fear that we should be worrying about?

[5762.18s] That is a good question. So is it, is open source-- So the scare of open source models, is it because, you know, Anthropic keeps screaming about open source is bad, open source is bad, you know, every single day, open source is bad?

[5774.68s] Um, yes and no. I feel like it's true that, you know, there are some players in the closed source industry, they wanna shut down the open source ecosystem. Their view is if you give open source to anyone, they will start hacking, you know, critical infrastructure.

[5792.34s] They will start doing bad behavior. Um, and so that's kind of their view. Um, so yes, I agree that some of the closed source labs have caused this problem.

[5802.68s] Um, but it's actually kinda funny because currently the government is regulating them first, and open source is still a question mark. Um, and so, like, it's kind of like...

[5812.58s] I don't know, they probably stabbed themselves in the foot or something. I don't know. Whatever, whatever the phrase is. Um, but I feel like it's--

[5819.16s] They did cause some controversy in terms of, like, saying open source is bad. But in general, open source models are actually good. Um, so you could-- I mean, theoretically, you can use an open source model and, you know, run this on all repos, and you will be able to find exploits, and you can exploit.

[5840.40s] So they're not wrong, um, but I feel like, you know, who has the infrastructure to do this? Um, you know, GitHub might automatically detect you and ban you or something.

[5848.46s] I don't know. There's many, there's many, um, layers of security for each section. Um, and so, like, I, I don't know. I, I feel like it's somewhat overblown, but it is, it is-- it's not zero percent probability.

[5861.80s] So it is a problem. Um, yeah. If that answers your question, but... Okay. Yes. So now we're gonna be talking about kernels. Um,

[5871.88s] so previously, you know, this is my favorite plot [laughs] as usual. Um, you know, if we were in a different future, you know, if we were in a different timeline that we did not discover o1-preview- Models would have plateaued.

[5885.86s] I think that's the fundamental point of this plot. It shows that if we have never discovered reasoning, we have never discovered o1, whatever, we will have plateaued, we will have plateaued in terms of accuracy.

[5897.28s] Um, and that is not good. Um, and because we have discovered this new paradigm of scaling, you know, models have continuously scaled even further.

[5905.24s] Um, but my take is the reason why we have stopped scaling, um, based on, you know, the old approach, is because the old approach only focused on hardware optimizations.

[5917.72s] We now have to move over to software optimizations and algorithmic optimizations. Um, we sh-- you know, we need to have new inventions of how do we scale AI even further.

[5927.82s] Um, and we can't just rely on doing ten trillion parameters or, you know, making the model bigger and bigger and bigger and bigger. Um, for example, you know, we have to do float8 reinforcement learning.

[5936.48s] Um, so if PyTorch has this methodology where you can do float8, float4 different precisions to make training faster, um, and that is one way. Um, another way, for example, as a software approach, for example, as I previously said, we found some bi-- you know, issues in gradient accumulation.

[5951.24s] Um, so when you do gradient accumulation, um, it was actually-- it was not calculated correctly during the loss calculation. Um, and you can actually increase accuracy by one to three% if you fix this small little issue.

[5965.00s] Yeah, so like, you know, the universal gradient accumulation bug fix was a software fix. It is not a hardware fix. Um, and so the fundamental view is you need to do more and more software changes, right?

[5976.29s] Another one, for example, Snowflake, we collaborated with them to make context, long context fine-tuning five hundred K context length. This was all software improvements. Um, another one is, you know, twelve times faster MoE training.

[5987.42s] This is another software improvement. Um, DeepSeek. You know, they released something called DeepSpark, which was just a few days. Um, and they showed that they can make inference, you know, fifty, fifty to six hundred percent faster, so six times faster than just normal MTP.

[6004.12s] Um, and so this is a software methodology, right? Not a hardware methodology.

[6009.94s] And, you know, DiffusionGemma, right? Gemma released a new diffusion model showcasing that you can get two thousand tokens per second by using a new architecture, right? So using diffusion LLMs to do faster inference.

[6022.90s] And again, this is a software change. And my main point is, is that in general, hardware innovations are getting less and less important. Um, and hardware innovations are actually slowing down.

[6035.98s] Um, so it's actually kind of interesting. Intelligence, you know, the scaling of, you know, intelligence in general, it's kind of like Moore's Law. Um, it's kind of like a-- there is a relentless progress, relentless approach to increase intelligence, and the same with Moore's Law.

[6052.76s] Um, and so like in general, you can see that, you know, this is Moore's Law over here. The number of transistors has continuously increased. Um, but, you know, single-thread performance is not increasing.

[6063.78s] It has stagnated. Um, and so this is kind of like, you know, this kind of reminds me of, you know, this plot, right. Scaling intelligence in terms of parameters probably has plateaued most likely.

[6076.50s] You know, hardware performance, pre-training, whatever. We now need to go into this new reasoning paradigm to scale even further. Um, so it kind of is like similar to the Moore's Law type graph, um, kind of.

[6088.42s] Um, and you can see, if you see on this side, the number representation of GPU. So why are GPUs getting faster and faster and faster, right? It's not actually the GPU itself that's getting faster and faster and faster.

[6099.96s] Um, it's the repres-- number representation, right? So like they change from float thirty-two all the way to float four. Um, and this made GPUs thirty-two times faster. Um, so it's not eight times faster, right?

[6112.66s] It's not thirty-two divided by four is eight times faster. It's thirty-two times faster. And the reason why is because of Tensor Cores, um, you know, the smaller mantissa, um, and so on.

[6122.86s] Um, and so like you can actually see, you know, even Tensor Cores with the introduction of Tensor Cores, it made the GPUs twelve times faster,

[6130.94s] and so on. Uh, actually, if you made the GPU smaller and smaller and smaller, it only made it three times faster. It's not even that important anymore. Um, and if you look at this plot, we are now at float four.

[6143.32s] So most of the GPUs that we have now are at float four. What is next? Are we going to be having float three, float two, float one? Are we going to have float zero?

[6154.34s] Okay, no such thing. But anyways, the point is hardware is kind of at its limits, right? We're already at float four. What is next? There is nothing next. Um, and so the, so the answer to this question is there is nothing next.

[6167.20s] Um, and so now we need to move over to software, right? How do we make new algorithms? How do we make new methodologies to continue scaling? Um, I also made this table, right.

[6176.78s] I previously said, why is, you know, you use float thirty-two, um, we change it to float four. Why is it, why is it not eight times faster? Um, and instead it's thirty-two times faster, right?

[6188.06s] Why is it thirty-two times faster? And the reason is because when you use-- when you do floating point precision, you have an exponent and a mantissa. Um, and the transistor space, the transistor space is the exponent plus the mantissa squared.

[6203.40s] Um, and so the trick is, if you make the mantissa smaller and smaller and smaller,

[6208.90s] you square their number of improvements, right? So float thirty-two, float thirty-two, you needed five hundred and thirty-seven transistors around, right? Five hundred and thirty-seven transistors. Um, to go from float thirty-two to float sixteen, you only need one hundred and five transistors.

[6224.66s] So actually you made, you made in the number of transistors five times more, right? So not two times, it's five times. Um, and so on, so on, so on.

[6234.52s] Um, so, you know, I guess you can go to one point five eight bit. I guess you can do that. Um, but it's actually kind of interesting because one point five eight bit, um, is actually not that much faster.

[6245.44s] Um, so one point five eight bit is actually not that much faster, um, than float eight. Um, if you use, um, you know, seven, seven mi-- seven exponent and mantissa two.

[6254.16s] Um, there is another one point five eight bit which you use float four. Um, so float four is one hundred and seventy-nine times faster than float thirty-two. Um, and the main question is we are already at three transistors, right?

[6265.12s] We are already around three transistors. What are we going to do next? Two transistors or like one transistor? So do-- like, you know, most likely GPUs are not gonna be getting faster.

[6275.48s] Um, that's the fundamental question of this plot. So GPUs are not gonna be getting faster.

[6282.06s] Instead, we need to focus on kernels, right? How do we make better kernels, better algorithms? How do we scale this instead, right? Don't do, don't do hardware optimizations anymore.

[6293.12s] Instead, how do we do, you know, these optimizations? Um, and so one of my favorite tools to use, you know, everyone should use this, is just use torch.compile. Um, so in my-- you know, it's the modern, you know, the modern time, do not-- as advice, do not learn how to write custom kernels.

[6313.20s] That is advice. Do not do kernel writing. Um, and the reason why is because torch.compile will take over all of kernel writing. Um, so you can see, for example, this plot, um, torch.compile was the red line, right?

[6327.54s] Performance. It doesn't look like it's doing [laughs] very well, right? It does not look like it's doing very well versus handwritten kernels, right? Handwritten kernels are the other ones, right?

[6336.74s] So torch.compile doesn't look like it's doing well, but that's because that's an old PyTorch version. If you have a newer PyTorch version, torch.compile wins dramatically, right? That's the orange line.

[6349.46s] Um, and all of these are handwritten kernels. Uh, the-- Okay, the black line is torch.compile plus nerve fusion. Um, so that's another torch.compile method. Um, but the red line, the green line, and the blue line-- Okay, the, the blue line is just no torch.compile, just normal PyTorch.

[6365.14s] Um, but the green line and the black li-- the green line and the red line are handwritten kernels. And you can see it does even worse than torch.compile. So like my view is like, what's the point of writing kernels?

[6377.38s] torch.compile does even better than you. Um, so the main point is you should always firstly look at torch.compile, right? Before you write a kernel, use torch.compile first. Do not start learning how to do Triton or, you know, CUDA or whatever is your favorite coding language for kernels.

[6395.32s] Don't do that. Instead, use torch.compile. Um, even worse, like, you know, this, this was RMSNorm. Um, you know, this is LayerNorm. torch.compile wins dramatically, um, you know, versus handwritten kernels.

[6409.64s] So I would not, you know-- Definitely only use torch.compile as your first try. Um, do not write kernels first. Use torch.compile.

[6420.54s] So the main takeaway is algorithms are much more important than hardware or whatever, handwritten kernels, right? Remember, DeepSeek released deeps-- you know, De-- uh, you know, DeepSpark. You know, there's other algorithms for, for speculative decoding like MTP, DFlash, DeepSpark, whatever.

[6437.81s] All of these are algorithmic improvements, and these made inference two times to six times faster, right? It wasn't like new, some new hardware. It wasn't some new hardware which made inference faster.

[6449.56s] It was algorithms which made inference faster, right? FlashAttention, Flash-- you know, FA2, FA3, FlashAttention four, FlashAttention five, six, seven, whatever. Right. All of these are algorithmic improvements, right? FlashAttention was ess-essentially a trick to do memory movement much better.

[6468.90s] Um, so how do we, like, orchestrate memory movement and use the caching structure of the GPUs much better? Um, and so FlashAttention's also a algorithm. Gradient checkpointing. You know, one of the most important algorithms for training is gradient checkpointing.

[6484.12s] Um, and all it does is you do not save all the activations. You do a trick where you only save the activations for every single layer, um, and then you skip all the intermediate activations in each layer.

[6495.24s] Um, and then you recompute the activations. Um, and gradient checkpointing saves memory by dramatic amounts, by like seventy percent. Um, seventy percent memory reduction with no change in accuracy.

[6507.38s] And, okay, training is a little bit slower, maybe by ten percent to fifteen percent. Um, and, you know, gradient checkpoi-check-checkpointing was an algorithm. Um, and you know, like in general, you should also try to understand, you know, what is the new data processing tricks.

[6522.20s] You know, how do we like, you know, stagger data? You know, do we do, do we do curriculum learning or something like that? I don't know. Um, we-- you know, how do we clean the data set before we actually pre-train the model?

[6533.08s] There are many tricks you can employ for data processing. Um, and obviously, you know, there is still a group of people--

[6539.86s] I don't know, I'd take an opposite view. There is a group of people who think mega kernels are the latest and greatest for kernels. You know, what is a mega kernel?

[6547.98s] A mega kernel is when you take an entire, you take an entire implementation of a model, and it's just one kernel, like one large kernel. Um, uh, maybe it's useful.

[6558.80s] Who knows? Um, you know, uh, you know, NVIDIA, you know, uh, NVIDIA has, uh, uh, ac-acquired Groq or something. Um, and you know, their view is, for example, you have two different systems, right?

[6569.66s] The LPU, which is the Groq system, does the decoding, right? So like the MLP layers, the MoE layers, does the decoding. And then the GPU, so the NVIDIA GPUs, does the attention and the prefill.

[6581.80s] Um, and so in general, you know, we might even have a future where we have different types of hardware systems. You know, we have ASICs, which are, you know, specially designed chips for, you know, computation, and we have generalized systems like GPUs.

[6596.10s] Um, and these ASICs and GPUs will collaborate with each other. Um, so for example, the attention, you know, the, the attention will be for the GPUs, and they will transfer over To the LPU to do m-- you know, the MLPs, the MoEs, and so on.

[6611.94s] Um, and then this is like a dance, you know, between them. And you can also do, like, pipelining, right? You can imagine that there's like many, many, many replicas of this, and they can like, you know, serve, you know, twenty people or, you know, one thousand people in one go.

[6624.92s] Um, and yeah. So this is, like, another approach. And, you know, this-- in my view, this is kind of an opposite approach of mega kernels. So as a mega kernel, your view is you want to combine...

[6636.55s] The goal is to make-- The goal of a mega kernel is to make one kernel for the full forward pass of a language model. Um, and once you make one-- once you c-- once you are able to make the language model, the forward pass into one kernel, you can now make the entire language model with thirty-two layers

[6654.98s] as one kernel, right? You can extend this. And then because the whole language model is one kernel, you can even further extend it, right? The prediction of the second token, the third token, the fourth token, the sixth token can all be just one kernel.

[6667.62s] Um, and unfortunately, this is very hard to do. It's very hard because attention is the problem, right? Attention has to see the tokens in the future. Uh, see the to-to-tokens in the past, not the future.

[6680.24s] That's cheating. Um, you have to see the tokens in the past, and that is a fundamental problem. Um, and it's very hard to, you know, it's very hard to make a mega kernel to combine attention and the MoE or MLP layers.

[6692.54s] It's extremely complicated. So in general, what, what people do is they'll make two kernels, right? One kernel for the attention part and the other kernel for the rest. Um, and so you will see there are two kernels.

[6705.29s] Um, and yeah. So it's very hard to make one mega kernel, but you can make two kernels.

[6712.82s] Yes. Okay. Any other questions? Any questions for kernels? So the main takeaway for... Yes, a question. Yes. That is a very good question. So the question was, because there's so many knobs for torch.compile, like one thousand or something, how do we reduce the experimentation time to like, you know, find which knob is the best?

[6728.36s] Um, so luckily, we have something called bisection or binary search. That's the trick. So what we will do is instead of checking every single one thousand combination, randomly sample.

[6739.54s] So random-- you do randomized bisection. You randomly sample fifty percent of the, you know, flags. You turn it on versus turning it off, and then benchmark which one is better.

[6751.10s] And whichever one is better, you then narrow down the search. You again do fifty percent and fifty percent and fifty percent and fifty percent. So it's actually log two of one thousand.

[6761.04s] I don't know about that. What is a log two of one thousand? I don't know what that is. Um,

[6765.40s] uh, two times... I don't know. Well, anyways, log two one thousand. I think you need to do thirty steps, I think. Or I don't know. I don't remember. Whatever.

[6772.66s] Two to the power of something is equal to one thousand, then log it. Um, so you, you only need to do-- You don't need to do-- You don't need to check all one thousand knobs.

[6780.90s] You only need to check a few steps, and then you will know which flag is the best. Um, so the trick is to use binary search or bisection to do this approach.

[6790.54s] Um, yeah. Yep. Yeah. Any other questions? Yes.

[6798.54s] Um, [clears throat] what are your thoughts on ASICs of like companies like Cerebras and Groq and SambaNova Labs? Um, do you see their future as real, or they're still a bit too immature to consider as a real possibility?

[6818.92s] So your question was, what do I think about ASICs, like, you know, Cerebras, Groq, SambaNova, I don't know, even startups, new chips. They do design their own chips. I feel like-- So the problem of ASICs is-- Is it ASICs or ASICs?

[6834.04s] Uh, whatever. The problem of specialized chip, chips is the architecture itself needs to be

[6841.92s] hardcoded in some of the chips, and that is the problem. If you hardcode some of the chips, you know, hardcode the infra-- hardcode the architecture, labs always like to change the architecture.

[6854.05s] And so every single time when the lab changes the architecture, do you need to update the chip? Um, but as a GPU, the GP-- The trick of GPUs is NVIDIA has made it, you know, NVIDIA, AMD, Intel, whatever.

[6866.22s] The GPU is extremely powerful because it has generalized ASICs inside of the GPU, right? The G-- The GPU is, in fact, a combination of ASICs. Um, and the ASIC is just one large ASIC.

[6880.10s] Um, so I think like in general, a GPU is much better because you can customize what goes inside the GPU. You can disable stuff that goes inside the GPU and stu-- such, yeah, so on.

[6890.76s] So my view is, I don't know. I don't--

[6894.06s] I mean, I don't wanna say anything, but like in general, I don't think...

[6898.14s] Like, you know, previously, as I mentioned, you know, hardware, there is nowhere else to go. You know, we are at float four. Unless if the hardware providers invents float, I don't know, float zero, then maybe we get four ti-- you know, another four times faster.

[6913.20s] But in general, I think, I think just people are focused too much on hardware, and they have not looked that actually the biggest improvements is not hardware, it's software, right?

[6922.22s] Numerical precision. Numerical precision was thirty-two times faster. Hardware is only three times faster, right? So hardware only contributed three times faster. Um, oh, actually, di-- Okay, the die size, you make the di-- you make the GPU bigger, you get two times faster.

[6937.36s] So that's, that's kind of cheating. So I, I wouldn't really say that's improvement. Um, but essentially, if you make the hardware faster, you only get three times faster. Um, so in my view, hardware is probably overblown.

[6948.38s] You know, hardware is actually not that important. The software was the trick that NVIDIA, you know, NVIDIA, AMD, Intel, all of these, you know, hardware providers, they banked on the fact that numerical precision was the trick, and tensor cores.

[6961.78s] Tensor cores, numerical precision, sparsity, you know, these software tricks. Um, okay, well, tensor core is not really a software trick, but you know, a tensor core is kind of an ASIC inside of the GPU.

[6973.30s] Um, and so, like, I feel like that's- Yeah. So my view is I don't, I don't really see a future for ASICs. That's my view. Um, I think that ASICs are like-- Instead,

[6982.82s] you know, to be honest, I'm actually quite surprised. We have lots of ASIC companies, but we have very few algorithm companies. Um, and the reason why is because ASICs you can sell, right?

[6993.04s] Every single year you can upgrade, you know. This year you pay one thousand dollars to ASIC version one, and the next year you have to upgrade, right? The problem with algorithms is algorithms is very hard to, you know, force the user or whatever to pay again.

[7009.25s] And so that is why hardware is very popular, because hardware is a very easy business model. But for algorithms, it gets more complicated, right? How are we going to monetize gradient checkpointing?

[7018.64s] I don't know, right? That's very hard. Um, so-- But the main point is the large labs themselves, I think like OpenAI announced a collaboration, Broadcom and Cerebras, whatever, you know, each lab themselves are going to the hardware provider and designing the chip with them.

[7034.56s] Um, so my view is like, maybe we'll have more of these like collaboration approaches, but I feel like standalone, standalone ASICs, I don't think they're going to last. Um, yeah, that's my take, I guess.

[7046.84s] Any other questions? Yes.

[7049.90s] So what are the kind of changes that you mostly see for like using models? I remember Gemma four came, and it was crazy that, uh, uh, Unsloth, and then you fixed it later.

[7063.22s] A fused loss could work it.

[7066.16s] Oh, you mean what are the types of kernels or...

[7068.70s] Yeah, what are the changes that we use for them to get these kernels? Uh, is there a change needed or like-

[7075.48s] Oh, okay, okay, okay. Um, so the question was what are the da-- you know, what are the changes for kernels or optimizations or stuff that is like interesting, I guess, for kernels.

[7083.52s] Um, so most kernels, when you write kernels, the majority of them are, are focused on memory movement reduction. How do we reduce memory movement? That's the majority of kernels.

[7095.96s] Um, for example, there is-- there's a trick called, um, you know, there's a trick called fused cross-entropy loss, where instead of making-- instead of the last layer of contr-- instead of materializing the full logits, there is a trick.

[7108.52s] You can do it in batches, right? You can do row by row materialization. Um, and so this would reduce memory by like a lot, by like, I don't know, ten GB or something, if you have long context or even more.

[7119.16s] Um, that's one way. Um, the other kernels-- Most kernels are called kernel fusion, where you, you have this like long PyTorch function,

[7129.38s] and all you do is you just write one kernel to do this whole PyTorch function. And torch.compile will do this for you. So torch.compile is very, very good at doing kernel fusion, right?

[7140.32s] You give torch.compile a function, it will write a kernel, a Triton kernel, whatever kernel, and it will just fuse everything. Um, it's very, very effective for that. Um, but I think in general, kernels are just reducing memory movement.

[7154.66s] Um, and so like I-- You know, to be honest, I don't really like to call it kernels. Most algorithms-- So most algorithms you either ha-- make training faster or reduce memory usage.

[7164.20s] Um, but kernels, in my view, kernels is reduced memory movement. Um, and so most kernels is just memory movement, you know, memory movement optimization, right? How do we, how do we use the caching structure of the GPUs?

[7176.70s] Um, you know, how do we not load the same variable twice or three times or whatever? Um, yeah. I'm not sure if that answered your question, but-

[7184.26s] Yeah.

[7184.58s] Next, reinforcement learning. Um, and after this will be reward hacking and agents. Um, so as a primer to re-- I'm assuming most people know, the most people know reinforcement learning, or do I need to prime people?

[7196.78s] Okay, I'll give a very fast primer for reinforcement learning. Okay. Fast primer for reinforcement learning. Um, what is reinforcement learning? You have this environment, such as this Pac-Man game, um, and your goal is, as the player, you know, to maximize reward.

[7213.86s] You want to eat all of the cookies, right? You wanna eat all of the cookies, but also escape away from your-- the monsters. I don't actually know what they're called.

[7220.74s] Enemies, monsters, whatever. Whatever they're called. Um, and your goal as Pac-Man is you want to maximize the amount of cookies that you eat, um, and that is your reward.

[7230.60s] The reward is the cookies. Um, and the action is whether you go up, left, down, or right. Um, and the environment is the game.

[7241.10s] Another good example, you know, another way I like to explain reinforcement learning is the goal of reinforcement learning is you want to have more good and less bad, um, during training.

[7250.96s] Um, so for example, at the very beginning of training, you ask the model what is two plus two? Um, the answer is clearly four. Um, but when the model starts training, it will be very dumb.

[7262.96s] It will be very bad. It will see B-- You know, the model will just say B, D, cat, dog, house, mouse, whatever. Um, and the trick is for all of the bad responses, you want to decrease-- You don't want-- You wanna like negatively reward this or penalize it.

[7279.32s] You wanna penalize the model if it says something bad, and you want to increase the reward if it says the correct answer. Um, so that is the trick of reinforcement learning.

[7288.22s] You just want more good answers, less bad answers. Um, and if it's like, you know, very close to the correct answer, so you know three is very close to the correct answer, um, you want to reward-- you want to negatively reward this a little bit less, right?

[7302.70s] Because three is much closer to four than B or D. Um, so if you do B or D, you want to negatively reward it massively.

[7313.02s] In reinforcement learning, the trick is you have a verification system, right? You have a verifier to verify if the model is doing good or bad. Um, so you call the model many, many, many times, um, and each of these examples, you give a verification number, right?

[7328.08s] So for example, um, the first example is very good, so you give it a plus ten score. Um, the next example is like, okay, so you give it a minus five score.

[7337.92s] Um, and then the last example is very bad. So you give it a minus one hundred score. Um, and reinforcement learning allows you to assign scores to each of those answers and questions.

[7348.75s] Um, and so that's kind of reinforcement learning ver-verifies. Um, and the trick of reinforcement learning is-- my favorite phrase is patience is all you need. Um, at the very beginning of training, your model will do very bad, right?

[7364.41s] Your, your reward will be zero, zero, zero, zero, you know, zero, zero, zero. You wait for a very long time, and then you will get the correct answer, right?

[7372.65s] So for example, this example, you ask the model what is two plus two, right? You start pre-training the model, you start pre-training the model. The model doesn't know what is two plus two, but after ten years, it will say four.

[7384.21s] Um, okay, obviously not ten years. I'm just exaggerating. But after ten years, you wait ten years, the model will then say four, um. And

[7393.31s] that is why my favorite pha-phrase is luck is all you need for reinforcement learning. You know, maybe by chance you will get four very quickly. Um, but you know, maybe you just have to wait, and wait, and wait, and wait for eternity until reinforcement learning works.

[7408.17s] Um, and so in general, your reward will be zero for a very long time, and then you will get m-- you know, you increase reward, um, after the zero.

[7418.83s] And you know, for reinforcement learning, there is a very simple algorithm for reinforcement learning, and the trick of reinforcement learning is remember, you know the final answer. You want to re-- you-- for example, you know, what is two plus two?

[7433.37s] You know the answer is four, but the problem is you don't know what is the reasoning trace. You know, did the-- was the reasoning trace good or bad? So for example, this example is, you know, to tell the model to create a fast matrix multiplication algorithm.

[7445.73s] Um, and the trick is, if the answer is right, you reward every single line as plus ten score. Um, and if it's wrong, you reward every single score as minus one hundred.

[7458.53s] Um, and you know, Andrej said, you know, in a Dwarkesh podcast, reinforcement learning is kind of like sucking supervision bits through a straw. Um, you know, we actually have stickers for them, if you like.

[7469.55s] Um, so you can get one of your stickers, which we can distribute at the end. Um, so Andrej's quote is this. Um, you know, and the main point is reinforcement learning is terrible, but everything else is even worse.

[7481.07s] Um, and so like, you know, reinforcement learning is the only tool we currently have that just works. It works, but it's not very efficient. Um, and okay, actually, my-- Okay, that's the next section.

[7492.43s] Um, but the main point is, okay, that's a reinforcement learning primer. Um, I guess does anyone have questions on reinforcement learning primer?

[7499.79s] No? Okay, I'll skip to-- Okay, one question. Yes.

[7503.59s] What would be a better technique than RL if there are any that you like?

[7508.01s] I will mention that in the next section. Um, there is, there is like, you know, better RL methods, um, but in general, reinforcement learning seems to do very well for now.

[7517.93s] Last, I think this is the last topic, or maybe not. Reward hacking and agents. The most fun one, I guess. Um, so okay, for reinforcement learning, reinforcement learning can only work if the probability of a good answer is more than zero.

[7535.63s] If it is less than zero, reinforcement learning will never work. So that is a fundament-- That is a constraint of reinforcement learning. The probability of a good answer must be more than zero.

[7544.69s] It can never be zero. Um, and there are many, many, many problems of reinforcement learning not working. You know, the formatting could be wrong. You know, you need to do some sort of priming or warm-up.

[7556.55s] So you have to do like some sort of trick to teach the model a little bit about, you know, about the thing that you're trying to maximize. Um, you have to do supervised fine-tuning.

[7566.89s] So one of the tricks of reinforcement learning is you actually need to do SFT or fine-tuning to make the model not dumb, right? To make the probability of zero not zero.

[7574.97s] Uh, the probability of a good answer not zero. Um, you need to do good pre-training. Um, and then the other problem is that, you know, during reinforcement learning, it's just way too out of distribution that reinforcement learning is just very bad.

[7587.29s] Um, so there are many, many problems of reinforcement learning.

[7591.11s] And I think we'll just-- You know, for the trajectories, reinforcement learning can assign incorrect rewards to the trajectory, right? Remember, the simple trick of reinforcement learning is we assign the reward to every single line as the same number, right?

[7605.97s] Either this is good or this is bad. And this is not good, because why? Right? You ask the model, I need to find what is two plus two. The answer is correct, right?

[7616.97s] The answer is four. The model says it's four. So you reward this whole thinking trace as plus ten. But this is wrong because, as you can see in the thinking trace, it says two plus two is equal to ten.

[7629.01s] Imagine, you know, in all of training, because the trick of reinforcement learning is we just literally assign ten to every single line or minus one hundred to every single line, we missed this bad, you know, bad thing.

[7642.53s] Um, so you can imagine when we keep training the model, the model might hack or do reward hacking or, you know, make gibberish. It will do gibberish in between, do some, do some sort of like new machine language which we can't read, and it will assign high score to that.

[7659.73s] Um, and so this is a very big problem of reinforcement learning.

[7664.83s] And the way to solve this or fix this is something called process supervision. Um, and process supervision, what you do is you manually check every single line. Not-- You don't just assign plus ten to the final, you know-- The answer is correct, right?

[7678.69s] The answer is correct, plus ten. Assign every single line as plus ten. You don't do this. Instead, what you do is you assign every single line as a different number, right?

[7688.53s] You assign some lines as plus thirty, some lines as plus zero, whatever. The bad lines as minus one hundred, right? This works very, very well. Um, unfortunately, process supervision cannot scale and is extremely expensive to do, right?

[7706.15s] Who's going to label this? It's the, you know, the humans, I guess, right? We have to label this data, right? We have to manually label for the labs. I guess that's why labs sometimes like, you know, they go to Scale or Mercor, whatever, right?

[7719.37s] They ask people to label the data. You know, is this good? Is this bad? Is this good? Is this bad? Um, and so on. Um, but the trick is you can also use a language model, right?

[7729.11s] You can use LLM as a judge. You can ar-- you can call a language model to label every single line. And, you know, uh, my view is like, you know, large labs are going to be doing this process more.

[7740.67s] They will call their own model iteratively to re-review itself. Um, and that is one way their view is they can reach AGI, right? Just b-by re-reviewing itself, right? Re-evaluating itself, rechecking, doing, doing, you know, automatic LLM as a judge process supervision, something like this.

[7760.39s] Um, but remember, there is a problem because even if you do process supervision, the model, you are using the same model to evaluate the model, right? The same problem as SWE-bench Pro, right?

[7772.53s] SWE-bench Pro, you use the LLM as a verifier to verify the LLM, which is definitely not good. Um, and the reason why is because you can do reward hacking.

[7782.65s] Um, a very good example of reward hacking is your model starts cheating. Um, so for example, when you want to make a fast matrix multiplication algorithm, all it does is it deletes the timer, um, right?

[7796.19s] Remember, you give the goal to max-- to reduce the time, right? Reduce the time of the matrix multiplication algorithm. Um, so all it will do is just delete the timer.

[7804.87s] Let's delete the timer, set the timer to be zero, and then there we maximize the reward. Um, obviously, this is not correct, right? Because the trick is you also have a correctness check, right?

[7815.91s] You check if the matrix multiplication is actually correct. Um, but there is another way. The model will edit your two matrices to be just zero. Um, and what is zero times zero?

[7826.93s] Zero. Um, and so the correctness checks also fail. Um, and so reward hacking becomes a very, very big problem because these models can cheat and do special tricks to go around your actual model, um, your intent of the reward function.

[7843.95s] Another very problematic example is it's not just about reward hacking. It can actually destroy your computer, right? By bad luck, your model might output, you know, some sort of corruption methodology, you know, deleting, you know, doing rm -rf on your entire computer and bye-bye, your computer's dead.

[7862.19s] Um, and so, like, you know, sometimes this also does happen. Um, so it's not just reward hacking. Also, trust of your tool calls, you know, trust of whether the model is actually doing good or bad is also a very big problem.

[7874.19s] And remember this plot that I showed, you know, if you include GPT 5.6 cheating on the benchmarks, you know, looking at the answer. You know, remember the previously SWE-bench, uh, SWE-bench Pro and DeepSWE show that models also cheat by looking at the final answer.

[7889.07s] You know, you can see that with GPT 5.6, if you cheat, it does very well. But if you remove the cheating examples, it does, you know, within trend.

[7898.39s] And then, you know, maybe you might be thinking, "Oh, this reward hacking thing is like, oh, it's like very rare, you know, very rare. It's not going to happen in real world."

[7905.93s] Um, well, GLM 5.2, during its training methodology, they specifically mentioned they have this new methodology for reinforcement learning called anti-hacking. Um, so GLM 5.2 introduced a method to stop, you know, reward hacking.

[7920.61s] Um, and what they do is they added a link checker. Um, so remember previously we mentioned how SWE-bench Pro, um, the model would cheat and look at the answer.

[7930.99s] Um, and so what GLM did is they had this check. Um, so during reinforcement learning, they will check every single tool call you make. Um, and if the website, if the website went to the answer, you would stop that from happening.

[7945.25s] Um, and so, like, GLM essentially added this, like, you know, filtering system for the entire reinforcement learning process. Um, and, you know, according to them, it worked very well.

[7954.89s] And remember this part about cheating examples. Um, you know, Opus, it seems like Claude's models like to always cheat, um, and GPT's models don't like to cheat. Um, but the main takeaway is models will cheat because you are, you are telling it, you know, like, you know, I want to maximize reward A, B, C, D, E, F,

[7971.87s] G. Um, and so the model will-- it will maximize it, but it won't actually follow your intent. Um, so you have to be very careful on this. Um, in fact, for GPT 5.1 during its training, OpenAI mentioned that they had something called calculator hacking.

[7986.53s] Um, and so in GPT 5.1 when they were training, um, they wanted to reward web tool use, right? So, like, you want to reward the model to use the web tool.

[7996.43s] Um, but instead, it didn't use the web tool. It used the calculator to fake the web tool. Um, and so during the training of GPT 5.1, this happened. Um, and so, like, you know, there's many, many, many, many problems with-- I think they showed, yeah, they showed calculator hacking.

[8011.21s] You know, you lie about which tool you used. Um, you know, you conceal uncertainty. You make facts up. Um, so there's many, many, many problems with, um, reward hacking, and this is not fake, right?

[8023.61s] So reward hacking is already in large labs training runs, right? This is just GPT 5.1. Um, I don't think so they mentioned GPT 5.2 or whatever. They're not-- Yeah.

[8031.75s] But i-in general, they showed that, you know, this thing does happen in real world. Um, you know, I don't know if you guys know GPU MODE, um, but GPU MODE does, you know, this leaderboard, um, for, you know, making faster kernels.

[8043.59s] So if you do want to write your own kernels, definitely post it on GPU MODE's hackathon challenges. Um, they're very, very helpful and very useful. Um, but you know, someone managed to hack, reward hack the GPU MODE kernel competition.

[8056.93s] Um, and remember, in the matrix multiplication example, there are two, there are two, there are two checks that we need to do, right? Make the matrix multiplication algorithm faster, but also it needs to be correct, right?

[8071.33s] There are two checks, the correctness check and the timing check. Um, and GPU MODE also had two checks, the correctness check and the timing check. Um, and so what do you think the model did?

[8083.19s] When the model w-- the model knew-- The model actually knew that it was being evaluated on the correctness check, right? It learned, "Oh, I'm being evaluated on the correctness check.

[8094.25s] I will now make correctness correct." Right? So it will output the correct kernel. And then the model knew that it was getting timed. And what it-- what did it do?

[8104.99s] It just, it just did the algorithm once and then saved it. And so it skipped all the other fifteen, um, you know, tests. Um, and so that's what the model did.

[8113.71s] So essentially, the model learned, the model learned that there were two tests, the correctness check and the timing check, and the model only did the correctness check correctly, and then once it went into the regime of timing, it cheated.

[8127.93s] Um, to be honest, this is actually quite scary. So essentially, the model learned that you're doing these tests, and the model actually knows you're doing the benchmarks. Um, and so this is actually very interesting.

[8137.99s] Um, and you know-- Oh yeah, this is, this is more and a, you know, larger example. The correctness check was fine, but the timing check, it cheated. Um, and all it did is it lo-- you know, there was supposed to be fifteen calls.

[8150.69s] In the first call, in the first call, it did all fifteen of the entire process, right? It did all of the fifteen runs. Um, and in calls two to fifteen, it just did a Python dictionary lookup.

[8161.13s] Um, yeah.

[8162.21s] I'll say, I don't know if you know about this. Very-- Right into the Volkswagen where they cheated on emissions. I don't know if you've heard about that.

[8168.77s] Yes. I-- Someone did tell--

[8170.43s] Yeah.

[8170.69s] Someone told me about it. Um...

[8172.15s] This looks very similar. It's like, "Oh, I'm not doing this. Let me turn this off." And then they cheated on, I think, outlined a lot of that.

[8178.05s] Yeah, exactly. So like, you know, it's not just models, I guess, that cheat. Even humans cheat, I guess. Yes. But I think it's called Goodhart's Law, that's the one.

[8185.05s] Like, if you have a benchmark, then the benchmark work becomes-- Is it Goodhart's Law? I don't remember. Yes. Okay. Yeah, the benchmark essentially becomes useless because people just cheat to maximize reward.

[8195.43s] Um, but yes, I guess humans also cheat. Um, yeah. Okay. Oh, my favorite example is, um, so on other labs, you know, you see on Twitter, on wherever, they say they made kernels ten times faster.

[8211.71s] Um, uh, no, no, no, that's not correct. They did not make kernels ten times faster. In fact, if you look through the code, they have no, you know, no-ops, so no operations.

[8221.59s] They also edited the timer. You know, they-- As I literally described, you know, I described they, you know, over here, um, you know, they edit the timer, they made matrices go to zero, they cheated.

[8233.83s] Um, and so, like, you know, this actually happened in real world. So some, you know, some of the labs, they published papers claiming that they made kernels ten times faster.

[8243.69s] But actually, if you read through the code and the examples, they-- these examples all cheated. Um, and so, you know, they re-- you know, this is not very good, uh, in terms of, you know, reward hacking.

[8254.19s] You know, reward hacking is a very big problem. Um, and you know, for example, what-- Some of the examples of kernel reward hacking, you know, not generating real CUDA code.

[8263.51s] Instead, it calls cuBLAS or some sort of, like, you know, already written system. Um, you have no-op kernels, which is essentially making the k-- you know, making the A and B matrix just zero.

[8273.55s] All it does is just doesn't do anything, right? It's just the kernel is empty, um, and you have, like, memory reuse. So you reuse the same answer over and over again.

[8282.69s] Um, you have timing synchronization issues, so that's cheating on the timer. Um, and my view is like, you know, if you do publish faster kernels or faster, you know, matrix-- If you think that your AI agent has made kernels ten times faster, please verify.

[8299.07s] You know, please look through the code before publishing because it is a very-- it's not a very good look. Um, and so-- And also, the biggest issue that I feel like people are getting-- forgetting is, you know, you made kernels ten times faster, you made matrix multiplication ten times faster.

[8318.35s] There is a theoretical limit for matrix multiplication, right? Matrix multiplication, you know, it's not-- You can't make it faster because there's mathematical limits on how to make it faster, right?

[8328.94s] And so, like, you know, matrix multiplication at the very, very, very olden times, you know, it's O of n cubed. You know, every single time researchers have make it faster and faster and faster and faster and faster, you know, it's now O of n to the power of two point three seven one three three nine, I guess.

[8343.17s] You know, researchers every single year are trying to, like, make this number smaller and smaller and smaller and smaller. Um, you know, I guess like, you know, one-- one five five two to one three three nine is not that small, you know, not that big, I guess.

[8354.21s] Um, but you know, they're having progress. But the main point is, you know, these researchers, you know, they show with mathematical limits, you cannot go faster than this. And so how can you do reward hacking that is even faster than that?

[8367.81s] Um, and so, like, the fundamental point is please verify. You know, to like the people who do research papers and stuff like that, please confirm your model is not reward hacking.

[8376.31s] It is a very big, big, big problem. Um, and you can see... Uh, uh, I think I only had one plot. Um, but yes, in general, please do not do-- Please check your, I guess, models.

[8386.63s] Um, I guess that's all for the talk. Um, you know, yeah. Thank you everyone for coming. Oh, more questions as well. [audience applauding] Um, okay. Thank you. Thank you. We also have...

[8398.33s] Oh yes, we have a whole bunch of stickers that you can take in the box over there and some pins and stuff. [outro music]
