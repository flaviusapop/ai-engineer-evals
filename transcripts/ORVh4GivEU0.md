# Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked

Source: https://www.youtube.com/watch?v=ORVh4GivEU0

Uploaded: 2026-10-10

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Are we up? Okay.
Can you hear me? Just like this just
fine, everyone. Good. Okay. Um, so we're
we're going to be doing a bit of a
speedun here because uh uh we've only
got 20 minutes, but um I'm I'm Peter
from Unblocked. And at Unblocked, we
build a context engine. So I'm going to
show you a couple of things. The talk's
going to be split into two parts. Um I'm
going to show you what a context engine
is and how it can add value to your
organization. And then we're going to
actually go and build a component of a
context engine. And I'm going to show
you a couple of open source projects
that you can uh go and play with after
this.
So there's the agenda.
What's a context engine? How does it
deliver value? And then we'll build.
Um so let let's just hop back in time
maybe a few years to the times before AI
agents. And in those days um you were
the context layer.
Imagine
that you're a new employee to an
organization and you're just trying to
get to grips with what's what's
happening. What you usually end up
having to do is look at the look at a
whole bunch of code, rip around
documentation systems just trying to
find the information that you need to
get your work done. Um, and not to
mention like all of the the sort of
shared history that's built up over time
through an organization dealing with
incidents and the battle scars that come
with it.
Um, so what a context engine does is it
takes all of that institutional
knowledge and it pulls it in and what
you get the scattered context that goes
into the context engine and out the
other end you get grounded context which
means that the context is all
interrelated to each other. It's intent
specific. It's personalized
and it's permissions aware.
And so I'm going to show you exactly
what I mean by that. Now
let's imagine
that I'm going to go into here into
Claude and I'm going to show you a
couple of interesting sessions that I
had. So um I asked Claude here, this is
without a context engine attached to
create a plan to optimize a component in
our layer called the source mark engine.
And uh I'm sure you're all familiar with
what Claude does when it starts a new
task. It's like a new employee. It
doesn't understand anything about your
your codebase or your organization. So
the first thing it does is it reps
around your codebase and and tries to
figure out what's going on. And so you
can kind of see that here. And you know
it figures it out eventually or at least
you know it confidently projects that
it's figured it out. Um, and so it
provides kind of like a a recommendation
for me there. But now I'm going to show
you what it looks like when you attach a
context engine to the back end. So now
what it does is it calls the unblock
context engine and unblock now delivers
a very comprehensive but taskspecific
context bundle for this task. And what
you can see is that it it's referencing
not only the source code but also you
know notion documents that talk about
the architecture um pull requests slack
conversations that were had about
optimizing this particular component um
and the the the net out is that you get
this really tight context bundle with
all these links. So now uh if if um you
know Claude wants to go back and fetch
more information, it has all these great
jump off points. But the really
interesting thing is is this. So here I
spent um you know a dollar 29 on this
and it took about a minute and 30
seconds. Um that was with the context
engine but without
I'm spending up to you know 260 and 3
minutes. So what you see essentially is
a 50% reduction in cost which is pretty
incredible.
Um now I want to show you another
interesting demo
um which is uh an interesting session
that my colleague Whoops sorry bring
this out here.
It's an interesting um session that my
colleague had with unblock the other
week. So what he we also have a code
review product and Richie works on that
and he discovered that the number of
issues that the code review product was
surfacing was was starting to drop. So
he just asked unblocked and unblocked
was able to pull this information
um and and you know narrow it down very
quickly to uh a likely cause which was
that we switched from Opus 48 or Opus 46
to Opus 48 and the behavior
characteristics behind the scenes um you
know caused all those issues to drop and
uh so what he did is he asked on block
to just fix it
and now on locked um was able to just
create a PR behind the scenes and it has
all that context and it knows what to
do. But the really cool part is you can
see that it created this description and
it's it's just remarkable like it it um
understood the PR that caused the
regression in the first place and then
it found a Slack conversation where the
conver where where this was being
discussed and pulled on some of the data
here to help inform um the fix which
which is just nuts.
So, I'm going to go back to wh I think I
lost my keynote presentation here. Let's
see. There we go.
So, you have the same problem with
agents, right? Cost. Oh, sorry. This is
the wrong [laughter] It's the wrong
keynote.
There we go.
So now I think what we're going to do is
we're just going to get right into the
building part because we're we're quite
short on time today. Um and so I'm just
going to summarize this. You've got
context scattered all over the place.
You've got context in PRs, reviews,
comments, issues and tickets, docs,
conversations.
Um and and all of that is uh
semantically queryable, but it's also
structured
and rag nails the content part. Um, it
it can be it can handle things like
content questions, find the code, the PR
that changed it, the Slack thread that's
debating it, and if you wrap that stuff
in an agent loop, it can go really
really far. You give an agent loop tools
to do file search after this and it it's
very powerful
but it doesn't handle some of the other
type of uh structural questions like PRs
that I merged last week who reviewed
payments the most open PRs etc.
Um, and these are queries. They're not
semantic searches.
So, I want to just show you again, um,
going back to Richie's example here
that he started the the conversation
with unblock by asking it a query based
question because there's a temporal
element. Can you show me a chart of
ratio weekly since January 1st? Okay.
So, in order to do this, it's not going
to be able to just pull this information
from a vector store because that's not
where that information is encoded. So,
it's it's going to have to do that um
through some sort of query engine.
And so, you know, retrieval has two
halves essentially. We've got semantic
retrieval and that can handle those
types of semantic based questions. But
today, we're going to work on this the
structured part.
We're going to turn structured queries
or natural language queries into
structured queries.
But generating the queries is actually
the easy part. The hard part is the
scaffolding that sits around it. So you
need to do things like understand the
schema so you can pass it to the LLM so
it generates the a tightly bound query.
Uh you need to also be able to map
identities. If I ask a question like
open PR is by Rashene, um it's not going
to know who Rashene is because his
identity in GitHub might be completely
different. So we have to be able to map
that somehow.
And then when you get the query out of
the LLM, it's untrusted. It could have
uh operations that are dangerous. It
could cross tenant boundaries. And so
you have to have some way of validating
that the query is is uh correct and
safe.
And then finally, uh, even though you do
that validation, there could be errors.
Um, and when you actually do the query
against the database, there could be
errors there as well. And so we can
actually get the LLM to try to correct
itself if it gets into that situation.
So this is what we're aiming for here.
We want to go to uh to this. We want to
be able to say something like open PR is
by machine and then we want to get this
kind of query on the back of that. So,
just take a sec here. U this is the
open- source repo
that we're going to be building against.
And I'm going to jump right into what
that looks like actually.
So, this is the repo here. It's called
the document query engine.
And I want to show you what it looks
like when we just boot it up the first
time. So, I can say, you know,
PR is by Peter
at ground zero. Oh, actually we're
actually not running it. So, I'll go
back.
Let's run it first.
Now I can ask my question.
So, when you start it's going to have
it's not going to be wired up at all.
It's going to produce nothing. So, we're
going to just gradually build this thing
up here. Okay.
First thing we're going to talk about is
automatic schema discovery. This is
completely dynamic. is schemalist.
Not and not all databases are
schemalist, but the same kind of
principle can apply. You can dynamically
discover the schema at runtime.
Um and so what what the technique
involves is sampling a whole bunch of
documents in the document store and then
deriving a schema from that. And uh you
know I just want to show you like one
tricky part of that which is inferring
enums. Um now the the the outcome from
this is that you can use an LLM as a
Thor hammer um and it can do a pretty
good job but actually you get uh really
really far just using traditional
procedural methods. So you can you know
don't always fall back to an LLM to do
this kind of what looks like
non-deterministic work. This is actually
quite deterministic this kind of thing.
So now that we've discovered schema, I'm
just going to show you what that looks
like in our demo. Whoops. First we have
to level up to the next
and then run.
So now
we've discovered the schema from our um
GitHub collection and this is just pull
requests. Okay, so it has not only the
schema here but also um indexes that
will help improve the performance of
queries.
The next step is identity resolutions
that thing I talked about about mapping
you know users to uh real identities
and um again this is this can be solved
just using simple procedural tricks. So
um that that's actually more or less how
we do it. Uh and underneath the hooded
unblocks when we take usernames or
identities from different systems and
map them across um you can do this kind
of fuzzy matching and then in the end if
you have to you can pass a list of names
to an LLM and have it act as a
tiebreaker.
And finally, uh, the last step before we
can actually show the cool stuff is
this. It's the synthesis part. And
roughly speaking, this is actually the
easiest part. We just take the schema
that we dynamically resolve from
earlier. We take the current date and
time, uh, maybe some information about
the user that's asking the question, so
it can easily resolve questions like my
PRs and not just Peter's PRs. Um and
then we pass it to the LLM and ask it to
synthesize a query for us. And the
outcome uh will look something like
this.
Let's get to this one.
So now I can go back to my engine and
try to run that query again.
And it's going to pull the documents for
me now and generate this query.
Now the next step I I was talking about
was was validation. This is actually the
most important thing. Um
your your uh query could contain really
dangerous operators like the function
operator for example which would execute
raw JavaScript um on the DB server which
is definitely not ideal. Um, but there
could be other things that you want to
do with this. Like for example, you
might have hidden fields that you don't
want uh to be surfaced either to the LM
or for the LM to to derive and execute.
If you have metadata fields, for
example, that contain um tenant IDs and
you want to isolate each query to a
specific tenant, you're better off
making sure that the LM doesn't interact
with those fields at all and then just
constraining it behind the scenes. you
can inject those fields underneath.
And that's kind of what that looks like.
So again, we're going to just quickly
show the payoff for that and what that
looks like.
Let's go up to our validation step.
Oops.
Run it again. So if I now ask a question
like this
PRs with authentication in the title
that is probably going to drive some
kind of like regular expression thing
and there we go. Okay. So uh our
validation engine said sorry regular
expressions aren't allowed you're
getting bounced and now we're not
allowed to do that.
So validation is cool. Um but what do we
do with that? you know, we got an error.
Um, but what we can do instead is just
take that error and just loop it back in
to the LLM and have the LLM kind of
self-correct.
And that's kind of what it that's all it
is. That's all it looks like from a
technical standpoint. It's just a loop
with some sort of maximum retry.
And so if I try this again,
bounce up to my retries and run that.
Now, if I try that query again.
Oops, that's the wrong one.
Let's try this one.
Now what you can see is that it actually
took a couple attempts. Um but it got
there in the end. However, um it
constrained it down to use match and
unfortunately this is an exact title
match. We don't have any PRs with that
exact title. So we need one more thing
which is this full text search.
So now if we add full text search to our
engine um hopefully the outcome that we
get is something that looks a little bit
like this. So let's try it one more
time.
Awesome.
So there you go. We got we went from
start to finish there. This is all open
source. So you can take a look at how
it's implemented and play around with it
yourself.
And this is what we built. Something
that can effectively handle all of the
uh other half of rag. So, anything that
has to do with uh structural based data,
you can have filters, aggregations, it's
time scoped, and it selfcorrects. But
what's really cool is that it also
powers a chat agent. And so if I go over
here and I say something like
um what authentication
related things have we've been working
on last week.
Now you get this whole thing that will
show you exactly what it's doing, all
the queries that it creates.
And now it has the data and it's just
kind of reasoning about it behind the
scenes. And there we go.
Very cool.
So there you are. Structured queryable
context for agents and humans. Now
there's just one last thing. Um on the
description you probably saw that we
were promising a context engine
simulator. If you don't want to wire up
unblocked uh right away because you've
got some constraints in your in your
environment, um we have an open source
project that will allow you to do this
entirely locally yourself. And so the
idea is uh it will create a context
bundle for you on a taskbytask basis and
then take that context bundle and run an
AB test against the same task and show
you the benefits of having all of that
context at your fingertips for your
agents.
And that's the uh PR code for that if
you want that.
All right.
And one last thing, if you want some
coconuts,
come by the booth.
Thank you.
