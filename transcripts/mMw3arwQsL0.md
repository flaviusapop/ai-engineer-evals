# 1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah

Source: https://www.youtube.com/watch?v=mMw3arwQsL0

Uploaded: 2026-10-22

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
A big part of my research is uh looking
into AI failures, investigating it, and
then learning from it. And joining me is
Tanmay Shah.
>> Yeah, hi everyone. I'm Tanmay Shah. I'm
a senior quantitative modeler and an AI
researcher. This is my second time here,
so it's great to be back. So, I will
hand it over to Vishal to get us a
started.
>> So, uh we looked at AI incident
database. It's a publicly available AI
incident database. And uh we looked at
um the AI failures and asked one simple
question, what these uh failures um
uh teach us about how the sys-how the AI
system should be evaluated and if we can
um apply those learnings to system level
evaluation.
So, the first thing that we see is that
AI failures um have been increasing
exponentially. And if you look at um the
last four um years of um AI failures,
particularly in the foundational model
era, you see that the jump is almost uh
vertical.
Um and many of us feel that um
uh the number of AI use cases that we
have in enterprises, um they um they are
much larger than our capacity to review
them each one by one. So, what we argue
is that we need a structured way um to
investigate these AI failures.
And to do that, um we look at the AI
failures essentially into three
dimensions. The first dimension is the
development stage when um the model and
or the AI system is uh developed. So, it
could be issues with respect to
data quality or tool architecture or
system design. Any of these things
during the development phase can
can break and once it happens, then
those errors can be propagated to the
next dimension, which is the deployment
phase.
Now, even if the model or the system
has some faulty design issues, but if
you have sufficient controls in
deployment, those errors can be
contained. And that is why it is very
important to kind of understand what
kind of controls do we have in
deployment and whether
we can contain those failures from
reaching from deployment production
platform to the final stage, which is
the context in which the AI system is
being used from a business standpoint.
It could lead to
reputational risk. It could lead to
legal or financial risk and all those
business context really matters
for the AI system in which it is being
used. And what we say what we propose is
that the model alone or the technical
strength of the model is just one part
of the system. We have to look at the
system holistically.
So, after defining those three core
dimensions, the technical strength where
the system
should be strong or in opposite way
where the system can break,
the second dimension is how do
we ensure that the deployment controls
are in place. And third, the business
context the AI system is being used. We
divide each of these core dimensions
into
several sub dimensions.
So, in the from the technical strength
point, right? There could be six major
sub dimensions which could be affecting
the technical strength of the AI system.
It could be
first related with the data quality that
we use for to build the AI system. How
the system has been designed for the
appropriate task that it is supposed to
accomplish. How is the predictive
validity or outcome analysis of the out
of of the AI system? Does that system
perform as we intend?
Um there could be fairness related um
checks.
Um failure modes essentially looks at
where when, how, and for whom the
uh system can break. Uh so, basically
mapping out all the failure modes of the
system. And finally, can we explain for
uh explain the decisions for the
regulators or other bodies
uh so that we know how the system is
arriving at its decisions. So, these six
sub dimensions are essentially part of
the technical strength of the AI system.
The next four are essentially looking at
how we are using the model. Um what kind
of authorities we have given to the AI,
right? Is the AI for informing us or it
it is out there to act on our behalf.
What kind of decision authority are we
associating with respect to AI? Uh
second one, human mediation. Um how
effective is human in the loop process
is, right?
That's really important. The third one,
exposure control. Who's actually using
the uh system? Is it internal employees
so that they see the error and they can
contain it or it is exposed to the out
there in the wild external customers so
that any small issue can really
propagate fast. And finally, what kind
of monitoring uh controls that we have
so that we see some uh issues in
production and we detect it and we can
contain it.
Finally, in the financial
or the business impact phase, we see
these three core sub-dimensions. What
kind of financial impact it would make
if there is an error? There could be
legal consequences and how many users
would get affected? That's the the last
one, the scale sub-dimension.
So, we
we we look at this this as one framework
which has 13
dimensions and three core questions as
we explained.
Once we define these 13 sub-dimensions
and look back at AI incident
retrospectively, we find that using
these 13 sub-dimensions, almost 98%of AI
failures can be covered.
Meaning that AI failures
are are associated with some of these
dimensions, in some cases multiple of
these dimensions, and in some cases few
of these dimensions. But, these
dimensions are involved. So, failure
AI failures have structures. We need to
map it and we need to act accordingly
according to these sub-dimensions.
Now, as I mentioned that some of these
failure sub-dimensions can be present in
these failures simultaneously. Meaning
that when something goes wrong with
respect to a particular failure, there
may be multiple things going wrong. What
we find is that on average, there are
six failure sub-dimensions that can be
present
in each of these AI incident failures
that
we we we have investigated.
Now, the question comes to our mind is
that are all of these sub-dimensions are
equal
or some are more important than others.
And the answer is that
some of the sub-dimensions can be more
critical than others. And what I'm
showing you here in the in the plot on
the Y axis is the association to harm
when these sub-dimensions are present.
And on X axis, we have the frequency of
these sub-dimensions being present. What
we see on the left upper side of the
plot,
sub-dimensions like human mediations or
effectiveness of human in the loop, harm
detection, meaning that whether we have
monitoring control in place. On on X
axis, we see things like scale and
system design. Although they are present
in many cases, but they are not
associated so much with harm as some of
the some of some of the earlier
sub-dimensions that I have mentioned.
So,
when we are really looking at the AI
systems,
some of these sub-dimensions can be
really critical. So, we need to
prioritize these
sub-dimensions by the potential of
making harm, and then allocate
appropriate resources to the to the
investigation of these sub-dimensions
rather than looking at all the failure
sub-dimensions equally.
And when we club the when we group these
sub-dimensions together, we see that
controls that we have in deployment are
more critically associated with harm,
followed by the business impact, and
followed by the technical failure. So,
this plot is essentially telling us that
once
once we have deployment controls taken
care of
for the high-risk system,
that gives us some level of assurance
that we can take care of the failures in
in advance, in contrast to just looking
at the technical failure alone. So, all
these sub-dimensions are important, but
deployment controls are far more
important.
And
what, in the next phase, what we did was
we
we designed a materiality scale, meaning
that if we can understand which AI use
cases are more risky compared to some
others, we can
we can prioritize these AI use cases
based on materiality, because
materiality directly rank orders with
respect to the harm associated with this
AI use cases. Meaning that
we can spend suppose we know which AI
cases are more more material then we can
allocate more resources to much higher
material AI use cases than compared to
some other AI use cases which may not be
as material.
With that,
I would hand over to Tanmay who would
explain how we can use those learnings
to build system-level evals.
>> Thanks, Vishal.
Uh so, so far as we have seen what these
failure teach us, so now let us use
those lessons to build system-level
evaluations.
So, first first of all, what we did is
that we have decomposed risk into four
components, which are how often the
model fails, whether that failure
reaches a real decision, whether it
cause
whether it goes uncaught, and how severe
the consequences are. So, in this
scenario, the deployment setup matters.
How much authority does the system have?
Does someone review its output? Can
monitoring catch
error before it causes harm? So,
this same model can create different
risk depending on how we deploy it. So,
what we are saying is that if risk
depends on the whole deployment system,
our evaluation needs to cover that
setup, too. So, that brings us to the
next question.
What should we test in an agentic
system?
So, see, in traditional machine
learning, we already know how to
challenge models. We test their
assumptions, input data, and behavior
under stress. Now, when we extend that
discipline to the whole deployment
system, then, like, does retrieval uh
bring back the right information? Or
what happens when a tool fails? Does
human review catch mistake? Or does the
agent stay within its permission or
boundary? And can the system finally
recover? So, here the logic still is the
same. The boundary of what we test gets
bigger. So, now the question is, how
should we test an agentic system?
So,
on the right, we have the familiar
traditional ML. We test a model on
held-out data, calculate metrics like
accuracy and AUC ROC, use those evidence
to inform deployment. But, we still need
to check the data and assumptions behind
those metrics.
But, on the left-hand side, we have an
agentic system which adds new
complexity.
So, the deployment system, like, it has
many possible
inputs, tool responses, and action
sequences, or trajectory, or rollout,
whatever you describe say. So, we test
selected scenarios. Sometimes, another
AI
uh agent or AI judge generates those
tests or judges the result. So, but that
judge can make mistakes, and the test
can miss important failures. So, this is
where we need to check whether the
evaluator is reliable, what the evidence
covers, and whether it applies to the
system we are actually deploying it.
That's why the evaluator is the part of
the system we govern. So, now I will
hand it over to Vishal to explain
how we can check whether an evaluation
is reliable and what to do when it is
not.
>> Thank you, Tanmay.
So, uh
we have seen the system-level evaluation
for evaluator as well as you know, the
whole AI system. The question is that
how should we really
And when I was looking at some of the
previous research, particularly in the
area of cognitive neuroscience, what I
found was the um this
the scientist
Peter Wason, he's the one who
coined this term
confirmation bias. And essentially what
he did was he
did a bunch of experiments, but
essentially uh in this case here, the
series that you see 2 4 6, right? He was
asking people to predict the next
number, and more often than not, they
were predicting 8 10, like even numbers.
But
um
those answers was those answers were
incorrect because essentially the
correct number was any increasing
number. Essentially proving that all
humans, like most humans, um in this
case it 79%of people tested
wrong,
uh may have some sort of confirmation
bias. And AI systems, as we know, uh
are trained on human-generated data. So,
uh what what he proposed was that any
evaluation or any
any evaluation that needs to be done has
to falsify, not to confirm. And that
that's the way to go about it. And we
take that learning from his research and
propose that eval system needs to be
failure-driven.
So, if the eval systems are
failure-driven, what would that mean?
That would mean that you would start
right from looking at your system claim
and testing it and trying to break it
and then identify where the system
claims are breaking, right? And then
what you do for fix? Either you uh
don't let the AI system run in you know,
in the in the in the territory where uh
there are failures or you come up with
uh supporting systems, right? Which you
are confident of. And you keep doing it
iteratively uh until you get um you to
the to the level of confidence, right?
This is essentially the first principles
based approach that we propose for any
evaluation system.
So, essentially you take take your AI
systems, perform this build-break-fix
loop, understand where the AI systems
could be trusted in terms of its uh uh
final outcomes,
and also a map out uh the uncertain
region and high-risk region where you
can not be very sure of the system's
performance, and you map out the entire
failure region map and route it based on
the reliability and materiality, meaning
that
particularly if you're using AI for any
high-risk rated system,
make sure that your AI is only being
used for
um the the the region that you're
confident of.
And with this, I will hand over to
Tanmay who would who who who would apply
this approach to a real uh AI failure
case.
>> Okay, uh sure. So,
uh so, uh let's make this framework
concrete and see how a narrow evaluation
can miss failures uh that matters in the
real world. So, I will quickly go
through the story behind it. So, a
customer needed to travel after a death
in the family. He asked an Airlines
chatbot about a discounted fare. The
chatbot said he could buy a regular
ticket and claim the discount afterwards
within 90 days. So, he relied on that
advice, but the airline later refused
because its policy uh did not allow that
request. Then finally, the tribunal held
the airline responsible. So, through
this example,
we we are seeing the failure chain. So,
it's crystal clear. So, incorrect advice
reaches the customer, the customer acts
on it, and the organization faces the
consequences. So, if we apply our build,
break, fix, and break again approach, uh
that could have exposed the failure way
before the deployment. So, we Ideally,
we would start with a clear requirement
like advice must match the approved
policy. Then we would challenge the
chatbot with questions about refunds
after travel. If those tests exposed
incorrect advice, then we could add a
policy check or human escalation. Then
we would test again to see whether those
controls caught the errors before it
reached the customer. So, that's our
framework in practice. We have to define
the claim, actively challenge it, and
use the evidence to
guide changes and make a deployment
decision. So, finally, I will hand it
over to Vishal to bring the pieces
together and conclude.
>> Um this is our final slide. So,
essentially, what we are saying is that
your evals should be risk-based um
rather than frequency-based. You should
look at your uh entire system and then
break it into the core components like
technical uh failure, deployment
controls, and business context. And then
assess your AI use cases materiality
with some
uh scale, uh and that could be your
company specific scale and
risk should that risk could change. And
then once you have that,
apply the system level stress testing on
the AI use case. And then once you are
confident about the region,
then only make the deployment decision.
Otherwise, it
may be too expensive.
Our final takeaway message is evaluate
the full AI system based on risk, not
just
one component.
Thank you so much for your time and
attention. You can
feel free to reach out to us outside.
We'd be happy to take any questions
later.
[applause]
