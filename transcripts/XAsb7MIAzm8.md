# Don’t be data poor — Anuj Iravane, Anterior

Source: https://www.youtube.com/watch?v=XAsb7MIAzm8

Uploaded: 2026-08-19

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/59/5930a7bdb77bfcbd2076570674a823bc1fd82d3980a67e359b95c001516e5c16.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/XAsb7MIAzm8.json.

## Transcript

[on-hold music] Hello, everyone. Uh, welcome to, uh, Don't Be Data Poor.

Uh, my name's Anuj. I, uh, I lead AI at Anterior. Um, just a bit about Anterior. We are a clinician-led AI company, um, built for health plans, uh, backed by Sequoia and NEA.

Um, and what we do is we run AI transformations for health plans, um, as part of which we build, um, agents for, uh, several high-stakes, uh, healthcare administrative workflows in production.

Uh, things like prior authorization, payment integrity, uh, HEDIS measures, et cetera.

Um, it's, it's okay if you're not familiar with any of these workflows, uh, because a lot of the work that we do can actually be summarized, uh, in, in the same way.

It's, uh, policy-guided decision-making over highly unstructured data.

And the unstructured data looks something like this, right? You have, uh, uh, you have these scanned fax bundles containing medical records full of patient information. Um, a not-so-fun fact, uh, is that I think around seventy percent of medical communication still happens via fax, um, and fortunately or unfortunately, this is the data that we end up working with

the most. Um, it, it is a very, uh, rich, uh, and information-dense, uh, data that we see here. Um, the data distribution here is, uh, it comes from a very long tail of rare, uh, cases with very nuanced scenarios.

Uh, it models an entire clinical trajectory for a patient, uh, and every single person's journey is very different. Uh, it also presents itself in, uh, varied formats. So you have, like, uh, things like bad handwriting, tables, checkboxes, um, key-value pairs, images, um, a lot of tough data to deal with.

But I, I personally think it's a very fascinating source of data that we see here. Like, it's, it's, it's like sort of like an observation through a very fuzzy lens over an en-entire person's lifespan.

Uh, it's really unique. And I'm sure you must have heard this, like, enough times today already, but, uh, uh, in healthcare, uh, the, the baselines for accuracy are just, uh, exceptionally high.

Uh, ninety-five percent is not good enough. Um, at Anterior, this is why we invest very deeply in datasets and evals, uh, and these unstructured medical records are, uh, are a staple source of, uh, data for these evals.

And we, we work with this kind of data in almost every workflow that we try to automate.

But the problem is we can't really keep this data. Uh, it's PHI. It's highly protected. Uh, we can't retain it. We can't reuse it. Uh, we can't even derive information from it, and most of our contracts prohibit us from, uh, from doing anything like that.

Um, even things like, uh, redacting it, anonymizing it, and keeping derivative copies, like, that's a strict no-no, uh, completely off the table. So nothing real survives in any sort of dataset that we wanna persist over a period of time.

So, so what this talk is about is, like, what do you do when the dataset you most need is also the data you're least allowed to keep?

And the, and the bet that we, uh, the answer that we put our bets on is that we can kind of synthetically generate this data ourself.

There's been a lot of focus on syn-synthetic data recently. Uh, you've, like, frontier labs, uh, uh, striving to generate synthetic data for continued pre-training, for RL, for computer use, for agents.

Uh, so it's, it's, it's a hot topic, and it's, it's a hot topic on our minds as well. Uh, and the moment you say generate, like, the first thing that comes to mind is, okay, can we, can we try to use an LLM to generate synthetic data?

And I think you can. I personally believe LLMs are a, a fantastic, uh, tool to generate synthetic data, and several teams have already demonstrated, uh, this already. There's been some papers, uh, in the healthcare space, outside the healthcare space.

Uh, people have successfully used, uh, LLMs to generate synthetic data for, for different purposes. Uh, there are some known challenges in trying to use these LLMs, uh, uh, to create data, especially if you're trying to one-shot the whole process.

Uh, it's really hard to generate diverse, realistic-looking synthetic records, and this is even more of a problem, uh, when you're trying to doing... when, when you try to do this at scale.

So, uh, oftentimes these medical records, uh, are over three hundred pages long, and it's like imagining if you wouldn't ask an LLM to write a novel for you in one shot, right?

So it's the same reason why you wouldn't use an LLM to just one-shot a synthetic record for you. Um, and LLMs seem to suffer from this very strange mode collapse problem when it comes to generating, like, diverse, uh, data, creative data.

And I think there's two main reasons for it. Uh, the first one is, uh, uh, like Ayush mentioned in his talk earlier, there's very little exposure to this data source in the pre-training data corpus.

Um, and today's objectives for pre-training and post-training are, are largely, uh, uh, they're only in-- they're not incentivized for creativity or diversity really. They're incentivized to be helpful assistants.

So with these challenges in mind, uh, I'll walk you through, like, one of our approaches in how we, uh, managed to build a pipeline to generate synthetic data. Um, uh, earlier I mentioned, uh, our, our forward tasks look something like this, right?

So you have workflows and tasks that, uh, start with some unstructured data and a policy, um, uh, and you execute your policy against that data. You follow this reasoning trace through it, uh, and you arrive at some sort of an outcome, which is your label.

So this is our forward task. Uh, and the idea we had was to try and reverse this process. Uh, can we actually start by sampling a random label, um, uh, g- figuring out a, a reasoning trace for that label, and then trying to generate data backwards from that?

Uh, the idea here being that if you can actually, uh, sample these two things, uh, with enough diversity, uh, we will have-- we will be able to generate data that's conditioned on diverse set of inputs, allowing us to kind of circumvent the diversity problem a little bit.

Uh, so just a quick aside on policies. We've talked about policies a bit, but, uh, let me just clarify what these really mean, right? So this is an example policy we have for, for a CPAP device for patients.

Uh, this particular one is for a medical necessity review workflow.

Uh, and it, it sort of outlines all these diverse set of conditions, uh, that a patient might have, um, in which a CPAP device should be approved or, or, uh, rejected.

Um, so and this policy, as well as many other policies, uh, you can think of these as, uh, essentially decision trees that outline all these sorts of conditions, um, um, that, that dictate how some outcomes are met.

And at Anterior, actually, we, we spend a lot of time and energy in trying to model these policies explicitly as decision trees. Um, uh, we work with, uh, symbolic representation, uh, uh, similar to decision trees, uh, and it helps us achieve a better accuracy, uh, and consistency score when executing them in LLM-based workflow.

And, and the reason why I'm bringing this up is that, uh, by having this sort of symbolic representation of a policy, you actually have a, a way to kind of deterministically sample different reasoning traces for a given outcome.

So back to our idea of, like, reversing the process, right? Uh, this, this sampling of reasoning traces from the policy is, uh, what helps us get that diverse conditioning input to then generate medical records from.

Uh, and the key idea here is that the distribution here, uh, that we sample from is, is a much more uniform, uh, and effective prior distribution than what you'd normally get from an LLM.

And one added benefit of sampling this way is that in theory, you're able to test, uh, for far more scenarios than you would, uh, likely get from production data sources.

So what I mean by that is, like, say you get a sample of, uh, two hundred cases from your customer, uh, um, and, and, and, and you try to, like, have an eval that measures performance against that, and you get a ninety-five percent score.

Uh, it doesn't really tell you about, uh, what you-- what your performance would be in those rare edge cases that are not in that dataset. There'll always be rare edge cases, uh, that are outside that distribution just because of the fact that our data is so, uh, highly variant.

So for those, for those familiar with Synthea, like, uh, they follow a similar pattern, uh, of sampling scenarios from a symbolic causal state representation. There's a few other folks in the space who are, uh, working with these symbolic representations to, uh, to generate diversity in synthetic data generation.

So let me walk you through the rest of the pipeline. Uh, right. So, uh, once we have this diverse set of samples as our conditioning input, what we did was we built an LLM-based pipeline that, uh, follows, uh, a coarse-to-fine pattern to progressively, uh, uh, build up a med-medical record layer by layer.

So here we first start with creating some patient invariants, like the biological sex, the birthdate, the blood group.

Uh, we use that along with the reasoning trace, uh, with an LLM again, to produce an ordered list of, uh, events and provider encounters that a patient might have had, and we call this the patient journey.

So this is a high-level, uh, you can think of as a high-level, uh, overview of what a patient might have gone through in their lifespan, um, uh, captured by a list of events on a high, uh, in natural language.

And in the real world, it is actually only during these, uh, uh, encounters, provider encounters, that documentation is really generated, at least for the data that we get. Uh, uh, most of our, uh, data source-- data is generated during these provider encounters, so we model exactly that in our pipeline.

Uh, uh, we first generate a document plan for each encounter, and then based on that and the preceding history of the, of the patient, we, uh, we fan out into generating the actual documents, uh, um, to hydrate them with actual synthetic information.

Uh, and this coarse-to-fine layering, uh, is actually what allows us to keep, uh, the different prompt payloads in the pipeline, uh, very token efficient, uh, from both input and output perspective.

While also enabling, uh, we, we... This also helps us enable to scale across, uh, longer patient journeys. So you can scale this, uh, pipeline, you can have a much longer patient journey, uh, and you can just fan out and generate documents that way without, uh, overloading the context windows of your LLMs.

Uh, finally, we have this sort of refinement loop in the end, uh, that we-- that, that uses a set of evals to provide feedback, uh, to improve specific parts of the generated documents.

Uh, for example, one of the evals we have is an LLM-based check for consistency, um, between all, between all documents. So this makes sure that, uh, there's no contradictions or, uh, uh, inaccuracies or conflicting information between two documents that are generated.

And this is important because we, uh, we have a parallel fan-out process, uh, that is used to generate these documents independently.

And because we started with the labels for this particular, uh, pipeline run, uh, what we actually also have is, uh, an ability to kind of use those labels, uh, run and, uh, and, and compare those against the generated, uh, uh, medical records to see if, uh, the task that we u-originally used actually matches, uh, is the data

is in concordance with the task inputs and outputs. So we can do this sort of round-trip check to ensure that our data is actually in sync, and by default, get, uh, correct labels by construction.

So, um, in theory, uh, this is a really nice property to have. Like, you can ex-- basically skip the ground truthing, expensive ground truthing process you need, uh, for, for data, for real data.

Uh, one thing to clarify here is that, uh, uh, so far, all the generation has been happening just in plain text and Markdown text. Um, it is possible to go from that to a rendered PDF, uh, but we don't really see much value in, in doing that, uh, because, uh, we have state-of-the-art PDF parsers today.

Uh, they're available to everyone, uh, and they just allow you to convert any sort of complex PDF into a nice Markdown representation. So all of the synthetic generation, uh, um, and evaluation happens in the text domain.

So this is just an example of, like, a pipeline that we created, uh, from scratch, and it's, uh, it's very easy to build. It's largely fully LLM-based. Um, but, but who came up with this, right?

Like, who, who am I to, uh, know anything about what a good, um, um, medical record looks like? Uh, so how do we know if this is any good?

And, uh, I think this has been mentioned a few times today already, but, like, you really don't. Like, uh, no AI engineer would ever would. Like, you want your domain experts to be the ones telling you what's good, what's not good, um, and which is why we believe that, uh, it is of great value to empower your

domain experts to own your whole data pipeline.

And specifically, we, uh, we do this in two ways, right? Uh, we enable our clinicians to kind of interject at each point, uh, in the generation process with a human-in-the-loop mechanism.

So at any point, a clinician can steer the generation process to make a, a medical record in the way they want it. Uh, we often see our clinicians use this, uh, to, to, uh, to first look at cases that happen in production, get some interesting ideas, uh, and then use that, uh, u-u-use those ideas along with this,

uh, the steering in this pipeline to make, uh, cases that look similar to what we might see in production or they've seen in production. And this is what makes the data generated from this, uh, really useful, right?

Like, you can actually model your, uh, your failure cases, um, uh, beforehand or even, uh, after they, after you see them in production.

And secondly, I think most importantly, we let our clinicians also own the whole logic of the pipeline. Um, we do this by modeling the whole pipeline as a skills-based workflow running on a generic, uh, agent harness that we built internally.

So every, every, uh, kind of section here you see, uh, all the way from the patient journey to the document generation, to the document enrichment, to the evals, all of these things are skills, uh, that run on our agent harness.

As an example, if a clinician wanted to, uh, say, maybe add support for a new document type, let's say for a new customer, they wanted their intake forms, uh, to look a certain way, uh, they could easily just make a new skill file for it, uh, attach it to the pipeline, um, and, and, and voila.

There, there wouldn't be any engineering changes required, so it's completely clinician-owned from that perspective.

And just an aside, generally, I feel like skills are, are really an amazing, uh, interface between AI engineers and domain experts, especially in vertical AI. Uh, we see this, uh, being, um, uh, we, we see this being modeled in, uh, several of our other workflows, both for internal use cases and in production as well.

So some results from this, right? So even though we only really use, uh, synthetic data for evaluation at the moment, there's already a lot of merits that we get from it.

Um, roughly ninety percent of our datasets are, uh, already made of synthetic data. Uh, this helps us, uh, maintain a very high, uh, production accuracy score, um, for across many customer deployments.

Uh, the pipelines that we-- that I just showed you, uh, already we are able to achieve a, a very high fidelity on this generated data. Uh, in a blind review, clinicians were not able-- were only able to distinguish, uh, synthetic from real about sixty percent of the time.

So room for improvement, but, uh, uh, but, but it's, but it's, it's close. And I'm, I'm quite, quite-- it's a quite promising, uh, avenue for us to invest more, more here.

And, and the, the, the, the fact that is the most interesting to me and, uh, what I really ex- what I'm really excited about is that all of these datasets, uh, well, most of our datasets today then are created just in time for these customer deployments, right?

You can-- When you have the ability to like create data from scratch so quickly, uh, you can kind of, uh... You don't need to depend on, on, on waiting for data from a customer.

You can kind of just model all your edge cases, simulate them, and test your workflows before you go live with the production cust- uh, go live in production.

So, uh, some takeaways, uh, if you're looking to build your own synthetic data pipeline in healthcare or even another domain, um, try reversing your inference workflow.

Diversity should, uh, always be sampled from a, from an appropriate distribution for your use case.

Uh, try to emulate the process in which, uh, uh, the data was actually generated. So like I showed you, uh, we were trying to sort of like u-- we were-- Using LLMs, we were trying to emulate how, uh, our medical records might actually be generated during patient encounters.

Uh, so, and I, I would highly recommend you try doing that. Uh, and the fourth most important thing I think is, uh, when you're, when you're making a data pipeline like this, it's really important to give your domain experts the keys because, uh, these are the people who know, uh, about your data and, and, and they will

help you, uh, drive towards a, a recursive self-improvement, uh, not the AI engineers.

Cool. So you don't need a PHI problem for this. Uh, anywhere, uh, the data you need is ephemeral, sensitive, or even expensive to label, you can think about, uh, generating data yourself.

Uh, and hopefully, uh, you won't be data poor.

Thank you, everyone. [audience applauding] [upbeat music]
