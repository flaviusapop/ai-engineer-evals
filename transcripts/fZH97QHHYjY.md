# The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev

Source: https://www.youtube.com/watch?v=fZH97QHHYjY

Uploaded: 2026-09-16

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
So great being here. Uh I'm Joe Bergam.
I'm the CEO of Hornet Dev and I'm here
today to talk about the unreasonable
effectiveness of BM25 for Agentic
Search. So how many of you heard about
BM25 before? Is it new or is it Well,
quite a few. So that's great. Uh I'm
also watching the World Cup. Norway is
playing there uh against the Ivory Coast
second half. Norway is leading so that's
good. So
yeah and at Hornet we are building
retrieval infrastructure for agents and
uh I've been working on search and
retrieval problems for a long time. As
you can tell I'm gray hair. Uh been
working in this space for more than 20
years. Um and in the talk today I'll
talk about why this kind of 30-year-old
lexical scoring function is uh making a
strong comeback.
First I will talk a little bit about
what I mean by agentic search or aentic
dribble and kind of define that for for
you all of you. Um
my definition is that agentic search is
essentially search inside agent loop. So
you have an agent that is trying to
accomplish a task, write a coding or
do some deep research or whatever task
and inside that you have some kind of
information need for the agent, right?
In order to get that task done
successfully
and you essentially need three things uh
to kind of build a good agentic search
system and that is you need a capable
model, a model that is able to use tools
and is able to formulate queries. You
also need a harness around the model and
how you kind of expose the retrieval and
the search functions to the model.
There's different ways to do that. It
could be through tool calling or it
could be through code mode. Um, Edo here
uh demonstrated what I call code mode
for exposing retrieval infrastructure.
So that's the harness part and you also
need uh a retrieval engine to be able to
do searches efficiently potentially over
billion scaled uh document sets
and to define BM25. So BM25 actually
stands for best match 25. So there were
some researchers doing plenty of
different experiments and experiment
number 25 turned out to be the best one.
So that's that's the background of the
name. It's essentially a scoring
function. So you can imagine you have a
query and you have a document and you
calculate some kind of score by
interaction between the query terms and
the document terms and you come up with
a score and you hope that this score
kind of is a good proxy for the
relevancy of the document with regards
to the query. Right? So one way to
calculate BM35 would be to take all the
documents and score each of them you
know and then figure out what are the
top K documents and then there's like 30
or 40 years of interest in how you
accelerate that type of retrieval top K
lots of different algorithms we also
invest a lot in that I'll show something
in this direction but BM25 is the
scoring function and there is a way to
kind of accelerate top K retrieval
Uh BM25 hasn't changed.
It's the same scoring function, but the
change here is really that we got a more
powerful user. Uh Edo talked about
general knowledge. The LLMs today have a
lot of general knowledge. They know
about entities, they know about
companies, they know about dates, they
know a lot, right? And by using that
kind of implicit knowledge that is built
into the parametric model, uh they
essentially become very good at search.
Um and that's the really change uh here
now that we're is kind of making BM25
more relevant
and BM25 used to be a kind of a baseline
function. Any information retrieval
research would include a BM25 baseline
and then you would put something fancy
advanced neural fancy stuff and then you
would compare it with BM25. I also think
it's interesting in how we evaluate
search before because you will simply
look at 10 blue links and you like have
scan it and you compute some metrics. A
lot of that is now going away because
the agent is not really it's kind of
powerful in the way that it can type out
a lot more queries than a human can do.
So it's less relevant to think about
evaluating these systems just by a
single shot query.
And this is one of my kind of favorite
benchmarks out there. I like to talk
about benchmarks. So browsecom plus is a
deep research benchmark [snorts]
uh published in a paper last year and it
has almost or exactly 830
questions. These are riddle like think
about it like a pub quiz. Do you have
pub quizzes in the US? Yeah. Okay great.
So like kind of a riddle type of
questions quite long and the agent the
harness of this kind of or the protocol
of this benchmark is that you have a
model and it gets a very simple tool
called search and it accepts a query
string and you return some snippets back
to the model and the corpus is about
105,000 or 100,000 documents. So that's
kind of tiny and these are web documents
and the end to end accuracy. Um all of
these questions have a golden reference
answer and you can kind of check if the
model and the entire loop produces that
exact answer.
Um but why kind of why do we need
retrieval?
I like to compare context windows with
floppy discs because I'm old in the 80s,
right? We install this kind of games on
our computers using floppy discs. So one
kind of you guys are so young so you
don't probably have this kind of
nostalgy but one floppy disc could fit
about 1.4 megabytes of data
and the current models before they start
degrading in quality that's I in my
opinion around 350,000 tokens. So that's
one floppy disc of data right. Um, so
you need retrieval in order to to fetch
the information that you actually need
to put into the context window
and browse plus really demonstrate how
uh retrieval quality affects the end
toend accuracy of the task. Right? The
endto-end accuracy here is essentially
is the model equipped with this search
tool able to answer the question, right?
the riddle like question
and if you artificially just stuff the
evidence documents that is needed to
answer this question into the context
window of the model the accuracy is
really high right so reasoning is not
the bottleneck the model given the edit
evidence up front answers the question
with a very high accuracy rate even GPT4
um but if you expose the model with a
harness with a retrieval tool. That
accuracy falls because it now depends on
the harness. It depends on the model's
ability to formulate queries and the
retrieval quality of the retriever.
Um so for me this is also quite
important because even if we get perfect
models like models that are kind of agi
you don't have to append make no
mistakes you still will be limited to a
context window that is approximately a
floppy disk right so you have to decide
what goes into that context window and I
think retrieval is still very relevant
as the previous slide showed
and in this browsecom plus data set one
of these riddlelike questions become a
search trajectory because the model
execute a query, gets some response
back, reads it, reformulates the query
and continues until it has kind of
filled up the context window or found
the answer, whatever comes first.
And we spend some time to investigate
these trajectories
uh to see how GPT5 is formulating
queries and we found a lot of
interesting aspects with that. Uh we
described it in a recent blog post as
well. You can find it on hornet.dev.
And we like to compare it with a AOL
query log. So AOL AOL was like a service
back in the day had some search
interface and they accidentally
published
um a very large sample of what people
were searching for on the web and they
were quite short and I have seen more
recent query logs as well and the user
human pattern are still searching with
just a few terms. GPD5 on the other hand
it's a much more powerful user. It has
the general knowledge and it can like
bam write out very long queries. It can
use a lot of syntax operators that are
kind of useful from it has learned from
web search. So site operator phrases
etc. And this is a new type of workload.
And on BM25,
BM25 has essentially two hyperparameters
that controls various aspects of the
scoring function. And I talked about
having a baseline and BM25 is usually a
baseline and browser comp plus as well
has a baseline with BM25, but it turns
out that that baseline is terrible.
So when you look at fancier techniques,
embedding models, what have you, um it's
stands out as a much better retrieval
paradigm than BM25 if you look at the
original paper. But more recent research
shows that the parameters that were used
in the browse comp plus research paper
was not really adequate to handle these
kind of long documents. So I like this
which BM25 do you mean? uh because it
has a quite dramatic impact on that
specific config benchmarks on the
overall accuracy
and why is BM25
now more powerful with the new user. So
I mentioned the general knowledge of the
user and that he can type faster and
more be more specific as a more powerful
user and exact matching is still
relevant right because the model knows
names entities uh zip codes uh skus what
have you that is not so easy to
represent with an embedding model which
kind of encodes all the tokens into a
fixed vocabulary. Uh it's also
relatively cheap especially if you take
into consideration the cost of doing
embedding inference right some of these
embedding models have like 8 billion
parameters and you encode text and you
have to stand up infrastructure for this
and what have you. So it's quite simple
and also the tooling uh in the overall
ecosystem is quite good. Um,
so it's it's readily available and it's
also very easy for the model to inspect
the results and understand why a certain
query formulation returned the result it
did, right? Because you're matching
literal terms and phrases and things
like that which can help it kind of
reformulate the queries.
So these are the three key things
and now into more hot topics on like
what is all you need. Um and this is a
very recent research that came out from
Waterloo from Jimmy Lynn's group up
there. They are doing a great job at the
information retrieval research and also
on agentic search. They have a recent
paper that I love. Uh it's called
scaling direct corpus interaction via
dynamic workspace expansion. So I'll
spend some time on expanding this. So
imagine you want to stand up web search
infrastructure for agents. A lot of
companies are doing that at the moment.
We are also working with some of these
companies to help them build
infrastructure for powering that kind of
use case. And there you have potentially
billions of documents,
right? So that doesn't fit into the
context window. So you obviously need
retrieval and BM25 is a good baseline.
So you can retrieve information over
that. And the result of this is um you
can imagine this as a search engine
result page SER for agents because you
can place these documents that are
retrieved from the retriever into a
workspace.
And if you organize this workspace as a
file system, you can uh play into the
same things that you have around skills.
You can have progressive disclosure
because you can have the document like
the title of the document and a small
snippet of the document and expose that
to the model and the model can then also
decide oh I need to read more of the
document and when it's doing that it can
use all the primitive tools that it's
really good at using you all use coding
agents so you all seen GP and rip gp and
said and whatever it's doing to kind of
manage context so here you get the
benefits of both worlds and also So you
get to combine sandbox infrastructure,
retrieval infrastructure. So and VFS and
just bash and whatever. So it's also
quite exciting, right? Because it
combines all of these new type of
paradigms that is happening at the
moment. So I'm really excited about this
type of direction. And it's also kind of
a hack, right, to optimize for what the
models are good at at the moment, right?
Because all the frontier LLM companies
are optimizing their model for cool for
coding, for bash, for tool use. So if
you put your kind of end to end task on
the trajectory of that you kind of
whatever there's a new model you know
there's going to be better at this as
well right
so might be that when we get AGI they
can just use the browser we'll see but
currently this is a very powerful way to
to build uh retrieval infrastructure and
a whole agentic search experience
and when it comes to evaluation right I
talked about this earlier as well. In
traditional information retrieval, we
were used to having just one query, one
rank list, compute NDG and compare it.
That is no longer very relevant when the
new user is agent because that agent can
reformulate queries and do more queries
and do expansion and all kinds of
different stuff, right? So, a lot of the
classical information retrieval
evaluation is now kind of dead.
instead look at like see if the model
can perform the task it's it's set to
and for example for question answering
does it get the answer right
and we at hornet we are betting on BM25
as one of the primitives and we have set
out on a vision to kind of have the best
most efficient way to evaluate uh BM25
because I think it's such a strong
fundamental primitive And this
illustration compares some anonymized
engines comparing with Hornet on the
same type of same type of hardware with
um web documents, 100 million web
documents on a single node. And as you
can see, Hornet has a much more
efficient implementation than the other
engines and can do more throughput for
the same type of bucks, which for a lot
of companies that are building
infrastructure at the moment for web
search etc. means a lot in savings.
>> What is the yaxis?
>> The y-axis is QPS. Sorry.
>> The Y axis is Oh, sorry. The Y axis is
latency. I'm sorry.
So, four claims to take away from this
talk. There's a new user.
It's more powerful. It's able to type
faster. It's able to read faster. It's
able to reformulate queries and it has a
lot of general knowledge which makes
simple tools like GP and BM25 more
powerful.
That's number one. Number two, which
BM25 do you mean? Uh there are
differences in implementation, in
performance, in parameters. So think
about that.
And also why is it effective for agentic
search? It's simply because it's
explainable for the model. So the model
can see and also use it in combination
with GP, right? Because you have literal
matches and GP is almost about literal
matches as well. And the combination of
these two is a very strong agentic
search or agentic retrieval paradigm.
There's a lot of references. I think I
will publish a talk uh or the talk will
be published and also the the slides and
if you hated it, you can
tweet at me.
Um there is not I was told that there's
not a room for for questions but happy
to chat about retrieval. You will find
me around the conference. Probably best
way to reach me is through my ex account
and that's it.
