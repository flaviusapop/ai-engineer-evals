# Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse

Source: https://www.youtube.com/watch?v=obfPzbapMIM

Uploaded: 2026-10-18

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

All right, let's get started. Welcome
everybody to our workshop on evaluating
AI applications with Lancuse. My name is
Annabelle. I'm a um AI engineer uh AI
solutions engineer at Langfuse. And I'm
today joined by my um colleague Donelli
who is leading AI solution architecture
at Langfus. So working with our biggest
customers on making sure they actually
shipping reliable agents to production.
I myself uh was in my previous life how
I like to call it because it feels like
a lifetime in a company building AI
agents for medical device compliance.
And in this industry it was super
important to make sure we are running.
We're making sure we have ground truth
data set that is validated by our
customers and we also ran a lot of human
in the loop systems and a lot of my time
I actually spent in Lenfuse and at some
point I decided okay why not swap sites
and also help other teams that are
shipping agents especially also in
regulated industries and uh joined the
langu team uh roughly seven months ago.
So but before we dive right into it we
wanted to get a little bit of a feeling
of who is here today and who we are um
yeah coming together with. So uh we were
wondering who of you has brought AI
agents to production before and with
that I mean been part of a team doing it
not necessarily yes someone in the
company did it so actually like been
part of a process to bring it to
production
okay that's good amazing it's a lot of
people and we hoped uh to have this also
and who of you has worked with languages
before
okay quite some and any other kind of
observability in evas tool
Okay. Yeah, also a few uh amazing. And
then finally, who has solved EVAs for AI
applications?
For the confident hands, I would love
you to come by at our booth and explain
us how. Um because actually it is quite
hard and I think um all of you have
experienced it if you're working with AI
or also just chatting with Chat GPT or
Claude. H it is quite tough uh because
AI agents can fail while the system
metrics themselves look green. So if you
for example look at this example here we
have a user support agent and the user
is asking can I get a refund. The agent
takes in the request looks up some
policies and then it's like yeah sure I
issued your refund and the user is like
thank you and it will take some days
until the user sees if it actually
worked out and the status is green.
Nothing went wrong in traditional
observability terms. There's also no
latency issues. But if we dig deeper
into what actually happened, the agent
never did refund anything. So the tool
was never called. It was never executed.
And the agent lied about doing it to the
user. And we will only know about it in
a few weeks when the user come backs and
is like, "Hey, by the way, I never get
I've never gotten my refund." And this
is the problem that we have with those
nondetermin deterministic systems. They
might tell us they do things, but they
actually don't. And this is why you have
to find an approach and a way to
continuously mine for those signals
where things are going wrong and make
sure they don't happen again or maybe
not even at all in the first place. And
this is a problem our founders also
faced three years ago when they were in
the way combinator batch and they
realized okay there's nothing like a
unit test for AI applications and we
need a solution for it. So they built
Langfuse which is by now an open source
platform to continuously trace monitor
and improve your AI systems. And while
we started out as a dev tool mostly by
now we also have domain experts as a
target group. So collaborating with AI
engineers to make sure the system does
what it actually should be doing. Uh but
also a new user group for the past
probably 8 to 12 months uh which are
coding agents that are helping our
engineers also to work with AI
applications and improve them.
Lenfus is by now adopted by more than
150,000 uh developers globally also
largely driven by our open source um
setup. Of course, 21 of the Fortune 50
have us as part of their core tech stack
when shipping AI applications. And every
month more than 90 billion observations
are ingested into uh length use
instances. Uh of course increasing
tendency as agents are taking more more
and more steps and also taking over more
and more tasks. Companies like RAMP,
Canva, Khan Academy and SUP uh work with
us and over the last three years we of
course spend a lot of time with them and
one thing we realized working with those
companies is that the ones that
successfully manage to ship reliable
agents and also continuously improve
them follow something that we call like
some form of this and the AI engineering
loop and it is about a set of practices
that help you to continuously improve
your system by taking a systematic
approach.
The foundation to this is always
tracing. Tracing is about getting all
the steps of what your agent is doing
into a more or less lock, but ideally
also in a way you can inspect it as a
human. Monitoring is about finding the
interesting ones. So what is going
wrong? What is going right? Where should
we look deeper into? But also
understanding how is it performing on
average. Building data sets is about
finding a representative set of examples
that you want your application to be
able to handle and also how you want it
to handle it and then you want to run
experiments on it. So try different
variations of your system to check um
how it is performing, how it's going and
then of course you want to evaluate how
it's going and this is not something you
do once but you continuously close this
loop and want to improve uh those AI
agents and learn from production and get
get it back into data sets. Uh but let's
dive in each of those steps a little bit
more into detail.
So for traces, the most important goal
is that you want to get deep insights
into what your agent is actually doing.
On the right side of the screen, we can
see a trace that is also a screenshot
from Lenfuse and in this case it's an IT
support agent. So an agent that is
answering questions from your parents so
you don't have to do it. And we can see
that there's first like the root trace
and we can see aggregate um time and
also uh costs of this step. But we then
also get a breakdown of each of the
individual steps that agent is taking.
So both the generations which are the
open AAI chat ones and also the tool
calls which we can see with a little
tool in front of it. So we have a
detailed view of what's going on and if
the screen would be wider we would also
see that we can see the inputs and
outputs and all the metadata involved.
This is then the foundation to track the
cost, the latency, the tokens involved,
and also have a log to inspect for you
as a human to really dig into what's
going on, but also for your coding
agents to work with it and look at it at
scale and just have this this
inspectable lock of what's actually been
going on.
Monitoring is then about making sense of
it at scale because especially now with
increasing uh automation levels, longer
traces and like a lot a lot of use
cases. It's just not feasible anymore
for you as a human to look through those
logs completely manually. But you
actually want a way to get aggregate
metrics on what's actually going on and
also uh detect signals where things are
going wrong. So for example, cost and
latency metrics, but maybe also quality
signals like our compliance guardrails
um kept true to or also like how many
users are actually frustrated with our
system. How many are writing all caps
messages because they are maybe a bit
upset with what uh the agent just did
and um yeah all of this aggregating and
then u of course also finding the
interesting stuff that you want to dig
deeper into.
what you get from production through
this monitoring is then also one of the
foundations um that you can use to build
out your data sets and data sets are in
the end a representation of what you
want your agent to handle in production.
So all the cases that it might be
getting also maybe out of scope requests
that you want to like correctly also be
deferred and make sure that like the
agent is not trying to give investment
advice or also uh answering what the
weather in New York is going to be like
if it's actually just a dead IT support
agent. And those um items you can then
have like the input but also what you
expect um it to have as the output which
can both be like a sample reply or also
expected behavior that you want to see
or keywords you want to have covered.
And this can then be used as a stable
benchmark either for like improving and
iterating offline or also as part of
your CI/CD.
Those data sets are then used to run
experiments on and experiments are um if
you maybe look back into university and
statistics or anything that you might
have done. It's in the end this idea of
varying something about your setup and
looking what happens then. So for
example, changing a prompt, changing a
model, changing the context or the tool
description and to see if it's then
better dealing what you actually what
you with what you actually wanted to
deal with and ideally isolating
concerns. So if you want to check if the
same model performs better with a
different prompt, you ideally only
change the prompt and not five other
things because otherwise it's going to
be hard for you to interpret what you
actually see.
And then finally, you need evals or
evaluation approaches to make sure you
can also measure what's happening in
those experiments because again you
don't want to look at everything
yourself. Uh which you by the way should
should probably sometimes do. Um but
still you also want the scalable
approaches which are for example LLM as
a judge. So using another LLM to check
what the LLM did. um or also code based
evals for things like um classification
tasks where you can check for an exact
match or um also checking behavior can
be a a deterministic check or if you are
checking for all caps type um things.
So this is the AI engineering loop and
what we observe with um many of our
customers is that there's depending on
your use case a few different entry
points into this. So if you're for
example in a low stakes environment and
you're only building your internal chat
agent, you might first not have a
observability tool in place at all and
then you maybe get started with tracing
and add some monitors to just check
where are people getting frustrated but
you don't care about the eval part too
much in the first place. You just build
it out over time and just like add those
test cases as you progress but you can
go to production directly. However, if
you're building a case that is customerf
facing and especially if you're building
a case that is in regulated
environments,
you probably don't want to risk the
agent doing something that it's actually
not supposed to do. So for those
regulated industries, we've seen a few
approaches emerging and the foundation
is always tracing. So you always want to
know what is actually happening, what
steps is it taking, what inputs and
outputs is it seeing and also what tools
are being called. And then on top of
this um those teams in regulated
industries found a few approaches on how
to go about building out these ground
truth data sets that you can then also
loop on improve on and also you probably
all heard about auto improvement. Um all
of this definitely needs the foundation
of a ground truth data set and you yeah
have a few approaches to get there. For
example expert curation so working with
your domain experts within the company
to make sure you're building out the
crown to data set. Then for example
shadow runs. So you run the process
continuously manually but in parallel
you also have the agent running and you
can always compare how would the agent
have handled it? How would the agent
have gone about it and then like this
measure the accuracy but also build out
your ground truth and then finally um
like we did it also in my previous
company. Run a fully human in the loop
system and over time slice the data into
parts where you are confident to
automate versus things where you always
want a human in the loop.
So, so much on the introduction. Uh, we
now want to go in a more practical
example. And for this, I'm also
welcoming Donelli again on stage and
we're going to look together into how to
trace your agent execution into length
use, how to evaluate and improve your
system, and how to continuously close
this loop.
>> Hi everybody. Like Annabelle said, I'm
Don, but you can call me Don to keep it
easier for everybody. Only my mom calls
me Don when I'm in trouble. Um, yeah,
that okay, that's great. heard a few
giggles. So, you know, nice nice
icebreaker. So, that's the first eval.
It went perfectly. Um, so now what I'm
going to show you is an example that we
built for a few financials institutions
that we're working with because they're
in the in in kind of this process of
they build their first prototype, they
build their first demo, but then the
question comes from leadership or maybe
from the teams. How do we we evaluate
this customerf facing agentic solutions
that we're building? How many of you
here are in financial services or in
finance? Yeah, we're in New York. So, of
course, you all are. Um, any other
industries others than financial
services, regulated industries like
healthcare and stuff like that? Okay,
cool. Awesome. So, I think this is going
to this going to speak to you very much.
Um, so basically what I have here is,
you know, a typical, you know, banking
assistant. Everybody, anybody of us that
has a banking services probably have
seen this in each of of your banks,
right? However, the all the stuff that
happens behind is you know very
important for the bank itself or for the
institution to provide you with very
accurate information because there is
like financial liability, there's legal
liability. There's a bunch of you know
risk for the bank itself to put out
these type of solutions when they are
powered by LLMs which as we all know are
inherently non-deterministic. So we want
to make sure that we reduce the
unpredictability and that we can then
reproduce the outcomes as much as we can
and figure out where are the failure
modes and where is the agent giving us
the results that we don't want so that
then we can you know improve upon those.
In this example I have a few things that
I I would like to show you. The first
thing is that I can impersonate, you
know, a few different type of clients
because obviously a bank is always going
to have customers that are like, you
know, your everyday Joe like myself. I
only have a couple of bucks in the bank,
but then you're going to have your ultra
high net worth individuals and all of
that. So, we can have here impersonation
of different kinds. And this is
important because we want to be able to
know if the agent is able to respect any
guard rails that we have put in place
when it comes to those type of uh
personas that we have. The other thing
is if you notice here maybe let me blow
it up. We also have PII identification
uh enabled and any sort of uh data that
is deem as PII is automatically masked
before it gets persisted into Langfuse.
Again, this is another very big
requirement for spec specifically
financials institutions that they don't
want to, you know, persist in an
observability system their credit card
information or social security numbers
or their clients. They want to keep that
on the systems of record and as much as
possible in their systems uh that they
own. So, that is also enabled and I'll
show you a couple examples on how we can
uh get that to work. And then we're also
going to see if the agent itself is
respecting some of the controls that we
have put in place and how is being
scored and if the quality gates that we
have defined are also being enforced. So
we're going to me measure all of that.
I'm going to show you a few examples and
then take you behind the scenes in the
product itself to show you how you can
set that up and then how an end toend
flow looks like. So let's say that I am,
you know, in this case I'm coming in as
Anna. I'm asking about international
wire fees. Very simple question, just a
knowledge base. And then in a few
seconds, it's going to come back and
give me the results from our knowledge
base. And here you go. You see in here,
I'm surfacing information that obviously
I wouldn't surface to a to a customer,
but I'm doing it here for the purposes
of the demo. But I'm calling out here
the tools that are being called, the the
data sources that are being called as
well and some of the details as well
that make up the configuration of this
agent when it comes to giving back this
answer. If I were to then say, okay,
look, I I lost my card. This is my
number. Is it blocked? I'm putting my
credit card number in clear text, right?
So that is obviously that's not not
great. So you want to make sure that
even though that the user you cannot
control that you cannot control what
your uses your users input in the system
you want to make sure that you catch
that whenever you are instrumenting and
whenever you are uh building your evals
so now we'll see in the trace itself
that the credit card will be indeed
redacted if I come here to langfuse and
I open my trace you'll see that now the
question is my car number is and then it
landed in LA completely redacted That is
because I have a masking function that
automatically any sort of PI information
that I have defined will be immediately
masked and then is not persisted in
plain text in my system. So just to show
you uh in terms of what a a typical
interaction looks like and I can see
from the top here this was the the
prompt that the user sent but then as
you all know behind the scenes there's a
lot of stuff going on that we don't
necessarily surface to our end users but
are critical for us as the platform
teams as the developers to understand
how the agent is is behaving performing
and the quality of the outputs as well.
I can see the entire tree of all the
steps that he took. You know, here the
the the anthropic LLM call that he made,
the tools that are available. Here it
called a list of tools. It listed the
accounts and and so forth. And these are
the outputs. But then more importantly
here on the top, I can see all the
scores that I have defined for this
particular use case. You see that
they're they're automatically calculated
whenever there's a a new interaction or
a new trace being captured by the system
and I can I can capture things if you
know down from if the information that I
gave to the customer is compliant with
banking information meaning that the
customer is asking about the weather I'm
not going to give that information it's
not compliant um if there's any sort of
failure modes um if there's any guard
rails that we're that we're blocking any
any answers that we're giving back to
the customer. One example of that is for
instance I can come someone can might
come and ask can I put my savings in
bitcoin right so that is something that
the bank itself shouldn't be providing
information about that because that is
you know that has some ramifications and
the agent you know correctly does that
but at the same time it is flagging it
as investment advice and this requires
you know for the person to either talk
to an advisor or or something else and
we are using a score to do that. And if
I go again to my trace, this is how I
see it. I have the input guard rail here
that tells me that this is the primary
risk is investment advice. And in the
score here, I can see that the intent of
the customer on this score was indeed
investment advice. So that way I can
very easily go out and filter for those
in particular. But anyways, I wanted to
show you kind of a simple flow of this.
The last one before getting into the end
to end on how you build a data set and
how you build an evaluation flow is that
the fact that we can also support
multimodal. So let's say that instead of
you having the customers writing via
chatbot they're calling your contact
center. We can come here. We can say I
want to process this call and this going
to do a speech to text and then the text
is going to be evaluated to to figure
out if there's any violation on on here
and I can come then in here it says that
the customer was asking about blocking
his card and I can indeed see the trace
here and I can even see the actual link
to the media that the customer was sent
or in terms of that audio uh or that
call that the customer made and also the
transcript and what the assistant gave
back. So that is in terms of the tracing
how can I capture all of those
activities. Now when I am trying to then
think about okay how do I then put
together or put in place a framework on
how to evaluate this interactions that
my customers are going to be sending
through my system because as we all know
customers are unpredictable. We might
design a system or a solution with a a
specific intention, but our customers
are always going to find very clever
ways to use a system in a different way.
And we also cannot anticipate every
single outcome specifically with LLM
power solutions that are going to happen
when we we release this into the wild
for customers to use. So that is when we
start relying on building our evaluation
criteria and for for us the anchor of
that is building data sets. So what is a
data set? A data set is basically and
let's go to this one that is the the
generic one. A data set is basically
your set of questions and expected
outputs that allow you to then measure
the quality of the outputs of your LLM
or AI solution. If you come from a
software development background, the way
that I like to think about this is that
these are your test cases. And I don't
think anybody here that has shipped
software into production will ship
anything without passing into QA unless
you merge into main or prod, which I'm
pretty sure most of you have done it,
but it's not a best practice. Um, I know
I know I have, but whatever. Um, but at
the same time, this is the way that you
can then have the evidence that you pass
the agent through a series of steps or
requirements that measure all the things
that you want to capture. And one thing
to note here that the expected output
doesn't necessarily need to be the
answer that the the agent is going to
give. It could also you want to measure
maybe the intent of the agent. You want
to measure what the agent is supposed to
do. If you want to measure behavior,
there are different ways that you can
measure the quality of the output. And
that is why you typically end up with
different sets of data sets to measure a
specific things or or specific areas of
quality in your agent fleet. You see
here how I have one that is like
basically red teaming my agent and
looking for prompt injection attacks and
any sort of uh attack that will allow
someone to come in and circumvent the
guardrails that we have put in place to
then provide information that they
shouldn't get. The other one I have here
is like very specifically for a use case
that I want to know which uh which cases
have been disputed and where the dis the
that dispute has not been solved. So the
point here is that I can come and and
curate a specific data sets that are
very specific to not only the use case
but also the technical requirements that
I have for that agent. This is where I
would say that not unfortunately because
I think I still think humans we are very
important. So this is where you still
need your domain experts in the loop
working with the development teams
defining what are these. There are two
main ways that you can basically create
your golden data sets. You either have a
team and I've seen variations of both.
You either have a team that already has
a spreadsheet somewhere. these are all
the things that we want to test on my
agent and just upload it and that's
pretty easy. You can come here and say
okay perfect I want to create a test
data set and then I want to upload a CSV
and you can upload the CSV and it will
exactly bring up everything that you
just had before. The other thing I like
to mention here everything that I'm
showing you can do it as well
identically through our CLI or NCP in
our APIs. It's just that I think it's
very it's better for me to show it in a
UI rather than telling claude to do it
end to end. Make no mistakes. Okay. Um
so that is that on that but then I could
also come here and say that I want to
add um you know items into my data set
for instance that are already as part of
my
production traces. So let's say that you
saw how I was already collecting a lot
of activity from my application. I can
come here and say I want to add all of
these into my data set and then select
the data set that I want to select. So
this way you can kind of dog food in a
way the data set that you're going to
use by looking at the production traces
that your agent is producing as long as
you have determined that yes these are
good examples of what I want future
outputs or traces to look like. Now an
important thing here to do is a process
that I always like to call out which is
error analysis. Right? So error analysis
is basically this idea that I want to
look at my traces and I think Annabelle
kind of talked about this uh very
eloquently as well when she was on the
other side as a user of of Langfuse that
she had to like and we were talking
earlier today. She spent like days like
literally looking at traces like that
was her job like looking at the trace
the structure what was what were the
outputs and all of that. And that is
still a very important process because
when you look at the trace you you first
start understanding how the agent is
behaving if it's taking all the steps
that you needed to take if it's calling
all the tools that it needs to call and
if it's giving you the output that you
want. That's you know very very
important. But then how do you simplify
that process? because obviously it is
not feasible for me as a human to go out
and look at thousands of traces once the
system is in production. So what we
typically do is we want to curate a
sample that is representative of our
production system on of traces for a
human expert to come look and give me
feedback. Right? It's the same as like
hey I have all this activity. I'm just
going to take 10% or 20% and I can say I
just want to focus on the ones that the
customer is talking about, you know,
disputes or credit card information,
whatever filter that you want, you can
do that. And then you can build for them
what we call an annotation queue, right?
In this annotation queue, effectively
what you're doing, you're telling a
domain expert, in this case, let's say
me, that, hey, you are the risk expert.
I need you to take a look at this output
that the agent is giving us or is giving
our clients and give me your input. And
the thing is here you want to make it
very very simple for the domain expert
because obviously they have their day
job. They cannot spend just hours
looking at this. So the the typical
things that I recommend is you can give
them like a couple scores that they can
give you, you know, yes, no, true,
false, a scale 1 to 10, whatever that
is. And then they can also come here and
give you a comment. So let's say here
failure mode, let's just say for for for
the sake of argument that in this case
is missing a citation. And then I'm
going to I'm going to put a comment.
Citation is not there. Needs to be
included
in all these cases, right? You're going
to go through this process and and look
how you know it was simple for me. It
took me what 10 seconds maybe. So let's
say I have I don't know a hundred of
these and it takes me 30 seconds each.
That is what 50 minutes. No, no, not
even. Right. I'm I'm I'm bad at math
today. But anyways, you get the idea,
right? So you you you can tell your
domain expert, hey, give me an hour of
your time. I'm going to curate a bunch
of activity for you. Just give me your
feedback. Just give me a few comments.
And now with whisper flow or something,
they can just dictate it. They don't
even need to type it. Right? So make it
very simple. The second thing that
you're going to do with this, I'm going
to mark this as completed. Now this
human annotation lives with the trace as
evidence. But then the second step that
I want to do is take all this
information, all this annotation that
they gave us and then actually use an
LLM to find all the failure modes or
categories that are patterns across all
of their comments. Right? So it there
might be you're not asking the the the
theme to invent categories. You're just
telling them, give me your unfiltered
raw commentary on these traces and then
you're going to use an LLM to then
figure out the categories because that's
what they are great at. They are great
at pattern matching. They are great at
extracting information from text. So
that way you keep it simple for the
domain expert and use LLM for what they
are great at. Now once you have all
those categories that is where we can
then get into our failure modes and
those failure modes if I come here and
look at my experiments that is what
you're going to see whenever I run an
evaluation you see all of these things
that I'm measuring against. Maybe let me
brought it up here. So now after I have
my domain expert give me the the the
inputs I extracted what are the most
common categories that appear in my
corpus of data based on my domain
expert. I can then define what are my
vectors or dimensions of you know
quality. Let's just call it we just call
it scores right but I like to come up
with fancy words to to say things. But
you see here how one of them was sites
experts expected source correctness for
formal register meaning that you know in
some languages you want to address your
customers with a more formal tone uh if
the language matches what the customer
came in with u must include non
solicited and so forth. So now that I
have that foundation of the categories
that I'm going to measure on the quality
of my outputs, then I can decide okay
cool. So now how am I going to grade
that right? What type of score is that?
What type of evaluator is that? And for
that I can either do come here and build
my kind of library of evaluators, right?
So that those as as you know traces
coming in they're automatically
calculating those scores for me but at
the same time I can have the scores
being calculated directly from the
client application whenever something
happens online in real time so that then
I can surface it back to the system. But
basically, I want to have a a way of me
measuring the outputs of the agent
across both LLM as a judge scores or
evaluators, but also deterministic
evaluators. Another lesson that we've
that we've seen working with these
clients is that the more that you can
have a mix um a balance mix that is
depending on the type of categories that
you identify between LLM as a judge
evaluators and deterministic evaluators
the better because what that's going to
do is if you rely 100% just on LLM as a
judge there's a nonzero chance that some
of the outputs are going are not going
to be accurate because that's just the
nature of the LLMs. But if you factor in
some deterministic checks that are
always going to be exactly the same for
the same inputs irrespective of what
happens, then you can have a blended
score or a blended assessment on the
quality of your agent. So that's what we
typically would like to see. And you see
here when I'm def trying to define a new
evaluator I can come and say I want it
to be a new LLM as a judge evaluator or
I want it to be a code evaluator and I
can define all the details on as to how
I'm going to evaluate that particular
agent activity. So that's that. And then
if I want to have a code evaluator, you
see this is just code. It's a function.
It's code. This is very simple. It's
just a reax. This is doing an exact
match. But this is going to give me the
same output 100% of the time. This is
not going to be well 95% or 80%. It's
always going to be 100% the same output
for the same input. So again, the lesson
here, you want to have a mix of both. So
that's on the evaluation side. So now
we've talked about like Annabelle said
and maybe let me go back here to the AI
engineering loop. So we've talked about
here building the data sets. We've we
touched on how we can then
operationalize the measurement of the
quality of those agents running
experiments. And then maybe let me go
back here. So basically an experiment is
anchored on a data set. That's my test
cases. Those are my tasks that I'm going
to run against my agent. And now I'm
going to say, you know what, this agent
is running today with this system
prompt, this model, these tools. What
happens if I change the model? What
happens if I make a change on the system
prompt? What happens if I now all of a
sudden I give it access to new tools to
access new data? So you want to be able
to kind of prototype that before, you
know, promoting into production and just
running on Vibes, which is pretty much
what all we've all been doing, right?
It's like, ah, yeah, it looks kind of
good. Let me just push it into prod. But
this is a a systematic way of you doing
that. And in a few minutes, I'll show
you how you can incorporate this as part
of your CI/CD pipeline, so you don't
have to be in the loop. So that anytime
a change hits on your agent, then a CI
job is going to kick off to run the
experiment against the data set. It's
going to evaluate your agent with a new
configuration and it's going to give you
a pass fail gate effectively across all
of the scores and evaluators that I
mentioned before. So you have a
consistent way on how you evaluate and
measure the outputs of these agents.
Make sense? Okay, perfect. So that's
experiments. That's great. So we touched
on experiments. We touched on data sets
and human annotation to bring those
humans and their expertise into the
loop. So now how do I bring it all
together? Right? If I come here and I
have my prompt this my system prompts
that I'm versioning here in Langfuse.
You can do it either here in Langfuse.
You know we don't we don't have it's
okay. We don't we don't even charge for
this. So that's fine. A lot of our
customers what they do is they have
another version in system. they have a
version in GitHub, GitLab, whatever that
is. But you should look at this as your
trigger for then kicking off the
automation to do your eval completely
automatically. So the way that this
happens is I already have defined an
automation here. And if you see the
configuration is triggering on any
prompt changes that I have here. And
then the action is it's going to launch
a CI job in my GitHub, which is this guy
right here.
Hopefully I don't I'm not get I'm not
getting the unicorn from from GitHub. So
it's this guy right here. So I have
already my CI set it up set up waiting
for any changes in the config of my
agent. Let me bring it closer here. And
then I can come and see my prompt. Let's
just see this one. I have five versions
of the prompt. You see how the prompt
has evolved over time. Version one, it
used to have this and then version two,
a slight change. Then version three, it
was, you know, we tried something
different. This is for development. Then
version four, we added more details and
also passing different parameters into
the configuration of the agent. But what
I can do now is I can say, you know
what, this is the production system
prompt that I have right now. I want to
test again with version 4 because I saw
some regressions. So I can come here and
do promote into production. And again,
I'm showing you this as a human, you
know, like a caveman like clicking
through. All of this can be done via the
API on the CLI. So you don't even have
to do this by hand. You can just call
the API and say promote this prompt
version with a production uh tag and it
will kick it off for you. I have the
production tag. I'm going to save and
promote promote to production which is
the new configuration. In a few seconds
we should have a new CI job that is
going is going to launch here that then
is going to kick off the experiment to
run my evaluation run. Okay, there you
go. Thank you GitHub. Thank you so much.
So perfect. So now I have this job that
is running automatically. So any time
that I push any changes in the config of
my agent, it's going to hit the CI. It's
going to run the eval gates to tell me
if I'm passing or failing any of the
evaluators that we have defined from
before. And then with this way, I can
have the evidence and also the assurance
if I can go into production, you know,
safely with this new configuration. if
it's actually the agent is degrading or
improving in quality or maybe even
violating any sort of guard rails that I
have put in place. That's going to run
for a few minutes, but let me show you
one that I run earlier. And to show you
the result, I can come here and see what
the output is. And it's telling me that
this was the prompt that was sent, the
version, the labels, and then it's
telling me that they gave passed, right?
So, perfect. And these are the
evaluators that I measured my agent
against. I have here the most include,
the source recall, the language match,
the correctness and not unsolicited
upsell. And I can also define minimums.
I can say this is the minimum threshold
I have for this specific score. If it
doesn't clear that bar, it's not going
to be considered as a pass uh to go into
production. Now, obviously, in this
case, I'm not crazy enough to just say,
okay, cool. So you pass, go merge it and
push into into main. I'm just letting it
sit there. But admittedly, you could
have a full end to end process that it
will just create the PR for you and it
will just wait for someone to review the
PR or maybe if you are, you know, like
like everybody's doing today, just
pushing the PR into main straight up uh
if it's clearing the bar, but at least
you have the evidence here, right? So
you're not pushing a PR just running on
vibes or just running on what you think
that the agent is good at at doing.
You're actually have the the paper trail
so to speak and the evidence on why you
make that decision for this new
configuration of the agent. Perfect. So
now I want to show you one couple more
things as an actual like use case,
right? because we've been talking a lot
about the technical aspects of of langu
and more you know organizations are
focused a lot on tokconomics right I
think 2025 in beginning 2026 everybody
was token maxing now everybody is like
token valuing or whatever they're
calling it now so everybody's like
trying to extract as much value as they
can of their tokens. So now let me show
you a couple of ways that you can then
show your bosses or your leaders or
whoever or maybe you want to build this
for your business stakeholders for them
to feel a little bit more reassured that
whatever agent solution that you're
building is actually bringing benefits
to the business. This is not just like
oh the cool thing that we're building.
Now I have here a dashboard that I'm
trying to put together a few metrics
that I can report on to the business
based on the data that I'm being
collecting from my agent. Right? The
first one is and this is where you might
argue with me in the logic behind this
but you know every organization is
different. But what I'm trying to show
here is that I've had 1,400
interactions of this agent over the last
seven days that didn't need to go to a
human agent, right? So that's great. So
that means that I'm saving, you know,
human capital from spending time to
talking to customers in in and do the
math then. How much has that cost me? It
has cost me less than $7, right? Over
the last seven days. If you take any
contact I used to be a contact center
employee back in the day 20 years ago
you know what you gonna pay that person
$15$20 an hour right so that person is
not going to handle 1400 calls in one
hour so already you're showing at least
some directional business benefit by
having this solution in place right so
that's the first thing the second thing
is you could also start pinpointing what
are the areas where your agent is
tripping
Right? If you remember, we define the
categories or the failure modes as we
call them in the industry where the
agent is not giving me the results or
the answers that I want. And these are
the ones that I'm capturing in order of
occurrence over the last seven days. You
see here that now out of scope, informal
register, and dispute not resolved are
are my top three and they've been
creeping up over time. So now, instead
of me having to go through thousands or
hundreds of thousands of traces trying
to figure out which one is the activity
from the agent that is causing the most
errors or the most trouble, I can come
here and scope it down. And I know
already that this failure mode is my top
one, the autoscope, the foremost
registered and the dispute not resolved.
So now I can come here in my tracing
and do a very simple filter and say
dispute not resolved. I can save it as a
view. So I don't even need to every time
filter it. You see how it's filtering up
top for me. And even on the side I can
come here and say dispute not resolved
equals zero. So that shows all the
instances where the customer had a
dispute or was asking for a dispute of a
product and it hasn't been resolved by
the agent. So it either had to go to a
human agent or it just lingered and the
session closed and nothing happened. But
now I can then spend my time instead of
going through thousands, I can scope it
down to maybe dozens or hundreds. And
now I can do um an investigation that is
more targeted. And now I can also find
where are the areas where my agent is
actually uh tripping itself up. So
that's that's one. The second one is
that if I want to come here in the
dashboards, I want to then be able to
say okay what are the number of times
where my customers are giving me either
thumbs up, thumbs down. I can I can
capture that as a score very easily. You
see here every time I can come here
thumbs up thumbs down and I can just
show it here in a dashboard very easy to
consume any business person any user any
human actually is going to be able to
see this and say okay most of them are
thumbs up that's cool but what about the
thumbs down let's focus on that you know
18% of them what's been happening and
then the other one is around the
security mix more in here good news most
of our interactions from the agent is
not catching any sort of risk in the
interaction that is having with the
customers. But we see here that in 89
cases over the last seven days, it
actually the customer was asking for
investment advice and the agent might
have given or might have tried to give
investment advice. So we can then go out
and focus on those. And again, same
thing. I can come here and say, let me
go back to my default view. And now I
can say instead of the numeric score, I
can come and say the categorical scores
add a condition. And then say what is
the intent or the security risk and then
the security risk, let's say investment
advice. And now I can see what are the
specific examples where investment
advice was identified as a reason for
being flagged and that the that the
agent shouldn't engage on that with the
customer. And you see here even from the
previous example um that I was showing
you. So that's kind of what I wanted to
show in terms of first the the nature of
going end to end on a solution that
you're putting customerf facing first.
Obviously, which has a lot of critical
implications in terms of liability, you
know, financial implications for and
reputational as well because you don't
want to be putting out information that
is not accurate or is hallucinated in
front of your customers and how you can
follow a systematic process so that then
you can show evidence and validate that
the outputs of these agents is actually
following the guardrails and the
controls that you have put in place. And
with that I would like to leave you with
Annabelle again so we can close and then
maybe we can take a couple of questions
at the end. Thank you.
>> So what we see some companies trying to
do or some teams trying to do is this.
Please fix my agent. Make no mistakes.
And there's probably a few things that
we can recommend less than this. Even
though your agent might be hooked up via
MCP or CLI with your data in Lenfuse or
in whichever tool you might be using. Um
this is something that we just see
producing rather slop than anything um
that is actually helping you. But of
course we're also very much in favor of
working with your coding agents to
continuously improve your applications.
Um so we wanted to share this just as a
picture how you can maybe memorize it.
So we have two of those a here. We have
one uh being the time invest. So, a lot
of time spent or very little time spent
and then also a low quality system or a
high quality system and
you don't want to be down there. If you
fully automate it and just let your
agent go for it and just be like fix
everything, do it for me. Um, this is
not going to turn out well. You will end
up with low quality and yes, you don't
have to do anything, but also your
customers will not be super satisfied.
At the same time, you also don't want to
go go the full manual way anymore. You
don't want to instrument your app
yourself anymore. This is something that
can be automated. You don't want to
catch all the failure modes yourself and
re review all the data yourself. This
can be automated. Um but at the same
time, for some things, you should get
your taste in. You should get your
domain experts in the room to build out
the data sets to curate what is actually
um what actually is the problem that
your application should be solving and
in which direction you want it to go.
And for this um you want to land
somewhere here. So where the ideal
balance is between like um you reviewing
data, bringing in your taste, bringing
in your domain expertise, but also
working with your coding agent for all
the things that you can automate like
instrumenting it, finding failure modes,
running the evals, maybe making also 20
experiments instead of only one um that
you would come up with and yeah, just
like avoid getting down there in the
left uh down corner, but try to be the
the tasteful AI engineer that is
bringing in the taste, making sure the
the emails are great and then you can
also more and more automate this loop
over time.
If we were you and we would have to get
started tomorrow, h this is what we
would be doing. We would install the
lenuse skill which is a yeah it's an
agent skill. So it's a set of markdown
files that is helping your coding agent
to wrap its head around how to work with
lenfuse and how to implement those best
practices. It is hooked up with our
documentation with all our integration
pages. um it is hooked up with our
academy where we ingrain the best
practices around data sets and how to
instrument and how to write evaluators
and all of this. So it's a a great
starting point um to do the things uh
automatically um that you should be
doing automatically but also to maybe
curate a set um of data that you should
look manually at. uh you should then
start to collect um also ground truth
that you can evaluate your agent against
maybe from historical data also from uh
production or from some samples that
you're running with your domain experts
and if you're in a regulated space uh
define your hard limits in a way to make
sure these are the things that
definitely shouldn't happen for
financial services for example it should
never give investment advice so make
sure that you're ingraining this also in
your evaluation set um that ideally
never happening but at least you will
know about it um when it's going to
happen
and we have a few resources for you. So
the repository Donelli showed you and
used um is also available online. Uh you
can check it out yourself. You can take
everything that you want from it and
also use it for your own use cases. It's
of course fictional data and not um not
something that actually um was taken
from our customers and I think also this
session will be recorded so you can take
a look again. uh we then also recommend
the langu academy which is like a larger
writeup of uh how to go about AI
engineering um the whole steps um
described again and we also have a
self-s serve workshop that is basically
guiding you through all the steps so you
understood it once and then um yeah can
go ahead with your own application
there's some opportunities to bump into
us over the next days uh one is um
Donelli is giving a talk also on
building deployment gates for AI agents
on Wednesday so Check it out if you want
to understand how you can make sure uh
that AI models that go to production are
actually um clearing quality gates. Uh
we're also having a booth, a booth 9. Um
I haven't checked out where it is, but
I'm sure you will find it. Um you can
meet the team there, but also you can
get custom stickers. So you take a
picture of your face and then it AI
generates stickers of your face and
length use with a maybe some jokes also
included. Um and you can take them home
and sticker it on everything you have.
And then finally, we also have a
community run. So if you want to step
out the conference center and meet the
team, we also have two of our founders
here um and a few more team members and
we're all big runners. So we thought we
just might invite everyone else as well
to join us um for this. So yeah, please
come for this one as well. And we're
super happy to use the remaining minutes
for any kind of questions. They also
have some non-custom stickers here. It's
just a lengthy sticker, but I think it's
still pretty cool. So if you want some,
you can come up uh and get them. We're
happy to take any questions. and ple
please meet us and don't be a stranger.
I'm handing this to Delli.
>> Yeah. Well, the Langfuse per se has a
hard dependency for their stores with
click house. Um that is just because you
know in the evolution of the product it
started with Postgress. Uh but then
Postgress couldn't handle the scale that
we achieved and like billions of
billions of events per day. That's when
we moved over to Clickhouse. So in terms
of that data plane yes in clickout so
but maybe the followup for you what is
the need for you in terms of that data
stores because we also offer the ability
for you to export the data you can
export it to S3 you can use the a yeah
you can use the API the CLI or the MCP
if you want to consume the data from
langfuse so it's totally up to you yeah
>> I want to host it on
>> yeah you you can host it 100% on Amazon
um it's you know we have a self-hosted
deployment as well um you can either use
our cloud offering that is fully SAS
turnkey you don't need to do anything it
runs on Amazon but if you want to run
the infra yourself because you have I
don't know some you know EC2 instances
lying around there you want to use we
also have a deployment model for that
and it comes prepackaged with all the
components
>> yeah super important question so the
question was about interator reliability
um and also probably just consistency of
LLM as a judge evaluators to make sure
it's actually catching um what you want
it to catch um there's actually also
part of this language skill is handling
this as well and helping you to um h
there's a term for it. Um it fell out of
my head but it's in the end about the
process of making sure the LLM is
judging like a human would judge and uh
what you do basically is you judge a
sample um ideally a representative
sample yourself and then you run your
LLM as a judge and you then optimize for
the LLM as a judge being coherent with
what your human human raiders do and
ideally you have like a few human
raiders and that's academic approach to
it. So probably the practical approach
to it is have one human label some data
and then optimize against this ground
truth and then ideally you just check it
over time to make sure your set stays
representative and especially if you are
using it for um running on production
data it's in the end ideally you just
start with having a a few too many false
positives so you catch a little more
than necessary but don't miss anything
and then you just tune it down over
time.
