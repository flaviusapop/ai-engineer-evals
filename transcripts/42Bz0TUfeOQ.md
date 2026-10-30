# The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize

Source: https://www.youtube.com/watch?v=42Bz0TUfeOQ

Uploaded: 2026-10-05

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Folks,
thanks for coming in out. I know it's
lunch time, so I know a lot of you folks
are trying to eat as well. Appreciate
you making the time and for everyone
listening online, thanks for tuning in
as well.
Uh my name's Fuad. I'm a product manager
here at Arize. Uh I've been leading up
kind of the experimentation side of the
house and one thing that I've been
really interested in is voice agents. Uh
quick show of hands here, maybe online
too. Who here is building a voice agent?
Anyone? Got Okay, we got a couple.
Uh I think it's a really cool space.
I'll be talking a little bit about
voice traces,
session views of voices, voice evals,
and some of the stuff that's new in
Arize. But I do want to kind of mention
this isn't a product pitch. This is,
you know, really on why voice agents are
invisible and how to see them. You can
use Arize to do that, you can use
another platform, but what I want you
guys to take away from this is some of
the failure modes and how you can
actually start to see that.
So, we all know voice agents are growing
really, really fast. Have a few tweets
up uh kind of proving this.
GPT real-time just dropped. That was
literally May 7th. Uh I have a
screenshot from a tweet an hour ago from
the LiveChat CEO talking about some of
this. Uh and Vercel on June 29th, which
is only a couple days ago,
um
on
voice agents in Vercel. So, as you can
tell,
uh this space is exploding fast and that
is going to start to matter because as
the space grows really fast,
it is also one of the hardest to debug
categories. So, first off, it's
exploding. Second off, it's pretty
fragile. There's a lot of failure modes
you can't really see.
Um
and
uh things like latency, turn-taking, and
transcription drift become really,
really important. Uh, and the log lies.
If you're just looking at transcripts,
I'll play a little audio file for you
guys in a second. Uh, it doesn't really
capture what's actually going on under
the hood.
And just to give you guys some ideas of
use cases, um,
there's a lot of them from customer
support, I think, which are the more
boring ones, down through drive-thru
ordering. If you've been to White
Castle, they have a a bot called Linda
now. Uh, Bojangles has uh,
Bo Linda as well. There's McDonald's is
doing a lot of these as well, which I
think is pretty cool. And personally,
I'd be pretty pissed off if I was at
McDonald's at 2:00 a.m. and I got 600
cheeseburgers. So, I think I'll show you
a little bit about the failure modes and
why it actually matters.
So,
uh,
this is an example where the transcript
looks fine, but the call wasn't. And if
you read the text logs, you know, user
says, "I need a refund for order 14."
Agent says, "Sure. Started a refund for
order 40." User says, "No, 14."
And it looks like the agent corrected
itself. But,
this wasn't actually the case, and I'm
going to I'm going to play the call.
It's AI-generated. Let's see if it
works.
>> I need a refund for order 14.
>> Sure. I've started a refund for order
40.
>> No, 14.
>> Your refund is confirmed.
>> So, if you notice in the transcript, if
you could hear the audio there,
uh,
it wasn't, you know, the the the
confirm- confirmation on the on the 40
wasn't actually done by the agent. It
kind of interrupted. Uh, and there was a
big, uh, kind of latency spike, uh,
after the user asked for the initial
refund.
Um, so,
we what actually happened was that two
2.4 seconds of dead air before the agent
actually responded. The agent talking
over the caller.
14 misheard, and obviously, the flat
robotic tone is is not a a look, either.
Um, so, these are all audio specific
issues. If you just read this from an LM
output, you would have no idea anything
is going on.
So, what you need to do is you need to
see the conversation beyond just the
transcript. Um, so that means the audio,
the transcript, and the trace all in one
place.
The session as a whole, so multiple
turns from the user back and forth in
the same in the same trace view. And
then metrics on those, so what was the
latency like? What was the time to first
audio like? Were there any
interruptions? Sentiment analysis, et
cetera. And these are some of the
features we've just released at the
beginning of this month in Arize AIX.
Uh, and really the point of this is the
same workflows that you're running now
to help your coding agents, uh, which
are, you know, pretty complex processes
now with harnesses, evals, uh, handoffs,
and subagents, tool calls, you want to
start to bring some of those best
practices into your voice agents as
well.
So, first off, you got to trace it. You
got to see each individual span. Um, you
got to see the live audio and play it
inline from your trace. Really matters
to have all this data in the same place
so you can start to debug things.
Uh, you want to see inputs and outputs.
You want to see the transcript,
obviously, but you also want to see, you
know, specific metrics like I mentioned,
like time to first token,
uh, audio token cost, interruption
events. And then finally, you want to
see linkage between these. You don't
want to just see these as a list. You
actually want to see some of the linkage
between things, right?
So, Arize gives you that one trace view
where you can actually play the audio
inline, view the transcript, view
latency inline, see the conversation
turn between the user, uh, and the
assistant, uh, and see your evals inline
as well. And this gives you a really,
really powerful tool to debug.
Under the hood, what this looks like is
we've actually mapped, uh, the semantic
conventions for audio onto open
inference. So, if you guys aren't
familiar, Arize is first to market with
open inference in 2023.
It is the first set of semantic
conventions that is completely open
source that maps
kind of what is happening with GenAI to
an OTel-compliant
set of conventions.
And I say this to say it's open source,
it's free, and it maps pretty much any
of the major foundational models or
model providers. You guys can go rip
this and send it to a Grafana back end.
Completely free to use. Not pitching the
product here, just explaining some of
the real engineering work it takes to
map things like web socket events to an
easily understandable set of semantic
conventions. So, you can start see
things like the session life cycle, the
audio input, the transcript,
conversation items, the output, and then
the response life cycle and token counts
as well.
And so, yeah, real engineering work went
behind this. It's all open source.
We've mapped all the foundational models
for you.
What this allows you to do is you can
now be provider agnostic and have one
queryable schema. So, those semantic
conventions normalize sort of these
disparate model providers, whether it's
OpenAI, real-time, or Google with Gemini
Live into a set of schema that you can
query. And if you've ever tried to debug
at 2:00 a.m.
off of a customer call, you know how
important it is to be able to query
across thousands,
millions, even billions of traces that
are coming in. You know how important it
is to actually get to the part that you
need to see, to filter that, to sort by
that. All that becomes incredibly
important.
And, you know, as new models drop, you
also want to be able to swap in new
providers and make sure that your
systems are still functioning.
So, no bespoke parsing per vendor. It's
one auto instrumenter. It captures every
single thing that I just mentioned.
And then finally, you want to be able to
replay the whole conversation. So I play
I played the audio for you guys in the
beginning of this, but the session ID is
essentially what stitches every turn
into the timeline, the full call with
every websocket event that's submitted
with some tags on whether it's the user
or the assistant.
You can actually play the audio in the
UI directly from the trace. No external
tooling.
No exports. Just play it straight from
the trace.
That allows you to see who spoke when.
When the agent paused, where it got cut
off, where the user got cut off, what
tools the agent actually went and called
when it did this. And so this really
starts the paradigm shift, which is
you're not just reading transcripts,
you're listening to audio, you're really
understanding the failure cases from
there with the trace open right next to
it.
And um
I'll just show you kind of quick quick
sneak preview of what this looks like in
Arise.
As you can see here, this is an example
of like
you know an agent that can call to get a
specific weather event. You can actually
see when the agent kicks off that tool
call in line with the rest of the audio.
And this allows you to debug failures of
that tool call while you're looking at
the session audio. So you're no longer
looking at disparate events from distant
systems, but you're actually looking at
the entire trace tree for everything
that happened in that session.
So
that real session, few issues that we
saw, right? Turn one, "Hi, need help
with the order, a refund for order 14."
We saw you know kind of that time to
first audio of 2.4 seconds of dead air,
which really impacts the user
experience. We saw in turn three that
the agent actually spoke over the
caller's interaction, which is not a
good look for any assistant, especially
one that's trying to be helpful. And
then ultimately if you look at the tool
call, you'll be able to also understand
that the refund was processed for order
40 and not 14.
Um
which is a huge huge mistake and
actually seeing that live in the tool
call is really really important. And
every single one of these things would
be invisible in a text log. But with the
session view you can actually scrub the
audio and find those failure surfaces
within the tools, within what the agent
is doing as well.
The next thing I want to talk about real
quick is evals that are specific to
audio. So I kind of mentioned a few of
them.
I think tonality and sentiment analysis
is really important. You want to be able
to classify user emotion based on the
actual audio.
Transcript can't do this for you. It's
very very easy to look at a transcript
and see that it it, you know, looks
fine, but tonality really matters.
Positive, neutral, negative, not just a
guess. Latency is really really
important in audio and it's important in
a few use cases. Models are getting
better. There's, you know, jet bar
architectures, etc. But time to first
audio SLAs are still really important
for customer service use cases.
And you want to be able to flag things
that are breaking that.
You also want to flag things like I
mentioned like interruptions,
inaccuracy, transcription drift, and the
task success.
Um
And you want to be able to run these
evals directly against the audio with
evals that are based on audio models.
So, you know, LLM as a judge evals on a
transcript are only so good. But
actually evaling the underlying audio is
really important. And so,
um we have kind of the tooling available
in Arise to be able to do that and we're
supporting all the major audio platforms
as well as they come out with new
models.
So again, evals specific to audio really
matter. They're not just transcription
based evals.
And as you start to scale up your LLM as
a judge evals or even move to agent as a
judge that are doing like complex tasks
like, for example, doing our back checks
to making sure the agent actually access
the system it was supposed to have
access to.
Being able to run these agent as a judge
workflows in Arise, starts to become
really important and we're kind of
seeing the industry move away from, you
know, just an LM as a judge analyzing a
transcript or even analyzing audio, but
actually accessing tools, accessing
third-party systems,
and hydrating some of that evaluation
information inside of it.
So, really easy to get started with
evals in Arise through skills.
It is literally as simple as, "Hey
Claude, create an audio eval for me for
sentiment analysis using GPT audio and
catch frustrated user tone on those
audio spans." And Arise will kind of
take care of all the rest for you. The
CLI under the hood
is able to query spans, do some trace
analysis, filter for the spans that are
audio specific, actually create that
eval, deploy it, and put it against
traces and spans in your actual system.
And this is part of why Arise exists.
Yes, of course, you can do this
yourself,
but when you're trying to query, you
know, billions of spans
with sub-second query latency, it
becomes really hard and also deploying
these live evals as they come in. So,
you're scoring them
while users are actually interacting
with your platform is really important.
And then the final thing I'll mention is
you also want these evals on the spans
themselves because then you start to be
able to do really complex querying and
filtering across your data. So, you're
not just looking at a failure and
looking up in an external system. You
actually have the eval scores in line
with the exact audio that you're looking
at.
And that's why some of this is really
powerful in Arise. Being able to see
those eval outputs directly on the spans
that are relevant helps you kind of get
a full understanding of what is going
wrong with the user interaction.
And then you can kick off workflows from
that. So, evals and monitors attached to
those evals can kick off investigation
agents that automatically start to dive
into, you know, what tool calls and
misrepresenting,
Um, where is my agent failing? Is it
capturing, you know, maybe a product
surface area that I didn't code it for?
Is there a new edge case I need to code
for in my agent? Maybe I need to expose
a new tool. All those become
um, possible once you have the results
directly on the spans.
And so,
I'll I'll just kind of flag and and end
with this thought. The same loop that
you're doing to improve some of these
tools like coding agents,
we now need to do for voice. And the
loop really follows observe, evaluate,
and improve. And then from that loop,
you can start to get some really really
cool continuous improvement loops within
the Arize platform or within another
platform if you choose to use it as
well. Um, and the idea is once you
observe and you have the data available
to you,
then you evaluate and you have the
scores in line with your observations.
Then you can start to kick off fixes,
whether they're fixes that you make or
whether they're fixes that an agent is
automatically making on behalf of you.
And then you can start to verify and
validate those fixes. So, we just
released agent experiments as well in
Arize. Agent experiments, you could
think of it kind of like Postman with
tracing.
So, imagine a world where you have audio
streaming in from your users, it's
automatically traced, you have live
evaluations in the platform that are
automatically scoring those
interactions. And then you have SRE
agents, so not an actual engineer that
you hire, but an SRE agent that's
looking through the traces,
understanding the failure modes,
hypothesizing a fix, and then actually
standing up a fix for you in dev,
replaying those failed traces for you
against that fixed endpoint,
tracing that to validate that the
latency actually decreases. And you wake
up in the morning, you look at a PR, the
PR has a description of a problem. Hey,
I found out why the latency was high.
Turns out we were not truncating our
tool results, and so we were passing in
way too much information to the agent.
Context got overloaded. I introduced the
truncation algorithm. I shipped it. I
actually stood it up in dev.
I tested against the traces that failed.
Here's the report card. Here's how
latency decreased. And you wake up in
the morning and all of this is ready for
you, and you just click approve or deny
on the PR. That is the future that I
think we want to see at Arize, where
self-healing software and continuous
improvement are realities for everyone
who's building agents. And I think
making that possible for voice is
really, really important.
So, start seeing your agents. Add the
Open Inference Instrumenter. Open
source, free to use, OTEL compliant. You
can send it to any back end. Um so, use
Arize, don't use Arize, start tracing
your audio.
The second part of this is actually
starting to do that analysis, and we
would recommend Arize to do that. Sign
up for a free account. Uh I'll have a
code up at the end of my presentation
for you guys to sign up for a a free
year of pro. Um but start checking time
to first audio. Start checking your
interruptions. And start evaluating
um
how these interactions are actually
going and whether they're accomplishing
your use cases. Whether it's a tone or
latency eval, um try using the Arize
skills to actually create that eval. Uh
we have some docs set up for you if you
want to follow along. Bunch of examples
and cookbooks ready. Uh and bring voice
into the same rigor as the rest of your
stack. You wouldn't be okay with this
happening at the coding agent level. You
wouldn't be okay with it happening uh
for an agent that's able to execute
stocks on Robinhood. You shouldn't be
okay with it, uh though the stakes might
seem a little lower, for a McDonald's
agent that's ordering your cheeseburger,
either. Um
and so I'll end with that. Please,
please keep building. Please connect
with me also on Twitter. I still call it
Twitter, not X. Uh on Twitter or
LinkedIn. Would love to kind of talk and
hear about some of the use cases you
guys are building towards so we can add
more echos to our library and make sure
this is useful for you. And if you found
this talk useful and you want to start
investigating your voice agents, there
is a free code up on the screen. It
gives you a year of Voice Pro for free.
It's a i w f 2026
and you can get started and start
tracing your voice agents. So thank you
very much. My name is Ali. I'll be
available for questions for a couple
minutes after but really appreciate you
guys listening. Cheers.
