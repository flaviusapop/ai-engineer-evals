# Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler

Source: https://www.youtube.com/watch?v=dZgA6btnb_s

Uploaded: 2026-10-25

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Hey, thanks for coming. My name is Vinod
Ganesh. I'm the CEO of Kepler. We have a
few of my teammates here as well.
I'm excited to be here to chat with you.
So, the initial inception of this
session comes from the World's Fair for
AIE.
Where we discussed at a high level
Kepler as a whole and how we do what we
do. Um and our big claim to fame right
now and there's a new bunch of other
stuff is Anthropic did a full deep dive
into our architecture, our technology,
and the biggest question that I got
after the World's Fair presentation was
well, how do you actually do this?
Um so, our partners and friends at Turbo
puffer have given me this session to
talk about how we use Turbo puffer as a
component of this overarching ecosystem.
Um also shameless plug, Jack and I are
doing a talk on the main stage in about
25 minutes. So, we're going to power
through this and if you want to hear
about fundamental investing in the age
of AI, uh feel free to come to that 25
minutes from now.
Um so, to talk a little bit about uh so,
quick background of myself. Um again,
I'm Vinod. I'm the CEO of Kepler. Uh
began my career at Palantir. I led the
compute layer there. Um then built my
own data as a service company and then
was head of business engineering at
Citadel.
Um so, a lot of what we learned here in
building uh Kepler comes directly from
the experiences of understanding how to
build and harness or a substrate or
whatever the cool new word is in pretty
aggressive environments where accuracy
and fidelity matter pretty aggressively.
So, let's talk a little bit about what
Kepler does. Um I know we're um we've
been in a lot of places. We're excited
to be part of Gemini Force um blog post
today as well. Uh they've a new model
out. Um so, the core tenant is um, an
analyst, if you're actually working in
finance, you never show a client or your
PM a number that they can't explicitly
validate or trace.
So, when you see something like revenue
grew 12.4% to 418.2
billion,
these are actual numbers that need to be
correct.
The challenge is we're all operating off
of probability machines.
LLMs are at their core probability
machines. The same thing that makes them
so creative and cool is the same thing
that makes them very difficult to use in
mission-critical situations.
So, a natural thing you see is people
that attach sources after the fact. Now,
this is cool,
but here's the problem that happens when
you just attach a source after the fact.
First,
LLMs don't actually read your documents,
despite what many people think.
What they do is they chunk a bunch of
things together, they do a semantic
search, and they retrieve information
that may be semi-relevant, if you're
lucky.
So, the first big challenge a lot of
people have is we have the wrong source.
Like, we've pulled information from
Seeking Alpha or Venu's random YOLO blog
that says Palantir will be worth
$100,000 a share.
Or, we have the right source and the
wrong number.
For example, when you read a 10K or a
10Q, you can imagine a world where I see
the number 17.
Well, what does that correspond to? Is
it 17 million, 17 billion, is it 17
million yen, 17 million dollars? Is it
17 million
was the revenue of this company in the
year 2023 in the 10K that's in 2025?
Or, is 17 the page number?
Like, all of these things are
considerations that occur when we're
actually working on any kind of
environment that requires verifiability
or numerical accuracy.
Finally, there's a piece of mental math.
Growth rates, margins, multiples, models
are not actually doing
Now, in some cases, they write code that
does do math, but models themselves are
not actually doing math in a way that
ensures fidelity and accuracy.
So, what we end up
having to develop is an architecture
where the model sites the numbers, but
never writes them.
At its core and the magic that powers
Kepler is retrieval finds the right
source, thank you TurboPuffer, which
we'll talk about. Code does the math,
and code meaning the model is not
writing the math, but predetermined a
deterministic code that we humans have
written.
And we have a post-processing filter.
So, let's break this down.
So,
what we did is we processed the entire
corpus of SEC data.
Now, that's 30 plus million documents.
Um our friends at TurboPuffer will be
hopefully working with us fairly soon on
how we actually surface this to all of
you.
Um but we ran a pre-processing step, and
we registered what we're calling
citations.
And so, citations are effectively the
deterministic numerical numbers that we
have pulled out of filings. Things like
revenue numbers, things like an income
statement, a balance sheet, things like
MD&A that actually says, "Hey, my
revenue grew 37% in human-written text."
There's about 20,000 of those.
There's three individual filing facts
that we've revealed as citable anchors,
which effectively means our ability to
tell you where a number came from comes
down to the ability to be able to click
on a number and actually reference back
a core document where that came from.
When we're running in production, we
actually refuse citations that we can't
verify.
Meaning, if I have a number that's not
cited, the model is structurally
incapable of producing this output.
Finally, uh the number of citations that
the filter has correctly extracted, we
got about 21,000. I'll I'll through this
in a little bit more detail.
How Kepler works and the piece and
anthropic, if you want more information
Google Kepler anthropic, you can read
about is the language models themselves
are planning.
Deterministic software handles every
number or even more generally every
single fact.
So, let's break this down.
A user asks the question. The LLM then
creates a plan with full knowledge of
tooling, deterministic retrieval steps,
uh citation filter, bounding boxes, and
this whole thing.
Now, let's actually make this specific.
Let's say I'm saying, "What is the
adjusted EBITDA of, you know, Google?"
Think about what's involved in getting
answering that question. I have to first
retrieve a bunch of facts across 10-Ks,
arguably over potentially different
years.
I have to figure out, uh you know, in an
investor presentation and an earnings
call, what new information was disclosed
or if a restatement came out and now I
have to actually update a number.
All of that is what the model thinks
through.
From there, we have tools that actually
retrieve, compute, build tables, and
register this entire infrastructure into
a citation registry.
That citation registry is what allows us
to not only give magnitude or metadata
associated with numbers or facts, but
type those facts.
So,
a simple example here. Let's say I do
look at Palantir's 2025 10-K.
In there, it says Palantir's 2023
revenue was, you know, let's say a
billion dollars.
All of those numbers that I just said
need to be contextualized. That billion
dollars, even though it appears in the
10-K from 2025, has to be annotated and
treated as 2023's data point. I said
billion. Well, if you looked at a 10-K
or a 10-Q, it usually says one.
The billions is up in the table
somewhere far away floating around. So,
we have to somehow take these complex
objects and actually give them the
annotations to be able to pursue
meaningful and traceable output that's
actually correct.
Now, after the fact, models like saying
stuff. That is what they do.
So, what happens when a model actually
invents a number that we cannot
deterministically prove came from a
trusted source?
We have to have a post process a post
processing step to actually strip this
information out.
And so,
we do this and we give you the full
traceability in the most I'm going to
claim this and I think it's true in the
most granular form of any tool on the
market. Which means you can click on
everything in the Kepler platform and
I'll show you screenshots that actually
allow us to prove this architecture
works globally.
So, um let's talk a little bit about how
this works in the realm of Turbo Buffer
who's uh been nice enough to give us a
stage to have this conversation.
First and foremost, let's look at a 10K.
Let's say we see total net sales. That
fact that $416,000
$416,000 It's a good point, right? We
don't know what that means. That
$416,000
number um needs to have facts associated
with it. Things like a value, a unit, a
scale, a period.
Now, here's the problem.
For those of you who work in this space,
everyone can say XBRL solves all this
issue. We don't need to worry about
pulling information out of documents.
That's true if XBRL weren't incorrect
like some 10% of the time. But even more
so, how many people are just looking at
public information when they're making
investment decisions?
Fairly few. They have their own One
Drive, their own BIP sync, their own
various investment memos that they've
put together and a slew of internal
information.
So, for our architecture to work, we
have to work not just across 10Ks and
10Qs, but also on top of your internal
data, your SharePoint, your Box, your
Ignite, your One Drive, your Outlook.
>> [snorts]
>> So, we structure the data where the data
structured and then we implement search
where it isn't. And what that allows us
to do is create a namespace in
Turbopuffer that actually combines both
the BM25 and hybrid search with the full
guarantees of the Kepler platform.
Here's how we do it. And this is
probably the slide I know people are
taking photos. This is the magical
slide. I'm not worried about revealing
this because this is a very hard problem
and it moves quickly.
So we use
zero entropy so
zero embeddings we use 1280 dimensions
here.
ANN is approximate nearest neighbors
plus BM25 is how we actually grab
information across I look at everyone's
taking photos. This is amazing.
>> [laughter]
>> This is how we actually grab this
information across our namespace.
We do do reciprocal re-rankings to
actually make sure that we pull the
right usually 60K or 60 documents back
and then we do another form of
re-ranking.
And this is a trusted form of re-ranking
where we pull back the sources that we
actually trust more than others.
For example, different sources will have
different pieces of information that
claim to be the same thing. An earnings
transcript an earnings call transcript
where a presenter says
my revenue was this that disagrees with
exists in the 10K is actually a it's not
a bug it's a feature. There's two
different pieces of information I have
to actually deconflict across these. So
you need to be aware of that as well.
We use a cross encoder to actually do
the re-ranking and then we return that
result to the model.
This step in this process is predicated
on two things. It's predicated on one
our ability to rerun embeddings as new
information comes in incredibly cheaply.
So generating embeddings is not a cheap
process. If you can do it and you can do
it efficiently great but if you're
hosting your own embeddings model it
becomes unless you're hosting your own
embeddings model it becomes really
expensive and very difficult.
So strategy here is we search wide then
we re-rank.
Now there's tenant isolation that also
becomes really important.
Now, when we actually hit any kind of a
document, we have a bunch of different
pieces that are important. For example,
it would be very unfortunate if Citadel
Desk 1 saw Citadel Desk 2's research,
right? So, we have to have security
built into the document level as well.
So, re- The first thing we do is if you
start at that middle query that goes to
the document, um every hit is
reauthorized in Postgres, meaning we
check the citation, the value, the
document across every one of these
computations.
Every builder adds a new filter. So,
we're building up these complex filters
over time that actually allow us to make
sure that as we're querying information
and querying data, we're not leaking
data inadvertently across a bunch of
different sources.
Only Auth itself can create a scoped
token to actually create this
information. And of course, the user and
aura come from a signed device.
So, this is the way that we ensure
security, and this is the way that we
ensure your alpha stays within your
firm's ecosystem.
Alpha's an interesting question which we
can talk about in a world where everyone
has access to LLMs as well.
Cool. Now, how do we make sure a number
can appear in the Kepler platform?
First and foremost, we assign unique
identifiers to each fact in our
platform. Meaning, we need to have
identifiers that both can do entity
recognition and entity resolution.
Each one of these source IDs corresponds
to a bunch of metadata in a fact stored
in a in a deterministic engine.
In order for us to show you the output
in a way that's customizable, we need to
have a display value. So, if you want
your whole Kepler platform in thousands
of dollars or in yen or in any of these,
we need to be able to post process and
show you the actual output.
And we have to show you how we got it
and where we got it from.
So, the invariant in Kepler, you can
click on every number, every fact in the
platform and see the actual source that
we got it from.
And that's how we actually give you
numbers that are truly citable,
deterministic, and reproducible.
This is also the item potent guarantee
that we're able to give to people. By
having this guarantee, we can run the
same query over and over again wherever
and get the same results.
So, here is what we uh
have to deal with.
When we ran this whole corpus of data,
um a third of all of our citations are
the math that the model didn't do.
What that means is pulling every one of
these citations out, whether it's web
results, spreadsheets, whether it's
coming from a filing exhibit, the model
itself can make up a bunch of things
from its own corpus or its own um
training set that are really, really
difficult to work around, especially
when you go to historical data. For
example, looking up a revenue number
from 2005 likely lives within the
model's training corpus.
But it if we retrieve it from that
corpus, we can't guarantee that it was
pulled correctly from the right year and
right scope, and that we can actually
trace it back.
So, just off of a whole, a third of this
are math that the model
that a third of all citations are the
math the models did not do.
Now, how do we actually do this live?
As tokens move forward as we're flowing
kind of like we're doing inference, um
we give these filters and these
references to an LLM that has to
actually resolve these. Think of this as
the LLM dereferences the pointer.
We then have a registry where the
sources themselves are looked up, and we
pull information out of that registry to
give you the traceability.
Now, the really powerful thing here is
when we don't have a match, we strip
that number.
That's a very aggressive thing to do. It
means your LLM will not be that
wonderful thought partner that you
thought it would be, where it would make
up, speculate, and project.
This means at this moment, and I'll say
this, Kepler's not a super useful tool
if you rely on model hallucinations.
Meaning if you're trying to be creative
or you're trying to I don't know, write
marketing content, Kepler's not the
right product to use.
That means there are certain industries
in finance where opportunistically
selling, like banking, probably don't
rely on numerical accuracy because your
job is to sell an offering. It's not to
create a DCF that's backed by accurate
traceable information.
So, by checking against our sources,
we've effectively created a ground truth
retrieval engine across any corpus of
data, including public equities as well
as your own internal data.
Now,
this is annoying. This means the
platform cannot be as magically powerful
as many people want it to be.
So, how do we actually ensure whether we
should strip a citation or whether we
should try to repair it?
And so, the core insight here is we have
a post-processing step that actually
tries to do a citation repair.
Which effectively means if we find
information that we can't reliably
trace,
should we try to repair that and do an
on-the-fly agentic determination that
says this information came from this
source?
The answer is in certain spaces we
actually do do that. And that's probably
the second piece of this presentation
that we can keep a little bit, um, kind
of like wishy-washy, which is how Kepler
maintains its IP.
Cool. Um, now, when we actually run
these queries, there are some numbers
that I think are worthwhile to share.
Because most people in this industry
right now are wrapping a lot of
financial research with an LLM and
they're saying, "Great, everything is
right as long as things are, you know,
ragged properly, I should be good to
go."
So, our filter across native, just like
running it on Claude or ChatGPT, um,
refused 10,981
citations from our evals. Meaning 10,000
about, I guess, 3,810 of these were just
straight-up wrong numbers.
This is the scariest thing ever if you
live in financial analytics. This means
hooking up Claude to uh, uh or open AI
or any of these models to just a native
rag tool or a vector database actually
isn't enough.
Now, there's really cool things that you
can do if you're looking at just
semantic search and that's it.
But if you're looking at anything that
requires numerical accuracy and
auditability, you actually can't trust
regular rag platforms.
This is a scary thing for a lot of
startups that are effectively chat GPT
wrappers. I'm not saying that in a
negative way. It's the reality of where
we are right now.
So, a new kind of architecture has to
emerge and that architecture has to
combine both the auditability and
traceability with the deterministic
elements of of course like numerical
accuracy.
Um models don't do math. This is pretty
simple and I think it's actually pretty
critical um insight here. Uh anytime
that we see some kind of situation where
the model is
uh forced to do math or if it can't
reason through something, we effectively
make that impossible.
By having that post post processing
step, the model can't actually write
something it can't cite. Meaning the
model is structurally incapable and I'll
be careful. The platform is structurally
incapable of producing hallucinated
numbers. The model can still hallucinate
and it definitively does.
Cool. Let's talk a little bit about what
Kepler looks like and this is a tiny
sliver of what our platform does when we
show the deterministic traceability and
all that. Um happy to chat through uh
this as if it's if it's useful. But a
simple question like Apple's 2025
revenue and how fast it grew,
every number being clickable means by
clicking on these, you see not only the
10-K or the 10-Q or the 8-K or the
investor presentation that it came from,
but you see the actual calculations that
are done behind the scenes.
Things like I did these two numbers and
I have a 6.4%
um
increase all becomes present and
traceable on the platform.
So,
this architecture I think will become
the standard. Um,
the opportunity in front of people that
are building financial research tools or
operating in the realm of AI
is right now limited by the lack of
architecture that actually supports the
workflows you want to do.
You can set up fully managed agents
right now that try to ask for ideas
based on, you know, generated
information, but you still can't produce
a DCF, which is why we still have
analysts down the street from here or
working right now on stripping
information out of S-1s and taking
information from a PDF and putting it
into Excel.
Our goal is to end that.
And so, um,
I do want to end on a kind of one very
important thing, which is
our guarantees do end somewhere. We make
models site numbers, not write them. We
verify every citation. Uh, we push
arithmetic to the compute layer, not to
the model layer. We isolate tenants and
we measure recall.
This means we can actually guarantee
that the ground truth research that you
do in your platform is unique and
powerful. It does not mean that we can
create a full-scale hedge fund that's
replacing everyone, at least right now.
And so, I see the move, and we'll talk
about this in, I guess, 30 seconds as we
go, uh,
to the next place, but, um,
the move that I'm seeing is folks will
be more quantamental. This is the
future. This is the opportunity. The
more that we can use unique retrieval
mechanisms in conjunction with, of
course, deterministic retrieval, um,
we'll end up in a really powerful place
where AI can finally do the stuff that
we don't want to do instead of sitting
there and doing the ideating that we do
want to do.
With that, um, there's an appendix here,
but thank you so much. Uh, I appreciate
the time.
>> [applause]
