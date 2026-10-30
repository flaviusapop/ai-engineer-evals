# What Does an AI Engineer Do Now? - Aparna Dhinakaran, Arize AI

Source: https://www.youtube.com/watch?v=ImnZ7s68jw8

Uploaded: 2026-10-25

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Awesome. Well, welcome to AI engineer.
Um
uh
thought given where at AI engineers New
York, we'd kind of revisit the question
of what does an AI engineer do? Feel
like every year we have an idea of what
an AI engineer does and
that definition kind of changes. Um
And as I was putting this talk together,
it was super timely because Karpathy
actually just tweeted something this
weekend where he kind of he kind of
talks about this growing gap between
basically folks at the frontier who are
running thousands of agents and swarms
of always-on agents and he really kind
of drops this funnel where 6 billion
plus users have maybe touched or
interfaced with an LLM. 1 to 2 billion
or maybe like casual free tier users. 20
million are professionals who have maybe
started using it for more taking some
piece of work that would have taken
weeks down to to days. But really those
at the frontier labs are which is a
super small percentage. It's like 5,000
users. Uh are the ones who are running
thousands and thousands of agents at
once.
And
as I look at this, it really is I mean
he's kind of dropped a bit of the
funnel. I mean the first question anyone
looks at this is that where am I on
this? And you know, he's kind of drawn
out a bit of a road map of how does
everyone get to in the next couple of
years one of those 5,000 users who are
running thousands of agents.
And this has been happening I'd say for
for a couple of decades now where the
abstraction layer has gotten higher and
higher. I mean
definitely faster in the last couple of
years, but we've gone from engineers
writing higher level abstraction
languages to I mean just copy-pasting
code,
using local agents to using cloud agents
to really the expectation now is how how
do all of us start running a team of
agents or factories of agents internally
and build toward that.
>> [snorts]
>> And what this has led to is essentially
what is a then and now of what an AI
engineer is. And this is
is this is a bit uh
I I think of a of a roadmap for some,
but I think internally this is what
we've already started to kind of push
towards. As an AI engineer, your job's
no longer to just write the feature,
write an AI feature, it's about how do
you build the loop to write that
feature. It's no longer about you know,
just reading the diff and actually doing
code review, it's actually how do you
set up systems and agents to do the code
reviews, and how do you write evals to
actually do the non-deterministic
um to review those non-deterministic
tasks.
It's actually no longer even about just
setting up metrics and and software kind
of telemetry, but it's actually how do
you have agents go through and read the
observability data and have agents
actually consume that telemetry to find
patterns.
And so, [snorts]
this loop that we've kind of been
talking about, which is the build, the
eval, ship, you monitor, you improve it,
well, the AI engineer is now actually
responsible not just for doing each of
those steps, but how do you build the
loop that does the that that actually
does each of those steps.
And at Arize, one of the things we've
rolled out in our product, and I'm going
to talk about a bit of what we've
learned in building this, is we built
signal to actually run this loop for AI
engineers. What signal does is that
signal actually looks at all of the
traces, it reads the telemetry, it
identifies patterns in that telemetry,
and it can actually put up a fix or a PR
if it has access to the repo.
And signal signal's an always-on agent.
So, this is an example of how signal
starts, but it actually starts off by
just reading the traces. Super simple
example, but it goes through, reads um
and all of this configurable, but
and
certain volume of traces that came in in
some cadence. It reads it and then the
goal is to actually identify issues from
that telemetry data.
It has to keep track of issues that it's
previously seen. So, we have to consider
the memory of did see something before
that it thought was an issue?
Did something seem like an issue, but it
wasn't actually captured and now as it
collects more data, it actually thinks
it's much more of a critical critical
issue. And so, signal actually starts
off by reading the traces to identify
problems.
And so, one of the first things
that we realized was that the future of
who's actually consuming telemetry data
has really changed. It's no longer about
humans consuming telemetry data.
It's not even about humans consuming it
and agents kind of taking on the task,
but it really is how do you set up your
telemetry data so that agents are the
primary consumers of that data.
And what that does is that that
observability data can become the
trigger for actually running and
triggering these always-on agents. And
so, the first thing that if you're
building a team of of you know, a
factory of really always-on agents is
what triggers these agents to wake up or
start. And there can be a variety of
triggers. For signal, for us it's you
know, it's configurable to run on an
ongoing cadence. So, every 3 hours, 6
hours, go pull the last, you know, X
amount of traces, read them, identify
problems. It can also be triggered by
events. So, Slack messages,
um if some user complains about
something, it can be a metric-based
trigger, but these are essentially
triggers to kick up the agent actually
starting.
Once the agent actually starts, we have
to spend some time figuring out, well,
what is what is an agent run actually
look like? For us,
we actually pull in all of the context
of the traces, um any additional
third-party data, so we allow collecting
to APM logs, APM metrics,
um
but all of the third-party telemetry
data that we want to pull in, um access
to the repo, um access to the actual um
the the access to any keys that are
needed to actually run run this agent,
but all of this information is um put
inside of a sandbox, and this is
actually what's started up every time
the agent wakes up. And so, the agent's
triggered, we build a sandbox, we put
everything that we need inside of that
sandbox, there's a proxy, the only way
to get information in and out of the
sandbox is by this single proxy, and
everything that happens inside of that
sandbox is actually already getting
traced, and every output, so the issues
that are generated and created are all
getting saved to some kind of memory.
And so, this happens every single time
the agent actually runs. Every time the
agent finishes running, so it swept
through all of the traces, um
it either found something or it didn't,
there's what actually stays and what
actually gets thrown away. What stays is
that if it found any issues, all of the
output is actually saved off in some
kind of memory, so that the next time an
agent gets spun up, it doesn't have to
start from ground zero. It has a history
of what are the issues that it actually
found. Um
the agents are traced, so all of the
telemetry data of what the agent called,
um you know, if it actually put up a PR,
all of those things are actually traced.
And any skills that it may have learned
while actually doing a run can also get
saved to the actual repo.
But, the things that go away is the
sandbox gets torn down, any credentials,
um you know, obviously get get removed,
um the repo access is removed, and so
all of the stuff that doesn't need to be
saved kind of gets torn down after the
run of signal.
And we've designed signal in a way to
actually keep this agent configure
durable. So, that means that either if
the
if the sandbox fails, or if the harness
fails, then it shouldn't have to start
everything from scratch in the middle of
the run. It should actually just be able
to pick up from the step that it failed,
and all of the state, so-called, is kind
of saved off in kind of a a memory
outside of the sandbox. And so, we've
designed this to actually be a very
durable agent, so that if it fails, it
can spin it back up. Um you can launch a
new sandbox, launch a new harness to
kind of pick back up where it started.
So, all of this is essentially the
underpinnings of how we built signal to
run every single run. Agent gets
triggered, agent gets started, loaded
with all the contexts, the evidence, uh
it sweeps through the telemetry data, it
either finds something or it doesn't,
all of that gets saved to memory. If
something fails in the middle, the agent
can get reset up.
And we built signal to also be you know,
agnostic of the model or the harness.
So, today signal supports not just Cloud
Code, which is what we started with, but
it also supports Cursor and Codex. And
the goal is to actually support all of
the the major, even the open source
harnesses out there.
Um and signal actually also supports um
multiple uh
it will support kind of multiple models.
So, even if you're using Claude code, uh
you can pick any of the models inside
the Anthropic family. Um and this is
really important to us because one, it's
an awesome way for us to evaluate the
quality of the agent um every time we
spin it up. It helps us control costs,
so we can see, you know, as we use more
powerful models,
the better quality maybe the PRs are,
but can we reduce the quality of the the
you know, can we reduce the cost and
actually still maintain the rigor um and
maintain the quality of issues that are
actually detected by Signal. So, this is
something we deeply thought about from
from first principles when we were
designing Signal.
And this is actually a pretty good segue
into what does an AI engineer need to
do? Well, an AI engineer really needs to
kind of learn how to write evals. And
so, we actually every time Signal runs,
Signal finds an issue, it puts up a PR.
Well, there's evals that are run on top
of the agent to test that PR. Um and an
eval can be as simple as um you know,
testing something as part of your
development workflow. You have a
dataset, you can be a simple prompt um
it with with outputs that you're testing
to make sure that there's no
regressions.
Um but these evals can also
they need to be kind of aligned with
human judgment. And I'd argue that this
is actually probably where an AI
engineer should be spending a lot of
their time as they're building the
system to actually run the loop. They
should be actually spending time looking
at the traces with their agents,
identifying what the common errors are.
Um and there's a lot of skills I think I
was hearing Lance yesterday talk about
the Claude skill to build evals. We have
a skill with the arise um evaluator to
actually help you build and write evals
as well as align those evals with the
human judgment. But, this is probably
where the shift to defining what is good
becomes really, really important for an
AI engineer to actually do. And for a
lot of teams I I think we speak with and
we work with, their question becomes,
"Well, how do I trust the evaluator?"
And do I do I really trust that the eval
is
um
you know,
is going to capture
you know, how how do I trust that it's
as good as my judgment? And I'd say what
we spend a lot of our own time doing for
our own products is that we actually
evaluate the evaluators.
Um we spend a decent amount of time on
actually building
these data sets, golden truth data sets.
We run e-vals, verify them against the
human output, and then try to align to
make sure that the judge actually agrees
with the human um
and and they're in agreement before we
actually ship out uh a new evaluator.
And these e-vals can then be used both
in an offline testing as well as in an
online testing manner. Um and this this
is probably what I would say as an AI
engineer is more and more of what the
job is becoming.
Um and so, what I'm going to leave you
guys with is as an AI engineer, you've
built this agent, you've built this
agent to actually run, be always on, you
run e-vals before you actually ship it
into production.
You can ship it, and then once it goes
into production, the goal is to actually
trace everything.
And tracing everything now means not
just tracing the agents, but also
tracing the coding agents behind the
agents that built this. So, you can
trace um
cloud code, you can trace cursor, you
can trace codex, but all these coding
agents can be traced so you can
understand what happened um in the
factory of agents that you all are
building.
And then these agents that all the
traces can then also be evaluated
online. So, there's an offline
evaluation when you're actually testing
what you're what a new change is, but as
it goes into production, these become
your online evals that you're running on
top of the telemetry data. This for us
ends up becoming the new data that then
gets pulled back into the agents to read
the telemetry data, the evals, and
surface up kind of problems inside of
the traces. So, the the system really
becomes how do you go from
collect data, eval that data, run agents
on top of it so that you can find
problems and figure out where the gaps
are to actually improve improve your
systems.
So, if I go back to kind of the question
that we started this whole thing with,
it's
what does an AI engineer do?
I mean, the gap between I think there's
a pretty big gap between what's
happening in the labs today and what's
happening with a lot of businesses. And
some of it could just be the data inside
of businesses are a lot more messy than
what is very constrained and testable
inside of a lab. But, AI engineers are
kind of the the role to close that gap,
and I would think it really starts with
tracing everything, tracing the agents
you're actually building, running evals,
so being able to learn how to test these
test these products that we're really
building, and then how do you build a
system so that agents can actually
improve from the telemetry that's
actually being collected
so that you're no longer just building
individual features, but you're actually
building the system to improve
to improve your products.
If you want to learn more, come check
out we have a booth. You can check out
Signal, learn more, but thank you so
much for listening to us.
>> [applause]
[music]
>> Hey.
