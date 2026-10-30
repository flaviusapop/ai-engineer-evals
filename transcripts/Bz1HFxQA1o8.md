# Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco

Source: https://www.youtube.com/watch?v=Bz1HFxQA1o8

Uploaded: 2026-10-20

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Uh when I was in the 10th grade, I had a
math teacher, Mr. Huff, who was uh
notoriously brutal on our math tests. He
would uh make us write our answers down
to the uh fourth decimal place in case
you happen to get to the answer by luck
or by chance.
And most of the credit for the question
was actually from the proof that you
wrote to show how you got to the answer.
And when I first started playing
AI observability software, uh
I realized that most of these compliance
and risk teams that I work with every
day,
they're kind of like Mr. Huff, but with
a a multi-million dollar compliance
budget.
And
I would let you know that playing agents
AI within banks takes a long
long time. And the reason is because
that keyword production.
I'm not talking about prototypes in dev
or staging or even like internal rag
agents to increase, you know, internal
employee productivity.
I'm talking about the applications that
these banks millions of customers use
every single day. The same ones you use
when you log into your bank's website or
mobile app.
And those are the use cases that matter.
In my team, we're on the front lines of
deploying not only our software, but
also engineering processes into the
largest banks in the world. And I want
to share some of the issues that our
customers bring to us
and the strategies we use to help reduce
the time to production from a year down
to a couple weeks.
So, let's take first take a look to see
how standard SaaS AI gets deployed at a
bank. Uh spoiler alert, it doesn't work.
There's outbound egress to the internet
and sensitive information can
potentially be leaked out.
Within
when you deploy on prem AI at an
air-gapped bank, the flow is a little
more complicated.
I'm going to walk through three pillars
today. Number one is the actual build
pipeline. How our banks pull images from
our software into their cluster.
If a region fails mid-request, what is
the data resiliency plan?
And then finally, one of the most
important parts is how do you ensure no
sensitive information leaks out to
internal bank employees and outside of
the the bank's VPC.
Compliance velocity uh and CVEs go hand
in hand. And
no platform worth their salt does not
have a plan for how they address this
first compliance hurdle, which is common
vulnerabilities and exposures. I'm going
to walk you through why this process is
complicated. So, number one, you can
take one CVE and you can research on the
NVD, CISA, or MITRE websites. But, in
reality, our platform, most platforms,
you have multiple images and each image
has multiple CVEs.
And I'm not trying to remediate CVEs for
one bank, but rather for multiple banks.
So, we have to create a system and
process around this. And the
complication there is that our banks are
on different versions of our images,
each with their own unique CVEs.
On top of that, banks utilize different
scanning tools, which output a report on
what CVEs are present.
Furthermore, they have specific policies
around what are the actual CVEs in the
images,
what the severity level is, and then
what the SLA is for time to remediation.
Our images rely on many open-source
projects and those projects contain many
transient dependencies which have CVEs
that our engineering team cannot
remediate. So, our team is we're
constantly looking into the release
notes for a lot of these open-source
projects cuz we have to provide a
detailed explanation back to the
security teams at these banks
on why we cannot remediate and why we're
dependent on these open-source project
maintainers.
So, once you've identified the CVEs that
your team your engineering team can
actually remediate there's multiple ways
of remediation. You can bump the package
version up to a higher version or
rebuild your image against the base
Docker image.
But, then we also have this complication
of certain banks saying we want to be on
version 3.8 of the package. But, another
bank might say hold wait, hold on. That
version is too too high. There's too
many CVEs. I want to be on an older
version of that package.
So, given all of this your software
still has to work and function.
And so, one solution that you can use is
creating a scale.
So, we have a scale that does a lot of
the heavy heavy lifting and reporting
and the
internal research as well.
And the output is a nice kind of table
format that has tells our engineering
team what CVEs we have to fix and also
provides explanations back to our
security teams from the bank on what can
we cannot fix due to these transient
dependencies.
Most of these scanning tools Sysdig,
Wiz,
Prisma
they just check to see if the package
has been bumped to a specific version.
But, it says absolutely nothing about
whether or not that exploit is actually
still in your application code.
And
so, how do you actually test for that?
So, one solution is creating a harbor
task and this is kind of like creating a
harness or a world for your for an agent
to try things out.
And so within this harbor task you have
instructions for the agent, you have an
environment which contains the actual
docker images for your application, and
then tests that you can run against the
agent to see if they passed.
The instruction here is a CVE for uh
this service, this package. And the
instruction I tell the agent is 2.6.2 of
this package
supposedly remediates the CVE. I want
you to go and write an exploit based on
the older version to see if this new
version still has that exploit. Then
write a test to see if that exploit
actually passed or not.
And then with harbor you can run a bunch
of docker containers or um harbor uh
modal or Daytona sandboxes, run these
all in parallel, and you have a bunch of
trials to see how the agent performed
over various trials.
And the What I'm trying to say here is
that it's not enough just to
say we bumped the package version up to
a specific number.
We have to provide the evidence to show
that the exploit is no longer actually
in the application code.
Uh the second pillar, disaster recovery,
is not like optional infra hygiene for a
bank.
The complication here is that the main
database platform most AI observability
tools use, including some of the
companies that are sponsoring this
conference,
there's no managed service for
failover across regions and data
replication.
Anyone happen to know what database
platform I'm talking about? It isn't
this So, with Redis, Postgres, there's
managed failover across regions,
but this one database
does not have that story.
ClickHouse is an amazing database
platform, but even in their data
resiliency docs they call out that
there's no managed service
managed failover across regions.
So this means the banks are kind of up
to themselves to to figure out that
disaster recovery situation.
So a simple pattern that you can employ
is you have ClickHouse in a primary
region,
a job that backs up to a bucket, and
then another job that restores that
bucket to a DR region.
Within that region, you might have
multiple pods that have replicas of that
data.
This whole procedure relies on
ClickHouse backup,
which is an open-source project
maintained by Altinity,
who they themselves are a competitor to
ClickHouse in terms of managing this
data failover across regions.
It's uh so with this procedure, they
ClickHouse backup shares logs on whether
or not the backup and restore happens,
so you can get this nice table.
But this status says nothing about your
data at this point in time.
A bad disk, a bad node, um bad
migration, replication lag, these are
all issues that can cause your data to
become stale, that is different from
when this job actually ran. So you can
go the extra step in checking the row
counts between tables,
uh running a check to see if the
replicas within a region have converged
to each other.
And the takeaway here is that it's about
data correctness, and not necessarily
just checking a box and seeing if the
backup and restore job ran. Similar to
the CVs, you can't just bump the version
and assume the exploit's gone.
You have to do these extra checks.
And uh one call out for any of the uh
architects who are creating this kind of
backup and restore within your cluster
is that you're also making a decision
around data residency, whether you like
it or not. When you're replicating to a
bucket, the bucket doesn't care if it's
in Oregon or Virginia.
Data residency, however, cares about
where those individual records are
stored.
So, one solution is you can
replicate just the IDs and the metadata
around your traces and your data
into different regions. But, then the
actual core trace data, that's stored
within one region and doesn't leave that
region
because of certain jurisdiction laws.
Uh the final pillar is most banks think
that they are not leaking any sensitive
information to their internal employees,
their users outside of their VPC,
but there may be side doors that are
open.
And this comes in the form of PII
MNPI being redacted. And there's many
different strategies for this. You can
redact information at the SDK level, at
the gateway level, using various
middleware.
And what this looks like in practice is
on the UI, you might have some customer
information,
sensitive information is redacted.
But, what about the judges that you're
using? I challenge all of you to look at
the system prompts for your LLM's judges
and check the traces to see if those
traces with the reasoning from those
judges contain any PII or MNPI.
Here's a system prompt for a simple
judge. It outputs a score and
explanation on how well the agent
performed for a given task.
But, there's one line here in the
prompt, which is seemingly innocuous
because you want the human reviewer to
be able to verify if the agent did a
good job and was accurate.
This just potentially may have allowed
the
judge to
leak and unredact PII or MNPI.
So, your UI still looks good, but then
on the back-end your LLM as LLM as
judges reasoning may
un-redact customer information and
sensitive information.
So, one strategy for this is you can
still have your judge read the raw trace
data,
but the reasoning for that judge is not
persisted.
The score, however, you want that score
it's for good good for evals, that
always persists through the UI, but then
on this other branch the reasoning, as
we saw, can still leak PII.
But in your application code, you can
have a check that tells the agent
this record does not contain sensitive
information and therefore can persist to
the UI. So, now you have a score plus
the reasoning
for the for this record.
And then if that check comes back
negative, it does have sensitive
information, then you just suppress that
reasoning from the UI.
Most of the banks we work with, they
want to see the LLM as judges reasoning
on this sensitive information.
And the extra upgrade you can add to
this flow is you have a second LLM as a
judge where the input has is redacted of
sensitive information and therefore you
can have confidence that the output from
the judge is clean and then you can have
that show up in the UI.
The uh takeaway here is that
having zero leakage and data sovereignty
is not free. In this case, it's the cost
of running another LLM call on the same
request.
So, one way we're able to build trust
with these security and compliance teams
is that we're not just saying trust us,
here's the answer. We have to show the
evidence and the work on how we arrived
at the at the answer. And many vendors
will tell you,
you know, we're
our deployment time to production takes
a few weeks,
but what they're not saying is they
didn't check that time against
your infrastructure, your security
posture, and the nuances about your
specific cluster.
And so certain signals that we look for
in terms of shortening that time to
production
is really just having a lot of processes
set up in terms of, you know, how you
pull images down from an from a
registry,
having GPUs sourced and ready to go for
running inference.
That timeline gets pushed out a couple
months when you have formal security
reviews, or you're building a custom LM
gateway or RBA configuration. And then
that timeline gets pushed even further
out
when you don't even have an approval
process for pulling images down to your
your registry,
and not having a not having a story
around sourcing and procuring GPUs. Now,
I found that most of these signals that
push the timeline out
are less technical and more about
internal
human and organizational challenges and
alignments at the banks.
Uh but still important factors to figure
out.
So, the theme for today is
showing your work. That is the real
lever that you have on compliance
velocity when working with a bank. And
when our banks, when one of our
customers come to us and tell us, "Hey,
our customers are having problems."
Those problems now become my team's
problems. And we break those problems
down into
uh engineering, workflow, and human and
organizational work streams.
The goal is to automate as much as
possible, but those problems are the
ones that keep me up at night. And I
want to ensure that our competitors
don't outwork us and don't outsmart us
on any of those vectors.
And I would say that you don't want to
just be another vendor, you want to
actually be solving your customers'
problems.
And I would say the biggest lesson I've
learned from working with these banks
and security teams
is that there's
so much at stake.
Checking accounts, mortgages, credit
cards.
Getting your answers down to the fourth
decimal place matters in these
situations.
And
there's a reason why a lot of the
software within these banks is old and
outdated.
But the the line between
legacy software and old banking
processes and innovation is moving a
little bit every day and it's because of
all of you.
So
I think all of you're, you know,
exploring different agent frameworks and
building with, you know, new harnesses,
playing with Jev.
And I would say for the few of you who
care about the
the slow, the boring, the bureaucratic,
the methodical, the messy human and
organizational challenges within a bank,
there's nothing like deploying AI
within the financial services sector
because there's so much so much at
stake.
And
yeah, if you all want to score your own
deployments against um these pillars,
just just reach out. I only discussed
three pillars today, but um
you know, there's a whole production
checklist that we use to
uh that underpins these pillars.
Going back to my 10th grade math test,
one of the best parts about those tests
were afterwards we me and my friends we,
you know, go to the lunch table and we'd
try to scribble down all the problems we
remembered from the test.
And then we use that time to talk about,
"Hey, here's how we approached solving
this problem and that problem." And it
allowed me to kind of think about
different approaches and different ways
to solving these problems.
And conferences like this are kind of
like that uh lunch table back from when
I was in 10th grade because I want to
learn from all of you on how you're
solving your your problems for for your
customers.
Thank you very much.
>> [applause]
