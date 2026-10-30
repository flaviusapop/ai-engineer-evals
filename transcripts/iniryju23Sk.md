# What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma

Canonical video: https://www.youtube.com/watch?v=iniryju23Sk

Source: https://youtube.com/watch?v=iniryju23Sk

Uploaded: 2026-10-27

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Uh my name's John Feminella. I work on
AI architecture and engineering at Two
Sigma, which is a hedge fund here in New
York.
Before I get too far into things, I have
a legal disclaimer slide that I have to
show you. It says two things. One, I
promise not to sell or market or offer
you any securities at any point in this
talk. And two, everything in this is my
own opinion and not the opinion of Two
Sigma. All right, thanks for indulging
me. If I don't say those magic words,
the 5G microchips implanted in me will
explode.
So, that slide is a good example,
actually, of how our industry is
regulated. And as a regulated company
with lots of controls, I think one thing
that's always interesting is to explore
what happens when controls fail, because
that gives you a good idea about why the
controls were there in the first place.
And so, I'd like to tell you a story
about that by showing you another legal
slide.
After August 2020, a very interesting
contract clause suddenly started showing
up in a bunch of commercial loan
agreements. And this clause essentially
tries to prevent a certain scenario from
happening. And it's complicated, but
I'll explain it like this. Let's say
that you're a lemonade stand business,
and you borrow money from a lender to
capitalize your lemonade stand. And the
bank that's overseeing that transaction,
that's in the middle between the
borrower and the lender,
sends the lender all of the money that
you owe in a catastrophic mistake.
You'd probably be mad and want the money
back, but the lender might also say,
"No, thanks. You paid us back and we're
all good, so we'd rather keep the
money."
Something like this happened in August
2020.
Revlon, the cosmetics company, had
borrowed money under a big 2016 term
loan. And that loan was split up into a
bunch of pieces across 300-plus lenders,
hedge funds, credit funds, CLOs, other
banks. And in the middle is Citibank,
the administrative agent. Being the
agent in this kind of transaction means
that you're performing the plumbing that
connects the borrowers with the lenders
and managing the life cycle of the loan.
So, in this transaction, Revlon pays
City and then City pays the lenders. And
City's not lending its own money, it's
just in the middle moving people's money
around.
So, here's the plan for August 11th,
2020. Revlon would pay about 8 million
bucks of accrued interest to both groups
and the lenders' principal would roll
into this new facility. That's an
exchange of paper, not cash. So, the
remaining lenders' principal would stay
put. And the idea here is that only
interest should be going out, principal
should not be moving at all.
And the bank had a piece of internal
processing software called Flexcube.
Isn't that a fun enterprise software
name? So, in Flexcube, the easiest way
to do this kind of transaction is to
pretend to record it like Revlon were
paying off the entire loan.
And that triggers the correct interest
payment calculations to everyone. You
can probably guess what's about to
happen next. So, you're supposed to send
the principal portion to an internal
wash account that you own as the bank,
so that it's booked and recorded
correctly, but it never leaves the
bank's perimeter. So, keep your eye on
that wash account.
What was supposed to happen is that the
boxes labeled uh front and fund and
principal should all include the wash
account number and should all have a
check box checked next to them.
So, unfortunately, it turned out that
was what needed to happen, but for
various arcane reasons, uh the boxes
were not checked. And although Flexcube
pops up a warning notification that
says, "Uh-oh, money's about to leave the
bank. Are you sure you want to do this?"
That was correct. Money was supposed to
leave the bank because they were making
the interest payments. So, the three
approvers who were supposed to approve
that looked at it and said, "Yep, that's
the right thing that's supposed to
happen."
And although that warning notification
popped up, the human operators carrying
out the transaction overrode that.
Remember, Revlon was making that
interest payment.
So, the principal never went to the wash
account, and instead Flexcube sent the
entire outstanding principal of the loan
to all of the 300 lenders, about $900
million instead of $8 million.
So, every [snorts] lender got the amount
that they would have been owed if Revlon
had paid the loan in full, but Revlon
didn't want to pay off the loan. It
wanted to hold onto its money. That was
a great deal for the lenders because
remember, Revlon was in trouble at the
time, so its loans weren't trading at
face value, and getting all your money
back on a deal that you thought was only
worth 60 cents on the dollar is a great
deal for you.
So, they didn't want to give the money
back even after Citi called them and
said, "Please, that was a mistake. Give
us the money back." And their argument
was, "We shouldn't have to give the
money back because you paid us in full,
and that's how loans work. You
eventually pay them back, and just
because you paid it back at a different
time than you were supposed to doesn't
mean that we should have to give it back
now." And so, to prevent that from
happening, uh commercial loan agreements
everywhere started including including a
clause like that one. So, what does a
payment error at a bank have to do with
AI agents? Well, the bank had this
procedure, it had these controls, and
everybody did what they thought the
right thing to do was. That's the
problem I want to talk about for the
rest of this talk. Every day, we're
giving real agents real autonomy over
systems like Flexcube. And how do we
prevent accidents like that one from
either from happening without locking
everything down or just hoping we'll get
lucky that they won't happen.
So, here's the crux of the issue. You
can't really know in advance what an
agent will do, right? They're these
non-deterministic systems. Uh and that
sounds scary until you remember that
humans are also non-deterministic
systems, and they're going to make
mistakes, too.
And so, most firms don't choose to say,
"Well, in order to reduce the risk of
humans making a mistake, we're going to
like lock them in rooms and prevent them
from talking to each other, and they're
all going to double-check everybody
else's work, right?" We allow them a
certain amount of autonomy along with a
certain amount of controls. So, we give
them boundaries, visibility, and we
equip them with systems and controls
that let them do their jobs effectively.
So, in this sort of model, safety and
innovation are not opposite ends of a
spectrum that you must trade off on.
There are things that you you
at the same time. So, I think you can
have your cake and eat it, too. And when
we were thinking about what controls we
wanted to apply to agents, we also
looked at some approaches that didn't
work for us. We don't want to sandbox or
lock down everything, cuz a sandbox with
no real access to systems is not is
safe, but it's not very interesting or
useful. If you let agents go wild and do
whatever they want, that's
uh, you know, maybe powerful and freeing
from a cognitive perspective, but the
isolation is very weak there, and that
that approach is generally not suitable
for highly regulated enterprises.
And then, if you just have policy
documents that agents look at or that
are part of your uh, specification for
the prompts, that's also not very
enforceable at runtime. You can't
guarantee that that will be part of the
enforcement controls. So, what did work
for us was thinking about what mix of
controls would get us both safety and
innovation at the same time. So, how do
we provide boundaries and stop problems,
but don't hinder folks from operating
correctly? So, we have a number of these
controls, but today I'll talk about five
of them. And when I say controls here,
what I mean are the guardrails and
shared capabilities that let teams move
in ways that don't hinder what they're
trying to do. And we want to We don't
want to reach some chasm that we need to
cross to to let people get their work
done before uh, and then make everyone
wait while we build a bridge to get
there.
So, these controls are composable. Each
one does one job, and then together,
they let us run agents with real
autonomy at an appropriate level of
safety.
So, the first problem is that agents
were showing up everywhere. We have big
teams with lots of agents running. We
have small teams with a few. We have
individual people running stuff in a
uncontrolled way. And these come in
every shape. Could be random chatbots.
It could be MPC servers glued together
in this Frankenstein hotchpotch. It
could be cool notebook experiments.
Could be really useful web tools for
folks.
But, it's hard to answer when you look
at that
a few simple questions, like who owns
this? What tools does it have access to?
What should it be doing? What should it
is be doing? If if answer those kinds of
questions, if you can't govern them,
then you can't really also reuse that.
So, you're tempted to build multiple
solutions to the same problem if you
don't know about what exists already,
and then the firm can't also govern
those in any kind of legible way.
So, one thing that firms sometimes do
here is add some kind of gate, like
don't let anything run until everything
is registered and approved and it's gone
through this very onerous process. And
that sounds safe, but if you look at
what it does, the work, every idea, even
some simple notebook experiment, is
going to wait in line behind something
that's really risky. And we don't um you
know, we we don't want to subject
everybody who's given the diversity of
agents to exactly the same process.
So, most people are going to give up, or
they'll just get pushed to some shadow
IT, less governed path that is um less
visible, and then we don't get to see
anything at all.
So, that's what motivated the first
control is an agent registry. You can't
govern what you can't see. So, the agent
registry makes agents legible, and it
registers, [snorts] retrieves, and
discovers the key facts about agents
that we want to know for any agent.
Um so, those are things like which tools
it deploys, what endpoints it's going to
talk to, which product does it belong
to, who owns it.
And humans, other programs, other agents
can then use the agent registry to
decide what's available at the firm,
whether that's useful for them, and to
go use that as the source of truth for
other questions. So, this doesn't
require extra effort on your part. It
just happens when you use one of the
firm's approved agent building
frameworks, it's automatically
registered, all that information is
recorded there for you. And if you want
to do a manual registration, you can
certainly do that.
So,
the second problem we have is that now
that we've got all these agents doing
all these things, we [snorts] quickly
notice that what they're doing is really
different. And that means our agents
carry really different risks, right? So,
a thing that summarizes Jira linear
tickets is really different than a
production deployment agent that can
touch a running system. And if we can
use the same if we We to use the same
review process to cover all of these
agents, then [snorts] every agent is
waiting in the same queue for weeks for
human review, and if people are going to
route route around slow processes, then
we wind up in the same situation that we
had before.
So again, you might be tempted to say
the answer is something like really
detailed heavy manual review by all of
these different constituencies. Again,
that feels safe, but now we've got a
trivial summarizer waiting 2 months for
the same sign-offs as an agent that is
touching production systems. And most of
the good agent ideas, most of the ones
that have value right away, start out as
small experiments, and you don't want
those people to wait in the same line as
the stuff that's touching production
right away. So the reviewers are
drowning in these like low-risk
requests, and the high-risk ones have to
share that attention pool. So we don't
want to trade away that speed if we can
help it.
So again, because not every agent needs
the same review, and because most agents
are purpose-built rather than
open-ended. When I say open-ended here,
you can imagine coding agents like Pi or
Claude Code. When you open them and you
start typing,
uh Claude Code or Pi doesn't know what
you're about to ask. It doesn't It
doesn't circumscribe its purpose in any
particular way, but most of the agents
that are deployed in enterprises do have
very specific purposes. When you're
engaging with that agent, it's to do
something specific that's well known and
well understood.
So they have a very specific reason for
existing and a very circumscribed
purpose. And you can tell these agents
apart from each other by looking at what
they declare up front, their tools,
um the end points they access, the
controls that that are applied to them,
etc.
So the third problem is that if you know
about your agents and what they're
doing, you'll quickly notice that many
agents don't talk to each other, or
sorry, they don't talk to just one thing
or in just one capacity. The more
open-ended the agent is, the more it
looks like a Claude Code or Pi,
the more it can do a variety and a
diversity of different things. Call an
internal API, run a tool like a web
search, that sort of thing. And [snorts]
each one of those is a different opening
a different door to a different kind of
risk. And if you give an agent an
entitlement for a role account, then it
can do a lot more damage than something
that's just going to read a public web
page, for example. So, the question is
not can this agent do X, but what's the
granularity that we need to solve for
for the agent to act successfully?
And again, one tempting answer is to
kind of be heavy-handed here or to give
every agent the same short allow list of
stuff that's safe to do and then block
everything else.
Uh that's safe, but it's also useless.
An agent that can't uh that can't search
or can't call an API or can't do any of
those things without asking somebody
first can't really do the work that it
was intended for. And then teams either
give up on those agents or they find a
way around the wall, and both outcomes
are costly. So, a wide kind of blanket
block on everything trades away the
innovation that we want to preserve and
avoids making a real decision about
risk. Um and as author John Shedd wrote,
"A ship in harbor is safe, but that is
not what ships are for."
So, the fix here is to let agents
declare their purpose upfront and say
what tools they're going to use or what
tools they need access to.
Um so, in the second column here, we
might
say that a research summarizer is going
to be allowed to use a web tool to
access research, but for a release
deployer agent, we're not going to allow
them to do that because they have no
reason to use that tool. And so, if they
try to ask for it, they won't get it by
default.
Um so, we don't need to make this kind
of decision for every tool. The agents
just have to say which tools they want.
Right? And and you're as the agent
author, you're in the best position to
say, "I need these four things out of
the 500 that are available."
So, the way we need to enforce that is
that when agents run in our managed
environments, they look at the registry
that we talked about before to look up
what policies apply to it at
initialization time. And that policy
gets translated into enforcible
statements, like which endpoints are you
allowed to access, which hosts are you
allowed to access,
uh what other types of resources are
available or not available to you. And
in this way, nobody's writing a ticket
every time they need to change the
access, nobody's going to talk to IT or
some other group outside of your team.
As long as you conform to the risk score
that we talked about before, and you're
in the agent registry, you're you're
governed, you're approved. So, this is
how we keep the cost to teams really low
for deploying, building, running agents.
And the same control architecture works
in a variety of settings.
The next thing we noticed was that teams
were building a a ton of different ways
to evaluate agents, and every stack
looks different, and some teams don't
build anything at all. Sometimes you
build like this really detailed stack
for how your models work, sometimes
it's sometimes there's nothing, and I
think in general we'd be upset if teams
were not writing unit tests, right? And
we consider evals to be kind of the same
thing. If models are changing, that's
like a runtime dependency that your
application has, and if your agent is
going to change models, it doesn't know
without the evals what's going to happen
to its to its outputs and to the quality
of those outputs. So, again, one
tempting answer here is let's have some
kind of central evaluation methodology
that waits for a full eval suite and a
committee sign off, but now every like
prompt tweak, every one-line change is
going to sit in that same queue. So, we
don't want to put more decisions on more
reviewers for things like that. We we
don't want to trade away that iteration.
So, again, you wouldn't ship software
without unit tests, so agents need
evaluations for the same reason, and we
want to provide this stuff at the level
of the firm that's going to be the same
for everybody. So, team A writing evals,
team B writing evals, they're both going
to have many of the same features. So,
we want to have one shared approach to
how we do evals, and have the shared
approach be something that's run by the
firm and available to everybody for
doing their evals. So, that covers all
the common parts of evals, and all
you've got to do is just write what's
true about your agent.
Uh and finally, maybe you've had the
experience of being asked to approve
lots and lots of individual agent
actions when there's a human in the
loop. So, that's fine at a small scale,
but once you're operating agents in
parallel or in production, this becomes
completely onerous and review requests
come in faster than anybody can be
expected to approve them. I mean, after
the first few times of this happening,
you succumb to review fatigue where you
just see yes, yes, yes, yes, yes, and
eventually you click yes on something
that's, you know, activating a new
nuclear bomb, right? So, you don't want
to click yes by reflex, but that's going
to happen inevitably.
And one recent example of this is, uh,
earlier this year a director at an AI
research lab told her open claw agent to
suggest emails to delete from her inbox
and then wait for her approval, but her
inbox was so large that eventually the
agent compacted its context and lost the
part that said, "Wait for my approval."
And then it deleted hundreds of emails
and didn't stop when she told it to stop
from her phone.
So, again, you might be tempted to try
to make a human approve every action,
but that's not the right way to do it. A
better approach is to let these
independent, conservative classifiers
make decisions about routine calls and
then send a person only the requests
that are most important, the ones that
are most likely to make a difference. If
you're saying yes 99.99999%
of the time, then that's probably just a
rule that the agent should follow, not a
request you need to ask the human for
permission for. And the stuff that's
unclear or ambiguous or potentially
dangerous, yes, surface that to a human
or if it's definitely just dangerous,
deny it outright. So, this is a way to
not have to do all the review work all
the time. So, we don't want to take the
same approach for both explicit, uh,
when an explicit rule is applied, we
want deterministic fast paths. When
explicit rules don't apply and there's
some ambiguity, we want a classifier to
do that work instead.
So, putting those five pieces back
together, you create a registry so that
every agent is visible from the day it's
created. You score each agent so human
review goes in the right spot. You run
on guardrails so that they only touch
what they need. You share evals and
metrics so everybody is reaching the
same bar without having to reinvent the
wheel. And then finally you govern your
runtime to make sure that classification
happens there and not somewhere else. So
each of these controls works together.
So I'll leave you with one question. Why
do cars have brakes?
It's not just so that you can stop, it's
so that you can go fast and stop safely.
So controls for our agents works the
same way.
Thank you very much. I'm John Feminella
and I hope you had a good time.
>> [applause]
[music]
