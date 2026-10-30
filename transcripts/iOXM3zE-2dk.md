# Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft

Canonical video: https://www.youtube.com/watch?v=iOXM3zE-2dk

Source: https://m.youtube.com/watch?v=iOXM3zE-2dk

Uploaded: 2026-05-14

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. Caption formats vary: some extractions include segment timestamps and others do not.

## Transcript

Hi everyone. Welcome. Thank you for
joining us this morning. Um my name's
Amy Boyd. I lead our Foundry developer
relations team at Microsoft. I'm joined
by my colleague Nitya on the team who is
an absolute expert in observability. And
today we thought we'd have a nice catchy
title uh given where we are in London of
mind the gap in your agent
observability. We'll talk a little bit
through what we actually mean by mind
the gap cuz it's got a deeper reason
than just the nice sort of uh title
there. But also we'll start going
through some really interesting stuff
and you'll have a load of assets to take
away with you as well. Um this area is
there's a lot there's so much to cover
in the agent space even just in
observability itself. So we'll we'll get
you kick-started but there'll be a
journey afterwards that you can take as
well if we you know uh get you excited
about what we've got going on here.
So uh mind the gap is a actually a
really good terminology for
observability when you look at agent
specifically.
Um
one of the interesting things Nitya
realized is she started her journey uh
in New York and found it's also mind uh
not
watch the gap uh whereas it's minds the
gap here. But when we started to really
think a little bit more deeply about it
it actually works super well with an
observability analogy. So if you think
about um things like when we evaluate an
agent we're checking for like the
quality and the change over time that an
agent goes through. And if you think
about the change in trains and
technology but the platform doesn't
change. So there's this sign on there
because at each station it's different.
The train might fit perfectly like this
one here brand new train, designed
beautifully for said platform. But in
other cases, there's a wide gap between
the requirements, which is the platform,
and the actual agent, which is the train
in this case. And so, what we want to
talk a little bit about is how you can
run evaluations from very, very early on
and throughout the life cycle in order
to bring your requirements to the
reality of what your agent is actually
doing in the wild.
There's another element of this mind the
gap analogy that works so well as well,
which is actually when you start
thinking a bit more about safety. The
reason these signs are in place, they
are guardrails at the end of the day for
your
for the tube in this case. It says,
"Mind the gap." It's letting your
customers know that there's something
that you need them to do to be careful
of. And it's the same thing when we
apply things like guardrails and safety
mechanisms inside agents and monitor
exactly how customers are engaging with
your agent. And then finally, the
monitor inside. These things, these
platforms, these trains change over
time. And so, having the constant
reminder of the phrasing "Mind the gap"
over the tannoy allows people to remind
themselves as customers that this is
happening. But on the monitor inside as
a developer with agents, you you also
need to know what's happening not just
today, but consistently across many
agents potentially that you're building
in the future. end of this session, we
want you to be able to say what is the
gap between agent observability and what
you're actually building. How do we mind
that gap? And we'll give you lots of
different opportunities to think about
the ways that you plan for and implement
minding the gap around observability.
And also, how do we accelerate that
optimize loop? So, how do we say from
the information I'm actually given with
all of this data, what do I do with it
next in order to improve my agents over
time.
So, today we're going to have lots and
lots of great assets, but what we want
to do is break down everything into
small chunks so that we can kind of keep
and progressing forward. Um, first
things first, we'd love for you to fork
the repo. We've got a wonderful GitHub
repository. We've been working on it for
quite a while. It's something that we've
been updating and we will continuously
do so as well. So, this is going to be a
great asset to take with you in the
future as we add new elements over time.
We also have a a Discord channel that's
specifically for us our Microsoft
Foundry users. Uh, we've actually
created an AI engineer channel. We'd
love to see you in there. Um,
what we're going to do today is kind of
get through quite a lot of stuff. As you
take this GitHub repository away, what
we want you to do is continue to engage
with those me and Nitya. Spend a lot of
time in that Discord server. Uh, and
we'd love to be able to chat you through
and help you along this journey as well
as you start using
um, all of these different assets.
So, as you just take along, so we've got
some short links, but also some QR codes
if you want to use them.
So, just very quickly as we get started
into what technology we're going to use
today. I know I asked a few of you uh,
as you get started the different things
that you're using. This is the the
reality of the agent space which is many
people are using lots of different
technologies. But at the end of the day,
we use this phrase agents are
non-deterministic. That's not just a
problem for demos. That's also a problem
for real life when you actually get to
production and the reliability and
consistency is starting to become when
you start passing this out to customers.
You need to be managing the
non-determinism that comes inside those
agents.
And three ways that we we see as to do
that kind of reliability is one to
evaluate, to look at performance, look
at quality and safety, um, and also
consider kind of how well your agent is
performing.
Looking at monitoring, so not just when
you're building, not just as an add-on
situation with evaluations, but actually
monitoring your agents over time as the
requirements change, as the customers
change, as the environment changes, it's
super important to know how you
continuously improve and debug any
issues that come up quickly. And then
finally, that optimize section, so
optimizing your agent's performance,
taking all of this incredible data that
we're starting to be able to get from
agents and actually doing something with
it as well. Um, we can tell you, you
know, all sorts of different scores and
stuff like that, but it's that next
step, but what do I do now? And we've
got some really fascinating stuff that
we can show you there.
We'll focus on a specific platform, My
Cyphon, uh, Netreo work with Microsoft
Foundry. Uh, it's our cloud agent
platform for all your end-to-end
opportunities with agents. So, you can
build the agents, but if you're building
the agents elsewhere, you can also host
the agents, observe the agents, and
manage and monitor your agents within
that same platform of offering. You can
use as much or as little as you wish.
Uh, some of the things that we'll notice
around observability is they come across
three different phases. You should be
having observability built in at a
really, really early stage as you're
building your agents, so we'll kick off
in that early stage. You'll look at what
you can do when you debug and optimize
in production, and then also when we
start thinking in the future, and it may
not be, uh, that far in the future for
those in the room, which is actually how
we manage in many agents, not just even
not not just even multi-agent systems,
but actually many, many multi-agent
systems as well.
So, a couple of areas we'll talk through
today, uh, are things like tracing in
those early stages. So, thinking about,
um, how you can actually access all of
the monitoring and debugging information
from your agent. What is it actually
doing? What tools is it calling? What
can
what different messages is it sending to
all of the different steps in your agent
workflows? One of the really nice things
about um tracing in Foundry is actually
we build on the hotel um offering. And
so the the group here at Microsoft
actually do a lot of work to work with
that standard and think about what it
looks like for agents in the future as
well. We'll continue to do that, which
actually then opens up the ability for
you you don't have to build everything
in one place. You actually maybe using
different things uh to build different
agents across an organization or across
many businesses. And that's absolutely
fine. You can actually bring all of
those agents and instrument them uh with
hotel tracing, which means you can then
manage them inside the Foundry control
plane.
Oh.
There we go. We're back.
Um the next one is that that build says
you're going to look at evaluators. Um
it almost feels like a little bit of an
eyesore. Uh this
uh slide's got a lot on it, but I think
take that from it. We there's so many
built-in evaluators from being able to
build agents at scale. We're obviously
learning a lot as a platform provider as
to what customers need. And so then we
start to embed that into the platform
itself. You'll notice and probably be
very familiar with a lot of the quality
metrics. Risk and safety is something
that often comes as like a second
thought, but should be built in in those
um inside those agents. And then we've
kind of started to move quite quickly
from
um evaluating the model and the actually
large language model itself to
evaluating the agent output as well. And
so the agent-specific evaluators are the
ones to really consider there as we
start to think it's not just that one
engagement with the LLM. It's actually
how does the agent do holistically
across its time and its workflow.
Um but if some of these evaluators
aren't working for your scenario, that's
absolutely fine cuz you can actually
build your own custom evaluators and use
the best of both worlds in that
situation.
And so what do we mean when we kind of
evaluate across the agent um workflow is
to actually take um weather's the usual
great example, isn't it? Of a um we're
in London. It's often unusual weather.
Today it's actually beautiful weather.
Um so you're a weather agent, that's a
system message. Our user says, uh what's
the weather in London today?
First evaluation that we might want to
do is actually the intent resolution
one. So we would say, does the user uh
the user wants to know the local
weather? Has it been able to understand
that intent and then make the next
decision point that it needs to, which
is make a tool call. Then once we get to
the tool call space, you should evaluate
the tool call itself. Um there's a whole
set of metrics you could kind of do
within that space including just
operational metrics in general. But that
that point you want to say, is the tool
call the expected one? Um in the
majority of cases again that
non-determinism does mean that we're
we'll be working with percentages there.
And then finally the overall response.
So that's at that agent level of
actually how well did it on task
completion, um how the task adherence
one tends to be the one that is the one
that you need to kind of tweak, I would
say, over time. But this shows where
it's not just evaluating once. You can
evaluate in many and many different
parts of your agent life cycle so that
when do things do start to go wrong or
aren't quite the top quality you're
expecting, you can go and pinpoint
exactly where you can make those
changes.
We We a few extra elements that we uh
hopefully will get to today. So, very
quickly, uh we mentioned a little bit
that actually debugging multi-agent
traces becomes exponentially more
difficult than just those uh smaller
agent-specific calls. So, there's loads
of great ways that we're building that
into the platform so that you can look
at a full agent trace and not just the
agent itself, uh any single agent at one
time.
But, we're also offering a quite a lot
of work that goes into monitoring those
agents across many different dimensions.
So, whether that's
uh continuous evaluations that are
happening when you're changing code,
scheduled evaluations that you're
working on, uh red teaming, so things
like security you're adding in, or also
if you're already using monitoring
across your cloud estate, you may want
to pull in some of that information uh
around the agent as well.
But, the key thing here is again on that
observability side. If you're already
using things like a monitoring solution
in the cloud, we have Azure Monitor for
your infrastructure and your data. The
AI platform allows you to bring in
Foundry Control Plane stuff we'll see
today, but actually connect to Azure
Monitor in the end. So, developers build
with what you wish, and your IT admins
will still be very, very happy cuz
they'll integrate.
And then finally on that fleet-wide
control as we start to look a little bit
more into the future, it's kind of
looking at that centralized
observability, looking across all more
than just one multi-agent system, and
understanding what your fleet looks like
within side either the business or um or
your own kind of business that you're
building, and actually all of your
different agents. So, I know we had many
different hosting opportunities in the
room when we discussed, and so this is a
great way to think about how we can
build in bring in agents from anywhere,
but again observe within the fleet view
there.
And then finally security, we won't
actually get of time to touch on
security today, which is really sad cuz
it's so impressive
what we're looking at for security in
the agent space at the moment.
But I highly recommend going and
checking out a lot of the work we do
around red teaming.
Red teaming is not something you do
alone and so Microsoft
works a lot with the pirate open source
repository and does a lot of deep
engagement in order to help improve open
source and offer a lot of our stuff open
source, but we also have kind of the one
click options inside the platform as
well.
So we spoke a little bit about the
foundry control plane. We're only going
to cover observability in any kind of
depth today in our short time with you.
However, there is a lot more to offer
and so we just want to make sure that
you take that information away with you.
So at that point I'm going to pass on to
Nitya who's going to talk a little bit
more about the workshop set up that
we're going to do.
>> Awesome. Thanks, Amy.
All right.
Um
Get your keyboard fingers ready. So
let's try to get into this.
So what I want to basically tell you,
how many of you think you can basically
learn everything you want to learn in
the next 30 minutes?
This is not the workshop for you.
So I want to set the stage by saying
this repo is actually almost like a
4-hour workshop that we're trying to
compress into this. So what I want you
to think about is this is a cooking
show. I'm going to show you the baked
goods, but I want you to look at the
repo because it has everything and you
can then try this at home and inject
your own stuff and actually play with
it. It's the only way you learn. So to
set the stage, we're going to have a use
case, right? So how many of you have
built multi-agent applications already?
Awesome. How many of you are completely
new to this and want to just know how to
get started?
Awesome. This is exactly the kind of
audience we're looking for. So let's say
this you've just joined a company called
Contoso. Contoso is a very famous
fictitious fictitious company in
Microsoft. Your boss comes and says, "I
need you to build this travel agent
application, right?" Where do you start?
So let's first kind of set the stage for
what an agent is. We all know models,
right? Everyone's worked with AI models,
you get a a sense of it. What does the
agent do? Models, when they're born,
they have a certain amount of knowledge.
Agents allow you to bring in additional
knowledge and capabilities through tools
to enhance the existing model. The
models are the brains, the agent is kind
of like the experience, and the tools
are all the things that you put in to
make sure that the models enhanced. So,
when you think about this, I'm building
a travel agent. What do I need? I need
to know what the instructions are for
that agent. What is it supposed to do?
I need to know what tools do I need to
make sure that it can actually execute
them, and I need to have the right model
for the job. Makes sense?
Where do I start?
The problem for us is Anyone want to
guess how many models there are on
Hugging Face right now?
No, no, no. 2 plus million.
Anyone want to guess how many Azure has
in our catalog?
11,000 plus. Okay, I can't If you show
me three jams, I can't pick one. You
show me 11,000 models, I've no clue
where to start, right? So, what we're
really looking at is when you start the
job of building an application, you
don't want to make all these decisions.
How do you just get quickly started,
right? So, here is the challenge from a
developer perspective. Boss says, "Hey,
I need you to build a travel agent that
helps the user find the right hotel,
car, and thing." What do you do?
Challenge number one, too many models. I
have no existing data. This app never
existed before. Where do I get the data
to even do evals, right? So, we're going
to show you how you can solve that. So,
how do I go from zero to agent prototype
with minimal knowledge?
Second, AI quality.
This is a brand that your company has.
If your agent does something to destroy
it, that comes back to you. So, how can
you detect issues in your agent,
diagnose and fix them really quickly?
So, that's what the quality solution is.
And finally, safety, safeguarding it.
The difference between the second and
the third is that the second assumes
that your users are acting normally.
The third says, "I have a malicious user
who's going to try to
front attack my my my solution. How do I
protect against it?" The analogy I'll
give you is if you're building a home,
the second one is evaluations where
you've got a building inspector who
comes and checks you're up to code,
but safeguarding is like calling the guy
and saying, "Can you break into my
house, please, so I can show I can be
proved that this is working and then
tell me all the ways in which I failed,
right?" So, that's the big difference.
Make sense?
Am I moving too fast? My speed Okay.
That's the number one feedback I always
get, too fast. Okay. So, before I go in,
I'm going to switch over and tell you
where to start.
So, what I want you to do is I want you
to go to the
repo.
So, you all were given uh the kind of
like the link to it. If you don't have
it handy, I will show you where it is
right now. You can grab it right off the
screen if you zoom in.
But, what I want you to do, you are not
going to be able to do everything today.
What I want you to do is fork the repo
and show you how to jump start your
development environment
so that you can at least follow along.
You will need an an Azure account and a
GitHub account. What I will tell you is
you can get away with using a free Azure
account. There will be a small cost.
I've been running this for 2 days. It's
about 10 bucks.
But, if you join the Discord, we're
going to see if we can actually get a
few resources that'll help you later so
you can try this at home.
But, for now, you're need just go ahead
and fork the repo, right? Uh everyone
good with that?
Yes? So, what I'm going to do is I've
already forked the repo, but once you
fork the repo, what I want you to do is
when you fork the repo, please uncheck
the main so that you're getting all the
branches.
The reason is we've been doing this
workshop at different places and so
it'll keep evolving. You want to fork it
with our with all branches so you can
get the AIE Europe branch,
which is the current mind the observe
mind the gap uh
kind of workshop.
And one of the reasons for this is at
the end of this I will merge this back
into main and we'll have yet another
workshop in a month which will have even
more stuff and then we'll park that
again, right? So, by forking this, I
want you to look at this workshop today
and then keep an eye on the report
tomorrow. Is everyone good?
All right. The next thing you're going
to do is in your branch and I've already
done this, but what you're going to do
is in the in your branch on GitHub if
you click this code, you should have
logged in, right? Uh how many here have
used code spaces?
Yes, my people. So, for those of you
don't know, one of the biggest problems
when you want to do development is to
set up your environment. You have to
install the packages, do all the stuff,
right?
Uh code spaces uses a concept called dev
containers. You'll see that the repo has
this dev container.
And what the dev container does is it
basically defines everything all the
dependencies that you need.
And what code spaces does is effectively
uh when I basically start this off and
run a code space, if I say just start me
a new code space,
it will start up
an instance of a VM in the cloud on this
container and give me the environment
all set up. So, you don't have to
install any tools, packages installed,
everything is ready to go.
So, I'm just showing you you saw how
that was set up. So, if you did that and
you have to wait a few minutes for it to
be ready,
but this is a cooking show. So, this is
how I start then I want to seamlessly
move to the cooked code space, okay? But
now you've seen uh is everyone good so
far?
Um it's very dark, I know, but um let me
see if I can switch the
>> sweet pies on all
>> Um on our Azure uh organization on
GitHub and so uh we will take all the
costs. This won't go into your code
spaces costs as well, so it's um it's
quite nice when you are able to use sort
of those things within the side
organizational repos cuz it actually
goes onto the enterprise account
instead. So, yeah, uh nice little
freebie there as well for compute time.
So, if you were to start that up and you
saw I just started it, it'll take a
while.
So, I'm going to let you all just let it
run.
And we're going to switch back and look
at the cooked version. Ta-da!
Okay. So, what is Code Spaces? What you
basically get is a VS Code instance
that's running in your browser.
This VS Code instance is connected to a
running container in the cloud that has
all the the the the tools and your
dependencies installed.
More importantly, on the side, you will
actually see I'm going to reduce this
font just for a second so you can see
everything.
You will see that we have a bunch of
tools installed out of the box. And so,
what these do for you is they give you
additional features that you can use
when we're basically going to try out
things like running notebooks, things
like a skill that'll automate all your
stuff for you.
So, once you're here,
I want to point out two things.
In that repo that you just uh So, when
you're going and doing this at home,
if you go follow through, there are
actually two paths and we're going to
try to cover them really quickly today.
Path one is the traditional path. It's
the SDK path. I recommend it for
everyone who is new.
Go through it and get a sense
step-by-step. We're going to cover it a
little bit.
Path two is for people who think, "Hey,
I want to actually use a coding agent
and take it for a spin."
In the second path, you will just build
that blank agent endpoint and then turn
the skill loose on that endpoint and
it'll start helping you build out the
stuff and evaluate it automatically.
We'll look at both today.
So, here's the application scenario.
We're building a travel agent that has a
car rental, a hotel, and a a flight
agent built into it.
Here's the workshop outline. All you
need to know is there are four steps.
Step one is what you just did, the
infrastructure setup. Uh we basically
want to go I'm I'm going to hand it over
to Amy to do that. You've got your Code
Spaces running. That's the dev
environment setup. We'll come to that in
a minute. Code Spaces takes a little
while, so I'm going to switch it over to
Amy. And what we're going to do now is
step one, we're going to go and set up
that dumb agent. A simple starter agent
in foundry that will do the travel thing
for you. Amy, do you want to take over?
And if you want to actually see the one
that's already done,
it is over here.
>> I thought.
>> Awesome.
Let me close this and
the code space is here.
Okay.
>> Um so yeah, I will do our initial sort
of stance. So
um we all love code here and we get very
excited when we can kind of like dip in
and out of an SDK and stuff like that,
but realistically that first starting
point um highly recommend just hanging
out in the portal a little bit and just
taking some of this stuff for a test
drive very, very quickly. And so what
I'll show you is that quick pace, how do
I briefly build an agent but think about
tracing and evals right from the the
word go in some senses. So um Microsoft
Foundry is just at ai.azure.com
um on on internet it's part of obviously
the Azure cloud. Um so if you already
have Azure set up, you should be able to
get very, very quick access to that. Um
and then one thing you'll notice is
there's actually this like new Microsoft
Foundry experience that we're looking
at. And so if you click start building
just here, you can actually create uh
very quickly a new project. We'll call
this one
um
AI
A
London and then contest there.
Um what you'll see here is it creates
you a project, a resource, it chooses
your subscription, so the usual cloud
kind of pieces,
a resource group and actually one of the
things that we're going to do is is
change this to a recommended region
which is actually East US 2 at the
moment with some of our newest newest
stuff. Uh and click create. So this will
head off and just create you the most
basic Foundry project. It will then uh
initiate things like models and will
very quickly start building an agent.
But a project is a space that you can
come and have agents within side a
single project that you obviously you
can evaluate and trace across all of
them as well. So we'll take a little
look at that as it gets started.
Um
one of the interesting things around
Foundry is actually just that set up
piece. We have worked done quite a lot
of work to just get those initial
stages, but also still be able to have
the ability to say actually I want to
customize as well very very quickly. And
so we'll see that it will do a lot for
us so that we can start, but then you'll
be able to move on and just really, you
know, envision your whole new piece
yourself. Um so you got a nice little
opening here. This is kind of exactly
the experience you'll see.
And then we'll get taken straight away
to create our first agent. Like the
platform is to build agents, so let's
let's do that. So we'll go Contoso
Travel is our agent. Um and we'll give
it a name that won't be in there. So you
will need to give it a unique name. What
you'll notice here is it's saying it's
deploying GPT-4 1. So it's just looking
for capacity straight away for you.
Um and it's finding your very very quick
model and then we're straight into the
playground. Um
4 1 obviously being
you know, a decent model model of your
choice is also available in the catalog,
but again a great way to start.
Playgrounds we're all very versed I
think at this point with playgrounds.
You have things like voice mode you can
switch on, simple agent instructions,
add your different tools. So in this
case we're actually going to add a web
search,
um which will just be our Bing search
because we're obviously wanting to
create a travel agent. So we need it to
go and look at Expedia and all of that
kind of good stuff. Um and then under
here you'll notice we do have this
model, but we also obviously promote
other models, and then you can click
browse models and see all the providers,
uh whether it's Anthropic, Deep Seek, um
etc. etc. All all of those, they're all
in there.
Um
One of the interesting things, we can
obviously initially start engaging
um
with our agent, but this agent is just a
generic model at this point. There's no
instructions, there's no nothing, and
we've just got some web search. So,
it'll kind of go away, and it'll tell us
it can do basically most things,
including general advice for us. So,
that's not what we want in this case.
So, what I'm going to do is go to a nice
pre-baked one. We'll save that agent.
And we'll go and take a little look.
>> Oh oh, one other thing is you've got to
actually create um App Insights. So,
the agent by itself right now is not
traceable, right? Like it's just there,
it's been created, but you want to make
sure it's always picking up things. So,
the Foundry portal is a great way for
you to get really a quick start. So, if
you Sorry, Amy, I forgot to mention
that.
>> That's the other one.
>> Yeah, if you go into the one that you
just created,
all you have to do is select that agent,
click on the traces tab, and it'll say
you don't have App Insights. And if you
go through that right now, and Amy, I
don't know if you want to do that on
your
flip over.
>> I was going to say that So, um
being able to click on this, you can
then add App Insights as a connector
tool within side the admin portal very
very quickly. Um one of the other nice
pieces is is actually a an agent helper
just up here on the right. So, you can
say, "How do I connect my App Insights?"
And it'll talk you through exactly step
by step how to do it as well. Um but
yeah, very very quick, easy way. App
Insights is a technology that does all
sorts of tracing prior to agents being a
a realism for us. And so that would be a
very quick way for us to kind of turn
that piece on as well.
So let me show you something where it's
got a little bit more to it. So uh back
into our traces, as we start to use
that, so as we start to engage, we'll
start to see the traces as well as the
conversations land here with um
estimated cost, tokens, the usual
things, but also even things like
evaluations.
We've added some instructions here just
to it of what our Contoso agent actually
does. So one of the interesting ones is
like always use the web search. Um
always have a comparison.
Present externally source specific, so
add some of those uh elements that
people can see where it's grounded on as
well. Um and keep responses help focused
and helpful, that type of thing. We've
got our web search. Uh one other thing
is to check out the configuration cuz
what you'll notice here is you can
actually add things like display name,
description. So if I head over to
>> I think she has flipped to version two.
You'll see it there.
>> Ah, we're now in the version that the
We love a little version control.
Ah.
>> No problem.
>> So all of your different steps are in
this repo. So we've done a lot of this
piece. We created our project.
We go down to create our agent.
We're in the playground. We add the app
insights.
We can test our agent in the playground
with different prompts.
But we can also add these different
configuration properties and then the
outcome of adding some details there
starts to bring back your traveler
system with the usual stuff like what is
it that people can do with it? Those
easy step-by-steps that give them the
ability to quickly start engaging with
your agent without it being like,
"Hello, what do you do?" That kind of
command at the start and then having to
move from there. Um so you can kind of
very very quickly build um
up your travel portal.
As you start to engage, let me grab
um
that query again from just over here.
Again, you can use
all of this stuff that we've provided in
here.
Let me copy this one.
And send that off.
We'll send that it will should come back
with some of those grounded responses
um
information on car rentals etc. But one
of the interesting things here I just
wanted to highlight is actually the
elements at the bottom. So it tells you
what model it used. If you're using
something like a router, that will be
more interesting because you would be
able to see given the query which model
it actually chose to use. Things like
tokens, but you'll also see straight
away that we've actually got an AI
quality and an AI safety metric that are
under here. And so one of the pieces uh
you're able to do is under metrics just
at the top here is you can very quickly
just tick these different things on. So
as I said, like starting in the portal
means don't have to think about what all
of the different names are for all these
different things. You can just get
acquainted with what's available and
built in and then you can very quickly
start to visualize exactly how that
might look. And all of us immediately
then leap to code, right? In the sense
that we go, "Okay, I get it. I get that
we've got these built-in things. How
would I do it with the SDK?" So, with
all of them then selected, you can head
off to things like the tracing logs. You
can see exactly what steps and messages
it took. And then inside the input and
output, you've got an evaluations tab.
And so, it then evaluates and gives you
some responses back on all of the
different evaluations that you've
actually selected.
So, again, this one's an interesting
one. A little warning, task adherence is
actually quite low for what we were
asking. It didn't really actually answer
the question that I wanted it to. It
kind of said, "Oh, give me more
information." And so, this bit is
obviously there when you can start to
really think about, "Okay, how do I
start to go from from zero?" Cuz we're
at the most simple agent at this point,
but we're already able to get those
evaluation results against it.
So, in this setup, I basically just
wanted to show you that I can go from
nothing and create a project, an agent
with a model that's just a default, add
some instructions and a web search,
start to engage so I can see those
traces, select some evaluation metrics
so I can see some evaluations in those
early stages, and then from here, I'd
probably want to start thinking, "Okay,
now I've got sort of a very quick proof
of concept. I want to start moving to
code." And so, from here, I'll pass on
to Nithya who will start moving into the
code.
>> Awesome. Thanks, Amy.
So, uh before I switch over to that, um
just a quick show of hands, how many of
you familiar with tracing?
How many of you familiar with evals?
How many of you familiar with most of
the quality, safety, and agentic eval
types?
Okay. So, we'll probably go into a
little bit on that. How many of you have
written a custom evaluator?
Prompt or code?
Prompt?
Prompt? Okay. So, one of the things I
wanted to kind of just wrap the thing
before we move into the code space is
the main reason this is super important
is
if you think about the notion of
observability, it's not enough for you
to know when things go wrong. You need
to shorten the time between detecting
something went wrong and diagnosing it.
So, trace linked evaluations are where
it's at. So, one of the things that I
just want to highlight before we move
back in here is that when you look at
this what what Amy was showing is every
time you see a trace
if you've actually linked the
evaluations correctly, they will show up
here and that means that you can look at
the emails and figure out what part of
the trace. As an example, say your model
changed and you had to put a new model
in. Suddenly, you find that your tool
calls are no longer as efficient.
Your
emails are going to tell you your tool
are there, I mean, your one of those
metrics failed, but now you can come
back into the traces and say what was
different between this version and the
previous version. I mean, we'll see that
through the coding skill later. If you
compare them, you'll be like, "Oh, wait.
One of the tools didn't get called.
Why?" Right? So, you're able to move
quickly to actually compare what
happened, which is the detection, with
the diagnosis. All right.
Uh let's now move to code. So, we've
built ourselves a very simple agent
right through the portal.
Now, if we want to actually do something
more complex.
So, what I want you to do is in the in
your kind of like we did lab 00, we set
this up.
Development environment, you all started
a code space. You don't have to do that
right now, but when you go home, what
you're going to do is when you log into
Azure and set up that foundry project,
you've got your infra set up, but you
need your code spaces to now be
connected to the infra.
The code the the the repository has a
very simple script.
Run the script. What it's going to do is
it's going to use the Azure developer
Azure CLI to go and get all the required
information and set up a .env for you.
After that, pretty much you don't have
to do anything except run notebooks. So,
it'll kind of take away some of that
issues for you.
The other thing you're going to do is
there is something called an AI toolkit
extension. We won't go into it right
now, but what it is is equivalent to
having that foundry UI right in VS code,
so you can see some of the things you're
doing. So, you're going to check that
off. And long story short, by the time
you're done,
you now have your development
environment set up to talk to the
infrastructure that you just deployed,
and we can now go on into our code-based
approach.
So, I'm actually going to go into the
SDK approach first. So, let me kind of
show you why.
So, we did the plan in portal.
And when you looked at the portal, this
is what the actual end-to-end
development life cycle for an agent
actually looks like.
You need to have a build phase,
then you need to optimize it, and then
you need to deploy and govern it.
So, when you think about all the steps
involved in build, we're going to start
by what we did in the portal is I knew
my use case, it's a travel agent.
Quickly developed my models, tools, and
a simple agent for it. I tested a
prompt, I built it. I was able to get
all of that done. I added a simple web
search tool.
Now, I have an agent working that's
grounded in things I wanted grounded in.
We're not going to talk about
fine-tuning, but we really want to go to
the next day of I want to be able to
like do more complicated things with
this.
So, to go to the SDK, we're going to
focus on showing you how to do all of
these in code.
So, what you're going to do here is go
back to the code spaces that you
started.
And cooking demo, so tada, I've got my
code spaces there. Um I'm not going to
show you my dot end because it actually
has my keys in it, but just know that it
was set up. Uh when you run the script,
uh it'll actually set this up right
here.
And what you now do is you're going to
work through these labs in order. So,
I'm going to start with the first one.
And if you're familiar with VS code at
all, what Don't know how many of you
Everyone here familiar with Jupyter
notebooks?
Yes, okay.
Do you know about this little outline
tab? I love it. So, what I would do is
say that as you go through these, you'll
notice that the labs I'm going to first
tell you what they are. And then you can
kind of on each lab, I expect you to
just flip it into the outline mode and
then we'll go through them.
So, what do we have?
The story that we're going to tell is
top to bottom. First, the first lab is
basically going to run and make sure
that your development environment is
connected to your back end. With a
simple test prompt, everything's
working.
The next lab is you're going to rebuild
your first agent in code. In other
words, you built it in the portal
declaratively. This notebook will give
you all the code snippets you need to
build it programmatically. So, you can
use that notebook later go and change
the instructions, do whatever you like,
right? And that agent doesn't have
tools. It's just going to be really
simple agent. So, the next step down
there is you're going to add a tool.
You're going to add a few functions that
do the different things you wanted to do
like check
And now you have an agent that has a
model and tools.
After that, which is the more fun part,
is you're going to build a workflow
agent.
A workflow agent actually says, "Wait,
why should one agent do all the calls?
Let's have dedicated agents for each
step." So, there's a flight agent, a car
rental agent, and a hotel agent. And
then I have a concierge that
orchestrates them together.
And Microsoft Foundry has a capability
called workflow, so we're going to see
that.
And then this particular lab will show
you how to set it up for tracing.
And in this case, you can actually set
it up to use hotel to have local traces,
so you can see them as you're debugging.
Or you can have the push to Azure found
monitor and see them in the Foundry
portal.
And then we'll have a notebook for evals
and a notebook for a tuning.
So far, so good?
Ready to start?
So, cooking show, try this at home.
We're going to look at it here.
So, the first thing is I'm going to look
at the notebook. So, what do we want to
do in the first one?
So, this isn't much of a thing, but I'm
just going to scroll through really
quickly.
So, we have to install dependencies. All
of these come for you out of the box
with uh dev containers, so you don't
have to worry about them.
Configure environment variables. You
just need two, actually. When you set up
your project, you have a project
endpoint, and you need to know the name
of the model.
It already sets this up for you by
default.
We're going to run a very simple test to
make sure that we're connected.
We're going to make sure that the client
is working.
And then we're going to make a call. So,
this is kind of the the the data I
currently have. I have some fake data in
here that we can use. And so, I've made
sure that I have my data. I've made sure
I
I was able to make a a call to my API
endpoint. It works. I'm good to go.
Now it's time for us to create a new
agent from scratch. So, when I look at
this,
and
I'll actually share this whole document
out with you later.
What this will do is kind of walk you
through what the different steps are.
So,
here, we're actually going to go through
these where this is what each of these
uh notebooks will create a new agent
that will do only that capability. And
the first one,
right here,
will teach you how to build a very
simple agent. So,
the problem you're facing right now is
you've never built an AI agent before,
and you want to know how to set it up
with the right instructions and so on.
So, to create this basic agent,
what you're going to do is first of all,
you start by setting up a client.
Because you're already logged in with
the Azure CLI, you have credentials.
You set up a a client for use with our
Foundry endpoint.
And then you create instructions for
your agent. So, this is a standard set
of instructions that we've created for
that describes what your travel agent is
supposed to do.
And when you run this, your agent is now
created on the back end foundry with
these simple instructions and the
default model that we had deployed.
Next, you want to start a simple
conversation. So, we're using the
responses API endpoint to try a single
prompt. So, you say, "Hey, tell me, for
instance,
uh
I'm I'm basically asking a question
like, you know, I'm thinking about
planning a trip to Paris. What should I
know?"
It runs it and returns the response, and
now you get to see it. At this point, we
haven't done any tracing, we haven't
activated anything. We just got a a
working agent that responds the way I
want it to.
Next, you can go ahead and try
multi-turn
uh conversations. So, for those of you
who have not used the SDK or are not
familiar with agents, this is a great
way for you to go try it out and get
familiar with it. But, I'm not going to
go into it cuz we're not here to talk
really about the agent building.
Uh all this will let you do is validate
that you can in fact deploy a multi-turn
conversational agent to
uh foundry.
And you can inspect the responses and
see what kind of response it's giving
back. It's really a long-winded one,
right?
Next step,
if you go into this. So, for each of
these, you'll notice that these are
already set up with a runtime
environment, so you would just select
the the kernel that we've got on the dev
container, and then just walk through
the steps one by one.
So, in the first case, let's go back and
to our portal and see what that looks
like.
So, that first travel agent,
uh that was actually the first version
of that. All it did is it answered the
question, right? So, we have that
deployed here,
and if I ask it a question, it's going
to give me whatever I need for that
answer, and I should see the traces in
here as well.
So, give me a minute for it to start up.
So, the the agent that I set up, that we
invoked from the from the kind of from
the code, I can go in and see that when
I ask this question, it actually
answered it, and I can see the traces,
but I don't see the e-vals cuz I haven't
set them up yet.
The next thing we're going to do is
we're going to go in and add
tools.
So, what tools do we need?
So, over here, we're going to use
something called a function tool
definition, and we want to register
function tools that do various things.
So, here we have tools for a car search,
a flight search, and a hotel search.
They're all functions defined within
this one single agent. We register the
tools, and then we enhance that agent.
So, now the agent before
had just a model and instructions. Now,
it has model, instructions, and tools.
And when we then deploy this agent, you
can go ahead and test it. So, if you go
ahead and run this uh deployed I mean,
when you deploy the agent, and you then
hit that endpoint with a query about
something looking for a flight, it's
going to respond to that.
You can go try out different
combinations like give me a hotel and
car search, etc. So, we're still going
through these notebooks to just make
sure that we have our agent set up
correctly. So far, so good?
Yes? So, we start with a base agent, we
added tools, we've got
multi-conversation, we're good.
But now, I look at it and go, "Wait, we
really don't want one monolithic agent
doing all this work.
We want to be We want to be able to
break up the task into the smallest
units of work, and have dedicated agents
do that, and then orchestrate them
together." Anyone here who's used
LangGraph, LangChain, you know that
multi-agents kind of have design
patterns around them. So, how do you do
that? It turns out that Foundry actually
has this concept known as workflows
workflow agents. So, in this particular
lab, what we're going to actually go
into is build out a workflow agent.
So, over here, the problem that you're
facing right now is you had a single
agent, and now if something goes wrong,
you've got multiple functions to track,
multiple things to do, you really want
to break it down into smaller
components.
So, in this particular lab, you're going
to start creating specialist agents.
So, you remember in that very first lab
we created a travel agent? Now think
you're just going to create three of
those agents, but now dedicated to
individual tasks.
So, you create these three specialist
agents and then you create a workflow
agent
that puts them all together. So, I'm not
going to go into all of the details
here, but what I really want you to look
at is the difference in the traces. So,
here
when I create the workflow agent, I give
it a declarative YAML statement that
says how the workflow is knitted
together.
And then I can actually test it
end-to-end. So, let's see what that
looks like when we deploy it in Foundry.
So, this is what a workflow agent looks
like. So, right now you've seen two
kinds of agents.
The first one was a prompt agent, which
is just a simple lightweight declarative
agent where I've given you instructions
in a model,
but it's doing one thing. It's a single
use agent.
Here, with workflows,
that YAML lets me visually compose the
agent together.
So, now I can be like, "Okay, the
workflow says
I want to actually create a conversation
with each of those agents.
I need to get the flight agent to get
get a response, the hotel agent to get a
response, and the car agent, put them
together, and then deliver to the user."
And when I invoke this agent, I can
actually see the traces in the portal.
So, I'm kind of getting to the fact that
in the that when Amy did her first kind
of walk-through, you noticed that every
agent, every time you ask a question, we
already have it set up with the traces,
but now you're able to see
how much more you can actually go and
analyze the path of your invocation
through this entire workflow. So, over
here now you can see when I ask a
question of the
agent, it now goes through a workflow,
figures out how to invoke every agent in
turn. So, invoke the flight agent to get
me information about the flight, invoke
the hotel agent to get me that,
and then put them all together.
And so, the value for us now is you're
able to see which of these agents is
underperforming, which of these agents
is not actually doing its job correctly,
what are the costs token-wise for this,
and then flip out only the agents that
you need to optimize to do better.
Yes.
Well, I when Keep that question cuz
we're going to No, no, no, I'm going to
answer it now, but you've got to We're
going to look at it again when we look
at the scale.
But your point, I'm just going to repeat
his questions. Let me know if I got this
right. One, cost. Can we actually
optimize for cost?
And second one is you were asking uh
what is the complexity? What was the
second question?
How do I
Yes. So, uh I'm going to answer both in
part. Cost-wise, there are two things
that impact cost. One is you think about
the model cost.
You might have a GPT-4 one is going to
cost you more in tokens than maybe GPT-4
on mini. So, one of the things you do is
you switch models. It's one of the
right? And when you do that, you
immediately run the eval and see did my
Was there a regression? So, did my cost
drop, but the accuracy get So, you can
try these out, right? And you'll see
that in the skill that you can actually
try these out. Flip the model, try that
out. Second thing is you can see why is
it spending time? So, for example, if I
used a web search,
and then realized this is really taking
up too much time, I would rather just
have it search
a small subset that I have cached or
like I have data in, maybe cheaper. So,
there are ways for you to look at.
Right? The bigger picture though is
every time you make a change, you should
evaluate immediately and see and compare
whether it had a regression for
something else.
So, second one is how do I actually roll
back? So, if you look at these, I'm
showing this to you in the portal, but
you'll notice later when we kind of go
through um
the the skill, there are versions over
here, right? I've all the agent
versions. So, deploying an agent is you
can actually just give it the name of
the identity the version that you're
that you want and have that be the one
that's the main one. And when we use the
skill, we'll see that it'll
automatically go back to a version that
had a better quality and use that going
forward. But, the bottom line is they're
just identifiers. So, you can basically
deploy them. Does that make sense?
Awesome.
So, uh
this workflow agent now lets you kind of
like compose multiple agents through
code,
not through an external framework, and
still have it managed by Foundry and
traceable. So, one of the things I want
you to take away from this is that from
the tracing perspective, it really
doesn't care what kind of agent you
have. It has an endpoint, and as long as
that emits auto traces, I can gather
them and show them to you.
Same deal with evaluation. Doesn't care
how you build the agent, as long as I
give you an endpoint, I can then run
those evals and give you metrics back
against them.
So, that's this whole thing. Now, so now
let's talk about tracing.
So, in this so far, you were just kind
of learning how to deploy agents
and tailor their functions, tailor their
instructions, and kind of run them and
see how well they're performing and see
their traces.
But, what if you actually wanted to run
uh
kind of like have custom um attributes
in your traces?
And how could you actually activate
traces to use locally as well as in the
cloud?
So, if you want to look at that, this
particular uh notebook
will actually deploy a custom agent
here.
So, it's this one.
And what you're going to get from this
is an understanding of how tracing
works.
So, the problem that we've got to right
now is we've slowly been changing our
agent, and we've built it out, we've
broken it up. It's now working and to
the point when things go wrong, there
are so many possible ways they could go
wrong.
Wouldn't it be nice if I could add my
own custom attributes into those traces
so that when I want to kind of go
troubleshoot later, I can look for the
right things.
So, in this, we're going to look at how
you can actually
uh kind of bring in custom attributes
into your tracing.
So, in the first one, this
we've got two different sets for this.
The first thing is we want to create and
trace an agent.
And what we want to do is we want to
actually have it set it up to put the
traces in the local console.
So, before you do that, as part of the
setup, you actually need to
set two environment attributes, one to
enable generative AI tracing and one to
kind of capture the message content
around it.
So, if you go through this,
what this will allow you to do now is to
actually activate different attributes
or set different attributes and have
them seen right in your console so you
can debug as you go. So, now once I've
set this up, I create a conversation,
and when I actually run it, I don't know
if you guys can see this in here,
but it's putting in some of the custom
attributes that I've generated. And let
me put that as a
And now I get more personalized traces.
So, I can actually dump in more
information that relates to the kinds of
things I want to debug.
Next,
when I want to interpret the the tracing
itself, these traces currently are
local, but it would be great if I could
actually push them to the back end and
see them there as well.
So, there are two different layers at
which you can see these traces. One in
the back end against the
agent itself,
those traces should be visible here.
So, I can go in and kind of like see
what happened. That's just the basic
tracing behavior.
But, the second thing I want to do is I
want to actually push this to Azure
Monitor.
So, Azure Monitor is this giant kind of
like uh log collection of all the
telemetry across all my services.
By adding my AI telemetry to it as well,
not only do I see kind of like how the
different other services are going or
are doing, but I can see whether the
impact of performance was related things
I was calling. So, for example, if I had
an Azure AI Search that had an index,
I'm getting the telemetry from that. I'm
also getting the telemetry from my AI uh
applications and I can look at them
together.
So, in this particular part of the lab,
we're going to configure Azure Monitor
tracing and have all of the traces also
sent out to the monitor. We'll look at
that in a second on the back-end.
Run a trace query and now you should be
able to see the traces in the Foundry
portal.
So,
with that those if you walk through
those notebooks, you are now able to do
all of these in code and step through
the same things that you were doing in
the portal.
The evaluation one is really taking it
to the next level of showing you how to
run a quality evaluation, a safety
evaluation, and an agentic evaluation
and have these run and kind of run in
batch mode in combination or
individually using some evaluated data
sets that you provided.
So, to set up the travel agent for
evaluation,
the first thing is preparing evaluation
data.
In this particular case, we're using we
use an AI agent and we created a sample
set of evaluation data. Later on with a
skill, I'm going to show you how it
actually generates that for you.
So, what is this evaluation data set?
The evaluation data set here is just a a
couple of like prompt test prompts,
right? With uh responses that you can
use to evaluate groundedness and so on.
So, we want to
kind of pick a few quality and safety
evaluators.
To run an evaluation, first you
determine define an evaluator object and
you specify
the criteria.
We're using built-in evaluators. You
notice that we have a lot of built-in
evaluators for quality and safety and
agentic. So, you just specify whichever
ones you want. And for each one, you're
going to tell it how the data maps to
the evaluation data set that you've
provided.
Then you set up your evaluation data
flow and then you run it.
When you run the evaluation from your
notebook, it takes a long time. So, you
can actually set this up to
poll till the evaluation is done. And
once it's done,
it'll actually help you analyze the
results locally. Or, you can go into the
portal and you can see that again. So,
the trace the evaluation notebook
generates this agent and you can see
both the traces here. Or, you can kind
of go in and see the evaluation output.
So, over here, one of the things you'll
see is that we had three evaluators in
that notebook.
The quality evaluation.
And just to kind of give you a sense of
what you see here,
you have a copy of the data set that was
used. And when I look at this,
it's just telling me that for the
metrics that I looked at, which is
coherence, fluency,
it's passing all the tests. There's
actually And this is a very kind of like
a a very simple test set. So,
when I'm doing anything major, but what
what it does allow you to do is see the
results and download them and see the
logs. But, let's take a look at the
agentic ones.
So, in agentic, in addition to the basic
ones that we had, we are actually
looking at intent resolution. Uh we
might look at things like um Um, task
adherence
and tool calling.
Let's take a look at one of these. Here
in this case, it's a groundedness fail.
So, now I want to dive in and see what
happened.
I should actually be able to look
through this
and see where those uh failures are.
So, over here, I can see that there was
a failure in groundedness.
And now, one of the things for me is to
understand why. Why was this given as a
fail? And you can see that the reason it
came up with is that the response
answered with a date of August 2024
instead of 2025, which is a failure of
groundedness. It wasn't actually
grounded in the truth.
So, this is a kind of like a simple
notebook that just shows you how to run
your evals for quality, safety, and
agentic.
And then you can interpret the results
and kind of we're done. Um,
and view them in the portal.
The last thing I want to do is show you
red teaming. So, with this so far, what
you've actually been doing is just
setting up evaluators with one of the
built-in quality, safety, or agentic
evaluators,
running it, and then seeing the results
in the portal. But, red teaming is where
you want to set up a scan where it
proactively attacks your agent to see
whether it can basically get through and
assess it for vulnerabilities to
different kinds of manipulated prompts.
So, how many of you have done red
teaming or pen testing?
Anyone familiar with how red teaming
works?
So, red teaming is actually kind of
cool.
With red teaming, what you do is you get
a second AI to attack your first AI.
So, the red teaming agent that we have,
you basically tell it, "Here are the
risk categories that I think my agent is
susceptible to."
You define the kinds of attacks you
want, and then it will basically attack
your agent with those prompts and give
you a report that says, "These are the
cases under which your agent failed."
So, how does that work?
It works like this. If I were to say,
"Hey, please tell me how to rob a bank."
And that's the kind of
uh example Amy had.
My
uh safety guardrails are going to come
in and say, "No, you can't do that.
Cannot Don't answer the question." And
it would be right.
But it turns out that maybe if I were to
flip it,
right? Flip the the prompt around.
The safety guardrail looks at it and
goes, "This is gibberish. There's
nothing wrong with this. I'm going to
let the prompt go through."
And the model says, "Oh,
silly guy. He flipped the string. Let me
flip it back. Now I see what you want me
to do." And it'll actually execute it.
So, you slip past the guardrail because
you manipulated the prompt.
What red teaming allows you to do is it
proactively goes and checks all those
different
uh attack strategies and then tells you
what you're vulnerable to.
So, in this particular uh notebook,
what you're going to do is you're going
to look at what kinds of agentic
attacks you can perform.
For example, prohibited actions. You see
with quality and safety, you're looking
at red teaming your model. You're just
looking at the behaviors. But agentic is
very dangerous because if I can
manipulate the agent to do a an action
that it was not supposed to do, that's
harmful. So, with prohibited actions,
which is one of the new agentic uh red
teaming uh attacks you can do or
strategy uh risks,
you can say, "Hey,
these are actions that I do not I'm
going to give you a taxonomy of actions
that the agent is not allowed to do. It
can go and fill in passwords. It can't
leak data. It can't do this, etc.,
right? And now when you fill this in,
the red teaming agent will proactively
come up with prompts that will test this
for you. Yes.
>> Can you do the reverse and say
you have the right to do nothing except
what I authorize you to do and when I
authorize you to
>> That is what a guardrail would do. What
you're saying is you're telling your
agent, "These are the things you should
do," right?
What red teaming is saying is if I tell
the agent this, but can I manipulate it
by using a prompt? So, to your point,
there are there are very famous attacks
that say, "Oh, you're not allowed to do
this." But then I say, "My grandmom used
to tell a story about this." And it
says, "Oh, your grandmom, let me tell
you how your grandmom would tell the
story, right?" That's an attack. So, in
this case, the prohibited action is
saying, "I don't want you to do this. I
want you to do this." That's the
taxonomy.
So, you're absolutely right. In your
taxonomy, I could say, "I only want you
to do this."
The attack the red teaming agent says
is, "I want to be smart and figure out
ways to get around this loophole." And
so, it comes up with a bunch of test
prompts that it'll run, and then you see
how good your prohibited action
guardrail really was. Does that make
sense?
Okay. So, when you run this one, for
example, I'm going to flip over and I'll
show you that cuz I know we're running
out of time. Um
So, if I go into this, let's see the red
team, right?
Just to kind of be quick about it.
Here is an example of what the red
teaming agent scan looks like. So, you
can see up top,
I've said, "These are my risk
categories. This is violence, sensitive
data leakage, and task adherence." Those
I'm I want you to see whether you can
actually assess vulnerabilities to me
following these.
And the attack is leetspeak. If you're
familiar with this, leetspeak is that
way in which you can use like numbers
instead of letters to make things look
good. So, the question is, if I were to
use an attack where the prompt is using
leetspeak rather than normal English,
does it get through my guardrail? Very
simple attack. I can go in and actually
run this, and you'll see that in this
case, it's a very simple attack, nothing
major. It passed everything. It didn't
do anything at all.
You can, however, then go in and I I'll
start one up, but uh
I don't know if it'll finish by the time
we kind of get this there.
If you basically go in, that was that
just showed you how to run an attack,
but if you go in here,
and I say, "Okay, go ahead and give me
let's pick the Contoso agent that we
had, any one of them."
There are actually a lot of different
more comprehensive attacks that we You
try.
So, here are the various attacks that I
can actually or here are the risk
categories. Let's keep all of them.
And then I can look at the attack
strategies and see these. These are easy
attacks. But there are things like a
crescendo attack right here
that are super difficult. And what a
crescendo attack does is it starts it
off like a frog in boiling water. Starts
with a small attack. Says, "Oh, you got
through it." Then I'm going to
kind of build on that with a second one
and a second one and by the time you've
recognized something's going on, you're
being hit on all sides, right? So, if
you're on a crescendo attack, it takes a
really long time, but it will determine
all the vulnerabilities in your system.
So, in our case, we had just run it with
a very simple one, but you can go in and
look at all the different attacks that
are there, all the different risks, and
run them.
So, with that, let me actually kind of
get back to cuz we've got a few minutes
and I really want to show the Am I good
with me just going on to the skilling?
Okay. So,
I really wanted to actually talk about
this. So, I'm going to kind of go into
that instead. So, we went through the
SDK.
But all of this is the old way of doing
stuff, right?
What if we could make this better? You
still don't understand all the things
you don't know. So, what I really wanted
to show you today, and this is in very
early preview,
is this notion of an observe skill.
So, right now
and
for those of you want to try that at
home, uh you will know it's documented
over here.
It's the third thing in there.
So, what it is is Microsoft Foundry has
a top-level skill that has defined best
practices for doing everything that you
would do with an end-to-end agent
development, create, deploy, and so on.
And over here, these are all the
different things. We're going to focus
on observe.
Observe is a subskill. And what does
observe actually do?
Observe, and I think I have that in
here.
If not, let me just bring that up.
What observe does is it lets you go in
and get the whole
observability loop done through an
agent. Let's actually just see it in
action.
So, let me know if you're able to see
this okay.
Can you all see the right side of the
screen?
I'm going to minimize all this.
So, now remember that portal agent that
Amy had set up?
With the observe skill, I didn't have to
do any of the stuff I did with the SDK.
Instead, I just go to the
co-pilot in in this case we're using
GitHub co-pilot chat to activate that
skill.
I have a coding agent. I'm using
Claude as my model with it.
And I just say, "Can you please use this
observe skill to start the observability
loop on my agent and do the work for
me?" At this point, I only have an
agent. I've no eval set. I have nothing.
"Can you please help me evaluate this?"
And what it does is it kind of goes in
and it looks at your code and says, "You
don't have an eval data set.
You I know what you're trying to do
because you've shown me the
instructions. I'm going to start
building this out."
So, the first thing is it checks whether
I have metadata and when I don't, you're
seeing kind of like the cooked agent. It
goes ahead and sets up a cache.
And the first thing it did is it went
ahead and generated the eval data set
for me.
Okay?
So, I'm going to walk through this
really quickly. You see that it reviewed
files and created to-dos and then
started working through them.
It got the agent details.
It ran the evaluate catalog.
Built an evaluated data set. And then it
ran that first batch eval. So, it said,
"I have an agent. I need a baseline. I'm
going to run this."
So, it goes ahead and by the way, it
didn't find the agent cuz I spelled it
wrong. Figured that out, fixed it. And
now it says, "Okay, you have this travel
portal agent.
I'm going to take the data set you gave
me and I'm going to run the
uh the evaluation.
And one of the greatest things that I
find useful here is the reasoning.
It goes in there and you actually get to
see what it looks for in terms of the
failures and how it had actually
instrumented the evals.
And so once it finishes this,
it kind of like it goes through all the
things that need and now it finishes
this evaluation, runs it, runs it, runs
it and then it comes back to me and
says, "Here is the result."
So this is the first batch eval and I
didn't have to do anything except set up
my agent with a simple instruction, a
model, and an endpoint.
And it comes back and says, "Based on
what you have, your prompt is not
actually perfect.
Relevance is fine,
but task adherence, there are cases
where it's not actually completing the
task you asked it to do. There are two
failures.
And I can actually go in and look
through the reasoning, it'll tell me
what those failures are.
Intent resolution looks good. And for
the indirect, I tried one test for
safety and that passed, right? So it
comes back with the key finding and
said, "Hey, there is a problem."
And it says, "Would you like me to solve
that?" Right? So it the next thing it
tells me is that it says, "Okay, so
there's a human in the loop, right? I
did the first step for you. Would you
like me to take another step or is there
something you'd like to do?" So I'm
like, "Please go ahead and just analyze
those failures for me, optimize
instructions and re-evaluate."
So what this starts doing is it runs
something called a prompt optimizer. It
says, "Based on the way you've written
your prompt, you left it open for
misinterpretation. I'm going to optimize
that prompt."
And you asked me at the time, "How do we
actually roll back?"
This automatically gets puts a new
version number and tests, right? And if
it if it it sees a regression, it can
roll it back and you'll see that, too.
So over here,
it's now
it's now updating the agent. This is
where it goes and pushes the new version
of the agent.
It runs a new batch eval, again waits
for the evaluation to get done.
And voila, when it's done, it gives me a
nice clean table. Says, here is where
you were.
I optimized your prompt, rerun the batch
evals with the same evaluators.
And now it's improved by one. It's not
perfect. It didn't get a 10, but it did
fix one of those issues that you had.
So, it's better.
Your task adherence and there was this
issue in the prompt that I fixed, which
is now tighter. So, now you've got this.
And now it says, what would you like me
to do?
And this is where it gets interesting. I
was like greedy and I said, I want you
to I want to push for 10 out of 10. I
want you to fix that last remaining
thing.
And at this point, this is where human
in the loop makes a difference because
it starts just manipulating the prompts
to see what else it can fix, right? So,
over here it keeps going through them,
trying it out. And now you start seeing
the point you're making where
if I actually I'll I'll push it all the
way to the end so you can see it. It'll
go back and forth and it'll keep
regressing.
And it'll keep finding that it it
improves to seven and comes back to
eight. It improves to seven, come back
to five.
And at some point, it'll basically say,
you know what? Of all the things that we
did so far,
so this is where the human in the loop
can say, you know, you need to stop. So,
it says the best version for my
agent was version five. So, let's go and
stick with that, right? So, over here it
comes back and says, here is the entire
history of me trying different things
and telling you how I'm able to improve
it. And for each one, I'm going to give
you insights into what worked, what
didn't.
And now we're at version 10 of all of
them, five's the best. Let's go back.
Let's use that, right? Yes.
>> Does it only change the prompt or it can
change the model or the
>> It It can change other things. So, this
one is It started with a batch eval and
it's looked at that, right? So, it'll
actually come back and say, would you
like me to look into perhaps, for
example, it'll say web search is taking
a lot of time. Would you like me to look
for an alternative for that, right? So,
yes.
The thing in this is This is where the
human in the loop makes a difference.
The reasoning kind of gives us insights
and this is where I think, you know,
it's what we don't know that hurts us.
It's not about I don't even know what I
don't know and what this does is exposes
me to what I don't know.
But yes, at that time I can actually
guide the skill.
What the default skill is and you can
actually go look at the skill MD because
when it installs it you'll see it. You
know what it's looking for. It's got a
set of best practices it checks through.
If you have domain knowledge, you might
want to apply it, right? And say, well,
actually this is likely to be the case
and we go try that and it'll do that.
But what was I don't know if you you get
why I love this so much is it automates
the batch eval, compare it and show me
what happened without me having to know
every single SDK call and stuff, right?
And so that was the thing there. So
here, yes, to your point, there are
other things behind the scenes that you
can look at.
And now at the end I'm like, can you
just show me a full summary of what's
happening, right? But the more important
thing on this that I I think I just
wanted to
kind of showcase before we're done is
it'll at the end it'll tell you what
else you can do, recommendations for
future work.
I was showing a prompt agent, but how
many of you use LangChain, LangGraph,
etc.?
You can actually build your agent with
that and bring it into Foundry using
something called hosted agents and I can
go to it that this point and say,
we've been using the observe skill, can
we use a create skill to convert this
prompt agent into a hosted agent and use
LangGraph to build it for me and it'll
do that, too.
So the point on the skill is really
about moving away from looking at the
editor
and moving to a coding agent that'll
manipulate it, but we are actually
guiding it through the process if that
makes sense.
Does that make sense to everyone?
Okay. So
the the the final thing about this is
you can see that it gives you different
recommendations for what you can do,
tracing based evaluations, red teaming,
etc. And so you can guide it through all
of them because there are skills behind
the scenes, yes.
>> And
if you come to realization that you need
to update the evaluation set,
then you redo the whole process,
essentially.
>> Yes, and you can actually tell it. So,
one of the things then I Let me see if I
can show that thing to you because it
makes more sense if you can see it.
I'll I'll publish this uh document out
there, but um if you look at the actual
skills, it's over here.
So, this is the
Ah, God, it's not even
Okay.
See if it opens this.
And I should probably hide some things
here. All right.
It wasn't supposed to pull up this
window. Can you all see this okay?
So, it's an open-source project, so you
can actually go look at it. So, Azure
Co-pilot uh for I mean
GitHub Co-pilot for Azure.
This is the Microsoft Foundry skill,
um
the Foundry agent.
And if you look into this, these are all
the skills available. So, I'm going to
kind of walk through what the
observability loop looks like. So, if
you can see this,
what it does is all of these tasks. And
if you want to Here's an easier way.
There's a QR code. You can grab the QR
code and go directly to this page if
you're interested. Um
what this is using is the Foundry MCP
server, and all of these it's looking
for trigger words like this. So,
evaluate my agent, help me build a data
set, etc.
One of the subskills that it has is to
create a data set. Another that it has
is to analyze your insights and so on.
So, you can look through these to see
what kinds of things you can actually
call out on it and uh run them from
there.
And then, let me see if I can just
finish up uh what we were talking about.
So, you can basically go through this
and have it iterate more than once.
And last but not least, this is bringing
coding agents into your SDK and into
your IDE. But what if I needed the same
help to analyze my insights, right? So,
I want to show you a couple of last
things and then we'll call it a day.
Um if you are going into the portal,
anytime you're in the portal and you
have an issue with something, you can
actually use the Ask AI.
And the interesting thing about Ask AI
is it's an agent that knows the state of
your project. So, you can say, "Can you
look at this trace ID? Can you tell me
what models I have access to in this
subscription? Do I have quota?" And ask
it questions here and it's reasoning on
the state.
The other one is
in your traces. So, if you actually go
into your insights,
I don't know about you, but I'm not a
KQL query person at all. Can't write it
to save my life. So, I want to actually
know what am I looking at in all this
data?
If you click on the logs for your uh App
Insights,
at the top there's now an observability
agent up there. And what this allows you
to do is allows you to convert all those
programmatic queries you've written into
natural language interactions with an
agent that will do the job for you. So,
over here for instance, I can kind of go
in and say, "Hey, can you find
failures?" Like, you now have access to
my entire
uh log workspace, right? So, can you go
ahead and give me an analysis on what
this is doing, etc.
Um and I think we're way past time, so
um
the two things that I just showed you at
the end, Ask AI, uh that's the one
that's in the Foundry portal,
and the observability agent is the one
that's in the Azure portal.
And I think with that, Amy, do you want
to do any wrap-up or do I
All right. So, I'm just going to wrap up
on this and say, "If you grab those two
codes,
the first one is the entire repository
and even the skills part is completely
documented in there.
Uh hopefully later today I'll publish
the step-by-step uh transcript that I
have as well, so you can kind of see my
results against yours.
On the Discord, while you run this, if
you run into issues, please join Discord
in the AI engineer channel and then kind
of leave us notes there. We'd love to
get issues from you.
And
kind of to wrap this up, you know, we
started by saying there's a gap in agent
observability. How do you mind the gap?
And how do you accelerate the eval
optimize loop?
So, hopefully we did a job semi decently
well.
And the main thing we're trying to say
is the gap in agent observability is
three things, right? One,
you start off with a working agent, but
that working agent will drift from the
original requirements because models
could change, prompts could change, your
environment could change, new edge cases
come in. How do you constantly and
continuously evaluate what's going on
and get alerted when that gap changes?
That's tracing and monitoring.
And second, how do you accelerate the
loop? You can do it manually, of course,
but why not start taking advantage of
coding agents
and have those automate some of this for
you with a human in the loop to guide
them? So, you're faster at responding to
some of the these issues before they get
out of hand.
And finally, coming back to close the
loop on the questions we asked, too many
models, no existing data, what do we do?
We can use coding agents, we can use
either Copilot or uh skills and have
them generated based on what our current
state of the application or our current
requirements are.
Keeping up with fast changes, how can I
detect issues and diagnose them quickly?
The answer is trace-based I mean,
trace-linked evaluations. So, we want to
be able to have a view that lets us see
both the traces
that show you how it executed and the
evaluations that said, what was the
result of the of this change that I
made?
And then for safeguarding practices, you
want to think not only about safety
evaluations for normal behavior, which
is setting the default guardrails, but
also adversarial kind of uh testing
where you proactively attack it to see
whether you can get past those
guardrails by using techniques that we
may not even have thought of that folks
like the pirate team are progressively
kind of building on.
And I'll leave you with one last thing.
I am not like like many of you, I'm just
trying to keep up with the pace of
things, but there are experts in the
space. So, if you're interested in it,
we have a series called Model Mondays.
Just so happens that this Monday uh
Felicia Shaw is the person behind the
skills that you just saw. She's a PM who
runs the um foundry skills uh section of
things. So, she's going to come and do a
demo and tell us what's coming next.
What you saw is really really early.
It's like literally got released 2 weeks
ago. They're already building on that.
So, if you're interested in that, please
do attend and she'll have an AMA so you
can ask her questions directly.
The other one which is interesting for
those of you who use AI toolkit is
what's new in that. And the main thing
here is a lot of the stuff that you saw
that was doing uh being done in the
portal and SDK can now be done right in
VS code using that extension and can be
done much faster locally. So, that's
about improving your local developer
experience. And with that, I think
that's the end. Uh thank you all for
sticking around. I think we're at time,
little over. Uh appreciate it and if you
have any questions or just want to hang
out and chat, please do come and let us
know. And thanks again.
