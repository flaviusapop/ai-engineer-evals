# The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse

Source: https://www.youtube.com/watch?v=TeErpYBUIeM

Uploaded: 2026-10-06

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Everyone, super excited to be here. Ah,
okay. My laptop was alerting me that
this starts now. Uh, hi everyone. I'm
Mark, one of the founders of Langfuse.
super excited to chat about uh what we
have seen how how people like
self-improve agents now and what kind of
like open source reference stack uh we
see emerging. I mean obviously my view
is based on working with our community
of people that use language to trace and
evaluate their their agents but I think
I try to keep the talk mostly to to like
more generic takeaways that work with
whatever stacks you're using. Um but
yeah happy to chat about the different
pros and cons after the talk. high
level. I think this is the year uh where
uh teams talk about like upleveling the
the level of uh where where they operate
themselves where increasingly good good
models just abstract everything
downstream. I mean coming from I don't
write prompts I have loops u Peter
writing about it auto research becoming
really popular. So I think this is kind
of where things are going on the like
like producing um application side but
also on the how to actually um build
good good agent applications and um over
the years really models have have
expanded a lot in capabilities um back
when when we started working on length
fuse this was right when ch was released
so uh where like even the simplest
applications didn't really work so for
example we built like github issue to
pull request automation similar to what
devon or kurs are building but back then
we could only manipulate like single
page applications like a single HTML
file because multifile edits were too
complicated. Since then all of these
things really accelerated a lot and this
really made made loops not possible. At
the same time a more like reference tech
emerged of how great AI agents are built
because building agents is different
from building applications. It's like an
like a link of like tracing and
monitoring like online how users really
use an agent application and then like
an offline component of how to build
data sets how to experiment uh regarding
like making changes to these agents and
then evaluating offline whether things
work then deploying new to production
then learning again for real users use
the application uh so it's like this
this kind of loop where traditionally I
mean you have like obsibility and the
data docks here in the tracing
monitoring side and you have like the ML
ops toolings like MF flow weights and
biases more on the like offline side
where this new category emerged and
that's also why we built length fuse
because you need to bring the online and
the offline together as as otherwise
like you either benchmark on data that's
inaccurate so the data sets they're not
in loop and like uh not in sync with
what's happening in production or you
monitoring like production data but you
don't really benchmark offline so you
need to bring the the both together but
this has been like a lot of manual labor
because you need to look at traces
update these data sets think about like
new evaluators uh then make these
changes create new hypothesis like it's
it's like a lot of work going into this
process and since starting working on
language we try to educate teams how to
how to do this process well but it's
it's usually like the ask them like oh
models got better now how can we take
ourselves out of the loop to uh to
automate it because it's really tedious
uh to get things going and that's what I
want to talk about how we see how people
go from manually driving this loop to
using AI to to drive this loop
um we use the visualization um like of
for example like the loopcraft article
or like many many articles in the space
that like layer different loops on top
of each other. How I mean at the at the
lowest level you just have like this
token loop of what's the next what's the
next token that's produced and on the
very high level it's uh like like the
most abstract form of thinking where you
as a human are still involved. So what
we see how um we go through them one by
one high level I just want to highlight
these are again possible because models
improve. So uh when when we started
working on length in 2023 like I mean we
had github copilot so like the lowest
level or the uh level two u then level
three was possible like more in 2024 and
now2526 is more like the higher level
loops of actually agents reasoning about
what what to even fix uh how to propose
new fixes and how to how to verify
whether they actually work. Where humans
are currently still involved is one you
need to align data sets of example
questions of how the agents are used.
This is so like where where humans need
to review um like like what what gets
amended to the data set and how to then
evaluate whether the agents actually
work. These are the the two blue things
in in loop number three. Then on the
proposal of fixes because if um like
your agent proposes how to change an
agent, you still want to see what was
changed because you have the risk of
like overfitting it to um to like the
data set and the failure definition. Um,
so I mean usually agents find all sorts
of different uh failure patterns, but
maybe some of them don't really matter
that much and you're like, huh, this
kind of use case for the agent, it
doesn't really matter that much. Like
this is like out of what the agent
should be actually be doing. So we don't
need to over fit our application to this
random quirk that we found in
production, but we want to like be in
the loop to to monitor this. And now
coming from this loop pattern, we try to
dissect it again into more like a
workflow where where we currently see AI
used the most is in proposing fixes. So
if we have production traces and we have
like evil criteria and data sets of how
to reproduce issues that we find in
production, then this how do we hill
climb against the data sets? That's like
a really cool uh way to kind of like
loop your way to a success with with
agents because usually they're like 10
different things of what you could be
doing. I don't know, use a different
model like aggregate context in a new
different way. Try whatever you find on
X uh in a given week to to see whether
it can like uh make a dent into
improving the agent. But really like you
maintain the boundary of what you
optimize against. And you use AI mostly
for like proposing improvements to the
agent implementation.
Like over the last I'd say month, we see
more and more teams also using uh like
like AI and and their loops to maintain
evil criteria and maintain data sets. So
uh usually what goes in here is you want
to like align how a data set uh looks
like for an agent with what actual users
are doing. So for example if we have an
customer support application like
support agent then the data set should
be like common support questions but
like users do all sorts of things with a
support application. So you need to
continuously keep it in line with uh
with what users are doing and you can
use agents for that. And for EVAs as
well if you see usual error patterns
then you can reproduce the error
patterns and propose new evil criteria
on these offline data sets. So for
example I don't know I want I don't want
to name competitors. I want to be
concise. I want to answer in the same
language as the user actually requested.
Um like the question in my customer
support application. So you can also
propose new evaluators. This is I think
rather newish over the last months. um
and where we see like the AI more
autolooping. However, usually teams that
are still involved in reviewing these
changes because they create the new
boundary for how then other agents try
to auto improve against it. If you give
this completely out of hand, you risk
like that you just create more slop
where we've used this in like a blog
post of ours where I'd say the target of
an AI application is always changing
because you don't really know like
usually you start with a very high level
task of I stick with customer support.
You stick with someone says hey in our
company customers need to wait a long
time for support answers and we have a
lot of people employed to respond to
them. AI should be able to do this
automatically or at least eight in
customer support, but it's a very wake
target because people don't even know
what happens in customer support every
day. So, it's kind of like, oh, we want
to automate all of it. However, then on
the way of doing this, you figure things
out based on like error cases of what
you even need to do. And that's like
this kind of like map that you like you
assemble the plane while you're flying
it. Um and how we then look at the uh at
this kind of like looping graphic is you
really want to be like involved in
setting the setting like the the goals
and how you make changes to data sets
evaluators you want to be in that loop
involved because you set there by the
direction and then AI can automate
against it and then off of the newly
implemented changes you'll see new error
classes and you can then like change
cause again on the most highest level
but thereby you pull yourself out of a
lot of like the more manual and tedious
work on the lower levels.
Um, this is then the high level view of
how how I would conceptualize like the
different scenarios that you can find
yourself in. I'd say if you implement
this uh like AI workflow well of tracing
online uh how your agents are working
implementing evals on how they are
working um having data sets uh of
example questions and then benchmarking
against them you are in this era in this
class like very high time invest because
you need a team who really works with
this data every week but also quality of
the of the agents is pretty high I mean
that's what teams have been for example
using length use for for the last years
and this is how you can get to I'd say
success with your agent application. Um,
if you fully automate it, I would say
you don't really need to invest any time
because you're just like, I don't know,
codeex goal mode your way to success or
like you add higher level loops on top
of it, but you also risk that like it
produces a lot of tokens, but don't
really make sense. So, I think you want
to be in this kind of like promised land
of you don't really need to invest a lot
of time, but you're like in the loop at
the most important steps of like setting
the direction of where you want to go,
but you take yourself out of everything
that's tedious. Thereby you're way less
time invested than running it manually.
But also the quality can be even higher
because usually if you need to do
everything manually you're bottlenecked
by your own time your own like
perseverance endurance uh or like
patience to look through so much data
and AI can just look so through like so
much more error cases. This agent will
be higher performing and you need less
time invest. That's the I think that's
what we were going for and how this then
looks like is uh you involved at the top
but also I mean you want ideally your
application to feed in interesting
signal. So for example when we talk
about the like customer support
application use case usually I mean
customers can swear at the support agent
customers can be like oh no you don't
understand uh like this was not correct
or like you can propose messages to an
internal agent who then can accept them
or change them when sending them out. So
there's like a lot of like implicit
signal that can feed into your process
without you as the agent developer
needing to do this manually. Uh thereby
you have like an like an instream of of
signal that your loop can act on. Um so
it's either you your team or some signal
coming in um and the lower level loops
can be automated. That that's high level
how we how we think about it. And like
uh like we put together like a super
quick demo application um that can that
can show this. Um so for example like we
as the language team we have a big
problem now because our like engineering
team uses AI a whole lot thus they ship
a whole lot and somehow we need to
update our customers uh and user base uh
what is what is new every week because
uh like in recent weeks like a lot was
released uh and usually need to update
documentation update a change log post
about it on socials and historically
like engineers did this themselves
because they maybe released like a
bigger feature like once every month so
it's okay to spend a couple of hours.
But now if they take themselves out and
really ship a lot of like product, they
want to ideally uh like automate also
that kind of like release process
because otherwise we are bottlenecked by
how fast we can communicate about
changes. So um we thought about like
putting together like a change lock
writer that just uploads like like
updates a lot of like the public assets
based on what we've shipped. Um however
then the question is is like how we
communicate good because if we
communicate badly about what we've
released then I mean we we kind of like
sabotage our releases if we like
misrepresent for example what has even
been released. So um setup is we have a
merge PR, we have a change writer that
uh suggests a change to documentation,
but then there's like a just like a code
review step as like a GitHub PR where
someone can review and either like
approve on GitHub and get it merged or
like submit like change requests of like
what needs changes in this um in this in
this change in documentation and and the
change log. Then the change writer would
act on this again to update the draft
until it's finally released. And now
both of these kinds of like either like
approvals or uh requests for changes can
get feed into like the AI obserability
and eval to to serve as a basis for auto
improvement of that change writer agent.
So what we've now done is um just use a
coding agent pointed at the like length
use agent skills but generally I mean
this would also work with other systems
but yeah length is like well positioned
for this to to ask like okay what has
happened in this application how can we
improve it I'll I'll pause a couple
times because otherwise it it'll go
it'll go by very fast. So what we for
example here identified that the writer
uh so the chain lock rider is factually
uh like very correct in how it makes
changes to documentation but clarity is
low. the edit ratio of us humans making
ch like submitting change requests is
still high and that we leak internal
jargon to our customers because maybe
our code has like internal comments that
we leave there for ourselves for the
future but uh like our customers don't
think about our application as like I
don't know like an ingestion pipeline or
as like I don't know some kind of like
batched evil Q like they don't know this
is like an implementation detail we
should talk about it as like an user
domain language and that's like uh
something we have identified here we're
Now the agent suggests changes to the
data sets and evaluators to test for
leaking jargon and um also like
increasing clarity in customer domain
language basically. So um agent now
closes this gap suggest changes to the
data sets and evaluators and now um has
an idea of how to change the agent
implementation to basically fix this
problem because in the end it's kind of
like just like a a problem of how we
provide context how we like provide the
skill that then educates this um content
writer and now we can back test it
basically on the updated data set to see
whether the new implementation would do
better than the old implementation and
I'll stop here again where we have
basically the baseline. So um basically
we reproduce the issue of userf facing
language. So let's talk about features
in a way of how users would talk about
it. So we reproduce this kind of problem
with the v1 baseline. This basically
existing implementation of the agent and
agent came up with a new implementation
where we see the v2 candidate. We are
still doing on format compliance and
accuracy in the same way as we did
before but we improved on like userf
facing language. So we see a positive
delta which sounds like a good change
now. Um so uh agent reasons about it as
this. I mean this is a bit I mean
internal application it's a bit yolo. So
we are like okay we are good of of just
merging this and then acting again on
the next change because this agent never
publishes anything to actual production.
It just raises PS on a repo. So it's
okay if it kind of like auto improves
and then we just provide feedback again
to whatever the next increment is. So um
here we use our like prompt management
logic so that the agent can just
basically feature release this new um
implementation and uh now it just
summarizes basically um how how we acted
on this. So high level um this is what
we have seen like most of our best users
do already uh when they when they build
agents like collect production signals
uh track them alongside like detailed
execution traces and then run agents
like on a loop uh usually like a crown
job like every day every week whenever
you have like a batch of basically
interesting user data again to then act
on it. Um either it's just user feedback
how how it's happens in this case or
internal labeling from like a production
system but it could also be you ask
people to annotate data like in app for
example in langu we also allow like for
annotations to feed into that uh into
that queue and yeah that's very high
level what we've seen happy to give you
like a more deep dive um demo at our at
our booth or after this talk but just
wanted to to wrap it up very concisely
with how we see this this space evolves
and um I think what's what's interesting
here is it drives the need for like a
very scalable data system because you'll
want to have agents really loop on this
data and like produce lots of queries.
This we see how langu was historically
very right intensive to like um ingest
evils and traces. Now it's way more read
intensive because agents can like like
chew through so much more data.
interesting number one and two you want
to really like own the data layer
because like now the traces of like for
example a year ago are interesting
context and you don't want to want them
to be locked up in like like a more
commercial system or something where uh
you need to sample data or retain them
for a long short time period but we want
to like retain them for a long time
period and not sample them and yeah this
really drives the need for like a
scalable cheap solution and we've worked
with many customers on this so happy to
talk one about uh oneonone about this if
you're interested thank you so much for
your
