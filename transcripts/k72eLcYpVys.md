# 1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS

Source: https://www.youtube.com/watch?v=k72eLcYpVys

Uploaded: 2026-10-12

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Hello everyone. I think we can get
started.
So, a few months ago, I did something
that was um a bit slightly absurd. I
took a coding agent. I pointed it at my
team's uh cloud
sandbox hosting environment and it said
try to break it and I let that run
overnight. And this talk is a bit about
what we found.
Uh my name is Kevin. I work at Amazon
Bedrock Agent Core. It's a sandbox
hosting environment or platform. And we
do more than that. We provide agents,
identity, memory, um, runtime
environments, sandboxes, gateways,
anything you want to use to build and
host your agents on agents on the cloud.
So the way this started was basically
with me taking a hard look at how um
customers use our platform
and increasingly I think a lot of us in
the industry see that uh a lot of
platform components on the internet are
just agents and increasingly they're
also sandbox hosted. I think today's
talks will maybe walk you through all
the architectures that can exist in
cloud hosted uh sandbox environments.
And so this kind of got me thinking how
can I perhaps emulate simulate the
customer and also test the service the
same way agents use our platform.
So the first thing I think we we set out
to do was create an abstraction or
interface that allows coding agents as
well as agent applications to interact
with our service uh in a way that's
pretty native to them. And today we know
that Frontier models know the MCP
protocol pretty well. So we spent a day
or two just creating an MCP server to
expose access to our environment and
platform um just so it can get started
pretty quickly. The second piece was
polishing that. Uh we spent some time in
finding the tools that can be made
accessible and uh smoke testing some
runs and and things like that.
So some of the tests we ran just by hand
was uh for example write a Python code
file and execute it or take a Python
file and uh convert into Java.
And then we realized we wanted to just
expand the test domains that we we were
going to set the coding agents to do. So
we asked to just plainly write a
thousand tests across 10 domains. And a
thousand tests here was pretty
arbitrary. It was just to cast a wide
net and see what caught back. This took
a bit of polishing because we knew that
a thousand tests would take a few hours
and was going to be a little tokenheavy.
So we um did things like credential
management credential management
injection um what happens when a test
fails. Is it a service issue? Is it a
MCP layer issue? Uh those are the kind
of things we we let the agent um figure
out.
So the architecture is honestly very
simple but it's also very powerful and I
think a lot of us have probably seen
this in our day-to-day uh development.
So we have our coding agent on top left.
We have an MCP server that basically
wraps our cloud sandbox environment and
all the findings get sent back to us. We
store them in a SQLite database just
because as some of you might have seen u
agents are pretty prone to write
markdown files but that doesn't really
scale when you have a thousand tests
that you want to run and this allowed us
to tap into concurrency or you can have
multiple sub aents running locally and
running and executing their tests and
storing those results uh locally.
Now, a thousand tests I think is kind of
easy to just say out loud, but really
every single dot on the screen kind of
represents a workflow that a customer
would actually run. So, we did things
like testing the sandbox uh life cycle.
How reliable is it when you put it under
stress? Um
things like file system IO, what happens
when you upload a file and download it
from the sandbox?
Uh tested performance.
We tested some software development life
cycles like uh for example writing
Python packages, Java packages um and
the like.
So to give you a perspective of what one
of these dots could represent, it could
be an end toend machine learning
training uh program. It could be
generating a PDF report.
Uh it could also just be um as simple as
opening a web page. And we re quickly
realized that our platform which at the
time was hosting two uh major
applications, one was a code sandbox,
the other was a cloud browser would have
different tests that mattered
differently to the sandboxes that they
were hosted in. So for example, here in
the browser, we asked the agent to
create a bunch of uh tabs and try to
scrape them all and summarize them,
maybe take some screenshots, download
them, maybe fill out a form, automate a
login workflow. But the point here is
these sandbox hosted applications uh
tend to go through different workflows
that demand different requirements from
the sandbox.
So we ran through the tests and I want
to talk about just three failures that I
think um showcase some of the patterns
we saw uh from these uh sandbox hosted
applications. So a simple one was we
uploaded an image, we downloaded it and
we wanted to see if the same thing that
we put up uh we got back when we asked
to download it and lo and behold that
was not the case. Uh we deep dived a bit
into it and we found that the encoding
layer at the MCP layer was incorrect.
The second one was a bit interesting too
which was a no bite. It just threw off
off our tests. Um a no bite can be a
zero. It could also be a marker in some
coding languages that just mean that
means that the string is is uh complete.
Now an interesting one that was
particular the sandbox layer is one
where we actually wrote files to a
specific directory in the sandbox and
when we try to get it back it just
wouldn't be available.
So now we started to segregate the
patterns uh and failures into two
layers. One was at the interface and the
other one was at the sandbox layer. And
it's important I think to draw the
distinction because uh when we start to
host applications in sandboxes we they
deviate a little bit from the typical
API service pattern where you have a
long running service that has exposes an
API uh and you you know send a request
you get an output that's reasonably um
shaped and you you kind of know what
your backend service does. But obviously
in today's world we we no longer have as
many long running applications rather we
have specialized agents that are uh
sandbox and environment we expose access
to them through a gateway and the
demands that they have on their let's
say computer environment are going to
differ greatly.
We know that and this is an experience I
think a lot of us can relate to which is
you are developing something locally and
you just start to see your agent uh
either a curo cloud codeex whatever it
might be do funny things like it might
uh download a package you might not have
expected or it might translate a CSV
file to JSON to PDF for whatever reason
and all of these workflows that your
agents will want to do are going to
demand uh different things from your
environment. So things for example like
how much memory or CPU your sandbox has
the permissions that are available to
your processes and file systems. I think
in a lot of the talks we'll see today
there are a lot of different
architectures that your sandboxes can
have. And the wider point here I think
is all these constraints have pretty
massive implications for your agents
ability to solve these problems.
And just to kind of visualize that,
these are some of the faults that we saw
when we compared two different
applications hosted in sandboxes. So at
the top we have the code sandbox and the
bottom we have the cloud browser. At the
bottom right we have the failure modes
that are highlighted in red which
signify how many times the sandbox
actually uh perished. In this case,
because cloud browsers, we know that
whenever we open up tabs, they're pretty
memory heavy. And so, a lot of our tests
fail just due to memory constraints. And
that wasn't really a fault we saw in the
uh code interpret environment. And when
we map them out a little bit
differently, we start to see that the
failure modes coales around sandbox
primitives. So we know some of the
components around file systems tend to
be file system permissions uh mounted
file systems uh permissions to read,
write, execute files, um whether or not
the file system uh is persistent or uh
ephemeral. Um and the tests were pretty
unforgiving. Um for example, in the
bottom right we have uh the browser
tests just starving the the sessions and
sandboxes out of memory and signaling
that as a complete failure. And I think
the wider point here is as we host these
applications in sandboxes and we expect
our customers to be able to build uh
pretty arbitrary workloads in these
sandboxes, we have to be pretty careful
that the sandbox constraints have
massive implications as to those agents
ability to complete those problems.
Now if we look a little bit closely and
this slide is pretty heavy on the second
column we have a lot of the primitives
used to compose what a sandbox container
um might look like. So we can go as deep
as kernel capabilities, things like
kernel interceptors, um these things
called extended BP BPF programs which
allow you to run kernel modules and
intercept programs at the at the Python
layer. Um those might uh control how
your agent actually can make some egress
calls, maybe make a internal API call to
um your internal company services.
If we diagram this out, this is kind of
what a very high level overview of how
the components in the sandbox might uh
affect your um workload's ability to do
its job. So here for example, I think
earlier in our talks, we spoke about uh
security secure compute which controls
the system control programs that your
applications might want to run. So for
example, say I have a machine learning
package that needs to spawn a process.
Does my process or container even have
the ability to start a new process? Um
perhaps I have a code interpreter uh
task that needs to download a Python rep
Python package into a very specific
module for uh the Python kernel to be
able to pick it up or are the Rust
binaries in the right location for when
the coding agent is able to um run or
execute a program. All these very very
small things tend to add up into your
agents ability to uh execute the
business problem.
Now just taking a step back I think this
was kind of interesting uh which was the
idea of like using an NLM to generate
basically unit test. I think we've all
done it. We I don't know if anyone
writes unit tests by hand anymore. Uh
and similarly if we go up up a layer
integration tests uh we we we can
anticipate agents to be pretty good at
understanding the problem space and
writing tests for them. But as we move
towards hosting more and more
applications which are just agents uh in
sandboxes,
we start to see the cracks in the model
which is um these very low-level
primitives and controls um might
actually hamper your agents ability to
do its state of goal. Um, and what we
were hoping to relay here is a a very
strong way to actually surface these
failure modes that are that are pretty
innocuous to us is just through fuzzy
testing your agent sandbox asking it to
complete perhaps in this case a thousand
workflows and seeing what results you
get.
And just to also make it a little bit
more tangible, um, a lot of us here
developers, we are very used to running
coding agents locally. You might have
your, you know, your your codeex or your
cloud running locally. And as we expand
and create more workspaces, you quickly
put a constraint on your laptop and now,
you know, your teams want to put these
coding agents in remote sandboxes so you
can scale how many GitHub PRs you you
work through and the like. But as you've
probably seen, the tools that you have
in your local workstation, your MCP
tools, your locally running applications
might not match what you have in a
remote sandbox.
And just a small shout out to uh agent
core. This is actually one of the
problems that we're very keen on because
we recognize that customers want to
scale their coding agents um and how
customers are actually running these uh
software development life cycles. So one
of the releases we recently did was
grant the ability to customers to SSH
into their um sandbox just to see what's
going on. And of course it's not really
a human who is SSH into your sandbox
anymore. or it's a coding agent who
you're developing with uh as well. But
the idea is there uh bridging into the
sandbox and poking around and seeing
what problems are causing your coding
agent or your application to not run as
smoothly is a pretty um stated business
problem for us and one that we're trying
to solve for customers.
And if you look a little bit uh if you
look a little bit at academia uh one
interesting example I think a lot of us
probably care about is whenever frontier
models come out the first thing we look
at is the sweet benchmark report which
is okay this model got XYZ percentage on
this three benchmark versus another and
there was a recent study made by some
researchers at UC Berkeley where they
found that given the right environment
controls and an exploit agent they
actually beat the three benchmarks like
reaching up to 100%. And in inversely uh
there was another study where um
researchers were trying to give a wide
set of business problems to an agent
with broken tools. Uh and of course the
effectiveness of that agent uh went down
greatly.
So I think this is uh mostly where I
want to aim to leave today which is as
these applications that we build today
are more and more agentic and they're
not constrained to a rest API service
that you you build for customers but
rather uh an arbitrary agent running
inside of sandbox it's really really um
uh challenging to find all the sharp
edges where the sandbox primitives uh
lead to you know a less efficient uh
ability for your agents to complete that
problem. So my challenge here for you
today is uh if you're looking to host
your agents on sandboxes, sure test it
locally, but also fuzzy test it with a
wide set of domain tests um remotely.
Yeah, thank you.
[applause]
>> [music]
