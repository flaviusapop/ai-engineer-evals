# Agents That Own Their Inference — Du'an Lightfoot & Khaja Omer, Akamai Technologies

Source: https://www.youtube.com/watch?v=4n08JHb90hI

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

I mentioned before my name is Dewan
Lightoot. I'm a developer AC advocate at
Akami and this is my colleague.
>> I'm Kaja Omar. I go by R. I'm a senior
software engineer at Akami. And we're
going to be talking agents that own
their own inference, building production
AI agents on dedicated GPUs.
Now, why are we here?
Things are kind of changing. And for me,
I started building agents before tool
calling. Back in January 2023 is when I
built my first agent. I would take a
prompt, that context was about 8,000
tokens at the time, and I would parse
that prompt and then make a tool call
with Python and then give the response
back to an LLM, right? But as I was
doing that, I found something
interesting. It can get really
expensive, right? And then I started
using local models to figure out, okay,
how can I do this? And then I learned
something else. There's another
challenge around that because if I'm
using a smaller model, it may not be as
capable and then I may be compute bound
that memory in that GPU may not handle
the larger context. So that's the inputs
and outputs and then the multiple turns
in the tool cost. How do we get the most
either the GPUs, the costs, the latency
that we need in production or just for
our own use cases, right? So the reason
why we're here, we're going to talk
about
agents that are often renting their
intelligence and then how you can take
back that control and own it.
When it comes to an agent, it's just a
loop. You invoke an LLM, it has access
to tools, it has access to an
environment, makes a decision, a
reasoning decision on what actions to
take once you invoke it or give it a
prompt. And then those actions are being
performed by your tools, your Python
code, your other programming languages
and then given back to a model. The
model evaluates that the actions, the
results and then updates the plan, takes
additional actions or the goal is
achieved, right? But all that
requires tokens to be generated, right?
And depending on your application can
lead to latency challenges. So we're
going to talk about how you can actually
man manage all of that on dedicated
GPUs.
So what does it mean to own your
inference? First, when it comes to
owning owning your inference, you
actually own the GPU or rent the GPU. So
when you do that, that means that you
have access to the GPU, the hardware for
that AI to be ran on, for the models to
live on, which means then you have
access to control where it goes. So the
data never leaves your cluster, never
leaves your data center, never leaves
your laptop, right? You now own that
intelligence and what's happening with
the model.
And if you're in the cloud, you can also
do something like private VPC endpoints
or have it in the VPC so it never leaves
your VPC. Right? I know we all have
different environments, have different
ways to set up our infrastructure. We
can talk about all of those.
Now what's the difference like when do
you own
when do you rent? Well, first if your
usage is high and steady, why is that?
Yes.
>> Yes. At the end of the talk, I'll have a
link to the slide and everything that we
showed code, everything. You can
download it and take it with you. So,
thank you. Now, when do you own if the
usage is high? Right? If you're
constantly
have a workload running, because if
you're paying for a GPU, you're renting
a GPU. What does that mean?
that GPU should always be working.
Otherwise, what are you paying for? So,
that's something you got to think about.
Then, when it comes to the data, if you
need that data to stay private, if you
need to own the data, you care about
your intellectual property, or you have
some governance and compliance reasons
why you can't use a public provider when
it comes to AI, that's another reason
you want to own.
And then
the hardware, that's something we got to
think about your hardware. If you can
afford the capacity and you have the
capacity, why not run those models,
right, for your use cases because then
you have that full control. Now, when do
you rent? If your traffic is low,
bursty, you just need intelligence
sporadically,
it might not be efficient for you to own
some GPUs. Next, well, we start talking
about intelligence. The more capable
models, they're going to cost for those
GPUs. And often times, those providers
will provide that intelligence on the
GPUs because they have the
infrastructure for that. So, it may make
more sense to use those providers to get
that intelligence, get those benefits.
And then the next part which is often a
challenge is that your teams may not
have the knowledge or the expertise to
support dedicated or self-hosted AI.
Now today's agenda we're going to start
out discussing some of the foundation
you need to understand like the
infrastructure stack we'll be using
units and memory budget. We'll look at
prefield decode and KB cache and what
that looks like. And then from there
we'll look at dis dense models verse
mixture of experts so you understand
what that actually looks like on the GPU
and why you would pick one or the other
from there will discuss how to optimize
your inference right once you figure out
okay we want to do self-hosted how can
we optimize this to get the most out of
our GPUs the inference engine that we
run and just our entire workload
and then finally from there. We'll take
that agent and deploy it into our own
dedicated cluster.
With that being said, I'm going to pass
it off to you, Omar. Right. Thank you.
So, next uh we'll talk about uh the
environment that you each of you is
going to get for this workshop. Um we
have a Kubernetes cluster with around
200 plus GPU nodes. Each of you gets a
single GPU. Um and we have set it up in
such a way that uh each of you gets sort
of like your own namespace and within
that namespace you will have like your
Jupyter notebook running and then you
will have your VLM inference endpoint
running as well that you'll be playing
around with. Um and then we're also
going to be deploying uh the agent on
there as well. Uh the cool thing here is
that the VLM endpoint that we have
running in your namespace, you're going
to be optimizing it uh as part of uh um
after the first four modules. And um I
think that'll be pretty interesting.
We're going to look at different
techniques that we're going to be using
there uh to do so. And you're going to
redeploy this VLM endpoint over and over
again until you have sort of optimized
it to increase the throughput uh reduce
the latency and uh make sure like you're
meeting all your SLAs's.
And then the other thing I want to talk
about is uh GPUs on LKE. So I work on
the Kubernetes side of things at Okami.
Um so this is sort of my wheelhouse. So
if anyone has any Kubernetes related
questions, uh feel free to ask anytime.
But I want to talk about what Akami has.
So we have the uh we're going to be
using the RTX 4000 ADA GPUs. Uh we also
have other GPUs available. Uh but these
are dedicated GPUs. EGPU has 200 uh eGPU
has 2 GB of uh VRAM with 260 GB per
second memory bandwidth. So the decode
will be pretty quick because of that. Uh
we have high performance in Tflops. Uh
large amount of CUDA core. So the
pre-fill will be pretty quick as well
because of that. Uh currently for your
workshop we will be using a single GPU
but that doesn't mean when you want to
deploy this at the end on your own you
can have different plans that we offer
as well where you can have up to four
GPUs in a node. So that goes up to 80
gigabytes of uh VRAM on a single node.
So you can deploy uh decently sized uh
models on there as well. Um and uh
everything is sort of orchestrated by
LKE. So setting up the node, uh
deploying the drivers, uh setting it all
up for you. So that way you don't have
to do anything manually. Uh everything
is sort of like one click. You click a
button, everything gets deployed and
you're off to races. Um yeah, for more
information, we have a link here as
well. Um and at the end, you'll
definitely get all these slides. So
you'll be able to get to the pages and
then um
I'll give it back to Dwan.
>> All right. So for the inference engine,
we're going to be using V LLM. Now, some
of you may have heard of Lama, which is
great for local, but VLM
offers some benefits that are better for
production. One of those being being
continuous batching out the box, the
other being page detention. Now, it also
supports the Open AI compatible API. So
if you're using whatever SDK that
supports Open AI, you can use it with
VLM.
It also allows you to do some really
interesting tweaks when you're setting
up inference for your for your endpoints
and for your applications. Now, I
mentioned continuous batching. For those
of you that don't know what it is and
how it actually works, this happens at
the prefill stage, right? the prompts
come in and normally with static batch,
let's say you have a school bus full of
kids. Well, in order for you to drop get
new kids with static batching, you have
to drop off every kid one at a time and
then once all the kids are dropped off,
you go back and get the rest of the kids
and then start the next batch. But with
continuous batching, you can drop off a
kid and pick a kid all at the same time.
This is way more efficient when it comes
to the KV caching that happens during
the preill stage.
now
or when it comes to page detention.
Paged detention is when you think about
the KB cache and you think about what's
actually happening there's memory space
that happens. So the prompt comes in and
the longest prompt is going to take up
memory space. When you when page
attention that memory space gets
allocated even for smaller prompts,
right? But with page attention now that
is all managed through c with the VLM
that ensures that you can continuously
pro process generate and batch those
requests as they come through VLM. It
has auler that kind of manages the
batching, but it makes this really
efficient. Now, there are other service
engines that are out there, and we'll
talk about some of those in this
workshop.
With that being said, some of the
metrics you're going to want to care
about is going to be throughput, right?
To understand how your GPU is performing
that time, the first token, understand
that, okay, you sent a prompt. How long
does it take to get the first token
back? from there that KV cache
utilization. We're going to look at
these metrics and show you how to get
all of that out of VLM and then the QEP.
So these are some of the metrics as
we're going through this workshop you'll
you'll see and be able to better
understand.
And with that being said, we're going to
access the environment. So if you can
scan this QR code, pull out your laptops
if you want to follow along. If not, you
can follow us as we go through the
workshop. In this Jupyter notebook, we
have nine different labs that we'll
cover and all of the resources and
dependencies are loaded into this
environment. Now, if you want to look at
the code and try this on your own at
home, I do have the repo public on
accommoders. I'll have this link along
with the presentation and everything
that we shared available with one QR
code that you can download. And if you
need me to make a short link, I will.
All right, with that being said, we're
gonna start with the first module in the
workshop. If everyone is connected.
>> Yeah, it was kind of slow for me too,
which is why I went to my own leak
shortener because I kind of made that
really fast with Russ. So yeah,
>> hopefully like if you do have a hot
spot, I would use your hotspot. Um but
we'll try to make the best out of the
experience.
Sound good?
Awesome. All right. So in the first
module module, we're going to talk about
the inference stack. We're going to
connect to our VLM endpoint, understand
it, see how it generates tokens. We'll
also look at building our first agent.
some things that we need to know, look
at some met some metrics and then
understand the model that we'll connect
to. The model that we'll use is going to
be Quinn 3 4B, but we have several
models that sit on a PVC that you can
actually load and unload for this
endpoint. Now, when we talk about VL LM,
one of the things about it is when you
serve an endpoint, it just has one
model, right? So if you want to serve
two models, you're going to need another
V LMA endpoint, right? Which means you
may need some model routing, a gateway
in front of it to kind of handle that.
Now, it does support authentication, but
there's no authorization. So you may
need a gateway around that, right? So
agent gateway is often kerve is another
one. Um, any others?
>> There's LLMD. There's there's all sorts
of open source tooling out there that
lets you do that. Uh but the main but
the main one is like Kserve is what we
use a lot. Um and it's it's pretty good
and doing the scaling, doing the routing
and the authentication as well, right?
Another thing it doesn't have is rate
limiting, right? If you're processing
requests, you may want to rate limit. So
again, you want to find a gateway to put
in front of it to manage those requests
and also handle the routing.
I mentioned that when it comes to the
runtime there are other
service endpoints that or service
runtimes that you can actually use for
the server. SG lang is one, tensor RT is
another and llama CPP which we do go
over this later with a little bit more
in depth so you can kind of understand
it. Now in this environment you are
connected to a Jupyter notebook that
lives in the name space. You also have
the VLM server endpoint that you'll see
here in a moment. And all of this is in
its own pod. And then you'll have
another pod. Well, another pod that you
can launch for the agent. And we'll see
that too. So, let's go ahead and install
our dependencies.
So, we'll install our dependencies. I've
kind of already ran through this, so
some of this is already loaded in my
runtime. I figured we don't know how the
internet will be, right? But the good
thing is once you send a request, it
happens within the cluster.
So once we send our first request
to understand how we're configured in
VLM, you can notice the model that we
have the name of your name space inside
of the cluster. The coupube config is
just for your namespace. So that way
nobody can access anyone else's
namespace in the environment. And then
we don't have an API key set, but you
can set one with V L.
Now from here, we're going to use the
open AI
API compatible endpoint to be able or
API to connect to the VLM QN
34B 4 billion parameter model. I believe
we're using that at FP8, meaning that it
actually sits at um eight billion
parameters. Is it eight billion
parameters?
>> No, four billion parameters.
>> Four billion parameters.
>> We're using BF16.
>> Oh, BF, that's what it is.
>> Four precision.
>> Yeah. So, we're using BF16 full
position. So, you times the bits or
bytes or parameters by two. So, it's 4
billion, which means it's eight gigs on
the GPU.
Now once we invoke we got our response
for the model and we can see what it was
actually served by. Now this was all
within our cluster. That was pretty
fast, right? It lives within our
cluster. So hopefully with this
experience since we're not hitting the
public API, we're already connected to
this HTTP. It's going to happen right
inside of the cluster. The response
should come back a little faster.
Now we're going to trace send a trace in
the end so we can actually understand
how this actually looks like when it
goes through the prefill the KB cache
and the decode phase.
So here we have our stream that we're
going to configure. We're going to look
at the chunks and do some calculations.
We'll get that time to first token so we
can understand that. We'll see how all
of this is generated here in a moment.
So if we run this,
I ran that one again. We'll come down
here and run that.
This may take a little bit to go
through, but we should see time. The
first tokens took 37 milliseconds and
time output token, the decode phase,
which means every token after the after
the time of first token, right? That's
going to be that inner in interle
latency, right? that inter latency that
happens when those tokens are processed.
So, we're calculating that and we're
getting about 40 tokens per second,
which is probably going to be our cap.
But when we start talking throughput,
that kind of changes because this is
just one request. But imagine if we had
hundreds of requests or 16 requests,
that throughput is going to be a lot
higher, but they're still going to be
capped at that 40 tokens per second,
right? Or it could go down, but we can
still get more on that throughput.
And I believe Omar will go deeper into
that. So one of the things that I want
to showcase is the question is around
why don't you just run this on CPU? Um I
didn't want to do CPU on environment
because this this um pod for this or
this container for the Jupyter notebook
is only one gig, right? So trying to run
a local model on this is gonna it's just
going to crash. So I kind of simulated
what that would look like. But if you're
trying to run a local model on CPU, it's
going to be a lot slower, right? It
can't do the complex multiplication in
those matrices like a GPU can. That's
the purpose of a GPU. It does all those
all that math in parallel, which makes
it a lot faster, right? So, we simulate
this on on the CPU.
And then from there, we actually look
look at this on the GPU to see how that
looks.
We got 45 tokens per second.
And one of the things about this and
which is interesting to me is that
I do a lot of I would say local models
and running them. But 45 tokens or 39
tokens per second isn't that bad for an
application if you're running it for a
specific use case. Right? If you have a
specific use case and you don't care
about the latency, you don't care about
those like if you have a chatbot, you
want that kind of that first token to
come fast. But for a standard
application where you just kick off a
job in the background, well, that 39
tokens per second may not be that bad,
right? So sometimes a lower token per
second or a lower time to first token
may not be as important depending on the
application and the latency that you
care about, right? you may care more
about the intelligence in the job
getting done than you do actually how
fast it actually happens especially like
I said if it's a background process.
Now here we're going to build our first
agent. Now for those of you that when we
talk about agents there are no tools in
this agent. So it's actually just a
request but just the foundation of the
agent. We're giving it a system prompt
so it knows it role when we do give it
to us later on in the course. But right
now we're just giving it a single prompt
and we're giving it a role as system as
a solutions architect agent for Akami
and you can see that it was able to
generate the response.
Now, this response pretty fast. It
works. But then the question is,
if we're trying to do this at scale or
we're trying to build an agent that
does more than just take it take a
prompt and generate a response, it may
need to make multiple tool calls, right?
So, that's when you start to think about
things like the KB cache. You start to
think about how much context because
when we started talking about that KB
cache, that's actually how much context
you can actually fit on that GPU, right?
And so with continuous batching, what
happens is you send a prompt to the
model. Well, you may have 100 users
trying to send prompts at the same time,
right? Well, continuous batch, they're
all going to be different sizes. So, a
smaller GPU can actually handle a bunch
of requests if you're using some with
something like VLM. Now, if you're using
something like Olama, you'll see you'll
get throttled a lot faster because it
doesn't process those requests the same
way. But VLM actually handles that with
theiruler
a lot better.
And so here we're going to set up our
our our
agent and invoke it and we're going to
actually going to look at the steps. Now
the code that we're using for this is
inside of common and you can actually
look at all the code that we actually
are importing that is custom code. So
here we have this foundation.py that
allows us to do some measures
measurements from with Prometheus from
VLM right we can look at those metrics.
Now speaking speak speaking of metrics
you can use Prometheus and you can use
graphana right at home I always use
graphana also when I'm building my
agents outside of just looking at the
metrics another thing that I always
build one of the first things I build
into my agents is observability
right lanefuse that's something I
commonly use how many of you have heard
of lanefuse now there are other tools
out there but it's open source you can
run that in your cluster as well right
beside your agents and then have access
that now your observability is private
as
Right? And you can see every step, every
trace, every span in your agent with how
many tokens, what was the latency, not
just from the time the first token, but
for every tool call, right? If you're
trying to troubleshoot or you're trying
to evaluate now, you can see all of the
latency steps in the spans. But then you
can see, okay, I'm using a smaller model
and it's making way more tool calls.
It's taking way more time than it
should. Why is that? Well, that's where
evaluations come in and OM will talk
more about that. But it's important to
have that visibility into your agents so
you can understand when you're using a
smaller model how to optimize. And that
could be something as simple as a prompt
removing tools or making the agent just
a little bit more specialized.
And so we'll run this.
And so we're looking at the steps. We're
going to look at the max tokens
and we should see the time to first
token. So you can see as we increase the
tokens,
what happens to the time to first token
in millisecond as we increase the pump,
right? As the prompts get larger, that
time the first token takes longer,
right? So the question is what do you
optimize on? Do you optimize on the
median or the largest? Right? The one
that took the most time doing the
latency. Well, you're going to optimize
on the one that takes the most time
rather than the median, right? And then
that way you can increase your median by
doing that.
Now, [snorts] here we talk about renting
versus owning. We're going to look at
tokens. How much are being generated?
This is where I I mentioned that if
you're using bursty where you're not
using invoking a model as much with a
provider
versus if you have a agent [snorts] or
some agentic applications that are
always working you can kind of compare
that cost.
So here we generate a response just to
get those tokens. And now we're going to
actually look at the billing and compare
which one would actually be more
efficient. So, if you're processing,
let's say, 200,000 tokens per day
on a hosted bill, rent it, that's going
to be about 1,500 per month, right? But
if you're renting a GPU, that's going to
be about a,000 per month. Now, it does
matter the size of the GPU, the size of
the model, the if it actually performs
the way you need. But these are some of
the things you think about when you're
trying to compare, should I rent versus
own? You can actually do the math on
that to break that down.
And we already talked about these with
the data resiliency, you know, the
compliance, the security, the controls,
and all of those good things when it
comes to running locally. Now,
before we go, the runtime landscape, I
mentioned that we're using VLL, but you
can also use SE lane, which is good if
you're using if you have requests that
share long prefixes, multi-turn chats.
So for agents a lot of organizations are
using SG lane for that. When it come to
tensor well this is about that peak
throughput on Nvidia hardware. It really
specializes in providing you that and
then llama CPP for that edge that that
really fast processing. It can help you
with those heavily quantized models like
on the ARM server.
So we're going to invoke one more time
here
and we're looking at our client just to
verify that we're still good. We're
verifying that we can connect. We can
see the model serve and we can see the
ID and I believe I can print the entire
so we can see how that require that
request actually looks when it comes
back. So I'm going to print this whole
thing as well. So we'll
and now you can see and actually let's
pretty print it. So we can see it even
better.
There we go. And so when that request
comes back, you can see the ID, you can
see the max model length, which the that
context length. You can control that,
right? You can tweak those parameters of
course when you're working with a model
but we can see everything about the
model itself.
Now we're going to move on to the next
session. Um this will have some taking
it further when you can explore the
cluster explore vm you can feel free to
do that in this
notebook. So I'm going to close that
out. We'll discard that and we'll move
on to units and memory.
Now the next section and I'm g kind of
go faster so Omar can has some time. Now
when it comes to units and memory, we're
going to talk about the ceiling when it
comes to token per second on using a
model. We're also going to look at the
model's real config and understanding
how a model actually is sits and how
actually looks um when it comes to a
GPU. So here, like Omar mentioned, we
are using and I'm going to make that a
little smaller. Let's see if we can get
more of that on there. All right. So
when we talk about the the model
actually sitting on the GPU, you have
the model weights for the 4 billion
parameter model, that model weights at
BF16 is going to be 8 gigs. So we have 8
gigs and the rest of the room is going
to be for KV cache. Meaning how much
context can you fit on that GPU? because
it all has to fit within there. Now,
when your prompt comes in, when we talk
about prefill, the model is going to
read that entire prompt and store it in
the KV cache. And then every time it
generates a new token, it's going to
update that prefill. So, that prefill is
going to grow, right? So, just because
your your your prompt that goes in is
one size, as it goes through and is
processed through the model, it's going
to increase as it generates, right? And
then imagine the tool calls, the system
prompt, all of these go to the model and
all of that has to fit on the KV cache
in order for it to be able to handle
your request efficiently.
And so we're also looking at um if we're
using at FP8, which is going to talk
about quantization and what that
actually looks like to shrink a model
and to still get the efficiencies that
you're looking for.
Now we're going to install our
dependencies
and then from here we're going to
connect to
verify what we have loaded. So again we
have the Quinn 3 4 billion parameter
model our workshop namespace the cluster
API key.
Now when it comes to models we have the
config.json JSON like what is actually
that file when you download a model you
get the config.json let's say you go to
huggerface you download a model you're
going to get a collection of files all
of those files are needed right you're
going to get the config.json JSON you're
going to get these save.tensors tensors.
Those tensor files are the model
weights, right? But the configuration is
what tells VLM how to handle that model,
right? So you can actually look at this
and explore those files to understand
what they actually look like. So here
we're showing what that configuration
file looks like. So we have 128 layers.
The size is 1,024. The attention head,
there are 16 attention heads. The values
are eight. Vocabulary size, right? How
does the model train? What is the
vocabulary size of that ma model? Right?
You can actually look at these
configurations. Can you modify them?
No. Right? These files cannot be
modified. But you can fine-tune. Right?
You can use lower. You can do all these
things to adapt the model. But to modify
these files, if you try to do that, it's
just going to crash. It's not going to
load.
Now here we're going to look at the
bytes per weight and where it comes from
and we calculate here we're looking at a
smaller model at BF-16 for the 6 billion
parameter model and the parameters you
multiply by two 1.5 gigs and for the 8
billion parameter models what those
params look like and it's gonna be eight
gigs
and if we compare the BF16 versus FP8
Now, when we talk about pre precision,
most models when they're trained,
they're going to be at sometimes FP32,
but you'll often get it at FP16. Full
precision, meaning that you multiply
whatever the model size by what? Four by
four, right? So, this 4 billion
parameter will be 16 gigs at full
precision, right? on your GPU when you
quantize it down to let's say FP8
well you kind of lose a little bit
capabilities of the model but not much
right but that's when you start to
evaluate right if your compute
constraint you have this larger model
maybe 70 billion parameters that maybe
you can do it at FP8 or maybe with int4
right all the way down to where now that
70 billion parameter models is rather
than 32 is 16 gigs, right? If that's
possible, right? I don't know how much
you're going to lose for the position,
but you'll have to evaluate that. And so
evaluation hardnesses are important.
So we'll look at the GPU where the
weights live.
So here BF16, you multiply by two, FP8,
you multiply by one. We're looking at
this for Quinn. And then we have another
model that we're going to use in this
course where it's say at 8 billion
parameters is five gigs on the GPU which
you can see how much you save with the
still intelligence that works for the
use cases that we're discussing if you
decide to quantize down.
So we're looking at this card the
gigabytes per second. you take the where
we're actually calculating. Okay, we
know how the speed of the GPU is 360 and
we're showing how to calculate to get
the tokens per second and where we're
actually bound. So, we're going to be
bound by the speed of the actual GPU on
how fast it can go. And we're showing
the math for the KV cache here. And I'm
trying to go a little faster so we can
get into the quantization and
optimization.
But if you go through these, you can
read through it and understand how the
KV cache formula works. Oftent times we
may not have to go through this and
figure it out, but you will have to when
you're trying to calculate, for example,
you have a 100 users you want to serve.
You have a smaller GPU. The question is
I got this smaller GPU. Let's say I'll
give you a perfect example. I had to do
a workshop and I had to figure out how
to serve 80 students and perform
inference for all the students with
about three or four GPUs that were about
20 gigs, right? Do I need that many? Is
it going to fit? Well, how big is my
context for the workload? What if
everybody is invoking at the same time?
Will the GPUs will the cluster support
that? Will continuous batching work? So,
you set up an evaluation to evaluate the
entire workload and to determine, okay,
is it going to fit or do you hit that
roof line, right? Do you have start to
have spill over the CPU? These is your
application slowdown
or the memory weights memory budget
versus KV pool. So we'll look at that
and then here's how you can actually get
that the math. So here's our we can get
37,000 tokens on this GPU right on the
Sega GPU this 8 gigs for the model
weights. And then the room that you have
is going to be 37,000 tokens, right? And
so if we have multiple users sending
requests, right? Well, this will show
how many users in their context list. So
if we have four users, they can all send
8,000 tokens, right? For input output
tool calls, this going to add up to
8,000 tokens at the same time on that
GPU.
And now we're showing the tax
as this increases
the different requests and the
generation of that request.
And this kind of shows how to do that
math when you're trying to understand
your compute constraint, your GPU, and
then the workloads that you're
performing. So you can take all this
code and apply it and be able to
take your use cases and do the math on
it so you can see if it fits on your
GPUs.
So we
will go to the prefill and decode. So
going a little bit deeper into the
prefill and the decode in the KV cache.
Again, we're using the Quinn3 model, but
we're actually going to dive in to see
how this looks. So we have the prefill,
which like I mentioned is going to be
focused on that time to first token,
right? from the time you press send, how
long does the first token, if you're
streaming, right? Because if you're not
streaming, you're just going to get the
whole response back. But if you're
streaming, how long does it take to get
that first token back, right? And that's
going to be that prefill stage.
And then the decode is going to be that
token, every token after that, that's
all measured. And if you're looking at
the metrics inside of VLM, you send that
to Graphana, you can actually view that
on the dashboard and you can watch,
okay, as I increase my prompts, you can
watch it increase, you can watch it
decrease, right? Right. And really
understand what's actually happening on
that GPU when you're sending requests.
So, we'll go through here. We'll install
our dependencies.
Then from there, we'll look at our
environment. Make sure we're connected.
Yes. And we're still using the Quinn
34B.
And we're going to look at the self
attention, meaning how does that KB
cache get processed. So this is the
actual formula. So you can look at that
soft max to really understand how that
KB cache is being handled within a
model. We're just doing it by hand just
so you can see the math on that. And so
when it comes to the KB cache, there's
the naive approach and there's the KB
cache approach that I would say is
handled. So the naive approach is you
take a prompt, the model looks at the
whole prompt and then one by one stores
that prompt in the KV cache and
generates a response. What KV cache
does, it says, okay, I'm gonna take the
prompt, I'm gonna learn from it, and I'm
gonna store it right in parallel. And so
the KB cache allows you to learn from
the prompt to be able to reference the
information rather than just doing the
fixed sequence of the naive caching
approach when it comes to handling that
KB cache. And so if we generate this,
[snorts]
we can look how it computes
the reduction of how much if you use the
KB cache approach
rather than the naive approach and we're
just showing all that by hand in code so
you can really break it down and
understand. And now we're going to look
okay using K KV caching and we'll
measure the time to first token.
And so here we have 57 milliseconds and
then the decode was 25 milliseconds.
And so we'll continue on
and we can see what VLM is actually
exposing. So we can actually look at
those metrics and we're just showing
some of the metrics that are actually
being exposed and how you would view
that in VL.
Now we're going to invoke the prompt and
we're going to increase it and you can
watch that KB cache fill
and you can see this is going to take a
little while. So we'll give it a couple
minutes while this process we're
increasing it. So we can see the KB
cache usage and we can look at the
metrics. So we have peak usage running
and then the KB usage after it's
finished. And this will be the math on
how you would process that. Again the
worker that we're using for this code is
in the foundation.py.
So that's going to be the helper for
this code.
Now we're going to look at the warm the
code um against the warm prefix caching.
Now preface caching is an interesting
thing. Um don't confuse it with prompt
caching for and that's something I
should have mentioned before. If you're
using a provider and you're paying by
the token, prompt caching, especially if
you're do you have a continuous
application that's running within every
five minutes, prompt caching is a must,
right? You can you can decrease the cost
by like up to 75% depending on who
you're using. So there is some ways you
can use a provider and save on cost. But
when we're talking about prefix caching,
this is caching that prefix for the KB
cache. And so when we do this, we can
see how this actually is handled
here. So the code is going to be 220
milliseconds
and it's down to 41 milliseconds. And
this all shows you how to do that in the
code. So you can go through that. And
I'm trying to go a little faster so Omar
can get to his part and hopefully we can
deploy.
All right. So we'll go back and we'll go
to the fourth section where we talk
about dense model verse the mixture of
experts on the GPU.
Now when it comes to a dense model, what
is a dense model? Well, a disc model
when it sits on a GPU, that whole model
is used to generate tokens, right? So,
if it's 30 billion parameters or let's
let's just do the model we're using now.
So, the Quinn 3 4B at BF16 8 gigs on the
actual GPU. Well, when that actually
generates tokens, when it actually is
working, that whole entire model is
working, right? So it's going to be a
little slower than if you use a mixture
of experts. Mixture of experts may be a
larger model. Maybe it's 30 gigs, but
when it actually generates inside of the
model, it takes a collection of experts
and only that that section of experts
does the generation. So even if it's 30
gigs, it may be 1.5 gigs just to do the
generation. So it's going to be a lot
faster. So that's one of the benefits.
Even though it's a larger model when
it's a mixture of experts, it's actually
a can be performed a lot better within
an application or a lot faster within an
application.
And so here we kind of talk about memory
and why decode is memory bound meaning
that when we talk about the generation
phase after that time to first token
when that generation actually happens
that's actually going to be bound by the
memory. So when we looked at the speed
of this GPU that's bound, you can't go
any faster than that, right? There's
nothing we can do to tweak that to make
it go any faster. But there are some
things we can do to help this at scale.
So we're going to look at our roof line
and plot that so we can actually see it.
So we'll make sure that we have our
model loaded. So we had a quint 3 for
billion parameter, right? and it's going
to be compute bound. So it's going to
hit that roof line. So we're going to
look at the flops. We're going to look
at this. So the ridge line is 297 flops
per bite, right? And where this is bound
by the memory.
Now if we look at the mixture of
experts, now we're just going to look at
this as code. So we can actually
understand it.
So at this 30 billion parameter models,
right? 128 experts and only eight active
per token. That's 48 layers,
248 hidden. And so now the expert mixer
expert, this is the weights. This is the
share weight. So this is how much it how
much is being used when it generates.
That's a lot that would be a lot more
efficient than using a smaller model. It
can actually be faster when it actually
does the generation.
And so here we're looking at the the
dense model, right?
is nine times fewer bytes than a dense
model, right? So it decodes a little bit
faster. So that's kind of breaking down
the two when you're actually trying to
figure out, okay, do I want to use
something like Mistro, right? Or do I
want to use like a Quinn model,
we compare the dent sizes.
So here we're going to look at the rate,
we'll look at the bandwidth, the GPU
serve. So measured Quinn 4B is about 40
40 tokens per second, right? The smaller
model of the Quinn, the 0.6. Now, this
isn't done on the CPU, but we're just
showcasing 300 tokens per second, right?
But we're looking at the ceiling. This
is actually looking at the bandwidth and
it's doing the math here to get that the
max that we can get. The ceiling that we
have on this GPU is going to be 45
tokens per second.
Now, if we enable reasoning
on that model and we can look at that.
Now, when it comes to these Quinn
models, if you're wanting to do any type
of agent and the model needs to reason,
meaning that maybe the prompt comes in,
you have tools and it needs to make
multiple tool calls. Well, you're going
to enable thinking. So now when it makes
a tool call, if it gets the results and
it needs to make another tool call or
verify the results to make the accurate
tool call, you're going to have to
enable thinking on these models. And
that's just a parameter that you can
adjust in the model, right? But with
thinking off, it just generated a
response. It was 35 tokens. But with
thinking on now, it had to think about
it. It cost about 600 tokens. Right now
with some of the models like provider
models you can actually set a token
budget for life of thinking. So that's
one of the things you can save on cost
with a provider model and maybe some of
the open models you can do that too. I'm
not sure.
>> Yeah, you can.
>> Yeah, you can also adjust that token
budget on the thinking as well. So more
tokens on thinking isn't always good but
sometimes it can help the model better
troubleshoot and better get to that end
result that you're looking for.
And so when we talk about inference,
there's a lot of things to think about,
but one of the things we want to think
about is that memory bound limit for the
actual card and then how to apply that
for the agent. So we look at all of the
modules, we talk about that KB cache,
the prefix caching, the attention heads
as well as quantization which um is
going to cover here in a minute and then
from there that continuous batching we
also discussed that. So if we split the
prefill from the decode, you have the
prefill GPU pool and the decode which is
memory bound. So the prefill compute
bound, right? So it needs to go from
your memory to the GPU and it needs to
be cached, right? There's
[clears throat] that that phase you can
you can do a lot of optimizations, but
when it comes to the decode phase,
there's nothing you can really do
because you're bounded by the GPU. And
so we kind of show this in code rather
than actually showing it because again
we [snorts] only have so much limitation
in this workshop.
Now with that being said I am going to
make sure that we are good to go here.
Um I don't think I need to switch the
mod. I think you should be good. Armor.
I'm gonna turn it over to you.
>> All right.
>> And then Yeah, we should be good to go.
You can talk about quantization. Thank
you.
>> All right. Thank you, Dwan.
>> Yep.
>> All right. So, let me close that. Sure.
>> That That's yours, actually. There you
go.
>> Okay. Cool. So, I'll be talking about a
whole different um uh optimization
techniques I think you can use to deploy
these models on Kubernetes. Um, like I
said, uh, my background is in
Kubernetes. I develop a lot of
Kubernetes stuff at Akami and I work on
the manage Kubernetes platform there.
So, a lot of the stuff that we do is we
want to make sure that we're able to use
GPUs on Kubernetes really well. Uh, use
all the different features that they
have. Um, and uh, we deploy a lot of
these models using some of these
techniques that I'm going to be talking
about. Um, so there's uh, different
techniques. So, we're going to talk
about quantization. I think this one's
like the main big one. Um, it's super
important. We're going to talk about
speculative decoding. Uh, this is a
pretty cool technique. It can give you
quite a big uh performance boost in your
uh throughput. Um, we're going to talk
about um like how do you uh you know uh
tweak your LM uh VLM config to make sure
that you're getting max performance out
of it and um you're meeting your SLAs's.
And then we're going to actually do some
tuning and evaluating. So this I'm going
to leave you guys with some sort of
framework that you can use to figure out
what exact configuration you need to use
for your specific workloads and specific
use cases. Um so I'll dive into
quantization.
Um let's see. And if we have time, we
can definitely go uh we can have like a
quick Q&A as well, but I think we have
30 minutes. I'm going to run through it
uh
at a good pace. So in quantization um
there's a whole lot of different uh
there's a lot of different types of
quantizations you can do. Um you know
there's the BF-16 the the one that the
model is going to start off with. That's
the full precision model that uh Quint
provides you and then there's a lot of
other conversations on top of that.
People have created FP8 that's one of
the models that we're going to look at
in this particular module. Um there's
INT4. Uh there's AWQ GPQ uh GPTQ. These
are different types of uh ways you can
quantize the model. Um there's NVFP4
which is Nvidia's proprietary
quantization technique that they use. Uh
it's hardware accelerated on black hole
GPUs and more. Uh that one is pretty
cool. Um but let's see. Let's dive into
it. Um
make this
hopefully we can fit that in there. All
right. So as you can see, you know, like
if you have the BF16 weights, it's going
to take a lot of your memory. Uh in this
particular use case, we have 20 gigs of
VRAM and we sort of want to maximize how
many requests we can serve with these 20
gigs. Uh so we want to make sure we have
enough space for KB cache. Uh reason
being the more requests uh the more KV
cache you can have on the memory, the
more requests you can process in
parallel. Uh thereby increasing your
throughput. So that's super important.
Uh so that's why we essentially want to
do quantization. We want to reduce the
size of the model so that way you can
fit more KV cache and essentially
increase your throughput. Um so that's
one reason. The other big reason I think
is also because you're shrinking the
weights essentially by in half. You
don't have to do that memory movement
between the different uh memory
hierarchies resulting in essentially
faster decode as well. So we will see
you'll go from you know 40 tokens per
second which is the base model will
probably go up to like 60 tokens per
second if not more. Um so let's look
into this. Let's um
install the dependencies
and then I'm just going to make sure
that the model is still available and
everything is running. So yeah, we do
have the model running uh the same four
billion parameter model and it's running
in the namespace. Again, as I said, um
sort of like a high level overview,
there's a whole different sorts of
different techniques you can do
quantization with. Um for example, like
um uh Llama CBP is a pretty popular one
for running a lot of these models at a
lower precision. Uh that uses GGUF
format. Uh that format is pretty cool.
you can have um uh you know five bit,
3bit, two bit, one bit quantizations
which is pretty interesting um and
pretty cool but the the downside of that
is you lose a lot of uh you lose quality
trying to get a lot of performance out
of it. So, there's a trade-off there.
Um, but for the most part, going from
BF-16 to FP8 is a very negligible drop
in quality and performance. Um, and it
will result in more performance while
keeping the quality exactly the same.
Uh, so that's what we want to showcase
and that's one of the assumptions we're
making. Obviously, like when you're
doing this for your particular workload,
depending on what you're using it for, I
highly encourage people to have their
own evals. uh me so that way if you're
switching from you know BF-16 your eval
are saying okay everything is good
everything's running well for our
workload you switch to FP8 you might
have issues where some things are
breaking here sometimes it's
hallucinating sometimes it's going in a
loop so a lot of those things can happen
for very specific use cases and in those
scenarios it's very important that you
have your own eval set and you're
running your own evals to make sure any
changes you make um are uh okay to make
and also you don't have any degradation
in performance
Um again we'll run and make sure that we
have the BF16 base and then we're going
to measure the performance. So uh we
have a little load test uh utility
package that we use to do some uh
testing. Essentially what we're doing if
you look at the levels where these are
like a at different concurrencies we're
making this request. Each request is
going to have about 256
tokens and the output is roughly going
to be about 128 tokens. So this is sort
of trying to simulate how many requests
you can process at one time and we're
sort of going to use this as a baseline
to see what the baseline performance is.
Um so for 32 uh we're getting aggregate
performance of 714
tokens per second which is pretty good.
uh at single concurrency we're getting
37.5 tokens per second. Uh so that's
important to uh note down. And also
we're getting um
uh 61 milliseconds for time to first
token. And then you'll notice the time
to first token goes up, right? Like the
jump between 32 and 64 is quite large.
We're going for 277 milliseconds to uh
1300 milliseconds. That's a quite a big
jump. and you might not necessarily want
to make that trade-off, meaning you
might want to potentially stop at only
32 uh concurrent requests that you're
processing and not go higher than that.
So that is an important thing to notice
there. Um again as I was saying um eval
are extremely important. Uh reason being
again you can have performance
degradation when you do quantization and
you can lose uh some intelligence
reasoning can uh not work as it should
there there's going to be a lot of
issues. So you want to essentially I'm
kind of simulating here like a uh at a
very basic level what kind of eval you
might want to think about. Um, you know,
you want to think about like if the JSON
is being generated correctly, if the
JSON is being corrupted when you reduce
the quantization, you know, at uh BF16,
you might have good uh responses, but
when you go to FPA, maybe potentially
your functions function calls are
failing. Why is that? It's probably
because it's not generating the JSON
correctly. So, there's a lot of these um
eval cases that are already out there
that you can kind of use in the open
source. Hugging face has a lot of evals.
You can go on GitHub, you can find a lot
of these, but you want to come up with
your own for your own use case. Um,
but then so next thing what we're going
to do is we're going to switch from BF16
to an FP8 model. So we are going to
essentially reduce the size of the model
in half. And once we do that, we'll kind
of get to see um what the performance
differences are and are they worth it
and are we losing any quality over it.
Uh so to do this uh you will need to be
in the root and then click on manifest
and in there you will see vlm.yaml. So
um
I'll kind of go over this. So this is a
typical manifest uh configuration file
that you uh uh have for Kubernetes
deployments. Um how many of you have
used Kubernetes before or have knowledge
of Kubernetes? Okay, quite a few. Okay,
great. So this will be quick. I don't
have to go over all all the details, but
essentially we have um a PBC which is
going which is essentially our cache
where all of our models are living and
we have a simple deployment with VLM
with a lot of different arguments and
flags here. Um so you can see we're
using the Quen uh 34 billion parameter
model. Um, and then we're going to
switch it to
this FP8 version from Red Hat. Uh, let
me
one more quick thing I want to quickly
mention is you see the dynamic at the
end. Uh, this is pretty important. This
means that not everything in this model
is quantized to FP8. In a lot of cases,
in a lot of different quantization
techniques, you might want to quantize
the model uh only specific parts of the
model and not the others to make sure
the performance stays the same and you
don't have a lot of uh issues there. So
that's one of the reasons why you'll see
dynamic, you'll see all kinds of things.
You'll even see quantizations where
certain heads of the model are going to
be 4bit and then some are going to be 8
bit and some are going to be full
precision. And you know, it's it's sort
of uh interesting that people are doing
that and finding a lot of performance
there. They're they're finding the
performance gain while making sure the
quality stays the same. So once this is
uh changed, we're going to save it and
then uh we'll just quickly go through
and run it and apply it. So this is just
making sure that the diff is good. Um
we're not causing any issues here.
Uh that should be fine.
And then we'll just go ahead and where's
apply? Right here. We'll just go ahead
and apply and that'll roll out. Um it's
gonna take uh a little bit of time. Let
me save that. But another thing you guys
can also do is you can open up a
terminal tab as well. Like if you just
click on the plus sign and then you'll
see a terminal option and then that will
also let you see sort of like what's in
your nameace and what you can do here.
So if you get you see the VLM endpoint
is still coming up. Uh this pod is
essentially your Jupyter notebook
running within your namespace. Um
let's see this will take a little bit of
time to come up.
Yeah. While this is coming up, does
anyone have any questions? We can
probably have one question in
>> cont.
was pre-quantized already.
>> Yes, it was pre-quantized. Yeah, you can
quantize your own models. There is LLM
compressor. Uh it's uh it's provided by
VLM, I believe. LM
compressor.
So there there there is tooling out
there for you to do this on your own if
you would like. Um, but yeah, the one
that we're using currently is already
pre-quantized that we downloaded off of
Hugging Face.
All right, I think that should be up.
Again, it's taking a little bit of time,
mainly because it's taking all the
weights out of the VRAMm and loading the
new weights in. So, it's going to take a
little bit of time to do that. Um,
anyone else have any question?
I'm sorry.
>> Look at your your VL your YAML file for
your arcs. Look Oh, looked like they had
uh two flags on the model.
>> Oh, they did. Oh, that's a good call
out. Thank you for that.
Did not see that. All right, we're going
to go through it again.
Let's rerun that.
Okay, that's probably why it didn't come
up as quickly as it should.
Oh, I can't do that.
All right. Any any other questions while
this is going through? Go ahead.
>> How do you choose between?
>> Uh, how do you choose between FPA and
intake? Uh that's a good question. So it
depends right like int 8 is going to be
slightly less precision than FP8. That's
essentially the reason. Uh the the
difference is like FP8 is floating point
so you get a little bit more precision
out of it. Uh and then int8 is integer.
So you could use either or. Uh again
these are all the other options that you
have. You can choose based on your
workload and where your constraints are.
Um but yeah you could totally go into
eight as well and it should be fine.
Um, where does it say that?
>> Good.
>> Stack. Oh, yeah. I mean, uh, oh, that's
the other good good call. Um, it depends
on the GPU as well. Some of the GPUs
might not necessarily support it.
>> GPU support.
>> Yeah. So, GPU support is important.
That's another good call out. So some of
the um uh GPU might support it but it
might not be accelerated by the GPU
meaning you might not get the full
performance that you would be expecting
out of it. Um for example the GPUs that
we're using we're using RTX 40008 they
support FP8 and we're going to get the
full uh precision uh full performance
out of it and it's able to hardware
accelerate all those calculations. But
if we let's just say use FP4, it won't
be able to do that and we would actually
not see a whole lot of performance gains
and we actually see performance go down
instead of it going up. So that's
another thing to keep in mind.
All right. Where is it?
All right. It has successfully rolled
out. So we'll uh take a quick look. So
now we can see it's actually using the
FP8 model now. And then we'll also kind
of quickly go through and do another
load test. It's going to be the exact
same. We're going to do it at uh
concurrency 1 uh four 8 and uh 8 16 and
32 I believe over here. It's going to be
exactly the same. So
and then once that is up we can compare
and see the performance differences and
why you would want to quantize.
Okay. the performance is in. And if we
compare it before and after, you can
see, let me make this a little bit
bigger. Uh, you can see even at
concurrency one, you know, we're going
for 37.5 tokens per second to 53.4
tokens per second. So, we're seeing
considerable jump in performance here.
Um, and then at peak throughput, we're
seeing uh at 64 concurrency, we're going
from 800 to,40. So, that's about, you
know, 1.4 four uh 42 times uh which is
quite a big performance jump but again
keep in mind the time to first token is
going up considerably as well uh
compared to 32 and 64
um but then yeah you can and then again
you want to run evals um we can quickly
run through this and it probably won't
have any differences so yeah again BF16
versus FP8 um there's not a whole lot of
uh performance degradation you should
spec it's it's going to work out of the
box for the most part but uh for
specific use cases it might not but for
simple eval cases that we had here it's
it's working fine
I think that is it for this module where
we'll jump into next is speculative
decoding which I think is a pretty
interesting one um let's see
let's jump in here all right so how many
of you have heard of uh speculative
decoding before
right quite a few people that is good.
Uh for those who don't know what
speculative decoding is, let me make
this smaller. Um it's essentially we're
using another draft model which is going
to be a much smaller model than the main
model that we're using and it's going to
generate multiple tokens ahead of time
and then our main model which is the
four billion parameter model is going to
look at those generated tokens and it's
going to either say it's it looks good.
That's it's going to verify it and say
it's going to look good or it's not
going to look good. Uh so in this like
diagram you kind of see like um the
draft model you know generated four
tokens ahead of time and then the
verifier model which is our four billion
parameter model is going to say oh only
the first and second token make sense
the other two don't so it's going to
discard it and it's essentially going to
do this each time it's generating new
tokens. So it's going to go in in a loop
there. uh and uh for for this uh
workshop we're going to be using the 6
billion parameter model uh from Quen as
a drafter model and see if that is going
to either help us or not help us in a
lot of cases uh it can also not help you
and reduce the performance um and
there's multitude of reasons for that
and we'll go into that shortly.
How are we doing on time? Good.
uh just make sure we are good here
target model.
Okay, before we get into it, I also want
to talk briefly about all of the
different ways you can do um speculative
decoding. Um there's a lot of different
ways and there's more ways coming out uh
every every few months. Uh but the you
know the draft model is one way. Um, a
lot of times, uh, a lot of new, uh, ways
of doing it is actually using a
diffusion drafter model, which I think
is really cool. Uh, I personally use
that for one of my home lab machines.
Um, and, uh, that gives you a huge
performance. The difference between that
and this is because it's a diffusion
model, it's going to be generating a lot
of tokens uh, at once, uh, rather than
doing what we do sequentially with LLMs.
Um, and then the verifier model is able
to verify X amount of tokens out of
that. Um
but but yeah there's a there's a lot of
different types of uh methods you can
use. You can use suffix decoding. Uh
there's a lot of times model would come
with a built-in drafter model as well.
So those are like the native models that
are trained along with the main model.
Uh so you don't have to uh import
another model to do this. Uh there's
medusa eagle again like diffusion dlash
is a big one that uh has kind of been
going viral and it's working pretty
well. So there's a configuration you set
for figuring out how long like how much
it generates before the verifier comes
in and verifies it. So you can set that
you can set it to two tokens, four
tokens and five tokens. And it's
important that you set it correctly uh
because if there are
for example let's just say you set it at
four and uh the model verifier comes in
it's like okay I only accept two that's
50% acceptance rate and that is pretty
bad. that's actually going to have a
negative impact because not only are you
running you're running two models so
you're spending compute to run two
models and then you're only getting 50%
acceptance rate and that's essentially
going to result into a decrease like
throughput. Uh so that's not something
you want. Um so that's something you
have to like kind of tweak and play
around with and see how many tokens do I
want to generate ahead of time. Um so
yeah technically you could generate 15
tokens but you probably don't want to do
that. You probably want to do two maybe
three maybe four. It also depends what
type of um
what's it called? Um let me go back.
Where is it? What type of method you're
using again? Like uh I use deflash uh
for a lot of my home labbing. And uh
that works pretty well if I set it to
eight. And if I set it more than eight,
I actually get a lot uh a lot less
acceptance rate and that causes my
performance to go down or be very flaky.
Um
but all right so we will next um
>> you got one more question
>> one more question. Hey uh sorry
uh this is from the last module but uh
how does dynamic uh compression work uh
in a sentence or two I guess
>> um so the way it works is if you do you
understand um the different heads of the
model uh different because there's
different layers within an LLM. So if
you look at the model.json JSON, you'll
actually see there's a lot of different
parts to an LLM and there's a whole
pipeline that sort of like pushes the
tokens from one thing to another. And a
lot of a lot of times when you see a
dynamic thing, it essentially is saying,
okay, I'm going to only quantize uh the
attention heads to FPA, but I'm going to
leave everything else as is.
>> I see.
>> So, so that's the reasoning. And if you
remember from previous modules, you you
saw that the FPA version is not exactly
half in size. It's not going four
gigabytes, it's like 5.1 gigabytes.
That's because not every part of the
model has been quantized to FPA. So
that's like sort of the dynamic part of
it.
>> See, is the same math applicable to all
the models or it depends model
>> depends model to model. Every model has
a different architecture. So
architecturally speaking, it depends you
know what parts of the model you
quantize. uh there's people who quantize
you know some parts of the model to uh
in4 but leave other parts to FP8 and
then leave some parts to like BF16. So
>> thank you.
>> Yeah.
>> All right. We'll run through this again.
I'm just confirming that our baseline is
good. We're using FP8 model here. Um and
then uh we'll do another load test
quickly um sort of to get another
baseline of um what it would look like
before we implement and add speculative
decoding uh to this particular
deployment in VLM.
And then while that is running, I'm just
going to make sure uh to
uh let me actually copy this correctly.
Not that.
Oh, never mind. You can just so in here
um we are setting the speculative
config. This so this is a particular
flag you can pass in VLM to set the
draft model. So we're setting it to the
uh 0.6 billion parameter model. And then
we're also uh setting how many tokens do
we want to generate as draft tokens. So
in this particular scenario we're
setting it to four. Again this is
something you have to do a lot of
testing on. Uh you have to try out do I
want to set it to four? Do I want to set
it to two? Do I want to set it higher?
It all depends on the acceptance rate
and uh how much performance you're
getting out of it. Um and then yeah once
you set this flag and we will redeploy
this. Um we go back in here. We got our
baseline.
And then let me make sure that it's
good. Okay,
things look good here. And then we'll go
ahead and um apply and roll this out.
And this is probably going to take
another couple minutes. So, uh does
anyone have any any questions? Go ahead.
Oh, one second.
>> I I noticed that you set the GPU memory
utilization to 7
>> which leaves a lot of your um
essentially leaves 30% of the VRAM
>> unused.
>> Is there any particular logic to that
choice? Uh in this particular scenario
um there could be a lot of reasons. Uh
sometimes you know you might have
multiple deployments on the same GPU and
you want to make sure that you have
enough RAM for something else VRAM for
something else and then you keep enough
VRAM for this but in this particular
scenario not really. We're going to bump
it up in a following module actually. Um
it's it's one of those knobs right like
you have to keep you have to make sure
that you're setting the utilization
correctly. If you set it too low, you're
leaving performance on the table. If you
set it too high, um you're going to um
kill your node, and that's not good.
>> Yeah. So,
this
>> Okay, it's still coming up. This is
taking a little bit more time.
>> Go ahead.
from
>> sorry one second
>> uh the bump that we see from 60 32 to 64
parallelization it's because of the key
value cache just blowing out or I mean
>> yeah yeah essentially the key value
cache is blowing out and it sort of hit
like its max limit and it can't go above
that uh so there's a lot of reasons so
there's that part and then there's also
uh the continuous batching and a lot of
times times will happen if if you don't
if you set the configuration to a level
where the continuous batching is not
optimal, it can also cause you to see
like high tokens per sec. Uh
uh you can see high latency there as
well. Um but yeah, in this in this
scenario, we're essentially hitting like
sort of like a ceiling on us uh uh for
us in terms of how much VRAM we can use
there. That's why we're seeing that.
But in the following modules, we'll see
how we can improve that scenario and
hopefully like make it better.
Uh, okay. All right, we're rolled out.
So, we now have speculative decoding uh
set up correctly. So, what we'll do is
we'll do a quick load test again. It's
the same exact test that we ran up here
where, you know, just keep in mind we're
getting 58.2 tokens per second for
concurrency one and then 42 milliseconds
of latency. So this is our sort of
baseline before we do speculative
decoding. Um but what I want to showcase
here is not a happy path where you will
automatically get a crazy improvement in
performance. You'll actually see the
performance went down drastically.
You're seeing 16% uh 16 tokens per
second whereas the baseline was 58. Um
and then even the time to first token is
sort of going uh up a little bit as
well. uh and you know we want to figure
out like why is this happening?
So there's a there's a big difference
and there's a big uh decrease in
performance like even if you look at
concurrency 16 we're going from 700
tokens per second to 240 tokens per
second. So that's a considerable
decrease in our performance. So the way
to interpret this is there's a lot of
different reasons. Um one is again as I
was talking about earlier it's the low
acceptance rate. uh if your acceptance
rate is very low and the verifier model
is just it's going to keep rejecting
those tokens that are generating by
draft model, you're wasting a lot of
compute to generate those draft tokens
and then the verifier is coming in and
then saying hey I don't want to take
this work like this is bad work. Um, so
that's one. Um, it could be because we
set the speculative tokens too high,
meaning in in our current config, we set
it to four. Maybe we need to set it
down. Uh, and see if that actually helps
in improve the acceptance criteria or
acceptance rate. Uh, there's a lot of
things with theuler as well with VLM.
Uh, depending on how it's scheduling
these requests in, uh, that could be
leaving some, uh, performance out on the
table. So, it also depends on
compatibility and things like that. Um
and then yeah again same GPU contention
you're using the same GPU uh to do this
work. So it could be uh resulting in u
the resources not being used correctly.
Um so in a lot of cases usually this
works but in our scenario it didn't
work. Uh the main particular reason for
that is um this particular
drapher model is not trained correctly
for this particular model. So that's the
reason we're seeing a a very very low
acceptance rate. Um so when you are
doing this for your own models and for
your own deployments, you have to make
sure that the model, the draft model
that you're using is going to be
compatible with the model that you want
to use it for. If you don't do that,
you'll run into scenario that I'm
showcasing here where like your
performance is going to tank and um
there's not a whole lot you can do about
it. I can tell you from the resource
perspective, this GPU has enough
headroom to support all of this. But the
reason for us seeing this decrease in
performance is because the the models
are not trained correctly. And uh that
is something you want to keep in mind
and test for as well. And you want to
make sure the speculative tokens uh are
set to the right uh number as well.
Um but yeah when you in your own time I
would definitely implore everyone to
play around with that number meaning
change this to from four to two to six
to one and see uh what kind of
performance gain you see what kind of
performance decrease you see and why is
that happening
but yeah that that's that is it for
speculative decoding it is actually not
going to help us in this scenario so I'm
just going to go ahead and uh comment
that out and then we'll redeploy this.
So we are back to our baseline.
>> Hey, you got one question.
>> One question. Hey. Um, so I know there's
probably some nuance depending on model
architecture, but in general from what
you've seen, is there a massive hit to
acceptance rate if you use like mixed
precision essentially like run the main
model at FP8 and then quantize the draft
model down to Q2? If I'm like really
memory constrained,
>> is it often even worth doing that? Uh,
or you know, what have you seen in
general? like does
>> that's a good question. Um a lot of
times it you it doesn't matter as much.
Um most of the time what you want to do
is you want to keep the draft model and
the main model at the same precision.
But let's just say the draft model is at
BF-16 and then the main model is FP8.
The mismatch can cause the acceptance
rate to be very low. So, and then the
the main part of it is you have to train
the draft model correctly so that way
it's able to generate the right tokens.
In our particular scenario, the draft
model was not trained correctly. Um, and
then it was also quantized down to FP8.
So, there was probably some issues with
that recipe when they trained this model
and which resulted in us actually taking
a massive performance set. Um, so a lot
of times when you when uh a lab releases
a model, they release uh a drafter model
along with it. So you want to use those
drafter models uh that come with the
model. Uh there's also thirdparty labs
that do their own drafter model. So you
can try out a lot of different options
that are out there and see which one
works for you. And in some cases,
depending on the use case, let's just
say you're using for coding, the drafter
model might work perfectly fine, but if
you're switching that to maybe some
English writing, very specific academic
writing, and it might not necessarily
work well, and you're going to see like
decrease in acceptance rate. So, it's
also uh it also depends a lot on your
use case as well. So, it's not
universally applicable.
>> Gotcha. Cool. Makes sense. Thanks.
>> Yeah.
All right.
Let's jump on to the inference side of
things. But before you make another
jump, any other questions?
Oh, yeah. I can put the YAML on there.
Um,
so the the fact that we have speculative
decoding uh presumably is because um for
for a model it's faster to verify rather
than decode.
>> Yeah. Can you just give a little bit of
mental model for like what it's what a
model does underneath the hood um to
verify such that it's faster than
decoding you know it can't be decoding
and then comparing against what the
draft model produces. So like
>> what is it doing exactly so so that it's
faster.
>> Yeah. So essentially uh when a typical
LLM is you know decoding you have a set
of vocabulary it's a huge array of bunch
of numbers and it's representing um a
confidence score for each of those items
right so instead of um instead of doing
that one token at a time when you run
with specular decoding you're running it
for a lot of you you're running the
model for parallel things. So with
continuous batching as well, you're
running a lot of different requests in
parallel. Uh so you're doing the same uh
you're doing the calculation for
everything. Uh and you're doing it at
once for a lot of different requests. In
the same way, you're doing the same
thing for speculative decoding. You're
checking the confidence score for this
uh the speculated tokens and making sure
that oh this is a high confidence, so
we're going to go for it. This is you
know 0.95 and this one is like 0.9. And
then you you accept that and then the
other ones you you know uh you reject
those. That's sort of roughly the mental
model is like you are in parallel
running uh through the layers and making
sure that each of the tokens that the
draft model uh outputs is has a high
confidence.
Yeah, hopefully that answers your
question.
Oh, one more question.
>> Do you have any examples that
>> uh yes I do. That's a good call out. Um
there's actually I left a few links in
here. Um where did I leave those?
Interpreting the results. Yeah. So
there's a lot of different uh writeups
on speculative decoding in in general.
If you do it right, you do see quite a
bit of increase in performance. Uh VLM
has actually done a big report on this
and they've seen about 1.5x increase in
token generation if you set it up
correctly with the right model and with
the right drafter and the right
settings. Um so yeah, this this does
excel. It's just a matter of getting it
right and tuning it correctly and making
sure you have the right um things in
place for it. Um but yeah, like from my
personal experience, um for my home lab,
I used the Quinn 3.6 35 billion model
and along with that I use a Dlash um um
draft model and I get roughly around two
to 3x token generation uh performance
improvement uh depending on the use
case. So it it does work. It's just a
matter of getting the right models to
work together.
>> How do you choose the model size
>> for the daffer?
>> Uh you want to you basically want to
figure out uh the smallest model that
you can run that doesn't take as much
GPU power because you the main model is
the model that has all the knowledge.
That's the model that you really care
about that has everything that you need.
But you don't want draft model to take a
lot of those resources away from the
main model. So you want it to be small
but not so small that it's dumb but big
enough where like it's going to actually
give you
>> you experimented with that. Did you see
like acceptance rates
like 3B model
>> 3B is too big. Uh the reason why is a
lot of models like I was talking about
qu 3.6 uh 35 billion. So it has it's a
mixture of experts model and each expert
is about three billion parameters. So
the experts can be around that uh and
you would get good performance out of
it. But for the draft model, you
probably want to be less than 1 billion
parameter just to make sure that it also
depends on the main model you're using I
guess right like if you're using if your
main model is like 400 billion
parameters you could probably get away
with using a bigger drafter model to
make sure that you get higher acceptance
rate. So it's you got to find the right
balance essentially. Yeah.
Cool. Um, do we have any other questions
over there? One more
before you jump in.
>> Yeah, I just had a question. How is the
draft model trained? Like is it
distillation or something else?
>> It's essentially distillation. Uh, so
you take the big model and you know you
distill all of its capabilities. You
create a data set and then you train the
uh drafter model using that. And a lot
of times actually what's there's
different techniques to do this. Uh the
other techniques you'll see is the draft
model is trained alongside the main
model. Uh so that way that's another way
of doing it and a lot of labs will
actually give you a drafter model uh
inside of the same package. So you don't
have to essentially download a second
model and run it. Um so there's a couple
of different ways of doing it. Uh but
probably the best way is train alongside
it and then that way you don't have a
lot of issues and acceptance rate sort
of stays high.
Cool. Um, we'll jump into module seven.
So, here I want to talk about some of
the different flags that you uh should
care about when deploying using VLM and
what and how you want to get the
saturation to be as high as possible.
Saturation meaning we want to get the
GPU to work as hard as possible as long
as possible. Uh, and because you want to
get your money's worth if you're renting
a GPU or if you're buying a GPU, you
want to run it uh as much as possible.
So
uh we will stop here. So uh one of the
concepts I want to talk about uh if you
remember previously we were looking at
the 34 uh 32 concurrency and 64
concurrency. We saw a steep increase in
the latency and the reason for that is
essentially you the throughput at some
point is going to flatten out and but
the uh but the latency can keep
increasing if you keep increasing the uh
concurrency. So you essentially want to
find the sweet spot and uh that is
something that VLM sort of lets you kind
of tweak and make sure that you find
that sweet spot and once you do find it
you can set the right settings for it.
Um but but essentially you want to find
the inter not so not the intersection
but essentially right before where the
throughput gets to like the flat state
but the latency is like still acceptable
enough. It's sort of like the point you
want to get to.
Um we will do a setup
and then let's make sure our settings
are all good still. Serving model is up.
Um, let me just double check if it's up.
Should be.
Okay.
And then here we're again going to get
um another we're going to do another
load test. So that way we know the data
and then we can based on that figure out
where that uh where this point is.
Essentially the we call it the knee um
where things are flattening but also the
concurren based on concurrency uh the
time to first token is acceptable. Um
once that is Oh, I think that should be
fine.
So you know the throughput is slowly
increasing as concurrency is increasing.
That is acceptable. Um and then you also
see the latency go up. That is also
acceptable but it's not going up
drastically. Uh but we should shortly
see the big jumps uh with more um
concurrency here. But while this is
running, any any other questions for
anyone?
>> Go ahead.
Oh, over there.
>> So my question was again on the previous
speculative decoding. Uh just wanted to
know based on your experience um with
like drafter model uh what kind of use
cases you have seen it to work really
like for example with agent loops with
tool call or with coding like what kind
of like use
>> uh agent loops it's really good at tool
calling it's really good at u browser
use is the one particular use case that
I use it for I want to automate a lot of
browser tasks um because there's still
you know you don't necessarily get APIs
for everything and so you want to bridge
that gap. Uh and uh yeah, the drafting
model helps you generate more tokens
faster. So you see your browser agent
just essentially run around and do
things faster. Uh so in a lot of ways it
does help. Uh I will say for browser use
I probably see around 1.5x increase
whereas for coding I see like closer to
3x. So depending on your use case you
may see more or less and and things like
that. Uh, and a followup on that one.
Are there any benchmarks like more trust
me bro like coding fire ship?
>> There there's definitely benchmarks out
there. I I'm I'm personally a little
skeptical of benchmarks whenever I see
them. I never get the same results. I
don't know if people agree with that
here. Um, so, um, yeah, for the for the
most part, like you know, you want to do
your own testing and see what works for
you because it very much depends on your
use case because the acceptance rate is
going to be different depending on your
use case, what you're using it for.
>> Thank you.
>> Um, yeah. Any other questions?
>> Mic check. Mic check. How's it going? Um
do like big models like codeex or cloud
like do they use this type of the coding
like have they published that they use
these patterns or is this more like for
open source if you're training your own
stuff or running inference
>> I don't know the question to if they do
it or not um I would imagine they do
sort of like free performance but uh for
for the open source yeah this is
particularly for the open source all the
open source big models that you want to
use all the Quinn models, the GLM
models, Kimmy models, they all have
specular decoding uh drafter models
available that you want to use.
>> Is there like a main drafting model that
they use for example for like DeepSseek
or GLM?
>> Deepseek actually came out with a new uh
thing yesterday I believe or the day
before. It's called DSpark. It's like
their own technique for doing specular
decoding in a more dynamic way.
Essentially they're figuring out how so
here our configuration is static right
like we say we're going to generate four
tokens at a time uh but with deepseek's
way of doing it they are making it
dynamic meaning you know it on on the
fly sort of decides oh I'm going to
generate only two tokens or I'm going to
generate four tokens or five tokens
depending on the acceptance criteria
depending on the GPU load and all all
sorts of metrics. So yeah, every every
model uh every lab has like their own
way of doing it as well and you probably
want to stick to that but you can also
experiment. For example, the Quinn
models uh Quinn lab doesn't release the
Dlash models for drafting but these are
released by uh a third party lab but
they work quite well with them. So you
sort of have to test it out and see.
>> Thank you.
>> Yeah, I think this is hanging right.
>> Yeah, I would check the pot.
Yeah,
might have killed a cluster here.
Uh
>> oh, I can't type. Uh
>> oh,
>> this was working well.
>> Refresh.
[laughter]
>> Let me create the tab again.
Okay. Um well, something is wrong.
It copied a URL and opened in a new tab.
See what happens.
Let me open a new tab.
I wouldn't close that one.
You know, in all the testing that has
not happened, it happened today.
Can I at least scroll through and go
through different things? Okay, at least
I can scroll scroll through
um
you know since uh the cluster decided to
take uh a vacation uh I'll sort of go
through the content that I was going to
cover. Um the main point of running this
benchmark here was to kind of show where
that knee is meaning where you see the
max throughput. Uh if we go back to this
diagram where you see the max throughput
while making sure you are seeing the
lowest uh tokens uh lowest latency for
token generation. Um and that that is
that essentially limit was at 32
concurrency. Um because anything above
32 concurrency you'll see uh the token
generation is going to be kind of the
same. It's not going to change much. uh
the throughput is going to be the same
but but the latency is going to go
drastically up and you don't want that.
Uh so that's sort of like the limit you
are hitting. Um and that is important
information that we need to keep in mind
and look at when we're deploying these
things. Uh and if
>> yeah you can go to 100. Go to look at
the spreadsheet
>> 100.
>> Yeah, go to 100 and then just continue
from
>> Yeah.
>> seven or eight.
Where is it?
>> There you go.
>> All right. Well, this one's working.
That's good.
All right. Cool. So, we'll jump into
eight. Um, let me also
[laughter] open up
Who's doing it?
>> Okay, so for module A, we're going to
talk quickly through um what sort of
flags and knobs you can tweak to make
sure that you can sort of get above that
limiting point that we were talking
about at 32 concurrency. You're sort of
seeing that limit and how do we kind of
get beyond that and what things you need
to keep in mind when thinking about
this. Uh so for this one I'm sort of
going to give you guys um a thinking
model is essentially you want to measure
and that's why with a lot of different
cells I was I keep running load tests
and it's super important to run those
load tests to see what your performance
is like and any changes you're making
how is that changing the performance is
it making better is it making it worse
um and in what particular metric it's is
it making worse right like if is it if
the throughput keeps going up or stays
the same but like the latency is
changing something is either correct or
wrong there. So, that's something we
have to keep in mind. Um, and there's a
bunch of different knobs you can sort of
like uh tweak in VLM to make it better.
But the main four ones are again the GPU
memory utilization. You want to make
sure that you're setting that correctly
depending on your use case. Again, if
you're running multiple models on the
same GPU, you might want to keep it low
and that's a trade-off you're making.
But if you're only running a single
model and you want to make sure that
it's getting the best performance
possible, you want to bump that up to
0.9 or point even 0.95.
Uh the other thing is you want to make
sure that uh the max numbum sequences uh
is set to a good limit as well. This is
something you have to figure out by
testing. Uh in our particular
deployment, if you look at the VLM.yaml,
um we start with 32 sequences, right? So
what that is doing is it's telling VLM
that it can only process 32 requests at
a time uh and not more than that. And if
you do more than that, you're going to
see some performance uh degradation
there. Um so there's a lot of different
flags, but those are like the key ones
that you want to keep in mind. You want
to make sure that you're setting the
model length to the correct length as
well. Uh and then you know you want to
make sure you're the batch tokens are
also set to the correct length. um you
don't want to you want to keep it bigger
if you want to do prefill faster if your
GPU can handle it. You want to do it
smaller if your GPU is a on a little
slower side and you can't handle it. Um
but yeah, the idea is you want to change
one flag at a time. You don't want to
change multiple things. Um and when you
change things, run the uh run the
benchmarks and see uh what performance
you're seeing. See measure it and then
make assumptions on what you should do
next. Um, kind of go through it quickly
here.
We have about what 10 minutes left.
Uh, oh,
>> I think we lost the P PVC. I think
that's what happened. I got
>> Oh, it got the different one. Yeah, I
need to actually change this. Rerun
this, I think.
Um,
let me actually just change this in
here.
This was supposed to be like sequential,
but other Jupyter notebook died. So,
change that and then that should work.
Um, again, like I talked about, there's
different knobs uh that you want to
tweak um and see what happens. But we'll
get sort of the measure. We'll measure
the baseline and then we'll change a
couple flags and see what happens next.
Um,
does it say work?
Okay, cool. There you go. It's working.
While this load test is running, any
other questions
anyone has?
>> Excuse me.
>> I noticed that there's a definite
fall-off when we're optimizing the
model. Like here, the 32 to 64, huge
falloff. Uh is that when you would
decide that maybe we should scale the
hardware or is that something that
you're confident you can still tune it
further?
>> Uh essentially is this is this the
ceiling?
>> Yeah, you figure out the ceiling by
doing mathematics. I think in some of
the previous modules Dwan covered uh
like what the max ceiling can look like
for tokens per second what the
throughput looks like and um you know
what sort of expectations you should
have for the deployment and if you are
like seeing those max expectations
that's probably the maximum limit of
your hardware and then you probably have
to get additional hardware or better
hardware to do so. Uh so yeah there
there is sort of a limit you know
there's only so much you can tune but
you're trying to squeeze as much out of
the GPU as possible.
You want to share the slides before you
continue?
Share the slides real quick.
>> The server
I can leave it up for a little bit,
couple hours. I'm not going to leave it
up just because you do have access to
GPUs. Um but what what I am going to
give you if you scan this QR code you'll
get access to the PowerPoint as well as
the repo if you want to spin this up in
your own AI cloud account or if you want
to run on your laptop you can do that.
So if you scan this QR code it'll take
you to a site that has all the resources
and if you don't have a cloud account
you can sign up and you get $300 in
credits with a free account. So that's
everything you need. And if you all have
questions, both of our contact
information is here. Omar, I'm Dwan
Lightoot.
>> Yeah.
>> And yeah, with that being said, if you
all scan the QR code, I'll let Omar
finish it up. I just want to make sure
you all get this before people started
to leave. Thank you.
>> We'll leave it up there for a couple
more minutes
gets it.
>> Yeah, go ahead.
personal assistant. Um, so
>> so you can use llamas. It depends on
your hardware. I think that's like the
first thing I would look at. Um,
>> no problem. Thank you.
>> Oh, you have both. for the sake of the
argument, let's just say you have the
best GPU. Let's just say you have um
>> Yeah. Yeah. You have the latest
Blackwill GPU. Um you know, I think for
testing and doing like figuring out what
model you want to use for your use case,
I think it's good to use Olama and Llama
CPP to quickly spin it up and try it out
and see what happens. Uh but once you
have a model that you know I'm going to
use for sure for this use case and this
this is working great you probably want
to switch to uh VLM sg lang or one of
these other model uh runtimes. Uh reason
being they allow you to run at higher
concurrencies and give you more
performance out of it. So if you have a
single agent running I think it's fine
to use Olama. It's not a big deal
because you only have one request going
in at a time. But if you let's just say
you're running like 20 agents and you
want to run it parallel uh
Yeah. Yeah, you can set up speculative
decoding with VLM. I don't think Olma
supports speculative decoding as far as
I know, but I could be wrong. Um, but
yeah, it when you want to get the max
performance out of your hardware, you
definitely want to do that.
>> Yeah,
>> I actually don't know if there's a
diffusion uh LLM. Is there an open
source diffusion model right now
available?
>> Yeah, Lana. Yeah, I mean I think VLM
supports it. So I think you you would be
able to run it on VLM. Uh Olama, if
supports it, you can as well. Um yeah,
that's definitely possible.
Okay, we'll switch back to the module
and kind of go through it. Um, again
like I was saying, at 32 you're seeing,
you know, good performance, but at 64,
uh, we're going at, you know, the the
throughput is sort of staying the same,
if not going up, but we're seeing, um, a
significant increase in latency. And to
kind of get around it, um, one of the
things I want to talk about is the max
num sequence. Again, this is sort of,
uh, how many requests VLM is able to
process at one time. It's sort of
setting that flag. If you want to have a
lot of uh requests being processed in
parallel uh then you want to sort of
increase this amount. So currently I
believe it's set up at 32. So we can
bump this up to
128
and then we can run this deploy it and
see how that changes the performance.
Okay, it changed a lot of things here.
Yeah, [snorts]
once this comes up, uh, we can do
another test and, um, and you you'll
you'll see the the limitations that
we're seeing here at 32 is going to go
away and you'll actually see the latency
be manageable again um, at higher
concurrency levels as well. So, this is
sort of like the loop you want to go in.
You want to find the right flags for
wherever the bottleneck is. find the
bottleneck, figure out why that is
happening, what flag you can tweak uh to
make sure that you're kind of overcoming
that bottleneck.
Um
it's come up.
That's going to take a little bit of
time. Um any questions? One more over
there.
>> Potentially bursty traffic
>> um at times. Um
>> Oh yeah. Is there such thing as like
bursting to serverless? Is that the
domain of you know model routing layer
on top? Like what is the pattern for
>> Yeah. Um I mean autoscaling is one of
the patterns like specifically I'll tell
you in LKE uh you can have uh dynamic
like autoscaling. So it can scale up uh
depending on your needs depending on
bursty traffic. it can scale up to you
know maybe use a node that has four GPUs
instead of one because maybe that
handles it better right so you can
automate a lot of those things uh to
make sure that you're doing it well and
the other part of it is like you can
also build like some statistical models
to make sure that you kind of understand
your traffic patterns over a long
horizon and then the uh the cluster can
also dynamically like sort of predict
your burstiness in some ways and then
can also scale based on that too
>> if you got your browser I can show you
where it's at
>> browser
you open your browser, I'll take it to
you.
>> Okay, so this one is successfully rolled
out.
>> Um, and then we'll do a quick load test
and
once that is run, we can see more.
All right. Uh, any other questions? Most
folks are gone, but
>> yeah, like foot
H.
>> Yeah. 32. That's where we saw the limit
last time. Once we get to 64, we should
see uh that it should improve. Okay. So,
there was a big drastic improvement. The
throughput actually went up quite a bit.
Um so, it's at 1100 tokens per second.
Whereas previously, if we look at it
over here at 64, we were at 800 tokens
per second and then the latency was uh
2,000 milliseconds. But now after the
change that we made um it is uh 1100
tokens per second and then the latency
is uh 800 milliseconds. So it's gone
down the latency has gone down quite
drastically and then we have also
increased the throughput quite
drastically. So the these are the sort
of the tuning you can do uh over time to
make sure that things are running well
uh once you have it up and running and
you can do this for your particular use
case. Maybe you're not going to have uh
six uh you know 64 concurrent requests
coming in for a particular use case but
maybe you are. So um you have to decide
based on your use cases
>> your concurrency one higher than before
like was that a trade-off you just did
>> concurrency one I mean it can be a
little higher or lower. It's not going
to be the same all the time but for
example before it was 37 but now it's
35. So it's a little bit of deviation
that happens with running models, but it
should be plus minus two sec two tokens
there. Um we're also running the full
precision model now. We're not we're no
longer running the FPA because we had to
switch the notebook. So that's the other
reason why you're seeing it go from like
50 something tokens to 30 something
tokens. Uh so that's the performance
that we're seeing there.
But but yeah, that is all I have. That
is one flag you can tweak. There's also
all sorts of other flags that I implore
everyone to take a look at. The workshop
kind of goes through it as well. But I
think we're on time and I'll give it
back to Dorne.
>> Yeah. Thank you all for attending our
session today. If you have not scanned
the QR code, the code, the repo, the
PowerPoints are available on this site.
Feel free to start a free AMA cloud
account. My name is Dwan Lightoot and
I'm joined by my colleague Omar and we
thank you all for joining us today. Feel
free to ask us questions after this
session. Thank you.
>> [music]
