# Why Frontier Models Fail as Buy-Side Analysts - Janie Gu, Google DeepMind & Suyeol Yun, LinqAlpha

Source: https://www.youtube.com/watch?v=aVbRSIQO2dE

Uploaded: 2026-10-25

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Good afternoon. Super excited to be
talking about Evals today. So today
we'll be covering the difficulty of
creating Evals for real world workflows
in production.
How Google DeepMind and Kaggle are
collaborating to solve this problem
and a case study that we did with our
partners at Link Alpha. So they'll
present next about a specific benchmark
called Mandate Bench which basically
looks at how how well models can perform
as a buy-side equity analyst.
So to start with some quick intros.
I'm Jenny. I'm a product manager at
Google DeepMind. I lead our Kaggle
benchmarks team.
Ivan is our amazing forward deployed
engineer at GDM. He can't make it today
unfortunately.
Jacob is in the crowd and from our Link
Alpha partners.
So he'll be presenting with me and Jack
also couldn't make it unfortunately.
So just starting with a quick intro
about Kaggle and how we got here. So
Kaggle you guys probably know Kaggle as
the home for data science and ML
competitions. I'm sure many of you have
have interacted with Kaggle or competed
in a Kaggle competition in in the past.
And so we've been doing this for for 15
years. Basically evaluating humans on
different capabilities in in the real
world. And we've built up a community of
31 million AI and ML enthusiasts across
the platform. Thousands of competitions
over the last 15 years
and one leaderboard that everyone really
trusts. And what has really made Kaggle
succeed in the last 15 years is is our
rigor. So we have sealed private test
data sets. We
um leak detection, anti-cheating
infrastructure, and really make sure
that that every single competition that
that is put on Kaggle
uh is designed really well and good at
evaluating humans on on the capability
that it's supposed to be.
Um and so that brings us to today. So,
in February 2026, uh Kaggle actually
moved into Google DeepMind
um and we're moving our subject from
evaluating humans to evaluating frontier
models.
Uh and so Kaggle is basically become
GDM's public platform for for
benchmarks. And our goal is to make an
open, neutral proving ground for every
single frontier model uh that uses the
same infrastructure, the same tasks, and
the same grading um so that you every
score is representative.
Um and our goal is really to become the
industry standard for benchmarks the way
that Kaggle uh already is for
competitions.
So, why does this actually matter? Why
are we Why are we getting into this
problem? Why is Kaggle trying to tackle
this problem?
Um and it's because benchmarks are
really important. Benchmarks are how we
measure progress in the AI industry.
And right now, the state of benchmarks
is fundamentally broken.
So, you think about all the different
ways that benchmarks are used today. Uh
frontier labs are using them to train
and hill climb models. Startups are
using them to decide what models that
they want to build their product around.
Investors are using it to judge
technical amounts.
Um and how you measure like what whether
the benchmark is correctly measuring uh
what you want it to measure is exactly
what the models end up hill climbing.
Um and when you measure the wrong thing,
the models actually get worse at at what
they're supposed to be doing.
So, there's a few different ways that
benchmarks fail today.
Um the first one is is relevance. So,
most public benchmarks don't actually
resemble the real work that that your
agents are doing in production today.
So, most of them test synthetic puzzles,
academic trivia, random math problems,
um and that bears little little
resemblance to what your agent actually
does in in production.
The second problem with benchmarks today
is it's very very expensive in terms of
a compute perspective, uh which is the
like most scarce re- resource in the AI
industry today. So, take a benchmark,
let's say it has 500 multi-turn agent
tasks, and you want to run it across 16
frontier models, um that costs tens of
thousands of dollars per sweep, um and
every time that a new model launches,
which is basically every week or two at
this point, um you have to do the sweep
again in order to keep your benchmark
current, otherwise it it becomes stale.
And the third problem that we see, uh
which is probably the most
underappreciated, is verification. So,
everyone like all the benchmarks in the
industry, everyone runs their own
harnesses, they report their own scores,
they they build their own like
self-reported benchmark implementation,
and the numbers are wildly different
across different implementations. And
this is mostly because of
infrastructure, not because of actual
differences in model quality. So, if you
have different scaffolding, if you have
different ways that you're calling
tools, if you input if you just
serialize the input into the model in
different ways, um you end up with
different benchmark scores, even if it's
the exact same benchmark on the same
model.
Um so, that last point, uh around
verification, I think, uh is probably
the most abstract. Uh so, wanted to to
deep dive into that a little bit. Um so,
we, uh in order to really understand the
the state of the benchmark industry and
all of the different problems,
uh we at Kaggle spent the last 2 months
reproducing 65 different industry
benchmarks,
um and recreated all of them, ran all of
them, and read every single trajectory
trace by trace to to really understand
what the problems were so that we could
figure out like what the infrastructure
we wanted to build was to fix it. And we
saw tons of issues across all of these
different benchmarks.
So I'm listing a few of them here just
to give you an idea of all of the
different problems. So for one benchmark
we found
the model that was being evaluated
actually found the API keys
in the eval container
for a different model and then called
different model and then use that
response and submitted it as as their
response to the eval.
Second,
most people when they when they build
their benchmark, they they don't
actually separate the agent being
evaluated from the agent being graded.
They share the same the same container
and models are really good at at hacking
their container now. So we found models
basically modified the grading script in
order to give them whatever score that
they wanted which was 100%
and and let themselves pass.
The third is just pure like statistical
variance. So we found for all 65
benchmarks we ran all of them multiple
times
and we found that running the exact same
benchmark even on the same
infrastructure
multiple times produced variance of up
to plus or minus 20% in the score.
And again, this is the same model on the
same exact harness on the same exact
infra.
So this is just reflective of
instability in in the the harness or the
benchmark design itself.
I think everyone's familiar with the
hugging face incident. So we found
instances of models basically trying to
look up the answers online
in different forums like hugging face or
Reddit or Stack Overflow.
And then this one we were very surprised
by. So, each harness uh actually ships
with its own default reasoning effort.
Um, so if you use the default uh without
setting it, um then you actually end up
comparing models uh at different
reasoning efforts. So, you might have
one model that's running on high and one
that's running on low if you uh if you
don't actually configure it uh in order
to make sure that it's a head-to-head
comparison.
Um, and a lot of the times when we were
recreating it, we found that people did
not do this uh because our scores
actually matched parity with the
original benchmark paper, um but we
found issues with with the score itself.
Um, and so given all of these problems
in in the industry, uh Google DeepMind
and Kaggle are are partnering to solve
this. So, we're doing a few things here.
Uh the first is we are partnering with
companies and researchers
uh to build to build benchmarks around
real workflows uh economically viable
real real-world workflows.
Um, and to make this happen, we are
offering free compute and frontier model
inference uh to anyone who wants to
build a benchmark. We're giving out $5
million
in grants in in Q4 to fund any benchmark
creation or research into fixing this
space of of benchmarks given how early a
space it is.
Um, and third, we will uh we will
provide you a forward deployed engineer
from from GDM to help you co-design your
eval uh to make sure the methodology is
actually rigorous.
Second, uh we we talked about this a lot
on the last slide, but a lot of these
problems are just issues all up and down
the infrastructure stack. Um, and so
what we're building at Kaggle is
standardized infrastructure so that
every score is auditable, uh high
quality, and and
repeatable. So, this includes
um sandboxing every run, having logged
proxy calls and open traces for for
every model call, and containerized
grading.
And then lastly, uh, the reason why we
specifically are doing this, uh, is is
for our expertise.
Um, so Kaggle has 15 years of designing
rigorous tests and preventing cheating
by humans, which we are now applying to
to the model evaluation space. Um, we're
bringing GDM researcher expertise to to
help us design all of these these
real-world benchmarks. Um, and lastly,
we're actually partnering with
independent research orgs, uh, like
Epoch to audit all of the benchmarks on
our platform, so you don't just have to
take our word word for it.
So, at this point, I hope I've convinced
you, uh, how important benchmarks are.
Um, but you're probably wondering, why
should I build a benchmark as me as like
a company with other priorities and
other things to do?
Um, and there's a two two big reasons.
Um, the first is it actually allows you
to build faster internally. So, having a
benchmark and having a rigorous
evaluation suite, um, allows you to
easily tell when when you model modify
your your prompt, when you modify your
hardness, whether you've broken
something or how you've improved your
product. Um, and then the second is if
you then want to publish your benchmark
externally,
uh, then labs will be encouraged to
actually hill climb on your use case.
Um, like most of the labs are are
looking for real-world benchmarks.
Um, and once the labs want to hill climb
on your benchmark, then they'll pour
trillions of dollars in of compute into
improving the base models,
uh, for your specific use case, so that
your product gets better for your users
over time.
Um, and with that, I will pass it over
to Link Alpha, um, to to talk through a
case study of Mandate Bench, which is
one of the first benchmarks that we
built on Kaggle.
>> [clears throat]
[applause]
>> Great.
Hi everyone. Um this is Suyo. I'm head
of AI at Link Analytics, and we create
we created a benchmark called Mandate
Bench. It's built co-developed with
Google DeepMind and Kaggle.
So before start, let me share briefly
about our company. So Link Analytics
builds AI research agent for
institutional investors, institutions
with more than $5 trillion
in assets under management using Link
Analytics. And more than 200 investors
use it actively. There are some of the
firms that trust us I listed up here.
And we're we're also a research team. We
have published 13 papers at
at the venue like ICLR or ICML
with co-authored with the BlackRock,
Blackstone, JP Morgan, etc.
So um
>> [clears throat]
>> I'd like to first go through the
existing financial benchmarks.
So most of these benchmarks prepare a a
golden answers and compare it with the
agent answer.
But in real world task two analysts can
reach two different answers and both
could be right. So existing benchmark
use relatively short and simple task.
They don't um
um they don't task a full unit of
analyst work. So they only get the
fragments of it. So Mandate Bench aims
to do two things. First,
its rubric explicit grades the
reasoning path. Second, we take the real
world real unit of work seriously. For
our analyst, the unit goes from the
funds mandate
or
and from the mandate all the way to an
investment memo.
So,
let's first look at what a task in the
benchmark looks like. Let me start with
a simple question.
Um how does an analyst work at a
um hedge fund? Nobody gives an analyst a
simple task. The PM gave analyst the
funds mandate and a company. For
example, the mandate looks like we are
an event-driven fund and we trade on
mergers and acquisitions with a
holding period 3 to 12 months. And the
PM asked, "Okay, here's a company A and
we know company A will be bought by
company B. Should we go long, short, or
just pass on this company? And please
bring me a investment memo with detailed
evidence and the reasoning behind it."
And this can take an analyst hours, 20
to 22 hundred hours easily. And this is
the one real unit of analyst work.
So, let's go deeper into an example
task. Here's a company called Sonoco and
it's a US packaging company. Recently,
Sonoco bought about a company called
Eviosys and it's also sold one of its
business called TFP. To value Sonoco,
you first need one basic number, which
is a sales. But five different sources
give the different um sales numbers from
5 5 billion to 8 billion dollars. Why?
Because each source counts a different
different Sonoco.
So,
first, the agent has to understand the
numbers doesn't match. Second, it hasn't
it has to find out why. And
and um
and third,
and also second, it has to find out why
and third, it has to rebuild Sonoco as
it was in May 2025 with Eviosys for the
full year and without TFP. This it will
be about 7.5 billion dollars of sales.
And that is just a small part of the
entire reasoning to skill analyst to
work through.
So, then how we grade the agent work?
So, agent submits an investment memo
long together with a reasoning graph in
the graph and then every fact should
point to exact two call it came from.
Then our former buy-side analyst
>> [clears throat]
>> write down the key reasoning steps that
any good memo would include. Each step
is a node in the graph. First, the
no-code agent must rebuild the company
it was in May 2025.
And what the new new
new business really earns and net out
what was sold and rebuild the debt.
If first that we ask
HR, we also attacked the memo with the
what if test. For example, management
pro- promised cost savings from the EVOC
still. But, what if the sales savings
were zero?
Would the call change? And does the memo
explain this
with clear reasoning about the moving
parts?
So, the
So, the So, the
memos can reach different calls and the
both can score well as long as the work
behind the each calls are there.
So, this is the result and you can see
the cloud of This is a preliminary
result.
Only runs over 10 tasks
of 50 entire task universe. And the
cloud with 5.5 scores best.
In the matter of time, let's skip to the
next page. And every model behaves
differently. For example, Astra 6 really
good at making a financial modeling,
while the Opus 5.5 is a balanced very
well over the cross different
um test. Okay, let me get back to Shane.
>> Um awesome. So, that was the first
initial 10 tasks um of Mandate Bench.
The the full 20 50 task benchmark will
be launching uh next month in in
November 2026.
Um and
uh this is part of many many other
benchmarks that are launching in on
Kaggle and and DeepMind over the next
few weeks. Uh we've partnered with a
bunch of leading AI startups uh to build
benchmarks in different domains.
Uh we launched HeyGen's code code to
video bench uh last week. Um we're
working on a couple other benchmarks
with Octava, Quadrillion, and Rehearsals
uh on on
meta
uh clinician workflows, research
workflows, uh and user research
workflows. Um so, if anyone in the crowd
is interested in in building a
real-world benchmark for for your
company,
uh we're we're very interested in
collaborating. Um as I mentioned before,
we're we're providing free model
compute, uh FTE support from from JDM,
and $5 million in grants.
Um so, please reach out to us. We we'd
love to work together. Um thank you so
much.
