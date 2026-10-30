# The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI

Source: https://www.youtube.com/watch?v=rWtbOgl5FTU

Uploaded: 2026-10-30

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> I'm going to talk a little bit about uh
going from beyond the model card, how
evaluations can be used to measure this
jagged frontier. Uh special focus on
finance for this audience as well.
Um yeah, so first off talking about
model cards themselves, we've built uh
some of the most important benchmarks
over the last couple of years that the
major foundation model labs have
included in their model releases. So
people I think are familiar with
artifacts like this. Uh last week we
have Sunder talking about our Val's
index on stage and then uh even just
yesterday Muse models uh reciting our
our Finagint benchmark. You know, it
keeps our lives interesting to have to
keep re-updating these slides as new
models come out. I had to double-check
new models didn't come out this morning,
but um these are say these these kind of
model cards reflect a general
understanding of what's newly capable
with the models. Um and so uh they they
can reveal from a single number how
intelligent is a model. In particular,
our Val's index is compiling results to
try and measure the economic impact of
models uh in domains like finance,
legal, but also coding, health care, and
things like that. So from these
high-level numbers, you can get a sense
of how capable a model is for uh
valuable work. Um but that doesn't give
the whole picture. And so when we dial
in a little bit more closely and look at
the constituent benchmarks that comprise
the Val's index, we can see a more
nuanced picture. And this may be
something you all are familiar with, the
jagged frontier. And the idea that
within a particular domain or set of
tasks, you may see different performance
uh from when you aggregate results to
produce that single number. And so you
can see here across the different
models, uh we actually see an
inconsistent performance for who's
number one.
Uh but that's made even more so when you
look at particular organizations or
companies. So in a lot of ways, coding
is indicative of what's happening across
every major vertical. Um when we look at
coding and actually create custom
benchmarks for particular repositories,
we see that that jaggedness just
increases even more. And so on on the
x-axis you've got different programming
languages and libraries. And on the
y-axis you see the relative performance
of models and see that it's even more
fragmented. But this isn't even to take
into account that there are different
harnesses in which these models can can
be used or the idea that you might be
optimizing for cost and latency as well
as performance. And so this all feeds
into the idea that the the granularity
of of the performance you see in a
general model card benchmark is not
necessarily what's most applicable for
people who are using these models or or
products in practice.
In parallel, AI adoption has gone up
considerably. So year over year there's
roughly a 2x increase in enterprise AI
spend. But with all that spend it's
still really obtuse to understand where
the ROI is coming from. You can see that
people regularly using AI is now 90% but
if you look at the smallest bar now we
have established ROI just at 7%. So for
all this token spend and increased
adoption it's still very unclear where
AI is actually driving value for a lot
of companies.
And I think two interesting stats that
jump out at me, the groups that are able
to actually track AI cost and spend are
much much more likely to actually
understand where ROI is going to come
from. And this is also a key blocker for
adoption itself. The groups that are
unable to actually quantify the cost to
the return on their investment often see
this as a big bottleneck to actually
widely roll out AI. And so I think evals
is the key story here. If people are
able to construct key evaluations that
measure what our model's capable of and
what will be the most efficient
utilization of those dollars, they'll be
able to adopt AI in their firm more
broadly.
I think one particular interesting
finding that that I want to share with
you all is an indication of why the
intuition that are
intuition of model performance as
presented by labs doesn't often align
with experience. So if you look at Opus
5.5 that's the kind of second tier model
from Anthropic. And on paper it's
actually cheaper. $4 and $20 out
compared to Fable 5.1's $10 and $50 out.
But in practice, and particularly for
this tax benchmark, you see that it's
actually more expensive, 14 more
expensive. And that's because the less
intelligent model is trying to expend
more tokens to try and get its work
done. But this actually bears out as a
3% lower score. Um and so you are
actually would have been better off
using the frontier intelligence. You
would have spent less and got a better
performance. Um but that kind of
intuition isn't isn't directly available
for people who are using the models in
practice. And so they may try and say,
"Actually, I should use a Sonnet or an
Opus." But end up overpaying for uh
inferior performance.
Uh and so I think this, you know,
reveals that we should actually take a
more diligent effort to figuring out
where return is coming from. And and
that will inform a more realistic
picture as opposed to the intuition that
labs are feeding directly.
If we look at look at finance in
particular, so that this kind of jagged
frontier concept, uh I've highlighted
the Vals Index, but we also have a
finance agent benchmark looking at
research tasks for finance, and then
Excel modeling, uh and then tax agent.
Uh and even across these benchmarks
again, it's not immediately obvious
which is number one or will be
consistently two or three.
This picture is made even more nuanced
when you look at the Pareto curve. So on
the x-axis, you've got cost. In
particular, it's cost per task, not just
token in token out cost. And on the
y-axis, you have performance. And and
here what we're looking at is that Excel
modeling benchmark. So seeing whether
these AI models can create and work with
Excel models that are core to work
that's happening in finance. Uh in the
green, you have the overall performance
across all of the questions. And then in
red, what we've done is is segmented out
the LBO tasks. So this is a particular
subset of Excel model tasks that you
might you might be working with in the
in uh
um using any of these models. Um and I
want to call out a couple things. In
particular, first what you see is that
the entire frontier for LBO is lower
than the overall task score. So the
intuition you would have from just the
the high-level EMB results would not
match what you see for the LBO
categories of tasks. And so if your firm
is especially doing, you know, one type
of Excel models over another, it's
important to have a clearer picture of
what's going to be actually relevant to
you. But the other is that the frontier
is also changing when you go between the
overall scores to just the LBO
subcategory. So, whereas you might have
thought you would have get the best
possible performance from using Feable
5.1, when you go to the LBO it actually
drops off the Pareto frontier. You're
going to be massively overpaying for
what is no longer the state of the art
model for that category. Uh and so
again, this kind of reiterates this idea
that it's it's less important what you
see at the top, but actually the subset
of tasks that are most relevant for you
and the cost performance optimization
that you want to see within your
company.
So, I want to share uh some some lessons
from actually building the benchmarks.
We talked a little bit about the results
and and why the results may be intuitive
unintuitive. Um when we actually build
benchmarks, one of the most important
things that we need to look at is the
metric we use to report accuracy. Uh and
so you you you have a different takeaway
if you pick a different metric. A lot of
benchmarks deal with partial credit. And
so what this is answering is in
expectation, if I were to give a
question or task to a model, what
percentage of the points would I expect
to uh see satisfied by the the the work
the work output of that model,
especially compared to humans? And then
the fully corrected answers metric is
more looking at of the percentage of
questions that I give to models, what
percentage of them will come back
perfect? And that's that's a very
different metric. It may mean uh that a
model is very good at producing uh an
incremental response that you can work
with to build a better response. Um but
if you were to pass this directly to a
client, it would be a coin toss of
whether it was meeting all the criteria
that you have. Uh and so picking the
right metric is very important to
accurately representing the performance
of a model and actually forming a good
intuition of what it can do.
There's another three components that we
think a lot about. So, validity, are you
actually evaluating what's going on in
the real world? That means are the
questions or tasks reflective of actual
work going on or are they contrived? Um
and then are the rubrics actually
describing what we're looking for or the
standard of excellence we want to see?
Reliability, this is usually a function
of the number of tasks or the sample
count. Um a lot of companies, they have
maybe five or six samples and they're
kind of vibe checking new models or
products as they get access. Um but it's
actually really important to have a
rigorous approach and have enough tasks
and samples to make sure your repeated
runs actually show consistent results.
And then lastly, discriminability. So,
we we don't think it's that valuable to
have benchmarks where all models score
100% or all models score 0%. Ideally, we
can we can actually discriminate between
models and see what the frontier looks
like. In particular, we also want to
make sure we're building benchmarks
forward-looking. So, what are the new
set of tasks that are even more
ambitious than what models can do today
uh to make sure that there's room at the
frontier for us to uh you could uh to
continue to see model progress as they
get better.
Okay. So, and then some of the
high-level problems that we've seen and
I think others
uh you know, can and and do run into.
The first is that agents solve the task,
not the problem. So, this is talked a
lot about as reward hacking. Um, and
we've seen a lot of instances where
we'll have a sandbox and models will be
run with our model proxy. And sometimes
they may try and actually call other
models uh within that proxy to escape
the sandbox or make use of the internet.
Uh, so it's really important to to build
the the containers in a way that you're
actually testing for what matters. Can
they can they do the task at hand um or
are they actually leveraging other tools
or maybe even other models to get there?
Um, we've also seen this issue in
finance in particular where a lot of the
times uh evals are looking at a set of
rubrics or or items that we want to see
included in the response. And so, models
can hedge and give three possible
answers uh which has a higher chance of
satisfying all the criteria um but in
practice, that's way way too much. A
person does not want to consider three
different answers. They just want to get
the the first answer and and have it be
right. Um, and so,
the goal here is to try and build evals
that are reflective of the actual work
people are doing and the work output
they want to see um not to build these
contrived evals that that the models can
actually gain.
The second is I think a lot of people
are starting to see that the cost of
software is coming down and it's it's
actually very very easy to produce code.
But
unfortunately, we still see in practice
that running evals is incredibly
challenging, especially from an
infrastructure side of things. Um, and
in particular, as we get to
longer-running agents, it means that
it's really important to have
infrastructure that can stay consistent
over a long period of time and then if
interrupted, can be resumed and
respawned back up. Um, we have I think
just recently crossed 6 trillion tokens
just in evaluation. Um, so we run a
considerable asset of evals and we run
everything in as highest degree parallel
as possible. Um, so I think this has
really been load tested, but I think
other people are going to run into this
even on a much smaller scale.
Uh, and the last is that I think a lot
of the existing benchmarks, they deal
with a single prompt, single response,
but in practice everything is
multi-turn. Uh, you have an initial spec
which you think covers everything, but
then you get questions back or you have
additional feedback once something's
built and then it takes more of this
iteration to actually drive to the end
output. And so I think benchmarks and
evals need to actually cover this
multi-turn component. That's not going
to go away.
So to look at a case study in
particular, when we looked at our team,
we did a little token maxing experiment
uh, where we we got free access to some
tools and just gave it to all the
engineers. Um, and they they really made
use of these unlimited tokens. Um, and
and if if we actually look back for that
month, we spent 1.5 million dollars
worth of tokens. This is like a team of
I think 10 or 12. So it's roughly 10
times the amount we were spending on
salary for tokens in that month. Uh, and
so that was pretty insane, but we saw
great output. And so our goal was to try
and maintain the same level of output
across all these engineers, but
massively cut cut down on cost. And and
really our solution to do that was of
course to build an eval. Um, we built a
bunch of tools internally and then have
now exposed this as a product called Val
Smith. Uh, and so this is you know, what
we're doing in coding and I think it's
again a sign of what's going to what's
going to come in other parts of
knowledge work. Um, so what we were able
to do is look at the GitHub repo um, as
a essentialized way of seeing what work
has already been done and what work is
continuing to happen. Um, and in
particular GitHub repos are comprised of
PRs or pull requests which have a GitHub
issue and a resolution. And so what we
can do is unwind the clock and give
those same tasks to agents to see if
they could have equivalently done the
work of humans.
Um, and in doing that we found a a a
much clearer understanding of which
models were overkill, were way too
expensive, and did not need to be used,
and then which ones were actually
capable of getting the task done. Uh and
I think again, this is another place
where the intuitions that a lot of
people have may not be what's actually
born out in practice. So, I think you
may see, "Oh, we're using a lot of
close-source models. We should try and
cut costs and use our own self-hosted
open-source model." Uh you can see the
comparison here we have between GPT-5.6
Soul and Kimiko 3, and we see that 5.6
Soul is better. It's It's going 2%
better on this internal eval. It's also
considerably cheaper than than hosting
it through a very, you know,
inference-optimized uh stack. So, it's
$2.50 instead of $11, and it's faster,
half the time. And so, there's no real
reason why um this kind of intuitive
sense of using open source would be a
legitimate way to drive down cost. Um
and so, this has resulted in two main
differences. One, we can actually figure
out which tools we're going to procure,
what the usage limits of those things
should be across the organization,
but then also, we can give
recommendations for engineers and say,
"We think that for this GitHub issue,
you should actually use this particular
coding tool with this model." Uh and
this is able to drive the cost down
considerably. I think we're spending 90%
less, but still able to get the same
output.
I think the question I would have for
you all We're We're continuing to expand
this approach and and take this model of
coding to other domains, knowledge work,
legal, finance, things like that. But
the key question is,
where are you tracking the history of
work that has already been done by that
firm? Some of these law firms have been
around for like 100 years. And so, where
Where is that I think quality of the
organization stored? Where are you
tracking the standard of excellence? And
so, that's today may exist in places
like email from the history of responses
that people have had with their clients,
may exist in SharePoint, may exist in
Databricks dumps, but I think this is
the key treasure trove that a lot of
companies have and don't realize will be
the major unlock for evals, and then the
unlock for AI adoption more
systematically.
Once these evals are constructed,
they can enable adoption to happen, but
we've also seen that there's more
advantageous ways that they can be used.
So, first is right-sizing.
So, rather than just token maximizing,
how do you figure out what the right
usage limit should be across the
organization? Negotiation. Once you
realize uh you have actual leverage, you
can take that to the conversation you
have in bulk pricing.
Then routing. This is becoming a core
primitive in uh
in a lot of AI products, um but can also
be done by users directly. And so, they
can build intelligent routers that
actually figure out the right model to
use.
And then fine-tuning or post-training.
Uh this this can be the most reliable
way for you to actually mint the tasks
and then have an external eval set to
make sure that this approach is working.
Last thought I'd leave you with is I
think for a lot of companies, they have
a competitive advantage that has existed
in the heads of employees through things
like institutional knowledge. And what
evals allow you to do is actually
codify the competitive advantage and put
that down in words or in scripts in
language. Uh and that will actually be
the the biggest unlock for uh making
sure that a company succeeds through the
agentic era. Okay. That's all. Thanks,
everyone.
>> [applause]
