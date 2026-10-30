# Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo

Source: https://www.youtube.com/watch?v=kiqubc5b5Yo

Uploaded: 2026-07-29

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/e3/e37a286ab133a9d60376d0fbad51bcd556665ea6ec4264c4a92d8cc2f203a360.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/kiqubc5b5Yo.json.

## Transcript

[upbeat music] Well, thank you everyone for coming. Um, today I'll be presenting what we've been building at Morgan Stanley, uh, sort of auto research agent to try and automate quant research.

Um, and I wanted to just take the, the first couple of minutes to sort of explain, you know, give some context on our team and also, um, you know, why we're even pursuing trying to build this, this auto research agent.

And so our group, we're relatively small. We're about thirty, uh, PhD AI researchers, and we kind of operate both, like, kinda half academic, so we're encouraged to, um, you know, publish papers, open source code, share our research.

And then the other half is sort of more applied internal work. And, you know, I think a lot of our problems or, or, you know, at least some of them are, are-- can be fairly well-posed.

They kind of have a similar shape to Kaggle, where we have, you know, an input time series dataset, and our task is to just, you know, predict future values and maybe with some other constraints of wanting the model to be well-calibrated.

Um, and so I think, you know, being on the sell side, we kind of have maybe less sort of adversarial selection, and so it, it kinda lends itself naturally to this auto research framework.

Um, and, you know, also I think there's-- we have a lot of sort of algorithms in production where we c-- have a feeling if we could just put in more cycles, there might be some improvements to kind of squeeze out, whether it's just better hyperparameter tuning or exploring a lot of different kind of ensembling these different methods

together. Also, you know, we have-- we work with a lot of different desks, and there's a feeling that, like, something we have built for, say, credit bonds could really transfer well to, like, muni bonds, and that kind of translation process should be something that can be automatable with, with agents.

And even, like, going to new trading desks and trying to build them new algorithms, there's sort of a lot of low-hanging fruit where, uh, they're not really using a lot of machine learning or, or AI automation.

And so, you know, even, like, a reasonably trained model should be able to have a big impact. And so sort of in the last year and a half where these, these agents became, you know, able to do long-horizon tasks, we've been interested in trying to do this automation.

Um, but it wasn't really until December of twenty twenty-five, and I think this is a pretty common sentiment now that, um, it really felt possible for the first time with, like, with Opus 4.5 and with, you know, these harnesses like Claude Code and Codex, where it really felt like the models were at a point where they could

do these long-horizon tasks and also kind of the idea of putting them in these harnesses that, that allow them to do so. And so, you know, really starting this year, we kinda made it a big effort to build this, this auto research agent.

And of course, sort of the, the top line goal is just maximizing P&L and maximizing the, the number of new algorithms we can put in production. Um, but, you know, we also had these design concerns.

Like, of course, we want it to play nicely and integrate with all of our data and sort of the pre-built scaffolding we have around back testing and evals. We also wanted it to be able to run the full spectrum.

So, like, you know, on one side, maybe it's a new dataset and we just wanna say, like, "Here's the path to the data," a natural language description of what we hope to predict, and the thing should go off and do research, build its own eval, and start doing experimentation.

And then sort of on the other side of the spectrum, maybe it's like, "No, we have our data scripts, we have our eval, we actually have a few good models we've already produced," and we just want it to kind of churn and do more cycles and see if it can find an improvement.

Um, also, we wanted to build this to be really model agnostic, so we could use any of the frontier providers or increasingly, uh, you know, any open source model.

And also, we wanted to build it in a way that, you know, as these models get better and better, it's not sort of consuming what we've built. Like, we kind of rise with the tide of the models.

And lastly, you know, really carefully think about, um, how do we encode sort of like our enterprise knowledge as Morgan Stanley and then our human expertise as, as quant researchers.

And so for, for the rest of the talk, I wanna start with sort of what I'm calling AlphaLab 1.0, which is our first version we released, I think it was early April, and we put out a full, like, forty-page tech report going through all the details and results.

We also open sourced all the code on GitHub. So I, I kinda wanna cover that more at a high level because all the details are so public, but I'm happy to talk afterwards in, in depth about any part.

Um, but then I really wanna cover, you know, sort of what's happened since then. So what were the initial results? What were the kinda failure cases since then? Because we, we have encountered a lot of failures.

And then talk about how we're really addressing those by building, uh, kind of our own rich set of evals and environments and how that's sort of allowing us to

improve the harness and climb towards this sort of self-recursive improvement and sort of our grand vision now for AlphaLab 2.0.

And so to start, you know, AlphaLab is an agentic harness and kind of going towards that, that first side of the spectrum. The, the goal is you have some dataset, you know, let's say it's like a, a exchange rate dataset or something, and you can just provide the path to the file, or maybe it lives on an

API, and you can just say, "Here's the API acce-access and the API spec." And then just in natural language, say what you wanna predict. So maybe it's as simple as, you know, the simple exchange rate.

I would-- just I'm curious in predicting one day out what the, the rate will be. And the harness then works in these, these three phases. So the first phase is research, and I'll cover these all more in depth.

The second phase is then actually building its own evaluation or back testing. And the third phase is sort of the mass experimentation, which is really the heart of the, the harness.

And then as output, you get a suite of trained machine learning models that are trying to, you know, do the, the prediction you care about.

And one design choice we made, so the harness is actually all our own code, so we decided not to use any off-the-shelf agent framework. Um, we wrote it all, and really Claude wrote it all.

And I think like in the era of, of Claude code, I, I, I like this approach of kind of building your own from scratch because you get sort of max freedom and max like, you know, you're, you're free to kind of tweak anything you care about.

Um, and so, you know, all the tool calls are done with these like functional tool calling, and that also allows us to nicely really be provider agnostic. So OpenAI, Anthropic, or open source providers, it's very easy to, to adapt the, the harness to any, any of those.

As far as the actual tools, there, there's a-- there's several, but the sort of three main ones are, one, full shell access, so it can write any bash command.

So this is how it's writing code, setting up its Python environment, editing code, running code. Um, another important one is web search, and this allows it to go read, you know, arXiv or technical blogs or anything like that and get sort of up to speed at, um, you know, at least in the public domain, like sort of

what's the state-of-the-art methods. And then the third one is, um, we use Slurm to manage our GPU cluster, but the, the higher level idea is just a, a nice abstraction where the model can say like, "I'm training a, a fairly big model.

I need four H100s and this many CPUs," and just kind of write the config and submit the job and not have to worry about like, doing hardware orchestration.

Uh, yeah. And to go into the, the actual phases. So again, the first phase is this, this research phase. And the idea here is kind of like almost like a super CLAUDE.md file or a super /init where we just want the system to go off and kind of build enough context such that it can start meaningfully,

uh, you know, forming hypotheses and testing them. Um, and we built, you know, AlphaLab is kind of this server-side running thing, but we built this lightweight UI on top.

And so sort of how we've done this is build this, this scaffolding of the to-do list. So it's first, you know, prompted to, to build the to-do list such that if it completed every item, it'd be able to start experimenting.

And this allows us to kind of keep re-prompting should it try to exit early. And so you can see, you know, it's talking about setting up its Python environment, um, doing different data loading, doing different kind of statistical testing.

And each item of the list it's instructed to build a, like take notes in a markdown file. And this also allows future agents to smartly query that and kind of manage their context dynamically.

A-and this is really where web search is used most because it will go off and read arXiv and, and get kind of good context from the public domain as well.

And so this can vary a lot, but, um, it takes, you know, roughly around three to four hours.

The second phase and what, um, is most different in 2.0 is the eval building. But just to say sort of our first implementation, you know, of course, the evaluation is the most important piece, and LLMs aren't malicious, but they can make, you know, very silly mistakes.

And if you're optimizing against a ba- a bad eval, the whole thing kind of falls apart. So our attempt to be more robust is have this sort of multi-agent framework.

So one is tasked with first building the eval, like actually writing all the code. And then that goes off to two critic agents, one that's told to be more high level, like are there conceptual errors in our evaluation or any kind of forward leakage of information, and then one that's more programmatic.

So it's like writing unit tests and integration tests. Um, and they write up any issues they find. If there are issues, it goes back to the builder to fix, and this loop doesn't end until sort of all of them are happy that the eval is good.

And then the third phase, and really the heart of everything, is this mass experimentation. And so we've, we've chosen, you know, both in the code and in our UI, this is kind of formulated as a Jira board or a Kanban board.

And so there's this sort of strategist agent that gets to look and query all the context from the previous steps. And it's just supposed to keep coming up with experiments it wants to try, and it submits them to this like to implement column.

And then as new cards come in, those get pawned off to worker agents that are tasked with actually writing the code to implement the strategy, writing the Slurm config, you know, what hardware does it need, submitting it to our cluster, waiting for the job to finish, and then look at, you know, the, the machine learn- learning training

curves, like did it underfit, overfit, and then also looking at the eval results. And then it sort of writes this postmortem analysis, which goes back to the strategist as each job finishes.

So the strategist hopefully can do this kind of self-evolution. So it can see like I suggested, you know, three variants of transformers that actually didn't work too well, but, uh, XGBoost is, is working really well, so I wanna explore more tree methods or something like that.

Um, and also in this step is where we as users can steer. So you can, you know, s- another reason we picked sort of this Jira formation is- Uh, you can cancel cards, you can add your own cards.

There's also a chat feature that's sort of cut off here, but you can chat with a strategist and kind of steer it towards more creative or kind of give it intuition of different methods it should try.

Um, and then we keep this, you know, ever-growing leaderboard where you can see, like, given your eval and given a held-out private validation set, like what are the best performing models?

And you can click in and see like, you know, from inception of the idea to the code, and you can pull it out and play with it.

And then this is just sort of our UI 2.0, which is really just optimized to look cool. But you can see like, you know, it's suggesting experiments, and this is really sped up, but how each worker kinda pulls it through, um, you know, building, deploying, and then analyzing the results.

And, um, you know, in our paper, we did more sort of academic datasets. So we looked at CUDA kernels, we looked at, uh, an academic traffic time series dataset, and we did the kinda classic, like, Karpathy-style LLM speed running.

Um, and it's sort of hard to benchmark AlphaLab, but we compare it to more of a Karpathy style, like single agent in a loop going, and it did find a better, uh, training config for training an LLM.

We also put this on a Kaggle competition, which was to-- for-- it was, uh, hosted by NVIDIA to fine-tune their Nemotron model to be a reasoning model. Uh, and it got in the top twelve percent of submissions, which, yeah, I think is decent, and also it only had sort of ten iterations to work with because we joined

late, and I think, you know, AlphaLab works best the more iterations it can explore. So presumably or hopefully it would've done better had it, uh, had more time. And then I can say at a high level internally, there's been a handful of, of models, all sort of the flavor where we had a decent model already, but we

just turn it over to AlphaLab to keep kind of churning on it, uh, where it's found meaningful improvements that are now working their way through risk and going into production.

And so with the-- my last couple minutes, I, I wanna talk about, um... You know, we, we ran into some real issues and hard questions. Uh, I think the first was, you know, okay, so we had some, some good results, but we've also had cases where it's really failed.

And so it's kind of always in our head like, how real is, is any of this? You know, if it, if it's failing on these hardest problems, how do we measure how, you know, how real this is?

And the second was, and I'm sure a lot of you might be thinking like, okay, a research phase sounds reasonable. Having a strategist and worker sounds reasonable. But isn't it sort of arbitrary?

You know, like, how do you motivate these design choices? And how we feel now is like, and I think a big theme of this conference is, you know, should we be making these dec-decisions at all?

Like this itself is a verifiable loop. Like an LLM should be doing this, this meta optimization itself. And then lastly, you know, on this, this 1.0 formulation, it's sort of like we give the data, we give the goal, and the LLM just goes off and does it.

So like how does that exactly encode our, you know, Morgan Stanley's enterprise knowledge, but just our expertise as, as quants, like sort of missing from the picture. And so the answer to all three we feel is really in building our own evals and environments.

And so to just sort of go one by one through the questions, you know, to the first point, and this is a lesson I learned over and over, like monthly working with these models, you have to start with good eval.

Like it's such an obvious thing. I think we were kind of overeager and wanted to treat it more like a, a human researcher, but you of course need like a very clear way to measure.

And so the, the biggest kind of change is now we're, we're very opinionated about the eval. It's very much like Kaggle. And so, you know, we treat it as data and description in.

The harness lives in the middle, and its only job is to submit containerized models, and it gets sort of the, the feedback of like a public leaderboard score. But you as a user get to see a private leaderboard, like held-out validation, how is the model performing.

And so, you know, in this case you can measure like just for any given task, how well does your model do? But of course, once you have this strict kind of format, you can think, okay, you know, to me, evals and environments are the same thing.

It's just you train in environments. So now what we've done is built on the order of like ten to twenty really careful environments, and that becomes a reinforcement learning signal.

And so we're, you know, quote-unquote, "AlphaLab-ing AlphaLab." So once you have that way to measure, you know you can do human tuning of the, the harness. So like maybe there should be two strategists and maybe they should debate or maybe they're, you know, whatever kind of ideas you have, you at least have a way to measure and

kinda manually hill climb. But what we're doing now is really this meta harness optimization, where the LLM is looking at the traces, looking at the val-- you know, the results, and improving the harness itself.

And also sort of a, a tangential axis is we're now collecting good traces from open source model and really touching weights and doing like GRPO or, or other, you know, on-policy distillation methods.

And so we see like the, the best performing thing might be an orchestration of open source and closed source models, but we're kind of optimizing the whole thing together.

And to the last point, you know, how do we as, as experts encode our expertise? We again think it's through environments. Like building environments or at least good environments is really, really hard work.

You, you know, it's-- You have to be-- There's of course like the data that goes in that's proprietary, but, you know, designing the, the verifiable metrics is maybe the easy part.

But then we're also doing these qualitative rubrics where we kind of look at the traces and say, you know, "What makes a good researcher? What's the thought process?" And we can grade each rollout on, you know, how well it's following our research process.

And so having these good rubrics that become the signal for the model to learn, we feel is really how we're, we're building our own expertise into the system. And so just to kind of conclude the, the 2.0 version is really having this strict environment and eval setup and, you know, whatever lives in the middle, we almost in

the limit kind of don't care about. We can initialize it to AlphaLab 1.0, but this-- it should really be this self-improving system. Um, and just to leave kind of the, the bigger picture headline result and my feeling is, you know, this ability to do general auto research I think will kind of become a commodity.

Like I think we're already seeing it with GLM 5.2, and so I really think all of your value as like an enterprise or human expert comes from building environments.

And so like, you know, temporarily for us that we're still doing like manual tuning against the environment, but I think in the limit, the, the auto research can research itself and just be this self-improving, um, process.

And so, um, my site's on there and then also the, the project page, again, the 1.0 version, we released everything and our plan is to keep just releasing because again, we think the environments encodes all of the, the value.

Uh, so thank you. [clapping] [upbeat music]
