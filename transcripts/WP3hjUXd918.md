# Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI

Source: https://www.youtube.com/watch?v=WP3hjUXd918

Uploaded: 2026-08-17

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/32/32c33e0c996870063b17c98e42962f1952b19a8736630a627f8c9e49bf9b9d21.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/WP3hjUXd918.json.

## Transcript

[upbeat music] All right. Good afternoon, everyone.

Thank you for, uh, joining and not watching the game. Uh, I hope it will be a bit more interesting or at least you will learn something compared to, to, uh,

hopefully Germany winning or some, uh... Anyways. Yeah.

All right, is this fine? Okay. [chuckles] All right, so I'm here to talk about... We are here to talk about context engineering in 2026. And more specifically, we are here because we've all lived that, that situation where you try to do things with an agent and ultimately it does just exactly the thing that you don't want it to

do, and it... In my case, it usually ends up like this, where I'm super mad and I just type back hoping it, it learns.

And, uh, usually the problem here is not that the, the model just got dumber and you need to switch to Claude or to Codex or, or whatever the, the harness that you're using, but it's more that the, the context is, is filling up and it's getting worse and worse.

The results are getting worse because of it.

In our case, this is important because we build courses and trainings for AI engineers specifically, and one of the features that we provide is an AI tutor to help answer questions based on our lessons.

And if the interaction is just like the one before and they are super mad at us, they might just ask for a refund, and it could end up like this.

So that's, uh, not what we want. And so what we did for this workshop and just for the AI tutor in general is to run many different experiments in order to figure out how, in our case, we can fix context rot or at least improve the AI tutor as much as possible and reduce the cost as well

of, uh, running the tutor. Uh, the QR code here is a link to a Hugging Face space where you have all these experiments that you can see, and also the AI tutor is open source.

We will share another code for the repo, but it's also linked on the Hugging Face. So everything is open source. You can access everything, uh, and even see the experiments online and use the AI tutor online as well.

In the next 80 minutes, we will... I will start talking about compaction, memory retrieval, and, um, everything that you can do in 2026 that usually works. And then my colleagues will jump in with, uh, our...

the architecture of our AI tutor, our decisions, what we built, and the evaluations that we built, the har- how we built them and what we decided to evaluate, and then, uh, the results and what we took out of this.

So of, of course, it's applied to our use case and our AI tutor, but hopefully you can, uh, get away some interesting insights at least from, from this and some best practices that we learned throughout.

More specifically, we is a Towards AI. Um, I founded the company with my partners in, in, uh, a few years ago, and we've always been focu-uh, focused around education.

Obviously, back in the day it was more about computer vision and, and more basic machine learning. Now it's, uh, towards AI engineering and agents, anything that works for the industry.

And I'm joined by my colleagues helping me develop this AI tutor and our courses, Omar and Samridhi, that will, uh, jump in later on. And here, more specifically, Towards AI is quite large, but what one, one of the things that we do is our academy, so the Towards AI Academy, where we build courses, technical courses for AI

engineers to upskill towards AI engineering. And as I said, we provide an AI tutor for the students.

So the, the AI tutor specifically, uh, will, will be like our baseline for all our experiments. We will use that to test all the different features based on real user interactions.

And to have the best results possible, we had five requirements we wanted to ensure that the chatbot follows. The first one, obviously, we want the answers of the chatbot to be grounded in our content, not just its own knowledge.

We need the, the tutor to be based in the current students and current lesson to not be a-- because we have multiple courses, so we just need to ensure that it answers from this course content.

Then it needs to hold long help sessions in case the student is debugging or, or, or just iterating a lot with the, the tutor. And, uh, obviously handle code because it's for AI engineers, so we just code a lot.

And it needs to have somewhat of a low latency to not be frustrating to use. And all of this is related to context engineering, and here we'll be talking about, uh, what is context engineering in 2026 or at least what we figured out from, from this, from these experiments.

And since everything here is in the context, uh, in the con- in the context of models, it creates two problems. First, the context window is finite. Uh, everything the model will see from instructions to, to lessons to code will lie in the same space that is limited, and the more you pile things in this space, the worse

the results will be and the more expensive it will be because you pay for more tokens. So that's one of the, the, the main problem we're trying to fix.

And the second problem is that the model is stateless. So when a student reopens the AI tutor, uh, typically if you don't build anything around it, the model will have no idea what's going on.

It's just starting from zero. So this creates two things we have to work on, the context management, which means within one session, and the memory aspect of these models, uh, which means across sessions.

And these- Experiments, and in this workshop we focus on the first part, the context management because you cannot have multiple sessions is if one session is, is shitty. So we try to really optimize for this, and maybe in a future workshop we will do one about memory, hopefully.

So for context management, what does the, the tutor sees? In our case, it sees, uh, many things from the system prompt to being, uh, for being a tutor and the context of our courses and stuff, to tool definitions, uh, so which tools it can use, how to use them, when to use them.

The chat history if it's an ongoing discussion, any old tool outputs that was called, course chunks that we retrieved to answer the students and finally, the user questions. So it's just not the user question that we send, obviously, and typically it's the smallest part, but it can also have...

contain a lot of code to debug and to help, uh, or, or error logs, so it can be large as well. And all of this together just ends up costing more and more to us.

So w- we really want to optimize this, this context management aspect. And what we've seen just quickly is that the, the main bottleneck or the main problem scaling the context is the old tool outputs which contains like any old chunks retrieved, all the tool calls and tool results pairs, uh, from, from all the tools called over the,

the many sessions that it could have-- the, the many turns that, uh, that one session could have have. And any, uh, file or searches that it did to, uh, in its own memory.

And the main problem is not, i- it's not that it's more costly, it's also that the quality degrades as we know with a problem called context rot because of the way how large language models are trained to handle longer context with, uh, we just inject facts into large corpus which doesn't tell them to manage the whole, the

whole context together or understand the global context. And,

uh, so, so one of the reason is to help with quality. We want to reduce the context as much as possible. And the others are that, uh, if you re-query the model in a, in a discussion, you resend every previous tokens, so you pay for them as well again, which is far from ideal.

And you increase the, the latency, so the time to first token or TTFT, uh, which makes-- which creates a very bad user experience.

So you may want to, in our case, manage our context for speed and for, uh, spending, not just because the quality drops as we will see in, in our experiments and, and in the results in the near future.

So how we do that to manage, uh, spending and, and speed? How do we manage our context? We use compaction, and the idea is just very simple. Uh, the idea of compaction is very simple.

It's just to try to have the smallest context possible that contains the information to be able to answer the question. And you drop or save the rest somewhere.

And to do compaction, even a, a good compaction, you don't necessarily have to have large language models. You can start quite cheap with trivial tools. Like, uh, if you have-- if you use tools in your system, um, like a web search or just executing code, you can automatically truncate outliers.

So if you have like one s- tool that, that produced three hundred lines instead of ten usually, you can just truncate almost everything except the, the head and tail, the, the beginning and the end, and just wr- write that it's truncated so that the model in the future can recall the tool if it's, if it feels it

lacks context. You can use the, the simplest approach that works the best, uh, to just use a sliding window or just trim. Basically use the last N number of, of turns that the user sent, which, uh, you need to determine bas- based on your, your own system and your users.

And you can clear, uh, for, for some specific tools depending on those that you implement, you can just always clear most of the outputs.

So that's for when... That's not even using language models. And then you can use language models to basically spend tokens to save even more tokens. And in this case you don't even have to h- to use large language models.

You can even use smaller ones or even lo- super small local ones that, that runs in like one MacBook. To do a, a few techniques, there are many techniques that exist for, for compacting.

Th- Those that had the most impact in our experiments were selective retention, where the language models will just decide based on where the discussion go- is going, what to keep, what to discard.

Then the simplest one here is summarization. So just summarize, continuously summarize the, some previous turns depending on your, uh, on, on your own application. And in the end you can do, uh, here what Claude Code does.

So when it reaches the limit, you just su- pro- produce a summary of everything and reset completely with that summary. And there are many more techniques. Uh, I highlighted here those that, that work the best.

We will discuss them later on in this workshop and the actual results and experiment setup. But those are the most successful techniques. And I want to highlight also, uh, delta summarization that Claude Code uses, uh, that is very useful when you spawn sub-agents, when you use sub-agents.

It just means to keep a summary and updating the summary based on the new summary that you produce over time. And then the, the sub-agent will just give that to the main agent.

But in our case, we don't use sub-agents because, uh, the tutor works really well with just one main, so we don't need to add complexity for that.

And lastly, after spending token to, to save more tokens, you can also offload things. Right now it's o- obviously memory and skills are super popular, so you can of course offload to your memory.

So just saving text in your documentations. And you can use what's been there for years now, uh, retrieval augmented generation, which is very powerful. And as a si-side note, we also compared with GraphRAG.

So everything... Even if I not-- I don't mention them, we compare them, and I highlight just the, the best results here. So we, we compared GraphRAG with, with RAG here, and it-- in our case, it just ended up being way costlier to set up and just tie on the results because, uh, it basically was a hundred percent

based on our real user evaluations. So we don't need to use GraphRAG, but it's-- it depends on your own case. If you have a very large dataset with inter, uh, with relations and interconnected topics and things, uh, it might be worth implementing.

So you definitely want to still test it.

And, uh, speaking of memory and of offloading to files, this is, uh, as I said, basically just saving them locally or, or in a server for, for you to use, which means it's fully reversible because you don't lose anything.

You don't lose any ongoing discussion. You just save them ready to be referred to in the future if the same student comes back and asks related questions. And it's basically the, the Karpathy's idea of the LLM wiki, uh, which if you link with some sort of, uh, chunks, so a version of RAG, it's pretty powerful, and it

makes your system become quite, uh, cheap and durable, and it's easy to inspect from both humans and agents. So it's really interesting. More specifically, it looks like this in our case.

So we have just chunks. We save everything into chunks, and we cross-link the chunks with pointers. And then these chunks are linked to raw data files from where they come from.

Then we have one index that will just map all these chunks, so just a link to all the chunks and some context of what it is about. And the agent will just see this index.

So it sees... It's like, I think it was four hundred and fifty tokens, so it's very small. And it just sees that index.

And then, uh, based on the user question, if it seems to be related to some user-specific question that it may exist in the memory, it will scan the index, it will go back to the chunk.

If it's enough, it will answer based on the chunk, the chunk retrieved. If it's not enough, it can even go back to the raw data to have even more information.

So basically, it's just the best way to pull context accordingly to the task complexity. So if the task i-is complex, it will pull more, and if it's simple, you'll pu-pull less.

And a parenthesis on this, uh, what we've seen working with our clients and just building this in general is that right now everyone is, is converging towards having more and smaller skills.

So you have... I-it's, it's way better to build small, very precise skills that refer to each other's skills to, uh, to save on context and just load skills one by one and even be able to spawn a sub-agent with one dedicated skill context instead of just basically to save context.

It's, uh, well, the idea of progressive disclosure, so you just load what you need right now.

Okay. Just to go back now on, on compaction, this is what the, the talk is about because memory, uh, we have made some experiments, but it couldn't really fit here.

It was a bit too much. And, uh, when talking about compaction, there's an important problem or solution that, uh, that appeared recently. Uh, well, not recently, but was way more popularized, is the, uh, the, the main problem is that first-- The main problem is that you-- when you ask a follow-up question, you need to recompute all previous

tokens every time. So you just end up paying twice for the same tokens, or three times or four times if the conversation is going, which is obviously far from ideal.

So what providers do nowadays is to offer prompt caching. So you will--

It-- They will save the embedding and, and KV cache, and I won't enter into the details, but they will precompute. They will have saved a lot of the, the compute for some tokens, and you can just reload them.

And what's interesting for us is that these already sent token that you reuse are much, much, much cheaper. Uh, specifically, it can go up to fifty times cheaper with some API like DeepSeek, uh, which we will discuss in the experiments.

And what that means is that if you send a very long context, uh, you will pay just one-fifth-- one-fiftieth of the, the price per token and just pay the full price of the que-- the new user question or the, or the new interaction.

And that's a problem for compaction because when you are compacting, summarizing, doing any transformation to this context, the, the provider cannot use the cache because it, it's a new context.

It doesn't-- The model is not intelligent enough to understand it's the same topic change. It, it just cannot use the cache. So you, you will pay full price for these new transformed tokens.

So here what it means is that you need to, to compress to... For, for compaction to be worthwhile, you need to compress by more than fifty times the context.

So it can be quite, uh, difficult in some cases w-without losing quality. So caching is truly a game changer, especially because nowadays, uh, almost all APIs offer it, very easy to use, and typically they, they save cost on like, uh, on ninety percent of the cost wh-when you use caching.

But in some case, as I said, it can go up to way more than that. And not only that it helps with cost, but caching-- cached tokens are also already computed, so it's way faster to get the first-- the, the answer back.

So ultimately, it means that summarization is potentially a trap. You may not want to use it at all, or you, you may want to just use it very specifically.

Which is what the most, uh, serious harnesses do nowadays. Claude Code, Codex, and all of them use context caching, but also use a different method of compactions. And we know that because obviously of the leak, and then because Codex is open source.

And then the APIs also provide ways to c- manage context directly and, uh, caching directly. So it's... It becomes, uh, s- when you build yourself a harness, like we do with the AI tutor, it becomes really interesting to understand when to use which technique and test them obviously.

So where is this going? Uh, it mean, it, it means that you don't, you don't want to just compact. You don't want to summarize everything anytime because it may kill the cache, and you won't be able to use it.

So mo- some, uh, best, uh, guidance that we found is that obvi- obviously, when the user seems to talk about a very different topic, you may want to refresh the session to clean it,

to clear it. Um, when you scope for files, use h- what I described with, um, progressive disclosure to just show the smallest amount of context possible.

You want to clear every old tool outputs that are not useful anymore. You may want to compact in some case. We will see that in the experiments in a, a few minutes.

And, uh, you may want to optimize for cache hits, so just having the model use... be able to use its cache. And regarding that, uh, providers are constantly improving their feature set to manage cache, so you just need to, uh, stay current and follow what, what the API allows nowadays.

But they all provide different methods. And, um, you will have access to the slides, but there's... Uh, I put a link earlier in the sl- in the first few slides on a very interesting article regarding, regarding prompt caching that I recommend checking out.

It's, like, on the sixth or seventh slide. But, uh, you will have a- the link to the slides.

And lastly, you may want to use a model router to optimize especially cost on various tasks.

And most importantly, and what the majority of people don't do, you want to log everything. It's super easy. You just ask Claude to implement Opik and track everything. It's, uh...

You don't have anything to do. So, uh, it's definitely worthwhile to, to implement, and you can track cache hit rate. You can track user frustration, which we've seen that Claude does.

So, uh, I keep, uh, telling it when I'm not happy. And, uh, you w- you may want to log for some, um, abnormally long outputs or any weird behavior that a small language model could detect.

And so all of this together is the, is context engineering, which basically means to decide what the model sees every time you call it. And to us, for the AI tutor, it means to decide what to keep in the current context window in order to optimize the caching, what to drop or compact, and when to do that.

Uh, and those two first things are exactly what, what we studied in many experiments that we, that, uh, my colleague Omar will share with you right now. And, uh, so you can follow along with the experiments on the, the QR code link.

It's the Hugging Face space that I d- mentioned earlier. And, uh, in there, there's also a link to the repo and, uh, everything.

All right, so welcome to the second part of the, of the workshop. So now that we have, uh, an overall idea of what context engineering is and what are the different techniques that we can apply to our agents, uh, now what we want to do here is see how they actually perform i- in, in our case, for

our AI tutor. I will first start by describing a little bit about how the AI tutor works, so the system design, and then I will follow up with the initial experiments that we did.

All right, so the AI tutor is actually very simple. It's one agent that... It's a ReAct type of agent that just loops over, over tool calls and thinking, uh, blocks.

And here we just create a very simple one using the LangChain library. So, uh, we use the create_agent method with the InMemorySaver because we, in this case, we don't save past conversations.

We just use the, the current history. And to customize this agent, we use the middleware feature of LangChain, where you-- we can add different, uh, features that can change the behavior of the agent at runtime.

So in this case, we want to summarize, for example, and clear the tool outputs. Or also, uh, in our case, have the, the user be able to choose the, the source, uh, uh, the sources, the, like, which lessons, which courses to, to use to, to answer.

To do that, we also add two different tools. So we have the first one, the retrieve tutor context, which u- which uses a very classic hybrid search pipeline. So, um, semantic search along with keyword search, and we combine both results to get the, the best possible list of chunks.

And then recently, we also added the second one, which is letting the agent actually browse the file system, the knowledge base, uh, just like, uh, we can... Just like coding agents can in the browsing your code base, for example.

And we also borrow from the idea of Karpathy by creating a wiki and helping the agent basically browse, uh, this knowledge base more easily.

I will come back to these tools in a few, in a few mo-moments. We also add a FastAPI app to wrap the whole system with an endpoint, and we add a Next.js, uh, UI to let students use the, the AI tutor.

So I will talk a little bit about the first tool. So we have a large corpus. So we have all of the lessons from all the different courses that we created over the past two years.

Uh, and also documentation from various public open source libraries like LangChain, LlamaIndex, and even documentation from, uh, OpenAI. So they, they make available, available all of the markdown files from, like, how to use the OpenAI API, how to use Codex, and we also have, like, Claude Code documentation.

So it's a very big corpus that has over eight million tokens. And of course, this cannot fit in a single context window, so we have to store it in a way where we can retrieve the most important or most relevant information.

So in this case, the agent receives a question, and the user can then choose, uh, well, beforehand, the user can choose specific source. So we can filter this knowledge base.

It makes it better for, um, to improve recall, so precision to get the most relevant information.

Then we do hybrid search. So this is very classic, um, hybrid search. We use a embedding model. In this case, it's a Cohere, um, Cohere model with a BM25 for the, uh, keyword, uh, index to get the, the most relevant top thirty, uh, chunks.

Then we merge the two results from the, uh, semantic, uh, similarity and the keyword search, and we then re-rank to the top five most relevant chunks.

And that's, that's what, uh, we, we return to the agent. We also have a limit of a hundred thousand tokens, so we don't want to... So let's say, for example, we, we go over, uh, we just remove the last few chunk, uh, the last chunks that make it so that we don't cross that threshold.

So these numbers, th-this configuration actually is not random. We did experiments, uh, to optimize this pipeline. Uh, I'm not gonna talk about it, but it's in one of the courses that we share.

Uh, basically, we just want to try as many configurations as possible and improve recall. So we measure, did we retrieve the correct page, uh, in our knowledge base, and we just choose the best, uh, settings.

So like I said, it, uh, yeah, in, in this case, it's very precise, very-- it's very good. But what if the agent needs to browse the whole knowledge base to get the best possible answer?

So let's say I want to learn about Codex, and I want to learn about Claude Code. How can I best use, uh, those two tools? And also, like, if we need to have var-various documentation pages in context, i-is this the best possible, uh, tool?

And there's a paper. Uh, I, I link it here in the, in the, in the slides, but it's, uh, yeah, it's a paper that shows that basically letting the agent browse the, the knowledge base can be very beneficial.

Uh, so you can look at it if you want afterwards. Very,

very slow to load. Uh, so that's why we ended up creating this second tool, the run key, key, uh, run knowledge base command, where the agent can browse, um, the knowledge base, the file system using bash commands.

So first of all, what we did first is create these, uh, three different, um, folders. So we have the raw folder with all the different markdown files. So all the lessons from the different courses, the documentation from the different open, open source libraries.

We, we also have this generated, uh, folder with... This is, uh, generated, uh, automatically with basically just the,

the, the, the titles of each of the markdown files, so it's easier for the agent to, to find, um, relevant information. And then we also have the wiki where, uh, in this case, it was Claude Code that created this.

It basically reads all of the raw files in the, in the folder, in the raw folder, and it creates a very, uh, concise, uh, set of files. So topics, frameworks, uh, from the different source, uh, sources.

So for example, I can have a topic related to fine-tuning. So in this case, the agent would be able to find all of the different raw files related to fine-tuning, for example.

Here, we let the agent only read. So this is when we actually deploy it. So this is the one you can try on the, on the space. Here, the agent can only read the knowledge base.

It cannot modify it. Uh, so we only allow these bash commands that basically cannot, uh, modify the, the file system. We also put some limits around this. So for example, if a command lasts over eight seconds, uh, we can just return an error or let the agent execute something else because it's taking too much time.

And we also cap the tool outputs to forty thousand, uh, characters. So in this case, for example, if a lesson is over this amount, what the agent can do is then, "Oh, okay.

So I just got the first forty thousand. Let me, let me do a follow-up command to get the last, uh, piece of the, of the lesson," for example. Uh, we also limit the number of the, of commands.

We actually never see the agent go over this limit of twenty commands per turn, but this is just a, a fallback, uh, in case it takes too, too much time to, to answer.

And we also sandbox, of course, the agent to only browse the knowledge base, this specific folder.

Like I said, we create this offline. So the, the three different file, uh, folders, we create this once or every time we want to add a new, uh, a new course, for example, we, we, we tell Claude Code, "Can you add a new, uh, can you add this to the raw, raw folder and also create new topics,

uh, around this new, new content?" So we do this once, and then we deploy it so that the agent, uh, can, can browse it.

With our current system prompt, we can see that it's, uh, used almost every time, so for almost ninety percent of the turns. We can tweak this to make it use it less, uh, or more.

We didn't optimize for, for this specifically. And I guess the most interesting aspect of doing this is that we measured the precision-- the recall of using this tool, uh, actually turn-turning it off, and we actually got the same amount of recall.

So just using the first tool was enough to get, uh, all the relevant information, and just adding this second tool was just fifty percent slower. Uh, ba-basically, it's faster without this tool because it does less tool calls.

Um, and yeah, we, we basically didn't see any improvement on, uh, on re-- on answering with the correct, uh, documentation. It, it was fun to add, but we, yeah, we didn't see any, any be-benefit.

And one reason for that is that we tested using real-world... Well, well, basically the questions we get from students. And basically those questions weren't complex enough, we guess, to actually benefit from using this new, new setup.

Um, so this is what-- uh, this is how initially, uh, our AI tutor managed its context. Uh, we, we started with this because, uh, it looked fast, it looked, uh, good.

Uh, we didn't actually measure anything. It was just like, "Oh, it looks good. Okay, we will just set it, set it like this." And so basically, we have these three different, um,

context engineering, uh, techniques where we clear the outputs, uh, after five thousand tokens. Uh, but we at least keep the last five ones. So this was basically a way to keep a very small context, uh, during a conversation.

We also added the, the capacity to summarize. So after thir-thirty thousand tokens, uh, the tutor... well, the system summarizes co-- the, uh, the history. But we at least keep the last twenty messages to make sure that, uh, those are very accurate, those messages.

And we also s- uh, have the source preference. So that, that just allows people to choose what, uh, sources to use, uh, when, uh, the, the tutor answers.

But like I said, these are unprove-unproven, uh, defaults, and we actually want to know what actually works best. Um, so I guess you, you can-- Louis showed this at the beginning, but you can access the tutor live.

I'm g- just going to show this very quickly. This is the Hugging Face space. So this is a separate UI, uh, just to show you. We also have the, the chat bubble one, uh, on the lessons, uh, on the course themselves, itself.

Uh, and here on the, on the left, you can choose the different, uh, sources to use, enable them or disable them. And then you can, uh, yeah, send your, your query.

So as you can see here, I can just, uh, send a new request. And we see Gemini, in this case Gemini 3.5 Flash, use its, uh, reasoning and use its, uh, capacity to, to do co-- tool calling and to answer.

And I guess, uh, here there's a... I think it's just the internet

bugging. But we should have a response. And yeah, the code is open source, so you can use your favorite, uh, coding agent to explore the code base and, uh, and learn

about how we implemented this, uh, specifically. So we have the different activity, uh,

the, the, the activity that the, the, uh, the model did. So four tool calls, it thought four times, and it used, uh, ten sources, and we have the, the final answer.

So everything that, uh, so every time the student uses this chatbot, we actually log everything. So

we-- for every single turn, we have, uh, the input tokens, the, the output tokens, how many of them were cached, uh, what was the cost, what time it took to, to get the first token, how many tool calls it did, and if we actually-- if the system actually did something around, uh, summarization.

So this is very useful, and that's, uh, what we are going to use when, uh, measuring the, uh, the different techniques. So why do we need to measure? Be- well, because, uh, the, the techniques that Louis showed all sound very smart.

So you, you might think that they are very, uh, useful, but sometimes they're not. And, uh, as we, as we discovered with our experiments, actually it might be detrimental, so because of the, the way APIs cache the tokens when they are, um, when, when they are sent.

And it's also difficult to, to know in advance what, what is best to use.

So before I go into the experiments, I just want to [clears throat]

define a few words because we're go-- I'm, I'm going to use these words throughout the, uh, the, the, uh, the presentation. So a preset is basically, uh, the way the AI tutor was set up in, in the experiment.

So for example, it can be In this preset we did summarization at this amount of tokens, or in this preset we, we used sliding window, for example. So th-that's what a preset is.

We have the different tasks, so a task type. Uh, for these initial experiments, we only did two tasks, uh, single turn and multiple turns, also sessions, uh, called sessions.

And one run is basically just running one preset on a task, and then you get the run. Um,

the bundle is just the, the result, so it's just a JSON file with all the different, uh, metrics that we save to the disk.

So first task, single turn. Uh, so these are question and answers, and we didn't generate this. It's not synthetic. Uh, we actually... Uh, I, I had Codex, uh, scrape all of the, uh, questions and responses from our website where students can ask questions and get answers from, uh, members of the staff.

Uh, and that's how I got this, uh, initial-- we got this initial, um, dataset. Uh, we cleaned the dataset and only used 60, uh, 60 pairs, uh, because we saw that some of the questions weren't good for the type of task.

For example, uh, there were old questions about previous versions of some libraries, and we, we might not... I mean, the-- right now if the tutor answers, it's not gonna be using this old version of the library.

So we just, uh, removed some of the questions, some duplicate ones, and, and, and we got, uh, this first, uh, dataset. And what we measure is the retrieval. So did we retrieve the correct-- I-is-- Did the tutor retrieve the correct lesson, for example?

This is done automatically. We can see, uh, just by looking at the code, did we, did we use the correct, uh, lesson or not. And we also look at did-- do we have the correct facts in the answer or the right kind of response in the answer.

These two, uh, are actually, uh, graded using, using an LLM. Uh, you can use APIs to do it, but, uh, right now I think the best way to do it is to use, use your, uh, Claude Code, Claude Code subscription or your Codex sub-subscription because it's cheaper than using the APIs.

We also have the second task, the session, so m-multi-turn, um, conversations back and forth. Uh, here, what we want to know is,

is the AI tutor able to recall facts after multiple turns? So this is a bit, uh... Th-i-in this case, we do use some generated, uh, content. So we do in, uh, generate facts that we put at the beginning.

So we have a student, like a fake student, state a fact. So for example, "I want to learn about RAG." And then we stuff the conversation with just filler messages because we just want...

Yeah, we just want to have a lot of messages. And then we have, um,

a probe, which is just the student asking a question again. So for example, it can be, uh, "What should I learn today?" And since the, uh... I'm gonna go through it in the next slide, but, uh...

Yeah, let's, let's, let's the, the example. So for example, here at turn one, we, we, uh,

we have the student, the fake student im-implement a, a state of fact. So it w- uh, the student wants to learn about RAG evaluation, um, and that, that's basically the fact.

Then we just add a lot of messages, uh, filler, filler messages. And then at s- at some point, we have the student say, for example, "What topic should I learn about today?"

And then what we expect the AI tutor to, to, to say is that, uh, the student should learn about RAG evaluation, so more specifically hit rate and MRR, for example.

We also have a gate part in the evaluation where, let's say we are testing the summarization technique. Uh, we actually just want to know, did summarization actually happen or not?

Um, so this is, this is, this is like one example of one task in the sessions, uh, dataset, in the sessions task.

Now we have the evaluation harness. Um, so the main, uh, harness, I guess the, the main function is the run, the run task, the run battery function that just, uh, runs this, uh, this task.

Um, we have the grading. Like I said, we-- it can either be a code check, so did we retrieve the correct lesson or not? And we can also have the LLM as a judge.

In this case, we use, uh, the subscription of Claude Code.

We also have the check triggers aspect. So this is just a check to s- to see that if the evaluation went, uh, good or not. Did we actually compact or not?

This is j- this is just to make sure that, uh, the, the run is actually good and we can save it. And then we have a generated report, uh, to see like what was the latency, what was the time to first token, and e-every metric that we can, uh, measure.

So yeah, basically we can evaluate everything and then grade it afterwards. Uh, we, we can run it once and then grade it afterwards.

So what, what we ran. So we ran eleven presets,

uh, and we changed them, uh, for, for each experiment. So we have the, the full history. So these are the, the main ones, the full history. So this is a case where we don't, don't touch the context.

We le- we leave everything as is in the history. And then we also have the production that I showed at the beginning, the defaults that we have.

Uh, so these are the reference points, and then we have these six techniques that I want to compare. So sliding window, prompt compression, uh, selective retention, and, and the other ones.

And I-- what I want to see is just w- what re- uh, memory recall, recall do I get, uh, if I keep everything else fixed. So I use the same model, the same prompt, the same tools, the same dataset.

What, what's the difference? Uh, now ju- now, just doing this was a bit expensive. I, I didn't expect this to, to get, uh, over, uh, five hundred dollars, uh, but it did.

And, um, that's one of the reason, uh, we did the afterwards follow-up experiments using, uh, cheaper models. But, uh, my colleague, uh, Samridhi will talk about this. Uh, so what arm-- So what, uh, basically what preset actually won.

Uh, and so these are our, um, our results. And as you can see, uh, we weren't expecting this, but basically not touching, um, the context was actually the best, the best strategy for recovering this fact over time ov- over multiple, uh, messages.

Um, you can see that the production, so the, the defaults that we thought were good enough were, were actually not the best. Uh, not doing anything is actually better.

Uh, we did two, uh, two different experiments, where one was just one trial and the second was, um, two trials. So we have, uh, like a more, uh, statist-- I, I guess it's, it's better, but the, uh, the numbers are not like ac-- can-- might not be accurate because it's just one trial and two trials.

But I guess the most interesting thing is just the order in which the techniques ended up being in the table.

So in this case, keeping everything wins on the memory side. But what about the cost?

Uh, this is what the production cost, uh, was for the single turn and the session. So almost fifty cents, uh, for a single turn and twenty-four cents, uh, for the multi-turn, for each turn.

Uh, we actually had very good memory, uh, recall for pretty much all the techniques in the single turn, because in single turn you don't have enough tokens to actually fire up the different strategies.

Uh, so for one response, you don't need to do summarization, uh, compaction, or anything like that. Uh, so that's why you, you see, um, high numbers. Uh, but as you can see, after in the multi-turn, uh, task, you can see that the quality degraded to thirty-eight percent.

Uh, and we-- if we compare this to the

full history, so here we don't touch the context, uh, the history of the model. We can see that not touching, uh, is actually cheaper, it's faster, and we have better recall overall.

So keeping everything wins on, on all of these, uh, three, uh, fronts. Uh, so why does it... So why is it actually, uh,

like, why is it, uh, why do we have less latency? Like, what's, uh... We want to, we wanted to understand that, and it's basically because if you remove the tool outputs consistently, then the agent needs to re-retrieve, uh, afterwards for information it already had.

So you're just making the agent, uh, do more tool calls, and that's why it ended up costing more, uh, and yeah, using more tokens and having less, uh,

uh, less memory recall. So these are the results we initially got using, uh, Gemini 3.5 with the, uh, this, this dataset of eleven to thirteen turns. It's not huge.

Uh, it's-- there's not many messages. That's why we wanted-- we now want, uh, in the follow-up part, do a more, uh, different experiments that my colleague Samridhi will, will show you.

So yeah, let me in- let me introduce you to Samridhi. Yeah.

Um, so this is gonna be my part, and, um, as we ended on the note where Omar just said that it costed it, cost, um, it costed us almost six hundred dollars to, um, run the evals that we ran.

One question we were trying to, um, answer with this extended evaluation was, um, so when do you, uh, when does compaction actually matter? Or should you actually compact or not?

'Cause we clearly saw that when we have, um, you know, the full answers in the window, it works really well, but it costs a lot of money. So, um, I tried to, you know, do this evaluation in like three sorts of context.

Uh, first one was cache chats. So, you know, like when you're chatting with Gemini, you'd be able to see that is the cache chat option. The second version is gonna be document plus tools.

So if you are pasting like a long document in the AI tutor or if there's just tool output, what happens then? And finally, you know, if you go local or if you scale this evaluation, how well is it gonna work out?

So, um, should you ever compact? So before my part, Omar just showed that on Gemini 3.5 Flash, um, keeping everything won. Um, but, uh, you know, the-- why did we come up with that question was because, um, you know, full history on a frontier model like Gemini would be very, very expensive.

Um, so, um, you know, with all this extended experiment, we are trying to figure out was it actually worth it or not.

But, uh, before we start that, I wanted to just talk about the different context we see in our AI tutor application. Um, so first one is gonna be like a long chat history, uh, where, you know, we have, um, a long chat, but all of the details what the, the students are asking or they're chatting about, they

can get buried in. Um, the second is gonna be a pasted document. So, you know, we do have a lot of students who are gonna just, like, copy-paste a lot of documents there.

Um, so, you know, um, and also because we have, like, limited, uh, context window, how does that fit? And then it's gonna be, you know, different tools that we use internally, um, but this is just gonna be, like, bunch of logs that the tools have.

And since, you know, these are, like, different context, each of them need some sort of different fix. So, you know, we had to evaluate it for all different, um, contexts that we had.

So, um, you know, the first obvious thing, uh, looking at the cost, uh, we were like, "Okay, let's try out a cheaper model and see, you know, um, does it do better?"

You know, what sort of techniques work on that? Does compaction work on it or not? So, um, DeepSeek V4 Flash was an obvious option, and we were like, we will, uh, try this out on this and see, um, how well it works out.

And, you know, you can see there is, um, you know, a, a drastic cost difference between Gemini and DeepSeek here. So here we can see, um, you know, there's a drastic difference between cost, uh, when we checked the performance on DeepSeek V4.

And the main reason was that, that we were getting a cache discount. So the cache discount on Gem-- um, DeepSeek was, um, you know, fifty X as compared to Gemini.

And even in this, um, you know, setting, we saw that keeping all, um, you know, all of the context still won. So, you know, we were just getting the best performance, um, in that case for DeepSeek as well.

So but, you know, the, the last thing from this experiment was that we figured out a cheaper model, but, um, you know, uh, now we wanted to see that even though we have everything, uh, you know, keeping everything, uh, makes it cheaper, but does it remember better?

You know, does, uh, keeping all of the context remember all of the details the student might be asking us? So, um, you know, this is how I tested out the memory of the model.

Um, so we have conversation within our system where, you know, students are asking questions like, you know, about their setup, about the errors that they're seeing, what-whatever they've already tried.

So I just took these questions. Um, so I just took these chats and, you know, asked questions about specific details just to see if the model is able to, like, figure that out and if it is able to give me an output for that or not.

And, you know, the results I saw is that ninety-five percent of the time, if the model was able to, uh, you know, give us the right exact details that I was trying to look for, and even when it is keeping all of the details.

Whereas if I summarize first or if I compact, um, the context I had, it only gave me the answer back thirty-two percent of the time. And, um, if you think about it, um, the reason for that is that when you summarize, you, you know, you, uh, remove all of the necessary details, so you're not able to, uh,

you know, keep all of those details, and the model keeps on missing those out. So, uh, you know, we are able to see that keeping everything wins in terms of cost.

If you have like a, you know, model like DeepSeek, um, then it also is remembering things. So, you know, it's not that if you have a long conversation, it is not able to remember things.

So, you know, it is correct ninety-five percent of the time. So the next thing we wanted to see is the cost part of it. Uh, you know, how does it actually, um...

Does it cost most? Does it cost the least? What happens in terms of tokens? So, um, you know, on DeepSeek, we saw, um, the setup that was sending the most tokens is actually the cheapest to run.

So the full history, uh, you know, setup that we had was sending the most tokens, but, uh, we were still getting the best results out of it because ninety-seven percent of the tokens that we had were cached.

And, uh, you know, as you-- as I-- as we just saw in the previous slide, cached tokens are really cheap. They're, uh, you know, they are charged separately. So, um, summarizing, uh, works the other way, uh, and every turn it makes, the model reads and writes, uh, new tokens.

And, you know, this is something that I ran on, like, thirty-six turn conversation, and it was about one point seven eight million tokens, and keeping everything still came out ahead.

And, um, so, you know, this answers the question that it wasn't just, uh, you know, Gemini. It, it works same on DeepSeek as well. So, um, the cheaper model is, uh, what brought the cost down, but the results are the same.

And, um, you know, in, in respect of this, I wanted-- the next thing I wanted to ask is what happens when the conversations really grow? 'Cause all of these were tested out on, like, short conversation.

If I really, really, uh, you know, increase the length of the conversation, how does that work out? So, um, you know, when I tried to, you know, run this entire experiment on a longer context, I saw that, um, you know, if even if I'm pulling like one specific detail out of it, um, the model performed really well.

So on the top part, the green line, those are all of the distincti-distinctive facts that the model is able to find out. So we can see that up until eight hundred K tokens as well, the model was not missing out on those facts.

It was giving me, like, good and consistent results. For, uh, you know, some ambiguous facts, um, the performance dropped, um, you know, to half of what I observed on the distincti-distinctive facts.

But for overall, our-- for our AI tutor, this, uh, you know, result, um, was really good. So, you know, we saw that, um, the model, even when you're not compacting anything, holds really well, even if you have a really long conversation.

So, uh, but so far, everything that I've talked about is only per turn. So, you know, every cost has been per turn. But does it help when, you know, we scale it?

Because, um, a chatbot is not something, um, that, you know, it's not like one-turn, uh, situation for a chatbot. Um, the tutor is a long-term service where, you know, students are asking, um, you know, questions on, on a massive scale.

So let's say we have, uh, you know, if I, I calculated this using this, like if we have hundred thousand to a million turns of questions every day, what would, uh, you know, be the cost on DeepSeek?

Or so, you know, for DeepSeek, the cost was, uh, approximately somewhere from eighteen thousand to like one eighty thousand a month. And, uh, you know, even though we don't see that sort of volume as of now, but paying per token starts to add up.

And so the, the alternative for that was going over to a local model just to see if we are getting the same sort of performance on local model or not.

And, um, so one way, um, you know, we were thinking that because local models cache as well, can, you know, we use the same sort of setup on a local model, and will we get the same result?

So, um, you know, because, uh, we had like hardware limitations, we just tested it out on a MacBook. The maximum context window that we could go up to was thirty-two K.

And, uh, so we thought that can we, uh, you know, can we do that locally now? Uh, but we can't because, uh, you know, the, the sort of, uh, lessons that we had are-- had are bigger than like thirty-two K context window on their own.

And once the conversation doesn't fit in the window, um, caching was no longer helpful for us. And we, uh, you know, we have to make, um, the context smaller either by compressing it or by retrieving only the parts that we need.

So, uh, you know, the next question we were trying to answer is, can we, uh, you know, once you have to compact locally, what actually works? So, uh, you know, for, um, the chat memory, going local, uh, and trying to keep everything stops winning because you can't keep everything.

And, you know, a simple, uh, question here would be that why can't you just keep increasing the length of the model? You know, why can't you use a bigger model?

Because of course, we have hardware limitations. For us, it was, uh, you know, a MacBook, but, you know, GPUs also have like hardware limitations. But, you know, we went from like a 7B model, 8B model to a 32B model.

Uh, but here we landed on the, uh, you know, conclusion that even though you keep increasing the length of the model, uh, it is not gonna increase your context window.

You know, you cannot repair that part. You have to, you know, make a choice there.

Uh, but, um, you know, this is only for the chat history and what happens when you are trying to deal with like documents locally. So, um, this was a little surprising because if you are retrieving results with like local documents, um, you know, it was really good.

We got like hundred percent accuracy in that case. So if, uh, you know, when students are pasting something which is too big, uh, you know, RAG is a good option there.

You can use that, and it can help you retrieve the exact, uh, data that you're looking for. Also, the processing time in this case was anywhere from twenty-five to sixty-five seconds, so, you know, which is, uh, pretty good in terms of the, you know, the output that we are getting.

Um, but, you know, if you are trying to like stuff the window with like more context than you have, we saw that, you know, it took us like approximately three forty seconds, um, to get the output when, you know, our, um, conversations were really long, and the output that we got was a single token.

So, you know, you are, um, not getting anything, but you're also wasting a lot of time when you are trying to do it. So, um, you know, you have to be careful about what option you choose in this case.

So, um, so, you know, you also have like different ty-type of retrieval strategies that you could use. The default retrieval is, of course, semantic search, where you're just trying to match, uh, you know, the meaning of the text, and that is the dense RAG, uh, heading that you can see on the chart.

Um, it mostly works, but, uh, you know, we saw-- We tried to make it work from like, uh, fifty K token to two hundred K, and we saw that, you know, dense, um, RAG worked really well.

You know, it was like eighty percent. But when we increased it to like four hundred K tokens, it was not able to retrieve facts that were buried in the middle, and it started giving us like zero percent recall.

Whereas, uh, you know, something like BM25, it still got hundred percent every time. So semantic search, uh, on its own is not enough, and that's why, you know, when Omar talked about our setup in the AI tutor, we're actually using a hybrid search.

We're using a mix of both, um, you know, dense and, um, you know, BM25. We're using a, a combination of both those. Um, so, you know, after all of this, we came up-- We had like one other question, which was like, uh, how does all of this, um, local setup compare to cloud?

You can-- Because that's the, uh, real way we'll see the result. So we wanted to put them side by side just to see, uh, what is the output. And for chat, uh, you know, the local setup was not up to the par of, um, the cloud co-- you know, the cloud setup.

On cloud, keeping everything scores, you know, somewhere from, from ninety-two to ninety-five percent, but locally it was stuck at like thirty-three percent, and the context window was a limitation here.

Also, you can see that, um, you know, local, um, local models actually work because, um, there is no cost. Like, you cannot see because you already own the hardware, though, um, you know, there's a throughput limitation there.

Uh, but if you use a technique like retrieval, uh, you know, you get like good accuracy even on a local setup.

So, um, in our case, what we found is that on memory, uh, you know, keeping the whole chat recalled about like ninety-five percent of the details that we were providing it.

It was able to, you know, give us correct answer ninety-five percent of the time versus it was, uh, like just thirty-two percent if you summarize it. Um, on long context, uh, you know, finding a single fact, uh, is easy for the model.

We went up to eight hundred K tokens and, you know, we did not, um, see any sort of context rot in that case. Um, on cost per turn, we saw that the cheapest run is actually the one which is sending the most tokens because caching makes, um, resending the same context, uh, you know, very cheap.

And on cost at scale, um, um, you know, it scales up for, like, let's say if we have, like, thousand students, uh, you know, Gemini costs us about, like, forty thousand doll- uh, forty thousand a month, whereas Deepsea- Deepseek was around nineteen hundred a month.

Um, so, um, going local saves us on a cost a bit more. So the main thing to take away is that, um, do not compact by default. You have to name the constraint that you have, and then, you know, look for a better alternative.

So what did we finally decide after all of these different experiments that we ran? Um, so we decided on Deepseek, uh, V4 Flash cache. Uh, we had hardware limitations, so for us, um, the cloud structure worked out really well.

It is also the cheapest considering the current, um, intake of students we have, so, you know, it works out well for us. Um, and we are using, on top of that model, we are using a mix of, uh, you know, we're using hybrid retrieval to, uh, you know, get good results.

For memory, uh, you know, we have chosen to keep everything. Uh, we have got, um, you know, a, a default limit that after thirty K tokens, we are gonna, you know, have compaction, but up until that, we're planning to, like, keep everything.

And, uh, you know, that is the tutor setup that we have.

So, you know, because, uh, we had, like, time limitations, so these are all the evaluations and experiments that I could pack into this time. But if you would like to, you know, learn more about these evaluations or you would wanna build a tutor yourself, um, this is the, uh, full stack AI engineering course, uh, on academy.towardsai.net.

Um, so you can go to this link and, uh, you know, go through the course. Um, but thank you so much, everyone, uh, and now we can take any questions. [audience applauding] [upbeat music]
