# ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay

Source: https://www.youtube.com/watch?v=TJPInBjhE4Q

Upload date (publisher UTC): 2026-07-12

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/a3/a32d95eba283d848f7e6d0fdffa54a793621a5d6db3f963867c969f28635af00.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.60s] Hi, everyone. I'm Sachin Gupta, and I'm a software engineer. The title is exactly what it sounds like. Your coding agent is creating review debt. Before I start, sit with the title for a second.

[12.86s] Notice what it is not saying. I'm not saying that coding agents are bad. I'm not saying they don't make us faster. I'm saying they, they're creating a kind of debt that nobody is measuring, and that debt is going to come due.

[28.48s] Over the next few minutes, here is what I'm going to do. I will define what review debt is. I'll walk five signal families that are going to compose it.

[37.14s] I'll score three real pull requests side by side, and I will show you a cross-repo scan of over five hundred PRs, which is nothing but three public code bases.

[45.68s] So let's go. So look here. Here's the gap nobody's measuring. GitHub's 2025 Octoverse report that covers almost every public pull request on the planet shows that the commits climbed twenty-five percent year over year.

[63.22s] And now over the same year, comments on the commits dropped twenty-seven percent. Now, these comments are nothing but the proxy for review activity. Code production volume actually went up, but the review attention went down.

[76.42s] They moved in opposite directions, that too, in the same year. Now, look at the teams furthest along the AI adoption curve. Faros AI tracks this cohort in their 2026 benchmark.

[88.40s] Median PR review time is up by four hundred and forty-one point five percent. And if you see, like if you calculate, you'll figure out that the review PR take five point four times longer than what they used to.

[101.77s] And then thirty-one percent more PR are now merged with no review at all. So AI produce-- AI is producing the code very fast. AI is producing the pull request very fast, but humans cannot responsibly review them at that pace.

[116.84s] This gap is called as ReviewDebt. It actually accrues quietly, it compounds, and right now, nobody has a number for it. But by the end of this talk, I will make sure that you will have a certain number.

[132.32s] Now, if you look at this particular slide, here is the story every team is telling right now. PR per developer are up sixteen percent. That's the Faros AI Acceleration Whiplash Benchmark, and that too from April 2026.

[147.34s] There were like twenty-two thousand developers, four thousand teams, and the median PR size is up sixty-three percent. Forty-four lines to seventy-two lines per pull request. That is basically sixteen months of long-term data from DX 2026 study, which includes four hundred organizations.

[166.90s] Now, if you see the cycle time open to merge, that is modestly down, and it is coming from the same DX study. The framing is very generous. PR throughput grew actually about eight percent, and the AI usage rose about sixty-five percent.

[182.34s] The gain that we see today is real, but it is actually smaller than the hype that, that is present. Every one of these numbers are real. None of them is a lie, but every one is a vanity metric.

[194.30s] PR count goes up when one PR splits into seven PRs. Median PR size going up is not a benefit, it's actually a bloating. Cycle time going down when reviewers stop pushing back.

[206.14s] These things tell you the speed of production. They do not tell you the speed of trust.

[212.18s] Now we will go into the next slide to see more.

[222.70s] Now, if you go looking for the second story, here is what you're going to find: reviewer fatigue. Engineers carry far more review load than a year ago. They're not happier about it.

[234.48s] Late-night merges. PRs are sitting unreviewed for three days, four days, and then they suddenly gets a thumbs up at 11:00 p.m. before a Friday deadline. Test theater. Tests are getting added, but they're actually asserting what the code did, not what the code should do.

[251.16s] They lock in behavior, including bugs. Architectural drift. Again, the same problem that is solved in three different ways in three different files. Nobody is actually holding up the architectural thread.

[265.90s] Finally, incident lag. When something breaks, the bug lags week or months after mon-- uh, after merge. Nobody connects the dot back to the AI-authored change. These costs don't show up in any dashboard until now.

[282.74s] We'll look into the next slide to know more about it.

[286.44s] So now let me give you the definition. ReviewDebt. It's the accumulating gap between code your agent has produced and the code humans have actually reviewed, trusted, and understood. It rhymes with technical debt, but it is more like a financial debt because it compounds.

[305.40s] It actually accrues interest, but this interest is not money. This interest is paid in human attention. It compounds because of the three feedback loop. First, the agent learns from your code base, fine-tuning, RAG grounding, in-context suggestions.

[319.88s] Code that was not deeply reviewed yesterday grounds tomorrow's PR. This debt becomes generative in nature. Second one, reviewers cede the architectural call. When most of a PR was generated, attention contracts to syntax and obvious bugs.

[337.00s] Big picture decision moved from review time to never. Third one, velocity expectations reset. Once leadership sees the new throughput, you don't get to hire reviewers in proportion. There is no slack left to pay the debt back.

[351.46s] Each loop on its own is survivable. Together, you will have a runaway, but the next question is: How are you going to measure it?

[360.79s] So how do we measure review debt? There are five signal families that has like 10 deterministic checks. Remember, the keyword here is deterministic. Every check is computable from a pull request and its repository.

[374.53s] No, we don't need any language model. Why? Because LLM, when it acts as a judge, it possibly can break two things. Number one, the score becomes a moving target.

[386.81s] The same PR, basically the score that you got for the same PR, will score differently when your model will change. Two, the scores stop being defensible in an engineering review.

[399.11s] You cannot put it on a slide. You cannot put it in front of an leadership. So what do you want? You want a number that is traceable to a deterministic computation, diff size and coupling.

[411.59s] Second, test evidence gap. Third, directory and ownership spread. Fourth, AI authorship indicators. Fifth, evidence and rationale gaps. These are the five families that will have 10 checks under them.

[428.19s] Let's walk each of them. The first one, the first signal that we have is diff size and coupling. This is the simplest one to calculate, basically. It's also the most often misread.

[441.39s] What it measures is the net lines changed, the files touched, whether changes cluster in one module or is it sprawling across many. Why the agent is struggling here? Agents are biased toward fix at the call site.

[454.89s] A human engineer routes a fix to the root cause. That keeps the diff very small. But an agent will reach into many files looking for the same symptom. The reviewer cost of a sprawling diff is not proportional to the size.

[468.39s] It is actually much steeper. So the cross-file coupling explodes the mental model a reviewer has to hold. We'll look into the second signal, which is test evidence gap.

[483.93s] So what is test evidence gap? Test evidence gap is nothing but test lines added divided by the production lines added per pull request. So AI-authored PRs, they ship with a far lower test-to-code ratio.

[496.71s] Sometimes there is no test file in place, and if there is any, it's minimal. So this gap is actually a consistent gap. And the problem with this particular thing is the number, the reason this number is basically brutal is the agent generate test.

[511.99s] They generate a lot of tests, but these tests basically assert what the code is doing. It bas-- It does not generate the test cases what the code should actually do.

[522.31s] They lock in the behavior, including the bugs. The ratio does not capture the quality gap. It just measures whether the test showed up at all. So the deeper signal is the next step that is a layer down.

[536.59s] We'll see the next one, which is directory and ownership spread.

[543.97s] So what is directory and ownership spread? Count the distinct code owner teams whose file appear in the diff. Now, what does it mean? Basically, a well-shaped PR concentrates in one team territory, but a sprawling one reaches across many team file, and the reviewer cost is enormous in this scenario.

[562.83s] No single human hold the whole mental order, uh, model. You need multiple approvals from multiple engineers in multiple different context. The coordination overhead easily exceeds the time the agent save producing the code.

[577.19s] This is where you start to feel the economics of review debt. The agent gave you free hours of typing. You spend those free hours buying multi-party reviewer attention back.

[588.25s] And the next one we are going to see is AI authorship indicators.

[594.01s] So what is AI authorship indicator? Before everyone gets defensive, this is not for the blame. We are not flagging that engineers use coding agents. We made the score so a PR shaped like agent-assisted authorship get extra reviewer attention.

[607.53s] So that way, you know, right, like, okay, this is the PR that is directly coming from the agent. And there are, like, the very common three detection mode. I must, I, I think everyone must have seen it by now.

[618.23s] One is the co-author footer, which is basically one of your strongest signal. You see that "co-authored by Copilot". Second one is the branch name pattern. Generally, you must have seen it says Codex, Copilot, Cursor prefixes.

[630.53s] Third one is basic "generated by", "assisted by", which is nothing but your PR body or commit message phrases. We did actually a real data check on three public repos, which comprised of five twenty-four PRs.

[642.55s] I'm not going to name the company, but for the sake of, uh, we are just calling it A, B, and C. Now, if you see the highest signal was the co-author footer, and the second one, the lowest signal was 0% on the repo C, even though it was done by coding agent, but they might have blocked it,

[660.45s] uh, saying any co-authored or, uh, like generated by et cetera, et cetera. The next thing that we are going to see is evidence and rationale gaps.

[672.37s] So evidence and rationale gaps. I think this is one of the most deterministic that I personally feel. It's the one that destroys reviewability the fastest. What it measures basically, does the PR explain the why or just the what?

[688.89s] On the left, if you see, we have an high gap. On the right, we have a low gap. The title says, "Fix flaky test." And all the data that you are seeing here is actually from some public repos.

[700.57s] Now, the PR body length is 18 characters. The commit message says updates. Obviously, I will not be-- If you gave it to me, I won't be able to review this, okay?

[708.69s] I cannot accept this. But in, on the right, if you see, when there is actually a low gap, the title actually is telling you what the change is all about.

[716.99s] The body has a symptom, the diagnosis, the change, and the link to the benchmark. Now, a reviewer can do the job. So in our regression fixtures and hand-scored teams, this signal destroys reviewability, fastest.

[731.51s] In the real open source data, PR bodies follow conventional commit format, so it fires most rarely there. But if you see the regression fixtures are just the demos. Okay, let's see how those five signal combine.

[745.35s] You will only have one number that is going from zero to 100, and the exact weights are basically your defaults. Now, if you're planning to adopt this, I would like you to do this first.

[755.55s] Run it backwards over the last 200 PRs that have been merged in your company. Calibrate the weight against your team actual reviewer experience. The score has to feel right against your actual guts.

[766.81s] We-- You are going to divide it into four bands. If you are zero to 24, which means you have very low review burden. If you have 25 to 49, you have normal, proceed with the standard care.

[779.19s] Fifty to 74, you need evidence from the author before senior review. And if you are [REDACTED:age] and above, definitely it's high split or request more context. Same shape as technical debt categories, but the unit is different.

[793.45s] Now, we are going to see what the scanner actually did.

[804.03s] Now, if you see, this is the clean PR. Unfortunately, I won't be able to give you a live demo today, but I will walk you through a CLI. I wanted to show three score pull requests side by side, the level where the framework become useful as a repeatable review conversation.

[821.41s] This is the first one. If you see, this is what the scanner says when a PR is well-shaped. Score out, zero out of 100. The burden is basically nil.

[831.31s] It's zero. We have a low review burden. The estimated minutes is six. No checks were fired. And if you look the structure here, that is why the list is empty, reviewer focus is empty, author next action is empty.

[845.74s] The framework only generate advice when it has something specific to say. A healthy PR produces a tiny, almost ceremonial report. That's exactly what you want. And the takeaway is most healthy PRs produce zero noise.

[860.91s] They get the work done without making any noise. This is not a tool that complains by default. Running it on every PR costs you one comment that says, "Look good."

[871.31s] That's it. Let's see the high debt PR now.

[877.93s] Now you see, what you see actually on the screen is from a public repo. This is a real scenario from the scanner regression suite.

[888.65s] If you see the score is here, sixty out of hundred. It requires evidence. It's, on the orange, it says Needs Evidence. Eighty-six estimated minutes of review effort. Look at the structured output.

[901.95s] It's actually not just a score. A why list explaining what fired, a reviewer focus list telling the reviewer what to do next, an author next action list telling the author how to bring the score down.

[914.69s] This is the part most PR quality tool miss. The score alone is useful. The structured advice is what actually moves the team behavior. Now, if you read the bullet four, it says, "PR has soft indicators of AI-assisted authorship."

[929.55s] This is information only, not a definitive claim and not a penalty on its own.

[937.81s] This particular ste-- uh, sentence is in the scanner output. The AI indicator check contributes five of the 60 points, which is nearly about eight percent. The other 55 came from a diff size claim mismatch and missing test.

[954.52s] Those would be high burden signals on any PR, agent authored or not authored. This is not an anti-AI scorecard, basically. This is more of a review burden scorecard. The agent did not cause the score, but the shape of the PR that is created by the agent did this.

[972.97s] Let's see the next one. This is a PR, basically, which is AI authored. It's very well-shaped and the score is sen- seven, which is low review burden.

[990.03s] Now, if you see the same agent, it has done the same kind of work, but the tests were added, so the CI is green. The risky path is called out in the PR description.

[999.29s] That's why we got the score as seven out of 100. It's very low burden, took only 14 minutes. The AI indicator check still fires, but it contributes two point.

[1010.55s] One, low severity. Second, the framework explicitly says, quoting the report itself, "Information only, not a definitive claim and not a penalty on its own."

[1022.95s] So when your team is going to ask, "Will this tool penalize us for using coding agents?" No. The answer is on your screen, low review burden. It's a very well-shaped AI PR.

[1035.41s] We are going to see the next one, which is basically our three public repos over five hundred and twenty-four PRs. I wanted to show you a 90-day AI search slope across three public repos and 524 pull requests.

[1049.86s] The review burden climbs even when the AI authorship doesn't. If you see this particular scan, we observe three things. One of them is the volume is the actual variable.

[1060.63s] AI authorship was flat, and it was five to 20% steady state, but the review burden was not. If you see one repo accumulated one hundred and eighty-six senior reviewer hours in 27 days, and another one took 43.

[1074.39s] The window length is same, but the volume was not the same. The burden was not the same. That is what PR volume is. Second is Amplifier only holds up under real data.

[1084.88s] Which means AI indicators fired on 5 to 20% of PRs every week across all three repos. None of those AI-authored PRs disproportionately landed in the high burden band. The positioning contract holds against real code bases.

[1099.64s] Third one is complexity drives burden, not authorship, which means across 524 PRs, four landed in needs evidence or high bands, which means all four were structural changes, which were large migration, SDK rewrites, multi-team refactors.

[1115.38s] The frameworks score complexity fairly. AI-driven volume creates the condition under which these accumulate. So now what 524 PR look like under the lens? Where does the review debt actually show up?

[1129.96s] In absolute terms, the scanner saw 524 real pull requests in three public repos, 228 senior reviewer hours cumulated across three public repos that were scanned over 27 to 90 days windows.

[1144.90s] Second one is nine PR per day, sustained merge rate, a high velocity repo. So if you see, it's all about the volume that is basically driving the burden.

[1156.22s] Third one is 5,036. These are the minutes that are basically spent on a single PR, which is nothing but 84 hours of review effort estimated for one single pull request.

[1171.67s] The score that we received there was 73, which said it requires an evidence band. Now, 5% to 20% of these PR every week across every week fire the AI indicator signal.

[1185.75s] Again, remember this is volume which is causing the review debt, which is changing the game altogether.

[1195.80s] We'll move to the next slide. Measure the problem. We have shown the cost. Now what do we do about it? So first thing is you should have one logical change per PR.

[1206.62s] I'm not saying like not small PR in the abstract, one logical change. That is enough. Second, test ship with the change. Even if the agent wrote the code, even if the agent wrote the test, the human author confirms the test assert what the code should do, not what the code is doing, what the code is supposed to

[1226.00s] do. Okay? Third, stay in one owner territory. Cross-cutting work splitting into per P-- uh, per team PR. Remain in your own territory. One approval, one context, one mental model.

[1238.76s] Author writes the why. The agent should not write the PR body. That's the moment the human author commits to understanding what they are actually shipping. Same review standard for the AI PRs as human PRs.

[1251.28s] The AI indicator amplifier only fires when other signals are weak. Keep the other four strong. The amplifier is invisible, so make sure there is no exception for AI. None of these is actually requiring you to have a new tool.

[1268.22s] These are the moves that you already are aware of. You just need to implement it.

[1275.94s] Now, how are you planning to adopt this? If you see, we again have five steps. Backfill, threshold, surface, aggregate, and talk about it. Backfill. So you run the scorer over your last 200 merged PR.

[1292.16s] Look at the one basically that has the highest score. Second, threshold. Set a basically justify line. Default, let's say you want to give it 50. So any PR scored at 50 or above requires a comment from the author.

[1305.74s] As simple as that. Surface it. Post the score as a PR comment on every PR. Don't block it. Just for the visibility purpose, surface it so that everybody should know what's happening over there.

[1317.50s] Aggregate weekly per team, which means the slope of each team debt line is the leading indicator. That's what your engineering manager should watch. Talk about it. Bring the number to a retrospective, every roadmap review.

[1332.20s] In every meeting, you should discuss about that n-number, like what was your score when you did this particular PR? That's it.

[1346.20s] Why this number matter? Because of this conversation? Absolutely not. Without a number, what you are just conversing is vibe. But if you have a number, it's actually structured. You can tell like, "Okay, with AI coding agents, we have a rollout which has added X percentage of the throughput," but you need to make sure you are also adding

[1367.02s] the Y points of the review debt that has been accrued over Z weeks. Now, at your current slope, that's roughly N sen- N senior engineer hours that you need to talk about.

[1378.56s] That moves the discussion from feeling to measurement, so you should always have a number. If you see, 2026, we are adopting things, but 2027 is the year when this conversation will shift to the governance model, and it's actually starting right now.

[1395.16s] Can you trust the code that you're shipping? If yes, we are good. If no, then who is accountable when an AI-authored change causes an incident? Where is the audit trail?

[1405.62s] So ReviewDebt is basically the bridge between these two columns. It's the first number that lets you have the right-hand side conversation without abandoning the left-hand side gains.

[1418.78s] We'll look into the final slide now. Now, three things I would like you to take away. First one is measure the gap. Don't build the tooling yet. Take 20 PRs from the last week, score them

[1436.10s] using the five signals that we discussed. You will basically get a number so that you will understand, okay, whether the framework is working right or not. Try to make the slope visible.

[1445.76s] The slope of a review debt over time matters most than the level. So plot it weekly and then discuss it with your team, maybe in a meeting or in a sprint planning, whatever the way you feel like.

[1456.90s] Have this conversation. Bring the number to your next review. Like, say that, "Okay, we do have X throughput, Y debt, and this is the slope," and then you are basically moving away from the vibe culture to the measurement culture.

[1470.94s] One quick call-out on anti-patterns to avoid. First thing is approve with comment merges. The AI did the boring part. No. Will you catch it in QA? No. PR are smaller now?

[1482.00s] No. Stop writing LGTM on the PRs. Make sure whatever we have discussed, the habits that we have discussed, we are going to follow them. This is the entire point of the talk.

[1496.02s] Thank you very much for listening.
