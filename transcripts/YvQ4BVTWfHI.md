# Is a Faster Model Actually Faster? Test the Whole Job — Morgan Suo, MiniMax

Source: https://www.youtube.com/watch?v=YvQ4BVTWfHI

Uploaded: 2026-10-21

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

Uh I'm Morgan from Minimax. Uh how many
of you knows Minax before? Oh wow. I
like that. Yeah. Because uh I joined
this M uh company for three almost three
years. But when we first like step into
the American market like uh almost no
one knows us. But at that time we have
the first video generation model. So I
will show you something of that at the
end of this speech. But first I will
show you like about our the latest
language model which will be released
next week. So uh today um I would like
to my topic is the hidden cost of a
faster model. So when people thinking
about like if you have a AI application
your product built in in your own pro
workflow. So when a new model arrives
when I say oh please we have a new model
do you want to try it? It can generate a
task faster but your I think your
question is should I switch to that
model? So you try a research task and
the report just comes back very soon and
but it misses a very important source.
So someone has to find that source and
fix that report. I think this is the
thing we did every every day. So did the
job really get faster with this faster
model.
Today we will look at how we reduce the
model computation and then we will ask
how to test the value of those changes
of this model. So let me show you the
job that we will use to answer this
question.
So at minimax we build different
multimodel models and pro products that
people use and a quick chat reply and
research report actually have different
needs. So the task tells us what good
performance means. Today I will focus on
our latest uh large language model M3.1
flash and one research job. So here's
the analyst question
as AI server demand is growing are the
companies supplying the circuit boards
turning this growth into cash?
The PCB there means printed circuit
board. I think you guys know that. and
unc it connects electronic components
that inside devices that such as the AI
servers. So our research case looks like
companies in this supply chain. The
internal review describes work across 14
company reports and the model has
several jobs. It must find the right
reports. It must compile the same
reporting periods and it must keep
different businesses separate. Then it
must explain what the numbers mean.
Think about the analyst who receives the
report. They need to open the source
behind an important claim and they need
to check a calculation. They need to see
what evidence could change the
conclusion. So a useful report gives the
analyst something that they can check
and that is our standard for a finished
research job. So when funding shows why
those checks matter.
This internal review highlighted a very
useful distinction. So profit can grow
but cash flow tells a different story.
A company sells more so is reported pro
profit rises but customers have not paid
yet or it has uh bought materials that
are still in storage. So the anal the
analyst needs to know why the model
should point to the cash flow statement
and the relevant is disclosures. So a
report earns trust when it claims can be
checked and the internal review here
describes the research output. So we
still need to verify it sources and
calculations and also we also need to
measure the time and cost on this same
job. But the technical task a heart use
separate tasks. So they help us to
understand specific trade-offs. With
this job clear, so let's look at what
changes inside M3.1 flash.
This table shows the main changes inside
M3.1 flash. So I will connect them to a
few simple questions. First, where can
we reduce the attention work? And
second, where can we store and move
data? And third, how does the serving
setup affect the time a user waits? And
fourth, we also control how much
reasoning the model does. These choices
affect different parts of the job and
each knows a check against the result we
want. So every optimization has to help
the finished job. And let's begin with
how the model uses a long input.
So nowadays I think every model says oh
I have a very big context window like we
said we have 1 million. So among this
one million how it can help you to find
the output find your result quickly
faster and correct.
So some passenger passages like in this
report like miter just much more than
others for this question. So sparse
attention itself means like we uses a
very small selection step first like the
blue uh box there. So it scores the
blocks of the tax and the main attention
then calculation calculate the uses of
the selected blocks and the model also
keeps the nearby tax in view and this
selection actually they can change with
the query and different questions can
also needs different passengers of the
the context and the number on at the
bottom show how much text is published
examples lacks and the full input can be
much longer.
For our research job, the goal is to
reduce this attention work across many
of uh these documents. But just within
this document, a very short footnote
there may change the entire conclusion.
So for a cash flow question, the
footnote may matter more than the pages
of industry outlook. So we want the
model to include that passage too.
less attention work still has to find
the important evidence. So the next
question is simple. Can we still find
the facts we need
M3.1 flash also uses like the this bar's
attention in its first three layers that
makes this retrieval an important check.
So this separate task places at
different OP positions in long inputs.
So in v run the model passes all 39
requests and the longest inputs were
about uh 830k
uh tokens. So the result covers the
cases in this test and for our research
job we need with real reports. Can the
model find a cash flow footnote? Does it
use the right reporting period? And can
it spot a conflict between different
documents?
So move this important passage to
different places in the input and then
ask the same question again. A long
input is useful when the model can find
a key fact. So finding the evidence is
one track too. Next we look at the
numbers we used inside this model.
So the model keeps the internal
information from earlier text which we
call this KV cache. And M3.1 flash
changes its keys and values from eight
bits to four bits, but the query still
stays at eight bits. And this can reduce
the data we store and move. It also
changes the position of that internal
information. Look at that table. So the
average scores actually is almost the
same but the sign score there it drops
like 6.6 percentage. So some but some
other scores rises.
So the average score actually can hide a
mistake we your user cares about. This
compares that two full setups but it
does not tell us which changes caused
each score. So for our research job we
should check the output out output
again. Are the sources right? Are the
calculations right? And does the
explanation match the evidence? So the
same ideas applies to another part of
the model is experts. Uh our model is
the MO ine architecture. So
it has the computing parts that we
called experts which is the uh M of E
experts. So it selects some of them for
each token in M3.1 flash. These selected
experts use four bit ways and act
activations.
The shared expert is outside this change
and ways of stored model uh values and
activations are values the model
calculates and lower precision can
reduce data movement and support more
efficient computation. But the full
calculation has several steps. So we
scale the numbers, we run the
calculation and restore the scale. The
position of these steps really matters
and the table shows like where scale
restore happens and getting that order
right is the part of getting the answer
right. So fast math still has to be
corrected. And when we check the
complete result, we we measure the
complete imp uh implementation. And for
this research job, we run the same
questions again. We inspect why the
answers still miss our checks.
And now we look at insight. We have
already look at inside the model. And
now we can look at how it generates an
answer for you.
So a serving method called speculative
decoding works in two stages. A faster
draft process. It can help you to
propose a short sequence of tokens and
the then the targeting model can tracks
it and the system keeps this first part
that the target accepts and makes a
correction when it's needed and then
continues this whole process. And
sometimes it keeps several proposed
tokens and sometimes the draft does work
what it cannot keep. So the opportunity
here is to get several tokens from one
target check and but drafting takes time
checking takes time. Rejecting this
tokens also takes time. So count the
time spent checking the draft too. These
checks propose tokens and but financial
claims and sources need their own
checks. So for our research job we
should also include the source retrieval
the tool calls and retries. The final
measure is the time to a report that an
analyst can really use in their home own
work. So even when one request runs well
many users can change this diff
experience.
Here's an separate serving test. So it's
uses the storage generation with low
reasoning effort but the concurrence
requests now like we rise from the 32s
to 64. So the total output per second
grows about 1.9 times
but look at the weight time actually it
the P95
weight for the first token rises. It
goes from about 1.5 seconds to 11.3
seconds uh6 seconds. So for 95% of this
request the first token arrives by this
time and the weight now is becomes like
eight times longer. So the medium stay
as uh the the time that we can satisfy
it. But we we cannot only look at the
median time. So it changed everything
that if we only like look at that one.
So the users feel the weight and even
when the throughput you see like oh we
have through like more than 300 per
second but still you need to care about
the final weight time. So the first
token may be reasoning and we will still
need to measure when the usable report
arrives. So set a dial line for that
report. we choose a low that miss it and
there's a one more setting that change
the work we ask the model to do. So this
is the first time we uh just use this
different
uh reasoning uh uh control. So uh from
this part uh so this is the default max
changes that we use in the request and
it can controls how many tokens we use
for this model thinking. So in the
document setup here so thinking stays on
but if we leave the effort blank the
default is max. So a default can change
the amount of work we request and one
coding test there shows the tradeoff. So
high reasoning and max reasoning. So the
high uses fewer up output tokens than
the max but the accuracy actually fell
from 80% to 68%.
So the fewer tokens came with lower
accuracy on those task items. So give
this task the thinking budget it really
needs. So for our research job compare
these settings on the same reports and
check whether each setting finds the
evidence and supports the calculations
and the quick first pass on the report
ready for review may need different
budgets. So we need to record this
setting or which reasoning control we
need to put and then used in our later
work.
Okay. Then when we ship this research
workflow with all these um new updates
we have with this model.
First we can fix this question on the
source reports and use the same
information cutoff and agree on what
makes a report acceptable before running
this comparison and then we can check
three things. The first is can the
analysts trust the report and open the
resources behind the important claims
and check the reporting periods
recalculate the financial financial
numbers and look for the evidence that
could change the conclusion. And second,
what did the finished job cost? How long
did they take? And include retrieval
tool costs and retries. So if a person
must fix the report before use, count
that work too. So include all the failed
attempts in the cost of producing uh of
producing this acceptable reports.
So test are the number of these users
you expect and check whether reports
arrive within the promised time and
measure the cost of report you can
actually use. And the third one is can
we repeat this result save this model
and runtime versions and also save the
prompt settings and sources. So keep
these examples of failures and we can
start with a small roll out and keep a
way to switch back.
So before we finish, here's a short
recap of today's talk. It's created with
Miniax A3, our AI video model, and you
can check here.
Okay. So uh this is another model that
we are working on and it's opened way.
So everyone that who wants to build this
actually it's only a one problem with
the text to video. Okay. So let's return
to this uh our opening question today.
Should we switch to a faster model and
look at this finish job that we talking
about for the last 18 minutes. So for
our analyst that means a report with
resources they can open and it has
numbers they can check it must arrive
when they need it and for uh this M3.1
flash changes how we spend computation
and the complete task uh shows that
those changes means for the user so
measure what we cost to finish job and
on time. So faster models uh I think
like faster mo models really matter but
what matter most is what we can do with
them. Thank you guys.
