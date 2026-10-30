# How to Write Your First AI Eval - SallyAnn DeLucia, Arize AI

Source: https://www.youtube.com/watch?v=gv4w23xYj-0

Uploaded: 2026-10-25

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Um, before we get started, I just wanted
to introduce myself. I'm Sally Ann, and
I'm head of product at Arize. Uh, been
at Arize for like 4 years now. Um, one
of the first projects that I owned
actually was building our AI agent Alex
into our platform. So, I've been dealing
evals for a little while now, and uh,
even building a lot of our evals
product. And so, I think the way that I
think about evals is that they're our
primary signal for our agents. Um, and
that includes all of our evals at Arize.
So, my goal today is you'll leave with
three things.
Um, a clear definition of what an eval
is and what it isn't. Uh, being able to
write your own criteria. So, I'm
hopefully going to be able to provide
you with like a little bit of a recipe
uh, for how you can think about evals
and how you can apply that for any of
your real agent scenarios. And then
we're actually going to build a working
judge in Arize. Um, and I'll show you a
little bit about the life cycle there
and how you can think about improving
your evals over time.
So, this is a bit of our agenda. So,
again, I'm going to give you a little
bit of context. I don't want to spend
too much time in slides, but I want to
make sure everyone has a really solid
foundation for what an eval is and how
you should think about it. Um, we're
going to explore some data in Arize
together, um, write our criteria, and
then we'll actually go build our eval.
That's the main part of our workshop
today.
Um, and then I'll give you a little bit
of like where you could take this for
what's next. Um, I love it to kind of
have some like working sessions so
people can collaborate together. I'll
try to like walk around the room, help
folks out. Um, and then I will show kind
of like a one-pager that's in Notion
that you can kind of open and follow
along as well.
So, just check the room a little bit.
Who here has either like shipped a
chatbot or an agent, ever written an
eval, or even just opened the Arize
product today? Anyone here?
All right, we got a a few folks here.
So, I think this is going to be great
for folks who maybe haven't done any of
this and even if you have, I think today
should still be pretty helpful.
So, going to start off the context with
like why I don't think vibe checks
actually scale. So, this is the vibes
problem as I see it.
You know, you have Monday, you maybe
change something to your prompt, you
ship it. It overall feels better. You
don't really have a way to know, but
overall things are looking good.
You know, Tuesday ship it, a week later
now that use case that you shipped a fix
for is broken.
And then next week, as the problem
continues to get worse and worse,
there's no way for anybody to prove
whether something was fixed or that it's
actually failing. have vibes to go off
of.
What you can't do without evals is you
can't detect regressions when you change
a prompt.
You can't objectively compare prompt or
even different model versions. You don't
know if a new model is any better for
your use case and you can't actually put
any official quality gates into CI as
you're shipping your agent. So, without
evals it's you can imagine it's it's
pretty hard
to actually know how your agent is
performing.
A question I commonly get is is an eval
just a unit test?
I think that there's a lot of comparison
of AI evals to like kind of traditional
software tests and I do think that
they're a little bit different. Cuz
first off, with a test you kind of just
have like one input and there's one
correct output. You can also read all of
the logic in the code. With an AI agent,
you actually cannot read any of that
logic. That actually comes out after in
the form of traces.
And so, you kind of need to have this AI
eval where you can look at like the
day-by-day itinerary in this travel
planner example I have here,
the budget breakdown or multiple
criteria basically. So, there's these
many valid outputs that you just can't
have, you know, a more traditional unit
test on like you can with software.
So, basically how I like to think about
this is traces are the logs for AI Um,
evals are actual tests. And I always say
that uh uh I used to have a meme, I
didn't include it today, but the hard
pill is you kind of need traces, you
need observability to actually do your
evals.
So,
this is an example here for why agents
make this harder. So, this is just a
sample example of what like a trace
could look like. And for anybody in the
room who's maybe not familiar with what
a trace is, um essentially it is all of
the steps that an AI agent took to be
able to get an answer back to a
response. So, a user says something and
then what I'm showing here in all of
those spans is all the individual steps
the agent took uh to get that answer.
So, in this example, there's like a
research agent that's going to go
perform some research, uh maybe even do
like some tool calls there. You have,
you know, your local agent that's maybe
retrieving something from a knowledge
base. So, lots of back and forth are
happening. And this is where I mean you
can see the logic of your agent. Um, and
we're going to explore some traces in
the Arize UI just a little bit. Um, so
you can see there's lots of LM calls,
lots of things composed together. And
so, you can imagine just having one
single unit test like in software not
really going to accurately capture all
the complexity that's in an agent and be
able to tell us how it's performing.
There's actually lots of different types
of evals. Today, we're going to focus on
LM as a judge. Um, LM as a judge is
where we take a secondary LLM and we ask
it to grade some aspect of our agent.
Um, and so, there can be things like QA,
summarization,
relevance, and then you get a label and
an explanation out of that. Explanations
are really helpful. Explanations are
kind of like the the reasoning or the
thinking behind providing a label. It
gives you a little bit of understanding
and not just have to take a label at
face value. But, there's lots of
different types of evals. I want to call
out decision models. Uh this is
something that's pretty new. Uh if
anybody kind of took or was a part of
the the Jevas a Job storm that happened
about 2 weeks ago and OpenAI just last
week released their decision model API.
So, I think decision models are going to
be a huge part of evals in the future.
Um, those are pretty cheap and fast and
it's uh more like a question answer and
you just get like a probability and an
output whether it's like a true or false
or a label. So, you don't get that
explanation that you get with Elements
of AI Judge.
The other type of eval is code. Uh,
these are really great for any
deterministic tests. So, maybe you have
some eval criteria that's like checking
if a word is in an output or making sure
that something's in JSON. Uh, that's
going to be really great for code-based
evals. There's also things like Rouge
and Blue scores that are popular code
evals.
Um, annotations I do see as a form of
evaluation. This is where we're having
uh you know, golden truths on golden
datasets. Um, sometimes they're
synthetic as well. Um, agent as a judge
is a newer type of eval that we've seen
maybe over the last 6 months.
Um, that's where we're going to take a
full agent and evaluate something in a
different agent. I think this is really
good for super complex um like success
criteria. Um, then we have user feedback
and business metrics and those three at
the end are going to be more for your
production use cases. But, you'll notice
the first four are something that you
want to use across your life cycle in
development and production. Um, and
that's pretty important because you want
this to be able to evolve with your use
case and you don't want to like put a
lot of investment in something you're
using in development and just throw it
away. Those evals can grow with you over
time and it gives you that consistent um
performance.
All right, let's go ahead and look a
little bit at the data. Um, so we're
going to pause here on this slide give
everyone a few minutes to go and get
started. That QR code is going to be for
the one-pager which has all of the
instructions for our workshop today.
Um, but I want everyone here to go ahead
to go to you know, app.arise.com.
Uh, we want to log into AX. So, if you
don't have an account um
encourage you to make a free um account
today. Um, and then I'll go over the
steps from there in just a second. Um,
and for anybody who already I guess
might have an arise account, the next
step is going to be getting an API key
from um a model provider. So, I'll pause
there uh walk around make sure nobody
has any issues logging into the
platform.
The question was, can you do you have to
use like can you use a custom endpoint?
Do you have to use a a common provider
for step two?
No, feel free to set up whatever LLM
provider you want. We'll just want
something that we can make LLM calls to
so we can test our eval out. But yeah,
step two basically go to your Anthropic
console, your OpenAI console, whatever
provider of your choosing.
You can find your AI providers under
settings in the product and we're just
going to want to go ahead and add that
API key in. So, let me go to my laptop
here
and show you all a little bit of how to
do this.
So,
settings here in the nav.
You're going to go click into that
and then under your account settings,
let me try to
Cool.
You're going to come to AI providers.
And you can see here we have a whole
bunch of different providers. So, just
choose one
that is your favorite to use, Anthropic,
OpenAI, Gemini, doesn't matter. Just
something that we can use to make API
calls with.
And I encourage you to use the test
integration button when you're doing
that just so we can make sure we have a
working API key.
Yeah, for for folks
you'll find the demo project. Sorry,
I'll go back. Just trying to make sure
everyone has time to to catch up, but
you can access the demo project that
we're going to use in one of two ways.
The first is on from this when you go to
this tracing page here, you'll see see
demo project.
I have the LLM agent. I know some folks
might have our older demo model there.
Does not matter which one you have, you
should be able to do our exercise today.
So,
we just want to be able to look at some
traces.
And you know, you can expand the time if
you want to see a little bit more data
there, but
give everyone a few more minutes cuz I
only saw a handful of hands that got the
AI provider. and to see what I can do to
see if I can get
one that we can share really quickly,
too.
All right, so if you have that travel
agent demo project opened,
this is a travel planning agent. It
takes a request from a user and then can
it make follow-up questions, call tools,
and basically returns a plan.
What I think good looks like in product
terms is it answers the follow-up
questions the user asked for and
respects the trip's days and budget. So,
this is generally what a user request
looks like. You can see the destination,
how long they want to go, what their
budget is, and what their kind of
general travel style looks like.
And that's an example of what we might
see from a user who goes to this travel
agent.
So, I'd love for everyone to take a a
few minutes. We want to look at the
traces. We kind of want to just take
inventory. What are users asking for?
What did the agent tool do? What tools,
what are the answers?
And then just kind of make note, was
this an answer that you would share? So,
just want to kind of explore the data
and get familiar with it.
As yeah, open one or two traces
and maybe start thinking a little bit
about what you'd want to measure as
you're you're looking through the data
here. So, as an example, let me hop on
over to the product. I explained mine to
last day.
Let's go ahead and take a look at one of
these traces. So,
you can see here,
this destination is for Prague, Czech
Republic, for 3 days, $800 budget. The
user asked for an option that feels more
local, less touristy.
We have some kind of our ideas here and
then we can start to view the plan that
the the trip planning agent created. So,
you have a detailed day one, day two,
day three. And if you want to see any
additional, you know, attributes, any
additional data that we have, you can
see that in attributes. And so, a little
bit of
how to navigate our product here. So,
again, this is the trace tree. This is
every individual step. If you want to
see the data that was passed in for a
step, like for example, we want to see
the data that went into OpenAI to
process our request, we can switch to
that span
and then look at the input and output.
So, we're going to get to this in a
little while, but we want to pay
attention to where the data lives
and what data we think might be needed
to do any of our evals. So, we'll spend
a few minutes here just exploring and
seeing what kind of insights we find.
Getting some questions about where to
find the actual data here, so let me
just show that one more time.
A lot of times in the new spaces it can
be a little hidden, but
didn't want folks to spend too much time
tracing today when we're here to talk
about evals. So, you'll just want to
click the traces
option on the nav here. This will kind
of prompt you to get started with the
rise, but we're just going to go to
see demo project and then
you can see it in recently viewed from
there.
And you can always expand the time to
see a little bit more data there.
Has everyone generally had time to like
find the project, take a a quick look?
See if you had nods, we'll give
I know.
Like fix that.
All right. So,
basically what I want folks to do now
before we get into the the next part of
of this,
is just like look at the agent and think
about how you would measure this agent
or success for this agent. Think of
yourself as the product person,
engineer, any real stakeholder of this
project and look at the traces, look at
how users are interacting with it, how
it's responding, and start making kind
of like mental note of what the things
are that you would measure. In the next
part of the workshop, we're actually
going to start defining what that
criteria would be, but high-level as
you're going through, think about some
of those things that you would measure.
Yes, so the question was like how we
should think about reading a a trace
here. So,
again for for anyone who may be just not
familiar, a trace is essentially a
collection of all the steps an agent
took to answer a user's question. So,
let's go ahead and open this one here.
So, at the top we call that our root
span.
Like the technical definition of that is
parent ID equals null. This means that
this span here doesn't have anything
ahead of it. It just sits at the top.
And this is usually where the input and
final output live.
And then from there we have our
individual spans. So, each of these is
what we call a span. I like to think of
it as a unit of work. So, let's take a
look at this first collection of spans
here. So, from the root span the first
thing that this agent did
along with calling some other agents it
looks like called the research agent.
So, this is a what we call a multi-agent
system where there's multiple agents
doing different tasks on behalf of the
bigger agent. So, in this first one we
have the research agent and that is
going to go ahead and call a tool. So,
each of these has like a type you can
see it different icons. This is an agent
span. This is a tool span. Tool span
that's going to be for getting external
data. So, you can imagine like in this
one research
there's some essential info that we have
to grab like things like weather or
sites or adequate things like that.
And then from there we're going to use
an LLM. You can see here all of the
inputs and outputs that actually went
into the LLM. So, this is your concise
travel agent.
And this is using that information from
that tool
to actually summarize that we can use it
in a later step here. And so you can
just go down the trace tree just like
that like one step at a time.
You can see how they all connect but
each of these is going to be doing a
step or unit of work so that it can go
ahead and answer. So, again the goal of
this application is to look at a user's
request for a trip and plan it for them.
Give them an itinerary of things that
they can do,
places they can stay all in accordance
with their kind of preferences.
And so each of these spans is the units
that were done to ultimately get this
final
kind of itinerary. Any questions on
that? Happy to answer some questions
about tracing while we're we're going
through this.
>> Yeah, so the question is is like there's
two LLM spans.
>> Yeah, so sometimes it's I'll go back and
look at the exact trace of what happened
there.
Sometimes it's instrumentation of
showing the the different like
the
LLM like choosing the tool to use and
then actually like passing that
information to the tool. So let's go
ahead and take a look at what happened
here.
And some of this is just kind of part of
instrumentation here.
So this looks like here
this way and I think the first LLM call
chose the tool and then I think in this
second LLM call
that's where the actual data of the tool
was passed to the LLM to summarize. So
here
it's kind of hard sometimes you have to
go down the trace to come back up. So
this LLM span chose this tool and then
this LLM span summarized the output of
the tool. So that tool went and grabbed
that like temperature data, destination
data and then the second LLM basically
summarized it so that we can do kind of
further work with it.
Yeah, great question. So the question
for for everyone in case they couldn't
hear it is is that kind of root node
making all of the decisions
or is there some flexibility with how
that works? And there's a lot of
flexibility. It comes down to what your
agent kind of infrastructure is. So you
can have what's known as kind of like a
supervisor or an orchestrating agent and
a lot of times that will make a plan for
the sub agents to follow
and then sometimes it's just passed kind
of to an LLM with a set of tools and
each step is goes like one by one. So
depends a little bit about like what
framework you're using, what your infra
looks like and the general architecture
of your agent.
In this case here this is a link graph
agent I believe. So we're not doing any
like supervisor architecture really.
Just we have a a few like modular agents
that are responsible for different
tasks.
Great question. The question was like
what strategic frameworks we support
with arise. We're agnostic to
frameworks. We have a bunch of what we
call auto instrumenters available
through our tracing package open
inference.
We don't have a preference of which
framework we want to use. Our goal is to
be really flexible and provide you with
really good observability and evals on
top of it. So
I can link our docs
where you can see all the different
frameworks that are supported.
Okay.
Let's keep going a little bit here.
Sounds like everyone had some time to
take a look at the traces, get
themselves familiar with the data here
and hopefully was able to spot some
things that they would measure
for the success. So
the first step of defining what your
eval is is defining what good means.
This is sometimes tricky for folks to
do. So I've kind of have this
little trick here for vague versus
concrete criteria.
I generally like to just write down what
good means but with really specific
criteria. So instead of just being like
helpful, accurate, good response,
you want to get a little bit more
specific. So answer that follows the
user's follow-ups,
matches the requested number of days,
keeps totals within the stated budget.
For this application those are all
really concrete criteria
for what success looks like. And I
encourage you you know if you're ever
building this for your application, you
know, sit down and and kind of think
about what that criteria is.
Another helpful hint that I have is
judge one quality
per eval. There's some exceptions to
this. I like to point out that for
especially the decision models
and agent as a judge, you can really get
away with you know doing multiple
criteria in one. But for LM as a judge,
there's lots of research that shows that
it really only does well with handling
one criteria at a time. So I think it's
good practice to just think of one of
them and then add more evals over time.
Building evals sets iterative thing. You
don't just build your evals and then
like set it and forget and you're set
for the life of the application. You
kind of have to iterate and so
um you know, when we're defining like
what success looks like, I usually write
down a handful
um and then kind of start to build those
and then over time we can add more and
more.
Um I mentioned I worked on Alex, our AI
agent um that lives in Arize and when I
first built evals, I had a very simple
set. It was like QA correctness. I think
I had some like user frustration, and of
course like jailbreak toxicity, those
types of safety evals.
Um and now we have 32 evals that run um
on Alex. So you can see how you want to
start with something small um and then
as your application gets usage, you can
ground that in real production data and
then evolve your evals to see what else
you might need to define success.
I see some questions over there.
Yeah, so the question for the the group
is is a generic eval better than a more
specific one?
I think it really depends. I think
generally speaking, I say building a
specific eval for your use case is
better. But what I would say is an eval
is better than no eval at all. So a lot
of folks like at Arize, for example,
when they're getting started, we have an
eval hub with a bunch of out-of-the-box
templates in it and they're really great
for starting. We have things like QA
correctness, hallucination,
uh session coherence, all sorts of
different evals and I think they're
great for getting started, but the the
key is and we'll go through this a
little bit today, is to kind of align
that to your use case um and then create
more specific ones over time. So I think
basic ones and reusing them, especially
across an org, are great because it's
better to have some evals, but then just
make them more specific.
All right, so start with one, add more
evals later.
Um I think in pairs or whoever the group
of around you, um I would like to kind
of have y'all jot down some ideas.
Um basically, there is six things we
want to write down. This is going to be
really helpful for us actually building
our eval.
Um so first, it's going to be the task.
Like what do you want this eval
uh to be going off of, uh what success
looks like, what failure looks like,
um,
what they're judging, like what the
evals are actually supposed to judge
here in this evaluation, and then, you
know, basically three bullets on what
pass would look like, um, and what fail
looks like. And remember from this slide
over here, the more specific and
concrete you can be, the better your
eval will be. So, we're going to use all
of this, uh, all these notes that you're
writing to actually build our eval in
the next step. So, the more specific we
can be, um, the better. And so, yeah, I
think it's a great opportunity to kind
of chat with folks around you, see what
you're thinking, what they noticed in
the traces, and I'll walk around and let
me know if you have any questions.
I got a question over here that was
like, um, the the way that the data
looks on the trace for this application
is pretty specific. It has all like the
request info.
Um, and the question was like, does that
come out of the box, or do I have to
like build that specific to my use case,
right? That was the just guy, make sure.
Um, and the question is is with our
out-of-the-box instrumentation, we kind
of abstract kind of all of the tracing
best practices for you. So, there's a
lot of common attributes that we send
in. So, things like input down value, or
the input messages that we send to the
LLM, that's pretty standard, but what
you can do is called, um, you know,
manual instrumentation or hybrid, which
allows you to customize. So, uh, tracing
is really flexible. We want to make sure
it's tailored and you get the
information you need for your use case,
but we try to make it easy at the same
time. Um, and if you have, um, you know,
your own applications that you want to
trace, on that kind of starter page was
our like MPX evals, that call brings in
all of our skills, uh, which is the best
way to do tracing these days. Let your
agent figure out how to instrument it,
and you can kind of nudge it along. So,
highly recommend that if you're going to
send in your own traces, uh, to evaluate
later.
All right. I'm just going to click to
the next slide to show you an example of
what this could look like, and then I
know there were some questions over here
that I'm going to come to.
So, just going to show an example, um,
here of like what your criteria you
generally want it to look like.
Um, so, this is like the task that we
want to judge. User sends a follow-up
about their trip. Uh, the success is
answers the follow-up directly using the
trip's details. Failures is falls back
to a generic budget. And you can see
here, this is the pass and fail. Some
folks asked me like why we want to have
the bullets and why the one-liner's not
enough and uh, the reason for that is
basically we're going to use this to
write um, our LLM prompt to do our LLM
as a judge. So we want to be really
specific so the LLM
um, can understand. The way that I like
to think about this is describing to
like a coworker or, you know, a
stakeholder like what success looks
like. You almost want to treat this
criteria uh, creation the same. So I'm
going to answer a few more questions and
then we're going to move on to the next
step. Uh, for folks who want to get a
little bit ahead of that, um,
you can this is just describing make
sure that um, if you have too much in
your criteria, you can cut it back, but
I think for the sake of time I'm going
to move here. Um,
we want to go ahead and start building
our eval. The first step is you're going
to want to go to those traces. Let me go
there now and you're going to want to
select a few
um, traces to actually add to your data
set.
Um, so for example, say you wanted to
just go ahead and evaluate the input
versus the itinerary. Like does the
itinerary have the general input? You
would want to save all of these root
spans to a data set. Um, if you've
decided you wanted to maybe test the
tool call and see if the tool call
returns um, the right information that
it was supposed to, you would want to
add in all of these tools uh, calls to
your data set. Um, we have filters here.
It's the best way to identify data. Um,
so one really great example, if it's
like root spans, you could do just
parent ID equals null or go off of the
default traces. Um, and if you wanted to
do like a tool call for example that um,
I think it was the essential tool,
you could also filter by name that way.
Um, and then you would just want to grab
these or go from the span view to, you
know, select those and add to a new data
set. So um, that's kind of the the next
step and then we're going to head on
over
um, to our playground to actually build
and test our eval. So,
folks can head over there
while I answer some questions. And let
me know if there any that come up for
adding to the data set and how you
should think about filtering. I want to
show some folks kind of the next steps
here for time cuz I know we don't have
that much left here.
So, everybody hopefully has been able to
go through, write their criteria,
identify some spans for what they're
building. And then this is essentially
kind of the first pass is what you
probably saw,
which I'm going to do now live for
everyone to kind of follow along with.
But we wanted to filter the spans you're
judging. That's what we just walked
through. So, look through the traces,
identify what span you need to evaluate,
build your filter, add those to a data
set.
And now what we're going to do is go
into our prompt playground. That's my
favorite place to go to actually test
out our prompts here. So, you can go to
the playground. I already have one set
up, but I'm going to go ahead and create
a new one. We have two types of
playgrounds
in our product. We're going to use the
prompt playground. That's great for
testing eval prompts or you know any LLM
prompts for your agent. We do also have
an agent playground. That's for testing
kind of your agent end to end here. So,
not so relevant for today.
So, just give it a name. I'm going to do
AI engine evals.
And then we can go ahead and create it.
So,
if you were in our eval hub,
you were over here and you created
an eval, you kind of have a slide over
that looks like this.
You can go ahead in the playground, just
add that from the drop down here. So,
you'll see your eval
pop up here. For anybody who's just
starting the eval process, we're just
going to do blank eval. And you can
actually just start writing your
template here.
So, what you're going to basically do is
take all that criteria and turn that
into a prompt. A lot of it should be
like paste. You can paste in those like
bullets that you had as criteria, but um
um a lot of times you want to first give
it kind of an intro, like you aren't
eval agent or an eval LLM uh looking at
the output accuracy for your
application. Let me actually just
load this one in. Okay, perfect. Um so,
I like to start my evals with an example
of what the LLM is supposed to do. I I
always kind of center it in its job.
You're evaluating whether an assistant's
output actually accurately captures the
details requested
um or input in the or provided in the
input. Um you then want to provide the
data. So, this is really important. When
we're looking at those traces, there's
probably uh attributes
that you want to identify. You don't
really need to worry about writing the
specific names in your eval prompt. We
do something called variable mapping
um that allows you to connect it to your
exact data. Uh the benefit of that is
that your evals can be flexible. Like,
if you've running on a data set calls it
one thing, and then your traces call it
something different, rather than you
need to update every eval, you can just
update the task where it's being used.
So, don't worry too much about the name
of the variable.
Um and then this is an example of what I
have written for mine.
Um these are the check-in particulars.
Those are things like those three bullet
points for pass and fail.
Um and then here I have mark only
correct if, you know, the output is
consistent with the input, incorrect if
there's a wrong destination, property
type, whatever it is, that's going to be
incorrect. Um and under params here,
you'll see if you set it up in the task,
that's where we have the labels. This
one here is just correct or incorrect,
but you can have, you know, a
multi-label problem. Maybe you do
correct, incorrect, partially correct. I
have use cases in Alex where it's
actually relevant to me to know when
something is somewhat correct, but not
fully.
Um you can also do things like not
applicable.
Um so, lots of flexibility. The eval
will return only one label, um
and then you have some things here
around the optimization direction, which
says like is good or is
correct the good thing or is a lower
score a good thing and then
explanations. Again, those are kind of
the reasoning for why the template
or by the eval gave a certain response.
And then what you're going to want to do
is load in your data set. So those spans
that you created and saved your data
set, you can load them in. And now what
we're in the spot to do is actually
start testing our eval.
We have all those inputs and outputs
that are here.
If you need to map them to different
variables, mine happen to be the same,
but you can do that here.
And so now what you can do is actually
start to run. I'm going to run with 41
mini, that seems good to me.
And we'll actually start to see the
output of our eval right here in the
playground. And this is a great spot to
just start iterating on your eval
template. Look at the response, you
know, kind of see if there's something
that you agree with or disagree and then
you can adjust the prompt and then
continue to run it over time. So that's
going to be what we do for the next
little bit here is try to get to a
template in a good spot.
And then what you can do is save that
off
here in this little button here, save
evaluator, and then that will be
available to use across the platform for
either our demo project
or for any application that you build
and bring into our eyes after. So
I'm going to walk around, help some
folks write their templates and then I
have just, you know, one or two slides
here to to close us out. I did want to
kind of point out that we do have some
tools to help you. I had everybody write
out their criteria and write their eval
and test it, but we do have Alex in the
platform
that can help you with that. So I
definitely recommend helping or having
Alex help you, especially after you've
done kind of your initial eval pass. It
can actually run the playground for you,
look at the results, update the prompt
and repeat. So that's really helpful for
when you're writing evals.
Um
pulling out a little bit of the the
remainder of the loop here. So we spent
a lot of time on the second loop our
second step today,
um where you instrument, you write your
eval,
um but then what the rest of the loop
looks like is we have things like
signal. That's our managed agent in the
platform that is able to look at your
traces, find issues for you, even make
fixes.
Um so this becomes signal that our
managed agents can then consume and
ultimately help improve your
application.
Um these are some things I think good
teams do next, alignment. Um alignment
is going to be the process of like
annotating all of those examples that we
added to our data set, and then going to
run that eval and seeing if
um it matches the human feedback. Um
online evals will be essentially us
putting that into a task and have it
running continuously over our traces. So
what that means in our eyes, every time
you send in a trace, we'll evaluate it
according to all your evals, and then
that automatically gets posted, and then
you can use that to actually monitor
your application.
Um a key everybody to walk away here
with is that every stakeholder evaluates
the agent. This is not just one kind of
role's job. You really want to get
everybody in the room who has some kind
of stake in the agent and have them
basically define what success looks like
according to their outcomes. So uh
product, eng, support, um experts, um
security, those are all folks. And then
um the key differences between like an
metric and an eval is like a metric
tells you that something might be
broken, but evals tell you what the
actual failure mode is. So you really
want to use both there.
Um and then I think what might be fun to
try next is we do have all these new
decision judges. Um and so I think it's
always interesting to take your elements
as a judge, you know, convert it to a
decision judge question, um and then
maybe compare the performance there, uh
see which one might be better. Um and
yeah.
And then again, start small, 20 traces
maybe, one dimension, one judge, you
know, read the explanations, iterate
over it, and then you can expand to more
and more evals.
Um and just some resources, we have some
docs, um, evaluate your LLM as a judge,
your judge docs. Uh, we do have some
deep dives on like the decision model
benchmarking. So, I think somebody had a
question of like, when should I use LLM
as a judge, when should I use judge? I
think that's a really great use uh, case
and uh, yeah, I'll be hanging out for
the rest of the day. Arize has a booth
in the expo starting at I believe 4:00
today. So, if you want to learn more
about evals, see a little bit more of
our product, definitely come find us.
Um, and if there are any questions,
um, happy to answer them and thanks so
much for joining me today.
