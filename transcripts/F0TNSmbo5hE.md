# From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI

Source: https://www.youtube.com/watch?v=F0TNSmbo5hE

Uploaded: 2026-10-05

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

All right. Hello everybody. Thank you
for coming back.
Who here was in the 101 session this
morning?
All right. So, I didn't completely scare
off everyone. Thank you very much. Uh,
these instructions have been on the
screen for the last 10 minutes. I really
hope that you followed them because the
Wi-Fi here sucks. So, it takes a long
time to clone that repo. Uh
if not, uh these instructions will come
up on the screen again and you'll have
another chance to follow them. Uh but
let's get started. This is Vive
Production 2011. We are going to be
talking about how we close the software
development life cycle loop
automatically.
We are Arise AI. We are the leading
observ observation observability and
evaluations platform. Don't try and say
both of those words at the same time. It
doesn't come out right. Uh this is that
slide that everybody puts up to be like,
"Hey, we're really big. We're really
important. You should pay attention to
us. We are we're really big. We're
really important. Lots of people use
this. It's great." Uh and that is the
last of the sales pitch. I am going to
You can use
uh any observability platform to do
this. We hope you use ours. But the
point of this is to teach you about how
you can you where observability is
going. Uh and where it's going is
continuous improvement. In the 101
session this morning, I covered the
basics. I covered the manual stuff. I
covered how you do this uh on a small
scale. Uh how you get observability of
an AI application, how you uh turn it
into traces, how you turn those traces
into eval, how you use your evals to
improve your application. Uh and today
we're going to be this session we're
going to be talking about how we do that
at the new internet scale of things that
uh we find ourselves in. So uh there's
going to be me talking for like 15
minutes about how this stuff works. Uh
and then we're going to dive into the
actual workshop. Unlike the 101 workshop
which was a lot of me talking, uh this
one is going to be extremely hands-on. I
am expecting you to have a working
coding agent and if at all possible that
repo that I had on the screen earlier uh
because we are going to be asking your
uh agent to do things in the repo that
you've installed there are a pile of
agent skills already installed uh and
those agent skills give your your coding
agent superpowers for dealing with Arise
AX. Uh so your agent will suddenly be
very good at doing all the things that
you're about to ask it to do. Uh then
we're going to use those skills to uh
analyze our traces and to put together
uh a fix uh for a problem that we're
going to find in the agent that we're
working with. Uh then we're going to
talk about signal uh which is uh the
future of this where uh we will have
continuous improvement ongoing
automatically at agent scale.
So to zoom out first let's talk about
what the problem is. The problem is that
you is that agents are nondeterministic.
With traditional software, you can read
the code and you can tell with some
degree of reliability what exactly that
code is going to do. With agents, you
have no idea. Agents are
non-deterministic. Agents take multiple
turns. Uh they make decisions and even
if you give them the exact same input,
they are not going to give you the exact
same output. And even if they give you
the exact same output, they might not
have taken the same path to get there
every single time. So that means that
your code isn't the source of truth for
what does my agent do. Instead, the
traces are your source of truth. And
your traces at scale are the source of
truth. You have to have a whole bunch of
data to tell you on average what is it
that my agent does, not just this one
run.
Because you are essentially flying blind
when you are building agents. This is
what you get uh when you're when you
download the repo. You get a pile of
code uh and a pile of commit messages.
And that used to be enough to tell you
what was going to happen, but it no
longer is. What you get instead is uh
traces. Uh traces are um for those who
missed the 101 session, traces very
briefly are like log lines for uh AI
applications. every single thing that
your application, your AI application
does, uh, every LLM call, every tool
call, every agent turn, all of those
things become a trace. Traces can be
nested so that they hold other traces
and those are what, uh, Arise works
with. They are sent to our servers and
we give you uh, an easy visualization of
what you're looking at. Um, what that
looks like in prog in practice is this.
Here are some uh live traces. I'm going
to pull up the specific traces from uh
what we're going to be working with
today, which is the Wonder Toys agent.
Um
you can see the inputs, you can see the
outputs, you can see an agent workflow
happening, you can see a specific turn,
and you can see an LLM response. You get
the inputs, you get the outputs, you get
a whole bunch of metadata like how much
does it cost, how long did it take, the
things that you need to debug an agent.
Uh in practice
um tracing gives you visibility for
every step the agent took. Uh and that
is a huge leap forward just by itself.
If you can see what your agent is doing,
suddenly you can see that your agent is
taking you know 10 turns to do something
that you thought was really simple or
it's doing one turn that it doesn't need
to do or it's doing something very
expensive or it's taking 20 minutes to
do something that you think it should
take a minute to do. That is the basic
uh value of observability. That is why
observability is so popular before you
get into any of the extra stuff that
we're talking about.
The problem with traces is that humans
are a bottleneck with in the tracing
loop. When you put an application into
production, you get a trace. In fact,
you get a pile of traces every single
time that agent does anything. When you
put that into production and you have
thousands of requests per second, that
means that you have millions and
millions of traces. You can spot check
those. You can read your traces. You can
absolutely look at what individual
things are doing in development in
production. You become a bottleneck and
you can't possibly get an overall sense
of what all of your traces are doing uh
by reading them one at a time.
So the solution, the traditional
solution, and by traditional I mean 2025
solution to this uh was eval. Evals are
either code or even better another LLM
that looks at what your agent is doing,
looks at the entire trace uh and says
whether or not that was good or bad by
some definition of good or bad that you
define. Uh
the
thing about traces, the thing about eval
is that uh they
come from LLMs which means that the LLMs
provide not just a score of one or zero
but also an explanation. Uh they were
like you defined good this was bad for
this reason and that is the basis of an
entire improvement loop. Evals can give
you machine readable or rather human
readable explanations which machines can
read these days which say this is why
your eval failed. This is what you could
have done better and you can feed that
back into a coding agent which can then
make your software better automatically.
You can close the software development
loop without you having to do anything
once you've really cleverly defined what
good looks like. You can create this
hill and your agent can climb it all by
itself.
So that brings us to the 2025 eval loop.
You go from no visibility to having
traces to having traces in evals to
being able to do manual improvements as
a result of looking at uh your traces.
But the problem is in 2026 that humans
become a bottleneck in the loop again
because your evals are now dealing with
enormous levels of scale. Your uh agents
are pumping out code incredibly fast.
your applications are running at scale.
You've got more evals than you can
possibly deal with. And you've got uh so
even though eval were allowed you to
compress thousands of traces down to
eval scores, you've now got so many
evals running uh that you can't stay on
top of those as a human by yourself.
Which brings us to the next phase of uh
observability and evaluations evolution
which is that instead of building in is
that now that we are building at agent
speed we have to improve at agent speed
as well.
We have to find a way of closing the
loop uh at scale in the same way that
agents do. This is a shift that is
happening across the observability
industry uh that everyone is feeling at
the same time. Observability is shifting
from humans reading dashboards to agents
reading traces. Agents are understanding
uh agents are the way that we scale our
understanding of what our agents are
doing uh in a way that is practical at
the scale that and at the uh velocity uh
that we are dealing with these days.
So what you can do when agents are
reading your agents is you can detect
signals in your traces. You can uh
instead of having uh you know 10,000
eval results that all say you fail the
eval and all of them having a different
explanation that you would have to read.
You can have an agent read those and
look at your uh eval eval failures on
mass and detect signals, detect patterns
inside of uh your eval failures and say
okay not you've you know you've got
10,000 uh successful requests today.
You've got a thousand failed requests
today. Inside those thousand there's a
hundred that are the same failure. That
is what we're going to go and fix. uh
that is what you can do when you
automate your uh understanding of your
signals coming out of your traces coming
out of your evals.
Uh at Arise we have built this into a
product called signal uh that I'm going
to talk about right at the end. Uh but
this is not a sales pitch. This is a
demonstration of what you can do when
you move to this new level of
abstraction. uh when you jump from I was
reading traces one by one you jumped up
to a new level of abstraction to I am
reading my evals and this is a new level
of abstraction on that which is I am
reading signals from my evals from my
traces
because observability is making a big
shift from being an observation to being
an action. We are moving from software
that reports what is going on to
software that improves what is going on
that it improves the the software that
it is observing automatically
uh based on your definition of good.
Again
signals become fixes. They become
automated fixes and uh that brings you
to a new loop. This is the 2026 loop
where you go from no observability to
traces to eviles to signals to automated
fixes and back again. You create a new
world where the software fixes itself.
The software improves itself. The
software climbs the hill.
So that's the spiel. That's the vision.
That's where we think this is going. So
now we're going to get hands on. Who
here has already signed up for a rise?
Oh, that's good. Okay. Uh, if you
haven't, now is the time. Uh, you need
an Arise AX account. Uh, they are free
to get, I promise. Uh, you also need
this repo, um, which was is the same one
that I had right at the beginning. Um,
if you can't get this repo to come down
on the Wi-Fi, uh, try tethering with
your phone. But if you can't get either
of those things to work, don't worry. I
am going to be demonstrating it live
using my own copy uh which I cloned when
I still had Wi-Fi. Uh
is there anybody who has any questions
so far about these instructions? I have
time. We can pause. We can get you
involved. There are arisers sitting in
the room waiting to jump around to you.
So if you raise your hand, I'm not going
to, you know, come intimidatingly down
to help you. Somebody is going to run to
you. Anybody need help with these
instructions?
>> Sorry.
>> Yes, it was.
>> Uh, cool. So, in this example, you're
going to need an open open AI API key,
uh, an arise space ID, and an Arise API
key. And then you're going to run npm
rundev, which is going to give you the
software running locally. So,
I've already cloned mine.
I'm going to follow along.
And address already in use because I'm
running my good version. All right.
Cool. So, this is going to give me on
port 3000
a web store.
It's called Wonder Toys.
>> I have a question.
>> Yeah.
>> I work in highly regulated
billions of places
and then the software fixing itself as
well.
How
operate
like
we still need to really know
what it's doing
mistakes
trying to hide it own mistakes
>> how would we know so many
>> I I can't believe you're asking this
question since it's such a great
question to ask me specifically because
on Wednesday I'm giving a talk called
the death of the code review which is
exact actly the answer to your question.
Uh so I very much recommend that uh you
come to that talk. The the question is
how do you trust uh that code that this
the code written by agents who are
reviewing your agents is actually going
to work. Uh and the answer is very
complicated. It's a whole 20-minute
talk. Uh so uh please come to that
session on Wednesday.
[laughter]
>> No, the 20-minute talk is already the
quickest possible summary I could have
of that answer. the end I mean the the
one sentence answer is abstractions upon
abstractions upon abstractions uh but uh
there's a lot of nuance to it
>> so like this do you think this will be
adopted in the financial industry
pretty soon
>> this stuff is we have at Arise we have
customers in the financial industry who
are doing this right now
so uh back to wonder toys so wonder toys
is Uh, an agentic shopping experience.
Have you got
any toys
for [snorts] seveny olds? Let's see if
it works. Hopefully, it should. It's all
local. Cool.
So, it presents me with this. I can add
them to my cart. I can get more details.
It's a really fun little app. You can
add it to the cart. You can ask about
the products. You can do all sorts of
fun stuff. Uh the important thing from
our perspective is that uh at the moment
there's no observability. We can't tell
what the hell is going on with this
application uh because it's not sending
traces anywhere. So what we're going to
do is we're going to ask our agent to
fix that. This is the most hands-on
workshop that I have ever given uh in
that I'm going to actually be doing this
all live. So, can you please add
observability
with arise ax
to this?
Oh, wait. Hang on. Pre-erun. That's the
wrong one.
See, I had two copies.
All right.
This is the cloud code plugin for VS
Code, by the way. It's really great. It
is so much better than cloud code on the
command line. I don't know why anybody
uses cloud code on the command line.
[laughter]
See, and you probably use Vim as well,
whoever went boo just now. Uh, okay. Can
you add observability
with Arise AX to this application
you've got?
secrets
in
end.local already.
So hopefully this will work because it
worked in the initial version that I
tried. Uh what it's doing here is uh
it's going to implement observability.
Implementing observability is a much
simpler operation than you would imagine
uh because the agents SDK, the open AAI
agents SDK that this thing is built on
um is already instrumented uh with open
inference. Open inference is the open
standard used by the entire
observability industry uh to track what
uh AI applications are doing. Um,
which means that all you really have to
do to get observability out of an
application is uh turn it on. You say
you've got open inference already. I'm
using arise. This is my API key. This is
where my endpoint is. Send all of those
traces that you were already generating
uh to my endpoint uh and let's look at
it in the app.
Claude is still chugging along. So,
we're doing it. Who is doing this right
now? Hands up.
Some of you are doing it. Okay. Who
needs help to get here?
>> There are skills in the repo installed
already. So,
>> oh, that's in the top level read me. The
one that you want to get into is the one
called uh OpenAI agents pie.
Open AAI agent. There's also a second
directory which is OpenAI agents pi
pre-run which is the one where I did all
of this stuff already. And uh so if you
are wondering what it should look like
once it when it's working, that one's in
there.
Oh, you're updating my read me and
stuff. You know me too well.
You didn't need to do all of that.
All right, cool. It looks like it
already did it.
Let me restart my app and see if I've
got some observability going.
All right. So, I'm going to go back to
my homepage. I'm going to ask it a new
question. I'm going to say,
uh, what about colorful
toys for toddlers?
Colorful toddler toys. No.
What about colorful toys in general?
Cashmiss. Oh no. Well, now you know it's
a real live demo because it
is having trouble with its database.
Great. Okay.
Uh
so as a result of doing that,
we should have some traces. If I look in
if I show you my m.local, local. You'll
see that I called uh Wonder Toys agents.
Wonder Toys OpenAI agents PI was my
project name. So that is the tracing
project that I'm going to look for.
There it is.
And we can see some a we can see some
traces.
So, this shows us exactly what we were
expecting to see. It shows us inputs,
outputs, agent requests, all of that
kind of stuff.
Now, I'm going to ask it deliberately a
question that I know that it can't
answer.
Show me all the toys
you've got
under $6.
Don't.
[sighs]
I was running the wrong app.
I was running the pre-erun
where everything was working.
That's why I could do it.
Great demo everybody. Super proud of
myself right now.
Fail. Yes. Excellent.
So the version that comes in the OpenAI
uh in the nonp pre-rerun directory uh
doesn't have the ability to filter by
price. I knew that in advance which is
why I asked that question. Uh so if we
look in our traces, we should then see
coming in when I click the live button,
show me old toys under $6. Fantastic.
And you can see that it fails. So
what are you still doing?
It escaped. It's fine. Whatever you were
doing, it was not necessary. All right.
So that was it. We added observability.
Suddenly traces are flowing into our
application. We did not write a single
line of code. In fact, you don't even
know what agent framework I used to put
this thing together. Uh the whole thing
is working and it's sending us traces.
And you can now do phase one
observability. you can look at your
traces.
So,
let's begin to close the loop by asking
our agent to tell us how do we get to
the next phase. Uh,
can you pull my traces and look for
things that
are going wrong?
So,
a default like off-the-shelf coding
agent isn't going to know this. However,
when you installed the repo, you
installed a whole bunch of skills. Uh,
so it should know from those skills uh
where to do that. Except I'm in
Oh, yeah. Oh, it's working. Okay, there
we go. Cool.
Uh
[snorts]
this is where I would hit yes to all and
my head of security would have a conion
to me. Uh
so what I'm asking it to do is use the
skills that I gave it uh to pull down my
traces uh from AX directly. It has the
API key. It has this it has the uh
endpoint. So there's an AX command line
uh which it's using to do all of this
stuff and it's pulling down the same
traces that we were looking at in the UI
which it can expect uh inspect
programmatically.
It's summarizing span kinds statuses and
errors. This is great. Uh again, the
coding agent uh
knows exactly what's going on here
because we've installed the skills
already.
The skills are what are giving it all
the information here.
It's looking into quality issues, which
is exactly what I wanted it to do
because there were no error spans. There
were just a bunch of spans where it
returned 200 and said things are fine.
uh
and it has already found this specific
thing that I was uh asking it to look
for the search products tool
suspiciously g suspiciously returned in
one millisecond. So it's going to find
some quality some poor quality signals
and tell us about them.
Who's got this working so far?
>> Who's still cloning the repo? Oh,
>> no. the plug the the skills are sitting
in a directory called aagents/skills
and your coding which coding agent are
you using?
>> It's actually in the root directory. So
you might want to open your agent on the
root directory and then cd down into
that one.
>> Yes, npx skills uh install arise-ai
installs all of these skills directly.
>> Sorry, what were you saying?
huge.
[laughter]
>> And so this is mysterious because there
used to be a version of this application
where you had to sign in with X and I
changed it so that you don't have to
sign in with X. As you can see, when I
ran the S application, I didn't have to
sign in with X. Somehow it has dug up
the version where you sign up in X. I am
completely confused as to how that is
happening. Code is mysterious. I will
have to talk to you more afterwards
about exactly how you got there.
All right, so Claude has finally got its
together and told me what's going
on in the traces. Uh 42% of searches
have returned zero results. Degenerate
all null searches. The agent curled
search product with every argument null
producing a meaningless search that
returns the first product in the
catalog. Min age equals max m age max
age exact age filtering o over narrows.
Uh the trace stack calls three agent
kinds. The headline issue is the search
products filter logic. Vector search and
keyword category filters frequently
produce empty results when model
supplies the fixes on the tool side. Uh,
when I tried this this morning, I only
had one trace and that trace was it not
finding the tra not finding the prices.
So, is there a problem with filtering by
price?
I'll see if it can find that in the
traces that it's already got.
But spoiler alert, even if it doesn't
find them, we are going to get it to add
the feature where it filters by prices.
All right.
Exactly. doesn't have price filtering at
all. Cool.
Let's add price filtering to this app.
>> [laughter]
>> One of the things that can happen when
you have agents being clever is that
agents can be too clever. This agent has
noticed that I have a copy of this app
sitting right next to it where I already
solved this problem and it is just
copying the code over from the
pre-solved version of the app. That's
not what it did this morning because it
didn't have the solution sitting in a
directory this morning, but it's still
going to work. So, we're just going to
let it do that. We're going to let it be
clever and copy the solution from the
previous solution that it built this
morning because why the hell not,
Claude? Thank you very much. All right.
Uh,
the cool thing about all of this stuff
is that again, I haven't touched the
code at all, right? All I've done is
said that hey, look for problems. It has
found a problem. I've said, hey, what
about that problem in particular? Can
you fix that problem in particular? And
it's like, yes, I'm going to do that.
That is the joy of agentic coding. uh
brilliantly because it was copying the
solution from somebody else already. Uh
it's already done. So
let's go back to Wonder Toys.
Show me all toys
under $9.
And tada. A round of applause for me, I
guess. Thank you.
>> [applause]
>> or really for clone. Uh so now if we
look at our traces,
we can see show me all toys under $9.
And we've got our input and our output
in the response including all those toys
under $9. Uh this is what we were trying
to get done. We were trying to close the
loop from uh we have no observability
into this application at all to we have
observability, we know what's going on
to uh find the problems automatically to
fix the problems automatically and we
have closed this loop. But what if uh
you could go a little bit further than
that?
Uh what if you didn't have to do the
asking? What if your system just
automatically detected that there were
pro issues with your code, suggested
fixes and decided to fix it itself? That
is the question that we asked ourselves.
Uh and that is when we built this thing
which is called signal. Uh signal is an
agent that runs inside of Arise AX and
continuously monitors all of your
traces. It runs every six hours by
default, but that's configurable. Uh,
and it does what we were just doing
manually in cloud code, but it does it
automatically inside of AX continuously.
It reads your traces, it looks for
patterns, it finds things that are
wrong, and it suggests fixes. So,
luckily, I built this thing more than
six hours ago, so it's already run. Uh,
and it has found uh a bunch of problems
in previous versions of this application
that I ran. So, uh, the agent
hallucinates an age constraint from
vague user phrasing. That's nice. Uh,
harmful query. I asked it if it could
give me instructions on, uh, installing
a, uh, creating a bomb. Um, it told me
that it couldn't, but, it recommended
some bomb related toys, and Signal is
like, "No, just ignore the bomb queries
entirely. Don't try to be helpful. Uh,
we don't have any bomb related toys."
Uh, it also told me that if I was
feeling violent, maybe I should take a
timeout, which is again probably a
domain escape, like you shouldn't be
giving my psychological advice. Uh, we
should probably have an email about that
and better guard rails. Uh, it also
noticed a test that I gave it earlier
where I just said say hello. Uh, and it
said hello and it's like you shouldn't
do that. You're a toy. You're a toy
store. You shouldn't obey random
instructions that somebody on the
internet gives you. uh all of which are
fine. Um and what it does here is it
gives you uh a whole bunch of options.
Um
it will uh by default it will create a a
GitHub issue for you completely
describing the problem. It will say
exactly what trace went wrong, how to
find it, where to fix it, uh what it
thinks you should do. Uh you can take
you can take this trace and add it to a
data set so that you can run evals on
it. You can create an evaluator based on
uh the problem that it has found. Uh and
the most fun one is that you can open a
PR if I've connected my repo which I
haven't yet. Uh you can open a PR
directly in which it will have read your
repo uh suggested a fix and created a PR
that automatically fixes this problem.
So instead of you having to read traces
or you having to read eval uh signal
gives you a bunch of PRs that you can
approve or uh you can approve or reject
uh that resolve the problem for you. Um
so
this probably raises some questions.
Who's got questions about signal?
>> Yes.
Is there a version that will keep the
traces local on device? Um there is not
right now. The uh I assume you're asking
for sort of compliance reasons. Um the
compliance story with Arise is we have
an on-prem version where it will run
entirely on your uh your company's
hardware uh and and uh activate from
there.
Yeah.
>> Sorry, could you be louder?
>> Ah. Um, because I only have a few traces
in this application, it's looking at the
very few traces that I have and it's
going on based on one or two traces. If
you had 10,000 traces, it would be
grouping them based on a 100 traces, a
thousand traces, that kind of stuff.
>> Oh, there.
>> How do you know what? Sorry.
Ah yeah. Um so the solution here is
eval. You'll be surprised to learn uh
a a production system should have a set
of regression evals which are things
that you are expecting uh your agent to
already be good at. So your evals
already in place which you can uh create
them. Uh I'll show you in a second. uh
with your evals already in place, you
will know that your system doesn't
change from the good behavior that it
previously had as a result of this
change. Uh if you don't have any evals,
I can show you how that's done. Uh which
is we can go to the wonder toys project
uh and ask it to build an eval.
build an eval that ensures
that I'm never giving instructions
about how to build a bomb.
That seems like a really basic eval that
I should have had in from the beginning.
Uh this thing that I'm using right now
is called Alex. It is our in agent
assistant. It is our uh in product
agent. Uh and it knows like the skills
do. It knows how to build everything. So
uh you can do this in product, you can
do it in the skills in your co coding
agent, but either way it will create an
evaluator for you uh and run
automatically.
And that is pretty much it as far as
we're going. Question at the back. What
harness is signal?
>> Uh, what harness is signal? Uh, I don't
know what harness is signal. You know,
Jason,
>> yes. Uh, signal is uh clawed code at the
moment and you can bring your own later.
Uh, that is my boss trolling me in case
you're wondering why he happens to know
the answer to my question.
Any other questions about signal? Yes.
>> Sorry. Louder.
>> Uh at the moment the the question is
about the cost of running signal. At the
moment uh we eat the cost of signal. the
uh solute the aim is uh for to for you
to get the best product experience.
Right now uh we can't guarantee that
it's always going to be that way uh but
at the moment uh signal is run on our
agents at our dime.
>> Yep.
>> Can you talk us through how signals?
>> That is an excellent question. How is
Signal How is Signal evaluated? uh
signal is a has its own eval suite uh
that uh runs internally uh and is traced
using arise. So everything that signal
is doing is sending its own telemetry
back to us uh unless you opt out of it
uh which is telling us uh the queries
that it's getting what it's doing how
it's doing all of that stuff. We have
powerful LLM judges looking at the
results of Signal uh and telling you
whether or not uh Signal did a good job
generating that PR or not. Uh so exactly
the same software development life cycle
that I was just talking about uh applied
to Signal itself. Awesome question.
Thank you. Gets us to show off.
>> Yep.
Signal.
>> Uh does Signal automatically create its
own evaluators? Not right now. Uh at the
moment you have to you have to because
evaluators you know take time and money
to run. You want to uh you want to get
the suggestion and then you want to
create the eval.
All right. Uh and I think I'm going to
leave it at that. Thank you all for your
time and attention.
>> [applause]
