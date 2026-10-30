# How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase

Source: https://www.youtube.com/watch?v=_4Ph2dhmUFI

Uploaded: 2026-10-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Hi everyone.
My name is Evan Cormos. I've been
delivering, designing, building software
for 20 years. The last 15 in enterprise
financial services.
I am a player coach at Coinbase.
And we're here today to talk about
trusting agents in policy-driven
workflows.
So, let's start with the policy and it's
pretty boring.
Um,
I'm going to go over here for my notes.
So, our starting point center centers
around the policy and
this sets the rules for how work gets
done within the organization and
including especially risk and
compliance.
Think of policy as the original
institutional intent
or the original system prompt.
So, ideally we have this written down.
Um, it's a little bit boring, so stick
with me.
Um, using language like must, may, and
should.
And the again, these help define the
rules and decisions about how the system
operates
in the organization.
Separate from policy, we have the actual
running system.
So, the first thing we're going to do is
separate these two
uh
these two both the build state and the
run state in two different moments in
time.
So, typically we're either defining or
chaining changing our policy
but this the system is constantly
running and it's constantly moving and
changing.
So, we could then sort of imagine a
compilation event that Oops, sorry. I'm
skipping ahead there.
It's constantly changing.
So,
it's evolving quickly with these
product-driven changes. So, everything
is expected to still be roughly bound by
the policy, but ultimately um
we separate this from the run state and
the build state.
So, inside the system,
what does it look like? We have a
familiar model if we have any enterprise
uh folks in the in the room here.
Um people, process, and technology.
But, where really do agents fit into
this model?
Um so, I see them as an operational
model cutting across all three.
They work with people, execute parts of
the process
themselves, and they use and are made up
of technology.
So, for our talk today, we're going to
be focusing here where agents meet
process.
What work we give them, what boundaries
we set,
and how we build trust in their outputs.
So, let's dive into your workflow.
And it's high-level and seems basic, but
if you haven't, there are good reasons
to map this out.
So, maybe a change has to be approved
before it goes live, or a customer goes
through has to go through verification
before their account is opened.
We expect work to flow in a specific and
gated direction.
So, I believe it makes it agents make it
worth revisiting what we can do in
parallel.
So, previously some work used to cost
too much or be too complex to coordinate
in this way.
But now we can run independent reviews
alongside each other, bring the results
together, but keep the required checks
in place.
So this is a directed acyclic graph or a
DAG.
It is a way to represent this workflow
or process, the steps, the dependencies
for a flow that moves forward without
looping back on itself.
Apache Airflow, if you're familiar, is
an example of open source software that
represents workflows,
their dependencies as DAGs in Python
code.
So
this Python code, this these DAGs can be
used to define and manage a number of
policy driven processes like, for
example, commercial lending.
We could also use a DAG to represent the
workflow to list a token on the exchange
in a specific region, if you're into
that.
Or we could use a DAG to represent a
regulated flow of delivering software,
which is a hot topic.
And one we'll spend a little bit of time
on, I think that
we've seen a lot of adoption within
agents, within software delivery, and
ultimately we're looking to leverage
that same
efficiency and scale in other areas of
the business and close that the the
adoption gap.
So let's stick with the
software delivery example for a little
bit.
What happens inside one of these nodes
of the process? And
I'll give you a hint, it's a loop.
>> I'm oversimplified, but we have a basic
version of what's happening within the
Let's Let's say this is a code review
process, right?
So,
we're going to essentially
do a number of steps and essentially
once we realize the work we recognize
that the work is good enough, we're
going to allow it to pass on to the next
step. And that's essentially the
function of the code review node.
The work doesn't always uh end up okay.
So, sometimes we have to take the
feedback from the code review and
iterate on it um until the work is a
good enough to pass.
So, this is a representation of a
directed cyclic graph or DCG.
So, as far as open source software, uh
something like LangChain LangGraph would
be what I would
um
say is helpful to manage the state of
DCGs.
Um and this is an oversimpli- an
oversimplification. These graphs can be
very complex.
So, zooming back out,
the inner flow um of the node, we have
people and agents working together.
On the outer flow, we have a policy
boundary.
But not everything goes to plan.
Um so, we have to handle exception
flows. We don't want the work to get
stuff stuck, and we don't want to design
for every edge case, either.
Um the exception flows will monitor and
see kind of what happens if you're
shipping code that gets canceled or
doesn't meet security standards, that's
something you would should want to know
about.
Volume shifts across the flow once we
start to add agents into the mix and
we've seen this with software delivery
and we'll see it in other processes as
we bring agents into those processes as
well where now all of a sudden if you're
reviewing code faster
you need to design it quicker or you
need to do the security scan that's
faster. So we see the volume shift
across the flow.
And this is where it's really important
that we have visibility into the process
overall from a a metric standpoint
because as we start to supercharge and
and
parallelize and add more efficiency to
the process we start to develop more and
more bottlenecks and so the operational
visibility of the process is extremely
important much more important than the
authoring and the building of your
workflow tool.
Um so we want to visualize the process.
So we want to add parallel capacity by
still keeping the controls and so this
is where we'll add more additional
capacity.
Okay. So we're doing some work we're
checking it we're using the feedback
again to refine it until the work is
good enough to move on.
But why is that hard? Oh it seems like a
pretty easy thing to do.
But as I mentioned before these graphs
get actually pretty complex
and we'll dive a little bit more into
why this is difficult.
And if you're familiar one challenge
with AI engineering is the variability
of inputs and outputs and
I believe that higher quality inputs
will result in better outputs at a lower
compute cost.
But what are quality inputs?
>> So,
we would generally speak to it as
context
model maybe. We can nitpick that, but
this isn't our area of focus today.
We're going to focus more on outputs.
But, we can't really talk about quality
of outputs without the quality of
without talking about the quality of
inputs.
So, ideally we've established a trusted
context for our agent.
Um and there's some references on that,
but one thing we can do in this model is
inject the DAG state into our agent and
let it know kind of where it fits into
the bigger picture.
Okay, so
now we've added even long time horizon
goals and that's emphasizes the need to
optimize the cost and efficiency of this
loop.
So, the check is where we decide whether
the work is good enough to move forward.
We need to define what good looks like.
That's the hard part.
And we need to have a reliable way to
evaluate it. Otherwise, more passes
don't necessarily
uh mean better results. The loop is
really only as trustworthy as the check.
So, if we want to talk about quality,
let's talk about the check and let's
talk about quality.
Okay, um I think building
with AI is an opportunity to improve
product quality overall. I like some of
the conversation about durable software.
Um
So,
I'm a believer in quality
and in traditional software
um we we built confidence mechanisms in
place
uh to give us confidence that the
software is of high quality.
And that's done with a variety of uh
mechanisms, but primarily systematically
with test cases, unit tests,
um checking these as a part of our
delivery flow to ensure that when we
make code changes, mistakes aren't made
that break other things, right? So, this
is a confidence mechanism that we've put
in place with traditional software.
The agents are probabilistic, and so the
same request can produce
different answers.
More than one answer may be acceptable.
And we still need evidence, but exact
output
uh comparisons alone really aren't good
enough.
Uh we need to build a representative
data sets and evaluate them
um
and define what good looks like.
We need to run uh
ev- these evaluations in repeated uh
series, and this is a statistical
analysis, right? Um where we actually
look at the outputs
uh and in volume and not just as a
direct comparison.
So, in combining with evals is sort of
your run time logs of what happened, or
sorry, traces, uh wh- which are sort of
your run time logs of what happens.
Um we've built this confidence mechanism
to complement um traditional software.
And ultimately, this is what we're going
to be talking about a little bit more in
in terms of driving confidence in the
output, not only putting this mechanism
in place, but how do we begin to turn it
on?
So,
where does the agent belong? Um back to
the lending example, like we can do KYC,
financials in parallel and sequence like
credit memo, risk review, documentation,
decision, all these things in our our
DAG. Um looking at each node, we want to
ask some certain questions like how
valuable would it be to have an agent
drive this node versus a human drive
this node? Um and we can sort of look at
some of these basic questions like can
we check it against the policy easily?
Can it run in a bounded loop? Can we
trace it? Can we fall back to a human?
Um if we can answer yes to these type of
questions,
and we we can kind of have a good idea
going in that this particular node may
be better suited for automation. Um but
throughout the DAG, we should look to
drive agent assistance. So, what we're
really talking about is not whether or
not AI is involved, but whether or not
AI we expect to take over at some point.
On the decision, you would probably
agree that we probably need that to be
human-driven. This is essentially the
check against the policy. Um so, this is
going to be a little bit more difficult,
I think, to hill climb.
But what do we mean by hill climb?
All right, how do we turn this on?
So,
day one, um we start supervised and
as we have agents and humans working
together as a part of the process, we
can
um manually um verify the output to
ensure that it is high high quality.
Um this is where we refine our data sets
and ensure that we have the right
confidence mechanisms in place. We've
defined what good looks like with the
domain subject matter experts and that
they're beginning to verify it.
When measured confidence reaches a
policy threshold, we can move towards
sampling. And what that means is humans
are looking at a slice of the output and
not necessarily all of it. Um we begin
systematic more systematic evaluation
through traces
Um in order to ensure that what we're
what the humans aren't seeing is still
meeting the quality bar.
And then finally, once we clear the
confidence threshold, humans handle more
of the exceptions of the process, but
still acting as participants in refining
the data sets and ensuring the quality
outputs.
Okay, so a few takeaways from this.
Um
DAG and DCG,
basic graph theory, but ultimately, how
do we build these processes that exist
today and where people are working them
and bring agents into the mix. And the
recipe really is to keep it
deterministic on the outside and make it
adaptive on the inside.
The next is quality through evaluation.
And this is really establishing a
complementary confidence mechanism.
So, it's not a feeling about a model. We
can actually provide research and
statistics about the quality of our
agents.
So, this builds confidence and
inherently trusts output.
Quality is a team sport.
AI engineers own the pipeline
to taking product signals
from all directions
and deliver applications that are well
built and utilize ML operations behind
the scenes.
Finally, agents accelerate
across the operating model.
I've included some references on the
final slide of things that I've spoken
about today.
This concludes my presentation.
Thank you very much.
>> [applause]
