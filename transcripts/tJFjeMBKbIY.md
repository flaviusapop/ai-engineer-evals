# Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings

Source: https://www.youtube.com/watch?v=tJFjeMBKbIY

Uploaded: 2026-07-30

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/0c/0ce456c5537ed7b826534515da8eca8aae422e199e0c6c43e4502152d0f3f976.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/tJFjeMBKbIY.json.

## Transcript

[upbeat music] Good afternoon. Thank you for being here.

Day four of our conference, a room with no windows, right just after lunch. You are the strongest people in this building. [laughing] Let me start with a confession. For fifteen years, my job has been one thing.

I sit in a room, a very smart, confident person hands me a piece of paper, and before my company spends a hundred million dollars, I have to decide, do I believe this paper?

This year, my job still exactly that. Except now, some of time, the very confident person handing me the paper is a chatbot. And honestly, the chatbot is often better written than humans.

Better grammar, nicer formatting. Never get defensive when you ask a follow-up question. Very, very sure of itself. The problem is, being sure of yourself and being right are two different skills.

Some of most confident people I have ever met in finance were also the most wrong. AI just learned that trick faster than rest of us. So here my whole wor- whole talk in two sentence.

First, almost every AI finance product is built to impress people for five minutes, and almost none are built to survive a room whose entire job is to not be impressed.

Second, and this is the part I promised the organizers I'd add, the exact same skills that fix your product is the skills that gets investors like me to write you a check.

Same muscle. I've proved both. And I'm telling this now, this week, because a lot of you are about to get pulled into exactly this. Your CEO saw a demo somewhere.

Your biggest cus- uh, customer suddenly has a compliance department, or you are three months from raising your next round. When any of those days arrive, I'd rather you to h- hear the hard part from someone who sit on the other side of the table, than discover them live in a room in front of the

people who bill by hour. A quick, a quick bit ab- about me. I promise this is the boring part, and I will keep it fast. Fifteen years of cross-border deals, Hong Kong, Mainland China, the UK, the US.

Mergers, IPOs, big strategic investment. On names you'd actually recognize, the kind of companies that go public and your LinkedIn feed won't shut up and about it for a week.

Along the way, I've sat in about two hundred investment committees, meetings. I've the [REDACTED:physical_attribute] to prove it. I checked. It's not genetics.

And here, the part that matters for second half of this talk, I've also read hundreds and hundreds of pitch decks, founders decks, bankers decks.

Forty-seven slide seed decks. I have seen fonts that should be illegal. [sighs]

Two hundred committee meetings taught me one thing.

No textbook says out loud, the number on the page is not what gets a deal approved. Trust in the number is what gets a deal approved. Money doesn't f- follow intelligence.

Money fol- follows trust, and trust is fragile, especially when the thing that wrote the page has never once in its entire life said the words, "I'm not sure."

Let me give you one small taste of what those rooms feel like. Early in my career, a very polished, very expensive banker present a beautiful slides full of confident wrong numbers.

One senior person in room asked one qu- quiet question, "Where does this number come from?" The banker paused for what felt like an entire fiscal quarter. The pause taught me more about finance than three years of exams did.

So I'm not sure as a-- So I'm not here as a builder. I don't build th- these systems. I sit across the table from them and from the founders selling them, deciding whether to trust them.

Today, I'm going to give you both halves of that, what breaks trust in your product and what builds trust in your pitch.

Let's define two machines that most everyone keep confusing. Machine one is a demo. One clean document in, one fluent answer out. Its the whole job is to make a room go, "Oh," for five minutes.

Machine two is a dem-- is a memo. The real document is a real committee reads before real money moves. Hundreds of pages, filings, transcripts, broker notes, spreadsheets, someone's rushed notes from a call last Tuesday.

Half the sources disagree with each other. And the memo's job is not to make your go, "Oh." Its job's to survive an argument. Basically, a family dinner, except somebody's uncle brought a spreadsheet.

Here's the everyday version of, uh, the gap. Ask your phone to summarize a long email. That's a demo. It's not just sound pl-- uh, plausible for ten seconds. Now imagine that some same phone has to stand in front of a bank and defend out loud why you deserve a mortgage.

Suddenly, plausible isn't enough. Now it has to be right, and it has to prove it. That second situation is what a memo actually is.

Now, you might think the demo world and the memo world never touch. Let me tell you about the most ex-expensive typo in history. February twenty twenty-three, one of the biggest tech company on the earth launches its shiny new AI assistant with a promotional demo.

In that demo, the assistant answers a simple question about a space telescope, and it gets a wrong, uh, the wrong answer. One sentence, one wrong fact about a telescope in a marketing demo, the market noticed.

The company's stock dropped around eight percent in a day. That's roughly one hundred billion dollars of value gone because of unchecked sentence. One hundred billion dollars for one sentence.

Nobody in that company asked the one question. Every junior analyst on my team is trained to ask before anything leaves the building, "Wait,

where does this claim come from? Did everyone check it?" So here's the punchline. Even the demo fails the memo test. The moment

real money is watching, and the real money is always watching, every sentence become a memo sentence. There is no safe demo anymore.

Keep that story in your head because of the same trust-breaking moment happens in six smaller, quieter, very predictable ways inside of your product every day. Let's go through them fast.

Six ways trust quietly breaks. Which source do you believe? Do the numbers agree? Do you hide contradictions or show them? Is that a, a fact or a guess?

Can you prove it in thirty seconds? And whose name is actually on the decision? Six. Keep count with me. I will keep each one short, and I will bring receipts.

Model one, not every source deserves the same trust, but most AI system treat them like they do. Think of like this. A number from an audit filing is your accountant speaking under oath.

A number from an analyst note is a friend at a party confident, probably from someone's internal email is a thing you overheard in a, in a elevator. Most retrieval systems can't tell them-- this apart.

They grab whichever text is close to your question and hand it over like a gospel. True story, anonymized. I know-- I once watched a, um, very expensive AI tool confidently quote a number from a group chat, someone's rough guess,

te-text six months earlier. The model loved the confident phrasing. The real audit number was the three rows away in the actual filings. The AI just liked the group chat version better.

It sounded more enthusiastic. If your system can't tell an accountant under oath from a rumor in a group chat, it, it is not ready for real money.

Model two, the numbers have to agree. Each other,

everywhere, every time. Here's a memo that already died. Page one says revenue growth,

uh, eighteen percent, eighteen percent. Page eleven, in a little table nobody reads for fun, says seventeen point four. Nobody in the room cares about the missing zero point six.

They care about what it, what it means. If this person didn't check the easy mathematics, what did they-

Not check on the hard stuff. That memo didn't pass,

not because of the number, because of what the number implied. And if you want the industrial strength version of this failure, remember the giant American real estate company that let algorithm to buy houses at scale.

The algo- algorithm was extremely confident about house prices. The house disagreed.

The company ended up writing off around half a billion dollars, shut the whole unit down, and let a quarter of the staff go. The model wasn't stupid. The model was unsupervised.

Nobody built the boring machi- me- um, machinery that forces the numbers to keep agreeing with reality after launch day.

Fluent and confident, remember, is not the same as right.

Model three, surprises people. A contradiction is not a bug. A contradiction is a gift. If the CEO says one growth number on the earning call and the official filing says the different, a different one, the gap is the single most interesting thing in the real story heist.

Real diligence lives for that gap. AI does the op- opposite. It is trained to sound smooth and helpful. So when it hits a conflict, it quietly picks whichever version reads nicer and moves on.

You never even learn there was a disagreement. I've sit through exactly this. CEO's number and the filing numbers

meaningfully different. Neither one, uh, nobody, nobody flag it. Everyone just used neither one.

We caught it because one person happened to have both documents open at once. Pure luck. Luck is not a control. Your job as a builder isn't resolve the argument.

It's to make sure that the argument happens in front of a human instead of quietly alone inside a box.

Model four, facts and guesses have to live in separate box.

And the fluent AI loves melting them into one smooth sentence. Example, the company will likely receive approval next quarter.

Reads like a fact, sounds like a fact. It is a guess. Somebody's best estimate wearing fact-shaped clothing. A committee's entire job is to agree with the guesses while trusting the facts.

If your system melt them together, the committee can't find them sim- seams, and then all, all they can do is to, is, is approve or reject the general vibe of the document.

You should not spend a hundred million dollars on vibes. I watched approval expected soon.

Turn across three drafts of a memo into approval received. Nobody lied. The guess just wore his fact costume a little longer.

Each rewrite until nobody remembered it stand-- it started as a guess. The approval did- didn't arri- arrive on schedule. That was an uncomfortable phone call. This fix almost embarrassingly cheap.

Label your guesses, a tag, a color, anything that survives being copy/paste into someone else slide three weeks later.

Model five, if nobody can find where a claim come from,

it doesn't matter how right it is. You've all heard about the New York's lawyer. Uh, he filed a l- legal brief written with a chatbot's help.

The brief cited six court cases, beautiful citations, prope- proper formatting, very convincing. One small issue, the cases didn't exist. The AI invested-- invented all six.

And here, my favorite detail, the part that should be taught in school. Before filing, the lawyer got suspicious, so he asked the chatbot, "Are these cases real?" And the chatbot said, "Yes."

That is like asking the guy who sold you the watch whether the watch is real. The judge fined him. The story went around the world. And my second favorite detail, the fake cases even had realistic, realistic sounding names and page numbers.

The AI didn't just lie, it just, uh-The formatting. It cited itself beautifully. Wrong, but beautifully. The lesson is a 30-second test. When someone points at a sentence and says, "Show me where this come from,"

you either click once and land on exact source paragraph, or you open seven browser tabs and start s- swiping. I have personally been the guy with seven tabs in a real meeting while the room full of people watched my scroll.

10 out of 10 wouldn't re- would not recommend. If you remember only one sentence from this wh- whole talk, the click-through is the product. Everything else is, well, written packaging.

Model six, my favorite because it's the most human. Someone has to sign.

Here's the story you probably know. An airline website chatbot told a grieving customer he could book a full-price ticket now and claim a bereavement discount afterwards.

That policy didn't exist. The chatbot made it up, uh, pu- uh, politely, fluently, confidently. The customer took the airlines to a tribunal,

and the airline's defense, this is real, was, was that the chatbot is, quote, "A separate legal entity responsible for its own action." That is the corporate version of my dog ate my homework.

The tribunal didn't buy it. The airline paid, and every one of us in a boardroom quietly took a note that day. You can't outsource accountability to your own software.

At the bottom of every real decision, a human signs. If your architecture doesn't have a findable human at the end of it, you ha- you have not built a product, you have, have built an excuse generator.

So build your AI around that accountable person, not instead of them.

Okay, the fix. Five things. Each one is a direct cure for a story you have just heard. This is almost word for word

what I'd demand from a vendor before letting their system near a live deal. One,

every claim comes with a receipt. Each sentence linked s- straight to its source paragraph with the source trust level attached, not a citation tab at the end.

Two, fact and the guesses stay visibly separate. At a glance at the page, I instantly see what's proven and what's somebody best estimate.

Three, numbers agree with each other automatically. The system refuse to ship a memo where the figures don't match. No human checking at 2:00 in the morning. Four, contradictions get surfaced, never smoothed over.

When sources disagree, the system raises its hand instead of picking the fr- friendlier answer. Five, a real human approval gate and is logged. Who's, who reviewed?

What changed? When they signed? That log is audit trail. Notice what's not on the list. A smarter model.

Not one of these is a bigger brain problems. All five plumbing and honesty problems. The winners in the, in this category won't win on benchmark points.

They will win because a tired, skeptical finance pers- f- finance person can trust their output at 11:00 at night without opening seven tabs.

Now the part I promised, the money. Many of you are not just building AI products, you are raising for them,

or you will be. So let me tell you what actually happens after you leave the pitch meeting. Your deck becomes a memo. Literally, literally, literally someone like me sits down and writes an internal memo about you.

Every number you said out loud gets checked, get, get checked against your data room. What, which means everything I just told you about the documents apply to you personally for license.

Okay, my time's up. Thank you. [clapping] [outro jingle]
