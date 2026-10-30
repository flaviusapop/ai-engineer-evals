# Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai

Source: https://www.youtube.com/watch?v=XTpyNrEgJQ4

Uploaded: 2026-10-06

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

My name is Sheila. I'm a DA at Akami and
we're here today to discuss um the topic
speculative decoding and how you can um
figure out whether it's worth enabling
for your workloads.
Okay, I'm a little anxious.
Okay.
So, typically when you ask LLM a
question, there are usually two phases
that happen under the hood. The first is
the model would read your prompt,
process all the input tokens and then
build what is known as a KV cache um
which is essentially the model's working
um memory um for the rest of the
request. And this happens only once. Um
and then you have the decoding phase
which is uh when the model starts to
actually write the answer. Um so because
every token depends on the previous
tokens um this process usually happens
one at a time. Um and so imagine you're
deploying an application that uses a big
model like llama 70 billion model. Um
typically like this would require like
even up to hundreds like forward passes
on the model and this is a very
expensive process right um and it can
cause a lot of latency for your user
applications
which um brings the question of like
what if you didn't have to use your
bigger model to handle the token
generation. What if you use a smaller
model to um do some of that guesswork to
speculate on a couple tokens? Um which
is still an auto reggressive process,
but the whole point is because it's
smaller, there's it's a faster process,
so it would be a cheaper process. Um the
output is still the same because um the
target model, the main model that has
the accuracy still has to verify the
tokens and it does this in one forward
pass. Um so that's the idea behind
speculative decoding. Um
I'll just leave this here for a second.
So as I said you have a small model um
which generates
token typically you can set it between
three to five for each cycle. The target
model would handle the predictions um
like be able to scale like basically
approve or reject it. Um and then for
all the for the tokens that are rejected
the target model would
um recomputee the the token for that.
Okay.
So, um this process it's great. It can
save you a lot in terms of inference
generation, but it's not free. Um
because you're hosting now two models,
you have to account for the memory
required to host that second model. Not
that much since it's a smaller model,
but you also have to allocate extra
space for um the KV cache for both
models. Um yeah so typically you would
consider running speculative decoding
when you have um extra space in GPU um
for example if your workload is high
concurrency your your GPUs are probably
already busy trying to run all the
requests so it wouldn't make sense to
implement speculative decoding but if
you have extra GPU space it's worth
considering but uh we'll talk about how
to evaluate whether it's worth um and
the first question is um choosing the
draft model. Um
yeah, so typically when you're deciding
whether it's worth enabling, um can the
draft model predict as accurate as the
target model? And then the other
question is whether um it's as fast. So
you would typically choose a model
that's definitely like a fraction of the
cost like um yeah, so these are the two
main um decisions that you have to
balance, right? Um,
I'm just going to leave this here. Um,
so for my situation, um, I will explain
why I chose these two models. For my
demo setup, when I was running this, I
have access to one GPU. I was running on
a Blackwell GPU and I wanted to run both
the baseline and the speculative
decoding setup in one. Um so to be able
to do this I had to choose a model that
was small enough to be able to fit
because I have to split the GPU
utilization between the both servers. Um
so this is what that looked like for
instance you can the baseline alone um
takes about 16 gigabytes
of weight and then the draft model is
2.5. So that leaves a huge amount and
space for KB caching. Um, and then when
you're thinking about choosing the
model, some of the things that you would
usually consider is um, first of all,
like I said, it has to be smaller,
typically 10 to 50 times smaller than
your target model. Um, it has to have
the same tokenizer. Um, ideally from the
same model family, otherwise you know,
you would have to like manually
translate between the different
tokenizers. Um, what's the other?
Yeah, those are the main things. I think
I'm forgetting one. Um,
oh yeah, and like I said, the cost and
accuracy. Uh,
okay. So,
oops.
So when I was running this, there's
three questions. Um, speculative
decoding, there's some work loads that
would benefit from it versus others that
wouldn't. Um, typically because the goal
here is to get a smaller model that can
predict almost as accurately as the
target model would. It helps with some
use cases when you have a workload that
is more like highly structured like
coding use cases. Um, what's another
one? Like writing JSON or SQL prompts.
Um, it would probably like benefit more
versus if you were using it for a highly
creative use case like writing poetry or
brainstorming or anything like that.
Yeah. So,
I think I have
this is a quick application. I'm not
even sure if it's going to work, but um
so here I do have for the first demo, I
just have um two tabs here. Um like I
said, this is just to focus on looking
at how the acceptance rate performs
depending on the type of task that you
have. Um so the first tab here is a
structured output. Um when I click this,
it will run both at the same time.
Whoa.
Oh god,
I'm just waiting.
Technical difficulties. I'm not sure why
my demo is not running. Um, let's see.
Oh, do I have to reconnect? Um, just
give me one second. I think I might have
to restart the
Looks like I need to restart the VLM
servers and my setup. Give me just a few
minutes. Is this on?
LSU
I
Oh. Um,
should I Yeah, I think I need Oh, it's
showing up. Okay, there we go. Um, so
yeah, I was saying this is a demo. So
when I run this, I'll redo it.
So you can see um as expected with a
speculative on the right side um it was
able to generate much much faster um 1.6
times faster. Um the key thing to note
here is how high the acceptance rate is
which is the rate of the tokens that
were accepted by the the number of
tokens that were accepted over the total
generated by the draft model. Um another
metric here um you can see with the
speculative enabled um you we are able
to generate a lot more tokens per second
um which improves the throughput. And
then if I run it for the other
case.
So here it's another use case.
Um as expected same thing. Um but in
this case I guess the main metric to see
here is the low acceptance rate. And
like I said, this is because this is a
more um there's more variety in how the
next tokens that would be generated
because first of all, the temperature is
set high. It's a creative use case. Um
yeah. Um what else? I think that's
pretty much for this um
case. And then the other situation where
oops
oh yeah this is what I was I should have
put this up here um just to explain when
it would benefit and then the other use
case would be context length. Um so as I
mentioned earlier there's two parts of
generating tokens. Um with speculative
decoding it's supposed to accelerate the
generating part not the part where the
model reads the prompt. So typically if
you have a use case where you need to
provide the model with a lot of context
like for rag applications or um
analyzing lots of documents um with
those situations um the model will spend
a lot more time with the portion of like
building the KV caching um especially if
you're using it to do like a quick where
the the generated tokens are much less
than the context like the input um
Yeah. So ba I think the main point here
is just how to think through like what
is your application doing? Um is it
highly structured? Do you have enough
VRAM space to even consider it? Are you
doing more creative scenarios? Are you
running a lot of concurrency um or not?
Like smaller batch sizes would benefit
from this. Um
yeah.
Yeah, I'm gonna leave this slide here.
This just basically summarizes uh what I
just went through. And if anyone has
questions, I'll take one or two
questions now.
>> Oh, I can't hear you.
>> Oh, yeah. Um
the question was are there particular
tools that I recommend for speculative
decoding? So I implemented this with VLM
um the serving engine. Um they have
really good documentation on how to get
started with it. This is the simpler one
of the simple versions of speculative
decoding. There's a couple others like
the engram medusa eagle that's more like
the architecture beneath is like more
advanced. Um, but for getting started,
yeah, I would say you can't go wrong
with just reading up I when I was doing
this, there's there's not much content
out there on this, but I did find a few
like blogs. Uh, when you re when you
type in circulative decoding, um, one of
the first blogs that will come up by
general compute talks about more in
detail. Um, there's also like two
research papers that were published um,
by Google and what's the other company?
Yeah, it but that's more like goes like
more in depth. Yeah. Um,
but I'm also trying to maybe like
make more content around this, like
maybe like videos. It was kind of hard
to go through this. I I'm a little all
over the place, but I would definitely
love to maybe like publish a blog or
make snippet videos. Um, yeah, on like
YouTube or somewhere, but you can
definitely find the resources.
>> Okay. Right. I should have covered that.
Um, but I don't have the I should have
put a QR.
Oh, um, as I said, I I'm from Akamay.
And if you're interested in like
learning how to replicate this, you can
find it on our website, our GitHub,
GitHub. Um, Akami developers.
Yeah. Um, yeah. So we have a a lot of
like different resources on here. Um I'm
focusing on in inference optimizations.
Uh we have other people that are
focusing on building AI agents um and
how to leverage our like manage
Kubernetes service, how to use Akami
functions. So if you have time, please
go check out our GitHub pages and also
we have a Discord channel that we're
trying to build up now. Um so it would
be great to chat with some of you on the
side. Thank you.
>> [music]
[music]
