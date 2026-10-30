# Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular

Canonical video: https://www.youtube.com/watch?v=7BcQdtRA3Tc

Source: https://youtu.be/7BcQdtRA3Tc

Uploaded: 2026-10-11

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Uh so let's get started. Uh hi, my name
is Abdul. Uh
uh I'm from modular. Uh today I'm going
to be talking about what modular is and
what value it brings to you.
So as you probably know today there is a
huge crunch uh for compute and there's
like no alleviation in sight. A lot of
these things are booked for the next few
years.
But there's also a kind of as a result
you have an explosion of hardware. We
call it like a Cambrian explosion. You
have Nvidia providing you know a few
generations of GPUs, the Intels, the
ARMs, the Apples, everything uh is is
present. They all have some niches uh
that they cover. But the problem is that
you have to ask is how do you program
all of these uh systems.
Now if you look at the current software
as it is today um it's kind of a mess as
well and that's because a lot of these
hardware choices bubble up from the you
know from down under uh into upwards
into the stack. So this is a diagram
showing how uh VLM supports both Nvidia
and AMD.
If you add extra hardware the the the
diagram becomes even more difficult. Now
today folks actually uh deploy not only
using VLM but also SG lang TRTLM
uh Llama CPP etc.
So at Modra we thought well this is kind
of a huge mess. Let's rearchitect the uh
the stack from the ground up and let's
build a unifying layer uh that unifies
all the hardware so everything runs on
our stack.
To realize this, you have to actually go
back to first principles and build a
complete software stack with
portability, performance, and
programmability in mind. So at the
bottommost level, we've developed Mojo,
a heterogeneous programming language
that's targeted towards AI as well as
general purpose programming uh as well.
It's kind of pythonic in style. So folks
that actually know Python today pretty
much know 90% of Mojo. Uh so we've built
that language and that targets both
CPUs, GPUs as well as all our
accelerators. On top of that, we
leverage Mojo to build max our inference
engine. Uh so that provides you with uh
AI inference for both for a bunch of
different modalities like image, video,
speech as well as text. We've built all
our kernels underneath the hood that are
built on top of Mojo.
Finally, today's AI inference is
distributed. So you actually need a
cloud solution as well. uh you need to
pick which hardware to deploy your model
on, how to route uh different user
requests to different uh machines, how
to do KV cache offloading and and and
distributed inference and disagreed
inference uh to be able to serve the
model at the speed and the cost that
that folks expect.
So putting it all together, we built a
modular platform that's fully
programmable. It's hardware abstracted.
It's it's soda perf. Uh and then it
actually can be deployed both on prem as
well as on our cloud as well. So it can
be if you have a cloud uh uh setup, you
can actually download the modular cloud
and and deployed there.
So let me kind of dig into each one at a
time, each part of the stack. So the
first is Mojo.
Uh so Mojo as I mentioned is a Pythonic
system programming language. It's not
unlike C++, Rust or CUDA C++. The thing
is what it enables is uh programmability
across different accelerators. It's
blazing fast. It's again it actually
competes with CUDA in terms of
performance. uh and you can think of it
as the best way to program CPUs and GPUs
within a Python-like programming
language.
In terms of how we think about Mojo,
uh you know, you can think about there's
three different quadrants, usability,
performance, and portability. Rockcom
and KOD and CUDA gives you massive
performance, but they sacrifice on both
usability and programmability. A lot of
folks use agents to actually program
these system nowadays.
Open CL back in you know a few years ago
was popular. It gives you great
portability but is sacrificed on
performance and usability. Triton is has
a good sweet spot that gives you 70% of
the Perf uh but it gives you portability
and usability
and Mojo is is trying to kind of fill
the niche of the sweet spot where it's
the best of both worlds. It gives you
the abstraction to allow you to write
portable kernels and and uh and usable
kernels while giving you also the
low-level access uh to get the maximum
performance.
We've actually open sourced uh
practically all of our kernels so you
can actually test this stuff. You can
benchmark it on your own machine. Uh we
have state-of-the-art kernels on Nvidia,
AMD and other hardware. So to tell you
what state-of-the-art is, it means that
our matrix multiplication is faster than
the coupe losses, the hip losses,
everything out there. And it's not by 1%
in some cases by 2%. We have the fastest
attention uh kernel out there, faster
than flash attention for uh as well as
like the AI it and things like that.
Uh one thing that we've announced uh a
month ago or so is Mojo 1.0, know the
stabilization of our APIs. Uh, and we're
going to be releasing Mojo 1.0 in the
next few months. And we're also open
sourcing Mojo uh, in the next few months
as well.
Sitting on top of Mojo is Max.
So, Max is trying to kind of solve a few
of the uh, assumptions that were made
uh, back in the day for PyTorch. PyTorch
is about 10 years old. It was not really
designed for the genai inference of
today. As a result, you have like VLM
and SG lang that stepped into the void
to give you things like KV cache, page
detention and and things like that.
And but all of that kind of kind of
complicated the entire PyTorch
ecosystem. A lot of folks don't really
uh use PyTorch as is. They're resorting
to these layers on top.
So think of a new approach and we call
that the max framework. So again it's
built from the ground up uh with the
best technologies with the best
state-of-the-art graph compilers uh the
eager mode execution. It's portable
across devices. It understands your mojo
programs to do novel fusion uh and it
gives you the maximum performance and
deployability that you're otherwise not
able to do in in in regular PyTorch.
So compared to other stacks uh this is a
single stack that allows you to serve
develop the model as well as optimize
everything in one cohesive uh system.
it within Max we support thousands and
thousands of models in fact thousands of
architectures uh everything from Gemma 4
to M uh Miniax 3 to GLM uh so any model
that you think about is is practically
supported in uh in in uh in Max and it
has the same interface that you'd expect
uh from what is standard today. So we
also provide a open AI endpoints that
you can use uh within the stack.
If you're familiar with like PyTorch
programming uh the figure on the right
would or the left will not be like
massive departure of your mental model.
Uh you can build a model as you expect.
You know you can import modules. The uh
programming language for developing
models is Python. So as familiar to
folks uh and you can compose uh things
as as you as you as you um as you build
them. We also support like the eager
execution to enable debugging as well.
Now the other thing that one has to
realize is modern LLMs uh are run on
across different GPUs and in many cases
multiple nodes. So also max the max APIs
provide you with a way to uh program
multiGPU system AC as well as multi-node
systems from within the API so that the
model is natively supported across uh
different GPUs and different nodes as
well. And this can also be
heterogeneous. So there's nothing to
stop you from saying the prefill is on
hardware X and the decode is on hardware
Y.
Finally, layered on top of all of this
is the modular cloud. So, as I
mentioned, uh today's AI inference is
distributed. It runs on many many
different machines. Uh it's
heterogeneous.
So we provide the module cloud which is
a performance native you know we think
of it as a glass box because you can
actually tinker with all the variables
uh that are available for you in both
max mojo and everything in between uh
within your endpoints. So it provides
provides endpoint deployment as well as
bring your own cloud deployments as
well. We also have a module cloud lab
that allows you to experiment with all
these different parameters and pick the
best point in the perto frontier that
you have for that model or based on your
workload as well.
Uh so in terms of like the UI uh if
you're familiar with like any uh cloud
provider I mean it's it should be pretty
familiar. You just go to the website,
you click on which model to you want to
run, you get an AP an API key and then
you plug that in uh to your HTTP request
and uh you can run it. You can have
dedicated endpoints as well as we can
serve your own custom model. Uh you know
in many cases folks have fine-tuned
models or models with their own custom
speculative decoders. Uh we could do all
of that uh for you as well.
Now, why do you care about all of this,
right? It's a lot of tech. Uh why do
folks care? Well, it's because you can
actually uh accomplish more things uh
through the system, right? So, you can
actually decrease cost. You can get
greater flexibility because you can
actually use different hardware. You're
not beholden to one hardware provider.
Uh you get portability. You can use
multiple different models. Uh etc.
So how does Perf look like? Well, we
benchmarked a lot of these uh and this
is like against uh state-of-the-art, you
know, the best combination of VLM or SG
lang [snorts] in a bunch of cases. These
are these benchmarks are independently
verified as well. So in terms of Kimmy
Kimmy
K2.5, we're 5.5 faster on TTFT uh
compared to VLM.
We can also get 1.5x throughput
improvements. So the token per minutes
on per GPU is 1.5x faster uh on B200
than it is on VLM.
In terms of Flux 2, and I encourage
folks to actually visit the booth behind
this curtain, uh there's a nice demo of
Flux 2. uh we're about 7x faster uh
compared to ters that compile with
diffusers. So again, Max supports
different modalities within the same
framework. So you don't have to use an
omni variant of a of a piece of software
or anything like that. We support both
video generation, audio generation,
image generation as well as text
generation.
Uh we also support you know things on
AMD where you can get a TCO benefit as
well where we're 4x faster than the
equivalent uh on um on on the MI355
systems. Actually you know some of this
is not a fair comparison because you
know some folks might say oh 7x is much
larger than 4x but this is you cannot do
that comparison very easily. uh that you
can you have to factor in the cost uh
per uh GPU and AMD is usually 30%
cheaper than uh the Nvidia equivalent.
Uh artificial analysis actually we've
been partnering with them uh and we've
been and they've independently been
verifying our results. Uh this is our
results like as of uh today. Uh we're
about 3x faster than the next competitor
uh on the flux 2 dev model as well. And
this is not playing tricks of
distillation and you know quantization
or anything like that. This is just raw
speed because we can leverage the
hardware from the ground up and make
sure that uh we're getting the max uh
the max PF benefit from the model
and you can actually go to artificial
analysis today and see and see these
results.
Now what does that mean to folks again?
It means you can open up applications
that are otherwise kind of not possible
because of slow inference. So this is
actually uh a kind of a live demo. It's
just somebody's pasting in the prompts.
Uh but the generation is is accurate. So
you can generate things in subsec
generate images in subsecond uh per in
many cases these are.3 seconds. Again
you can go to the booth. There's a nice
demo where uh you can give a prompt and
then it reads the video feed and then
renders it as well.
Uh the other one data point is Gemma 4.
So Gemma 4 was a a recent model that was
just introduced about a month ago, a
month and a half ago. Uh again we're
quite faster than other any other
competition out there. Uh so uh you know
many cases actually some of these are uh
hardware companies. you know, Samanova
is a hardware accelerator. Uh we're, you
know, let's say 6x faster than that. And
in general, we're much much faster than
others. And by the way, we're for all
these cases, we're just starting.
There's more optimizations that we're
landing uh as as as time goes on. So,
we're never never stopping to improving
these things.
So, we have a bunch of uh places where
you can get involved. You can join our
open source community. So, a lot of our
code is open source. We have over
700,000 lines of kernel code that we've
open sourced. We've over open open
sourced all of our model definitions,
all of our max serve. Um, we have AI
skills. So, if you're not familiar with
Mojo or Max, you can actually use the AI
skills to port uh from languages that
you're familiar with into Mojo or Max.
You can also join us. We're hiring. So,
there's pamphlets on the booth where
we're hiring for a variety of different
positions. So, as I you probably know,
we we hire from low-level kernel
engineers to high level folks that work
on Kubernetes and everything in between.
You can actually try all of this. So,
this is not uh demoare or slideware. You
can pip install modular right now if you
want to and try all of this stuff. And I
welcome everybody to validate these
results.
So, with that, I kind of that's it. And
uh but I'm open to questions if folks
have it. And I'll also be on the booth
uh for the next few hours as well.
[music]
