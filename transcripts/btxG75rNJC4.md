# Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer

Canonical video: https://www.youtube.com/watch?v=btxG75rNJC4

Source: https://m.youtube.com/watch?v=btxG75rNJC4

Uploaded: 2026-09-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

So,
put your model somewhere.
Put your agent. You're hoping for the
best. You're waiting for something to
crash. Everything looks good.
Everything's fine.
and you see this
and that's the problem right in these
type of bugs there is no crash there's
no warning no error and there's high
confidence that's not a quality issue
because uh right this is something that
you don't really know what and how and
why
um welcome to this talk my name is Ival
this is aaf and together We're going to
take you on a journey of how we ended up
fixing those type of bugs. A little bit
about us. We work at AI21, which is an
AI research lab. We started as a
foundation model company, most famously
known for Jamba, which is a hybrid
architecture between transformers and
mamba, which is an SSM state. And while
we were doing those, while we were
training those models, while we were
shipping those models into production
and had users and we had a lot of
workload, we got into several
interesting bugs. And these are the bugs
that I think are the hardest to deal
with because this is not a quality
problem. It's not something you can take
your research team and try to optimize
or solve or make the model be better at
something. This is an engineering
problem. This is an issue where that
there is high confidence but the output
is bad.
So let's break let's dive deep to the
first case what we call the imposter
request where just to set up the scene
what are we talking about we are talking
about how we during the training of our
jamba model more specifically we did gpo
which is a type of RL training and again
this is a hybrid model layers of mamba
and attention
and just to make sure we're all aligned
what is the type of a request
So life lives life of a request. So we
start with the prompt token tokenization
and then in the forward pass we're doing
both prefill and then decode. After that
we finish the forward pass detoenization
to go back to text.
And the thing about the crime here is
that it's bad on so many levels but
mainly on these three. This is what we
call the one in thousand gibberish. It's
not something that will happen in the
first 500 or 900 requests, but it will
happen in the 10,00 which is rare enough
to duplicate it easily but not right.
It's too common to ship it.
Sorry. H also it only happened in VLM
not in other not in any other infra
framework and it's something which is
laid on set. It's not something that
will happen if you have only few
requests. You need some sort of
workload. So it's rare. It's light on
set and it's very engine specific. It's
a very very hard task and we had to
bring one of our best detectives to
handle that. So I'll give it to SF to
explain how.
>> All right. Hey guys, thank you. Uh
thanks you. So we're going to start with
um trying to reproduce something that
was very difficult to reproduce. Um and
basically um VLM has got a lot of um a
lot of flags, a lot of the CLI flags and
a lot of knobs you guys can turn and
tweak. Um and one of the things that
helped us understand how to even
reproduce it because when we try to
reproduce it on the first time just
sending prompts here, prompts there a
few batches um it didn't really help us
manage to get gibberish back from our
model. The model responded back just
fine. So what we did was is we tried to
make it happen in a very very short um
amount of time. So we'll get a a quick
feedback loop when we try to deb debug
it. So what we did was is we took one of
the one of the um most default and most
common um um flag that the VLM allows
you to play with which is GPU memory
utilization which basically allows you
to to choose how much memory how much
GPU memory you want to allocate for your
for your weight for your activations and
for your KV cache and so on. and we
reduced it from 90% to 20%. And once we
did that and then we started uh running
a lot of requests uh simultaneously
um all of a sudden request number let's
say 8 854
suddenly returned gibberish and when we
did that we uh we sampled all of the
batches with temperature zero. So we'll
be able to deterministically and
constantly get the same request to get
to return to return and respond with
gibberish.
Um so um like Ival said it happened only
in VLM and um we used um in order to uh
another way to reproduce it and to
understand where the issue really came
from. We used um uh hugging faces
transformers as a baseline since
transformers is a very had a very um
vanilla and uh plain implementation of
our mamba kernels as opposed to VLM
which uh all the kernels and all the
engine have gone through a lot of
changes and modifications to support a
lot of um cool features that VLM
supports. So we use transformers as our
baseline to understand whether or not
there is an issue with our um with our
inference or not with the model or not.
So what we did was we took VLM and we
sent uh all of our prompts through VLM
and we generated a response all the
responses we got and now in our hands we
have the response along with the log
props because because in VLM you're you
able to get your log props out and
inspect them. Then what we did was we
took the full sequence the prompt and
the generation and we uh uh passed it
over to to hugging faces forward pass
but all we did was run just the prefill
um and then we uh uh samp we took this
the logit out of the prefill um um
response we ran it through softmax and
then we were able to u to compare the
divergence uh in the distributions of
our tokens.
Um that's a short uh pseudo code of how
that look like. You can see here that we
uh take up the prompt. We we run it
through gen uh BLM's generate. We get
the uh the response back along with the
uh with the log props. We pass it over
to to hugging faces forward pass. We
only run it with prefill. Um we've
created some function called compute log
log props which um runs this is the
softmax. Um then you calculate the
difference between them and then you'll
be able to tell the divergence between
every one of the tokens log props. All
right. So now that we have the tools in
our hand to understand where the issue
could maybe come from um we started to
look at different suspects in VLM's
engine. So the first thing we looked at
was um the CUDA prefill kernel of Mamba.
Um we looked at it we inspected all of
the all the math that's being done here
that's being done there. Um, and we
looked at the tensor in, and the
tensor's out before before we called the
prefill and after. Everything looks just
fine. Second thing we did was running
Nvidia's compute sanitizer tool to
really see if we have any out of bound
memory. Um, any other memory uh bugs or
issues.
Looked okay to me. Um, then what we did
was we tried to isolate between the
decode kernels and the pre-filled
kernels. Now, we saw that the pre-filled
kernels were working just fine. So we
tried to not call the decode kernels
because in Mamba you're able to do that.
Um so what we did was um we moved all of
our calls and all of our computations to
go through the pre through the pre-fill
kernel and there you have it. The
gibbish all of a sudden kind of
vanished. So we were like okay it's got
to be the decode kernels. But you know
how it is in software you get excited
too quickly and then you figure out it's
not what happened. So what we did was uh
we tried to start playing with the with
VLM's engine and we kind of needed to go
and you know lift the hood up and see
what we can do to maybe get a bit better
understanding and maybe you know get our
hands dirty because BLM didn't really
give us more um tools to really um debug
our kernel and our and our forward pass.
So once so once uh once a tensor once
the request gets all the way to your
forward pass and before it goes into
your prefill and decode kernels you
don't really have any identity. You
can't really tell what prompt uh is
currently being processed. It's all just
tensors and and numbers and matrices. So
what we did was is we added to the
request ID to some class called forward
context that uh that we propagated all
the way down to uh to Mamba's forward
pass just before the the prefill and the
decode kernels were called. And there we
just managed to uh you know have a
simple uh if condition with a request
ID, the one that gave us gibberish and
put a break point there and then we were
able to to to infer and to really um
inspect all the metadata that comes
along with it. And the second we did
that, we saw that the request was um for
the first time when it went through the
uh through the forward pass, it's
actually doing decode before prefill.
the scheduler um decided that it's um
that that this request should be doing
decode before prefill and as Uval said
earlier in our in the life cycle of a
prompt a prompt should first be uh going
through prefill and then decode and what
happens was is that when when in Mamba
um you run a request first uh with a
with decode first after a long a lot of
other requests were already computed the
state was already kind of um overused
and we were using uh the data and the
computations of stale requests, requests
that came before it. So now we were
actually running decode on on previous
requests and that kind of generated
gibberish for us. So the kernels weren't
doing the wrong thing, they were called
at the wrong time for the wrong
requests. And now and why did it matter
only for Mamba? The reason is was is
that in uh in attention uh when you
write the tokens KV you write it you
write the tokens cavies before you
actually you read it. So even if you
have stale data it's being overwritten
but for mamba as uh as I said when uh
when you first go through the decode
kernels you first read the state and
then you compute over it. So what
happens was is you just use over you use
stale data um um when you do the when
you do a decode and the fix was
relatively simple. Well, we just needed
to make sure that what we do is that
when a request first when the when
theuler first classifies a request, it's
got to it's got to make sure that um
that um that it sets that that if a that
if that if you sees a request that's
whose tokens were never been computed.
Um we and and they're zero to mark them
as to mark them as uh as prefill as as
prefill. So the so when they get to the
forward pass, they'll actually just be
um uh used for prefill and not decode
and not u and not chunked. You can see
that it was merged after some time. Um
and that really leads us to and then we
thought everything was fixed, right? We
thought everything was fixed and there
you have it. No more issues. But that
but that was almost the case because
after a little bit of time it gets us to
case number two which um surfaced
another issue that we've faced in our in
our RL and our inference. Um so we ran
RL and and when while we were running um
our our trainings our post trainings um
and we looked at our evaluations and all
of our benchmarks we saw that we had
some log prop spikes between the rollout
and the FSTP step. Uh so and that was
before any weight app update. So some
weights uh same inputs and the two log
props should be identical. Now they
weren't. Um we saw that every 12 step
cons constantly
um there was a log prop spike and that
was kind of weird. Now what would you
guys do right? What can what what's the
what's the first thing to do here? So we
wanted to find some lever that changes
how things fail and not just how much
they fail. We want to see how much um we
want to tweak some knobs that that don't
just tell us, hey, this error um this
error is very very bad. This error
happens uh this many times or or
[clears throat] and so and so on. We
wanted to tweak some knobs that kind of
tell us that once we tweak that knob, um
we understand how it's wired to uh
anything in the in in VLM's engine. And
so we'll be able to specifically go and
and debug that specific part. Um that's
some uh some some cool meme that you all
wanted to put in. Um
so what we did was is we decided to um
to increase the the the amount of
rollouts per prompt. Uh since we saw uh
in our default RL engine we have um
eight rollouts per prompt and we saw
that it happened con deterministically
every 12 steps. We decided okay let's
try to tweak it up a bit and uh and
increase the amount of rollouts per
prompt. So we started doubling it from
say eight to 16 to 64 32 and 128. And
you can see here that it's almost um
almost um there's a pattern here that
that the more we increased it the closer
um it happened because what we wanted to
achieve here we wanted to try to
reproduce the issue as fast as possible
so we'd have a faster debug uh debug
loop feedback loop. So when we when we
when we ran it on 128 rollouts per
prompt, it happened immediately on step
one and we didn't have to wait for step
12 and step 24 and so on. Now you might
think, okay, so you guys played with the
with the GPU memory utilization before
you you tweaked it, you decreased it. It
looks like, you know, when you test on
pressure, um, it really surface things
up. So So we we thought that as well.
And when we reduced the GPU memory from
zero from 0.9 to 0.2, two, it actually
caused the issue to go away. So, we
actually pulled the wrong lever here.
Um, and the reason is is because we
noticed that Mamba kernels um used um in
32 unsigned in 32 index pattern uh
pointer. So, once the offset went past
some you know 4 billion um uh numbers,
it wrapped around instead of throwing an
error. Um so uh when we shrank the GPU
memory, VLM allocated a small state
buffer and um and the cache index never
got large to hit that slot. So we were
so we were just not reaching um far
enough for the buffer to trigger an
overflow. So again the fix was rather
simple. All we needed to do was just
change one word, one one data type
variable um from u in32 to size t which
basically means for most modern
architectures hardware architectures
size t would mean to uh it would be now
changed to unsigned 64 uh bit and that's
a very large number. We didn't we never
reached that number and that overflow
now never happened.
So what we can see here is that we had
um two scenes and one criminal. Um both
kind of you know they had similar
symptoms. Both had silent gibberish and
and silent log prop spikes which also
kind of pro sometimes generated
gibberish. They were both around the
mamba state cache. Um they were both
surfaced by memory pressure whether it
was for worse or for the best and uh
both found via log props um forensics.
um stateful inference inference systems
don't fail loudly they lie to you
confidently I mean obviously sometimes
you get crash you get out of bounds
errors you get other you know exceptions
and so on but sometimes there are some
errors that don't surface up and you
don't get a trace log you don't get
anything you have to go and dig and
understand why things happen um so if
there some takeaways to take from this
um presentation is build a log props
comparison script if you need to compare
your quality you need to compare it to
understand whether you modelize the
issues or not. Um log props comparison
script with a baseline of some other
inference framework that you have or
built is always great. Um reproducing
underression constrain memory. Uh crank
the scale up, play with other knobs that
the inference framework gives you and
really try to understand where the issue
comes from. Uh look for what moves um
the failure shape, the timing, the space
and the location. And when things don't
really have identity uh thread identity
through and what it also I want you to
take from this and don't be afraid to
even you know for complex uh systems
like VLM or any other um complex
framework don't be afraid to go dig in
the code get your hands dirty um
sometimes you know model languages LLMs
are um they might tell you how things
work but you know without you seeing it
in your own eyes getting your hands
dirty you won't get full understanding
of what's going on. Um, thank you. You
guys can add us on LinkedIn. Scan the QR
code to read the actual blog that we've
published with this finding. Um, yeah,
that's it.
[applause]
