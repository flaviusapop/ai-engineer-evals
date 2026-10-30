# Large clusters for small models — Daniel Svonava, Superlinked

Source: https://www.youtube.com/watch?v=g4SsanB0gMc

Uploaded: 2026-09-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

All right, I think you guys can hear me.
I can certainly hear myself.
Um, whoever came closer gets a t-shirt.
I I meant it. There's like back full of
t-shirts over here. Uh, and also for
questions. Maybe there will be some
questions at the end. If you ask a
question, you get the t-shirt as well.
And if you can guess what is on the
background of this slide, you get a uh
you get the t-shirt as well. Any
guesses?
What does that visualize? This picture
in the background?
No. Anybody has seen a transformer
model?
>> Uh yeah, positional encoding. Very good.
You get the t-shirt, sir. All right. So,
today we'll discuss u basically small
open source models and how they are
pretty good now and how they create
unique challenges when you want to serve
a bunch of them in your own cloud. Uh
everything we'll discuss is kind of open
source. Uh do it yourself.
This is the kind of stuff you can just
uh you know run a command and own the
stack. So there is no proprietary uh you
know pieces of the puzzle here. Uh let's
get this uh underway.
Well, this works. Okay. So small models.
What do we mean by small models? Um you
know depending who you ask, the way I
think about it is basically models that
you can run on two three generations old
Nvidia hardware. The whole model fits
into one GPU.
um and therefore they are easy to serve
those GPUs are available and they are
affordable as well. Um and then most
people think okay small models um there
will be some kind of tradeoff in terms
of um you know quality of the results
and hopefully I'll be able to do a good
job in this talk to convince you that
actually for specific tasks you can be
at frontier or beyond frontier
performance and get all the other
obvious benefits right uh orders of
magnitudes of uh kind of cost savings
and uh potentially quite big uh latency
or throughput improvements of course. Um
so this is kind of one of the charts we
like to show. This is the artificial
analysis intelligence index over time.
And what they typically don't show you
is that there is like a breakdown of the
open source models you should think
about right there is the GLM 5.2 and so
on those kind of frontier open source
models with let's say 750 billion
parameters. Um but then there are the
small open source models kind of
trailing the big ones and trailing the
frontier. You can see the frontier is
kind of getting diminishing returns
these days and the small models are
catching up right. So uh you see this
kind of convergence saturation on top
and and kind of growth of the of the
small models um and you know let's say
quen 3627b
somewhere around the performance of GPT
5.1. So if you have a workflow, if you
have a pipeline that uh you know can run
with GPT 5.1, now you can move that to a
small model and uh you know get all the
all the benefits we discussed. So small
models not dumb anymore. Um now
it is also about how you use the small
models, right? So you can't just treat
that 27 billion parameter quen 36 as
your kind of totally generalized I can
prompt it to do anything kind of model.
Now you need to adopt the approach where
um you basically figure out slice of
tasks from the generalized model
workload and then per task you figure
out which model in the open source fits
the task the best. You run some evals
maybe some adaptation we'll discuss um
and then you know that's how you kind of
reach the the right quality uh to
actually push this into production. So
here is some example of a contract
review agent that uses you know nine
different models. This is the kind of
shape that you will see in your
workloads in your agents as you move to
using small models for your um setup.
you'll start to see that okay instead of
kind of hammering one API with bunch of
different requests uh or one model you
rather use a fleet of models and then
your problem is okay how do I serve all
of these different things in a way that
my infra people don't go crazy right and
this is just one of the agents that you
might be running and there might be you
know 10 of these in your company so how
do how do we sort of you know that's the
kind of expansion of infrastructure
scope let's say um Now all of those
different tasks that I mentioned there
is an open source model that's uh
sitting there waiting to be used um from
you know OCR to question answering on
top of documents to labeling images
generating SQL you know reviewing code
uh there are open source models
fine-tuned and trained for those tasks
uh you know if you use an open source
model that's trained to do OCR on
receipts in Vietnamese that project has
seen the most receipts in Vietnamese,
right? There's somebody who like took
the time to gather as much data as
possible and on that task that model
will outperform pretty much anything
else. Um, and there is, you know,
hundreds of thousands of models on
hagging phase that look like that,
right? So, it's just uh it's all sitting
there and it's all free basically mostly
quite permissive licenses. So the models
exist you know that that's not the
bottleneck
and you know we've been talking about
like open source AI since 2024
and uh it's so far still not really
happening and to the extent it's
happening in companies it basically
equals like open source AI equals AWS
bedrock uh except when you look at the
model catalog in bedrock it's like very
you know restrained in model types that
are available these models are old uh
often you two, three years behind the
state-of-the-art. Um, and when you do
any kind of fine-tuning in bedrock, you
don't actually own the fine-tuned or
trained artifacts. So, you can't, you
know, use it as an actual advantage in
your business. It kind of stays serving
from the bedrock infra.
Um, so that's on the proprietary. Now if
you do small models serving on open
source infrastructure blm sglank
different solutions just know that these
things are not tuned for any specific
model or any specific hardware model
combination you'll have to do the tuning
right this is the do-it-yourself all of
these tools ship with guides on how to
actually do the tuning the parameter
sweep tailoring to your traffic and so
on. This is a kind of open-ended
research project every time you try to
adopt one of these tools. So this is not
really something that sort of you you
take it and it's like an engineering
project and a week later you have a high
performance surveying infrastructure
doesn't work like that. Um and that's
kind of the typical problem with open
source tools, right? This kind of like a
little bit too much do it yourself. Um,
and then on top of this not being kind
of pre-tuned for small models, the small
model workloads and traffic that uses a
bunch of different models kind of flips
the equation for inference uh kind of
clusters, right? So normally when you
try to serve one big model, um, your
problems are how do I share that model
across multiple GPUs? How do I have a
router sitting on top that understands
the state of all these workers? you know
the KV cache state and so on and then
makes a top- down routing decision of
okay this request goes to this worker or
this group of workers and and so on
right it's very top down setup but if
you have small and fast requests and you
have many of them the this this sort of
top down routing becomes the bottleneck
right because the router has a little
bit obsolete version of the worker state
and it's just really hard to saturate
the workers if you have that kind of
upfront decision on that's that has to
get it perfectly right in terms of u you
know balancing the local cues on each of
these workers because there's many small
requests right um and you know like we
have experimented with the VLM and
SGline routers for small models and this
sort of traffic and it's very hard to
get your GPU utilization beyond 20 30%
under constant load and the problem is
that those batches are just not
correctly sized basically because you
that routing bottleneck. Um, and then
the third problem is that with small
models, you benefit a lot from Loras and
just model adaptation in general. And so
the traffic that you have to serve, you
know, contains, you know, people coming
to you and saying, "Hey, I have 10
loras. How do I, you know, use this with
our serving stack? Um, or I have this
custom fine tune I made last night. You
know, um, I I want to serve this in
production." And this conversation
between the AI engineer and the
infrastructure person in getting those
you know lauras up there custom models
up there that's the thing that takes
time and basically that's like the main
killer in organizational uh velocity is
talking right like ideally you would
want the infrastructure engineers to do
their job and you would want to those AI
engineers to do their job and they don't
have to talk to operate on the
day-to-day mode. So, so you know they
they are not blocking each other
basically. Um and this kind of model
adaptation desire around small models
kind of breaks that and creates a lot of
back and forth and uh that's a problem
right uh so these are some challenges
related to okay we have a bunch of small
models how do we have a cluster how do
we serve this efficiently
um so we have been playing with this
problem for a while I'm Daniel actually
from superl I kind of skip the intro um
so we are you know VC backed company out
of SF and we have been building AI
powered search and document processing
systems and and agents for the last
couple of years and our main painoint
has always been inference. um
specifically these problems that I have
described. And so we have iterated and
iterated and explored different
topologies for clusters for uh running
you know large wide fleets of small
models in different environments because
sometimes you need to deploy together
with some platform in some environment
where who knows what is available there.
um you know the small models make it
easier because in whatever environment
you can get some L4s or some kind of
small GPU quota is much easier. So this
is kind of I'll describe a little bit
about the topology of the cluster that
we have kind of converged to and by the
way this whole thing is Apache 2.0 So
completely open source. Um you guys can
just take it and wrap it and now we are
an inference startup. Um this is open
source from kind of the control plane
all the way down to the thing that runs
on the GPU. Um so we we didn't pull any
any punches. Uh and the topology is
basically there is a gateway and instead
of having a router that kind of
predecides what goes where there is a
gateway that parses some of the request
and attaches some metadata to the
request inserts that request into a
shared queue and into some side
channels. I'll go a little bit into that
and then the workers pull from that
centralized queue instead of kind of
pushing the data down to the workers.
And this way they can saturate
themselves better. And then the worker
um setup I think I have a slide for that
uh will describe how uh we basically
absorb the complexity of different model
architectures into kind of a coherent
set of workers that you know don't have
like competing Python requirements and
stuff like that. Um so that's kind of
the overall topology.
Um and this is kind of life of a
request. So maybe just uh I'll call out
a couple of things from here. Um
we you know one of the things we don't
like about the OpenAI kind of API
standard is the B 64 encoded kind of
JSON not good for small models not good
for high throughput. So we use message
pack throughout like a binary format. Um
this way we can also push all the
multimodel data through the actual API
gateway. So there is no like hey you
know binary data over here and then
request over here and then the cluster
needs access to your cloud storage to
start loading some b some binary data
images or videos. We kind of encode it
all and we push it through the gateway.
Um and then the gateway kind of
separates some of these heavier pieces
to not clog the internal queue and
differs it on cloud storage kind of
inflight while the request is in Q. So
it kind of splits up some of these
requests that are let's say over a
megabyte and then uses cloud storage in
the back end. Um but as a user you push
all your bits and byes into the API
layer and it's kind of clean interface
because of that. Um
basically the whole stack is rest. So
gateway rest the the worker is rest and
then over a socket locally it kind of
attaches to different runtimes and we
have basically pytorch kendle and sglank
on the as as a runtime um and and then
when we do the optimization I'll kind of
go into that on how we make sure that
whichever runtime we are using and
whichever code is running in that
runtime is the most efficient one. we
have an auto research loop for that
basically. Um but yeah, so so life of a
request kind of looks like that. And
like one tidbit is that you really want
to make sure that the gateway that's
kind of the first thing that's hit by
the request doesn't do too much work
because then it becomes a bottleneck,
right? So you don't even want to parse
the whole request. You want to be able
to kind of look at the packets and uh
figure out the general shape of what's
coming. do the annotation and then you
have the workers however many workers
you have hundreds of GPUs that that uh
look at the queue state and then pull
from there and and the queue we use u
nats jetstream and that thing can do you
know million requests per second like
that's very hard for that to become a
bottleneck
um so yeah like ideally you don't want
to serialize this serialize as you go
through all of these different
components that's basically the kind of
obvious thing. Um this is a little
animation that shows the idea behind the
centralized queuing, right? So instead
of the top down router trying to uh you
know fill in the local cues just right,
which is basically impossible. um you
know the the whole idea is hey can we
somehow centralize the queueing and can
the workers uh rather pick up the task
of forming their own batches with their
own prediction of the cost of the batch
uh and and then you know become much
more efficient. Now one tidbit and kind
of side note once you kind of start
working on these things uh you realize
that it's actually really hard to
predict u how many things to pick up
from that share queue for the batch to
be really like really the optimal size
and so you would want some mechanism
that sort of allows you to put some
things back into the queue if you figure
out oh like I pulled a little bit too
much and that's a network hop right so
that's a problem and we have special
optimization for that for machines that
have multiple GPUs locally, right? So
there is a there is additional kind of
machine local queueing element that
takes advantage of the fact that the
local processes that run on the multiple
GPUs on one machine can kind of
negotiate with the queue a little bit
back and forth which over the network
you know there's like milliseconds extra
that that would add and so uh we we
don't do it over the network only when
we collocate the um workers on multiGPU
machines
and you know the I mean we are not
talking about like 5% differences here
Right? So like you centralize the queue
and now you get double the throughput of
the cluster. So this is this is uh
significant. Uh I mentioned three
different runtimes. So basically it's
either you know we write let's say for
models that are encoder only we write
the the PyTorch code and we kind of
optimize it and we have a auto research
loop that optimizes it. Same for
Kendall. We started to play with Kendall
not too long ago. We still can't get it
to perform anywhere near the PyTorch
performance. So it's a little bit more
of a research project. It's just the
dependency like you know the worker
Docker image with PyTorch is like 12 GB
and the worker do basically binary
statically linked binary with Kendall is
maybe like 10% of that right and if you
care about uh kind of waking up from the
cold state and loading these images on
bunch of different machines the you know
going from 12 gigs to a gigabyte or
something like this makes makes a huge
difference. So that's kind of the
motivation behind Kendall. It's just the
the getting the same performances from
PyTorch is is is really hard. And then
SG lang we have there as a kind of uh go
to baseline like we should perform as at
least as well as as SGANG with the
optimal tuning of all of those
parameters that I mentioned that you
have to do the tuning. Um here is some
numbers. So for example when we wrap SG
lang with the socket and with our kind
of RAS side car um actually we can
improve on the bare sglank performance
just because we kind of uh do something
on the batching side that natively
sglang doesn't do and probably you can
make it to do that if you do like if you
develop custom plugins into sglang and
stuff like that like probably you can
match our performance because you know
you can just push the same logic into
the SG Glang core server uh but now you
are developing custom code that only
works with SGLAN and the whole lesson
here from small models is that the
runtimes are super diverse right you
don't want to necessarily get staged
with any one particular runtime because
there is you know we have I think on the
order of 50 different adapters now that
that we parameterize for the different
models and so you need to somehow deal
with this kind of underlying complexity
and it's probably not by building a
bunch of plugins for one specific
runtime it's probably some kind of
abstraction uh which in our case is this
rust site car concept and then the
socket um
now I'll talk about couple different
numbers but in terms of like language
around benchmarking you know the knee is
this concept of like when you ramp up
traffic on a server uh when you sort of
request more and more throughput from it
and it gives you more and more
throughput that's when you go kind of
linearly up and And then at some point
you hit this point where you kind of ask
for more and more is not coming. So you
kind of flatten out and the latency goes
up. So we call that the the knee and
it's it's like a useful concept in in
benchmarking. Uh because that's kind of
the point of saturation, right? That's
that's kind of the maximal performance
without hurting latency. Um
so just to give you some ideas of what
is possible on relatively small
hardware, right? And different types of
small models. So this is measured on the
RTX Pro 6000. We we kind of work with
Nvidia L4, you know, A100's, RTX Pro
6000, H100, that sort of range. Um,
again, those GPUs are much more readily
available kind of on demand in any
cloud. Basically, most continents have
quota, you know. Um and on this kind of
stuff uh you can basically get uh for
embedding models even up to let's say uh
hundreds of millions of parameters you
can get hundreds of thousands of tokens
per second encoded into the embedding
right so imagine you are sitting there
now like hitting your text embedding
tree on open AAI API instead you could
be like having one GPU and push half a
million tokens per second into that
thing and get the vectors out
right
like is this like connecting right you
have half a million tokens that you are
pushing into single GPU that's not even
that big per second and you are getting
out vector embeddings for your search
system as opposed to like pushing all of
that into a managed embeddings endpoint
somewhere and paying like orders of
magnitude more money right and you can
get latencies like you know low tens of
milliseconds for these calls like if you
use uh you know cohhere openai APIs and
so on these are hundreds of milliseconds
right and and this is not rocket science
you know you can have just like massive
costsaving massive latency improvements
and relatively e easy operation um with
with like handful of GPUs and some some
infra around them right so this is like
really low hanging fruit if you start
anywhere with open source models small
models embeddings are like no-brainer,
right? Uh but it doesn't end there. So
let's say u you want to look at uh named
entity recognition, you want to look at
let's say multi vector search u even
generation rate uh of text or structured
outputs and so on. um you you can be
getting you know thousands of tokens per
second output from uh you know task
specific generative models as well per
uh like let's say half a thousand per
second for for one GPU there at the
bottom um and so let's say you are
generating synthetic data you are
generating annotations for your
finetuning for your evals you know don't
do that on a on a managed endpoint
That's a perfect task because you have
it kind of under control. You can survey
the quality. That's a perfect task for
uh open source model on your own infra.
Um and then you like if the infra you
have around those GPUs is like
reasonable you'll get linear scaling
with with the number of those GPUs. Um
now another sort of u idea if you are
into small model serving uh is that you
don't you know normally um you have kind
of worker pool per model right you have
a set of workers set of nodes uh they
have GPUs you kind of bring those up you
preload the models the models load for
tens of minutes because there are
hundreds of billions of parameters uh
and so you're happy okay they finally
loaded now I have a worker pool this
mentality doesn't really work with small
models. Yeah. Yeah. Quickly. How how
what's the time left?
>> Over.
>> Oh, six minutes is over. Okay. All
right. So, pack models on the same GPU
is faster.
Um,
this is a story of how you still want to
pin some models, but you want to also do
u basically uh lazy loading and eviction
uh as a kind of function of memory
pressure. You want to figure out how to
combine the two. Um there is a little
bit about kind of auto research. We have
auto research loops for uh adding
support for new models and for their
performance. Um we build a lot of
internal tooling to do the measurement
to feed into those out research loops to
basically push the numbers forward. Um
and maybe perhaps most importantly when
we ship support for a model it has all
the tuning done right. So there is no
okay let's do a parameter sweep. We
bundle basically a config for end to end
the whole cluster. Um this is a setup
for the auto research loop. There is
like a meta loop that builds the harness
that then runs the loop and there is a
dashboard on top that helps you
understand how it works. Um, we have
custom UIs for that. And
one of the outputs of that was a Laura
that took 80 cents to train and it
improved 18 it improved quality of
retrieval on German legalist STEX as a
proof of concept by 18%. And that's it.
So small models are good. They are
relatively easy to serve. uh they are
actually much cheaper, faster, is as
smart and that QR code goes to the
GitHub repo of our cluster that I just
described. Give us a star and happy
self-hosting. Thank you.
[applause]
