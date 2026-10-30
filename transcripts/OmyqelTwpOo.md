# How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit

Canonical video: https://www.youtube.com/watch?v=OmyqelTwpOo

Source: https://youtube.com/watch?v=OmyqelTwpOo

Uploaded: 2026-10-26

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Um all right, we're going to talk about
voice agents. And
most of the agents that we deal with on
a day-to-day basis,
um they they do things in the
background, right? They they write code
for us, they do research, we give them
something to do, a task, and we walk
away, we come back, and we don't really
care if they take an extra 10 seconds,
an extra 10 minutes, maybe sometimes 10
hours, right? Um and we expect that. But
at some point in the last year or so,
you have probably interacted with
another kind of agent, a real-time
agent. Maybe when you called your
pharmacy, maybe uh when you called the
airline. I talked to one just the other
day when I called a car dealership.
And at some point in that conversation,
you did the the most human-like thing
possible. You spoke over it. You
interrupted it. You confused it. And the
entire conversation fell apart, it just
didn't feel natural. And then you did
what I do every single time,
operator,
hit zero, like get me to a human, right?
So, how do we fix that? How do we make
these agents as human-like as possible?
Um and so, like in in a um a finance
space, what if your caller
was calling to schedule a payment,
and they changed the the payment amount
midway through, they changed the date,
um and and the agent didn't keep up with
it, right? That is where we start having
issues, especially in the finance space.
The the the the risk is much higher,
right? So, how do we fix that?
So, we're going to talk about how can we
build human-like voice agents for
financial services. And when you think
about building a good voice agent, one
of the first things that comes to mind
is latency. We need it to be as fast as
possible, right?
Well, latency is part of the equation.
Latency has a finite budget, and we'll
talk about what that is.
Um but the keyword here is human-like.
How do we make these voice agents as
human-like as we can? That's the goal.
So, there's quite a few people that are
talking about voice lately. Um some of
these might look familiar. We've got
this this guy Sam.
Um he's excited about voice models. He
says uh that they're starting to change
the way they that we interface with AI.
Isn't that true? And then this this um
weird name here in the bottom right,
Swyx. I don't know if you've heard of
him.
Um he says oh
uh that this is the OG modality.
Um the correct modality for aligning AGI
to our intents is very good voice AI
engineering.
That's that's that's a pretty bold
statement there. And then like get here
says we learn to speak before we learn
to read. Right? Voice is the most
natural interface that we have. So, how
can we make it
as natural as possible and human-like as
possible? Quick show of hands, who who
here has ever built a voice agent and
deployed it to production?
All right, I see a few hands. All right,
so some of you know the challenges that
you might face when doing this.
Um others here who have not built one,
maybe you have um seen a very good
example of one. Have you ever used
ChatGPT's advanced voice mode to have a
conversation with ChatGPT?
Okay, so that's that's cool. Segue here
that OpenAI actually chose LiveKit to
power that that functionality there. So,
it's a very good example of a good use
case or a good uh good example of a good
voice agent. Um LiveKit is the
open-source
real-time framework and infrastructure
for these human-like agents. Um agents
that can hear, see, and speak to a
person on the other end. And so, we're
not just talking about voice, actually.
Um
there's there's multiple ways to
interact with with agents, voice, video,
data streams, uh even physical AI. We
have a robotics division as well, but
voice is the entry point voice is is the
most natural modality, and voice is
where there's a lot of challenges. So,
we're going to focus just on voice
today.
So, in a traditional voice
uh voice agent, you have what's called a
cascaded pipeline. This is three models
that work together. You've got your
speech-to-text model, your LLM, and your
text-to-speech model. And these all have
to work in unison. And there are also
these other models, these real-time
models, speech-to-speech models, right?
And they replace that pipeline. But
that's a newer concept. Um it's it's
getting better, but it's not quite there
for every use case yet, right? But even
then, we've got the traditional pipeline
with three models, we've got the
speech-to-speech models. There's so many
things to choose from, so much
complexity. Where do we even get
started? And here's what we have to
choose from.
Hundreds of models, dozens of providers,
and quick show of hands here, who has
ever picked a model based on a
leaderboard? Like you pick them whatever
model's at the top of the leaderboard,
that's what we're going to use, right?
Well, we're going to talk about why that
does not work for real-time agents. We
can't just pick models off the top of a
leaderboard.
Um because leaderboards, they score
these models, these components, but
we're shipping a conversation. We need
to be able to score them together. So,
we're going to talk about how we can do
that. So, let's go through a scenario
here. Let's let's suppose that a caller
uh wants to pay their bill. And they
say, "I want to pay on the 3rd."
But the speech-to-text model hears the
30th.
And then the LLM is planning now for the
30th, and that goes into the system. The
LLM doesn't know any better. It doesn't
know that the speech detects model got
it wrong. And so all of those errors
flow downhill from there. And so the the
the leaderboard, it can't show us this.
It can't judge this because it just was
looking at it individual models, right?
And so also these leaderboards, they
score these models based on clean audio.
But your callers, they're calling on the
speakerphone in traffic with kids in the
backseat, right? So we need to be able
to score our own agents based on
real-world use cases and examples.
So let's let's say that we fall into
this leaderboard trap. We just pick a
model.
Um then the the first question that
people ask is always, you know, which
model should I pick? So they use a
leaderboard, they pick a model, but that
the actual question that we should be
asking is which stack should I ship for
my use case?
And so that is what we're going to
figure out. How do we answer that
question?
So
before we answer that question, let's
say that you have picked some models and
you start measuring. How are these
models performing?
Let's uh say you're you're testing your
TTS provider. And TTS provider on the
dashboard, it's it's
uh reporting time to first byte. And
that looks really fast, 210 milliseconds
time to first byte. That's super fast.
Um but we've actually tested lots of
popular providers that are shipping up
to 3/4 of a second of silence after that
first byte. So a byte does not equal
audio.
So what we're actually looking for is
time to first audio. How much time does
it take for our user to actually start
hearing something? So time to first
audio is what we should be measuring,
not time to first byte.
Um so imagine, you know, the payment
went through and and and you you're
asking, you know, um you know, did my
payment go through?" And then you hear 2
seconds of silence. That's not very
reassuring, right? So, we need to be
able to measure this this gap that the
caller hears.
Now, the same story for lang- uh large
language models.
So, time to first token is what
we get in text. It's it's a text-based
measurement, but tokens do not equate to
audio, either, right? Your TTS can't
start speaking on a token. A TTS model
text-to-speech model actually needs an
entire sentence to start speaking.
Um and so, that's what we need to
measure is actually time to first
sentence.
Um because a an LLM that is very fast at
producing tokens is not always the same
LLM that produces the first sentence the
fastest.
So, time to first sentence is what we
should be looking at.
And then another thing that
most leaderboards don't measure is these
these agents, they need to do things.
They're not just there to chat with us.
They need to be able to do things on the
back end. They have to look up a
transaction, uh check for a payment
status, submit a dispute, right? And so,
these take time, 2 10 40 milliseconds.
And and so, how do we handle that? How
how do we hide
40 seconds or more of latency?
Well, we can't. That The answer is we
can't. But ask yourself, what would a
human do in the situation?
So, is a human just going to go silent
while the system is doing something?
No, they're going to say, you know,
"Give give me a second. I'm looking that
up. Um system's running a little slow,
almost there." Or they're going to move
on and they're going to ask another
question while the system is doing
something in the back end. So, that's
that that's the human-like behavior,
multitasking, right? We can do that. So,
why can't agents multitask and do that?
Well, that was a trick question because
they can. They should. They should be
able to. And this is the shape of that.
Um this is the only code that I'm going
to show you uh in this in this talk, but
this is a normal tool call and the the
one line is what makes the difference
here.
Um, this one line, this update, this
async await, this awaiting this tool
call is is the whole trick here and this
is what's handing the mic back to the
agent. This is allowing the conversation
and the tool to stop sharing a thread.
They're just they're separate now. And
so um, this is what again makes the
agent more human like because it's able
to keep the conversation going as
something is going on in the back end.
So, don't don't take my word for it.
I've got a quick demo here and we'll
listen and see what it sounds like.
>> Thank you for calling The Gilded Rose
Hotel. How can I help you?
>> Yeah, I'd like to book a room.
>> What dates are you looking at?
>> Uh, next week, Wednesday through Friday.
>> Next Wednesday, July 30th to Friday,
August 1st?
>> That's right.
>> How many guests will be staying?
>> Two.
>> I have queen two beds, king double
queen, a suite or the penthouse?
>> Would you prefer a city or ocean view?
>> Ocean.
>> May I have your name for the booking?
>> Jesse Hall.
>> Is that Jesse Hall?
>> Yes.
>> What's your email?
>> me@me.com
>> Is me@me.com correct?
>> That's right.
>> And your phone number?
>> 555-123-4567
>> Is that 555-123-4567?
>> That's right.
>> I'll need a credit card to hold the
room. What's the the number?
>> We'll stop here.
Okay, so you notice here that the
conversation kept going. There were no
awkward pauses. Um I even interrupted it
and it just kept rolling with it, right?
It It didn't ever fall apart or feel
unnatural. And we see here, you can see
the the tool calls that are happening
along the way and the things that it's
doing. It's actually communicating with
a back end and it's saving every uh
piece of information that I'm giving it.
But what it's doing is it's not waiting
for the back end to say, "Okay, that's
saved. Now you can move on to the next
one." "Okay, that's saved. Move on to
the next one." It's moving on to the
next thing immediately. It's keeping the
conversation going. And if for some
reason a tool call would have come back
with an error or something, it would
have then corrected itself. It would
have said, "Let me Let me verify this or
that, whatever happened, right?" And
worst case scenario, if it was having
issues, it would
uh it would actually
uh um
pass me over to a human in that in that
uh scenario then, right? So, this is how
our agents should operate.
Now, there's one more um axis of this,
and that is knowing the agent knowing
when to speak and when to to listen,
when to keep listening. And so, this is
called turn detection. And so, LiveKit
has a um a built-in turn detector that
doesn't only listen to the transcript
like most turn detectors do. It also
listens to the audio. It listens to the
rhythm, the pitch, the intonation. And
we published the numbers on this. The
the leading um um alternative still
interrupts and cuts users off 9.9% of
the time. And ours, 4.5%
in our use case. We ran it against the
our hotel agent and others. And that hap
And that is what the numbers that we got
for our use cases. This is all open
source. You can actually run these
e-vals and run this against your data
set and see what numbers you get. See if
you get a um uh better uh increased
numbers here. And this is just one small
piece of the puzzle again to make these
voice agents more human-like. Them
knowing when to stop talking or when to
listen. For instance, if if I were
trying to make a payment and I said I'd
I'd like to pay 500
and $55.23,
right? Most of the turn detectors would
have stopped at 500 because they saw 500
on the transcript and they saw
2 second pause, I must be done, right?
But ours would have heard my inflection,
knew I wasn't done talking, and it would
have waited for me.
So, let's look now at that latency
budget, that the gap. This is the gap
between the caller's last syllable and
the agent's first audible response. So,
the turn detector decides when the
caller is done, the language model
begins preparing
a response based on a provisional
transcript, and then the TTS starts
generating that audio as soon as it can.
And so, every model that you choose,
every function, every handoff, all of
that is right here within this window,
and this window has a finite number, a
fixed window, a fixed size. And so, if
you can stay roughly inside 1 and 1/2
seconds,
the call still holds, the conversation
holds. It's starting to feel a little
off at 1 and 1/2 seconds.
But if you can get down to 5 or 600
milliseconds
between this the two turns, that's when
it really starts to feel human-like. And
so, that question before,
how fast can I go? We just needed to get
to go faster and faster. That's not the
answer. The answer is how human-like of
an agent can I fit within this latency
window.
So, again, latency, that's a budget, and
and we know how how to fit into that,
but how can we be as human-like as
possible? That's the goal.
So, if we add all this up, that that
question, which model should I pick? We
That was never something that we could
answer because these scores, again,
these leaderboards, they can't answer
that because they're basing it off the
models, but we are shipping a
conversation. So, let's answer that
actual question. How can we pick the
models? Which models should we pick?
So, this is what we have to do. We test
the conversation. We take a complete
working agent So, that hotel
receptionist that you heard just a
minute ago, we took that. It has a real
back end. Um it's an actual It's not
just a demo. It actually works. Uh and
it's open source. You can check it out.
So, we take that agent and we put
simulated callers against it.
And these callers can pursue goals. They
can change their mind. They can
interrupt. They can mumble. We can add
background noise. We can make sure that
this is a real-world scenario, and we
run all of these simulated users against
that agent.
Um we can run text-based simulations,
which just tests our business logic. Or
we can also run audio-based simulations
that tests the speech recognition
capabilities. It tests turn-taking. The
entire um the entire voice pipeline is
what's tested there. And so, we take the
scenarios, and the scenario should
describe what the caller wants and what
actions the agent should take, what the
outcome should be.
And then we score that. We score those
outcomes. And so, in the hotel
benchmark, you know, did the correct
reservation hit the database? In a
financial benchmark, you know, did the
correct authorized amount get charged,
right? And so, we we check these agents.
We make sure that every all the outcomes
are met. And then we don't score it
based on just the completion alone,
right? Because we know that agents can
game completions, right? We have to make
sure that they took the right steps. Did
they take 10 steps when they only should
have taken two steps, right? Did they
hallucinate a function call? These are
the things that we have to test, the
entire conversation there. And then, we
swap the stack out. We We have the same
agent, the same scenarios, but we change
the models.
And then, we run that loop again. The
identical input Every model sees
identical input byte for byte. We swap
the models, we run the loop. We swap the
models again, we run the loop
continuously over and over, and we are
building at that point a benchmark, a
personalized benchmark, for our use
case, for our agent. So, there are as
many benchmarks now as there are agents.
You run this against yours, and you find
out which models work best for your
situation. That is the only way to find
out which model is best for you.
Now, this is how you catch surprises. Um
a model that that gets the answer for
you the quickest is the right model for
you, right? And surprisingly, that model
may not be the model that that's at the
top of the leaderboard, right? But it's
best for your use case. And again, these
benchmarks, the simulations, all this
this methodology, it's all open source.
So, you can You can check it out for
yourselves, you can run it against your
agent, and see how yours performs.
And so, here is the results of that
benchmark on our hotel agent. This is
the LLM that ranked the highest for our
hotel receptionist agent. That's Gemma 4
31B on LiveKit inference.
You notice on the second line, the same
model, Gemma 4 31B on another provider,
was slower. So, LiveKit optimizes its
inference serving for voice workloads.
And LiveKit is model agnostic, so you
can use any model that you want. So,
again, you plug those models in, and you
figure out which one is work it will
work best for your use case.
Now, if you remember one thing from this
this entire talk, remember this that a
voice agent isn't just a chatbot with a
speaker attached. It's There's so much
more complexity there. It's a real-time
system and that needs to respond like a
person. We need to make it as human-like
as possible. And and and when we
evaluate it from that viewpoint, we will
be able to to build that.
And so, here's a checklist. You can take
a take a photo here. We need to set our
latency budget that the caller hears.
Measure time to first audio, time to
first sentence. Confirm critical dates.
Anything that's financial money, we need
to make sure that we have those those
checks in place. Verify identity before
an account is accessed. Keep listening
while slow tools run. Keep the
conversation going. And then run the
complete conversation repeatedly through
simulations. Test the final state,
privacy safeguards, unnecessary tool
calls, turn-taking. All these things and
then when you find these failures, you
turn those into regression scenarios and
you keep testing over and over again.
So, start with one one of those
workflows or failures that you care
about. Keep Keep iterating then. Run it.
Listen to the conversation. Check what
happened on the back end. At some point
in the very near future, I hope, that we
all call one of these voice agents and
we talk over it. We confuse it and it
just rolls with it and it's and it's a
very human-like experience.
That's That's our goal, but here's what
I need from each and every one of you. I
need you to go build that. Thank you.
>> Woo!
