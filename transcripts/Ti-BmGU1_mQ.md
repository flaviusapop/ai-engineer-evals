# The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI

Source: https://www.youtube.com/watch?v=Ti-BmGU1_mQ

Uploaded: 2026-10-17

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> Uh thank you for everyone for coming
here. Uh not too sure whether to be
happy or sad that so many people are
suffering from the token bill. It's a
full workshop. Uh
Yeah, that uh we're going to talk about
tokenomics. So,
a little bit of a a background with the
kickstarting it, right? I'm Eugene from
Felis AI. I'm CEO and founder of of it.
Uh and I'm part of the team behind the
Arabic AI open source project, the first
AI model under the Linux Foundation. And
and we work on next generation AI
architecture. Uh that's a little bit of
my academic background. And my Twitter
handle is PicoCreator. But,
but more importantly, right? Uh
uh
a little bit of background for Felis AI
is that our mission is to make AI
accessible for everyone, every language,
every dialect, every country.
And we do this We do this by creating
the world's largest platform of open
models, of over 40,000 open models. And
this includes specialized fine-tune like
the Sunflower model, which is Uganda's
first language model, specifically for
their language, and a lot of other
specialized models. So, we're not just
not talking about the biggest open
source model, but specialized language
models or specialized use cases, uh some
of it which I'll touch as well.
And when we when we can go on scale in
terms of variety of model,
Felis AI also we serve customers at
scale. So, some of our largest customers
are literally serving 2 trillion tokens
a day.
And and they're And and they're serving
it at around 0.3 per million tokens or
60K a day.
And they're doing it on around 512 AMD
GPUs, uh MI215. Uh
and for this customer in particular,
it's a private 400 Android BM OE model.
Uh and they're serving it around Opus
4.8 class performance. So, it's lots of
concurrent requests, lots of token
volume. That's what we mean by scale.
And if you look at it, 0.03 per million
token at over 4.8 class, it's not
something that is not something that you
can get off the public cloud market.
This is specially very specialized
setups that is meant to run at the scale
that we are talking about. So, that kind
of
uh leads in into two major disclaimers
that I'm going to start off. One, we
sell inference. So, everything I cover
here will cover the will will touch on
any provider. Nothing here is specific
to Fiddler's. But, to to for clarity, we
sell inference. So, so this is from our
data points, from our experience,
respectively, as well. Okay?
The other thing is that
this workshop is going to cover a lot of
optimization at scale, and it probably
will not fit you if you're like spending
less than 10K a month in your
organization.
Uh my word of advice for those who are
below this this uh metric mark, and this
is an arbitrary metric, is that if
you're spending less than this, you're
probably better off focusing on like
trying to get strong use cases within
your organization, rather than trying to
optimize the token spending bill.
Because a strong use case can bring your
organization way more than 10K a month.
And and that's and that's what should be
your main area of focus, and that's not
my area of focus for this talk.
So,
what we are going to cover in this
workshop uh is four moves in in in four
major order: measuring, right-sizing,
uh how do you buy your capacity, and how
you check your process.
So, measuring.
Yep. You'll be surprised at how
essential this is. Uh
like, how many of you know your total
token spend? Can I have a raise of
hands?
Wow, only half the room raised hand.
Okay. How many of you can measure at the
department level? Those those who have
their hands raised up, leave your up.
And so, I see about another half went
down. Yeah. And it gets lower and lower
down to the team level, to the use case
level. Uh we like easily 30 40% of our
customers that reach out to us, the
first thing they had was a single shared
key that everyone in the organization
used. And that was like
Uh uh how do we even measure that? How
do we start from there? So So this is
not and a vendor specific like you need
to start splitting up your keys, start
splitting up by departments, start
splitting up by major use cases so that
you know where all your tokens are.
Um and this is then from then on it can
inform your workload.
So yeah, API keys shouldn't be that hard
to issue. Um once you know that, right,
you can start right-sizing things uh
respectively. Like like which team is uh
and workloads spend on it? What was the
person waiting for? Like some teams
deserve the tokens per second. Some
background agents running at midnight
probably can don't deserve the tokens
per second speed that you're paying for
it. Uh yeah, don't pay for ultra on a
background agent. That's just dumb. Um
and and from that also you can also look
at your usage to better advise like uh
dedicated capacity that you may
purchase, be it for open models or even
close models.
Uh yeah.
And also you can also check which team
spend the most token and whether they
are productive. Uh I'll touch on that as
well.
One of the things that you should know
in AI workloads, right, uh and you all
may already experience, right, is there
are two major tracks with very opposite
economics uh respectively. So there is
the agentic workload and obviously
there's things in between where it tends
to be like long-running multitenant
agents. Coding agents are a particular
example of this. Some Some Some may have
some devs like run coding agents like
literally overnight over a long period
of time with uh with multiple
compaction. And and these things
maximize the context uh usage.
Process automation is the other extreme.
Uh think call centers, think email
routing, things your meeting notes
transcribing, and things like that. It's
all It's much shorter in context in
general, though
there are a lot of examples that defy
this statement.
But, it's very process-driven, very
task-isolated,
and it's it's a volume game,
essentially.
So, well, what do I mean by more usage?
And this is probably one of the first
major explosion a lot of organizations
face.
In particular, when they jump onto the
open cloud hype or one of the cloud
clones. So, you like like from from from
various developer teams that we we
support, like for example, we sampled
one of the team, and it was only five
devs, and they were averaging around
continuously eight running agents for
one of the companies we work with. And
And so, they were previously running
Opus 4.8 of the API, and they were
essentially spending 150k a month
continuously running these agents.
Some of it is the agents that they use
to code, some of it is the agents that
kick in at night. They They were
slightly more advanced. They already
knew that they they they they should
kick things off at night when no one's
are working. But, essentially, they were
spending 116 billion tokens a month. And
we literally helped them switch to GRM
5.3 instance.
Previously, it was 5.2. They already
upgraded 5.3, and that was like a single
node. That was less than 10k a month.
And they were And they didn't see any
disruption or impact. So, knowing your
team allows you to make these decisions
respectively. And like like I
highlighted, like knowing
processes workload also allows you to
split things off. So, like, for example,
previously, they were running everything
throughout the day, but they they
started scheduling some of the
background agents when the team was
asleep, and it runs through night. So,
this allows you to utilize their
hardware respectively.
The As I I touched on briefly, the other
side of process automation is purely a
volume game.
Extremely predefined.
I
I can give you more specific example off
the off the record, but you think of it
as like millions per day or even tens of
millions per day, decisions in call
centers, lines of code scanned,
emails and text messages filtered. Like,
one of the telcos we work with, like,
they easily hit peak 10 million messages
in a single minute. And this shouldn't
come as a surprise. Happy New Year is
the worst. Yeah. So So So these
And they And they help And the reason
why they filter messages is because they
provide a feature about like providing
safe phone for kids. So they needed an
AI to scan like basically is it
profanity, sexual content, etc. etc. So
So this This is really not a long
context, but a volume game. Other things
like Other things is like maker-checker
processes, approval processes, document
processing.
These are all volume game for multiple
organizations. So I suspect for the
financial institutions here, since we
are in New York, a lot of OCRs, a lot of
documents, a lot of approval, a lot of
transaction risk the is is under this
category.
Okay.
So yeah.
If you're not yet tracking your token
token spend and token view split, right,
we are open sourcing
a tokenomics tracking tool, which is
just a very fancy way of like splitting
up your API key and tracking which API
key spends how much,
which is separate from this talk. Yeah.
So if you If you want to again update
it, feel free to to scan this QR code
and respectively. It also if you want to
slides for this talk and when the
recording is released from AI
engineering to be notified about this
talk, you can also get
fill up the form there.
Okay.
Okay. Okay.
So yeah.
That was about measuring. Um yeah.
If you are not measuring, you can pretty
much ignore everything else I say and
start with measuring first because
all your biggest ROI is just by
measuring. But once you have things
measured, right, the question is
how do you right-size it? And this is
where things gets more complicated. Uh
In In general, right,
one of the things that we start to
observe as as AI gets deployed at scale
within organization is that there tends
to be a pattern of like because AI is
the shiny new hammer, we try to apply it
to everything. Especially within the
innovation labs, we just try to apply to
every damn thing. And we tend and and I
have seen
organizations literally apply fable to
really the silliest of things. So so you
there's a lot of models and a lot of
models are really expensive and and and
and and figuring out
to do and where it fits is is is
important is an important step of the
process.
I know open models I mean a lot of you
probably heard about open models and
that's our line of business.
Yeah.
And and so a lot when a lot of companies
come to us for example to like find open
models that fit their use cases
and drop in replacements. This is
we generally guide them along their use
cases. So these are these are general
rule of thumb that is probably going to
be updated month because open models
release every few months and same thing
close source models.
Things change rapidly. But but there but
the thing is what we find right exciting
actually within this year is things have
started to change. Like in the previous
year
the best close source model is without
better than the best open source.
Almost.
But as this year approach right we are
starting to see the gap close. We are
starting to see situations where where
some of the open models are even on par
or even surpassing. So like for example
before the Opus 5.5 update came out Kimi
K3 was
beating Opus
in UI design in some of the UI
benchmarks.
And and this is like very
public benchmarks. Within customer
benchmarks right we were already
starting to see open source models beat
very specialized benchmarks in
specialized use cases. So like A
particular one to highlight is like for
example, step one five model. They it
was able to achieve near Opus and extra
quality despite being like a 10 x
smaller model in financial benchmarks uh
financial use cases. And this is it the
best coding model? No, but in that use
case, it's actually extremely strong and
competent.
So so so the landscape is slowly
changing where where where you can have
drop-in replacement for a lot of use
cases that are sometimes even just 10 x
cheaper
respectively for the uh uh if if you
know your workload and you can drop it
in respectively.
Special shoutout is also DeepSeek-V4 and
Flash.
For some reason, and this model is
extremely popular across all workloads
respectively because it's easy to prompt
there
uh for a lot of companies. So well I
well the rest of the models I have
listed there they are they are like
default for good in their categories.
DeepSeek-V4 and Flash seems to like be
quite popular regardless the case. Yeah.
Uh though benchmark score doesn't seem
to justify why why is it so popular.
Yeah.
Yeah. Uh another thing to highlight,
right, is that recently like and this is
like for a few weeks ago,
uh
the a new class of uh AI models have
been introduced called uh classifiers
one-shot
classifiers most popularly known as JAF.
Open-source projects have already
started uh taking off like simple JAF.
And these are models that are entirely
focused on just making decisions and
classification on on tasks. Uh the main
advantage is that because on a technical
level only, they are commonly 10 x
cheaper than existing models or even
faster at the same time. Uh the downside
is it cannot give a chat response. So so
so these are things that are changing
and happening that you all may want to
start looking into on like on like
segments of how you want to improve your
your token economy.
Yeah.
But
but back to the The the
the token economy part, there is two
major tracks and it is important to
separate out and track this
track them respectively. It on the
agentic side we're talking about long
running long context as I said earlier.
And
to and you have to understand this
workload tends to be extremely cash
heavy, extremely input preview heavy and
cash heavy and there's only a small
percentage of output. We see across like
agentic use use cases in employment only
1% of the request is to the output
tokens. And and and this is this is very
logical because it takes multiple turns,
rinse and repeat.
But
this also decides your token cost
because like if you've seen token cost,
right?
Deployment cost, right? Output is may
have the biggest number, but even your
input value is much smaller or the cash
is much smaller, it it gets repeated
heavily in in this use case.
Yeah.
This is not
coding agent workshop,
but one of the most common patterns that
we we see in a lot of organizations,
right? Is that is that typically
typically in terms of like trying to
scale up their AI agent deployments we
within within the coding teams, right?
They tend to have the best agent do the
planning and a faster
a faster cheaper agent do do the
implementation and then maybe the best
agent do the review again. There's a
good reason why this split is very
common across all the agent frameworks
is is that you get the best of both
worlds because like the implementation
phase is tends to be tends to be very
token heavy process. A lot of processes
repeated back and forth like key
modifying the file, testing, checking
for results, rinse and repeating. And
and you and most and most of these
agents are especially this
especially like Gemini 5.3 flash is more
than capable of doing a task at the same
quality level as a much more stronger
agent like I say Astra or Opus,
uh respectively assuming those agents do
the planning. We have worked with some
of the organizations where literally the
planning and review agent is the best
frontier close muscle model, and then
the workers that implement it is the GRM
5.3 flash as an example, or Deep Seek
4.1 flash.
Yeah.
One of the observations that we made
from from this from from this kind of
split pattern, right, is that
unfortunately, as much as we wish that
everyone does so, nobody really switches
their model to save the company money.
Um this people are lazy to switch the
models in general. You you want to give
an incentive to switch. Or or
alternatively, if your agent harness is
good enough, so like for example, some
harness like M, they automate the
process. Like like it uses a the weaker
model as a baseline, and then it uses a
big the smarter model to automate
switching when it needs a smarter
consultation.
This
This helps reduce the friction
respectively, and helps improve your
your token economics at user scale. Like
a a major rule of thumb that we we now
give our clients after going through a
few times is that you want the smarter
model,
and since it's already so expensive
as a baseline, but you but you want the
the faster model to the cheaper model to
be faster.
And that naturally sets an incentive.
People want to get their work done fast.
If the model is smart enough to get it
done and it's cheaper, they will just
use it because it's faster, not because
it's cheaper. Um we had teams where
where where both models were the smarter
one and the cheaper one was maintained
at the same tokens per second speed, and
it and as long as they had the token
budget in excess, right, no one
switched.
And it and on the flip side, we have
seen teams, which is the other extreme,
where they set an extremely low budget,
and so that if they use a smarter model,
right, they just burn it in one day.
Yeah, then everyone just switch to the
to the Dharma
into the faster model Dharma and faster
model because that's their budget. It's
like almost as if the smarter model
didn't exist. So, like be aware about
your team dynamics on how they switch.
The The best trade-off is to speed
because people are naturally
incentivized for it. So, faster,
cheaper, they will just switch it to it
respectively.
Yeah.
Once again, reminder, measure, and you
measure two separate token keys.
Uh and but this also goes beyond just
measuring. For example, like CICD is a
very common use case right now of things
running in the background.
Uh we we have helped set up for teams
like faster tokens per second
that that is running for the the users,
like the humans,
but much slower tokens per second
um speed, but much cheaper at scale for
the CICD pipeline. Uh and and this is
just the nature of like what's your
priority respectively respectively
across the task.
Yeah.
And you can control that at a key level.
So,
another major finding is that we had
experience with deploying for for teams,
right? Uh
uh
So, like for example, for some
companies,
uh
how many of you had the fortunate or
unfortunate experience of the CEO
saying,
"Everyone must implement AI now, and
everyone must have a second brain now."
Yeah.
Multiple organizations have started
this. Uh in some cases, like even in in
the UAE, it became literally mandated by
by by by the law of the country. So, so,
like
a lot of departments are not prepared
to know what is the trade-off
respectively.
So, a good rule of thumb, right? Well,
developers tend to know,
okay, all these smart models, what's the
trade-off
uh between deep seek flash and GR553,
for example?
Most
uh your your finance department have
absolutely no idea. Your your support
department has absolutely no idea. They
they'll just pick whatever's the first
model and probably just go with it. So
So, our general rule of thumb is that
give department models labels, but not
the model names. And this also gives you
a lot more control as you switch it out.
Uh what like like advised earlier, fast
versus smart, but in some cases also
like finance agent or Excel spreadsheet
agents. Um these are hyper-specialized
agents that were fine-tuned to those
tasks respectively. And
and this also gives you a lot more
control. It allows you to swap up the
model. It allows you to split split the
traffic and test in between with without
without telling, "Hey, users, please try
this." The downside is also users may
sometimes complain when you do that and
you screw that up. But having that
control is a good thing. Uh another
pattern that we see, even though you do
this, is maybe some of a dash preview
version. So, that's a variant of it, but
it gives you control without without
taxing the communication burden across
the organization. And this is extremely
important because like
like some of the teams that we work
with, right? We literally saw members
running Llama 2 models
when when we are talking when talking
about like in this year because no one
switched the option. Yeah, so you really
really need to need to uh need to set
this in place.
Yeah.
All right. Process track. Process track.
A lot of things that I mentioned earlier
don't really apply as much to process
track because process track tends to be
a lot integrated into the applications,
into the workflows,
uh respectively. And and that's just by
the sheer volume of the traffic. Um
yeah. And And of all of teams in the
process track, right? Uh they tend to be
a lot more focused on focused on the
right sizing already by default because
because if you're running like trillions
of tokens
you most departments will not approve it
like $10 per token million token. It's
just not possible. And and so so so they
start they start early with the evals,
the benchmark, and then subsequently
finding the model that right size fits
it. Uh
yeah.
So
So the thing is like the common question
is how do I know the smaller model is
good enough? You don't need to That's
the wrong question to say. You just need
to make sure you set up your test cases,
your evals, and your examples. And then
subsequently just do the search process
from there. Uh
companies like us will be more than
happy to help you because we have over
40,000 models. But then But then if
you're
It's also not that hard to just download
10 models from Hugging Face and just
try. Uh So So from that you you just do
the search, find the cheapest model that
kind of like pass most of it, and then
you just see how you iterate from there,
fine-tune from there. Uh we also have a
more specific process that I don't think
is unique to us that we'll cover as well
also.
So for example, like in for one of the
major telcos that we work with, right?
We actually helped their team lower
their
inference cost 250k to 7.6k a month
switching from existing close-source
model just by going through this process
of like, "Okay, you're running the best
model first. Let's see what what models
we can split off, and then subsequently
what's the models that we can fit in in,
and then what can we fine-tune?" And
this was This was like to uh beat the
customer support use cases and and so on
and so forth.
Yeah.
And
to re-highlight back Jeff uh and simple
Jeff, which is a open-source project
that we did uh that replicates it.
You'll be surprised at how many m-
percentage of your AI traffic is
classification traffic.
Uh
At the end of the day, right? Like Yeah,
sure. Answering the customer support is
text.
But even then, right? Even then, right?
A lot of teams, right? Already have
predefined text output that they put
into the context for the model to output
for most cases. And and you could use a
classifier there. And there's a lot This
is a new new new shift within AI world.
And that this is one of the big levers
for this kind of processes in lowering
your your token bill.
Yeah.
So,
one one one example of such a model when
it comes to fine-tuning. So,
a lot of models and processes, right? Uh
do benefit at this scale where you start
to fine-tune your own model. Uh on the
flip side, for coding models, well,
there are organizations that will
fine-tune models for you, like Devin,
for example. Uh
a lot of developers generally just want
the best model. So, it's kind of
unless you are in this AI space, it's
kind of hard to keep pace in fine-tuning
the best coding model. But on the flip
side,
for your domain,
it might be worth it to fine-tune a
domain model for your use case,
especially if the model is much smaller.
So, for AT&T, for example, when they
fine-tuned their models, they they they
went from being open class to like 27B
to even 7B models. And they have
published this. So, so we were one of
their launch partners. And you can
actually try their open dialogue models
respectively. And and This is basically
what they use behind the scene. And and
it's all about volume here. Like, I I
think I think most of you understand the
scale of AT&T and the call centers and
things like that. Uh yeah. But it's a
good example of how you fine-tune models
to to specialize use cases. And once you
reach that point,
other organizations that are major
example of like Shopify have started
doing this. And and things and and it
doesn't necessarily need to be a
large-scale fine-tune. So, for example,
in the Shopify use case, they did it
because Shopify
web store had a proprietary la-
programming language for how to
configure the the web store.
And the existing models just weren't
that great at it, so they went to
fine-tune it. Uh
but and AT&T also they had examples of
that uh
in particular on like how to arrange the
the cell towers and things like that.
Yeah. Uh very telco-specific task. I
might not be the right expert to answer
that question. Uh but they had those use
cases. So so they fine-tuned
respectively.
You too may have that those use cases.
And how do you bootstrap such a model,
right? Is that the good news is that
uh you can easily bootstrap things these
days because if let's say you're willing
uh if the best model that is too
expensive to run at scale can do the
task,
you can already get started. So so so an
easy way to do this, right? Uh that we
see very commonly is like either you
generate your own data or prepare your
own data, which is hard.
No one likes to do that for some reason.
But that but another common path is that
they start with an expensive model
and then they deploy in a small scale
and then they generate
they they generate data set. I
understand that some labs it's against
their terms of service to do that, so
you may want to check with your lawyers,
but there are labs that openly embrace
it. So, for example, Google Gemini uh
their their frontier models, they
literally have a dedicated API service
for this. Uh so so so this allows you to
build data sets respectively on your use
case on a strong model, which you can
then which which you can then reduce
dramatically to let's say a 7B scale. Uh
alternatively, open-source models are
more than happy for you to to to run and
distill on, so you can run the best uh
open-source models respectively as well.
Once you collect them, you can then
fine-tune the data
and then you can fine-tune and
respectively like different sizes to see
what fits best. So, once again, like in
the 80/20 example, they have the 27B and
7B for different levels of the call
center.
Like your routine your routine calls may
come in at a Wait.
I don't think I can say which size goes
where, but your routine calls can come
in for the much smaller model, and then
it escalates up due to some classifier
triggers as an example.
Then then so so so that's how you get
the traffic to flow, get the traffic
split, and then you get it at that
efficient level. Uh one of the things
that we also tend to work with teams on
on when doing this is that even even
when they go through the stages and they
completely split over their traffic to
the fine-tuned model, because the best
of the best models still progress,
uh they get they uh we typically advise
them to cut over a cut a part of their
traffic as a shadow traffic to the best
model to keep building the data set.
And and and this allows you to ride the
wave and progress of the best open
models respectively.
Uh and the unit economics is actually
very important here, because like
one thing that I would like to remind
people, right, is people severely
underestimate the the the speed that AI
is going, especially for models that you
can run much cheaper at scale.
Like you take this laptop as an example.
I like to measure, right, what is the
best model that I can buy in the most
expensive MacBook Pro
here. And today's best models, be it
MoE models at 31B, 32B, 27B size,
is already much better than GPT-4.
So,
essentially,
this model that can run on a laptop is
already better than the best model that
you have last year. Give and take.
People like to argue on the specifics,
but let's just say broadly.
And when you fine-tune it to your task,
that means
if you can run that model on a laptop
respectively, you can run it on on on
your GPU servers at scale much more
efficiently.
Yeah.
So,
Yeah. So, that brings in to the next
topic, buying GPUs which which which is
apparently increasingly a challenge. So,
yeah, that's where companies like us
come in.
One of the things that
we we realized through a lot of customer
conversations, people are rather
surprised that things don't scale
linearly.
Uh what I mean by that is like
there is a huge trade-off between tokens
per second on an individual request to
to the cost
to the cost of the request itself. So,
for example, if you do not care about
about the cost, you could run the best
the model, let's say a fixed model, on
the best hardware,
on all eight GPUs, batch size one, and
you could get, let's say, 100 tokens per
second, 200 tokens per second. If you
like if you really want and and and this
is not our specialization, like you
really want like thousands of tokens per
second, that's where companies like
Cerebras is more than happy to offer
that as well. And it costs even more.
So, there are definitely use cases where
this makes sense.
But,
it's but a lot of people fall into the
trap of thinking, "Hey, so if I have the
speed, maybe it's half the cost." It's
not even close. Like like a rule of
thumb that I sometimes say like, "For
every two x of speed, it's three x the
cost and it compounds."
In this specific example for JM 5.3,
it's like one JM node is like you can
see the same server, 112 tokens per
second for running individual requests.
But, if you run 16 requests in parallel,
you get about half the speed for all the
requests, but you literally 10x the
output total output. You And and that
that gives you like literally
around 9 to 10x lower in cost.
In just like changing your changing your
target speed profile.
And so, when a lot of customers ask us
like, "How do we deploy things at
scale?" Sometimes the first question is,
"What's the model quality you want? And
what's the tokens per second speed that
you want?" And then we start
recommending the amount GPUs, the amount
deployment. And this
this target tokens per second is an
important trade-off.
Essentially, um
in more extreme cases, right? If you
really, really can run things at 10
tokens per second, rarely anyone does,
but there are some weird use cases that
allows it. You can get even more
incredible to- total throughput volumes,
respectively. Typically, we see
customers choosing between 20 30, which
is kind of like
uh your chat GPT speed without without
too much thinking, all the way until
like 60, which is like the fastest
speed. And if they want 120 tokens like
it tends to be this this range. Most
stick between 20 30 to 60, depending on
how how long the chain of task is.
Yeah.
So,
yeah, uh I kind of mentioned you
generally only want to pay for the
tokens per second speed uh when when
it's in front of someone. Uh whe-
whether it's in front of your developers
or whether it's in front of your
customers. Those are the trade-offs that
you want to make. And even within then,
right? We have seen cases where even
just a slight tweak down, right? Can
easily save two times the cost, but has
near minimal impact for the cus- uh
customer, respectively.
Yeah.
And once again, background jobs, please
don't run it at 120 tokens per second.
It makes no sense when you do that.
Yeah.
So,
uh once you have Previously, I said
measure, right? You're able to see your
your your traffic pattern. So, a lot of
traffic patterns tend to be bursty in
some nature with some base load because
someone's always running something at
some time, uh especially background
agents. And and this is where you can
you can also
plan your deployments, respectively. Uh
I know it since we're are doing
financial a lot of financial may not
have this as an option, but because they
are only dedicated instance deployment,
but if for some cases where people allow
mixed where they have dedicated
instances with some burst to the public
cloud,
this is where you have some flexibility
respectively. So, like the biggest cost
savings you have right now in the market
is deploying a dedicated instance if you
know your base workload.
So, as long as you fully use it, you
kind of have a savings there. But,
it's a bit more complicated depending on
your traffic pattern, and a lot of these
things can be tested and validated uh
respectively. And this is like
essentially what any inference company
will work with you. It's not unique to
us. We'll be like, "Hey, this is Do you
know your traffic workload? Can you
share some data?" And then subsequently,
we'll be like, "Okay, we propose this
much. You can try switching to this."
And then we we generate we can generally
show you your savings respectively. And
in some extreme cases where you have a
lot of spikes, you may want to have
limit your dedicated capacity to a
certain amount and let the spikes spill
over to the public cloud respectively.
The different use cases uh
have different right sizing, but this is
something that by measuring your token
workload once again at the beginning,
you can start
exploring these options, and the savings
can be huge. Like once again, like for
the customer that we served two 2
trillion token, and that was like uh 4.8
Opus class model,
they are paying less than 0.0
$3 per million token. Like you can't get
that price anywhere. Yeah.
So, yeah.
Simple disclaimer is the spikes really
matter. Uh
it's very rare that someone has a short
spike at the extreme end where they like
run a workload every month at that
scale, and then nothing else matter. So,
so usually some base workload exists.
It's just how big of a base workload.
Yeah.
So, yeah. Then the last one is check
your processes.
Uh this has nothing to do with inference
optimization from here onwards.
Um
Some slides may sound that very critical
of AI, but I'm generally an optimist. Uh
just this I just want to lay that out
because things can be quoted out of
context.
So,
one of the
uh
Pandora's Box question or problematic
question that we are starting to see is
that a lot of organizations starting to
ask, "Hey, I'm s-
10x 100x in my token spend, but I'm not
seeing results at that same scale."
Um respect- like like we are starting to
see reports from from various
organizations like uh AI where AI has
limited productivity only has 6%
productivity or 7%, which is not the
scale that a lot of us were promised or
we envision.
And
and unfortunately, this is
the case because we are at the stage
where everyone's just taking a giant
hammer and hammering everything.
Um
it's not that AI is not useful, it's
just that we tend to just spam it
everywhere. And yeah, if uh there's a s-
there are times where I just want to
like, "Can you please not do this as
another co-pilot?" Because it's just too
much of it. You need to think of how you
use it respectively.
Uh um yeah.
And
and another major issue that we start to
realize is that well well AI's are
are being deployed at a larger scale and
more frequently,
and people get faster in creating stuff,
the organization
processes may not go as fast.
The first bottleneck for for coding
coding environments will be the CICDs,
and you all may heard that CPU becomes a
bottleneck respectively. Uh
another another thing is like is just
the processes in place
uh respectively. How do you trust? How
do you review? I think the previous
speaker spoke at length at trust.
Yeah, the lack of trust is what slows
things down. And this could be
rightfully so. Maybe the agent the the
AI agent was badly designed and
shouldn't be trusted. But it also flip
and inverse. What if hypothetically the
that agent was doing everything
perfectly? But people weren't trusting
it because it didn't have the test in
place, it didn't have the validation,
and it didn't build that trust. That
slows things down. And these things
make and these things have a much bigger
impact.
So,
once again, be very wary about how the
hammer is being used because you need to
make your adjustments accordingly.
So,
and this goes back into saying like
tokens are not work done. You have
uh
um um and one major example that I will
highlight, right, is is this happens
more often than than I would like, is
that sometimes spamming more agents and
more tokens sometimes means you get the
same task done multiple times. So, one
of the anti-patterns that we started
seeing, right, uh
we are well in overall the engineering
organization improve productivity by
clearing more issues quickly, automating
clearing of issues, for example, like
when someone like when a QA and and
things like QA teams reporting an issue
and the agent automatically fixing it
without even an engineer, those are
great. But
one of the one of the common issues that
we start facing is that people get
ambitious
really fast. And they instead of doing
small changes, they start doing huge
changes like changing like half the code
bases or one quarter of the code bases.
Sometimes when this is planned with
proper testing, it's great. But a lot of
times, right,
the change is happening at such a large
scale, right, the bottleneck becomes the
on the reviewer to merge the code.
And because because everything is done
on such a large scale where a human
cannot process it, one of the common
anti-patterns that we start seeing is
that okay, someone has implemented the
the there's issues being done. And
because there's so much code being
generated, issues that do not have code
generated do not get reviewed and do not
get picked up by the reviewer.
So, someone needs to generate the code
using an agent. And then when the agent
generate that giant pile of code,
which should be a lot less if they were
to like properly review prompting and
stuff,
the reviewer look at it and it's like,
"Huh, this is too many code.
Can I ask my agent to highlight what
changes are relevant and then
re-implement it?"
And and and in the end they started
rebuilding it by hand
with the with the agent. So, they
literally discard the first agent's job.
There's multiple good reasons why this
happened. For example, like reviewers
want to maintain control and quality of
the main code base, but this is a very
common example of a bottleneck where you
where where if you didn't think the
process through, you're just throwing
more and more things. And respectively,
and the speed is not
increasing. So,
review your processes. A good way around
this is naturally to to to instill
better testing practices and so that you
can automate that and filter out. Also,
reminding teams to like, "Hey, split up
your your your merge or or make it more
modular to make it easier for the review
process." Like things like that. These
are human processes. It has nothing to
do with the AI. And yeah, we tend to get
too excited about AI sometimes. So,
this is not just a code problem.
Uh we are starting to see like because
uh AI agents are being deployed to make
decks, this deck was entirely
design-wise was generated by AI. I went
through multiple iterations. It's not a
zero-shot. I I went through every page
like at least 30 times
to to change the text, but the design
was done by agents.
And and sometimes within the
organization you're starting to notice
people that just one shot from the
entire slides, things like that. And
and they start passing it around. They
start doing meetings. And then it's on
everyone else to filter what's the
inconsistency, what's uh
what's the misalignment? Why is this two
data points completely different? This
is also another example of like same as
the previous example, people generating
code or people generating slides or
people generating report and the burden
shifts onto a some human down the road
to verify things. So, be very aware
about this organization change. Uh
why am I still an optimist is that I I
don't think this is necessarily a bad
thing in itself because the problem is
everyone needs to learn. And this is
where we just start adapting our
processes accordingly.
Uh and the other major thing is that
well, there are a lot of common examples
on how to use AI.
You'll know your subject domain for your
organization better.
And there will be use cases where an AI
could be used in place to automate a
process, for example,
that could save your organization uh
millions of dollars or increase your
productivity at a grand scale
that
that only you will know and not me as an
AI expert will come in.
I like to point to the most uh famous
example that Walmart had where was it
Walmart? I believe it's Walmart. Where
they literally started putting a stool
a stepping stool inside every single
truck.
And that was like the simplest change,
but it lowered their bill by the
millions because it lowered back
injuries across for heavy goods
respectively. It it's some something
specific like that with the use of AI.
And and it may not even necessarily be a
the best AI model, but actually can have
the biggest impact.
Yeah.
Yeah. So,
uh doubling down on my previous point,
uh one of the term that that was coined
by uh that that's been trending is
called the slot grenade. So, generating
lots of things in AI and then leaving it
to someone else.
Do not let slop grenades happen.
Uh and this is a culture thing and a
processing.
Yep.
So,
the some guideline rules that I would
set and this is more subjective. People
people disagree.
Um to prevent a slop grenade from
happening, enforce that people should
own what they hand over or generate. So,
for example, this slide, I own every
text that is generated. If there's an
issue, that's on me. It's not my AI
agent who who who has an issue.
I do not get to hand it off to an agent.
I must own the responsibility. Same
thing for code, same thing for anything
that is generated.
And you also have to measure outcomes,
not usage. Uh
And so this gets more complicated
because I
I don't want to explain too too long to
this, but like there there is like this
simple formula that's that I think
people take as a rule of thumb, tokens
times price divided by outcomes someone
actually use.
And and and this help guide a lot of
things. Smaller, more efficient models,
faster model, bigger model, yada yada.
But,
what I don't like about this is that
another analogy that I'll use about AI
is think of it more as like supplements
or steroids that enhance the team.
Think of it as uh like if let's say I
use construction work as an example.
It let's say I can use it to increase
the muscle mass for the workers. For
example, not that it's ethically to do
so. I know that's not the case, but
let's just say as an example in the
train of thought. Some teams will have
it and they improve productivity, some
teams don't.
But, even without that, it's quite clear
some teams are much better than others.
And and so the AI being a supplement
here, right, doesn't necessarily change
everything. So, you need to be aware
that outcomes outcomes are hard to
measure
respectively, but it's something that
you can start measuring and observing
most importantly back to the first step.
Measure.
You know the tokens spent per
department, per team, and you can start
seeing which team is performing better
and you start seeing how much tokens
they use. You can start seeing what
works.
Yeah.
Yeah, as I said, this is flawed
measurement. So, yeah. Uh that's that's
the high-level overview respectively.
And if
if you want to to like kickstart your
process internally within your
organization, you can you can either
talk to me or my team or like you have
six questions for you to start asking
like
who team spent what, what's the what
what must you test to use a cheaper
model, what's your base load, what's the
default model for each team, and which
workload has a person waiting that you
need something faster, yeah. And how
much of what we generate is useful.
These are like guideline questions for
you to start asking to refine your
tokenomics.
Yeah. So, Q&A.
Yes.
>> Yeah, so when you mentioned
fine-tuning models, is that
>> Test, test.
>> Um
>> Yeah, I'm trying.
>> like SFT sort of fine-tuning or is there
like other sort of
uh fine-tuning methods that you have
depending on what specific use case
there is or what data there is?
>> Uh okay, so in general, it tends to be
SFT, but I don't think
um
Well, we do provide fine-tuning services
and it tends to be SFT.
I there is a lot of methods that are
happening right now currently. I know RL
is very sexy right now, especially in
the coding environment, because it's
easy to generate the data in the loop,
but what we realize for a lot of
organizations, especially like in New
York, for example, financial institute,
things like that,
there's not really an RL environment for
financial task, for example.
And and so it tends to be more SFT base.
And and there are also other
organizations like adapted adoption AI
where where they are starting to also
automate the the the refinement of the
data sets for you to train the model be
SFT base or thinking thinking of machine
base.
Focusing on this might be the wrong
question. It to me generally what people
should focus on is the evals
respectively. So here's a good example
for Jeff that came when the Jeff model
came out and then we did the open source
project called simple Jeff
which replicates the Jeff API for
existing open source model. A lot of
people quickly realized that the Quen
27B was really good at this task.
And and there were multiple teams that
went to fine tune the Quen 27B.
I on on our side because we are trying
to take the approach like our company
like we want to accept any model and
then we just build the API on top of it.
We started taking the approach of like
hey we see the benchmark we see the
existing model why don't we prompt tune
it instead. It's not even fine tune.
And then and then two weeks later as
hugging face went to do all the
benchmarks at scale like over 10,000
questions things like that. Somehow my
prompt tuned Quen 27B beat most of the
27B fine tune.
So
this this is not a flex because I'm
quite sure now my model is beat by the
recent Cloudflare fine fine tune model
that was done on a more proper basis but
it's more of like the tuning method
might the tuning method might not be the
right question it's more like what's
your evals and what's the results that
lead to it.
>> And follow for that do you need
do you need to collect golden traces for
the set of data you need if you're doing
SFT or whatever it is or can you do it
let's just say like your your prior task
the frontier models get like 80%
accurate right? So maybe 20% of the time
it makes some sort of mistake. If you
fine-tune on that, won't the fine-tuned
model also get like 20% of it wrong? Are
you supposed to filter that out somehow
and get only the golden traces for
training, or
can you just throw all the traces in
and train?
>> So, this is
more of a personal opinion technique
because uh so,
the generally, I try to split the data
set because people are lazy filter.
Um so, I try to at least get a golden
trace data set.
And the golden trace data set maybe is
much smaller
uh respectively, and we just and we then
we fine-tune that with a much heavier
weightage
uh
as well. But, there have been multiple
papers especially
as
especially
with thinking tokens
that even the non-
uh the failed task, right? The as much
smaller model, when you fine-tune, tends
to benefit from the training because it
improved the thinking process even if it
got the wrong answer.
Um this is something This is really a
good case of like try and then measure,
and it works 70% of the time. Sometimes,
you just you need to increase the golden
trace ratio, but it's a general rule of
thumb.
I think for a lot of customers when
they're trying to
to SFT down a smaller model, the general
rule of thumb they're trying to keep is
can I keep to the near same level of
performance, and maybe the eval is down
1% or even in some cases it improved by
10% because the base model wasn't
specialized for these tasks.
And
more importantly, does it 100x reduce my
bill?
So, that's usually the motivation
respectively.
Yeah, golden samples are critical if you
want to do beyond the baseline. And
sometimes that requires humans to
actually look at the data, which as much
as I love my customers to look at the
data more,
people don't like to do that.
>> Hi. Um how would you deal with uh code
spend that would mostly come from
Claude's code and all the integrations
there? Cuz then your model is fully
locked into the Claude uh ecosystem, I
suppose. Do you have any advice on how
to deal deal with those type of
situations?
>> Uh yeah, unfortunately Claude code is
the example of fully locked in.
>> [laughter]
>> So, uh sometimes sometimes the first
movement is actually getting
um them able to switch
the harness. Um
harness it seems to be a lot more
flexible thing right now. Like we have
seen organizations that are like fully
locked in. Like I'm only going to use
Devin only or Mboni. We have seen
organizations that um that are more
flexible. Like literally
they are running their they are creating
their own agent harness. And I'm my
response is like, "Why? Why are you
creating your own agent harness from
scratch?" Uh but
like a common one that we see people
switching to is for example Pi. And this
is also because there's a lot of
excitement around it. People have shown
that
even with the same model, it gets a much
cheaper cost per token because of the
way it's simple and efficient. Um and
from there on, the I think the beauty
for the Pi coding agent harness is that
it's easy to adapt because it's so si-
so lightweight. We've seen a lot of
teams that just start prompting their
agents to make modifications.
And once
once they have that, then then they
start getting the cycle of experimenting
and changing. Uh
a common way to get them to be very
incentivized to change is to actually
introduce a
a a good enough model that is really
fast, like 100 tokens per second. And
then suddenly they start giving that a
try. And some people start or like some
of the first shift would be they still
use their Claude code as their planner.
And then they instruct the Claude code,
"Use this Pi agent with this model to do
the implementation." Hence the planner
implementation split.
It's more yeah, and that's where the
transition started to happen. It's not
easy to change people's agents, but
yeah.
>> Um
Yeah, so an example of these could be
perhaps to expose this this smaller
agent as an MCP in inside cloud or
having these tools where you can offload
I I suppose is that something that you
would you you would say could work?
>> MCP is more tricky because MCP agents
unless done right don't have access to
your file system. So typically it's just
something way simpler like pies
installed and they run the batch command
pie this.
Yeah, that that's usually the case.
>> Thanks.
>> Yeah.
>> Can you share if possible any case
studies about
caching solutions being very thoughtful
about caching and the outcomes that have
been generated for specific customers
even if it's anonymized?
>> What's the specific challenge you're
talking about? You do one caching you
Okay, is your question more like you
want anonymized you do Wait, you do not
want customer private information to
save in the cache.
>> No, so so like with customers that
you've worked with have you got any case
studies you can share about the outcomes
that they've been able to generate
because of being thoughtful about how
they cache and different sort of caching
methodologies?
>> Uh I think this one we can take offline,
but in general for our larger scale
customers we deploy them with dedicated
cache. So it kind of solves a lot of PI
issues because it's the the cache is
only for that customer.
Um yeah, and obviously there's prompt
formatting, but I may need to dig in
more specifically like what you're
trying to ask here. The short answer is
yes, but there's a lot of way to
interpret this. Yeah.
>> Cool.
Sorry about that.
>> Uh thoughts on turn or task-based auto
routing?
>> Oh,
um I'm a I'm generally more towards
task-based.
Um
mostly because it's much easier to
control expectation at a department
organization level.
So, this this is back to like, hey, a
department may have a label model and I
kind of auto router that model for them.
Uh
I know there's a lot of hype right now
for turn-based auto routing. One of the
issues with turn-based auto routing is
that you need to lock down your your
turn-based auto routing to let's say at
most two to three models.
If not, your cache will be extremely
inefficient to be used. So,
um so for example, we have seen
turn-based for GRM 5.3 and GRM 5.3
flash. Make sense. But if you put in 30
models and it keeps changing your model
every turn,
your your low cache hit rate will start
to wreck your your optimization.
>> Yeah, that's what I've seen before. I
saw I saw it like request level and it
just didn't make sense and then
>> Yeah. But two models tends to be okay.
Uh task
and organization makes the most sense.
Yeah.
>> Yeah. Yeah, I agree.
>> All right.
Okay.
Thank you very much and uh if anyone
wants to find me specifically for more
questions, feel free to just come up
front and ask me or find me by the side
once the next speaker's here. Yeah.
Thank you very much.
