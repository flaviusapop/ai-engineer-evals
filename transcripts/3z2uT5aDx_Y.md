# Build Evals That Actually Matter - Nick Ung & Akshay Sharma, Lyft

Source: https://www.youtube.com/watch?v=3z2uT5aDx_Y

Upload date (publisher UTC): 2026-07-19

Transcript source: YouTube captions retrieved through web extraction. Segment timestamps retained when provided; transcription errors may remain.

## Transcript

Hi everyone.
My name's Nick and I'm here with Akshay
to give a talk about eval.
We are from we're from Lyft and we've
been building Lyft customer support AI
agent for a year two now and gave a lot
of a lot of thoughts about how to build
eval that actually matters and scale
our AI agent multi-agent AI agent
system.
Just a little bit of quick
introductions. My name is Nick.
I'm a data science manager. I've been at
Lyft for 6 years, a long time Lyster.
Uh
really excited to talk to you a little
bit more about eval.
And I'll pass to Akshay.
>> Hi everyone.
I'm Akshay. I'm in Nick's team and we've
been working together
uh on
customer support agents for Lyft, uh
improving the hardness, improving the
evals, things like that.
And I've been at Lyft for almost 4 years
now. I'm very excited to be here and
talk about uh building evals that
actually matter.
>> Super excited to be here and super
honored to be to be on the online track
for AI engineer warfare.
Uh
yeah, then let's dive in.
Uh for the agenda of today,
uh our talk will primarily focus on
eval. Uh
we will start by sharing how we think
about the end-to-end pipeline for our
evaluations for building support
customer support AI agent system. Uh
we'll go into deep dive into each
component more deeply as we go. We'll
start by talking about offline
evaluations, online evaluations,
eval hardness, as well as what we are
planning to build going forward.
All right, let's dive in.
I want to quickly explain the
you know, high-level system of how we
think about evaluation system for AI
agents.
So here you can see we have the
development phase and the production
phase.
So during development
if you're building agents, you should be
very familiar with
you know, managing contacts, building
web pipeline to give your agents
educational contacts,
defining your tool, building your
agentic graph as well as writing a
system prompt.
So once all of that engine agent
engineering process is done, you have an
you have an AI agents.
The way we think about this is before we
launch this AI agents to productions, we
want to go through a rigorous offline
evaluation process to make sure that
this agent
actually has sufficient performance
before we launch this to a live users.
So coming from you know, data science
and machine learning background, we've
been building model machine learning
model for for for for a while and I
think the way that we think about agent
development is very similar to building
machine learning models as well. If we
are running
offline evaluations for our machine
learning model before that goes to
productions, I think we should do the
same for AI agents as well any other
agentic platform agentic applications.
But what I think you know, offline
evaluation how that how that is
different than
traditional machine learning model is
that you know, we typically we're
building specifically for customer
support AI use case, we're building an
agent that's multi-turn.
So for offline evaluation, there will be
a component of simulated conversations.
So you want you typically want to have a
data set synthetic data set that's
representative of your production
traffic
have our user and that plays plays out
the complete multi-turn simulated
conversation
as far as having a grader such as a LNN
as a judge
to be able to evaluate how good that
interaction was.
And then we have a launch gate, right?
We want to make sure that we have
certain criteria on our offline eval and
we're meeting that criteria before we
decide to launch this AI agent to
productions.
And so the the real imperative here
really is that it we don't want to use
our live user as, you know, test data
for our AI agents. And I think in any
any cases that that is not not a good
practice. So we really want to emphasize
the importance of having an offline
evaluation process.
So once the agent hit productions, we
also have our online evaluation pipeline
as well. We have our own favorite
tracing tools to
trace all the executions and contacts
that the AI agent used to respond to a
real user in in production's
environment. We have our online graders
as well that grades how well our AI
agent is doing in productions. And as
far as having a human in the loop
pipeline to do error analysis, identify
failure mode, and feed back that
insights to the development teams to
continuously improve our AI agents.
I want to quickly go over I think three
of the most common reasons why we think
evaluation typically fail in
for for different teams.
So, the first reason is that, you know,
the the grader that we create, the
scores that we create needs to be
meaningfully gating something. Uh this
is
what we really emphasize on in the
previous slide that we need to have a
launch gate. If your LM as a judge is
just floating out there, that there's a
score, but no one is really using that
score as a meaningful gate uh for your
development and production environment,
then that LM as a judge is not not
available.
Uh we have also seen a lot of a lot of
mishaps people have when they're
creating the LM as a judge. Uh there's a
lot of different opinion out there on in
terms of how do you create uh a good LM
as a judge, and typically
uh and unfortunately also very early on
in our journey, the LM as a the LM judge
that we created are uh very noisy, too
generic. Uh it will output a score, and
but people don't really believe in uh in
what the LM judge is doing, or they
don't think the LM judge insight is
actionable.
And finally, I think when something
regresses in production, we need to have
clear mechanism to be able to to to
catch that regression, as well as
identify clear owners to be able to take
actions on uh the insights of our
graders and regression gates.
Very cool. I want to
sequence into talking about our offline
evaluation system. And uh as we
as I touched on earlier on, I think this
is the most critical piece uh going from
development cycle to to production. We
really want to have a robust offline
evaluation system to be able to get more
confidence in uh in the AI agents that
we are shipping to productions.
We took a lot of inspiration from this
paper called TauBench,
which is developed by the wonderful
people at Sierra AI,
and this is specifically for
customer support AI agent, but we also
think this is applicable for any
user-facing agentic applications.
So,
here, as you can see, this is a offline
offline simulations where you have the
AI agent as well as a user
LLM that are interacting with each
others to produce the multi-turn traces.
You have agent domain policy, which is
essentially what the you know, for each
customer support use case, there is
instructions, policy on how to handle
different different customer support
issues.
So, taking inspiration from TauBench,
this is sort of a high-level approach
that we have in creating our offline
simulator. As we mentioned earlier, we
have our LangGraph agents that we've
built.
And we have defined
an instructions for our user LLMs,
right? As you can see,
for simulation-wise, we define the user
intent. We define you know, what this
intent is supposed to to represent.
And we define the user data point or the
world state of the of our user.
For example, you know, the driver that
are coming to us might be a luxury
driver that might have been driving for
us for for a couple years, and so and so
forth.
And finally, to define the user user
behavior or user personas, as we would
typically see with our real you know,
real-life users well. We also created
these different persona for our user.
Uh, one example here is, uh, you know,
this can be a loyal long-time Lyft
customer, but they are frustrated with,
uh, with our Lyft earning systems.
So, in our offline simulator, we have
this language agent that are, you know,
interacting with our user LLM model and
generating this multi-turn trajectories.
Uh, of uh, of this multi-turn agent take
uh, agent trajectory.
And we also built our offline offline
grader or offline evaluator. Uh, LLM
judge is a big component of that. We
will dive dive a little a little a lot
more deeper into how to build a great
LLM as a judge.
Uh, and apart from, you know, LLM as a
judge, we also have more deterministic,
uh, evaluator as well. And these usually
looks like a code assertion, as you see
in traditional unit test. Uh, and for
example, here some some of the
deterministic criteria that we have
created so far uh, looks something like
this, right? If, you know, if in this in
this specific interactions, the AI agent
is supposed to grant concession, we'll
write like a rules like this whether or
not the AI agent has indeed grant
concessions. Uh, and we'll compare the
agent uh, agent two calls with the
expected outcome to make sure that uh,
we we can measure the accuracy of the
agent instruction following behavior.
So, one of the big gotcha that we face
with running our offline evaluation is
the creating synthetic data is is one of
the key challenges in making sure our
offline data set is representative of
our production
and data.
So,
uh here we, you know, uh here we have a
meme here.
Uh
What ideally what you don't want to be
doing is just to simply prompt an LM
model to generate 50 different test
query for your offline data sets.
Uh so, here's a couple suggestions where
you can approach this, you know, much
more much more realistically and uh
assemble a data set uh
that closely resemble to your production
data.
So, this is also something that we would
try to do for customer support AI agent
as well. We take uh we we we we take
some sample from our production data.
Uh so, uh
Lyft user has been reaching out to
support for a long time. We take a
sample of our real production example
and uh supplement our offline data set
with that.
And you
And the second thing that we can we do
is we mutate
uh different criterias for from our
offline um data sets to be able to cover
different golden path and edge cases.
So,
one problem with our offline evaluator
is that
as as we mentioned in the previous
slide, if you were simply
uh sampling different 50 50 test use
uh test query from
uh by using an LM model, uh
another thing an another big gotcha that
we we face in in building this offline
simulator was that we were using a
Frontier Lab LM
uh model to role-play Lyft user in our
offline evaluations.
Um and for the most part, you know, our
frontier lab model are trained to be
helpful assistant rather than a
uh live user that might not
uh that might not sound as nice as uh as
always.
So, I I think uh
for everyone that have tried customer
support before, you know, you don't
typically reach out to customer support
agent uh with a very nice verbatim.
Um, so in our first pass at running our
offline evaluation, what we noticed is
that our LM user sounds almost too nice.
And as you can see on on the right here,
these verbatim are very very very very
complete. They use the LM user are very
patiently explaining the issues that
they're facing productions.
And our first attempt at our offline
evaluation gave us 90 plus pass rate or
accuracy rate, right? Uh this almost
sounds too good to be true, and I think
it indeed is the too good to be true.
So, in reality, these are the real user
verbatim that we get in productions.
Uh
as you can see here, most user, they are
they're impatient, they're already
frustrated. So, the verbatim they they
they they don't want to explain their
issues like a l- LM user well.
Uh so, typically what we see in
production is is something like this. Uh
and in in fact, in reality, the the the
these makes, you know, AI agents uh much
more difficult to evaluate.
So,
what can we do here? How how can we
make sure our live user LM uh
simulate this real-life live user much
closely, right? Uh so,
what we
what we how we approach this is we
fine-tune a LLM model with Lyft user
verbatim. So, instead of speaking like
this, very verbose and very nicely and
patiently explaining their issues,
uh, our LLM user will
produce verbatim that resembles this
much closely.
And the benefit of this is, while, you
know, we we did see our evaluation score
goes down after we have fine-tuned a LLM
model that speaks more like a Lyft user,
and therefore making our evaluation more
difficult, uh, but in reality, this is
really what you want uh, when you're
building this user simulator, right? If
you have an eval that's too easy, that
doesn't give you any real uh, production
insights into how your AI agent is
actually going to perform. Um,
and this also give you a lot more room
to be able to tweak your AI agents to
deal with, quote-unquote, difficult
user.
And as I as I gave a little bit of sneak
peek earlier as well, we also did a lot
of work to define Lyft user personas.
Uh, this can really ground our LLM user
to adopt a specific Lyft user persona,
and therefore, uh, simulate our
real-life user much more closely. Uh, a
couple of different user persona that we
have defined here, uh, are, you know,
bypasser user who just want to escalate
to agent, regardless of and not giving
AI a chance, refund seeker, uh, AI
skeptics.
So, the
we we really also took inspiration from
this paper, uh, from Microsoft user LLM
Microsoft paper, uh, and I think they
adopt a very similar similar approach as
well. They fine-tune a
uh, user LLM model until evaluation
score goes down.
Um
but I think in reality, this is really
what's expected and and good for for
your applications.
All right, I I'll hand it off to Akshay
to talk more about LLM judge.
>> All right.
Hi everyone. So, I'm going to take from
here. I'll talk about second problem
which we usually face when we are doing
evals with LLM as a judge.
And here you can see
uh
this is how pretty much everyone is
using LLM as a judge to evaluate their
agents. The focus can be slightly
different based on the use case. Someone
can focus more on safety, someone can
focus more on cost and latency, someone
can focus more on quality, but people
are going to measure these sort of
metrics more or less.
So, uh we want to detect leaks, we want
to detect safety issues,
uh and and things like that. So, some
parts are deterministic, which can be
evaluated by code, and some are not,
which are evaluated by the LLM.
Now, the problem with this approach is
uh that these metrics are too generic
and not actionable.
So, for example, we also started with
our eval journey using pre-built metrics
from DeepEval,
which was uh
which were measuring tool usage
appropriateness, uh response
helpfulness, conversation naturalness,
completeness, and things like that.
And we did see those metrics,
but the problem was these metrics were
not actionable. They were not giving us
any actionable insights. If something if
let's say a response helpfulness is 0.5,
then what do we do with it?
So,
uh
things like and other other scores like
toxicity score, bias, fairness,
conciseness, all these are kind of
relevant, but if the metrics are just
scores, we we don't know what to do with
them.
So, we can use these pre-built eval
metrics as a baseline, but we shouldn't
use them as our core eval metrics
because we want eval metrics to be
actionable and tied to the business
outcome or the product which we are
focusing on.
Uh
Okay, so what LLM as judge should be.
Uh we collaborate very closely with
um domain experts and utilize their
insights.
So, eval should be framed around a task
success or failure.
And a binary outcome is very easy to
calibrate and train
um LLM judge that can consistently score
your agent trajectory.
When we partner with domain experts and
data scientists to build metrics which
are actionable and aligned with business
goals, we can see much more meaningful
results
uh and actionable insights.
Not only this is more consistent, uh but
when an agent fails an interaction, we
can systematically analyze the error
pattern
and have and actually know what what we
can do to fix this.
Here is an example of an uh actionable
metric for our use case, uh which is
called education rubric. Here the AI we
define the metric how it should be, and
we define success and fail criteria for
LLM judge. So, for example, the AI agent
tries too many times to educate the user
um if it could have escalated the the
issue.
Or if it's escalating too soon without
giving any chance to educate the user.
So, things like that comes under failure
category, so we we mark this as fail, uh
but if it's an expected behavior, then
we mark it as as pass.
>> Uh okay, so
with this, how do we validate if our LLM
judge is working as expected?
First thing is we need to treat it as a
classifier. So, how we train our
classification models in machine
traditional machine learning, we can
also treat our evaluation judges as as
those traditional binary classifiers
with binary outputs. Once we have binary
outputs for every metric or a task based
on our business goals and functional
requirements,
we can hand label
around 100 examples with pass fail
labels and then split the data into
train, dev, and validation sets like how
we used to do with machine learning
models.
Uh then we score precision and recall
for our judge based on human label
ground truths, which will give us an
actual report on how good our judge is
performing.
Uh
and how do we split our data to do to
calculate precision and recall is this.
So,
we split the data similar to how we used
to do in training machine learning
models, but the difference is the
percentage of splits.
Uh and here we are not actually training
models. So, we are just using the data
to inform judges prompt. So, the
percentages are little bit different.
For example, in training data, we we
pick a few short examples from that from
this set for the judges prompt. And then
we iterate the prompt against the dev
set
and improve our harness or our prompt.
And then finally, we validate against
the test set
uh
to see that we didn't overfit on the dev
examples.
This is the practical
way of like splitting the data and then
calculating precision and recall scores
for your judge to actually know that the
judge is working as
expected.
All right, next slide. Okay, so
this is another thing which
This is another thing which most of us
ignore when we are doing evaluations,
which is criteria drift and validating
the validators. The key idea is that we
actually discover what our evaluation
criteria is by looking at the data and
grading our outputs.
Our and our sense of quality will also
evolve with with new data we see and
more
examples we grade.
So
the evaluation should not be decoupled
from model observations. In fact, they
should be developed
They should be co-developed with the
model when we are testing the evaluator
and calculating the precision and recall
scores.
So
uh the
There's always a gap when we when we
talk about LLM as a judge. We cannot
define the criteria beforehand and then
evaluate agents against them.
Our criteria should also be evolving as
and when we see more examples and then
we should refine our metrics
for our judges and then evaluate judges
on top of those metrics.
Okay.
So
the next step
One of the things which which can make
the numbers we are reporting more
meaningful is to add some statistical
rigor to it, right?
Uh, we report alignment rates as their
point estimates.
So, if we add confidence intervals, we
do some calibration and proper sampling,
uh, the same numbers can become more
meaningful.
We should definitely reserve the
expensive rigor for the moments uh,
number actually gets something or
like like a shipping decision or we are
reporting numbers to uh, company
leaders.
But,
depending on the use case, we should
definitely have
uh, confidence intervals for the
for the numbers we report.
Because every score needs an interval.
So, this is just a small example to give
you
uh, an insight on what this actually
means.
Uh, let's say we have two evaluators and
one scores 84% and one and the other
scores 88% and the number of samples we
number [clears throat] of traces which
we have uh, used is, let's say, 50.
So, to show that like this is
this is a very small gain and we we need
much more than 50 examples to actually
uh, show that this gain gain is real.
Uh, with just 50 examples and only 4%
0.1% gain gain, we we don't actually
know if this gain is real or not.
So, bigger gains and
bigger gains and paired designs need far
less
uh, and we can reserve the rigor.
Statistical rigor for for things which
matter the most.
Okay, so this is uh,
non-exhaustive list of observed eval
anti-patterns. I'm not going to read all
of them, but uh
these definitely contain some
low-hanging fruits.
We need to put in time and effort if we
if we need meaningful evals.
So, we cannot rely on LLMs for
everything yet.
Uh
and what I can say is ignoring the data
is one of the most important
uh things
which we shouldn't do uh
and which we sometimes don't focus on
due to lack of time or resourcing, but
it acts as the foundation for meaningful
evaluations. If you don't look at the
data, you won't be able to create
meaningful criteria
uh or labels. And if you don't have
labels, you won't be able to evaluate
your judges. And if you're not
evaluating your judges, you don't know
if your
uh
agentic pipeline is working as as
expected. So, this acts as a base. So,
uh one of the most important things we
should
not ignore.
Okay. Uh we we said that we want to make
metrics more actionable
and standardize the pipeline, but how
actually we should do it?
So, this this gives you like a template
to
to do an error analysis loop. And it is
important to know that this loop is
something which runs continuously. It's
not uh not a one-off audit.
Uh
so, we deep dive into raw traces. So,
once we have logged our traces for our
agentic flows, multi-agent systems, or
whatever we have in our uh
use case,
then we pinpoint failure modes. So,
basically we try to identify what
exactly is failing.
And we only keep the metrics that change
our decision. We remove all the noise.
We only prioritize on the metrics which
are tied to business use cases,
functional uh requirements, and actually
something which changes a decision, then
we form a fresh premise
to reevaluate and then we repeat it. So,
we can have like a regular cadence of
doing this pipeline. It can be weekly,
it can be bi-weekly, but this is
something which needs to run uh
continuously and it's it's not a one-off
audit.
Okay. So, tracing. Tracing, as we said,
is
uh
one of the most important things and
everything kind of depends on it. For
diving deep into raw traces, we
definitely need to log them first. So,
we can use tools like LangSmith,
LangFuse, etc. to log and view the
traces.
Uh and here each trace captures the full
graph execution, which nodes ran, what
LLM saw, which tools were called, uh
what was the token usage, what was the
latency for every call, and things like
that.
We can also add its traces with metadata
if you want, which gives you more
insights than
uh than the actual data.
Okay. And we also have annotation
queues. Annotation queues are nothing
but
uh
an interface which is very helpful for
domain experts to label or give feedback
to evaluators in in an
easy-to-understand
UI. So, they don't have to look at the
raw traces, uh JSONs, and stuff stuff
like that to figure out what to focus
on. They can use this annotation queue
and they can give feedback uh or label
examples easily. We can then add these
traces to datasets for offline
evaluation or we can use this for uh
calculating our precision and recall for
our judges.
So, this forms the basis to validate the
evaluation with ground truth labels.
Okay. All right.
Now I'll hand it over to Nick to
to close the evaluation loop.
>> Thank you, Akshay. Uh and I think the
the goal of having eval is to be able to
feed
uh our evaluation insights back into
improving the model performance or our
agent's performance. So, here uh I'll
introduce
a couple of ways that we can think about
continual learning for our AI agent and
closing the evaluation loop. Um and here
you have model learning, context
learning, and harness learning. A model
learning is really about, you know,
post-training, updating the underlying
model weights, and training a custom LLM
models. Uh
context learning and harness learning is
really more about improving uh
everything else other than the models.
Uh so, context is improving what
information the agent is receives. This
can be documents, this can be uh the
stored memories of the user, tool
outputs, and so and so forth. Hardest,
uh that means updating the model system
prompt, um tool schemas, control flow,
routing, retries, and and so and so
forth.
So, I think from, you know, the error
analysis that Akshay had shared earlier,
I think that has really helped us to
understand how can we improve uh our
agent prompt as well as updating uh
updating our knowledge space, and tune
the context management strategy that we
have our AI agent. Um the identified
seller mode really help us uh be able to
feed that insights into actual
improvement for the agent AI agents.
So, I want to quickly talk about what's
next for us uh in our journey of
building customer support AI agent at
Lyft.
Uh we
have a We we we have We have some some
level of ability to run our offline uh
simulator, but in fact, I think, you
know, it's not repeatable. These are
currently stored as
uh scattered script across different
notebooks and different analysis repo.
Uh I think one thing that we're looking
really really looking into investing is
a systematic eval harness
and having a
uh a a harness system that can help run
our offline evaluation in in a
systematic and standardized manner and
allowed uh different people to
contribute to
uh our evaluation suite with uh very we
we we predefine uh primitive and
conflict-based uh workflow.
Uh another thing that we've been talking
thinking a lot about is uh post
training. Uh as we mentioned earlier,
you know, identifying model failure mode
has really helped us tune the
agent context and as far as the agent
harness, uh but over the years, we have
gathered a lot of real user signals on
our agent performance as well. Uh so, we
we're really starting to think about how
do we fine-tune our model that does
different tasks for our customer support
AI agent
uh as far as framing a reward modeling
problem to to enable reinforcement
learning.
I want to quickly share a little bit
about the work that we're doing with
eval harness and how we think about
building uh building building eval
harness for uh agent-facing
uh user-facing agent deep applications.
Uh so, again, eval is really that
scaffolding that you that we need to be
able to run eval efficiently uh in a
standardized format across
all the different agents and sub agents
that we have for our customer support AI
agents.
And and as you can see from my offline
simulator slide earlier,
our eval harness is config driven and
these are typically stored as YAML file
that's easily editable by different
contributor and not just by engineers.
Analysts and data scientists can can
contribute to this evaluation suite as
well.
And you know, with
thousands if not tens of thousands of
examples
in our evaluation suite, we need, you
know, parallelism and throughput to be
able to run
our offline evaluation in a reasonable
amount of times.
And to enable
user to be different user to be able to
to be able to contribute to our eval
evaluation suite, we also define, you
know, primitive around our eval eval
harness.
These are high-level things like task,
data sets, personas, LM adapter, and and
evaluator.
And after all, you know, the benefit of
having an eval harness is that you can
define the config once and run these
eval indefinitely many times across
different at different touch points or
different gates of your agent
development process.
This can be, you know, locally when
you're developing this agent.
Uh at any point when you tune a prompt,
you can run the evaluation suite and get
an immediate in
immediate feedback on how your agent is
doing compared to the previous versions.
We can run these at pre-commit hook
to make sure that our performance
doesn't degrade before we push a change
uh
uh agent service.
Uh another area that we are looking at
is also a CI/CD and how we can use our
eval harness to uh build our regression
test suite, uh acceptance acceptance
test suite as well.
So,
that wraps up our presentation today. Uh
we've gone through a lot of
We've gone through a lot of uh
a lot of different topics uh for
evaluations.
Uh really, I think this is a an
end-to-end journey
uh for building a evaluation pipeline
that works for customer support AI agent
or any user-facing agent tech
applications. Uh Akshat and I, we are
very interested to hear about, you know,
what you all have been working on and
share any learnings that you have for
eval. So, feel free to contact us
uh if you have any questions or you just
want to share some uh brainstorm about
how to improve your evaluations.
All right, thank you and I hope you all
enjoy the AI Engineer World Fair.
>> Thank you.
Thanks, all.
