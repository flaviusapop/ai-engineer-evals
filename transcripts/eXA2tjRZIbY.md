# The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI

Source: https://www.youtube.com/watch?v=eXA2tjRZIbY

Uploaded: 2026-10-06

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Uh, can everyone hear me? Okay,
awesome. Thank you so much uh for
attending the session. Um, my name is
Vun. I'm part of the team at Resolve AI.
We are building AI for prod. uh
basically we're building agents to run
and fix your software. So in this
session we'll cover what are the six
pillars of an agentic harness that
you'll need in a system that is there to
fix and run your software.
Uh before I get into the session just a
quick show of hands just to understand
for me to understand who's there in the
audience. I'm assuming most of you are
engineers. Uh how many of you have been
on call before? Uh quick show of hands.
Awesome. Have you tried to use AI to
help you with your on call? Show of
hands.
Awesome. For the people who raise their
hands, uh can you tell me that 90% of
your on call work is being done by AI?
Uh can you comfortably say that?
Awesome. Yes, that's what we realized
when we started the company as well.
This is a really hard problem to solve.
So, and in this session, I want to share
like our journey. What is the evolution
we went through? what are some of the
learnings we had specifically in
building such an agentic harness. Before
I get in um I want to set context on uh
what we are experiencing today. So the
first wave of AI really was focused on
coding and uh truthfully I think most of
the most for most of us the way we code
has fundamentally changed and I also
wanted to share context on why that is
the case. Uh firstly code in itself is
self-documenting. It's easy for AI to
actually parse and understand what's
there to help you out with the next
step. Second, inherently code is very
modular. So it's easy for for AI to
actually break it down as chunks and
navigate to the next step and also help
you extend and build and be build beyond
it. Third and the most important thing
is code is single domain. Um you do not
need to teach AI multiple domains to
reason across them. it's easily able to
navigate to the next step and that is
one of the reasons why we have such
defined benchmarks as well. You can
objectively assess how good is AI in
solving this problem for you. But in
reality for engineering 70% of our time
is spent on the other side not
generating new software but rather in in
production systems basically running and
fixing software. uh and this ranges
through a broad range of issues as well
right like operating and running
software typically you can actually put
it in three broad buckets like one is u
think of the healthcare analogy that's
the easiest way I like to think about it
as well one is the regular on call and
maintenance think of this as regular
small problems that are coming your way
maybe you need a Tylenol for uh some for
some pain that you have maybe you need
an Advil so These are the regular on
call style alerts that you need to deal
with. Second category is the incidents
where you need all hands on deck. It's
equivalent to a surgery. Systems are
shutting down. You need everyone's
attention who's uh who's involved or
responsible to come in and fix it. And
the third category is more like your
daily vitamins. So you need to do a lot
of things on a regular basis to keep to
maintain the health of your system going
on. So be it things like taking a look
at your infrastructure, taking a look at
your costs or maybe some platform
engineering work that you do to scale.
So these things are fundamentally hard
because they're not exactly like code.
They cut across multiple different
domains, multiple different tools and
that is the repercussions that we are
starting to see when the euphoria of
initial initial euphoria of AI is
starting to settle in. And that's what
you're seeing in the news right now. So
there's a lot more talk about the number
of issues maybe AI generated code is
starting to create in production and
there is talk around what are the right
frameworks to deal with these uh issues
in code. Second uh the era of bottomless
AI is over like the unlimited AI is no
longer there. You can increasingly see
conversations about tokens token
optimization token efficiency. How do
you basically improve those
architectures, those rigorous
engineering architectures that you need
to efficiently and precisely use AI? And
third, uh this is the conversation that
is probably made popular by Satya Adela
who's the CEO of Microsoft where he
started talking about the architecture
you need on top of your regular models
for any domain specific AI to work. So
there is a broad classification, right?
like whenever you look at a generation
tasks, you don't have an output or an
outcome in mind. Uh you don't want
you're not specifying to AI exactly how
an image should look like, how a blog
should look like or how a website should
look like. So that's where the euphoria
sets in. But when you think of a flip
side of a task where you have a single
correct answer that you want AI to get
to that is when the disappointment
starts to set in which in most cases
most people dub it as a last mile but
that is the single longest mile that you
have to run with AI that is why you you
need these architectures for you to
focus on a specific problem. Now beyond
all this uh operating production systems
is also a multiplayer and a multi system
problem. You're not just doing it on
your own. You need to pull inmemes for
for different teams over time. All of us
have specialized in different categories
of engineering. We are put in different
teams. Uh we need to talk to to solve to
resolve any issues across AI. So sorry
across your production systems.
All in all uh our company resolve AI
started with a single thesis. So we
genuinely believe that all of this uh
all of this work that you do on
production systems like fixing issues or
like uh running your software on a
day-to-day basis should be done by
agents in most part. That's one of the
reasons why I was asking can you
confidently tell 90% of your work or
more is being done by agents and
engineers should just be running those
agents where agents take care of like
fixing and running your software. So
that's why we've built uh resolve AI as
three categories of agents. There are on
call agents to fix your software issues
that come in on a daily basis. And there
are incidents agents that will help you
drive incident channels and get you get
you from a complex incident to a root
cause and fix. And lastly, there are
ambient background agents that will help
you with your production tasks. Be it
things like deployment monitoring or any
of the analysis that you have to run or
any of the conditions that you trigger
where you want a specific investigation
to happen. underneath all this is the
same resolve agent architecture that is
what we'll be talking about today uh and
what it takes to get there to build it.
So let's start with a question. So why
is this even required right like why
can't we just point the biggest model at
production data models are of course
getting better the reasoning capacity is
getting better uh to fix your software
issues it it genuinely demos well
whenever you focus on a particular use
case and you build your harness on top
of it shows up with a very good demo but
slowly as you start to scale across use
cases and teams that is where uh some
that is where very familiar cracks start
to appear in the system so what are the
kind of cracks that we have seen as you
start to scale in the product along the
way, right? First thing you'll notice
that of course models will have
anchoring bias. This is a very strong
thing that you have to deal in your
harnesses itself. They they're designed
to give you like a coherent answer. Um
and first of as and when new models
start to come out with better reasoning
capabilities, you also need to maintain
the treadmill. uh you also need to
continuously change uh which evaluate
firstly evaluate which model is suitable
for the task and also update uh the
right model for your use case and second
and a little bit of an overlooked item.
So we always associate a model to a
workflow or an outcome but every
workflow has hundreds of different types
of tasks. So there are reasoning tasks,
there are deterministic tasks that you
go through, there are things like image
gener image reasoning or you're
reasoning across images, you're
reasoning across SQL or things like
logs. Now all the models frontier models
that you see around each of them is good
at a specific part or a specific uh kind
of task. So the orchestration engine
that you need to imagine for uh moving
across these models for a workflow first
of all needs to keep pace with how
models are evolving and second it needs
to be able to marry the best model for
the best task
and second failure mode uh is of course
the context windows. I know the context
windows are expanding but context
windows context windows are not just the
problem uh for for solving for for
solving a complex problem like this. The
second part is if you provide large
enough context, models start to
overexplore. It'll start to come up with
hypothesis that don't even exist or
sometimes might not even get you to the
right answer. Now, if you supply very
limited context, of course, they
underexplore. They won't be able to get
to they won't actually have visibility
into what other pathways exist or
probably what other potential hypothesis
can exist in solving a problem.
Especially for production incidents,
this becomes a huge issue because
telemetry is literally infinite. You can
start to create as many log lines as you
want, as many metrics as you want. And
now when you start to marry that with
your code and infrastructure, that is
when real real cracks in system uh
starts to appear.
Third and my and my most favorite one is
uh defining causal reasoning. So models
are there to please you. I mean, we've
all come across these use cases where
you push the model hard enough, uh,
it'll start to agree with you in every
different direction. So, models are
specifically designed to give you
coherent answers, but not causality. But
production incidents, the only thing
you're looking for is a causal chain of
evidence like a detective. What are the
steps that took place that led to a
particular incident so that you can
actually fix uh the right issue instead
of creating a patch. So especially when
you're solving a hard problem like
production reasoning you need causal
reasoning built into the mod built into
the system not just coherent answers.
And the next one is of course
guardrails. I won't harp on this topic
too much but all of us have read uh some
news or the other where let's say AI is
going and deleting a particular file
system or like a database. Uh so AI it's
also this is a feature right not a bug.
uh AI might have determined that the
cleanest possible fix is just deletion
of that particular code snippet. You
can't fault it for it. You just have to
build guard rails uh around the system
so that it works in the right fashion.
What is the least privilege access that
AI can operate with in any given
scenario? And lastly, learning loops.
Any system that you build should be
scalable across your team or your
organization in the best case. Every
time you're using AI for production
incidents, like I said at the starting,
it is a multiplayer problem. You have
multiple different teams like SR,
platform teams, uh backend engineers or
service engineers, all of these people
should be involved and most importantly
all of these people should have the same
context. Now when you add temporal
discussions on top of it like uh your AI
system should have the same context of a
previous investigation in the 100th
investigation or else you're starting
the wheel from the same time again. So
these are the failure modes where we've
seen the cracks appear. So that's why
we've actually built an agent
architecture that answers these same
questions exactly. So there are six
major parts uh for any AI architecture
that has to work in a specific domain.
The reason I'm mentioning it as a
specific domain is models are there for
general purpose reasoning. Now when you
want to harness these models into a
specific answer, you need to take care
of six different pillars. The first one
is model orchestration. Like I
mentioned, uh model orchestration is two
layers. one, how do you keep up with the
model treadmill with the latest models?
And second, how do you match the best
model for the task? Is it Gemini for im
uh image specific reasoning or is it
OpenAI for deterministic steps or is it
claude for open-ended investigations?
You need to constantly keep evaluating
what is the best uh possible model for
the task at that point in time. So this
is an engine that we've built uh up
front very early. Second is context
engineering. Now context engineering is
often minimized to like uh the database
or an execution solution. Oh, are you
using a graph rag? Are you using a
knowledge graph? Are you using x y and
z? Those are all implementation details.
But what matters as a goal is what is
the precise amount of context AI needs
to solve that specific problem. And more
often than most often than not, it's a
combination of techniques. you might
have to use a graph rag kind of a
solution for AI to start investigations
and when you actually further go into
the next steps you need to determine you
need to define very precise tool calls
so that you don't burn through tokens
very quickly when you're making multiple
tool calls in in form of log queries in
form in form of metrics or dashboards or
code queries etc.
The third one is causal reasoning like I
mentioned. So this is one of the first
uh principles that we've built into our
system at resolve AI where uh the
evident the root cause is always based
on a causal chain of evidence. What are
the exact or precise steps that happened
that led to this particular issue? If
you're not able to establish that chain
of evidence, we have to give out that
information with a low confidence level
and point the user in a different
direction. This is true for any domain
specific AI and this is true for resolve
AI as well where we are pointing you in
a different direction if we don't see
the if we don't see the data beyond a
particular point.
The next one like I said is governed
actions. This is quite straightforward.
Uh it depends upon every team, every
different organization uh depending on
uh depending on the access levels or
probably the restrictions that you have
or the industry you operate in. What are
the specific guardrails that you need to
define for AI to operate under? Is it
read? Is it right and under right? What
are the specific conditions for right?
Uh etc., etc.
And lastly, a learning system. So, think
of it like this. Every interaction that
uh you're doing with an AI system is an
opportunity for learning. So, uh AI
system has to learn not just from an
investigation it is going through, but
from a how from how a user is actually
interacting with it. Like am I giving
you positive reinforcement? So is this
turning into a positive eval? Am I
giving you some negative reinforcement?
Am I am I guiding you or steering the
investigation in a specific direction?
Those are different kinds of evals. So
that leads into the last piece which
where eval is also a very critical step.
So this is the starting point and ending
point for any agent architecture. So the
way we think about evals is in five
different levels like I mentioned. What
is the positive reinforcement you can
give? What is the negative reinforcement
you can give? And can we trace your
path? How did you come up with this
solution? Can we score you like an
engineer based on that? How would the
how would a best engineer perform this
investigation? And how do you compare
against it? And on top of it, how are
you calibrating yourself as as AI? How
are you giving out that confidence
level? So all these are systematic eval
infra evals that you build into one
platform that you constantly have to
push the architecture against whenever
there's a new model, whenever there's a
new use case or whenever there's an
architecture change.
Cool. There's enough talking. So let me
actually show you this in action on how
it works in resolve. Like I mentioned
our platform uh is specifically there.
So there are two categories of agents
that we work with. One is an on call
agent, one is an incident agent and of
course the background agent. So uh since
like I've since most of you are
engineers over here, you might be
familiar with the system. Of course most
of your telemetry or observability uh
alerts are firing into a collaboration
tool like Slack or Microsoft Teams or
whatever you might be using. In this
case, what we are seeing is Graphfana
fire firing alerts into our common Slack
channel. Um so Resolve automatically
picks up those alerts and kickstarts an
investigation. What you see here is uh
it is throwing an error about a log
skill and it starts to provide what is
the what are the uh what is the root
cause that it found for the uh alert
that came in and also the other
contributing factors or other theories
it rejected. It gave a quick root cause
and evidence and recommendations. But
let's actually deep dive. So in most
cases like I said this should be a
multiplayer experience. So let's
actually go into the UI and see what's
happening here behind the scenes. So uh
it the work starts off from resolve AI
when it treats the alert that's coming
in as a prompt in itself. So it takes
the prompt and it spins up a bunch of
different agents actually two different
categories of agents uh to get the work
done. So first category of agents are
basically investigators. So they are uh
trained to actually uh go through the
investigation just like how an engineer
would firstly find out what is the issue
gather more information from metrics and
traces etc and figure out where the
issue is happening from traces logs and
now start to correlate that with things
like change events uh or any of the new
deployments that would have gone in and
your code and your infrastructure. So
primarily it's doing this translation or
reasoning across four types of data
sources. your code, your infrastructure,
your knowledge bases and your
observability platforms. Based on all
that it starts to give out this uh root
cause or this root cause what we've seen
there are so one of the log skill is
actually experiencing high high failure
rate. It trace the issue all the way
down to some stale integrations that are
still live in the system. The
interesting part is it's also showing
out some other ruled out theories where
generally we would start an
investigation at the same time there was
a GCP outage. So you would actually uh
this this would be a perfect correlation
as well right going back to AI that is
designed to give you coherent answers.
So a GCP outage happened at the same
time. So of course this might be the
issue uh that we are seeing or there are
other traffic spikes that it is
experiencing
uh without missing integration. So uh
that would be the other thread that you
would start to pull on. So let's say if
I'm a new engineer, if I'm starting in
okay resolve gave uh this as a root
cause of course it's we have also
designed to go operate with the least
trust policy. So let's say if I I can
start to highlight and it'll start to
it'll pull me in so that I can
interrogate this further. uh in this
case let's say uh let's ask resolve uh
is this related to uh GCP outage
so
it's giving out the answer here but
there is other other precise questions
that I ran I want to share with you so
there was other deployment errors that
happened at the same time so that is
what I was pushing resolve on going back
to what I mentioned if you push uh an AI
hard enough it'll start to agree with
you we've designed the system to go
against it. It'll only base its answers
based on the causal causal chain of
evidence that it created. Since it is
able to establish that, it's able to
give out a very coherent answer. So,
this uh also lets me actually pull in my
teammates so that this truly becomes
like a multiplayer experience. Let's say
if I give uh I can pull in,
can you take a look at this? This can
pull in my teammate directly from Slack
so that we can collaborate on this
virtual war room experience.
This was a quick demo like I said uh the
currently and what I talked about today
is just one uh axis of the architecture
right like now there is the other axis
of the architecture where you just need
to productize an AI like if you want to
put this in uh in front of any user or a
customer you need to make sure it runs
on a robust platform those are the other
aspects that you have to think through
but this is something that we are always
familiar with so that's been my time.
And uh if you're interested to learn
more about uh about Resolve AI and which
customers are currently using us and how
are they using it, uh please check us
out at the booth L28, I believe. Uh and
by the way, before you leave, take out
those cool bags uh that are right
outside. Thank you so much.
>> [music]
