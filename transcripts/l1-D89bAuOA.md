# Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google

Source: https://www.youtube.com/watch?v=l1-D89bAuOA

Uploaded: 2026-09-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Hi everyone, welcome to our talk on um
our LLM performance benchmarks reliable.
A little bit about us. I am Ashok
Chandra Seeker. I'm a staff software
engineer at Google. I work on inference
performance evaluation and optimization.
Um and I lead a couple of open source
projects. One is called inference perf
uh which is a benchmarking tool to do
reliable performance benchmarks and uh
I'm also the sig lead for LLMD
benchmarking. LLMD is a distributed
inference framework um that makes
production scale inference possible.
>> Hi everyone, I'm Jason Kroger. I'm a
software engineer at Google. Uh I'm also
a co-maintainer of inference Perf and a
few of the sub projects that Ashok
brought up. uh and I work on inference
performance and benchmarking.
>> Okay, let's get started. Um let's look a
little bit about the how the benchmark
ecosystem looks like. Right? You have
your model server frameworks. Uh these
are VLM, SGLAN, um and other model
servers and all of these have some
benchmark capability within them. Right?
These are primarily Python scripts and
are developer focused benchmarks to see
how you can measure the performance of
your model server itself. And then you
have your competitive analysis tools. Uh
these are MLPF, semi analysis,
artificial analysis and so on. Right?
They mainly aim for competitive
performance benchmarks to compare like
chip and accelerator performance. Uh and
then you have your typical web
benchmarks. Uh these are like locus,
graphfana, ksix um and so on. These
mainly focus on highcale http
benchmarks, right? uh and then you have
your um last segment which is the
production scale LLM benchmarks right
these are to actually benchmark uh your
production inference serving stack and
that is our focus today right we'll be
focusing mainly on inference perf and
how we solve this uh production scale
benchmark problem
so if you have run a benchmark before uh
it typically looks like this right um
you have some sort of benchmark hardness
uh and then you specify what model you
are bench benchmarking the number of
prompts you want to run, what is the
input output sequence length uh and the
request rate or the load you want to
send, right? Uh and your output looks
something uh like what is on the right.
Uh this is basically your uh input token
throughput, output token throughput,
some latency metrics, time to first
token, time per output token and so on.
Um so what are some issues with a simple
benchmark like this? Right? So if you
want to actually benchmark production
scale workloads um here I have LLMD
inference stack as an example right uh
you can have uh online serving you can
have batch workloads and if you see the
inference pool below uh there are like
lot of servers that are running right
and then you have like complex
configurations like pre-fill decode
disagregation um and workload
autoscaling and other things that are
going on under the hood and usually the
scale is much larger right so your um
normal benchmark harnesses runs into
issues when you try to benchmark a setup
like this. And if you look at like the
key characteristics of what we want out
of a production scale benchmark, we need
to be able to do high load uh which is
limited in a lot of tools out there. We
need to be able to simulate real world
workloads, right? Um what use it is if
it is just some synthetic workload that
is not accurately representing uh what
your customers are going to run. Uh and
then metrics fidelity is very important,
right? Are the metrics accurate and how
well they work?
Uh this is like the set of metrics that
LLMD measures uh by default. Uh I just
pulled it from the website there. Uh as
you can see it's not just like a single
QPS that you are running, right? You are
sweeping a a list of various loads and
uh you try to measure what the baseline
is and what optimizations you are making
and what the difference there is. um you
need to find the right point where the
server gets saturated so you know the
right optimal uh point to run your
servers on uh to maximize performance
and to save costs um and things like uh
SLOs's become more important right what
is your um time to first token P90 SLO
and are you conformant to that SLO
so when you run like um normal benchmark
like we saw before what are some of the
pitfalls that you run into right uh we
have been uh running benchmarks for a
couple of years. So we run into all sort
of uh different results that people
share and a lot of times we aren't able
to reproduce the results that are shared
by other people. Right? So that is what
motivated this talk. Um so these four
common uh things that we see as an
issue, right? One is accurate uh metrics
and two observability into your
benchmark tool itself. Um do you know if
your benchmark harness is actually
failing? Is it not able to maintain the
load? Um and three reproducibility. Uh
there is some inherent uh randomness uh
in like the data sets that you use. So
how do you make sure it is reproducible
and four the data set quality itself.
So this is an experiment we ran. Um we
asked like different benchmark harness
to generate 200 QPS and this was the
result right. Um so a couple of things I
want to point out. Um, Python has this
global interpreter lock GIL if you have
been working with Python, you know that
which makes everything uh sort of single
threaded. So even when you have like a
multiCPU mission, a lot of times you are
limited by the performance of a single
CPU uh when you're CPU bound especially,
right? Uh so this kind of shows a single
process um benchmark harness and a
multiprocess harness and how the QPS you
are able to achieve differs based on it,
right? when you run with a really uh
small shad core mission, you can see
that even when you request 200 QPS, you
are only getting 38 QPS and then you
give it a bigger mission and then some
of these uh single process harness they
cap out at like 170 QPS, right? This is
a much more powerful machine. Um but it
is a problem because you ask for 200 QPS
and then you don't know whether it
actually delivered it. It will just say
I ran it these are the numbers. So you
think okay you ran 200 QPS but in fact
you you have not.
Uh the other issue that comes out of it
is the latency inflation right if your
server is saying okay this is how much
QPS I was able to run and this was the
accurate numbers that is one thing but
if your uh benchmark harness is actually
inflating latency right because it's
thrashing trying to collect all the
streaming token requests um in one of
the tests we noticed like u the delay
was up to 58 seconds. So you might look
at this and go oh my server is
bottlenecked right it's not able to
handle all the requests but in fact it's
actually your benchmark client that is
inflating the latency right uh we ran
like a th000 QPS test uh when your when
your benchmark harness is actually able
to scale out you can see there is very
minimal latency right this simulated
server so there shouldn't be any latency
at all
um and like I said there are like other
variables that go into it right in one
of the benchmarks um someone shared and
they said, "Hey, we are getting 20%
better throughput." Then we looked into
it and we found out the benchmark
harness were setting the model
temperature to zero, right? Which means
your model outputs are a lot more
deterministic and it was able to turn
out a higher throughput than what you
would normally see in like a real
workload, right? Where your model
temperature is somewhere around 0.7. Um
another thing is like we used a a shar
GPD data set the same data set across
two different benchmark harness and they
produce different input tokens right
this is because they sample them
differently they truncate them uh
differently so as a user you don't have
insight into this right you run it you
trust the numbers it produces but they
are wildly different
uh and there is much more right do you
actually force it to generate till the
end of sequence are you looking at
prefix cache rates how do you do mult
multi-turn uh replay via benchmarks and
uh how how do you actually get high
fidelity uh on the actual workload that
would resemble your production workload
right
so the main thing I wanted to convey
here is like a lot of times you diagnose
it as a your server or inference stack
problem but in a lot of cases it could
be your benchmark harness
so what is the solution to this how do
we actually do reproducible benchmarks
Jason here will take you over
Thanks Ashook. Uh so yeah, how do you
how do you solve these problems?
Uh we al together inferencepf uh the
CNCF project spanned out of Kubernetes
working group serving uh to provide like
a standardized place for us to work with
the community and solve some of these
issues together.
uh it enables the ability to have like a
userdefined declarative configuration uh
that allows you to have clear
reproducibility across runs.
We also added a load generator uh that
solves the GIL problem in Python uh
across multiple processes
and reports those client metrics back
along with server metrics to ensure that
you have the highest metric fidelity and
you're able to actually observe when
your tool is having an issue versus your
system under test.
So, first going over the load generator,
uh you see that
the main process actually cues requests
based off of the planned time that they
need to execute, which is based off of
your configuration. This may be in some
poison process or constant rate or
maintaining a constant number of
concurrent requests. This request Q
channel is then spread across multiple
processes which pull and ensure that
they execute with minimum overhead but
then also observability about when they
execute versus their plan time.
And you can see this working at scale.
So this is a comparison across other
tools uh some being the HTTP scaled
tools like K6. uh but you see that even
at 5,000 QPS
inference perf was able to keep up due
to this architecture and most
importantly actually report that it was
able to keep up.
Other portion is configuration. So
earlier I show showed a brief example of
how you might simply run a benchmarking
tool. And here on the left you can see a
simple example running a random data set
against an endpoint. But the actual
configuration that we have in front of
inference perf is very detailed with a
lot of knobs that allow you to
accurately
uh test your configuration off of your
workloads. You can see here on the right
that this is uh configuration for
conversation replay where you're able to
configure not only like the input output
length but their distributions etc.
And further
beyond just the ability to configure a
single run, we've actually worked
together to have a published set of some
of these workloads and configuration of
inference perf that are tied to
state-of-the-art inference workloads.
For example, here in the workload
catalog that we've put out, you're able
to access standard multi-turn
uh generation,
tree of thought, agentic generation uh
as well as batch summarization and
others.
Each one of these has a simple
definition uh kind of in natural
language that allows you to understand
what the scenario is. But beyond that
there's also pretty detailed
configuration metrics not only in
inference perf configuration but in
generic terms so that this can actually
be shared across tools and have a place
for standardization of these workloads.
So kind of the culmination of these
things uh leads us to actual results
that we can clearly display. Uh and
here's a screenshot from Prism which is
a UI we have for sharing not only those
workloads that I showed before but also
some benchmarking results. Uh and Prism
is a part of the LLMD project. Here you
can see a benchmark result for the
agentic code generation workload that we
showed before on TPUs. Uh these three
lines you see here
show you The difference between
combined optimizations is the green line
and a baseline that is just a simple
Kubernetes service instead of in front
of multiple model server replicas. It's
important to note here is that this is
at production scale with eight replicas.
And you can see that the combined
optimizations were measured to be much
higher than the baseline scaling into
almost hundreds of thousands of tokens
per second.
So the takeaways kind of the principles
for benchmarking validity based off of
the pitfalls that Ashok brought up
earlier.
At production scale, you need client
concurrency and you need observability
into your client's behavior and its
ability to meet your configuration.
The metric fidelity allows you to
actually observe your client's behavior
as well as your system under test and
understand that your scenario was
accurately executed and your performance
results were valid.
The stochcastic variables uh and
non-determinism or determin determinism
that you set amongst your run needs to
reflect your real world demands uh for
your workload.
And most importantly, your data sets do
truly matter. Your workloads
uh need to be as close to what you are
intending to test as possible. And
uh we have examples in the workload
catalog.
So here we have three links to some of
the things that we've presented on here
before. Inferencepf is our benchmarking
tool and there's the git repo for it.
Llmd is a project that we work under and
inferencepf under it in LLMD benchmark.
uh LLMD is for production scale
inference and then LLMD Prism which was
that UI we showed for the benchmarking
results uh and the workload catalog that
defines some of these workloads.
So that will answer questions after but
we appreciate your time.
[applause]
>> [music]
