# State of Data — Sean Cai, Independent / State of Data

Source: https://www.youtube.com/watch?v=ZyIoTOAbRfs

Upload date (publisher UTC): 2026-07-26

Transcript source: First-party AI Engineer published transcript JSON: https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/25/25ef50f6de3a2becaa0b5670e84bdbe47cae7024756632b23b43b3791ae59cfa.json. Publisher reviewStatus: needs_review. Segment timestamps retained; transcription errors may remain.

## Transcript

[0.08s] [on-hold jingle] Good to, uh, give this talk, and, uh, I just wanna say right off the bat, this is probably gonna be a little different from what you've seen so far at AI Conference.

[20.24s] I'm here to not deliver an agenda on any company's behalf, but just to expose a lot of alpha in data markets. Um, but also just tell you what's really going on behind the scenes, um, in a, in a very murky landscape where nobody seems to know how Mercor, Handshake, and a lot of these folks actually produce data.

[38.92s] So, you know, q-quick reframe before we start. When people hear data markets, they picture Scale around twenty nineteen. They picture these rooms of annotators in like Manila labeling images, and that's, that's real, and it's maybe, you know, ten to fifteen billion dollars a year per lab, but it's kind of the least interesting part.

[55.20s] Um, the models work now. What's scarce and badly priced is the sort of data that takes them from generalist competence into real expertise. We knew this since, uh, twenty twenty-four when Scale got acquired, and we were, um, spamming a lot of GPQA datasets.

[69.74s] So look, um, let me start with this framing. Data is to the white-collar revolution what coal and iron basically is to the Victorian age and the information age right now.

[80.36s] Um, I have this piece called The TAM isn't a vertical. It's all of labor. And so the supply chain is basically just doing what every sort of industrializing supply chain does.

[89.94s] It unbundles. Two years ago, one vertically integrated giant like a Mercor or a Surge or a Scale AI, if you're guys-- if you guys are unfamiliar, they're massive data companies.

[99.72s] They had to do all of it, but that was because that's the only way that unit economics worked in an immature market. Today, um, that's increasingly not the case.

[108.58s] Specialists out-compete the giants at a lot of steps, uh, sourcing the people, building environments, uh, designing rewards, running evals. The fragmentation, I would say, is pretty permanent. It's not transitional.

[121.14s] And, uh, quality increasingly does not scale linearly with quantity, which leads to a sort of cottage industry in data land right now, where you have labs literally mandate, uh, vendor diversification on the scale of like twenty to thirty different vendors because they inherently distrust their ability to scale quality with quantity.

[139.96s] So to orient you, you know, here's, here's the sort of argument as it developed this year. Um, January, we saw a lot of industrialization and unbundling. You'll hear me come back to this mechanism I call the Antikythera mechanisms, which is this sort of bespoke systems that translate messy business context into evals.

[158.18s] Uh, increasingly important in labs' hungry quest for real-world seed data to set seed ends. Um, I also explored this concept called Type 1 versus Type 2 data, uh, contrived versus non-contrived for the more researcher types in the audience, and why the GPQA-style playbook that works in twenty twenty-four for data acquisition kind of falls apart on long-horizon,

[177.00s] non-verifiable work. Um, so, you know, going through all these topics, all of which are online, uh, I'll als- I'll actually just skip to the more interesting part, but I'm bringing this up just here in case any of the particular topics I talk about are, are particularly interesting and you wanna dive in more.

[194.84s] So model improvement is a function of three inputs. We all sort of see this, uh, commonly expressed as the compute data and talent. I put together this very, uh, like rudimentary sort of chart online in one of my pieces in a re- very rudimentary, uh, equation just to express the fact that, you know, if there's any sort

[212.86s] of imbalance in this compute data and talent, then you start seeing, uh, sort of inefficiency in producing, uh, what I call like generalized AI model performance, right? But also, uh, we, we see a sort of inefficiency in, in CapEx spend that i-- that is a sort of result of this equation right now.

[229.72s] Um, exponentially increasing CapEx spend, but sort of like, um, AI revenues are, are sort of falling far behind. Uh, data is sort of the underfunded leg here. It's the one that sort of turns a generalist model into a real expert.

[242.88s] It's the one that's, uh, actually, I believe, quite lacking in this equation, and thus because of the imbalance penalty parameter concepts that I'm expressing, um, presents a whole opportunity.

[255.68s] But, you know, going back to what I said at the start, what is data actually? So most people picture state-based data, the rows in an ERP, which is like the final output or a saved file.

[266.80s] That's kind of the twenty twenty-three like next token prediction model, um, and it's mostly personal data wrapped in privacy law. What is actually available nowadays is process-based data, which is the trajectory, the reasoning tra-trace, the sequence of decisions.

[281.60s] Um, so it-it's kind of what gets a professional to get from a blank page to a finished work output and sort of delineates how the work gets done. Um, so on top of that, it's a quality axis.

[291.90s] This is the vocabulary I'll use all talk. Um, type, Type 1 data is a sort of pure capture of real workflows like GitHub commits or session replays with minimal reward shaping by non-experts.

[302.44s] And Type 2 is contrived data where you sort of hire experts, you sit them in an arbitrary setting, you have them manufacture examples. Type 2, the right place to start models when they're reading at a first-grade level.

[315.14s] I think anybody in the world could teach them, uh, as a third-grade teacher. But Type 1 is what gets you from twenty to eighty percent, so to say, 'cause the, the, the realism is inherited from the work itself.

[325.66s] And the structural reason why it matters is the data is kind of the most depreciable asset there is. Um, a dataset is only valuable insofar as frontier data markets as the frontier moves.

[335.18s] So the only durable supply of it, technically, is a live business you partner with, not a dead startup's code bases like so many data companies out there are buying today.

[343.84s] The dirty secret of the industry, though, is that everybody sells, um, Type 2 and bills it as Type 1

[352.25s] So now let me talk about the central axis of how you can think about the sort of verification and deciding which application layer domains are, are, like, maturing first and why.

[361.15s] Uh, you know, there's a reason why Claude Science came out so far, um, you know, now in the future after models got good before a lot of other application layer advances.

[371.97s] So Jason Wei is a researcher online whose blog is great. You should read him. He has this law, it's called Verifier's Law. The ease of training a model to do a task is proportional to how verifiable the task is.

[382.22s] So I break verifiability into three axes here. And once you have them, a huge amount of this market stops being mysterious. First, asymmetry of verification. How hard is it to decompose a task into checkable steps?

[393.66s] Veracity of verification. How much consensus is there about what correct even means? And then thirdly, proliferation of verification. How often does the real world sort of hand you fresh examples of verified work?

[404.35s] If you think about why coding is the first mature AI app layer market, that's really no accident because we were blessed to have something called GitHub from Web 2.0, which solved all three of these at once.

[415.29s] Unit tests, they sort of give you objective decomposable correctness. The community agrees on what working code means generally, and there are effectively infinite public examples with these commit messages as basically free reasoning traces.

[428.65s] So they score high, high, and high on these three axes. Now, look where the money is trying to go now. Biology, security, taste, finance, healthcare, law. These sit pretty low on veracity, pretty low on verification, and the verification examples are sort of like locked all in these enterprise workflows no Web 2.0 system ever captured really, or very

[448.01s] sparingly few. Uh, that's why, you know, probably maybe you've been approached by Mercor to buy your Slack logs or your Jira logs as of late if you work [chuckles] at an AI company.

[457.32s] And, uh, that's the whole game, right? It's, it's predictive. It's not just descriptive. Classify any professions like tasks on these three axes, and you can sort of tell which markets mature most.

[466.11s] So it's no surprise that after code, we went to search, and after search, we went to finance, and after finance, we went to healthcare and law, and after healthcare and law, well, I'd say cyber, biological, uh, and scientific discovery, and maybe even taste, which is probably the most unverifiable out of all these.

[484.05s] So verification is a sort of bottleneck. Um, let me talk about why the industry sells a lot of snake oil here and why most benchmarks you see are, are sort of quietly fake.

[493.87s] Um, the dominant type two recipe is, like, let's hire domain experts. Um, let's have them chat-- use chat to generate plausible tasks. Let's have them solve those tasks, and let's cherry-pick the ones where the model diverged, and let's package them as a hard North Star benchmark.

[509.19s] And then this is the perverse part. Let's sell the data to hill climb that same benchmark. It's basically, um, and maybe some of you guys here in SF have heard this a little too much.

[518.69s] It's Goodhart's law with a profit motive, basically. The moment your measure, like, becomes a target and then the target is set by people who aren't true domain experts, it stops sort of measuring anything real.

[528.00s] And so the whole market, uh, I like to call it, sits in a sort of fog of war.

[532.91s] Labs, vendors, and enterprises, they're all kind of guessing which data actually improves the model. Nobody can see this clearly. There's a structural tell.

[540.83s] Contrived benchmarks, they only ever test a single isolated in-distribution question. They can't test whether a model sort of sustains, like, correct reasoning across a long dependent episode because these tests were all sort of meant to be solved in isolation.

[552.95s] Uh, in May, I spent a lot of time in this, um, increasingly, uh, in a lot of Anthropic blog posts, but also like a lot of other researchers have noted that cross-harness differencing and cross-infrastructure differencing is the primary cause for a lot of benchmark divergences in performance.

[568.58s] A lot of you are probably very familiar with like the frontier suites of the world and the deep suites of the world benchmarks. Um,

[576.77s] there are issues that all of these benchmarks have, uh, related to that specifically. In particular, just high false positive and false negative rates that are not immediately obvious when you look at the above head stats on the benchmark.

[592.21s] So a single benchmark number under a single scaffold is like basically one sample from a distribution whose basically width nobody me-measured. And that's why there's so much what I call benchmark psychosis today.

[603.33s] It's like a-- It's a pretty noisy sample. So, um, you know, really briefly on an example I took, I, I always have like-- I basically have an internal version of VALS AI and a lot of private benchmarks.

[614.75s] Um, so I, I took three finance tasks from three real-world vendors, um, like an ARR waterfall reconciliation, an LBO valuation memo, and a sort of like long-short pair trade for hedge fund, uh, trading.

[626.91s] So it's long-horizon, non-verifiable finance tasks, relatively robust like deterministic verifiers paired with LLM as a judge, uh, applied correctly. So, um, when you actually run these, I think [chuckles]

[641.41s] you'll, you'll notice very clearly Opus 4.8 is worse than 4.7 on a lot of these rubrics. Uh, you'll, you'll start noticing things if you actually do ru-rubric analysis at the 4.7 to 4.8 step over-engineered self-reflection.

[653.61s] Um, you'll, you'll notice that, uh, GPT 5.5 and Opus 4.8 score within three points on the same task. They fell in like exactly opposite directions, whereas GPT nails the arithmetic, um, but Opus nails the, uh, the methodology but loses arithmetic, which is to say, uh, it's, it's clear if you actually do very good agnostic benchmarking, um, you,

[674.99s] you can tell where the post-training directions for a lot of these teams went. And subsequently, it informs, I think, like a lot of the data that, that comes for this.

[684.07s] Um, so look-- you know, going back to the start, a single benchmark number is a sample from a distribution nobody measured, and it's basically like taking a Swiss Army knife and using the screwdriver bit to cut cheese and like concluding the knife is broken.

[696.11s] Um, [chuckles] so, um, you know, the, the receipts from the last slide, this, this goes into an RL environments report that is sent to labs. Um, but no single leaderboard number ever shows you this part of, um, you know, data which some of the most sophisticated RL environment companies, some of which are actually here at this conference, um,

[718.65s] would, would show you this. So, um, how do we read sort of which domain is next instead of chasing hype? And you can actually use this as a proxy data markets as an upstream indicator of what next application layer products the labs will come out with.

[735.49s] In, in January, uh, Anthropic was spending a lot on cybersecurity data from new vendors.

[741.95s] And in March and April, they were spending a lot on biological data, um, from, from associated vendors. And what do you know happened like two to three months after?

[750.81s] Well, Mythos and Cyber and Claude Bio/Life Sciences today. Uh, so if you want to use this checklist I use, classify the professions tasks into three axes, apply the long horizon bar, the, the ones real labs use, um, enforced step length, heterogeneous tool calls that aren't interchangeable, state transitions that genuinely constrain future actions, mandatory failure recovery.

[775.23s] Uh, you'll notice a pretty mixed bag, uh, of, of how long horizon is even defined from the vendor perspective in terms of specs. Um, and then three, you want to look at the raw data for five signals.

[785.71s] So sequential decisions against like one entity, an inferable action-- uh, expert action per step, outcomes recorded by independent parties. Um, but moreover, just economically available high wage work. So, uh, su-subsequently, one, one counterexample to keep you honest, like, uh, robotics, the modality is not settled, um, Ego versus Teleop versus UMI.

[806.59s] But moreover, I, I find just generally a huge degree of unsophistication within robotics data vendors today. A huge degree of unsophistication. Y- [chuckles] uh, I don't know. Some of you guys are probably robotics researchers in a crowd.

[818.85s] I don't know how many times like people have come up to you and they're like, "Oh, here's like a hundred thousand hours of like iPhone video from my friends in India.

[825.53s] Do you want to buy this for Ego data?" [laughs]

[828.41s] Um, so, uh, in, in, in that sort of domain, your vendor's, uh, choice is entangled with an unsolved research question. At the end of the day, you have to realize like RL environment companies, if they actually succeed, they're more so research accelerators.

[840.09s] It's a boutique industry. If it's venture scalable, it's because the infrastructure they're building agnostically in-house helps an enterprise application layer use case rather than assuming that data markets today will stay as they will forever.

[854.25s] So don't die on a modality hill, basically.

[858.27s] So, so one last exhibit just from my work. This is the map under everything I just described. Look, the share of the white-collar work is sort of on the vertical axis.

[865.31s] Task horizon is on the horizontal. Short horizon is a l- is very addressable right now. But you think about this long tail on the right side, this deep dependent long horizon work.

[873.41s] That's where the real economic value and data build out sort of both lives. And this threshold line that comes-- kind of moves rightward every time somebody builds a real world data pipeline.

[884.49s] Um, now I want to talk a bit more about the model layer. Um, it changes who needs to build what. So historical fact, no pioneer of an infrastructure technology has actually held more than ten percent of the market in the long run.

[897.53s] Um, I'm not saying th-this applies to Anthropic, but you know, just those who forget history are condemned to repeat it. Railroads built company towns. They charged tyrannical rents. They got nationalized as soon as the automobile moved in.

[909.96s] AWS and Google, they consolidated the infrastructure layer and still never captured the application layer. And right now, OpenAI and Anthropic are carving out these fiefdoms. But like all these pressures from anti-distillation export appeals, enterprise exclusivity, they're basically the equivalent of railroad rents in their erode, right?

[927.73s] Like the automobile in some cases has already arrived, like GLM five point two surpassing G-GPT on a lot of real world rubrics, um, is, is, is pretty hard proof that a lot of app layer companies can decouple themselves from the model layer.

[942.21s] And because models differ on efficiency and modality, they're not fungible like electricity. So it's not, it's not exactly leading to nationalization, but it's definitely not heading to durable lock-in either.

[952.92s] And the whole question on what to build next hinges on whether a general enterprise can decouple models from foundation model labs. Um, but luckily, you know, w-we, uh, for a lot of data companies, this is actually where they're headed.

[966.33s] I came here to give a talk on data markets. I'm here to tell you that the successful data companies nowadays are all pivoting to enterprise.

[976.71s] I maybe shouldn't say this in a public setting, but Mercor and Handshake, people don't notice an incredibly large amount of their revenues are enterprise now. Enterprise in ways you wouldn't expect a data business to do.

[989.53s] Once enterprises stop renting a lab's intelligence and starts owning their own, you need an entire abstraction layer that doesn't exist yet. There's like five jobs, serve and route small models targeted by cost latency and performance profiles.

[1001.65s] Um, and, uh, two, manage your RL data sets instead of like, um, a cross-base model migration. So when you swap to a new open source base, you rerun post-training automatically instead of starting over.

[1015.19s] Three, the Antikythera mechanisms that I talked about before. Um, and in, in the interest of time, happy to talk more about like emerging infrastructure needs afterwards if you want to.

[1024.31s] So let me bring it all together. I think data companies all realize that they have to be Neo labs. Data businesses do not stay data businesses because the durable value sort of accrues to the services and app layer of actual work.

[1035.39s] So two takeaways. You know, if you're a researcher, stop outsourcing your definition of realism to the same vendors you buy your evals and tasks from. Um, that's kind of just letting the task-- test writer grade the task.

[1045.16s] And if you're a builder, your moat's not the data, it's the sort of pipeline into real world work, plus the infra to keep retraining on it as the models improve underneath you.

[1054.79s] I'll close on this. Uh, I'm building, um-- I'm working on something new. [chuckles] This is the first public announcement of it. I'm building Antikythera mechanisms. I'm working with a lot of real world companies to monetize their data assets, but moreover, help implement RL as a service with a lot of the enterprises in the world, mitigating a lot of

[1072.29s] the pitfalls of a lot of companies I mentioned. If you guys want to talk about it afterwards, I'm on Twitter. I always write a lot on Twitter and Substack, and, um, I'm around afterwards too.

[1083.41s] Thank you. [audience applauding] [upbeat music]
