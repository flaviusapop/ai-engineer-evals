# Your Fridge Is a Valid Payment Device — Eleonora Drykina & Nina Žižakić, In The Pocket

Source: https://www.youtube.com/watch?v=gonAewBZxfU&hl=en

Uploaded: 2026-10-14

Transcript source: AI Engineer's first-party, machine-source-reviewed transcript segment JSON, recovered from the official talk page. Source: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/04/04404c8e19d882a6beb7a7018a52d788535bdedef6d9f1761682f2f046e42e32.json . Segment text is preserved; transcription errors may remain. Original segment timestamps are retained in publisher-transcript-gonAewBZxfU.json.

## Transcript

Uh, hi, and welcome to our talk titled, uh, Your Fridge is a Valid Payment Device: Uh, Unremarkable RAG in Production. Uh, let me start by explaining the title. So, um, this is a pla- page from one of our client's rule books. Uh, so it's one of the many documents we, uh, built our, uh, RAG system around. So you would expect, uh, sort of a dry financial document, and that's mostly actually what  it, it is. Uh,

but there are some, uh, fun sort of tidbits, uh, there too. For example, um, this page, uh, which, uh, shows a list of devices you can pay with. So it's... there's, uh, stuff you'd expect there, like, uh, phone or cards, but then there's also more creative, uh, ones like, uh, cufflinks, a handbag, a garment dress, and even a refrigerator. So I thought it was really cool to find a, a fun fact like this in documents,

uh, you'd expect to be, uh, very boring.

Um, so, uh, uh, let's, uh, introduce ourselves. Uh, this is the only photo that we have of the two of us together. Uh, we don't usually wear, uh, XR headsets, uh, but on this day at the office, uh, we were trying all fun... k- all kinds of fun, uh, gadgets. Um, so I am Nina. I am an AI engineer.

Um, and I'm Eleonora. I'm a product engineer. We work at In The Pocket, uh, a digital product studio with main office based in Belgium. We help our clients with AI transformation and custom software.

And, uh, today, uh, we are gonna talk about a RAG project we built for one of our clients, uh, a large, uh, Belgian, uh, fintech company, and it will, uh, stay anonymous, uh, for, for the, for this talk. Um, so at its core, uh, this is a classic, uh, RAG problem. Uh, and in this talk, we wanna show, like, the technical decisions we had to make and, uh, to go deep into how,

how we built this. Um, it's the... a talk we... that would've been useful, uh, for us, uh, at the beginning of, uh, this project. Um, so, uh, what is, uh, the problem we ha- uh, have? Um, so our client is, uh, running the biggest payment scheme in Belgium, uh, and all the r- rules, uh, about this scheme are, uh, written down in, uh, rule books. So these are, uh,

PD- around 270 PDFs, uh, so or, or around 6,000 pages. A lot of the informations is, uh, a lot of the information is in tables, um, around 3,000 tables. Uh, and this is how they, uh, sort of structure their, uh, knowledge. A lot of important, uh, knowledge is in the tables themselves. And the, uh, rule books, uh, refer to each other a lot. So, uh, one rule book would refer to another, and then, yeah, that one to another

one, et cetera. Um, so doing a RAG for a financial institution, um, comes with, uh, some challenges. Um, the first one being the citations. So of course, always, uh, answers should be correct. Uh, but especially, uh, in a financial context, it's even, uh, more important. Um, so every answer needs to cite the exact rule book,

uh, section and page, um, so that people can see where the answer is coming from. And the second, uh, challenge is grounding. Uh, so the LLM, uh, that's, uh, running underneath is a general, uh, model, so it's trained on, on, uh, general knowledge. So it knows a lot, including, uh, things about other payment schemes, uh, or how they work or their fees. So we kind of had to, uh, decide and make sure that the knowl- which knowledge is okay

to, to use. To, for example, it's okay to know what a bank is. That makes sense, and it's not something that would be, uh, defined in the rule books. Um, but, uh, what another payment scheme charges or how it works, that's, uh, should not end up in an answer unless it is in the rule books. Um, so, um, this is what the solution we built looks like. So it's a chatbot. Uh, so you ask a question, and it answers

based on, um, these rule books. If the answer is in a table, um, it will show that table as well. Uh, and below the answer is the list of sources it used to, um, retrieve the... or to make the answer, including, uh, specifying the, uh, section and the part of the rule book such that the user can open, uh, uh, that rule book. And in this example, I ask, "Can I pay with my fridge?" I got an answer, and I can then ask also

follow-up questions. Um, this is, uh, what the whole system looks like. Uh, so it has, uh, two parts. On the left part is, uh, the indexing, so this is what we do sort of offline. Uh, and every new release of the, these rule books, um, we turn these PDFs into chunks and store them in a vector database. And on the right, uh, uh, part is about the serving, so the online part for every, uh,

uh, question that a user asks. Um, the agent searches this vector database, um, and then the answer gets streamed, uh, back to the user. So I'll talk about the indexing, and Eleonora will talk about the serving part. Uh, so about the indexing. The setup is, uh, pretty simple. So we start with the PDFs, we split them into chunks, we, uh, add me-metadata to,

uh, each chunk. Uh, we do some special processing for, uh, the tables and then, uh, we, uh, generate the embeddings. We generate two types of embeddings, a dense one and a BM25. So I'll, uh, now go into detail about the first three steps, and Eleonora will later talk about the embeddings. Um, so, uh, the first step, splitting PDFs into chunks. Um, the way it works is

we pull out the text from, uh, every page, uh, we split it into, uh, paragraphs, and we sort of pack paragraphs into a chunk until it reaches about 2,000, um, uh... around 2,000 characters. Uh, and we also make sure that we never split a table over, uh, two chunks. Uh, we also detect se-section headers using, uh, regular expressions, so things like, uh, chapter 3 or 4.2.1.

Um, and that gives every chunk its, uh, section path. Uh, s- for example, this one lives in chapter 4, section, uh, 4.2. And, um, that path is used for, uh, adding a citation, uh, but also it's used to, uh, fetch the whole, uh, section when the agent, uh, needs more context. Um, and this all works because we don't overlap chunks. So,

uh, a section is, uh, like, is just a collection of chunks, uh, and i-if we put them back in order, it's, uh, back sort of, uh, as it originated. Um, for the second step, we, um, for every chunk we add metadata. So in this example, we see the, the text of the chunk, uh, from this fridge rule book. Um, and then below is, are some, uh, metadata fields. Uh, so we need the, um,

the rule book name and the, the page, such that we can actually show it in the citation or, uh, in the source, uh, card to the user. Um, w- together with, uh, and th-that the user can then, uh, it can be linked to the PDF. Um, we also, uh, use the, the section paths, uh, both for that, for the citation, but also for the agent to be able to fetch the whole

section at once. Uh, and then we also have the chunk index, uh, which lets the agent put, uh, a section or even a rule book, uh, back together. Um, the agent uses, uh, rule book IDs to be able to get a list of all the rule books or see what's available. And at indexing time, for each rule book, we generate, uh, an LLM, uh, yeah, using an LLM, we generate a summary,

um, which is then attached to each, uh, chunk for its, uh, uh, for, about its, uh, rule book. Um, and that, in that way, the agent knows what the document's, uh, passage comes from. Um, and for the rest is, um, the rest of the metadata is, uh, business logic fields. So, um, what type of, uh, rule book it is, which role, uh, roles it applies to, uh, whether it

contains a table, and these are the things that agent, um, uses, uh, with the, or gets with the search results. Um, then the third step is the table processing. This one, uh, is important because, uh, as I said, there is a lot of knowledge within the tables. We initially didn't, uh, kinda realize it, um, and so we, uh, the, the initial processing was just straightforward, uh,

fetching, uh, getting the plain text from, uh, the PDF, and that didn't format the tables well. But in this dummy example, you see that the, the domestic, uh, field, uh, spans over multiple rows, and cross-border over two more rows, and then the refund spans over both. So if that's not, um, uh, cle- uh, or well, uh, put into text, uh, yeah, the agent can fetch wrong information, and especially with

important things like fees, uh, it's important to, uh, yeah, fetch the, the right, uh, row and for the right column. So what we do is we transform the tables into a CSV format. So we duplicate basically those, um, uh, those fields, and then we, uh, uh, in that way, the agent, uh, fetches it, and when it fetches it, it, um, fetches the correct,

uh, uh, the co- correct, uh, row, that the one that it needs. And that really made a, a big difference for the correctness of the answers. Um, so this was, um, uh, about the indexing. Now we have these around four thousand chunks. Um, and now, uh, Eleonora will talk about the serving part.

Yep.

Okay, so the previous part, build the index. Uh, now this part is gonna be ar- about finding this right ten chunks out of four thousand chunks that have been prepared. The obvious move here would be go for dense embeddings, turn the question and every chunk into a vector, compare the distance. And that is great for the meaning, but rulebook codes, message names, exact identifiers would look like

noise to an embedding. But to the member who's asking the question, quite often this is the essence of the question. With BM25, we have the mirror image, exact tokens would work, paraphrases wouldn't. So we combined both of them in one Qdrant, Qdrant call and fused them with reciprocal rank fusion. Um, dense's top 50, BM25's top 50 fused down to the top 30, re-ranked for section coherence and

top 10 fed to the agent. Um, and the nice thing about RRF is that we don't need to calibrate the score between these two legs. Um, on the retrieval only evaluation, uh, of 63 questions compared with dense embeddings only, hybrid approach moved hit rate from 92 to 97% and didn't lose a single question that, um, dense embeddings already could find out. Okay, so

we have our 10 decent chunks, but not every question fits in 10 chunks. Some of them are chained. One rulebook points to another, and the answer would be only complete once you follow that pointer. Some of them need breadth. List every fee for this transaction type is never gonna fit in the top 10 of anything. So instead of a fixed retrieve, then generate pipeline, our agent has four tools, narrow to wide. Search rulebooks always comes first.

That's the 10 chunks we were talking about previous slide. If that is not enough, retrieve rulebook sections pulls the whole section in order by section path, which is exactly the approach Nina mentioned earlier, um, storing the section path. And this base off here, zooming out, is just fetch every chunk with this path sorted by chunk index. Above that is retrieve full rulebook, which works

for small rulebooks only, and list available rulebooks for when agent needs to know what exists at all. So a few guardrails made this work in practice. First, if a rulebook is too big, over roughly, uh, 100k tokens, the full rulebook tool refuses to dump its content into the context and hands back the available section

list instead, with a warning that the rulebook is too long. Second, if a section name doesn't match, it hands back the available sections so that the agent can retry rather than give up or try to invent the name. And last, uh, there is a tool called Discipline, instruction in the prompt, because most of the questions require two to four calls. Uh, but before sixth call, the agent

is told to ask itself whether it's fetching something genuinely new or just rephrasing a search that already failed before. And this one came from us watching real traces when the agent tried the same search again and again, hoping that number would eventually show up. So cost for all of this is latency, a median of 38 seconds per answer. It is not just a chat reply, it is a

small research task. And, uh, we lean on streaming to make 38 seconds feel like something is actually happening and not just chat being stuck, which takes me to the next slide. So in our first iteration, we really wanted to step away from the basic chatbot UI, and we prepared UI components and described them as Pydantic models available to the agent, saying, "Here are the components you have. Use

them in your answer together with text." For example, source card was a component, an event could be a component, there could be collapsible checklist component, and so on. The idea was to have somewhat AI-generated UI, which would be more readable than a plain sheet of text. The problem is you can't stream a partial Pydantic object. It only becomes a valid JSON once the very last token arrives. As you can see here, for a system whose answers take 38 seconds,

that meant 38 seconds of nothing on screen, and then everything arrives at once. So the fix that saved the experience was splitting the answer in two parts. The agent now streams markdown prose token by token, and the front end styles it live as it arrives. And then the source card is one piece that says it's a real UI component. It doesn't hold, um, any information you want to click before you read the whole answer, so we're

not losing anything by waiting for the full answer to stream before appending this component. And that gives us a clickable card instead of a plain link sitting in the text, which is nicer for the user. Um, but once this answer, um, is on screen, the next question would be what the user actually does with it. Clicks the source, copies the answer, keeps the conversation going,

or drop off. So that's the user experience we want to keep track of, and, um, this brings us to logging. Um, so for now, we went with the simplest logging solution, Azure Table Storage. We log every question, tool call, answer, feedback, good or bad, uh, plus events like clicking source, copy answer Together with the conversation history, which stays deliberately small.

It's just last 20 messages. It's context. Um, for where we are now with this product, it's enough. Once the product grows, we will figure out what we will actually need by then.

And how do we know that any of this actually works? Um, our eval questions come from real sources, two rounds of user testing with actual members, plus behavioral guidelines for what our AI assistant must and must not do. For example, no advice, stay neutral about competitors, and say clearly when something isn't present in the rulebook. Um, we have about 86

end-to-end tests run with Promptfoo for agent, LLM judge against the rubric, plus check that the right source document actually got cited, plus the retrieval-only evaluation from earlier. Um, two things we learned from running evals that we would like to share is first, that LLM Judge evals have noise floor, and you need to rerun

before you trust the delta. For example, when we ran our own eval, 5 out of 12 flips didn't reproduce. And the second, sometimes the rubric itself is the bug, uh, not the model. So we had a hallucinated date that the judge kept punishing, and then it turned out that this date was actually real text sitting in the rulebook.

Yeah. So now about the, um, the usage. Um, so we launched this, uh, rulebook assistant in, uh, June. Uh, for, uh-- So initially, it was launched only to, uh, the internal users, uh, of our client, and the goal is to, by the end of the year, launch it to, um, their, uh, external members and, uh, their clients. Um, so for now, we have,

um, uh, yes, some, some already, uh, usage, uh, numbers. Uh, we have around 900 questions so far, uh, split into, uh, more than 100 conversations. Around 34, uh, yeah, 34 people are, uh, actually using it. Um, we also, uh, captured the thumbs up, thumbs down, uh, feedback, but most of the people kind of stopped using that feature, uh, after the first

month. And, uh, we also have information about how many times the sources were clicked or the answers were copied. Uh, but those are the numbers. We also, uh, used AI to, um, uh, for the, uh, uh, uh, analytics. Uh, so, uh, uh, on the right-hand, we, we, uh, have, uh, yeah, how LLM interpreted it. What we saw is that, um, in the first month, as we asked,

uh, the people, uh, we had some, uh, red teaming, so people were trying to, uh, break this assistant, trying to get off-topic, uh, or questions. But, uh, by the third month, uh, and more than, uh, or more than 90% of, uh, the questions were actually real questions. Um, secondly, um, people use it for, uh, real cases. So we saw people, uh, using it for, uh, they would paste an email from their cl- uh, client,

uh, and ask for help answering it, or, uh, they would, uh, paste a raw protocol message, uh, table, et cetera, and then they would, um, draft a, a reply that they want checked. And, uh, thirdly, um, we also, yeah, since we didn't have m-many, much feedback from thumbs up, thumbs down, uh, we were trying to, um, interpret the sentiment of the conversation by looking at the follow-up questions.

Uh, so, um, i-if people say thanks or move on to a new topic, uh, we would, uh, yeah, um, count that as a positive, uh, interaction. And if they ask, uh, the same thing again, then it was probably a negative interaction. Uh, and that's, um, most we-- from that, we saw that most of the conversation, uh, went, uh, well.

So what are, uh, to, to, to sort of summarize, what are the main learnings, um, from this project so far? Uh, we, um, on the document side, we, uh, want to, uh, find that it's important to keep the structure. So the section part is important also both for, uh, retrieving the answer as well as, uh, being able for the agent to sort of zoom out, um, the, the, uh, knowledge. Uh, we also saw that the

tables need their own, uh, sort of special treatment, uh, and their own, uh, processing. Um, from the agent side, yeah, as mentioned, giving it multiple zoom levels, uh, and deciding, uh, how much context it needs, uh, was important. And in general, it was, um, uh, very beneficial once we switched from a, uh, like a single shot, uh, call to an LLM to an agentic retrieval. We saw that,

uh, the, uh, evaluation, uh, go, uh, numbers go up by quite some margin. Uh, from the UX, uh, perspective, uh, streaming, uh, was what made it, uh, sort of, uh, uh, a usable and, uh, a good tool. Uh, and, uh, we only add a structured component when the, when it's, like, uh, required by the, uh, UX. Uh, and then the last one, uh, it w- we found it

important that, uh, we tested with, uh, real users early on and, uh, to also use these, uh, tests to, uh, create, uh, or to use these, uh, user interviews to create the Promptfoo evaluation, uh, evaluations that we can, uh, use to, uh, shape the product and make the decisions of, uh, if some-- if an im-- what we think is an improvement actually is an improvement. So thank you for listening

to our talk.

Thanks.
