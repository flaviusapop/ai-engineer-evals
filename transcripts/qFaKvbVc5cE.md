# Teaching Agents to Search with NVIDIA Data Designer — Dhruv Nathawani, NVIDIA

Source: https://www.youtube.com/watch?v=qFaKvbVc5cE

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

The workshop is about something more
generic and more powerful. It's about
how do we build data pipelines um using
the tool that we created Nemo uh data
designer uh to be able to create or add
any kind of functionality to a model or
an agent.
So let's get started. And by the way, I
have a GitHub repo uh where I have some
notebooks. So if you're interested, you
can scan the QR code or you can go to
that GitHub repo. Um and I'll have the
same QR code on all the other slides as
well. So if you miss it, there'll be
more chances to get it.
So what is the workshop about and what
will we learn here? Um the first thing
we're going to learn is how do you
actually take a target agent behavior
that you want and turn it into a data
problem right? So basically can we
create data for this targeted agentic
behavior and then can we train a model
to learn how to um uh do that task. And
so we built a tool called data designer
to build uh synthetic data pipelines uh
which does exactly that. And the use
case that we're going to target today is
search. Um, and by the way, this is a
very reusable framework. So if you want
to create data for something apart from
search, this is exactly how you would do
it.
And there's two ways to participate in
today's workshop. So um, we have, you
know, of course, you can follow live,
try to run the notebooks, but since we
just have like probably an hour or less
than an hour, um, you could also listen
now and then run the notebooks later.
Um, so yeah, make sure you get the
GitHub link. And if you want the slides,
I also have the slides on the on the uh
GitHub repo.
So you're going to need four things if
you're going to follow along either now
or after the workshop. Obviously, you
need a GPU enabled machine. So a cloud
VM or a workstation. Um, you also need a
Tavi search API key. Tavi is a company
that does uh search for agents. If you
sign up on their website, they'll give
you a thousand credits for free. And you
need data designer, which is our tool
for creating data. It's fully open
source. Anyone can download it, use it,
do whatever they want with it. And all
the notebooks that I've provided um on
the GitHub repo.
So here's the agenda for today. So we'll
first spend a few minutes talking about
what is data designer and why do we
actually need a framework like this and
then we'll talk about uh the basics. Um
there's three notebooks I'm going to
actually be showing you code. U the
first notebook is about the basics of
data designer. How do you actually
create data that you want? And then the
second notebook is about model context
protocol or MCP. How do you actually uh
create agentic data? And then the third
notebook which is what um is the super
interesting use case of search. How do
you actually teach a model to do search
and then we'll leave some time at the
end for questions.
So I want to start off with a quote from
Andre Karpati and he said internet data
is not the data you want for your
transformer. So this is um a very uh
valid point because internet data could
be you know highquality sources like
Wikipedia or it could be you know
someone's opinion on Twitter or X or
some other platform right so how do we
actually know um what data is useful for
training AI models and what data is not
useful so uh we need to process this
internet data curate it and then uh
create training data from it so that's
the traditional approach approach. What
we're proposing is that we could
actually synthetically generate data uh
either from scratch or from a seed data
set. And so that's what data designer is
for. So data designer is a framework to
create synthetic data.
And what do I mean by um seed data? So
seed data like you could use Wikipedia
data as a seed and then try to create
synthetic training data from Wikipedia.
So your synthetic data is not just made
up by a model. It is grounded in real
world uh distribution and real world
data.
So data design is a completely
open-source framework. We have a large
team at NVIDIA that works on this. Um
and uh you can just install it by uh
running pip install data designer.
And I think um what's really um what
we're really proud of is data designer
has been used to create six and a half
trillion tokens of um training data and
this is increasing every single day. Um
and yeah we're keeping track of the
GitHub stars as well. So if you like our
repo give us a star.
So uh what is synthetic data generation
right? U well one way to do synthetic
data generation is take a loop run it a
million times and then if you want to
create a product review data set just
you know continually prompt a LLM saying
give me a product give me a review and
then give me a customer profile that's
one way to create a data set but you're
going to run into a bunch of issues if
you do that so what's missing um well
diversity diversity diversity that's the
most important thing right if you
continually prompt LLM after 10, 12,
maybe 20 tries, it's going to start
repeating stuff. It's not going to give
you what you need. Um, you're also
missing correlations between all the
features that you're looking for in your
data set. Um, you don't have
multimodality.
Um, you know, you're not really able to
steer the creation of that data set and
there's no validation, verification, uh,
and so on. And if I create a data set, I
can't really share it with you because
how do you actually take the uh process
that I use to create my data set to
create something similar.
So that's why we created data designer.
So how does it work? Uh we have many
different columns or features in data
designer. U these columns are
essentially um a data designer
abstraction.
In data designer, we generate data
column by column. So first you have your
seed column which is completely
optional. So I gave the example of
Wikipedia which could be a seed data
set. Um we could use any data set as a
seed. So anything which is a CSV, JSONL,
parket file. So you could use your own
company data as seed. And then you can
try to uh add sampler columns to inject
diversity. So let's say you are trying
to create a coding data set. Well, a
very simpler sampler column would be
like easy, medium, and difficult coding
questions. So that's a sampler column.
You could add which is difficulty. You
could also add subsamplers. So for easy,
you could map it to a specific type of
problem. For medium, you could map it to
a specific type of problem and so on. So
we'll get into all of this. I know it
feels a bit abstract, but we'll get into
all of this once we look at the code. Um
and then we have columns for generating
text, for generating structured data,
for generating code. Uh we also uh data
designer is now multimodal. So you can
generate images as well. Um and you can
validate your generations too.
So the whole idea is we build a DAG or a
graph which describes how your data set
should be and then this DAG once you're
ready to execute on it you can just hit
one click and get a data set out of it.
So there's three different notebooks
we'll walk through today. Um I know some
of you are thinking well in 2026 he's
going to be showing us code right? I
mean now there's codeex and cloud code
and all these amazing tools. So I think
if you understand the code, it'll be
much easier to use codeex or cloud code
to write your own uh synthetic data
workflows for you. Uh so we'll just take
a brief look at each notebook now.
And by the way, this is our repo. So
this is our data designer repo. It's
fully open source. Um and this is the
GitHub repo that um I have created for
this workshop where we have notebooks.
Um so you can try out notebook one 2 3
and then we also have um the slides here
if you want to follow along or if you
want access to the slides after the
workshop.
So let's go to the first notebook. So
this is our intro to data designer
notebook. Can everyone see? Okay. or
should I zoom in?
It's good.
Okay, so
first things first, we set up our
environment. Um there's a bunch of uh
prompts in here that we're importing.
And then what we do is we just, you
know, import data designer. That's it
literally. Uh and once you do that, you
see in data designer there's a concept
of model providers. Um, so we're
currently using uh VLLM, so that's local
inference. So I'm running this on a on a
on a Nvidia GPU cluster and then we have
access to different types of models,
right? So on my local cluster, I have
access to GPTOSS 120 billion. You can
use any model or any open model to
create synthetic data. Um, some closed
models prevent you because of licensing
issues uh from creating data from it and
using it for training models. But open
models are usually fair game. So I'm
using this model and um the goal here is
can I actually take a data set of
Wikipedia topics uh for this notebook.
So like you know different like uh what
Wikipedia has so many different pages
and um uh many different topics. So we
just made a list of those put it in a
CSV and then we basically just call our
config builder with seed data set. And
so essentially now we're um trying to
create a data designer workflow but with
Wikipedia uh topics. Um so once you do
that you can add question difficulty.
You can say easy, medium, hard, however
you want your data set to be. And then
there's weights you can specify. So you
can have more medium questions than um
you know easy or hard. And then there's
all kinds of sampler columns you can add
about question difficulty. So for
example for easy you might do like
direct lookup or simple fact or
definition right but difficult might be
you want something in more detail or
obscure um and then once we get to the
LLM generated columns you just call this
function add column and then you have
your prompt which is essentially going
to um look something like this.
Just trying to find it.
Yep. So, you are an expert trivia
question writer. Um, so here's a topic
difficulty question type. So whenever
you put these uh ginger templating for
topic, what it's going to do is the
topics you created in the previous um or
in the seed that you had from your
Wikipedia, it's going to insert those at
runtime into this prompt. So essentially
every prompt that the LM sees is now
unique and diverse. And so the model is
going to give you diverse data when you
actually hit generate.
Um and then um you you can also have
like a structured column. So a
structured column is when instead of
trying to generate like text data um you
can try to generate like a JSON or
markdown format or any custom format
that you're interested in. Um and uh we
know that LLMs you know we have to be
nice to them. We have to talk to them
but sometimes they may not give you that
structured format that you want. So then
we just end up dropping those records.
So the way um data creation works is
we have something called preview mode in
data designer. So essentially when you
hit preview what's going to happen is
it's going to try to create three
records for you and then you can go and
look at those records. So let's look at
some records. So all of this will make a
lot more sense. So the topic here is the
worldwide web. Um, and the question or I
guess some consortium of the worldwide
web and the question is which W3C
recommendation is identified by the same
three-letter abbreviation that serves as
a airport code for some city in Norway.
So there's no way I would know the
answer to this question, right? That's
why these questions are essentially hard
because you want to invoke the model to
do search, right? But in this first
notebook, we're just trying to create
question answer pairs. So uh which is a
very simple data set. So I guess this is
the answer the model came up with. And
then you can also add LLM as a judge to
score how your model is doing. So this
is the question the model came up with.
This is the answer it came up with. And
then um this is the question quality. So
we can have another model judge what uh
it thinks of the question that the uh
previous model created um and so on. So
in the end you end up with a data set
like this. And by the way, we have a a
function that you can just push your
data sets directly to hugging face. Um
so it's super easy to use
and um you can also visualize all of
your questions here as you can see. And
then you can get some stats about your
data set. Obviously we generated only
three records here. So uh you know these
stats are not very meaningful but if you
generate like hundreds or thousands of
records you could do that. And then we
have something called batch mode. So
which is data designer.create create and
here instead of a 100 I could just you
know put how many other records I need
and then I can go and create all these
records and as I mentioned previously we
generate data column by column so in the
batch mode first you generate the
questions and then you generate the
answers right so this is obviously a
very simple example and then you have
the LLM as a judge
um and here's your final data set that's
what it looks like so That was the first
notebook. I think it's quite
straightforward once you look at it and
try it out. Um, we have a second
notebook which focuses more on MCP and
then we're going to build to the third
notebook which I think everyone will
find interesting because that's where
we'll actually talk about search.
Sorry.
>> Yeah.
>> Oh yeah. The all the GitHub links are
the same. I'm just putting them in every
single slide. So, if you missed the
first one, you can you can get it. But
I'll pause here for a minute if you want
to scan.
So, um let's talk about MCP. So, MCP is
a standard which allows um an agent to
essentially connect to tools, right? So
the tool here is tavly which is nothing
but a search tool for agents. There are
many other search tools as well. Um so
that's basically the um uh what what we
need the mo what we're trying to teach
the model here is how do you do search
right so uh tavly is a good tool for the
model to use to learn how to do that
search. Um so going back to the second
notebook.
So here what we'll do is we'll just
build upon some simple concepts from the
first notebook and we'll add um how to
create agentic data. So again you have
the imports you have the the model
configs and then the same seed data set
the same sampler column. So question
difficulty, question type and so on. And
then you actually create the question
and then at the end you get like a
config, right? I don't know why it's
printing printed this in like uh light
color but yeah this is essentially your
graph um that you're creating and then
you have the answer. So it's the exact
same thing except now when you actually
create the answer you add this tool
alias here. And so the goal is instead
of just trying to answer the question,
the model is now going to use a tavly
search tool to try to find the answer on
the internet. Right? So that's we're
build we're building upon the first
notebook where we were just like okay
please generate a question and then
please generate an answer. Now it's
please generate a question and then hey
you have this tool available. Can you
use this tool to go to try to find the
answer rather than trying to generate
the answer? So that's that's the
difference between the first and the
second notebook.
And then again you have the preview mode
where you can generate a few records and
then you look at your records. And by
the way data creation is very iterative.
It's not like one and done. So when you
create some data you look at it. If
you're not happy with it, then probably
you go change your workflow, change your
prompts and then you know iterate on it
and then once you're happy with it, you
can send it off to batch execution. So
let's look at what um the second
notebook produced. So let's say the
question is
uh to which German city did Teleifan
move its headquarters in 1949. Does
anyone know the answer?
No. Right? I mean I don't know the
answer. So um
what we want to do is create questions
that are difficult so it invokes
reasoning and tool calling from the
model and so when the model is actually
trying to respond to this um it's as you
can see here it's using tavly so the
first search it made is tell if you can
moved its headquarters in 1949 to which
company so essentially it's using one
search tool called here and then um it's
going to get an answer so this is the
query from the model and then here are
the results. These are all the URLs and
then for each URL it's going to give you
a title and then it's also giving you
the content. So that's what Tavali gives
us right if you make a query or that's
what it gives the agent when the agent
makes the query and then you end up with
the response and then finally at the end
you can create your data set with batch
mode just like we did last time. And if
you're thinking he just blazed through
this whole first two notebooks, that's
because the crux of it is in the third
notebook, right? So, um that's what I
really want us to focus on today. So,
let's talk about search. Um cuz we just
went through a couple of notebooks
showing us how to use data designer and
that's fine, but what's the problem
we're actually trying to solve? So, um
like I mentioned before, I'm a research
scientist at NVIDIA and we're also part
of the Neotron team. So, Neimotron is a
collection of found open-source
foundation models um that we've created.
Uh we just released our latest model
Ultra, but we also have two other
models. So, we have three different
sizes of models. And so, as part of that
work, we actually had to teach Neotron
how to do search. And that's very
important, right? Because maybe this
feels like a long time ago now, but
maybe two or three years ago, I'm sure
you all remember looking at like I don't
know chat GPT Claude or Gemini and then
looking at the web UI and it says the
knowledge cutoff date is December 2023.
So the reason it said that is because
well you have to start training the
model at some point. So you have to stop
collecting and creating data at some
point, right? So let's say they're
training the model in January 24. by
December 23, they need to like um
essentially freeze the data. So,
anything that the model knows after
um December 23 is not part of its
training data. So, if you had to ask a
question like what is the weather today,
there's no way the model can answer that
question from its training data, right?
Uh question.
>> Yeah.
So yeah, definitely scan the QR code. So
the idea is how do you actually um teach
the model about current events because
learning about current events seems as
important if not more important than you
know knowing about uh things from the
past, right? So um that's why search
exists and that's why models need to
learn how to do search. Um so coming
back to the slide um so teaching neotron
models how to use search tools that was
our motivation and um um we essentially
the model needs access to real-time
information to be able to do useful
things. So how did we actually do this?
So before I get to how did we do this?
We need something to measure progress
on. Right? So um in the foundation model
community when you need to measure
progress on something you use a
benchmark which is like a standardized
test set without the answers right like
we don't have the answers so one of the
benchmarks for search is browse comp uh
which is a really difficult benchmark
and uh the FIFA World Cup is going on
right now so I don't know how many
soccer fans there are here but I'm I'm a
big soccer fan but we don't call it
soccer but um between 1990 and 1994
four. Which teams played in a soccer
match with a Brazilian referee? Had four
yellow cards, two for each team, three
in total, blah blah blah. I won't read
the rest of the question, but it's it's
quite complicated question, right?
There's no way that any of us know the
answer to that or maybe there's like,
you know, someone who's um really
wellversed in this who has the answer at
the top of their head. What we would do
back in the day like you know three four
years ago is we'd actually try to break
a problem down if we had a complicated
uh query like this and then we would
reason about what queries to actually
make. We would go and search on Google
or elsewhere uh get access to more
information and then reason about what
was our original goal, what information
did we get access to and then proceed
from there and then finally arrive at
the answer. Right? So the answer is
Ireland versus Romania. I I didn't know
that.
Um so how did we actually create a data
set that allows us to train a model to
go from 0% to 30% on this browsecom
benchmark? Um so that's what we're going
to learn about today. So to do that we
took we did something um uh we we used a
seed data set which I described earlier
except our seed data set is not just
Wikipedia it's something that um is
essentially a graph of Wikipedia topics
so it's called wiki data and what we did
is we did a few hops along this graph
and that is our seed data set and I know
the diagram on the right looks like a
tree it's not a tree it's a graph
So um if it looks like a tree that's my
fault. Uh it should it should it should
be a graph. Um and essentially um you
can see um on the right the first topic
is Nvidia and then Nvidia is connected
to Jensen who is our CEO and then that
is connected to Oregon State University
because Wiki Wiki data says that that's
where he went to college and then that
college is located in Benton County and
Benton County is loca is actually named
after a person called Thomas Hart
Benton. So if you took um if you
randomly sampled an entity in wiki data
and then did five to eight hops along it
and I'll explain why five to eight
you'll end up um with a hop like this
like the green you know set of entities
with like arrows in between. So that is
essentially our seed data set to create
uh search riddles. So, one search riddle
that I could create from this, and I'm
going to have to read this from my
speaker notes, is
um
which company was founded by the person
who went to college where the county was
named after Thomas Hart Benton. So,
there's no way the LLM knows the answer
to that in the training data, right?
Because if we give an agent the chance
to cheat, it's going to cheat. It's
going to just give us the answer. it's
not going to use the tool calls or the
tools sorry like search that we want it
to use right so we want to make the
questions as difficult and as I guess um
riddle like as possible so we can invoke
the search behavior from the model so
this is our seed so I I spoke about the
first step which is create random walks
with seed and why four to eight or five
to eight hops sometimes it just you know
if you do these hops it just goes
completely off topic like It will say um
I don't know like u a person's name and
then it will say well human being well
sure that is true but you know it's not
really related like basically your hops
will go off topic so that's why we want
to as a heristic stay between four and
eight that's what worked well for me and
then you transform these seeds into
search riddles and then um you execute
the search via the search tool which is
tavly so that's how you create a data
set with a prompt and a with a search
prompt and a search response, right? And
then we evaluate our data and then
something that's not mentioned here is,
you know, we train our models, right? So
once you have the data set, you train
the model with it and then you measure
performance on a standardized benchmark.
So let's look at the notebook and see
how we can do this.
Any questions so far?
Yes.
So the reason uh it was important to do
I guess it's not difficult questions
it's questions that the model uh cannot
find on the internet readily uh cannot
find answers readily on the internet
too. So like if you took that full blob
of text that we had in the browsecom
benchmark and you put that on the web
you're not going to get the answer. I
mean you will get the answer because of
the AI search thing with Gemini now but
that's what we're trying to teach the
model essentially. Yeah.
Okay. So
um so this is the tutorial for the end
to end aentic search.
So we already spoke about the way we do
this and how we create the data. We
already spoke about how we import all
these um prompts and I wrote a function
to like use Tavi with MCP. You can go
and look at the code later. Um and
here is where we have our seed entities.
So this is the example I showed you.
This is just one seed entity. So the way
uh my seed collection algorithm works is
like you can run it a million times and
you get million different hops along
wiki data right so those are just topics
we want to ground our search riddle
creation on
so another topic is
um we like modern art and like I'm not
really an art buff but so I don't
understand most of these words but
essentially this is like another seed
hop that you can
So the way to create this data set is um
well you are an expert search agent that
uses web search to answer questions
accurately
provide valid JSON with the final answer
supporting URLs and a short
justification and here are the tools you
have available. You have one tool which
is tavly search and then here's some
usage guidelines for the tool. So, like
we're like, "Okay, please please don't
use more than like, you know, don't
don't like call the tool like a hundred
times and spend, you know, $1,000 or
something." I guess those are like all
kinds of instructions you can put in
there, but essentially um uh jokes
aside, what you want here is um your
agent shouldn't go crazy and try to like
you know spend way too much money
answering a question that's very easy or
you know something like that. So that's
why we have all these instructions and
we also have an example. So this is um
um something like in context learning,
right? So you put an example into the
prompt and then the model can
essentially um learn from that example
how to actually call the search tool.
So here's your prompt that you want to
create. So here what we do is um we
collected the wiki data hops. We can
insert those hops into the prompt here
uh which is our um you know seed entity.
And then uh we ask the model to
essentially come up with a question um
using any or all of the seed entities
from this hop. And then we ask the model
to
create a response using uh this agent
solution draw which I showed earlier.
So in the in the second notebook. So
once you do this, you'll end up with a
preview data set. And so here's our
preview data set. So Indian Council of
Medical Research is the start entity for
the seed. And then apparently that's
located in a city called Bhuaneshwar
which is a capital of some state in
India. Uh so that's our seed path. And
then here is the question that the model
came up with.
And then this Asian solution draw is not
displayed in here. But if you look at
it, we can we can see what it looks like
here. So it did a bunch of tool calls.
It reasoned about the question and then
it's trying to find the answer on the
internet.
So that's how you create um a search
tool called data set. And I guess I'll
pause here for questions and then we can
move on to the next few slides after
that. Any questions? If something was
Yes.
Yeah,
>> absolutely.
>> Yes. So we moved the bird benchmark from
26 to 41%. So you asked the you know
exact right question and we have a blog
post on this as well. Um you can read
about it. Um so all the data sets we've
created with data designer um we have
blog posts and you can see right here so
I was involved in this work as well. Uh
so yeah this talks about SQL and I can
also share the link with you after um
but essentially data designer can be
used to create any kind of data set for
training AI models possibly other data
sets as well if you're looking for test
data sets not related to model training
and so on. Um and we have a bunch of
data tools that we've created in our
team apart from data designer that I'll
talk about in the end.
>> So the soda is 70 on bird is because
it's agentic. Our um current SQL data
set is not agentic. And um also a sort
on benchmarks is very much model
dependent. We're talking about moving uh
Neotron Nano which is our small size um
LLM or SLM. Okay. I don't I don't know
if you can call it an SLM because it's
an MOE but it's an LLM. And so um for
that model size it's a pretty
respectable performance on board. Yeah.
question.
>> Yeah. No, this is a deterministic
algorithm to create the seed data and
then the uh tool calls and the agentic
stuff is in creating the actual like
performing the actual search once you
have the question and creating the
trajectory. We call it a trajectory. So
creating the search trajectory this is
deterministic. This is just something I
came up with to create seed data. Yeah,
you can have any kind of seed data.
Maybe like you know you can come up with
a better way of creating seed data than
this as well.
>> Oh great question. So we could do that.
Um we have created data sets that can be
used in pre-training and post-
trainining. My main focus is post-
training um or you know creating data
sets for post- training. So this
specific uh um I guess project was SFT
uh in posting.
Yes,
>> there's no reason apart from the fact
that uh I think someone at Nvidia did a
deal with Tavly to get credits. You can
use Exa. Exa is another search agent uh
provider. You can write your own search
tool. Um I guess so. Yeah, there's that
as well.
>> Yeah.
essentially.
>> So the golden responses are generated by
um tail designer using the model that
you choose and so um in the first
notebook um yeah and sorry I think I
think um you know I went a bit quick
because it's we just have an hour for
this workshop uh previous version of
this workshop was 2 hours. So the model
that I used is GPDOSS120B
to create the data. Um but data designer
is not just a collection of LLMs that
you can use to create data. It has a
bunch of LLM and nonLLM models as well
working together to help you create
diverse data.
>> Say that again.
>> This is SC. Yeah. Uh what do you mean?
Yes.
>> Yeah.
>> Yes.
>> Yes, you are distilling. But in some
cases, you can even go beyond
distillation. And that's the case that
I'm trying to make because we have built
this uh tool that allows you to create
diverse data. So for example, a
completely different use case that I was
working on. GPTOSS gets some percentage
on this uh benchmark called strructal
which is a way to measure how models do
on JSON, markdown, XML, YAML and CSV
formats. And Neotron actually distilled
from GPTOSS but went beyond GPOSS's
performance. So it's distillation but it
can also be more powerful than that
because of all the things we've built
into data designer. Yes.
>> How can I use data designer?
>> You can use data designer for RL.
>> So let's say uh and by the way we're
doing this for search right now or or
the team at NVIDIA is doing this for
search. So instead of trying to create
the golden solution like how he
described it or or you know um executing
the search riddles as written on my
slide, you just don't do that step and
then you essentially end up with a data
set full of prompts and then we have a
tool called Nemo Gym which is
essentially um an RL um reward function.
You know I guess it's an it's a it's a
tool to basically teach your models how
to do RL. But the thing is in Nemo gym
you write like a a function that
essentially gives you a reward and then
you can use our uh any RL training
framework to execute in real time with
those tools and then provide a reward in
RL.
>> It's a great point. We're thinking about
how to do this actually currently. But
to build something generic is the is the
challenge, right? Like we don't want to
build something specific to one use
case. Yeah.
Yeah.
Is this reliable and accurate for
ETL?
So I haven't tried it myself but I think
it is because it it should be because um
we've created a diverse set of data sets
with data designer and I think at the
start we showed about 6 and a half
trillion tokens and if it's not reliable
you should come talk to us and see how
we can help you.
>> I can't hear you. Sorry.
Sorry, I'm not able to hear.
>> Oh, I I don't know about that. I I'll
come back to you at the end and we can
we can chat more. Yeah, sorry about
that. Okay. Um, we have about 15 more
minutes. So let me move on and we can
have more questions at the end to
something really interesting which is
evaluating your synthetic data right and
that's not an easy thing to do because
without this evaluation step
the synthetic data is not that useful.
So when I started just to give you a
sense of how SDG as we call it works
synthetic data generation I started with
50,000 seeds and in the end I ended
[clears throat] up only with 7,000 high
quality endtoend SFT records and then I
used that to train the model and we
moved the benchmark from 0 to 30 right
so that's great but 50,000 to 7,000
that's a lot of you know um um funneling
and filter ing for high quality. So what
like I'm trying to focus on here is that
data quality is the most important thing
when you're trying to create data and um
what do I mean by quality? It can be
task specific but it can also be generic
like diversity is one way to um you know
one axis of quality I would say. Um so
after that I created this function to
help us um show like this is what the
LLM as a judge scores for each
trajectory
um and what is like your um you know
number of words in your uh question or
search query and then here is your keep
percentage 66% and so on. So what's
really so you can take a look at that
function later but what's really
interesting is how do you actually check
if the answers that the model got are
correct or not. So I came across this
really interesting example and the
search riddle was quite simple. It said
which comp which country owns US steel
and I thought the answer is the US. And
so um I you know I I guess the agent
predicted US in the training data set
and um my verifier said that it was
correct but then I went and googled it
and apparently the US sold US steel to
Japan I think if I remember correctly a
couple of years ago. So even my wiki
data seed can become stale, right? And
so that's the real challenge is how do
you actually evaluate and um uh tell if
the data that you've created is
um good, accurate, you know, relevant
and so on.
Um
so I guess if you go and implement a
determinist I guess like a simple
matching function like how I did you'll
end up with like 24% and then you'll be
like well my data is terrible why did I
do all of this but that's not entirely
true because here low percentage I
expected because I don't know how to
actually create that function. So this
is an active area of research is how do
you actually evaluate this data? So I
think evaluation from my perspective is
a very multifaceted problem. So you
can't just take LLM as a judge and put
it in there and hope that that's going
to you know give you everything.
Evaluation is a problem where if you
check for a 100 problems and if you see
that those 100 problems do all you all
you can tell from checking for a 100
problems is those 100 issues don't exist
in your data set. there could be a
thousand other issues. So that's the
challenge is how do you actually
evaluate the data? Um so we have a few
different ways that we do that. Um one
of them is like I mentioned earlier LLM
as a judge which is generic. Uh
something I did really interesting is I
actually did LLM as a judge with uh and
I took the judgments and I sent them to
human reviewers and I have those
reviewers um cross-check the judgments
of the LLM and essentially give me
confidence that the LLM is judging my
responses correctly. So that's one way
to do it. And then in search you could
look at real-time information. So you
have to basically find a union of all
these different different uh layers of
evaluation that's going to essentially
give you enough confidence in your data
set.
So that's it for the code. I know I
blazed through this but hopefully I've
you know um given access to all of this
in my GitHub repo so you all can take a
look. Um so let's talk about a few other
use cases. So like I mentioned earlier,
we are the um you know part of a much
larger team that creates Neotron, right?
So um my focus or my team's focus is
essentially creating data sets or
creating a framework for creating data
sets and or I guess both of those. So
there's all kinds of data sets we've
created. The first one that we spoke
about today, search tool calling. Um and
then we also have a data set to do
multi-turn tool calls. So, I think the
search one was very much single turn,
right? Like we're going from prompt to
response. But what if you had multiple
turns or what if you had multiple tools
um or you know not just search tools but
like you might have a I don't know a
weather tool or a coding tool and so on.
Um so we're working on multiple
different projects here. Another really
interesting one is structured output
generation. I briefly spoke about it.
There's a benchmark called strructal
which measures your performance on toml,
json, yaml, csv, xml and all of these
are super important because everyone
wants to use um you know agents to do
everything. Now, I'm sure you all have
seen the the uh the blowtorrch meme uh
on LinkedIn or something, but but uh if
we're going to be using agents as um the
central piece in software applications,
then they need to reliably give us um
like a JSON format or a YAML format and
so on. So, that's what we were focused
on there. Um we've also worked on SQL um
that someone asked about here and uh
we've also worked on scientific
reasoning. Um there's also pre-training
data sets that we've created using data
designer for stem performance and so on.
Um and so I can talk about the best
practices for generating data. Um I
won't go over this in detail. There's
because you can always look at the
slides later but essentially diversity
before volume. I think the Kim K2 paper
showed something similar which is 10
strategies one epoch is better than one
epoch. Sorry 10 strategies one epoch is
better than 10 epochs one strategy. And
um you always want to use the cheapest
correct column type. So like using a LLM
to create a sampler makes no sense,
right? It's a complete waste of
resources. But using LLM to generate
text data makes a lot of sense. So our
samplers are written in Python of
course. Um and then you generate you
overproduce data and then you filter
down like I mentioned earlier and then
you verify what you can uh iterate on
the preview. I think the best way to
know if your data is any good is to
actually look at the data. That's the
best way. Uh if you can look review a
few samples and um of course what is
this idea of data designer? Essentially
you're taking the data creation process
and making it um something you know
version controllable uh sharable like
code. So essentially we're creating code
that can create data. So now you can
share this code with anyone because you
know we already built all this tooling
for sharing code and having version
control and all of these other things.
So if you're trying to do search but not
exactly the way I did it and just
slightly differently you take my code
you modify it and you can create your
own data set from it. Um,
so something that's super interesting.
I'm getting into the extra slides which
I didn't think I would. I think I have
10 more minutes. Right. So, um, this is
something that's really interesting.
We've created uh something called
personas. So, Neotron Personas USA um
it's also inspired from this other paper
which is scaling synthetic data creation
with 1 billion personas. So, what is a
persona? Right. A persona is essentially
um so we're trying to solve the problem
here of how do you know if the data
you've created actually
um adheres to like demographic
information or you know grounded in some
real world distributions right that's
very important u so if I were to create
a data set of healthcare records in San
Francisco California well I want to make
sure that the uh the demograph the
actual demographic of San Francisco is
reflected in my data set, right? So like
the number of uh you know there's all
kinds of demographic features. Um so we
created a data set called Neimatron
personas uh using data designer but is
also now a seed in data designer to
create more data sets and um this
essentially allows you to learn from
user data without actually leaking any
single person's information out there.
So now you can train AI models and you
can learn from the aggregate of um you
know people's information but you don't
actually have to have like for example
my healthcare records you know directly
um uh being used in training an AI
model. I I keep using the healthcare
example because I want to find a
sensitive industry which is like you
know there's HIPPA compliance there's
all kinds of regulations there right
that we have to respect. So, um, so this
is a persona. Um, this person is a
50-year-old pharmacist with a free
spirit, balances her relaxed approach,
blah, blah, blah. But essentially,
there's a persona, there's a
professional persona, um, first name,
last name, middle name, gender, age,
um, all kinds of things. And we have a
million of these. You can take this, you
can use it, um, however you please as
seed to create more data.
So yeah, I think with the personas um I
will probably stop here. So we have two
more minutes. I'll talk about these
other tools and then we'll leave time
for questions. Oh, one question. Yeah.
>> Yeah.
>> For
>> Yeah. Yeah. Yeah. Yeah. So essent that's
essentially why we created it is to um
have a way to learn from aggregate
information without actually like you
know having individual people. So like
you could create synthetic social
security numbers. Now, they're not
actually going to be like your social
security number, right? But I think the
idea is like if there's um for example
um um I don't know what is a good
example that I
>> Yeah. Yeah.
>> Yeah. Yeah. Exactly. So for example, we
we actually created some tax data for u
you know a customer and this tax data I
realized there's exactly uh seven people
in the US who are below 18 earning more
than $10 million a year on their tax
return but there's like way more people
who are older and they're earning you
know x or y or z amount of money and so
the tax data that we create let's say we
want to create a synthetic W2 form we
want to make sure that that form is not
just random values from the LLM because
the LLM is not going to give you um if
you have you asked LLM to tell a joke
it's going to tell you the same joke
every time. So similarly, it's not going
to give you like numbers that are
realistic, right? Like it's always going
to come back to the average of things.
And so when you create data, you want to
make sure that that synthetic W2 form or
1040 form or whatever is actually um
adhering to real world distribution. So
that's why we created this persona data
set.
So we have a bunch of tools uh just two
minutes and then more questions. Sorry
about that. Um so we have a bunch of
tools that we've created. Data designer
is only the tip of the iceberg I guess.
Uh but it's our most successful tool so
far because it's our oldest tool. Uh we
also have uh you know at NVIDIA we have
data curation tools. So which is Nemo
curator which I'm sure there are other
talks about this. I I believe I saw on
the schedule. Um it is very interesting.
you know you have to take data uh real
world data curate it modify it
post-process it get it to a state where
it's usable to train in LLMs or you can
create synthetic data so I think it
depends on your use case like I'm not
going to stand here and say synthetic
data is the best thing ever for
everything but I think there are
specific use cases where you want to
curate real world data or where you want
to you know generate synthetic data um
and so we have data uh curation tools we
have data designer which is our
synthetic data generation tool We have a
new tool called anonymizer. And by the
way, all these tools are completely open
source. So everything that our org does
at NVIDIA is fully open source,
including Neotron, including all these
tools. Um, so you can use it however you
want. Um, so this data tool is called
Nemo Anonymizer. And the goal here is
can we actually anonymize data? So, I
don't know about you guys, but I I don't
know if I should be saying this when the
talk is recorded, but I've been putting
all kinds of things into my agents like
you know, I accidentally put my API keys
in there once or like you know some
other sensitive information, right? All
this log data for like all your agents
that you're using. You need some way to
anonymize it and before it's usable,
right? So, that's what anonymizer does.
So, that's just an example, but there's
obviously many other ways to use
anonymizer. And then we have Nemo safe
synthesizer which is allowing us to
generate safe synthetic versions of
sensitive data sets um as well. So yeah
come talk to me if you have any
questions. Um here's my LinkedIn if you
want to stay in touch. Uh again you can
use data designer. I would love for you
guys to try out the notebooks. I'm so
sorry that we had to we had only one
hour so I had to just like blaze through
all the code but you can try out the
notebooks. We also have the blogs if
you're interested in text to SQL or some
some other use case. So um this is this
is showing us how to use the personas.
Um I think there's a blog somewhere on
how we created the personas data set for
the US. We took the census information
and we used a PGM, a probabilistic
graphical model to essentially um create
um like a connection between all
basically take that demographic
information, process it and then try to
uh uh create a data set from it uh
essentially. So that's what we did. Um
and so every country pro uh publishes
this uh demographic information. So,
it's not really like um I'm looking at
other slides now. We we've done a bunch
of these workshops recently. Um but
yeah, there's all kinds of personas if
you're not if you're trying to build for
something outside the US, if you're
building something for Japan, India,
Singapore, Brazil, I'm sure we have more
now. So, we we have all kinds of
personas data sets. So, um it's giving
us um um a way to uh create customized
AI for whichever country you're
interested in.
