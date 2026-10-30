# Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI

Source: https://www.youtube.com/watch?v=v5tm5EAzsAs

Uploaded: 2026-10-24

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Hello everyone. My name is Sophia
Yakoubovitch. I'm a forward deployed
engineer at Arize, and for those who
aren't familiar, Arize is an
observability backend that is designed
to make AI work. Now, what does that
mean?
Building AI systems can be inherently
intuitive in some sense, especially when
a lot of that low-level abstraction is a
low-level programming is abstracted into
the mind of an agent. Unfortunately
though, that mind can be a bit of a
black box.
When that black box is difficult to
understand, it's difficult to predict,
and therefore difficult to debug. And
that's where observability becomes
essential. Observability helps you
understand what your systems are
actually doing. It's essentially shining
a light in the black box. And once you
understand what the system is doing
step-by-step, you can then evaluate it.
Run evaluation metrics to track its
performance, and then use that data to
iterate and improve your agents over
time.
But I want to take this one step
further, because the biggest challenge
isn't determining what broke,
the biggest challenge is that when you
do submit a fix, you want to make sure
that you don't break 10 other things
along the way. Now, raise your hand if
you've had that exact issue before. You
push
Yep, seeing a lot of hands. You push a
simple change, you know, should be a
should be
easy, no issues, and next thing you
know, everything's on fire.
So, today we're going to discuss how you
can use your observability as a way to
build a robust regression process. Not
only something that your engineers can
do, but an automatic process that feeds
into your CI/CD.
We're going to break this down to three
parts. First, we'll discuss why agent
regression is so different and difficult
to detect. And the first thing we're
going to touch on is that agents don't
fail at the code level, they fail at
runtime. We're then going to use this
premise to build out our regression
loop. It's going to be a five-step
process. We'll touch on it at a
high-level overview, and then we'll move
on to the Arize platform and show you
exactly how you can do it today.
Then, we'll close off the session by
closing that regression loop at agentic
speed and touching on where we're seeing
the next frontier of agent observability
move to. And if you stick with me till
the end, I'll introduce a paradigm shift
that I hope you'll all find interesting.
So, let's get started. First, with a
concrete example.
So, imagine with me that you have a
support agent, and you have a security
engineer that has approached you. And
that security engineer has reviewed the
policy of your support agent and
determined that he wants to add one
line, a simple one line to your agent
that will ask your agent to confirm
before it takes any action.
Sounds simple. Sounds harmless. Your
security engineer says he has the
intuition, and oftentimes we're quick to
make this change. I'm not even going to
ask if you've done this before cuz I
know everyone has pushed a one-line
prompt change and just assumed
everything will go well. And the reason
we make that assumption is because we
think that because it's written in
natural language, that we have this
intuition on how these agents are
performing.
We're really coding on vibes, and we
don't want to be. We want to be able to
code with a numeric evaluation suite
backed data. We want to have scores that
prove that these changes are actually
making a positive impact and not just
crossing our fingers. But let's say in
the scenario you did push that one-line
change, and now you are running your
evaluations on your production data a
week after it's been submitted.
And the first thing you notice is that
you actually have a 17-point improvement
on a action safety. So, your security
engineer was correct. It asking the
agent to confirm before taking any
action does improve its overall safety.
But your observability engineers are
continuing to evaluate, and they also
check for task completion and they
notice a 17-point
degradation.
Now, this is occurring because if you
have an agent that's confirming before
every single action it's taking, now
tasks are being uncompleted. If a user
leaves the session, that session is
never completed to the end and I have
incomplete task and you see this
unlikely result.
You may not have caught this initially
when you were thinking about the
project, but your evaluation suite has
caught this. And ironically enough, the
overall average of both is net zero. And
what I want you to take away from here
is just because you improve the
dimension of one agent does not mean
that you're improving the agent as a
whole.
The question I have for you is, would
you have shipped this change?
Many of us would have before the
evaluation test. And this is why it's so
important that we get these numeric
results so that we're not shipping on
vibes, we're shipping with backed data.
So, to understand where the mistake that
we made is is we made an unrealistic
assumption. And that assumption is that
the error is going to occur at the code,
but the error rarely occurs at the code
level. Instead, these agents are failing
at runtime.
What the code reviewer saw is here on
the left-hand side. It was a one-line
change in the system prompt markdown
file.
Easy change, simple to understand,
simple to approve. But in reality, this
code change was local, but the
behavioral changes of this code change
was in production. It was in the
runtime. This one simple line has
shifted how the agent operates. It's
adding additional steps. It's changing
how the agent works with other
sub-agents. It's changing how the agent
calls tools. All of these different
trajectories, which could be thousands
of possible trajectories, are not in
your static code. They're only in your
observability back end. They're only in
your traces. And so, what we are saying
here is that the diff tells you what
changed, but the trace tells you what
actually happened. And there's a shift
here, that traces are becoming the new
source of truth. These structured logs
of what your agents are actually doing
actually is what truly represents what
these systems are doing. In traditional
software, logic was written down. It was
very clear to determine what that
runtime was before you ever pushed
production. But now the logic only
exists at runtime. The observability
becomes essential when we're looking at
regression testing. This gap between
what was written and what actually
happens is filled with silent errors. So
to capture that, we need to start our
regression testing by looking at our
traces.
So let's build out this regression loop
together.
It's a five-step process. We're going to
start with our production traces. We're
going to build evals, run experiments,
and then close it all up to be an
automatic gate at CI.
First, I'm going to do a five-step
high-level overview. And then we're
going to go into the actual product and
show you how you can do it yourself.
So step one is we're going to select a
data set. Seems simple enough. We want
to pull real production traces. We don't
need to synthesize data. If we already
have real user queries, real inputs,
real tool calls, we're pulling from that
directly. It's important that our data
set is a representative work is
representative of the average workflow
that our users are going to be pushing
into our systems. But it's also
important that we capture known
failures. We filter out com
moments where often errors, often fails
at eval metrics. Capture those into your
data data sets. You also want to capture
edge cases. Maybe not as common, but
just as important. And one thing that we
often see users forget is capturing
successful workflows that we want to
protect. Because again, we're not just
trying to make sure that the fix is
going to work, but we also want to test
that we're not going to break something
that was already working. So it's
important that we capture all four of
these in our data set. Once we have this
production data set, we can then build
out the rest of our regression testing
suite.
The second step is we want to have a
scoring mechanism. And this is where we
bring in evaluators. Now, show of hands,
how many here are familiar with the
concept of evaluating agents?
I'm so happy to see so many hands. This
is a core foundational part of agentic
engineering.
Evaluators allow us to take metrics and
dimensions that are important to your
engineers, your product team, and
actually quantify them. What do I mean
by that? Let's take some metrics that
are important for your agents, things
like hallucination, accuracy, tool
trajectory, step efficiency. All of
these metrics are subjective in nature.
And you may have a human that reviews
them and can potentially determine
whether or not something was
hallucinated, whether or not the most
efficient pathway was taken. But we want
to be able to automate this process. We
want to turn a subjective metric into a
numeric score. And we do this by
leveraging LLMs. We use a concept of LM
as a judge, where we judge a span, a
trace, some log data against an LM. The
LM has a particular guide of how it
determines whether or not something was
hallucinated or factual, something was
efficient or not efficient. And now
we've done essentially a binary
classification. In this example at the
top right corner, you could see a task
completion eval, where the LM as a judge
is
has a task of determining whether or not
something was complete or incomplete.
Now we've taken a subjective metric and
we've essentially turned it into a
binary score, 0 1. You can translate the
score across 0 to 5. You can have
multiple different labels. But you've
now turned a quantitative measurement
into a qualitative score that you can
measure against. You're not limited to
LM as a judge, you can also use
code-based evals or ML-based evals as
well, determine based on what that
metric is. A code evaluator is great for
your deterministic checks, but an LM as
a judge is good for your
non-deterministic checks. So, once we
have a list of all of our metrics that
are important to us, we build evals for
each of them. Now, we have a testing
suite that we can go against.
Step three is we're going to run our
baseline experiment. And what this
experiment is is we're going to take our
agent and run it against all of our
production traces, um all of our
production data sets.
We're after we get the output of those
production data production data sets,
we're then going to run our eval testing
suite on top of that. And that's what's
going to be our baseline. Now, you can
do this in the SDK, it's just run
experiment. You'll pass in that data
set, pass in that task, pass in your
evaluation suite, and you'll get those
results. We're going to touch on how you
can do this in the UI, as well as how
you can do this with your coding agents.
But, once you have that baseline
experiment, you're then going to add
your one change. Change that policy,
rerun the evaluation, what are the eval
results? A simple process. Now that you
can quickly iterate on, and not just
with one policy change, but test
multiple changes within your prompts.
Test multiple models. If your team comes
with you comes to you and says, "We want
to switch the new fable model, it's five
times more expensive." You're not going
to switch without proving that you're
going to get a good ROI. This is how you
can prove that with a numeric set of
measurements to determine whether or not
it actually is improving your investment
to switch to a more expensive model.
And you can adjust this policy, rerun,
and compare. Rerun and compare how
changing the prompt, changing handoffs,
changing tools, changing models is all
going to affect your overall output. All
without having to deploy to production.
And then we can automate this. We push
this experiment into CI to complete this
automation. Now, each time that you have
a pull request, let's say you set this
up in GitHub actions, for example, each
pull request each PR is run through an
experiment workflow against the
evaluations that your team has deemed
important. And you don't merge until it
meets all of the regression criteria
that you have listed. Now, you're no
longer pushing on vibes, you're pushing
with confidence that you actually do
have a positive impact on your
performance. And if it is negative, you
go back, you test, and you reiterate.
So, let's actually show how to do this
in the platform.
Let me switch over. Um here we have Here
we have the Arize platform, and I'm
showcasing this exact refund agent. You
can see in our baseline experiment what
our scores were, and then you can see
that plus 17 points on action safety and
minus 17 points on task completion. Each
one of these points Each one of these
line items here is a different test that
I ran with different prompt changes,
potentially different model changes, and
I'm evaluating each one of them to see
which one has the best trade-off to get
to where my end goal is. And I can see
that overall I'm going to have a plus 18
18 points on action safety and plus six
on task completion. Now, how can we
build these individual points? Well,
there's a couple ways. We'll do this
first in the UI. I'm going to jump into
the playground here.
I'm going to create a new playground.
We're going to start with the prompt
playground to test a single agent. Let's
call this AIE NYC.
Perfect. Once I'm in the prompt
playground, here is where I can test a
single agent. An agent A single agent
all is essentially just a single prompt
with a set of tools attached to it, a
model LLM configurations, and so we're
going to replicate that here. Now, I've
already stored my prompt in my prompt
hub, so I can pull it right here. I've
got version one, and then I can pull up
my data set. I've already selected a
data set that I can use here
and that I've gone through and pulled
out those edge cases, those known
failures, and those successful workflows
that I want to protect, all listed in
this 100-row data set.
I can test this right now, or I can test
multiple prompts at the same time. So,
I'm actually going to duplicate this,
and I can change a line item directly in
here, or I can load up a separate
version right here and test side by
side. So, I can see just how quick just
how both of these prompts are affected.
Now, of course, we have to add our
scoring mechanism. So, that's going to
be our evals. I'm going to click here.
I'm going to add in my task completion,
and then I'm also going to add in my
action safety. And you can see here that
there's a ton of other pre-built halluc
pre-built evaluators you can select
from, hallucination, user frustration.
And we've got some code templates,
security checks, etc. And you always
have the ability to customize your own.
Once I run this, it's going to run on
every single record, and then it's going
to pull out those eval scores. And then
when I go into my
data sets here,
go into my
experiment run flow, it'll pop up
under here as well. And I can pull up
all those metrics that are important for
me. I can look at latency, I can look at
my evals, I can look at my total cost
and error rates, and track that over
time. So, I can look this for PR
changes, for playground runs. And
there's one more other option that I
want to show here, too. And that's if I
go into playground, click here, and I do
agent playground.
Call this AIE. Oh.
There we go.
Agent playground allows you to not only
evaluate at a single agent, but at
multiple agent levels. If you give us
access to connect to your agent
remotely, for example, through a HTTP
call. If I go into remote agents here,
you can connect your remote agent
directly here, so that you can change
how different sub sub agents communicate
with each other, all directly in your
code base, and then we can call that.
So, each record in your data set will
call against your agent, will test, will
get the output, will run those evals,
and then score it in the same mechanism.
So, you have two ways of running play
running these experiments within the UI.
You can run them in the prompt
playground testing a single agent or run
them in the agent playground and test a
very complicated multi-agentic system.
Now, this is in the UI, but of course
you can do this programmatically with
the SDK, rest, or CI or CLI, but my
favorite method to do this is actually
with coding agents. How familiar is this
group with the concept of agent skills?
Ah, I love to see when people are saying
advanced.
Agent skills allows you to connect your
coding agents with external databases
and advanced contexts. Arize has a
public repository of skills that allows
you to connect to every feature
available in the Arize UI. This means
that you can close the loop between what
your coding agents are producing in your
IDE, the code that they're producing,
with what is actually happening in your
observability back end. So, let's
actually touch more on that closing the
loop.
So, how we're going to close this loop
at agent speed. We've got the same loop,
but instead of running it by people, we
want to run it by agents. Now, I'm going
to highlight two key takeaways. We only
have 2 minutes left here. And the first
key takeaway I want to touch on is what
the engineers are doing. Today,
engineers are the ones that are closing
the loop. And to summarize what that
loop is, is we have observability first.
That is as your systems are running, we
are taking that log data, that tracing
data, and we are tracking it for every
run in production. We then take that,
evaluate it, get those scores, then we
can implement a change at that could be
a prompt change, model tool scale policy
change. And then we test that change. We
iterate on it with the experiments
workflow.
Finally, we improve it. If it passes,
great, ship it. But if it fails,
we close the loop. We take those failed
cases and we bring it back to the
observability layer. These new
production traces that failed then
become new cases in our regression
testing suite. And that's the first
takeaway here, is that every failure
should become a test. Every failure
should make your agents stronger
and harder to break.
Once you have these regression tests
that are regression test suites that are
constantly building on themselves, you
have a more robust method of
continuously iterating and improving.
That's takeaway number one. Now,
takeaway number two, going back to that
loop, I have a question for the group
and that is, what if an agent could do
the investigation and propose a fix?
Because right now, the manual
investigation is that that's the
bottleneck. Humans are the bottleneck
here.
So, what we're seeing is a shift from
observability to self-improvement. The
manual bottleneck here is that humans
are still reviewing dashboards. They're
still triaging and shipping those fixes
and reviewing those PRs and that is the
ultimate bottleneck. So, we want to not
only close this loop, but we want to
close it at agentic speeds.
We don't want to just give humans the
ability to debug agents. We want to give
agents the ability to debug and
understand themselves. And that's the
shift that we're seeing in
observability. Is observability is no
longer about humans understanding
agents, it's about agents understanding
themselves. Agents having the tools to
improve themselves. Agents having the
tools to be accountable. Remember what
we talked about in the very beginning.
That is that traces is where the real
runtime is. That's where the real logic
is stored. If your coding agents are
pushing PRs and I know they are, they're
pushing PRs without actually knowing
what's happening in production. That
means they're pushing PRs blind. They're
reliant on the static code. They don't
know what's actually happening in
production. By closing that loop, by
connecting your coding harnesses, your
coding agents with what is actually
happening happening in your production
database, you are giving your agents the
full understanding of what these changes
are actually making. And that is the
second and final takeaway. That is that
the best agents don't just learn from
failures. The best agents fix
themselves. And that's the future of
observability that we're seeing is that
agents can not only see, but they can
evaluate and improve themselves on their
own.
Thank you.
