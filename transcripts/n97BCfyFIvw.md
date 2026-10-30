# "The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic

Source: https://www.youtube.com/watch?v=n97BCfyFIvw

Upload date (publisher UTC): 2026-07-14

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/c3/c3b6e2e41d74ee2bc206b15e8804e4f036e2f62565538ea6c7c95b4d2f6d5613.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.22s] [on-hold jingle] Howdy, folks.

[23.72s] So good afternoon or good whatever time it is when you're watching this on YouTube. I'm really excited to be here. And, um, today I want to talk to you about really, uh, what it takes to keep the human in the loop where engineering is concerned.

[40.70s] I really wanna start with the human side before we talk about the architecture here. I think that the engineer of the future is gonna be really defined by the person who is able to choose what is worth doing.

[54.73s] They're gonna own the evidence, they're gonna own the understanding, as well as the verdict around increasingly automated work that's being done by agents. Now, when I use the term verdict, I don't mean that we're suddenly all gonna be Judge Judy.

[70.36s] We're not. But what I mean really is something just a little bit different. I mean, we're gonna be accountable for the production decisions. Does something ship? Do we block it?

[82.36s] Do we redirect it or accept the risk? Quality is something that we all talk about a lot, but quality produces evidence. A verdict assigns responsibility, and answerability is really what lets us stand behind a verdict.

[99.06s] And this, of course, is not the only way that our industry is starting to think about our roles evolving.

[106.76s] Boris Cherny recently put some useful language around what many teams are starting to feel. The old craft boundaries are getting blurry, and roles are rebundling around the work itself.

[118.10s] And the important question here becomes a lot less about what is your title and more what part of the system can you own.

[126.78s] Now, I like this taxonomy quite a lot. Um, it's optimistic without being overly vague, so things like prototype, build, sweep, grow, and maintain. And these are real engineering modes.

[140.06s] Agents are gonna help with all of them, but the scarce thing is not merely doing the task. It's gonna be knowing which mode your product needs and what quality bar applies, and who owns the result at the end of the day.

[153.54s] Now, we've been talking about harnesses and loop engineering and software factories over the last couple of days. We can talk why this shift is happening. We've moved past the model as the whole story, right?

[164.78s] With harness engineering, the coding agent is the model plus the harness around it, right? Your context, your tools, your file system, Git. And the harness is what turns intelligence into something that you can delegate to.

[176.60s] The next move was loop engineering, where we weren't just prompting one run anymore. We were designing systems that kept prompting, checking, and remembering, and deciding what happened next. And that's really when agents started to feel like infrastructure.

[190.98s] And once you start putting all of those things together, you get that software factory. Dex covered this well in his talk. But you have agents that are running inside that inner loop and evidence that comes out.

[202.72s] Humans still end up making the production decisions in this loop, and the win really isn't moving us from it. The win is moving human judgments to the highest leverage checkpoint, I think.

[215.00s] And this is why it starts to matter now. AI-generated and AI-assisted code is becoming normal code for a lot of us. One of Sonar's twenty twenty-six surveys said that AI-assisted code is no longer marginal.

[227.70s] It's increasingly having a large role in our code bases. And once that happens, answerability stops being this philosophical word. It becomes an engineering requirement. And there's a quality point here as well, right?

[239.96s] Like, we used to care about clean code, code that people could read. But cleaner code is actually not just gonna help the next human and the next person on your teams.

[249.28s] It actually helps the next agent. Another one of Sonar's research, uh, studies found that clean and messy repos had roughly the same pass rates, but clean code actually used fewer tokens and caused fewer revisits.

[261.12s] So there's a lot of benefit to maintainability that can fuel efficiency for your factories. Now, making generation cheaper does not automatically make review cheaper, right? I think a lot of us are facing this moment, and we know that engineers are not naive.

[276.72s] The Sonar numbers say that almost everybody is skeptical of AI code. Now, I love working in my software factory. I love building my engineering loops. But the problem is still capacity.

[288.42s] If ninety-six percent of people don't fully trust that code, but only about half always verify before committing, we have this danger that we've got distrust without bandwidth. And so safety comes from making verification cheaper, clearer, and harder for people to skip.

[304.12s] And if you zoom out from the individual reviewer to the organization, review and validation start becoming a bottleneck when governance isn't able to catch up and adoption is already moving way faster than any company can go and set their policies.

[318.44s] And this means that we have some hard questions we have to deal with, like did a model actually touch this file? And the hard questions are also like what constraints guided that work?

[327.90s] What evidence was produced? What risk was accepted, and who owned the result? Now, the agent can ship more than any of us can review, right? So what are we still good for?

[340.38s] I think it's a question that's on a lot of our minds, right? And, you know, if Homer Simpson's experience automating computers can teach us anything, maybe this is our future.

[351.22s] I don't think it is, but it's one direction things could take. Now, let's try that again. If change is where humans enter the loop, if generation scales faster than comprehension, the scarce resource becomes judgment that's backed by evidence.

[366.38s] So the question is no longer how much can the agent do, but where does human judgment still create leverage? Now, I want to talk to you about two terms that I'm going to use for the career part of this talk, alpha and decay.

[382.54s] Alpha is the gap between what you can do today and what current models can do. That gap is a very real thing, and decay is the clock on that gap.

[394.62s] If the thing that makes you special is a capability, the frontier is eventually going to come for it, right? And there's a whole conversation around this. This is one of the reasons why taste keeps coming up.

[407.44s] Paul Graham had a point here that I think is very right. When anyone can make anything, choosing what to make becomes very important, and I buy that. But I also think that we have to be very careful because taste can become a magic word for whatever part of the work we don't want to explain just yet.

[426.06s] Mitchell Hashimoto gave us a more useful version of this definition. Taste is the ability to make high-quality, qualitative judgments where no objective metric exists yet. That matters because it puts taste before the benchmark and before the market has fully voted.

[442.50s] When you try out a model and you see the kind of UX and the kind of experiences that it builds, you can often tell when you think it has taste or lacks taste, or where there's a gap there that humans can fill.

[454.92s] Now, this is also only useful if we can turn some of this concept around taste into critique, examples, and better judgment over time. So yes, taste matters when production gets cheaper, and if anyone can generate ten options, the scarce skill is really knowing which option deserves to exist.

[474.98s] But taste is not some eternal moat. It's alpha as well. Now, the people with taste are still going to matter. I personally think they're still going to matter for a long time.

[486.46s] But the best version of that skill is not mystique. It's making better calls and leaving behind examples that your team and the system can learn from. Now, let's apply the decay test.

[499.75s] Well, we used to have speed. That decayed. We used to have recall. You know, harnesses have memory. Verification is moving into harnesses, evals, static checks, and model critique. Taste, I continue to think this is going to decay much more slowly, but it still resets as models learn from examples and preferences.

[518.74s] Even judgment, in some ways, is a slope rather than a wall. So the strategy is not to cling to any one capability. It's for us to keep moving our edges up a level.

[528.46s] So this is one of the reasons why what can the agent do is not the best strategic question anymore. The list of things that agents can't do just keeps shrinking.

[538.12s] The better question for us is really what can only a human be answerable for? Not because, you know, any of us are, are magical in any way, but because some decisions actually require ownership.

[550.88s] They require context, risk acceptance, and responsibility after that work ships. This is why the word engineer has to get just a little bit stricter. More people than ever can now make computers do things, and I think that's truly awesome.

[566.28s] The total addressable market for builders has never been larger, and that's so cool. But it's a huge expansion of the leverage. An engineer is not merely somebody who can code, you know, and, and get things to exist.

[579.47s] An engineer can reason about systems. They think about constraints. You defend trade-offs. You can manage risk, and you're the person that can be reached out to when things start to break.

[588.72s] So what are things that engineers should avoid if we want to stay effective ac- and accountable in this moment? Well, the first thing to avoid really is cognitive debt.

[599.14s] Now, cognitive debt is the erosion of your understanding and memory around how to solve problems. I think a lot of us start to feel this the more that we're using agents every single day.

[609.43s] I know that I feel this a lot, and it's because we're deferring more and more to AI to solve our problems. For code, it's the gap between how much code exists in your repo and how much any human on your team genuinely understands.

[623.59s] And this is why things like delegation depth end up mattering. You can have a build that passes, you know, your tests, a PR that you can merge, but your s- team can still end up losing its ability to actually explain the system that they are shipping to production.

[638.38s] Now, a very real pressure is almuch-- is also how much we delegate. So agents can now stay inside the system long enough for the human to lose the thread.

[647.60s] So a thirty-second run, right, can feel like an interaction, but an hour or a day scale task, so something long horizon, that's a work stream. And when tasks can end up l- you know, lasting that long, especially when you begin running many of them in parallel, review can't just be a glance at the end.

[664.72s] It has to become a whole control system. The second thing to avoid is cognitive surrender. Now, this is when you blindly accept AI's, um, responses. Like, delegation is important because delegation says, "Do the work, then show me enough evidence that I can judge it."

[682.42s] I still make a judgment in that situation. Surrender is really saying, "Hey, your answer is now my answer before I have formed any opinions myself." Now, uh, Wharton did a study that kind of offers us a warning light here.

[696.02s] When AI was wrong, seventy-three percent of people still s- thought that they, they, you know, they picked the wrong answer, and they felt more sure. So the failure mode is not using AI, but it's borrowed confidence.

[710.26s] The third thing to avoid is orchestration tax. Now, if you've been in the Bay Area, you will see people who, for better or worse, are still walking around with their laptops open or are talking to you about cloud agents.

[721.89s] And we're increasingly trying to run more and more and more in parallel or telling each other that we're shipping with hundreds of agents or thousands of agents. More AI agents running does not mean that there is more of you available.

[735.14s] Your cognitive bandwidth does not parallelize. So every loop that you create ends up causing more decisions to route, merge, verify, and integrate. And the fix is not necessarily fewer agents, but it's about designing your attention like a system.

[751.40s] Like where you enter, what you acquire, what you reuse. You just wanna be very intentional about it.

[758.06s] Now, accountability can be a scary word for a lot of people, and I wouldn't be surprised if it made you wanna go hide in the bushes and just tell your agent to deal with it.

[769.55s] But accountability is not what remains after agents get good. It's what lets the rest of the whole system scale. If agents can do more work, if they can do it faster, in parallel, better than what many of us could do, the scarce thing becomes the ability to explain intent, to inspect evidence, to accept risk, and improve the

[790.12s] system when the decision was wrong. Now, here is the career math. The half-life of an edge might be one model release. Speed, recall, verification, even taste all move as the frontier moves.

[806.00s] But the half-life of a signature, your credibility, your expertise, is much longer. And by signature, I really mean the name on the work, the person, the team, the institution, whoever stands behind what's actually shipped.

[821.20s] So skills can earn leverage. Accountability can turn leverage into trust. And this is one of the lines that I wanna draw pretty clearly. Agents can choose, they can route, they can merge, they can escalate, they can operate inside policy.

[834.72s] And in many systems, you know, they can, they should. But execution and responsibility are very different things. The agent can follow your runbook, but it can't inherit the consequences.

[844.80s] When something fails, the question is: Who understood the policy? Who accepted the risk, and who owns the blast radius? High agency is something that a lot of us talk about these days as being, like, this thing that we're looking for when we're hiring.

[858.24s] High agency is actively taking ownership of your outcomes. So knowing when to delegate, when to inspect, when to stop, and when to put your name on the result. High agency in this world is not, "I personally do everything."

[871.94s] You know, that version doesn't really scale. It's not just hustle theater, but it's ownership with judgment attached. This agency ladder tries to make that a little bit more concrete.

[883.02s] At the bottom, you've got someone that flags a problem and leaves it for the system. Higher up, they execute, diagnose, propose, recommend, and resolve. And the rare top movement is discernment.

[895.18s] You know, maybe you find a problem and you decide whether or not it's worth investing in. Maybe it's not, and maybe you move on. But when agents make more paths possible, agency is not chasing every single path.

[907.56s] It's really just deciding which paths deserve your ownership and attention. So translate that into an operating model. Agents can run much more of the inner execution loop. They can investigate, implement, test, and report.

[921.08s] I think that there's leverage in that. But that outer loop is still engineering. So deciding, verifying, approving, owning. That inner loop is capability. The outer loop is agency.

[933.06s] And this is a boundary that I really care about. Your agent returns evidence. It returns diffs, tests, logs, rationale, traces, trajectories, screenshots, whatever the work itself requires. But then the engineering really begins.

[948.72s] We decide whether the work was worth doing. We verify whether the evidence is enough, and we approve or redirect or own what reaches production. It doesn't matter if you're someone that's just working with a small number of agents or whether you're working with thousands of agents.

[963.36s] I still very much think that these ideas apply. So the boundary is not human looks at AI output. The boundary is evidence and responsibility.

[973.70s] So here's an operational rule. Explain it or don't ship it. And it's not because humans have to type every line or read every line, but because someone has to understand the work well enough to defend it.

[985.39s] If you've ever worked in a large code base or an enterprise code base, some code bases have this concept of an owner's file or cer-certain subdirectories where there are people who are on the hook for that part of the system.

[996.34s] You can think about this in a very similar way. Who's accountable for that part of your architecture and your code base? Your model might write the code, and the question is really still whether you can explain those changes that the agent is shipping, whether you've got the evidence whether you understand the risks.

[1012.26s] Now, this is one of the things I want you to remember near the end. Automation moves the floor for all of us. Engineering continues to move up a level, and our new work might be loop design, evidence design, and brownfield stewardship.

[1027.36s] But fewer keystrokes doesn't mean less engineering over the next few years. It means that there is more surface area that needs taste, verification, ownership, and ultimately care.

[1040.44s] I don't think I've ever been more excited about the future of this field. Every time that we have made it easier to write software, we've predicted that the world would need less of it, and in fact, the opposite happened.

[1053.96s] Higher level languages happened, frameworks, cloud, low code. The pattern always went the other way. And when you lower the cost, latent demand ends up appearing. Those ideas that people didn't think were feasible to build and get out there are suddenly unlocked.

[1068.72s] And agents are gonna do the same thing for a lot of people. It's not gonna remove engineering work. It's gonna move the bottleneck from, "Can we build this?" to, "Should this exist, and can we answer for it?"

[1079.58s] So build the factories, keep the lights on, own the verdict. I hope this was useful. Thank you. [audience applauding] [upbeat music]
