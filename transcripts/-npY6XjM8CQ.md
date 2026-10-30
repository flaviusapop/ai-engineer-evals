# When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI

Source: https://www.youtube.com/watch?v=-npY6XjM8CQ

Uploaded: 2026-08-02

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/1f/1fb0275a3112c54107264ffda3de2e213dbf703ea5ca03c84dca20eba4aa7e7d.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/-npY6XjM8CQ.json.

## Transcript

[upbeat music] Let's get started. When will the benchmaxxing plague end?

In the tech industry, we love a hype cycle, and in AI, we really love a hype cycle. And the way we do that is when a model comes out, there's a big announcement, there's a lot of benchmarks cited.

Sometimes, to keep things interesting, we do a little chart crime, and then people actually go and use it. And if the expectations aren't met by the reality, then we have allegations of benchmaxxing.

Benchmaxxing, of course, being when labs are training too hard on benchmarks in a way that deviates from what people actually care about. So the existence of that term indicates that we have a sense that benchmarks don't always equal reality.

And so in this talk, we're gonna figure out why does benchmaxxing happen? Why are traditional benchmarks not always accurate reflections of real-world value? Is this intrinsic to all benchmarks, and will we ever know which models are best?

And the answers are incentives, poor methodologies, no, and yes. All right, that was my talk. Thank you so much for coming. Um, actually, it looks like I have a few extra minutes, so let's, let's move on.

I have a few extra slides we'll, we'll go through.

So we have a sense that benchmarks don't equal reality, but the industry is dominated by a lot of popular but very bad benchmarks. So there's millions of dollars on prediction markets being wagered on LM Arena outcomes, even as we have industry leaders openly bragging about gaming LM Arena.

And you have thought leaders like Gwern saying it can be easily gamed. It's past time for the LM Arena people to sit down and think about whether they're doing more harm than good.

Andrej Karpathy had a similar observation when he noticed that the models that he thought were best were not lining up with what LM Arena was ranking. And he said, "Unfortunately, the teams are not getting better models overall, but better LM Arena models, whatever that is.

Possibly something with a lot of nested lists, bullet points, and emojis." So why does this happen, that sort of industry insiders are telling us that this benchmark is not useful, but it still gets a lot of play?

The problem is that AI is aimed at everyone in the world, is, is something everyone in the world can use, and so everyone needs some tool to figure out which models are best, and benchmarks are what we have for that.

But if you can't-- If you don't have the ability to assess if a benchmark is good, what you do have is the ability to assess what's popular. And this creates this avalanche, this feedback effect, where the conversation is very much driven by incumbency and marketing, and less by real-world value.

And even myself, right? Like, unless I actually look at a benchmark in a fair amount of detail, I don't have an opinion on it. So it's a very challenging problem.

So what are the things that benchmarks do that lead to these problems?

There are a handful of key anti-patterns that we're gonna go through.

The first is price. Let's say you want to make an agentic coding benchmark, which these days is a very popular thing to want to do, and you want a thousand tasks in your benchmark.

Each task takes sixty hours to make. Each software engineer in your workforce costs half a million a year. That's fifteen million dollars to make your benchmark. And if you think that over time, about a third of those tasks are gonna get washed away every year due to models getting better, that's five million dollars to replace them.

So that puts you out of budget for most projects. So then people turn to a variety of workarounds that have their own problems, one of which is trying to use a lot of AI assistance, which ultimately does not really work.

Like, you can't push the frontier forward from within the frontier. You need to inject that external human expertise, and it needs to be good expertise. If you try to use cheap labor, you're gonna get what you paid for, and the whole result is not gonna be that useful.

At Surge, one of our differentiators has long been that we are not trying to minimize cost. We are trying to maximize quality. And part of that means paying a lot of money for good workers.

We've always believed that, but especially in twenty twenty-six, models are just beyond the point where you can make do with anything less than the best workers.

Contamination is often thought of as when labs are explicitly training on the test set, and that does happen sometimes. But really, contamination is the default outcome unless you are very, very good.

So labs put a lot of effort into holding back this flood of data that's gonna contaminate their models.

But inevitably, if you have public questions and answers on the internet, that's gonna get memorized to some extent. So SWE-bench Verified, here's an example prompt. You can give Opus the first part of the prompt, and it will verbatim spit out the rest.

It does that with the answers as well.

And we actually did an investigation where we compared looking at the repos that SWE-bench Verified was built out of,

how much has Opus memorized the SWE-bench Verified contents versus the rest of the repo? And we found very clear evidence that Opus had memorized a lot of SWE-bench. In the most recent model card, Opus 4.8 talks about its SWE-bench score.

It does not disclose this contamination. We as an industry aren't really in the habit of doing those disclosures. And so what that means is that as benchmark consumers, we're just missing that information.

Reward hacking is also a big problem. Reward hacking is basically when a model finds a lazy and creative way to meet the letter of the law, but not the spirit.

You need to think about designing your rewards as a adversarial process against this maximally lazy agent. Gradient descent is basically like water flowing downhill, looking for the path of least resistance, and so your verifiers need to be robust to that.

Another key challenge is simply just not having the ambition to make a sophisticated enough benchmark. Automation Bench tests that agents are able to make tool calls in an enterprise environment.

The problem is that a lot of the verifiers are these hard-coded string matches. And so you'll see it for things like phone numbers, where there are many different acceptable phone number formats, but this verifier just picks one, and the prompt doesn't tell you which one it is.

So the result of this is that Haiku and Fable both score twenty percent on this task. Haiku scores twenty percent because it makes a bunch of mistakes, and Fable scores twenty percent because it gets it right eighty percent of the time, but then just happens to pick different formats.

So if the benchmark task is not differentiating between Haiku and Fable, it's not a useful task.

And more broadly, in twenty twenty-six, many of us in this room are looking towards AI that's about to remake entire industries, and benchmarks are ideally our lighthouse on the horizon to let us know when that's coming, and a simple hard-coded string match is just not going to do it to measure that sort of impact.

Another important aspect of a good benchmark is taste. Perhaps it used to be the case that benchmarks were these dry academic, you know, question and answer sets, but nowadays, a benchmark is an artifact expressing what-- It's an, it's an aspirational artifact.

It's an expression of values of what you want your AI to do and how you want it to behave. And so you need to have some product sense in this process, some sort of a sense of what you want the AI to do, and that sense is unfortunately missing from IFEval.

IFEval has been cited on many model cards, and the way it was constructed was taking a bunch of arbitrary prompts that no user has ever asked in earnest and mashing them up with a bunch of other prompts to create a prompt set.

The problem is that because no user actually has asked, "Do not use any commas in your response," or, "Use the letter T at most once," you have to believe-- For this to be useful, you have to believe that there's a generalization from this to actual things that users are gonna ask.

IFEval just happens also to have a bunch of prompts that are fully unsolvable due to having contradictory instructions. So this one starts by saying, "Repeat this response verbatim," and it ends by saying, "Translate this into Hindi."

Obviously, you can't do both of those at once.

Here's one that says, "Write a riddle that includes exactly one bullet point. Make sure to inc-include a few bullet points." Again, this is just fully impossible.

It uses a sentence splitter that does not align with how humans would actually split the sentences,

and a lot of the prompts are not fully verified. So this one says, "Write a story." There's nothing in the verifier that checks that a story was written. It just checks that the ASCII character I is not used more than once, which means that all of these responses get a full score, including response D.

The way it gets a full score is by reward hacking and using the Cyrillic I character instead of the ASCII I character. IFEval is totally fine with that.

Another challenge is operational ability. Making a big benchmark requires a lot of QC work, and plenty of organizations just don't make that investment. APEX is a RAG benchmark where the agent is given files and then asked questions about them.

And in some instances, what's in the file and then what's expected in the rubric don't line up. So an agent that does the thing that it's seeing in the ground truth is gonna get a negative score.

And a lot of the data in APEX is seemingly synthetically generated because it's full of obvious placeholder values or dates or places that don't exist.

And so as a result, the model is more likely to develop eval awareness, where it realizes that it's being tested, which undermines the entire exercise. It also just takes you out of distribution from actual real-world data to something that is obviously fake.

So that's an overview of some of the key anti-patterns that happen during benchmark creation. But benchmaxxing is a two-way process, and there are all sorts of fun things that labs can do to benchmax, and that's what we're gonna talk about next.

So the, the core value that we're all trying to get towards is human eval, right? AI exists to serve humans, and so just having humans look at the responses and make ratings, like that's what we care about.

The problem is that human eval is very expensive, and so a lot of what benchmarks are doing is trying to get around that, and you are trying to distill human preference into something more scalable, and you're hoping you do that distillation in a way that's still sufficiently faithful to what human eval wants.

But what this means is that inevitably there is a point where you can keep hill climbing on a benchmark and the human eval stays flat.

And you can actually take it even further if you want, where you keep hill climbing on a benchmark even as the human eval goes down. But if for whatever reason you think this is necessary for marketing or we have sort of organizational politics or incentives that are demanding this, that's how it can end up happening.

In this instance, the prompt is, "What time is it?" And the response is absolutely deranged. No human eval is ever going to choose this. But LM Arena puts it at the top of the leaderboard.

So again, you have this divergence, and if you're trying to benchmax, you just cannot care about that. Another thing you can do that I've heard stories of is you can actually hire a crowdsourced army to vote for you on LM Arena, since LM Arena basically does no filtering of their workforce.

And you might say, "Well, we anonym-- You know, LM Arena anonymizes, so how are they gonna know who to vote for?" That's actually quite simple. You have your model include a watermark that tells the crowd who to vote for.

There's also all sorts of things you can do with running your evals in conditions that are, like, not fully representative of the apples to apples comparison you're trying to make, and then not always being super transparent about those conditions in such a way that undermines the validity that the community is trying to interpret because they don't have

that contextualizing information. This was a paper, um, again, about LM Arena and talking about how some of the dynamics of how it's run lead to models overfitting on LM Arena.

Um, in this instance, the specific chart we're seeing is that Meta tested twenty-seven models without disclosing that it was doing so, um, which, you know, distorts the results.

So how are we gonna end benchmaxxing? We need to hold the benchmark industry and the labs to a higher standard.

The first thing we need to do when making a good benchmark is start with great human experts, and those experts inform everything that is downstream from what types of tasks are we going to have the agent do, how is success measured,

what are the input files that agents are given, what are the tools that they're given. But we also do need that product sense. So imagine you're making a medical benchmark.

It's not enough to have doctors who can answer specific medical questions because if you're trying to test how ready are we for agents to be deployed into hospitals, you also need someone with the business sense to know what's the regulatory environment, what's the legal requirements, because that is gonna impact what types of tasks you're trying to have

the AI solve. You need high-fidelity input data, which is best done by going out and getting it from the real world, having actual people create this data. Synthetic approaches are possible, but it is very, very hard to do it reliably.

The tools need to actually work. A lot of benchmarks have tools that are buggy in various ways, and unless you're intentionally making a benchmark about buggy tools, this just introduces noise.

You need verifiers that are fully aligned with the prompts, and this is a two-way alignment. So the verifiers need to be verifying everything the prompt asks for, and everything the prompt asks for needs to be covered by the verifiers.

And if you get either side of those two misaligned, then it's gonna be unfair to models and you're introducing random noise.

You need to thoroughly QC everything, and you need to have a private holdout set so you don't get contaminated.

And if you do all this right, then you'll avoid what often happens with benchmarks, which is when labs get to, like, eighty percent and say, "Okay, this is saturated."

And I used to think that saturation was just them saying, again, "We don't think training on this further is going to increase real-world value." And it often does mean that, but it can mean that because the lab is saying, "We realize twenty percent of these tasks are broken."

But the problem is that as you're hill climbing, you don't know what twenty percent are broken until you solve all the others. And so as a result, you have a lot of noise, and if that twenty percent of broken tasks is randomly, but in a biased way, assigning the rewards, it's gonna really distort the model relative ranking

you're trying to get. So at Surge, we created a benchmark called Hemingway Bench to measure writing. There have been a number of writing benchmarks that each use various mechanical means to try to assess writing quality, but we believe that writing is just too rich and deep and nuanced and frankly human of an activity to measure with mechanical

benchmarks. And LLM as a judge doesn't really work either because LLMs don't have good taste in writing. Again, this is sort of the you can't expand the frontier from within the frontier situation.

So what we've done is we've just created a workforce of thousands of professional writers in various domains, technical writers, poets, journalists, editors, and we just have them do blind model comparisons, and then we create this leaderboard.

And it is quite expensive, right? Human eval is very expensive. Getting the time of these professionals is quite e-expensive. But again, our goal is to maximize quality, not to minimize costs.

So in conclusion, benchmaxxing is the exploitation of benchmark misalignments between human preference, but we can do better, and we can hold the industry to a higher standard, both the people making the benchmarks, like myself, and the people who are reporting on the benchmarks.

And if you'd like to be a part of that, of course, obligatory pitch, at Surge, we're hiring for basically all aspects of that. Uh, and if you'd like more spicy takes from me, uh, please follow my Substack.

Thank you very much. [audience applauding] [upbeat music]
