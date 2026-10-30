# The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef

Source: https://www.youtube.com/watch?v=KhRjivBSwiw

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

We'll get going. Uh my name is Yonyi
Michael. I'm one of the co-founders of a
startup called Typede. Uh we're here to
do along with uh our founding engineer
Brandon Calendarer this workshop. Um we
have a two-hour time slot. We're going
to try and keep it as interesting and
fun as possible.
Uh, I know it's very tempting right now.
You guys all have your laptops out and
Germany's down one- nothing in the World
Cup game, but it's our promise to try
and make it as fun as possible, so you
don't feel the need to be streaming
that. Um,
so, um, what we're going to talk about
today, uh, is we're going to do like
before we actually get into the fun,
roll up your sleeves, do more of a
technical workshop, I wanted to walk
through a little bit around the problem
set that we're trying to solve here at
Typedev. um and kind of set the stage
and give some context for concepts and
principles uh that will later be applied
to the actual workshop that Brandon will
lead us on. Um so the main idea behind
this talk um is the background on typed
defeaf. We're building uh the enter the
trust layer for data agents to be able
to access and perform uh high complexity
tasks on data platforms and data
systems. Um and so the title of the talk
is the data context layer which is a
core piece of infrastructure um that
we've actually built to help us with
that mission. Um, and so, uh, a lot of
it, uh, comes from the idea that perhaps
maybe you guys aren't as much into the
data space, but once you try and
unleash, uh, coding agents or software
engineering agents on the data, it's
actually a lot more of a nuance, complex
environment, and there's a lot of things
that you need to think about when
building the right harness, when context
engineering for these agents to be
really effective. That's what we'll be
talking about. The punch line is like
the the model isn't the bottleneck. The
model's going to continue to grow in
capabilities. Um but the missing context
to make these agents actually effective
is the important part in this. Um so
this is what we call the data context
layer.
Um all right so here's the bet that
we're taking as a startup called typed
defeaf. Um all of us have spent let's
say like uh the last two years generally
in the industry um going and thinking
about context engineering for coding
agents right so we have like the the
anthropics the codeexes of the world the
cursors um where you're able to
understand how to map repositories
effectively do retrieval and then tool
design for these coding agents to be
really effective. um where we're falling
short and where we're starting to see
there's more of a need for is that the
same thing needs to be done for agents
that are able to access and touch the
data and the data is exactly where uh if
an agent is confidently wrong which it
often time is it can actually end up
costing a lot of money right because a
lot of these metrics and calculations
that we're asking agentic analytics to
actually do wind up on things like board
decks um or their metrics in a model or
their pipelines that fail quietly that
have really really important important
features and and um and metrics and
measures that they're trying to
calculate. Um so the core bet that we're
saying is that agents are going to be
core operators of these data systems. In
order for them to be really effective,
we need to be able to ensure that when
they do read and write actions, they're
able to do these actions safely and
accurately and be able to trust these
results at scale. And that only really
works if you're able to give the agent
the reasoning layer so that it can
actually understand the data system end
to end very much like how a data
engineering or a data team that actually
has working knowledge that was able to
build the system from end to end is able
to also reason about it. So that's the
goal of the data context layer here.
Um, so where I'm going to say what we
found over let's say the last year and a
half of us building in this area is that
there are three general concrete areas
where today's let's say coding agents
fail over when you're trying to get them
to be effective in data. The first thing
is impact analysis. So essentially like
what breaks if I actually make this
change. Um the next thing is join
recommendations. So if the is this
actually is this join actually safe for
me to make across my data system and
then safe code changes generally as well
right safe transformation logic changes.
So does this edit still mean the same
thing? Is it preserving the meaning of
this metric or is this metric definition
now going to change because I'm making
this data commit and this data change
that's happening. These aren't fringe
tasks, right? These are like the
day-to-day uh tasks and workflows of
like data teams um as they're thinking
of how to actually get enterprise data
to be working with AI. And if your agent
can't reason and do these tasks
reliably, it's very hard to actually
trust it. It's very hard to actually
trust it to give it right and even read
access many times. U and that's what
actually matters is be able to get them
to be effective core operators of our
data systems and [clears throat] not
just like question and answers types of
agents.
So here's the gap the core gap that
we've been able to define and like
really discover through our work here.
Um this context that the data needs is
uh is uh distributed across many
different systems, right? So your
warehouse can have the store. It stores
the the rows and the actual data itself.
Your transformation code has the actual
business logic that's really important.
Your BI tool stores the metrics, the
dimensions, some business definitions in
there. And then you have your docs and
Slack channels and um and Slack threads
and like tribal knowledge that
oftentimes lives in like people's heads
as well, right? But the agent actually
needs something in between all of that.
It needs to actually understand what a
model means, how it relates to other
models, what breaks if I make this
certain change, um and then which
operations are actually safe to make,
right? Um and for the next let's say 15
minutes while I'm going over this like
we'll be using like um a term that's
called grain. So for all of you like
non-data folks in the room what grain
actually means from like a data team
perspective is um is uh um sorry is like
what does each row of the table actually
mean? What does each row actually
represent? Um and so if the grain is
customer by month uh and I accidentally
turn it into customer by week then every
downstream sum after that uh can become
wrong even though the SQL compiles and
everything runs correctly right so
that's what I mean when I talk about
grain change um
and so let's make this a little bit more
concrete like in terms of reliability
what does it actually mean if someone
asks an agent why a pipeline's row count
row count suddenly spiked and it jumped
40% overnight. Um, the agent can go and
write valid SQL. It runs it. It could
render a beautiful chart, but at the end
it's going to report the wrong root
cause, the wrong analysis of what
actually went wrong. It says, "Looks
like there's more data that came in. Um,
but what actually happened is there was
an upstream column that uh turned a
onetoone join into a one to many join,
right? So that means the grain actually
changed. uh and the agent literally
cannot tell a real spike like a real
data spike and differentiate between
that and like an actual grain change
because the grain isn't in the data
itself, right? Um and so the agent can
run the query, it could get some sample
rows, it could sample the data, it could
read the SQL very well to understand,
but it didn't know that what one row was
actually supposed to mean and that now
it means something completely different.
Right? So this is why valid SQL isn't
enough, right? Right? The semantics are
actually very very important when you're
trying to get an agent to be effective.
So then let's say like the like thinking
on it, there maybe two obvious fixes for
what you can do for this type of
scenario. And this is why neither
obvious of like neither of these obvious
fixes actually works, right? So you can
give the agent the code, right? But the
problem with that is if you go and give
it let's say like your DBD project or
airflow project it's redriving the
context every time from scratch right on
every single prompt which means it's
probabilistic um it's bounded by the
context window which doesn't always work
very well and then every time you start
a new session you have to go and rebuild
that context from scratch. Then let's
say okay let's try and give it database
access. So I'm going to connect my
snowflake or datab bricks MCP to it. um
and instead it can see the rows and then
it can pro it can it can see sample some
data but it doesn't actually have an
understanding of what each row actually
means. So it can read the numbers but
not necessarily explain it right. And so
the first situation is one can read uh
uh one can read the code but doesn't
actually have memory to be able to
persist the knowledge of the context
that you spent a lot of time going back
and forth and having bu build up and the
other sees the data but doesn't actually
associate the meaning behind it. So
neither has like a persistent model of
how the system actually behaves and
that's the mission that we set out to
try and solve.
So let's like take a step back and name
exactly what's missing from the context
that you need to actually give the agent
to be able to reason effectively across
these uh uh complex data changes. There
are four facts let's say that decide
whether an answer is right and none of
them are actually written down anywhere
that the agent can read or infer. So the
first thing is what what one row
actually represents in a table. This is
what we talked about the grain. The next
thing is whether a join is safe or not.
And then there's what a metric actually
means and what relates to what. Right?
The dependencies are very important um
in data systems. [snorts] And so an
agent can read your SQL just fine. Um
but it can't see these four things very
easily at query time when it's the most
important time for it to gather the the
exact context that it needs. So the goal
of what we did was let's see how we can
make them computable and queryable so
that the agent is effectively able to
grab just the context it needs just at
the time it needs and not have to
rebuild it during every single session.
So the next few slides are about how we
actually went about doing that. Um and
so let's take for example the join idea.
This is like the the second fact that we
talked about in the previous slide and
this is because let's this is a good
example because it's a cleanest example
of like why syntax isn't actually enough
to be able to get the agent to be
effective. So there's one join, we call
it like an an equa join that's happening
here that's written a certain way, but
it could have four completely different
outcomes depending on the underlying
data, right? So it can either preserve
your rows, it can look up a dimension,
or it can silently replicate every
single row when it goes from like a one
to end type of relationship. The same
thing is for this between clause that
happens oftentimes in SQL. So it could
be a safe as of lookup or a date spine
that actually explodes your grain,
right? So the agent can see this syntax
but it can actually understand which of
these scenarios is going to result
because of this syntax syntax. That's
not really a model or capability
problem. That's like a context problem
that we're actually trying to arm the
the the agent with.
The fourth fact in here and this is one
of the more fun ones that I like to um
to show off is that um understanding of
like what models what data assets relate
to other ones. Right? So this is which
models are in the revenue domain for
example, which are in the product domain
and those oftentimes correlate to the
personas of the people that are actually
trying to access or run the datas to
access these uh the core metrics or
numbers that are in these uh in these
domains. Oftentimes today like teams
will organize it based on folder names
and a lot of times it's tribal knowledge
to understand which models relate to
which um business units. But you can
actually discover it from the you can
actually do more and actually discover
it from the structure of the data. So
for example you can take a look at how
the models actually connect looking at
lineage for example table level lineage
column level lineage looking at shared
keys looking at shared naming. So the
system clusters them automatically for
you into the domains so that when you go
and ask the agent okay which models are
in my revenue domain for the revops team
um it becomes a query that the agent can
actually run and not a question it has
to ask like you know that has to go back
and forth with the human to be able to
understand which are in the same domain.
So this is kind of the same principle
for context engineering that you see
over and over again. It's you take
something that is tribal knowledge that
lives in someone's heads or lives in
some documentation elsewhere and you try
and actually compute it and then make it
queryable for the agent.
Um, so how do you actually produce these
facts, right? And the key principle here
that we talk about a lot is like you
want to always be as deterministic as
possible first and then only use LLMs
when you're trying to resolve ambiguity
or do things that models are actually
really good at, right? And so you're
able to compute grain and lineage
straight from the actual SQL itself. So
what we do is we actually take all the
transformation logic and we parse it all
the way down to the as to actually
understand how the data is actually
structured right and that way the agent
can't drift from the actual
implementation itself because the the
basis of the graph and the context we're
giving it is actually derived from the
implementation itself. Um and then uh
and then you can do things like verify
join safety against the actual data.
Right? So is the join key really unique?
This is something that you can do by
profiling the tables, right? So you're
able to go and profile the the tables
that you have in your warehouse. Um, so
that allows the agent to not really
guess about things like cardality. And
then you can use the LLM for things
where the human readable parts of it,
right? So if you're trying to understand
business names or summarize the utility
of models or resolve any ambiguity from
like the first two layers in there,
that's where the LLM can really come
into the picture.
um these facts are computed and then
checked against your data so that the
LLM um uh just kind of names these data
assets at the end on the graph that
we're building and that allows it to
make sure that we're not actually
drifting from the core implementation.
That separation matters because um it
keeps the core facts tied to the actual
implementation kind of like we talked
about and to the data itself.
So that's all good and great. Where does
this all live? What we call we call it
the data context layer. At the end of
the day, it's a graph, right? And it's
computed once and then on every commit,
it's refreshed atomically, right? So,
we're incrementally modifying the uh
this context graph as data teams are
making more data commits to it. So, it's
always representative of the the
freshest state of uh your production
enterprise data. Um, and the reason is a
graph. The reason it's a graph and not
just a pile of text or the robust set of
markdown files is because of the access
pattern, right? So the agent's able to
pull exactly the the subgraph it needs
in one traversal. Um, and it avoids
things like prompt stuffing or context
stuffing and it scales way past 500
models because you're not like rereading
the project every time you're trying to
build the context layer. Right? over the
last few years, we've obviously seen a
huge resurgence of like graph databases.
And I've always like wondered even like
before AI like what the main utility of
it is, but it turns out that models and
AI is very very good at being able to to
grab context and be able to write
cipher, be able to write a query against
it and then traverse. Um, and the nature
of how data assets are, it's very
dependency based. So it yields really
nicely to be able to create these uh
typed objects and nodes and edges in
this graph.
Um.
Oh,
you guys can't see the slides. Oh,
>> can you guys turn off the lights? I
don't know.
No.
Oh, okay. Um,
oh that's better. Getting a little
better. We dim them a little bit more.
Sorry guys. I should have uh thought of
the the black background and other
colored. Um, but I can happy to send
this out afterwards also the deck.
Okay.
Um, apologies for that.
Um
so um yes let's see so you can see or
maybe you can't see I guess um but there
there's like a sample of like a subgraph
in here and you can and what you're is
actually represented is that the edges
carry a lot of provenence right so the
edges are defining different types of
relationships amongst the the data
assets themselves we have like for
example um uh is is materialized by has
a semantic definition and these are all
nodes that are representing different
types of data assets in the actual graph
itself. So there'll be like a node that
represents a semantic view for example
um and then there will be a node that
will present like a physical table which
is like the actual physical represent
representation of the logical code um of
the table itself. Um I'll send this to
you guys afterwards so you can take a
closer look at it or we'll figure out
how to get it to you guys. Um
and uh and so yeah and so this is like
essentially like what a subgraph will
look like. Um and so if we go back and
think about the use cases that are
relevant that the agent can now solve
because of this context layer that we
have um is is impact analysis is the
first one right so the agent proposes a
change um for modifying like a model's
grain for example right before it
actually does that before it writes a
line of SQL to make this change it can
actually walk downstream the graph and
ask each node that is a downstream
dependency of this node it's trying to
change does this actually break the
grain that you have represented in this
node here. So here it's able to catch
that um uh a monthly AR measure would
get repeated across weekly rows if I'm
trying to go from the monthly grain
change to the weekly grain change and
that downstream there's some ARR that's
actually summing all of the different um
values for this on a monthly basis which
would result in let's say the metric
having like a 4x um of the actual value
amount that it's actually accurate right
and then it could land on let's say
everything downstream on like a board
level dashboard that you have because
the context graph is inclusive of your
entire data system. Everything from like
source systems all the way down to the
BI layer in the dashboards layer. So the
agent has visibility and able to walk
the lineage all the way across the the
data life cycle if you will. So the key
part is this all happens pre-flight,
right? It's not at build time. It's not
in a production incident. It knows a
blast radius before it actually even
acts on it.
And then the second use case here is
join recommendations, right? So this is
fact two. Um so this is like the agent
wants to attribute the the exercise here
is like the agent wants to attribute a
arr by marketing channel right so it
doesn't pick a path because of like
column names that it's able to
understand it actually checks whether
each join key is actually unique and
this is done because we're profiling the
actual tables themselves um and it's
verified against the data right so then
it has the recommendation of what the
actual safe join path is to make this
happen while flagging the ones that will
actually cause like a fan out or like a
7x um in in rows or one that will
suddenly like silently drop 12% of the
rows downstream as well. So we're making
recommendations with actual reasoning
and evidence is the key here and it's
grounded in the data itself.
And then safe code changes, right? This
is the third fact. Oftentimes you'll
find like business definitions. The
reality is they're oftentimes nested in
the SQL itself, right? And so if you're
asking an agent to let's say tidy up
some measure or some metric that you
have and it removes a predicate um
syntactically that will work right the
the SQL will still compile um but what
it's actually happening and it it could
could look harmless but the predicate
was actually a very important part of
the business definition itself right so
here in this example it's dropping the
definition of um of paid right so it
it's silently redefining what the metric
uh the metric to include trial churn uh
across all the way downstream three
dashboards that are actually happening
representing this metric. Um so this
context layer actually catches this uh
change in business definitions and
business metrics before it's actually
implemented. Um and so this is like if
you're making the agent ser like have
these as like first class constraints.
It's not just a comment that is in some
YAML file or something like that. That's
the key here. And that's the line
between like a a syntactic refactor and
a change that a human can actually
trust.
So all good and great, but does it
actually work? Right? Um and so you have
to you have to measure this. Anytime
you're building anything agentic, you
need to be able to measure it. Um and so
we practice like eval driven
development, which is a very important
part of it. We're essentially going and
creating a bunch of like real production
data engineering use cases and tasks and
workflows that range in difficulty from
like easy to blind and they each run
multiple times and they're is they're
each running on isolated clones of the
actual data environment which is a very
important part so that there's no actual
leakage that happens across these
environments and then we have pass fail
that's running checking the actual
output of it. We have some LLM as judge
doing like impact analysis things as
well. Um, but the key findings here is
that although it's the same models, it's
the same task, the only variable that's
changing is where the agent has the
access to the data context layer. And so
you see a material lift um when it has
this right context. It's able to reason
across these really complex changes and
the task success rate goes up
tremendously. It's almost 35 points
higher when it's armed with the data
context layer. And this exact benchmark
is obviously going to keep growing and
keep evolving as we're working with more
teams to figure out their kind of um
bespoke use cases in there. Um but the
signal is consistent, right? The better
context um the more rich context you're
able to give the agent, the outcome
changes tremendously than just let's say
like swapping models or adding more
generic like tools, MCP tools um to to
the model itself.
So, I'll wrap up here, but before I wrap
up, the the five patterns, and I'll hand
it off to Brandon, obviously, but the
five patterns that are even if you're
not building this exact system, these
are some key takeaways that we've really
learned the hard way actually over the
last like year of us building this,
right? The first thing is like
deterministic always when you can,
right? Don't ever try and take like your
entire DBT project or your Airflow logic
and just throw it to the model to be
able to try and do these tough complex
tasks. That that won't work, right? Um
what you really want to do is be able to
get a really deep and detailed
understanding of the transformation
logic in a deterministic way. So parsing
it all the way down to the as to
understand the structure the
relationship the dependencies are very
very important. And then things like
being able to compute grain right like
that's something that you can use. We
spent a lot of time refining and like
using like relational algebra to
actually calculate and compute for each
stage of the data life cycle. Um and
then use the model when you need to when
it's like summarizing models or
summarizing the different data assets or
categorizing or classifying models are
really great for that. The second thing
is store evidence not conclusion. So
it's oftentimes good to just keep the
signals and then let the agent be able
to reason because these models are very
capable. They're very smart. They can
reason at query time effectively. And
then the third thing is that traversal
always beats prompt stuffing or context
stuffing, right? um it's going to want
to let it pull the subgraph that it
needs. Don't dump the entire repository
at runtime. It'll pull the subgraph and
be able to traverse to figure out how to
solve the task at hand because all the
dependencies and everything is clearly
mapped out there and the context when
naturally you'll have be running more
efficient AI because the context is
going to be a lot smaller every time um
the task is trying to be solved by these
agents. And then the fourth thing is
like own the tool surface. So like what
we found is a curated a curated type
tool set always beats like a buffet of
just like off-the-shelf MCPS. Um even
like for the MCPS that we do have that
give our agent access to Snowflake MCP
or data bricks MP we found ourselves
like rewriting a lot of it to kind of
match the capabilities and functionality
of what we're trying to accomplish. Um
and then um let's say the fifth thing is
we talked about like eval right this is
uh the most important thing you can't
really build a reliable agent regardless
of what the agent is doing if you can't
measure it you can't learn from anything
you can't measure um and so invest in
like the eval infrastructure early and
often and it's a continuous like living
breathing uh piece of your software that
you have to always maintain and up and
and update um and run continuously.
So to close uh this portion of the
workshop, this hasn't been a real
workshop so far. It's just me kind of
rambling, but we'll get to the fun part
now. Um what we found is the agents
don't really fail at data engineering or
data task because they can't read or
write SQL. They do that. They do a very
good job of that. They fail because they
don't have or they don't understand what
the data actually means, how it flows,
or what breaks when it changes. Right?
So if you make that that context really
a first class citizen um you extract it,
you compute it, you persist it, and then
the agent's able to query it in a really
efficient way because you have a graph.
Uh then you're able to cross a line
between from an agent that only reads
your code to one that's actually ready
to like operate your data system. And
that's like what we've built with this
like data context layer.
All right. Um so thank you for that like
little brief talk um that we've given
here. I want to hand it over to Brandon
who's actually going to like start
walking you guys through more of like a
hands-on workshop that carries over some
of the concepts we talked about in here.
Um, I won't take any questions out
because I want to make sure that we have
enough time for Brandon to go through
his entire workshop, but I'll be around
like after this and whenever like feel
free to reach out to me. I'm happy to
chat more about this. Thank you.
[applause]
Good job.
Okie dokie.
How is everybody doing today? You're
doing good.
Fantastic.
Sorry, give me one moment.
All righty. So, the topic that I'm going
to talk about today um is uh definitely
related to what Yonyi was talking about.
We're going to try to bring these
concepts together in a form that we can
actually do in uh the rest of our time
here. Um so, my name is Brandon. I'm at
Typed. Um, and you're going to hear a
lot of talks here at the conference this
week about how agent is only as good as
the context you give it and that
building that context is in fact the
actual job. And so this is basically a
hands-on version of that exact same
lesson. Um, over the next 90 minutes,
we're going to build a context layer for
a coding agent together, a real one over
a real example codebase. We're going to
be using the quadrant codebase today.
Um, and then I'm going to show you uh
the last part, which is that even if you
build when you build these amazing
tools, um the agent's mostly going to
ignore it unless you help it along the
way. Um, getting it to actually use the
tool is going to be uh where the work
really is. Um, so
before we go ahead and dive in, um, if
you want to go ahead and follow along,
this QR code links to my GitHub
repository, which does have all of the
relevant code. Um, that repository has a
few Jupyter notebooks for people to
follow along with. Again, don't worry if
you don't want to have set that set
everything up. The dependencies there
are uh docker compose or docker for
running neo4j. Um and if you do want to
try out the llm portions of it live, you
can use an open router key. However,
that's not required. It'll all run
offline if you desire or you can just
follow along with me uh as I build it up
here. Um
so, uh I'm going to leave this up for
just a little bit longer and then I'm
going to start doing a little bit of
talking for people to be able to set
things up if they want to and then we'll
dive into the notebooks themselves.
Okay, everyone got the scan in. Ready to
go?
Give it one more minute.
All right,
perfect. So, let's start where every
coding agent starts, which is text
search. Um, I'm going to ask about this
type for this strct called posting list.
Uh, it's a real type in quadrant. Um, so
when the agent goes, it runs rip grip.
Um, and you see great, it found that we
have these two different um, answers
that are exact matches. They're both
exactly posting list. Well, we see it
has a dozen more look alikes. You know,
we have a posting list view, a posting
list iterator, etc., etc. Your agent's
going to do the same thing. It's going
to GP. It's going to get this wall back
and it's going to pick one, right? It
may pick the right one. It may pick the
wrong one. It's going to explore that
one first. Maybe it has to go back,
backtrack, read the next one to actually
figure out what you want, right? But it
doesn't really have any means of knowing
which posting list you want, right? It
it it can't the text itself doesn't have
any concept of identity or you know
which posting list is actually you know
meaningful. Um this the the things you
care about you know what methods use it
where it's used what crate that it's in
that's not necessarily just in the text
it's in the actual structure of the code
itself. Um, so we just watched Yonyi
make this, you know, a very similar case
for data. And it's it's problematic to
have the the agent redive the entire
system for every run with no memory. Um,
because for one thing, it's going to be
expensive, right? It's going to go
through it's going to have to reread the
same set of files every time. If you ask
it the same question five times, it's
going to go back and read all those same
files every time, right? But the
important thing is that it's fragile,
right? when it goes back and it reads
those five files, it might read them in
a different order next time or it might
read one file first that gives it the
wrong answer and sends on a goose chase
to another file. Right? So, it's that
issue of actually having this thing be
deterministic and not as fragile uh that
we're really trying to accomplish when
we're trying to engineer context for
these kinds of agents, right? The goal
isn't necessarily to get the agent to be
a lot more correct or a lot more
efficient, even though that's sometimes
the case. The real goal is to have it be
a lot more deterministic, right? because
we're trying to apply as much
determinism as we can to this very
non-deterministic system. Um without you
know this persistent trustworthy model
of the code, it's going to guess um
every time. And you know what we see is
that over time the models have been
getting better and better and better at
guessing, right? You know, we can all
see what happened when we ran cloud code
a year ago versus running it now, right?
It's completely different experience. So
like if we want to build a context layer
for code, we basically want to follow
this exact same recipe um but um just at
a slightly different uh level, we're
going to scale this down so that we can
build a workshop and you can leave it
something that you can actually run
today um instead of trying to replicate
all of our uh our entire product up
here. So we're basically going to take
um that that concept this exact this
extract persist and query um to
basically go ahead and start extracting
information out of our codebase. So
we're going to pull out information
about the symbols you know every every
type every trait every function uh with
its real identity and location. Um we're
going to the relationships between these
different symbols get uh edges inside of
our graph that we can traverse. These
get computed once and they end up being
uh queried many times. This is the same
uh overall approach as what we do when
we're tackling a sprawling data
architecture just with a small enough
example to run in this room. Um and so
yeah, that's basically what I was just
saying. Uh so we're going to send it up
today. So uh this is going to be a
concept that you're going to hear about
a lot during the conference. Um I
thought it was I thought it was really
cool. I I brought up I made the slide of
three levels of context and look at the
schedule and someone has a talk about
four levels of context tomorrow. So I
feel a bit preemptively oneuped but
we're still going to go through this
today because I think it's still uh
pretty useful for this context here. Um
so you can think about context of a
coding agent in sort of this terms of
levels. Uh that's how I like to think
about it. So level one is sort of what
you just saw. It's the GP, it's the glob
raw strings, no structure, right? Level
two is where you get, you know, most of
the code rag solutions that we have
today, right? you get um semantic
search, you index the code, you embed
it, right? You do some nice lexical
search, semantic search, you get ranked
results, right, of all the, you know,
the locations that this this thing was
mentioned in. But at the end of the day,
that's still going to be a flat list,
right? It's going to be a flat list that
gives you more relevant results. It's
going to be still a flat list. It's not
going to show you the relationships
between these different code, right? So
the the top level or or the highest
level at level three is in our opinion a
traversible graph. Um something that
links the symbols with real identity and
adds typed edges between them that you
can actually traverse. Um so I think for
the next part of this workshop we're
going to go through and build up through
these different levels and by the end
we'll get to an agent that can answer
questions about the codebase um using
this traversible graph. Um,
and uh, yeah, let's uh, let's let's lay
it out. So, as we're building this,
there's going to be a few different uh,
stepping stones or rungs to get to that
level three understanding of how we do
things. So, rung zero is sort of the
syntactic level. First, you need to
actually parse the code that you're
actually trying to trying to understand.
And so, the easiest way to do that is
with something that's language agnostic
like treesitter. And that gets you a
very basic high-level ASD breakdown of
the different um parts of your codebase
and how things interact. Um, however,
that still doesn't really have any idea
how to deal with collisions, right?
Posting list, the symbol that's in
posting list.rs and the posting list,
the symbol that's in, you know, quant.rs
are two different posting lists. They're
still going to collide at rung zero. So,
the name of the game is going to be rung
one. So resolution is the one thing that
GP can't really do, right? It's the
thing that turns those two ambiguous
posting lists into two distinct
identifiable types, right? So with Rust,
it's a little bit cheating. You kind of
get wrong one for free because Rust
compiler will do a lot of this work for
you. And uh you know, we'll basically be
using Rust do.json to give us all that
information basically out of the box.
Now, is this cheating? Yes. Um I picked
rest on purpose because I needed to
build this workshop and you know
building an entire parser for a whole
other language or trying to build
something out is a little bit harder.
However, at the end I will talk about a
more useful case of this on Python and
there's an example notebook in the repo
for you guys to peruse on that if we
don't get to it uh during this workshop
today.
Um the next layer uh that we're there is
a there is a notebook for I'm not sure
we'll get to today is rung two which is
the actual meaning behind um these
different things that we're extracting.
Right? So these first two layers are
solely deterministic. We're basically
always trying to be ground our
understanding in as deterministic a base
approach as possible. So we build out
these first two layers using tree sitter
and rest.json JSON and then if we have
some time we'll explore um how we build
out that rung two layer like how do we
take that information feed it into an
LLM to classify and summarize and do the
things that the LLM are good at as
opposed to just trying to throw
everything in there and asking it to
make sense of it.
Um fantastic. So, now we're going to go
ahead and open up our uh notebook 01
and
going to be
confused.
Bring this over here. Oh, actually
it's already here.
Okay.
All right. Can folks see this? Okay. Or
did I bring them up on your side? Great.
So
this uh this notebook, what this
notebook is going to do is it's just
going to walk through the process of
building up those uh those levels of
different context for our uh our
quadrant project. We're not going to be
indexing the entire codebase today. It's
a little bit big. Um we're taking a look
at uh a sampling of I think five crates.
Um it gives us a good corpus of code to
look over uh for our testing here. Um,
so we can start going ahead and running
these cells. And so what we do first, we
just do a bunch of setup. Um, and now
that the
setup is good, um, we can go ahead and
start looking at the, um, yes.
Ah,
it is in the GitHub. Yes, I can put up
the link again to that
real quick.
bring that up.
Um, so the link is up here.
Uh, if you don't want to follow on
locally, there are collab links in each
of the different um, things there. Yes.
Uh, for the collab for the notebook one,
if you do want to use the graph, you
will need a Neo4j or a login. Okay,
that's just a that's just a special
thing for that.
Okie dokie. So, we can see here um
there's a bunch of additional code in
here to actually do all of the um
parsing inside of uh Rust itself. I'm
not going to necessarily go over that
today, but it's all available in the
repo for you at your leisure. Um we just
have a magical function here today uh
extract rust gate that will uh pull out
the information from running trees
sitter across the rust codebase. Uh and
then another one that will go ahead and
do the same thing but for our
information from uh rest dock. So we can
see here that from the first couple of
crates we've pulled out um a bunch of
symbols from freesitter and then a bunch
of symbols uh resolved versions of those
symbols from Rustto do.
So now we can go ahead and start running
some code that's going to start trying
to understand why we're differentiating
between rung one and rung zero. So we
can see when we ask about something like
posting list in rung zero we see that
okay we see this exported version of
posting list we don't know actually
where that originates from though we
can't resolve that backward into the
actual um location where it was defined.
Um, so that's what rung one is for,
right? It's going to be able to say this
is posting list. This canonical location
is here at posting list posting list
posting list and that actual location is
at this path at this line, right? So
this is what's going to be able to let
us figure out when things get reexported
outside of a crate, link it back to the
original crate. The agent's going to be
able to traverse all the relationships
between those different things um once
we actually build out the graph itself.
Um so now we'll just build very quickly
the level two that I was talking about
before. Um where we have a kind of index
where we build a uh very you know where
we basically take all the symbols and
then we let um a function go that just
does a full text search. Right? So we do
a search and we get the same problem
that we saw in grap. Right? We can
search for posting list and we can get
very useful information. We can see this
is the reexport. This is the strruct.
This is the strruct. But it's still not
going to tell us the linkages between
those different things, right? And the
agent can infer that and it can, you
know, make the make the figure out, oh,
probably that if the posting list
posting list is a strruct, it's probably
reexported up here. So that's probably
the basis of it. But you don't want it
to have to make that logical leap every
single time because it's going to be
that one time where it gets it wrong and
then it's going to end up on a
completely different wild gase.
So our next step here, we build out the
we start building out the actual graph
um itself. So we take that all those
different um uh symbols and uh
information that we just extracted, we
transform that into a bunch of nodes and
edges that we can populate into our
Neo4j graph. Um and then we go ahead and
actually um load all of that in. So once
that's in the graph, right, we can even
go into Neo4j. Um we can see we have you
know a beautiful little graph of u
references to all the different parts of
our uh of our of our codebase here. Um
so now that we have this sort of graph,
we can build tools that specifically
harness the capabilities of the graph to
give our agent access to something
that's going to make it easier for it to
do its job. So if we build a tool and we
want to say okay I want to look at a
function and I want to see what's going
to change what's going to break if I
change this function right so we can
build this function blast radius where
we say okay you pass in the qualified
name of something the canonical name
it's going to go in and it's going to
try to figure out walk down the graph
through those different edges that we
defined try to figure out exactly um
what depends on this thing what will
break if this thing gets changed right
and so in that sense you can ask the
agent to answer a question that would
have taken multiple grapes across
multiple different files and in theory
um the agent can just answer it in one
in one go. So of course that didn't work
because why would it why would it work
live demos everybody?
Okay, so you can see here when we say
we're going to pass the blast radius to
this strruct, we can say, okay, cool.
It's linked here via it gets returned by
this um there's a method that does this
um it gets returned here. So we can see
all the linkages that we're able to
establish um just by having the content
inside of the graph.
So finally um we get to resolve our
collision problem. Um now if we say we
have two different posting lists and we
want to see the difference between them
um we can call our new tools blast
radius for this posting list and this
posting list and we get a different set
of results. Changing one posting list is
not going to in fact the same level of
changes if you impact change the other
posting list. So even though these
things have the same underlying name,
the actual canonical resolution of them
results in us being able to more
definitively say what's going to change
when you break this thing more than just
going a grap reading all the files and
then trying to guess. Um so now we can
actually take what we built so far and
build a very small limited function
agent to actually use this new tooling.
Um now that we have uh this blast radius
tool um we can wire up a very quick
little agent. Um this agent is very
simple. It's just a pyantic agent um
that uh is just configured with a system
prompt that says you have the ability to
uh run these different tools and we
wrote some very basic tools for it to be
able to use blast radius the
implementers methods of um that work
with very basic cipher queries in order
to get the information out. So once you
have this information in the graph,
writing the queries to actually pull it
out becomes quite simple. Um if you can
express the idea that you want to uh do
then it's pretty easy to write cipher or
the equivalent language in whatever
graph you're using um to actually pull
that data out. And that's a sign that
you have created the right schema for
the job.
So now if you go ahead and run this
agent, this agent will actually spend a
few turns um calling the tools and
trying to figure things out. Uh and then
it will go ahead and uh try to answer
our question. So for now if we can say
what breaks if I change posting list
tell me each dependent symbol with its
file line and then it will tell me
exactly uh what will break um based on
the blast radius finding and we can see
here what tools it called. It started
with search did a couple of searches
before calling the blast radius uh and
then doing another blast radius call. So
we can see that if you have an agent
that is uh skilled enough in tool usage
um it can use these new tools to uh
build out its understanding uh of the
codebase. Now this part is a uh more of
an interactive section where you can
build whatever tool that you would like.
Um, how this basically works is we can
write a tool that basically executes
arbitrary arbitrary cipher. Um, so here
we're wr writing some cipher that says
find me all of the um symbols within
this file path um and then just lay them
out. So this tool will do just that. It
will find all of the symbols in this
file path and lay them out for me.
Um,
yes. So then if I wanted to write a new
tool, I wouldn't even necessarily have
to know cipher, right? Um I could give
the agent access to a system prompt that
has a schema in it, right? That tells
the agent, okay, these are the different
nodes, these are the different edges.
And I can write um I can write my um my
requests in natural language like I want
to see uh every strct that implements a
trait along with the trait that it
implements, right? And if I run um if I
run that uh it'll take a second because
the agent's going to actually try to
figure it out. And it does. It actually
generates this cipher query that it can
run and it can go ahead and pull that
information um out of the uh out of the
graph. Um we're not going to get to uh
rung two today, but we can get a little
taste of rung two. So so far everything
has been very deterministic. Um you get
your structure and you get your
resolution. Um that third rung I was
talking about was the actual semantic
meaning. um you can actually have an LLM
summarize these symbols and uh embed
them. And uh typed defaf actually has an
open source library for this called
fenic. It's a dataf frame library for u
marrying traditional dataf frame
operations and LLMs. Um so here we're
just doing a quick configuration of
fenick where we say we're going to have
it talk to open router. Um we're going
to pull in some information. We're going
to say uh we're going to try to classify
this specific rust where we're going to
pull in the kind and the qualified name
and the dock string and then we're going
to ask in one concise sentence what is
this rust item for and so when we run
fenic over this over this corpus over
these rows we get back um the summarized
outputs from the LLM. So in the long
run, right, the idea would be to bake
this information up into your graph so
that this information is also available
um for the agent. And the nice thing
about this is that this is auditable
when you generate it. So if you're
looking at this and you say, "Hey, this
explanation of what this function does
is wrong, we can go ahead and actually
get that fixed." If the agent on the fly
figures out what that function does and
it's wrong, you're not going to know
that it's wrong until much later down
the line when it writes code that
doesn't work.
Um, awesome.
Yeah, sure. Um, that was uh notebook
one. We have a little bit more stuff to
talk about, but I'm happy to take any
questions about the content that was
there and I'll put it back up real
quick.
Yeah, I see two in the back. will come
back with a with a microphone
>> testing.
>> Yeah. Is the is the graph reestablished
at runtime when whenever you're uh
building these a
uh traversing them?
>> Define runtime. runtime as in uh when
the PR or CI/CD comes through or
>> yeah in an ideal world I mean we don't
build this product for a living but like
in an ideal world that would be uh
cached and saved in the a canonical form
as like say the gold version based on
main for example right um and then as
you tweak stuff and modify things
locally you need to probably maintain a
local copy of that that would ideally be
incrementally refreshed so you wouldn't
have to do it all up front
>> yeah I
My question is similar.
How do you
uh think about the cost of keeping
these structures up to date versus
you know whatever the increase in
performance and fidelity um because at
least for me you know I'm using AI to
make
uh large changes. So
>> um so it's hard for me to know um
offhand you know whether it would really
be better if you have to maintain these
structures.
>> Yeah, absolutely. I think I think the
key to that is [snorts] um a lot of
these problems can be boiled down and
incrementalized because a lot of the
things that you're doing is you you
don't necessarily have to reindex the
things that you've already indexed if
they're not changing, right? And when
you're making broad sweeping changes
across your codebase, like you are
changing a lot of files, but there also
are a lot of files you're not changing,
right? So if we can be smart about
incremental reindexing, making sure
we're only keeping track of what's
changed, only reindexing that part, then
what we've seen so far is that the
trade-off is in fact worth it.
Especially as the context size of what
you need to keep indexed grows, it
actually becomes more useful because the
cost of doing it live every time just
becomes even more expensive.
Um, thank you very much. That was super
useful. Um, I I'm I'm wondering how it
works on kind of like a real code base
in a in a messy language where uh for
example you have dynamic dispatch or
like not not all types are available at
you know at compile time or before sorry
when you just analyze code. So have you
tried like what are the limitations any
any any tips there?
>> Yes. Um we I do have a third notebook
here which is talking about that in
particular. Um which is basically how
you do this thing on a language like
Python which doesn't have the same uh uh
easy access to the types as graph as as
rust. Um we use we can use other
tooling. We can use tools like griff and
same type sitter. Uh types will still
give you a and griff will give you
static resolution of some of the other
stuff like the types. You can use
something like tai uh to do type
checking as well um to gain more index
there. Yes, it does become exponentially
harder with different languages. Um, so
the and I will talk about that a little
bit later on. Um, but yes, the answer to
your question is yes, I did think about
it. It is a much harder problem which is
why I chose to solve a slightly easier
problem today.
Yeah.
I don't think you should be building
this to be clear. [laughter] This this
is this is a this is a worked example
for educational purposes. um people
build these kind of coding uh graph
things like on the reg on the regular
and I wouldn't try to build one from
scratch um just for doing code analysis.
Uh I don't know if that answers your
your question and I think they are worth
it to build. I don't know if it's worth
it for everyone to build their own. I
think there is probably a and there are
a bunch of folks in this game already
that are are doing this sort of you know
analysis just on the code layer. Um, so
I I would say it's probably not worth it
for a single person to build if for the
purpose of being a product. It is
probably worth it for someone to build
for the purpose of learning about how to
build an agent and how to build tooling
and how to build context graphs. Um, I
think the scale of this problem is like
where it that's where it's more useful.
That answer your question?
>> Awesome.
>> So uh my question is about the data
context layer uh that you talked about
earlier. Uh so uh I'm assuming that
that's useful in a for a like a
developer. So you develop this this
context layer and it helps uh produce uh
better SQL procedures whatnot. Um so uh
two questions number one um does it have
you seen if it helps at runtime as well?
Uh like inference time uh that's number
one. And number two, um do you have any
benchmark results to demonstrate?
>> Yeah, absolutely. So what Yonyi was
talking about in his talk, um we do have
benchmark results for that. Um what we
do is we've uh we've tried to find a
representative data architectures which
is kind of hard because you can build an
easy tour example like in your in your
in your and say oh my agent aces 100% of
my tests on my 30 model corpus and it's
like okay that's not very impressive.
Um, so what we tried to do is find uh
open source examples of data
architecture that was larger. Um, so we
ended up settling on using uh I don't
know if anyone's heard of Mattermost.
They're a instant response and chat
company. Um, they actually open source
their entire DBT project with like
several 300 350 models in it. Um, so
we're actually able to pull that down,
simulate data in there, and then run
evaluations against specified scenarios
inside of that. Um, asking it to do a
specific task, break something in there,
and then ask it to fix it. ask it uh
build out a set of you know new tasks
for it to build new things. And we're
able to see that uh by building out our
evaluation layer and layering out you
know evaluations of how correct it is,
how complete it is, um how efficient it
is, right? We are able to see that uh
with the appropriate context our agents
are able to do a better job uh overall
and in certain particular categories uh
to uh like accomplish those same tasks
better than just cloud code running
alone. Um
>> and what about the earlier question or
the other question about inference time?
>> So uh it does so you're talking about
like when the agent is actually running.
Yes, when the agent is actually running
>> that that that's when we find the most
use out of it because when the agent is
running, it's going to be querying all
of the tools that we built and that's
where the real value is coming into
play, right? If the agent's able to
query all this stuff at runtime, it
doesn't have to rederive it all at one
time, right?
>> So, um, so then have you tried this with
like NL2SQL benchmarks like Bird or
Spider or one of those?
>> Yeah. So, I mean, yes. And no like yes
we have tried it on some of those
benchmarks. I think the the tricky bit
is that like the goal of the product
isn't necessarily to write analytical
SQL. The goal of what we're trying to
build for people is more on the data
engineering side. So it's
I think you know it's it's sort of a
very common thing to say oh we're going
to build text to SQL and we're going to
build that. I think everyone's trying to
build that, right? But it's I think it's
more important to say we want to build
the tools that are going to make it
possible for you to actually trust text
to SQL, not necessarily that we're going
to be able to, you know, come in and
write better analytics queries for you.
Like we want to make sure that when you
are actually going in and doing your
day-to-day work of maintaining your data
architecture that we're going to be able
to help you with that. Did that answer
your question?
All righty.
So, popping back into if I can find my
mouse.
Popping back into the slides.
So
what we saw there at the end, right, is
that when we
uh we can actually go ahead and tell
these different posting lists apart. Um
because we're able to uh query our new
graph context. Um and we're able to
actually figure out all the dependencies
of a given symbol with one hop uh
without any regrabing. Um and so how the
query works you know it matches on the
qualifi the fully qualified name and
then it goes and finds all the
dependencies and
that's it guys great workshop we're done
for the No. So the thing is like this is
cool. This is real. This tool is really
great right? This tool can do in one
call what it would certainly take
multiple graphs to do. I don't think you
could accomplish this in one grab even
if you did the perfect grab, right? But
uh the problem is the agent
you have to actually go and give it to
an agent. So when you give this agent
this tool and you give it this agent
this tool and you give it alongside all
the existing tools the agent already has
and you know we have this really cool
tool, we've seen it do this amazing
stuff and it ran GP anyway. Um, if you
give it access to the graph tools and
GP, it's going to run GP anyway. And we
gave it amazing tools, a precomputed
traversible model of the codebase, and
it just ran grip anyway. It just globbed
and read files and and ran grip and it
would sometimes, you know, poke the
graph and get confused and then get back
to, you know, waiting through the graph
stuff. And this is where no one really
tells you. Everyone's like, "Oh, he
built these cool sexy tools and they do
this amazing stuff." But the agent has
to actually use them, right? you have to
do the prompt engineering and the rest
of the hard work and the evaluations.
That's the rest that's the hard part,
right? You can build that notebook. You
can build the your amazing graph context
in an afternoon. The hard part is
actually making the agent use it. Um
like the uh yes. Um and why does it do
this? Well, it's because of the post-
training. The models are trained and
designed to call these tools, right?
There are so many circumstances in their
training where the answer is to GP and
read, right? And you're not going to be
able to necessarily fight that um just
by making a better tool. You can make a
better tool, but the agent's muscle
memory isn't going to let it use it.
It's very similar to humans, right? You
can build humans a better tool and if
you try to force them to use it, you're
going to get they're going to not be
happy about it. This may be a little bit
topical. I don't know. Um, but so the
the important thing is that like you're
not necessarily competing on the merits
of your tool being better than all the
tools inside of the toolb tool set of
the agent, right? You're trying to fight
against its own reflexes. So how do you
actually do that, right? Because I don't
think there's a question anymore that
yes, if it could query the graph, it
would be more efficient and better.
We'll prove that later, but how do we
actually get it to do that? And the
answer is to not really fight the the
prior experience of the model, but to
kind of lean into it, right? We we make
the graph feel more like the model is
using grab, right? You know, you you you
take this you take a a tool that maybe
called query search or query graph or
query whatever and you just call it
search, right? The agent will use it in
a certain kind of way. What I found is
that if you call a tool search, the
agent will basically always do multi
keyword search into it with no training.
So you have to you have to kind of meet
the model halfway, right? You take the
model, you name it search, you account
for it to adjust for how the model is
going to query it and then you just, you
know, you get back the results from the
graph and you return the results from
the graph in the same form as rip grab,
right? You take the same tool structure
and response as rip grip and you return
it back to the model, right? Because
that's what the model's been trained on.
It knows how to handle this stuff and
you're not going to get it to completely
change its own self um just by
prompting, right? And the last thing is
that you need to have uh your tools pay
off in the first call uh every time
because when something when the agent
goes down a path and it finds a a dead
end or something that it thinks is a
dead end. It called search didn't get
any results. Well, sometimes it's going
to think search is broken. If I'm
getting no results and like I there
should be results, maybe search is
broken. I should try another tool,
right? It's not going to go back and use
that tool again. And if it does, maybe
it tries to use a different way. you
can't really necessarily predict that,
right? So, you have to do your best to
make sure that your tools are returning
something that's super useful uh right
away. Otherwise, they're just going to
go back to GP and they are uh never
going to come back. So, the second
notebook is uh shorter. Um it's a little
bit of a more
focused example and this is all about
evals, right? How do you actually show
that the agent is doing what you think
it is supposed to be doing, right? And
how do you actually um prove that your
tool is better than the existing tooling
that may already exist, right? So um all
of this stuff is already pre-cached. I
did this run. If you do want to run the
notebook locally, you can absolutely set
sample size to um something greater than
zero and run the eval live. It will take
a long time. Don't say I didn't warn
you. Um but um I did run this overnight
with uh five retries and uh 30 questions
in my email set. So that's where these
results are coming from for this uh for
this notebook. So
the first thing that we do um after we
do this setup is um we basically
uh set up our our test cases, right? So
we're going to have an agent with um our
new graph tools. So we're going to give
the agent access to the same model and
our graph tools. We're going to have our
control agent that's going to have
access to the same model and a set of
file system probing tools that's
maintained by paid by dantic. Um so uh
that's going to be our two test agents
and then we're going to build up a
corpus of questions. Um each question is
a real task. We're going to figure out
okay questions like what public types
break if I change posting list? There
are two posting lists. What do I use?
You know this kinds of thing. um where
we try to you know say okay this this
should be a question that should be
really good for the graph this is a
question that's probably great for for
for GP um you know there's a control
questions that are probably be good for
both right so the gold data for this is
actually we do pull the mind data from
the graph we do cross reference it back
to the source code so it's not that
we're polluting the context of the gold
with the output of the graph we do have
to cross reference it to make sure that
the gold isn't cheating um so now we can
go ahead and load up our uh our gold and
we can basically start trying to set up
the actual evaluation structure itself.
Um and so this is what lays out what's
basically a good eval question versus a
poor eval question. Um you want an eval
question that can be in an ideal world
your eval should be able to be
deterministically scored. I think LM is
judge is really fantastic for a lot of
use cases but it tends to be overused
when you really should be trying as hard
as possible to have your scoring be as
deterministic as possible. It's going to
reduce variance in your runs and it's
going to reduce cost in your runs and
it's going to make you happier in the
long term. Um, so you want to create
questions where the answers are pullable
from the you you're able to structure an
answer to them that's gold that works.
You're able to check the answer against
the gold. Um, you're not just asking the
agent to provide its opinion and then
asking another agent to counterman that
opinion with its opinion. Those
questions don't really tend to ever work
out as emails. Um,
all right. So, this is this is some
craft text. You don't need to worry
about this too much. This is just
basically building out the um the the
test cases that I was saying. This is
the deterministic part where we check to
see if it cites all the evidence that we
expect it to site. Um, we're basically
just creating a list of examples,
creating a list of uh uh things it
should be citing, and then checking to
see if it's citing all of them. For the
eval themselves, we're using a
configuration in Fidantic Evals just
because it's really easy to set up. Um,
how this works is we build out uh our
two different agents and then we build
out um the agent runner itself and then
we build out an evaluator, right? So,
this is what actually will evaluate the
agent based on um the given tasks that
we have in front of it. We'll basically
compare what the agent has said to uh
what we expect it to for each given
task, right? And that way we're able to
compare the responses and the results
between our prep agent and our graph
agent. Right? So that's how we're able
to establish um one you know what is the
actual utility of our skills and two um
how do we uh what what can we improve or
or what can we do better as time goes
on. So um go ahead and run.
Right. So I'm not going to go ahead and
run the eval again because that would
take about 30 minutes. But um we can see
that we run the eval the first time and
we run it with uh k equals 1. So we just
say for every task in our data set
onehot graph agent graph agent and we do
that the graph agent doesn't do very
well. You can see that the the graph
agent it does edge out the the graph
agent a little bit but it's not really
consistent and it's not really like very
it's not what we wanted, right? But what
we have to understand is that the goal
wasn't ever necessarily to build
something that's going to be more
correct than Grap. The goal because all
of us that use Grap on a day-to-day
basis when we use our coding agents know
that it's very good at what it does.
Like it uses GP for a reason. It's not
going to be wrong a lot of the time,
right? But the important part is not
that it's right the this one time I
tried it, but that when I try it 10,
five, 10, 15, 20 times in a row that it
gets it right every time, right? So
that's how we need to actually start
sampling these tests. Now when we say we
run these same set of tests over the
same corpus five times to get our our
pass at K metrics. Now we get a slightly
different um answer. Right? So we have
two different statistics. Our pass at K
and our pass hat K. Our pass at K says
across these five runs was this ever
correct? Right? In that case they're
still they're very similar. Actually
graph has a little bit of an edge there.
Um the graph doesn't sample any of the
private variables only the the private
part of the crates only the public. So
there's some control questions that the
graph will always do better on. Um but
what's really interesting is when you
change the metric and say is it doing
the right job on every run and when you
do that the numbers completely flip
right now all of a sudden the graph
agent is twice as good at doing the
correct thing all five runs than the
than the graph agent. Right? Um, and we
can see that within that ad that's doing
that stuff and it's doing it more
consistently, it's also doing it more
efficiently, right? We can see that over
the course of all our different runs, on
average, the graph approach took about
three and a 3.1 times fewer tokens. The
last part is, okay, how do we actually
get the agent to use the graph? This is
where your evals come into place because
you basically have to write an eval that
says, hey, examine all the tools in my
trace. How often is my agent using the
tools that I want it to be using? And
then you can get your sort of adoption
numbers, right? So that's how you can
get to a place where you can say, "Oh, I
wrote a prompt that didn't have any
instructions in it to use the tools. I
got 34% of tool usage. I went back. I
changed my prompt. Now I have 72% tool
usage." Right? So the eval are the only
way that you're going to be able to
actually understand that the agent is
using the tools that you want it to use.
Um, this is just a test of that exact
concept. we have uh two different
prompts that are both trying to answer
the same question with the same tool
set. Um if you if you nudge the prompt
uh if you just naive it will just go
ahead and grap um and then we'll start
doing some other stuff. If you nudge it
the ideal world is that it will go and
actually run the search and use get
symbol to go and figure out the actual
answer. [snorts]
And so the recipe for building, you
know, really solid, honest evales is to
mine real task candidates out of your
corpus. Uh build a deterministic as much
as you can, an anchored scoreer. Uh and
unit test the scorer itself first. Um I
like pantic eval. There's many many
other eval things out there, but the
core structure of them is all going to
be the same. You have a data set, you
have cases, you have an evaluator. Um,
make sure you run your evals many times
over and reports pass at K, pass at K,
uh, and all your different metrics. And,
uh, make sure that you are,
um,
putting in examples of things that your
agent may not necessarily be good at
because you don't want it to pass 100%.
It's not a useful if your e if your
agent's passing your email 100%. Your
email is too easy. Your agent should be
close to failing your emails. um like
your emails are your chance to see where
the metal hits the road and what your
agent's going to do in as hard as
possible circumstances. So it doesn't
really do a good anyone any service by
just uh giving it very easy and very
simple evals.
All right, anyone have any questions on
this eval notebook before I jump back
into the slides for the last part of the
talk here?
Uh I I was just wondering in the example
when or when you were discussing how you
the agent would often use GP instead of
graph. So you had to retool it to be
this search tool. Uh was there ever any
uh uh like attempt to take the graph and
distill it into a file structure maybe
like with some loss but a file structure
that then GP would naturally search over
so you didn't have to define any
separate tool at all.
>> Yeah. Not today. um just because
uh there was a bit of a time crunch but
I think that's definitely a reasonable
approach. I mean I think that's what you
know that's corporate llm wiki you know
with all these different things where
like you can get a lot of these
different benefits just from the
markdown corpus but like I and I think
that that's that's definitely true and I
think that you would still get a lot of
the same like benefit out of it but I
don't like in the markdown like the ele
wiki that kind of stuff right I still
think that that your problem is going to
be like you want real like edges and
provenence between them right and like
those connection connections are where
it's going to be really hard because
even when you do something like Grain or
something like that, right? It yeah, it
builds all the stuff in markdown, but it
does build a graph on top of it for you
to see the timeline and the connections
and stuff, right? So, I think at some
level, you know, if your task is based
in needing to understand the
relationship between these different
things, then at some level you're you
will want some kind of graph. Even
though I do think that you can get a
very similar level of of of of success
out of out of an approach like that.
Yeah.
Um, do you think there's anything
missing from a setup like this for
letting non-technical, non-data engineer
folks like kick off a PR with this as
like the guide through a codebase? Have
you tried that or like is there a
something you'd add before you empower
people to do it that way?
>> Oh, like for this as a as a tool?
>> Yeah.
>> Oh, yeah. I think um
that's a good question. Yes. I I think
the
the the easiest part I mean would
probably be like starting to hook it in
as an MCP to the tools that you're
already using. So you would have you
know this code graph in addition to your
your cloud code and you would ask your
cloud code to call the graph and do
those other things and then you would
write skills in order for it to actually
use that that that properly. I think
that would be the the best approach
there. Um, but I would think that yeah,
if you're less technical or
non-technical, I I would think that, you
know, the the the goal would be that you
would if you want to engineer the agent
to be using these things in the context
of actual coding, you would promote
these prompt engineering things I'm
talking about here into skills and give
those to your coding agent.
>> Yeah. Like that PR lands at the engineer
for the first time with like a halfdeent
first pass as a result of being more
deterministically guided by this.
>> Yes. Yeah. And and I think that the the
deterministic part is helpful because
you can like like we were talking about
before with for the question in the back
like you can incrementally just diff
over what's changed, right? Analyze that
deterministically and get a really
really fast conclusion back about what's
what's happening and what's been
changing since the last time as opposed
to waiting for the agent to go and read
everything and look at all the changes
and and give you back that that same
diff.
>> That's one back there. I think
>> um did you uh experiment or think
through like different uh levels of
resolution like one thing I was thinking
of um in some of the earlier talks is
like you do next token prediction and
you will have the prefix I think people
said which is just like
>> you know it's all at the level of like
this is the whole string of everything
in the codebase here you have the
symbols but like the symbols is a
certain granularity,
there would be higher levels of
granularity that are imminent in the
codebase and making those things
searchable and accessible to an agent,
you know, might have payoffs and I was
wondering if you thought about that or
if you have thoughts on how you'd
approach that.
>> It's a fantastic question. I did think
about this. There are uh and I will
actually talk about it at the end of the
at the end of the the presentation. Um
there was definitely some follow-ups I
would do here. Um if you were actually
trying to build this um you would uh uh
use something like SCIP to actually
trace the call graphs inside of the
codebase. You can actually see what is
calling what and how that interacts
because you can track um like symbols
and how they move across the codebase.
But if you want to actually track, you
know, what is calling what and how it's
all connected, that is the higher level
that you're talking about and you need a
you need a slightly augmented approach,
another rung of of of deterministic
parsing. And you can do that um with uh
there's like a Rust or SEIP. Um there's
similar SEP outputs for like TypeScript
or or Python. I was going to do all of
that too, but I I ran out of time.
[laughter]
But to answer your question, yes,
there's uh there's definitely more
structure we can extract from a given
codebase. And that's sort of what we try
to do at Type Def is find all the
different ways that we can pull as much
context as possible out of the data that
we have.
Um I have a quick question for how would
you say like this concept of the data
context layer um combines with like
something like a data catalog like is it
the data catalog would help feed a graph
are they kind of redundant to both have
in an enterprise
>> I don't think they're redundant I think
they answer different questions um your
data catalog is a
a sort of fixed understanding of exactly
what is present in your data warehouse
which I think is a kind of a different
ask than what the context graph is
trying to extract right um I think they
they coexist you read information from
the catalog to form the the context
graph um so what you'll try to do is
basically say okay I have my say my dbt
project that has you know a bunch of
models in it those models build out uh
uh tables and views in Snowflake, right?
So we may say we're going to ingest that
DBT project. We're going to pull in all
that SQL. We're going to parse it, link
everything together, and then we're
going to say, oh, okay, this model is
corresponding to this table. Let me go
query the catalog, get information about
that table, pull it into the graph as
well. So we can say okay this model is
uh producing this physical table and
this physical table has these columns
and these columns have these these
profiles and that information all comes
from the catalog right so that catalog
of information the information schema
the profiling information all that stuff
that's essential to what we do and
that's all in the catalog so I would say
they coexist more than it's a
replacement
>> [clears throat]
>> to try to bring this back to like data
engineering and this concept of like
eval.
Do you think about the same way in terms
of like asking a set of like data
questions and then seeing how those
react uh to using the tool or not using
the tool?
>> Yes.
>> Yeah. Yeah. Precisely. Oh, so do you
have more? Sorry.
>> Sorry.
>> Oh, I didn't know if you were done. Um
yes absolutely. Um we do use uh like I
was saying we basically try to find like
as as real a data corpus as we can and
then we try to
find multiple different kinds of
scenarios right so you have your basic
fix a bug um where the scenario is we'll
inject a diff into the codebase that
introduces a bug right and then you'll
ask the agent to go and try and fix this
bug um and then you can you can test you
know that it looked at the right places
that it checked the right things that
when it fixed the bug, it didn't fix it
upstream or fix it downstream, right? By
putting a band-aid on it, right? It
actually found the right model and fixed
the right issue. And you can make those
tests easier or harder, right? Like you
can you can change the prompt language
to say, "Oh, I think there's a problem
with model XYZ." Or you can say for the
harder example, my down my dashboard Y
is having this issue where this number
is doubled. I don't know why. So forcing
the agent to work backward from what
that depends on upward through the tree
to understand like where the actual root
cause the issue is coming from and then
asserting that it actually goes in and
fixes that problem instead of leaving it
be. Um so that's what's really hard and
the problem is that the agents are
always going to cheat. Um so in your
eval harness you have to be really
careful about hardening it. Um like for
example your agent if you if you if you
say that oh my test case is the agent
will check out a branch and then it will
go and try to fix the problem. The agent
will very happily cheat and use git to
go back to main and try to figure out
how you introduce the problem in this
branch from from there. Um and it'll go
and very happily find the branch name
that says this is a test and be like oh
this is a test. Oh I can cheat on this.
Um, so you have to be very careful about
hardening your your your harness to
actually uh be representative of the
tasks that uh you want your agent to do.
Um, because that's always going to be
the danger there.
>> For these evals, do you find people like
encoding them from scratch for the most
part or like
>> there are there are some existing
frameworks for this? Um, ADE bench is is
a great one. Um, it's probably the
current industry standard for this kind
of like data engineering benchmarks.
They have a very similar approach um for
uh uh creating problems in repos using
diffs and then having the agent go and
read data from the warehouse and read
data from the code and try to fix the
problem. Um so those do exist. People
are wiring them up and I think it's
becoming more and more of a thing. I
think the harder part is always the
scaffolding around it because for code
you just have your codebase but you need
a running database. You need it to be
you know populated with the right buggy
data. you need that data to be
internally consistent. So you don't want
the agent to be spinning around trying
to figure out, oh, oh, why are the
numbers from 2024? It's we only
generated 2024 data in our sample set.
So, um, I think you run into those kind
of issues a lot. Um, which is why people
are trying to standardize it in AD. I
think the hard part is building out a
benchmark like that that other people
can use that actually has a big enough
data set. That's going to be the tricky
part and that's not something that has
been done yet. Uh, at least to me.
to my satisfaction.
Um but yeah, the uh you know, we get
back the the this is just a
summarization of the same results we
just saw. Um, we see that as we uh
increase the amount of ability, as we
tell, as we get the agent to use the
tools more, um, the agent is able to be
more consistent in its ability to answer
the same set of questions and is able to
answer those same set of questions um,
more efficiently. Um, and
an example of why it's quite important
to uh, run these eval multiple times.
It's not about your per shot accuracy,
it's about your determinism.
Um, and the number that actually matters
was how do you actually make sure that
your agent is using the new tooling. And
so you really want to make sure that
you're getting your adoption numbers up
and that you're measuring your adoption
of the tools because that's really
what's going to get you um the right the
last part of the way, right? You know,
an elegant tool that gets reached for a
third of the time is just a third of a
tool. Um, and every capability win that
you can get from better tools is gated
by this number.
Um, so this is why we built the eval,
not to prove that the tool is good, but
to prove that it's not going unused.
So the hard part about this whole talk
was basically admitting that graph works
really, really well. Um, I did all this
work and I built this context graph and
I ran the evals and it was a tie and it
was like it was kind of frustrating and
you kind of want to keep optimizing and
building the thing and trying to get
more and more out of it and it's kind of
a trap, right? That instinct is like to
build more I think can sometimes lead to
a sunk cost, right? like the agent has
its own reflex. I have mine what I think
it should be doing. And like we're we're
trying to meet in the middle, right, and
actually figure out a way to move
forward with this, right? And it's like,
oh, you think that maybe it's just that
you just need more testing or more eval
or or or more something, right? And you
end up with this this false feeling of I
just need more rigor and more tests and
then the agent will be better at using
the tools. But you really maybe you need
to ask, hey, why is GP working so well
as opposed to saying, why isn't it using
my tools? Well, maybe the answer is that
GP actually does work really well
already, right? So maybe you're not
going to win by fighting it. Um maybe
you're going to have to lean into it
just a little bit. So the agent is going
to GP anyway. Uh so when you keep trying
to out engineer GP, um you're just going
to have a kind of frustrating time. Um,
so if you can design as with the grain
as much as possible, help the agents
lean into what they want to do anyway,
uh, it will help you out quite a bit.
Um, I've now done multiple talks where I
I I had a conclusion, finished the talk,
I said, "Let me rerun one set of evals
and then I had to redo the whole talk
because the conclusions were completely
different." Um, what had happened was I
wrote my evals and I built this whole
harness and I built it wrong and I got
answers that were directionally correct.
They said that graph beat GP, but I
wanted to look into it a little deeper.
And when you look into it a little
deeper, you'll find that oh, that tool
that we made, it returns the path to the
file, but it's not like the right path.
So sometimes when they call search, it
would find the wrong path and it would
go down a wrong path to trying to read
these files. So you actually have to go
in and you read all of your different
traces, right? Go into logfire, make
sure or go into wherever you're you're
you're you're sending your traces in,
right? and make sure that you're
actually reading them because you're not
supposed to just if you just look at
your scoreboard, you might get answers
that look directionally correct or or
that look great for you, but they may be
burying underlying issues that are
actually much larger and and a much
bigger problem inside of your inside of
your architecture. Um, so the fix is
never just to make the number higher or
nicer. It's to build a harder eval. Uh,
read the traces, find the artifact,
harden the harness, and then rerun.
Never trust your own scoreboard.
Um and yeah, these are just some of the
other thoughts I had. The you know, the
the models are only getting better. Um
so, you know, you can you we can
continue to believe that the models are
going to have less variance and more
drift towards being able to uh do the
work that we want them to do. So, the
easy part may actually be building the
context, building the tools. The hard
part is really going to be building out
your eval loop, building out your
monitoring observability, and making
sure that your agent is actually doing
the work that you want it to do with the
tools you want to be using. Um, and so
all the stuff is there, the the score,
the loop, uh, it's all in the repo if
anyone wants to play with that um on
their own time. And uh,
yeah, so this is what I was talking
about before. You know, we did I did
cheat by using Rust. Um, the Rust
compiler already did run one, right?
It's homework. uh picked the language
that was free because the lesson was you
can build a well-engineered version of
something uh on a relatively easy
instance of a problem. Uh and in
general, if you can get things to work
on a slightly easier problem, it's
slightly easier to go and scale that
back up to a larger issue. Um so we now
can say, oh wow, we have this really
easy thing that we did for Rust. I want
to do for Python. And Python is just
harder, right? like you can't really if
you look at this these lines of code
you're not going to get anywhere right
if you GP client you're going to get
stuck in a land of 50,000 clients you
can use static analysis to to load this
stuff and things like that but you know
you're going to have like a a difficult
time and so this is where a code graph
really earned its keep right in a case
like this where the code bases are
larger and the the languages are are
less well structured a code graph is
actually even more effective than grap
in that case Because for Rust, you know,
I want to see what implements this
trait. Okay, cool. I just search imple,
right? Like it's really easy. But for
Python, that becomes a lot harder,
right? So that's where um you really
would need to build something out that's
more robust. Um but the structure of the
graph and the structure of the tools
doesn't necessarily have to change,
right? It's the structure of the way
that we ingest and load the data. And if
you make that modular, then you can
build that out with for as many
languages or as many projects as you
want, right? So that's kind of the
underlying structure for like how type
def works is we try to build out as many
of these different injest processes as
we can to pull data from many different
places and then sort of synthesize it
all into one. Um there is another
notebook for this. I'm not going to go
through it now because we've we've all
been here for a little while and um but
feel free to go through it yourselves
and uh try to learn more if you want.
Um, last thing I was talking about was
uh basically the meaning rung. Um, the
structure is what's telling you what's
connecting to what, but the meaning is
telling you sort of why. Uh, so there's
comments in code and dock strings and
all the other information. And folding
all of that information in helps us
understand the intent that the coders
had when they wrote the code in addition
to the actual structure of the code that
currently exists. So um we would
basically want to add in small uh passes
like this to say basically summarize the
information from the code um and uh
understand it at a at a rowbyrow basis
so that search can now answer what the
code does in addition to um its
location. Um, and
the important part when you're building
something like that, um, you're building
this sort of auditable semantic analysis
that's going to go on top of your
deterministic analysis. Um, the
important part is to ask many small
questions and not one big question. The
answer isn't writing, you know, one
really. So when we do analysis in SQL,
right, we don't just write one really
really good prompt and throw your SQL at
it and say, "Hey, uh, here's a pedantic
model with 10 fields like give me all
the information you can out of the SQL,
right? It's not going to work." Um, a
model is going to hallucinate. It's
going to invent information. It's going
to not collect as many as much
information as it can. You want to
basically instead of asking the model 10
things about a chunk of code at once,
you ask the question, you ask the model
10 different questions about 10
different smaller chunks of the code
that answer specific questions. Right?
You parse the structure
deterministically and then ask many
small focused questions that play to the
model strengths. Right? Instead of
asking the model to look at an entire
block of SQL and tell you what all the
columns mean, you parse the SQL and you
say, "Hey, here's one column. Here's its
type. Here's the comments." you know, is
this a measure, is this a dimension, is
this blah blah blah, then at that point,
you can ask the agent to do
classification and summarization, and
those are the things that it's good at,
right? And if you want to weigh it more,
um, you give it a more you give it more,
um, prompt input to that single focus
question. You don't try to cram more
questions in. You give it more context
for it to be able to answer that single
question with. So, small, grounded,
auditable, semantic operations over our
structure. Um, that's what our library
fenic is for, and that's what we use it
for as part of typed. Um, so that last
ladder, the last rung in the ladder,
which is basically we have all this
stuff layered in, we know how everything
links together. Now, what does it
actually mean? Now, we can start pulling
some of that semantic understanding of
what things actually mean by using the
LLMs in the last layer.
Um, yes, so as I was talking about
before, there's a lot more that you can
do here. you actually want to build a
coding uh codebase graph analysis agent
um you can use you can leverage call
graphs to understand who's calling this
and who references this right and you
know it can read the comments inside and
outside of the code and it can fold in
pros from outside of the code it can
fold in GitHub issues and and and your
your your linear issues and your ticket
and stuff so that's how you build this
into something that's actually more
useful and and and grounded is you start
small you start with the smallest
possible thing you can do which is how
do
extract structure out of this codebase
and then you move on to how do I take
that structure and layer into it the
semantic understanding that's really
going to help um build out
a substrate that's useful for agents to
actually work inside of this space and
make changes um and that's sort of what
the uh where the end goal is there so
anyway thanks so much guys uh this has
been my talk the agent will grip anyway
um I'm Brandon calendar from typed defev
here is the link again for the workshop
and my LinkedIn. So, uh, thanks. I can
take any questions or or any other
things, but thanks so much everybody.
[applause]
Any any questions? I can pass around the
mic for one last round.
Have you tried this kind of workflow
like across repositories where things
might be either microservices or like
going across HTTP boundaries um with any
success?
>> Uh
not particularly no. I think where where
this would where this would come into
play is on a single repository. Now we
do that at scale for our like larger
data architecture product. So I think it
can work. um you basically just need to
the hard part there is obviously
figuring out the boundaries between the
different things. So you basically need
to write
boundary classifiers that basically try
to understand um I was trying to do an
example with Python and Rust like with
maturin so you could have a similar
example of that but I didn't have time
to do that but you basically would need
to write some way of understanding when
rust called code is calling Python or
vice versa right to try to like build
out that linking layer between them. Um,
so yes, you could do it. I just think it
would it would require quite a bit more
work.
>> Any other questions?
>> Sorry.
>> I got you.
>> Cursor does a lot of the um level two
stuff. So like when you see like cursor
doing searching through your codebase,
it's usually doing semantic search like
vector embedding search um and that's
that's that that does work really well.
Like I think that there's a reason why
there's all these like code rag products
that do um that do semantic or
retrieval, right? And I think that
that's that's really great. It's just
that you know that approach does get you
the ability to find all the places in
the code that you want to then examine
with the agent. But you still have to go
and examine all those places with the
agent. Right? The goal of this approach
is if I want to be able to in one shot
say I know that I'm looking at this
function right here, right? I basically
want to be able to do the IDE click on
the thing to see all its call sites but
within my agent without my agent needing
to grab everywhere. That make sense?
Any other questions? All right, one over
here. One sec.
>> I imagine half the fun of building this
is that you end up with uh I don't know,
sort of a a vector of the graph that you
can recall.
>> Yeah. Um, I'm really curious about
caching and storage as you really start
thinking about scaling this given that
uh making sure the agent gets it right
on the first call is so key in steering.
>> Yeah, that makes sense. I think um as
you as you start to scale out your um
your graph database, you're going to
start finding that it's
uh it can get very hairy very fast. And
you're you're absolutely correct. Um, so
I think storage is less of a concern, I
think, because like these like yes,
these graphs do tend to uh get a little
sprawly, especially as they grow and
they're harder to kind of garbage
collect for, but they do um I'm less
concerned about storage and more
concerned about like
the amount of compute that it takes to
actually run like graph analysis across
all these different things. Um, so I
think the as you try to scale it up, I
think the main thing you need to focus
on like I was saying earlier is the
incrementalism like figuring out how to
rebuild this thing without regenerating
all of it I think is probably the most
important part and that's something we
fight with at typed death for trying to
build this you know at a larger scale
across a large data architecture because
you don't want to have to go and query
your warehouse you know 500 times again
right you don't want to have to go check
you know compile and all the SQL code
again right? You want to be able to
update the stuff as it's coming in. So,
I think the most important way to get
around that is design for incremental
indexing first as a first class citizen.
Um, that's kind of the only way you'll
be able to get to a point where you have
to deal with the other scaling problems.
I I think you have to deal with the
problem of reyncing the information long
before you have to deal with the actual
scaling problem of how to store it or
how to compute across it all.
Yeah.
I found that for us the building of the
golden data set and maintaining it is
always the biggest problem.
>> Yeah, I
I agree with you 100% to that and I I
that's that is one I don't have a great
answer for. I don't think because I I
think
I think so. I have two answers to that
actually. One of them is that like the
the gold data set isn't necessarily
if I was if I was actually building this
and I was testing it on something, I
would pick a specific snapshot of that
codebase, right? So I could say that
this is my snapshot and that when I run
my evals, I have a deterministically set
of my gold questions, right? That's
that's kind of a copout to your
question, right? But that's what I would
do if I was actually designing this,
right? Is I would I was I would design
this against a snapshot. So my eval
questions are deterministic and aren't
changing over time, right? Because the
in an ideal world, right, your agent is
going to get better and better at
answering the same questions. But
changing the questions based on changing
the corpus doesn't actually help you
evaluate if your agents are getting
better. Right? The best way to evaluate
if your agents are getting better is
have them do the exact same task again.
Right? So it's sort of your answer is
you don't because you if for the purpose
of evals your gold should be constant
against a constant corpus. Does that
make sense? Now if you're testing live
yes like you need to be able to figure
out new ways of testing it against your
codebase but I think that and like your
fixed eval set are different things.
Does that make sense?
>> Yeah. But like
>> Yeah. Yeah, but I mean like if you so if
we go with the codebase example and
let's say you have a kind of like a
complicated bug that is like a function
that is calling a different function and
there's like a in one of those functions
there's like a bug or there's like a if
like you said and then you have an eval
that tests that if this bug was
introduced then the agent went to this
and this function and fixed it but then
you do a refactoring and then this
function is actually not even used
anymore. So then the eval breaks.
>> Oh, I see what you're saying. So in that
case, I I think it's still I think man
is still the same because what what I'm
saying is that I when I'm building my
eval, I would say my eval is a
combination of a specific commit that
like my code is at, right? The specific
diff that I want to introduce to see if
the agent can fix it and then the
resultant set of changes from that
prompt, right? that should always stay
constant. Like I I I see what you're
saying because like yeah, the code's
going to change and it's not going to
need to fix that issue anymore, but
that's not what you're testing, right?
You're not testing the agents ability to
react to the new code. You're testing
the agents ability to make that change
based on that circumstance that it was
in when you wrote the eval, right? Like
that task I don't think has changed.
even if like it's not relevant anymore,
it's still testing something that's
useful. Does that make sense?
Question.
>> Great talk. Loved it. Um
this kind of reminds me of ontology um
>> classes and this is what Palunteer is
making a killing out of actually.
>> Yeah. So um
once you build the ontology and the
dependency um can we talk with the LLM
in these higher constructs now?
>> Yes.
>> With these classes.
>> Yes.
>> And is this is essentially what you were
kind of insinuating at this point in
time.
>> Yes. So that that's that's basically our
product, right? Is is is that concept of
we we build um we build the context
graph, we build the ontology layer on
top of it where we try to organize all
the information around your data
architecture, where things are pointed,
where things live, what things mean. Uh
and then we give the agent access to
that tool set to be able to answer
questions and and make changes within
your data architecture.
Excuse me.
All right. So, this may be a little
naive, but so going back to kind of the
product you guys are building, what you
demonstrate here. So, a lot of stuff you
showed here is very similar to what
Neo4j showed at an earlier workshop,
>> which is like, okay, here's a knowledge
graph. You as the developer with domain
expertise are going to build a knowledge
graph in this area and they're going to
provide it out to an agent and then make
that agent query cipher to get some
semantic information. I'm responsible
for I'll call it a sprawling data state
where there's a lot of you know
thirdparty software as a service. We've
got other things that are internal. My
team is responsible for you know
bringing in a lot of information for
those things. Some of them are highly
configurable like a salesforce. You
bring the information in you put in the
data warehouse etc etc and eventually
you have business intelligence on the
other side and also interaction. So the
goal is how can I get my pretty small
team of pretty good people to define the
semantic relationships between all of
this stuff in one place one time with
good version control so that then I can
both provide context and tools to AI
agents for mostly analytic work but also
write back occasionally and
documentation for human beings that have
to use these systems whether that's
onboarding or in one place I haven't
figured out the right way to do that
yet.
>> Let's chat.
>> So, are are you gonna are you going to
give me that? Because you also said like
you're not going to do the data catalog,
>> right?
>> No, we're not gonna Well, the thing is I
think I think what what I what I mean to
say is we're not going to be limited to
the data catalog because we're not going
to be reading just your Snowflake
catalog, just your, you know, just your
warehouse information. The goal is to be
reading from your Salesforce, from your
from your from your fiverr, from your
your um your air bite, from your
whatever, from all the transfer
mechanisms that you have, your airflow,
your whatever.
Incorporate all of that into a single
understood context tree uh context graph
that we can actually traverse. And then
from there, the goal is to actually um
distill out of that the things that you
were talking about. The the main problem
with semantic layers is no one wants to
maintain a semantic layer, right? It's
kind of a dirty word because once you
build one, it's all really cool and and
sick and sexy, but then you have to
actually keep updating it every time you
add models and it's it's a nightmare.
So, the goal of of typed defe is you
really just it was great. Thank you for
like gave a great understanding of
exactly what we want the product to be
able to do, which is exactly what you
said is to be able to reason across all
those different layers that you have in
your data architecture. build off a
single graph that you can actually trace
how data is flowing from Salesforce all
the way down to your BI layer, right?
And then when your agent asks when you
ask your agent a question like hey um
where is my like where is AR being
coming from it's able to say oh yeah
great that originates up here in the
Stripe data actually and then it gets
joined into your Salesforce lead data
down here um to like figure out you know
this this thing down here which is where
the actual data is being calculated.
Yeah, like that that lineage is very
useful, but and for us it's, you know,
partially for the data team that's doing
this development. Great. But I want that
to eventually be accessible to the
business, right? So they can look at
their report and we're like, that's not
right. What the hell? And then rather
than coming to my team and to yell at
me, they can say, "Oh, well that's
actually owned by these people on this
system and this record and like this is
the person I have to talk to."
>> So
>> keep it all together.
>> Agree 100% with you. And I think that
what we're trying to like one thing that
the LLM sort of let us do at a high
level that wasn't necessarily possible
for is be that kind of translation layer
that sits between the business folks the
the accountants the analysts right the
and then the data analyst the the
engineers or whatever things like that
right because what we're saying is what
we want to say is okay that business
analyst says hey that number in that
revenue dashboard is wrong right so the
process for them to fix that would be
Okay, I need to go file a ticket
somewhere that gets sat in some system.
Someone picks it up, triages it, tries
to figure out who owns that thing,
right? Sends it over to them. They had
to talk to the original. So I it's
crazy, right? I worked at Salesforce for
this, so I I get a little bit of that on
a high level. Um, so the goal with type
defeaf, right, is for able that that
that business analyst to be able to go
in and say, "Hey, my dashboard is
broken, right?" They can put in the name
of the dashboard. We can pull up the
dashboard, you know, in that session
where they are. we can trace back and
say, "Oh, yes, I think I see what's the
problem here. It's probably that, you
know, I'm multiple layers back, this is
happening. I can detect that this team
owns this this model up here. I can go
ahead and file that ticket for you with
the resolution information already
encaptured in it because I already can
see what the root cause is because I
looked back three layers and saw that
this select was wrong, right? I can
trace that back to a change that landed
last week, you know, oh, that's why this
broke here, right? And oh, we can see
when that happened because there was an
airflow run over here that actually
populated that data, right? That's what
we're trying to get to is that unified
vision of how everything works from
runtime through lineage and being able
for the agent to actually answer those
kind of questions and sit between those
different layers and make that process
more efficient because if if instead of
that ticket sitting around and bouncing
between five different teams, if it's
immediately understood understood what
the problem is and that gets routed to
the right team right away, that team can
even just in an ideal world where our
product is ubiquitous and works
perfectly, that team can just say,
"Yeah, that solution sounds good check
plus and then it goes and implements it.
Right? So that's that's the dream,
right? So but that that's kind of what
we're trying to to get to and we're we
are definitely part of the way there. So
be happy to chat.
>> All right. Any final questions?
Cool. We'll be around if you guys want
to connect with us on LinkedIn or
anytime. We love chatting about context
graphs generally. So thank you guys so
much for coming through and we'll catch
you guys later.
>> Thanks everyone.
>> [music]
