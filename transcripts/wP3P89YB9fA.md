# Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar

Source: https://www.youtube.com/watch?v=wP3P89YB9fA

Uploaded: 2026-10-29

Transcript source: YouTube captions retrieved through the web extractor. Caption text is preserved; transcription errors may remain. The extractor does not supply segment timestamps.

## Transcript

[music]
>> My name is Taylor Luttrell and I'm
joined here by Kilian Carlson.
Together we make developer content at
Sonar, the maker of SonarQube. But
today, in particular, we are jazzed,
dare I say,
to get you all up and running with Git
Guardian so that you can both find and
critically fix issues
in your AI-generated code
before they ever emerge.
Now, before we dive into the hands-on
demo itself,
if you would please direct your
attention to one of the screens on
either side of this room,
we've provided for you a QR code and
also a link there below
which, once followed, you can use to set
up a free, I should note free, 14-day
pro trial for Git Guardian.
So, this is going to be really important
if you want to follow along step-by-step
and play-by-play with this workshop,
you're going to need Git Guardian. So,
we'll give you all a minute to get that
set up, should you like.
And just in the meantime, while you do
configure that, if I could get a quick
show of hands from the audience,
who amongst you is already using an AI
code reviewer as part of your CI
process?
Okay, so that's a fair number of you all
and that's what we like to see.
And whether you are or you're not, we
hope that you will be able to derive
some utility from today's session. We'll
give you all just another minute as you
sign in to Git Guardian and set up that
trial.
Next I have for you
another QR code and I promise this
presentation is not exclusively QR
codes, but this one is in fact very
important as this will take you to the
dedicated GitHub workshop repo that we
have created so that you can get up and
running with Guitar.
This project is going to help exercise
some of Guitar's incredible capabilities
and Mr. Killian here is going to walk
you all through that in a minute, but as
you get set up, I do want to note that
everything we do in this session is
going to occur in the browser. So,
you're not going to need to set up any
local tools, install any local
environments.
All you need is a GitHub account and
access to Guitar to follow along play by
play. Uh just a couple of housekeeping
notes as y'all are getting signed in and
set up. Uh in this workshop, we're going
to guide you through a few different
things, namely installing Guitar as a
GitHub app.
Going to need access to GitHub for that.
And then critically utilizing Guitar
across a few different pull request
scenarios. We have three prepared for
you in this demonstration that are going
to demonstrate how verification with
Guitar goes beyond simply code review.
And don't worry, this is very
beginner-friendly if you're not
especially technical. We're going to
start slow with Guitar's out-of-the-box
verification and then we're slowly going
to ramp and build into some of the more
advanced features. We're actually going
to create a project-specific
configuration that teaches Guitar your
project's conventions. And then lastly,
we're going to round things out with a
CI
uh failure diagnosis and you're going to
watch some automated fixes occur
directly on your PRs.
So, if you follow along with Guitar and
with this repository, then by the end of
this workshop, you're going to walk away
with Guitar installed,
three verified pull requests, as well as
a practical understanding of
a number of things such as, but not
limited to, verification instructions,
rules for your repositories, as well as
CI failure analysis.
I hope by now you're all set up with
guitar. You've logged into GitHub. Go
ahead and refrain from forking the
repository right now, as Killian's going
to walk you through the steps uh
specific for our configuration.
I want to start instead with a scenario
that I'm sure many,
if not most of us are intimately and
also frustratingly
familiar with, which is
we all know that AI coding agents are
wildly effective at writing code, both
at speed and also at volume,
but while these agents are supercharging
our teams to write more code and much
more quickly, we ought to pause and ask
ourselves who or what is actually
verifying the code that our agents ship.
And whether consequently
the code that our agents ship is not
only secure, of course, and maintainable
and reliable, but also whether it is
practically and not just functionally or
technically correct.
As we know, agents,
as they're generating more code and
they're doing so faster than anyone can
realistically inspect, a couple serious
issues have begun to arise.
The first is an obvious review
bottleneck.
We have teams with a fixed number of
members, but which are now facing
an increasing number of changes uh via
their AI agents. They're being inundated
with code to review, and as a result,
queues are growing, merges are sitting
waiting and unattended to, and reviewing
is essentially becoming
uh a job, a chore, if you will, that
nobody wants to handle and simply
doesn't have the time or the resources
to tackle.
Number two is we're noticing an increase
in the number of production incidents.
As incidents scale with the rate of
change given that coding agents
do not always respect the project
architectures that you spend so much
time devising your team or your company
or organizations coding standards or any
of the guidelines that you've
established. They're unaware of those
things. They lack the proper context.
And with these issues threatening to
undo the very progress that coding
agents promise, the answer has to be
faster
than
um
anything that humans can perform and
also better than human review
in order to keep up with the rate of
changes that are being introduced by
these agents. And so, what we have for
you is
Guitar, which is the
code change verification agent. And it
stands out apart from and above the rest
in a number of ways, namely
it functions with a high signal to noise
ratio
and effectively minimizing the false
positives, the number of false positives
in order to improve the fix rate and
reduce token expenses as well.
It diagnoses CI failures. This is really
unique.
And it separates real breakages from
flaky noise or infrastructure noise. And
it also, crucially, fixes these issues
accordingly.
And it fixes autonomously
also.
So, that you can move forward as quickly
and as freely as possible. Effectively,
you choose your level of automation and
you also choose your level of
involvement. We're giving you the reins.
Guitar also iterates until all of your
changes pass CI to be absolutely certain
that you can ship the code that your
agents are generating. And lastly, it
provides a high degree of transparency
into the review process and your CI
through a number of dedicated analytics
dashboards so that you can continuously
improve the speed, quality, and
effectiveness of your code delivery. So,
in essence, and and just to recap, Git
Tarr is designed for platform and
engineering teams
uh who need to ship code with confidence
at agentic volume and also agentic
velocity.
And it complements SonarQube with an
understanding of each code changes
context and intent.
And Git Tarr leverages a variety and a a
wide body of context sources to
accomplish this.
Suggesting educated and informed fixes
from such things as PR diffs
and details and comments and whatnot um
from the CI uh CI logs as well, the the
very logs that I personally hate to to
have to sift through.
Um from project-specific instructions as
well. Um
configurations that you can write
yourself in the repository rules and and
much much more. And we're going to dive
into some of those during the session uh
today.
And I should note that for anybody who
is worried about noise, as I mentioned
uh Git Tarr is tuned for signal
uh because we understand that every
false positive is a token spent and a
fix attempt that risks an
unintended change. Um and rather than
adding more noise and burdensome
decisions to an already complicated
review process, Git Tarr does do the
work of getting the change through and
in the process verifying and fixing
everything so that you don't have to
yourself.
At a high level
Git Tarr's review engine is triggered
when a PR is opened and it calls upon
that wide body of context that we just
spoke about to produce findings and also
fixes posted directly to your pull
requests as actionable guidance that you
can interact with
with comments
or if enabled, automatically fixed and
merged. And to demonstrate just that,
I'm going to pass things off to Kilian,
who's going to walk you through the
hands-on component of this workshop.
Should you have any questions, if you
get blocked,
feel free to raise your hand or call on
me. I'm going to be walking around the
room and I'm happy to assist should you
all need any help. Thank you.
>> Cool. Thank you very much, Taylor. Um
hey everybody, I am Kilian. I am a
developer content engineer at Sonar. And
um we're going to hop into the hands-on
section of this workshop. And before we
do that, uh the first thing, like Taylor
mentioned earlier, is we're going to
want to have the Guitar app already
installed. So, if you haven't done that
yet, please go to app.guitar.ai
and sign in from there and then start
the GitHub install. And the second thing
is right here, I have the workshop repo.
It's at
github.com/sonarsamples/aie-new-york-workshop-guitar,
but you can find it under the repos tab.
And
the first thing that we're what going to
want to do
is just go ahead and fork the repo.
And make sure that the owner is the
organization that you've installed the
Guitar app to.
And you can name it anything. You can
keep the name. You can name, you know,
test run, whatever works for you. But
the most important thing is that this
right here, copy the main branch only is
unchecked. There are multiple branches
for different exercises I'm going to
walk through, and if you only copy over
the main branch, you're not going to get
those different exercises.
So,
we're going to go ahead and click create
fork.
And once that's done, the next thing
that we're going to want to do is hop
into actions.
Right, by default,
GitHub disables workflows from forks.
And in order to set up some of the
things that we're going to do, like
automated merging and approvals, you're
going to want to enable that.
And then the last thing is that if you
want to make sure that Guitar is able to
read this fork, you can go into the
Guitar dashboard.
Um
go to settings.
Go to configurations and repositories,
and you should see your repo pop up
there.
But okay, just to hop into this
exercise. I have here Box Office, which
is a fake sample ticketing API for a
small concert venue.
>> [snorts]
>> And it's it's a pretty simple Python
project. We have orders.py here, where
somebody is able to purchase a ticket
or cancel it and get refunded.
We also um have this uh checkin.py, and
what this does it just handles the logic
for somebody to hypothetically be able
to scan a QR code and get someone into a
concert. And this is a pretty basic uh
example application, but there is a test
suite here um that cover all of the
existing uh functionality. And every
time a PR is opened,
uh the test will run.
And so, what we're going to do right now
is actually open pull requests for each
of the three branches that are in there.
And the reason for that is because
Guitar can take a few minutes to run,
and instead of having to wait for each
review to happen sequentially, we're
going to open them all up and then go
through them step-by-step.
One thing to note is make sure that you
set your base repository to um
what you are trying to do.
Uh set your set your base repository to
the fork that you have made.
So, I accidentally hopped back to the
base repository, but yep, right here.
So, I'm going to open new pull request.
Oops, I kept on checking it.
>> [snorts]
>> Yep, so you're going to set that to your
um
run right here, and then click
sequentially stage one, stage two, stage
three.
So, yep, create pull request here.
Going to set up another one.
Pick stage two.
Create pull request.
And then open up the third one.
Again, make sure that this is opening
against your fork and not the upstream
repository.
All right, so all three should be
running. Guitar should be running its
review
um while we wait. And so, let's hop into
the first PR right here.
Um
this is just going to be Guitar's out of
the box review. We haven't done
anything, we haven't configured
anything. This is just when it looks at
a PR, what it suggests. And what this
change does is
we are adding the functionality for
someone to order a ticket, and then
transfer it to a friend. So, if I buy
two tickets, and I send one to my
friend, we should both be able to go to
a concert hypothetically.
Now, I have included in some pretty
basic validation here that just makes
sure like, "Hey, the ticket's not
found." If you don't have a valid email
address or it's a voided ticket, it's
not going to let you transfer those
tickets. And uh some tests for that as
well.
And the tests for this uh PR pass. The
workflow is green. The CI is green.
Um
and one thing that I want to point out
here as well while we wait for the
review to land is that while Guitar is
is reading this, it's analyzing in a
different way than more traditional
static analysis tools or other tools
might be doing. Where static analysis
like SonarQube is incredibly important
and it catches security issues like SQL
injections to where, you know, traveling
through 20 different files and
functions, it's able to identify um you
know, SQL injections before they land in
your database.
What it can't do is infer intent, right?
By looking at your descriptions, your
titles, at your existing code base
compared to the features that you're
adding, it cannot infer that, "Hey, the
business logic that is being attempted
uh to create here
um doesn't add up in the way that it
should." That's why we need both layers
on top of each other. They cover
different capabilities and both of them
are complementary
towards having a fully verified
application. We need to be making sure
that our code is completely verified as
it scales in volume and speed.
Otherwise, um outages and and breaks are
almost guaranteed.
So, um I'm going to hop back into
the main conversations here and we see
that Guitar has added a finding. So,
anytime Guitar finds an issue, it'll add
a comment
um at the line that it finds an issue
and it also posts a code review that has
all of its findings, as well as
descriptions and suggested fixes, and
provides a nice summary at a high level.
If we read this here, it says buyer can
refund and void a ticket after giving it
away. So, when adding this PR,
right? When you buy a ticket and then
send it to someone else, if you go ahead
and cancel your original order,
it gets canceled for your friend. Right?
This is an edge case that wasn't
accounted for, and there wasn't even a
test that almost caught this. There was
a test that said, if you have a voided
ticket, it won't let you send it, but
not the reverse.
Um and it also identifies, right here,
that the issue is in the original
ordering file, orders.py. So,
the the if you were just a reviewer
looking at the diff,
you wouldn't necessarily see in the code
that you're adding that there's anything
wrong. You would have to have working
knowledge of how cancellations already
work in your application in order to
understand what's being broken.
Now, this issue only multiplies
as as we do more and more agentic
coding. The surface area of applications
gets more and more complex,
um and in order to maintain an
understanding of how every last function
works is almost impossible at the rate
at which we're coding. That's why
reviewers like Guitar are absolutely
necessary because it compares all of
your features against existing
functionality even when it's not readily
apparent in the PR diff.
And so, awesome. Guitar has posted its
review. Now, what do we do? It's very
simple. You can either click this apply
fix right here, or you can just comment
Guitar fix, right?
Comment that.
What Guitar is then going to do is add a
new commit to the PR. It will continue
to iterate and re-verify the new commit
blindly. So, if any side effects in the
workflows happen to occur, Guitar will
keep working, will keep iterating at no
extra cost per PR to make sure that it
gets fully green by the end.
So, Guitar is working on that extra fix.
And what it will end up doing is just
fixing in that orders.py
um file and adding extra validation for
this. Just takes a couple minutes and it
automates this entire process of
diagnosing a break,
re-pushing, and then fixing and
verifying your commits every time.
I am I am really passionate about the
fact that we not cannot be shipping
unverified code. This is absolutely
essential and we need to be verifying
every PR with context, with
verification, with both deterministic
and um
a logical understanding of what's being
done here.
So,
while this fix lands,
it'll just update uh the commit here.
We'll see it pop up in the files change
diff. Um it will analyze and make sure
that the workflow goes green,
and
um
it should be ready to merge.
But, I'm going to move on real quick
into the second pull request,
where we're going to cover context.
So,
every repo or every team has extra rules
and uh business logic that doesn't
necessarily get represented in the code.
So, that could be something that lives
in your senior engineer's head or in a
wiki or in a confluence page or
something like that. And these business
rules
don't necessarily have anything to do
with code correctness. So,
for this PR right here, we are adding in
a $3.50
service fee for every ticket that's
that's purchased. So, if you buy a $50
ticket to a concert, at the end you're
going to be paying $53.50.
But,
for this hypothetical company right
here, they have a rule that says
every price we show a customer is the
all-in price. I don't know about you,
but it is the biggest pet peeve in the
world for me when I go and buy a ticket
for something and it's like $30 and then
with fees and everything like that, it's
like $70 by the end of it. Um this
hypothetical company cares about user
experience. They care about you. So,
they have a business rule that says
every price we show is the all-in price.
But, how do we enforce it? How do we
enforce that this is going to get
reviewed by a code review agent. Well,
there's a couple different ways. One is
this uh review
directory.gitar/reviewdirectory
and another one is this
.gitar/rulesdirectory.
So, what a review directory does is you
can add all the context you want, as
many MD files, as much of your business
logic as you want to add and Gitar will
steer its own reviews according to this.
And this is super powerful, by the way.
Like, I encourage you on your own, just
throw as much context as you want at it.
Uh Gitar is incredibly efficient and
powerful at ingesting this and applying
it.
Uh for the rule section right here,
rules are awesome. I set these up all
the time. Rules are if a certain uh
criteria are met by a PR, then a rule
will fire and take an action. So, for
this one, is every time an some of the
pricing files are edited or updated, it
will check and present to a reviewer a
list of hey, these are all the customer
facing fields that are edited and it'll
let you know these are all in or
otherwise.
But you can do a ton with rules. Um one
that you can do is if let's say you and
another engineer are talking about uh a
new capability or feature in a Slack
thread. You can set a rule that says,
"Hey,
every time I paste a Slack link in my PR
description,
go into Slack, look at the conversation,
and check my code against the discussion
that we were having." And it'll just
fire every time that you do that. It's
super cool. I love this capability.
Um and if we scroll down, oops, a little
sneak peek of what Gittar found there.
But we can see that um there's this, you
know, service fee that gets added and
some tests.
If I hop back into the main
conversation,
we can see that Gittar posted his code
review.
It posted the rule, right? It sees all
of these pricing fields and it lets you
know, "Oh, this is is or is not an
all-in price." It finds the bug. Now
again, guys, this is not an engineering
bug per se, right? If you're just the
world's best programmer in a vacuum,
it's it's not like this is incorrect,
but according to your business and your
use case, this may or may not be what
you want to do. So Gittar is able to
check against this. It is so powerful.
We're not going to go ahead and merge
this one in.
Um we're just going to leave it before
hopping into the third exercise.
Oh, and just um
the Gittar fix
uh and then I'm going through and it's
been fully verified from the previous
exercise that we did. Um Gittar
uh approved it, fixed it, and we can see
that um
Let me look at the diff.
Then I went ahead and fixed this
orders.py
and added in this extra check.
But moving on to the third exercise. And
what we're going to do here is we are
going to enable full automation and
merging complete pipeline verification
from the moment you open your PR
to the moment that it gets merged in.
And there's going to be a little bit of
settings that we have to adjust here. So
if you want to follow along, I highly
encourage you to. If you just want to
watch and set this up later, the read me
for this repo has all of the
instructions available for you.
Um so the first thing that we're going
to want to do
is hop into rules, scroll down, and
click allow auto merge. That sets up the
GitHub setting that allows for GitHub's
auto merging.
Next thing is to go to rule sets.
Hit new rule set, new branch rule set.
And for rule set name, you can just say,
you know,
workshop
rule or whatever you want it to be.
Make sure it's active.
And make sure that you target default
branch.
And the rule that we want to set here,
the check we want to set is require
status checks to pass.
And what that will do
is if you type in test here, is that we
are going to require our CI to go green,
our test to pass before we say, "Hey,
this is good to go ahead and auto
merge."
Again, if, you know, you missed any of
those steps, this is in the read me
with all of those different requirements
listed there for you.
So go ahead and create that. And if your
company has secure
off set up like mine does, it may
enforce
a code, which I have right here.
Awesome. Cool. So we've created a new
rule set.
So, you may see already for this PR,
it's just been blocked. A test has
failed. But, what this is doing is it is
essentially refactoring the way that
tickets are scanned. Um
what it's saying is that, "Hey, we're
going to update tickets now at the point
to the ticket page URL and refactoring a
little bit of the logic that already
existed within the application."
Um
but the the the test failed. And if you
go into that and you look at what
failed, it says, "Test ticket cannot be
scanned twice." So, it caught a check
that was missed in the refactor. Um
if I scan my ticket,
I should be one and done. I don't want
to continue scanning over and over and
let all my friends use my same ticket
behind me. It's pretty basic, but it's
easy to miss logically.
In Guitar's uh review,
it is able to inspect CI. It says CI
failed. It says, "One test fails at the
gate check-in. Scanning an already used
ticket a second time returns 200." So,
if you have any failures in your
pipeline,
Guitar is able to inspect the logs and
fix.
One of the
I guess biggest annoyances in my
engineering career is like the test log
inspection loop, where you have to go in
and see what failed and then try and
diagnose and then, you know, fix it
locally and then push it and then wait
for the pipeline to rerun. And some of
these pipelines can get really long. And
then you're just waiting and then it
fails again and it's just this
time-consuming, money-burning process.
And you may even need to like keep
pinging another
engineer about reviewing.
And I'm getting a headache just thinking
about it.
Guitar just solves
all of that for you. It is able to
automate that process and keep going.
So, it's very simple.
All you have to do is type
guitar, sorry I'm doing this with one
hand, is guitar auto
apply
on
and then guitar auto merge on. And what
auto apply is going to do is just allow
guitar to keep pushing fixes without
needing you to to click yes on it every
time. And then what auto merge is going
to do is whenever it doesn't detect any
more issues and whenever your pipeline
finally passes fully, it's just going to
go ahead and merge that in for you.
Um
cool.
I'll add that.
>> [snorts]
>> Guitar auto apply on, guitar auto merge
on. If I refresh it, guitar Oh, it
already did it. Hit it with a nice
thumbs up. Thanks, guitar. Um
And so, guitar will iterate, push a fix,
validate it, verify it, and then
eventually merge it in. And this will
happen within a couple minutes.
This is
beyond powerful, right? To
be to be able to set up your
application. And by the way, adding the
comment like we did is just for the sake
of this workshop because I didn't want
to auto merge in the other PRs. You are
able to go into the guitar dashboard and
turn on auto approve and auto merge for
any of your repos that you want. You can
be selective. You can choose the level
of automation and approval that you set
up for each repository. If you have an
incredibly agentic workflow with tons of
guard rails and tests and a
sophisticated pipeline, um and then you
add guitar on top of that,
you're just able to let these rock and
roll right off the bat.
So, I'll refresh this.
Guitar still working,
um but it will continue to go and push
until everything is fully merged.
The repo as well.
Uh I encourage you to continue working
on it on your own at home. There are
some extra things at the end um
that that [snorts] are more advanced
capabilities for you to check out. Uh
Taylor's going to talk about a few of
them, but you have a 14-day pro trial
that I encourage you to use on this
repo, that I encourage you to use on
your own repositories. Um I think you're
going to get a lot out of it. Um so
instead of uh holding y'all hostage to
watch Guitar add its uh auto merge in as
it's iterating and applying those fixes,
I'm going to pass it over to Taylor to
talk about a few more features.
>> Well, thank you Killian for the
insightful demo. I hope that we were
able to help y'all get a rocking and
rolling with Guitar. Just want to pop
back up to discuss a couple more
advanced features that Killian has just
mentioned, uh which he touched on, but
whose
walk-through would go beyond the scope
of this short and simple workshop. So,
first note that at the bottom of the
read me in the repo is a take it further
section, as he just mentioned.
I would encourage y'all to follow that
after this workshop. Follow it at your
own pace, take it home. Um but to
quickly highlight, Guitar does enable
some additional features including
but not limited to
number one, functional validation. As
Killian mentioned, it checks each PR
against the ticket in the case of Jira
that it implements. And this is really
powerful because it ensures that the
change is correct and complete and not
just clean. All right?
So, it works with Jira currently,
linear. It works with Slack as well,
which you can can connect through the
Guitar dashboard at settings and
integrations.
For example, you can reference a Slack
message or a Jira ticket to better
inform and structure your reviews with
Guitar.
Guitar also takes advantage of a feature
that we're calling knowledge, which
learns conventions and also references
false positives from the feedback that
it receives and the feedback that you
provide to it. And it's weighted by
reviewer seniority, actually, which is
pretty neat.
Um
and this shows essentially the rules
behind every review, where they come
from, and why they're coming into play.
There's two that I would like to show
you all today. The first is cross repo,
and the other is cross PR analysis.
Cross repo analysis finds PRs that may
very well merge cleanly independently,
but um
but break code in another repo. Right?
And there's actually no limit on how
many repos it analyzes. Just food for
thought.
Um and then there's cross PR analysis as
well, which checks in-flight PRs against
each other.
As you probably know, or may very well
have experienced, I certainly have, two
PRs can each pass alone and yet still
break
production together, and that's just a
risk that grows with every agent you add
into the stack.
So, Killian's walking you through the
dashboard. Um just to quickly touch on
each of those features. Um if you would,
perhaps we could click into a single one
of these findings.
Note that it points you to the fix,
shows you where this is occurring, and
importantly, why it actually matters,
right? Why you want to defer to a uh to
Guitar to go about uh fixing it.
And that is Guitar in a nutshell. We
hope that y'all have found some utility
from this. Um again, feel free to take
this home should you like to better
familiarize yourself with the tool. Play
around with all of the context that you
can throw at it to get better and more
informed reviews.
Um there are a couple that come with the
um enterprise feature. All of this is
going to to ship with with Pro.
And so we'll open the floor now to any
questions. Should y'all
have any questions for us, we'd be happy
to answer those. Thank you very much.
>> Yes, so Git Tower has MCP connectivity.
It's able to ingest um context like that
in a variety of ways. Um
>> Configure your own integrations. Yeah.
>> That that sounds a little bit different
from the knowledge capability that we
have. That sounds more like the context
capabilities where it'll review, you
know, code against, you know, like
architecture guidelines and things like
that. The knowledge tab that we have is
um
steering Git Tower specific reviews. So
if Git Tower posts a review and suggests
a fix in a certain way,
you can say, "Hey, we actually tend to
fix stuff in, you know, this type of way
or or XYZ manner." And Git Tower can
save that for its own fixes in the
future.
That's a great question. I'd have to
follow up on you about how exactly
knowledge ingestion works. Um
but I I I believe I actually I actually
know for a fact that there are ways to
get that connected, whether that's in
the knowledge feature itself. I would
have to follow up with you about that.
