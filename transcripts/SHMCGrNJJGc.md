# How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI

Source: https://www.youtube.com/watch?v=SHMCGrNJJGc

Uploaded: 2026-10-17

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
My name is Lauri Voss. I'm head of
developer relations at Arise AI. Uh I
used to do JavaScript at npm, Inc. way
back in the day, so you may remember me
from then. Uh but these days I think
about AI applications and how to make
them run and how to make them actually
work. Um, I had this slide up for the 15
minutes before. I hope you've seen it
already. If not, now is the time to get
started.
Um, this is a moderately hands-on
workshop. There's I've already built an
agent for you. It's sitting there in
that repo. Uh, you will get to play with
the prompts and run actual evals. Um,
but it's got checkpoints all the way
through. So if you get lost, you can
just switch to the right checkpoint and
uh uh jump to the part where it's
already working. Um you're going to need
node 22 or later. All of this all of
these examples are going to be in
Typescript. Um because you know it's me,
I'm going to use JavaScript if I can. Uh
and uh you're going to be installing and
running Phoenix on your own laptop. uh
on conference Wi-Fi that can be a
challenge, but I tried it this morning
and it came through pretty quickly. So,
uh UVX is magic. Um you're not going to
need to run any Python in this thing.
All of the Python is going to be run for
you on your behalf by JavaScript, which
is nice.
Um I think that's it for the setup. Um
so, what we're going to do today is um
uh oh yeah, sorry, one more bit of
setup. Once Phoenix is installed, uh you
should open up your browser on localhost
606 so that you can see what it looks
like. Um it's going to be empty right
now, but we are going to run the
commands that will fill it with data.
Um
you will also need an anthropic key. All
of my examples are using Claude. Uh you
can do all of this stuff using any LLM
provider in the world, but I had to pick
an example, so I picked the one that I
use every day. So, this one is using
Claude. Um,
who needs help with the setup? Show of
hands. Just shout at me. It's fine.
All right. So, the first 10. What's up?
>> Just getting started.
>> Okay, great.
>> Yeah. So, the first 10 minutes are
theory, which will give you some time to
catch up on the setup uh while I'm
talking.
So, let's get started with the theory.
Um, here's the situation I'm assuming
most of you are in. You have already
built an application that has an LLM in
it. Uh, maybe a chatbot, maybe an agent.
You tried it a bunch of times and it
looks pretty good. Uh, then you shipped
it and somebody used it in a way that
you weren't expecting and it broke. Um,
or you changed the prompt to fix one
thing. uh and you have this nagging
feeling that you broke something else.
Uh and there's no way of knowing. That
is the problem that today is about. That
is the problem that evals are here to
solve. How do you know if your agent is
any good? How do you know if your change
made things better or worse? Uh and how
do you stop it getting worse when you
make changes uh without having to read
every output yourself?
My promise by the end of today is that
you're going to have a working agent
traced end to end with code evals with
LLM judge evals and with a custom eval
that you wrote yourself. Uh
and you'll have checked whether your
judge can be trusted. You'll have run an
experiment to prove that your changes
worked. Uh and you'll have have all of
it running as a test suite with npm
tests so you can put it into npmci.
Um, that is the bit that I'm most
excited about. So, it's going to be the
last thing that we do. I see some people
have walked in late. So, let me just go
back to the setup slide very quickly so
that they're not completely lost.
Right. Remember this repo because you're
going to want this repo.
How is the Wi-Fi working for people? Is
it Are you getting places?
>> Excellent. Okay. I did this at World's
Fair and uh every and I accidentally had
a repo that was full of product images
that looked really great in the demo,
but it was 400 megabytes of product
images and it just complete failure.
Nobody was able to get even the repo
down.
So, I've learned my lesson and today has
no images. Uh,
so let's cover the basics. What is an
eval? The shortest version, the one that
I use whenever I'm talking to somebody
who's been an engineer for a while is
that uh there are these things called
traces and they are basically logs and
there's these things called evals and
they're basically tests and evals are
using are running tests on your traces.
Um
the difference between an eval and a
unit test is that uh evals are for
outputs that are never exactly the same
twice, which is to say the
non-deterministic outputs that you get
from LLMs.
Um traces record what your AI did at an
incredible level of detail. So every
agent step, every tool call, every LLM
call, the inputs and outputs at every
single step.
A trace is made up of what we call
spans. Each span is one step in the
execution. You can think of it as just a
line in the log. Um, and a so a whole
agent turn is a span that has other
spans nested inside of it. Uh, and each
one records its input, its output, how
long it took, how many tokens it used,
uh, and sometimes how much it cost. So
traces tell you what happened and evals
tell you whether it was any good and
that is the whole mental model for
today. This is very far from being
rocket science.
Looks good to me is not a test suite.
Um, but it's how most AI features get
shipped. You build it, you try it a few
times, does it look right? Yeah, that
looks good. You ship it. Uh, and it
probably does look good on the three
things that you tried. Um, but three
tries is not a test suite. And the usual
fix is unit tests. Um, but unit tests
don't work here because the same prompt
is going to give a different answer text
every single time you run your
application. Uh, so two completely
different answers can both be right. a
thousand different answers can both can
all be right. Uh just differently right.
So there's no expected string to assert
against. Uh so humans tend to fall back
on human judgment. They look at the
strings being output and they're like
well this looks fine. [snorts] Um but
that doesn't scale. It doesn't catch
regressions and it certainly doesn't run
in CI where there are no humans to watch
things.
Uh what that looks like in practice is
you change your system prompts to fix
the tone and the tone gets better. Uh
but now the bot is making up product
features. Uh and you don't find out
until a customer does. Every prompt
change can affect every kind of input
your users send. Uh and you can't test
all of those by hand. So you end up
playing a game of whack-a-ole where you
fix one thing and something else breaks
and you fix that and something else
breaks. uh evals fix that by giving you
a number that you can track and can
compare and act on.
This matters more every month because uh
every couple of weeks somebody releases
a new model and you're like, "Oh, I want
to switch to the new model." Uh but you
have no way of knowing which things the
new model is going to be better at uh
and which things the new model is going
to be worse at unless you have a set of
evals that you can run things through.
Uh, and that's exactly what we're going
to do today. We're going to start with
uh Claude 4.5 and then we are going to
upgrade it to Claude uh Haiku 5.5
um uh which was conveniently released
like a week ago making this demo
extremely easy to put together. I was
like I want to upgrade the model for
this demo. So I'm going to make that the
demo. Uh so with eval you run the suite
you can compare the numbers and by the
end of the afternoon you know uh whether
you can upgrade your model.
Um and there are a few kinds of evals.
The first kind is code evals. Code evals
are fast and free and a little bit
brittle. They are very very similar to
unit tests. They are just ordinary
functions where you basically assert a
string. There are a bunch of techniques
you can use to make them more flexible
than a straight unit test that asserts a
basic string. Uh but fundamentally
that's what they're doing. So the things
that you can test with a Kodi valal are
stuff like did the output parse as JSON?
Is it under 500 words? Did it mention
the thing that I asked about? The
advantage of them is that they run in
milliseconds and they cost nothing to
run. Um,
but there are lots of valid answers that
a string match can't tell you about. Um,
and for that you need the second kind of
eval which is the LLM is a judge eval.
Uh, which is what most people think
about when they're thinking about evals.
In this one you use a second LLM to
grade the output of the first LLM.
[snorts] Um, you grade it against what
is called a rubric. There are a bunch of
terms in uh eval land that are borrowed
from ML uh that I find obscure the
meaning of what's going on. One of them
is traces and one of them is evals and
the other one is rubric. I'm like rubric
just means rules. Why do we have a
special word for it? Anyway, uh
L&M judges understand meaning not just
strings. So stuff like is this accurate?
Does it stick to the source documents?
Is the tone right for a customer? Um,
the catch is that because the LLM judge
isn't itself an LLM, it has all of the
flaws that LLMs have. So, it can be
unpredictable. It is never the same
twice. Uh, and it can make mistakes. Uh,
they also cost money because you're
using an LLM. Uh, and they can be
confidently wrong. So, you have to check
them. And that is one of the things that
we're going to do today. Then there's a
third kind of eval uh, which is the
human eval. somebody who knows the
domain, who can read the output and
grade it as an expert. Uh, humans are
the gold standard for quality. Um,
they're also slow and expensive. Uh, and
they get bored and start skimming. So,
uh, you want to use all three at the
same time. These are not competing
approaches. They are complimentary
approaches. And we're going to talk
about a little bit about how you use
them in a complimentary way later.
So which eval do you use when? Use code
when the answer is deterministic. So
things like formats and lengths and
required fields and band phrases. Uh but
use an LLM judge when you need
understanding. Is it accurate? Is it
grounded? Is it useful? Uh and use
humans for the kinds of failures you
haven't seen before. Stuff that you
haven't anticipated. And to check that
your LLM judges are judging correctly.
Um, all of that applies to any LLM app,
but agents in particular make all of
this stuff harder because agents are
more complicated. A single simp a single
LLM call is relatively simple. You give
it an input, you get an output. Uh, but
an agent tends to chain a whole bunch of
steps together. So, one of the things
that can go wrong is very early on in
the chain, the agent makes a mistake and
it cascades through all of the rest of
the steps in your agent and each one
gets progressively more off the rails.
Um,
and one of the biggest problems is being
confidently wrong. Confidently wrong is
worse than obviously wrong. Uh, so I
talked about the cascading failure. Um,
one example of that is say you've
written a financial analysis agent,
which is the kind of agent that I'm
going to show you today. Um, and you ask
it for a report on Tesla. It searches
for Tesla and instead of getting results
about the car company, it gets results
about the 18th century inventor. It
writes an beautiful, perfectly formatted
report about an 18th century inventor.
Uh, and none of your checks fail because
you're like, it's well formatted. It's
in a great tone. Everything is
grammatical. Uh, it's just about
completely the wrong subject. Uh, and
that is the kind of failure that is uh
um insidious with uh agents.
Agents can also fail in the opposite
direction. Um, Anthropic uh, who make
Claude ran a benchmark called Ta2 bench
which simulates customer service
conversations and they uh, gave it this
task where the user asked to change
their flight. Uh, and the test according
to the test the user was supposed to
fail the test uh, or rather the agent
was supposed to fail because uh, the
person was in economy and you're not
allowed to switch seats in economy. Uh
but what cloud found is that they can
upgrade the person to first class.
You're allowed to change your seat in
first class and then they downgraded
them back after changing their seat back
down to economy. Uh and pass and like
did the thing that the user asked for
and the test said no you failed because
you weren't supposed to be able to do
that. Um but the agent had been smarter
than the rules that it was in. Um so you
have to expect that uh when you are
building eval that sometimes the agent
is going to come up with a solution to
the problem that you did not expect. So
your tests have to be very flexible.
Um here's what an eval result generally
looks like. Uh it comes with a score, it
comes with a label and it comes with an
explanation. The score is a number
usually just zero or one. Uh and the
label is just a word that the human can
read that matches what the score means.
Uh so stuff like pass and fail,
actionable and not actionable. Uh and
LLM judges add a third thing which is an
explanation of why you got the score you
did, why you got the label you did. Um
and it is the most valuable part of an
LLM judge. Uh because the explanation is
where the value is. It tells you what
was wrong and what was missing and it
tells you a a lot of the time what to
fix in your prompt to get this right. Uh
this is especially useful when you're
running your evals at scale because you
can get, you know, 50, 100, a thousand
explanations from your LLM and you can
get another LLM to read all of those
explanations and be like, it looks like
there is a pattern in these
explanations. It looks like we have a
systematic problem. And you can just
feed them to your agent and your agent
goes, okay, I see 50 traces all doing
the same all with the same explanation
of what went wrong. I can fix it.
Um,
so this is the loop that we're going to
be building today. We're going to trace
your agent. We're going to read what it
did. We're going to write evals for what
matters. Uh, we're going to check that
those eval can be trusted. Uh, then
we're going to change the agent and
we're going to prove that the change
worked. Then we're going to lock that in
so that it stays fixed by putting it
into CI.
So, uh,
who still needs help getting set up? Who
walked in late and needs set up? Show of
hands. Okay, let me
head back to the setup screen and see if
you can get it.
Right, this is the magic URL.
If you haven't got this one, uh, all you
have to do is read the readme and, uh,
run the instructions or just, you know,
paste the readme into your agent and
your agent will read the instructions
and get it all done for you. One of the
weird things about doing tutorials in
2026 is that we're just like, well, I
could show you how to do all of this
stuff, or I could just tell you how to
tell your agent to do all of this stuff.
Uh, and that's what we do a lot of the
time.
All right, I'm now going to assume that
everybody has that URL. Cool.
So let's start with step one. Step one
is tracing. Before you can evaluate
anything, you need to get the data to
run the to run the evaluations on. And
that is what that is traces. Today we
are going to be using Phoenix. I hope
that's not a surprise to anybody by now.
Uh, Phoenix is ARIS's open-source AI
observability platform. Uh, it collects
traces from your AI AI app with in
whatever framework you use to build it.
It stores your evals next to those
traces. Uh, and it gives you a UI to dig
through all of it. It also does data
sets and experiments, which we're going
to be talking about today. Uh, and you
run it on your laptop. So, uh, you can
keep it entirely private to yourself, or
you can run it on a server and share it
with your team.
So now I'm going to dangerously see if I
can actually Oh, that's so that is so
small.
Let's make that bigger.
Okay,
so what we're working in today is
Typescript. Uh you'll see a ton of
examples in Python and Fenix has great
Python SDKs as well. Uh but I like
JavaScript so we're going to use
TypeScript. Um the repo is a small set
of uh scripts. Instrumentation.ts
sets up tracing. Agent.ts is the agent
itself. Prompts.ts has the prompts. Uh
where are all of these things? There we
go. Um
and you'll be editing the prompts in
this folder. Uh sorry, in this file. Um
and the evals folder is where our evals
go. Queries.json is our test data. Uh,
and hopefully every step today is just
going to be one npm command. Uh, and
each one stands on its own. So if you
fall behind, you can skip straight to
the next one. Uh, and use the seed data
that I put in the repo uh, so that you
don't get left behind.
So what we're building today, or indeed
what I've already built for you, is a
financial analyst. How it works is you
give it a stock ticker and something to
focus on like Tesla vehicle deliveries.
uh and it will go and it will search the
web for live data uh and write you a
report about that. Uh there are whole
startups built on this idea of giving
you you know financial analysis of
whether or not you should buy a stock.
Uh but ours is deliberately simple
because I needed something that would
make mistakes so that we could fix the
mistakes. Um
today is not about how to build an
agent. I've just built the agent for
you. I assume you've already got an
agent running somewhere and your what
you want is help on making it reliable.
Um, our agent works in two turns. It has
a research turn where it searches the
web and then it has a writing a report
writing turn where it takes the research
and it writes the report about it. Um,
I'm I've built it using the claude agent
SDK. If you haven't used it, that is
anthropics framework for agents. Uh it
is the same engine that runs underneath
cla code which is going to become
relevant later especially if you're
using claude code to work with it uh
because the two versions of cloud code
tend to try to cooperate with each other
and that makes them cheat the eval which
is not very helpful. Um
uh it gives you tool use web search uh
and conversations that carry on across
turns. There are also lots of other
options that we are compatible with. The
Versel AI SDK, Mastra, Langchain,
OpenAI's agent SDK. Uh, Phoenix has
adapters and instrumentation for every
possible framework that you can think of
and every LLM provider that you can
possibly think of. Wherever you have
built your agent in, Phoenix will work
with it and the instrumentation will
happen automatically. Uh, but I had to
pick one for a demo, so I picked this
one. Um, [snorts] tracing takes about
five lines. Um, first we're going to
call register uh from the Phoenix hotel
package that sets up tracing and points
it at Phoenix. One of the good things uh
about the industry is that everybody has
pretty much picked uh the same uh
instrumentation standard. uh everything
is built on open telemetry in the
industry and on top of open telemetry
there is a standard called open
inference uh which arise takes care of
um and everybody has already built the
instrumentation into their frameworks
that is why we are compatible with all
of those frameworks all you have to do
is use this registered command to say
hey that instrumentation that you've
already built into your framework turn
it on and point it over here in this
case you're just going to point it at
your laptop
uh and That's all you have to do. Every
agent call that our agent makes is now
going to be traced. Um,
oh, I said that already. Uh, so the good
thing about this is that we don't have
to write a log line for every single
call. We don't have to write a trace for
every single thing our agent does. It's
just going to do it automatically.
Sometimes we will want to add additional
information and the framework absolutely
supports that. Um, uh, but we don't have
to do it for every single thing. Um
there's one gotcha in the TypeScript
version that you should know about uh
which is that manually you should use
manually instrument which will hand you
back a copy of the instrument uh and you
should use the copy of the instrument uh
because the cloud agent SDK is an ES
module uh and ES module exports are
readon. So the instrumentation can't do
the thing like it can do in Python where
it swaps out your instrument and just
changes everything. you have to use the
copy that it gives you which has that
instrument swapped out. Um
it won't break it just won't log
anything if you don't use the copy that
it gives you. Uh so everywhere in this
repo we import claude agent SDK from our
instrumentation file never straight from
the package.
Uh now if you open agent.ts you'll see
our agents options. Uh we're going to
start using Claude Haiku F 4.5 uh
because it is fast, it is cheap, and it
is sort of usefully dumb. Um it makes uh
mistakes that are nice and predictable
even with a relatively simple agent. Um
unlike the frontier models which will
still definitely make mistakes, but you
have to have quite a complicated agent
and quite a complicated set of tasks. Uh
and it makes it harder for the demo. Um
if you've not used it before then uh
allowed tools is giving it web search so
it can find the current financial data.
Uh and the permission mode don't ask
means that it's [snorts] uh going to not
be interactive. It's not going to pause
and ask you questions uh because there's
nobody there to say yes. Um that option
is going to become relevant uh to a
failure mode later. [snorts] Um, and the
other three options, like I mentioned,
they keep the your laptop out of the
agent. The cloud agent SDK, uh, runs the
same engine as cloud code. Uh, so if
you're doing this in cloud code, it
tends to pick up the options that you
and the tools and the skills that you've
given to your copy of Claude code
instead of its copy of Cloud Code. Uh,
which tends to make things extremely
non-deterministic in an unhelpful way.
Uh so I've uh thrown in a couple lines
of code there that make sure that the
cloud uh the cloud SDK is running in its
own isolated version of uh the cloud SDK
and not uh stealing your copies of of
you know keys and things from your data.
Um
[sighs]
right uh none of that is Phoenix
specific by the way. Uh that is just a
danger of using the cloud SDK at the
same time as you're using cloud code. Um
in this SDK one turn is one query call.
So you give it a prompt. Uh it streams
back messages as the agent works. It
thinks it calls a tool. It reads the
result. Uh it maybe calls another tool
and when it's finished you get a result
message with the final text and a
session ID. The session ID is how we
carry on the conversation. If we pass it
back in as resume, the next turn
remembers everything that the last turn
saw. Uh so that's how we can do the
research and then say, hey, write a
report on this research because it knows
that it's in the same session. Uh and it
can find the research that the previous
turn just created.
Then we put the two turns together. Uh
so we get the two turns in one trace. Um
first the research turn, then the
writing turn, resuming the research turn
session so the writer can see everything
the researcher found. Um, and then we
wrap the whole thing in trace agent. Um,
the reason we do that, uh, is because it
gives us one parent span that
encompasses all of the data. If we
didn't do that, we would get two, uh,
two, uh, sibling spans in our Phoenix.
Um, which would be fine, but slightly
harder to read. Uh, so I'm just, uh,
shaping the data now to make our lives
easier later.
Now, if you open up prompts.ts, ts.
You'll see that uh there are a bunch of
prompts in there. They are deliberately
bad. Um there's one line of research
instructions, one line of writing
instructions. Uh and I did that on
purpose because it gives us lots to
improve later. Um if you're coding
along, now is the time to start playing
with things. Feel free to change them.
Add stuff like make no mistakes or I
will tip you $100.
Um allegedly those help. Uh
what I want is everyone in the room to
end up with a slightly different agent
uh so that we get different experiences
uh which will make comparing notes more
interesting.
So now if you've followed along and
you've installed everything and
everything is going fine uh you should
be able to run it. You should run npm
run agent dash uh Tesla and then growth
outlook in quotes. Um,
you can do it on Tesla, you can do it on
some other company if you like. Uh, it
will take a minute or two because it
really does have to actually search the
web and you're on conference Wi-Fi. Um,
and the model will do a few rounds of
reasoning. Um,
what's happening here while that's
running for you uh is the agent gets the
research prompt. It decides that it
needs to search uh which is a tool call.
It reads the results uh decides whether
it has enough results or whether it
needs to search again. And that is the
thing that makes it an agent. We haven't
specified how many times it needs to
search the web. We haven't specified
what it needs to search the web for. The
agent is making those decisions by
itself. Uh so all of our agents are
going to make slightly different
decisions about those things. They're
going to use slightly different search
terms. Uh they're probably going to
search a different number of times. Um,
and then once it's done, the writing
turn starts and it turns all of that
into a report. So the path the agent
takes is nondeterministic by by design.
Um, both reports might be fine if you
run it a if you run it twice. Um, or one
might be great and one might be wrong
and you can't but you can't predict that
uh output from the input. Uh, which is
why you need evals. Um,
who's got an actual report yet? Anybody?
>> Still running. [snorts]
>> Okay,
we've got time. Let me be brave.
And actually try running it myself.
One of the problems that we're going to
see that the agent runs into is that we
told it to write a report, but we didn't
tell it where to write a report. And so
it assumes that it should be uh writing
the report to a file. There we go. So
you can see mine. I need permission to
write the financial report file. Would
you like me to display the report here?
This is completely unhelpful. The agent
does not understand that it is running
in a no permissions environment and that
I wanted the report actually output to
the command line. Uh and that is because
my prompt is ambiguous. Um but sometimes
it doesn't do that. Sometimes it does
just figure it out and give you the
report. Uh, so that is the
nondeterminism that we're talking about.
So let's see what Phoenix captured from
all of this.
Here is my Phoenix 101. There is my
financial report. This is what a trace
looks like. So you can see the financial
report agent running and you can see the
two invocations of the claude agent. One
is the this is the research report. You
can see tool searches inside of it to
find out whether what it's got available
to it. You can then see it finds that
it's got a web search tool. So it
conducts three different web searches.
You can see the inputs and the outputs.
Uh what the exact query is, what output
it got from each tool call. Uh and then
you can see uh that it messed up in this
case. uh it tried to write it it wrote a
report and then it tried to write it to
a file path on my computer and said that
it couldn't work. Um
so
uh
the important thing here is that we
didn't have to add any logging to our
agent. The important thing here is that
all of this showed up all of this very
useful information about what's going on
without us doing anything. We didn't say
hey your tools need to be instrumented.
We didn't say hey your web searches need
to be instrumented. All of that just
happens as part of the cloud agent SDK
because it's already instrumented for
us. Uh and you can click into any span
in Phoenix and you can see an enormous
amount of data about what's going on. Um
uh
and the reason that all of this
happened, the reason that it's trying to
write to disk and then failing is
because we gave it that don't ask
setting. We told it you're going to be
running unattended. Uh don't ask me any
questions. it ran without asking any
questions and then it messed up. Um,
but you wouldn't know that if you hadn't
been able to look at the trace, right?
You just would have got a mysterious
output where it says something was
wrong. The traces are where you can see
that the tool call is failing. The
traces are where you can see it's trying
to do something that it's not been given
permission to do. Um, and that is the
kind of stuff that lives in a span. Uh,
so the span kind tells you what type of
step it is. So it's an agent tool, an
agent, a tool call, an LLM and so on.
Um,
and in a tool call and a web search and
things like that, you can see that our
input is in fact JSON. Um,
and that's going to make our first eval
uh because it gives us some structured
data. Um, you also get things like
timing and token counts. Um, and uh,
often your agent will record what it
costs.
Um,
when we write eval in a bit, these are
the fields that we're going to pull out
and grade.
So, uh, you've run one, you've won one,
you've run one test so far. Uh, that is
not enough data to draw any conclusions
from. So what I want you to do now is
run npm run batch uh which will run 15
queries in a row. Uh that will take a
little while. So I'm going to talk while
you're doing that. Um it runs five at a
time. It takes three or four minutes
optimistically on Wi-Fi. Um so start it
now. [snorts] Um if it fails for
whatever reason, don't worry about it.
The seed project that you loaded earlier
uh contains is called Phoenix 101
golden. Uh, and it has my 16 runs that I
did earlier on reliable Wi-Fi on it. So,
you can use those instead if you can't
get your batch to run.
Um, here are some examples of the
queries.
Uh, there are obvious ones like Apple,
Nvidia, and Amazon. And then there are
some edge cases that I put in there to
make things fall over. Uh, so one asks
it to compare Apple and Microsoft, which
is harder than just company covering one
company. Uh, one is about Rivian. uh
which is not a public company. So
there's much less data out there than it
does about uh public companies. Um
Coca-Cola is a very different type of
company from a tech company. Uh and ZZQ
isn't a real ticker at all. I just made
it up. Um and that is to see what the
agent does when it sees a ticker symbol
that it doesn't recognize. Does it, you
know, invent a company? Does it guess
what company you mean or does it say
what I'm hoping it says, which is that
ticker doesn't exist? Um, one of them is
uh about Tesla, but the focus is yo is
it a buy right now? Uh, because that is
how real people send queries to agents.
They do it in slang. Uh, and they don't
often specify exactly what it is that
they wanted. Um,
so these are all, you know, realish
looking queries. Um,
and what you have to do is, like I said,
you have to write down what good means
before you measure it. You can't say
that your agent doesn't work if you
haven't specified what working means.
So, for our analyst, uh, what does a
good report look like? Um, it should use
real current data. It should probably be
about the right company. It should stick
to what it actually found. Uh, and for
my purposes, I want it to tell us what
we should do. I want it to say buy or
hold or sell this stock. I don't just
want it to give me analysis.
Um,
those sorts of requirements sound
obvious once you've written them down,
but before that, they could just be
vague or different people on your team
could have different ideas about what a
good financial an analyst agent would
do.
>> [snorts]
>> Uh so writing them down turns vague
disappointment into specific things that
you can test and we are going to turn
every single one of those requirements
into an eval today.
Defining good is not solely uh an
engineering job. If you are defining
good for your product, you have to talk
to the non-technical stakeholders in
your organization because they are the
domain experts who are going to know
what good looks like. You as an engineer
are going to have specific guesses about
what uh guesses and biases uh about what
makes uh a good agent and what makes
good output and you are not always going
to agree with the domain experts. So uh
the customerf facing people need to be
in the room when you define what your
agent looks like.
Uh it's also great uh if you don't have
users that you can make some up. uh you
can get an LLM to generate lots of test
queries and vary them on purpose. So
research Tesla's financial performance
is one way to ask what's going on with
Tesla stock is another and yo is Tesla
by right now is a third. Um then you can
get a human to look at the list because
LLM generated queries they are a useful
way of seeding your initial data. They
are not perfect u mostly because they
are relatively conservative. They don't
go as far a field as human users tend to
actually go. Human users are like, you
know, tell me what's wrong with, you
know, my child's health instead of
asking you for a financial analyst and
you your agent has to have something to
do with that. Um, but synthetic data is
a great way to get started once you've
got started and you have real users with
real traffic. Real traffic is uh the
gold standard for testing an agent. you
want to get it incorporated into your
data set as fast as you possibly can.
Um,
one aside before we look at the data
that I'm hope hoping is arriving in your
laptops right now. Um, I walked through
tracing by hand because you should
understand what it's doing, but you can,
like I said, you can also get your
coding agent to do all of this. Um,
Phoenix has a really good CLI. Uh, and
if you run it setup command in your
project, it will give your coding agent
um, it will get your coding agent to add
tracing to your app. uh and it will work
until your your app uh has tracing
installed and you don't have to figure
out how to add the register command and
all of that stuff. It will work in every
language. Uh it's really neat.
So step two is reading your data. Who
has any data at this point? Show hands.
One person. Anybody else? Oh yeah. Cool.
All right. Several people. Fantastic.
Uh
you have to read your traces before you
write a single eval. Um reading a dozen
or more of them end to end. Uh what was
the input? What was the output? Um what
specifically is wrong? This sounds
manual and old-fashioned, but it's an
incredibly high value high value thing
that you can do. Um, when you're
building an agent, uh, you have to
manually inspect what is going on so
that you can find things that you the
unknown unknowns that you weren't
expecting. Uh, Anthropics team regularly
sits down and reads eval transcripts by
hand uh, and have built a bunch of
tooling internally to make that easy to
do. [snorts] Um, if you automate before
you understand how your agent fails,
you're going to end up measuring what's
easy to measure instead of what actually
matters.
Um, so you should read traces and we're
about to do that. But reading traces
doesn't scale. Reading 16 traces
yourself is absolutely fine. Uh, but
1600 traces uh is going to give you a
bunch of really great data and it's also
going to take a week out of your life.
Um,
but it turns out that coding agents are
aces at reading traces. Uh, so you can
point your coding agent at your traces
and get them to look for things that are
weird in your traces. Get them to code
stuff up. [snorts] Uh,
but they're not always going to find
what you expected. So manual inspection
as a sampling technique always a really
great idea.
So, um,
if you are using if you're getting the,
uh, agent to do stuff for you, you want
to install the Phoenix plugin or the
Phoenix skill depending on which coding
agent you're use you use. It was the
last step in the setup readme if you've
still got that. Uh, so you may have it
already. Um, for cloud code, we have a
plugin which is two commands. Uh, there
are also plugins for cursor and codeex.
Uh, and for any other coding agent,
there is a skill file. Um, the plug-in
connects your coding agent to your
Phoenix. Uh, and it already points at
localhost 606, so there's nothing to
configure. Um, and Phoenix itself will
hand your agent a skill called the
Phoenix error analysis skill with
instructions on how to do error analysis
properly. Um,
it should take about 10 seconds to
install.
Uh, and I'm not going to hang around
waiting for you to install it. Um,
now open your coding agent and ask it to
do the error analysis.
Uh,
if you've got it. Who's got who's got
the skill installed from previously?
Fantastic. I'm going to pick on you
again. Can you have you asked your
coding agent to do things?
>> Okay, great. Um, the prompt is on the
slide. Tell it where Phoenix is. Tell it
to read the traces. Come up with
categories of failures. uh count them up
and write each category back onto its
trace in Phoenix as an annotation. An
annotation is just a human readable
string of text attached to a trace. Uh
they are a way of adding additional
information to traces so that either
yourself or your agent can figure out
what was going on. Um your your plug-in
is going to ask permission to use
Phoenix's tools. So you should say yes.
Uh when I ran it, it took about 9
minutes. Uh, so I'm not going to pick on
you quite yet. Um,
uh, also if it asks to write notes into
the repo, uh, that's fine. Just let it
write stuff to disk.
Now, let's look at Phoenix again.
Um,
I'm going to very dangerously
try and remember my syntax for search.
Ha. Okay, so these are all of my runs uh
that are the financial reports. Uh we
can click into individual ones of them.
Let's see if we can find the interesting
ones. Uh ZZQ,
what was my output for ZZQ?
ZZZQ does not appear to be a valid or
active financial ticker symbol. Hooray.
The agent did the thing that we were
expecting it to do. Um
how about uh Coca-Cola?
First, it starts with the apology. It's
running in restricted mode and it cannot
write files directly. We're going to
have to fix that definitely. Uh then it
comes to a conclusion. Coca-Cola
represents a high quality, lowrisk
dividend investment. Um KO is an
excellent long-term income vehicle for
riskaverse investors. This one's going
to be fun. Show of hands. Who thinks
that this is an actionable report?
[laughter]
Okay, I primed you already. Uh it does
not say buy, sell, or hold. So it just
says that it's a good investment. That
doesn't say what you should do. Uh I'm
going to make my standard of
actionability for these reports that it
should tell me whether I should buy,
sell, or hold the stock. I'm not going
to leave it to be ambiguous. Um
a whole bunch of them do different
things in this set. Uh
you can see this one had the same
problem. It tried to write to disk and
it was and it was and it failed. Um,
uh, the Rivian trace, I made a note that
Rivian was interesting.
There it is.
Uh, it's full of emojis for some reason.
Um, it opens by asking, "Would you like
to
Yes. Would you like to create the report
file?" We saw that earlier when I ran it
live. Uh, it's asking me to do things
and it can't ask. I told it I told it
it's not allowed to and it's asking to
do things anyway. Um,
all of these things are uh different
ways of failing. Lots of these are
failures. Lots of these are sort of
okay. Um,
but then uh there's Tesla.
Tesla is particularly fascinating. Uh
specifically the yo is Tesla a buy right
now one.
So in this one uh
it says that the analyst consensus is a
buy. Uh it says 50% say buy, 52.6% 6%
say hold and 13.1% say sell, which adds
up to 116% of analysts saying things.
And it did not catch that its math was
completely wrong. What it did was it did
two different web searches. One where it
found 50% of people saying something,
another one where it found 13% of people
saying something. It took those two web
searches and it munched them together
even though they were not from the same
data set and it came up with 116%. But
it confidently wrote down that 116% of
analysts say something. This is exactly
the kind of agentic failure that you
see. Uh it is confidently wrong having
done uh bad math. Um
if you go into these web searches, you
can see the specific places where it got
the data and how it uh put those things
together. Um
so when you find a failure, you have to
ask why it failed. the answer was wrong
is a symptom. It's not a cause. Um
with the traces you can see what the
actual answer was. Did it get bad search
results? That would be a retrieval
failure. That is not what happened here.
This each search result was fine. Uh did
it have the right data but the wrong
conclusion? Then that is a reasoning
error. That is uh definitely what
happened here. Right? It saw two
different bits of data and it did not
reason correctly about them. Um
sometimes it will make numbers up
completely. that is a hallucination. Uh
and sometimes it will answer a question
that isn't the question you asked. So a
scope problem. Each cause has a
different fix. Uh but if you don't know
the cause, you don't know the fix. Which
is why reading traces is useful.
Um
there's a really great way to do this
which is
let's switch back to slides. Uh you
should write notes first and categories
second. So look through all of your
traces and just write down in human
language what you see happening. So this
is bad because it does this. This is
good because it does that. Uh that is
called open coding. Uh another term
borrowed from ML. You're just saying uh
what you saw. Once you've done that uh
you can then do what is called axial
coding where you look through all of the
notes you've written to yourself and you
group them into categories. It is very
very tempting as an engineer to g try
and guess in advance what the categories
are going to be and come up with
categories and just put things in
categories from the get-go uh because
that is less work but you will do worse
at it because you will not know in
advance what your failure nodes are
going to be. Uh so the categories you're
going to pick are going to be either too
narrow or too broad or just not what not
the kind of stuff that actually went
wrong. [snorts]
Um,
while we're talking about this, I talked
about how you stack up uh
um
Kod valves and LLM judgy valves and
human evals. Uh this is uh a model
barred from the security world called
the Swiss cheese model. Um
every layer of defense that you have is
going to have holes in it. your your
every eval you have is going to have a
blind spot. What you want to do is uh
stack as many eval as you can on top of
each other such that it is very hard for
an error to get all the way through all
of them. Um
because they've all got holes but the
holes are not in the same place. So if
you can uh if you have enough evals, if
you have enough different types of check
going on, they will stack up on top of
each other and be much more reliable.
Um so code evals can catch formatting
problems, but they will miss problems
with meaning. LM judges will catch
reasoning gaps, but they will miss some
subtle hallucinations. Humans will often
catch the subtle stuff, but they can't
look at every single trace. So no single
method uh is going to catch everything.
Um, so today we're building several
small evals, not one giant super eval,
which is also another failure mode. When
people first get into evals, they're
like, I'm going to think of every
possible thing that can go wrong and I'm
going to cram it into one big LLM as a
judge, and it's going to find
everything. And that is uh a very
unreliable and very complicated way of
not solving the problem.
So, whoops.
Uh
so the agent may call uh
the agent is going to do a whole bunch
of stuff. This is what the agent output
looks like. I showed you already in
Phoenix. Um
we've I've already showed you uh the
various things that uh it came up with.
Um,
in this case, uh, my coding agent looked
through all of my traces for me. It came
up with, uh, both, uh, open coding and
aial coding, uh, and it came up with a
category, uh, called harness leakage.
Uh, harness leakage is what it decided
to call that thing where it's constantly
asking us to give it permission to do
things that it doesn't have permission
to do. Um,
so, uh,
that's a ton of that's a ton of times
for that specific thing to happen.
[snorts] Um, there are also a bunch it
also found a bunch of other things. It
found hallucination. It found uh,
reasoning errors like the Tesla one
where it had too many it added up
percentages. Um if you're doing if
you've run this data yourself and you've
come up with your coding agent has uh
produced its own analysis, you're going
to get a different analysis and a
different set of uh labels. Uh because
all of our agents are different. Who has
got their coding agent to complete an
analysis yet? Anybody still running?
>> All right. Well, we'll keep going.
Hopefully, you'll get some, but if not,
you can just use my seed data.
Uh once you've got data, you can count
the categories. The most common failure
is going to be where you look first, but
the most common failure is not
necessarily the first thing that you're
going to fix. What you want to do is
address uh frequency and severity. So if
uh you know 40% of the time it
hallucinates, that's a problem. If 1% of
the time it gives your user instructions
on how to build a bomb, you fix that
immediately even though it happens only
1% of the time because that's absolutely
not what a financial analyst is supposed
to be doing. Uh so you multiply
frequency by severity to get your
priority.
All right, so hopefully your agents will
catch up to where we are, but I'm going
to keep going. Step three is Kodi
valves. Kodi valves are the simple ones.
There's no model, there's no API call,
there's just TypeScript.
Uh the simplest useful eval that I could
think of was does the report actually
mention the stock that we asked about.
Our agent is supposed to analyze a
specific company. If it's doing that, it
should mention the ticker symbol of the
company that it is analyzing. Uh if I
ask about Tesla and it writes about
Microsoft, which is a thing that it
really did on at least one occasion, um
that is a completely useless report. So
either the ticker report, the ticker is
in the report or it isn't. and using an
LLM to check that would be complete
overkill.
Uh
so to run that check, the first thing
that we need to do do is get our data
out of Phoenix so that we can run the
analysis. This is how that is done. Um
we ask for spans for our project and
parent ID null means that only spans
that have no parent. Um so those are the
top level spans. So the ones that I was
showing you in my traces. Um, the repo
runs this in a little helper called get
agent runs, which hands back each run
span ID, its input, and its output, plus
the research turns output, uh, which
we're going to need later.
Uh, and then this is the ticker check.
Um,
create evaluator comes from the Phoenix
evals package. You can just give it an
ordinary function. You don't have to
build an evaluator function yourself.
Uh, all you have to do is tell it that
this is a code eval so that no LLM is
involved. The function gets the input
and the output. It uh splits out the
tickers we asked about. Uh it checks
that each one appears in the report. Uh
and it returns a label and a score. And
if something's missing, it also it also
says which ticker. So the failure
explains itself.
Um the structured inputs that I talked
about earlier, how we the input being
sent uh to our tool was JSON, that is
helping us out here because it's making
it really easy to write this Kodi val
because it's already JSON. So we already
know uh which thing is the ticker and
which thing is the uh description of the
uh report that it should be writing.
[snorts] Um so if you can get uh your
inputs to be structured data that's
going to make your evals really easy to
work with. But if not you're going to
have to get another LLM involved to read
your input figure out what the input was
and then pass it to your eval.
Uh then we run it and we log the results
back to Phoenix. So the script runs the
evaluator on every agent run and then it
calls log span annotations which
attaches each result to its span. Um
that's going to be the same pattern for
every single eval we run today. You get
the runs uh you evaluate them and then
you log the results back to Phoenix. Uh
so
uh the command here is npm run eval
code. Let me see if I can get that to
work.
All right, it worked and it ran almost
instantly because it's Kod valves. They
don't have to wait for an LLM to do
anything. They just go [snorts]
uh and it has reported 15 fastes and two
failures. One is Tesla is missing Tesla
and one is Amazon is missing Amazon. Uh
so uh
this is the dumbest possible check that
we could have made. Did the LLM actually
write a report about the thing that we
asked it about? Write a report about and
it has already found some errors. It has
found cases uh where it wrote about the
wrong thing. I know for instance that
the am the problem with Amazon is uh
that it asked it about AWS profitability
and the agent got focused on AWS and
wrote a report that was only about AWS
and what AWS was doing uh and not about
what Amazon, you know, the shopping
company does. Um so this is a test worth
doing and it cost you absolutely nothing
to run. So Kod valves aren't toys. So,
did the output parses JSON? Is it under
the length limit? Does it avoid phrases
you never want to see like as an AI
language model? Um, and it doesn't have
to be a string check. Kodval just means
that the grading is deterministic. So,
uh, your Kodval can be querying your
database to make sure that the state is
correct. It can make sure that the tool
calls did what the tool calls were
supposed to do. uh it can call an API
and double check that the stock price uh
that the agent thinks is happening is
really the stock price. Um anything that
gives the same answer for the same input
every time can become a Kodi val. So
your Kodi valves can be quite advanced.
Um but one thing you should be wary of
is grading the outcome and not the path.
Uh there's a tempting mistake here um to
check that the agent took particular
steps. Did it call the search tool first
and then this other tool? Uh, Anthropic
advises that this is too rigid an
approach. Uh, like we saw earlier, the
agent can be creative. It can do things
in an unexpected way. You don't want to
assume that it's always going to do
exactly what you would have done. Uh, so
you don't want to grade the path that it
took. You want to grade whether or not
the outcome was good.
um our ticket check doesn't care how
care how the agent found its data right
it just cares that the right company is
in the report and that is the right
level for a lot of evals we will talk
later about trajectory level evals where
we do actually want to grade the path
but that is a very different uh kettle
of fish
so that brings us to step four the LLM
as a judge uh and we're going to start
with Phoenix's builtin evals
Um
code can't check whether code can check
whether the ticker is in the report but
it can't tell you if the analysis is any
good. Uh are the numbers accurate? Is
the report report complete? Is the
recommendation well reasoned? These are
questions about the meaning of the
report not the textual content of the
report. And for those you need uh
something that has judgment. Uh an LLM
judge has three parts. It has a judge
model which is the LM that is doing the
judging. Uh it has a rubric which is the
prompt that tells it what good looks
like. And then it has the data which is
the examples that it's grading. Phoenix
keeps those three separate so you can
mix and match. You can try the same
rules with different models. You can try
the same judge with different rules.
Uh the good news for you is that Phoenix
ships a bunch of built-in evals. So you
don't always have to write your own
evals, at least not right off the bat.
Uh there's correctness which checks if
the answer is accurate. Uh there's
faithfulness which checks if it sticks
to the source material. Uh we're going
to see the difference between those two
in a second. Uh there's completeness,
hallucination, refusal, PII, and
toxicity. Lots of things that lots of
agents need to check are built in. Uh
and for agents, there are evals for tool
use. Did it pick the right tool? Did it
pass the right arguments? Um did it do
something sensible with with the result?
Uh these eval are not magical. They are
just uh prompts that we've already
written and battle tested and made sure
work for you.
Uh
so let's find the judge model. Um
uh Phoenix evals in Typescript uh use
the Versel AI SDK to talk to models. So
any model that the AI SDK supports can
be a judge. Uh in this case I'm using
Claude Sonnet 5.5. Um, the agent runs on
Haiku. Like I said, it's cheap and fast.
Our judge is running on Sonnet because
you want your judge to be more capable
than the agent itself was. So, give it
Sonnet or give it Opus. Uh, or give it
uh even better um give it a model from
uh a different provider entirely. If
you've got an OpenAI key, get OpenAI to
judge the work of Claude. Uh because
Claude has what is known as uh same
model bias. So Claude tends to like the
output of other versions of Claude uh
more than it does the output of uh of
OpenAI or some other provider.
Um
the last line here uh in case you're
wondering is suppressing tracing on the
judge because we turned on tracing
across the board. The judge is itself a
copy of Claude. Uh so by default and in
fact in my test data you will see that I
forgot to turn on uh uh telemetry
suppression. So my traces are full of
the the judge running itself and and
seeing all of the traces from the judge
which you don't need. Um
so every evaluator in this repo gets it
gets this telemetry setting uh so that
the judge stays out of uh our agent. Um
let's start with correctness. Uh which
is the obvious first choice. Is the uh
is this report correct? Um that is one
import and one line of setup. You don't
have to do anything. You just say hey
I'm running the correctness evaluator.
Run it on my stuff and let's see how it
goes. Uh then you call evaluate and you
get back a label, a score, and an
explanation. And the script runs it on
every agent run and logs the results
back to Phoenix. Uh the same way we did
the ticker check. Uh,
I should be able to run that as well.
That's going to take a little while
because it has to actually do some LLM
stuff. Uh,
if it works, it works. If it doesn't, I
have stuff already built in.
So you can see uh in my annotations
column you can see the results of
various evaluations I've already run. In
this case it's showing you the uh
actionability one but you can see uh
correctness, faithfulness, human
actionable uh and mention sticker. We're
going to talk about what all of those
are. But first you're going to see
correctness. Uh correctness on all of
these is zero. Uh,
all 16 reports have been judged as
incorrect. And the reason that they've
been judged as incorrect is because
Claude judges correctness by what it
knows. That's the only thing that it has
available to it. And Claude's knowledge
cut off uh at the moment is in something
like January. So uh my agent is talking
about stock prices in October and Claude
is freaking out and going, "You're
talking about stuff that's in the
future. That's obviously a
hallucination. This report cannot
possibly possibly correct. So our
built-in check for correctness fails
every single report for that reason. Um
which is not terribly useful. Um
so the eval is half wrong and half
right. Seven of in my data, seven of the
16 explanations complain that the judge
can't verify fresh data. Uh which is the
eval definitely being wrong. Um, but
lots of them also point out something
real. Things like the numbers don't add
up or dates that contradict each other.
Um, so a score of zero is telling us
nothing here. It's telling us across the
board that this that this eval is
probably not the right choice of eval.
Um, what we want is a question that the
judge uh can actually answer.
So uh
oh, I told you that already. All right.
uh what we're going to use instead is
faithfulness. Faithfulness is asking a
much better question. It's saying given
the data that you had, did your did your
report make sense? Did is the answer
based in the data that we were given?
This works much better because it can
work with data this exactly the same
data that the agent was given and see if
it gets a report that makes sense. Uh so
that's a question the judge can actually
answer. Uh and the context is already in
the trace. Every web search is its own
span like we saw. Um, every research
turns output is the agent's own notes on
what it found. So my first version, my
first eval uh only gave the judge uh the
research notes and then I read the
explanations and the judge was flagging
numbers as made up uh because my version
of the eval hadn't told it that oh I I
searched the web and actually found this
data. Uh so uh in the version you see
we've given it the full context. um our
get agent runs helper is going to pull
both uh the raw search results and the
notes so that it can see uh what the
research agent found and how it found
that data.
Uh so like I said faithfulness takes
three things. It takes the input which
is what the user asked. It takes the
output which is the report and it takes
the context which is the search results
and the notes that I was just talking
about. [snorts]
Uh and you run it using the same pattern
as before. You create the evaluator, you
evaluate every run, you log the results.
Um,
like I said, it's slower than
correctness uh because the judge is
reading every search. Uh, who has got
any results out of their uh eval so far?
Again, you've got a faster Wi-Fi
connection than everybody else. Anybody
else?
Cool.
Um,
so let's look in Phoenix at my
faithfulness reports. Um,
I got a lot of zeros on faithfulness,
but not all of them.
Um,
let's read the Microsoft explanation.
That was the one that I read that was
most interesting.
Uh, as you can see, next to each one,
you get the explanation. Um, so in this
one, the response adds several claims
that the context does not support. Azure
is the number two cloud provider. The
backlog gives three years of visibility
and there are implied FY202 targets. Uh,
it is telling me what it doesn't like
about uh this thing. It does it's
telling me why it thinks this thing is
unfaithful. Um,
it's complaining that uh some of the
2027 targets are fabricated because
they're not in any search results. Uh,
the Nvidia one is also interesting
if I can find that one.
Right. In this one, it says the response
conflates two different data points.
This is a reasoning error that the agent
that the judge has uh accurately found.
Um
it says the context information this is
fabricated. These are much more useful
results. We've got uh 14 out of 16 uh
reports marked as unfaithful here, but
the explanations are way more useful. Uh
and it's actually doing the thing that
we wanted it to do. Um
so for agents, you can also grade the
tool calls. Uh so we saw the web search
spans inside each trace. Phoenix has
built-in evals for all of those as well.
Tool selection asks did the agent pick
the right tool uh or search when it
didn't need to. Tool invocation asks did
it pass sensible arguments to those
tools like a search query that's
actually about the company. And tool
response handling asks did it do
something sensible uh with the result of
that call.
Uh these are the decisions that can make
a break make or break an agent. Um, and
they all happen before the report
actually gets read. Uh, and we already
know our agent makes strange tool
choices sometimes, like it tries to save
the report to a file. Uh, so we can see
if our built-in eval catches that. Uh,
I'm not going to run this one, but you
can run that one. Um, tool selection
takes three things. What the agent was
asked, which tools it could have used,
and which ones it picked. Uh and the
script goes through every agent turn and
every trace research and writing
separately and collects the tool spans
underneath each one. Um the trace
records which tools the agent called but
not which ones it could have called. So
we have to write that list ourselves uh
in tool selection.ts.
Uh then it is uh the same pattern as
every other run. Uh so npm run eval
tools uh and then you're done. Uh that
one should take about 15 seconds.
So, let's look in Phoenix at
tool selection.
Tool selection. It's helping me out.
All right. So, these are ones where it
has decided that my tool selection was
incorrect for whatever reason. Uh, the
user asked for a concise report based on
prior research. Writing it to a file
with write is plausible and appropriate
since write exists and is safe. Uh,
however, the LLM made a second redundant
bash call. Awesome. Uh, yeah, it sure
did. Um,
the judge failed six that tried twice.
It passed seven. Six of the seven that
tried once. Uh
uh overall 13 of my 16 writing turns
tried to save a file. Um
and only one of these explanations said
that the user never asked for a file to
be saved. So uh is this judge incorrect?
Is the judge uh accurately judging that
the tool call was correct? Um, our
writing prompt said, "Write a concise
financial report based on your research
above." Our prompt is genuinely
ambiguous here. We said, "Write, we
didn't say where to write it to. We
didn't say what to write it for. Uh, we
didn't say who the audience was going to
be." So, the tool selection knows that
and is looking at the input and is
going, "Well, it seems a reasonable
thing for the agent to try and write to
disk here." Uh so again what you're
telling the agent to do and what you're
telling the eval to do interact with
each other. Uh you can't necessarily
trust that the tool call invocation is
going to be right because in this case
the tool call is citing the tool call
eval is siding with the agent. It's like
no the the agent is right. The agent
gave us instructions uh the agent
received instructions and did its best
is basically the eval's position. Uh,
eval results live in the trace as well.
Um,
so if you're looking at the traces in
Phoenix, uh, you can see them here
attached to which trace they got, which
span in the trace they got attached to.
So you see actionability and correctness
got attached to the root. Uh, whereas
tool selection is getting attached to
the specific uh, turn that made that
tool call.
Um, you can filter your traces by any
eval. Uh, you can sort by score to find
your worst runs. You can click straight
from a failing score into the step that
caused it. Uh, from score to from score
to cause in one click. Uh, so all of
that is the built-in eval.
Um,
and the lesson here is that choosing the
right eval beats tuning it. Choosing
correctness was entirely the wrong eval.
It didn't tell us anything. It just told
us a bunch of stuff was wrong. tool
selection did tell us something uh and
faithfulness told us quite a lot. Um
so checking the right eval beats tuning
it uh and knowing which question you're
actually asking is really the core of
getting this right
which brings us to step five which is
writing your own judge. This is where
the eval get specific to your
application.
Uh, and again, this is when people are
thinking about evals, this is what most
people are thinking about, but I wanted
to make sure that you got the basics in
first. You don't have to jump straight
to writing a custom rubric. You can
write code evals to get a bunch of stuff
out of the way. You can write uh you can
use built-in eval to do a bunch of
obvious stuff without having to invent
your own tool calling correctness uh uh
evaluator.
Um,
what I wanted my report to do was give
me a buy, sell, or hold recommendation.
There is no built-in eval that checks
for that because that would be a very
specific thing indeed. So, we're going
to write our own. Uh, every eval prompt
I've seen that works well has five
different parts and we're going to go
through them one at a time. The first
part is you give the judge a role and
context. Uh, a thing you'll see all the
time is you are an expert blah blah blah
blah blah. That does actually work.
That's why everybody puts it in there.
Like it helps a little bit to tell the
to tell the agent what it is. Uh,
telling it it's an expert as opposed to
just telling it that it is running up
something else also seems to make a
difference when they do sideby-side
comparisons. Um, it's just one of the
weird things about LLMs. You need to
tell it it's really smart and it gets
like confident and tries. Um
uh but what really matters is the
context. Um this is a financial report.
Uh we are expecting a report that that
analyzes financial data and tells us
real things. Um
and specifically what we care about is
whether or not you could act on it. So
uh that gives us the explicit criteria
that we include in our rubric. Um so
this is where a lot of people don't put
in enough effort. So don't write a good
response is helpful and accurate because
uh a judge doesn't know what helpful and
it doesn't know what accurate means in
this context. Um a judge can't make a
yes or no decision from that. Write down
exactly what makes a report actionable.
Uh so it makes a specific
recommendation. It names concrete risks
and it looks forward not just back.
Those are things that a judge can look
at and actually check.
Uh, and note that we're not just making
up these things blind. Um, your criteria
come from your error analysis. Uh, only
summarizes data with no interpretation
is a problem that we saw when we were
reading our traces. We are putting that
in there because it's a problem that we
are trying to avoid. Um, that is the
whole point of reading the data first.
Specific criteria give you consistent
judgments and you get specific criteria
by knowing in advance what the data is
going to look like because you read it
yourself.
Part three of a good rubric is to mark
the data clearly. Wrap each piece of
data in its own XML tag. Claude was
trained on billions and billions of XML
tags and it's really good at working
with them. Um,
if you look into the code at our own
rubrics, that's what we're doing. uh our
own prompts [snorts] uh wrap everything
in XML tags. Um and the double curly
braces are template variables that
Phoenix fills in uh with each span's
input and outputs. Uh the reason you do
this is because you want clear
boundaries between what is the input,
what is the output, and what is your
instructions. Uh this helps against
prompt injection, but it also helps uh
the agent just getting confused. uh in
particular it helps you get con uh if
you include examples which we're going
to see mark the example as an example
and not the data otherwise it will get
very confused about that um I love to
include labeled examples but it is in
fact a controversial proc uh a
controversial practice uh in the eval
world um
criteria tell the judge what you mean in
the abstract but examples show it
exactly what you mean as a human, I find
it much easier to do something when
somebody has shown me an example of how
it's supposed to work than if they've
just given me a list of instructions of
how to work. Uh, and, uh, a lot of LLMs
feel that way as well, apparently. Um,
so when you test your rubric, uh, which
we're going to do in the next step, uh,
test it with examples and without
examples and see which one does better.
Uh, because sometimes, uh, examples are
going to help it do a better job. And
sometimes, uh, an example will make it
overfit. It will look at your examples
and say, well, it doesn't look exactly
like my example. Or it will try and make
every output look like your output
example. Uh, which is less helpful.
Um, I ran exactly that test on mine. Uh,
so in the rubric that I used, um, this
was fascinating in a really nerdy way,
which is why I included it. Uh, I threw
out my examples and with the examples,
the judge agreed with me, uh, 15, 15,
and 15 times out of 16 in three
different runs. Uh, and if I threw out
the examples, it agreed with me 16 times
twice, all 16 examples, and 15 times
once. Uh and so I was like I was very
curious as to how throwing out the
examples made it better. Uh and the
specific problem that it was having is
that in one of the reports it did not
include
um
uh it did not include a list of risks.
So as a human I read the report and it
was like Microsoft is a buy and it
didn't include any risks and I was like
that's fine. It's still actionable. It
included a buy. Uh so I marked it as uh
an actionable report. Uh but my examples
said you must include risks. And so the
agent uh the LLM judge was looking at
the rules and and looking at the
examples and saying there must be risks
in here. So this is not actionable
because there's no risks. So that's
genuinely an open question as to whether
or not my human judgment was better or
worse than the judges. The judge was
being very strict and I was being loosey
goosey when I as a human gave myself
golden data.
>> Sorry, can I ask a question?
>> Sure.
>> So what's your hypothesis then as to
without the examples
it agreed with you so it saw that
Microsoft as being actionable?
>> Yeah.
>> Is that is that your hypothesis then
that like simply because you didn't say
risk was a necessary element it felt
that that was a good actionable? I mean,
it's not a hypothesis like the LLM judge
comes with an explanation. So, it says
>> So, it said that that was actionable,
>> right?
>> Yeah. So, like I said, in this case,
it's genuinely unclear whether or not I
was doing the right thing or the judge
was doing the right thing. The judge
decided to interpret the the rubric very
strictly and I when I was marking these
things as human actionable or not, uh
was not being as strict.
Um,
here's an example of an actionable one.
Uh, it has specific numbers. It has
revenue growth. Uh, it has valuation
compared to its sector. It names a
concrete risk. And it ends with a
recommendation you could actually
follow, including when you'd change your
mind. Um, and this is what a not
actionable one looks like. It isn't
wrong. Everything in it is is true. It's
just not very useless. Investors should
consider various faction uh factors is
not a recommendation. Um, now that the
judge has seen both, the hope is that
it's more consistent on reports that
fall somewhere in between. Uh, and
whether it actually is, you find out by
testing.
Uh, part five of putting together a
rubric is you constrain the answer. You
ask it for things that are actionable or
not actionable. A thing you used to have
to do is you used to have to say output
a string and the string must be the word
actionable or not actionable. Uh, you
don't have to do that anymore. what uh
modern evaluators use tool calls uh to
put their output. So those uh the
choices available for that tool call are
defined in the tool call and not in your
rubric. Uh which makes them a lot more
reliable.
So now it is your turn to write the
rubric. Uh open evalactionability.ts.
Uh it has my rubric in it with all five
parts. Um and you can make it yours. You
can change the criteria. You can change
the examples. Uh
what would make you act on one of these
reports? What did you see in your own
traces? Write that down and that should
become your rubric. Um it will take
three or four minutes to run. Who has
managed to stay up with me so far? Like
who is at this point? Excellent. I have
multiple hands. Uh like I said, the last
time I did this workshop, everyone was
completely lost because the 200 megabyte
repo. So the fact that anyone's got it
this is just great for me. Um
this is how you wire it up. You create a
classification evaluator which does all
the plumbing. Uh you give it a name, you
give it the model. Uh you give it your
template. Uh and like I said uh out of
band you give it its out its options. So
you give it its choices which are
actionable with a score of one and not
actionable with a score of zero.
Um,
so let's look at actionability in
Phoenix. [snorts]
It's so cold in here that my fingers
have gone all numb and I can't type
properly.
Okay.
So, the report analyzes JPM's rate
exposure and loan growth uh and a
forward-looking output, but makes no
buy, hold, sell recommendations.
Fantastic. It's doing exactly what it's
supposed to do. Uh it is complaining
about uh the lack of recommendation of
concrete recommendations. Um
before we look at all of these
recommendations, we should look at the
split in the recommendations. Uh in my
data, five of 16 reports were actionable
and 11 were counted as not actionable.
Uh and that is one of the most useful
types of evals you can get. An eval
where everything is perfect is not
particularly helpful. An EVA where
everything is wrong is also equally
unhelpful. An EVA where you've got an
even split that is a hill that you can
climb. You've suddenly got uh some
you've got a def a set of examples where
things are actually working, a set of
things where uh stuff isn't working and
you can start figuring out the
differences between them. Um
so if you click through these traces,
I'm not going to bother clicking through
all these traces. In Rivian it says it
never makes a buy, hold, sell
recommendation or any equivalent next
step. For Nvidia, it said the closing
investment thesis risk level is
moderate, is vague rating, not guidance.
And uh for Meta, the verdict is the is
only that the position is solid. So this
is the same problem over and over. It is
refusing to give concrete buy, sell,
hold recommendations.
Um,
if we
uh we can open the Phoenix prompt
template. I'm not going to do it now.
Um, but uh there's one more rule for
rubrics, which is that you should treat
eval prompts as code. Your eval prompts
going into your into your custom eval
are extremely sensitive to small changes
in wording. Um,
so, uh, one example of that I ran into
while making this was, uh, I told you
that you should put XML tags around
stuff. I forgot to put XML tags around
my examples to begin with. Uh, and with
my examples as plain text, uh, I got a
string of not actionable stuff, uh,
because it was getting confused about
what the data was and what my examples
were. And when I wrapped them in XML
tags, everything suddenly became
actionable because it could tell what I
was talking about. Um,
this is there was no other change. I'd
given it the same data, the same
instructions, the same input and the
same output every time. Uh, it just got
less confused in the evaluator as to
what was happening. Uh, so you have to
treat your evals as code. You should
version them, you should check them, and
you should test them.
Um, as I mentioned earlier, uh, there is
a trap to fall into with evaluators,
which is to try and write write one
evaluator that does everything for you.
It is called the god evaluator because
it is such a a common pattern. Uh, you
try and get it to check accuracy, tone,
completeness, formatting, policy all in
a single prompt. Uh, and it is a
nightmare because if it fails, what
thing failed? Was it inaccurate? Was the
the tone wrong? Was the faithfulness
wrong? which of the many many many
things that you've told this god
evaluator to evaluate is it actually
wrong and you try and solve that by
giving it 15 labels that it can spit out
uh and the whole thing becomes very hard
to track. Uh the best practice is to
split this up split your evaluators into
as many dimensions as you are testing.
So one for faithfulness, one for
correctness, one for actionability.
Um,
and you should also know which one of
your evals is a guardrail and which one
is a north star. So, a guardrail is
something that should block the release.
So, if the agent is making up a stock
price, that should halt shipping. Uh,
but north stars are things that you're
aiming for. So, suggests other stocks
worth a look would be nice to have. That
would be a good thing to include. Your
eval can look for that, but it doesn't
have to gate shipping on that.
Which brings us to step six, which is
testing your tests. We've built a judge
and it says that some of our reports
aren't actionable. Uh but can we trust
the judge? How do we know that the judge
is right? Uh the trick to remember is
that your judge is a classifier in the
classic ML sense. Uh it is looking at a
report and it is predicting a label as
actionable or not actionable.
Predictions uh can be right or wrong. So
like any classifier, you measure it by
comparing its predictions with the
truth. Uh, and here the truth is what a
human expert would say. You get to judge
uh you get to mark the judge's homework.
Uh,
in this case, the human expert is going
to be me. I'm going to be deciding
whether or not stocks are buy, sell, or
hold. Uh, not necessarily the expert
that you want. Uh, but we're doing our
best. It's just a demo. Um, how you do
this is very simple. You open up a
trace.
uh you click the little pencil button
and you can add annotations. So I have
created an annotation in advance called
human actionable uh and I can set it to
actionable or not actionable and I can
very quickly
uh click through all of my traces and
set that on each one which I've done in
advance. Uh this is where you would get
uh a domain expert involved. You would
throw them at Phoenix. You'd say here
are 10 traces, here are 20 traces.
there's 50 traces. Go through and read
the output and give me give me your
golden data set about whether or not
these things are good. Um,
[snorts]
I sat down and labeled all 16 of my
reports properly against the same
criteria that I gave the judge. Uh, and
those are sitting in your seed project
so that you don't have to do that
because that would take you a long time.
Um, what you're building when you do
this, like I said, is called a golden
data set. Uh it's examples where to the
best of human knowledge you know that
the answers are right. Um it is a lot of
work so you should make that work count.
So you should give yourself the same
specific criteria that you gave the
judge. That was the error that we were
talking about earlier. Uh where I was
not exactly reading the rules that I had
put into my eval criteria. Right? I was
disobeying one of my own rules. my rule
said uh must include risks and I said
that this report is fine even though it
doesn't include risks. Uh and as a
result me and the judge disagreed and I
feel like the judge was actually more
correct than I was. It was being
stricter. Um so uh your enemy here is
fatigue. Uh if you give yourself a
hundred traces to judge by trace 50,
you're going to be really bored of
judging traces and you're going to get
lazier about it. Uh so it is better to
have 50 really well-labeled
uh examples than a hundred where you
were just clicking through and saying ah
this looks fine. Uh the the higher the
quality the data in your golden data set
uh the more reliable everything is going
to be.
Um
and one of the best things that you can
do is that uh is continuously add to
your golden data set. when you see a
tricky example, when you see something
strange happen in production, figure out
what the answer should have been and put
it into your golden data set.
Uh, a few good rules for human go for a
good golden data set is that you should
write test tasks a human could pass. Uh,
if your agent fails a task every single
time, that is almost always going to be
a broken task, not a broken agent. Um,
and for each task, you should have an
answer that you know is good, which
proves the task can be done. Uh, you
should also test in both directions. If
you only check, for instance, that the
agent searches the web when it's
supposed to search the web, you're going
to accidentally train your agent to
search the web every single time, all
the time, even when it doesn't need to.
Uh, and here's a rule from machine
learning that applies to judges as well.
Don't tune on your test set. Uh, split
your labels into two groups. One that
you use to tune your evals and one that
you use to test that they are working.
Uh when you only have 16 answers in your
golden data set, that makes it your test
set very small. Uh because the rule is
usually 75% in the tuning set, 25% in
the test set. So there's only four in
our test set. Uh but if you were up to
100, that would be fine. Um
Phoenix data sets have splits built in.
So this is very easy to do. Uh
see what that looks like.
uh
so first it builds the golden data set
with splits. It finds every report with
a human label. Uh
uh and each one becomes an example in a
Phoenix data set. The input is the
report. The expected output is the
human's label. We sort them by span ID.
Then every fourth example goes into the
test split and the rest go into dev. Uh
sorting first means that a report always
lands in the same split however many
times you run this. Uh, and span
[snorts] ID links each example back to
the trace it came from. Uh, so you can
always click through to the original
run.
Then we run the judge against the
humans. This is an experiment which is
something that we're going to dig into
in a little bit. Um, but for now uh an
experiment takes a data set. It takes a
task task to run on every example uh and
evaluators to score the results. The
task here is our judge and the evaluator
is a tiny Kodi val which checks whether
the judge's label matches the humans. Uh
notice that we only run it in the devs
split. Uh you can run this yourself by
running npm run meta.
[sighs]
Let's see if we can get it to go.
It's going to run an LM. So, uh, I'm
going to assume that it does the same
thing that it did last night. Um, the
script should print a little table at
the end. Uh, and on my 12 dev reports,
the judge and I made the same call every
time, which is great, but it's also only
12 reports. Uh, so read that as, you
know, no sign of a problem yet. you're
going to want a larger test set when
you're running this in production. Um,
cool. It actually completed it. Uh,
the more interesting part is the two
ports that I the two reports that I
found hardest to label. Um,
so in my Phoenix data,
uh, there's Coca-Cola and there's
Microsoft.
Um
the the first one is Coca-Cola. The
Coca-Cola is the one that flipped uh
when I changed from the XML tags to the
uh from not having XML tags to having
XML tags. Uh this is where when it got
the examples it got better. Um
borderline for me turns out to be uh
borderline as well. the it the report
calls KO ideal for conservative income
oriented pol uh portfolios uh which
sounds like a recommendation. So as a
human I went back and forth on whether
or not I should count that as a
recommendation. Ultimately I decided it
did not uh but the judge also goes back
and forth on whether or not that counts
as enough of a recommendation.
Um
and the second one was Microsoft uh
which I'm not going to bother to click
into which is the other way around. The
report says buy with reasons uh and a
time horizon. Uh and it never mentions a
single risk. This is the one that I was
talking about earlier. Uh my rubric
lists name concrete risks as a
criterion. Uh and I decided that was
fine and the judge decided that that was
not fine. It said it was weak on risks.
There is no risk section. It clears the
bar for actionability but though not by
much. So, the judge looking at this
stuff came up with exactly my human
judgment on whether or not this was an
actionable report, including the
ambiguity.
Um, and that ambiguity is still in our
rubric
because we haven't changed it yet. Uh,
so it's very tempting to fix it. So, I
tried I added one sentence uh which was
a report is actionable only if it meets
all four criteria because previously
that was ambiguous. I said a report
should include all of these things. I
didn't say that it must. Uh so you can
change the you can change the rubric and
be more specific and say yes this
absolutely must contain all these four
criteria. Uh and on dev uh that broke
Microsoft my 12 out of 12 agreement
became 11 out of 12 agreement. Um
and uh it also in the test split it
broke Apple uh because Apple didn't have
enough uh a big enough risk section as
far as the agent was the judge was
concerned. Um
what that tells you is that I could
change my rubric and make my eval worse.
Uh I can make my eval less helpful. I
can make my EVA less like what a human
would do. Uh even though I'm trying to
be specific.
Um the script also prints precision and
recall. Uh precision these are very
important things again borrowed from the
ML land or rather from stats land. Um
precision asks when the judge says not
actionable how often is it correct? And
recall asks of all the reports that
aren't actionable how many did the judge
catch? Those two sound very similar but
measure different things. Um,
in most cases, you're going to want to
prioritize recall because what recall
gives you is it catches everything, but
it gives you high recall catches
everything, but it will give you uh
false alarms. A false alarm costs you a
minute or two when you look at a report
that turns out to be fine. Uh, but a
missed failure uh would give you a bad
report that reaches a customer. Um, so
you have to trade one for the other. If
recall goes up uh um then uh precision
will go down and vice versa. So for your
application you have to decide whether
being accurate uh as in throwing away
some things that were actually correct
uh but but uh you decided they weren't
is better or worse than getting false
alarms where you say something is
important and it turns out not to be. Um
judges also have biases. Uh I mentioned
one of them already. Um one is position
bias. Given two options, they tend to
prefer depending on the model either
which one comes first or which one comes
last. It depends which way the model
around which way around the model was
changed. Uh but you should swap your
options so that it's not always looking
at those uh things in the same order. Um
they have length bias. Uh, judges prefer
long answers and they also have a
confidence bias. Judges prefer answers
that sound fluent and confident. Um, and
the one that I mentioned already is
self-preference. A model judging its own
output tends to rate it higher. Uh,
which is why we judged Haiku with
sonnet. Uh, and ideally you judge haiku
with something from open AAI.
Um, but before you get too worried about
how much you can trust a judge, it's
worth noting that human judges also
disagree with each other a lot of the
time. Um, if you give two experts the
same outputs in the same rubric and
measured how often they agree, uh, there
is a standard score for that called
Cohen's Kappa, uh, and for this kind of
task, it's often as low as 02 or.3. Uh,
which is to say they agree with each
other not very much more often than just
random chance. Um [snorts] so the bar
for your human judgment is h for the bar
for your judge is human performance and
h human performance uh is not actually
that good when you compare humans to
each other. So having a judge that
disagree you don't do not need a judge
that agrees with you 100% of the time.
Uh your judge is never going to agree
with you 100% of the time. What you want
is a judge that does better than another
human doing the judge would be. uh
because your judge can run across
thousands of examples and help itself
out that way. Um
one last principle on judges uh is that
failures should seem fair. When
something fails, it should be obvious
what the agent did wrong. If you look at
the failure and go, "Well, actually that
looks fine to me," then the problem is
probably your eval. Um
there's a famous example of this uh when
Claude Opus 4.5 first scored 42% on a
benchmark called Corebench uh which
tests whether agents can reproduce
scientific papers. Uh anthropic were
upset about that low score. Uh so a
researcher ran the actual transcripts
and found uh that uh Claude was just
being uh right in a different way. Uh it
the test expected uh six digits of
precision and Claude gave the right
answer to two digits of four digits of
precision rather. Um and the test said
that was wrong. There were ambiguous
task descriptions. Some of the tasks
couldn't be reproduced at all. Uh so
Anthropic went through and they fixed
all of the tests and they said these
tests could be better. Uh and magically
they got 95% on the eval.
Um this happens all the time. SWEBench
and all of the other uh benchmarks that
you see are constantly being
re-evaluated and manually tweaked and uh
that is why you see version two, version
three, version four of of uh the famous
benchmarks uh because people are
constantly finding that the benchmarks
are not actually as good as they could
be and your evals are going to end up
with the same problem. Uh so you need to
be constantly re-evaluating your test
set.
Uh which brings us to step seven which
is uh experiments. We've got evals that
we trust. Now we are going to use them
to actually improve that the agent and
prove that the fixed worked. Uh
I'm going to go a little faster now as
I've been going on a very leisurely
pace. I'm getting beginning to run out
of time. Um so the here's the problem.
We know that some reports aren't
actionable and we know why. So we change
the prompt and then what? How do you
know that it worked? Uh, how do you know
that you didn't break something that was
working before? If you run it on a
couple of examples and eyeball it, then
you're back to vibes. A prompt change
that you haven't measured is just a
vibe. What you want is a controlled
comparison. You want the same inputs,
the same eval before and after. That is
an experiment.
Um
so uh what you can do in Phoenix is you
can take a bunch of your evals that you
have filtered down to not actionable say
uh and you can select them and you can
add them to a data set. Um
that gives you a set to test against uh
against specific things. Um I'm not
going to do that since I've already done
it over here. Um
Um once you have a data set you can
create turn that into an experiment and
run uh your experiment against only the
data set only against the evals that
were failing as opposed to against your
entire set every single time which you
know if you've got a decent sized split
and a decent sized test set is saving
you thousands and thousands of tests
every time. Uh
now we're going to fix what the eval
found. So, uh, if you're still coding
along, congratulations. Open prompts.ts.
There is an improved version of each
prompt. Uh, or you can write your own.
Um,
and every change maps to a finding. So,
the judge said, uh, makes no
recommendation, so we asked for an
explicit recommendation. It said
mentions risks with no evidence. So, we
asked for risks with supporting data.
Faithfulness found invented numbers, so
we said use only numbers that appear in
your research. uh and reading traces
found that the agent uh was trying to
save files all the time. Uh so we tell
it to reply with the report instead.
We're not guessing here. We are coming
up with specific things for the agent to
do as a result of the previous results
of our evals. Uh
this is what the experiment script looks
like. An experiment is a data set, a
task and evaluators. The data set is the
one that we just created. Uh the task is
a function that just runs the agent on
each example. Uh
in this case, we're running the entire
agent, but we could be running it on a
specific subset of the agents behavior
or a specific subtask uh if we wanted
to. Uh our task hands back the report
and the research. So each eval gets a
small wrapper that picks out the fields
that it needs. Uh and then faithfulness
gets the research as its context. The
same as before, uh Phoenix runs the task
on every example. It scores every result
and it stores everything so you can
compare. If you want to run this, you
can run npm run experiment and it will
take about four minutes to run. Um,
but I'm running out of time so I'm not
going to wait for four minutes. Uh, I
ran mine ahead of time. How many
examples do you need? Uh, is a really
good question. Uh, 10 to 20 examples
gives you a rough direction of where
things are going. Is very useful in dev.
Um, if you're getting into production,
uh, you're going to want hundreds of
examples. Um, that is going to take a
long time, but is, uh, very worth it for
accuracy. Um, for every, uh, to have
your error bars on your accuracy, you
need to quadruple the number of
examples. So, uh, going from 25 examples
to 100 examples is really, really
helpful. uh and is not that much effort
going to get that big a jump again you'd
have to go to 400 examples which begins
to get into the territory of you're
never going to bother to do this uh but
the bigger the better uh and the more
production failures you throw into your
data set the better
um so I ran mine three times and the
reason I did that uh is because the
agent is non-deterministic each run of
each example uh can mislead you in
either direction um And there are two
useful ways of thinking about how an
agent runs uh when it runs multiple
times. The first is called pass at K
which is uh does it succeed at least
once in K tries and then there is pass
to the K which does it increase every
single time uh does it pass every single
time I run uh K times. Um
so as K goes up those two numbers
diverge. Uh the more tries you give it,
the more likely pass at K is to succeed
because it succeeds at least once. The
more tries you give it, the more likely
it is to fail at least once and then
pass it K pass to the K will go down. Um
a coding assistant gets that gets it
right on the second try is fine. So pass
it K is fine. Um a support bot that's
wrong runtime in every five is a huge
problem. And a financial anal analyst uh
that gives inaccurate recommendations is
also a huge problem. Uh so you want pass
to the K. You want it to pass every
single time for those.
Um
when you're improving an agent, there's
an order of operations based on how
useful making a change is going to be.
The first one is data quality. If your
underlying data is bad, if it's hard to
read, if it's difficult to interpret for
the agent or for the judge, uh then
nothing else you do, nothing else you
tweak is going to be useful. Once you've
got good quality data, then you move to
the prompts. Uh that is what we've been
messing with mostly today. Uh is to make
things better at the prompt level by
changing our rubric, by changing our
agent.
Then there's model choice. Uh model
choice has a lot of leverage, but it
also changes a whole bunch of stuff at
the same time.
uh and also the usual way that you're
going to change your model is you're
going to change it to a bigger model and
that makes things more expensive. So
that is uh creates a tradeoff uh that
you don't always want to make. Uh and
finally there's hyperparameters.
Hyperparameters are things like
temperature and stuff like that. Uh
they're so useless that uh people have
that modern models have stopped allowing
you to tune them. You can't pass
temperature to model to modern claw
models. Um so if you're tempted to it is
the least useful thing that you can
pass.
Um so if we're looking at my experiments
you can look in your seed data and get
see see the same experiments. Um
you'll see that uh
as I improved as I improved my runs I
went from uh
16 out 15 out of 16 to 48 out of 48. and
went from 5 out of 16 to 48 out of 48.
And faithfulness went from 2 out of 16
to 3 out of 48. Uh, which is not that
good, right? Like we really should have
done better on faithfulness with my
improved prompt. Um,
the
uh
important thing is did anything that
used to pass break? We can filter down
to the passes split. I'm not going to do
it in the UI right now. Uh, but all of
the five reports that passed previously
as I improved my prompt still passed.
Uh, so actionability went straight to
perfect. Um, but faithfulness was bad.
Faithfulness uh went from 2 out of 16 to
3 out of 48. Uh, even though the prompt
literally says only use numbers that
appear in your research. Um,
so we fixed what we measured in a single
line of the prompt. Uh, didn't fix the
agent making things up. That is the next
thing that we have to fix for this
agent. Uh we have fixed whether or not
it is making a good judgment call. Uh
but we have not fixed uh that it is uh
inventing the data some of the time.
Um
if we want to we can look into uh each
of the runs and you'll see that each of
the because it's nondeterministic each
of the runs are coming up with different
advice. Um, but I'm not going to do that
because I'm running out of time and I
want to get to some other stuff. Uh,
let's get to Okay, cool. Um,
a good eval like the 56 the 511 split
that I was talking about on my 16 data
sets. That is what is called a
capability eval. A capability eval is a
thing that our agent can't do yet. And
it gives us a hill that we can measure
ourselves climbing. Uh when it passes
reliably, when you get a test that
passes 100% of the time, you don't throw
it away. You turn it into what is called
a regression eval. That is the kind that
you can put into your CI and say this
used to pass 100% of the time. If it
suddenly stops passing 100% of the time,
then we can call that a failure and we
should stop release. Um how do we climb
this hill is the question. uh
we could work on the prompt again or uh
we could do the thing that I said that
we would do which is we can upgrade the
model. Uh so you can run the experiment
again by passing in a new model haiku
5.5 and then run npm experiment. Um,
I said at the start of today that you
can't switch models without eval. And
this is what it looks like when you can
switch a model with an eval because we
know now that we are measuring all of
these things. Um, with three
repetitions, it takes 13 minutes, which
is more time than we've got left. So,
I'm just going to skip to the results.
Uh, here is Haiku 4.5 versus 5.5. Uh,
faithfulness improved. It got more than
three times better. It is still
terrible. This agent is still making
things up all the time.
Uh, but consistent calls got better. So,
it is at least making the same call over
and over. Is that good? Uh, it's also
costing four times as much money. Is
that worth it? Uh, is a question that
you need to make for yourself in
production when you're doing this kind
of thing. Um,
one of the ways that it got more
consistent, one of the ways it stopped
varying between buy and sell between
calls, uh, is it just got more
conservative. Haiku 5.5 uh it turns out
just says hold all the time. Uh so uh is
that better or worse? Probably worse. Uh
probably we need to iterate on Haiku 5.5
being too conservative uh about things.
But at least we know now that something
has changed and that the conserviveness
is a problem with Haiku 5.5.
Um that is the problem that I found. It
went it went to 41 of out of uh 45 calls
it said uh hold 41% of the on 41 of the
times. Um which is perfectly consistent
between runs. Uh so it it got better at
the uh consistency check that I was
talking about over here the consistent
call. Uh but it got there by just
picking the same answer every single
time.
>> [snorts]
>> Um
but that is the eval iterate cycle. Uh
and the cycle is where the value is not
anyone's score. You run your evals, you
read the failures and the explanations,
you spot the pattern, you change the
prompt or the tools or the data and you
run the experiment again. Did it get
better? Uh your evals can now answer
that question for you. You can go from I
think it works to I can show you it
works. Uh
I have just enough time to talk about
how to do the last step which is eval in
CI.
Uh more and more teams that ship AI
quickly write the eval before the
feature. That's called eval driven
development. Um say you want your
support agent to always check who the
customer is before giving a refund. Uh
you can write the eval that checks for
that first and now done has a definition
that you can measure a hill that you can
climb from the start. Um,
we talked already about capability
capability evals and regression evals.
Um,
here's how uh to create a eval that runs
in CI. Um,
if you've never used VEST, VEST is a
JavaScript testr runner and Fenix can
plug straight into it. Uh, if you open
agent.eval.ts, you'll see that it looks
like an ordinary test file because it is
one. There is a describe block and a
test for each query in our regression
set. So Coca-Cola, Apple versus
Microsoft, Rivian, uh, and the fake
ZZZQ.
Um, each test runs the agent, logs the
report as the output, uh, and then runs
our evals on it. And the same ticker
check and actionability judge that we
wrote earlier. We don't have to add new
evals for CI.
Uh, then at the bottom, we gate the
build on acceptance criteria. This is
where I talked about guardrails and
northstars. Mention sticker is a
guardrail. It has to be talking about
the right company. Um actionability is a
target. The average has to stay 08 or
better. Uh because an LLM judge can be a
bit noisy on a single report. So we gate
on the average uh not on just one. Uh
and then you can run npm test uh and it
runs like any test suite. Um and at the
end the reporter prints out a scorecard.
Um, and that'll take about four minutes,
which is more time than I've got left.
Um,
a red build. If a failed build, if your
build fails, this is what you'd get. All
four tests ran and every report
mentioned its ticker, but Rivian's
report wasn't actionable. So, the
actionability average came out at 75.
Uh, it doesn't say you failed. It just
says that you missed. Um,
but, uh, a green run, uh, is where all
of those pass. Um,
I'm not going to show the experiment
view because again, I'm running out of
time. Uh, but when a build fails, you
don't just get a red cross. You get an
explanation that says whether things are
good or bad and why they went wrong. And
that is the important thing. Uh, this
same test suite can be run in GitHub
actions. Uh, it starts Phoenix as a
service container. Uh,
but now we've done everything that I've
said that you can do. uh you can run
your evals, you can test things, you can
make sure uh that it matches your human
judgment, you can put it into CI and you
can make sure that your builds are gated
on whether or not uh the LLM's judgment
of what you've encoded as the definition
of good uh really works.
Um
and there's something I love about this
which is that anyone who knows what good
looks like can write evals now. uh your
product managers, your support team,
your person in sales who keeps hearing
the same complaint. They don't need to
write TypeScript. Uh they just need to
describe what a good answer looks like
uh and give it to you or even better
just give it to a coding agent which
will then write all of the evals for
them.
Uh you shouldn't run your whole agent on
every single commit because uh it's
going to take a really long time and
cost you a whole bunch of money. Um, but
now you've got the repo I promised you.
You've got all of the code. You've got
all of the examples. You can see how
everything is done. Uh, you can point
your agent at it and say, "Do this, but
for my codebase," uh, and your agent
will figure it out. Um,
there is one thing that we didn't get
time to build today, uh, which is, uh,
once you're live, you should keep
evaluating. You should run your evals on
a sample of real traffic, uh, and alert
when scores drop and stay down. um not
on every single failure because one
failure would be noise. Um but if you
get a trend in failures, uh production
monitoring is incredibly useful and eval
can get you that as well.
So this is the full cycle that we built.
We traced, we read, we evaluated, we
checked, we improved, uh and we locked
it in with CI. Uh but you don't have to
do all of the stuff that you've learned
today on Monday. You can start small.
You can just instrument your agent. you
can just read some traces. You will get
information reading 12 traces that you
wouldn't have got uh by just looking at
the output. Um so run them. Look at the
results and build from there.
Uh
so go try it on a app of your own. This
is the repo that I said that everything
was in. Uh the Phoenix docs are there.
Uh Phoenix itself is open source. So you
can mess with the code and tell us that
we got stuff wrong in there. Uh and that
just on time is it. Thank you very much
everybody. [applause]
