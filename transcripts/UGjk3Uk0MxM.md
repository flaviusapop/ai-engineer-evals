# The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft

Canonical video: https://www.youtube.com/watch?v=UGjk3Uk0MxM

Source: https://youtu.be/UGjk3Uk0MxM

Uploaded: 2026-10-19

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

All right. Uh
since it's already like 11:12, I want to
start talking about the workshop. Um so,
I'm going to do this as a guided
workshop, so I'll go through all the
examples up here on screen, um but you
can also uh try and follow along. So,
the repo is there, the environment
variables are there. Uh
so, the environment variables give you
access to a bunch of Foundry models that
I've deployed on uh Microsoft Foundry
project. Um and they have a certain
amount of token capacity. It is possible
that we are going to go over the token
capacity
um in you know, in this session. Um
I only got found out very recently that
this workshop was accepted, so I tried
to get as much resources as I could in
the small period of time. Um so, in that
EMB file, there is actually uh multiple
different possible environment variables
that you can comment in or comment out.
If we do start getting 429s, um you
know, uh rate limit exceeded errors.
Uh so, yeah. So,
I'm hoping that there's enough capacity
for all of you to be able to try out
those models, and uh we will see. Uh I
also have my colleague Cedric here. Uh
so, Cedric is going to be wandering
around while I'm talking, so he might be
able to help uh with with issues as
well.
Uh if you In terms of setting up the
code, if you already have Python and UV
on your machine, then you can do a get
clone of the repo and run UV sync, and
that should have everything you need to
run the examples uh once you have that
.env.
Uh otherwise, you can make a GitHub code
space. That's uh basically a VS code in
the browser that has everything set up
for you.
Uh who here uses UV? Cedric wants to
know.
Okay.
So, it's not number one yet.
But, the other question here, who uses
Python?
All right, then more people. Okay.
>> Pretty much everyone uses Python here.
>> Yeah. Oh, did you count the overlap? All
right. Okay. All right, so if you didn't
take a picture of that screen yet, just
take a picture of it now. Otherwise,
Cedric also has a picture of it on his
phone, so he can go around if you need
those links.
Uh, so the goal of this workshop is to
be able to get a feel for the
differences between the different, you
know, uh, top-of-the-line models and see
how they differ and, you know, what you
can improve about them. So, I've set up
a bunch of different examples and also
evaluations and optimizations that we
can do to improve our experience across
models. Uh, and I think this is a really
important thing for all of us to just be
to be doing as AI engineers because, you
know, as you've seen, like, there's so
many new models that come out all the
time. And, you know, the US government
at any point could cut off access to a
model. So, we need to like, we need to
have options, right? So, we need to be
able to,
you know, point our AI applications at a
different model and and have it still
work or know how to improve it. Uh, so
that's the goal here is to get more
experience with more models. So, uh,
these are the models I've deployed
inside Microsoft Foundry. Uh, so I've
got uh, GPT-5 5, that's a standard one I
use all the time. But, then I've got
Kimmy K2.6, that's a uh, more recent one
that's quite good. I've got Deep Seek V4
Flash. And then I have Mistral Large 3.
So, these are the four models that we'll
be comparing in this workshop.
Um, so as I was saying, you can
in order to set up the workshop, here's
the repo that that you're all into. So,
if you don't have Python on your
machine, you can just click on the code
button and there'll be a big button here
that says create code space. So, you
click on that, it'll make a code space.
So, then here's the uh, the code space
and then this has um, I've already put
the dot env, but then you go and you
grab that other
um
URL that I put up there to get the env.
That goes to this file here. You
download it. You open that.
And then you create a dot env
with the contents, okay? So, this is
pointing at a that foundry project that
has those four models deployed.
As you've seen, that does have
you know, it has token limits. So, if we
start getting rate limits, you can start
you can try these other models that also
have the four project deploys. And then
I have a separate one specifically for
Anthropic just because it has different
terms for that project. All right.
So,
so yeah, and then once you've got that
set up, then you v sync will sync all of
the packages that you need for Python.
All right, so that's the setup.
Now, I'm going to actually go through it
and do it do it up here so that you can
you know, hopefully follow along if you
want, or you can just watch watch what I
do.
So, as I was saying, we do have the four
models, and you can compare models just
doing benchmarks. You're like, oh, you
know, this one has good quality
benchmarks and good safety benchmarks.
You can also look at you know, the cost
and thoroughput and stuff like that. And
you can get this approximate notion for
how good these models are, but you don't
really know how good a model is until
you use it for your particular scenario
because there's so many different ways
of using models. And a particular
benchmark isn't really going to tell you
how it's going to work for your
scenario. So, that's what we have in
this repo here is a ton of different
scenarios, and we can try out these
models for each of them. So, we're going
to start really really basic, all right?
So, just a single LLM call that asks the
LLM to do something. So, what you see
for each of these files is that they all
start off with the model variable and
they default to GPT-3.5. That's kind of
our baseline. It's obviously it's a very
good model.
But then if we want to try a different
model, we can just uncomment that line
and that will be the model that gets
used. So, this file here
is connecting using the OpenAI Python
SDK to the Foundry URL and passing in
the key from the environment. And the
prompt we're doing here is how many
times does the letter E appear in the
following sentence? The elderly
gentleman eagerly entered the elevator.
Count carefully.
All right. So, then we send that to the
OpenAI responses API and say, "Here, use
this model with this prompt and then
let's see the raw the output, right?"
So, we're doing the classic thing of
asking LLMs to count. And so, we'll see,
you know, how well they're able to do.
So, I'm going to say UB run examples
with the name of this this file name
here. And this is all in, you know, in
the read me. So, we're just going
through
one by one. So, you can just copy-paste
from there. All right. So, GPT-3.5
is actually very good at math,
surprisingly good at math. My colleagues
have been running a lot of finance
benchmarks on it lately and they're
like, "Oh my god, like it does so much
math in its head." So, it does actually
get this correct that there are 13 E's
in this sentence, right? So, now let's
try Now we just change it, right? So,
okay, let's say we want to try Kimmy.
So, we go and we change to Kimmy and now
Kimmy will be the model that's used.
And we see, "Okay, can Kimmy count as
well as GPT-3.5?"
And it does. It gets 13. All right. Now
you might be thinking, "Oh, is this just
too easy? Let's try DeepSeek V4 Flash.
And this time it gets six. Okay.
So, it missed out on seven of the E's,
right? So, we can immediately see that
there's definitely difference between
you know, DeepSeek V4 and those first
two models. And then finally, we'll try
Mistral. And this one gets eight. Uh so,
what we see there's a difference here.
All right. So, when you see this and
you're like, "Well, I want to be able to
use all these models." Then you start
doing some prompt engineering. You're
like, "Okay, what if I say, uh you know,
break the sentence into words,
count per word,
uh sum, show your reasoning, right?"
Let's try Let's try that, right?
And you know, we can fix our typos, not
that it matters. All right. So, let's
try it with Mistral and see with a
little bit of prompt engineering, can we
get a better better response here?
All right. And it got it, right? So, you
know, by breaking it up, doing a little
chain of thought here, it was able to
come up with the correct answer, right?
So, immediately, we can see that there's
obviously differences across models and
if we change prompts, you know, we can
get uh different outputs.
All right. So, now let's get more
interesting and go to more real-world
scenarios. Uh so, let's look at RAG. So,
RAG is still one of the big uses.
Arguably, really everything is RAG.
Agents are RAG, too. Um
So, we have this So, RAG is when you ask
an LLM to answer a question based off
some context, right? And the thing
that's important for RAG is that you
want it to answer the question and stay
grounded in the context. You don't want
it to make up anything that is just from
its weights, right? You're trying to
force it stick to the context, right?
And that's what I find really varies
across the models is that the smaller
models, the less powerful models are
actually much more likely to go to their
weights and pretend it was part of the
context.
Um so, what we have here
is um we have a data set about carpenter
bees and we ask it a question, "What are
the key differences differences between
how honey bees and carpenter bees build
their nests?" But this data set only has
carpenter bee information.
Uh so, it should only actually be able
to answer about carpenter bees. So a
good response in this case would tell me
the carpenter bee information and then
it say, "Sorry, I can't tell you about
honey bees. I don't know." Um, so we
tell it like, "Hey, your job is to
answer based on the sources, cite the
sources. Um, here's your here's your
question, here's your sources." All
right, so let's go ahead and try that
out and see what we get.
All right, and it's Yeah, so when it's
doing the search first, very basic
search. Okay, so it's sending did the
search. All right, and what we see
and it says the data set does not
provide details on honey bee nest
construction. So this is what we
actually want to see. This is from GB55.
GB55 is very good at knowing what it
doesn't know.
So now, let's try switching Um, Kimmy's
also good as well. So I'm not going to
show every model
every time now just for for sake of
time.
Um, so let's try Deep Seek, right? Cuz
we've already seen that, you know,
there's a distinction here. Now Deep
Seek, once again, says provided sources
do not contain information. All right,
so Deep Seek did a good job here. And
now let's go to Mistral. Uh, Mistral,
sorry. Cedric, how do we say Mistral?
It's French, right? French company?
>> Mistral.
>> Mistral. Cedric's going to be my French
translator. Every time I need to say it,
you're just going to say it.
Now, Mistral.
Mhm?
Yeah, okay.
Mistral.
Um, so Mis- Mis-
With Mistral
>> [laughter]
>> Um, we do see that Mistral actually
answered uh, from its weights uh, even
though that information was not in the
sources. So this is an example where a
model went into its weights even though
we didn't want it to do, right? Now
we can try to force it. Once again, we
can try to do prompt engineering. Uh, we
can say uh, wait, actually so it would
say
uh, if the if the answer
for a bit of info
is not in sources.
Say
no source provided. I think this is what
I got it to work. Uh
oh, I will try that and do not make up
an answer. All right, let's try this.
>> [snorts]
>> So, we're trying to force it to realize
when it's giving us information that's
not in the weights. And sometimes if you
force it to say, "Hey, for every bit of
information that you're giving back in
your answer, you have to prove that you
got that from from the sources, right?"
Um so, here I'm trying to have it
associate each of the things in that in
that answer with a source and um
and maybe that will force it to realize,
"Oh, wait a second, that wasn't
actually, you know, in my in my answers
here."
All right, it's still going out. It's
going to think it's thinking really
hard about it here.
Okay.
And there we go. Honeybee details are no
source provided beyond interactions with
carpenter bees.
>> [laughter and gasps]
>> Um so, it definitely knew when things
were not source provided. It still gave
the information. So, we got a little
closer. But as you can see, this is
definitely uh a difference that I see
with rag and rag is what I work with the
most. Uh so, it's it's something you
want to evaluate when you're looking at
models to use with rag is are the models
willing to admit what they don't know,
how likely are they to make stuff up?
All right, so now let's move to image
input. A lot of these models are
multimodal, so they will accept images
as input. And you know, there's lots of
really cool um situations you can do
with image input. So, here we've got
some files locally and we're just going
to send them to the LLMs and ask them
some questions about the files, right?
Um I'll show you the files.
Examples, image input. Okay.
All right. So, the files we have here
are this picture. This is an aurochs,
not a unicorn.
This picture. This is of some crocodiles
that I saw in Costa Rica that I was very
afraid of.
And then also we have
this picture which is a list of plants.
Basically like a screenshot of a table
with some really small fonts in it.
So,
we're asking each of the LLMs to
interpret each of the images, right? So,
first we say, "Oh, is this a unicorn?"
Right? That should be easy to say it's
not a unicorn. Great. Then we say, "Hey,
are these alligators or crocodiles?"
That's a bit tricky. They are actually
crocodiles because of their snout. I
spent a lot of time reading the
Wikipedia page about crocodiles and you
got to look at their snout and then you
know. Luckily, GPT-5.5 has also been on
a Wikipedia binge and so it knows that
when it sees that snout, then that is
crocodiles. And then the cheapest plant,
it correctly found the cheapest plant in
that like fairly small text screenshot
of a table. So, that's pretty impressive
that GPT-5.5 could do that.
So, now let's try it with Now, for these
models,
we can't use DeepSeek cuz DeepSeek only
accepts text. It's not a multimodal
model. So, we're only going to try Kimmy
and Mistral.
So, you know, it figured out the
aurochs. Okay, good. Just making sure it
works. All right. And then for
crocodiles, it does say crocodiles
correctly.
And then cheapest plant, it got the
cheapest plant. So, Kimmy is doing a
great job as well.
And then finally, let's go to Mistral.
Here.
Let's see. All right. So,
you know, it knows it knows it's not a
unicorn. It didn't know it was an
aurochs.
This one, it wasn't sure.
It thinks they're alligators.
So, it you know, it's having a harder
time looking at the it thinks that
they're alligators. And then for the the
plants, it pulled out a plant that's
$2.30, which is way more expensive than
the cheapest plant. It was supposed to
find one for 58 cents. So, the Mistral
isn't able to answer these kind of
images. Now, here's the thing, when it
comes to multimodal understanding, you
can't really do much prompt engineering
cuz either like the like the the model
either understands an image or it
doesn't. Like you might be able to do
some prompt engineering if you know
you're in a very particular domain and
there's some hints that you can give to
it about how to read a particular kind
of graph.
Um but really with image input, it's
about figuring out, you know, for the
kind of images that you're going to send
to the LLM, does the LLM understand
those images? Is it going to, you know,
is it going to work for that scenario,
right?
Um because it may be that, you know,
maybe Mistral is really good at
particular kinds of image tasks, but
just not this, right? So, it's all
figuring out what is the task you want
to do and is the model going to do a
good job at it?
Now, what's interesting with the
multimodal, too, is that a lot of these
also depend on the language, right? Here
I'm using English. Remember, all these
models are super English-centric, but if
you switch to a different language, like
if I ask in Spanish if they're caimanes
or cocodrilos, it actually thinks uh it
says it gives the wrong answer because
it's getting so confused in its head
between these different like words and
how they map across English. Like it
just becomes too hard of a task both
understand the difference between
alligators and crocodiles and also
remember that caiman means alligator in
Spanish and is not the same thing as the
caiman that we have in like Florida.
Anyway, it's like it's fascinating to
see that once we switch to Spanish, it
fails at the task. Um so, that's another
thing to keep in mind, especially we're
in California, a lot of times when we
develop applications here, they are
bilingual cuz a lot of, you know, 50%
Spanish-speaking here. Um so, you know,
your
your mileage may vary as you change
languages. Okay, so now let's go on to
function calling, also known as tool
calling. So, tool calling is in fact the
basis of like all agents. All agents are
based off of tool calling. And this is a
a capability that the LLMs are trained
with specifically during the training
process. So, they are trained to be able
to look at a definition of a function or
multiple function definitions and look
at the user input and say, "Okay, based
off that user input, I want to call this
function with these arguments and
and then, you know, just return that."
So, in this example here, I'm defining a
function using JSON schema. This is what
the LLMs understand. So, I say, "Okay,
here's my function. It has the name
create calendar event. It has this
description and these are the parameters
it takes. It takes a title with this
that's a string. Here's a description,
right?" And all of this is all going to
get sent to the LLM. So, we send this
full JSON schema to the LLM and say,
"Hey, here's the function. You got to
decide whether you're going to call this
and how you're going to call it, right?"
So, this is in fact, even though this
this is like an object, this is prompt
engineering here. Everything here is
actually like me deciding what is going
to be the best for the LLM, right? What
type should I use? What description
should I add here? What should be the
names of these parameters? Cuz the LLM's
going to decide based on all that
information how it's going to call this
function.
Uh so, then we have a user message. So,
it's like So, the user's like, "Oh, can
you throw something on my calendar? It's
a platform team sync. Me, Sarah from
Ange, Marcus, the new PM Priya. Tomorrow
at 1:30 p.m. It's virtual on Microsoft
Teams, okay?" So, then our then we tell
the LLM like, "Hey, you're a calendar
assistant. Today is Monday, June 29th.
Use the available tools to process the
user's request." And we send it the
tools. And so, now the LLM is looking at
the user request, looking at the tools.
And in this case, it just has that
create calendar event. And it's going to
decide, "Hey, is there a tool here I can
use to answer the user?"
Uh and then we're just going to go
through and see what tool calls it
decides to make. Uh so there we go. So
in and this is like really low-level
tool calling here. Uh once we build an
agent, we're going to abstract on top of
this, but I wanted to start with the
most low-level tool calling we can do.
And the LM just responds back with
here's the name of the function and
here's the arguments that I want you to
send. The LM itself doesn't call the
function. That's up to us to do. All
right, so what we can see is that uh I
put my I put the expected on the left
just so you can see and we can see the
actual. So GPT 55 did add me as an
attendee, which I didn't really want. Um
but it did pretty good otherwise. So
let's try
uh Deep Seek and see how Deep Seek does
with this one.
Cuz what we want to see like when we're
doing tool calling, we want to see is it
calling the right tool? So it is in this
case. It is calling the create calendar
event tool. And is it passing in the
arguments that we expect, right? We have
certain arguments we expect. In this
case, Deep Seek put you as an attendee.
And then for the location, it said
virtual {parentheses} Microsoft Teams,
which is not what I asked for, right? So
it's not adhering to my argument um
constraints as much. Let's try Mistral
as well.
And see how it does. So once I see this,
I can start to realize like, "Okay,
there's some ambiguity, right?" And you
know, if it if it called it with the
wrong arguments, that means there's
ambiguity. I need to go back into my
descriptions and say, you know, uh you
know, don't you know, don't include me
or you, just named attendees.
Um you know, you could say first and
last if provided, right? So you start to
see, you know, what what you haven't
been specific enough about and start to
clarify that ambiguity and then, you
know, evaluate all the different um
inputs and see how it's doing.
All right. So that was a basic tool
calling. The next thing we want to do,
we're building up to agents here. The
next thing is to do tool calling in a
loop, right? So when we have an agent,
it's calling tools in a loop until it
reaches a goal. Um so, we're going to
demonstrate using this just a function
calculate. So, this calculate takes a
mathematical expression and returns back
the output, right? And we have, you
know, basic support for uh evaluating
these uh mathematical expressions. So,
we're giving it basically a word problem
where it's like, "Oh, this store is
having a sale. If I buy three shirts and
pay, you know, this much tax, what's my
total?"
And this can be done several different
ways. It could be done with multiple
tool calls to that calculator call with
like one little expression at a time,
like, "Do this, and then do this, and
then do this, and then this." Or, if the
LM is very clever, it could batch all
that into one long expression and do a
single tool call. So, here we're testing
efficiency, right? Where, you know,
there's more like a lot of times once
you have tool calling in a loop, the
differences between the models is their
efficiency. Are they able to get to the
goal faster? Can they accomplish the
same goal with less tool calls, right?
So,
that's what we're going to say. Uh
the only system prompt is do not do math
in your head. Okay.
>> [laughter]
[gasps]
>> So, let's see.
Uh
that one's really for GB55 cuz it's so
proud of its math abilities that it's
always trying to do it in its head.
Like, "Come on."
All right. So, GB55
indeed does the entire calculation in
one expression. So, it only required one
tool call to get to the final result.
So, that's good. That's good. That's,
you know, fast. It saves us time. So,
now let's try with
um
DeepSeek. The only reason I skip Kimmy
all the time is cuz it's actually a very
good model, and so it does pretty much
uh on par with uh GB55 uh for much of
these. Okay. So, now we can see with
DeepSeek,
it is going through and it's doing and
and and and it's doing like so many how
many it did like four. It did four tool
calls, right? So, it still got to the
correct answer, but it took four tool
calls. And every one of those tool calls
is another network request, right? And
so, you know, when we're evaluating two
two models, we want to both look at the
final answer, but also how how long did
it take to get to that final answer,
right? Um actually, Kimmy did do
something really interesting the other
day. Let's see if it does it again
with this one. Cuz Kimmy most of the
time works quite well, but Kimmy does
sometimes get into weird loops
um
when it's kind of like double-checking
itself.
Uh okay, this time it did well. Yeah,
the other day when I did Kimmy, it like
got the right answer on the first try
and then decided to check its work with
the like four other calls. I was like,
"No, you're good. You're good."
[laughter]
>> [gasps]
>> Um so that's what that's what we're
looking at here, okay? Is how many how
many calls does it actually need to get
to the end.
All right, so next
um we can go to
uh agent loops. Okay, I'm actually going
quite fast through this now, actually.
Uh okay, good. [laughter]
Um all right.
So now we've got the basis, right? We've
seen tool calling, tool calling in a
loop. So now we can actually build like
a proper agent. And for this, we'd
usually use an agent framework. Uh I've
gone ahead and put three different agent
frameworks in here
uh so that you can pick your favorite.
So we have LangChain, Pydantic AI, and
Agent Framework. Uh I'm sure there's
other agent frameworks as well that I
missed, but hopefully you can find one
that you like there.
Uh so these are all, you know, the same
idea. All right, which one do we want to
show?
Someone vote.
LangChain. All right, LangChain is still
very popular and uh hopefully there's
some LangChain folks here today at the
conference. All right, so with
LangChain, we are using LangChain V1, um
which is a a nice uh newest TK version
of theirs if you haven't tried it in the
last year. And so we connect to the
Foundry models from LangChain. and what
we have here is a travel planning agent,
which is a classic example. So, it has
tools. So, we have a tool for search
flights, search hotels, and check budget
to check if a certain flight and hotel
fits within the budget, uh and then
search activities within a city. Uh then
I've got some middleware, which is just
for me to see what tools are happening.
And then we have the actual agent call.
So, the agent has a system prompt that
says you're going to help users find
flights and hotels. Uh you're you know,
it has some rules here like search for
both flights and hotels, prefer direct
flights, yada yada, always check check
budget, and then ask for activities at
the end based off the remaining budget.
Then we have the user message. I need to
fly from SF to New York City next month
for 3 nights. My total budget is 6 600,
and I want direct flights and an
activity.
All right. So, we have all that, and
then we are running the agent. There's
some additional code here that's just
logging out the tool calls so that we
can see it. So, let's go ahead and try
that out.
Okay.
And so, this is going to log out the
tool calls that happened. We're starting
off with GPT 55 here. Now, what's
interesting here, you'll see turn one.
Let me make this bigger.
Turn one, it says is parallel. So, one
thing is you can do with LLMs is uh is
like many LLMs support parallel tool
calling where if you give them a bunch
of tool definitions, they can suggest a
multiple tools that can be called at the
same time in the same turn. And this is
really good from a performance
perspective because on your server, you
can actually file like you can send off
requests in parallel to like two
different databases, right? Uh so, as
long as they're independent of each
other, this is a great thing that LLMs
can do is say, "Hey, these two these two
things can be done in parallel. Why
don't you do them?" So, uh GPT 55 on the
first turn and "Hey, search for hotels
in New York City and search for flights
in uh from SF to New York City." cuz
it's decided that there wasn't a
dependency between them.
And then, once that came back, once it
had all the options, it did a check
budget um based off of the flight cost
and the hotel cost that it got back from
that call.
And then, it saw what the remaining
budget was and then it did a call for
search activities with that remaining
budget. So, this is probably the most
efficient agent that we can have for
this scenario.
So, let's see if we get similar
um
results when we change models here.
Do do do.
And of course, here you can even change
and compare across both models and
frameworks, right? Because every
framework has a slightly different tool
calling loop. We also call it the
harness, right? So, a lot of times that
you're you want to compare both models
and harnesses and and you'll see there's
interesting differences across them. All
right. So, this time we're with Kimmy
and Kimmy is not paralyzing uh as well.
I don't know if that's because Kimmy
doesn't support parallel tool calling or
it's just deciding not to in this case.
So, this time it did the same Actually,
it did even more calls. So, it did
search flight and search hotels. It did
over two turns, so that's already less
efficient cuz it didn't paralyze. Then,
it decided to do two calls to check
budget cuz I think it was checking like
one more option. And then, it did the
final thing. So, this one took two extra
tool calls and it took longer because it
didn't paralyze that first uh set of
turns.
All right, let's see how we do with
DeepSeek.
And you can start to see why it's hard
cuz everybody asked me like, "How do you
evaluate agents?" Agents are the hardest
to evaluate because there's so much
going on. There's so many different
things that are happening along the way.
It's like, are is it calling the right
tools? Is it calling them efficiently?
Is it calling things in parallel? Um in
this case, you know, this one uh didn't
do any parallelizing, um but at least it
only did four tool calls. So,
you know, reasonably efficient. And then
Mistral Mistral often will see Mistral
often forgets the very last step.
And so, we'll see. Um you know, that's
the other problem with the agents.
Sometimes agents, when they get to the
like once their context window fills up,
they might forget some earlier
instructions. They may not be as
thorough um with, you know, paying
attention to what the original steps
were.
And sometimes you have to like kind of
prompt them along the way to
to remember like, "Oh, wait, you're
supposed to you know, finish up with
this final step here, right?"
Okay, so it did it didn't do parallel.
So, what we're going to see is GPT-5.5
is very good at parallel tool calling.
Um the other ones not not aren't doing
it. Okay, so Mistral decided to only
search flights and search hotels and
then not do anything else. Um so,
[laughter] it did it did it kind of gave
up there. Um so, that's an example
where, okay, we'd have to do some
additional steering there to be like,
"Hey, are you sure that you have
everything, right?" Um you could use
something like the route loop. Uh Jeff
Huntley is here today. He made the route
loop. And you know, you can you can
force uh you know, you can force agents
to be more aggressive
uh instead of just using the default
loop.
All right. Okay, so that uh that was an
agent example of saying we also have
agent examples in the other frameworks.
Um but what you see is the code is
really similar across them.
Uh I tend to think most agent frameworks
are, you know, pre- more similar than
they are different at this point.
Um but, you know, you're welcome to
check them out.
All right. So, now we can talk about
evaluations, right? So, we've been doing
everything just, you know, manually
running them and observing the results.
That's nice to get a feel for the kind
of differences that you can see, but
when you're actually going to be, you
know, doing something for production,
you do want to actually have bulk
automated evaluations that you can
reliably run and compare results, right?
So, the first step that we can do is
just uh doing evals for um
without, you know, with just using
string comparison, right? Um so, the
example I have here
is with that create calendar event tool
call, cuz what we can do is like we're
actually getting back the arguments, we
can actually just do a straight string
comparison say, "Hey, did it give back
virtual, right? We wanted virtual for
this, did it give back virtual?" So,
when you're testing a single tool call,
you can just check to see, did it check
did it call call the right tool and did
it use the right arguments? So, that's
what we're going to do in this one.
Um and we set up a bunch of test cases,
right? Cuz when you're running evals,
you want to have lots and lots of test
cases. You also want it to be easy to
add more test cases, cuz once your app
is in production, you're going to see
how users really use it and you're like,
"Oh, okay. Thank you. Everything's
broken." No, and then you're going to go
and add those new cases of user input to
uh your, you know, your evaluations to
make sure that you don't drift, right?
This is called like model drift or your
your your drift away from it. So, you
don't want your evals to drift away from
your user inputs. So, once they're in
production, you want a good system for
getting new user inputs into your eval
cases. So, here what I do is I've got
like lots of different um you know, uh
cases here. Like, here's a user message,
here's the checks, and these checks are
just doing really string comparison,
uh some list comparison, and we check
different things, right? We check the
date math.
Uh I always check LLMs on date math, cuz
usually they're kind of bad at it. So,
another tip, if you're doing dates, give
them just give them a tool to do date
math, okay? Cuz it's too hard to do date
math in your head. Uh especially on leap
years. I was evaluating
>> [laughter]
>> And LLM on a leap year, that was hard.
Uh then we had um
okay, ambiguous durations. I did one in
Spanish, right? It's nice to test across
different languages, whatever languages
you're going to support.
>> [snorts]
>> Uh this one I guess is written written
real slangy. Yo, can you book the big
conference room? Okay. All right, so we
have various edge cases there, right?
And then we're let me to run these
evals.
Okay, and these evals in this case I'm
going to run it across each of the
models and the use cases. A lot of times
in reality when I'm running evals, I'm
just running it on a single model and
then I'm comparing to like a previous
run where maybe I'd done a different
model. Uh but you know, for today uh
since we are actively comparing across
models, I'm going to run it across all
the models so we can see
um it's for each of them it's doing the
tool call, checking the args that come
back,
and deciding if it's a pass or a fail.
Uh now here's the thing about evals is
that you don't want to just have these
like
just be part of like your pie test, like
your test suite because these are slow,
these are expensive. Yeah, question?
>> Um I see you just roll, you know,
checking strings against
Uh do you know if any frameworks do this
a bit more elegantly
>> You don't like my string checks. Um
yeah, so framework-wise for evals a lot
of so first of all, most observability
providers have evals built in, right? So
if you're doing LangFuse, LangSmith,
LangChain, um Arize, like they all have
their own framework built in. For
Foundry, we have um we have two
different frameworks uh for it and I
actually I do have the examples in the
repo. Um um those ones there's Azure AI
evaluation SDK, Open uh AI.evals
um from the OpenAI package. So there's a
bunch of frameworks, there's also
DeepEval
and Prompt Prompt foo in JavaScript if
you're a JavaScript person.
And which one?
>> Vali.
>> Vali?
>> Something like that.
>> Mark Vali, okay.
>> V A L L Y
>> V A L L Y, okay. I mean you use that
one. Um so there's a number of eval
frameworks um I'll I'm going to use a
fancier one soon. But for string check,
but here's the thing like like for
string check, you don't really have to
do a fancy one
um
because you're like
>> If you're looking for it to do a
specific
>> Yeah.
>> Do the parallelization you mentioned for
>> Yeah, yeah. So for tool calls, yeah,
that's where you're going to get a bit
fancier, yeah. Yeah, so I wanted to
start with the basic, but yeah, most of
the time we can't get away with just the
basic, right? Um oh, they did actually
really well this time. Wow, nice.
Um so usually we're going to have to
move to fancier evaluation. Um so that's
when we start to bring in LLM as a
judge.
Uh so this is cuz a lot of times, you
know, the the output is a lot fuzzier
and we need to use an LLM to help us
reason about that fuzziness. And there's
many frameworks that do wrap this um
For this example, I just decided to
write it entirely in the in the code so
you could see. So the idea when you use
an LLM as a judge
is that you need to give it, you know,
put the LLM in judge mode and say,
"Okay, you are an evaluator. This is
what you're evaluating and you need to
either say does it pass or does it
fail?" Right? We're trying to force the
LLM to say does this pass or fail? Um
and we also want it to give it reason,
right? It's really really helpful to
have it give it reason. So we want pass,
fail, and a reason. And then we give it
the query, we give it the response. And
for grounding this, we also want to give
it the context cuz that helps it
actually reason about it. So sometimes
in order to really evaluate, you do need
access to more information. So like tool
calls, if you're trying to evaluate
whether it was an efficient user of tool
calls, you can't you have to give it
everything. You have to give it the tool
call definitions. You have to give it
the traces of the tool calls it made,
right? So to build really good
evaluators, a lot of times you're you're
not just giving it the input output,
you're giving it every everything that
happened along the way, everything that
was shown.
Uh so here we, you know, we tell the
LLM, "Hey,
we're going to use the judge model of
GPT-5. It's a pretty good judge model."
And we're going to ask for it to output
some JSON that we can look at. So let me
go ahead and run
uh this
LLM as a judge. Now, here's the thing,
um this is going to be
even slower because now each time we're
running an eval, we're both running our
own code, which is using a model, and
we're then using another LLM to judge
that code, right? So every single eval
case is actually two LLM calls. And then
many times you actually run multiple
LLMs as a judge. Like you'll have like
five different evaluators that you're
running. Each of those is going to be a
separate LLM call, right? Um so that
that's what is tricky about evals is
that you can't just run them all the
time. You can't necessarily run them on
every single CI
uh and every single commit because they
are fairly slow to run. Cuz normally in
production, like for rag, when I'm
evaluating rag, you know, you usually
want like 200 test cases at least, maybe
800. And that's that's like a lot of
calls to an LLM, right? So that that
takes some amount of time.
Um so you do want to think about how
often you're going to be, you know,
running evals. So you can see that it's
going through its text it it's got a
bunch of different test cases, different
questions and answers. And it's it's
looking at the results. Now, in this
case, what I did was that I like pre-ran
the um
the questions and answers. This is a
common way of doing it, too. Like get,
you know, get all your get your context
for the evaluator beforehand
um because then you can change your
evaluator independently from your app,
right?
Um and that's more efficient. Cuz a lot
of times what you realize is that your
evaluator is incorrect, right? Like that
you haven't written good evaluator.
Uh so that's what you have to figure out
when you're doing LLM as judge, you have
to figure out like wait, is the problem
my app or is the problem my judge,
right? And uh you also want to calibrate
your judges with human input as well.
So, it definitely helps me working on a
domain you know, or work with a domain
expert that can help you label your data
and say and you know, do they agree with
your LLM as a judge? Was it actually a
pass or a fail?
Uh so here we get the results back and
we can see you know, the model
um
and their scores um
most of them got like two out of three.
Mr. Owl got one out of three. You know,
so they're they're they have some work
to do on being more grounded here.
So that is the generator of using LLM as
a judge. As you see, there's quite a few
frameworks that uh make it, you know,
that have built-in LLM as a judge that
make it easier to do it. Um but I want
to show that you you know, you can't you
can't also do it yourself. Oh, also I
should recommend if you're interested in
evaluation, Hamel.dev. I don't know if
he's at the conference this week, but he
has the most amazing resources and he
teaches courses all the time about
evals. And also he's very good memes. I
actually used these last night. So, if
you're ever chatting with someone about
evals and you need an eval meme,
uh what was it what I was doing last
night? Yeah, building an LLM as a judge
it's it's hard.
>> [laughter]
>> Uh so very important resource here. How
can we trust the LLM judge? You have to
calibrate your LLM judge.
Okay.
All right. So, that was LLM as a judge.
So now um but then they as you see, it
is hard to build
judge evaluators, right? Like you have
to like follow Hamel on Twitter and take
his course and learn all these best
practices for how you write uh a good
eval.
Um
uh so we have this new tool from
Microsoft Research. It's very new, like
the last week. Um it's called Assert.
And Assert helps you write the judges
based off of the spec. So, you write a
spec. You say, "Hey, this is the agent
I'm building and this is, you know,
roughly what I want it to be doing, my
idea about how it should work, and um
what kind of users it should support."
And then it will generate lots of test
cases. It'll like flesh out your your
spec into um into actual judging
rubrics, and figure all of that out for
you based off of, you know, all the the
it's very based in in research, right?
So, we've done that for the travel
planner already in here.
Um so, here's the um so, it's under this
assert eval. Okay.
So, what we can see is that we write a
YAML file cuz we all wanted more YAML in
our life. What I realized about YAML is
that I might hate YAML, but it's also
better than everything else for what I
need it for. So, there we go.
Um so, in this YAML, you know, we
describe
uh the context, and we describe, "Okay,
we're going to use this judge model. Um
these are the kind of dimensions we care
about is budget, you know, budget
pressure." So, we can we can give it
more information if we know, like, "Oh,
we care about ample budget, tight
budget, invisible."
Um you know, so, you can you can
stratify it. This is called
stratification. You can you can
pre-stratify if you want, uh or you can
just have it come up with the
stratification.
Uh and then we have more dimensions
here. And there's this there's also a a
skill an agent skill that helps you
write this YAML file so that you don't
have to write it yourself cuz
no one wants to write it, right? Um and
then we have the actual thing that's
evaluating. This is the LangChain travel
planner that we saw before. Uh so, this
just makes sure that it's tracing
everything cuz it's saying, "When you
are doing evaluations, you do want to
see every single tool call so that you
can really properly do these
evaluations."
All right. So, then it it runs it all,
and then we can see the results. It does
take a, you know, a decent amount of
time. So, we've already got the um evals
in here.
Uh so, I've got them running.
Uh there's like a little like front end
that you can use to view them. Okay.
All right. So, here is the result of
this um a search evaluation.
Um so, basically it you know, it came up
with the different behavior categories,
right? So, making like budget in
infeasibility, direct flight preference
rule violation, required tool use,
right? So, uh it comes up with what
behaviors are you know, allowed but not
allowed.
And then it comes up with the test set.
The test set is really is pretty fun.
Um
and here we go. Scenario 65. Red eye
before the installer walked through the
coach with six parent text one weekend
to see Alma. I really like that these
are obviously LLM generated titles,
right? So, it came up with all of these
coach with a clipboard. Um
it can it comes up with all these
scenarios based off that that YAML to
try and simulate users, right? Cuz the
whole thing it's really hard to
bootstrap your evaluation before you go
into production, but you want to have
evals before you go into production,
right? So, how do you figure out, you
know, what your test set is going to be?
And so, this assert framework helps a
lot with making that test set
and bootstrapping your evals.
Uh so, it has prompts and scenarios. And
then we have the results. Okay. So, for
the results, it ran it um across Deep
Sea, Kimmy, and GBD 5.5 and uh came up
with the you know, with the numbers
here. Um and in this case the the lower
numbers are better. And so, we can see
that uh GBD 5.5 did way better than the
other ones. I was actually surprised cuz
Kimmy, we've seen that Kimmy has
generally been quite good today um and I
was thinking it was kind of on par, but
at least for this scenario, uh GBD 5.5
had the lowest number of violations, and
so it is it's scoring the best here.
Um so So yeah. So this is assert. I will
say I'm I'm brand new to assert since it
only came out like a week ago.
Um so this is all I've I've used it so
far, but the idea here is that it's
helping you to build those evaluators to
build that test set and to follow the
best practices and bootstrap your evals
so that you can start start off um you
know, with with some really good evals.
Cuz what we're seeing is that we keep
telling people like you got to run
evals, you got to run evals, and then no
one's running evals or they're running
like the default evals like coherence
and fluency. Never run those. Like LLMs
are great at being coherent. You never
have to check if an LLM is coherent. If
some if they're not, like something
really bad has happened. Um I do
sometimes use the groundness and
relevance evaluators for my rag things,
but most of the times the built-in
evaluators are not what you want. You
want to build custom evaluators. And
that's what this is helping you with is
like okay, you need custom evaluators to
really see if your agent is doing a good
job. Uh but you know, you need some help
bootstrapping those custom evaluators.
All right. Oh, we have 3 minutes left.
I've been blabbing. Okay, finally, um
you know, earlier we were talking about
prompt engineering like okay, how can we
tweak this prompt in order to work
better for these models? That's pretty
painful, right? If you have to tweak the
prompt every time you switch models and
like rerun evals, that's like a lot of
work.
Oh, there's a little timer. Thank you.
Okay.
Uh so if you Yeah, if you have to tweak
the model every time, uh that's a lot of
work and you don't know which way to
tweak tweak the model, right? You don't
know the details of every single model,
what's going to really work well for it.
So uh what I've added is this as a final
example is using Dspy. Has anyone used
Dspy here?
Cool, a couple people. So Dspy, the idea
of Dspy is that you declare your program
like you say, "Hey, I'm making this
program that's expecting to take user
input and then turning it into a
structured counter bit." So, you declare
the constraints of your program and then
Dspy is going to figure out the prompt
that adheres to those constraints. So,
Dspy is going to write your prompt. So,
you you're basically checking your spec
in and then having Dspy by write the
prompts based off of doing evaluations
and seeing, "Hey, what prompt is going
to satisfy those constraints?" And it
actually uses these this cool algorithm
called Jeppa, genetic credo algorithms.
It can use these genetic algorithms in
order to come up with the next best
prompt to try, which is really really
cool to watch it do that. Um so, that's
the idea of Dspy.
And so, basically we have to set So,
it's very different, right? You can't
just take your standard code and just
use it. You kind of have to rewrite your
whole code cuz now, instead of checking
your pro- like your prompt isn't in your
code, your constraints are in your code.
Your spec is your code. The prompt is an
output from this Dspy process, right?
So, here I'm doing I'm asking it to
generate a numbered list where each line
has exact word count and the first
letter of the line spell out a target
word. So, this is the kind of input and
then we have a bunch of constraints that
are checking to see is the result
correct, right? So, you need to set up
your spec and then set up like checks,
tests to see, "Hey, does the output
satisfy this constraint?" And that way
Dspy can keep iterating, hill climbing,
right? Basically hill climbing until it
finds a prompt that satisfies those
constraints, right? So, you give it the
student model, the reflection model, uh
then it runs this Jeppa uh optimizer,
which you know, tries to find the best
um prompt, and then we get back the
result. So, the result I have it stored
here so we can see it. It does take a
fair amount of time. It took like 6
minutes on this task. Um but here, this
result is the actual instructions. So,
let me add word wrap into there.
Right. So, this is the system prompt
that it came up with based off of those
constraints and
those you know those checks, right? And
so this is nice because this is a system
prompt that works with Mistral. Cuz I I
picked Mistral cuz that was the one we
were having the hardest time with,
right? So especially with using smaller
models, this means we can use the
cheapest model and still get the results
we need, right? So there's been some
great talks by like Dropbox, Shopify
about how they've used DSPy plus Jeppa
so that they can move off the larger
models and use the smaller models and
maybe even deploy it on their
infrastructure and get the same results.
But the key was trying to you know using
this order to figure out what that
optimal prompt is.
So this is a definitely a different way
of writing your apps and
it can feel a little
different to you know to have the prompt
be the output of this process, but it's
also potentially really powerful
way of writing it and can give you a lot
more model independence and more
flexibility to be able to use more of
these models.
So I wanted to yeah, make sure that
people knew about that as an option as
well.
Okay.
All right. So So yeah, so that was all
the things that I wanted to show. As you
can see there's lots of differences
between models, different ways you can
improve the model output and then
evaluate it and then improve it.
I do encourage you like yeah, just just
tinker with the models. It's I always
learn so much whenever I you know try
out different models um
and see how different they are. Oh, I
never showed Anthropic. I meant to show
Anthropic. Okay. I do have some
Anthropic's deployed as well. With
Anthropic you do have to use a different
API. That's why I wasn't using Anthropic
most of the time.
But of course you might be interested in
Anthropic. They They use the messages
API instead, so you do have to switch
your code around. But I actually
specifically like it for rag because
here's interesting is that
with Anthropic they actually have this
notion of citations built into the
models. So, you can actually you provide
the sources
in this structured format. So, you say,
"Hey, this is my source. It's a
document. It's text. Here's the text of
it." And then you enable citations. And
then the Anthropic models are actually
trained to return back blocks of text
with citation. So, you can extract those
in a programmatic way, which is really
nice when you're like building front
ends. You can just link your citations.
So, that's really cool. So, that's even
another thing
to look at is
you know, a whole different ways of
calling models, too.
Okay. All right.
And yeah, we're kind of at time here.
The the repo will stay up. So, you're
welcome to keep working on the repo.
I do need to rotate the keys that I put
in that .env because I mean, I trust
you, but I don't know how much I trust
you. And Cedric always already said I
was bad for doing that.
So, I I won't be able to keep those keys
up for much longer.
But, hopefully with the repo you can try
it out. You can also try it out with a
llama. I added a llama support
yesterday. So, if you want you know, do
you want to try a llama, too? If you're
doing local models, you basically just
change the examples to point at the
local llama server. And you just have to
change the model names as well, right?
But, generally they should all work with
a llama as well because it's same API.
All right. Thank you, everyone. Oh, and
there's stickers.
>> [applause]
