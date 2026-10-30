# How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater

Source: https://www.youtube.com/watch?v=CLve4Nx_RwI

Uploaded: 2026-10-24

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Good morning everyone. I'm Sam Green,
team lead for applied AI at Bridgewater
Associates, and this is my colleague
Erin Lensky.
And today we're here to talk to you
about the Vault, the data platform that
we've built at Bridgewater to turn
unstructured data into a first-class
asset in our investment process.
And as part of the talk this morning,
we'd like to share three lessons that
we've learned building the Vault.
The first is that humans and agents have
very different needs from a data
platform.
And so you have to build for those
different needs
separately.
The second is that the greatest impact
occurs when a single tool can meet both
of these sets of needs at the same time.
And the third is that the real prize is
when you can build the foundations
needed to make agents a proactive
participant in your investment process
or whatever you're doing with your with
your your tools
instead of a reactive reactive tool for
your humans to use.
Before I I dive deeper into talking
about the Vault, I wanted to start with
some some background about Bridgewater.
Over the last 50 years, Bridgewater has
been in the constant pursuit of the
world's best understanding of how
markets and economies work. And turning
that into a systematic encoding that we
can use to stress test our logic over
time.
And what originally began as a set of
if-then rules on a yellow legal pad
evolved into a continuous compounding
process with humans at the center
constantly looking for the next thing
that's changing in markets. And more
recently, we've been working on building
AiA, the artificial investment
associate, which puts a machine at the
center of this continuous process.
Across all these phases of evolution,
we've had a constant philosophy in mind,
which is that we want to be constantly
looking at how the world is changing and
what's going on in the world.
Noticing what what dynamics are not yet
encoded in our understanding and use
that
learning to improve and compound for the
future.
For most of Bridgewater's history, that
meant building and overseeing time
series models on structured data.
And that structured data needed to be
carefully built so that it could be safe
for use in our research process and
aligned to our internal ontology and
world model so that we could get great
leverage out of using the the data that
we had built.
With the emergence of language models,
we had a huge new opportunity to engage
with a with a much wider world of data.
Um, you know, news and research,
transcripts, policy documents, and all
of the internal conversation that was
previously just in the ether. So, the
internal memos and meeting transcripts
and debate happening inside the firm.
We quickly realized that all of that
data needed the exact same treatment to
be fit for purpose. It needed to be
carefully cleaned, governed, and made
ready for use in both point-in-time
research questions today and also our
systematic study over time.
And when we looked out at the landscape
of data vendors and data platform
providers, there was nothing that
provided us with all of the control that
we needed to build and maintain our data
advantage.
And so, we built the Vault, which is our
repository of external and internal
unstructured data.
Um, and the platform that indexes,
organizes, and makes all of it ready for
use by our human investors and agents.
Today, the Vault has more than 100
million documents in it with thousands
more added every day, uh, minute by
minute, from 135 external sources and
again growing all the time, as well as
all of the data from inside of
Bridgewater. And crucially, all that
data is not just dumped on our
investors' desks. It is carefully
aligned to our internal internal
ontology with enrichments like the
countries, concepts, markets, and most
importantly, time period discussed in
the document.
To bring this to life, I want to start
with a quick motivating example. So,
what I did here is I asked a fairly
basic representative investment question
to an enterprise chat client. I asked,
"How is AI infrastructure investment
impacting the Korean won, and do market
participants expect this to continue?"
And as as you're all I'm sure familiar
with,
the agent goes to the web and looks for
resources it can draw on because I've
explicitly asked it to go find
other people's perspectives on the
question.
And you can see it it zooms in and it
finds 15 relevant-looking resources to
draw on
before it gives me back its answer.
And when I when I zoomed in on the
answer it gave back, a couple of things
stood out to me. The first is that even
though it found 15 relevant-looking
sources, it only picked one or two to
answer to answer my question.
And the second is down at the end of
this response where the agent itself
acknowledges that it hasn't answered my
question.
It didn't find enough documents on the
open web to establish a market consensus
and meet the meet the parameters that I
laid out.
When I double-clicked even further, the
problem got even worse.
One of the notes that it primarily drew
on to answer my question was published
way back in July of 2026, even though I
asked this question and captured this
answer just at the end of last week in
early October.
In the age of AI and in investing, four
three months is a massive amount of
time. It's not even close to good enough
to draw uh draw on this resource to
answer my question.
When I ask this exact same query
attached to the vault,
something totally different happens.
The first is that the connection to the
vault helps to prompt the agent that it
should look for a specific period of
time when answering my question. So, it
zooms in on October 1st to October 8th.
It finds a much wider array of
resources, 52 candidate documents that
are relevant to the query over this
specific period of time because of the
vault's much more significant corpus of
content that's relevant to investing
questions.
And when it ultimately answers my
question, it draws on seven instead of
only one or two.
And gives me back a rich answer that the
agent is
more confident is going to address my
question.
And so, for us, this is the the big
lesson of from building the vault to
kind of motivate the talk today, which
is that it takes great data and the
right connectors to make agents
impactful.
And I'm going to talk hand it over to
Aaron now to talk about some of the
product engineering takeaways from
building the vault.
>> Thanks, Sam.
So, hi. I'm Aaron. I run product
engineering at Bridgewater. I'm going to
take us through a few of our learnings
from building the vault over the past
few years. I'm going to start with one
that might seem obvious, but I still
think it's worth saying, which is search
is hard.
But, it gets even harder if we're
designing for two different consumers.
And in this case, we're designing for
humans and agents.
I'm going to go over the difference here
starting with us. So, humans need
precision and a high signal-to-noise
ratio because we can only read so much.
Even a fast reader manages about 300
words a minute, and personally, I'm much
slower.
Agents are a different kind of reader.
They're far less sensitive to precision.
If the data is there, they'll find it.
And basically, anything you hand to them
will get attended to.
They scale super quickly and they come
and they consume about
uh a hundred times faster, 30,000 words
per minute.
And so we need to build Vault for both
of these.
And when we're thinking about the
dimensions that matter, there are these
five on on the board.
Recall, precision,
filtering, entitlements, and scale. Some
of them matter to people, some matter
more to agents, many to both.
I'm going to go deep on three of these.
Precision for people, scale for agents,
and then filtering for both.
So, precision.
Once we've filled the Vault,
our which was a heroic effort by our
data and legal teams, recall was no
longer a
pressing issue. However, the number one
complaint was Vault search is bad.
As a product owner, it's painful to hear
that, but my response was let's
benchmark it. And that's what we did.
We collected questions and found the
best documents by hand, including ones
that looked helpful but weren't.
In all In total it was about 200
examples and it took us less than a
week. It was not fun or very glamorous,
but it was very helpful.
And after we ran it, it was very clear.
Search was bad.
The key metric we were looking at is
precision at 10, which is of the top 10
results, how many are the right
documents.
And we were hitting about 60%. So, the
people were right, it was bad.
But now we had a way to measure all of
the improvements. And here on the board
are five of them. And by the time we got
done with Agentic Search,
we were up in the 90-95% uh recall at 10
or precision at 10.
All right, so that was precision.
Now on to filtering.
Like anyone, we want the most relevant
documents. But when we looked at the
production traces, what we were seeing
is that almost always there was some
condition, either as of a certain date
or from a certain source or about a
specific asset.
And all of that requires advanced
filtering, and that's where we ran into
our first major performance issue.
So I'm going to quickly go through this
of a little bit technical here of
there's classically two ways to fill
filter a vector database. Post filtering
will use that vector index first and
then filter the top results by metadata.
It's fast, but recall could be pretty
low because the globally relevant
results might not match your filters.
On the other side, we have pre-filtering
where we'll filter first and then
calculate distances for every one of
those matches. The advantage there is
that the recall is very good, but it can
be very slow, and we needed something in
between.
So that's what led us to try and then
ultimately switch to Turbo Puffer. Their
approach, which they called native
filtering, looks only in the nearest
clusters that contain matches and then
scores just those. What you end up
getting is something that's fast like
post filtering, but with close to the
same recall as pre-filtering.
And lastly, I'm going to talk about
scale.
Human scale for us is pretty pedestrian,
100 queries an hour. We have 300 users.
They're going to search, you know, every
so often. It takes our users minutes to
read the docs that they're that they're
receiving. Agents, on the other hand,
are a few orders of magnitude beyond
that. Easily 100 plus queries a second,
and agent swarms can hit thousands
easily. And they obviously, will read,
as I said earlier, will read docs in
seconds. So we needed something that
could scale as well, and again, Turbo
Puffer handled that easily, too.
So we were covering all five dimensions.
I didn't talk about entitlements, but
I'll be talking about that later today.
Um but we covered it all. It unlocked
new workflows.
But it didn't change how our researchers
worked. They still weren't coming to
Vault every morning.
And that's my second lesson that I want
to share here is that
no matter how amazing the tools are, we
can't just drop them on our investors'
desks and expect them to be used. We
need to migrate their old habits
into an a new form.
And so we looked at what they were
already doing.
Many of them were living in email. The
research came straight from the brokers.
They had subscribed
lists. They had rules that filtered
everything into folders. It worked. It
was familiar.
And they knew that they weren't missing
anything.
So we had to build all of these features
into the Vault.
That's exactly what we did. Everything's
searchable. The subscribe lists became
saved searches.
And folders became saved collections.
It's the same habits, just a new home.
And once we had them there, we can open
up new habits.
So we can ask they can ask questions
across all the data as Sam showed. They
can follow dynamic feeds by topic. And
they can hand those collections over to
their agents to take further action. And
that's when we clearly had product
market fit.
And once we had that fit, the users
wanted it everywhere. So we put it in
chat. We made a phone app. It's in Slack
in their IDE. And of course, we availed
all of that to the agents as well. Um
including a a CLI because agents love
CLIs.
And so
the main question here is okay, so what
does this enable?
Sam's going to talk about what we're
building right now.
But first and foremost, it's helping us
to move around that research circle
faster.
With our pocket analyst, which is our
first AI analyst, it can do it can do
hours
it can do hours of research in just a
few minutes for a few dollars. And
that's relying on the Vault.
And then we're expanding now with the
researcher, which is the next
generation. It's the same idea stretched
across days or weeks.
We're also able to train custom models
to more intelligently reason over the
vault's data and use those together with
other foundation models to feed
systematic decision-making processes.
The forecaster is our first one, which
produces AI-generated macro-relevant
predictions.
And then, we also have a built
investment signals from the vault,
turning unstructured data into
structured, tradable strategies.
Now, I'll hand it to Sam to take us
through Vault's latest capability.
>> Thanks.
So, like I alluded to at the beginning
of the talk, the real prize is when you
can take agents from a reactive resource
that can be ready to answer a a human's
question and instead make them proactive
participants helping to steer your
high-value professionals towards the
most important areas for their
attention.
And the way that we're solving that
problem is in an experience we're
calling the investor workbench, where
the
agent is always on tracking what's
important to that investor and
presenting them with the areas that are
most in need of their attention.
It looks like an experience like this
that relies on the vault,
where a topic is proposed and several
pieces of information are presented to
the investor to decide whether they
should dig deeper or ignore that topic
entirely.
You can see here the card that an
investor sees in order to decide whether
to dig in deeper into the same AI impact
on currencies question that we looked at
earlier in the talk.
And the investor receives everything
they need, an agentic summary if they
want a quick scan across the agent's
findings. They also get the exact
evidence that the agent was drawing on,
so they can assess for themselves what
was leading to this recommendation.
And if they choose to dig deeper, they
have a direct connection to the research
output from the analytical tools that
Aaron was just describing.
And when they dig deeper alongside the
agent to look at the dynamics driving
this question,
the learnings are automatically
captured, the results of their
collaboration are automatically captured
back in the vault.
And so this for us is the key lesson.
The vault enables compounding because it
provides the right evidence, the right
extra internal and external information
at the fingertips of our investors and
agents, and it automatically captures
the synthesis that they generate and
puts it back in the corpus for the next
turn.
And that makes us go around the circle
faster and better.
And so when we think back to our the the
question we began with,
what it takes to make an agent work is
the right context and the right
understanding of what's going on in your
world.
And so our question for you is, does
your AI know what's going on in the
world? And does it remember what your
firm has learned about it? Because we
are teaching ours too. And if these
sounds like an sound like an exciting
challenge, we'd love to talk. Thank you.
>> [applause]
