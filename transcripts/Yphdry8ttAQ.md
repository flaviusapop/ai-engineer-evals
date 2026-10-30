# Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI

Source: https://www.youtube.com/watch?v=Yphdry8ttAQ

Uploaded: 2026-08-19

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/97/971a7d4ad1de6d28975cdbfc86cee5b650e6f3aee2c827c7726c05d859934929.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/Yphdry8ttAQ.json.

## Transcript

[upbeat music] Hello everyone. [clapping]

So my name is Ayush Bhardwaj, and I did applied AI for a hedge fund, and now I do everything tech plus applied AI for a pharma tech startup, 'cause you know the way startups are.

You have to do everything. We have multiple hats. So before I start the session, I would like to do a small survey. Can I get a raise of hands for all the engineers in the room?

Oh, okay. That's a tough room. Now can I get a raise of hands for managers?

Okay, just to be clear, managing AI agent does not count. [laughing] You have to manage people. Oh, okay, we have a few managers as well. Interesting. So it'll help me like fine-tune my talk a bit.

So today my aim is to take you through the journey of how do you actually build and iterate in applied vertical AI, and my experience is from the hedge fund and the pharma tech company.

So before delving deep into the recipe, I'll just like take you through what do I even mean by applied vertical AI 'cause I don't know, it, it sounds like a very weird term.

It's like the vertical word is kind of forced. Uh, I won't lie, it is. I coined this term probably. So applied AI is like built for-- So vert-- Applied vertical AI essentially applied AI, but built for one very specific industry.

Its, its aim is to simulate a job of a person in that particular industry, in a sense. So an example of applied AI is Google Translate, which is like general purpose, helps you translate.

It could be used in education tech, and it can have like tons and various sorts of uses. Whereas Allos, which is my employer, the pharma tech company, we specifically build drugs with AI, so that's a very specific use case.

Another examples of applied vertical AI field could be the legal tech firms that are now coming up with. You must-- I'm sure you must have heard about them. So those are like, uh, another good examples of applied vertical AI.

So when I left the hedge fund, right, so I was expecting that the world will change for me 'cause, you know, hedge funds are like really fast and really pressure sensitive, whereas pharma is like, "Okay, we're gonna take fifteen years, but we're gonna do it right."

Hedge fund was all about like, you need to do it fast and mostly right. It does not matter if we lose at one paradigm as long as we are overall winning.

Whereas a pharma firm is like, "We have to be absolutely right. You can take a week more." And it was true. It's, it's a completely different world. But to your surprise, and to mine as well, nothing changed actually.

My job increased, but the core part of my job, applied AI, remained the exact same, and I cannot, uh, express how surprised I was 'cause I thought that it'll be a complete different thing, but apparently it was not.

So, uh, so then I spoke to other people as well across legal AI and the people coming up with the proptech firms, which essentially the real estate tech firms.

And I realized that everyone is kind of building the applied vertical AI in a very similar way. I could see some steps that could be essentially abstracted out, and that's what we'll do today.

So, uh, before, again, delving de-di-uh, deep into that, I received a few reach outs saying, "Are people actually putting agent into production?" And I was like, "This is such a wrong question to ask."

Everyone is putting agent into production, even like fifteen year co-- uh, [REDACTED:age] kids these days. The question to ask is whether they actually work, whether they actually make or save money, whether they justify their ROI, whether, uh, they are making way more than the amount we are investing into it, like end to end.

And I can say from my anecdotal experience, yes, at the both places I worked, the agent either saved the money or made more money. So with that, let's get started.

So the recipe, I'll take you through a series of seven steps roughly, and try to like make this process as simple as possible. So the first step is formulate the problem.

So this is sounds like very trivial, but a lot of people, specifically startups, get this wrong. They just try to do too much at once. Whereas from what I have learned and what I think a lot of colleagues would agree, you need to pick a very narrow task.

You just cannot ask it to do everything. A good example for this could be, let's say if you build something in finance, you won't ask it to like, "Hey, can you fetch me top three market opportunities that I could invest in?"

No, that won't work. You have to be like very specific. Like you pick a market, you say, "Let's take the US equities," then you pick a industry, let's take IT, and then you ask it to like rank stocks based on some parameters like capital expenditure or let's say the AI, um, uh, investments.

So you pick like very specific things, and then you, uh, sort of formulate a very narrow job for the AI agent to do. And you can build like n number of AI agent.

Last I checked, there was no tax on building more AI agents, so why do you want your single agent to do everything? So this is important, and this in the same, uh, in the pharma context, it's the exact same.

We just break down the process into steps and then ask really pointed questions with the agent. We model our agent for a task. So once we have our pom-- problem right out of the way, we know what we're trying to solve.

The next step is identify the data, and I cannot stress this enough. This is a really, really, really important step 'cause everyone has news data. Everyone has like sell-side reports from JPMorgan, Morgan Stanley.

Uh, everyone has the arXiv preprint server or PubChem or your research papers, right? But what actually makes your application better than, let's say, ChatGPT or Claude? It is your proprietary data.

So the thing with proprietary data is it's really expensive to buy, and most people won't sell it to you, so you need to curate it by yourself. Imagine your organization has been working for three years, right?

They already have a lot of data. It's just unstructured. And in the age of LLMs, I think this is a very fairly easy task to make unstructured data into structured data.

Like a LLM workflow could do it overnight. So to give you a great example of the-

proprietary data that finance industry has, it's the trade thesises, which is like what trade work and why it worked. And in pharma, it is the data for failed experiments.

'Cause successful experiments data, yes, you can get it, but failed experiments, that's relatively hard to get. So now we have the problem, we have the data. What's the third step?

That is to model the problem, like write the prompt. So while writing prompt, you-- like, what we should aim is to model it after the person who you are trying to replace.

I mean, that's the hypothesis, but yeah, no offense, we are not trying to replace anyone with AI. But that's the ideology behind writing prompts, encode how a person would solve this job into multiple steps.

So it's just like a, like a mental model. So this is again, fairly simple. Next thing, observability. I'm sure you have been to this conference at three years, and this word, I think, I don't know, you'll be hea- hearing about like a thousandth time.

There are tons of observability provider. If you can see it, you can fix it, so you need observability to see the traces, understand what your, uh, AI application is doing, and debug it.

So sorry, but all of this was the easy part, to be honest. All of this fits one screen. The mythical 10X engineers can do this stuff in minutes. Like literally, this is the code you precisely need to build an AI agent, so that's why it's not the moat.

Uh, of course, except your proprietary data. So what do you do now? What do you do after doing the first four steps,

which is observability and prompt and, like, uh, getting the data right and everything? You iterate. Now, the thing with iteration is, like, when I joined the hedge fund, I thought how hard it can be.

I mean, everyone can iterate. I mean, we have been iterating our whole life for each of the task. But to be honest, I could build it, but I just could not tell if it worked, 'cause

I'm not a trader. I'm not someone who has a PhD in biology or chemistry. I just don't understand what the model is saying, what is the output of my AI agent is.

And since most of you are engineers, you would relate. You can instantly tell that Sonnet 5 sucks because you have your own training. You understand, okay, this code is not great code.

Whereas some X model that's a fail five, you see, okay, this is great, but not as great as the hype is. 'Cause you have been trained for this for life.

You have a mental model to judge these things, but you just do not have the same kind of mental model when it comes to, like, predicting trade thesises or doing, like, really specific tasks that vertical AI industry does.

And this is also the place where, like, a lot of vertical AI projects quietly die because on the surface it looks like you have made it, you have built it, let's put this into production and start selling it.

But no one would buy it, the same way you won't use an inferior coding model. So as an engineer, when I ran into this, I just couldn't accept, honestly.

I thought, "No, there's certainly more that I can do. We don't need other people." So I thought I could, uh, LLM as a judge my way out of it. [laughs]

And this was a really, really stupid mistake, to be honest, 'cause what LLM is essentially doing, it's, it's predicting the next probable word. So if you see, it's just like jargoning its way out.

It does not understand what alpha means. It does not understand how to actually create value unless you have, like, taught it some way. And whereas a human can just tell it instantly what's bullshit and what's not.

So I'll just try to delve a bit more deeper on why you can't just iterate. So first thing is that model cannot verify itself, specifically in these fields, because reinforcement learning via verifiable rewards is really good at math and code because you have, like, answer keys, you can verify your code is, uh, compiling or not, and there

is tons of step. You can just model, uh, the complete thing around this. But when in these fields, there is just no way to model it. And, and let's say if any error gets in, it's just compounds with every stuff, and that's what LeCun seems to think as well.

And now the more important part that we touched upon previously, the data. So the interesting thing with pharma and finance is the data was never there, and I'll explain to you why.

So any institutional manager holding over hundred million dollars in qualifying US equities are forced to publicly file their holdings, long position holdings, every quarter. And once a hedge fund does this, this is the percentage decrease in their returns because everyone just sees those reverse engineers and takes away their moat.

And when it comes to pharma, right? So this is the number of, uh... So by law, you are, like, required to di- disclose every clinical trial, pass or fail, you have done.

But thirty percent of the firms, which is like nearly one-third of firms, never do. And in like 2026, FDA had to, like, publicly remind over, I don't know, but two thousand sponsors that they are, I mean, doing injustice by not, uh, releasing unfavorable results.

Because this is the exact data which helps the model think, which helps your LLM actually reason through these complex and niche industries. And they hide it because for them it's like a chicken laying golden eggs.

Why would they sell their chicken? So naturally, neither OpenAI nor Anthropic has that, has this data because it's like gate-kept. You just cannot hire a trader for hundred dollars an hour and have them annotate that stuff because there are, like, lots of NDAs, and they definitely earn more.

So okay, now I have told you about tens of problems right? Now, you will naturally think, "Okay, yeah, right. Then what do we do? How do we build a startup in like a vertical spa- space?"

So- Very self-explanatory. You hire the person who you want to sell it to, 'cause there is, to be honest, no other way around. I have tried a lot of stuff.

You just need to hire the user. In finance, in a hedge fund, this was very easy because the user was kind of like my boss, the trader. We worked together.

But in the pharma tech startup, it was very weird. We are, like, a bunch of young engineers, and we are like, "Oh, we need a [REDACTED:age] scientist in our company to tell us what to do?

Yeah, I guess we do." And then we hired someone, right? And that someone actually changed the trajectory of our tools. Our tools started making sense when we pitched to the other pharma companies, the big ones, the big pharma.

They started liking our tools because it kind of spoke their language versus the normal jargonese LLM language. So once you have hired the user, let's say, then what would you make that user do?

You try to build a learning loop out of it. The domain expert can start at the, like, a very, very low level, the ground level, where they just think about prompts.

Okay, uh, uh, I mean, let's not ask, uh, LLM to do this. Let's ask a very specific query again. They'll help you curate data. Just like engineers know which conference are bullshit, which are not, which, uh, research paper sites are great, which are not, which are, like, top leaders in engineering, which is-- which are just, like, influencers.

Similarly, a pharma expert or, let's say, a trader knows which sources are more reliable than the other. So they help you curate their data, they help you, like, refine your prompts better, and they try to create, like, thinking models of how they would think about a problem.

'Cause, I mean, let's say if you s- if you, uh, follow five steps to solve a problem, right? You just cannot do it in, in any random order. There has to be a logical flow.

There has to be a natural flow. That-- so that's what they, uh, try to curate, like decompose a problem, gradually refine, and then finally judge. So the person who sort of has lived through the complete of the industry that they're trying to revolutionize, their judgment is now, like, turning into agents.

So that's what's happening behind the loop. So, uh, to do this, there are, like, again, multiple ways. I mean, each of these could have been a hour-long session on its own, and I wish I could take, but these are, like, few ways that I identified.

Uh, I'll just, like, take, uh, you through them, like, really quickly in the interest of time. So supervised fine-tuning, I think most of you would know where, like, model mimics human de-demonstrations.

Uh, reinforcement learning from human feedback is, like, a kind of a, a very efficient way where human preferences train a reward model. Then rubrics as a reward is, I, I like to call it reinforcement learning from AI feedback.

This is because that you can-- human can just create a rubric, and then AI will just, like, grade itself based on that rubric and that improve its own processes.

But again, there is a slight chance that you might run into an echo chamber with rubrics as rewards. And the cheapest of all, and I think the highest ROI, is the error analysis.

Whereas the observability part that you set up earlier, you just analyze the logs plain and simple. You understand where model is going wrong, and then you just try to correct it.

So this is where you have, like-- don't have to touch any weights and the most highest ROI way to get the impact from, like, start on. And once you understand, like, uh, what more you could do or if error analysis is solving or not, you can just gradually climb up the ladder and probably, uh, later on go

to the ultimate reinforcement learning from human feedback. 'Cause that's, I think, in our industry, kind of the golden standard these days, that you need to do RLHF to actually get some edge.

But, uh, certainly there are some pitfalls of it. Like for example, now there's GLM five point two, right? You fine-tuned it, right?

Uh, Alibaba Cloud or let's say DeepSeek will release a newer model, then you have to fine-tune that too as well. So there is a cost. It's not cheap. So once you have done all this, you just create a loop, and you just, like, go onto that loop.

You hired one user, you hire more users. They ask more queries, the scope increases, the data increases. At this point, you are kind of generating your own data. The exercise you have been doing in loop, right?

That exercise itself is generating a very, I would say, a crazy data set of what works and what does not work, and this loop never stops. Once you feel confident enough in your application, you just ship it, provide it to the external paying users, and then you see the magic of it, that it actually works.

So I just pulled this stat from Stanford AI Index report 'cause it's a really nice report that gives you an idea of what the state of AI is, and this says like eighty percent, eighty-nine percent of enterprise AI agents never reach production.

Again, I disagree. Every AI reaches production, but it just fails to work or, like, justify its own cost. So that's the real thing. You can just build and ship AI agents whenever you want, but you need to justify ROI.

And finance and pharma are two such industries where if it does not make money, it's shown the door. Simple. They won't, like, wait and say, "Okay, maybe it'll work in two years.

Maybe the cost will be lower in by the third year." No, it has to instantly make money. It has to, like, hit the ground running, and if it does not, shown the door instantly.

So just to summarize the seven steps that I feel are, like, good enough to give you an abstraction of how the vertical AI industry moves. You formulate the problem statement, you source your data sources, you prompt it well, you refine those prompts, you observe how your tool is performing.

You don't iterate yet. You hire the user, and this user or users now play with the tool as much as possible. They, like, kind of form a learning loop, an endless learning loop that goes on.

And at a point when you feel, yeah, it's, it's really delivering that alpha over, let's say, Claude and ChatGPT, you just ship it. You start earning money. So-

One more interesting thing. So HITL is like kind of a thing. Everyone is like, "Yeah, let's add human in the loop." I would say not yet. Finance and pharma are still those two industries where it's AITL, AI in the loop, 'cause everything is, like, done by the expert, but the AI assistant really helps save time.

Like for example, uh, it may take an X amount for a trader to form different trade thesises, and AI can just give him five candidate trade thesises. But which one would actually work in the market and which won't is the decision, uh, the decision still lies with the trader.

And same for pharma. When you're, like, picking drug candidates, which one to pick, the expert still does it, but you just, like, reduce the time of expert by a lot, lot.

So, and, and it will stay this way for really long. So, uh, for the models to actually make good decisions, they don't need to do correlation, they need to do causation.

And as Ya- as Yann LeCun puts it, these are like text statistics, not real world models. You cannot just pattern match with past and use it to predict the future.

And so we are, like, kind of not there yet. That's what I call as the AGI line. Once we are there, yeah, probably then models will just, like, make drugs.

You will have vibe coded drugs. Someone would be vibe coding market. But yeah, not yet. So a final takeaway that I would call if, if, if there's one thing you are taking away from this talk, this is it.

Model infra ecosystem, everyone selling you tons of stuff at this conference is just commodity. Everyone has it. If you have it, everyone has it. Everyone can pay X number of dollars for a subscription, but what is moat?

And no one will come and sell it to you. You will have to curate it on your own. It's the domain expertise. You need your data, you need other people's data that is just not out there on the internet, and that, that's what will form your moat.

So thank you for your time. I think you enjoyed the talk. And yeah, let me know if you have any questions. We can meet outside. Thank you. [audience applauding] [outro jingle]
