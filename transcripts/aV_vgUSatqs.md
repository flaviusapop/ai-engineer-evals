# Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal

Canonical video: https://www.youtube.com/watch?v=aV_vgUSatqs

Source: https://youtube.com/watch?v=aV_vgUSatqs

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Hi everyone, welcome in. My name is Mark
Lumus. I'm head of developer tools at
PayPal. With me I have Naveen Kumar.
He's our tech lead for the developer
tools team. And today we're going to
talk to you a little bit about CLI.
The title of our presentation is meant
to be a little provocative and you'll
understand why at the end of the
presentation.
So today we're going to talk a little
bit about a specific kind of CLI,
interactive CLI,
and we're going to set up an exercise
and we're going to give you for those of
you who wish to participate, this is a
workshop after all. We'll give you a CLI
that you can make work better in an
Agentic workflow. So that's the purpose
of this workshop today. So we're going
to give you plenty of time. We'll talk
for a few minutes. Try to keep the
talking to a minimum and then we'll get
you started.
Now it's kind of interesting. I think
someone said what's old is new. When I
started my career long time ago, I have
gray hair.
Everything was a CLI. Everything was a
command line interface. Any of you
remember working with MS DOSs before we
had Microsoft Windows? There you go. My
first job out of college, I was
designing embedded systems. And so you
would connect to a computer over a
serial port and you would pull up a
VT100 compatible terminal and you would
start typing. And that was your CLI.
That was the the the way you interfaced
with the computer. So with today CLIs
have kind of had a resurgence I guess
you know with the maybe it was clawed
code that really made them much more
popular and now we have codecs um and so
a lot of people are are adding CLI uh
tools so that it's easier to access the
capabilities that they want to expose to
an agent. Now, with interactive
CLI, this is why we're here today with
what we want to talk about. Um, agents
shell out to Bash constantly, and that's
good.
But if they run an interactive CLI,
that may be bad because not all
harnesses handle interaction very well.
And if they don't handle it very well,
they'll fail quietly. You won't know. No
errors, no nothing.
But why do we care?
Interactive CLIs are great
because the next question can emerge
based on what way you answer a previous
question.
Flags multiply if you try to create
flags that predict all the possible
flows.
The choices are contextual and they can
also be responsive to what's happening
in an environment. So if your CLI is
calling an API and getting a response
and then the question comes up based on
what the API returns, that's really
really challenging to handle with flags
and the guard rails can live in the
interactive flow.
So here's an example over here on the on
the left. We see a a sample CLI. It's
interactive.
The CLI's opened an interactive prompt,
an error key prompt.
The human sees it. The human can use the
arrow keys, but the agent doesn't see
it. The agent sees a redraw loop, not a
question. and the harness loses the UI
state.
So here's the failure mode. It's silent
and invisible.
So the common fix will just add flags.
And flags are fine for simple use cases.
You have uh you know what the you know
what the flows are up front. It's a
single pass.
All the options are independent. Great
great use case for a a a simple flag.
But when the answers change based on the
context
or they're changing based on reactions
to real time events, that's when it
becomes a problem. You really can't use
flags for those situations.
Now, an agent is not like an automation
script.
An automation script knows nothing.
All of the decisions are pre-baked up
front. The agent can reason. It can
react.
It can ask. It can retry. It can back
up. And most importantly, an agent can
walk a decision tree
if you provide provide one. You can't do
that with flags.
So we already have a model today
for what's happening here. It's called
accessibility.
And so if you map what we do for humans
to what we need to do for agents, then
the solutions become apparent. It's the
same discipline with a new reader.
So here's the here's the challenge.
How might we keep the guard rails and
the guidance and stop pretending that
agents and humans have the same
abilities? Now, I'm not going to answer
this question. That's the whole purpose
of this workshop.
So, here's the challenge. We've got a
CLI. We call it Bris Barista 9000. It's
going to take coffee orders
and it's going to fail when you try to
run it from an agent because it's
interactive.
And if you choose to participate in the
challenge,
the winner will win a Mac Mini.
Walk walk away with it today.
It's in that bag right there. [laughter]
>> That was a challenge in and of itself
getting a Mac Mini. I'll be straight up.
Okay. Now, [clears throat] simple rules.
We're going to give you a CLI.
You make changes to that CLI, run it
through an agent,
and it's going to send some information
up to our server.
And then it's going to update a
leaderboard. And we'll put put the
leaderboard up in a moment. We don't
have two inputs, so we're going to
change the slide deck out for the
leaderboard so you can see it.
Now, here's Naveen.
He's going to talk you through this.
>> Thank you, Mark. All right.
>> Cool.
Yeah. Uh I think it's an exciting
assignment for everybody and this topic
is very near and dear to me but uh
keeping things aside Mark are we getting
any coffee after we build this
[laughter]
>> I hope so if we're successful
>> okay cool so yeah let me uh before we
start into um the assignment I want to
take to a journey right uh when I
started my engineering career I started
to play with ids. I started to use
Eclipse because I was primarily using
Java.
And as time went by, moved into
Intelligj uh Jet Brains. It was amazing.
Looking back, five or six years behind
uh things started to evolve. there were
new ids in the market especially
Microsoft VS code which gave birth to a
lot of u other ids as well.
So if you look right now Microsoft had
its own VS code editor but later on new
AI id started to pop out like cursor
windsurf to name a few.
In all these journeys, CLIs were
constant, right?
At some point, I thought, okay, you
know, CLIs are having a slow death of
their own. Maybe they are not going to
come back.
But, you know, uh I I I actually like to
see this hangover movie dialogue that um
you know, all all the four friends are
in the car and they say, "Hey, we are
back." Imagine CLI seeing that to each
other. And in the world of AI, they are
actually VC, right? Whoever bought it,
yeah, I don't know. But the whole story
is now the CLI have changed. And who is
responsible for that? Agents, right? So
this workshop is primarily focusing on
agents, your CLIs. And this is going to
be a hands-on exercise.
There are rules to it.
There are no rules to it. So feel free
to hack as much as possible and you know
the prize is here. Um so yeah we have
maybe uh ven if I can get the laptop. So
we have couple of things.
So we have yeah um so we have the repo
which is PayPal cafe. It has the CLI
that you can actually download. That's
the barebone CLI. Now, it's not going to
be that easy uh for a Mac Mini. Yeah. Uh
so, you will get some initial commands
with it. Uh play around with it.
Register yourself. Uh provide your
username, whatever you like. Um your
nicknames, anything, and
try to brew a coffee out of it. Okay,
that's that's the goal. And in this
whole exercise, we want you to also be
innovative in your approaches
and going forward, it's going to get
interesting with agents using the CLI.
So think it from that perspective.
I change this. I just change my laptops
here.
Now during the during the session, we're
we're not starting you out with any
hints.
Once we feel like enough people have
gotten the the repo installed, can run
the the CLI as is, then maybe every 15
or 20 minutes, we'll share a good idea.
Now, I'm not going to call it a best
practice. I'm just going to call it a
good idea because I feel like we're
early enough in the journey here where
we don't know what the best practices
are. We're kind of feeling them out now.
They're good ideas. I'm also hoping that
at the end we'll hear some great ideas
from you in the audience so we can
share. So just keep that in mind. We're
we're all learning. This is a journey.
We'll come back to that towards the end.
Is it not working?
Give us a couple of minutes. I think
we'll get the technical issues resolved.
seems like people are actually using it.
So on the right side you will actually
see get CLI and um if you see PayPal
cafe/ rules that's where you will have
all the rules outlined to it.
Feel free to start working on the CLI
till we figure it out.
Okay.
>> Do we have the Europe?
Oh, is it that one?
>> Yeah. Hey, there you go.
>> Nice.
>> Awesome.
>> Thank you. Thank you so much. Hey
Cool.
So you can see this is
Oh, we do see some signings. Okay. So on
the right side you will see get CLI. You
can download that and I hope you guys
can see it. It's at the bottom right.
And there are some rules here. You can
click on these rules and it will pop out
some rules.
So, we'll probably take around about 25
to 30 minutes. Um, and in between we'll
interrupt with more slides and make it
interesting. [laughter]
>> Where's the laptop for the other slides?
Venode's got it. Okay, that's fine.
and we're here to help. If you're having
trouble, please raise your hand. We'll
try to assist you as best we can.
a little bit about the models.
Don't use models.
Now, we had a little bit of a debate
internally. There are some great models
out there.
The interesting thing about this
challenge,
if you use the highest thinking mode on
the bleeding edge LLMs, you can probably
brute way brute force your way through
this.
But I feel like in the current climate,
teams are starting to think about their
token budget. And so you don't
necessarily want to waste your
highinking tokens on
running a CLI tool. So the real
challenge is can you make Haik coup or
sonnet or something at that level
run your CLI? We know you can do it with
the highest. Can you do it with
something that's somewhere in the middle
that's faster and cheaper? That's the
That's the interesting challenge if you
if you want to take it on.
>> Sounds fun. Yeah.
>> Awesome.
Since we are on the coffee topic, uh
Mark, were you aware that San Francisco
City has the best bakeries in the entire
United States? Were you aware about that
fact?
>> I was not aware of that.
>> Yeah, you should definitely.
>> Go on. Yeah. Go on, tell me more.
>> Um, I have I've done some bakery crawls
uh around in the city and they are so
fun. Like you should definitely check
out all the amazing bakeries out here.
>> Okay.
>> Yeah. Any favorites? Butter and crumble.
My favorite one. Although I couldn't go
there. [laughter]
Awesome.
So as of now we have J Gray Codex
at the top. So guys please catch up with
him or her
So with the init command, you could
actually register your names.
I hope some of you have figured that
out.
Do you want to talk about the first
You might have to think about
Once I plug it in, I
>> [sighs]
>> Go ahead.
>> Okay,
>> cool. Um, let's move on to some
presentations. Meanwhile, you can start
working. I mean, you'll continue working
with the CLI that you have. But as as a
first hint, you know, it's it's a good
idea to start using T-Max. How many of
you know about T-Max here? Okay, quite a
fair amount of audience out here. Um, so
yeah u in short start with running T-Max
and um start by putting help command.
Now, help is really important because
every AI agent in today's world relies
on the help command before it even
starts using that command.
[laughter]
So,
yeah, send keys and capture pain gets
you far. Now, T-Max actually um for
those who actually don't know about it
is like a multiple you could actually
use multiple terminal sessions uh with
the T-Max and it's like a split pane
feature that you could leverage with
T-Max.
So, with this example, you can see here
um I mean the screen is very short for
me. So, let me just zoom in a little
bit. Yeah, T-Max D. Now, what this
flag does is it detaches
the entire uh CLI and puts it under a
different emox instance all together for
[laughter] you.
So
you could see
size uh T-max capture pane like I said
you could actually have split panes in
T-maxes. So you could actually take care
of u working around with um in in the
CLI and uh that's one of those cool
features that can help your agents
perform lot of activities. Um, think of
it when you want to run multiple agents.
You could actually spin up different
sessions and T-Max actually takes
a log of those things where it knows
what are you working on and resumes
those sessions whenever it's needed. So,
it's actually helpful for agents to
communicate and start communicating when
they have multiple sessions open. And
these are some long running tasks that
you could actually run inside T-Max.
[snorts]
Second good idea is IPC site channels.
So like I mentioned before, T-Max was a
good upgrade.
So instead of doing screen scraping,
which T-Max actually does um for visual
in inference, [laughter]
you could start using side channels. Now
[snorts]
site channels would help you define your
arrow keys that you have and help you
understand and I'll go in the next slide
uh how it works but the agent should
know what is the output JSON now this
becomes really critical in the entire
talk is output JSONs and Asians want
that since we have multiple
personalities now earlier we used to
only cater to human beings now we have
agents. So think of both these personas
so that your CLI can actually take
advantage of both these use cases.
So site channel for those who don't know
about it let me explain to you in in
simple words think of it like adding a
REST API to your web application and the
website gives humans a visual interfere
uh interface.
The API gives you a machine structured
interface right so think of side channel
as exactly the same that's one of those
analogies that I can refer
read state send input as a data
[clears throat]
so we have the bista brew hyphen agent
now this this is a command that will
help you run
your CLI with background agents, right?
Um, you want your agents to be running
in the background and uh you put all of
these commands, they are going to help
you try using it in your current CLI.
See if you are able to
um make some progress in the barista
application that is out there for in
your laptops.
Now, there are a couple of things that
you could actually provide as an example
out here. You can see barista
[clears throat] brew ask and then
there's a bunch of information out
there. Oh, what is it? Okay, fields then
small, large, medium, maybe the sizes of
the coffee and yeah, default as large.
What does that even mean? That's input
data, right? So all you have to do is
feed in this input data so that agent
actually knows that and you got to do it
in machine readable formats.
So this is where um that thing comes in
play.
So don't just tell the agent what the
human sees, okay? Think it out of the
box. What are the agents going to think?
They have different skill sets and you
have to start leveraging those skill
sets.
Same prompt with a different brain. Now,
[clears throat] so on the left side you
see I was talking about different
personas. One is the human beings and
the other one is the agents.
The CLI is the same but when you look at
the way it is structured human beings
want set of options but on the other
hand you have agents wherein you could
provide all this information in one
single input file. [snorts]
Okay. So this is where we call this as
context injection comes in play. You
provide context in such a way that let
me take an example. You you are actually
low on oat milk. Okay. And uh you have
only two gallons of uh oat milk left.
Tell your agent what kind of information
it needs to ask the user.
confirm it if if two ounces are good
enough. Do you want me to pick a backup
for you?
This information should be provided
using context in injection as a
technique and you can leverage this in
the CLI that you are actually building.
Try using it. Maybe you'll be on the
highest on the leaderboard.
So we started a journey from T-Max which
is basically
screen scraping to injecting skills.
So T-Max is low effort. I think a lot of
you might have tried it. But this is
where site channels [snorts] also will
help you in providing [clears throat]
good um sort of feedback to your agents
and context injection will provide you
those different scenarios that you can
think about which doesn't happen in the
human case.
So yeah, keep pushing your scores.
You want to show this?
>> Yeah.
It
does take some time.
>> There you go.
>> Okay, [snorts] cool. We do see a lot of
traffic out here. [clears throat]
[laughter]
Oh, somebody is really close to 5,000.
Is it bank?
Okay.
[clears throat]
Any questions so far? Anybody wants to
get it answered? Any queries?
>> Sorry.
>> [laughter]
>> Okay, let me repeat that question to
you. [clears throat] What happens if
multiple people reach a score of 5,000?
Mark, you want to take that?
>> So, the the idea was we would look at
score and if there's a tie, we would
look at which one took the least amount
of time. Now, based on the resolution of
this, I see several that are that have
completed three of three in zero
seconds.
I see [laughter]
a bunch of these that have completed it
in zero seconds. So,
I need to consult with someone because
that's not supposed to be possible.
But the idea is that we would look at
the high score the the score first and
then the time it takes to respond
second. So that an accurate response
returned quickly would be biased over an
accurate response returned slowly.
So we have only one for now.
>> Okay, sorry.
>> We have only one.
eventually comes
to
this is the bottom of the leaderboard.
Nicholas [snorts] game up.
[clears throat]
0 second.
Do you want to
wait two more minutes?
We can open it up ideas
how engaged they are.
Did we have
>> [clears throat]
>> In just a few minutes, we'll
open up the floor for some idea sharing.
So, I'm I'm hoping that we'll hear some
great ideas that go above and beyond our
good ideas because I know that there's
some out there.
Mark, were you expecting so many people
to be in the 4,000?
>> Yes, absolutely.
>> At this conference?
>> Absolutely.
>> Awesome.
Were you not?
>> No, I was. [laughter]
What do you think? Anybody can make it
to 5,000?
>> I don't know. We'll hold it open.
[laughter]
>> Why don't we open the floor up now?
>> Yeah, sure.
We'd love to hear ideas. So, did anybody
in the room come up with other ideas
that were able to get them to such a
high score so quickly?
Nobody wants to leave the desk.
[laughter]
Oh, we have Yes.
Let me let me come over to you
[clears throat] because I can barely
hear you.
>> Okay.
it it's a very easy to game benchmark
because the only thing that matters is
you fulfill one order within like small
like a very small latency. So if you do
a deterministic parser um it which
defeats the spirit of this challenge
entirely but you deterministic parser
and you have something like really close
to the server you can get the latency
down uh really quick if you just brute
force it.
>> Okay, which is that what you did?
>> That's what I'm doing right now.
>> Okay. All right. Now you said something
interesting the the deterministic parser
that's running in your CLI.
Okay. I actually like the idea of the
determinism in the CLI.
And [clears throat] the reason is that
if the CLI is a tool to be used by an
LLM, then you absolutely want it to be
deterministic. The LLM is the
non-deterministic player here. We want
the CLI to be as someone described it a
small sharp instrument. Should be very
very focused on what it does. And every
time you give it a command, you want it
to come back with the same response. So
you don't want to build an agent into
the CLI and then hand that CLI off to
another agent because you don't know
what you're going to get.
Any other interesting ideas?
Obviously we a lot of people have
figured out how to game the system.
>> [laughter]
>> Where there's a Mac Mini, there's a way,
I guess.
>> Yeah.
[laughter]
Wait
five minutes.
Five minutes.
The score hasn't changed in a while
before the site crashes.
>> Did you do refresh?
>> [cough]
[clears throat]
>> Why does it say reconnecting? Oh, there
we go. Okay.
See, the network is a little laggy. The
network is a little laggy out here.
>> A lot of lot of computers.
Sounds good.
Crash.
And we're frozen right now.
[clears throat]
Here we go.
No change in the results. Okay.
Do we want to wait a few more minutes or
call it?
>> Yeah, five minutes.
>> Five minutes. Okay.
You want to bring the PPD to PPD for the
closing arguments.
>> We're going to give it about five more
minutes.
>> Yeah.
>> And then we'll call it.
>> Where's Bon? Where's Bonk? Raise your
hand.
>> Who is Bon? Okay, we have something.
>> All right. Big smile. Big smile.
[laughter]
Now,
>> we do want to hear how you did it.
So once once we call it, then we'll
we'll we'll we'll let you explain what
you did. I'd love to hear.
[laughter]
I need to go over here.
>> Yeah,
>> hold on.
Sorry. I should have asked for another I
should have asked for another microphone
for the room for questions.
>> Um, yeah. So, Bonk is just a an agent uh
thing built on top of cloud agent SDK.
Um, it built the whole thing. Prior to
this, I already had a sort of eval bench
skill that will create sort of an
environment and um optimize. So, it
basically ended up building a uh
deterministic
CLI solver and then now it's just
running on a T-m slamming your APIs.
>> Okay.
>> Yeah.
>> All right. aso. I think I got lucky
because I hit it at one point at like 29
milliseconds. Uh probably because we're
in the same region.
>> Okay.
>> It's just a network latency,
>> right? And this is all done on claude
>> uh claude agent SDK. Okay. Just driving
it through Slack.
>> No, which model?
>> Opus 4.8.
>> Okay.
>> Yeah.
>> Did you try it with any other models
>> for the build uh for building the CLI or
>> for for your a for your agent? How would
we do that? The CLI is completely
deterministic. Sure. Sure. So, so the
agent built the CLI and is just running
it on T-Max now.
>> Okay.
>> Yeah.
>> Awesome.
>> Yeah.
>> Congrats.
>> Going to go to the next one. Danny.
Who's Danny here?
You see
last one.
[clears throat]
What do we want to know?
>> Yeah. How'd you build it?
>> Yeah. So, I don't know anything about uh
coding at all. I'm I'm using uh I'm
basically a Vibe coder. I have a couple
agents and I just said, "Hey, here's the
problem. Read it and then fix it and fix
it." So, I just have Yeah. Cloud code up
on uh VSC.
>> Have you ever built a CLI before?
>> Uh no. I I saw a couple hours ago that
obviously there was a prize to be won.
So, I got in and I said, "Hey,
[laughter]
uh figure this out. Explain it to me
like I'm, you know, like I don't know
anything." And then explain like I'm
five.
Yeah, I I I don't know. So, and then we
came up with uh yeah, we came up with
some good results and I said, "Hey, we
need to make it faster and give me some
suggestions and yeah, seriously." So, I
I guess [snorts] we have uh two scripts
running and the first one got the uh
49.98 and then I said, "Hey, make a copy
and give me some suggestions for how we
can get the 49.99."
>> Right.
>> Did you get any suggestions? Uh it's
this agent's pretty automated. So I just
say like hey here's the start here's the
end give me a couple you know questions
at the beginning if you need it but then
fix the problems so I don't have to deal
with it kind of thing. So sorry that's
not a very good
>> No it's good. I'm I'm sure a lot of
people are wondering like writing a CLI
is that something that you would ever do
or would you ask your agent to do it for
you? So clearly we have many people in
the room and just going to point Claude
or Codeex at this and say build a CLI,
make it fast, make it deterministic. And
those are the three ideas, right?
Okay. You want to change the slide?
There it is.
>> [clears throat]
>> So, we talked about
all of our suggestions.
We heard some ideas.
The predominant idea was let your agent
figure it out for you. I love that idea.
Um,
anything else before we close it out?
All right, there you go.
Takeaway for us based on our
instructions, our recommendations.
Give it good context, give it a side
channel,
and tell it to use T-Mox. Those are
three good ideas to start with.
Thanks everyone.
Bonk, you want to come on up? [applause]
>> We still have Monk as the winner, right?
Yeah. Okay. No, no, we called it. We
called it five minutes ago.
>> Okay.
>> Yeah. Yeah. I'm not gonna change
[clears throat] I'm not going to change
it.
>> Yeah.
>> We We called it.
>> Awesome. [applause]
>> Let us
[clears throat] We'll get We'll just get
a picture,
>> you know, social media. That's right.
It's a real Mac Mini.
>> It's a real Mac. Oh my god, these exist.
[laughter]
>> All right, awesome.
>> Where'd it come?
>> [music]
