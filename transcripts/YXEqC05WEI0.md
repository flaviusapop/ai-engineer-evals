# Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health

Source: https://www.youtube.com/watch?v=YXEqC05WEI0

Uploaded: 2026-08-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Hello and good morning. Chetana gave us
a great overview of you know what a
bridge does.
Today I'm here to talk more from a
practitioner's view of you know how we
are building health care AI within Hinge
Health. So hi, I'm Rashi Agrawal. I lead
AI and ML at Hinge Health and today I
will be talking about guardrails that
are needed to build member-facing health
care AI.
I want to talk a little bit about the
state of health care AI right now. We do
have a lot of frontier models which are
running and believe it or not, 40
million people actually use these models
for triaging their health care issues.
But there is a caveat and these are some
of the headlines that have been
happening in the past few in the past
one year or so.
Poisoned by a chatbot.
Let's start with this one person. A
60-year-old healthy man asked a popular
AI assistant how to cut salt from his
diet.
The LLM told him to swap it with bromine
sodium bromide.
He did it for 3 months.
He landed in the ER with paranoia and
hallucinations.
Bromide levels 200 times the safe limit.
3 weeks in the hospital.
For what? For following diet advice?
Let's look at another pattern.
The first independent safety test of a
consumer health AI out of Mount Sinai
found that this health AI is under
triaging life-threatening emergency 50%
of the times.
Diabetic ketoacidosis, respiratory
failure.
And it told the people to go see a
doctor in a day or two.
The right answer was ER right now.
And this is in French.
In February, ECRI
the patient safety group that hospitals
trust to rank their top risks
named AI chatbot misuse as the number
one health technology hazard of 2026.
Number one on the list that they publish
every year.
So this is not this is not really a
frontier problem.
This is the production baseline that
we're working with right now.
So the question comes, how do you ship
AI to somebody who's already trusted you
with their health?
The next 20 minutes are all about that.
It starts with three non-negotiable
foundations.
One,
the constraint is the architecture.
Most AI safety failures in health care
are not model failures.
They are architectural decisions that
were made before even a single token was
generated.
Two,
deterministic rules belong above the
model, not inside it.
What can never be wrong
cannot be left to probability.
And three,
safety is a continuous evaluation layer,
not a one-time gate.
Launch of your product is where the real
risk starts, not where it ends.
That's the first part of what I want to
talk about today.
The second half is what happens when the
architecture is not enough
and a human has to make a decision of
what ships versus what holds.
>> [snorts]
>> Let's start with layer one.
Protecting PHI takes both
policy and architecture.
Policy tells you what to protect and
architecture makes sure that it actually
happens.
The first thing that changes when you
start shipping member facing health AI
is where PHI lives.
Most teams treat PHI as a runtime
problem.
Something to redact when a log gets
written to a dashboard.
That's the reactive version.
The architecture version strips PHI at
the pipeline boundary. At ingestion
before it ever reaches the data lake.
By the time the data is stored, the PHI
is gone.
So, a developer opens a dashboard
there's nothing to redact.
The PHI was never there.
The rest of the architecture works in a
similar way.
Production and non-production stay
completely separate. No pipes in between
because even a single pipe is all that
it takes for member data to leak into a
dev environment. And HIPAA laws are very
stringent, especially in health care.
You know, the regulatory bar is much,
much higher. So, you have to be very
careful about the architecture that
you're designing.
Another big thing access depends on two
things. Your role and your geographic
region. We all work with the teams which
are geographically distributed, but not
everybody has access to PHI. That is a
certification, a policy that is applied
to specific regions only.
An engineer outside the regulated region
cannot reach raw PHI at all.
And the compliance rules, HIPAA, FDA's
good machine learning practice, state
laws like Texas, Triaga, they are not
afterthoughts.
They are the grounding input in how you
actually design your systems.
You cannot slap on HIPAA on top of, you
know, an underlying system or an
architecture.
You start with it and let the
architecture grow around it.
When PHI is protected at the
architecture level, you're not just
trusting that the policies will get
followed.
You're actually relying on a system
that's incapable of certain failures.
Let's move to the layer two.
Probabilistic systems are great at
generation. We all know that.
However, they are unreliable for things
that cannot can never be wrong. So, the
rule is very simple.
Must not fail behavior belongs above
your prompt, above the model.
And what does above the prompt actually
mean?
It means that there is a code layer that
runs first
on every turn before the model even
runs.
The code layer is what makes your
irreversible decisions. The decision of,
you know, whether this is an emergency
escalation, should they be routed to
911, should a clinician step into the
loop. All of those are irreversible
decisions which need to lie at a
deterministic code level layer.
The model handles the long tail of your
conversations and interactions with your
members.
The picture to hold in your head is a
stack.
Code on top,
model below.
Every turn goes through the code layer
first.
Most turns do reach the model, but the
model never gets a vote on high stake
calls.
Here's how you can think about it in a
different way.
A model is not a guardrail.
A model with a system prompt is also not
a guardrail.
Code that runs above the model is
closer.
Even the labs that be build these
frontier models publish the authority
hierarchy.
Root, system, developer, user,
guideline.
Every layer above user is one prompt
injection away from being overridden.
If the labs themselves don't trust the
prompt as a security boundary, neither
should you.
>> [snorts]
>> So, what does live in this code layer?
Let's examine it a little bit. Let's
take three examples.
First, very very relevant to health
care, which is emergency escalation.
If a member mentions self-harm, suicidal
ideation, or an acute medical emergency,
the system must route to 911 or 988. The
model should not even see this turn.
Code runs first, decides, and routes,
and makes a decision right away.
Another example, intent routing.
Which capability in your underlying
multi-agentic system, multi-agentic
architecture handles a conversation
turn?
Is it clinical? Is it tech support? Is
it education from the millions of, you
know, credited articles? Is it exercise
recommendation?
The model can help to classify, but
high-stakes path must must again take a
deterministic route
at the top itself.
You You don't want like a clinical
question quietly being routed to your
generic tech support agent. That's
unrecoverable.
Third, identity verification.
Anything that touches member data has to
check that the right member is at the
other end.
That's an authentication check. And
authentication is a security bound
boundary. Prompts are not.
The underlying pattern across all three,
code runs first. Code makes the
irreversible decisions. The model
handles what's left.
Last but not least, layer three.
As we all know, safety is not a gate you
pass once. It is a continuous layer that
runs the whole time.
Most teams treat evals as a pre-launch
checklist.
You run your tests, you ship, you move
on.
That's necessary, of course, but that's
hardly enough.
What actually holds up in production is
judges that continuously keep scoring
real conversations as they happen.
Not a saved golden data set.
Live traffic.
Scored on a lot of dimensions all the
time.
These signals come from three sources,
and each one catches something
different.
First, automated judges. 30, 40, name
it, you know, as as much as you can
scale. Automated judges with multiple
dimensions, always refreshing.
Clinical accuracy, safety, escalation,
relevance, drift, refusal, etc., etc. I
can keep going on. But you you get the
point.
These are the automated judges that are
always going to catch regressions and
any even sensitive drops in quality.
Second,
your gold mine of information. That's
going to be member feedback.
Thumbs up, thumbs down on each and every
single message. That's the truth signal.
That's your member communicating with
you.
And it's the only one that comes
straight from the person that you're
serving it to.
It catches tone problems and things that
judges miss.
>> [snorts]
>> Third, sample traces. Random samples
spread across capabilities with
high-stake cases checked every single
time. 100% sampling on those.
Ultimately, people need to read these
signals.
People are going to catch what no single
metric is going to catch.
And here's the part that nobody really
warns you about. The bottleneck is not
the compute, the models, the capability.
It's actually having enough people to
read the signal and act on it.
One more thing about layer three.
Some failures, you can't just prompt
away.
You ship the fix, it comes back under
new conditions.
New prompts, new tools, the model
shifts. You ship the fix again.
Each round buys you less and less.
The rate never hits zero.
At this point, monitoring is not a last
resort. It is the first resort, which is
always on.
A new failure that you see in production
simply means you now have a new judge.
Your underlying architecture and your
system needs to be able to keep scaling
with new judges, new monitoring as you
keep scaling your, you know, consumers.
And [snorts] that's the point.
Monitoring is how you know that the
architecture is still holding.
>> [snorts]
>> But monitoring also tells you when the
architecture is not enough.
And when the architecture is not enough,
a human has to decide.
And this is the second part of my talk
where I want to focus on the decisioning
frameworks.
>> [snorts]
>> Let's take an example. You're about to
ship, you know, uh consumer AI again in
the healthcare space, and you have a
feature, a specific capability that
you're about to launch.
And there is one issue left on the board
5 days before your launch.
And you have multiple different
stakeholders.
Five stakeholders look at the same
issue.
Each one sees a different risk.
And they don't agree what to do about
it.
Clinical sees member safety risk. They
want to hold the launch.
Legal sees regulatory exposure.
Compliance sees audit risk.
Product sees adoption risk.
The If the If it ships broken, the
feature won't land.
And engineering sees velocity risk.
They can't fix it without slipping the
date they want to ship.
Five rational people,
five different risks, and five very
different fixes.
So, what do you do? Do you hold the
launch and fix, or do you actually ship?
The next slide is the framework I
actually use for making these decisions.
Five rules.
This is how I think about decisions when
stakeholders disagree.
Rule one.
Worst case always wins.
Severity is set by the worst possible
plausible outcome, not the average. And
this is extremely relevant in health
care.
A bug that lightly annoys 100% of users
is way less severe than one that could
cause serious harm in 0.1%
of cases. This is non-negotiable.
The worst case matters more than the
average case, always.
So, when you're triaging, don't ask,
"How often does this happen?"
Ask,
"What's the worst version of this?" That
sets the severity.
Rule two.
Severity is not capacity. This one keeps
politics out of it.
As we all know, as we ship features,
there's always a little bit of
contention between timelines, features,
deliverables.
But, a bug's severity comes from the
harm that it causes.
Not who owns it, not whether your team
has the capacity to fix it, not how hard
the fix is.
You have three options in front of you
at this point. Fix, delay the launch,
or accept the risk with explicit
sign-off. Those are the three.
You never quietly downgrade a bug just
because you can't get to it.
Rule three,
asymmetric default.
When you don't know what to do, always
pick the safer mistake.
And there are two spectrums to it. One
is safety bugs and polish, the other
side is polish bugs.
For safety bugs, the math is one-sided.
Shipping a real safety bug is much worse
than delaying for a false alarm.
So, for safety bugs, when you're not
sure, always hold and fix.
On the other side, for polish bugs, the
math runs the other way.
Delaying a launch
costs more than shipping a small flaw.
So, when you're not sure, ship in case
of polish bugs.
Ultimately, the framework doesn't decide
for you. It just tells you which way to
lean.
Rule four,
revealed risk tolerance,
not stated risk tolerance.
Your launch bar is what your org already
accepts in production,
not what it says it will accept.
If a behavior has been live in your
existing product for weeks, months,
without escalation, without member
complaints, without leadership concern,
you cannot you cannot call it a launch
blocker just for a new thing.
Your stated risk tolerance might be no
bugs in production,
but your revealed risk tolerance is
what's actually shipping today.
Calibrate to the revealed one. That's
the floor.
Rule five,
humans are the constraint.
Judges scale.
Pattern interpretation doesn't.
Always, always design for human in the
loop.
Judges code traces automatically.
Dashboards refresh every few hours.
None of that is hard anymore.
But what's hard is having enough people
to read the signal and act on it.
One more piece around this.
Fast follows are committed debt, not an
optional backlog.
If you didn't ship it at launch, it's
not a wish list item. It's already
committed.
The five rules tell you how to decide.
But they all assume one thing.
That your underlying signal is true.
So here's the discipline that needs to
come first.
In a non-deterministic system, the judge
is also non-deterministic.
Before you trust the score, verify the
scorer.
And here's what it looks like in
practice.
Say you're watching a clinical accuracy
judge in production.
The score has been steady for at 4.9 for
weeks.
Today, it drops to 4.5. And tomorrow, it
stays at 4.5.
The immediate instinct is, let's start
changing the prompts. The agent is
broken. Let's fix the agent. That's
reactive.
And it's risky.
You fix one thing and you break another.
Worse, you're changing the agent based
on a signal that might not be true.
And the discipline needs to be
different.
First, ask whether the judge is right.
We can solidify that with a with a
concrete example.
Uh let's take it side by side. In
scenario A,
same question, member asks about
caffeine. The agent gives FDA standard
guidance. 400 mg for most adults, less
if pregnant or on certain medications.
The judge flags it as a hallucination.
Because the agent mentioned pregnancy
and medications without checking.
But that's just clinical context.
The judge is over calling in this case.
Fix the judge in this scenario.
For the same question, scenario B,
the agent says 1,000 mg a day is fine.
That's well above the safety limits.
The judge correctly flags it.
And the agent is wrong. In this case,
fix the agent.
The rule is always ask, is the judge
right before changing the agent's
response?
Fixing a judge prompt is not cheating.
Judges are software, too. And they need
to continuously evolve.
This is what production discipline looks
like when the system is not
deterministic.
Here's the whole talk in one slide. If
you screenshot one thing, this would be
it. Six takeaways, three from
architecture, three from decisioning.
On the architecture side, the pattern is
very simple. Don't X what you can Y.
Don't policy what you can architect.
Don't prompt what you can code.
Don't gate what you can monitor.
On the decisioning side, the pattern is
how humans decide when the system
cannot.
Score by the worst case and default to
the safer mistake.
Calibrate to your org.
And always design for the human in the
loop.
Fast follows are debt, not backlog.
Yes, building guardrails first is slower
than bolting them on later.
But that's the design, not limitation.
We are not building a generic low-stakes
chatbot.
We are building a system that has to be
worthy of someone's health.
The architecture is how,
the decisioning is when,
and member trust is why.
Thank you. Let's continue the
conversation on LinkedIn. Thank you.
