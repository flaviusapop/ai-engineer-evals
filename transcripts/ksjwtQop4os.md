# Vector Isn't Enough: Hybrid Search & Retrieval — Jeff Vestal & James Williams, Elastic

Source: https://www.youtube.com/watch?v=ksjwtQop4os

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Thank you for coming. Uh my name is Jeff
Estle. I work at Elastic. I am a AI
architect. We picked a new title this
year so make it relevant. This is James.
You want to introd yourself?
>> Yeah, I'm James Williams. I'm a uh
solutions architect focused on search.
So, I help customers with all the
technical stuff you're about to walk
through today.
>> So, this is a very hands-on, as in I do
not intend to talk much. I've been
talking a lot lately on the road, so
we're going to have me not talk a lot.
Um, you're going to go through hands-on
stuff. I will say in the upper right
corner, you'll see that short URL. Um,
it's a ELA elastic. This is the workshop
environment. Um,
quick note. So, they never told me how
many people were coming. So, I took a
random guess of 75. Looks like I
undersshot a bit. So, there um 75 of you
will start up pretty quickly. The other
handful that are a little slower on the
on the trigger here. It's just a few
extra minutes to start up. Um but
basically, this is going to take you to
an instruct environment.
And then I'll give a little intro. I'm
just giving this spiel while it goes. Um
we'll go to
this. You're going to go here and then
you'll hit start and that's going to
spin up an environment for you. So while
that's doing it, um, so how many people
are familiar with Elastic, the company,
Elastic, Elastic Search. All right,
pretty good. It's good turnout. Um, and
how many of you have used Elastic to
build a like a a ragbacked
application, retrieval, augmented
generation? Great. How many of you are
sick of hearing the term rag from the
past two three years? Fantastic. I know
I said it about a thousand times at many
conferences and um my boss who no longer
works here actually used to get really
mad when we keep bringing up rag. Now
the thing is um return a meant
generation didn't actually go away.
Luckily it just kind of fell to the
background. But as agents got more and
more uh capable and you know effective
they just kind of took over the
management of being able to you know
retrieve data and and analyze it. So the
models are getting certainly smarter and
smarter. Um you know Fable came out for
a minute and teased us and then ran
away. But um there's still a a need for
pulling in information into these models
be it you know things that are time
based that change proprietary
information um price data anything out
there that the model hopefully hasn't
been trained on whether they tell us or
not. Um but there's a need for that and
so that's where things like elastic
search come in. It's the retrieval layer
that helps make these these agents very
capable. And the the trick or the catch,
I guess, is if you feed these models, no
matter how smart they are, garbage data
and you confidently tell them this is
the answer, pretty much they're going to
believe you because that's what you're
telling them. So, we want to be able to
give accurate information and and give
it. So, this is kind of what this
workshop is about. I'm sure there's 20
other workshops that explain how to
build agents and I we actually have some
too if you want to go to our website but
this one's going to talk to you kind of
remind about um vector search semantic
search why it's important where it's
useful but also where it breaks down and
then we'll go into um the kind of
lexical search BM25 so that's that
keyword search we've been doing for for
decades um where it's still relevant
today and useful and then also again
where that kind of breaks down and then
putting bring them together into hybrid
search. So, being able to kind of get
the best of both. We'll do combinations
with uh RF, which is an out of the box
combination. And then we'll do some a
little bit more advanced um linear
combination where you can tweak those
balances a little bit. And then should
you have time, we'll actually put it
into um a little bit of Elastic's agent
builder platform where you can see what
happens if you retrieve bad information
and tell the agent it's it's good, it'll
doesn't work. I mean, it works, but it
gives you a bad answer. And if you give
it the correct answers and things like
that, um should you be very quick and
get all the way to the end, there is a
bonus um one about um sorry, rerankers.
So reranking where it comes in useful
that um the workshop is kind of
basically four plus a bonus um chapters
challenges. Each one has two parts.
There's the part in the dev tools
console where you just run API commands
within Elastic Search. Um each one of
these environments if you're in it and
hit start and everything, what's
happening is a serverless instance is
being spun up for you. Um and then
you'll load some data. It's a small data
set, you know, it's a workshop, so
nothing crazy. And um you'll run the
kind of the the short version of each
one of these in the dev tools console
and then you'll hop over to a Python
notebook tab and you'll run the more
in-depth one. What I would say is I'm
going to stop talking in a minute and
let you work on the workshop and then
every 20 25 minutes we'll kind of check
in and see where people are at. I'll
tell a little summary about the the cha
the chapter challenge you're at. Um, to
get the most out of this workshop, I
would definitely spend time reading
through what's in the the Jupyter
notebook, especially it kind of talks
about why the documents come up in the
orders they are and how to tweak it and
how to tune and why it's important. Um,
if you just blindly hit run all in the
notebook and fire through, you'll be
you'll be done 10 minutes. But if you
actually spend through it, it's going to
probably take longer than this workshop
session. So, um, with that, I'll let you
get started. So, some of you should
start up right away. Some of you will
take a few more minutes in the meantime.
Is anyone actually started? Sometimes
you take a few minutes. That's the
thing. Yeah,
>> we got it.
>> Okay.
>> And if you get stuck, raise your hand.
I'm basically the runner. So, I'll check
out what you've got going on on your on
your system and and and potentially help
unstick you if if it's something
trivial. And if you have any questions,
feel free to raise your hand. happy to
provide a little bit more detail about
what's going on in the exercise if um
you're looking at something and you're
you're a little bit confused and want
won't want won't want won't want won't
want won't want won't want won't want
won't want won't want won't want to ask
a question there
and this is all also available um in a
repo that should be public yeah I made
it public um so you can run the
notebooks
um outside of instruct either after or
or whenever if you want
>> kind of glossed over this But the one
big thing that I think has changed with
rag over the last year year and a half
is some of the data providers for vector
database and we're in that in that
bucket have brought inference into the
vector database. So you will see
embedding generation happen within
elastic search serverless. We have an
inference service called Elastic
Inference Service. Very um creative name
that powers the models that are being
used for these workshops. So we've got
GINA models from from an acquisition
that we made. So we actually do our own
model development now. And um and it's
focused mostly on dense vector models
and re-ranking models. So you're going
to get insight into some new tech that
wasn't part of Elastic Search a year
ago.
That's that's all I have to add there.
>> We've heard of chunking.
>> We do we do we do help with chunking. So
yeah, we can answer this and feel free
to jump jump in. He's the manager of the
search specialist team. I just wander
around. Um so as James mentioned the we
have you know the text field semantic
text in elastic search. So there's a
couple ways to do this. Semantic text is
kind of the automatic easy way on road.
Um, so by default we will chunk on
sentence boundaries and break into a
certain amount. I can't remember off
hand what the number is
>> 250.
>> There you go. And so that's you know
configurable. So by default breaks on
sentence you can break on word
boundaries. You can change it. Um the
the Gina model that James mentioned we
you know part of Gina now or Gina is
part of us whatever. Um it has a very
very large context window but you're not
always going to want to fill that for
various reasons. Um, and so you can
configure chunking down to the word to
paragraph, page boundary, things like
that.
>> We have a semantic mapping field in
elastic which basically takes a piece of
text and chunks it. So if you send us
five pages of text, we're going to chunk
that into 250
token chunks with one sentence overlap
and store that in the in the system for
retrieval. There are frameworks that
talk about semantic chunking and there
are other labels for what I will call um
large context window chunking. We
actually and and this is talked about in
the lab in the later sections. We do
have a technique that we use called late
chunking that can work on large context
windows that is not exposed via elastic
inference service yet but it is
something that the GINA models do
support. That's the closest thing that I
would say we would have to semantic
chunking. But we don't really have a
need for that construct because the
semantic text field itself uh allows us
to deliver the same thing you would get
with semantic chunking just by chunking
the data and then and then running
searches across it um in a you know in a
semantic flavor and you you'll get
exposed to that in a lab. So we would we
would solve the problem with traditional
chunking and hybrid search, not any
exotic semantic chunking scheme.
>> You're welcome.
>> All right. Yeah.
>> Yes. So I made it available for a week
because I know how things go. Um so it
is available for a week there. Um,
and
this isn't a this isn't anywhere. Um,
I the workshop is in my repo for better
or worse. Um, and so the
the notebooks are all in here. So if you
if you want to run just the notebooks,
um, you know, you can hook it up to your
serverless cluster or any kind of
cluster should should work that has
semantic text in there. But yeah, the
the workshop itself is good for a week.
And where was I?
And yeah, so like I mentioned, the the
first part the first half of each lab is
this dev tools where you run a mapping.
The left side is the input for your API.
The right side is the output. And then
you'll get down to part two
where you pop into the Python notebook
and it'll automatically connect to the
um the Elastic Search environment that
spun up for you.
I see they're letting folks in as as
folks kind of go out to make sure the
room is still full. Um
the top right hand corner is really the
URL that you want to hit. That's where
all the workshop content is. And then
there's a second URL that is the source
code repo for all the notebooks for the
workshop today. Those are the two most
useful resources. So if you're coming in
and you haven't fired up the workshop
yet, top right hand corner and then the
bottom right hand corner if you're
interested in the Python notebooks that
power the content that you're walking
through today.
I'll probably repeat that message every
time I see someone walk in.
That is a really good question and I'll
repeat it so the other folks can hear it
but is is a major point of this um lab
sequence to let you know that VM25based
search which is traditional lexical
search we've been doing for a long time
and dense vector semantic search do
those two things need to be put together
to form hybrid search that is the core
thesis right now that we have as a
company and the only thing that we add
to that well obviously that that's of
value is the option of adding rerankers
on top of that but yes that is a core
thesis we're firm believers in that
approach and that's in line with
everything that I've seen since before
even joining elastic even if you're
using a dedicated just pure vector
database you often have to pair that
with some other retrieval system and do
the equivalent of hybrid search. The
advantage to elastic is and you're
seeing this in the labs. It's one API
call. We handle all the inference that
happens from ingest chunking to
real-time search where the query gets
translated into a query vector and we do
all the work for you under the hood. And
that's what we we consider that of high
value especially when you're talking
about largecale use cases where latency,
accuracy, tunability matter.
They are configurable. The chunking
settings, are they configurable? They
are. The documentation has insight into
how you can change them and what chunk
settings can be changed. So, we've got
very detailed um API docs that walk
through that. Uh they're not described
in detail in the workshop, but if you go
to the elastic docs, you'll see what the
what the configuration settings are for
chunking. And some of our customers do
bring their own vectors and chunk on
their own. We support that through
standard um SDKs. So if you're using
Python, Java, Net Core, like pretty much
any TypeScript, any modern programming
language, um you could still use Elastic
in the format for these workshops.
You're just doing more work as a
developer.
>> And so I'm sure people are moving along
and you can continue on as at your own
pace. Um, like I said, I'm going to
check in every once in a while and kind
of talk about the the labs a little bit.
So, the the first one, right, the the
whole point is essentially this little
chart right here talking about how
vector search works and and semantic
search and what you're getting it. And
so, when
when you use an embedding model that's,
you know, hooked up to Elastic and you
know, we talk about Gina as the out of
the box one, but you can certainly bring
your own. You can hook up to other
inference services. um we just make it
easy for you to get started with Gina,
but certainly bring your own and use
semantic searches or semantic text as
well. But the the nice thing about this
particular way it sets up is you know
when you create an an embedding at query
you know at inest time you create the
embedding from your your document but
then at query time you need to use the
same embedding model to do the query
time otherwise it's you know like me
trying to speak Portuguese it would not
go well. Um so by when when I started
when we started doing this a few years
ago um in the early days early um you
know you had to keep track of the
inference ID you had to keep track of
the model and then the model you know
then you have developers all and you
have to like make sure everyone's using
the right one and there's all this
things. So by embedding it in the ID in
the uh field itself it helps on two
ways. one, you only have to set it once
and as the person who's setting up the
index, um, you know, there might be
other people using that same index to
ingest their own data or query it,
right? So, you can set that up once
again, whether it's the Gina model or or
some other model. Um, anytime you use
that field, it just becomes like another
field. You just either send data in or
you query it. So then at query time,
what you're seeing up here is um the
text comes in. It may or may not get
chunked up depending on the the size and
settings. It goes to the um maybe the
elastic inference service which is
default out of the box. Maybe goes to
another inference service. That's fine.
And then we generate the embeddings and
we then pass it back to elastic to do
the um HSW&N. We do have other discount.
We have disk ANN but by default we're
using HSW the hierarchical navigable
small worlds graph. um basically just
allows quick traversal to find nearest
neighbors of of relevant documents and
then you get back your top k five 10
whatever you want documents and that
allows you to ideally if everything's
working well find documents or you know
chunks that are semantically similar to
what you're asking and as you learned in
the lab it's not the exact keywords it's
the idea of what you're asking so if if
all of us in this room ask you know how
to set up security on, you know, TLS on
elastic search or something. We're all
going to phrase a little differently,
but the idea is all the same. And so
hopefully you get back the same
documents.
And you kind of saw where sometimes that
breaks down.
Um, one of the key places is if you have
a very specific keyword, um, certainly
if you have a keyword that is not a word
like a product ID that has makes no
sense, it's very specific, um, semantic
search then kind of falls apart because
it doesn't really need that. And that's
what the second lab is where bringing in
um, BM25, lexical, keyword filtering,
and all the other traditional so-called
search uh, methodologies we've been
doing for a long time help can augment
that. And so I'll give you I'm sure some
of you are progressed past that one, but
I'll check in in a few minutes and
review lab two. And again, if there's
any questions, feel free to ask,
>> right? Page. Yeah. Paging. So if you
have like a hundred results, you want to
get back 10 at a time. Is that is that
what you're asking for or
Oh yeah. So you can do that. There's um
I forgot the the exact thing, but
there's a basically essentially a
checkpoint ID. And so then it it
continues on. And so yeah, you're not
researching again. You're not rerunning
the search for that part. It goes on. So
you can that's what our pageionation API
part does. So if you know that's a
possibility, you use that and then we
send you that key and it's basically
like this is where you start and
continue on.
>> I think the official label for it is
point in time. There you go. If you're
looking in Elastic Docs, uh just you
search for point in time and it shows
you how to use point in time to do to do
just that.
>> Oh, good question. Um so the the summary
field is generated just for this
workshop and it was generated by an LM.
It it's not exactly part of it. The real
reason is when I first ran through this
and you print out the whole body field,
it was way too long and it was
cluttering everything up. So just having
this little summary field. Now that
said, you can use like for example an
ingest pipeline in elastic search and
make an inference call and say I do want
to generate a summary of of this you
know document or I do want to pull out
the possible queries that could do that.
So you can do that on uh ingest. It's
just for this particular thing it was
just to make it easier. But so the the
vector field you're searching is is the
title. Yeah.
>> And as we get deeper into the labs, we
don't use that that construct, but there
is LLM completion API calls in in the
later labs that it would be the exact
same thing. You just wired in your
ingest pipeline
>> question.
>> It's a great question. So when it comes
to work that we've done to make HNSW
more efficient, um that started two
years ago actually two plus years ago
where we introduced int 8 quantization
which I still I think is still the
default. So by default we're going to
take float 32 vectors and quantize them
before we store them in memory. We still
we still keep the full vector um but
we're only storing the quantized vector
in memory. We also have uh BBQ which is
yeah and we got a blog that talks about
BBQ. This is a little over a year old
maybe even a little bit longer than a
year old where we've compressed the HNSW
um graph vector that we use even more
all the way down to uh basically a bit
and and there's sophisticated stuff
under the hood that supports that and
still keeps the recall high. And then we
just introduced disk BBQ which pretty
much eliminates the memory overhead for
um for vector search. The only uh
difference I would say between disbel
as the underlying mechanism for search.
Um and then and the newest form of that
is disbrietary
to elastic. No one else implements that
[clears throat]
graph-based search. You want to take
that one? [laughter]
So, graph based search. Uh, so to be
fully clear, we are not a graph
database. There are some very specific
graph databases. Um, graph has its
place. It usually has a lot of overhead
to keep and maintained. If you do that,
great. Um for the vast majority of the
people though it's we find that it's not
really needed where the ability to
especially with quantization where you
can search across large amount of
documents quickly. Um now especially
with the agent world too where you can
do multiple queries in. So you can one
of the labs later on it does a couple
round trips I think just two as an
example but you can go in get your kind
of first phase get a sample of documents
and then see oh okay so they're all
related to this tag and then go
searching. So that's where things like
filtering and um some of our other
search methodologies help. Um and so
yeah, I mean I just it comes up, but we
haven't seen it, you know, too often as
an actual blocker where you have to set
it up.
>> And and the last thing I'll say about
that is what we see is far more common
is um machine learning models that do
classification on the fly, which is
another way to solve that graph
challenge. works in some situations, not
not in all, but Neo Forj and other graph
databases have been around for a long
time. I don't know of any that scale
really well, and we're trying to target
multi-billion vector data sets, which
means that um we're very careful not to
not to intro introduce a construct that
keeps us from being able to scale at
that level. And we we we haven't found
the need to go there yet, although it
comes up a lot. It was a big theme last
year at this conference. I remember
being here and seeing graph rag was was
heavily talked about, probably will
continue to be. Um,
I haven't seen a technology nail that
yet.
And maybe there's a Neo Forj person in
here that would contest me on that and
say, "No, no, no. We have it figured
out." I think they do, but not at not at
the scale that we operate at.
>> Yeah. Oh, so you came from their
session. Nice. Okay.
in the back.
I think the question was we can use
classification models to uh um to
achieve some of the same results you
might get with with a with a graph
traversal. Um so we have the concept in
elastic of running uh machine learning
models in in elastic on what we call ML
nodes. um you could basically upload
whatever classification model that
you've identified that works and wire it
into elastic that way. The other model
the other option would be to create your
own model that you have your own
external inference to and and
potentially use that um in place of uh
of our ML technology and I'm hoping that
we'll introduce more sophistication down
the road in that area. But we don't have
anything noteworthy to announce right
now. We're focused on taking the genome
models that we have and pushing the
limit to what we can do with handling
unstructured data and and dense vector
embeddings and rerankers. We'll probably
end up pivoting off of off of that once
we nail the um the reranking piece and
and the and the dense vector models that
are that are in development and you know
doing quite well in the market.
I'll add in too that along with that so
there's classification models and you
can also run things like NE models name
entity recognition so you know if you
pull out the entities if you're trying
to identify person location um business
names things like that or product names
you can run those on the fly as part of
a you know part of the query where you
as the the query comes in you run it
through the ne model and ne models are
very fast because they're they're small.
They're really small models and you pull
out these entities and then you know
again now with agents and things like
this you don't have to wire up crazy um
painless scripts the agent can take
those and then create a query that's
more tuned for that. So there's a lot of
ML capabilities that we don't talk about
as much as we used to because again like
Jim said we kind of pivoted to focus on
other things but they're still there in
the stack and very capable
filtering in that's great.
What's up man? Um one of our
distinguished essays over in the corner
can ask him all our questions. I'm gonna
now redirect. Um for the people who came
in aside from Sneil, the upper right
corner is the short URL for the workshop
and you can spin that up. It opens up a
kind of lab for you lab environment and
also spins up a um elastic search
serverless cluster all set up for you.
So feel free to run through there.
So, there's um
there's one main knob for reciprocal uh
uh RF and it is and I'm I'm spacing out
here off the top of my head. I do not
know. You're you're pulling it up.
>> I don't know if we expose it in the in
the RF um
attributes for the retriever.
What's the default constant
>> constant? The rank constant. I It is
something that you can configure. Um I
don't know what the range is.
>> That's what lab five is the optional
one. It's all about
well lab five is rebranking. RF is in
there somewhere. Um sorry brain melted
for a sec. Um it's in there somewhere
about talks about what what Sil's
talking about a little bit more example
and you can change things like that. So
>> So I don't know did that answer your
question?
>> Okay cool
>> fire away.
That's a great question. There's
actually a table that kind of explains
some of those decision trees in the
later workshop. I want to say workshop
number four. But the short answer is for
a small document corpus and and and my
rule of thumb is always see what you can
accomplish with a combination of BM25
and semantic search. If that gets you
the recall or precision uh target that
you're looking for, whatever relevance
targets you have, stop. Anytime you add
anything on top of that, you're going to
be taking on an additional latency hit.
Only do that if you need to. And the
next uh you know extension point would
be to um to use a rebanker model and um
and then it's just a matter of picking
one that that you think is going to work
best for your corpus and doing some
testing and validating that it moves the
needle enough. Um that would be kind of
the standard happy path approach. There
are some folks that would change that uh
recommendation slightly and and say look
just do BM25 just regular search um and
and then and then add semantic search if
it's not um relevant enough but I'm a
big fan of dense vectors so I would just
go ahead and wire them into the
architecture right out of the gate and
uh that way I don't have to worry about
things like you know you you you get
into these weird situations with lexical
where you're starting to add synonyms or
get into advanced um lexical tuning
techniques that you might not need if
the semantic search is able to to pair
well with a lexical search.
>> Welcome.
All right, so I know people are moving
along which is great. Um just give a
little wrap up on lab two which again
was about your favorite be lexical
search. Uh but hopefully you did learn
uh you know get across the point that it
does it does have its its points. Um, we
just barely touched the surface on
Lexical because, you know, for 15 years
or so, you know, a dozen years at
Elastic, that's what we had. So, if
you've ever been on the Elastic Search
doc sites and you go to the search part
and you click on the search API, there's
an insane amount of ways to change and
tune and tweak lexical search. Because
to James's point, before we could do
semantic search, we had to do all these
uh crazy things to get relevant search.
Um luckily now we don't have to do quite
as much, at least usually once in a
while still. Um but with lexical search,
you do it does have a it's its point. Um
but it does tend to break down um
anytime you break out of looking for
very specific keywords or a very
specific phrase. Um the upside of it is
it's I mean I don't even want to say I
was going to say it's generally faster.
Although now with quantization things
like that that's not always the case but
um by default it's kind of faster. So um
in lab three
most people are probably along there but
you move on to combining them.
And I will say that even though I'm a
big fan of dense vector search that
lexical search usually does have lower
latency profiles in almost all use cases
and that's because there is no ML
inference happening. So anytime you go
semantic search with with dense vectors
you're introducing um a call to um you
know an inference endpoint and more
often than not that inference endpoint
is going to be more of a bottleneck than
the rest of the system. And that's
another reason why we wired um the
inference into the into the data
platform because when you're doing
endtoend testing, it doesn't matter if
your vector database returns vectors,
you know, really fast. If the inference
that you're depending on is slow, then
your search is going to be slow.
I think that's a question that is
shapeshifting as the data platforms wire
more capability into the systems and
these models improve the um and every
vendor is going to have their own
specific take. Our take is that
everything starts with traditional
search which makes a lot of sense given
our heritage and then you add semantic
capabilities on top of that and and then
you layer in re-ranking if you if you
need to in terms of where that stuff
happens. That's where the devil's in the
details. As as a developer trying to
build an architecture around this stuff,
your options are are quite vast. And
depending on the stack you start with,
you're going to have perceptions of what
you should be doing in the data platform
versus what you might have some sort of
middleware around it that that is that
is wired up. And and I'm using the word
middleware kind of loosely, but there's
a whole application runtime construct
that's went away ever since this this AI
boom started. that is going to have to
come back and it's either going to land
in the data platform itself where we're
doing inference and some of these other
things you would normally have to
coordinate with these external services
or um there's going to be you know
platforms to try to try to accomplish um
that and then use the data platform as
just kind of this thing that you plug in
and I'm thinking about like old school
stuff like back in the old days when I
started my my tech career we were doing
object relational mapping and and the
database was, you know, supposedly
pluggable. You swap out your credentials
and it doesn't matter because you're not
using SQL anymore. Um, I think that
we're in the very early days of AI where
for retrieval purposes as soon as you um
soon as you start writing code, you're
locked into whatever stack you've
picked. and and that dictates a lot of
different design decisions that that you
have to make especially as you start to
scale. And where we kick in and have an
advantage against let's call it a
simpler stack would be when the the data
volumes get larger and the latency
requirements become more um you know
more
I don't want to say severe but the
SLAs's are really tight. That's when
we're going to shine because we can do
things that the other platforms can't do
and we've got a level of tunability
especially on the relevance side that
that can't be accomplished with other
data platforms.
That's a very good question that we do
talk about in the lab but I don't think
we provide that authoritative answer key
of here's how you construct your weights
based on you know things that you can
tell from the shape of your data or the
shape of the searches that you know
users are going to execute. The um the
short answer to that is today that's
actually hard to do. Um the longer
answer is and and this is something that
I think you'll see come from us is um
there's a missing element to relevance
tuning that hasn't been um addressed in
a way that makes this turnkey yet. And
um I've actually got a reference
architecture that I put out a year ago.
It needs to be refined. It's based on
Mashra about auto that covers autotuning
and that concept. Um, but in a perfect
world, you would actually be able to
take the searches that are coming
through the system and the telemetry
from those user experiences and things
like click-through traffic and and and
thumbs up, thumbs down, basically
telemetry from the users. And then also
um any other business metrics that you
have wired into your use case to uh to
actually tune the relevance which might
introduce different weights for linear.
Um it might um toggle between RF and
linear with specific weights depending
on the type of query coming in or um you
have all sorts of other types of
techniques. The one that I think is more
common than even those two is just
coming up with different sets of of
filters um based on the the query that's
coming in. So um Sunnil built out the
original architecture for this. We
called it an intelligent search layer.
Um and it's something that Azure search
has tried to kind of wire into their
product. It is something that you can
actually do today with elastic using the
agent builder construct which is covered
in the last lab. Um, but that's that's a
little bit different technique than just
tweaking the weights on the fly based on
what we're seeing. You you would
actually have um the um the LLM
interrogate the query and then and then
execute searches with different filters
based on that interrogation, which I
actually love that technique. I think
it's fantastic and I'm glad that we have
a construct for it with with Elastic.
And that's that's all, you know, stuff
that agent builder designed to solve
for.
Yep.
>> Exactly.
And that's where I'm hoping and and this
isn't something that that we've
announced that we're going to do yet,
but I'm hoping that at some point you're
going to see uh the concept of autotuned
relevance um be something you can enable
and and have attributes or settings that
you specify to to turn that on and maybe
even turn it up depending on the uh the
use case and and what you're seeing with
actual usage of the system. And and just
to be clear with everybody in the room,
we have not released any technology that
does that yet, but it comes up often
enough in the field when where I'm
working with customers that it's
something that if we had it, it would
move the needle big time and make
developers lives a lot easier. Would you
agree?
>> Okay, I'm gonna I'm gonna bring it up
again to our CTO and make him make him
say no again.
>> Right. So, we're gonna just walk through
this one. Most of you are probably along
with that past it. If not, it's all
right. Um so
right so we're trying to combine the two
the two different methodologies here and
the the crux of the problem is and it's
in here somewhere right like BM25 has a
scale it scores documents from zero to
kind of whatever whereas vector search
normally it's zero to one and so when
you have these scales that do not that
aren't the same obviously A poor result
in a lexical BM25 search is almost
always going to beat out from a pure
number perspective a good semantic
search. So then it's the fun game of how
do you combine them? And so there's a
couple of different ways. Um we don't
get into the kind of choosing one on the
fly here but there are you know
different ways to get into that. Kind of
getting the basics here. So RF is kind
of designed to be the
out of the box
works pretty well um until it doesn't.
But it's the it's a good first start.
You don't have to know how to tune. You
don't have to really know
um the details of your data. But the
idea then is that essentially forot
there's a table in here. You you throw
out the scores. So you you run the two
searches in parallel. you take the
order. There's a little bit of that rank
constant in there, but essentially if
you're high, if your result document is
high in both, it's probably a good m
it's probably a good match. When they're
not, that's where the kind of
combination gets into play. And you have
this pretty simple, where is that? I
scroll past it. Um, scoring in here. And
then you have a table. And so
essentially what you're returning is not
a a uh list of
uh score documents scored order. It's
just the rank order. And so that's why
there's a rank constant in there. Um
because you're just getting the rank of
the documents. And you can see in here,
where is it working?
Yeah.
Um it talks about it in this table where
the the documents come in in different
um different orders, but by ranking them
then you hopefully get the best answer
for you. But that doesn't always work.
And actually James mentioned this a
second ago, filtering is a really
powerful and effective way to help
along. So if you can filter your data by
keyword,
geoloccation, date, anything that gets
that data set down to a smaller
candidate pool, you're going to have
better results usually. And because you
have a smaller thing, you're not just
casting a net over everything. You're
filtering it down and you're narrowing
it down, right? It's like if if I want
pizza tonight, you know, I'm not just
going to search for food maybe, but I
can if I did search for food, I can then
filter by pizza and at least I'll just
get pizza results or you know, things
like that. So, um that's where filtering
comes into play and it's it's something
elastic search does very very well and
and very quickly and we have a lot of
different ways to do it. But then it
gets into that doesn't always work. And
so you can get into linear combination
and there's we talk about minmax in
here. There's different things you can
do. Um but this is where you're
normalizing the scores. So instead of
taking the order, you're going to then
instead just normalize the scores. So
everything has the same scoring range
from zero to one and you can put them
together. And there's a little bit of
the the tuning examples in here. It's a
again it's kind of the
um intro level to tuning for sure, but
you can tune the weights and you can see
um which one works well. And this is
where judgment sets comes in. And this
is where things like um you know we have
a lot of different workshops and things
like that and the the intelligent query
layer and things like this do this more
automatically not in and sophisticated
way but essentially you have your
judgments that that a human these days
you can get an LLM to help you but um is
based on this query. these are the exact
documents I want. And then you run your
experiments and you see which weights
work for you to give those results as as
accurately as possible
through here.
Do you have something you want to add?
Sorry. And I will add one more item
because this is actually a technique
that we used in the intelligent um
intelligent query layer architecture
that um that that we were talking about
quite a bit. uh last year and the year
before. Um, Elastic supports the concept
of search templates. So, you could
technically have three different search
strategies. One that uses RF, one that
uses linear and maybe another one that
uses um a combination of linear or RF
with a reranker. And um if you have a
layer on top, let's call it an LLM
that's got a simple prompt that says
based on this type of query, I want you
to route to this search template. Based
on this other type of query, I want you
to route to this search template. You
can literally have the equivalent of a
what I'll call poor man's um autotuning
where you're literally toggling between
different search strategies based on
what the search query that's coming in
looks like. and you have something and
it doesn't have to be an LLM, but you
have some way of interrogating that
search to decide which search template
to invoke. Most developers that are
building out an advanced use case where
they don't have a single strategy that
they can use for all queries are going
to end up with something like that under
the hood. It's just a matter of how hard
it is to actually code that up. And in
the case of elastic um a lot of folks
don't know about search templates but
that is a powerful mechanism that can be
used uh to reduce the amount of
boilerplate code you have to write for
that type of architecture.
Not covered in the labs but noteworthy
to at least have an understanding that
that that concept exists in elastic.
So the table at the end again is kind of
the take it with a grain of salt but
it's a good way to get started right
like if you don't know your your data
too well or it's all you know kind of an
unknown query mix you can start with RF
it does work pretty well it's not
something we didn't invent RF but we do
use it other places uses it um and then
beyond that you can start getting into
um other ways to com to combine the data
um but you don't always have to do
hybrid search sometimes semantic search
is enough sometimes times BM25. Um, but
usually we we find that there's some
combination of of semantic and lexical
search that helps the um the retrieval
work most effectively.
And then lab four
is where you um despite the title you do
put it into a model but we're going to
show you how
again as I said at the top of this LLMs
are extremely you know smart's not their
best word but you know they are
effective at giving you answers um but
you anytime you have to feed them data
of that they're outside their training
knowledge or anything, you can pretty
confidently get them to give you the
wrong answer by providing them the the
set of data and say the sky is orange
and then usually it'll tell you the sky
is orange. Um there's ways around that,
but this is where we kind of show you
that retrieval is still important to
agentic um answers.
Quick show of hands. Are there any folks
that are not [snorts] actually past lab
three yet?
Okay, good. People are cruising along.
Awesome.
And so it's worth mentioning too, this
is where we actually get into agent
builder um elastic's agentic platform
which has um the ability to obviously to
run agents to run tools and skills. Um
you can hook into lots of LLMs. The
elastic infrance service has you know
all your favorite LLMs available to it.
Um but you can again bring your own um
your LLM and and it's able to then run
these tools directly against uh the data
within elastic and actually now it's not
covered in the work in the the workshop
but we have uh workflows and workflows
essentially are anytime you have a an
ordered set of tasks you want completed
can have decision trees and things like
that. Um the agents can call these
workflows and they can also reach out.
So you can call out to other systems,
you can call MCP tools, you can call
APIs, call anything to your heart's
content. Um, but again outside the scope
of this workshop, but since we have a
little time here, this is where the
agent has the ability then to start
doing things. So not just retrieving
your answers for you, but there's a
whole other workshop that you could go
to where because of you know an incident
for example the the observability the
hotel trace data you bring in it can
decide yeah the system is not is running
out of of resources it needs to scale.
So you can call a workflow for example
to autoscale your Kubernetes
environment. It's just one example, but
this is where we actually get into agent
builder and it walks you through a
little bit of the um
the capabilities.
and one of the more interesting things
about agent builder for folks that are
software developers is the fact that
everything that you see in a cabana user
interface in agent builder is is
programmable programmable via API. So if
you decided that you wanted to do a
quick prototype and you're using our
agent builder mechanism within Elastic
and you think, "Oh, I have to rewrite
all this code from scratch now and build
out a real app." You don't have to do
that. You can reuse those same endpoints
in your application and make the same
calls in a custom user experience that
um that you control. And then you have
the added benefit if you decide that you
wanted to pull those agent builder
components out and wire in another
framework or another, you know, another
set of APIs that you either build or use
a different framework for, uh, we would
be compatible with that as well. So the
goal for us is to provide as much
turnkey experience as possible, but not
lock you in so that you're forced to
build applications the way that we want
you to build them. We're very flexible,
almost to a fault. So when you ask us a
question, oftentimes the answer starts
with it, it depends.
Did anybody come in recently that
doesn't have the URL?
Sorry. Thought so, but start up there.
Um, so it's in the upper right. It's
that short ELD one. And in case anyone
um
came in later and didn't catch me say
it, this will be available for a week,
the actual workshop itself. And then the
blue by James um link is the the repo
that has it has all the the notebooks in
there. It has all the other code in
there, but the relevant stuff you'll use
without instruct is the notebooks. You
can hook it up to any elastic search
cluster you have free one. Well, sort of
if you hook up a different service. Um
but it'll load the data and you can run
through it all. So that that'll be
available until someone deletes it.
delete me.
>> By the way, thanks to our distinguished
architect over here, Sunnil, we uh
wanted to make sure that we give you
bonus content, bonus workshop materials.
There are additional workshops available
online that have the same format that we
used here today where there basically is
an instruct environment. It's pre
pre-built so that you can walk through
the concepts and learn more about how
Elastic works under the hood. We highly
recommend that you hit that URL and and
use the workshops. It's essentially free
training and once you complete those
workshops, you'll probably increase your
market value by I don't know$100
$200,000 a year. It's a guaranteed pay
raise.
>> Okay. So, while people are working on
that, I'm going to do two things. So,
one of the So, sorry [clears throat] I
kept talking a couple times about um you
know providing new information and
up-to-date and um fresh and whatever
proprietary information to the these
LLMs as a way to augment it's where the
augment the a and rag comes in augment
their knowledge. The other thing that
comes up a lot and this is coming up
more and more in the in well everywhere
especially as agents start running
around and and doing things even faster
is being able to site the sources. So
models are really good at coming up with
information and oftentimes it is
correct. But what they're also great at
is lying to you because not because
they're specifically trained for it. But
what happens is if there's a very thin
line line between say two other lines
that you ask a question about and it
doesn't know that specific answer but it
knows enough other information around
the answer and about other topics and
related it can come up with a extremely
convincing um you know response that
unless you're an expert or really know
the actual answer can can trick people.
So, all that [clears throat] to say, one
of the things that's in this lab, it's
kind of in the middle, and it's up on
the screen right now, is the ability to
have an LLM site sources.
Most models
do not have the ability to site their
sources because it's not a database.
It's it's these models are not doing a
table lookup and pulling information.
It's generating tokens based on his
training. Anyways, so by providing the
actual answers to the LM and having it
parse it out and put together a
human-friendly answer or whatever format
you want it in, it can also then cite
its sources. This is extremely important
in things like legal, which is you've
probably seen in the news come up a lot
of times where lawyers are getting in
trouble because they're having cases and
then they're making up answers, citing
cases that don't exist or twisting the
answers. So if you can have the model
process you know large amounts of data
complex data but still site the answer
um it makes them a lot more useful and
trustworthy
to a point.
So when you go into
this
as James mentioned um one of the nice
things about the agent builder platform
is that it is all also API driven. So
that's kind of why the the lab in this
one was a little bit reversed to show
that where you can build all this
programmatically. So you can build
skills and tools and agents and you know
through I built this all
programmatically and that way you can
create it, tear it down, scale it,
change it as you need um but still use
all the capabilities built into the
stack and things like that. Um so we'll
go in here and then you can um ask a
question you know we go into overview
we have a lot of skills out of the box.
So these are the skills and I'm sure
everyone here knows this because you're
an AI conference right but a skill
has a lot of different things but
essentially it's explaining to um you
know a model or an agent how to perform
a task in a certain way. um when when
tools should be used, how to create
presentations, how to create other
services. Um but it's anything you can
write down to kind of help it out. So it
doesn't have to just figure it out by
itself. Um some things is just ways to
make it faster. Some things is when you
run very specific outcomes. Um if you
want to give it core instructions as as
shown in here. Um and so we provide a
lot of out of the box things um skills
for you like if you want to create
graphs, visualizations,
searching um but we also create tools.
So the difference then is a tool is
performing an action. So a tool that we
pro you know provide here out of the box
are things like running searches,
listing workflows. I talked about
workflows. There's the way to actually
reach out and you know query external
services or run things in a very
specific um deterministic manner but you
can create your own tools. So if we go
into the the agent that you created for
example and you look at the overview um
it's a very you know simple agent again
for the purposes of today it has one
skill. It talks about how to diagnose
and and um an issue that you're looking
for. So, it's pretty pretty um pretty
short here compared to the out of the
box ones, but this is where you can
provide as much information to to help
it out. So, it helps to find the clause,
find the fix, talks about um looking at
the error codes. The other things that
it can do is I think it has one tool.
Yeah. So here we're um we have a search
tool but if I add other tools just to
show
create a tool create a new tool. Um
[clears throat]
this is always a fun question I like to
ask. Who here knows or has heard of ESQL
within Elastic?
Okay,
>> we got one. Nice. It's about what I
expect. I was happy to hear though that
a a lot of you are familiar with elastic
in elastic search. So that that's good.
Um ESQL is a newer
u query language within elastic. It's
the ES pipeQL. So it's a uh SQL near SQL
like um language. So you have a SQL like
syntax and then essentially the pipe is
in there to you pipe commands together.
You you run the thing, it passes it to
the next pipe and so on and so on. Um do
that. So you can have VSQL tools to
query um you know documents in elastic
search. Index search is [clears throat]
kind of an interesting tool or yeah
tool. So ESQL is you're running a
specific query. You're you're querying
you write down the query you get back
specific fields. Index search is kind of
this I almost think of it as a
documentation tool. So you're you're
telling it for a specific index or set
of indices this is what the index is
for. This is what the field mapping is.
These are what the fields are. If you
have say a product index and a pricing
inventory index, it tells how to combine
them. Like with ESQL, you can join uh
indices together. So it talks about that
and agents because they can do round
trips and do exploration. They will
generally be able to figure out um you
know the indexes in your in your index
in your cluster. So if you just ask a
question and it doesn't know anything,
it's going to do this query search tool
and it's going to look at the mappings
or it's a mapping tool. It's going to
find all the indices and then the
mappings. It's going to try to guess
like what sounds like a product thing
and then it's going to try to put them
together. Anyways, it'll roundroin for a
while and that costs tokens and we all
love token spending. So this is a tool
that helps speed up that dramatically
and kind of help point the agent in the
right direction.
Workflows. I think I talked about this a
few times, but we can run things in a uh
orderly fashion and reach out to other
systems. And then MCP, if you want to
call out to an external MCP server, you
can [clears throat] do that. I will
mention at this point also that the
tools in agent builder, both the out of
the boxes one and custom tools are
exposed as an MCP. So, Kabana exposes an
MCP uh server. So any of the tools in
there you can use you know if your agent
has um wants to connect via MCP
and the last one. So you do this in the
lab
but this shows basically how the agent
can then do multiple um
multiple loops. So it has to do first it
loads the skill to see how to answer the
question about um keeps dying with a 137
why does it happen and how so this is a
two-part question right why does this
happen why is my cluster dying with you
know the 137 uh exit code so it has to
figure out the answer to that and then
how do I change my settings to to
prevent it so it's a two-part question
and again so runs that skill
and then it starts to find the answer.
So goes a couple loops and it diagnoses
your problem of you know tells you why
this 137 is happening. It's actually
it's the o the fun out of memory manager
running and killing you. Um then it
talks about how to uh tune your JVM
options to to fix it but talks about
preventing. So
because the answer within was within
elastic and it had the ability to you
know query it and then run multiple
tools and things like this it's able to
kind of get you that answer and uh get
you get you on your way.
>> Yeah. And the one thing I'll add is that
if you're if you're in active prototype
mode and you're trying to to get to um
search logic or query language um logic
that that actually solves for your use
case. This is actually a a pretty nice
developer tool and debugging tool to
find out what um what searches will work
to retrieve uh the data that you need.
And the last thing I'll say about uh I'm
a big fan of ESQL. I started out a
little bit skeptical because there were
some features in Elastic Query language
that weren't in ESQL. I think that it's
feature complete enough uh for you to to
at least take a look at it, especially
if you're building a gentic search use
cases because there's some really cool
concepts in ESQL uh that lend themselves
well to um to solving for for certain
search um tasks better than elastic
query language, which you should
consider a superset of what ESQL is
today. Um, and the other thing about
ESQL that makes it fantastic is uh the
ability to have parameterization wired
into the MCP tool calling chain and and
wired up with agent builder, which is um
a fantastic ad that technically is
doable outside of ESQL, but the way that
we have architected ESQL and our agent
builder and our MCP endpoint, it is the
happy path to a lot of the um let's call
them agentic search use cases. that you
might have. So if you have not looked at
ESQL yet, highly recommend you do that.
And if you were trying to pay attention
to some of the innovative stuff that
we're doing around search, first place
to to look is actually going through the
ESQL docs and seeing what new novel um
retrieval mechanisms we're coming up
with because we're doing some very
interesting things with federated search
and potentially calling out the
different systems within an elastic
query language um you know query that
that is not considered traditional
elastic. Um, and that's stuff that's in
development now, but you're going to see
that hit hit the product. And when it
does, ESQL is going to be your gateway
into that.
And I'm talking about things like being
able to do like parquet queries on
things that are external to Elastic with
with an SQL call, which could be
incredibly powerful if you're also
joining that with data that comes from
Elastic.
You can actually see that the the agent
used ESQL for this uh this call. So this
is what it looks like. Um so it can do
things like fork off and then so this is
where it's combining uh two of the
two of the search threads. That's what
the fuse is down there. And um so it's
able to ask these questions and then
return the answer. So you can see it's
you know there's the pipes that can um
again you run a query you run a phase of
it essentially get the answer and it
moves on to the next and next pipe
language like that. So it's um yeah it's
very parameterizable is
>> parameterizable and it's it's trying to
accomplish all the things that the
Splunk query language tried to you know
to do with with Splunk in its heyday. uh
and then um and then also marry that
with SQL concepts which are obviously
tried and true and I think that the uh
the last thing that you'll see with ESQL
is the queries are are more tur they
don't have as much markup in them uh to
actually get to get the retrieval right
which is one one added benefit to that
piped uh construct and there are other
other companies that that leverage the
same technique in order to build out um
you know search usually it's for
unstructured data sets logs
Um, and you know, and I'd say that that
was the primary reason we started
building ESQL was to build, you know,
the best best-in-class search experience
so people could get rid of all their
Splunk stuff. And and now we've pivoted
to where this construct is so useful
that it should be available in all the
pillars of elastic, search, security,
and observability. It's a first class
citizen construct for for for all three
pillars going forward with a primary it
being the primary mechanism for where
we're going to innovate.
>> And so you can see when it's doing its
one of the the hybrid search query, it
[clears throat] responds. It shows you
so you have the you have the audit trail
essentially of how it got to these
answers. So, not only citing the answers
all the way at the bottom and you can
click on them and if you want to deep
dive into the fun world of JVM settings,
you can do that. Um, never doing that
again. But, um, just kidding. One of the
nice things too is then it'll show you.
So, we're limiting five and it it does
five. It tells you it found five
results. um doesn't clutter it all up in
in the UI here for you. But you can
click on that and you can hop over to
this is discover. It's kind of where we
discover documents. It's the kind of
normal searching around interface of
Cabana. It's changed a little bit over
the years if you haven't used it in a
little while, but now you can do ESQL in
there. And you can see here then it has
the five documents that it came back
with. And if I close like some of these
panels,
builds a nice little chart for you. I
don't know if that's the most helpful
chart, but you can see then with the
query up at the top, you have the actual
documents. And
go in and see the full thing. And so
here's the body of it. And so we were
searching
part of this. Oh, here it is. Looking
for the URL. So the URL again, this is
because we provide the URL as part of
the document, we're able to, you know,
provide essentially a link to more
information without having to just
guess.
>> I think this room closes out at the 420
mark. Is that correct?
>> Yeah. Timer says 18 minutes till
>> 18 minutes, which means you have
>> Let the hammer come and hit us.
>> Yeah. Which means you you do have a
little bit of time to ask questions.
>> Yeah. And there is the Yeah, feel free
to ask questions. Sorry. Um there is the
lab five about um
rerankers.
Lights are like burning my brain. Um so
reranking in there is is an interesting
um thing that I think a lot of people
don't kind of fully understand why you
want to use it. And so that's why we
added this on um to kind of explain why
you want to use it. And if this spins,
see if that comes up. Maybe it's my
thing. Reranking is taking the So if if
[snorts] the queries that we've been
doing here and everything is the first
phase, call it of of retrieval. The
second phase you can do retrie uh
reranking. And so
if you're running vector search,
semantic search, hybrid search across a
first phase and get back a large set of
data, then you can take that data and
you can rerank it. And reranking has I
wish this thing was working. I think
it's me.
re-ranking combines the
the query and the the document as
scoring time together. So normally with
with vectors you you know you ingest all
your data whenever that is and then at
query time you query it and it just does
um HSW or or one of the disk algorithms
and returns a set of documents but the
the query and the the documents aren't
really scored together. Reranking
combines those together, but because
they're running together at at that
query that phase second phase time, you
can't pre-mbed. So you pay the penalty
of having to run inference at, you know,
at query time. Now the way you do this
then to kind of help this along is by
not reranking your entire corpus of
data. You run the first phase to get a
smaller set of data and then rerank with
a model to then you know rerank that
that small set of data.
Sorry, there we go.
Trying to
show an example instead of just talk.
Here we go.
My lab was dying.
So if you get to this in here, you can
see toward at the end um again kind of
the points on here about
when you can add a ranker if you have
that that the latency budget. If you
don't if you can spend a a little bit of
extra time to let this second phase run
and generating embeddings because that
precision of the you know if it's answer
one versus answer two if that is a
critical step that's where paying you
know the the slight um latency penalty
comes into play. If you just get your
documents good enough in the first phase
and let the agent go after them, then
you probably don't need a reranker. But
it's when you need to have that or that
specific order come into play um come in
and um and we see that a lot with
agentic search use cases. We're seeing a
lot of situations where folks are
testing the evaluation based on the
first, second, and third document chunk
coming back, which gives you a very
small window of opportunity to get the
answer right. If you're just handing a
small set of candidates to the to the
large language model to answer the
question versus a larger candidate set
and then and then asking the model to
get it right. And and that's where a lot
of relevancy issues come in. You're
passing in too much context. It's a
multiple choice where two or three
answers look equally right to the LLM
and it just picks one and and if it
picks the wrong one then your your users
and their beta testers for your new
agentic search system complain about the
search not working. Very common, very
very common. And um you know oftentimes
a reranker like this will will actually
be very very useful.
And so there's two points or two types
of um reankers at least you know that we
support. So there's point-wise these are
what most reankers are today and this is
what that the V2 model is. And so the
point-wise it it still combines the it
takes the query and the document
together but it just scores them
independently. It's only looking at the
the query and the document, nothing
else. Listwise, which is what is in the
Gina V3 model, takes your candidate set
and I think it right now, for example,
up to 64 documents or 64 candidates and
it looks at them all together. And so
that way way if the if the answers
essentially or the the potential
candidates are all very similar like
they're all pretty much talking about
the same thing. That's where having the
listwise can edge out pointwise because
it can see the nuance see it can see the
nuances um within that list because it
sees the multiple documents together. Um
it does take a little bit of extra u
memory or or time because again it has
to generate embeddings for all those
candidates all at once and hold them
together in memory and run um run its
evaluation across them as opposed to
just firing one at a time and do that.
So if your if your data is pretty
diverse and where the answers come back
and it's you know it's a pretty distinct
set of candidates where you know one two
three four five are all pretty different
enough that the pointwise is hitting it.
Sorry.
There we go. Um then point wise usually
pretty much usually works out. But
again, if you have that set where the
the potential candidates are all
extremely similar, listwise is probably
going to help you out for the best.
and somewhere in here
because we want to be helpful. You don't
have to run
um
while it is a two step a two-phase um
you know phase one is query phase two is
your ranking you don't have to manually
um have those as separate separate API
calls we can do it all in one shot um
you do it in the lab it's in the
retriever you can you can do it
>> can you rerank any SQL
>> yes
>> yeah okay [laughter]
um so you can do it in SQL too but one
dot basically you have the reranker you
tell what reranker you want to use you
know the model and the query and it runs
both phases for you so that way again
you're not having to manage the
inference setting separately you're not
having to call the inference API then
query then rerank you can just fire it
all in one shot and we'll take care of
it for you
so I'm going to put up that
slide again with few of the links again.
So the upper right is what we've been
doing today. That's available for a
week. The bottom blue reference repo is
where the the code for this lives, the
notebooks and things like that. And then
there's the two red ones in the middle.
Um Sunnil's secret elastic environment.
Oh man, typo it too. Um everyone's gonna
take a picture of it. So, and then the
other god
>> just proves that we're in a live
session.
>> I'm gonna blame the lights
>> and that we're just, you know, we're
doing stuff on the fly.
>> Still got to run.
Okay. Um, and then the other workshops
online. So, we do have a bunch of other
workshops that online that are
completely free.
And so things like working with streams,
if you have streams of data coming in,
it's extremely um efficient way to
handle that data. Another rag one,
lexical search, vector search tutorials.
If you have anyone's doing uh
observability work, so things with open
telemetry data or looking for root cause
analysis, things like that, we have a
labs on that. So, a couple observability
labs.
Should be some security ones in here.
So, security is a big platform, our big
part of our platform. Um, doing anything
from like attack discovery and detection
rules. I know there's new ones coming
out too. Um, as
we add in more and more agent capability
into the stack.
Any questions?
All right. So, let me ask a question
real quick.
If you hang out in here, do you
automatically get a seat in the next
workshop?
I'm just curious if that's why people
hang out. Okay. I'm trying to judge
who's still working and who's just
hanging out, which is totally fine. I
Yeah, I get to leave either way. We're
going to assume that most of you all are
hanging out and that you're not, you
know, waiting for help on anything. But
if if you are, you've got another 7
minutes and 57 seconds.
Sil, you want to demo anything for seven
minutes?
Hopefully this was a good use of your
time for the folks that are still in the
room. And we'd love to get your
feedback. We didn't tell you this, but
there is a feedback um data entry point
at the end of the workshop. So, when you
finish it, you do have the ability to
tell us how awesome the workshop is or
or how much you didn't like it. And if
and if you say bad things, then it will
hurt our feelings. But but we will make
the workshop better for others after the
fact.
