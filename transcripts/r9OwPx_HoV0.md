# YouTube

Source: https://www.youtube.com/watch?v=r9OwPx_HoV0

Uploaded: 2026-09-16

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Hi everybody. Uh,
thank you for coming today. Uh, welcome
to a talk about nothing. Sorry, a talk
about retrieval.
My name is Yuval. I work at AI21, which
is essentially an AI research lab. And
today I want to talk to you about
something that most people don't want to
talk about, which is chunking.
And I hope to convince you by the end
that chunking isn't dead and there is
something to do with that.
And really, if you are at
X, LinkedIn, wherever, you've probably
seen that RAG is dead.
Right? I think people also killed MCP
lately.
And RAG is dead again. Long live agentic
AI, retrieval, agentic search. And there
is come the come a time where you have
to ask yourself, how many times can RAG
die? Right?
And even when someone says, well, RAG
isn't dead, like Jerry, the CEO of
LlamaIndex,
they still have to kill something, and
apparently this something is chunking.
Like, don't invest in it. Don't do it.
And this is the reason that people said
that chunking is dead because everybody
is using agentic search now, right? You
have grabs, you have LS, you have finds.
All of these are great,
but these are still not enough if you
have a lot of data and you have various
amount of queries.
Just a second.
And I think that the main reason that a
lot of people don't like to talk about
chunking, it's because it's not the fun
part, right? In every rug or files uh
system, we have two stages. The first
stage is the like the boring one, as you
may. The one you do in the beginning.
You have a lot of data. You have to
pre-process it. You have to decide on
the chunk size. And then you have to
store everything in a vector DB.
The other part is the retrieval part.
Essentially, the the one that happens
per query. This is something which is
much easier to do, right? It's much
easier to optimize. You can use all your
queries, and then you can play with the
max K,
uh top K, sorry. You can uh play with
the hybrid search, maybe. Those kind of
things.
Much more fun to do retrieval tuning,
right?
Uh so,
I will claim that if we have to kill
something, if something has to be dead,
then it's probably retrieval tuning. And
yes, identic search probably kill that.
And but still identic search, even if we
can accept the fact that it killed the
retrieval tuning, it's still not good
enough when you have a lot of right
scale, a lot of data. It costs a lot of
money. I don't think I have to mention
that anymore. Token maxing is like
something that everybody's talking
about. And the thing underneath, which
is if the data itself is not ordered in
a right way
in your folders, in your directories,
you still get something which is
inefficient. So, let's try to think of
like a timely example, right? The FIFA
World Cup is now. And let's imagine that
we have a data set that contains of all
the FIFA World Cup. So, every directory
is the let's say the '98 one, the 2002
one, and so on, and so on.
But if your query asks
whi- which team won the most
World Cups,
you can't just go to a folder and ask
that. You have to go to every folder,
see who won, and then aggregate this
together, which is very inefficient.
The answer, by the way, is Brazil, I
hope, at least according to
Woo! Yeah, uh
according to the time that this uh
conversation is happening.
So, retrieval doesn't actually die,
okay? We're not killing anything in this
uh lecture. It is got demoted into
plumbing.
And
I think that everybody who worked on any
rag system know the feeling. Day one or
week one or maybe even month one, if
you're very thorough, you're picking
some sort of a chunk size. Let's say
512.
Uh maybe you're probably putting some
overlap, right? 10, 20%, so on, indexing
everything, and forget all about it.
And you can, right? We talked a lot
about the fixed chunking strategies,
where if your chunk something which is
too big, right? So, you get the whole
picture, which is nice, but you're
losing a lot of the nuance, and all the
chunks will not get meaningful
embeddings. Where if you will choose
your chunks to be too small, you're
getting the big picture lost.
And really it won't be as efficient.
So, what this tells us is that chunking
is essentially a lossy compression. No
matter what we're doing, we're losing
something.
And
I will I will claim that there is no
right chunk size.
And a lot of you who worked on data will
say, "No, but we have this corpus, we
have this data set, and we really used
it, and we optimized our system to work
very, very well on this data."
And we thought so, too. We had a lot of
experience with it, with a lot of
different types of agents and systems
and workflows that you can really, and
right? You think about benchmarks. How
easy it is to overfit your model to a
benchmark.
But not with uh rag. It doesn't happen
there.
And you cannot really optimize it per
data set. And I will claim that it is
query dependent.
And how can I be so sure? How can I
claim such a thing? Because we run
experiments and we tested and now I'm
going to present it to you.
So what we did, instead of saying what
is the best chunk size per data,
let's find out. Let's Let's actually
take a data set
and duplicate this data set several
times. In this case, six times.
In every duplication, in every instance,
the chunk size is different. So we have
a database with a chunk size of 2,000, a
database with a chunk size of 1,000 and
so on and so on.
And we did it with several data sets. So
QMSum, which is a meeting transcript
data set, NarrativeQA, which is question
answering on novels, and Seinfeld data
set, which is trivia about nothing.
Not really. It's a trivia trivia
questions about the transcripts of the
Seinfeld. It's a
kind of a trolling data set that we
built
in-house. We also published it if
anybody wants the the link at the end.
And we tested on all of them
to see what happens. And first of all,
we just wanted to see for every data set
which chunk size is the best.
And what we're seeing here is an example
from the Seinfeld data set where
essentially
two queries, which are different by
nature,
get different results
based on the chunk size. So the first
question, what is the name for Jerry's
favorite shirt? You can say this is a
very focused question, very specific
question. The answer to it is probably
very contained and this is something
that a smaller chunk size will do best
in. And you can see
rank one versus rank below 50. Between
100 tokens fixed uh uh size
chunk size to 100. Whereas a question
like where who does Jerry describe as
his nemesis and pure evil, which I'm not
even that big of a Seinfeld fan and I
know it's Newman. Uh but if you look at
the transcript, it's not something you
can find that easily. And you can see
that it really changes, right? If you
use small chunk size, you will not get
the answer.
And what we did to really after we ran
all of these things and we noticed that,
we said, "What if we had an oracle or a
genie, if you want, that can tell us for
every query what is the best chunk size
to do retrieval for?"
This essentially is the oracle
experiment. This is what we wanted to
know to see the potential. This is not
right, we already have the answers. So,
we're not actually building a system
here. We just want to see what is the
potential that we have here.
And what you can see here, okay, in this
graph, all the blue First of all, the Y
axis is the recall. Higher is better.
Uh the X axis is the number of retrieved
chunks. So, it's recall at K versus K.
You can see all the blue lines, probably
indistinguishable, but
each of them is the performance for a
fixed chunk size. Whereas the orange one
is the oracle line. This is for every
query,
we took the best one out of these.
And
you can see it happens across several
data sets. In a lot of them, you can
actually see that the blue lines inter
intersect with each other, meaning that
indeed for a lot of the data sets, no
chunk size
actually dominates. And what's more
interesting is that there's a lot of
potential. The gap, which you can see
between the orange line and all the blue
lines, is big. And when I say big, it's
something like 20 to 40%.
Just from doing strategy on chunking and
very simple strategy,
may I add.
And this is like that this gap, this is
what the choice of 512 or 1,000 or
whatever, right? This number is just
arbitrary. This is what it costs you.
And I think that the the problem here is
like
it's a bit tricky because it's kind of
like a
an information problem that we don't
have the information that we need at
every stage. And what do I mean by that?
If I'm looking at the indexing part
where I do have control over the chunk
size,
I don't know what the queries will be.
I can guess. I can maybe estimate. I I
can try, but I don't know what the
queries will be, so I cannot
adjust my chunk size accordingly.
And the retrieval part where I do have
my queries,
I cannot control the chunk size,
right? It's already fixed. And I
obviously will not do the entire process
per query from the beginning.
So, we looked at prior works such as
notably Entropic,
contextual retrieval, where they enrich
every chunk, and others that fancy try
to improve the latent space of every
chunk. But this is not the direction
that we went. All of them just stayed in
the model of let's work with a fixed
chunk size, whereas we took a different
approach. And we said, "Why commit to
one where we can commit to several?"
And we call it the multi-scale indexing.
Essentially, we're just doing what we've
seen before. So, we're checking the
database, we duplicate it, and chunk it
with several
chunk chunk sizes or window sizes.
And then,
sorry, um, and then this is happens at
the indexing. And then at retrieval
time, we are querying all of them. So,
if we had n uh
duplicates of database n window sizes,
we now have to run six different
retrieval calls per query. Uh sorry, uh
six is n.
And how do we combine them? We obviously
cannot use the oracle, right? The oracle
is something that we have just for
potential. In real life, we don't know
the answer.
Uh but what we can do is to find some
sort of merging algorithm.
Now, you would say, when we look at it
like this,
what can be the issue? The fact that we
have
n ranking, but the rankings are for
chunks.
And chunks with different sizes are not
really comparable, right? So, instead,
we opted to do something which is pretty
popular these days, and a lot of the rag
systems actually work like this, that
instead of just retrieving the chunk,
when we're getting a chunk, we're
retrieving the entire document, right?
When context window grows, we want to
give more and more context. And now, in
this case, we have n right? And uh
rankings of the same documents, because
they're not chunks anymore. And this we
can compare.
And in this case, you can think of
retrieval as essentially just voting,
right? So, it's not
purely ranking. We don't have run
ranking, and then we're doing a re-rank.
We're having n different ranks of the
relevant documents, and we want to
aggregate them all into one.
That's why we're using something called
RRF, reciprocal rank fusion, okay, which
is pretty much a simple uh formula. We
tried several things. This worked the
best. And as you can see, it's not a
model. It's not something that you have
to do specifically, like especially.
This is just a simple script that takes
really no time.
And this is how the full uh uh
how the full system looks like. So, we
have the indexing n times, then uh we
query each query from every database,
and we're using RRF to combine them all.
And the results
you can guess that they're good,
otherwise I would not uh
standing here in uh
being way too much uh
uh confident. All right, but you can see
we tested across several data sets, a QM
sum, narrative QA, SciFeL, and also a
finance bench. Uh we took all of them,
and it matches the best uh bits that
best fixed uh size.
Let's see it in a graph. Uh it's a bit
hard to see here, so I'll walk it
slowly. Every row here is a chunk size,
so you can see 50, 100, and so on. The
bottom row is our method, this one, the
one that you
do from all of them and then combine,
and the every column is uh recall at
something. So, recall at 1, 2, 3, up
until 10.
What you can see here is that two
things, right? First of all, that across
like recall at whatever, uh our method
still wins, which you can think is very
easy, but the fact that you have to
combine all of them is not very it's not
something which is very trivial.
And also you can see that the quality
actually increases. The heat map where
you can see it's become much greener.
And again, this was just something that
I wanted to show in large. Here you can
see uh all four of the data sets, where
we do achieve
better results uh
really
quite like 20, 30, 40% even in a lot of
the things. Uh also, there are results
that I did not show you here, uh which
uh are on MTAB. Uh
you can see in our blog, I will put the
link later. We're getting there also a
lot of improvements, somewhere between
10 to 40% depending on the data set.
Now, I'm I'm I'm not naive. I'm not
going to claim here that this costs
nothing. Obviously, there is a cost,
right? No free lunches. Everything has
to come with something. And yes, this
costs with extra memory. It costs
something between two to five to
O of one, right? A constant of
additional memory where you have to keep
all of those uh
all those uh copies of the database.
However, if you think about it,
latency-wise, it doesn't really affect
that because you can do all the
retrieval part parallelly.
And also, the RRF part doesn't really
take a lot of time.
Uh I will say that this was a very nice
research project that we did and we got
really really cool results. There are
things to do, right? There are places to
improve. There are future work uh to do.
More precisely, we want to understand
how many chunk sizes do we want and and
which.
All right, that the fact that we worked
with 50, 100, 200, and so on was
pretty arbitrary uh to be honest. So, we
do need to figure out how to compute
this and how to know how many copies
exactly do you need. Uh also, go beyond
RRF, right? The fact that we're using
RRF is because it worked the best from
the methods that we used, but it doesn't
mean that there is no better method.
And if I need to leave you with
something, I would say that agents
didn't kill retrieval.
Nothing died. Come on. Uh it's just
infrastructure. And the part the bad bad
part is that it's infrastructure from
2022.
And with really simple
simple methods, you can take your
RAG system or anything that has to do
with storing data and then retrieve it
with 20 to 40%
again, without any
something too sophisticated.
So, if you
want to hear more about or read more
about it, you can read the blog. There
is also an example code there and the
sign for data set. And that's it. I'm
Yuval. Thank you so much being here.
>> Woo!
>> [applause]
[music]
