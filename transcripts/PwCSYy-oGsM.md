# Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI

Source: https://www.youtube.com/watch?v=PwCSYy-oGsM

Uploaded: 2026-10-12

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
Morning.
I'm Michael, head of developer community
at Druid AI, and this is Dan, our
co-founder and chief product officer.
Quick context on who we are. Uh, Druid
is a conversation AI startup with
hundreds of customers across EMIA and
Americas and we've been around for a few
years. And because we sit with so many
customers putting agents into
production, we hear the same question
over and over again. How do we actually
tell if our AI agent is effective? Which
numbers matters? Which artifact should
we inspect?
There was no clean answer out there. So
we built our own reference model and
measurement framework and we use it to
help our customers evaluate their
agents. And one of the ways we explain
it to our customers is a simple analogy
uh interns, right? Who doesn't love
interns? So that's exactly how we'll
walk you through today on this session.
So here's a scenario. Uh let's take a
business scenario, right? You're a
manager at a banking customer service
center and hire two interns for the
summer. Same team, same job description
for both interns.
By August, here's what their dashboard
says, right? Intern A contains 80% of
conversation, escalates 20% to their
senior bankers. Intern B contains 96%
and escalates four almost nothing and
dashboard is green. Now you have one
return offer to give. Who gets a
full-time job offer? At first glance,
intern B looks like the obvious hire
here, right? Intern B hired handle
almost everything alone. Didn't keep
pulling their senior bankers into a
conversation.
But surprisingly, offer to intern B is
the wrong offer.
Here's what had actually happened with
intern A as an example. The customer is
authenticated at 7 a.m. on a mobile app,
asked what it would take to uh ask what
would it take to pay off a mortgage
early. The agent can answer the math,
pull the balance, run the calculation
and give a complete response
contained in every definition. But that
question is a signal. The customer is
rethinking their mortgage. That's a
refinance. That's a real revenue on the
table here. So the bank writes a rule,
answer the customer, then route the
context to senior banker. That design
handoff is part of agent A's 20%.
The metric doing this is a containment
uh the percent of conversation handle
without a human. It's easy to measure
and it's on every dashboard.
This is the exact gap our customer kept
hitting and it's why we built a
reference model and a scorecard and
Dan's going to walk you through that
framework.
>> Thank you. Thank you, Michael. Um this
is the framework that we build
because our customers and prospects
asked us
how do you know that the agent our agent
it's delivering to the job? How we know
that the agent is effective?
So we build this framework sitting on
six pillars
splitted in two groups
with governance across all these
pillars.
The configured group, it's what the
agent is built off, what exists before
the agent runs.
Under the runtime, it's what the agent
is doing at the runtime. What tasks
creates, what tasks execute, and what is
the output
across all these groups. It's
governance.
From the business perspective,
what is the expected boundaries? And
under governance,
we observe and we monitor error
tolerance,
risk, very important, compliance,
observability,
accuracy and hallucination and tone and
sentiment.
all together
26 components that are observing and
analyzing
the agent behavior
as a whole.
So with that framework,
you stop debating
whether the agent
feels ready and you move the discussion
based on the facts and you level the
field and you can take a decision based
on mathematic rules. So let's dive into
it.
Each individual component
it's scored on three levels. It's get
zero if the respective component is
missing
doesn't exist. It it gets one point if
we can measure it. We can absorb it,
observe it and we can measure it
not to that not necessary automatically.
So I can observe it and measure by hand
equally good like it is the risk defined
what is the risk I can read it I know it
and the best gets two points in score if
it's managed managed means it's tracked
it's observed
and analyzed over time because
everything it's in a dynamic What
happens yesterday might be different
today.
And
to accumulate all these different
metrics, we wave them based on the
importance. And you observe that the
governance
cluster is the most important because I
am analyzing the effectiveness of the
agent from the business per perspective.
they produce the expected business
outcome. So the governance group gets
39%.
Further on the mandate and we will see
what it means gets 26%.
Platform 12 outputs 9 and so forth. And
you will notice that the technical
aspects are measured are contributed but
are weighted lower because we focus on
the business effectiveness of the agent.
Based on this metrics, we will see that
a green containment
that at the beginning looks the winner,
it's based on a fact and can be a very
different outcome when we measure all
these components.
Let's look a little bit inside each
cluster.
governance
super important and many times
it's forgotten to be approached from the
very beginning. We focus on the
technical aspects and then we tend to
observe the business effects afterwards
with this framework. We start with that.
It helps a lot in the envisioning phase
as well. Choosing what functional area
to approach with AI and I see in my
projects literally departments competing
who should come first because they have
a mandate from a board you should absorb
AI. So all of them are looking to do it
and the framework helps them to decide.
So anytime I'm defining an agent, I
start setting his boundaries. What is
accepted
tolerance? And you might say
zero. I want to be perfect.
I want to be 90%, we know that AI is not
always perfect, but sometimes 50% is
good as well. In autonomous agents, I
want to have a higher target because
there is no human in the loop. Should be
perfect or cancel the job. But in a
humanto AI collaboration,
I know that the final decision is to a
human. So AI is creating content and
then human decides. So 60%
error tolerance might be good
risk.
It is the risk defined.
I am in synergies with all the other
departments. So I know that my agent
should run under this risk uh uh
blueprint. I need to look somewhere and
have these risks defined. And uh if you
look at the numbers the agents we
measure in here are good 97%
because there is risk compliance defined
for this agent.
Compliance it's good. We evaluated the
agent is compliant with sock 2 and back
policies. So got a good score.
Observability it's also good. I look the
agent is logging everything
from input reasoning decisions and then
call integrations everything is logged
good score on there drift
good score we are still in the
boundaries in the base established for
with the first go live date it is
measured and tracked
accuracy
3% hallucination
part of them automatically determined
other set manual annotation but
altogether
accuracy it's measured and tracked and
tone and sentiment because these agents
are conversational agents I observe and
extract the tone and sentiment from the
conversation so all together you see
how many seven very important metrics
measured
agent mandate super important I know we
have the system prompt which says the
boundaries but it's just this is just a
part what is the agent definition what
this agent should do the other things
unlimited scope should not be done by
the agent so hallucination control
what's the business impact Why we are
doing this agent? We are not just
experimenting technology. I expect this
agent to achieve 70% contract renewal.
This is an ROI. We will measure it at
the end to judge the business success.
What are the policies boundaries
based on what facts my agent should
reason? Isolated context. These are the
documents. These are connected systems.
security,
what systems this agent is allowed to
engage with. Super important. I want to
sleep at night knowing that my agent is
only accessing these three endpoints. I
don't give give him access to an MCP
server with 4,000 tools and I don't know
what he's doing. Isolated context. And
secondly, who is allowed to engage with
my agent.
And last but not least, I want to stay
in the budget. I don't want to have the
surprise that one week later, my agent
consumed 20K
with whatever resources he engaged with.
So all these five pillars
creates the agent mandate.
platform capabilities.
We want the agents to work together.
We don't want the agents to reinvent the
wheel. If one agent is performing good
because he is managing right the memory,
humans handoff and orchestration on his
skills, I want all the agents to behave
the same. So I am measuring that as
well.
very important handoff. I don't want
each agent to handle his own handoff. I
want to have a central action center
where people are engaging with all
agents in my organization. So I am
evaluating if each particular agent is
talking with this superior uh service.
I'm getting more into technical topics
which are contributors to the overall
score but all of them are under
governance and the business purpose. So
yes there are skills defined but how
granular, how discoverable they are, how
orchestrated, how thin or how large it's
the uh the prompt combining multiple
skills
are the skills coming from a central
repository are built on the spot or are
human coded.
What tools are available? You will see
at the final judgment that the performer
agent is not the one with the largest
number of tools.
It is with the effective uses of tools.
So very important this aspect as well.
And with this I concluded the
definition. But what happens at the
runtime? I need to log.
I need to create tasks based on the
mandate and then execute the tasks. Are
the tasks written? Is the input logged?
Is the required context present? How do
I know
it's the success criteria created
together with the task? Because if I
look and I see that the agent renewed
the contract, I want to measure if that
renewal was successful or not. If I
don't have the success criteria linked
with that individual contract, it will
be impossible to judge. So the agent
should explain everything he's doing.
This is what the task topic is.
And at the end, I want to validate the
output. there is one single score that
evaluates if the agent was successful or
not.
So in summary,
combining
all these metrics,
agent A scores 83%.
If you remember at the beginning, his
containment was 80%. Escalated 20 times.
Agent B escalated just four times.
However,
observing and measuring the governance,
the mandate, the final outcome,
the final score, it's in favor of agent
A. And if you look at the clusters, in
each individual cluster, A was better
than B except the skill. B had more
skills but was lack in explanability
in tracking success and compliance with
the governance. So all together this
framework gives the true winner
Michael back to you.
>> Thank you. Thank you Dan.
So those seven pillars and the scorecard
uh that's the framework and this is a
framework that we've used uh with
multiple of our customers and it's been
working out really well for us and what
customers typically tell us is that hey
they finally have a some sort of
framework that they can use to measure
the effectness of the agents that
deploying and be able to have a
discussion intelligent discussion with
their business stakeholders. So here's
where going back to the inter uh intern
metaphor breaks right in your favor. Uh
when you hire a person, the interview
ends, right? But when you hire an agent,
it never ends. You rerun it every week
on a live traffic against a human
baseline instrument, evaluate, improve,
retest. Again, going back to what Dan
said earlier, the drift, right? The
green line you see on the right here is
the um the vanity dashboard as flat 92%
all year. The teal line is the wheel
score sliding from 83 to 60 because
you're measuring it on a weekly basis.
So same agent, same green dashboard but
different metrics across the time.
So now one of the things especially if
you once you start to engage with the
business stakeholders let's say your CFO
or something you know the first first
question comes out is the is the ROI
right and the and the fear sets in the
fear is that only measurable thing about
an agent that you're working on you're
deploying is like whose job is it does
it take away from right and that fear
survives because the we mostly haven't
measured the alternative alternative. So
here's a reframe that we try to
typically work with our customers. A
good intern lightens your workload. The
routine works moves off to your desk and
you get sharper at the work that's left.
Right? Same test for an agent. What did
it take off of your plate and what did
that free the time to allow your
business to do? Right? The agent hands a
balance check at 7 and 9. So the banker
spends next morning with the customer
who's rethinking their mortgage. The
agent made the banker better at banking
and that's the column belongs on your
scorecard and that's some of the things
that we try to work with our customers
as well.
Now a a confession to make about the
opening the intern was never
hypothetical that 8020 split was a 2026
root AI adoption benchmark for financial
services. So everything you just heard
is backed by our anonymized aggregate AI
agent production data. Uh the same
metric containment four different
industries four different right answers
financial services at 80 healthcare at
87 HR and IT at 93 and higher education
and 99 containment rate. Now when you
look at the data higher ed isn't better
than banking. banking just design more
handoff in their agenting AI design
that's what you wait the outcomes per
agent against one universal number the
numbers different across different
industry this is the druid 2026 AI
adoption benchmark uh we gathered 15
months of the production AI agent data
and uh it contains many useful data uh
across different industry as well it's
free to download and if you Look at the
next slide here. this slide uh this is
where you can um QR code you can scan it
you can uh download the report and it's
the framework that we developed is
really about defining the mandate
contract the boundaries score the whole
agent run it weekly uh against the human
baseline and that's a framework that we
typically uh work with our customers to
kind of so we wanted to present it you
all kind of share the framework free to
use and uh one Last thing is uh we're
located at the booth LG11 right across
from OpenAI Microsoft booth. So feel
free to come by and I would love to have
some conversation with you all. Thank
you very much.
>> Thank you.
>> [music]
