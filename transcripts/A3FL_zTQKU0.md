# Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics

Source: https://www.youtube.com/watch?v=A3FL_zTQKU0

Uploaded: 2026-10-23

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> My name is Stephanie Jarmak. I am an AI
engineer as of a couple weeks ago at
Omni Analytics
where we have a platform that
has like a governance semantic layer to
have a shared understanding of business
data using our beloved agent Bloopy.
Before that I spent a year at
Sourcegraph where I was a solutions
engineer for Amp, a coding agent, and
then I moved into some sort of amorphous
type role where I was largely doing
their evaluation platform. I built a
very large public benchmark called Code
Scale Bench to understand how agents are
working across very complex code bases.
And then prior to that I was an
astronomer.
So I come from this from a research
scientist sort of point of view where I
relentlessly question everything, hence
the title of Lies, Damned Lies, and
Evals.
It says how to trust your agents, but I
think largely this talk is mainly about
how to not trust your agents.
So here's one example of a run I had
done back at Sourcegraph when I was
testing out their code search MCP tool.
This is just to show all of the
different sort of numbers that you can
have after you run a certain evaluation.
The what I was trying to do was figure
out hey, why isn't this coding agent
actually using the tool that I'm trying
to get it to use? And so you know it
ran, I have all the traces and
everything and then I you know looked at
some of the primary sort of metrics that
you're looking at when you evaluate the
overall effectiveness of a tool and it
showed we
basically what I had done was I changed
the initial prompt given
to the agent and then I ran it cuz I
wanted it to use the tool.
And what I saw was okay, uh, it was 28%
cheaper. That's that's interesting. Um,
but, you know, that shouldn't really
change any of my decisions around what
I'm actually trying what I'm interested
in measuring and understanding in
changes to um, the actual harness and
setup, uh, because it still didn't use
the tool.
Right? So, you need to be able to
understand like what it is you're
actually
setting this up. The the 28% um, is
maybe an interesting avenue to go
explore. Okay, we have some level of
like experimental space to be figuring
out what's the variance and what's going
on with the with the cost measurements.
Um, but we still weren't like seeing it
actually use the tool um, that it was
supposed to. And, uh, basically we had
this whole like, um, indication that it
was receiving certain information and
then just trusting that that information
wasn't there. And that was purely
because it didn't use that tool.
And I also want to talk a bit about the
impact of the harness itself. Um, so,
here's an example, and this was from a
third-party source where they had 63 or
so tasks, um,
on Turbo Bench 4, which is a pretty
popular, widely used, um, benchmark for
coding agents. And they, you know, you
have like let's say you're trying to
pick which model you're going to, um,
put into your harness. Um, so, here's a
comparison they did they did they did
with, um, Opus 5 then and Astra. And
they saw that, you know, with Open
Hands, which is one of the open
harnesses, um,
Opus 5 beat it out. But then when they
swapped the just the harness, um,
itself, then they saw that Astra did a a
much better job, right? So, it was like
30-plus percent sort of difference
difference in the, um, effectiveness of
these configurations. So, the takeaway
here is you want to be
actually evaluating the closest like
configuration that you can that's going
to reflect the the work and the
environment that you're going to be
measuring because there are so many
different variables involved. And, you
know, you might be uh, you know, you
might see all these um, benchmarks and
whatnot and see the the fancy results,
but it might not do what you expect it
to do within your actual
environment.
Um, which leads a bit into what I kind
of disambiguate and expand a little bit
more on how to interpret um
like public benchmarks versus what is an
evaluation. So, an evaluation is you're
making measurements to
make a decision about your product or
process and those changes. And the the
public benchmarks as they exist um are
really primarily helpful for you to have
a broader understanding of like the
larger landscape and get a short list of
what you might be exploring within your
own um organization or your own um sort
of tooling. Um, but you don't want to
necessarily over index too much on what
some of those results are because of the
spiky nature of all of the training of
these different models and things like
that. So, you know, if you are a law
firm, um you don't want to necessarily
be looking at like the terminal bench
results unless of course you are looking
at incorporating coding agents
with your devs, right? So, you want to
make sure that the configurations
reflecting um your actual environments.
Um, and then the you can also like think
of benchmarks really as just a um
standardized sort of reference set for
comparison. So, you have these public
benchmarks, but then you can also set up
benchmarks within your organization to
use as like setting them up as
reflective of actual workloads as
possible and just have this sort of
iterative flywheel process where you are
um
increasingly sort of hill climbing to to
optimize for your for your
configurations.
And uh you want to approach this uh to
the best of your ability as a as a
scientist kind of when like once you
sort of short list what your various
configurations might be, you want to
look at what are the different variables
we're going to think about changing um
so that we're actually going to be like
that the results will reflect what our
system is, right? So you can think of
workload coverage. So you want to pick
tasks that are going to actually be
reflective and you could cluster them
into different families and things like
that. Like when I was making the coding
benchmark, um didn't want to just like
the reason I built out a whole different
one was because at the time it was
largely like STB bench was just bug uh
fixing, but there's a whole other
different swath of tasks that are
relevant to developers across the
software development life cycle. And the
way that you integrate different tooling
into those different like workloads is
going to potentially be different. So
like a model might be more effective at
code understanding than it is at
actually fixing a bug, for example. And
then you want to try to see, okay, how
many like different runs do I want to do
um because as we all know, these systems
are non-deterministic and so you might
see some level of variation um across
run to run. Um and then as I had shown
before with like that different
configuration of the model and the
harness, you want to think about how is
how are the different sort of um
combinations of potential changes going
to have these um interaction type
effects, right? And how how is that
going to potentially be
um influencing downstream effects?
And you also want to be able to
gather as much observability data as
possible. So, you know, retain all of
your traces and everything. Um so this
sort of goes back to one of my the first
examples when I was trying to figure out
like what is happening, why why is it
not um calling this tool. So first, you
know, you want to sort of break it down
into what is the sort of entire
uh context available to the to the
agent. So it was that tool even
available, right? Cuz if it wasn't, then
you okay, you stop there and you you fix
that um particular, you know, scenario.
And then you see was it called, um
etc. or like what what were the values
returned so you like basically keep
going along the the pipeline of
available um, information.
Um,
and I this one um,
the like so as you're going along that
pipeline
let's say uh, I do this improvement,
right? For this uh, tool it finally uses
the much better tool. Um, but then the
actual like outcome that you care about
at the end of the task, like that still
doesn't change, right? So there are
scenarios too where you can have this
beautiful tool that you're like really
optimizing for, um, but then the agent
the configuration or or or whatnot for
whatever reason which then is your job
to go in and and figure out and fix, um,
it's not leveraging um, that
information. So you want to keep all of
these different um, things in mind like
the non-use and the failed attempts um,
and everything um, when you're trying to
basically be a detective in
understanding what is actually going on
um, in your system.
And uh, you also want to
uh, really control what the measurement
is that you're making. Um, so in this
example, um, when I was doing the uh,
tests of um,
the comparisons of different sort of uh,
search tools, right? I was interested in
optimizing for like a better basically
like an F1 score balancing for precision
in addition to recall. Um, so in this
example was with like grep, right? So
Claude or whatever were going out and
basically pulling in the entire kitchen
sink. Um, so in this example Claude went
out and got like 295 files returned when
it only really needed six. So you know,
if I was somebody who in this uh,
scenario was like, okay, all I really
care about is that it pulls in any
possibly relevant piece of information,
then maybe a recall of one is
sufficient, but in my scenario I was
interested in optimizing for a
completely different um, type of value.
Um so, this is relevant to for when
you're looking at those like single
number scores and public benchmarks,
like what was the actual validator
measuring and why did they consider that
to be important? Um cuz what what you
might want is going to be dependent
entirely like on your business needs.
And um there's like a interesting sort
of overlap that kind of happens when
you're thinking about evals um and then
sort of quality gates and reviews and
things like that. So, I just sort of
wanted to touch on that a little bit
here
um in terms of like the trust and the
safety. Um so, I have like a software
factory that I've been experimenting
with having um these different approval
uh queues essentially of I want to
automate as much as possible with uh for
the work to get done, but I also do not
trust these systems like at all. Um so,
I'll have these uh regular audits. Um
So, uh as an example, um basically I
will have like a rep- like put through
the request for some work to get done um
and then it it um has approval and
required checks, but uh
basically what was happening was the
agent noticed things were going wrong,
but then there was no mechanism in place
for it to actually like enforce uh a
stopping situation. So, you need to sort
of decouple what's happening with um an
agent or some other system like flagging
something versus um actually enforcing
that um like gate within the code
itself. And then how that is eventually
potentially escalated to a human.
Um
cuz this sort of goes into you need to
also think about balancing that human
review load, right? So, if you have for
in this this comes from um basically
auditing and repairing LLM as a judge um
failures that were happening um in a
separate system. Um but they were seeing
like a 1% uh, false alarm rate. And if
all of those, like, um, basically the
alarms that are raised go to a human,
that would result in 10,000 reviews. And
like, does your organization actually
have the capacity for domain experts to
be going and doing that? Um, so it's,
you know, you need to think about where
that bottleneck might be and how you,
um,
like, change what the sort of alarm
rates, um, tend to be. And, you know,
what, how consequential are those, are
those, um,
alarms going to impact like downstream
effects?
And, uh,
we want to also consider that, um,
you know, the actual agent trace itself
can sometimes not be,
um, reliable or like trustworthy. So, in
this particular example, um, researchers
were doing, um, some checks to basically
seed in, um, different sort of like
security issues, um, that were provided
to the agent. And, um, they had like a
hash check in place to check for like
any sort of tampering with that system.
Um,
and with, uh, using that setup,
basically, uh,
everything passed. It didn't It didn't
notice, um, any of those, um, injected
security issues. So, but when they had
an independent, um, sort of, uh, record
comparison, um, take a look at basically
all of the traffic history in the model,
um,
uh, changes and things like that, then
they were able to detect everything. So,
you want to make sure that like,
depending on the security needs of your
system and how you're actually measuring
and and observing, um, what's going on,
that you have sufficient sort of, um,
trust in, uh, the the actual record that
you're retaining of what happened.
And, so this is basically just like an
overview of, um,
like, going back to that, original um,
example of, you know, how we're trying
to think about um
evaluating realistic sort of work um
associated with your particular um task
loads. So, you want to identify like a
target work comparison. So, um I'm doing
a lot of this right now at um Omni and
working on their evaluation harness. So,
we're um looking at our internal
production data and seeing how uh our
users are interacting with the agents
and sort of uh having a classification
of the different types of um
things that can be done. So, in our
example, it's um Q&A, which may be easy
questions to harder questions. Or it
could be dashboard building and app
building and things like that. So,
there's all these different sort of ways
of classifying the actual tests. Um and
then you want to um
be like identifying um
are these changes actually like the
putting into the system actually uh
adding value or where the failures in
downstream? Um and we're doing all of
this, right? And trying to come up with
representative proxies of actual uh
workloads, but ultimately like
production is truth. So, after you
deploy some of these changes, then you
need to also have measurement systems in
place to get all of that relevant data
in the actual environment that that your
system is being deployed in. And you can
do this in shadow and whatnot as well to
to gain some of that information if if
some of it would be kind of um less
trustworthy to to change and you have a
higher blast radius uh radius of of
effects and things like that. Um but
ultimately, you want to be like
essentially optimizing for as much
observability
um and realistic environments for where
your system is going to be deployed for
you to be able to trust some of these um
values.
So,
you to um
identify
like
what level of um sort of risk you are
going to be um willing to accept. Um so,
the way I have it sort of set up within
my own um systems um is I within my
software factory, like as an example, um
for like giving the agent some level of
um autonomy in making some of the lower
risk um decisions is um
uh basically, they will identify what
the next um action would like be, like
why it's needed from a human to um be
able to weigh in on that, what the
actual operating scope is.
Um and then, you know, what um like
potential um
suggested sort of human check removed,
like given the available um sort of
spaces. But, um you want to be able to
come up with those different sort of
boundaries of
when is it safe to autonomous
autonomously deploy versus um stop and
escalate to the human.
Um so, I have a GitHub repo with a bunch
of the different um skills um that I've
worked on. Um there's a few in there
that have uh direct uh relevance to um
evaluation design and harness
traceability and reliability procedures.
And then, I also have this like
monstrous 300-page archive tome that,
you know, you can point your agents at.
Um you can point your agents at all of
this, right? Um to like pull in some of
those best practices into your own
systems.
So, thank you.
>> [applause]
