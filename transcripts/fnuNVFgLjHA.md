# Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI

Source: https://www.youtube.com/watch?v=fnuNVFgLjHA

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

My name's Fuad Ali. I work in product at
Arise AI, and I've been working on agent
experimentation and generally agent
tooling across the stack at Arise. Uh,
you just heard from Lori, uh, who's also
part of our team here at Arise. He's
going to be flitting around the room.
Aparna, our co-founder and CPO, will
also be flitting around the room to help
you guys out if you require during this
workshop. Uh, what we're going to be
talking about today is building
self-learning loops for your agent. Um,
and just to give you a bit of background
on myself and and how I got into the
space. I think this concept of
self-learning loops is really new to
this idea of AI engineering, uh, and
there's a lot of features in Arise that
kind of help you support it. But, to
kind of frame this,
um, I actually worked in back in
distributed systems at SpaceX. And
it is actually quite interesting how
we're kind of coming full circle in this
world of telemetry where, you know, if
you think about it, uh, a rocket system
that is continuously course correcting
every millisecond is actually consuming
its own telemetry and then actioning
that telemetry in order to self-correct.
And basically what I'm going to explain
is how we've sort of built this idea of
self-learning loops for your agent in
Arise, and how you can use that to
self-correct.
Cool.
So, to give you a bit of history on
Arise, we made a few big bets. Uh, we
were first to the market with LLM as a
judge back in 2023.
Uh, we created the first set of semantic
inventions for LLM applications with
open inference open sourced. Uh, we
created the first real-time AI data
store, ADB. Uh, in 2025 we released
agent evals and Alex, which is our
in-house agent, uh, to kind of help you
with AI engineering. Think of cursor for
AI engineering. And in 2026, the next
big bet really want to make is how you
can create self-correcting agents with a
feedback loop. Um, and I think
everyone understands sort of like how
that is going to be extremely powerful
to this idea of of agents generally. Um,
and so I really think the the industry
is evolving quite a bit um when it comes
to software engineering. Uh, you sort of
have the classic, you know, software 1.0
where there's an app and it's traced to
Datadog and there's some sort of
observability platform that human beings
read, a human dev then writes code to
actually correct it. I think 2.0 was
really humans interacting with this in
prompts. Um, so same thing but instead
of you writing the code, you write a
prompt that then corrects the behavior
that you're seeing in your app. Uh, what
we're moving to really is phase three,
which is the fully autonomous loop.
In this loop, your application produces
telemetry events, observability, and
then what is actually reading that is
your coding agent. It's not just a human
reading it and then putting a prompt in.
Um, if any of you guys are using things
like Cursor, Claude Code, the Datadog
CLI, you're already seeing some of this.
Uh, the gap is you're still probably
prompting that to go read that
information from a back end like Datadog
or whatever it is. Um, and I think when
you evolve to the to the needs of like,
you know, thousands of agents across the
stack, it starts to become pretty much
impossible for a human being to actually
read those things. And so um
going to be talking a little bit about
some of the new features in Arize that
we've released that kind of support this
uh flow. But what I want you guys to
center on is that observability has to
evolve from humans reading dashboards to
really programmatic interfaces that
agents consume, agents can operate on,
and agents can self-reflect on as well.
So, just some proof in the market, uh
Arize has processed over 1 trillion
spans.
Uh, we've run over 60 million
evaluations per month.
Uh, we have over 3 million downloads per
month. Uh, trusted by a ton of different
cool teams, uh, whether it's Spotify,
Reddit, Uber, Trip Advisor. So, just to,
you know, build some confidence that I'm
not just here vibe coding something and
telling you guys how it should work. Um,
And I think if you look at the industry,
um, the industry is really kind of
moving towards this as well. It's not
just, you know, these teams, but it's
also teams that aren't even Arise
customers, like Ramp Labs, and how
they've kind of moved to this idea of
making
software self-improving and
self-healing. Um, and I just point this
out to say the industry is really moving
in this direction. It's not just us. You
want agents that can detect a problem,
investigate it, ship a fix in the same
loop. Uh, and that's sort of the loop
I'm going to show you guys how to build
today.
Cool. So, um, I think
the the big problem I want to outline
here is the failures that cost you are
invisible at launch. And that's sort of
by definition, because
if you had caught them, they wouldn't
have cost you. You would have shipped a
fix already.
Um,
and I think like really what I'm trying
to center on here is, you know, your
agent works in your experimentation
phase. It works with the evals that you
set up. You don't really know all the
evals that you have to set up before you
ship it, otherwise you would have
written it. Um, and something breaks an
edge case that your team just wasn't
aware about. For example, in this in
this example, a shopper's asking for a
birthday gift under 30 bucks, they get a
list of items over 30, 50 dollars.
And then, what you'll see in production
is the agent confidently purchases the
wrong item, always does so extremely
confidently,
uh, because it never verifies the
product.
And these don't Again, these don't show
up in staging. They show up when users
complain. They show up when you get a
support ticket. They show up when you
get paged on call at 3:00 a.m. Um, and
that gap, it works in staging, didn't
work in production, something sees off,
is what I'm trying to close here.
Cool. So, uh real quick, just to ground
our kind of talk in an example, we have
this thing called the Wonder Toys
Assistant. Um, it's a shopping
assistant, very simple application, has
a few tools available to it to search
products, get product details, get the
information required for one particular
product, purchase that product, uh check
an order status, and cancel an order.
Um,
we have the OpenAI Agents SDK running on
top of this, a fast API backend, uh
search with a vector search and a text
fallback, and it's traced to Arise, so
you can actually see the source of truth
for what that agent is doing in
production.
And just to give you a little kind of
like sneak preview of what that agent
is,
very simple,
you know, you kind of have like a web
interface for Wonder Toys, and I'll zoom
in a bit so you guys can see.
Um,
I can click on ask about the product,
ask the agent to
purchase the product, and don't worry,
no real credit cards involved in this
demo at all.
Cool.
Um, so that just grounds us a little bit
in the example we'll talk we'll be
talking about today.
Um, and I think the the key thing here
is we're going to be going down a few
routes to explain some of the new
features in Arise.
Um,
but
really, it's going to be four commands,
and then a bit of clicking around the UI
interface. You're going to get clone the
repo, and don't worry, I'll I'll flash
back to the slide so you guys have
enough time to walk through this.
You're really just going to get clone
the repo,
navigate to it, add your API keys, npm
run dev, and your tracing should be set
up after you've gotten an API key from
Arise, uh and an Open AI Open AI API key
to run the open AI agents SDK.
Um, and that's pretty much it. And then
once you start clicking around, you'll
see that the traces automatically start
flowing uh, into Arise.
Cool.
So,
um, we're going to get to kind of like
how we can actually start breaking this
thing, but
um, the specific bug I've put in this
repo is around this kind of idea of
price gates. Um, so most of the most of
the kind of queries will work and you
guys are welcome to play around with it
on your own.
Uh, but if you ask for a birthday gift
under $30, you're going to be get
getting items over $30. Very common edge
case, one where, you know, a specific
gate wasn't triggered. Um, and without
the actual kind of context of the coding
repo and the context of the traces, it's
very hard to find edge cases like this
um, in, you know, sort of an opaque
system that's just emitting telemetry
data. Um, the agent won't find it. It'll
return a confident list of completely
wrong products. How do you actually
write an eval for an edge case you
haven't seen yet?
And so, the first of the new features
that we have in Arise to kind of talk
through this is called signal. Uh,
signal is an out of the box agent that
lives on the Arise platform in a sandbox
and it's really just one toggle to turn
on in project settings. And what signal
does is it continuously
runs on your production traces
um, in the background. And so what it'll
do is it'll read every trace that's
coming in. It'll start to cluster
failures by root cause, dedupe those
failures across runs if the same
failures are occurring. And because it
is an agent with an entire harness, it
can actually call to external tools. So
what you can do is you can connect
signal to your GitHub repo. You can
connect signal to downstream data
sources like DataDog. And what signal
will do is sitting on top of your trace
data, which is a the of truth for what
your agents are actually doing in
production. It will then self-reflect
and go look at the code for the agent
that you're running. Go look at
downstream data sources like DataDog.
And can actually write an investigation,
write a severity entity entity type and
and collect some evidence for that, and
actually write a PR for you and open
that PR. Um so you're, you know, kind of
flashing back to the beginning of this
presentation that I was talking about
where
we have this evolution of software
engineering. We're going really to that
phase three where the agent is consuming
its own telemetry data off of the
Observe View platform. It's then looking
at its own code and then trying to
propose a fix based on some evidence
that it has.
Cool.
So, that's That's the first part,
signal.
Um the second part is really around this
idea of skills, and we'll be having a
workshop later today that goes really in
depth to all the skills that we've
released. Uh but maybe you don't want to
have that agent managed on a rise. Maybe
you just want to be able to pull data
from some store that you have. Uh what
we've also released is this concept of
rise skills.
Um so rise skills allow your coding
agent that you're working in, whether
you're using Cursor, Clockcode, uh
CodeX, or 40-plus other coding agents,
OpenCode, Hermes, whatever it is. Um and
this can actually start to query the
traces from rise. So, um a good example
of that I think is
Uh give me 1 sec.
I can actually ask my coding agents,
this is just Clockcode, but I can ask my
coding agents to actually go read my
traces once I'm in the repo. And so,
it'll be able to see what the agent's
doing uh from the trace data as well as
the actual code for that agent at the
same time and make some really impactful
fixes.
Cool.
Uh so, variety of skills. We have skills
for creating data sets off of failures.
We have skills for uh going in and
reading traces and doing some of that
trace error analysis,
uh as well as skills for, you know,
actually running evaluators and running
tasks on the platform as well.
So,
the first part of this kind of skills
workflow is that Clock can actually
write the fix for you because it's
sitting in your coding repo. Similar to
Signal, Signal's running on top, it has
access to your GitHub repo, it can go
push up a PR for you.
Um and so,
so these two paths are sort of
equivalent. Um you have Clock code with
the Arize trace skills. That's kind of
like an on-demand method. Let's say
you're an engineer working on your
product continuously and you're actually
sitting there and trying to improve it
versus Signal, which is the always-on
sort of continuous method. It's
continuously serving up, uh you know,
new insights, new analysis for you based
on your trace data.
Um and Signal, like I mentioned before,
can actually kind of root cause that
because it has access to your coding
repo. It can write an investigation
report, um and it can actually try to uh
put up a PR based on that. And it's not
just, you know, individual traces that
they're looking at, it's looking at the
entire context of what your agent is
actually doing in production.
So,
um
real quick cuz I want to get to the meat
of this presentation, I'm going to pause
here and keep this slide up. Like I
mentioned before, we have Laurie in the
room and Aparna in the room um to help
out and run around and kind of help you
guys set up. Aparna's right here. I
think Laurie is
somewhere else in the room, but he'll
he'll be running around. And we got Dat
as well from our team. Uh so, real
quick,
these are literally the only four
commands you have to run. I would
recommend signing up for a free account
at arize.com to just get your Arize API
key to start seeing some of the traces
flowing in. And you will need an OpenAI
API key as well for this presentation.
So, I'll pause here, leave this slide
on, and then we can start walking
through getting the traces for the
Wonder Toy signal, and then what I'll do
is we'll walk through how that loop
actually starts to get into production.
Um so, yeah.
And if anyone needs a key, uh Dad is
more than willing to give give you guys
a key.
All right, how's progress going so far,
guys?
And if you don't have your laptop, don't
worry. I'll be walking through sort of
what this flow looks like uh if you were
to have done it yourself, as well.
I'll give you guys maybe 2 to 3 more
minutes to set up your API keys and to
run these commands and clone the repo. I
know that the Wi-Fi has been a little
wonky today, so we won't fault you guys
for that.
Uh no, you do.
You still get the access to evaluators.
You don't get uh there's a few features
like code evals and things like that,
yeah.
And for this flow, we'll mostly be
showing how Cloud Code can do that
tracing analysis for you through the
skills and through signal. Um so, it
won't be it won't be necessary for this
one.
Anyone having any trouble? Anyone need
some help? Feel free to raise your hand
and we'll flit around the room.
Sorry?
Here, I'll jump down.
Sorry.
>> The Git clone is not installing.
>> Ah, okay.
Cool that's probably a Wi-Fi issue.
So if you guys are having Wi-Fi issues
let me know when you can start to see
the repo pull up it might take a few
seconds
but this is generally the structure of
the repo
we have kind of the agent all the
scripts that it needs
and a bunch of other things there so
I'll give you guys a few more seconds
cuz I know the Wi-Fi is a little slow
once we get folks starting to get into
the repo
please make sure to sign up for an API
key as well
and get your open AI API key as well so
we can get started.
Should I just keep going?
And just a reminder all you have to do
is run those few commands so you get
clone
the repo then you'll CD into that repo
so I'm already in there.
Then you'll NPM install.
And then make sure that you have your M
file loaded this is where you're going
to be putting your three keys.
No doubt at the end here.
Wait sorry.
Which one?
Oh, the doc get at the end.
For example, got it.
Can't change it right now, but uh well,
we'll get it going.
Cool. All right, I'll start I'll I'll
leave this up for for maybe 10 more
seconds. Um very simple, make sure you
put your M values in. Uh there may be a
bug there as well, um but just make sure
you look for the dot M file and put your
own keys. Um just to show you an
example,
uh I will take this off so you don't see
my keys, but there are there are some
keys in there as well. Um
and then you NPM install and NPM run
dev.
So, what you'll then see is that your
Wonder Toys interactions, so your
interactions with this chatbot, are
being traced to a rise. Uh and in your
rise traces, you'll actually be able to
see
um
the things that are coming in through
this chatbot, right? So, I can see that
I started an agent workflow, the Wonder
Toys agent then um responded, it
searched products, uh took another turn,
and actually found the products and
returned them to me, uh and I can kind
of see the output of what that agent is
doing. So, this is like kind of like
baseline value prop. Can I trace? Can I
understand what's going on? Uh and then
the second part of this that I wanted to
show is sort of like some things that
Signal can do on top of this. So, you
have all this trace data uh coming in
through a rise.
And what you actually want to start
doing is you want to enable Signal to
actually run on top of your agents.
And I'll show you an example of Signal
uh in a repo.
So, Signal runs continuously in the
background. It takes a few minutes to
actually get started once your traces
start flowing in. Uh so, I'll show you
we're getting hit with a little slow
Wi-Fi, but I'll show you an example of
Signal already set up and ready to go
and sort of how it's it's sort of doing
that loop of self-improvement.
So, kind of like I mentioned earlier,
traces are flowing in through a rise.
Every interaction you do with the app
comes in.
Um and then this is sort of what Signal
looks like. Um
so,
Signal has kind of this clustering
analysis of different issues that it's
seeing across your application. Uh
you'll see sort of this table of uh
categorization of what those issues are.
Uh you can see those issues trending
over time. Um and then you can actually
go read examples of what that are,
right? So, in this example, uh we can
see some serialization issues with
Python. Um and that that is corrupting
the agent um input. And you'll see that
it actually opened a PR for me already.
Um and so, I can just one click go into
that PR and start viewing it. Um
there's also this idea of like writing
at least the ticket out of that
investigation. So, you'll see this
overview of what um this stock agent is
doing, fabricating results for example,
a hypothesis of why that's happening,
evidence for that within an individual
trace,
and then a proposed fix for you to go
and and then do yourself.
So, kind of going back to this concept
of like agents consuming the telemetry
data,
this agent is sitting in the back
consuming the telemetry data, actually
writing out the evidence and proposing a
fix for you.
In this example, we've still, you know,
left the code review to a human. Your
mind's a limit on how far you want to
take these things. We do recommend you
do that as well.
But, kind of this idea of like the
self-healing software, you can see in
action.
How are we feeling on
setup? Is Was the Wi-Fi able to get up
and running for people? Did they Were
you able to No? Okay, cool. I will
continue kind of through the
presentation, and maybe we can take some
time at the end as well to kind of float
around the room and help you out.
So, kind of the four steps that I wanted
to walk through you guys were one,
detect. So, surface the fallback failure
before a user had reported it.
Two,
based on that failure and Evals running
in your platform, actually investigate
what's happening with real traces.
And so, in our example, there was a bug
with the price check. And so, what
Signal and your skills via Cloud Code
was able to do was look at the traces,
look at what a user is asking within the
trace around, you know, the price being
under $30, actually marry that to an
investigation of the code path that
checks the price filter, and then
propose a fix for you. So,
in my code, there was a bug with how it
was actually doing that price filter,
and using Signal, using the trace data
that's in a rise, and using the skills
via Cloud Code, I was able to see that
interaction happen with a real user, and
then fix that, you know, kind of wrong
filter in my code for the agent. And
then finally, we have this verify path.
Wasn't planning to get to it today cuz
it is a little bit of setup, uh, but
happy to kind of talk through that and
then we'll make sure to, uh, kind of
return when the Wi-Fi is good as well.
So, again, just a just a quick recap on
the basics here.
Uh, we have this idea of, you know, the
core loop running on a real agent which
detects the issue around the H filtering
bug, investigates, uh, using the arise
trace goal or through signal,
uh, fixes
that issue cloud actually patching the
fall back, uh, and then verify it, uh,
which I'll kind of walk through how that
works in arise as well, uh, with
harnesses as a judge and agent
experiments. Um,
and then signal it'll kind of do this in
parallel as well for when you don't want
to be hands-on with the keyboard and
want to run this in the background. Uh,
signal will be tuned to your own
taxonomy, your own traces. Um, it you
can also configure it to be set off
alerts. Um, so for example, if you have
an alert on a specific eval that needs
to stay below, um, you know, 1% trigger
rate, you can configure signal to be
triggered off of an alert, um, or, you
know, a latency spike or a cost spike or
anything like that. Um, you can then
have custom harness judges running in CI
on those PRs. Um, you can experiment
with those and then you can kind of
optimize things from there.
Uh, and quick quick shout-out as well at
2:00 p.m. Lori will be doing a workshop.
Hopefully the Wi-Fi is a little bit
better as well where we dive deep deep
into some of these workflows as well.
Um,
so, kind of centering us, I talked about
this loop. I think we all kind of get
the picture of I have an app, it's
traced, this traces flow in, and then in
addition to the trace data, uh, whether
it's signal, whether it's your own
coding agents, having trace data which
is the source of truth for what your
agent is doing, as well as your actual
repo data which is the code that defines
what your agent should be doing, uh, you
get some really, really interesting
analysis, um, and the ability to
actually make improvements at scale.
Um
I think one thing that we didn't talk
about yet that I want to get into is
sort of how do we evaluate agents using
agents? So, this is kind of like an
example of pull the traces,
you know, look at my code, figure out
what's wrong. When you want to have sort
of this more adaptive analysis, we tend
to think of it as Harness as a Judge.
So, I think raise your hands if you guys
are familiar with LLM as a Judge,
loosely speaking.
Cool. Awesome. I think pretty much
everyone in the room should be familiar
with that at this point. Um you know,
very common pattern, you feed in an
input, your LLM as a Judge reads the
input, uh whether it's uh summarization
task or a hallucination eval, whatever
it is, it then responds with a set of
rails
um on how well uh the sort of the agent
did on the response. What we're really
moving to is Harness as a Judge, and
this is for a few different reasons. I
think firstly,
LLM as a Judge is really a fixed rubric.
So, when you have a use case in mind,
and when you have an eval that you know
you want to score on, it works really
well at catching those known issues.
However, like I just kind of explained
with the price filter,
you don't always know what those issues
are going to be like before you hit
production. And so, Harness as a Judge
is a way to do that adaptive analysis.
Um so, observe what the agent is
actually doing, and adjust what you
actually test as the agent goes. So, the
criteria kind of emerges from the
trajectory. Um was this the right tool
to pick? Were the arguments valid? Was
this grounded in the right context that
was handed off by another agent, for
example? This idea of that unknown
unknown. So, that price filter was an
example where I wouldn't have written
maybe a test case for that, um
but an Harness as a Judge is able to
kind of do that adaptive analysis for me
with the trace analysis that it has in
it.
Um so,
this is sort of like verifying in plain
language. You're
not column mapping, you're not writing
boilerplate, you know, sort of eval
templates and and text. The rubric is
really just a sentence and it reads the
actual trace tree directly,
um, then runs in a sandbox against those
real traces,
um,
and so I think it gives you a bunch of,
you know, tools on top of that because
it also runs in an environment. So, one
example that I see from a lot of
customers is around this idea of access
checks. Um, an LLM as a judge might be
able to read an input and read an
output, but because it has no data
outside of that unless you paste in
every user in the system into the system
prompt, it doesn't actually know or have
context on what that user should be
doing or should have access to. Whereas
a harness as a judge, because you can
connect it to external systems, it can
then go make a call to actually say,
"Hey, is this user allowed to do this?
Does the trace reflect the access that
they had?"
Um, and so harness as a judge is
essentially moving from just a
foundational model call that scores an
input and that comes out with an output
rail to a more agentic flow where you
can actually call tools,
um, and and sort of do that unknown
unknown catching as well.
Cool.
Um,
so I think
we we kind of talked about, uh, harness
as a judge, um, how that would have
worked in this scenario is
scoring the fixed to fail and and
actually deciding whether to pass the
example or not. So, for example, "Pass
if every return product's price is
within the requested min price max price
range. Fail if any result exceeds the
budget." Um, and it's actually able to
go into the code and check that those
filters are working correctly,
um, and this rubric now will catch this
on every subsequent run and not just,
uh, you know, an individual test case
that you've coded for before.
Um, so quickly checking in, we talked
about the detect, investigate, and ship
the fix.
Um,
shipping the fix part is kind of what I
want to talk about now with agent
experiments. So, maybe we've found an
issue, we've grounded that in real trace
data, we've investigated that, we know
why it's wrong, and we've decided that
we have a fix worth shipping.
Before you ship the fix, you probably
want to test this on a set of results.
And I'm not sure how you guys are doing
this today, maybe you're deploying to a
dev environment and then manually
testing.
Um,
what Arize has come out with is agent
experiments that allow you to test that
in an automated way via CI as well. And
so,
uh, I don't think any of us are
strangers to the concept of, you know,
data sets of failure cases that we
collect over time.
Um,
what you can do with agent experiments
is you can actually stand up that dev
agent behind an endpoint and hit that
with a data set directly from Arize. And
that data set will be actual traces that
your agent has failed on. So, in the
previous example, I kind of showed you,
uh, the Wonder Toys where maybe I have a
few traces asking for,
um,
birthday gifts under $30 that actually
failed. Uh, what I can use Arize skills
to do is actually go create that data
set. So, I'll I'll have like, call it 25
examples of budget constraint searches
that failed, right? And then I ran the
workflow with cloud code,
uh, I did some trace analysis, I
identified the bug in my code, and I
have a fix ready as a PR. Or maybe
Signal did that all for me in the
background. How do I actually go hit my
agent with that data set to make sure
that the proposed fix is actually
validated? And that's sort of what agent
experiments allow you to do.
With agent experiments and the agent
playground in the product, uh, you can
actually run against that fixed version.
So, you deploy it to dev, it stands up
behind an endpoint, uh, you stream sort
of the, uh, data set inputs into that
agent, and the agent actually responds.
And then you can score it with the same
judge rubric that you have in
production. Uh, so then you can compare
kind of side-by-side what the agent in
dev mode is doing with the fix versus
what the agent of production did and
look at whether you're actually catching
uh any of those edge cases or not.
So, similar to kind of like other data
set experimentation workflows, what you
want to do is you want to look before
the fix and after the fix,
look at your judge, which is in this
case the price correctness judge, um
look at your examples and queries, look
at whether, you know, maybe latency is
increasing, cost is increasing, so you
have sort of a view of those operational
metrics as well,
um and then quantify the results of your
experiment. Um and then, you know, maybe
alluding a little bit back to this idea
of the self-correcting loop,
it as a full storyline, you now have,
you know, agent that's operating
autonomously on your traces, looking to
see if issues are arising. So, you know,
I can see that the user asked for under
$30, the response was clearly over $30,
investigating why that's happening with
reference to a code base,
putting up a fix in the form of a PR for
what how it thinks it can improve that.
In this case, it was a filtering error.
And then,
because our experiments are actually
exposed via skills and APIs well, the
agent can actually redeploy itself on
the new PR
and verify itself against a data set of
actual failure cases
before it even notifies you or decides
that it's worth your human review. So,
you know, this full loop happens
completely autonomously. The agent will
actually go collect the failures, create
a data set for itself, run it against
the new version of itself, and prepare a
response back to you that says, "Hey, I
think I found this issue. I investigated
it. I know why it might be happening. I
pushed a PR. I then ran that PR in dev
against the data set of failures I
found, and I saw, you know, um
in this case a 36% increase in
performance on this specific evaluator."
And all that information to you is
available to you in the PR itself for
you to then just go read, validate the
code, do some code review, and ship.
Um so, I think this makes it like, you
know, kind of coming back to this idea
of the loop.
Um
I think it makes it really, really
powerful to go, you know, full circle
where you have the detect, investigate,
hypothesize, and fix loop, and then you
also have the validation loop, right?
So, how do I actually know that this fix
is correct, and it's not just uh you
know, an agent in a sandbox saying it's
correct? How do I actually go test that
on real failures and real uh edge cases
from my working example, um and how do I
actually, you know, start to stand that
up and auto test that for me? Um And so,
I think, you know, we'll we'll come
back. We'll we'll have some time as well
to kind of help you guys around uh in
the rest of the workshop if the Wi-Fi's
doing a little bit better.
Uh but
I'll I'll go back to the slide that was
previous, um so that you guys can kind
of walk through this yourselves. One,
getting the tracing started. If you're
not collecting tracing, nothing else
works.
Um takes sub-second sub-10 minutes on
your on your own agent. We have
instrumentation skills. We have support
for all the big agent frameworks, all
the foundational model providers.
Um enabling signal and going deep, uh or
using clock code to actually use the
Arize skills to do that investigation
for you.
Uh verifying it with a harness as a
judge, and then measuring that with
agent experiments.
So, before we end, I will go back to
this, and we'll we'll we'll walk around
the room and try to help you guys get
this set up. Uh if you're having trouble
with the M files, um
if you just search through the repo or
ask a coding agent where the M file is,
um it will kind of help you do that. Uh
other than that, make sure you get clone
the repo,
um and you get your API keys from the
Arize platform, uh and then you can
actually start to see these traces
coming together. Um
in the spirit of AIE workshops, I think
this really works better when you guys
see it and touch it yourselves, and
actually try to do it. So, hopefully the
Wi-Fi works, and I'll I'll come around
hop around. If you do have questions or
you're blocked at any point, feel free
to ask me. Odds are someone else in this
room is experiencing the same issue. Uh
so, I'm happy to kind of shout out some
advice as we go. All righty, and if
you're having trouble installing the
skills as well, uh I have it up on the
slides here. Uh very simple NPX skills
add ariseai arise skills. This will give
you access to an interactive mode where
you can choose what you want to install,
or you can just choose to install all of
them as well. Uh and this includes
skills for trace analysis, data set
curation, as well as evaluators.
So, as an example of like some of the
skills you can run, uh I can ask Claude
code, "Hey, check my traces for any
errors or anything I can fix. Acquire
circumference with the code for the
agent in this repo and use the agent
skills." And uh we will be sending out
kind of a recording of this as well as
all the resources you need to kind of
get started with this. So, apologies for
the internet if it doesn't work out
today, you guys will be able to get up
and running very quick as well. All
righty, guys, we got to close up uh our
workshop for now. Thank you once again.
I just want to leave you guys with sort
of
this detect, investigate, fix, and
verify slide, uh which kind of covers
the through line of how uh you can get
started with Arise and how to create
yourself-improving agents. And then once
again, uh feel free to connect with me
on Twitter or LinkedIn. Uh and if you
want a free year of Arise Pro as well,
uh just use the code on the screen. Uh
we have a free tier that's always free,
free to use. For this conference only,
we're also giving out Arise Pro for
free, which gives you a bit more of the
usage limits.
Uh if you guys are running agents with,
you know, thousands and thousands of
traces. So, thank you guys so much.
We're running another workshop at 2:00
p.m. uh led by Lori that'll go into a
few more code examples. Hopefully, the
Wi-Fi is also a little bit better then,
and yeah, we'll get going. Thank you
guys. Appreciate you.
>> Mhm.
