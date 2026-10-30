# Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar

Source: https://www.youtube.com/watch?v=LQW_Wvqhp04

Uploaded: 2026-10-29

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Uh I My name is Tariq Shakir. I am the
CEO of Sona, as you just heard. And
we're here to talk today about how we
have been
um helping companies build software
factories that actually work for
enterprises. And I thought it'd be an
interesting way to start to start
looking at actual factories cuz we know
how to build actual factories. And for
those of you who have a little bit of
the gray hair and all of this sort of
thing, you may uh remember the 1980s.
And in the 1980s, you could find cars
that were really good cars. But if you
look at the picture here and if you
remember those times, the cars like
didn't quite fit together perfectly.
Right? You'd have different pieces that
would leave big gaps. It would be really
good cars that just didn't kind of work
the way they were supposed to. And then
uh Toyota and particularly Lexus came
out with a commercial. And it showed
something very simple, which was a ball
bearing
running across the seams of this car.
And it was kind of revolutionary at the
time because it showed that you could
actually build a car that fit together
perfectly. And instead of building for
volume and building and then fixing the
old mindset, you could actually have a
mindset focused on ship it right, on no
rework, on customer happiness.
And
there was not This was not a single
change. What happened was that people
really started thinking about the
factories differently. They started
engineering a building factories that
were engineered to deliver quality. And
there's a number of different pieces
that I think still resonate today. The
first is you prioritize quality instead
of volume.
The second is that you fix the system,
not just individual symptoms that you
see.
The third is that you design for
something that can be built as opposed
to designing the wheels and designing
the washer bottles and whatever it is
and then hoping it fits together.
You solve problems as they occur as
opposed to kicking the can down the road
and fixing it at the end.
And you empower everybody. Anyone could
stop the line, not just the boss.
Now, why am I talking about this? It's
actually because modern software
development actually embraced all of
these principles. If you think about how
we build software today,
what is considered best practice, a lot
of the terms and the practices came from
that idea of a Toyota production system.
Agile, Kanban, error budgets if you're
in the SRE world, continuous
integration, these ideas all kind of
sprung from
this notion of how do we build factories
that work.
And it's worked really well for us in
software development so far. But agents,
as we all know, you wouldn't be sitting
here if you didn't understand that
agents are changing the game.
And as agents are changing the game,
weird things start to happen.
First of all, this is research that was
published last month of the effect of
implementing asynchronous agents in your
development life cycle.
And I'm sure many of you have seen this.
You have an explosion of the number of
lines of code written up 2,450%.
You have an increase in the number of
commits. So, the volume, code creation
is now easy and it is now abundant.
And by the way, more and more people,
I'm sure many people in this room are
saying, "Okay, if it's easy and
abundant, how do I automate it? How do I
build factories, agentic software
factories that help automate and scale
this?" And today, we just finished our
what we call state of code developer
survey.
It'll be out next month, but this is a
little preview. Today, 5% of developers
that we spoke to say that they're
running agentic software factories, but
34%
said in a year they expect to and 39% in
financial services. So, people are
thinking about how do you actually build
these next generation factories.
And there's a a couple of gotchas in
here. Security risk, the agents can work
really well to help you build stuff. It
can also work really well to help you
hack stuff, help you attack stuff, find
vulnerabilities, find quality issues,
etc. And so,
as I was writing this um presentation
kind of over the weekend, a little
just-in-time again from the Toyota
production system, um Satya Nadella
posted this article on X. If you haven't
read it, I think it's a great article
that I think everyone uh should
internalize. But one of the things he
was talking about insider risk of models
inside of companies.
And one of the things that he talked
about was the need for an engineering
approach to containment and governance
built around strong deterministic system
design, human controls, and reliable
operating procedures.
And this really [clears throat]
resonated with me because what we are
seeing is a paradigm shift
in software factory design or software
development, let's call it more broadly,
that we need to engineer, we need to
build systems that engineer confidence
and quality into
agentic software factories.
So, to start doing that, I think it's
important to understand the limitations
that we're facing. So, what's the hard
thing about this? And there's five that
I'm going to call out. The first is that
human in the loop doesn't scale. And
this may be, I don't know, to this room
it may not be all that controversial,
but every virtually every company I talk
to, I say, "What's your AI governance
strategy?" And they give me all the
stuff and they say, "But don't worry, we
have humans in the loop." And the
problem with humans in the loop, as I
mentioned earlier, 2,450%
increase in lines of code, 240% increase
in commits, but the same study showed
only a 30% increase in releases. We
haven't figured out how to scale from
producing stuff to shipping stuff.
There's automation needed, there's new
tools needed, and
really importantly, this is a concept
that really I I see it every day now,
and I'm sure many of you do as well, uh
called cognitive surrender.
Uh and this study was done just a couple
months ago, and it looked at how often
do humans agree with AI? And it turns
out they agree with AI when AI is right
93% of the time.
And four out of five times they agree
with it when the AI is wrong.
All right? So, it's not that human in
the loop is Yeah, we just need to make
things faster. It's actually that it
doesn't work in
the agentic era.
So, that's problem one. Problem two is
that agents struggle with large complex
code bases. They're very very smart, but
you need to understand what happens in a
code base in order to work on it. The
left-hand side is a study that was done
on code translation, and what it shows
is that
>> [clears throat]
>> the agents were able to get it right 91%
of the time when the code base was
10,000 lines of code.
And by the time it got to even 50,000,
and I'm sure everyone in this room
operates off of much bigger code bases
than this, but when it was trying to
translate 50,000, the accuracy
collapsed.
Similarly, another study looked at um
how many tokens does it take on a large
complex code base to complete the same
task, and the variance was 30x, not 30%,
but 30x, and the reason is because
it the agent spends a huge amount of
their tokens trying to understand how to
navigate the code base, the structure of
the code base, things like this. And
it's kind of like if I'm trying to go
from uh
from LA to here, and if I pick a random
starting point. If I happen to pick
White Plains, I will get to New York
pretty quickly. If I pick Albuquerque,
it's going to take me a long time and a
lot of cost. Same thing happens with
agents.
Errors compound. This is another
important concept. This is
a study out of meter
and meter looks at and you can find this
on their website. They look at how
effective
are agents at completing tasks that
humans can do. And the way they look at
this is can you complete a task that
takes X number of hours. So you can see
here the Claude Mythos preview which is
the latest version that they've
published was good at completing tasks
that take a human 16 hours.
Okay, so that's really good but there's
an important caveat in the fine print
here which is this is at 50% accuracy.
When you add it when you dial up the
accuracy to 80% it the curve flattens
substantially because as you do long
running tasks errors compound. If you
have 95% accuracy on each task by the
time you're at 20 steps, you have 30 36%
accuracy.
Right? And so that is another issue we
have to deal with in software factories.
Probably the most aggressive headline I
put in here is is this fourth point that
LLMs are unreliable reward seeking
judges.
Um as you know, so the question that we
always get is well can't you just ask an
LLM? And so people have been studying
this as well and this is all again the
first on the left hand side is from
PayPal AI's research lab. They published
a paper this month actually and found
that between depending on the model and
the situation between 7
and 17% of verdicts change across what
they called identical replications. Ask
the same question, got a different
answer between 7 and 17% of the time.
And if you start challenging, this is a
study out of meta now. If you start
challenging the LLM, are you sure? Very
simple challenge. It'll actually change
its mind 7 to 34% again depending on the
model. So you ask the AI
judge twice and you may get a different
answer.
And then lastly and I won't dig into
this one too much cuz I think it's
probably self-evident to everyone as the
time to exploit near zero,
the ability for us to respond is
incredibly challenged. And so,
prevention is something that we believe
the software factory has to bake in to
the design. Has to engineer into the
factory.
So, as we've thought through this,
we have um written down what we call the
code confidence formula, which is
basically how do you build How do you
think about a software factory that
delivers what we all want, which is
outcomes that we can feel confident in,
right? Not outcomes we can trust, not
blind trust or anything like that, but
outcomes that we can feel comfortable
with or we can sit and tell our
executives, our customers, our
shareholders, our CEOs, our boards that
yes, I believe this factory is working
well. And we think there's four
components to this. The first is being
crystal clear about the intent. If you
don't know what you're trying to build,
you can't tell the agent what to build,
and you will not get the outcome you
want. The second
is guide rails.
And we very specifically talk about
guide rails, not guard rails. Guard
rails prevent something from going off
the road. Guide rails help keep you on
it. And I think what agents need are the
small nudges to guide and govern those
agents.
The third part is verification that
needs to be independent, thorough, and
issues fixed as opposed to just cans
kicked down the road.
And then lastly, evidence.
Trust, but verify. Trust, but understand
that it was done with proof.
Uh that is consistent, audible, and
repeatable. And we multiply these
together because
we've seen a number of situations where
one of these elements is missing.
And if it's zero, the confidence goes to
zero. If you do all of this, but don't
have evidence, you go to zero. You don't
have confidence in the outcome.
So, we really think about factory design
is requiring these four elements. And
I'm going to And as we put together
factors, as we help customers, I'm not
going to walk through every box on this
page, but as we help our customers and
partners build
these software factories, we're very
deliberate about how do you get the
intent, bottom left-hand side in purple.
How do you put the guardrails in place?
How do you do verification in a way
that's thorough and independent? And how
do you produce the evidence? And by
doing this, we see amazing results. So,
these are real results now from our
from [snorts] our customers. The first
one is focusing on intent and
guardrails. And intent and guardrails,
we have a product called Sonar Vortex,
which gives intent guardrails and in the
agentic loop starts to do verifications,
again nudging the agents. And what we
see when we provide agents in
long-running and large complex code
bases with long-running tasks uh with
>> [snorts]
>> this information is a 36% reduction in
token cost because you're putting it in
White Plains, you're actually you're
putting it close to the answer, you're
helping it understand the map. You don't
have to burn tokens on things we already
know.
And 92% reduction in issues in the
commit. Right? So, it's cheaper and we
can get a better outcome to go into that
verification stage. This is again all
because we're nudging the agent to keep
on track.
Then you get to verification, and we
started life as a verification company.
This is how we see the world as through
a verification lens, and we have a very
strong point of view that independent
verification has to cover the full range
of issues
that is both precise
and cost-effective. Right? Use CPUs when
you can use CPUs, need GPUs GPUs when
you need GPUs. So, we look at
deterministic mixture methods, and then
you add in agentic mixture methods, and
it comes up with what we think is the a
gold standard of verification.
And what we see is when you apply this,
our product is called SonarQube. So, we
talked to our customers, over 1,000
customers recently, and we said,
"Are you
How likely are you or how often have you
seen these issues from a gentle coding?"
And the the statement to read here is
SonarCube users are X% more likely than
non-users to have seen a very positive
impact. So, 81% more likely to have seen
to believe that AI coding has had a very
positive impact on code security if you
have that gold standard ver-
verification.
34% more likely to have seen an impact
on time to market, 76%
on outage frequency.
So, again, as I come back to how do we
have confidence to ship, what we're
seeing is that if you put these pieces
together and you build verification
incredibly strongly as a first-class
citizen in the factory, you are actually
building confidence and you're seeing
results, better security, more confident
in time to market, improved
or reduction in number of outages,
improved reliability.
And, of course, as I mentioned, you have
to do this with evidence. Make sure you
pass the quality gate. Make sure
whatever There's lots of acronyms up
here, whichever ones you need to pass,
whether that is your IT general controls
inside of your internal controls and
operations, whether that's MISRA if
you're building cars, or any of the
other ones that are on here, producing
the evidence is what lets you sleep at
night. It's what gives you confidence
that you can move forward.
So, that, in essence, is how we think
about the challenge of the future, that
code is abundant,
that confidence is scarce,
and really the goal that we have and
that we think that everyone should have
as we think about the future of software
development is how do we deliver
confidence. And the factories of the
future need to be able to deliver
confidence.
So, with that, I want to say thank you
to everybody. We have a big booth, it's
a big red booth
on the floor right over that way and
would love to talk to you more about all
of this. Thank you very much, have a
great morning.
>> [applause]
