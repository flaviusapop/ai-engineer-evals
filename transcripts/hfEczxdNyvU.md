# Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust

Source: https://www.youtube.com/watch?v=hfEczxdNyvU

Uploaded: 2026-10-06

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Hey everybody.
My name is Doug Guthrie. I'm a solutions
engineer at Braintrust.
Um I have a few colleagues, uh a couple
colleagues in the room that uh can help
if you get stuck anywhere uh within the
workshop today.
Also, um I get interrupted all day long
during calls, so if you want to
stop me at any point and ask a question,
I'm up for that as well.
Uh hopefully you've had a chance to grab
the QR code by now. It just takes you
out to this repo.
This is what we're going to be us- using
today uh as part of the workshop and
going through understanding how you can
do observability
within Braintrust and sort of using all
of the different features
within there to build better agents.
That's really why we're all here. Like,
how do we actually create good quality
agents?
Um I'll leave this up for
uh
10 more seconds or so.
I'm going to have this again later in
the the presentation when we actually
get into the workshop. So, if you if you
don't get it, um
you can also Google um dpguthrie on
GitHub and search that re- uh repository
on on GitHub and you'll be able to find
it.
Cool. So, um we're all here to master AI
observability, uh and I'm going to give
you what that looks like in the context
of using Braintrust.
Uh quick agenda. Uh I do have some
slides that I want to sort of set the
foundation for doing observability, and
I think um
what we've learned of how to how to do
it really well. So, I'll sort of set the
foundation for what that looks like. Uh
give you a sense for how do we generate
signal in this massive amount of noise?
Um you all have probably seen a trace or
you can understand that the agents that
you're building are generating a massive
amount of data. And being able to parse
through all of that and actually derive
some type of signal or insight is
challenging. That's where the challenge
resides. It's there's one side of
actually being able to trace and then
have a sort of platform that allows for
observability. Then there's the other
side of how do we actually do something
with it and derive some type of insight.
So I'll show you what that looks like
within Braintrust and then we'll sort of
walk through all of what what I what I
described or what I've shown on on these
slides in the workshop. Um as I said, uh
if you have a question, feel free to
jump in. I do not mind. Uh I have sort
of at least I'll try to save some time
at the end for some Q&A as well. So feel
free to save your question to the end.
So just a quick Braintrust intro if
you're not uh familiar.
Uh we are an AI and we are an Evals and
observability uh platform. Our sole goal
is to help our customers
build better agents. Uh we we sort of uh
help enable our customers understand
what quality looks like and then how to
improve it in a real measurable way.
Um
one of like the the more fun parts about
my job is that I actually get to go
speak to some of these customers that
you see up there in the top right. I get
to understand how they are building
their agents. And a lot of those
learnings actually make make their way
into our product. Make their way into my
other engagements with customers. So I
get to go actually talk to the engineers
of Cloudflare and I get to talk to the
engineers of Dropbox and I get to
understand what they're doing, the the
types of scores they're creating, how
they think about our new feature topics,
what that sort of creates, the the types
of automations they're building on top
of it. Uh I hope to give you some sense
of that today.
Uh mentioned some of this, right? We are
an Evals and observability platform. Um
you think about like evals and
observability, I think they're like two
diff two sides of the same coin. Uh
taken together, it's really what's going
to allow you to create better quality
agents.
Uh if you if you hang around and I mean
like if you
if you aren't a Braintrust customer, if
you're not using Braintrust today, would
highly recommend coming back and looking
at Braintrust in the next month, 2
months. Uh
where I think we see the the industry at
large today is is a more like very
passive way of observing data. Uh sort
of what I alluded to of like being able
to derive insight. Uh Braintrust is
moving, I think, a little bit more
towards what we call active
observability. It's It's actually giving
you the primitives, uh the foundations,
to give you the right insights where you
don't actually have to pull from your
platform and understand what that means
in the context of your agent and and
what you need to go do to go and improve
it. Uh so, uh active observability is
the is the way in which we can start to
bring those insights to you so that you
can build better quality agents.
So, quick quick Braintrust stuff there.
Um
I'll plug this again at the end, but we
are We do have a booth at the expo. Uh I
think it opens around 5:00. Come and
find. I'll be there tonight. Come and
find me, ask some more questions. Uh
we'll be here all week as well.
So, the the foundation to all of this,
uh the foundation to observability in
general, like I'm guessing most of you
already know here, is tracing. You have
to be able to understand all of the
different steps that your agent takes,
right? What are the the the things that
it's doing to get to its final output.
And not only not only that, but what are
the inputs to those tools? What are the
outputs of those? And if you if you
start to think about like all of the
different steps that your agent can
take, this can balloon um pretty
quickly. And being able to sort of parse
through this, this is the challenge that
we are trying to solve. But without that
tracing, right? We're not actually able
to understand what's going on, where
quality is actually deteriorating.
Uh and so, being able to
uh one, trace all of this data and then
derive some type of insight again is
where where Branch is going to provide
some value, but
it just in
in general, if you're thinking about
observability, if you don't have some
part of your stack
in in a trace that looks like this, then
it's it's a black box. It's going to be
very challenging for you to actually
surface those quality issues or, you
know, point Codex or cloud code or
whatever you're using out there to like
understand what's going on. If that's
that that data is not there, you can't
actually surface those
those places where the agent is falling
down, where it could be improved. So,
tracing is the foundation. I think
if you look at the eval side and of
course talking today the observability,
it all sort of centers around us being
able to capture all of the different
things that our agent is doing.
So, just another quick call out on the
Branch Trust side. We we have a lot of
different ways. So,
I'll skip ahead just a little bit. The
workshop that we're doing is built on
it's a you know, dummy sort of support
agent. The the sort of agent isn't the
thing that's important, but it's built
with the Open AI agents SDK.
We have lots of dinner different
integrations with all of the different
agent frameworks. We have integrations
with all of the AI providers. We have
different programming languages. So,
depending on how you are building your
agent, whether it's the example today is
in Python
but it could be TypeScript, it could be
Java, Ruby, Go. So, we are pretty
flexible in that we allow you to sort of
bring whatever it is you're doing today
from a programming language perspective
or how you are building your agent,
whether it's with a framework, whether
you're using Open Telemetry, whether
you're sort of hand rolling your own
orchestration, whatever it is, Branch
Trust has a way to hook into that pretty
seamlessly. And I think if you're
looking out across the market, right, if
you're trying to understand how do I
how do I trace this this agent,
you're going to have to have the ability
to go across a lot of different things
generally. And you can see over here
there's a lot of different ways in which
you can integrate your stack into
Braintrust. So again, I just have the
dummy agent today is using the open AI
open AI agents SDK, but that's certainly
not what we're confined to.
This is something that I sort of
I say the word flywheel like, I don't
know, 100 times a day it seems like. Um
The whole idea and where I think we've
gotten a lot of feedback from our
customers
is the the way in which that the way in
which they are building better agents
today is they are creating something
like this, right? And what what I mean
by that is that production should inform
development. You should have a really
simple and easy to create flywheel that
allows you to
develop some type of change, fix
something within your agent, test
whether or not that change regress the
agent in some way or improved it. You
should be able to have the confidence to
go and deploy that agent to production.
When you deploy, right? We need to be
able to observe it. That observation
though, we need to like tack something
on top of that which maybe you don't see
necessarily called out specifically
within this flywheel, but you need to be
able to derive some type of insight at
scale.
Most of the customers, especially on the
slide that I showed earlier, they have a
massive amount of scale and being able
to derive inside or having a human comb
through that data would just be
incredibly challenging. And so we need
to layer intelligence on top of that and
that's one of the things that that
Braintrust will offer, but I think just
if you're thinking about the the process
of building a better agent in general,
you need a flywheel like this. You need
to create something where production in
some way informs how you go and change
your agent. And so this is what I'll
show you a little bit today when we go
through the workshop is how we can
actually surface some of those insights
in an automated way from our
support agent, bring those insights back
to our development process, make some
type of change, run an eval, right? That
that sort of loop uh becomes sort of
uh
it's just incredibly important. And and
hopefully it becomes a very trivial
thing that most companies and most
developers can just very easily plug
into.
So, when I say signal, uh I just in this
context I mean two different things that
we will sort of wire up also during the
workshop.
Uh I mean uh scores. So, this could be
uh you know, evaluators. This is just a
way to measure the output of your agent
in some way. Uh you have some particular
failure mode, you have something that
you're trying to understand about the
agent when it um
when it received some input. Uh we we
can create a lot of different types of
scores. Uh one of them you see over on
the far left is a code-based score.
These are generally uh very fast, very
cheap, uh and very easy to run. Uh you
can imagine like I'm trying to validate
a schema. I am trying to understand was
tool A called before tool B? Was it
called in the right order? Uh things
that can be produced very very quickly
uh and without sort of having to go into
an LLM.
Uh the more subjective, though, is that
LLM judge. We want to bring some sort of
like human
uh understanding to that that that
trace, right? to that interaction that
just happened with that eval case or
even uh online as well. And so, you
could actually, you know, give the LLM
some criteria of how you want to assess
the output or assess that conversation,
and it should produce some score. Um
And then there's there's a probably
actually a fourth one here, but the
third one that you see over on the right
is an LLM
LLM judge aligned with human review.
What's also important, you could
probably imagine, is if I have an LLM
judge and it's producing results and we
are sort of making uh decisions based on
the those results, we should probably
understand whether or not those results
are good or not. And so, there should be
some element of human review. I think
especially if you are using these judges
in an online sense, right? You are
scoring actual interactions of users
with your agent, you should be able to
provide some type of interface to users
to provide that review to calibrate
those those judges, right? This isn't a
set it and forget it type thing. Uh your
agent will evolve, so too will your
scores. The the fourth one that I
actually have an example of in the uh
the work the workshop is a sort of
code-based score, but it invokes an LLM
under the hood. Uh you can imagine like
there is branching logic or there's just
uh more advanced or complex things that
you need to do uh based on some type of
logic that you want to encode in your
code-based score. Uh so, you could do
that as well.
Uh these are some of the things that I
think I've heard in in different
conversations with with our customers.
Uh I think again, it's like take it with
a grain of salt to some degree. Like
it's not always going to fit 100% of the
scenarios every single time. It's It's
where I've seen a lot of success across
our customer base. Um just being able to
like understand the reasoning that the
LLM gave for producing a score,
incredibly helpful especially on that
human review side where it's like, "Hey,
I can understand why it produced that."
That will then inform how I can go
change my scores in some way.
Um binary scoring, I think uh especially
at the outset when we have sort of an
agent that we are putting out into
production, binary scoring I think is is
better than, you know, A B C D or or so
on. And you should be incredibly harsh.
Uh you should produce really hard
examples. You should You should if you
get 100% on every single one of your
evals and and we probably will today
because it's
uh sort of dummy use case, but if you
get 100% of your uh 100% on your evals,
yeah, one, you probably don't have uh
strong enough
test cases in your data set. Your scores
probably aren't harsh enough. Uh so, you
should sort of look at that and and and
sort of calibrate accordingly.
Um another one that I've seen, you know,
again, grain of salt including some
examples in in your prompts tends to
tends to help and then perhaps using a
stronger model for scoring than for
generation, right? Let's bring a little
bit closer to human subjectivity as
possible to this. Obviously, this can
change based on
the the the type of traffic, right? If
we start to talk about online scoring
and things like that, but um
to that point, there are obviously two
different types of scores, at least the
way that we see that here at BrainTrust.
There is the offline, right? This is our
with our e-vals. We are sort of trying
to derive some signal of whether or not
we should push this thing to production.
This is going to give us indication of
did it improve or did it regress?
Um this is going to be uh you can
imagine wiring this up to
Excuse me.
It's my daughter.
Um
yeah, so you can imagine like wiring
this up, right? To CI. You can imagine
wiring it up to some sort of automated
pipeline.
Again, where you're running it offline
and then on the flip side, the the whole
idea or like the thing that we're
talking about here is how do we how do
we derive signal from things that's
actually happening in production? And
one of those things that you can do is
use those online scores and and score
that traffic as it's incoming into
BrainTrust. And again, the idea is to
attach some type of signal where then
you as a user can actually go in and be
like, "Hey, my routing accuracy score is
zero in these examples. Is there some
sort of pattern that I should be aware
of based on this feedback, right? So I
need to go from like this massive amount
of data into something that is much
smaller and easier for me to consume."
The second signal is a is a feature that
we have in BrainTrust called topics.
The idea here is that you want to like
understand patterns within your data.
You want to go a little bit further
beyond the
uh the known unknowns, right? So, like
your scores that you've already created
uh in your offline evals, they are
failure modes that perhaps you've
already recognized. There are things
that you already are testing for, but
that's certainly not the the scope in
which your agent can operate or the
failure modes that it can encounter. And
so, we need to understand beyond that,
and Topics is one of those things that
will help enable that. We should be able
to um understand silent failures. So,
you can see there like these very sort
of traditional scores like factuality
and and moderation. They're They're
going to catch a very small subset of
errors, and and probably you have a
little bit more uh bespoke scores that
that you're using.
And then to that point, like the evals
that you're running again are using
those those subset of scores to
understand improvement or regression,
but there is a sort of wide swath of use
cases that your test scenarios are not
capturing, that your users are actually
uh probing your agent with and trying to
like get some type of output, and
perhaps maybe it's not the right one. Um
so, we want to capture these edge cases.
We want to capture the tail end, and we
want to structure uh then the flywheel,
right? We want to bring these examples
back to our data sets. We want to run
evals. We want to perhaps create new
scores based on that feedback.
So, so what is what is Topics? Uh Topics
uh in general or at a high level is a
way for us to understand patterns within
your data. Um we can create clusters of
those patterns and give you a sense of
frequency with which those things are
occurring.
Uh also important to call out here is
that there are both built-in and custom
facets. And And what what I mean by that
is when you go into your BrainTrust
account, you can enable a feature called
Topics, and out of the box you can see
task, issues, and sentiment. So, I can
understand, "Hey, what are What is the
common user intent? How are users
feeling when they interact with my
agent?" And what are the common agent
issues? So, I can and that that sort of
taxonomy, where I'm not necessarily
providing that taxonomy up uh up front.
The LLM uh creates that uh for me as
part of this pipeline. But, I can also
bring my own custom facets. I can I can
sort of build my own prompt, and I can
build my own pipeline to create these
patterns within my data, right? With
respect to the things that I care about.
Uh
go go back to this. Um
this is you know, just an example of of
of an illustration that you might see
with the topics that were generated. Uh
but, why why would you use it? I think I
sort of alluded to this a little bit,
but you want to be able to not have
blind spots. Uh you want to be able to
understand all of the different ways in
which your users are interacting with
your agents, and then allow that to
inform what you go do as a developer,
right? This this doesn't even
necessarily have to be an issue or
failure mode. This could be like
potentially um feature requests, new
things that your agent could do based on
the way users are actually interacting
with your agent.
Um so, this is like I think one of the
ways in which I've seen a lot of our
users start to use this uh is actually
create this or or sort of understand
what's going on and inform what a road
map should look like for the agent,
right? It It starts to uncover things
that were not necessarily aware of with
respect to these agents running in
production.
Behind the scenes it is a really complex
pipeline.
Um you see over there on the left a
preprocessor. So, if you think back to
my my first slide with the that trace,
and that's like a very very small trace
uh relative to what I've seen our
customers generate. What we need to do
is preprocess that data into something
that is meaningful to give to the LLM.
Um
so, we give you a what we call a default
preprocessor. We essentially take what
what you'll see in our thread view, and
you'll see that in just a little bit,
but it's the back and forth, right? It's
the user, it's the assistant, it's the
tool calls. We preprocess that massive
trace into something that is meaningful
is much smaller. Uh we then pass that to
a facet, right? The facet is the thing
that that I just described, issues,
tasks, sentiment, your own built-in
facets.
What we're going to do here that that
pre-process data is going to be passed
to that facet. We are going to then
summarize it. That summary, we then
create a vector embedding of that
summary within our back end.
Uh,
on top of that, once we have that vector
embedding, we can now go create what we
call a topic map. This is sort of what
you saw on the previous slide of the the
scatter plot. Uh, this is what now
allows us to label our traces and
classify them. And if I have those
labels and those classifiers, it becomes
incredibly trivial for me as a user, and
also incredibly trivial for me as a user
um, using a coding agent on top of
Braintrust to now start to filter
through that noise using all of that
really rich data. Uh, important callout,
the pipeline that you're seeing, the
facets and that embedding step is
actually using a a hosted model that we
have. So, we have just done a lot of
work behind the scenes to create um, not
not like a feature that you would just
like show in a demo. Obviously, like
we'll we'll see some stuff here today,
but this should work at scale. You
should be able to run this on 100% of
your traces. That's that's the sort of
goal of our topics pipeline. It is
uh, just to get like maybe more detailed
than I should, 6 cents per um, million
tokens on the input side and 40 cents on
the output side. Uh, compare that to
like other models that are that you
might be using uh, on the LLM judge to
create that same type of signal. You can
create a pretty compelling use case, um,
especially if you start to see value in
the the sort of topics and the labels
and classifiers that we generate as a
result of it.
Um,
I also alluded to this a little bit,
like why did we build this? Uh, we've
met we have customers that that generate
uh, massive amounts of data. And one of
the things that I think we solved for
very early on was being able to ingest
that data and then being able to
allowing our customers to query over
that data in in sort of sub-second
speeds.
What we need What we didn't necessarily
have at the outset was the ability to go
do something with it, right? And this is
where that active observability comes
into play. Like
>> [snorts]
>> how do we now go derive insight from all
of this data, especially this data at
scale? This is where that the challenge
comes into play. And so if you have this
really complex pipeline that has been
architected to both run at scale, um and
I mean that from a technical perspective
as well as a cost one, uh like I alluded
to earlier, then we can actually provide
a I think a really interesting primitive
and foundation that our customers can
build on to inform that flywheel.
Um at the end of the day, the the the
thing that we're trying to do is
enable our customers to build that
flywheel and to build it in a way that
actually um
improves their agent quality and they
can do it very, very quickly.
All right. Hopefully I I didn't lose
anybody there in the in the presentation
and you all are ready for
workshop. Um quick show of hands,
anybody still
need the QR code or the URL for the the
GitHub repo?
Yeah.
Yeah, I'll keep it up here for
30 seconds or so.
>> Uh my team uses Lightstep.
I think Lightstep kind of sucks.
Can you give me a list of things that my
team says, "Well, why should we use
BrainTrust instead?" That I can go to
them and say, "These are the things that
BrainTrust gives you in the likes of the
town.
>> Oh, man, you're going like straight
competitor here, huh? Wow.
Was not prepared for for that. Uh I am
I'm certainly not the guy. Like I will
not be up here bashing anybody. Um
I I do think that we
we have a a stronger offering and I
think we have a stronger offering in a
in a lot of different regards.
Um certainly not in any particular
order. One of them is the the
flexibility that I showed to you on the
other slide. There is the ability to go
across multiple languages, multiple
programming, excuse me, multiple
programming languages, frameworks. Um
It's a very agnostic way to build your
agent. Uh LangSmith, I think, has some
of that as well, but they are definitely
geared towards LangGraph and
uh LangChain and deep agents and and
those types of things. And I think they
have features that are only sort of for
that.
Um the other thing that I think if you
go back, actually I used to have a slide
on this, but
BrainTrust built their own database in
late 2024. And and the reason that we
built this database is is Ankur, our
CEO, recognized very early on the
trajectory that we were going in from a
agent perspective.
And
so he we were using ClickHouse behind
the scenes at the time and recognized
very quickly when we onboarded the likes
of, you know, the the customers that you
saw on there, Netflix and Microsoft and
Dropbox, that they ClickHouse just very
quickly fell down at scale.
And we had to go do something different.
And so this is where the engineering
team and Ankur built BrainStore. This is
our own purpose-built back end. I think
at the time people thought we were
crazy. They thought like, "Hey, there
are all of these like open-source
alternatives. There's ClickHouse. Like
there are these things that actually, um
you know, allow us to do this and do
this well."
What you now see, and especially like
you probably see see on the LangSmith
side, they've just built their own
database.
Um
Arise, they just built their own
database like 6 months ago. I think
people are starting to recognize uh that
this is actually a problem that's not
solved for with out-of-the-box
solutions, and you need something
custom. And so, in that regard, I think
we're like a year uh ahead of some of
these these competitors.
And where that shows up is is in topics,
is in being able to generate real
insights on data at scale.
Um there there's probably some other
other ones. If you want to, you know,
come find me afterwards, we can we can
get into it, but um I'd say that that
last one, like the having our own back
end, and the things that we were able to
build on top of that, has really what is
really enabled us, I think, to separate
ourselves from other players in the
space.
Yeah.
Yeah, you.
Yeah.
>> [snorts]
>> Yeah, I mean, like during the workshop
sorry if if anybody couldn't hear that
the question was just like examples of
topics and a little bit more insight
into how into perhaps the the process
and
are we actually generating anything that
is
meaningfully different because the
traces are relatively the same. They are
going to be semantically similar.
Um
I think you'll see this in the workshop,
hopefully.
Uh I think the the customers that are
using this in production would would
probably disagree with you. That's why
they are using it is because they are
they are seeing those those differences
and they are seeing those show up as
different classifiers, as things that
they they weren't yet aware of before
actually running that pipeline.
Um I I think part of it is just like is
getting your hands dirty a little bit
and actually putting in your actual
traces. Like I have dummy demo data
where I've, you know, used a script to
hopefully create some differences that
we create this.
I think you naturally see even more of
that when you have actual users interact
with the agent. Um the traces look
probably somewhat similar, right? We're
invoking the same tools. It's going
through the same uh
workflow.
But I think, you know, depending on what
your agent is doing and what your users
are doing with your agent
and I think maybe to back up a little
bit, I think a lot of us are building
agents that are increasing in complexity
or they're building systems that are
increasing in complexity.
And it creates, I think, some some
differences that that will show up on on
screen. But
you you'll see when you create an
account, you actually have
you have a free account. You can send
data up to a certain point. You can even
toggle on topics to see if it is
actually generating some of these
things. So, we'd just encourage you even
after this workshop to go play with it.
Um and and see if it does generate some
interesting uh topics for you.
Yeah, go for it.
>> bring your own traces
as you are not showing to your customer
using your own data.
>> Yeah.
Yeah, the the question is like
uh can we can we use topics perhaps on
like uh our own sessions with Cloud Code
and Codex and and so on? Absolutely. One
of the things that you'll see if you go
to our integrations page is an
integration with Cloud Code, integration
with Codex, uh Cursor,
Open Code. And so you can I'm actually
working with um multiple customers right
now where they are trying to do exactly
that and layer topics on top of that. I
I think a lot of I don't know exactly
where the question's coming from, but I
think what I've heard is that most
engineers today, most teams of engineers
are using those tools and there there
needs to now be I think insight into the
efficacy or how well these things are
actually improving the workflow and and
and those types of things. And I and I
think there's
there's probably some machinery that
still needs to be put in place, but if
you're just looking to hey, understand
what people are doing in those those
different tools, I think topics is a
really good way to start to understand
that.
Yeah.
So we have uh we have a few different
hosting options. One is just full SaaS,
that's what you're all going to be using
today.
Uh we have both a BYOC and a hybrid
model.
Um and so maybe to like back up even
further than this or than the question
is like BrainTrust was actually
architected from day one to support a
hybrid uh deployment. And so by that I
mean uh the control plane, the web app,
right, the the metadata that we store is
always going to be hosted by us. The
data plane, so your traces, your data
sets, your experiments can actually be
hosted within your VPC, within your
infrastructure. Uh we deploy across all
of the major cloud providers. Um but
yeah, you actually we have, you know,
those customers that you saw up there, I
would wager that 90% of them are uh
self-hosted ones.
Yeah. Yeah, sorry. Green shirt.
Yeah, so the the question is like how do
you handle long-running conversations
with topics?
Uh some of it is I can I'll be show you
this during the workshop, but there are
different settings that you can
configure that operate on
uh they can operate on different traces,
that can operate or can only be invoked
after a certain time period. Uh so
depending on like generally speaking, I
think there's an understanding of how
long conversations tend to last that
tends to inform the settings that you
create. But there's I don't know
getting into the workshop probably
answers that a little bit better. Uh but
I think we can answer that one.
Cool. How about one more and then we'll
jump in.
Yeah, this this the preprocessor, we
give you a default one. You can bring
your own custom preprocessor.
Uh you have data that exists outside of
uh what we can parse uh from input and
output or what what's going to and from
the LLM. You have stuff that's in
metadata. You have stuff that's within
some other span that maybe we're not
sort of
pre processing as part of that default
preprocessor, you can absolutely create
your own.
Uh the other one again like I think I
mentioned was the facets. You can bring
your own facet. You can build your own
uh thing that you're trying to
understand or to derive patterns of
within BrainTrust. But yeah, this I
think one of the the other really cool
things about this pipeline is it's
completely hackable uh in the best sense
of the word.
Cool.
I see a 30-minute timer. I think we we
have till we have till 11:00 though.
Cool.
All right, so I'm going to assume
everybody has the the workshop
or the the QR code here or at least the
the access to the repo.
Is that we zoom in a little bit?
Okay,
this could be a little bit different
based on you having a BrainTrust org or
not.
Like I said, Noah is back here and can
help if you if you run into anything.
Also, you know, if you want to like just
yell at me for a little bit that's
that's fine, too. So obviously the first
thing that will need here is a is a
BrainTrust organization and it's all
I'll sort of walk walk through this this
guide with you all and and we'll start
to understand exactly what I just
described there. We want to create that
flywheel and I think we'll we'll focus a
little bit more on the online side, but
just know that there is the the flip
side which is the e-vals and I do have
an e-val as part of this that we can
also chat about.
All right, so
a little bit of a a teaser there that
was not meant to do that, but we will
create a new organization.
Um if it if it's your first organization
that you've created, uh you're going to
navigate to that that link. You may have
some different steps at the outset. It
may actually uh ask you to provide some
AI providers and a uh generate an API
key. Please go through that. I also have
steps for those as well. Uh you just see
a slightly different uh flow because I
already have organizations created here
on the BrainTrust side.
If you see if you see a screen like I do
now? Quick raise Raise your hands.
Do most people Are most people just
creating a new Braintrust org for the
very first time?
Okay, cool. Awesome. I love to see that.
Um we created the org. Is the next step
to create a project?
Sorry?
Oh.
Internet issues. Love that.
Okay, so nobody can participate.
Okay, bummer. I don't know if anybody
was here last year. We had the exact
same
exact same problem.
Um well, we'll just go through this
though, and
I will try not to go too fast
knowing that nobody else is is doing
this here, but
So,
you'll see that you we we created an
organization. Uh you'll also see where
we automatically created a my project.
Uh you can you can delete this if if
you'd like. Uh we're going to create our
own project for uh this workshop.
Uh
I would label it this, AIE-workshop.
All of the sort of code in the repo
uh
assumes that you have done this. Now,
you could certainly uh not do this and
then change some other things in the
repo, but I just wanted to call that out
if you are following along. Uh just know
that you'll need to uh make sure that
the project that you've defined here is
also matching what you have within the
repo.
So, the the other two things that we'll
need to sort of complete this is uh one,
we will need to generate or create an AI
provider.
Uh so, if you go over to Braintrust and
into your settings,
you'll see a uh a place where you can
actually configure your AI providers.
Uh
I'll click this one up here.
There there should be a lot of different
uh places for you to add
some type of API key or uh what we just
released very recently is workload
identity federation for some of our
major AI providers.
But you can also
our organizations tend to also do or
where I see them also build is like
they'll have their own gateway. And they
want to connect their their gateway to
BrainTrust. They could do that using a
custom provider.
You sort of give the underlying spec
that that gateway sort of conforms to
how we are authenticating to that and
some other sort of URL authentication
type. So generally speaking you can
connect to a lot of different AI
providers in a lot of ways. I haven't
seen anybody not be able to connect to
anything
from from BrainTrust. The the other
thing maybe just to
if if you are sort of following along
and you are using a gateway but that
gateway has perhaps some firewalls
you'd probably see some some errors on
this side.
Just know that you know there are ways
in which you can sort of allow certain
IP addresses to those different places
that perhaps only allow certain IP
addresses like a gateway.
Um
I'm going to stop sharing just for a
second so you don't see my API key.
All right, one more I'm going to
generate an API key also.
Okay.
>> All right.
So, just to recap what I just did here,
I went over to AI providers. I added
both OpenAI and Anthropic as API keys.
Uh the reason that you'll need this is
if you do configure online scoring and
you're using judges as part of that, uh
you will need to choose some type of
model. So,
another call out here is that when you
actually invoke those those scores, you
are using your own models to do so. The
only caveat to do that is that Topics
pipeline, which uses our BrainTrust
built-in models um for that complex
pipeline.
All right. So, we essentially just did
uh sort of step zero here. We uh created
a new org. We have a project called AI
e-workshop. We have an AI provider, and
then we have an API key.
Uh if you haven't done this, right? So,
we can now clone this repo.
Looks like I did not update something
in the code.
All right. One more time.
>> All right, anybody thumbs up, thumbs
down, is this okay from a you need to
zoom in?
Cool.
Okay, so let's let's start going through
this. Um
obviously we're going to be using some
some different tooling here to uh to
power this. I am using UV as the the
sort of package manager to install all
of my uh Python dependencies. So, if you
don't have UV already installed, you
would use this command. Uh I already do,
so I'm just going to run
uh UV sync and then add some dev
dependencies as well.
Uh so, that should create a virtual
environment within your directory and
then should install all of the different
uh things that are required to run this
workshop.
The next thing that we will do is uh
create our .env file and we already have
one as a example. So, you can copy that
one over.
And all you're doing in this one is you
are adding an API key that you generated
on the Braintrust side and then you are
adding a default model. Um this is
really only needed if you wanted to spin
up the the sort of chat UI uh or then
run I think evals as well. But these are
the the two things that you would sort
of create or modify within that .env
that you just copied over
uh to to power and run this workshop.
There there's some other ones that you
know, there's some instructions in that
.env file of what you could also uh
change like if you wanted to follow
maybe those best practices that we
talked about earlier of maybe creating
or having a better or higher uh more
powerful judge model, you could do that
as well. Just if you're if you're not
aware
what this should be
there is the
the um this is the the .env that we just
copied over. Again, I'm just modifying
or added my Braintrust API key and then
I added a a default model and this
default model obviously is going to be
something that is accessible via the
providers that I that I configured on
the Braintrust side.
So, if I did open AI, I'm going to do a
GPT model, Anthropic uh Sonnet, and so
on. So, just make sure that these those
two things
uh mirror one another.
The The other thing that's going to be
really important uh
for this workshop is to install the
Braintrust CLI. Uh this is going to
allow you to run arbitrary SQL, to run
evals, to view your logs, to create data
sets.
You think about that flywheel that I
just described,
a lot of those things are are part of
that flywheel and it's something that we
can plug into our agent to actually
start to do itself, which you'll see at
the end of the uh at the end of the
workshop.
So, you'll see over here, I already have
the uh the Braintrust CLI installed. Uh
I'm also going to do a BT setup skills
and I'm going to use Codex. Uh you might
be using Cloud Code or Open Code or
Cursor or Quen or Gemini. That's
supported also, but the idea here is
that we are going to give our coding
agent access to some skills to
understand how to create a data set, how
to run evals, um how to write SQL, and
so on.
Yeah.
Switch to what?
Oh, yeah.
That's a really good idea. Where I don't
I don't think I've ever actually done
that in here.
>> [laughter]
>> Any idea?
>> What is it? Control
B?
Let's do this.
Sorry?
Command shift B?
Type in what?
>> All right.
>> [laughter]
>> I'm guessing you all all were hoping to
see me navigate around a terminal and
not have any idea what I'm doing.
So we're we're all good. This is better
for everybody. Awesome. Sorry about
that.
Okay, cool. The The next thing that we
will do is we will initialize
uh the the CLI.
Um I'm going to do something slightly
different because I have uh
already initialized uh an ending to
OAuth into Brain Trust to access a
different organization.
So I'm going to do
Oop.
So if again, if you already have the
Brain Trust CLI and you created a new
org, uh you'll go through that, and then
you'll just uh select that org that you
just created. So for me it was ABC DPG.
Cool.
And then I will run that BT init, and
I'll look for ABC.
And so this is just going to create a uh
config.json file in the directory that
when BT runs, it knows what org and
project to to access. So you can imagine
uh checking this into your your repo.
All of your engineers now sort of like
have access to um you know, BT has an
easier way to understand what org and
project that should uh run an eval and
query data from.
Cool. Let's
uh now go through uh actually setting up
some of the different things that will
need as part of uh the workshop. Uh I'm
just going to seed a database.
Uh I'm going to skip over this smoke
command, but I'm going to run make
ready.
Um, if you don't have uh, make or access
to to make, there are the actual
commands right below it that you can
also run.
Uh, what this is doing right now is just
just trying to understand, "Hey, did we
set up everything correctly? Do we have
the the Braintrust CLI? Do we have a
Braintrust API key? Uh, do we have a
default model? Those types of things."
So, uh, I think we're all good to go
forward now.
Uh, then just to kind of give you a
sense for maybe the at least in this
case the the trivial use case that we
are that we are powering. Uh, very uh,
simple chatbot, but really what I want
to understand is is it sort of wired up
in the right way? Are we seeing logs
flow into Braintrust? And so, I just
clicked the button in our chat. We
should now see a log show up over on the
Braintrust side with the uh, the
question that we just asked. So, here is
an example trace that was just created
uh, based on the, you know, the the
integration that we have with OpenAI
Agents SDK.
Um,
I think maybe to that to that point, uh,
just to show you like what sort of
integration looks like uh, within
Braintrust. This is obviously a
a single example. Um, but all we're all
we're really doing is is uh, is this.
This is what we're pulling in from the
the Braintrust SDK and we are setting a
trace processor to a Braintrust tracing
processor. Uh, there is also an easier
way to do this. There is an auto
instrument that is a single um, line
change. The the the reason that I did
this is because I'm also using our
gateway under the hood. Um, maybe I
buried that a little bit. Braintrust
also has
a gateway. So, all of those AI providers
that you have configured within
Braintrust, we can now access uh, from a
single interface, uh, which is what
we're doing here, but we have our sort
of uh, tracing set up from our SDK,
right directly for OpenAI agents. We are
setting that trace processor uh to a
Braintrust tracing processor. And again,
this means that all of those traces that
are emitted, all those spans that are
emitted, are now uh going to Braintrust.
Uh maybe we'll just do it Actually, no,
we won't do it from here because that's
not light mode.
Okay. So, I also have uh a script in
here or I have uh code in here to run
evals. And obviously, this isn't like
the the necessarily the point of the the
workshop, right? We're talking a little
bit about observability. But but I think
uh in the context of observability, you
need to think about the flywheel. And
and part of that flywheel is evals. Um
the things that we are able to
understand and derive about what
happened in production should make their
way back to our evals. Uh and so,
there's also within the uh the repo that
you have a uh sort of dummy data set,
right? It has a few uh test cases that
we want to now run through our eval. So,
what we've just done again is used our
Braintrust CLI. We've created a data
set, and we've actually loaded in a
series of rows via that. Um I'll now run
the eval. Again, this will go uh run
through that that data set. It'll sort
of pass each row within that data set
and invoke our agent. And now, we will
store all of that sort of um
uh all that telemetry and the the sort
of results of that of that eval uh
directly within Braintrust. But you
could also imagine this is going to be
incredibly informative when we do go run
that flywheel, when we do go start to
under- stand uh and we go make a change.
Generally, you want to compare it
against something. You want to be able
to understand did I improve or regress
from the last time that I actually ran
that eval.
Uh so, we have Actually, I'll just come
out to Braintrust.
Uh so, we should now see over here in
our experiments page our eval that we
have run. You see the the series of
scores that we've defined for this
particular use case. Uh you could also
see and and maybe I'll come out to this
in just a a bit, but uh we have
different scores, right? Just like I
described earlier, there are there are
scores that are um more more code-based.
So, required tools called, "Hey, I I
have this question. This is what I
expect." Uh then I have maybe a little
bit more of that LLM judge. So, support
resolution and the tool use quality. So,
sort of a series or a um mix of scores
that can provide the right signal for
understanding what's going on with our
agent.
Okay, let's let's get sort of to the the
meat of this, though. The The idea here
is that we can now uh create some type
of signal within our uh within our logs.
So, obviously, we have a single log
right now, uh and we will need to to
generate some data and put it into
Braintrust. But, before we do that,
let's um use those series of scores and
push those into Braintrust so that we
can now configure an automation so that
they can run when logs come into
Braintrust. So, again, I'm going to use
this uh make push scores command. This
is actually going to look for
uh the series of scores that we've
created and push them into Braintrust.
Uh so, there is a way in which you can
define these in the UI. You could also,
like you you you see here, define your
scores in code and push them into
Braintrust. Uh with the idea being that
you'd want to run them as part of an
online automation, uh or perhaps uh we
also have a playground and you could
give that to another user of the
playground and they can use that same
score, but have it version controlled
within your repo. Um again, here are the
series of tools that we just uh Excuse
me, the series of scores that we just
loaded into Braintrust. Uh you should
now see, if you go over to your scores
tab, the different scores that we
created. So, I have, let's, you know,
support resolution as an example, right?
This is going to be
an LLM judge.
Uh and and what you're doing here,
again, is defining that criteria in
which you want to judge something with
the with with with respect to the um
the the the user's interaction with that
agent. Uh one thing I'd call out here is
that there are different sort of
variables you can access and pass to an
LLM judge. Uh this thread is is sort of
what I described earlier. Um it's it's
what you would see if you come over to
our logs page and you click on the
thread,
which is this icon here, but it's it's
really just going to be that back and
forth of that agent, right? This is
really helpful, especially if you have a
multi- turn conversation and you want to
sort of pass the entirety of that
conversation to the LLM, you can use a
variable called thread. There there
there's some other ones uh that that you
could also use like user messages or
assistant messages or simply input and
output from a particular span because
you want to create a score that
understands and scores look up policy as
an example. But, there's a few different
ways in which you can start to think
about how do I start to assess the
quality of my agent across a lot of
different dimensions.
So, now that we have our scores loaded
into Braintrust, the the thing that we
need to do now is actually wire them up
to run when traces come into Braintrust.
Uh what what that looks like on the
Braintrust side is an automation.
Uh if you look in your logs page, you'll
see up here in the top right uh
automations. This is where you can start
to create rules that your scores can be
invoked on.
Um
there are if you if you look at here at
the scope, I think this is is really
important, especially you start to think
about like the different use cases that
you have. Um
you could think I have a multi-turn
conversation, but my uh turns are
actually across different traces. I
don't see them nested under each um I
don't see each turn nested under a
single trace.
So, what I might want to do in that case
is select this group scope and then
provide some type of ID, some type of
way to understand how things are
related. In my case, it's a conversation
ID.
Um the other thing that you might want
to do is create a score that is invoked
for a particular span. Again, you want
to assess some type of intermediate
output or intermediate step, and you
want to target a particular span. When
you do this, when you click span, it'll
default to the root. Um you could also
add any type of filter for I want to
recognize, let's say, my lookup policy,
and I want to say in this case
something like that.
So,
I want to understand if this is is root
or the span attribute name is in lookup
policy.
Uh there's also, again, like the trace,
which is what we will use for this demo.
Uh this is going to allow us to uh
essentially access all of the different
spans within that trace to produce some
score.
Uh so, in this case, I'm going to pull
out my uh communication quality,
and my support resolution and tool use
quality. These are all LLM judges.
So, if you're following along, um just
know that depending on the sampling rate
that you uh that you put here, you're
going to incur actual model compute uh
when you go and and load data into
Braintrust via these judges. So, just
wanted to highlight that. Again, if
you're following along and and perhaps
maybe you want to uh
lower this a little bit. Uh I'm just
going to go to 100% just so you kind of
get a a really good signal or a really
good idea of what this could start to
look like.
So, what what this what what I've just
done now is I've said, "Hey, any new any
new logs that have come into Braintrust,
I want to uh run those scores against
those, and I want to run against the out
the the trace."
Okay. Let's uh let's let's jump into
topics now. So, there's there's one side
of our signal that we that we can
create. This is the more scoped down way
of understanding a failure mode, right?
This is perhaps something that we have
We're obviously eval-ing for. We have
recognized to be something that um you
know, we need to understand if we are
regressing anything as we go and change
something within our agent. Uh topics
again is is more for those unknown
unknowns. Those those areas that we are
not yet testing for or that we're not
yet aware of.
Uh you'll also notice right next to our
automations is an enable topics.
Uh and actually let me come back this. I
think the the first
thing that we'll do here, enable topics.
So, you'll see you'll see a screen that
looks like this. Um and you'll see those
built-ins. So, task, sentiment, and
issues. So, sort of what is what I
described, what are people or users
doing with my agent, what is their
sentiment, are they happy, are they sad,
and then what are sort of like a broad
range of issues that they are
experiencing uh with respect to that
interaction of that agent. So, I'll
enable this.
Um this will apply to existing traces.
Obviously, not a lot of data here, so um
we'll eventually see some data show up
here. The thing that I again
allows you to bring your own way of
understanding patterns within your data
is where you can actually create your
own facet. Um you'll also notice here,
this is where you can also define your
own preprocessor. Uh we're just going to
use the default thread one here today,
but just know that if you wanted to
bring your own function to BrainTrust to
parse something within that trace, uh
you could certainly do that.
So, if you look, there's also a file
within that repo called support workflow
issue facet. It's a markdown file. Uh
this is the prompt that we will be using
for our custom facet.
And so,
back in uh BrainTrust, I'm going to grab
the uh support workflow issue
name.
That will be our custom facet.
And then I want to grab the the prompt
here.
Um the other thing that you'll most
likely want to do is to exclude certain
facet outputs. So, you can see here I've
instructed the LLM to output none when
the following criteria has been met. Uh
what I don't necessarily want to see is
um
facets that are that are generated where
it's like, "Hey, this there's no problem
here." Uh I'm I'm really only interested
in the things that are that are going
wrong. So, I will grab um this regex
also at the top.
And I'll paste it here.
Uh you can also choose to apply to
existing traces.
Um not super important in this case
because we have uh we don't have very
many.
So, on on the topic side, that's that's
really all you need to need to do to um
start to understand whether or not you
can see some patterns within your your
data.
Um
if you come back over to our our repo
here
and you look for a perhaps a different
way. Uh I'm not going to go through
this, but I just wanted to highlight
again the the ability to utilize the
BrainTrust CLI to do a lot of um
interesting things. So, that's sort of
workflow that I just went through in the
UI, I can also do here within uh BT. I
can actually configure these topics to
to run. I can configure those those
automation settings.
Um so, here I've defined my task
sentiment issues and my support workflow
issues. Uh the other thing that I did,
you can also see some different
configurations down there.
There is different ways to configure the
settings, right? So, that pipeline that
runs in real time, you can control how
it runs or
what it runs on. And so, by that I mean
you might want to add a filter. You
might want to say like, "I only want to
run my topic pipeline on traces that
meet this criteria." Uh you may again
want to apply some type of sampling rate
based on uh some understood metric you
have about traffic and uh cost this
could potentially incur, so on.
You also want to understand the the
topic window. Like when I generate my
topic map, what is the sort of range of
traces that I should use based on some
window? Uh this one I'm going to
This is I think maybe the question you
had earlier in the green shirt around
like
how do I how do I maybe configure this
when I have long-running conversations?
Um part of that is that group by scope
is being able to pull in perhaps other
traces that other turns that exist
across other traces. Uh this also is
another setting you can configure where
you want to perhaps, you know, this
could be a day, this could be 2 days.
Like you all understand that the the
conversations that your agents are
having or users are having with your
agents stretch a very um long time
period. And so you can configure sort of
when the topics pipeline gets gets
invoked. Uh I'm going to do something
really short here. Um but again, you can
configure this based on your
understanding of the users' interaction
with your uh with your data. Excuse me,
users' interaction with your agent. Uh
then again, there's the same sort of
scope that that I highlighted with the
scores.
Uh you can have this run at the
individual trace. Or again, if you have
that multi-turn conversation that exists
across multiple traces, you would use
this group and then use that sort of
common um identifier, right? In my case,
uh I have a conversation ID that's being
logged out as metadata.
So I'll click save.
So now we have sort of like the the
topics configured. We've enabled our uh
out-of-the-box ones, and we have also
created our own custom facet, and then
we have configured our automation
settings to uh to be run when data comes
into BrainCert.
Uh on top of that, so now we can
actually start to see what some of this
looks like.
There is a command here where you can
run um essentially the I I have some
trace data stored out in an S3 bucket.
Uh we are going to just import it.
Again, under the hood here, what you're
going to see is BT sync.
So, we can actually take that data and
push it into Braintrust.
Um
maybe to your to your question in the
blue shirt about LangSmith earlier, I've
actually helped a lot of customers
import traces from other providers
because they wanted to like maintain or
still have some of that that data. But,
just highlighting like this is a really
great way to uh to do this at scale.
So, you can see here we just we just
loaded in uh 968 traces.
Uh
1,052 spans, or that's the the rate,
excuse me. Uh 5,260 spans. So, pretty
pretty quick way to get data into
Braintrust. But, again, like the whole
idea here is for us to start to generate
some signal and start to understand
where we can make some improvements
within our agent. Uh so, you'll start to
see like here's uh just some
uh some
examples of traces. Uh you'll also see
that this is the this is actually two
things you'll see here. Um each turn is
actually represented uh as its own
trace. So, this is the the newest user
question and here is the the output for
that question. Uh you can also notice
that there are 11 previous messages. And
so, I might want to do something where I
I pull in my conversation ID.
And so, now I can start to pull in other
traces that are that have that sort of
same metadata. But, the the sort of
OpenAI agents gives you somewhat of a
cheat code where it actually just
attaches all of those previous messages.
So, we don't necessarily have to go
through this step, but just wanted to
highlight another feature within
Braintrust that allows you to group
traces by some arbitrary metadata that
you've defined within those that they
they they share across those traces, and
you can pull all of those relevant
traces into the tree here.
Um really quick, right? The thread view,
I think is a really great way to
understand sort of like the back and
forth
uh of your agent. Uh there's also um
the timeline view, which is a great way
to understand like perhaps where
bottlenecks exist, or you could even see
there's really interesting information
for, you know, cash hit uh across the
different LLM calls. So, this
information, I think, can be useful in a
lot of different types of of workflows.
The the other one I'd highlight, and I
haven't really talked about this yet, um
this little blue icon in the bottom
right is our agent loop. Um everybody
has an agent, right? Uh so, you can
actually use loop to do a lot of
different things across the platform. Uh
you can use loop, in fact, to create
your own UI on top of that trace data.
And so, this is, I think, a really great
way when I was talking about the other
scoring method of I want to uh allow
humans to go and review output of
whether it's the agent or the LLM judges
themselves and provide some calibration.
This is actually something you can
prompt loop with, and it'll vibe code uh
a UI on top of that trace data. So, just
a different way to bring in perhaps
another persona to sort of inform that
flywheel.
Um you you'll also see as part of this,
like we're starting to see some some
automation start to be triggered. Uh so,
we have my uh judge automation, so
communication quality, support
resolution, and so on. And what you
should also see is some topics starting
to be generated as well. So, in this
case, right? We have a user who wants to
check the status of a returned item
refund, and so on. Um we have a negative
sentiment. This user expressed
frustration and dissatisfaction with the
status of a pending transaction.
Here's my support workflow, my custom
facet here. There's an order record
retrieval failure. Both specific order
ID lookups and broader customer searches
failed to locate the order.
So, just wanted to you know, two
different things here, right? We loaded
traces into Braintrust, and based on the
sort of automations and topics we've
configured, we are now starting to get
that signal in real time. Right? So,
that complex pipeline that generates
patterns within your data it shows up
immediately. Right? It shows up um based
on how you've configured that pipeline,
obviously. But, this is the now the
signal that we're going to be able to
use. Um while this while this starts to
uh populate, I'm going to go out to
another project where I where I already
ran this. Um so, I showed you some
illustrations earlier of what this uh
perhaps starts to look like um within
Braintrust. So, at the top here uh in
this page, what you start to see is a uh
snapshot in time of your of your topics
and the frequency with which uh the
traces that we have recognized some
pattern in patterns in, where they are
being grouped.
And so, in the first example, I'll
expand this.
Uh I can understand what users are
trying to do with my agent. Right? I can
see at the top uh damage and transit
resolution seems to be uh the most
frequent thing that again users are uh
using for my agent. And this is I think
going back to what I was describing
earlier when I was in the slides is I
can actually use some of this
information to understand like perhaps
where my agent can actually go um
further or the thing that I don't yet
have built within my agent that users
are trying to do. Um all of this taken
together will will be used to sort of
inform that flywheel. Um a little bit
further down, I have my sentiment topic.
Uh my issues did not get generated. The
The reason this didn't get generated is
because we we look for at least 100
matches or 100 facets that were
generated as part of that pipeline. Um
and this sort of agent that I built and
the out-of-the-box prompt that we have
for issues don't exactly jive or match
and we don't really generate um
we don't we don't really generate facets
as a result of that, but I I that this
is a sort of a good thing. Like, we
don't want to just generate bad data. We
don't want to just generate signal that
you can't actually go do something with.
And so this is where I've created my
support workflow issues.
And in this case, I'm starting to
understand, hey, there's a record lookup
failure. There's something going on with
my agent
that we haven't again recognized with
our evals, but we are understanding that
there is a lookup failure as part of
that agent going through its process.
Right, this is the kind of information
sort of all taken together. This with
the the context of our online scores
that actually allow me to go do
something with it and and improve my
agent in some way.
Any questions?
Cool.
Okay. I want to show you sort of like a
a workflow that that I think, you know,
I certainly did when I when I first
started at BrainTrust and I think a lot
of lot of folks um
they did as well, right? We've generated
that signal. This is great.
Um now I need to be able to go do
something with that. And so I think, you
know, obviously within the the
BrainTrust UI here, there's a lot of
different things that I can utilize to
start to understand or again filter
through that noise.
Um I might want to look at, you know,
the the different um
classifiers or the different labels that
were placed on top of these traces,
right? That map to those topics that you
saw in that other illustration. This I
can use, right? To filter this down. Um
probably increase this.
No.
Uh this I can use theoretically to
filter this down in some way, right?
Based on the the the feedback that we
are getting
uh and understand
the thing that I can do from there,
right? So like I filtered my result set
down.
I'm drilling into a trace
and I'm recognizing by kind of parsing
through the trace and the spans within
there
what went wrong.
Um maybe I'm again using my online
scores to filter this result set down
again, perhaps even further.
But I but I think like that the workflow
that you might go through is you'd use
this UI and you'd start to understand
all the different things, like all
what's going wrong. I'm going to take my
task X and combine it with this
sentiment and I want to see what sort of
insight I can derive from it.
Um obviously generating the signal,
really great. We have a lot of data now
that we can actually go make some of
these informed decisions, but I think
you all can probably recognize the the
problem with that approach as well. It's
like I am very reactive. The the onus is
on me as a user of Brain Trust to like
go through and click buttons and filter
and then parse through these traces.
Like there's got to be a better way. Um
I might want to use Loop. Loop is a
right again, the agent that is embedded
here within the platform that can do
different things. Um I asked it in this
case, help me understand what I should
improve in my support agent based on
recent logs.
So one of the things that you'll start
to see that's I think again, really
interesting from a uh flywheel
perspective, is how we can start to pull
in relevant data to inform that
flywheel.
Um
another thing that I think is again,
really interesting
about Brain Trust and specifically Brain
Store, the back end that powers it, is
that you can write SQL directly against
it. All of that trace data, all of those
spans can be accessed by writing SQL.
Um you may not want to write that SQL,
but your coding agent can very very
easily write that SQL. And so what
you're seeing happen here is Loop.
Again, Loop is our our agent in the
platform. I asked it a question and what
Loop did is it started firing off a
bunch of SQL queries. It's pulling in
context that is relevant for the
question that I asked it. What you're
probably not able to do and again,
thinking at scale, you're not going to
pull in every single trace searching for
signal, right, using your agents, your
coding agents.
You need that signal attached to your
traces in some way, and you need that
signal to be real.
And then you need a very flexible way to
start to query across all of that data,
so you can only pull in that relevant
bit of information.
Um the the last thing that you you don't
see in this one, but you'll see a little
bit later, is once I find those
interesting examples based on the signal
that was generated, I now want to go to
this.
I want to investigate that trace. I want
to click into that span. I want to look
at the input. I want to look at the
output. Right, this is the kind of
analysis that I would probably do, but
I'm not able to do at scale. But if I
can offload some of that again to loop
to inform what I might go change or
might might go fix or might go add, or I
could offload to my coding agent, this
is the kind of thing that actually I
think drives agent quality in a really
efficient way.
Um so, I'm going to skip through some of
this, but sort of what I described here
is using topics and scores to understand
and and to like actually parse through
that that data based on the signal.
Um what you might also do now is you
might actually use that that filtered
set of data. You actually found an
interesting example, and you want to go
add that to a data set, right? The thing
that allows us to now go improve that
agent. I want to go bring that example
back to my offline evals. Right, I could
do that here from the UI. I'm going to
add this to my data set. Now I have this
sort of edge case, this thing that I
need to go and sort of improve upon or a
new feature I need to add based on what
I've seen with this user's interaction
of my with my agent. I can go add that
back to my data set. But again, like the
thing that becomes important here is
adding the right thing back to the data
set based on the signal that was created
within within our logs.
And then of course, you'd go and you you
guys don't want me to see me code and
and figure out if I can improve the
agent. But once I once I did, I'd go run
my eval again. I'd go compare that to
the last time I ran the eval. Did I
improve? Did I regress? That new example
that I pulled in, did I make it better?
Did I actually improve those scores that
I ran in an online sense? The other
thing that you might want to do is like
you actually recognized these new edge
cases, you probably want to go create a
score. Right? I have a record lookup
failure. That that seemed to be the the
problem that I encountered the most. I
probably want to go create a score that
allows me to capture that before go
before pushing my my agent to
production. So, there are all of these
steps, right? These things that you
would probably want to do to create that
flywheel.
And what I think becomes really powerful
here is when you can run this in an
automated sense. When I can plug a skill
or I can plug some type of workflow
using all of the primitives that I just
described to automate all of that.
And so if you look here at at our
workshop markdown file, there is a
GitHub repo for skills that that we have
out there. There's actually a single
skill at the moment. The idea is to give
your coding agents the ability to run
that automated flywheel. Right? We want
to actually go through that exact same
thing. I want I want Codex or Cloud Code
or whatever to write SQL. I want it to
view traces. I want it to view spans. I
want it to create new scores and run
evals and modify something within my
agent and I want to do that, you know,
watching my my screen. Yeah, go for it.
Yeah, the the So, if you look at my
If you look at my eval that I've created
So,
this is this is sort of what an eval
looks like in in Braintrust.
Um your data set here is actually part
of like the the commands that we ran at
the outset was to load our sample data,
like our series of test cases into
Braintrust. But but you could also
imagine like this is at the outset, this
is like my sort of scope down view of
the world in which my agent operates,
right? These are the test cases that I
want to give to it to understand, "Hey,
should I go push this thing to
production?"
But the the sort of like operation of
the thing that I'm describing here is
that
the
where you start to improve the quality
the most is is when you can curate
traces, curate examples from production,
and bring those back to your your data
set. So, this right here, like this sort
of like very sim- simplistic workflow,
is what I was describing.
This pin this um this record here, this
row, this trace, it perhaps is
indicative of some failure mode. And I
want to bring this back to either an
existing data set or a new data set that
I want to run an an eval against.
Correct.
Um
so, I think like the sort of culmination
of of all of this is
uh how we can uh use all of those those
sort of primitives that I described
earlier. I think the topics pipeline uh
running behind the scenes is is kind of
the the star of the show. Um the the the
importance of adding to the the data set
though is
your your evals should evolve with your
agent. And when when I think about
evals, I think about a data set. I think
about my agent, right? So, it's like
function that invokes my agent. And then
I think of the series of scores that
allow me to understand good or bad with
respect to those test cases being passed
to my agent.
But, when I create my eval set,
it's a very sort of like
it's a way for me to establish a
baseline. It is certainly not
representative entirely of what users
can do with my agent.
And so, by me adding new records to that
data set, it allows me to capture
different perhaps failure modes over
time and
go make changes within my agent so that,
right? We don't we don't continually
experience those those issues in the
future.
But, it's it's more about like the the
evolution of your agent and ensuring
that all of those sort of like things
that come along with your evals evolve
with it.
Um so, that you can one capture new
things, but also like as you go change
your code, you're not regressing based
you're not regressing your agent based
on previous interactions that you sort
of curated into that data set. Um
there's there's a few different ways to
uh install this. Uh I'm going to choose
just the top one.
>> [clears throat]
>> Uh so, if you have the the GitHub CLI
installed, you can use that. Uh there's
also uh NPX.
And there's just cloning the the repo
locally and and following the different
install so, like with respect to the
agents that you're using.
Okay.
So, we we have the the skill file. We've
installed that.
Um so, now I might want to just like run
this this flywheel. I want to see this
in action. So, I'm going to I'm going to
do two different things here.
I'm going to run this.
And then I'll actually show you um a
previous example so you're not just
sitting here watching Codex run.
So, we'll do that.
We'll let that run. I'm going to go out
to
another repo.
Okay. So, same same prompt. Um, and
actually let me, I think I sort of
skipped over one thing here that I think
is probably important to
highlight. Right, the actual, uh, logs
here that were generated or like the
topics that were that were generated.
So, we should now we have all this
signal, right? This is the thing that I
just, um,
executed Codex against this project. It
should now be able to pull back all of
these different things, right? these
tasks, these sentiments, uh, this
support workflow issue. All of this and
these scores are attached to those
traces and are now part of this
workflow.
So, we'll let this kind of go, uh, in in
this in this terminal over here.
All right, we'll we'll come to this one
as it's running.
So, sort of like what you saw in in the
loop session,
uh, what you'll start to see here
is, uh, Codex writing SQL commands. So,
BT SQL
and we're going to pull back all of that
information or the relevant information
into the session. And so, we can
flexibly query across this project now
and across these traces
and we should be able to also recognize
and understand or Codex should be able
to recognize and understand those topics
and those, uh, those scores that were
run.
Um, so we have, you know, you could see
here we have 968 support traces, that's
exactly what we loaded in. There are
scored failures, a visible cluster of
escalate to human tool errors.
Um, I'm going to inspect the classifier
outputs and representative failed traces
and turn that into a concrete summary.
So again, the ability to flexibly query
with that SQL tool
uh becomes pretty impressive. Uh looks
like it was able to recognize something
with our scores. Uh and then is, you
know, continually querying. And then
this is what I described earlier of
actually being able to drill into the
individual trace. So, it found
something. It found some example that
would allow us to um improve our agent
again in some measurable way. We want to
view that trace, write some more SQL, um
but this is really what allows us to be
very comprehensive and and actually
pulling in all of that really rich data,
uh but only pulling in those things that
are actually going to drive uh some some
change that we can make within our
agent.
Okay, so let's see what what else we
just did here. Um looks like we're
looking at how to run evals. We are
viewing existing data sets. Uh we just
created a a new data set. Actually,
we're in the help command. Um but but
hopefully what you're able to see here
is this.
This is what we're trying to create.
This is what the This is what like the
the primitives in
uh in Braintrust. Our topics, our
Braintrust CLI, the backend allowing you
to write SQL, uh having a platform that
does both evals and observability. Um
all of these things sort of taken
together allow you to again create that
that flywheel and then do so in a in a
really meaningful way.
Um
more than happy to take some questions
right now. What's it's really just
waiting a little bit on
Codex to to cook, but
curious if if anybody has Yeah, go for
it.
Yeah, we have a hybrid deployment. So,
it means the data plane, so where all of
the data resides, so your traces, your
experiments, your data sets, they would
remain in your infrastructure, but the
control plane, right, just like the web
app that you're looking at, uh, would
stay with us.
The The hybrid deployment is only
available for the enterprise plan. Yeah.
Um, to that point, just if you're
curious, like there's two different
flavors of that. There is a BYOC one,
where, again, data plane is deployed in
your infrastructure, but we manage it
for you. Then there is more hybrid,
deployed in your data plane, your team
manages it. We have sort of a a
Terraform provider or Helm charts based
on, uh, the the the cloud that you're
on.
Back of the room? You don't have to
yell.
Um, I I think for the for the most part,
and I think this is changing a little
bit, uh, folks are using more of the,
uh, the models from the the big model
providers. Uh, that's generally what I
see. Um, I I think that's that's
starting to shift a little bit. Um, I
know like at the outset, it it was very
very heavily skewed towards the the
major model providers.
Um, I don't know like specifically, I
haven't seen small models necessarily,
but I have seen folks start to, um,
perhaps fine-tune their own models and
and see if it can't drive, you know, the
whole idea, again, like beyond behind
it, like evals, as as one example, is to
be able to understand if I can swap in
and out models without sort of
introducing regressions or, uh,
deteriorating quality of the agent. But,
yeah, I'd say largely it's it's the the
major model providers, perhaps maybe
shifting a little bit.
Sorry, is this like for an LLM judge?
Oh.
Yeah, so
uh important callout, um
could actually see it probably back at
at this screen when you're looking at
the
uh topics automation settings
and advanced.
The The The only option you have for
both the summarization and vector
embedding step are Braintrust hosted
models.
Um
the there's a couple reasons for that.
One is that we we've trained trained
these models to do specifically this.
And and two, like the the complexity of
the pipeline
sort of um
makes it so that you can't just
necessarily plug in any model and and
and hope to achieve similar results.
Uh we started off by allowing different
models to be plugged into that, but the
the topics pipeline or the topics that
were generated as a result of that just
were not were not good. And so, we have
enforced it so it's only Braintrust
hosted models for this step.
Yes, you can. Um
I can go out to
Uh so, because all of that uh
all of that data exists as metadata
essentially on top of the trace.
You can pull it out for different uh
visualizations.
So, I think in this case, I have a saved
view. Um and just, you know, some some
brain trust stuff here.
Uh if you wanted to create your own sort
of dashboard or your own view, uh this
is how you would do that. Uh all of
these views are like uh you can save it,
you can create your own custom charts,
but uh up here at the top, you can see
sort of sentiment over time, tasks over
time,
top sentiments, top tasks, like the
things that you've built custom uh can
be pulled out in here. Uh you can see
that like in this case, I'm looking for
classifications.sentiment
is not null, and I'm grouping by that
label. So, these these become pretty
simple to to set up. Yeah, I think so
this again, grain of salt. Uh generally
speaking, what I've seen though is like
uh newer agents or newer things that are
just being pushed to production have a
higher sampling rate. And over time,
those sort of like known unknowns or the
things that your scores tend to surface
become less and less, and the signal
that you derive from it will will also
become less. And so, you start to scale
back that sampling rate. Uh I I think
there's also if you're doing things with
an LLM judge that is a little bit more
on the classification side or on the
taxonomy side, you can look to alter or
you can look to swap that out with
topics. Um
Dropbox is a customer a customer that I
work with, and they have this like very
complex series of classification scores
that they run to understand some
taxonomy
uh with respect to their traces.
And they have experimented with uh using
topics to do that. Um one because
actually the most important reason for
that is is it's a much more
cost-effective way to run across the
majority or 100% of their traces, where
the LLM judge just was not able to scale
to that. You're you're able to generate
as much signal. So, I think there is to
maybe to summarize, there is a maturity
that I think informs what the sampling
rate should look like. It tends to scale
back as the maturity of that agent
increases. And then there is
the types of things that the that your
LLM judge might be producing. If it's a
little bit more on that classification
or taxonomy side, you can look to swap
that out with with topics.
Yeah, so not directly within the UI, but
you could create a code base score.
Right? You could imagine like I invoke
score one.
Based on score one's output, I go do
something and I invoke score two. The
return of that function is an array of
scores. Right? It's an array of score
objects. But it's yeah, it's certainly
possible, but you define it within code.
There's nothing within Braintrust that
allows you to say, "Hey, I want to run
score A
based on the result of that, I want to
wire it into score B or C." But it is
certainly possible just to create it
within code.
Oh, yeah. You could you could also just
um your filter could look specifically
for the presence of that score span and
then only be invoked when when it when
it's there. Yeah.
Um I forget the the customer, but this
was surfaced the other day and it was
more on the on the task side. Um I don't
remember specifically what it was, but
it was actually something that they
didn't realize that users were doing
with their agent. So, it was more of the
use case of like uh feature request or
um you know, unknown unknowns, but with
respect to
what users were doing with their agent,
not necessarily a failure mode. And I
think that's been the perhaps the most
surprising thing for me is that people
are using it to uncover those types of
things. I think when I was starting to
like play around with the feature and
talk to customers, it was
you know, the the majority of it was was
for me at least focused around the types
of issues that you would be able to
uncover, but I think there's just like
such a broad range of patterns that
you're now able to sort of
uh
attach to your traces and then use those
sort of patterns together to inform
something about like the the world that
you didn't know about your agent. Um so,
yeah, it's I don't have the exact
uh
thing that the
uh topics uncover, but it was much more
around like, "Hey, I didn't realize this
uh these users were using our agents or
trying to use my agent for this."
Um right now, I would say they're
they're like use case driven or you
could even imagine
uh agent specific. So, in my case, I
have this support agent and in my
project, I am writing my logs for my
support agent into my support agent
project. I'm also storing the data sets
that I'm running my evals for my support
agent. I'm also storing the scores for
that support agent in that project. So,
they tend to be a uh
a a container for relevant resources for
a use case use case or an agent. Uh we
are introducing very soon a a sort of uh
first-class agent object into the
project and so, you could imagine maybe
there is a multi-agent system and you
want all of the agents' logs to go into
the same project, but still have some
delineation between agent A, B, and C.
Uh so, you could imagine doing that as
well.
>> Um yeah, so the the sort of monitor page
that I showed earlier is uh
project scoped.
Um if you wanted to create a more like
organization scoped view, you'd have to
uh create queries and pull data out of
BrainTrust.
Um that'll eventually change. Uh it's
more
How do we How do we allow our customers
to do this?
at scale. Um you could imagine trying to
query across
however many different projects and
pulling that data into a dashboard uh
becomes a little bit challenging. So,
yeah, at the moment we are
uh project scoped, but you could imagine
that that that's starting to change over
time. I mean, I think that's probably
fair. Um
I I think maybe what you'd potentially
see is your your evals
changing um
as often as you are changing the agent.
Like and it's probably perhaps it isn't
even that frequent, um but I do think it
does have the prospect to change in some
way
based on what you're able to infer from
users interacting with that agent,
right? Like this could be This could be
a prompt. This could be a tool. This
could be a new tool. This could be um
something within the runtime or the
architecture that that needs to change.
And to me, like what I've seen more
frequently is that your evals will
generally change as a result of
something that you are change Like
obviously if it's a simple prompt
change, like you're probably not
changing a lot within your evals outside
of maybe curating some new examples into
that data set. Um but but I do think
what I've seen is that
agents tend to evolve um
somewhat frequently, and I think if you
are being informed by actual
interactions with uh with users in a
real way, maybe they're actually
changing a little bit more than you'd
expect. Um but yeah, I I do think it's a
fair, sort of, uh piece of feedback
where
uh
the agent isn't very complex. It doesn't
have, or it's not, you know,
it doesn't necessitate a lot of changes
based on the scope of of what the agent
is doing. And so, the evals may not
change too much as a result of it. Uh I
do still think there is value in being
able to
generate that signal in production of of
what's going on. Um especially if you
can do it in a cost-effective way,
then then, yeah, it becomes like that
part of it I still think there's there's
value to.
Yeah, like I I have customers that do
both. Um
I I I think some of it's preference.
Some of it um sometimes is just not
understanding what Braintrust can do.
Um
allowing So, like the the codebase
scores, I think, is a really good
example of this, where you may have a
really complex codebase score that uh
uses different Python dependencies or
TypeScript dependencies,
and you need to run that, or you think
you need to run that in your own
infrastructure, because you have all of
these, sort of, like, complex
dependencies that are powering it.
What you can do within Braintrust, when
you when you go push a score, and even
when you push a codebase score, you can
bundle dependencies within that push.
And so, the things that that score
relies upon can still use those. And I
know some customers that I've worked
with just didn't understand that they
could they could do that. Uh to me, the
value is, like, not having
some of that, like, asynchronous code
within your own codebase that um looks
for those triggers, or is like it looks
for, "Hey, this trace was generated, and
I need to wait 60 seconds from the last
event to go, sort of, be invoked." And
so, to me, the value is, like,
offloading some of that complexity into
Braintrust. Though, you still can do
that. Um one of the, I think, unique
things about, like, the Braintrust data
model is that you can actually update
spans in in
So, if that span already exists within
BrainTrust, it is mutable. And so, you
could add you can you know, change the
metadata, attach scores, attach
different metrics.
And so, if you wanted to do that in
code, you had sort of like the
um you know, the machinery in place on
your side, it it becomes pretty trivial
to go and like, "Hey, I have this span
ID. I want to go attach these different
scores and metrics to it."
So, I think some of it is just like it's
preference. Um some people just want to
have a little bit more control,
perfectly fine. Uh you can certainly do
that. So, to me it's a
one it's
our back probably. Like you you still
want to like be able to write some of
that trace data and then lock down who
can see it. I think that workflow that I
just described is is a like that
flywheel, that automated flywheel, is
actually a great way to do that because
I can surface insights to people. I can
generate a PR based off of all of those
insights, but I don't give them access
to the underlying traces. I give them
access to the analysis of those traces.
Here are the SQL queries that I ran.
Here is the aggregate data that I pulled
back. Um if you have just like no engine
engineers are able to actually view that
data, write it to a project that nobody
has access to, um lock it down from that
perspective, but then create sort of a
service account that is actually able to
like go run that sort of flywheel on top
of it, so you don't lose access to all
of those insights.
Yep.
Most underrated features. Um
My guess is the BrainTrust CLI is very
properly rated. I I think I I
I'd tout that uh any chance that I can
get or I uh tell any engineer. The
reason I say that is because I think
we we released it in late February. We
had a user conference.
Um and I still think like I'm going out
to customers today and I'm asking like
are you using the Braintrust CLI CLI?
Are you using it? And some of them still
aren't. Um, but to me, most like I'm I
would wager 100% of you are using some
coding agent, right? Like this is how
you are coding today.
Um,
having the CLI as part of that, like I I
hope you were able to see some of the
like types of workflows that you were
able to create. Um, to me it just is it
becomes so incredibly compelling. You're
already in a terminal, you're already in
your IDE, whatever it is.
Uh, use the CLI, attach that or or give
your coding agent the skills to
understand how to use that.
And then use that to augment your
workflow. Um,
the other one that
the other one that could be like
somewhat compelling, it depends I think
a little bit on your your organization
and the different folks contributing to
that flywheel.
Uh, we have a feature called remote
eval. It's a way for you to expose that
eval to a playground. And this is more
like how can I perhaps uh, like in this
scenario, there are perhaps subject
matter experts, there are product
managers, there are folks sort of like
contributing to that flywheel in some
way. Like they are modifying prompts or
they are doing some of that hill
climbing. And we sort of crafted like
all of this um,
you know,
the these applications for them to go
plug into in a low code low code type of
way. The remote eval allows you to
expose that eval that I showed to you
earlier that like eval with a task and a
data set, you can expose that to a
playground
with parameters so that the user of the
playground can actually go and start
changing the system prompt or a tool
description or something like that. Like
why that might be interesting for an AI
engineer is that you don't necessarily
have to be sort of like the bottleneck
in producing applications or uh,
producing something for a product
manager to go plug into and allow them
to modify a prompt or contribute to that
flywheel. So, maybe not as
not as impactful as the CLI, but
potentially given your organizational
structure could be. I think I got most
of that. Tell me where where I'm off.
I I think like the the thing that I
that I started doing here is exactly
that. Uh like Braintrust itself, at
least at the moment, doesn't have access
to your code base, right? It doesn't
understand like what you've written and
based on the information it has, it
can't go recommend a change necessarily
to specific functions or agent
architecture.
But when you bring the um Braintrust CLI
into your sort of coding agent, and then
attach that obviously like I'm I'm
within my repo here, I'm able to now go
through let's see if we've been able to
like get something here. So, in my
session,
uh based on what I've been able to sort
of understand, we are creating new new
scores. So, there's a score change.
Um there's we can skip the tests.
There is uh looks like newer tools that
we were able to add to our agent again
based on some of that insight.
So, I I think like the the answer to
your question is like
this is absolutely possible. What what
I've just sort of demonstrated here is
that flywheel of like, "Hey, figure out
what's going on in production, use my
scores or use my topics because I have
sort of attached
information of
you know, issues or sentiment or
whatever it is, this becomes incredibly
compelling now or interesting for that
agent to pull in, and then go modify
your agent in some way. Um
I think eventually as you get further
down here,
see now we have new examples to our data
set.
We have uh looks like we've created a
new data set with those examples. We're
now going to go run our eval probably a
little bit further down here. Uh you can
also see like we are querying directly
from that experiment that was run.
So, that whole sort of flywheel is
captured here within um within this
agent improvement skill. And I think
hopefully I answered your question to
some degree. Cool.
Um
this to me is like one of the most
compelling parts of Braintrust right
now. Uh we're all sort of developing our
agents such to some degree with the help
of a coding agent. If I can bring the
right context, if I can have access to
the right primitives that attach the
right data to my traces, then this this
flywheel, this like automated automated
flywheel, becomes pretty interesting.
So,
I I I I absolutely think it's feasible.
Um if I could show you
I'll show you this example. Um actually,
if I come back here
So, within the platform right now, there
isn't like a button that you hit that
says like, "Hey, go do the the
flywheel." But what I showed you is that
you can very easily plug into this using
all of the tools that you already have.
The things that you're now able to to do
on top of this, right? You could imagine
like maybe plugging this into a GitHub
action that runs at some particular
cadence that that gets triggered based
on something and we open a PR.
Uh you could also imagine it's like
triggered off of a Slack message, right?
There are lots of different ways in
which I think this could be triggered.
Under the hood, all of the things are
available for you to go sort of opt into
this. Um one example
Here's a here's an example of uh a
GitHub action that that I that I
created. So, under the if you look,
there's a a YAML file that actually runs
through uh Claude code. It pulls in the
Braintrust CLI. It pulls in the skill.
But the the sort of again, like the
thing that we we need still here is we
need to understand in this case like
what changed. And this is like my very
very trivial supervisor agent uh
example. What changed?
Why these things changed? Why did Why
did uh in this case Claude code
recommend these changes?
Here is the the actual impact, right?
Based on the evals that that I ran.
Here's some links out to Braintrust
where you can actually go inspect those.
Here are these regret regressions that I
pulled in based on that analysis.
And then here is your PR. You You're the
reviewer. Go figure out if this is like
a meaningful thing that we should go and
and and produce.
Um so, I absolutely think this is
something that that you can opt into
today. Like we have customers
that are absolutely doing this. Um one
of them that was on a that the first
slide that I showed is using this to
generate five to 10 more PRs per day
than they were before. Um if you have
again all of that information, if you
have like the uh
that really intelligent Codex Claude
code or whatever querying very flexibly
over your production data and pulling in
the things that are that are
interesting,
I think it becomes pretty compelling
from a lot of different use cases.
Yeah.
Yeah, that that Braintrust skills repo.
This is open source.
Yeah.
There's a There's a YAML file in here as
well that like that went through the
actual um like GitHub like it did it
within a GitHub action. Open source as
well. Yeah.
Yeah.
Yeah, so what it looks like
is
Um, so I I I showed earlier how we write
evals or one of the ways in which you
can write evals with BrainTrust is by
using
that eval code.
So,
here's my eval for a different project
that I'm taking you outside of. The the
one sort of thing that I call out here
that's different that you didn't see in
the previous code is the parameters.
Um, under the hood here I am essentially
uh
I have exposed different parameters that
that touch my sort of agentic system.
And in this case it's, you know,
something
somewhat trivial, right? It's the
supervisor agent, but if you look over
at the playground itself,
um, come over here.
So, you have different things that you
can pull into BrainTrust, right? The I
think,
you know, I don't think a lot of people
use it very much for prompts anymore
outside of like the the very basic
stuff, but that remote eval, I can
spin up a dev server, so I can be local,
I could write um eval my file name
{dash} {dash} dev. It spins up a server
and it um automatically looks for it on
localhost 8300. Um, you could also
expose this server within your own
infrastructure. You have sort of um
created that eval and you have exposed
it and then you've also exposed
different parameters. So, in this case
I've exposed a system prompt and the
model
for that system prompt. And if I scroll
down a little bit further, there's also
math agent prompt, model, research agent
prompt, and model. But, I can sort of
interact with all of that complexity,
all of the tools that each one of those
agents have directly from the
playground. I can simply click run,
it'll go through, and all of the code
execution remains on the server and then
the results of that eval are streamed
back into the playground.
>> Yes, Brain Trust will initiate a post
request
to an eval's endpoint that you have
exposed on that server.
So there's there's like very
I can show you another example here.
Um
where you can there's a sort of like
create app function
that you can use or you can sort of
strip out the things that you would need
to spin up the server.
But
that that remote eval server right now
is is stood up on modal. I'm using this
create app. It exposes all of the evals,
at least in the way that I've configured
it, in my evals directory. And now those
are exposed to the playground for users
to go and play with. One of the things
that we are doing internally right now
is we are and it's really driven a lot
by interactions that we have with our
customers. I think I mentioned this at
the outset like
people are thinking very heavily right
now about
how well their their coding agent is
actually how well how efficient they are
with their coding agents.
Um and part of that is actually it's
running evals on the skills that they're
using. It's understanding the sessions
that they have with cloud code and codex
and so on.
I think they're still I say that with um
I say that because we are
putting a lot of effort behind the
scenes into creating some of the
different primitives and machinery that
our customers can go like plug into or
use to start to go understand those
those types of things.
Um yeah, just because you see like two
commits and and one star there is not
indicative of like where we
uh like what we perceive to be as a very
very important problem uh for engineers
today.
Yeah.
Cool.
Awesome. Thanks, everybody. Appreciate
you coming out.
>> [music]
