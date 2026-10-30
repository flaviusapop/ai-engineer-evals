# From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases

Source: https://www.youtube.com/watch?v=YIxzNZDDy1A

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Before we get started, if you want to
follow along, though this is a practical
workshop, so I see a lot of notebooks
out there, great.
Um if you if you want to follow along
exactly as I'm going, you should have a
wand B account or weights and biases
account. If you don't have one, you can
register and get a free one.
And we also give you inference credits,
so you can do an evaluation that way,
and sandbox access is also included. And
um if you want to use something else
like like open router, you can do that
as well. Or even a different provider,
whatever you want to use. I will just
use this as the example in the workshop.
And if you have an AI agent, you can
just tell it change something and make
it work with my setup.
So,
let's go.
Quick about me. I'm Wolfram Reimann Oh.
And my slogan is I have evaluate models
for breakfast, build agents at night,
and preach AI all day long. I do that as
an AI evangelist at Corvus and weights
and biases.
And um I'm also a co-host on Thursday
AI, the podcast.
Alex is also here. He's a the main guy.
And if you have technical issues during
the workshop, you can contact him. He
will help you out
so we don't get interrupted.
But he's your man.
Thanks, Alex, for the help.
And yeah, you can follow me on X or
LinkedIn, and Wolf Benches wolfbench.ai.
Easy to remember.
Um but this workshop isn't just about
Wolf Bench. It's why and how I built it,
so you can stand up your own model and
agent evil from zero to leaderboard.
Um yeah, my backstory basically I
started as a little child loved AI from
the beginning. Then when ChatGPT
happened, I decided I want to focus my
career on this. Um if anyone knows the
old good old times in local llama when
the block was quantizing models, I was
testing the models or I started that
way. Was asked a lot about helping with
inference and stuff. So, I became a
consultant. And
yeah, last year
I went full in in a German AI startup
and this year I joined Qorvo.
And I've been on the podcast for a long
time, right Alex?
So, but this is about you. So, the
workshop, who you are and why you are
here. I think there are different kinds
of people and I'm interested in which
category you think you belong to. So,
for instance, the agent builders. Are
people building agents here that want to
evaluate their agents?
Someone here, someone here, a couple.
And evil newcomers. Any people who want
to do meaningful evaluations but have no
idea what they are doing yet and want to
learn this?
Okay, those are more. And model
evaluators. Who is interested in which
model and agent should I trust? Which is
the one I want to use? Anyone interested
in that specifically? Over there and
over there. Great. Platform and evil
leads. The people who want to do
comparable and reproducible evaluations.
Someone here.
A couple here. Great. Trace debuggers.
Those are the people who are looking at
the actual traces and trying to find out
what went wrong and how to improve this.
Over here. Great. And skeptics.
Who does not trust the leaderboards? I
mean
No, every hand should go up, right?
>> [laughter]
>> But why is that and how can we change
that? And that is part of what we are
talking about and how you can build your
own. But first, my my guiding principles
are mindset is greater than skill set
greater than tool set. So, the tool set
is what we are using and that changes in
AI changes almost every week, every
month. Something new comes out and it
changes all the time.
So, skill set is how we are using tools
that we have. That applies to different
tools. So, if you have a great skill,
uh, you know how to use the tools, you
can switch to other tools. But, the
mindset is the most important thing
because that is the hardest to change or
to improve. And for evaluation
specifically, that is why we benchmark
and what to watch out for. And skill set
is just how to use the tools. And tool
sets, I will show you a couple of tool
sets and you can build your own that way
like I did with Wolf Bench.
And the premise is one score is not
enough because performance is a
distribution, not a point. The thing I
disliked about the leaderboards and a
lot of evaluations I have seen is you
see some nice bars and you see some
numbers and it's an average, an
aggregate, and it doesn't really tell
you very much. And that's why people
always say or often say, "I don't trust
this and I have a different experience."
And there are things hidden behind the
numbers that we can find out and look
at. Because
is it a really a good model? Did it have
a lucky run? What are the hidden
trade-offs? Stuff like that. And that's
why I built Wolf Bench because I wanted
to know which models can I use with
which agents. The agent changed over
time. In January, it was Open Claw. In
February, it was Hermes Agent. And uh,
I'm using a lot of Codex now. It was
Cloud Code before. And I still want to
know which models work the best with
which settings.
And yeah, like I said, most evaluation
results collapse into just one score.
And most leaderboards rank the models.
You don't even see the agentic systems
behind it. Or yeah, different versions,
settings, even if you even see what uh,
settings they have used for this. And
they vary a lot, so you see some scores
and somebody else reports the same
benchmark, but they use different
settings. So, can you really compare
them?
And is there a way to inspect the
results to those people got? So, Wolf
Bench is a framework. It has charts,
dashboards, leaderboard. It's open
source, by the way, and there's also
methodology, and that is what I want to
talk about most. So, you can use that
methodology with your own tools.
And for WolfBench,
one thing that is that is applicable to
all the benchmarks is you have to decide
which metrics are interested to you. Do
you want to look at an average? Do you
want to look at the worst and best
scores? Do you want to look at how many
percent of the benchmarks it can solve
at all? And how much does it
consistently
and also cost. That is also something
that not everybody takes into account.
How many tokens has it burned? How much
did it cost? And it can happen that a
cheaper and faster model takes longer
and costs more than one of the bigger
models because it just used so many
tokens.
Also very important are uniform
conditions. So, you have the same setup
every time because if you change just
the variable, one of the many that are
there, and we will look at a bunch of
those, if you change it, it is basically
a new benchmark now.
And also multi-agent, if you want to do
different agents, which ones do you look
at? And always do multiple runs. A
single run is benchmark lottery. It is a
random result, and it is just a ballpark
number. So, you have to do multiple
runs. I do five with WolfBench, but you
could do more
if you have the money, of course. It's
always a trade-off. Uh transparency is
also super important to me because I
publish all the results, and people can
look at that. So, I don't just show a
score and say this is why this is my
number one model, number two model. I
upload everything and you can inspect it
and check it out, and have your agent
check it out, which makes a lot of sense
with all the data we've collected.
So, basically get the thinking right,
and then the tools become
interchangeable.
And the most important thing I
I think that people need to realize is
you're not ranking a model. If you're
benchmarking a model, it's this model,
but you are actually benchmarking a
specific configuration. So, you use a
data set, and if you change the data
set, it's a new benchmark. You have the
model, and behind the model you have the
inference engine and whatever is
happening on the endpoint that you often
can't control. But if they do an update
for the inference software, it can
change the results again and you you
have no way to actually see that. Unless
it's your own inference on your own
system. Agent orange. Also the agent
orange, if I test blood code or code X,
it is a different version if I test it
next week and I do the update. So
that is also important to keep in mind.
And same thing with the sandbox. Even if
you are using a sandbox provider and
they change something in their back end,
you may not even notice and it could
have an effect and all the settings you
choose yourself. So change any part and
it's a different experiment. You have to
keep that in mind.
Um okay, here's a glossary. You will get
the presentation, so I'm not going
through all of this. Most of you are
very familiar with this and I will
explain whatever
is needed at the moment.
So we are looking at a specific tool set
because it's a practical workshop and
this is one way to build it, not the
only way and will show you the different
ways and you can pick your own stuff. So
to follow along, you should have your
laptop and your terminal, Python, UV and
Git are recommended.
We have files to download, so if you are
not following, you can download the
results and import them and use the tool
set anyway. So you don't have to follow
along everything, but if you want to,
you can do it and use your own results
that way.
Um yeah, you should have the Wi-Fi and
an API key is optional. I showed it in
the beginning. I'll show it in a minute
again.
So you can get this.
So here again, take a screenshot. Scan
the QR code. This is where you can get
you get to a form where you can get free
inference credits for the duration of
the AI engineer conference
and to do that you need a free One B
account. There you can sign up if you
don't have already. If you don't already
have one. Who has an account already?
Does anyone here use One B?
Bunch of people. Great.
Okay, and also the sandboxes, I'm using
the core weave serverless sandboxes in
your offering where you have an isolated
box for each task, which is super
important because otherwise you would
change your own system with every
evaluation run and then it would be even
more random.
Okay, we are looking at six swappable
layers and we'll choose each one and you
can do the same. So this is the skill
set how to do it and the mindset in the
background and now we choose the
different tools for this toolkit that we
are building. So we need a benchmark,
which is a data set. We need an
evaluation harness to run the data set
and the evaluation and
yeah, to orchestrate all of this and to
run it in sandboxes so it doesn't run on
your system.
And also we need an agent harness. What
which agent do we want to use?
And the model and service.
That is of course usually the thing that
people are most interested in. How does
this model do?
And the thing is you are not just using
a model, you're always using an
endpoint. It's always on a provider if
it's open router, they are routing to
other providers. They are a lot and if
it's open AI or Google or XAI or
whatever it is,
they have their own setup and you are
also evaluating that in a way. And all
the settings you can choose.
So the first thing is which benchmark do
we use? You can start with the
benchmark. I did it that way because I
wanted to test agentic use with
different harnesses so I decided I want
a benchmark that does that. So I looked
at all the benchmarks that have been
used by the frontier labs and I saw
terminal bench was on pretty much
everyone. And it's an agentic benchmark.
It's not a coding benchmark, not just
it's a agentic benchmark where there are
tasks like like fix the git repository,
crack a password,
repair a database, stuff you would ask
your agent in normal use as an example.
And that's why I picked terminal bench.
But you could if you are interested in
multilingual stuff, MMLU is one thing.
or if you are interested in multimodal
stuff, MMU Pro is something. If you are
used interested in GUI agent use, then
you would book pick a different
benchmark. If you are interested in
mathematics, coding, whatever it is,
there's a benchmark for it and the thing
is find the benchmark that is
yeah, most interesting to you and that
is comparable. You could also make your
own, of course. You can make your own
data set.
And regarding Terminal Bench, that is a
gentic, so that's why I chose it to
benchmark agents. There are versions 2.0
and 2.1 and 3.0 is in the making right
now. I chose 2.0 because 2.1 wasn't
available when I started.
If you are starting now, choose the
latest version 2.1, but I'm using 2.0
because choosing a new version would be
a new benchmark and I could not compare
the scores anymore. It actually fixes
only 28 of the 89 tests, but it would be
a different benchmark for all the
models. I would have to retest
everything I already did.
And I did a lot and never enough, but I
did a lot, so I don't want to make a new
version of Wolf Bench right now.
I will do that at a later point, maybe
with 3.0
or if a big new jump in capabilities
happens and we need a different
benchmark.
Evaluation harness.
This is you have chosen which benchmark
you want to use, which data set to use.
Now you need something to actually run
the evaluation and Harbor is a default
framework that is for Terminal Bench.
There are others. Inspector is a great
framework
by the UK
AI Security Institute, which has a lot
of different benchmarks you can use.
It's also very popular.
The LM Evaluation harness, I used that
years ago, so it's been around forever
and OpenAI has their own eval stuff. You
can build your own runner
or one of the others. You pick what you
want. Some people can also Some people
start with picking their runner and then
they pick one of the benchmarks it
supports. That is also a valid way.
And now for the first practical step,
let's install Harbor. In this case, I'm
using the current version. It was
current yesterday. I'm not sure if it's
current right now. It changes a lot, but
I pin it to the
to the version, and I highly recommend
people stick to one version
because anytime you change one of the
variables, if it has an effect on the
evaluation, and many have, then, yeah,
you are changing already a variable, and
the comparison comparability is
suffering.
Even if it has a bug, you are at least
testing all the models with the same
bug.
But, it's a visual thinking, of course,
because sometimes you have to update if
a new version of the
harness of the evaluation harness
supports a different agent or provider,
then you may be forced to update. What I
recommend for the people who are really
serious about this, fork the repository,
maintain your own fork, and just
backport whatever you need.
And if you install it,
this is There's a line break missing.
It's UV tool install Harbor. So, it's
installing in a UV environment, so it
doesn't affect your system, and you can
cleanly uninstall it again. Then, you
should have this version.
The next step, agents need a sandbox
because if you just run it locally on
your own system, then second agent
running, it would find a system that has
already been changed, and it would
interfere with your system, so I would
not recommend that. You can use Docker.
That is very common, but it's very hard
to parallelize that depending on what
system you are using. So, you need a lot
of resources. So, that's why there are
cloud providers, and I have to give a
big shout out to Daytona. They supported
me in the beginning before Qualif had
their own sandboxes, and I wanted to
start with this. So, they really
supported me a lot, and I have done a
lot of the evaluations I have with
Daytona. Now, we have our own offering,
so I'm dogfooding it, and um
that's why there are two options here
that I recommend. The Qualif sandboxes
are for those using the Kubernetes
service, and the the golden one here is
the Qualif serverless sandboxes. You
just need your Vent B account.
>> What about the
Ah, okay. We also have a
Um, I
Can you uh
I I turned off Slack, so it's not shared
here.
If anyone wants to get the PDF right
away, just go to Alex. This is probably
the easiest way right now.
Um, okay. So, after you've installed
this,
uh Harbor is installed. Now, we need a
sandbox client that is part of Harbor.
And in this case, there's a part of a
couple of things.
Here's
the QR code for the presentation.
Yeah.
Good. Um, UV tool install Harbor in
square brackets won't be installs the
provider to use the sandboxes, and you
don't have to do anything.
Once it's installed, you just have to
have your API key.
And you configure this in a YAML file,
and here's just the next step. You don't
have to copy this. There is a link and
an easy URL you can just enter with the
full configuration a couple of slides
ahead. So, just so you This is just so
you see it. But, if you are following
along, you should just type the UV tool
install command to install the Harbor
won't be provider if you are using this.
Let's continue.
Next step, agent. This is the most fun
part for me because there are so many
agents, and I want to test how does this
agent do with this model? And
here's a list of some of the agents.
These are all the agents, and there are
even more that are supported by the
Harbor framework. So, we have Cursor, we
have Claude, we have Klein, we have
Codex, Open Claude Hermes agent,
um,
and Terminus 2 is the default agent for
the terminal bench and Harbor framework.
And this is not a real agent. You can't
use it for your coding stuff, or you
shouldn't. It's more like simulating CLI
environment to the actual model, and it
sends
keystrokes, and the agent executes them.
It's one way to do this.
So, in simple agent, which is a default
if you are seeing Terminal Bench scores
somewhere, and nobody said it's tested
with a different agent, that is the
agent they used.
And then, which model do you want to
test? You have to pick a model, and you
have to pick a provider. If you are just
using GPT 5.5, you will be using OpenAI.
If you are using Claude,
Fable,
lucky if you are to use it, then
you will be using Anthropic.
Also, Google also provides some of the
Anthropic models. And these are the just
some of those. OpenRouter provides
almost all of them, probably all of
them, even with DDR enabled, so you are
not sending any data
to the model vendors.
And we also have our own inference core,
with serverless inference, where you
also get selection of open-source
models. And in this case, what I wanted
to test is GLM 5.2,
which was the latest model I tested, and
also the best open-source model,
open-weights model.
So, I just picked this for the
demonstration. You could choose any
other, of course.
And now the thing is the settings. There
are a lot of settings. Some are very
familiar to people, some maybe not as
much. So, the context window size is
also very important, because you always
see this model has this context window
size, but every provider has the Yeah,
some providers choose to deliver a
different size, a smaller size, for
performance
performance reasons. Like our own
inference also doesn't offer the full 1
million of G
GLM 5.2,
only 256K,
but that way we can serve it faster,
and the quality of the model
de-
degrades after a certain amount of
tokens. So, basically, half context is
already very um
very much noticeable. And the thing is
it costs a lot if you always go to the
million and then you compact. So, I
personally think 256K, that's why I
recommended it to our inference team to
use this in that situation. Um I also
use the same with Codex.
Um
basically, right now that gives you the
best quality at the best price
performance and speed.
Thinking and reasoning efforts. This is
a big factor and I have done different
evaluations with different thinking
modes and they really have a big effect
on the model and sometimes a very
surprising effect where if you raise the
thinking, it goes down, but I will tell
about this when we get to the slide. So,
system prompt. You don't always have the
ability to change the system prompt or
even inspect it, but it is a very
important factor. And if you think about
an agent like Open Law Hermes agent, you
have the sole MD where and put a lot of
instructions. And now imagine you are
using this with the benchmark. And if
you give the instruction you are helpful
assistant, it will be very different if
you give it an instruction it is an
autonomous agent
doing stuff. I have seen results where
the model
or the benchmark delivered a bad result
because the model tried to ask the user,
but there was no user and it didn't
know. So, if I change the system prompt
and tell it you can't ask the user, it
would behave differently and it would
get a better score, I'm pretty sure. And
that would be completely changing what
I'm testing. So, there are so many
variables here. Also, tool config. If
you give the agent web access, I've seen
where a model went out and looked up the
solution for the benchmark because
Terminal Bench is a public benchmark.
And you have to look in the traces to
see what happened here. It It's not
really It's not even a bad thing if you
want an agent, it should be smart. And
if there's a solution for the problem,
why should it try to think of it if it
there is a published solution? So, it
depends what you really want to measure
and if you want to give it access or
not. And not all of those do that.
Or not every time.
Sandbox resources, all the thing. If you
give it less CPU or memory, it may run
out or it be maybe
slower, so it takes longer to do
something or even crash and then you get
a bad result. And it's not the model's
fault, it's because of the sandbox
configuration. Task timeout, every task
gets a timeout. By default, they range
from I think 5 minutes 15 minutes to
over 3 hours.
One is 3 hours something and another one
is 2 hours or so.
And that means you have to decide how
much time you want to invest. When I
started with Wolf Bench, I gave every
task a fixed 2 hours because I didn't
want to
basically handicap open weights models
which are often running on less powerful
inference endpoints than the big SOTA
frontier lab models.
So, if you are running DeepSeek on a
local system, it's usually not as fast
as GPT on OpenAI systems. And that would
skew the score if you don't give it
unlimited time. But I noticed when I was
going with 2 hours that
if the model can't do the task, it
sometimes just goes in circles and tries
and tries and tries and fails and fails
and fails. So, it was very expensive and
took a long time because if I do 2 hours
per task and there are 89 tasks and I
parallelize them depending on how much
concurrency I'm using, which is the next
point, it takes so long. It takes so
long and it costs so much and you don't
get a result because it just can't do
the task. So, I noticed 1 hour is a good
mark.
If you use the default terminal bench
the
test duration will rise.
Concurrency, that is what I meant.
You don't want to wait 98 89 hours or
even twice the amount of time. You want
to do concurrency, so you have multiple
trials happening at the same time. But
then you have to decide how high can I
go? If If I go concurrency 89, I can do
all the 89 tasks of terminal bench at
once.
But, if my inference endpoint is not
fast enough and I get rate limited, then
I will get bad scores or even no scores
at the the end. The same with the
sandboxes. If I have sandbox provider, I
get resources and if I use 8 GB per
sandbox,
yeah, it sums up quickly and maybe you
get over the limit you are allowed.
Retry policy, how often to retry
something. That is also something if I
don't retry a task and it fails because
a sandbox crashed, I get a bad score for
the model. But, it wasn't the model's
fault. So, if there are errors that you
should retry and there are errors you
should not retry. Like if the model
causes a crash on its own by doing
something stupid, that is actually a
fail you want to measure.
Temperature,
the usual stuff. Um that is a difficult
thing for a benchmark because which
temperature do you use? Some model
providers they give you the recommended
temperature to use with their model.
Some don't. And some agents have a
default. Some agents
decide based on the model. And there are
so many combinations that you have to
decide, do you want to look for every
model what is the recommended one? If
there is none, which do you use? How do
you make sure that people who are doing
the same benchmark are using the same
setting you chose? It's difficult.
And top P as well. Do you use 0.95
or do you use one or do you any value?
It's just one setting and there are so
many others. And max new tokens, how
many tokens is the model allowed to
generate? You have to decide on this
because there are recommendations by the
providers, there are limitations by the
by the the hosters.
You have to choose something and usually
you have to configure it. And if you
can, you can also set a seed so the
randomness is reduced. We I when I
started benchmark, I used temperature
zero so there was less randomness. There
was never no randomness. And I've seen
things as small as a traffic driver
update to change the actual results I
got. Even if everything was uh
deterministic or looked like that.
Because we have floating point rounding
errors, we have performance
optimization, so many effects that
change the result even if you use a
temperature zero. And nowadays, when the
model is recommending temperature one,
then you should not set zero, of course.
Otherwise, you would be going against
the recommendation. In that case, you
could set a seed, but even if you choose
a seed like 42, it's very popular. You
know why. And the thing is, some model
may be more have more luck with that
seed than others have less luck with
that seed.
It's all choices you have to make.
Now, for this choice, which
inference we want to use, I have on the
left side the normal inference core with
serverless inference. If you want to
follow along and you want to use open
router because you don't didn't go
through the getting your own key here,
you could use open router as well.
In either case, you just use an end file
and put in the variable at the bottom
here. You just put the variable, the key
in the end file, and then we will
use that with the agent.
Um if you use open router, you have to
set some special settings to use our
provider, the One API provider. This is
very important if you are using open
router and benchmarking a model. There
are so many providers, and by default,
you get one of these. They decide which
is the best at the moment. So, if you
are running a single benchmark run 89
tasks, you may get half the task with
this provider and half the task with the
other provider. So, you definitely have
to set which one you want to use.
And after all this, you have chosen one
part for each of the six layers we went
through. We have chosen Terminal Bench
for our evaluation, we have chosen
Harbor and a specific version of that,
we have chosen our sandboxes, we have
chosen Terminus 2 as the agent. GLM 5.2
and we have specific settings.
If you are doing evaluation, you will do
the same.
Whatever framework you use, whatever
model you use, you have to make choices
and you should be very clear what you
are using.
This is important when you are
publishing your results, so others know
what you have actually used and
measured.
So, here is another QR code. This gives
you the full configuration, so you don't
have to copy stuff from the slides and
here's a formatting that has been messed
up a little. Excuse this. Um
If you download this configuration, I
will show you in the next slide how to
run it and it will take about 5 minutes
to actually get the results in this
case. And I will also do the same. So,
if you want to download the config,
here's the QR code.
And I will go to the next one. So, let
me just not just show it, but actually
run it. So, take a look at this. What we
are doing, we are sourcing the end file
to get the API key we find two slides
back and then we are running it with the
UV run harbor run config command and
giving it the configuration you
downloaded or created
and then we can actually
get the results. I will do this right
now
in the shell.
So, the first thing, installing the
harbor framework. Executing the command.
I will zoom in a bit.
So,
if my Wi-Fi is working the way it
should,
it's full.
Okay. We are letting this run.
I will go back
in a minute.
So,
continuing with the presentation.
So, we are
running the thing and it will do just
one test. I didn't want to use 89 tests
for this, otherwise we would be sitting
an hour
overtime. And that is only the time I
give every test, so afterwards the
verifier has to run and check if it's
correct. That takes also some time, so
it takes even longer.
But, um Harbor pulls the tasks, the
Terminal Bench 2.0 data set, it uses
that from the configuration.
So,
this is the part
where it has
Terminal Bench version 2.0
in the config. Then, it starts the
sandboxes using a provider we are using.
So, it creates a sandbox per task,
depending on the concurrency, how many
it uses. Then, it runs the agent. It
actually goes in the sandbox, installs
the agent, and executes the task. Give
it Give it a system user prompt,
basically, saying here, "That is what
you have to do." The agent does it. And
afterwards, it
collects the results
from the sandbox before it is destroyed.
And it gets the trajectories, really,
what is the agent doing? You get a lot
of information that way.
And this small task, it's one of the
smallest, it's just a Git repository
where something has been lost, and it
should be find it in the Git tree and
restore it.
This takes about 3 to 5 minutes. Let's
see how far we are here. It's installed
now.
Then, we install our One B client.
And the next step, in this case, I'm
just getting my API key from
the One Password.
And then, I'm writing the configuration
here.
This is the one you can download. I'm
just catting it into a file.
And loading the end file. Now, the API
key is in my environment variables, and
I will just This is the run command.
Run the evaluation. So, now it's
starting to go out, starts the
sandboxes,
install the agent, run it.
And this is all happening here.
And while it's doing that,
I will go back to the presentation.
Next part.
Run as evidence, not only a score. The
formatting is totally messed up here. I
will fix the presentation and we will
upload it. This is just the directory of
what is in the in the evaluation folder.
We can create this live as soon as it's
done. Of course, it will take about 5
minutes should it
take. Right now, it's starting the
environment, which is creating the
sandboxes.
So, just letting it run. Oh.
This is too early.
And when we have that, we get
one task and it is scored. It either It
gets a score of one or zero. Did it
succeed or did it fail? If you do that
for the 89 tasks, you get an amount how
many tasks it did and then you do that
over five runs, for instance, and then
you get a percentage and you know how
many percent of Terminal Bench did the
model get. And then this is usually the
score that the labs report. Most people
just report the average across five
runs.
And this is the installation of the Wolf
Bench Toolkit. What we have done before,
it was all the Harbor framework and
Terminal Bench and this is what I
programmed, what I created. The Wolf
Bench Toolkit is a way to work with this
data because otherwise you now have a
couple of files and you have some score,
but how do you analyze it? So, this is a
collector, what Wolf Bench does and I
will It's best if I show it when I open
the program.
So, let me go back here.
While this is happening, I will just
start it in a new shell.
And we just clone it and go in there.
So, it's open source, Apache 2 license.
You can use it for your own projects. Of
course, you have to adapt it if you are
using something else than Terminal
Bench, but
it's easy to adapt nowadays. Just tell
your agent.
Quick question. Who's using agents for
stuff like that?
Not everybody?
Oh, I'm surprised. I still I still see a
lot of notebooks, by the way.
Because
some people now just pull out their
phone, take a screenshot, and say,
"Okay, agent, go. Do whatever he is
showing on the stage."
Next year.
Okay, so it's downloading and I'm also
downloading all the results I did with
all the runs I did so far.
So, quick spoiler, I did
uh 430 runs right now across
um where is it? Uh
it was
430 runs.
But
anyway, here are the agents I tested so
far.
Cloud code, Hermes agent, open clock
cursor, Codex, Klein is not published
yet. That is on my list and some other
agents. If you are making an agent,
contact me if you want to appear as
well. And some models I tested, many on
those W&B, that was on our own
inference.
So, the the final cost was unfortunately
not as high as it is displayed, almost
40K here.
So, this is some of this is on our own
inference, but I just use the prices
that have been published.
So, let's see where we are here. It's
downloaded.
So, the 13 megabytes, those are the
results. If you want to see all the
trajectories, those have been uploaded
to weave and you can just inspect them.
You uh um don't have to um download
gigabytes of data.
Now, if you want to use the Wolf Bench,
you can set some variables, so it is
also an uploader, but I will show you if
I just start it.
And this uses a Remeo notebook
to um provide a dashboard, an easy way
to handle all the evaluation data.
So,
any moment now.
There it is.
So, this is a dashboard. You can enter
your information where you want to
upload the traces if you have the We
stuff. Then you can discover VMs if you
are using XE dev or Hetzner, it will
find all your VMs on there and you can
filter which VM names are evaluation
VMs.
Because I don't run the Harbor Framework
on my own laptop usually. I run it in a
VM so I can turn off my laptop or my
Wi-Fi doesn't go off and the connection
to the sandboxes fails
because that could also affect
something.
Um in this case, everything is local as
soon as I download the stuff which I
did. So, I can just scan my local
directory and it will find all the run
data I already did. So, here are the 443
unique runs.
And it shows you here a filter so I
every run that has a score is
is measured. It has to have all the
tests. If some tests have not been run,
it's not a valid res a run. It was just
a test run. It shouldn't have too many
errors or timeouts. And then I get a
list of all of this stuff and I can
choose which models I want to create um
uh nice chart for. In this case, I will
just use all of them. Then you can also
just change the names of the models and
sometimes you also have to change the
thinking because the parameter you give
can be changed by the agent.
Like if you are using a thinking extra
high
or if you want to use a thinking max
mode and your agent doesn't support it,
maybe it is called a different way. And
then you have to change it so it's
really reflecting what has been used
actually.
Now, after all of this is done, I can
just create my results file. You can
upload to We view if you have the key. I
do not have set the key so I right now
don't have the button.
Now, I create a save file and this is
one JSON file that contains all the
results. You can share that with other
people. And
in the end, I generate a chart which is
a artifact I generate. So, now from all
the results I did, I get a new chart.
And this is the same that I then in the
next step, I have an uploader as well.
After the chart is generated, I just
upload it to wolfbenchmark.ai and it's
updated. If I
activate this option to replace the
index.html and it is online
immediately.
So, going back to the present Oh, let's
just check how far the benchmark run.
Oh, it's done. See, it's done. Trials
one, mean score 1.0. So, it had one
task, it solved the task. So, it worked.
It finished and it fixed the Git
repository.
And this task is now in my directory
and I could import it, but it's not a
full run, so it is not displayed by
default.
And once we have done that and uploaded
this, we can look at what Wolf benchmark
provides. This is also the mindset thing
again, what do we want to look at?
And in this case,
this is what we just did.
I showed you the dashboard.
And now we have to take a look at the
leaderboard and what it means, because
the leaderboard itself, whatever it
generates, it is not just an answer, it
helps you to find a better question.
Like, what are you looking at? Do you
care about the capability of a model or
the reliability of a model? And I will
show you what that means
by going to wolfbenchmark.ai.
And the thing is,
I will just make it a little smaller.
So, they are sorted from left to right
and I have all of the information here.
Most benchmarks you look at, they just
show the terminal's two score and they
only show the average. So, this is an
interactive page, which is used not only
to display results, but to create charts
that you can then copy and paste and put
somewhere else. There's a screenshot
symbol so I can show stuff on X for
instance. So if I want to show how did
this model do, I can just mark it. I can
remove some of the bars or reorder the
bars. So it's interactive. So I can
create my report that way.
And what it also has it in the URL. So
everybody can
if you give the URL to this, they see
the same thing you had on your screen.
So I'm switching over here.
And
it looks a bit overwhelming sometimes
because there are so many information so
so many information on the same
bar. Like I said, you can filter to
different information to make it a
simple bar, but I like to see this
because the darker part at the bottom,
that percentage is how many percent of
the whole benchmark has a model solved
in every run of the five runs runs I
did. So that is what I call consistency.
This model and this agent, they have
solved the task 60% of the whole
benchmark every time. And this means if
that is a very high score, the model is
very reliable because if it solves the
task, you can expect it to solve the
task all the time.
While the yellow score is the average,
the one score that usually is reported.
And the up and down arrows around it,
those are the best and the worst scores
in one of the five runs. So if those are
very close to each other, then there's
not a high variance. So you can expect
the same score. If they are very far
apart like we see here from 79% to 60%,
that means there's a lot of variance.
And that is a sign that the model
there's a lot of randomness involved
here. You can't really trust it to
execute the the task. Even if it has a
high score,
it's a bit random if it does it. And the
highest mark is the star, that is the
ceiling. How many percent of the
benchmark has it solved at all, at least
once.
The amount of task that tells you how
Yeah, in an ideal case, that would be
the score the model should get all the
time if it's perfect and always doing
it. Although, that would also be an
indicator that it is probably
benchmarked for this. Um but it shows
you how far it can go. So, what you want
is a very very high ceiling, a very
stable average, and a very high solid
base. And if a model has the same score
and they are almost the same, you can
still see that the solid base
is different. And then in that case, I
would pick one that has a higher solid
base.
Like here, it's 73% to 74%. It's almost
the same. If you just look at the
average score, it's almost exactly the
same thing. Could be
a variance, just variance. But this is a
bigger difference. It's 6% points, and
that is a noticeable gap. So, you see
the extra high thinking is better than
the medium thinking, as we expected.
But if we are looking at
um This is also very interesting. I will
show it in the presentation. Let me
switch to the presentation.
So, these were the different ways to
imagine the model. Ah, risk and cost
tolerance. I have to show you this
because this is something If you look at
the second best model on my evaluation,
it was Gemini 3.5 Flash. So, this model,
a flash model, is almost as good as GPT
5.5. So, what gives? If I just look at
terminus, so we don't have so many bars,
and I can also say I just want to
compare these two.
And yeah, it's a great model, Gemini 3.5
Flash. But if I look at how did it
achieve that, I have a 3D view, which
shows you how many tokens it used to
achieve that. And it has been billions
of tokens to get that score, while GPT
5.5
used much less.
Let me zoom in.
So, 136 million tokens for GPT 5.5,
compared to 1.65 billion tokens for
Gemini 3.5 Flash.
And the thing is, if we also look at the
price, which is another 3D view, this is
the cost. And I can even show both at
the same time. The cost is now a shadow.
You see that the cost is over here. It's
overlap because it used so many tokens,
but this shows that Gemini 3.5 Flash is
very close to GBD 5.5, but it used so
many tokens that it cost even more
than GBD 5.5 of course. So, it costs in
this case $620 compared to $497. So, 500
to over 600. So, it's not that you Yeah,
you have to think about this. Do you
want to use a fast and cheap model?
But you have to compare is it really
faster and cheaper because all those
tokens also take time. That is one
thing.
Going back to the presentation.
And
it's a decision surface. It's not just a
chart. So, you load your snapshot and
you can add your own if you did it and
you execute the code, you would see
them. And then you can filter like I
showed you different metrics and models.
You can reorder the bars and export your
own.
And then
you can show this and make a social post
about this or write an article, whatever
you do.
Um you can do this. In this case, I was
looking at which is the best model on
this benchmark. So, my number one right
now is GBD 5.5 with Codex. It is even
better than Fable because if you are
asking what happened to Fable, that is
also very interesting to take a look at.
If I put Fable in here, it's had 13
refusals. So, it refused. And if you
take a look at the cost, it goes so far.
It was my most expensive benchmark.
Don't tell anyone
because it cost 11,000 just to test
Fable and it failed because it refused
so many tests. Whoops.
And that is also something of course you
have to decide. That is when people say
oh I don't trust this benchmark this
model is in the first place.
Look at what happened here and the
benchmark has to be transparent so you
can look at the traces and see what has
happened then it makes sense suddenly.
Okay.
Going back and yeah like I said the best
model was Codex with GPT 5.5 but as you
can see it was pretty
very expensive.
Let's zoom in. It cost almost a thousand
bucks. While Cursor with the same model
cost only 282.
So that was very cheap compared to the
other one
and it used a little less tokens here.
But
yeah that's you could say okay this is
the best combination but maybe the other
one is from a price and performance
perspective the better one.
And Terminus also had the highest
ceiling but if the scores are very close
to each other
that could be random. You have would
have to do 10 runs or even more to be
very sure but you have to make a
choice sometime and pick one and go with
it.
This was also the thing that I just
showed Gemini 3.5 Flash compared to GPT
5.5 lower score bigger bill so in that
case it would make more sense to use the
other model.
And this was also super interesting and
surprised me a lot when I tested
Opus 4.6 at the time I raised the
thinking to max and the score decreased.
It really got worse and I did the same
with Claude Code because I used Titanus
as well and there I saw the same effect.
When I do that with GPT if I increase
from thinking off to extra high or from
medium to extra high if I raise the
thinking level the model gets smarter as
you would expect. So why did it get
worse with Opus? That was surprising to
me and the difference if If look at the
traces is that you see the model it
thinks too much. It's overthinking. And
that means I give it 1 hour. And if the
model thinks for a minute or two and
then decides I want to execute this
command and the command doesn't exist on
the machine yet, then it thinks another
two or three minutes. And how do I
install this? While an agent that is not
even thinking, it's just doing stuff. So
the first impulse is I run this command,
get an error message. I run this
command, get an error message. I install
it, get an error message, fix it. And it
gets more turns. So it can do more. That
is the difference between thinking for
an hour and not doing anything or just
trying, trying, trying, trial and error.
And the interesting stuff is that the
GPT models, they are by default they
appeared not as smart as Opus. Opus is
very capable out of the box. Even with
thinking off, it already got a great
score. If you compare that here, it is
already with off better than medium here
on GPT 5.5.
And even the solid base was higher. So
it did more tasks in every run.
Yeah. So that is stuff you have to look
at. And if it's surprising, take a look
at the traces to find out what is
happening here. Model overthinking.
I also saw the same with Fable, by the
way, where the model was very smart and
it
seemed to know it was so smart. So what
it did is it decided to go this
direction. And even if the benchmark
said it should be done that way, said,
"No, I know better. I will do it my
way." And then the verifier at the end,
it ran, tested, and failed. So the model
was too smart for its own good in some
cases.
And this is also an important feature I
have to show you. The bar is a claim,
the trace is evidence. I'm talking about
traces all the time. So we have the bar,
which is what we see on Wolf Bench. You
have the nice bars. And the thing is you
can click any of the bars, any of these.
You just click it.
And you get taken to our One page, where
we have weave, which allows you to
inspect all the traces. In this case, I
just clicked one bar, and I'm seeing all
the five runs that composed that score.
And I can now pick any of the runs,
go in here,
and uh
this I should remove.
I'll show this later.
Uh go away.
So, we have 89 chords. That are the 89
tasks that I have been doing, and you
can see all of the traces here. It's a
lot, so it's loading a bit. And then you
can go into any of these,
and you see the task name, and you see
the reward, did it succeed or not, and
you see all the steps. You see the
initial request, the user message that
says, "You are an assistant. You are
tasked to do with this." Then you see
what the LLM did as a first command,
what analysis it did, and what it wants
to do, and then the command it sends,
and so on. And you can really inspect
all of this what has happened, and look
at it. Or use your agent, and have this
done. And we have a new feature, which
is also an agent built into the
platform. So, you have an agent inside
of weave, and you can just tell it to do
this. There's a talk about this by my
colleague,
Tim Sweeney is doing it on July 1.
There you can check it out. I use agents
a lot, because reading all the traces
takes a long time. And if the agent
gives you a link to weave, and you see
that it's true what it says, that is
also very good.
So, to recap,
there are so many variables relevant to
benchmarks. You have the benchmark
version, the OneBench 2.0, 2.1, the
agent version, the model service and
route, even updates to the infer-
inference endpoint can change the
results and the settings.
Sandbox resources, like I said, if the
if the agent runs out of resources, it
will fail, and then you get a bad score
for the model, although it wasn't the
model's fault. Sampling, temperature,
all things we discussed. Thinking
defaults, like maximum not being higher
if it thinks too long and a smaller,
faster agent reaction could work better.
Time out policy, retry policy. If you
don't retry and there has been
infrastructure error, you would get a
bad score. So, after every run I go
through all of the errors and mistakes
and check if there have been inference
issues. You can find that out if there
are repeated characters or if prompt
template um
tokens leak into the actual response,
then you know there's a tokenizer issue,
an inference server issue. And
especially with new models, that is a
big thing. If you are benchmarking
models as they come out, they are so new
that the inference engine maybe has not
the best support yet. So, I have done
evaluations where the new model wasn't
that great. A week later I did the same,
everything was the same, and it was
better because the inference engine has
been improved.
That is also part of this.
So, use the message, bring your own
everything. You have the building
blocks, check out the presentation,
think about what you want to do, which
evaluation to use, which agent to use,
which model to test.
You have the mindset now to know what to
look out for and apply this to make uh
leaderboards and charts and evaluations
that are more reliable than if you just
run something and publish a score.
So, run your own reproducible benchmark
configurations. Share the results.
If you want to work with Wolf Bench,
contact me. If you want to run some
models, that would be great. We could
collaborate and publish the results so I
don't have to run everything.
And uh if you want to make an off-spin,
that's also great.
Use another framework, whatever you
want. And if you are building models or
agents, feel free to contact me so I can
benchmark them. I work with some of the
agent uh creators already and will
publish results soon.
Yeah, that's basically the end of the
presentation. I hope you could get
something out of it. And if you have
some questions, now is the time.
Otherwise, you can catch me at the booth
and uh big shout out to Alex for the
help. The podcast Thursday I is every
Thursday
and in the morning
the time zone I'm from another time
zone.
8:30
um
Pacific time.
Every week because it's so hard to keep
track of what's happening and it's hard
for us as well so we are forced to do it
so we can report it to you.
Okay, thank you.
>> [music]
