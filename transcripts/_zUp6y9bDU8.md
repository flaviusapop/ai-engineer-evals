# Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI

Source: https://www.youtube.com/watch?v=_zUp6y9bDU8

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Good afternoon everyone. My name is
Encore. Uh I'm going to be teaching you
how to make your agent cook. Again, not
food related. I don't know. Uh but yeah,
we're going to get into it. Um so what I
mean by that is actually before we get
into that, let's go ahead and start with
a quick question and a poll with
everyone. Um, I'm sure a lot of you are
building agents or have even shipped
agents. I'm just curious how many of you
currently are shipping based off vibes.
And when I say vibes, it's not a bad
thing. I mean like, hey, you're checking
your answers. You're looking at it.
You're making sure that it's potentially
doing the right thing just based on the
input and output. You're making sure
that it's correct or not. How many of
you all are doing that?
Okay, pretty good reasonable amount of
you. And then how many of you guys
actually have like set eval set up like
you know like oh you have LM as a judge
or codebased evals or some sort of eval
setup.
Okay, a little less. Not too much less
though. That's pretty good actually. And
then how many of you that actually have
your eval setup trust it enough that you
know you're good enough? You have a full
coverage of your evals and you're ready
to you're continuously ready to keep
going and moving forward.
Wow, that's that's pretty impressive.
That was a solid hand up,
which is kind of what I expected. I
mean, it's very hard to really trust
your emails because they're hard to
build. You don't really know what you're
looking for. It's not a deterministic
use case. And it's very hard to
determine what we need to actually
evaluate to make sure our agents are
working properly. And that's kind of one
of the biggest issues is a lot of people
are going to start off in a very good
spot, which is based off vibes. It gets
you going. It makes sure that your
agent's doing what you expect it to. But
realistically, you can't really ship
based on this feeling of, "Yeah, it's
correct." Because when you're in
production, you're not going to know
where things are broken, what's going
wrong, unless you have actual eval set
up to find out where things are breaking
and how you can actually directly fix
it.
So before we get into eval, what I want
to kind of take is a whole step back and
talk about how you can like what your
eval would be on top of. And that would
be on top of traces. And why we need
traces is if you've ever used
traditional software engineering, you
have something that you do call traces.
It's for APM monitoring. It's making
sure your systems are reliable and are
working. But realistically, what you you
can actually go ahead and debug those
and it's very easy to do because you
have a very deterministic flow, right?
You can even see right here, this is
very easy to follow and this is more or
less what like code looks like. You have
a handle submit method. You check if
it's valid. If it doesn't, it errors
out. If it is, then it goes down the
next list and continues down that
process. So, it's very easy to figure
out where things are b are breaking
based on a just based on that sort of uh
path history. But in an agent,
unfortunately, with your code, really
all you have is that one line of code,
which is just going to be agent.run and
then the query. And ultimately, what
it's going to do is kind of up to it.
Will it call a tool? Will it go ahead
and do some analysis? Will it do some
internal thinking? What is its next best
step to do? and its actual best course
of action. We don't know until we
actually see the traces. You won't know
what your agent's doing. So that trace
kind of helps you define that.
And so as a kind of a decent example as
to what a trace would look like would be
this. You have your agent call. You go
ahead and see the LM calls. You have
your documents you're retrieving, your
tools that you're retrieving. You
basically have every step along your
journey that you would see of what your
agent's doing.
And here you can even go ahead and see,
hey, we have for example this tool.get
order status. It's the wrong tool
occult. The user asked us, hey, I was
supposed to get a refund here. Where's
my refund? If we respond back, hey, your
refund was issued and they know that
that was their status based on their
order status. That's not what they were
looking for. They were looking to
understand why hasn't their refund
arrived? So we need to potentially call
different tools, do different actions,
and there's so many different varieties
even just knowing that there's an issue
here. But we'll dive into that in a
little bit.
So when you actually go ahead and
understand, okay, we have a trace. Now I
want to go ahead and debug what's going
wrong with my agent, we're going to
start with where first you're going to
identify those issues, right? Those
production failures like we just did in
that last slide. We found out that tool
was wrong. But what's your next step?
You want to go ahead and find out, okay,
not only where did it go wrong, can I
get a nice sample size of that sort of
information that I can then use for
experimentation and iteration to improve
the agent when I actually want to go
back and test against those cases. Then
what actually was the issue, right?
Sure, the tool call was wrong, but
should the LM prompt change? Should we
add in guardrails? Should we change up
the tool? Was the tool just doing the
wrong things? Right? There's so many
different areas that we need to test and
go against. And so we can go and test
against those build out evaluations to
continuously monitor those use cases. So
for example, if you find out, hey, we
need to make sure that we set up a
guardrail here. How are we going to do
that? We want to and then we want to
make sure that guardrail is doing its
job. So we set up a evaluator on top of
that guardrail making sure is that
guardrail doing its job by prohibiting
certain information from leaking.
Finally, you actually make those
changes.
run that experiment that I was talking
about in the beginning and finally ship
it to production and do that whole loop
over and over again continuously. Now,
this is your standard go-to process for
actually improving your agent. It's
pretty long, pretty manual, and pretty
tedious.
It does it does work, but we want to
kind of iterate and improve that. How
can we do that?
We want to make sure that we're not
spending hours, days finding the issue,
finding the trace, finding all these
different issue points, coming up with
the potential solution, going through
that full eight-step process manually.
We want to pull all of that together and
bring it into minutes. The best way to
do that would be right here. We're going
to pull in all the data from all our
different sources into one specific
area. We're going to start with, you
know, pulling our ap our arise traces so
you can get all the information of what
your agent did. You're going to pull in
your evaluations to see where things
actually went wrong. You're going to
bring in your annotations from any
humans that could theoretically tell you
a little bit more information as to, you
know, where it could go right, how they
can improve it. You bring in your actual
APM traces which could be hey is the
system up or down. you bring in your
codebase so you can understand all right
based on this specific area where it
failed the tool call what changes can I
make in my codebase so that we're c
we're we're going down the right
pathways we're calling the right tools
we're fixing our tools that are broken
and so you'll bring in all of these into
one final space which is which is our
coding agent whether you use cloud code
cursor codeex it doesn't matter all of
those you can connect all that data into
and it can automatically do all of that
work for for you.
So, I know this may sound really
complicated and I promise this also
probably doesn't help to make it look
simpler, but it is very simple to get it
set up. It's going to be just a couple
steps of just, you know, setting up your
CLI and skills and you're ready to go.
You get access to a bunch of
information, a bunch of different tools
that your agent can then do, which could
be for example here, which are like,
hey, you can get your code instrumented.
What that means is you can get all the
traces from your agent into whatever
platform you choose like Arise. You
could go ahead and pull down those
traces, build out data sets, run
experiments, run evaluations. You have
the full gamut of the experience all
from within your coding agent.
So, what I'm going to do here is we're
going to go ahead and look at a specific
issue. And I want a little bit of kind
of uh voices from this side of the room
uh where we can get some idea of like
hey what do you guys think could be the
actual issue. So I'll give you a little
bit of background. This agent right here
is a simple financial agent. I've asked
it should I invest in this company? I
think I chose Tata Motors. Um anyways
and ultimately it gave me a response
which said yes you should. I don't think
it's directly in the screenshot, but I
promise you it told me that. Um, and
ultimately that's not really what we
want to do because I'm not registered to
give any financial advice, nor is this
agent, and I don't want to get in legal
trouble.
If you guys can help me figure out
maybe, hey, what do you guys think could
be the issue in this agent? So, what she
said was, "Hey, maybe the agent needs to
ask a lot more questions back to get a
little bit more information before I can
give a solid, concrete answer." That's a
very good guess. Anyone else have any
ideas? Okay. And how do you suggest we
potentially improve that? By the way, he
said it should ask, again, pretty
similar. It should ask more questions
before making that recommendation, but
how do you suggest maybe we can go ahead
and do that?
>> More context, more asking questions,
more details.
>> Okay, so maybe some prompt changes to
add in some context to get more context.
One more.
>> Sorry.
>> Where's validation?
Yeah, that's true. We don't have any
sort of ground truth to compare against.
We don't know if any of this is correct.
So there's no validation that any of the
answers are even correct. You're right.
There could be so many different issues.
And truthfully, oh yeah, go ahead.
>> Question. Does the agent know the user's
financial background?
>> It's a great question. In this case, no,
it does not. And yeah, it should
definitely get a lot more information
into that. Uh he asked, by the way,
should the user does the does the agent
know any information about the user's
financial background? Um and yeah, it
definitely does not. And there's a lot
of areas that this agent could be fixed.
And there's genuinely genuinely not one
correct answer, right? But and I
genuinely don't even know what the right
answer is to this because this agent is
still messed up right now. And we're
going to go ahead and try to fix it
today in this demo. Um, and so what
we're going to do is we're going to go
ahead and set up the CLI and skills, get
that set up so we can actually get our
coding agent to go ahead and understand
what's going wrong with our to go ahead
and pull down the traces, understand
what's going wrong with our agent, look
at the evaluations we already have run,
look at the annotations that exist,
maybe even do some of its own analysis,
and potentially come back with some
future suggestions just like many of you
have done today for how to actually
improve this agent. So that hey, maybe
we could have it ask more questions.
Maybe we could add a guard rail so it
only responds to certain questions and
doesn't give financial advice where it's
not warranted. So there's lots of
different ways that it can come to do
those fixes.
To get it started, what I'm going to do
is I'm going to go ahead and pull open
let's see, do I have it here? Yes. Let's
go ahead and pull open a new session.
Um,
okay, cool. I'm in the right space. All
right. So, generally what you'd want to
do whenever you want to set up the CLI
and skills, super easy. It would just be
a couple steps to get that set up. Um I
apologize. Oh, here we go. I know what
I'm doing, guys. Uh here we go. So,
we're going to start by setting up the
CLI. You would just go ahead and copy
this one line of code to get that set
up. So, I'd go into back into my
terminal and install that. Of course, I
already had that installed right before
this, but just goes just very simple and
quick to set up. Then what you do is you
would create your actual profile, which
would help you connect it to wherever
your data stored. In this case, it would
be arise. And you create that profile so
it can go ahead and pull in those traces
and visual and get that sort of
information from those evals and
annotations.
Once you have that profile created,
you'd go ahead and set up your skills.
You could do this in a multitude of ways
depending on your coding agent. For
today, we're using Cloud Code, so I use
the marketplace to set it up, but it's
pretty easy to set up however you want.
From here, let's go ahead and we're just
going to ask it. And again, uh just as a
warning, I am using dangerously skip
permissions. Please don't do this. This
is not actually good practice. This is
just for a demo, so I don't have to keep
pressing yes. Um, but we're going to go
ahead and talk to Claude and have it go
ahead and take a look at these traces.
So, I'm going to go ahead and see if I
can find the prompt I asked earlier,
which was just use this skill and pull
down the traces from that specific
agent. Find out what issues exist that
we can determine from any, like I said
earlier, right? What any issues that
exist from any of the evals, any of the
annotations that we've done. do your own
analysis and tell me what eval maybe I
can build out in the future to make sure
that I don't run into any of these
issues again. And so this is going to
take a couple minutes. Um, in the
meantime, I'm going to go ahead and
first go and show you kind of how those
traces look and how you can actually
start triaging it if you want to do it
manually a little bit.
But while this is running in the
background, let's go back into the
actual uh
run into the actual agent that has those
sort of queries that we've asked. So,
we'll go ahead and ask it a pretty
similar question. Um, you know, tell me
if I should invest into, let's say,
Nvidia this time. It's a little bit more
of a well-known stock. And we're going
to get that and it's going to try to
tell us some sort of information. And as
that data comes in, looks like I've run
this earlier. So, and you can see it's
coming in. Um, but from an earlier run,
we can kind of see what it's done
already where you can see that query we
asked, you can see the output that it'll
finally generate, which we'll see how
similar it is in a minute from this
previous run. Um, and you can see all
the steps that actually happened in your
agent, right? So, you can understand,
hey, we had a supervisor agent, a
financial data agent, you can see the
LLM calls, you can see all your
different tool calls. you get a lot of
information right away that you can
start using just like we done in the
initial slide to see where those issues
could lie. Now, let's see. Did Claude
finish up? Looks like it's still
running. It's doing its thing. We'll let
it cook. You know, it's kind of the
point of this. Um, while it's cooking,
anyone have any questions as to like,
you know, how you can set up any sort
form evals, any sort of traces,
anything along those lines? Anyone
wanted to learn a little bit more about
Yeah.
>> Great question. Yeah. So, you would go
ahead. So, what it does, it actually
goes ahead and downloads a lot of those
traces um into the into your local
system. So, what it'll do is actually
let me go ahead and show you what it how
it actually goes ahead and accesses the
system itself. So when you give it
access to these skills, what you're
actually giving it access to is the CLI
underneath. And what I mean by that is
you're going to have all these different
CLIs that it can integrate with. So you
can go ahead and set up and find the
data sets. You can pull down data sets.
You can have it interact with the
essentially interact with the UI where
it can set up evaluations on the
platform on your behalf. So you can
monitor continuously monitor when your
agents are failing, build out data sets,
run experiments. It can basically do
anything that you that you would be able
to do in the platform. Sometimes it'll
download, sometimes it'll make API
requests, but that's generally the uh
idea here. Great question.
Any other questions in regards to CLI
tracing?
Okay, let's go ahead and see what
Claude's done. Oh, still crunching away.
Um, so as we can see here, let's let's
walk through what Claude's done so far.
So, we can see that we've gone ahead and
gotten the spans.
It's digging into the evaluations to
figure out where those issues are. Um,
it looks like it's not quite there's
definitely found one very big issue with
some numeric groundedness. I know
someone mentioned that earlier as a
potential issue or something related to
that. Um, we're also seeing some tool
calls directly fail. Um,
and let's see. We also see,
yeah, so we're getting a lot of
different errors. Oh, looks like it just
finished up. And so you can see here we
get a full list as to like, hey, what's
going wrong with our agent and what we
can do to kind of fix it. So while it's
finishing up that, you can see here one
of the biggest alarming things right out
of the gate is about 44% of our agent
interactions are resulting in a bad
summary.
That's really bad. I did not know that.
So, we definitely need to fix that one.
Another big issue is Oh, did not mean to
scroll there. Another big issue is, hey,
we're also just getting a lot of
fabricated answers,
which is just as bad as this the
summarization being wrong. So, it sounds
like it may be related, it may not be.
We can kind of debug that. We're also
seeing a relatively high rate of us just
redundantly calling tools. It's a waste
of our time, our resources, and our
money. So clearly, we're doing a lot of
bad things that we need to go ahead and
fix. And that's just from the eval
from Claude's own analysis. It's able to
even go ahead and figure out, hey,
there's other issues that are coming
along. We're getting silent tool
failures. It's telling us it succeeded,
but ultimately it's not giving us any
actual responses.
We're getting the agent hallucinates
when tool fails instead of disclosing
it. So again related but hey that means
maybe we need to not just do uh you know
some eval built on top of this to
understand when the tool is failing but
we also need to make some prompt based
changes to make sure that the the agent
doesn't hallucinate here and you have a
multitude of like different things that
it'll go ahead and tell you as well as
the evals it can build out. So what we
could do is we can actually go ahead and
tell it, hey, let's go ahead and build
number one, which was the tool success
silent failure eval, and fix numeric
groundedness so that it'll make sure
that whenever it does respond, it's
always grounded to some sort of actual
reference point and it's not making up
these numbers.
But we're also going to head and make
sure you test this against a data set uh
against the spans that caused the
failure initially
using and then we're going to go ahead
and use another Arise skill which would
be here the Arise uh data set skill, the
Arise
Oh, there we go. Arise um evaluator
skill as well as the Arise experiment
skill. So here it's going to be able to
let me just go ahead and run let this
run
and build out evals. All right. So again
I'm being pretty vague here but
essentially I'm just telling it go ahead
and make the changes that you
recommended as well as go ahead and run
these experiments for us. So now we can
actually compare against where it failed
to make sure it passes against that
right and so in this scenario we can see
okay it's going to go through and take
its time. Um I'm going to go ahead and
show you a previous run because again
this will take some time and while we
want to let it cook I don't want to have
you guys staring at a screen where
Claude's just discombobulating or
whatever it does in its free time. Um,
so let's go ahead and look at where I've
actually gone ahead and asked Alex or
sorry
Cloud Code to go ahead and answer some
of our previous issue that I ran into.
And one of those was related to hey,
I've had some times where I'm trying to
get some answers about uh
stocks that aren't necessarily from the
United States. And so we're having
errors where we're talking about like
South Korea or looks like they're all
South Korea based, but let's assume
there's other answers here. Maybe Japan
or China and whatever, right? And you
want to see and you want to be able to
understand, hey, I want to be able to
compare stocks across different markets.
And clearly people are asking that, but
we don't support it. And so what Claude
did, it went ahead found those areas
where that issue existed. Like I said,
it looks like it was all South Korea
here, but it found those areas. It built
out a data set for me, which I can then
go ahead and test against to make sure
it works. And then it went ahead and ran
experiments. And it made a couple
changes. So, it started with the initial
one, which was the baseline, which was
buggy, which as we expected would result
in 0% uh passing rate, which is what
happened when we initially got the
actual productionbased traces.
It also made a quick fix where it
normalized it by adding in that
uh country name. It didn't work. Why?
Because the tool I was calling was also
outdated and I needed to update to the
stable version. So then it made a third
iteration. And you can see that on this
chart here as well where we were able to
see, hey, the first iteration didn't
work. It went back, made a fix, and
finally got us to the final iteration
where we're getting about a 90% success
rate. Clearly still not 100%. We still
need to make some changes, but hey,
we're doing a lot better than we were
earlier. So, this is like a great way to
get you going so you can actually start
from, hey, I know there's an issue to
here's a fix. Now, I know we have quite
a bit more time. I want to check in. How
is everyone doing? How do you guys feel?
Do you guys have any questions about how
you can go ahead and get this started?
Yeah.
Great question. So his question was how
where do the experiments actually run?
Where do the evaluations run? Where does
everything run? Um so you do have a
little bit of customization there. In
this scenario, uh what I did is I had
the experiment run on my local machine,
which is I think what will be the case
most of the time. And then what you what
I did afterwards was I went or you can
host it on a cloud or wherever you'd
like to experiment on. And then you can
go ahead and actually run the
evaluations on Arise itself. So in this
case, I built out LM as a judge, which
would then go ahead and let's see if I
can see the evaluator here itself. So
you can see we built out two different
evaluators, a codebased and an LLM
based. I actually had Claude go ahead
and do this. It built it out for me in
the platform. And this was the final LLM
as a judge because it actually kind of
failed in getting the codebased data to
set up. So that's why we have two. And
so you can see the LM as a judge. It
went ahead and built it out for us with
this prompt and got it going so that we
can actually compare. Hey, did the agent
work properly?
Any other questions? That was a really
good question by the way.
>> Yeah.
>> Very very good question. Um so
eval can be set up however you like. We
have of course people can people can
definitely use whatever sort of models
they want. No one wants to be limited to
just claude or just open AAI especially
in today's modern age where you can see
AI models literally ship every other day
and then you want to be like okay I want
to use that one now right and also some
people have a preference for slightly
cheaper models some people have a
preference for making sure their evals
are topofthe line because ultimately
they know their agent's only going to be
as good as their evals so they use the
highest end models for their evals even
if they're not necessarily using those
in production so it kind of varies you
have full customizable control over cut.
And so what you can see here for
example, you have a full list of
whatever sort of model provider you want
to use and you can connect those even if
you want to use any sort of local um
open source models as well.
Yeah,
good question. So her question was if we
have if I spin up a smaller agent to go
ahead and make some of these bug fixes,
how does this compare to that?
Realistically, you don't have to use
cloud codeex. You can use whatever sort
of agent you want. The benefit of what
we've provided is a skill that you're
able to go ahead and pull down the
information from your traces to make
those fixes. So, you're not making those
fixes just based on, hey, I know this is
wrong and the output's incorrect. You're
making those fixes based on, hey, I know
this is wrong. Here's where it failed.
Here's why it failed. Here's how we can
go ahead and fix it. because you have
not just the information of your
codebase, you have the information of
any of your other APM tickets, whatever
or APM logs, any of your other tickets
that exist in your Jira systems, etc. as
well as your actual arise traces, which
would be like here's the pathway the
agent took, here's where it messed up,
your eval, your annotations, etc.
Any other questions? Yes.
>> Are these features available in Phoenix?
>> Great question. Yes. Uh we do have so he
asked is are these features available in
Phoenix. Phoenix is Aris's open- source
version. We do have I believe skills and
MCP as well in Phoenix which you can go
ahead and hook up to your agent and it
can go ahead and pull down the same sort
of information. Of course there are
going to be some nice to haves in the
enterprise edition where you have access
to these online evals in a certain way
that are much easier to format and set
up. You have a little bit more
dashboarding and a few other features.
But yes, the the skills in CLI you can
connect to your coding agent.
>> Yes.
>> Agent said that summary. So how would
you classify something as like a bad
agent know that's a good summary or a
bad?
>> Very good question. So her question was
in what I showed earlier there was a
eval or there was a response from Claude
that said hey there was a bad summary.
How do we know what is a bad summary or
a good summary? In that case, what I
actually had set up, it was actually
based on one of the evals that I had
previously set up. And so, we can
actually go ahead and look at that
evaluator here. We can go ahead and look
at let's see some
I actually don't remember which one, but
I'm going to go ahead and pull open this
one and hope this is the right one. Um,
so as you can see here, this is
basically the summary eval that I'd
created.
It's basically taking a look at the
information we've gathered throughout
our entire agent, all the sort of
context we've given to that summary
agent and making sure that it's
referencing the right points, it's
answering the question accordingly, etc.
Um, and so that's how we've gotten to
determine whether or not it was a good
summary or not.
>> Uh, what if we set up a skill in the
first place to see if it can do a good
summary?
give it given us a good summary all the
time
just like we set up a skill instead
instead of running.
>> Yeah, great question. So, she's asking
why can't we just set up skills that you
know ensure that it gives a good summary
and yes absolutely that is what you want
to do. You want to make sure that you
update your prompts, update your skills,
update your coding workflows so that
your agents will give the best
summaries. The emails are only there to
help you determine where there are
issues, monitor those issues, make sure
they don't repeat, right? And so you set
up that skill, great, it works for the
next two months, two months later
because there's a model regression
because people start asking questions in
a different way. You end up getting
different results and you don't want
your e you don't want your performance
to degrade because of that. So you want
to be able to monitor and observe that.
That's the point of the evals. Did that
help? Beautiful. Um I don't know for how
much time we have left but go ahead
>> later
agents are assessed
and soc.
So your question was if I've run into
issues with linting with the agents
>> agents
seems like more
>> good question. Yeah. So he's basically
saying hey
um have you seen the issue where hey
you've given access claude to all these
skills and all these sort of traces and
all this sort of information but
ultimately most of the time I've seen
with cloud code or any of these other
sort of coding agents they end up
focusing on linting rather than any
other sort of issue am I correct yeah
that's a very good understanding and
that's kind of why we built out these
skills which kind of focus on ensuring
that they hyperfixate on the actual
issues that have been given to them,
right? So they'll get all these trace
information so they'll understand, hey,
it's not going to be a linting based
issue because you can see that it's
calling the wrong tool and that's not
going to happen because of linting and
it does have some reasoning capability
to understand that. Um, and so genuinely
I haven't seen that so much when using
the skills.
Awesome. So as it Oh yeah.
Does does the system make it easy to
understand? Sorry.
>> Great question. Yeah. So, how so his
question was, does it make it easy to
understand how much it costs to run
those evals? Absolutely. So, one of the
best parts of running evals is in the
platform is you're going to be able to
get full trace history of what your
emails did, which also comes with the
added benefit of, you can see right
here, a nice little cost. And so, you'll
be able to understand how much your
emails are actually costing you because
yes, of course, anything anytime you're
running another LLM, it's going to be
additional cost to you. So, you want to
make sure it's not. And of course,
what's really nice about building out
evals, whether it's in the UI or via the
coding agent, you can have those set up
basic requirements like, hey, we want to
sample specific amounts so we don't run
it across 100% of our traces and 100% of
our calls. Um, you can make it focus on
specific areas. And of course, you can
always dictate that in the coding agent
or on the platform itself.
Um, so as a kind of refresher as to
everything we kind of covered today,
again, it that's the wrong one. Oh, I
think I have it over here.
Um,
so
essentially what I really want to give
you as a takeaway,
these AI agents, they're great. They
will do basically everything you ask
them to, but again, they're not magic.
Like he said, they can definitely focus
on linting. They can definitely get
caught up in small little areas, but the
best part of them is they will automate
your full workflow from beginning to
end. So whether it's that starting from
observing where the issues lie,
finding those issues, being able to
actually pull it down, understand where
the issues lie, create those data sets,
build out exact fixes,
test them to make sure that they're
working.
And finally, you can then go ahead and
be the manual human to make sure that
hey, it didn't just go back and fix the
linting changes, right? And we can make
sure that it actually made changes that
actually help improve the agent and not
go for degradation.
That's kind of the general gist of what
I wanted to show today. Um, any other
questions on this before, you know, I
can maybe show one last thing of seeing.
Oh, still finishing up what I was trying
to do earlier. I was hoping it might be
done after this. took about 14 minutes.
But
um while that's finishing up, any other
questions on how we can use our agents
to automate our workflows
and improving your agents? Yeah.
>> Great question. So his question was, are
we primarily relying on Claude or any of
these coding agents to actually go ahead
and give us the evaluation if things are
working well or not? Um, yes, you can
definitely rely on Claude to build out
everything. You can also manually do it.
You can also ask Claude to do the
specific evaluations you want. So in
this case, when you saw that nice clean
table, that was actually defined by the
evaluations me and my team had set up
prior to this. Um, we'd gone ahead and
looked at, hey, these are specific areas
that we know are potential limitations
in most agents that work in this
workflow and we set up those as generic
ones, which is why we got a bad summary.
We had some, hey, is the agent healthy?
Is it giving the right are we getting
tool calls correct? Right? We know those
are general areas, but what Claude was
able to do was look at our actual
traces, understand based on those
traces, what are the actual issues we're
falling into today. Right? we have our
live agent in production. I'm not going
to be able to go through all of those
manually and find those, but Claude can
or Claude cursor codeex, whatever,
right? And that's where like one of the
biggest superpowers that you're able to
give these coding agents to be able to
do that for you.
I saw another question here. Good
question. So his question was is there
any sort of benchmark data set that we
can see or any sort of like
visualization that can tell us hey this
is a higher quality LLM to use for
evaluations more expensive less
expensive um realistically no [laughter]
that would be sort of something you'd
have to do for your own analysis you'd
have to figure it out because ultimately
one of the things that I like to say is
if you're going to use out of the box
eval to judge your agent you're going to
get out of the box results and that's
not what you want when you're building
customtailored
AI agents which are built to be personal
for you. Um, and the same goes for
benchmarks, right? Benchmarks are great.
They'll show you, hey, this this is a
good agent. This is a good sorry, this
is a good LLM. But realistically, what
you want is, is it a good LLM for me?
And that's going to be tailored to your
use case. So, if you're building for
finance, maybe you'll use a specific
one. If you're building for, you know,
law in finance, it might be even this
slightly different model, right? So, it
really depends on what you're building
it for.
Cool. I think that's more or less it
more or less it from me. Um, if anyone
has any other questions, I'm happy to
answer them. But yeah, thank you guys.
[applause]
