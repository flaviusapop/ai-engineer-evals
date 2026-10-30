# SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar

Source: https://www.youtube.com/watch?v=bI8WyG9YB0I

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Cool. Uh so I'm here from uh Codex's
deployment engineering team and I want
to quickly say a few things to introduce
the amazing folks at Sonar as well as
Killian. Uh, so I'm gonna skip some of
the agent basics I typically talk about
because I get the feeling that this
audience knows what they're doing when
it comes into that. We're gonna dive
right into the harder questions like
what does it mean for an agent to have
completed a task? What are trust
boundaries? And we have three kind of
spicy claims that we want to present as
well. Uh, one is done means a task is
completed with evidence. two is that
containment is not correctness and three
is that the feedback contract belongs
inside the loop. So when we have an
agent loop that tends to follow a few
predictable patterns. We tend to have
this model action uh we have the
execution that is governed by the model.
We observe the changes whether that be
logs, results, output or otherwise and
we continue updating the plan. That's
sort of like the overarching agent loop
that we follow. And then with each
individual task, we have uh an outcome,
we have invariance, we have a generally
defined scope for what we're working on.
And of course, we also have acceptance
criteria as well. Uh so the definition
of done for us typically it's a
reviewable diff, some tool evidence,
that type of thing. It doesn't mean just
saying fixed. It actually means saying
fixed and providing the evidence
supporting this fact. Uh so cheaper
implementations tend to shift the
bottleneck to specification and
verification and that's really not what
we're wanting to do. Um there's this
idea of correlated failure as well and
there's typically a couple of common
failure modes that coding agents uh tend
to fall into. it tends to fall back to
incomplete context. Uh where or maybe
there's a local fix that violates some
global invariance that we have. Uh or
better yet the the generated test that
we actually do to verify results in the
same issues just being propagated
through. Uh so selfcritique is useful
but it's not an independent oracle and
we often tend to find that some of the
results of the agent and the verifier
tend to be orthogonal to each other. You
can't uh determine whether a task is
done without looking at both parts of
it. Uh so you you typically want to
almost seek out disconfirming evidence
of a task being completed uh according
to the compiler is it done according to
the tests analysis so on and so forth is
it done and it's you can't really
replace human review in the entire cycle
as well. Um the the next point I wanted
to quickly hit on is uh containment
doesn't equal correctness. Uh we have
the execution layer which typically
defines what an agent can do right what
tools does it have access to uh what
scope does it have uh per view over what
approvals does it need to act and then
we have the uh with this execution layer
we have the artifact layer uh and this
is really where the results are
evaluated uh is the result acceptable uh
what tests were produced what analyses
what policy even what intent is there Uh
so a sandbox can contain a right but it
can't prove that a query is safe. Uh so
what I'm trying to get at is that no
oracle is proof and that you want to
layer controls with different
boundaries. Sort of this defense and
depth uh these multi-layers of
guardrails. That's sort of the overall
idea. And the great part about that is
that you as a [snorts] human, you own
the intent, you own the exceptions, and
of course you own the decision whether
to ship it or not. Uh so this is one
last thing. Uh there's a feedback
contract that we tend to advise as well.
Uh typically those come with skills um
which of course are procedures as to how
to accomplish a particular task. uh MCPs
contain structured tools and context and
of course we are able to provide life
cycle checks with hooks really good for
finding out if you have hard-coded
secrets or that kind of thing as well.
Uh so with this you want to create this
full CI and human review process that
should ultimately be the core of what
the human's role is within this. Uh and
that sort of so anyways um what you want
to evaluate when you are creating this
sort of agentic process is a few things.
Uh what's the boundary for example uh
are you able to uh intercept secrets
before model input for example? Uh how
is the project grounded? Uh do you have
any concrete rules or locations or
vulnerability paths that you are able to
provide? Uh what is the scope? Are
parameters binding while preserving
behavior. These are things to check for
and of course you have to constantly run
your rechecks. Uh assert that the agents
are not the terminal state. Uh so
anyways uh enough yapping from my end of
things. Uh if there's a three points
that you take away from me, it's that
done means a task is complete with
evidence. Two is that containment is not
correctness. And three is that the
feedback contract belongs inside the
loop so you can fully take advantage of
the capabilities that your agents such
as codeex provide. [sighs] Uh so
Killian, let's uh let's make that loop
uh complete, why don't we?
That's about all for mind of things. So
thank you so much for uh giving me the
opportunity to give this introduction.
>> Thank you.
If you can take a look at this then um
and and scan it and follow through it'll
be very helpful. There are a few
prerequisites. Um again I am Killian. I
am a developer content engineer at
Sonar. Um, so thank you very much again,
um, OpenAI and Tony for giving us a
little intro into all of this. Um,
Codeex is a very powerful tool. I use it
all the time. I found it very helpful.
It's has a fast CLI. It has a, uh,
pretty smart sandbox system and the hook
system that it has as well integrates
really well with tools like Sonic Cube
like I'd like to hop into today.
So, wiring your team for agentic
development with sonar cube and open AI.
Um, the question I want to pose today is
how do we make sure that the code and
the output generated by agents like
codeex is verified that it's safe. At
Soner, we have this idea of the agent
centric development cycle.
We did um some some research in the past
year or so and we surveyed over a
thousand developers and we found that uh
42% of committed code is either AI
generated or AI assisted
but 96% of developers do not fully trust
it. Right? So the vast majority of
people do not just think hey this is
safe right off the bat. Less than half
of them say that they fully verify the
code before they push and merge it into
the codebase. There's a bit of tension
there. No one trusts it. A bunch of untr
untrusted code is getting into the
codebase. Um the reason being is that
the bottleneck used to be code
generation, right? How can we create
what we're what we're trying to do to
achieve the desired outcome? How do we
actually write the code for an
application that we're trying to build?
um with AI agents that has for the most
part part been solved with them either
doing it themselves or with the
assistance of of AI agents. So the
bottleneck has shifted now from just
code generation to code verification.
Right? We have a massive amount of code
being generated but now it is up to the
human limitation of hey how do I make
sure that this is safe? what help and
what tools can I get to verify that this
is not going to nuke my codebase or nuke
my customers and create all sorts of bad
uh issues going on. So we have uh four
steps in the AC/DC the agentcentric
development cycle. One of them is not
necessarily from sonar that is generate
that is whatever coding tool you're
using codeex anything else um that is
the generate step but sonar owns guide
verify and solve. What guide is is we
inject the agent with proper context and
that includes your project guidelines,
any rules, any specific architecture to
make sure that it has high quality
context before it even starts building
anything. We found that this reduces
token cost overall and at enterprise
scale that I mean saves a lot of money
in the long term. verify is as soon as
it's done creating uh whatever task
you've assigned to a generated code, we
want to make sure that no issues are
being introduced. So no security issues,
code quality issues, maintainability,
anything like that. None of that needs
to be pushed out to production code. And
then solve is okay, we have detected
there's an issue, right? There's some
sort of injection vulnerability or
whatever that's going on. we need to
remediate that quickly um and as
efficiently as possible so that we can
kind of have this iterative coding
system right there. And the last slide
I'm going to show before we hop into the
actual activity is uh the concept of the
inner loop and the outer loop of
verification. Outer loop is your
traditional CI system that you have set
up, right? So you write code, you push
it to GitHub, GitLab, whatever you use,
the pipeline runs and something may
fail, right? Your test or a scan or
sonar cube may fail and then you go back
to the IDE and then you try and fix it
and then you push it and then it fails
again. This has been the bane of my
existence, the bane of many developers
existences. So we want to save time by
shifting left to the interloop and
that's the IDE. So that's as soon as we
are done generating code, we want to
verify that it is correct within the IDE
without having to push it out. Um, this
saves a lot of time. Uh, I mean,
especially,
you know, being able to automatically
verify all this stuff. Time is money at
at enterprises and your engineers save a
lot of money on therapy bills as well
without that frustration. Um
all right that is the last slide I
really want to focus on uh before
hopping into the terminal. [snorts] Uh a
few quick things I want to touch base on
before that you're going to see two uh
two tools that I'm going to talk about
our tool for context our tool called
context augmentation is what we're going
to use for the guide stage and our tool
for agentic analysis you're going to see
in the verify stage. We'll come back to
those later. [snorts]
Um, and the the big takeaway as well
that I want everyone to keep focusing on
is this bottleneck has shifted from code
generation to code verification.
Um,
before we hop in as well, everyone
should have Docker running if you're
able to on your computer. And just quick
show of thumbs just so I have an idea of
people who have been able to follow
along with the prerequisites so far.
Thumbs up if you got Docker running and
are kind of primed, ready to go. hop
into the terminal and follow along.
Awesome. A few. Perfect. Thank you. Um
if not, again, this repo is available.
You can follow through with this on your
own time. Um you will have all of this
information. So, let me pop out of this
real quick. I only have limited view.
Cutting the top part of my screen off,
but should be good to go. All right. So
the first thing that we are going to do
is we are going to run this script
called apply sonar. Um this is just the
the repo that I clone locally. [snorts]
This is going to require a bash
terminal. So if you're on Windows you
can use git bash or something like that.
Um so I'm going to go ahead and type
that in. That is
apply
sonar.
All right. And this is going to do a few
things. This is a personal tool that I
built. It is not an official Sonar
product. Um, it is just a shortcut. So,
we're not spending 10 minutes clicking
through a UI or anything like that. Make
sure my Wi-Fi is doing all right. Okay.
Running through a little bit of computer
slowness up here. Um, but it'll this
will create a Sonar Cube cloud project
for you. Um, runs the first scan for
you.
Okay, EU
and it will off me in. So, we'll just
pop open the browser.
Um,
this will install a few related Sonar
Cube tools for you like our CLI and
anything else that we're going to need
to run our plugin with Codeex on top of.
All right,
bear with me as it looks like I'm
bumping into just a little bit of Wi-Fi
slowness in here, but shouldn't be a big
issue. So, that has been successful.
Um, you're going to want to put in um
the org that you want. So, the org that
you were created that was uh created for
you when you made an account. [snorts]
and that'll run. Um, this right here,
just to talk about the project, this is
a tiny Python project. Nothing
complicated. There's like four files,
less than 200 lines total. And I have
planted four vulnerabilities in there.
Three of them are security
vulnerabilities and one of them is a
code smell. And um when this script gets
done running, then we're going to hop
into the dashboard and make sure that uh
we can see stuff up there.
All right.
Normally, uh I think there's a lot of
people trying to access this Wi-Fi. Uh
I've not seen this take longer than a
minute on my own personal Wi-Fi. So, if
you're following along at home, don't
think you'll have to be sitting around
like this um for a little while. Whoops.
So, I am You know what? I may have
actually forgot to export my token,
which is a step in the repo real quick.
So, um this should be in your shell. I'm
going to pull out my disconnect real
quick just for a second so I don't
expose my sonar token to a room full of
a bunch of people. And then I'll pop
right back in.
Uh so there should be some steps in the
the repository. You will navigate
through the dashboard. I think it's
under administration within sonarcube
cloud.
All right. re mirror.
All right. So, this will run. Um, a few
things I want to talk about as well. So,
we are going to see a uh SQL injection
issue that pops in. Okay, awesome. This
looks like it's working now. Um, so
it'll go through and it'll automatically
create um everything for me in the
dashboard.
The security rating that it will come up
with is going to be E. This is the very
lowest. We have uh baked in some
security issues and uh Sonar Cube
immediately detects these and says,
"Hey, this is no good."
The next thing that I'm going to dig
into as soon as this gets loaded is just
walk through a couple issues. One of
them is going to be an open AP uh open
AI API key. Very relevant if people are
using codecs. I have done this. It's
actually right here in the codebase.
Oops, someone forgot to use an env file
or pass this in as a variable. Um, this
happens all the time. And what a lot of
times what happens is people
accidentally push these into production
code. Um, and the average remediation
time for a secret in a public repository
is 90 days right now. That is crazy.
that is your your token is just sitting
out there for all the world to see, all
the bots to scrape for 90 days. We want
to prevent this as much as possible and
we have a couple tools for that here.
Um, another issue that I'm going to
highlight for y'all here in a second is
there is a SQL injection vulnerability.
Um, and if anyone who was just perusing
through this code is a security wiz, you
may have noticed it, but um, right here
in this database.py file,
I am passing in
um, a query from here directly into an
fstring that is being uh, cursor
executed. So the argument is going
straight into the string. That is bad
news bears especially because this um
function search task is being uh given
an argument from cy.orgv
that means that anybody who controls
cy.orgv RV gets to control your
database, right? This is really bad.
Sonar Cube is able to detect this and
will let you know, hey, here is the data
flow that we're detecting. It's using
symbolic execution and taint analysis to
identify the data flow and and trace it
as it moves through your application.
Um, there's going to be a few things
that we do as soon as this is set up.
One of them is um
installing the the sonar cube codeex
marketplace. Another one is wiring that
to your project. And then another one is
um making sure that everything is is
connected in the plugin. So this is
almost done here. Apologize for that
short wait, folks. Um, and if you are
running this yourself, hopefully it is
um either finished so far or or almost
done.
This will be done momentarily. But the
three tools that I'm going to focus on
today are [snorts] the um the secrets
detection hook that we offer. We also
have a uh list issues tool through
codecs and that allows you to see any of
the issues from sonar cube within the
terminal. And then the third one is
being able to find and fix issues from
those listed issues that we pull in in
in the plugin itself.
[snorts]
Any questions so far from anyone? If you
have questions, by the way, if your
setup's not working, we have our lovely
team from Sonar over there. They're
going to wave hi real quick. Um, if you
raise your hand and bump into anything,
they are more than happy to come over
and talk to you and and help you through
everything.
All right,
analysis complete and I can go ahead and
click into my dashboard.
Open that up.
Like I said, this is going to be our
Sonar Cube cloud dashboard that shows
you all of the issues that it's detected
um within your project.
And if you've had any issues with Wi-Fi
or or being able to install any of the
prerequisites, um again, no problem.
This repo that you scanned uh the QR
code for,
just reload that.
That repo is going to be up for you.
All right.
So, here's the dashboard and I'm not
going to spend too much time here. Um,
but we can see here that this security
rating is E. There are those three
security issues. There are four total.
If I click on this, we can see here is
that OpenAI API key that was able to
detect uh that that's here. Um just
plain text in the source code. And if I
go back, the other one I want to focus
on is this SQL injection vulnerability
right here. This is the one I talked to
uh y'all with the the CIS.orgv issue.
And this is taint analysis tracing the
data flow from the source here
all the way through different files and
functions into the sync right here. Very
very helpful.
All right, popping back over to the
terminal.
Um, let me hop over to my handy dandy uh
command clipboard that I have here. I'm
going to do codeex uh plugin marketplace
add. And what that's going to do is
that's just going to add the Sonar Cube
Marketplace here.
And um this as soon as that's in, we're
going to hop into a codeex itself, we
will see the Sonar Cube uh plugin
available and we'll be able to select
that.
So give that a few seconds. Uh,
appreciate all of you all folks being
able to bear with me as I bump into just
minor connectivity slowness.
Again, in your normal agentic workflows,
I'm sure things will be moving much
faster for you.
Perfect. I'm going to pop open codeex.
Sweet. And I'm going to do slashplugins
and then just search for sonar cube and
install it. So that is get the
marketplace
run it slashplugins uh invocation and
then type in sonar cube and that is
installed.
Right. I'm going to exit out of this so
that it can reload and so I can just run
a couple more commands. Um,
I'm going to uh say sonar
off login.
That's just going to authenticate the
CLI um
which uh will allow us to use a lot of
the capabilities that the plug-in is
built off of.
After that, uh, we're going to get to
finally the the final wiring step, which
is just Sonar integrate codecs as soon
as this gets off for us.
Yep. Allow that. Perfect.
So, that will take hopefully not too too
much longer. Uh, a couple seconds. get
that updated and then we'll write um do
this integrate codeex command here.
Oh, looks like it's running into some
more. Um
try that. Look like for some reason the
the Sonor token which is exported is
getting lost.
Pop back in for youall real quick.
See if you can't see my screen again.
Perfect.
I'm going to go to the clipboard
and pull this back over.
All right. So, uh, what this is going to
do is a few different things. This is
going to get you your secrets detection
hook. This is going to get you your
agents uh MD directive to use all the
solder cube skills and this is going to
give you um other skills and uh the MCP
config as well.
It's perfect. This is just going to go
on a little bit longer and then
everything will be fully wired up to use
the Sonar Cube codeex plugin.
Quick time check. Okay, we should be
good.
So for me, this is going to install uh
two extra things that some of you who
are using the free account may not see.
That is context augmentation and that is
agentic analysis.
Uh agentic analysis is a hook that fires
instantly after any edit that the agent
does. So if you tell it to write a file
or modify any file, it will
automatically execute and that runs
serverside analysis on the code that was
just written. What context augmentation
does is it detects hey when it's about
to do something when Codex is about to
perform a task then it will feed it with
the the guidelines and uh relevant
architecture and other information like
that. Okay, we are we are finally
rocking and rolling here folks. We have
a few things that were added. Um,
specifically some hooks in here. There
are some skills under the hood as well.
And I'm going to copy this real quick.
So, I'm going to pop open codeex.
Trust all of these hooks. Thank you,
sandbox. And the uh the MCP server is
getting booted up with sonar cube.
I'm going to do is I'm going to say,
hey, can you push a commit using my
token?
This is a a fake secret that um the the
plug-in suggests that you try with
immediately. Say sure.
So you can see instantly this was
blocked. No secrets were leaked into the
L1 context. Nothing is being stored in
any logs or anything like that. As well
if you ask it to read a file with a
secret in it, it will not do it. It will
be blocked. Codex never gets to look at
any of your uh secrets or anything like
that that are that are being leaked into
your context. This is super important.
People do it all the time. We all know
what to do. Yes.
>> Write a script to read the file.
>> So,
>> that's possible. Um, this mainly works
on the tool use, right? It's it's a hook
that's invoked on on the the user prompt
submit tool. So, if that is bypassed,
then it is possible that that hook may
not be invoked. But for basic usage of
um codecs and its tools and and and
prompting it and things like that, if
you leak any um secrets into the prompt
or if there's anything, it will detect
that. Uh, looks like we're having a
little bit of internet connectivity
right here. Uh, I'm going to reaunch up
that MCP server real quick.
And so what the MCP server is going to
allow us to do is to use the skills that
allow us to interact uh with between
codecs and and the Sonar Cube cloud uh
dashboard that we saw earlier. For
instance, if we were to say, hey, list
all of the issues in my project, it's
able to fetch that
and uh and return information to us. I'm
just going to go ahead and exit out of
this real quick and open it back up
and get that Sonar Cube MCP server
booted right back up.
>> Yes.
I am very sorry it's hard for me to
hear. Would you mind walking up or
speaking a little louder? Louder.
>> Yes.
running this on my own. The apply sonar
script that get gets us all provisioned
for me never takes longer than a minute
if I'm running it on my own. Um
everything else the MCP is is about as
long as any other MCP that it takes
assuming normal connectivity. Um, I'm
doing my best to work with the
connectivity here, but um, outside of
that, I would say there's no extra, uh,
overhead that any of these really apply
for or any of these add to a normal, um,
developer workflow.
So, I'm going to double check that that
MCP is uh, up and running real quick.
And um like I said, what what the MCP
does is allows you to have access to all
of the tools to where anytime you ask it
to do something related to uh Sonar,
like the issues in your project, it
automatically detects what's going on um
and and will invoke any of those
relevant skills. One of those skills is
context augmentation, which is knowing
that okay,
we have the sonar cube tools, but our
network does not seem to be populating
uh the MCP with any of that.
Let me see. Let me see if it'll work
with us regardless. Let me say list
the issues in my
project.
Um,
any other questions so far? Figure I
might as well take a few while we're
waiting. Yes.
>> Yes. So, the the the CLI um actually
only sets up the configuration. The MCP
runs within Docker. So, it will
sometimes go through the MCP if it's
using any of the skills um that it has
there. But for the most part, this
plugin and everything just sets up the
configuration and then invokes um skills
through there.
>> The the the CLI helps you provision and
set up the MCP and everything like that.
And then there are commands that you're
able to to invoke through the MCP with
the CLI. And I want to clarify the
difference. There's a CLI that this
plug-in lives on top of. So there are
certain things where you can say hey
execute um you know this this task for
me and it may route through route it
through an MCP skill or through a CLI
command.
Okay so looks like we have the MCP it's
just running very slow because of
network because it was able to detect
that for us. So in our list issue skill
as well as this context augmentation
skill
we can also see that hey even when it's
looking at its skills we are running the
secret scan and making sure that there
are no uh API keys nothing like that uh
leaked in uh when it when it takes a
look at at any of its files including
its own skill files.
Okay,
we're valid. It's looking through all of
these and again um running into network
connectivity here. This should all
happen in a normal uh agentic workflow.
Uh much quicker than that. [snorts]
Any other questions I can take while we
wait for this to to to boot up a little
bit?
>> Uh enterprise server.
Yeah, absolutely. This is available
across any levels of of Sonar Cube use.
Be that cloud, be that server, be that
enterprise, be that the free tier. Um,
everybody should have access to this.
Now, uh, the limitation there is uh,
context augmentation and agentic
analysis are two tools that we do not
offer on the free tier. Um, but if you
have those entitlements in your org,
then you'll be able to use those tools.
All right.
So, we were able to see that we can get
those same issues that we saw in the
dashboard now available in the CLI.
Imagine that this took 15 seconds and
that the uh that the engineer has a
fully connected Wi-Fi connection. Um
they will have this available very
quickly within their IDE. Here is the uh
uh secret blocked uh blocker severity
that I mentioned earlier. But the one
that I want to highlight and get fixed
today is this S8702.
This is a rule that we wrote
specifically for AI agentic workflows.
We do not want AI coding agents to write
code that other agents are able to
exploit. That is the cy.orgv flow that I
described a little bit earlier. Again,
anybody who has access to cy.orgv
will be able to have control over your
database. We want to prevent this. So,
I'm just going to tell uh codeex say,
hey, fix s2.
That's going to run. And again, all of
these issues, you can instantly pull
them to your terminal and ask codeex to
fix it. There was going to be something
that is different on my machine versus
anybody following along is that is
you'll see as soon as code is edited and
changed here. The post tool use hook for
agentic analysis will run. What that
does is if there were any new
vulnerabilities introduced in the fix
sonar cube will scan it server side. If
you do not have agentic analysis that is
totally fine. you can just scan your
code uh during your next uh CI push or
anything like that. But um regardless it
will get verified using a gentic
analysis just closes that loop and gives
you automatic feedback to know that hey
I have not introduced any more issues.
Um, I don't know about y'all, but I have
been in uh coding sessions sometimes
where I'm like, "Hey, fix this issue."
And then three more kind of pop up and
I'm trying to fix those and it's like
trying to conquer a hydra where these
just kind of propagate out. Using this
automatically verifies that you're not
causing any new uh vulnerabilities to
come about. Awesome. So, we were we were
able to fix this. We get a parameterized
query. Wonderful. Um, and this post tool
use hook completes. What it lets you
know is is it lets you know there is an
issue in the file. However, that existed
beforehand. That was one of the issues
that I had already pre-baked in here.
So, it's not going to try and solve
everything else in your file for you. it
is smart and it just realizes that hey
whatever was in the code that we changed
we're going to uh analyze that and make
sure that there are no new issues
introduced from that code. So wonderful.
Um it reanalyzed that code in line and
verified that it passed. Um and we no
longer report uh S8702.
So we are able to find and fix and
automatically verify
um new code uh as it comes into our
workspace.
All right.
So I want to leave a little bit of time
for questions at the end. So I'm just
going to um move through to this last
piece here. And this is
um adding a new function, right? delete
a task by ID to database.py. And this
when asking it to come up with uh new
code, it will use context augmentation.
As I mentioned earlier, this fetches
relevant context rules architecture from
your project and feeds that into the
agent. Now, I have no idea how long this
may take to work. I imagine within less
than a few uh minutes. Normally, it's
seconds.
Um
however what I want you to realize as
well is that using this is the full
cycle all within the terminal as we are
guiding the agent. Oh look it finishes
very quickly. Very well done. um is we
we um get relevant context. Um we you we
get this to be fixed or implemented in
this case when we're asking it to
implement a new uh feature. It gets
verified from the uh agentic analysis
hook and if there were any issues in
there uh they would be flagged and Codex
would continue to iterate until it is
remediated. So that's how we're getting
that guide, verify, and solve uh
methodology in here. All right,
I'm not going to spend any more time in
the terminal. Um this again is available
for you to work on uh at your own
leisure. Uh there's a couple more things
in there that you can do like um go
ahead and track down some of the
remaining issues. Um if your org has
entitlement for context augmentation and
energetic analysis uh using that a
little bit
um but we are able to see that secrets
get blocked right we can do find and fix
on issues that exist and then new tasks
that we're having it do uh have a much
stricter verification layer wrapped
around it and thank you very much for
waiting through some of the network
connectivity issues with this
um I want to say that we at Sonar have a
booth downstairs. I would love uh to
come and talk to any of you guys. Would
love to chat about either AI related
coding or anything outside of that. Uh
feel more than free to come out and say
hi to us. We have swag, we have guitar
hero, we are we are um having a party
down there. Um, our uh community that we
have, our sonar community, I believe
it's community.
Is a great resource if you get stuck
working through the repo at all in your
own time. Um, that is where our
engineers who build the product are able
to answer questions and and help people
along um who who run into issues. But
thank you very much for uh listening and
working along with me. And if you guys
have any questions, uh, feel free to
come up or raise your hand and we can
work through that. Well, again, thank
you very much for coming. My name is
Killian, uh, with Sonar and, uh, I hope
to see you down at the booth. Appreciate
it. [applause]
>> [music]
