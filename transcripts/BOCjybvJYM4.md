# Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse

Source: https://www.youtube.com/watch?v=BOCjybvJYM4

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Hello everyone. Welcome to the workshop
on continuously improving agents with
Langfuse. Um you can already go to
lenuse.com/workshop.
There are steps there that we will go
over today and that way you can also
later at home when you want to revisit
it go over it yourself and there are
also some extra steps that we won't
cover today that you can find then as
well we'll show this QR code later in
the presentation uh again so
continuously improving agents
what does it mean we will be talking a
lot about um different processes that
teams use to then uh to improve their
agents or to detect changes and improve
their agents in different ways and you
can change these together into a
continuous loop and as we know in San
Francisco we really like loops and so
this process and this set of these set
of processes together you can it's also
often called AI engineering
so what is AI engineering and why do we
need it and how is it different from
traditional engineering the main
difference is that AI agents are not
deter deterministic. So your system your
status of your system can look healthy
while the responses or the actions your
agent is taking are wrong. Sometimes
it's actually wrong. Sometimes it's also
not qualitative enough.
And so um this is what AI engineering
solves. For the people who are not
familiar, um, Langfuse offers a platform
to actually execute on these processes
and, uh, we are open source, model
agnostic, framework agnostic, so you can
actually use us with whatever setup you
already have.
There are some large companies that
already use day-to-day, but we also have
a large community of smaller individual
users who really help us because they're
working on many different setups and
agent projects. And this is definitely
one of the um ways we keep up to date
with where this very fastm moving field
is going. By the way, uh this workshop
is given by Annabelle and me today and
Mark, our founder, is also somewhere in
the room and there he is. And we will
also be walking around to help you um
during the workshop if you need
anything.
So AI engineering um we like to show or
visualize the set of processes that that
people do in this graph. Uh this is what
we call the AI engineering loop. The
exact setup depends a bit on the setup
also of companies. Um it depends on
different needs but high level you can
categorize them in these five steps. And
the main thing here to um remember is we
have two big parts. We have an online
part tracing and monitoring and an
offline part building data sets
experimenting and evaluating
not in production and
we are today mainly going to focus on
the online part here tracing and
monitoring. So tracing you instrument
your application you deploy your app to
production and you will see traces
coming in of what your agent is doing
how it's interacting with users.
Based on that you will be monitoring
these traces and monitoring is on the
one hand automatic with evaluators and
with dashboards but also the human
feedback part cannot be underestimated
here. You will also be collecting
implicit or explicit explicit user
feedback and also manually be going
through some samples of these traces.
This together I don't know if you can
see oh the yellow um box is actually
quite clear. Great. Um, this together
the online part of the AI engineering
loop is already a lot. A lot of teams
that are not in high risk industries can
actually just start with these two and
based on what they find during
monitoring of their traces can already
um make simple fixes or improvements to
their agents, deploy these to production
and see their traces coming in. This is
a great first step and it will already
get you very far. Um, and it it's a
great way to iterate on your agents
fast. Once your product matures a bit,
your setup matures or you are in a
high-risk environment where any mistake
has bad consequences, um it makes sense
to also work on the offline part. So
that's really for structured testing. So
your data sets are your structured test
cases. These will be heavily inspired by
the way by what you see during
monitoring. And when you want to make a
change, you run an experiment on your
data sets. You evaluate the results of
the experiments. And only when the
results are better, you didn't introduce
any regressions. That's when you deploy
to production. Before we go into the
workshop, we very quickly want to focus
on the two parts in the online loop. Um,
so that's tracing and monitoring because
this is really important. Everything
starts with your trace. So because if
your trace is bad, you will not be
catching everything during the
monitoring step. If you don't catch
everything during the monitoring steps,
your data sets will be not as good as
they could be. You will not make the
best informed decisions on what to
evaluate, etc. So, it's really important
to take enough time to make sure your
traces are set up well. So, what's how
do you build a trace? A trace exists um
consists of observations and
observations are different steps an
agent is taking while creating an answer
for the user. These consist of LLM calls
or these can also be tool calls or other
things. These can also be nested.
Um each observation also has a lot of
data attached and this depends on the
kind of observation. For an LM call,
this is usually the duration, token
cost, um token usage model that was
used, a prompt version that was used,
everything you can think of that will
actually help you assess the quality um
of your LM call. And for tool calls it
can be completely different. For
example, if you do a web search, one
data point can be the query that was
used to do this web search.
So this is really important so that you
can then do monitoring. Well, monitoring
there are a couple of different
functions of monitoring. One is you want
to have aggregate metrics to then see
overall contingency over time. How is
the health of your system? both things
like the cost of your system for example
but also the quality. So if you set up
evaluators uh to measure the quality of
your responses uh you want to make sure
this is not going down over time. A
second very important one is signal
detection via user feedback. You will
have as your application scales a lot of
traces and will be impossible to see um
or go through everything and user
feedback is a great way to surface the
ones that actually are important to look
at. Third one is feedback and evals. So
you will set up automatic evaluators and
uh also you will do some human
annotation to make sure um you catch new
things. One important thing here. So you
have the automatic evaluators. These on
the one hand are very scalable. You can
keep on doing them on all your traces.
On the other hand, you will you're less
likely to catch very new or nuanced
cases that you didn't think about on by
yourself. But user feedback and human
annotation might scale a bit less well,
but these are where you will detect
really things you haven't thought about
yourself.
So this is what we'll focus on today and
my colleague Annabelle will go through a
practical example and Mark and I will be
walking around. If you need help, just
raise your hands. So today's focus as L
already mentioned is all about how to
effectively working with a trace of your
application also how to decide what you
actually want to monitor. So what is
interesting for you in your application
and not like generally and then also um
how you can leverage coding agents to uh
10x yourself a little bit but also maybe
where you should uh be in the loop and
not let the coding agent do everything
on its own. So uh let's dive into it and
um to do so uh we first want to meet our
sample application for today and we
brought for you specs the dad IT support
agent. So this uh mini repo came out of
a a mini project um I did uh for my dad
because my dad always asks me questions
on WhatsApp uh about how how to set up
his phone and also how to set up all
kinds of things with his printer or his
computer. Um so I built this little
agent that is replying to him um in the
production version via WhatsApp. In this
case, we now have a a nice little UI.
So, how you can imagine working it is we
have a user, my dad or whatever dad and
um the dad is asking specs a question
and specs has a few tools available. So,
we can get support context. So, some um
information about what kind of phone is
dad using and what kind of operating
system is it on? What kind of apps does
he have? And we also have a search help
library. saw some frequently asked
questions where there's some context on
how to go about solving certain issues
and um yeah it can use these tools and
then we also use the uh use openai the
API endpoint uh to generate replies and
get a reply back to our uh dad in this
case. So this application we're going to
first um look at traces together but
then also think about what is actually
interesting that we want to know about
uh to make sure dad gets the support he
actually wants to have.
So um yeah, you can scan the QR code
here. Um you will find the workshop
repository and um I'll get uh the setup
together with you. So no worries and
we're going to go through step by step.
There's also documentation in case you
get lost, you could also reference there
and if you want to explore more
afterwards. Uh there's also be going to
be some more um modules available. So
let's go to lenfuse.comworkshop
and we can see that um yeah this is a a
markdown page here. Uh but if you click
here on the lenfuse/langfuse
workshop, we actually get to git
repository and right here on um yeah,
you can clone uh the repo into your um
IDE. I already did that. Um so it's
prepared and we can see here that the
first thing um we need to get set up is
of course some uh end variables. And for
this um let's create a
or together on languis.com.
We can go to launch app. I already have
an organization. Um but you can go to uh
launch app or also if you're on the page
here and then uh select a region. It
doesn't matter which one you're taking.
And then um you can create an account
and as soon as you're in there uh what
you will see is this page. So there will
be a project autocreated for you and you
will land um on this page and there you
can get your um API keys by uh clicking
on create new API keys. Um, so maybe
I'll give you just a second uh to get to
our website and get this um get this set
up. And this will be the the very first
thing we have to do together.
And I'm going to show also here the
steps that you will also find on our um
workshop website.
So quickly signing up, creating a new
account.
And for everyone who now did that
already, um we brought uh for today an
open AI key. So you can scan it. We're
going to rotate it afterwards, of
course. Um but for today, um this is
your API key to use and you can add this
into your N uh file
and then we'll uh get started.
Yeah. So just copying the NF sample and
then getting there.
Okay. So when we have the uh repo
cloned, the first thing we have to do is
um we have to quickly install the
dependencies. So we're running here a
TypeScript application that is using the
OpenAI um agent SDK and uh yeah like
this we can quickly install all the
dependencies um it is available and then
we can
also start it by running npm rundev
and I'll pull this out here. It's
opening here directly.
I'm also going to open it here and we
can see our um yeah our sample
application and by the way if I'm a
little too fast like here are the steps
uh in the setup page on
lenfus.com/workshop
um how you can also get there um step by
step by adjusting the um end file and
then running uh the application. So
let's see what we have here. we have our
um dad support agent and it's already
greeting us uh with certain questions if
I have maybe questions and also we have
some um sample questions that dad might
ask um so we can say here how do I turn
on my Bluetooth on my iPhone and then
specs is taking a second and using in
the background the tools um that we're
like needing um to get there and then we
replies to our dad in this case uh now
with a step-by-step in instructions on
how to um yeah how to turn on Bluetooth
on the device and um what happened now
in the background. That is now uh the
interesting part um that we want to look
into. And if we now click back into
tracing and this is now also what should
happen for you if you run the
application and ask a single question
then uh we see the first trace popping
up. So every row here is an observation
and we can also see that they have
little different icons and these
different icons mean that they are
different things. So if we click into
one of them, we can see that the whole
thing is rooted in our um our agent
observation and then below we have a few
generations but also tool calls where
certain context is pulled. Um so this is
now already a fully instrumented
application and there's also a
step-by-step um guide on on how to get
this actually set up. But we also have a
lengthy skill that you can use to
automatically get it set up. And for
today, we actually want to focus on
working with those traces instead of
step by step uh setting them up. So, um
yeah, here we have our trace. And if we
now uh get back to our um
lenfuse.com/workshop page, we can go
into the monitoring workshop uh module,
which is the part that we actually want
to check out together today as lot
already mentioned. So, um in our context
of our dad support app, what does
monitoring actually mean? So whenever
dad is interacting with the application,
we of course don't see what he does uh
because we don't sit next to him. That's
the whole point about the agent. H but
we actually want to track what's going
on and we don't only want to track um
what kind of things the agent is doing
but we actually want to make sense of
it. So we thought about what are
actually things that can go wrong in a
support application. And the first one
is maybe the dad is disagreeing with the
application. So for example um if I'm
asking a question, how do I set up
Bluetooth? Um, then I'm wondering, okay,
um, how does it actually work? Where's
the button? And dad is, um, asking this,
and we might want to catch this because
there was something maybe not clear
enough, not detailed enough, um, for the
question to actually be properly, um,
done. So, um, let's get this set up
together. We're h starting with the um,
yeah, with copying this git command
here, get checkout checkpoint for
monitoring. And then we can get back
into our um, IDE.
and run this command. And we can see now
that we swapping or switching to the uh
monitoring uh step of our workshop. So
it's a checkpoint. And now we want to
wire up those um those evaluators in our
application.
So um if we go down a little bit, we can
see that the first thing um that we have
to do together is configuring the
Lenfuse evaluator model. So I'm going to
jump into our uh application here.
I'm going to close the tracing part and
I'm going to hop into our evaluator tab.
So here I can see I can get started with
my evaluators and there's two different
possibilities. I can either set up
codebased evaluators for more
deterministic checks about my
application and I can also get set up
with some LLM as a Dutch evaluators um
which are like more for the implicit
things that you might want to get out of
the conversation history uh and actually
want to find out there. And we can also
see that we have some uh templates here
and that our uh user disagreement one um
is actually one template that we are uh
providing here. So if we click on here
we can see okay we need to get up uh set
up with the um LLM connection. So I'm
going to jump over here and very quickly
stop sharing because shouldn't see the
API key.
laptop died.
So this is in the end um a possibility
to use a certain model to evaluate um
what's
going on
and to
give one second.
Okay. Yeah. So what I now did is I um
set up a new LLM connection and in this
case I'm using again the OpenAI API key.
Go back.
Yeah. Um so I connected the OpenAI API
key now that we um set up together. And
um in instead you can also connect all
kinds of other uh models of course and
you can also um use your own proxy in
case you have a have a gateway
configured yourself. And now we're going
to um jump back into our evaluator page.
We're going to click on create
evaluator. And now select our template
again
and select the model. And what we can
see here now is that the first thing we
can do together is we can filter for the
actual um observations that we want to
target. And in this case uh we want to
go um not for the generation um but for
the agent that is the root um of the
whole uh trace that we're having here.
And then you can also see that there are
some other options. So you can also
target tool calls or generations. But in
our specific case, we want to look at
the um input only. So we want to see uh
the the message of the user um being
looked at. So
looking at our instructions here again,
um we have a certain way to target those
different
different parts um of the observation.
So we're taking the agent, we have our
evaluator prompt here, and down here we
can see that um via um curled brackets,
we're actually pulling in um context
here. And to target the part of the
trace that is actually relevant for us,
uh we want to set up this JSON path here
and make sure that we're targeting the
part um that is that is correct in this
case. So for the conversation history,
we actually want to target the whole
message array. So, we're going to copy
this here
and we're packing it in here. And what
we can see down here now is that it's
mapping in the message history of your
trace. So, it's pulling together what
was the interaction, what did that ask,
what the tools um do, and then also what
kind of reply was generated. And as a
second part of um detecting if a user
disagrees um we of course um need to
also target the last message that is
coming from the user and like this
also get information here
and we can see that down here now we're
mapping how do I turn on Bluetooth on my
phone into this um evaluator and if we
now
execute this we have our first live
running evaluator. So you can imagine if
now a trace is coming in where um dad is
saying okay how do I turn on Bluetooth
and then he asks as a follow-up oh but
this button is actually not there I
don't know where to find it and um it's
not true what you're saying then we
would catch this because this is
actually an interesting event a signal
for us to understand okay where are
things going wrong and probably like in
the first 500 questions there it's not
like all 500 fail but maybe there's five
or six or seven different ones where
we're not clear enough and that might
need some more detail to actually go
deeper into it. So user disagreement is
our uh first example. Let's look at what
also might be interesting.
And in our case, we now have one um
where we're catching with a codebased
evaluator if maybe there's some all caps
used. So if I think about how I'm
interacting with cloud or codeex
sometimes if I'm getting frustrated, I
might just use all caps to get my point
across. And I think many of you have
also done this in chat applications. And
we see especially in chat applications
that this is actually a good way of
catching some frustration from the user.
And um in this case it's all caps. But
as an alternative this could also be
maybe cuss words or um yeah certain
terms that you should maybe not usually
use in a chat. Um but when it's an agent
you might tend to rather um go for it.
And uh for this we now want to set up a
codebased evaluator so we can actually
make sure uh we get that uh when he's
frustrated. So um as we can see here we
now have a little um Python snippet here
and if we go down a little bit um we can
see uh that here the actual evaluator
function is defined and um it's
targeting again a part of the JSON path.
So it's like extracting uh the certain
user message and then it's checking if
there's all caps in there and in case
it's doing all caps then we return a um
a boolean score true. So let's copy this
here so we can get this wired up. And
I'm only copying the bottom part because
the upper part is actually static. And
I'm setting up an additional evaluator
in this case now a codebased one.
And um we also support TypeScript code.
Uh so in case you're rather operating on
TypeScript, this is possible. But we now
want to go for um Python code. And um we
call it all caps.
frustrated.
And since we're going for a boolean
score, let's also add a little is um so
we always know if it's true, then it's
um he is actually frustrated uh with all
caps. And then I'm going to also down
here replace this part um with our
of course
copying it again.
And of course down here you can um write
all kinds of custom code um that you
want to go for. So whatever you want to
evaluate if it's certain words you're
looking for or uh for example also if
you have some brand name that always
should be written the right way. So for
example for length use also sometimes
the f is written big. We would usually
write it small. So you could also catch
these kind of things to see where maybe
things are going wrong. And yeah let's
get this set up. So we have our second
evaluator
created. But then of course we also need
to think about what kind of observations
do we want to target. So let's look
again here. Um we say okay of course we
want to run it on live observations. So
we want to know what's going on in
production. And we're again targeting
the um the observation type agent.
And here I can select this going for the
agent one again.
And here on the right side, we can also
s that see that we can do a small little
test run on it. And here we see that in
this case it's um returning a false
because we're here only asking the
questions about the turning on and off
Bluetooth. And as soon as we're happy
with it, uh we can then uh click on
execute. Uh just as a short note here
like right now we're running on
observations but this of course is also
possible to run on all kinds of
experiments that you might might want to
do in an offline improvement process
instead of running it on live production
data. So yeah right now we're happy with
uh just running it on live observations
and let's also click on execute here.
Nice. Uh so let's check how this
actually turned out. Uh because we of
course want to know if it also works.
And for this I am jumping back into our
IT support agent.
Let's kick it off first with a how do I
turn on Bluetooth again.
We're taking a second and then we're
getting our replies.
Zooming in. Yeah, I can't try. It's also
small for me. I was earlier like I
should have brought more glasses and
yeah, now we can see it. Perfect. Um, so
let's get frustrated
this one first. And of course, our agent
is somehow dealing with it because we
have some specifications in the system
prompt. And I might also um need of
course the reply first. So let's see. We
get some more details
and then I can maybe ask.
No, there is no such Bluetooth
sign
just to disagree a little bit with the
agent
and he says that I'm right. So let's see
how this turns out in our traces.
Okay, we see we have a few more um now
here coming in
and let's check maybe on this one. Okay,
we also have some evaluators coming in
already. Let's dive in a bit deeper into
what's actually going on here. So uh we
can see that this is now not the
Yeah, we have our user message. How do I
turn on Bluetooth? we get a reply and
then we can see that this is the output
we're getting back. Okay, dad, no
worries. Let's try the other um way
first. So here we had some um
disagreement going on and up here we can
see actually this little score. So on
the top left is probably still small
zooming in. Yeah, we can see now that
our root observation like the overall
agent is actually tagged with a user
disagreement um true. Uh because here
the the user actually said okay it's
actually um in this case also all caps
um is actually not true and it didn't
work out. And uh we can see this here
now and have like this also signals. So
we could in theory now filter for the
observations that are having a um maybe
user disagreement true or also um all
caps frustration uh true and like this
find the ones that are actually
interesting for us to work with.
Okay, so these are the ones where we get
something out of the more or less um
production behavior um of the people.
There's also one additional thing that
is often interesting to monitor in a
production application mainly being um
if someone is trying to do something
that is actually not supposed to be done
um with the respective uh application.
So we call this out of scope request. So
in our assistant prompt um we are
specifying here that the agent is
supposed to help with all kinds of phone
IT support questions. Uh but of course
dad also has different kinds of devices.
So maybe a printer also computer that he
wants to um get uh get questions
answered with. But right now we're
scoped um to this um specific scope. So
for this we can also um set up these
kinds of evaluators
and we are calling them in this case now
out of scope request. And here we have a
different uh dynamic. We're not looking
at only the last user message or the
message history. Um but here we're
actually also looking at the system
prompt. And because we are defining all
of this via this JSON path, we have the
possibility to target this also
specifically. So, um, one final time,
let's get this evaluator, uh, set up.
And for this, we're jumping into our,
um, evaluators page. We can click on
evaluators. And once again, um, we can
select our out of scope request
template.
We now want to target um, generations
because we also want to reference the
system prompt.
And let's now map our variables again.
So we are taking the
system prompt which in this case is the
very first message that is sent in this
interaction.
And then we're also taking our last user
message that is coming up.
And in this prompt now we define okay we
also wanna we want to always compare
like what the system is actually
supposed to do and what the agent is
compared to do uh supposed to do um to
what the user is actually trying to do.
So
this is now wired in
not mapping the variables right now
and let's execute this one as well.
Okay. So whenever now dev would try to
do something with the application that
he's actually not supposed to and then
we can know about this and then we can
based on this information take an
informed decision. Do we either want to
fix this so or expand the scope of our
application or do we maybe have an issue
in communicating to our users what
they're actually supposed to do with our
application and in this case of course
it's only the IT support but maybe in
bigger scope application there's
sometimes things people are trying to do
and really misunderstand how the system
is supposed to use supposed to be used
and like this we can uh yeah catch these
kind of things um that are going on and
go into more um detail here. Perfect. So
this is how we can set up evaluators and
monitors um for our application. And I
think what you can uh clearly see here
is that this is not about um
copying just what's out there and what
can use. And of course like many of
these things you could now reuse for
chat application but it's really about
thinking what is what are the typical
fail modes we will um endure in our kind
of application and not about like trying
to copy paste u what's out there but
really looking into what's going on. So
whenever we would want to work uh work
with this now we could for example now
go for um
use like using these um scores now to
also filter for certain um
for certain traces
and results.
Here we have two and like this get like
an insight on how often these things are
actually going wrong.
Perfect. So um like this we can wire up
monitors and see u what's going on and
um let's now seat some production
production data in to see what is
actually um happening and how this
performs in our app. And for this uh we
go down to the end of our um mon
monitoring module and we have a script
here to seat some um production
information
and like this have a bit more data to
actually look at. So I'm jumping back
into my um repository
and I'm copying our command. And what
you can imagine is happening in the
background is we have just a set of
traces as a data set. And this
information um also includes some scores
and we are seeding this um into our um
into our application into our language
instance um directly.
So, let's see if it already is seated.
Taking out our score filter again.
And we can see now, yes, there's new
things coming in.
We actually now have a lot of um a lot
of data, multiple pages of traces. And
now the question is of course how can we
work with this and how we can we find
out um what is actually going wrong or
also what is going um right in our
application.
And um all of this data is usually then
used to inform what you actually want to
make sure that it's also working in an
um offline uh improvement process. So
these production traces and especially
the ones that you find that are
interesting to look at h can then be
used to build up a data set that you can
use um in your offline improvement
process uh to to make a better
application. Um but today uh we want to
focus on the uh monitoring part and the
tracing part. So let's see how we can
maybe use our coding agent to find the
larger scale issues that are in this
application. And for this um let's
install the lenfuse skill together. Uh
so we can um use this
and for this we have a little command up
here in the setup step
and I I usually go actually with just um
telling my coding agent uh to install it
for me but you can equally also just um
install it separately. So we have a CLI
and we also have our skill and this can
be installed then in my case now
with claude
trusting my application
and what is now going on is that it's
pulling our CLI and our CLI is exposing
all APIs that we have so you can always
access your traces your scores your data
sets experience ment runs but also start
them through your um yeah command line
directly or also with your coding agent
together
and like this work more effectively um
with lenfuse and this is actually also
when you are trying to instrument your
application in the first place and try
to get your first traces and this is
something you can uh use to
automatically add tracing to your
application and get your first insights
so here I'm now um installing language
skill and uh just to see how it's done
then running I'm going uh over to codex
I already installed it in the background
and what I now want to find out what is
actually going wrong in my traces. So
what are the kind of information um
steps that are going wrong? What kind of
um scores do we actually have in there?
And I'm asking my coding agent here now
please use the length fuse skill
to find issues
in our traces
and naturally cudex will take now some
time uh but just to understand what's
going on um cudex is now accessing um
the live traces that we have in our
application so it's looking for what
kind of questions are asked what kind of
scores do we find in there? Um what is
maybe a lot of all caps frustration um
going on there also where did the user
disagree but also beyond what we
officially set up. So it's also checking
on is there maybe issues with our
latency is there issues with our tool
calls um anything that has been going
wrong in terms of what we didn't want to
um so to find where it's silently f
failing in production h even though we
don't want it um wanted to do this of
course and since this is now going to um
just run a little bit I think this is a
good moment to also um wait for codeex
and just take a few questions um in case
you have any okay let's see if the um if
we're there yeah uh we actually got
report and I could save this now as a
markdown but I'm just going to um very
briefly
show you the one that I prepared
and I'm swearing I'm not p hacking and
we can also look at the proper one but
just wanted to show you how this looks
like. So what our coding agent now did
is ran it ran over the um production
traces that we we seated in there. It
was like around 120 traces or it was 70
traces and it actually looked at all the
different dimensions where things could
be going wrong. And we get a quite um
detailed report now um about like how
many traces were there, how many
observations did we have also how many
of those were tool calls and what we
have in there and then it also generated
us some findings and the first finding
here is actually that um we have a
silent retrieval quality failure and
search help library. So this is actually
something we didn't evaluate for um but
uh we also didn't realize before that
our um lookup of information uh tool uh
where we're looking like what kind of um
question could what kind of answer could
be the right answer that is actually um
silently failing and not actually uh
doing what it's supposed to do. So
that's the first one we see. Um but we
also see that um the retrieval misses
are increasing latency and cost. So we
have some issue in like tool retry calls
um where we are detecting some kind of
um problems and we can also see that
there's um an evaluated coverage gap
that uh is across like recent traffic
and um we we actually don't uh evaluate
everything but we only get um signal
from a subset of the traces um that are
going on there and just briefly
verifying um if Codex now also came up
with the same. Okay, it also detected
that the prompt version is um is off
and then it also says about the latency
text for the retries
and we have the monitoring cover split.
Yeah. And like this we can find um those
issues in our application but we can
then also make sure that we find a way
to um to fix them and uh like this um
yeah improve the the application over
time and make sure um that we yeah that
we fix the issues that are actually
coming up.
Okay, so
we get the proposal here to save this.
Um, but actually let's see if we can get
also a fix in here. So what is the most
interesting part? Um, I actually want to
get rid of the search help library one
because if it's not really helping us to
use those tools, then we can also um
remove this. Um, and for this we can
also use our skill
our search help library tool.
And because we now have the repository
context, it actually can also help us um
fix um issues in the code and not only
um in our Langu setup. And yeah, now
it's getting um it's getting back to
work and um fixing this uh for us in our
application.
But let's now take a moment to zoom out
and understand what actually needs to
happen um with this. And for this um
we're coming back into our um slides
here again.
Uh so what we now focused on today is
actually the part of catching signals
from our production traces. So we
initially set up our tracing and made
sure that we have a step-by-step view
into what is um actually going on. What
kind of tools is our agent using? What's
the inputs and outputs and h get a
signal from this. But what does need to
happen with those kind of signals to
make a continuously improving agent over
time and uh for this like on the one
hand we need to maintain our evaluation
criteria. So um we had this question for
example on how can we make sure that
it's like not overindexing on something
um or like not really telling us
anything. And um yeah from this signal
we need to make sure that over time we
actually have a good um setup of our
evaluators and get the information we
need to get. Um but most importantly we
also need to maintain our data set. So
when you initially build an application
um you might think you know what kind of
things that people are trying to do. Um
but over time you will realize that
there's a lot of edge cases that you did
not account for and not cover um
beforehand. And that's why you need um
to over time uh also maintain your data
set um create good production examples
um add them to your offline events and
then make sure that you also can iterate
and whenever you make a change also ship
um with confidence so you can make it
part of your CI/CD and uh make sure that
is um yeah actually not regressing
whenever you introduce a change.
So um we today only covered the part of
the AI engineering loop uh where we are
looking into the online evaluations. Uh
but actually of course um there's more
to it. So it's all about uh making sure
you know what's going on, you catch the
interesting parts. um if it's a user
disagreement or all caps or if it's
cussing um or also some kind of quality
evaluations that you can do and out of
this um you're building and especially
also maintaining data sets over time. So
all of this is not a one-off. You
actually need to make sure that you are
like putting in the reps and close the
loop continuously to to also have then a
data set that represents what your user
users are doing. And on those data sets
you then want to um run experiments and
evaluate those experiments. Um so you
always have a good uh indication of how
good the quality of your of your app is
and um whenever you deploy then also
know um that that you can ship with
confidence.
So
this is the core part of our workshop. I
just wanted to briefly mention some
things. So today we only looked into
that part. Uh but on our website you can
see in this length workshop that this is
actually a eightstep um uh workshop
where you are guided through every
single module. So, we can only touch
upon this one and this one today, but
there's also prompt management to
Lenfuse. You can set up those data sets.
And um this is a step-by-step
walkthrough where you're guided through
um uh all of these steps and like this
uh can get it set up properly. And um we
of course also recommend to to uh to use
the the skill um to get the setup
together with your coding agent. And if
we uh were you and we would have to
start tomorrow um this is exactly what
we would uh be doing. So we would take
our repository um we would um use the
length view skill to get up set up with
tracing to really know what's happening
in your application um via this command.
We then would review traces manually and
really understand uh what people are
doing and then um yeah finally get into
the motion of building out our traces
and set um email setup for our
production traces to then get also into
the motion of um optimizing offline.
All right, thank you so much everyone.
Um I'm taking a few more questions but
thank you so much for participating and
Mark is around lot is around I am around
and we're super happy um to discuss
anything with you and we also have a
expo booth so please come around the
next few days and uh chat with us
>> [music]
