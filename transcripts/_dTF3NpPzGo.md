# Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI

Source: https://www.youtube.com/watch?v=_dTF3NpPzGo

Uploaded: 2026-10-22

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> So, I'm here to talk about
all these words that we call
slub and
more importantly, I want to
try to help fixing what Karpathy
termed as the the slub apocalypse
that he thought would start in 2026 and
I think we've seen that on social media.
So, uh
to try to fix this and to stop slub, we
first need to define it.
So first, what is slub? There are tons
of different definitions from the
various experts in the field, but what I
think we can all agree is that it really
sucks to read something that feels
generated.
And it usually looks like this with
uh the the words that we know of, the
delve and uh the generaties and other
things like these and the main problem
is that even as models get better with
fable uh GPT-6.1 and all the the better
models,
slub doesn't seem to go go away. It just
keeps on scaling.
So, we need something different than
just training the models more, it seems.
And I really want to try to at least
first define what slub is so that we can
understand why it's there.
And so to me, slub is made of six main
thing.
First, there are tons of overused words
by language models that we don't really
use like delve that we really know well.
Second, it's usually too general. It's
always talking about most themes, most
projects. It doesn't share nothing
specific. And I'm myself guilty of using
that on LinkedIn as well, which
I guess it's the LinkedIn meta, so it's
it's normal there.
And worse slop sloppy text usually says
nothing. It's just like nice words put
together
that we don't even usually use.
And even worse than that, it says
nothing, but it also repeats itself a
lot. So it repeats nothing and it's too
general.
And
uh
even worse, it hallucinates. As we know,
models hallucinate, so the sloppy text
also we can't really fully trust it.
And lastly, the worst to me is that it
usually has the wrong tone or at least
it has no tone and like everyone's tone
at the same time. So it just doesn't
really talk like you. It doesn't share
stuff that you would share.
So my goal here today and with this
project that I've been working on is to
first measure this sloppy writing.
Uh not just slop words. I don't want to
rebuild EQ-Bench slop score. It's just
it's really about measuring how sloppy
is a writing.
So in order to do that, we are well
today right now releasing a new
benchmark that we called Tone-Bench.
Which
uh the whole goal is the of the
benchmark is to measure if the new
models or models are good at creative
writing, which I will try to define as
well.
So here's the plan for today.
Uh the plan is to justify do we even
need another benchmark? Then how it
works, what we measure, what how we
built it,
and I want to share like the cost of
building it,
our decisions, what we learned already
from for writing with AI from the
benchmark, and share some more stuff
about this.
So with that,
let's delve in.
So the first
First thing, do we even need another
benchmark again? And just looking at
LinkedIn and X X replies, my replies on
X, I think we do.
It's like people are spamming more and
more generated content. So, at least
have them be decently good.
And
uh more precisely, I also really need
it. We are a small team uh at Towards
AI, my company, and we have one side of
the company that is focused on
education. We build tons of educational
content, mostly for AI engineering.
And as a small team, obviously we use AI
as well for that. And it's been
extremely annoying to review this slop
uh constantly and try to fix it.
We uh I published hundreds of videos. We
published thousands of articles. We
released a book. We are working on a
second one uh for AI engineering.
>> [snorts]
>> And so, we really need to have the best
models possible that will help us write
better
uh and not be full of slop.
And another nice uh addition to that is
that I've been sharing about this
benchmark on on X for quite some time as
I've been building it.
And it got really nice engagement, and
people seem to confirm that we did need
some sort of more creative
uh writing benchmark like this one.
And
lastly, just to
prove that I think we are the right team
to work on this benchmark, we
well, I've been
build evaluating AI models since my
master's and then PhD. And now at
Towards AI, we do build evaluation
pipelines for our clients. We have 15 AI
engineers with us, and we have creative
writers, editors uh on board. So, we
already have that for our content. So, I
think uh well, I wanted to leverage that
to build a benchmark and help the
community even more.
So, what did we build exactly?
Hopefully, I I try to share as much as
possible, and I'm happy to chat if we
can help uh even build your own or if I
can just share some some of our
learnings.
So, what we built is super subjective.
It's a way to measure if a model can
write like me. And how I define that is
the is just that if I can read it out
loud like right now without cringing
because of the
the the the words that I wouldn't use
myself.
So, the process is very simple. The the
benchmark the process benchmark the
benchmark process is very simple.
We have
a prompt that is the brief and the
research that we send to a model, and
hopefully it will generate
entirely a video script that I could
have written.
Uh obviously that doesn't happen. It
really sucks usually, but that's the
whole goal, and we measure that that
final script against our rubrics and um
just our whole evaluation pipeline.
And
the prompt that we send to every model
in the benchmark is much more in-depth
than that. It it looks more like this
where we have a lot of details on how I
talk, how I write, all tons of examples
of my previous content videos. We have a
lot of information on storytelling in
general, active sentences, and just how
to write well.
And we have uh directions on what to
generate and what to do for this current
task, which in the
the model would generate one script.
And this is just one of them. In the
current benchmark, we have 10 different
scripts
uh that we worked really hard to make as
good as possible, and we built rubrics
for them to help um
as we will see LLM judges
uh rate these these generations.
So, we have 10 different scripts. Some
of them are published, some are not. We
don't say which ones are the benchmarks
so that we check for contamination as
well.
And
then what do we do with these 10
scripts?
We take all the models out there and we
try to measure their generations.
What that means is that
for every single model we will do 10
times this process, generate the article
from the prompt. In fact, we generate
five of them. I will very soon share
why.
Then we have four different LLM judges
analyze them. I recently added Jeff as a
test. Not sure if I will keep that, but
I I
I added it just to see if it worked
well.
And
then we calculate in the end a final
score for the leaderboard.
I will go through all of these steps
from left to right. So, first, why do we
generate even five scripts?
It's to check for intra-model
variability, which I highly suggest if
you are building your own evaluations
because especially I guess on a creative
task,
sometimes as we see here with Grok 4.7,
some of the generations are outliers
where it's as we see for the from the
benchmark it's just as good as Opus 5.5,
but on just one generation out of five.
So, we want to measure for that and the
worse the model is, the widest the
variance.
So, uh
we have some learnings about that that
I'll share at the end as well. But yeah,
it's
we we found that five drafts seems to be
the good middle ground in terms of of
cost for us to execute and to measure
this this variability.
So, what do we measure exactly and how
do you even quantify writing quality?
That's been the challenge and we worked
on it for for quite some time.
Right now, it's all open on the
benchmark and there are way more details
on the benchmark page as well. But what
we measure is nine different metrics
that we detailed
that that we really detailed, but
I can condense them in five main
aspects. First, we measure the tone. So,
does it sound like me? Which means that
like can the model adapt to a specific
tone?
Second, we measure just pure is it good
writing?
Uh does it have like good hooks, good
emotion emotional transition, and
all the the aspects that we're looking
in a in a good story.
Then, we measure if it follows
instructions. Did it follow the the
length the the expected length, the
format expected?
Uh did it put the right
images and right right things in the
right place?
Fourth, we measure for research
accuracy.
So,
uh we have a research brief along with
each script, and we just measure if it
hallucinated or used the research
correctly. And lastly, we measure for
slap using EQ-Bench slap score, but also
our own measurements.
And what uh this looks in terms of what
the judges see is more like that. We
have around a thousand words of examples
and
uh and instructions and directions
around
each of the metric that we have along
with the script to analyze, my own uh
script as some sort of of guidance, and
the brief and the research.
So, all in all, it's a 14,000 prompt
that we send to to every judge to then
get uh the feedback that we'll dive in
next.
And
uh so so the judge just analyzes the
writing quality. It doesn't focus on
length
uh and doesn't know which model is
writing. Uh we just do that after with
with code itself.
On one metric like tone and voice, which
is our main metric, it looks a bit like
this where we have a lot of detailed
descriptions of what is my tone and what
to expect and how to analyze this.
Then the judge will
categorize between six categories first
and after having found a category, it
will give a rating.
Uh we found that this is
the best way to measure for this more
qualitative task from uh just binary
that we usually suggest to use or uh
directly categories or directly
percentage. We found that this actually
works really well.
And uh
it has tons of examples of what each
score means in terms of of writing for
each of the task.
And what the judge sent back is
something like this. It has the nine
different metrics scored with a
justification for for the score and an
example of like uh I I wrote this score
because of this example in particular.
But the main thing is that
all of this is automated. Uh obviously
because we with 120 models, we we
generate five drafts each for 10 tasks.
It quickly goes to the thousands of
scripts to review, so we cannot really
review this
ourselves.
And the problem with LLM judges is that
they have preferences.
Uh some models prefer themselves. Most
models prefer themselves.
And uh particularly OpenAI. And what I
found quite funny when studying this
is that it seems like Anthropic and
OpenAI are really in a in a war here
where they seem to have past training on
hating each other,
which is quite funny.
But all this to say that you really want
to check for when you have when you use
LLM judges, like using GPT for instance,
if you want to know which model is best
for your task, uh be careful and use
different model family just to ensure
cuz we see here that OpenAI really has a
strong preference on
its own family of models, not just one
model, but all OpenAI models.
And so to fix also for that, we listened
to a few comments that I got on X, so
just thing to use human for a creative
task, which would be ideal, but quite
impractical.
We still tried to to do that in a
scalable way,
where right now we compared manually me
and three of my teammates
1,000 AB pairs of degenerated scripts,
not the full scripts, but like
a good chunk that is comparable between
two scripts, two generations.
And hopefully we'll do more and I want
to publicize this also for
to get help from the community in the
future, but that's not
right now.
So, what did it cost us and what's the
workload behind that?
For me, for us, it was a kickoff cost in
terms of hours of around 500 hours to
build the 10 scripts, define all the
rubrics, find the examples,
try to
quantify quality, which is very
difficult.
And then I just iterated myself with
four different 20X subscription for 4
months to build a benchmark and all the
other things and experiment and change
the the
the metrics ratio and
all these things. And so we just spent
thousands of dollars there.
And
if you want to do this a similar type of
benchmark, you need to know that it cost
quite a lot. Right now, if I just change
one thing in the rubrics or how the
judge rate
generations, it will cost us more than
$2,000. And if I just change one line in
an input prompt for a model when it
generates, it cost us more than $4,000.
So, it's very uh very expensive to
experiment and change these things in
the prompt. So, you want to do this
uh carefully.
Now, what can we get out of this
benchmark, out of Tone Bench? Uh you can
get tons of things on the the website
itself. There's like
a lot of details.
But, importantly, uh I want to share
that what I've learned from the past 4
months is that you don't want to pick
for for creative writing is that you
don't want to pick the model that will
generate a one-shot amazing post. You
just want to find a model that will be
the least annoying to you to get to
where you want to be.
So, uh
like there won't be any perfection
anytime soon, I think.
And what that means right now on the
benchmark, it means at scale GLM 5.3
flash is extremely good, extremely
cheap. It's 50 times cheaper than the
best one, which is Opus 5.5 extra high,
which is
uh 2.5 times cheaper than Max thinking,
but with same results. So, you don't
want to use Max for writing, usually.
Um
And otherwise, for the best
uh
how to write with models that we got out
of this is to first have an extremely
long and detailed prompt. It cannot be
long enough, and the more the better.
You want to add
every example you can think of of what
to do and how to do it. Same thing for
negative examples of things you don't
like and that doesn't sound right or the
words you don't want, everything.
You you can share every If you write
newsletters or whatever, you can share
it in full, and it will just be better
as well.
And what we've seen that really really
helps is to use a high-thinking judge
just one time, one to three times,
otherwise it will loop into slap. So,
just one review of another model with
the same instructions, directions that
will give feedback to the writer.
Really like I don't have
quantitative metrics on that, but it it
helps a lot.
And for a company, if you work with APIs
and want to do this at have the best
results at scale possible, what I
suggest is to
generate several drafts, like 10 drafts
of one specific thing with a cheaper
model like GLM 5.3 flash.
And then have a smarter high-thinking
judge like Opus or or whatever you want
pick and merge the best parts of each of
this these drafts. Which I think it will
still land way way less expensive than
just one generation by Opus 5.5. And I
think will lead to better results from
what I've seen.
And lastly, you want a human review. You
cannot really go around that.
But all of these benchmark measures
obviously my voice, so it's super
subjective, but I and it's just one that
that point you don't want to fully trust
it blindly. Doesn't mean Opus 5.5 is the
best model.
So, but ideally it's a strong signal to
find which model is good at writing and
which is less sloppy.
Um
I suggest you to build your own
evaluation pipelines. If you want we can
help. You can chat or reach out. And
regarding the benchmark, it's live. We
just like right now published it and
released it.
So, there are tons of
graphs, tons of insights, tons of
comparisons,
and details on the implementation, full
methodology.
So, just
check it out and hopefully it's useful.
Thank you.
>> [applause]
