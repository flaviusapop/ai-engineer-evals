# How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed

Source: https://www.youtube.com/watch?v=phchDt63qAA

Uploaded: 2026-05-30

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> I'm Ben Kunkel. I'm the edit predictions
lead at Zed. Um, we recently announced
our model Zed 2 and this is how we
trained it. I'm going to go through a
lot. This is obviously a pretty short
talk. So, I'm going to try and leave
enough time for questions at the end,
but it's if you're not familiar with
training models, uh, it's going to be a
bit of a whirlwind tour. So, if you're
not familiar with edit prediction, it's
essentially giving the model a region of
code around the cursor, asking them to
predict the next edit that you're going
to make. We give it various data in such
as your recent edits, your cursor
position, the type definitions and
variable definitions or of things around
your cursor, as well as diagnostics,
errors, etc. It obviously needs to be
very fast cuz it runs on every
keystroke. And so, it's ideal for a
small specialized model, fine-tuned. It
can do this task and this task only.
Um, so that's what we've we've done.
So, the pipeline in essence is taking
these opt-in production data. Uh, this
works really well cuz it's snapshots.
So, all of that data that we have
collected, related like related
types and definitions and etc., all of
that gets captured and then we're able
to turn that into training data.
In order to do that, we use a process
called distillation where we take a
frontier model, we give it all of that
input, and we say, "What prediction
would you make?" This is a pretty
difficult process as it turns out, even
though the frontier models are pretty
smart. If you ask them 100,000 times,
they're going to give you 100,001
answers, right? And so, there's a bunch
of problems there that we've had to like
finely tune the prompt that we're giving
that frontier model
in order to get good
things out. One of the things we've done
to try and get better,
um, predictions to train off of
is
we run some offline or static
evaluations. So, uh, we have some
heuristics for, you know, is it just
undoing what you just typed? Is it
ignoring that editable region boundary
that we've given it, etc.
And if it does, then we send it to
another frontier model
with a similar prompt like, "Hey, it
failed in this way. Can you fix it?" And
so, that we call that the repair step.
And then, once we've repaired the bad
predictions,
then we can essentially turn what the
teacher made into the expected output of
the student model or Zed 2.
Um, up until that point is reusable
across experiments. So, this is stuff
that we can cache. We can train multiple
experiments on top of that by turning
what the, uh, frontier model predicted
into the format that we want the
experiment to output. And so, that's the
next piece is this prompt formatting.
This is experiment specific. I.e., are
we including diagnostics this time? Are
we not? How much of the edit history are
we including? Those are the kinds of
experiments we're running. And so,
we'll turn what the teacher gave us into
the prompt to, uh, distill and train our
student model.
And then we'll we'll do our uh, final
set of offline evaluations.
Um, the nice part about this whole
process, we've designed it in such a way
that it's all JSONL or a single line is
a giant JSON object. These files get
huge. Um,
but each stage just adds some more
fields to it or moves some fields
around. So, it's a very like,
uh, fluid and dynamic process.
Um, we're generally doing 100,000
examples to train a model. Like, that's
our peak. For these smaller experiments,
we'll cut it down lower to 10 to 50k
range.
Um,
one interesting thing that we're trying
right now is to use what we call settled
data, which is the idea that eventually
the user writes the answer, right? When
you request a prediction as you're
typing, eventually
you're going to like write the code in
the way that you wanted it. And so, we
can wait given that we're the editor,
we can just wait until you stop editing
that editable region that we gave the
model, snapshot it, and save it.
Um,
and then use that to inform our
training. Uh, this is actually this is
very noisy because by waiting on the
edit region to settle, you could change
your mind, you could have an agent come
in and rewrite it completely. It could
be completely different from what it
looked like when the prediction was
made. So, what was maybe a reasonable
prediction, it no longer looks
reasonable.
So, we need some way to filter that out.
One way that we can do that is by having
generating 10 of the teacher predictions
and seeing if any of them are close
using like Levenshtein's distance type
of thing. See if any of those are close
to the settled state. And if they are,
we know a couple of things. We know it's
predictable
and that it's not noisy and, you know,
completely different than what the input
was, right? Cuz we're giving the same
input that we gave for the original
prediction
for this new prediction.
Um, that turns out to be quite
expensive. For 100,000 examples, you're
then doing, you know, a million
frontier model requests. That is
prohibitively expensive.
Fortunately, given that we've now
trained models using the original
teacher predictions,
uh, our student models or Zed 2 is
approaching the teacher in terms of
quality of prediction. So, instead of
running the teacher, we can run our
student checkpoint or something
50 times.
That costs us basically nothing.
And we can see do the same process, see
if any of them are close to the settled
region using Levenshtein or something
similar.
Um,
this gives ideal training examples,
right? Cuz there's a by looking at the
range of distance to the settled state,
there's a region that are super far
away,
we can be confident that that's just
noise.
There's a con- there's a region that's
super close, that's like it's super
obvious what you're going to be doing,
right? You you typed function add A
plus,
it's obviously B, right?
Uh, but then there's this interesting
section in the middle where it's almost.
That's like the ideal
what we want in our training examples.
For example, the stuff that's past the
training data cutoff of our student
model. So, new functions etc. that it's
never seen before that you actually
wanted. And that's going to show up in
these new training examples that we can
then, um, train off of. We generally
don't train off of the actual settled
state just because it's still noisy, but
we can train off of, you know, what was
closest to the settled state.
So, to run those offline evals, we're
running on a held out test set. Um, just
making sure we're not training the model
on the same stuff we're testing it on.
Um, delta car f is our Levenshtein.
Essentially, it does a like n-gram
comparison of various sizes of n.
Um, and then we're tracking this
reversal ratio, reversals being it's
undoing exactly what you just typed.
Um, and we can also look at the kept
rate in production.
Uh, we're gener- when we're evaling,
we're generally running against three
teacher predictions cuz a lot of these
have no one right answer. And so, by
generating three distinct answers that
were all generated by a frontier model,
we can be pretty sure that if it's close
to one of those, it's a pretty good
prediction.
So, for our experiments, um, this is the
training and production part of it. Uh,
those evals that we
um, don't necessarily correlate to what
users actually want in their editor.
And so,
we have this page set up of our
experiments. These are the two that are
live right now. You can see
over here,
we've got this one being sampled at 15%
and that's going to get the rest of
production traffic. And so, we have a
dashboard that I can't show you of the
acceptance rate, latency, all of that
kind of stuff for these experiments. But
this is a page that we created so that
we can, you know, once we've deployed
it,
set it to 15% of traffic, set it to 20,
make it our our live running model. Um,
so this V 0211 seed coder, this is what
we released as Zed
Um,
for diagnostic error counts, it's pretty
much exactly what you'd think. We
snapshot how many errors there are
before the prediction, how many there
are after. And then we're and try and
use that to judge the quality of the
model.
So, that's it. I There was a lot. Happy
to answer, uh, questions. I think we
have five or eight minutes left. So,
yeah. Uh, you said it's very noisy to
determine like the settled state. Are
there any signals that you can share
that you use like like git commit, for
example, or Sorry, what was the
algorithm? Uh, so you said that uh,
determining the settled state like when
the user has is satisfied with that
block of code, for example, is very
noisy. Are there any particular signals
that you can use already that are useful
like, for example, they get committed
something. Sure, yeah.
Um so we don't look at the get commit,
we could.
But uh right now we just do like you
stop editing that area for 10 seconds.
And that that serves as a rough enough
heuristic that um
so it's only in the cases where you are
like consistently editing that location
for longer
um without pausing for 10 seconds that
we wouldn't snapshot it. Um
any other questions?
All right, I guess you guys get your
time back. Thank you for coming.
>> [applause]
[music]
