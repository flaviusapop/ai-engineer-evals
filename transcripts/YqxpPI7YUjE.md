# Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo

Canonical video: https://www.youtube.com/watch?v=YqxpPI7YUjE

Source: https://youtu.be/YqxpPI7YUjE

Uploaded: 2026-10-29

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Well, thanks so much for showing up to
this discussion here. I'll probably
actually ask for a little audience
participation as well.
We'd love to get to know how you guys
are thinking about things. The goal of
today
is to talk a little bit about Codo,
which is the organization I'm
representing, as well as how software
factories have evolved. This is sort of
what we're seeing in the industry where
a lot of AI native or AI first companies
are starting to head. I think everyone
has a grand vision of where these
factories can go, and we believe Codo is
a critical part of that, not the
complete picture of that. So, there's an
element of what we do, where we
specialize, and then areas that are
outside and we'll make sure to be clear
on some of that.
I'll I'll kind of hop into the first one
that's worth kind of walking through.
I'm what's called a solutions engineer,
so I spend time with organizations
talking through how our product or other
products might fit into their workflows
and teaching about Codo as a platform.
What I often hear from customers is that
they're super excited about going from
ticket all the way to production. From
somebody generating code or somebody
coming up with a ticket and being able
to push that all the way through, and
what they're finding is at the pull
request level or at the review stage,
they're struggling. This has become a
huge bottleneck. Code generation, I
wouldn't say is solved, but it's
definitely moving at a rate that we've
never seen before. And so, this has been
a big bottleneck. This is also where
it's critical that we provide the human
or the coding agent or the review agent
with as much context as we can to make
sure that we're making the right
decisions. This is really the trust and
verification layer.
All the other components are still
valuable, but just worth noting that's
where we'll focus a lot today is on that
review section here.
I want to give a a practical example.
Um, as I mentioned, code generation's
not necessarily solved, but when we're
looking at code and when we're creating
features and when we're trying to
generate new code, new features,
we can often miss things that we're not
trying to. So, this is an example where
we have just a one-line change. This is
on Bitwarden, which is a open-source
password manager, and you'll notice that
we have just one line change to our data
model. If I was a developer and I saw
this, it seems good to me, right? I'm
going to say this seems like the right
change. I wanted it to rename it.
I would probably merge it. I would
probably look and see that the build
passed, that unit tests passed, maybe
even my linters passed. It seems like
this is a change that we needed. This is
a feature that we wanted.
Let's Let's approve it. So, I'm curious,
maybe just from like a show of hands,
but like how are you guys when you're
talking about code review or review
changes? I would imagine you have a
bunch of tools. When they all give you
green checks, does that mean it's good
to go or what does that What does that
look like for you guys? Maybe a show of
hands, like how many have merged a PR
that they were like, "Uh, it seems good
to me. Not 100% sure. I I didn't look at
all the lines of code." Uh, maybe just a
raise of hands. Yeah.
Right. So, every everyone here, I think,
just about everyone here is like, "We
can't look at all the lines of code that
have changed. So, we rely on these
tools." There's a bunch of great tools
out there. Worth noting, not all tools
are built the same and not all uh
context is built the same. In this
example that we would have just merged,
we would have missed the blast radius or
the effect that this can happen. This
one line of code change can affect
multiple repos. In this example, again,
I'm using Bitwarden as as a sort of an
illustrative example, we have a back-end
server that could be connected to web
clients, that could be connected to
mobile or iOS devices, it could be
connected to MCP servers or CLI. And
you'll notice that all of these
components are affected on that one line
of change. So, this is typically found
in production, right? Like maybe a bug
or a user story or the web app crashes.
And so, we'd love to be able to catch
this as early as possible.
Context is king here.
Um one of the things that uh Codo will
do and I think uh is is really important
is build out a software graph of the
repositories that your team is working
on today. This will build it out
automatically and it'll also build out
an integration surface. So, not just uh
you'd be disappointed or uh it wouldn't
be as valuable if we said just Bitwarden
server was connected to Bitwarden
Android, but not what the actual
components are that are connected. And
so, this is a huge area of if we're
building the software factory, if we're
not looking at every line of code, how
do we get this to my agent to my review
agent uh to be able to take this into
account?
Another thing that's worth uh calling
out is like
not everything is
uh is is purely functional. Some are
going to be a bit more senior-level
reviewers, custom rules, maybe a bit of
taste that's involved, and how are we
learning from some of our past mistakes?
Um so, when we go back to like the
software uh factory for example here, we
have a human that reviews it, but is
there a way that we can bring that human
reviewer back into the code
intelligence, back into the review
layer, rather than it just being every
time that's the bottleneck, if that
makes sense?
So, in this example here, we have a
custom rule that we can add, which says,
"Hey, if we're going to change anything
about public APIs, we want to make sure
that we add either a deprecation flag or
we review this a bit more."
Additionally, we'd love to have this
information pre-PR, pre-code generation.
So, is there an opportunity for us to
bring this information in before we've
ever generated line of code knowing that
we have potential downstream effects if
we make some of these changes. These are
some of the areas you can see that in
this example we've got an MCP server,
we've got code base wisdom, we're
getting those custom rules or or tribal
knowledge that might exist, bring all
that into into our coding agent long
before we're pushing it up. That doesn't
guarantee that it's not going to make
mistakes, right? I think any anybody
would say that we want to double check,
but this gives us a much better
opportunity and a much better shot at
making it right on the first try.
Worth calling out here, I think
many organizations are thinking should I
just use cloud code or my implementation
agent to just do the review.
This review stage has some information,
but some of this is actually valuable in
the actual generation stage. It's also
worth noting that an implementation
agent has a bunch of other things that
it's doing that are not related to
review. And context windows are getting
bigger, but that doesn't mean that
things don't get buried, that doesn't
mean things don't get hallucinated. And
so there's debugging, there's
implementation, there's exploring the
code base versus a review agent has a
specific set of context that we want to
use. And you'll notice here on the right
we potentially have some room to focus
on other things as well. So, not just
the code base wisdom that we saw or the
graph, we can even bring in more
information that might be custom to this
specific run or this specific review
that we have potentially some room for
as well.
So, this kind of goes into the agent
that wrote the code, we don't need him
grading the code. One, we have more
context window available.
The other is we want to make sure that
these are independent. So, that can be
things like uh the LLM that's being used
under the hood, whether it's Anthropic,
whether it's OpenAI, whether it's open
weight models. Can we leverage multiple
models to try to get rid of some of that
bias? Another is the harness. If the
harnesses are the same, we could have
some bias there.
We would love to be able to swap out all
of these or even make adversarial
reviewers um that have the ability to
look at the same code and see if there's
differences in what we're finding.
If we find the same thing,
probably high signal that that's that's
true. If we find completely different
things, then it might be worth further
investigation.
Awesome. And then lastly, how do we take
this information from this specific
example and make sure that it doesn't
happen again?
Uh I know a lot of organizations that I
work with will do postmortem reviews and
these are valuable. They'll we learn
from it. Often we learn things that
don't have anything to do with code, but
have to do with organizational changes
or process changes that we need to do.
But for the code level changes, how do
we bring that back in and make that
actual tribal knowledge a organizational
knowledge that everyone can use goes in
automated fashion. And this is a this is
a huge area as well.
You can see in this example here
uh
Codo, for example, suggesting a rule
based on a comment on a PR. So, that way
we can go back and now apply that rule
to every PR in the future.
Uh you'll also see that because we have
that software graph information, we can
see the blast radius of that one line of
code change was large, we can flag that
to the reviewer, whether that's a human
or another agent, to make sure that
we're looking at this a bit closer.
So, wanted to show this at least from a
a uh
you know, high-level view of what we're
talking through.
There's a bunch of things involved in
each software factory. Context is going
to be king. So, can we get the right
data, the right information? Can we
apply those rules or standards that we
may already have or ones that we want to
learn from? And then can we check this
pre-PR using MCP CLI like there's great
things to catch at the PR level.
However, if we could have caught it
earlier, then maybe we could have caught
it at the code gen stage or have ability
to remediate and go from there. Um I'll
show a little bit of this live, but I
just wanted to at least show some of
what we're thinking, how we've seen
customers building out their software
factories. Um
curious if there's any questions so far.
I'm I'm happy to pause, but
um
what what does this look like for you
guys?
Were you Were you raising your hand?
>> Yeah.
>> Yeah, go for it.
>> So uh
during the PR stage
>> Yeah.
>> Uh we go through a review.
Or I go through a review with the agent.
I tell the agent, "Hey, I want to change
XYZ. I want to load some questions
about the code base, what was
Um
and then
I go in and I fill in some
documentation.
Basically what you're saying
where it'll get applied on the next run
of the factory.
>> Yes.
>> Uh
so you're you're doing all that then,
right?
>> Yep. Yeah, we're able to to bring in So
I'm I'm showing just some some examples
of what we do and I'm kind of focusing
on the software graph and the custom
rules.
Uh we can bring in a bunch of other
things like ticketing systems, things
like that as well.
>> Do you find that most of your clients
have problems with intent
on before
the code gets even written?
>> Yeah. So if we go back to this section
here on the uh the ticket right here,
right? Maybe the ticket isn't written
super well. Is that Is that kind of what
you're describing?
>> Maybe or
>> Okay.
>> whatever context is produced
to generate the
implementation aspect.
Um
the linkage between those two
is missing the real intent and so it's
learning the wrong
the wrong thing.
>> Guiding it. Guiding it. So you're saying
like the agent can then start going like
I think one of the that maybe a lot of
people experience is the
over-engineering of some of these agents
where I asked it to do one thing and
it's now like recreating everything from
scratch. Is that kind of what you're
describing there? And maybe even
>> We're approaching the problem
incorrectly.
It just could be
>> Totally incorrect. So not even
over-engineering just just just wrong.
Yeah.
So Coda I can maybe even show a little
bit of this live here. If I go in we've
got integrations with things like Jira
tickets or
linear tickets and then these will go
into every PR review. So if I go to like
this one for example, you can see here
we'll link in tickets directly into it.
>> Wow.
>> When you go when you go from dark mode
to light mode you really get you get
blasted there.
You can see there's acceptance criteria
in here and then if I go back to the
review
if I go back here
you'll see that we actually will
highlight requirements gaps based on
that ticket that we just saw. So this is
when we're when we're talking Coda we're
not looking at just those things but
we're looking at are we completing the
ticket? So are we actually going down
that that rabbit hole? And because we
can do this review PR
pre-PR we can actually guide the agent.
So typically what we'll do when we work
with clients is we'll say run a review
periodically. So we'll often put a skill
in there which says as we're generating
code about at your 25% your 50% your 75%
mark go ahead and run a review make sure
we're on the right path. As I mentioned
that context window earlier starts to
shrink and so like this is one of those
things where
if I go to this one
this specialized review agent can act as
almost a manager agent in this way of
guiding the agent from doing the wrong
thing or over engineering it or things
like that.
Did that help answer that question
there?
And then maybe maybe further that we
need to talk through it.
Okay.
Cool.
Any other questions, comments? Just
curious here.
Okay.
Awesome.
We'll be at the booth
downstairs
the the code of booth. I'm happy to talk
through it with you guys further. I
think a lot of our our clients are
getting towards this how do we make this
software factory run and the critical
section that at least our platform is
solving for is that review stage. How do
we give the human as much information?
How do we bring this context layer this
code intelligence and wisdom layer into
the review agent to make it as accurate
And so then
I'd say that the next layer of where
we're going is what ones can be merged
without a human looking at it. I think
today people are already doing that.
We'd love to know which ones that we
should which ones that we should not.
And so that that blast radius
information is available there.
