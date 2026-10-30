# How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI

Source: https://www.youtube.com/watch?v=-AKPRSYccJc

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Um, so my name is Nana Andukquay and I
am uh developer relations lead at Kodto.
We're we used to be just like an AI code
uh code review platform but now we're
kind of expanding beyond that. that's
all about code quality and governance
across the software development life
cycle. And I've spent a lot of time um
thinking about and working on like what
does a structured AI coding uh process
look like. There are many different ways
that we're all doing it. I would love to
hear from y'all especially towards the
end of this. But I'm just going to have
what I want is to walk through what that
can look like. There's a repo I have
that everyone can fork. And if you do
nothing else from this, ask your AI to
analyze and grab some tips from the
structure of this the repo and try to
see what you can apply to your own
workflow. All right.
All right. So, we're going to walk
through just a little bit of the
beginning, who I am, Nana. Um,
definitely passionate about uh AI for
developers. This is my thing as a Devril
and as a former uh full-time software
engineer. And I live in Boston. And this
is my cat, Pippen. He's named after Lord
of the Rings Hobbit, not the basketball
player, which people ask me a lot about.
And you know, that's what this is what
I'm here for, implementing structured AI
coding workflow. Um we're going to be
using a COD. Um you'll be able to sign
into the platform. If you don't want to
use it for um some of the earlier stages
of the SDLC we'll walk through, you can
just use it for uh PR code reviews.
And uh first things first uh if you want
to you you'll want to have access to the
slides and I think the best way to do
that or the easiest way to do that is to
go to github.commyame
and then it should be the repo should be
at the top of the repository or um those
are the slides um that will link to my
GitHub or my um my Google slides.
So hopefully everybody can I'll give
everyone a minute to do that.
So yeah, slides are here. The repository
should be at the top of that. And
somebody anybody raise their hand if
they don't see it or can't get access.
Thumbs up if I'm good to move on or or
I'll wait.
Okay.
Um, so in general, where and how code
quality can break down? Uh, who who here
is, you know, using AI for coding? I'm
assuming everybody.
We have do we have Claude code fans here
and Codeex?
Wow. Wait, less hands for Codeex. Okay.
I thought they like blew up in the past
couple months. I've been using codecs
for a lot of stuff. But um where can
code quality break down in the agentic
development life cycle? Uh everywhere.
Planning and design, development, code
review, testing, deployment. There are
so many potential failure modes for um
for using AI for coding just to ship
high quality software. And that is where
we come into this process where we kind
of have to overdo it with steering AI
coding agents to get what we need out of
it just so that we can get behind or
stand behind the quality of the code and
be like, okay, you know what, I can put
my name on that. This is good to go. We
can move this forward through the
pipeline or I'm I feel safe to have
another developer review my code at this
point. [snorts] And so I really believe
that we should be building qualitydriven
systems. I think that there needs to be
a verification um aspect to agentic
engineering and it really starts with
number one defining what code quality
means to you uh and your team if you're
working on a team of developers that
needs to be defined and then that needs
to be that needs to live somewhere. it
needs to be codified so that our AI, no
matter what interface you're using, can
extract that information and do its best
to adhere to the code standards that you
have in place. And then once you've
decided where those standards live,
whether they're locally in your specific
individual repos or if they're in a
context management layer, which we'll
get into, then you can decide and pull
that into the different interfaces. If
that's your CLI, if that's your IDE, um
your your CI workflows, it should be uh
distributable.
And uh we do not have to go through all
of that. Um I already explained that we
might just be able to Okay. Well, here's
what we're going to do. We are going to
operationalize our context. Um I have a
repo that has rules. It has skills. It
has a it has you know a bunch of
different things in it and we want to
leverage that for planning for code
generation and code review and the whole
point is that we want to verify the
quality
early and often and [snorts] ideally
it's the same standards that we are
asking the agents to check against
across each of those phases. That's
that's really the whole point.
Oh, these are my skills. I have so many.
Um, and yeah, so I think uh I'm going to
go ahead and just jump into what we need
to do. Um,
so first
let's go to the Kodto quality workshop
signal pay.
If y'all can see that.
Oh, I can't increase the uh
let's see.
Okay, so this is the repo that we're
going to. It is Kodo Quality Workshop
Signal Pay. This is a payments app. And
what I want you to do is fork this repo
and let me know when you have done that.
And then what you're going to do is
clone it. [snorts] If you want to work
through this on your own time, all of
the instructions are there in the
readme. And I'm going to be leaning
heavily on my coding agents to actually
help me implement this, you know, like
at a meta level.
So, code quality workshop-signal pay.
And in this repo,
this is where we're just going to walk
through the process of planning for a
coding change. We are going to read the
repo rules to determine, okay, which
rules are relevant for this particular
coding change. We're going to use skills
and then make sure that we're writing
proper tests using some TDD and BDD
skills, test driven, behavior driven
development. Then we're going to ask our
coding agent to implement um the code
change and then run local gates. We have
llinters, we have um you know static
analysis that we're running because we
want some deterministic checks and we
want AI as well like a good combination.
And then we'll open a pull request and
have Codto uh review our PR in uh
directly in GitHub. And after that we'll
actually review what the coding uh the
issues were that Codto found and we're
going to resolve that automatically with
an agent skill. [snorts] And what are we
building? This is a self-contained fast
API payments API and um there's no front
end or anything. So we can just uh go
ahead and focus on it'll be like a it'll
be like an API that you can view in the
UI.
[snorts]
Okay, some things to
look at with the repo structure. We have
an agents MD File. We have a hidden plan
directory hidden um and rules, skills,
docs. We have the actual API itself. We
have tests. And we're using SER Grep as
well for static analysis. And we have
our CI workflow like verification um
process. [snorts]
So, first things first, we want to run
this app locally. So, I'm we're going to
use the instructions make setup once you
have cloned this repo. And like I said,
you can walk through this on your own
and just copy and paste the uh
instructions. Let's see. Where do I have
Okay, once we've done that, it should be
make run, I believe.
All right, now it's running
and
locally it should be available. And this
is the payments API that we have.
Nothing crazy, very simple. Um, not
really the point of this, but uh this is
what you should see when the app is
running locally.
Okay. There's also some other endpoints
available if you want to take a look at
that.
>> [snorts]
>> Now, you can uh choose your lane if you
want to just do this hands-on or if you
just want to observe. Here are the
quality gate checkpoints that we'll be
walking through. And uh there's a whole
setup gate process, right? We have these
different commands that we're running
and we have a verification command that
is uh pretty important. So, you have
this uh working already in your local
repo. And if you need help, ask your
agent for um changing anything locally
to make sure that this can run very
smoothly. The next step we're doing is
we are going to use Kodto. And uh what's
great about Kodto here is that we're not
just going to run this in a pull
request. We want to set up our account
with Kodto so it can actually ingest the
skills that are in this repo already and
to ingest the rules that are in this
repo. And this is going to be critical
for us to be able to then apply that as
context to the code review phase as
well, not just with your your coding
agents or when you're planning. Um, and
like I said, you don't have to do this,
but we can um we'll get to that part in
a second. [snorts] So, some standards
gates that are important to this are the
rules themselves. We have different
payments API focused rules that are
contained in this repo and it is the
agent's job to be able to determine when
I have to implement this code change
that you're requesting for me. Uh I need
to determine which of these rules are
going to be relevant for this so I can
adhere to them. They're all here in this
um in this repo as well as the skills
for implementation.
Um and then we have the planning and
test-driven development gate. There is a
highlevel plan in a planning template in
this repo and then we have an execution
focus plan and this is very detailed
templates because from what I have found
is the more detailed that you are uh
relatively speaking uh the the more
detailed that you are or consistent and
structured with your planning uh phase
and the document that your agent has to
go back to and read then it's going to
adhere a bit better and also correct
itself. itself when it realizes it's
missing some uh critical points of your
uh process
and you want to be able to identify what
is the expected behavior what are the
skills that I'm going to use for
implementation all of that is here as a
part of the planning template
and then we have the local verification
gates I use rough pyite bandit pi test
sp and uh conventional commits
deterministic evidence that the changes
made locally preserve the local
contract. I am a huge believer in
combining deterministic tools with uh
AI. [snorts] And then the last gate is
the pull request review and the
remediation gate. When we open a PR,
Kodos findings are inspected, fixes and
deferrals are documented and then we can
rerun our verification command after we
fix those um coding changes. And that is
going to be a process of completing the
code review loop um on your own and as
opposed to just stopping right there at
that local uh passing that local run.
[snorts]
Here are the prerequisites. We need git,
GitHub account, uh GitHub CLI and
Python, uh UV, Node.js JS and npm and
any coding agent that you use,
preferably co codeex or cloud code and
then we will get our Kodto account.
[snorts] Okay, so here are the setup uh
instructions. I'll let you all do that.
And we're going to sign into the Kodto
app.
This is app.codto.ai.
And that's it. Um, if you can sign in
here, you'll be able to get set up to
connect the GitHub application to the
forked repository.
So, app.codto.ai.
Um, use Who here has a Codto account
already? Does anyone Okay, great. Um,
[snorts] so yeah, sign in and sign in
using your GitHub email. I think that's
the easiest way. and uh and you will be
able to uh you'll land let's see here at
the integrations page or the homepage
and you'll need to add a connection
which will be the GitHub cloud uh
connection and it will take you through
the installation guide. I recommend not
connecting like all of your repositories
just the forked repo. It should be
listed under there but let me know if
it's not. [snorts] So, if I click on
GitHub and the installation guide,
connect your organization. Um, I'm
already connected, but it should be
listed right here for you to add. Um,
this is just an example like we're using
Kodo as an example of whether you use
Kodo or not, you'll want skills and
rules to live somewhere. Ideally, if
you're working on a team, it's going to
be outside of your local repo, unless
you have a good use case for containing
them in that repo and it's like hidden
or something. If not, there are many
there are a few context management
layers that are out there. I think
unblocked is one of them. And that's
it's just a separate place for you to
manage that context at at all times that
you should be able to pull down wherever
you are. Does that make sense?
and us using Codto is just an example.
Okay, when you've signed into the Kodto
portal, you've connected GitHub to your
fork, then you'll need to generate an
API key from the Kodto portal and you
can do that down here by clicking on API
keys on your profile and create an API
key and name it.
You'll probably want to save this API
key somewhere um locally so that you can
then add it to codto.codto
uh slashconfig.json.
So generate the API key first and then
you'll want to save it save that through
um this uh JSON structure. And again, if
you have access to the repo, you can
have your coding agent do all of this
for you. [snorts]
We also have Kodo skills. You can use np
npx skills add-toskills.
If you don't want to use it, the skills
are already local in in the uh repo.
>> [snorts]
>> Okay, this is the task that we're going
to work on a payment workflow safety
process. The task is to add one small
payment workflow. It's going to be
either a refund workflow or a capture
retry handling workflow. You can choose
which one you want, but this is an
intentionally small change, right? with
um some potential risks kind of built
into um the code or or it's a sensitive
aspect of this uh this payments API
[snorts] and uh payment mutations are
where a lot of AI generated code can
look like plausibly correct but can
introduce some issues. So I think it's a
perfect example for us to walk through.
[snorts]
Um and yeah, Veru's going to use this
all of this text really. We're going to
have our coding agent use all of this to
do either one of these tasks. Refund
workflow or capture retry handling.
[snorts]
And here is where you can copy paste the
agent prompts to get started. First,
it's like help me configure this repo
for the workshop. I have a Kodto API key
from the portal if you're using that.
And then here are the requirements for
getting set up locally. Um I am going to
since I already have this part I'm just
going to copy and paste install or
verify Kodto skills read agents.mmd and
rules and select the relevant repo local
rule ids for this hands-on task
and I'm doing that in uh codeex. I wish
I could. Let's see.
[snorts]
So, I'm in my uh I'm in the project and
I'm just copy and pasting, getting my
agent really ready to start working on
this project, giving it that context
that it needs.
and raise your hand if you have any
questions of where we're at at this
point or if you want me to slow down or
go back.
>> Right here,
>> installer verify codto skills. We're
reading the agents.mmd file and the
rules and then we are asking it to take
a look at the repo rules for [snorts]
the hands-on tasks that we're about to
implement and explain why each of these
rules will be relevant for the upcoming
task
and then I have optionally compare those
rules with kodto get rules if those are
those skills are available if you want
to download the skills
Okay, [snorts] let's see what is it
saying. I'll ground this in the repo's
own instructions first and verify the
local codto setup and dependency health
before selecting the rules.
Okay, it found uh it's aware that we're
inside the workshop
project
and it is has also identified that I
have the Kodto skills. [snorts]
Oh, the repo local workshop skills are
not installed yet. So, I'm going to run
the repos installer which will only
copies committed local skill folders
into the agent skills directory. Okay,
great. So, it's going to process the
local skills that we have. [snorts]
And I'm going to let that run. I'll go
back up to
where we are at. It's the setup prompt.
Let's see if it's made progress. After
we are clear with the agents and they're
good to go, then we're going to switch
into plan mode. And so for this planning
uh mode, we're saying use the local the
repo local workshop planning skill to
turn the hands-on task in the readme
into a highle implementation plan
[snorts] and a build session execution
plan.
And then we wanted to read agents, read
the rules and uh use any relevant skills
to determine what are the constraints.
And this plan must include an
implementation skill handoff. And that
names the first uh uh that names the
first implementation skill and the
test-driven development prompt that it's
going to be chained to and run next.
Do not write the code yet. I'm a big fan
of plan mode, but if you don't want to
use plan mode, it still has this prompt
to uh to [snorts]
make sure that you're not going to
implement anything.
It is taking a while.
Well, that's because I have all the
verification stuff set up.
All right,
[snorts]
let's see.
>> [clears throat]
[snorts]
>> All right. Okay. It's taking a while
to do this.
[snorts]
>> I'm probably going to do the capture
retry.
Uh, I've
What about you?
>> Well, I was thinking the refund, but
where do you tell it that you're doing
that?
>> Uh, it should prompt you and ask you.
>> Okay.
>> Um, and if not, then you [snorts] can
make that clear as a part of the prompt.
And what point are you at now? [snorts]
>> Okay. Awesome.
Okay. Finally, it's done. verified the
repo instructions. It ran the install
skills um instructions or uh command.
All of the local skills are now pulled
down. And here are the selected repo
local rules for this payment workflow
task.
So these are all the rules that are
going to be considered as a part of this
uh process.
>> [snorts]
>> you know, maybe I'll do the refund uh
workflow with you as well. I'm going to
copy and paste the planning prompt and
switch into plan mode. [snorts]
Um,
it should ask me, but I will say I will
work on the refund.
What was it? What is it called? The
refund.
[snorts]
Uh,
here we go. The refund workflow
plan. [snorts]
[snorts]
Okay, let's see. So I'm going to use the
repo local workshop plan from task skill
and the payment item potency skill and
then ground the plan in agents.mmd
readme and the rules. I'll only read and
inspect files. No code or planned files
will be written in this particular mode.
So [snorts] now codeex is assessing the
current behavior of the app. We
obviously we don't have this implemented
um but it's determining okay what needs
to be done what would take what would be
the shape of the code change that needs
to take place this is uh I should
probably dig into the templates actually
right now as codto is working so that
you can see what the planning templates
look like.
So here are the planning templates. I
truly believe that this is a really
important artifact to be able to take
with you if you're not already using a
structured template. Um, I think that a
plan should answer what behavior are we
changing, which rules apply, what skills
would guide the agent, which tests prove
the expected behavior, and what kind of
quality gates should pass before we
review. [snorts]
And it starts with a template for a
highle plan and then a build session
execution plan. And for this workshop,
this is what we would expect it to look
somewhat like.
And here are the templates. We have a
summary,
the problem that we're solving, any
particular constraints that we need to
worry about, and then we have skill
routing. This can be helpful if you need
to plan ahead of all the skills that you
would expect your coding agent during
the implementation to start kicking off
one by one, especially if you want to
use some type of loops um or like goals
in codeex or cloud code to work on your
behalf without you stepping in. And
[snorts] we have a scope behavior
scenarios and verification gates,
failure and recovery rules and a commit
plan. This allows for a very structured
process for uh your coding agents to
work on very specific tasks, organize
the code in a nice way that is
presentable, make those commits in an
organized way using conventional
commits, and then get to a point where
you can actually submit a pull request
and everything is organized the same way
that one would working on a team back
when we didn't have AI. [snorts]
and then the build execution template.
What I've noticed is super helpful is
having a documentation of the starting
state. What branch are we in? Um what is
the current local verification process?
Are there any commands that are expected
to run to determine that uh this code uh
passes or fails? um any of the
expectations with llinters and uh and
then of course this is the
implementation skill handoff and
execution steps. Um I want the I want to
know that the agent knows every single
step in this process of making the code
change and I want it to determine what
the test plan is um as well.
And then it's definition of done or
completion notes. You need to make sure
you've run all of the commands uh for
this uh for this branch. You need to
make sure that you've identified what
was deferred. If you've changed your
mind at some point, everything is
documented in this plan. [snorts]
And now we've got one, the refund
workflow workshop plan. We've got our
summary. We have the repo rules that are
associated, the highle implementation
plan, and the build session execution
plan.
And also there's some assumptions here.
Um,
[snorts]
who here has arrived at this at this
point?
Okay, cool. So, I'm going to go ahead
and implement this.
[snorts]
And while this is
happening, [snorts]
we can go to some of the slides.
So what I was saying about
operationalizing context, planning,
codegen, and code review, this is what I
found to be incredibly helpful for
consistency across the SDLC. I use a
combination of different agent skills
and it depends on the repos that I'm
working in. It depends on the
programming languages and frameworks
that I'm utilizing. But at a high level
and so you'll see some Python skills
here at the top like Python, Pyantic,
Pyrite or Python typing uh contracts. Um
a lot of these skills are available uh
all over the internet or you can have
your coding agent build it themselves.
And there are some ones that I've gotten
from from some popular um developers out
there. Um, and those are one's from
Aaron Francis are the audit skills.
There's audit boundaries, drift, audit
names, audit abstractions, dead code,
and auditing errors. I found that these
are incredibly powerful for really
simplifying and improving the quality of
code during the implementation um phase.
I don't know if he has these publicly
available, but if you can um look these
up or find them or have your coding
agent create them yourselves, this is
definitely a step forward in like the
right direction for quality. [snorts]
Um as I said, enforcing quality early
and often. So one of the values of using
skills and the codto get rules here.
This is about pulling down those rules
from your context management layer and
then determining um which uh which rules
are going to be relevant for the task
[snorts]
and then I believe in then running local
code review workflows. I don't care what
you know tool that you use. If it's uh
codeex, if it's cloud code, their
built-in code review, if you're using
Kodo, whatever it is, always run a local
code review because there are always
these small changes that you could
probably make earlier before another
developer has to see your code. And it's
worth it to be able to address that
sooner rather than later.
We're trying to mitigate um issues um
popping up. And then we're running
automated code review in CI or git
provider which is by default. [snorts]
And when I did this um I walked through
this entire workflow for an open source
tool that I'm building. And the proof
was in the amount of lines that I
changed in a large PR. It was
intentionally large because I want to
test wanted to test the the quality of
this actual workflow itself. And only
one bug was uncovered in over,900 lines
of code um using uh Kodto for that like
automated code review and it was one
reliability bug which made a lot of
sense. Um but this was a really good
exercise for me to see that this there
was value in this process.
[snorts]
Yeah. So I I I wish I had like a graph I
could um show you of how I have like
higher level uh I have like planning
templates that I'll use for like no
matter what repo I'm in here is the plan
structure that I expect and then there's
overall code quality like at the highest
level like engineering standards um that
are specific or that are that can apply
to any programming language and then
like below that it's okay all the repos
that use Python. Here are all the skills
for that. And like you you kind of have
to decide what would be most relevant
depending on your use case. But the more
general a skill is then the more access
it you need to have it other many repos
need to have to it. Is that does that
make sense? Um take a look at this uh
for example.
Uh, let me make sure I'm scoping this
just to my
uh
repos.
Oh, okay. Okay. Well, take a look at
this. We're in the Kodto portal and this
is the rules section. So across multiple
repos there are rules that were inferred
and ingested and saved here in the
portal and they are divided by there
there's like a a rule name in general
and like all the details that are
generated here based off of the context
from your repository and then they're
divided by categories. There's
accessibility, correctness,
maintainability, architecture, security.
Um, and then they're also uh organized
by level of severity.
Not every uh not every rule should be
treated with the same level of severity.
There are some rules that are strong
enough to where you want to block a
merge. There are others that are just
like it's good practice, but this isn't
something that it would be detrimental
if it were to get through. [snorts] Um
and yeah so this is these are some of
the ways in which uh th these rules can
be categorized and I believe they can
also be scoped to specific repos if you
want to get granular or if you want kod
to infer that uh itself or whichever
tool that you use. You can actually
design that process yourself to scope
those rules so that they rules or skills
so that they only apply to very specific
repositories.
>> Can you can you What was that?
>> I don't think so. I think Well, the only
thing you can do is like filter on that
in this dashboard. Um, but that's a
really good question. I'll probably
bring that back to the product team to
to verify. Um, but what brought up that
idea?
the repositories,
>> right? They're they're divided right now
by org level and by um repo level um
naturally or natively
[snorts]
that those were good questions. Yes.
>> Yeah.
I guess
you know how
[snorts]
[snorts] I'm just curious.
It can be. And so great question. How do
rules become rules? Like how does COD
determine um what is a rule or what
isn't? Because it seems very automated.
So you can it depends on how you've
organized things already. If you have
coding rules that are literally in a
rules uh you know directory, it's going
to be very easy for COD to be like okay
every single one of the rules that I see
here I'm just going to copy and paste
like most of those contents um in and uh
ingest it here into the portal. But
there are some rules that will show up
as uh suggestions
and this is from specifically from
reading or analyzing the actual
codebase. Um so you might not have
explicitly written these rules into your
code but these are the conventions that
Codto has noticed based on analyzing the
entire codebase. It will not
automatically create a rule for it, but
it will come up as a suggestion for you
to be able to review. And this is what
will be generated. You can edit all of
this. There are examples of good code
examples and bad code um just to make it
very clear to AI agents uh what good and
bad is. And then you can define the
category and the the warning levels. And
then once you're happy with the way that
this looks, you can then accept it uh
and activate that rule and it'll
automatically be applied.
>> Yes. Keep going.
on the other side.
How does
that
kind of
>> um for Kodto it's or
>> well I saw like
I'm going
>> [snorts]
>> Um I think for for this it's just
pulling in the local uh repo rules that
are most of them if not all of them are
associated with the different paths to
take in this workshop. Um but in general
like the codto get rule skill is talking
to the back end of the codto platform
and [snorts] it's sort of like this
agentic uh rag process of determining um
what which ones are actually irrelevant
and it filters it down
>> yeah
[snorts]
>> that was a really good question Uh,
okay. So, the plan was implemented and I
don't know why it created a draft. I
like real PRs, but fine, whatever.
Um, copy the link.
All right. Add refund workflow with
quality gates. Did you get there? Uh,
okay. [snorts]
Awesome. And here we've got the summary.
I'm just going to go ahead and make this
a real PR because what I want is for
COTO to review this
without merging the pull request.
[snorts]
If COTO is connected to your repo, this
is what you should see automatically pop
up. It's going to start the analysis
process.
[snorts] And of course, I'm not looking
at all of the code because we don't have
all day to do that. Um but the you
understand the point of uh implementing
these processes. So in a few minutes um
COD will be done analyzing this uh code
and we'll bring up any potential issues
and we're going to take a look at what
those are. Um as a result of any
potential coding issues that come up,
we're going to run an agent skill to
automatically resolve it.
[snorts]
>> Are there any other questions? Those
were really good. Yes. I have a question
and a question that follows from it is
something I've seen with skills is they
can be like super general like right try
code and like this is what looks like
and I have arguments with engineers
where I'm like this is super general it
should be in the agent's weights by now
and like I think you should wait until
something pops up but to settle these
arguments it would be really useful to
have data like this skill in the metric
shows that it's actually useful does
does Kodto offer anything like that or
how do you know these skills are
actually valuable versus just like Um,
COD is just ingesting the skills. It's
not evaluating uh the quality of them,
but there's a tool that does do that.
Tessle, have you heard of Tessle before?
TeSSL
is a um company that is all about skills
eval. And you can determine it will tell
you are there any security concerns with
this skill or is this actually as
effective as you expect it to be. That's
a tool that I would recommend for like
integrating that to uh to determine to
determine that.
>> Thank you.
>> Yeah.
>> Okay. Um, a PR summary was generated
automatically.
We've got a description and we've got a
diagram of the changes
and it's showing the legend API inmemory
store in a function. We've got the API
client and the fast API app and the
different uh let's see the endpoint of
the payment refund endpoint
that's pointing to four different uh
[snorts] fields.
[snorts]
Um, so one of the things that I would
recommend, but I I realized I just
skipped over was the verification
prompt. So we can after doing a, you
know, a a process of creating the the
making the code change and actually
doing a local review, we run a
verification prompt to ensure that
everything passes. But Codeex already
did that automatically on its own um,
just because of the way that the repo is
is actually set up. But this is would be
a best practice for walking through that
process [snorts]
and any day now codto would be great.
[laughter]
Well, we can take a look at a PR that
I've already created. And this was a PR
where I didn't run any of the processes
that we were just talking about.
But I do have the context uh pulled in
through the Kodto portal and this is
something that uh highly consider you
looking into when it comes to that
context management layer that I was
talking about here in the code review.
Codto identified that there were rules
in the codto portal that are relevant
for this actual code review. We're not
talking about planning or implementation
anymore. We're talking about code review
specifically. And then it pulled in also
the relevant skills um for this uh this
code change.
And here [snorts] there were some action
required uh results that came up.
There's a rule inside of this um inside
of my org where Python functions must
all have a dock string attached to it.
And so this was shown as a rule
violation and an issue around
maintainability.
The only reason why it's action required
is because that was determined by our
engineering org that this is of high as
high of a severity because you can
customize the level of severity of your
rules. It doesn't have to be something
that is blockw worthy. It just needs to
be something that is addressed. That is
up to you. [snorts]
And here is the evidence that's
associated with it. Require dock strings
for all Python functions. Well, I would
say methods. Yes.
Yes.
>> Yeah. [snorts] Um so this is being
determined right during the code review
phase of okay which rules are going to
be relevant. The part that can be
deterministic is that you can decide
based on the level of severity of the
rule this uh code this uh branch or PR
will be will be blocked. And so that's
something you can configure in the Kodto
portal is in the case of any action
required or high severity issue uh is
identified we block the merge until you
have fixed it and code will run again
and verify that you have. in terms of
making sure that
>> [snorts]
>> uh there's a potential that it won't
determine that their relevant rule will
actually Yes. Um and I I'm really glad
that you brought that up because it is
something that we have talked about with
the product team. Um and the more uh
enterprise customers that we speak to
the especially in highly regulated
industries, they really want determinism
in exactly that fashion. Um so that's
something I'm hoping we can push for for
making a real thing because I think it's
extremely important. I agree with you.
>> Sorry.
>> Yes. after fixes doer verification
also because changed.
>> Yeah.
>> You mean this?
>> Yes.
>> Um after I've you've resolved issues.
>> Yes. I think it's best practice too just
in case. Um you you never you never
know. So
>> is it done automatically?
um how many
>> you're I think that's more on your your
agent might be the one that will
determine like oh I'm going to run
verification or not and you can prompt
your agent to do that anyway um
regardless um but yeah so it depends on
how your your agent kind of responds
[snorts] and finally Here are the
results.
Oh, okay. Five skills were invoked.
Uh, all right. So, we've got one bug,
three rule violations, and two skill
insights.
There [snorts] is an issue with the
refund item potency stored in memory.
So, refund payment uses the process
local uh dictionary to store and replay
fund results, which is not durable
persistent storage. and we have the
piece of code that is related to that
and we have the evidence as well, the
rules and the following files.
Um, the important part here that you all
should definitely play around with is
copy and pasting this agent prompt that
is meant to fix the suggestions that uh
pop up. Um, you can do that manually for
each of the issues that present
themselves or you can run the Kodto PR
resolver to automatically resolve. Did
you already run that that skill?
>> I wanted everything to be
code or be rechecked because [snorts] it
can happen something else.
>> Absolutely.
>> It's important if we have any kind of
automation to include verification
section again.
>> Yep. I think that's best practice and
that's um that's what I would do or I
guess pregenai era um just to be careful
and that's what you want your agents to
do as well.
So that was a really uh good point.
[snorts]
Um after seeing all of the results in
this uh PR, then that's when I ran the
COD PR resolver skill and I ran it
against the pull request number four and
I saw that it's pulled down all of the
issues that COD has already identified
from critical to high. And where did it
go?
Oh, okay. So, it pulled down all of the
results and now I can decide, do I want
to review each issue individually or do
I want to autofix all um for the sake of
this uh workshop, I'm just going to
autofix all. But, uh, this is something
if you want to be a bit more hands-on
and make decisions with your agent to
actually plan how you're going to make
the fix, you can do that yourself with
the review each issue. Uh, um, option
[snorts]
autofix all.
[snorts]
And now let's see how it reacts. So I'm
going to autofix all six codto issues.
And
what should happen is okay. And you can
see here it says then it's going to run
verification and it's going to make the
uh commits and it won't be the commit
will be blocked if it's not structured
in the correct way automatically. Um,
but this is that point where it'll do
that after and it'll take that next step
further by actually posting back to the
PR and uh with a summary of all the
changes that were fixed.
And from there, that's how the PR will
be updated and all of the issues that
were resolved will be uh crossed out.
I I mean I've done I've used work trees
for for that. Is that something that
you've used?
>> Yeah.
>> Um yeah, that's not something that Kodto
really handles. Like that's something I
I found the coding agents kind of handle
themselves.
That's a good point though, a good
question.
Any other uh questions before I wrap
this up?
>> Yes.
[snorts]
>> Yes, you can run a code review. And I I
didn't run that for this because time
was flying. But um you mean for COD or
for your coding your coding agent?
So we are coming out with a COD review
local workflow and it will talk directly
to the Kodto backend. So all of the
agentic capabilities that you would have
in a pull request you would also have
locally and be able to address.
>> What was that?
>> [snorts]
>> How does it review all of the code? It
clones the repo.
>> Yeah, that's the process that we do on
the back end.
[snorts]
It's like a temporary cloning just so it
has an understanding of Yeah. the the
broader scope of the changes beyond the
code diff.
>> [snorts]
>> Really good question.
Okay, I think we are about just about
out of time. So, [snorts] it wasn't able
to go through um everything in detail,
but like I said, uh if nothing else that
you take from this, take this repo and
ask your AI some tips on what kind of
verification steps that you would want
to implement or you would want to
practice implementing locally. Um, and I
think that that would be a really good
major step to just put add automatically
add more structure into your workflows
and consider any tools. There are some
uh open-source tools that have similar
context management layers to what Kodto
does. I think um uh there's there's one
of them out there, but if you look it
up, you should try practicing having
rules and skills and other um
engineering standards, whatever it is,
stored elsewhere that your um across so
that you can pull down that information
um when relevant to your the stages of
your workflow.
Oh yes, it's called packmind, I think.
Packmind.com.
[snorts]
So definitely look into this if you want
an open- source solution for um uh
governing your AI code um through
different rules and things like that
consistently across um [snorts] your
teams and your repos.
[snorts]
Okay. I wish the internet was faster,
but it's not. So, I I I don't I can't uh
this never happens, but here we are.
Uh let me know if y'all have any
questions. Um I'm I'm here, I guess, for
the next couple minutes.
>> Thank you. [applause]
>> Let's
>> Yes.
I did.
>> I'm at a point now where I don't clear
like I let the the the context like
compact and I haven't really had issues
like I would have maybe three four
months ago with the I guess the
advancements that they have made. I just
don't experience much degradation.
>> Okay. like comp.
>> Yeah, I do. Um, but if I really feel
like it, I'll just create a new a new
session and maybe copy and paste some of
the stuff from the previous session into
it.
[snorts]
>> Yes, we have a a massive booth here. So,
>> yeah, check us out.
>> Um,
Yes. Yes.
>> Do you have any local options for
security reasons?
>> Yes, we have like onrem deployments and
pretty much all deployment options that
you would want um because we do work
with like banks and you know things like
that and um companies like some teams at
Nvidia there's like no other option but
to do that. So yeah we do that
integration.
Thank you.
[snorts]
Let's see where did Oh, there it is.
And here is the fix summary. [snorts]
>> Yeah, it did. I'm like not even I don't
even know what time it actually uh it is
right now.
And how many things were resolved? All
of them. All issues were resolved.
Awesome.
Okay. Thank you all. Uh if you have any
questions, I'll be out there. [snorts]
>> [music]
