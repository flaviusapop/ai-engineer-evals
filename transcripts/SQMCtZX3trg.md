# The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)

Source: https://www.youtube.com/watch?v=SQMCtZX3trg

Uploaded: 2026-09-21

Transcript source: complete timestamped publisher transcript at https://ai.engineer/talks/SQMCtZX3trg-youtube-adf82bdf7bbc681384e6 . Includes slide text interleaved by publisher. Replaces capped native extraction.

## Transcript

001. [0:12](https://www.youtube.com/watch?v=SQMCtZX3trg&t=12s)
     Hello, everybody.

002. [0:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=15s)
     Hello.

003. [0:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=15s)
     How's it going?

004. [0:19](https://www.youtube.com/watch?v=SQMCtZX3trg&t=19s)
     Okay, I think we still have some people checking in, but, uh, I'm super excited to be here.

005. [0:28](https://www.youtube.com/watch?v=SQMCtZX3trg&t=28s)
     Okay, first off, let me reload these slides because my Claude Code was still building something on it

006. [0:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=39s)
     . Um, okay. So the contrast is a little bit low, um, so please bear with me. I'm gonna try to cover, uh, what you cannot read as much as possible. Uh, I also have heard that the Wi-Fi is not the strongest. So, um, while it is a workshop, uh, hopefully you just do, uh, take away a lot of the lessons, um, and then can apply it whenever you want to. Um, but I do have a sample repo if you want to follow along. Um, okay, first of all, hi. My name is Paul. Um,

007. ![A black and gold illustrated book cover introduces the talk.](https://assets.ai.engineer/sites/aiecode2025/sha256/d9364acffa023d0bdba1be67452121d7a8daef61c8fd9f4fc0db424e3c1caa7c.webp)


     The Dark Arts of Skill Engineering



     Paul Bakaus introduces lessons from building Impeccable, which began with a skill for bringing agent-generated designs back to a design system.

     Text in image

     ```
     IMPECCABLE

     THE DARK ARTS
     OF SKILL ENGINEERING

     PAUL BAKAUS · CREATOR OF IMPECCABLE

     01 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Enginee…
     localhost:8910/index.html?v=40#1
     Ask Gemini
     Work
     ```





     [1:06](https://www.youtube.com/watch?v=SQMCtZX3trg&t=66s)

008. [1:09](https://www.youtube.com/watch?v=SQMCtZX3trg&t=69s)
     I'm really glad you found your way into this room. Um, I'm the author of Impeccable. Who here has used Impeccable by any chance? Can I see some hands? Okay, a few people. Nice. Um, so for those of you who have not used Impeccable, Impeccable is a skill that I've built for myself mainly. Um, I've built this large enterprise app, uh, over the last year, and it has, like, lots of different views, states, whatever. Um, and I wanted to design really

009. [1:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=99s)
     quickly with my agents, with Codex, with Claude. But I noticed that, uh, even though it gets me quickly to something that I can look at, uh, normalizing it back to the design system was really, really challenging. So the first skill that I've built for myself was called Normalize, and it kinda, like, brought it-- brought whatever Claude designed back to the design system. That's how I started. And I also used, uh, Anthropic's front-end design skill, like maybe many of you, um, when I first got going. And from there on, it kinda expanded into

010. [2:09](https://www.youtube.com/watch?v=SQMCtZX3trg&t=129s)
     more and more design skills that allowed me to turn Claude Code and then Codex and other harnesses more into a design harness. Um, at some point, I decided maybe other people might find, uh, um, might find this useful as well, so I open sourced it as open source skill, uh, uh, released it, and, uh, it turns out, uh, a lot of you liked it. Um, so if you haven't checked it out yet, um, uh, yeah, give it a go. Uh, it's on, uh, impeccable.style. Um, but today won't be a talk about

011. [2:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=159s)
     Impeccable per se. It'll be about what I learned from making these skills because it kinda escalated. It started with, like, a simple prompt and then, uh, went all the way to what it is today. Um, a lot of people have looked at the code of Impeccable, and they see, like, a whole bunch of scripts in the script folder, and they're like, "What is all this stuff?" And so, um, I wanted to share some of my knowledge that I've gained with you. So let's get into it. Uh, let's talk about the dark arts of skill engineering.

012. [3:16](https://www.youtube.com/watch?v=SQMCtZX3trg&t=196s)
     Okay. Um, yeah, the production value of this talk is out of this roof. Um, okay. So first of all, you've all seen this kind of design. Um, this is actually a real design, uh, built with, uh, the front-end design skill, uh, and Claude Code. Um, and you probably all have seen a design like this. This is for, like, a fake kids reader-- iPad reader app. Um, you have italic serif, uh, you have, like, some capitalized, uh,

013. [3:46](https://www.youtube.com/watch?v=SQMCtZX3trg&t=226s)
     hero, um, and you have, like, a eyebrow text, like a kicker, whatever you wanna call it, at the top of it, like a weird label. Um, you have beige. I call it Claude Beige. Claude Beige, uh, backgrounds. Um, and now it's not necessarily a bad design, right? But I think you all can point this out and say, like, "Well, this is clearly AI-generated. It's clearly slop." Um, and it turns out slop is a moving target. Um, you've all seen-- You might have thinking-- might have been thinking of slop

014. [4:16](https://www.youtube.com/watch?v=SQMCtZX3trg&t=256s)
     as purple gradients, but, uh, we've kinda moved on since that, uh, into Claude Beige. Um, okay, so this is where I started. I started with a system prompt and a prayer, basically. Um, so I, I started using the front-end design skill, uh, like many of you, and it's, like, fifty-five lines of named bans. Uh, no scripts, no routing, pure prose, right? Uh, and you just hope for the best. Um, that sometimes worked and someti-- and most of the time it didn't.

015. ![The slide describes the original frontend-design skill as roughly 55 lines of prose without scripts or routing.](https://assets.ai.engineer/sites/aiecode2025/sha256/c80c78a4f4f720e802e57708edf844b02fb1266547a924cdcf50a643738c532e.webp)


     A System Prompt and a Prayer



     Impeccable began with Anthropic’s frontend-design skill: about **55 lines of named bans**, with no scripts or routing. Bakaus says it worked sometimes, but failed most of the time.

     Text in image

     ```
     A SYSTEM PROMPT
     AND A PRAYER.

     IMPECCABLE

     Level 0 · the spell

     Impeccable started as Anthropic’s frontend-design skill: ~55 lines of named bans. No scripts, no routing. Pure prose.

     03 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine[illegible]
     localhost:8910/index.html?v=40#3
     Ask Gemini
     Work
     ```





     [4:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=260s)

016. ![Examples from the original frontend-design skill accompany a critique of broadly applied bans.](https://assets.ai.engineer/sites/aiecode2025/sha256/dd285430df25794eb323eba46d9897d607dd35ba36a43b3ea0d9871bf24d52d7.webp)


     Frontend Design: The Original



     Bakaus argues that **blanket bans** over-apply: forbidding Inter can push the model to the **next most likely font** without making it more creative.

     Text in image

     ```
     IMPECCABLE

     Level 0 · frontend-design · the original

     # frontend-design / SKILL.md · the original, ~55 lines
     "NEVER use generic AI aesthetics: overused
      fonts (Inter, Roboto, Arial, system fonts)"
     "...Cliched color schemes (particularly
      purple gradients on white backgrounds)"
     "Never converge on common choices
      (Space Grotesk, for example)"

     › github.com/anthropics/skills · frontend-design (the original)

     Named bans, applied to every project. Two deep flaws: it over-applies, and a ban just relocates the model to the next cluster. Fixing them is the whole build.

     04 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     localhost:8910/index.html?v=40#4
     Ask Gemini
     Work
     ```





     [4:42](https://www.youtube.com/watch?v=SQMCtZX3trg&t=282s)

017. [4:46](https://www.youtube.com/watch?v=SQMCtZX3trg&t=286s)
     So, um, for example, uh, I'm just gonna read some of this, so, um, if-- I mean, maybe it's already readable. I don't know. Um, but for example, in the front-end design skill, you have sentences like, "Never use generic AI aesthetics, overused fonts like Inter, Roboto, Arial system fonts, um, or clichéd color schemes, particularly purple gradients and white backgrounds. Uh, never converge on common choices like Space Grotesk, for example." Um, now, there are two problems with this approach. The first one,

018. ![Examples from the original frontend-design skill accompany a critique of broadly applied bans.](https://assets.ai.engineer/sites/aiecode2025/sha256/dd285430df25794eb323eba46d9897d607dd35ba36a43b3ea0d9871bf24d52d7.webp)


     Frontend Design: The Original



     Bakaus argues that **blanket bans** over-apply: forbidding Inter can push the model to the **next most likely font** without making it more creative.

     Text in image

     ```
     IMPECCABLE

     Level 0 · frontend-design · the original

     # frontend-design / SKILL.md · the original, ~55 lines
     "NEVER use generic AI aesthetics: overused
      fonts (Inter, Roboto, Arial, system fonts)"
     "...Cliched color schemes (particularly
      purple gradients on white backgrounds)"
     "Never converge on common choices
      (Space Grotesk, for example)"

     › github.com/anthropics/skills · frontend-design (the original)

     Named bans, applied to every project. Two deep flaws: it over-applies, and a ban just relocates the model to the next cluster. Fixing them is the whole build.

     04 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     localhost:8910/index.html?v=40#4
     Ask Gemini
     Work
     ```





     [5:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=307s)

019. [5:16](https://www.youtube.com/watch?v=SQMCtZX3trg&t=316s)
     it over-applies, and then a ban just relocates the model to the next cluster, and I'll show you why this is a problem a little bit further down the road. But really, you tell it not to use Inter. It just uses the next best font it finds in its latent space. And so it doesn't actually make it more creative. It just-- Again, this is why I said slop is a moving target. It kinda picks the next best thing. Um, I have, uh, learned my lesson here, um, the hard way because, uh, I don't know if you noticed, but the reason why we got

020. [5:46](https://www.youtube.com/watch?v=SQMCtZX3trg&t=346s)
     purple gradients in the first place is because of Tailwind. Tailwind's default sample pages theme, whatever, was purple. Um, well, it turns out I've turned the web orange before. Many years before that, I created a framework called jQuery UI, and the first default theme of jQuery UI was orange. So overnight, I colored the web orange. I thought people would modify the theme, but no, they didn't. Um, so I learned my lesson. Um, okay, the median is the model's gravity.

021. ![Examples from the original frontend-design skill accompany a critique of broadly applied bans.](https://assets.ai.engineer/sites/aiecode2025/sha256/dd285430df25794eb323eba46d9897d607dd35ba36a43b3ea0d9871bf24d52d7.webp)


     Frontend Design: The Original



     Bakaus argues that **blanket bans** over-apply: forbidding Inter can push the model to the **next most likely font** without making it more creative.

     Text in image

     ```
     IMPECCABLE

     Level 0 · frontend-design · the original

     # frontend-design / SKILL.md · the original, ~55 lines
     "NEVER use generic AI aesthetics: overused
      fonts (Inter, Roboto, Arial, system fonts)"
     "...Cliched color schemes (particularly
      purple gradients on white backgrounds)"
     "Never converge on common choices
      (Space Grotesk, for example)"

     › github.com/anthropics/skills · frontend-design (the original)

     Named bans, applied to every project. Two deep flaws: it over-applies, and a ban just relocates the model to the next cluster. Fixing them is the whole build.

     04 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     localhost:8910/index.html?v=40#4
     Ask Gemini
     Work
     ```





     [6:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=367s)

022. ![A dark gravity well illustrates the claim that a great prompt alone is not enough.](https://assets.ai.engineer/sites/aiecode2025/sha256/35936f9236748f8a52bef7fa3d0a00e4fb24a9fd85b9250d8321cef03948874e.webp)


     The Median Is the Model’s Gravity



     A gravity well depicts the model’s pull toward the median. Bakaus argues that even **250 lines** of carefully crafted skill prose cannot overcome it; a great prompt alone is insufficient.

     Text in image

     ```
     The median is the model’s gravity.

     Even 250 lines of real taste can’t out-write it. A great prompt is necessary, and nowhere near enough.

     05 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     localhost:8910/index.html?v=40#5
     Ask Gemini
     Work
     ```





     [6:11](https://www.youtube.com/watch?v=SQMCtZX3trg&t=371s)

023. [6:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=375s)
     Even two hundred and fifty lines of like artisanal crafted beautiful skill prose cannot change this. It's just not enough. It doesn't help enough, right? It's nowhere near enough. Um, and I learned this the hard way, and hopefully you don't have to. Um, my overall thesis for this talk is that prompting is sort of like the starter level, but harness engineering is where you should end up. Like you should reframe when you're building skills, you should think about,

024. ![The slide states “prompting < harness engineering” and contrasts a spell with magic.](https://assets.ai.engineer/sites/aiecode2025/sha256/77675076905376d264392a4a0ce52db905e9374fa0fa4cd91f77da0bd6621155.webp)


     Prompting and Harness Engineering



     Bakaus argues that skill builders should treat skills as **extensions of the coding harness**, with capabilities beyond a packaged prompt.

     Text in image

     ```
     IF YOU REMEMBER ONE THING

     prompting < harness engineering

     Prompting is the spell. Harnessing is the magic.

     IMPECCABLE
     06 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     Ask Gemini
     localhost:8910/index.html?v=40#6
     Work
     ```





     [6:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=389s)

025. [6:45](https://www.youtube.com/watch?v=SQMCtZX3trg&t=405s)
     okay, skills, the same way as MCP, is an extension to the coding harness or whatever harness you're in. Uh, it's not just a prompt that you package. It's something more than that, or you should at least conceptually think about it more than that. It is extending the harness of whoever is using that thing. Uh, and it also has more capabilities as just prompting. Uh, and when I thought about it that way, it sort of like clicked for me. Um, prompting is a spell, harnessing is a magic. And we'll talk about nine different dark

026. ![The slide states “prompting < harness engineering” and contrasts a spell with magic.](https://assets.ai.engineer/sites/aiecode2025/sha256/77675076905376d264392a4a0ce52db905e9374fa0fa4cd91f77da0bd6621155.webp)


     Prompting and Harness Engineering



     Bakaus argues that skill builders should treat skills as **extensions of the coding harness**, with capabilities beyond a packaged prompt.

     Text in image

     ```
     IF YOU REMEMBER ONE THING

     prompting < harness engineering

     Prompting is the spell. Harnessing is the magic.

     IMPECCABLE
     06 / 53

     Interface text:
     Claude
     The Dark Arts of Skill Engine…
     Ask Gemini
     localhost:8910/index.html?v=40#6
     Work
     ```





     [7:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=427s)

027. [7:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=435s)
     arts today that I learned, uh, in the process of building Impeccable. Um, we'll make, uh, sub-agents argue with each other. Uh, we'll talk about how to force divergence as opposed to convergence, route in like a model, um, and basic-- You, you've seen this probably. Um, most modern models are a mixture of expert architectures, and Impeccable is built like a mixture of expert skill. Um, we give, we give them memory.

028. [7:45](https://www.youtube.com/watch?v=SQMCtZX3trg&t=465s)
     We'll create scripts that talk back, and I, I promise this will make sense. Uh, hooks that fight back, live wire the browser, and use more of the harness, compile to every harness, and design for the weakest model. Let's get into it. Number one, made it-- make it argue. So if you're building something like a critique skill or code review skill, um, here's one huge issue. Uh, if you are-- I mean, you probably noticed this when you're working with Claude Code or Codex, that doesn't matter. But if you

029. [8:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=495s)
     ask Codex or Claude Code to review its own work, it will usually rate it as very high. It's like, I mean, like, "I've built this, so I've done a great job," right? Like, it's like grading your own homework. Doesn't make any sense, right? Um, it anchors on what it already created. Um, now that's not great. Um, what can you do in order to solve this? Well, you can make a model argue with another model, right? Adversarial prompting is also called.

030. [8:45](https://www.youtube.com/watch?v=SQMCtZX3trg&t=525s)
     So you have two sub-agents, and they never see each other's work.

031. [8:51](https://www.youtube.com/watch?v=SQMCtZX3trg&t=531s)
     And here's why this matters. So in Impeccable, there's a critique command that actually critiques your design. And you can point it to your landing page, you can point it to anything. And there are two particular failure scenarios. The first one, and this is almost impossible to read, so I'll explain it. The first one is, um, a strong page, right? So it's a really good-looking page, but there's a whole bunch of maybe like, uh, deterministic errors. And Impeccable actually has a deterministic

032. [9:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=560s)
     engine, uh, like a design linter that can detect things like bad contrast. It can de-detect things like, you know, too many fonts. Um, you know, maybe things that are too close to the edge of an element. So it detects some of, I would say, polish issues. Um, but you could have this really beautiful website, and then the detector runs, and it's doing that as part of the same skill and the same model thread. And then the model, uh, just sees the detector

033. [9:50](https://www.youtube.com/watch?v=SQMCtZX3trg&t=590s)
     output and says, like, "Well, I guess there's five hundred issues, therefore, this design must be bad." Now, that's one. The other one is the opposite. The other one is it's actually a really terrible page or maybe like an empty page, but there are no detected issues by the, by the deterministic detector. So the model is like, "Hmm, we didn't find any issues, so this must be great design." So both of those are not amazing. Uh, what you want is, and this is what, uh, Impeccable's critique skill does, it, uh, it kind of combines two

034. [10:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=620s)
     things. It spawns two sub-agents, uh, and they are blind to each other. Um, and that's how you get to a balanced critique. So the first sub-agent, um, does, um, um, act like a design director. So it's an LLM, um, that acts like a design director. And so, um, it looks for hierarchy, it looks for slop, it looks for heuristics. And so it does a critique the way a human would with the browser tools that are u- that are available to it. The second sub-agent runs deterministic,

035. [10:50](https://www.youtube.com/watch?v=SQMCtZX3trg&t=650s)
     deterministic detector and also collects browser evidence. And then once both of those results come in, the main thread synthesizes both into one ch- into one critique, and that produces a much more balanced result. And before I go on, um, I realized I actually have not, uh, have not shown you where the sample repo of this lives. So let me bring this up real quick. Um, if you want to clone this and you have a decent enough

036. [11:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=680s)
     internet connection, go ahead if you like. Um, so this is, um, uh, pbakaus/impeccable-talks. Um, the talk lives here, but also in the dark arts folder, there is a starter folder, uh, and a demos folder. Demos, uh, has a pretty average median page that you can manipulate. Um, and then, uh, in the starter kit, you

037. [11:50](https://www.youtube.com/watch?v=SQMCtZX3trg&t=710s)
     have enough to build sort of a, a mini Impeccable if you want to, if you want to follow along or, or try it out yourself. And so as part of this, um, this tutorial here too, uh, you'll, you'll follow along sort of the checkpoints, the dark arts, and build something yourself. I would suggest, you know, if you like to multitask, great. Um, you can apply this, by the way, to anything. You can do like a code review thing. You can do, um... it doesn't have to be design skill. Um, but I wanted to have something for you to play.

038. [12:21](https://www.youtube.com/watch?v=SQMCtZX3trg&t=741s)
     Uh, back to the deck.

039. [12:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=744s)
     So two blind opinions beat one confident guess. Um, you can use this again, I already said code review, design review, but also a security audit one is a good example. Uh, or a plan, creating a, a really good plan, uh, of say critique, where you have multiple LLM judges argue with each other before it gets good. Or ranking outputs is a good, a good example. Now, here's the problem though. Codex, why? Why you don't let me do this?

040. [12:54](https://www.youtube.com/watch?v=SQMCtZX3trg&t=774s)
     It's bad. Uh, it turns out that Codex never created these sub-agents when I first tried this. Um, and I banged my head against the wall, and I'm like, "Why is this?" It turns out Codex has a different permission model than Claude Code and other harnesses. In Codex, you have to explicitly, as a user, request the use of sub-agents for anything in the harness to use sub-agents. So if you're distributing a skill, you're out of luck. The only way to

041. [13:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=804s)
     make this work, as far as I know today, is to actually tell the model, "Okay, if you have sub-agents capabilities, but you do not have permission, please stop right here and ask the user." And so that's pretty much the only way you can get Codex to comply. So in Impeccable, um, if you see something that, you know, makes you go, "Huh," um, it's probably because of that. Like, you know, through, um, lots and lots of issues that people filed and, um, a lot of testing on, on

042. [13:54](https://www.youtube.com/watch?v=SQMCtZX3trg&t=834s)
     my end also, um, a lot of this obscure knowledge got into the skills so that it works truly across harnesses. Um, for instance, here you see kind of pseudocode of how this would work. And then also, I, uh... this is another really important thing. Um, very often, if Codex realizes it can get away with something, it will do it. So, um, if there is no punishment for not spawning sub-agents, it will simply not spawn them. It's like, "Well, this

043. [14:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=864s)
     is the easier route. I will take this easier route." So what you have to say is, "Actually, if you cannot use sub-agents, you must say that you are giving the user a degraded experience." And Codex hates that.

044. [14:40](https://www.youtube.com/watch?v=SQMCtZX3trg&t=880s)
     So use that to your advantage. Um, so, um, you can watch them argue. Um, now I did not pre-record an actual example here because I- I'm like, "Let's do it live." Um, so we're going to go into Cursor and, um, I'm gonna do like a critique and let's hopefully it'll work. I don't know

045. [15:10](https://www.youtube.com/watch?v=SQMCtZX3trg&t=910s)
     if Composer spawns sub-agents, uh, well enough, but let's see.

046. [15:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=922s)
     Uh, Composer, by the way, if you haven't used it, is a really fast, well-balanced model. So it's kinda, uh, kinda neat for, um, for work that you wanna show on stage in particular. Um, okay, so now it's doing something here. Um,

047. [15:42](https://www.youtube.com/watch?v=SQMCtZX3trg&t=942s)
     okay, this, this repository I think has an old version of Impeccable that just doesn't spawn agents. Let's see, this is the unfortunate... Well, maybe it does.

048. [15:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=959s)
     Uh, I'm not sure if it did or not, but I at least wanna show you what the type of critique looks like. Um.

049. [16:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=980s)
     Uh, all right, now it's asking me a bunch of questions of what I actually want to create. I'm gonna skip this. Uh, and now I get a design critique, um, on what's working, what the priorities issues are, uh, persona red flags. Now, the actual thing that I wanted to show you unfortunately couldn't be seen in this particular set, but we can come back to it. Um, if you run this in, in Claude Code or Codex on the most recent version, you should very clearly see, I mean, in Claude Code it's very easy to see

050. [16:50](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1010s)
     the sub-agents running and doing its work. So it will spin up two sub-agents, and you see it at the bottom of the Claude Code thread, uh, doing its thing.

051. [16:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1019s)
     Okay, level number two. Uh, a ban just moves the problem. We talked about this already. Um, you ban enter the model graphs, graph Space Grotesk. Uh, how do you solve that? How do you force divergence? Well, a ban only moves the model around inside its own cluster. And what I've built for Impeccable and for a bunch of other skills that I've released is what I call an anti-attractor. Uh, and the anti-attractor works by creating a random seed of sorts, and that can come from user

052. [17:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1049s)
     input, or it can come from a script that it can run that produces something that is completely unexpected to the model because that's what you want. And so in this case, for instance, it would be font selection. And instead of selecting this safe next step prediction font, it went c- into a completely different space through a different seed. Uh, there are three techniques that, you know, are easy to hard and work differently. The first one,

053. [17:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1079s)
     um, is, is something you can do right, right now. It's the most simple one, and it's to shave the safe picks. So basically tell the model, "Okay, name your top three fonts." And then the model is like, "Hmm, okay, I got the top three fonts." And then you're like, "Now throw them away." And like, "But why?" Um, but then you basically shave, shaved off the, uh, the next token, uh, that is predicted. Um, and you do that three times, and then now you get to a different space of the, uh,

054. [18:30](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1110s)
     like a further away in the latent space, right? Um, now that's doable, but now at some point you still get convergence. So this is just, you know, a limited technique. The second technique is to generate a lot of different things and then have a sub-agent rank. I've done this for a shader library that I've created called Radiant Shaders, and, um, the goal here was to create around 100 different shaders, and the problem is every time I, I would say, you know, create a new shader or create ideas for 10 new

055. [19:00](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1140s)
     shaders, I would get the same repeating ideas. Uh, I solved this with two-- in two different ways. The first one is I created something unexpected, a random seed, a creative seed. In this case, I used celebrities. I said like, "Well, what would Rihanna look like as a shader?" Um, or "What would Beyoncé look like as a shader?" And, um, and then the model was like, "Hmm, let me think about that." So that's the first thing. And then I said, "Well, generate 100 of these ideas, and then spawn a sub-agent

056. [19:30](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1170s)
     that ranks all of those ideas." Uh, and that's important. It has to be a sub-agent because the sub-agent doesn't know anything, uh, from the prior context of the session, um, and, uh, and can then completely change the order. The third one is to create a random seed from a script. So in Impeccable, for example, when you first start a project, it calls a script called color.js. And color.js has, um, over 100 hand-selected, uh, they're

057. [19:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1199s)
     not complete color palettes, but they are primary colors and they're kind of like a starting point of a palette. And it reads that, and then the model uses that as a creative spark to build a palette around it for you. You can still say, "You, I don't like this." I mean, I don't like what it proposed. But it, it turns it into a different direction. So those are all ways to create divergence. And when you design something with Impeccable, the same brief, depending

058. [20:30](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1230s)
     on the user's input and, you know, color script that runs, et cetera, can produce vastly different results because of that, because I didn't wanna have the whole internet look like, uh, everything else. Number three, um, here's the problem. If you cram everyth-everything into one skill, it kind of blurs them. The instruction following becomes not very good enough anymore. So if you're building some general purpose skill and you expand it and expand it and expand it, at some point, uh, it

059. [20:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1259s)
     becomes really, really blurry to the model. Um, here's a concrete example of this. The Anthropic front-end design skill, uh, the former version of it, they just shipped a new version three weeks ago. But the former version had a line that I read earlier that says, "Avoid system fonts." That's okay for landing page design. But for product UI, oftentimes you want it to feel as native as possible, so system fonts are actually the thing that you want. So how do you solve this? Um, you

060. [21:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1289s)
     can say, I mean, you can have this giant if/else block in a skill. Say like, "Well, if the user wants a landing page, do this. If the user wants a product, do this." But that becomes really convoluted, wastes a lot of tokens, and, uh, honestly doesn't work very well. So Impeccable started as a lot of different sub-skills and now has this, um, mixture of experts model that routes internally. Um, both in terms of, uh, capabilities, so you can call Impeccable critique or Impeccable polish,

061. [21:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1319s)
     and you get a different MD file loaded behind the scenes for that particular job, so it's not just one giant skill MD. Um, but also, and this is something not a lot of people know, behind the scenes, Impeccable decides based on your brief and what you input, whether you're trying to design something brand-y, so like a landing page or something that wants to attract attention, or whether it's the actual product that you're designing. So it switches registers and then loads

062. [22:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1349s)
     completely different rules for those two registers because product design and brand design are very, very different. Um, so that's also something that I would recommend you doing if you're building a larger skill. This works for bi-big multi-tool skills, works for context on-demand type of skills, uh, per audience behavior, agent toolkits, that kind of thing. Number four, everyone starts from zero. Skills by default don't have long-term memory. Uh, they don't really compound

063. [22:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1379s)
     over time, but you can make it so. So, um, you have a skill folder, and you can save things in that skill folder. In fact, in Claude, you even have an environment variable that, uh, resolves to the actual directory, uh, that you can save things in, which is nice. Uh, no other harness supports this right now, I believe. Um, but you can, you can hack around that. Impeccable uses a .impeccable folder in the current repository root. Um, but you can also save things directly in the skill folder, um, and

064. [23:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1409s)
     maybe ask the user to g-ignore them. Uh, how could this work? So for example, if you're running a critique in Impeccable, that critique is saved as a file in that folder. Uh, and by default, it's gitignored. But then, if you then later on say, "Well, okay, I just ran a critique. I'd like to polish my page," even if you do it in another session, it actually uses that prior critique as a signal to understand what have we found out about this page. And it can look at all prior

065. [23:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1439s)
     critiques and see sort of the progression of the page. Uh, for example, you could have said in one of the critiques, "You know what? I don't agree with this critique. I don't think you're right, and I think I really like my instruments as fonts." Um, and then the model would be like, "Okay, no problem. I'm gonna mark this for later." And the skill is now smart enough. The skill has, uh, built context to realize, okay, well that's the user preference, so I'm gonna respect it going forward. Um, so compound engineering, um,

066. [24:30](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1470s)
     really, uh, is an interesting theme for skills as well. You can make skills aware of prior sessions with that technique. Um, so make the runs compound. This works really well for resumable gradients, uh, resumable agents, progress tracking, uh, multi-session refactors, migrations, that kind of thing. Um, uh, for instance, one of the things that I do all the time is refactor my code and, um, how do I do that? By having a sort of like a skill that spawns

067. [24:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1499s)
     itself across multiple sessions and tackles one file at a time. So I basically tell it, "Okay, here's your TSX file or whatever, um, for today's session, um, and now refactor everything around this file and linking into that file," and, and then it sort of builds up context over time until it's completely finished with the whole code base.

068. [25:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1522s)
     Okay, number five, uh, buried rules get skimmed. Um, we talked a bit about this before, but this is a little bit of a different point I'm trying to make. Um, now especially with weaker models, and now if you're building a skill for yourself and you're only running Opus or you're only running Codex, um, this isn't that, that big of an issue, right? You, you know which model you run, uh, you know if it works with GPT 5.5, for example, uh, I'm good because that's the

069. [25:52](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1552s)
     only w- model I use. Now, if you want to distribute your skill to lots of users, uh, this is where things get kind of hairy, uh, because some of those users might be running Sonnet, some of them might be running Haiku, some of them might be running Grok. I don't know. Um, uh, some of them might be running Gemini. You know, you never know. Uh, sometimes I meet somebody who does. Um- But,

070. [26:18](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1578s)
     um, uh, really that's where it gets complicated, right? Um, because you need to build for the lum- lowest common denominator and ideally for the, for the one model that is the weakest as at instruction following. For example, GPT Five Mini is not a very good rule follower. Uh, there are things even in Impeccable that don't work with GPT Five Mini. Um, it consistently doesn't load certain MD files that I thought it. Uh, it consistently doesn't spin up the live mode. So

071. [26:48](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1608s)
     there are, uh, boundaries to instruction following across these models, and it gets especially bad with longer skills that have lots of rules. So how do you work around this? Well, in Impeccable, Impeccable really is kind of bionic of sorts. It's really not just prose. It is a combination of scripts that run inline within the skill at certain times, uh, and then prose around it. For example, every time you call Impeccable, it runs a file called

072. [27:17](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1637s)
     context.mjs, and the context.mjs does a couple of things. The first thing is, uh, if there's a product MD, which is Impeccable's, uh, it's almost like design MD, but it is for product strategy. So for instance, to understand who's the target audience or what do you want to achieve with this thing, which is oftentimes more important in a, in a design interview than, you know, how, how round do you want your borders to be? Um, but it supports both. It supports product MD and design

073. [27:47](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1667s)
     MD. And by default, context.mjs brings these files together and then spits them into the session. Now, that's not exciting, but when those files are not available, it will actually give the, uh, the skill structured JSON and say like, "By the way, there is no product MD, and here's exactly what you should do about it." Or here's another thing that context.mjs does. It actually makes Impeccable self-update if there's a new version of Impeccable. Now, with your permission, so we

074. [28:18](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1698s)
     will a- it will ask you, but it will say, "Hey, by the way, there's an update available for the Impeccable skill, uh, and here's what you should do now to ask the user whether, whether they want to update Impeccable." So it's, it's overloaded in many ways, um, and it will always tell the model the exact instructions on what to do next. And the really interesting thing about this is that I found that that works significantly better than some random rule in the prose of the main skill. When you put something out,

075. [28:48](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1728s)
     uh, from the exit value, uh, from the standard out of a script, uh, somehow the model will follow it a lot, uh, more than before. Uh, so that could be environment, uh, aware setup, dynamic onboarding, repo state gating, adaptive flows, anything really. Um, actually before I end this session, one of the shortcomings of this technique, and this is something to be aware of, is prompt caching. So this works super, super well

076. [29:18](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1758s)
     to keep a skill, uh, sort of like, uh, you know, flowing in the right direction, instruction following, but it does so at the expense of prompt caching. Um, if you need prompt caching, if you run a skill many, many times, uh, and you want the whole thing to be cached, this is not a good technique to use. But I found it to be very useful in really interactive scenarios.

077. [29:41](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1781s)
     All right. Number six, hooks that fight back. It's something I shipped quite recently and, um, and I really like it. I wanna show you what I mean by that. Um, so a lot of people have Impeccable systems, but sometimes they forget to run it. Sometimes they're like, you know, I don't know. I mean, the, the-- I mean, I wish-- Codex is actually pretty good. Some of the harnesses are pretty good at consistently looping in the right skill. Um, but because

078. [30:11](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1811s)
     it now bundles as one skill, uh, oftentimes, uh, the harnesses forget to simply call Impeccable when you don't explicitly mention it. So now you're building some front-end code and maybe it doesn't follow your design system or whatever. Um- Now that can be solved with hooks. Uh, who here, who here has used hooks before in Claude Code or Codex? A few people. Okay, nice. Um, so this skill that I've built here, Impeccable,

079. [30:42](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1842s)
     ships design hooks. So I've basically built a design linter that runs under the hood and ships with the skill. When you install Impeccable, uh, these hooks install into Claude Code, Cursor, um, Codex, and GitHub Copilot, uh, and they will keep the model, uh, exactly where it needs to be. So the hooks come to you. It's a guardrail that fires on every edit. Um, and, um,

080. [31:12](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1872s)
     there are some, there are some differences between the different providers here. So the hook syntax for Codex and Claude Code is not the same. Um, and also the behavior is not the same. So for instance, we found out that with weaker models, slightly weaker models like Composer and Cursor, uh, you kind of want to use a, um, pre-tool use hook that prevents writing of code as opposed to a post-tool use hook. Post-tool use basically happens right after the agent has written a file, for example, and then

081. [31:42](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1902s)
     it, it tells you, "Hey, by the way, like, the contrast of these colors is bad," or, um, you know, "You have a purple gradient in here." And then ideally, the model is smart enough to actually fix it. Um, some models don't follow those instructions very well. And so if you do a pre-tool w- use hook, you are actively preventing the writing of this file in the first place. So it's a much more heavy-handed approach. Uh, but we needed to do that for certain models and certain harnesses. Um, but this is nice.

082. [32:13](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1933s)
     And what's even nicer about it is that you can personalize it to your design system and your use case, uh, or whether, let's say, you use it for code reviews. You can personalize it with your own ESLint rules, uh, with your own, uh, synthetic syn- syntax guidelines, et cetera, uh, and then expand it from there. Um, so passive guardrails beat a command no one remembers to run. Um, so these are passive guardrails that always keep you in the right lane, uh, on track.

083. [32:43](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1963s)
     Uh, again, that works for linting, for formatting. Um, of course, if you're using Claude Code or Codex, it already uses, uh, some of the linters for things like, uh, syntax formatting. But design linting is a whole different, uh, game. But I would really encourage you to, uh, try out hooks in combination with a skill and think about, okay, well, my skill does this. How can I create a feedback loop, a validation loop that uses hooks, uh, to actually keep me on the right lane?

084. [33:14](https://www.youtube.com/watch?v=SQMCtZX3trg&t=1994s)
     Um, okay. So here's-- It's hard to show loop-- uh, uh, hooks in action, but, um, you know, if you can see this, this is roughly how it would happen in an agent. Um, so, uh, for instance, in this case, I would use, let's say, Gemini does this all the time. Gemini, uh, creates animations on images like crazy. Um, it will animate any image, and it will usually do a hover zoom-in effect. Um, it loves that. Um, and that's

085. [33:44](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2024s)
     something that Impeccable flags. And in this case, it-- the hook would fire silently usually. That's why I built this fake demo, because you can't usually see it. Um, and then it will tell the model, "Hey, by the way, here was a violation." The experience of this is that oftentimes you don't have to do anything. The model just c- course corrects and fixes itself. Um, now one important thing, if you do this and you ship it to users, very important to add a way to create ignore rules or something like that,

086. [34:14](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2054s)
     because oftentimes these hooks have false positives as well, and you want a way to configure those hooks. Um, otherwise, it gets really annoying very quickly. Um, Impeccable ships with these design hooks that, uh, allow you to create ignore rules at a file basis within a CSS rule, so like, uh, many granular levels, uh, to exclude certain files, for example.

087. [34:38](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2078s)
     Okay, level seven. Now, you can't really tune pixels to a chat box. Uh, now this might not be relevant if you're not building a design skill, but I think the general point is relevant. So if you think about a skill as harness engineering versus prompting, then you think about the harness as a whole, right? You're living in Claude Code, for example, or you're living in Codex, uh, or you're living in GitHub Copilot. Now, what capabilities of that harness that you can

088. [35:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2107s)
     exploit to make the best user experience for your use case? That's the question you should ask yourself. Uh, for example, uh, Cl- uh, Codex on desktop now has an in-app browser built into the, the actual dev-- um, uh, app. Can you use this in-app browser in some interesting ways? Can you use the browser screenshot tool in some interesting ways? Uh, and in my case, I could. I realized, hey, there's probably a way to connect the

089. [35:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2137s)
     in-app browser, uh, and spin up the development server and just load the page there, and then kind of connect it to the main thread in some ways, so I can allow the user to visually iterate on that page, um, instead of in the chat. Um, and so in Impeccable, what this looks like is, uh, it's not using MCP. Um, it's simply spinning up a live poller, a little server that, uh,

090. [36:08](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2168s)
     looks for input and in- inserts a snippet into your development server. Um, it then, on the page, when you do something on the page, it sends an event back to that actual poller, uh, using, uh, server-side events. And then, uh, and this is, I think, the, the, the clever bit maybe, or the, the bit that makes it all work. Um, the poller then stops. So the poller, uh, ends itself. There's a standard out message. We talked about standard out before, right? The exit value of

091. [36:38](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2198s)
     this thing. And, uh, the model reads that message and realizes, "Oh, something happened. I better do something." So in this case, uh, in the skill itself, I give it instructions on how to handle this event. I say like, "Well, if this event comes in, you should probably build some design for this particular section of the page, and then you should send it back to this poller so that it arrives on the user side." And so this is a direct connection

092. [37:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2227s)
     between one harness capability and another harness capability, so the chat thread and the in-app browser. Um, and, uh, yeah, this is kind of like how, how it looks like on a diagram. But I think the best way to experience with it is to, is to see it. So let me bring this up. Um...

093. [37:35](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2255s)
     Okay, cursor. Uh, I think I'm already in live mode here. Um, okay. So I, I booted up live mode already, and now I'm in picker mode. I get this little bar here at the bottom. Uh, and as you can see, I can pick anything on this page. Um, I g-- now I get this little overlay bar and, um, I can select all sorts of sub commands within the skill. So these are basically translating to MD files that live within the skill. Uh, I can select the

094. [38:05](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2285s)
     amount of variance I want, and then, um, I can hit Go. And now, um, here in the thread, you can see that it picked up the actual signal in the main thread, uh, because the poller stopped. Uh, and it now knows hopefully exactly what it needs to do to first wrap this element in some special tag. Then it knows how to create, uh, variants and, uh, that are marked up in a special way with

095. [38:34](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2314s)
     CSS. Uh, and now it did that. So now, as you can see, the, uh, the thing updated immediately. I now get these three variants, and I can click through. And then if I like one of them, I can click Accept and accept it. If I don't like, like one of them, I hit, uh, Escape, and I'm back in this normal mode. Um, so this shows sort of like, uh, how to exploit an, a harness capability, uh, in an effective way for one problem space, in this case,

096. [39:04](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2344s)
     design. Um, you can also, uh, insert elements with this thing, um, and sort of click into anything here. You can, um, you can draw on top of this and leave comments. You can leave annotations if you want. Um, you can dictate. Uh, you can, uh, steer the whole page by simply writing into this. And then, uh, again, this goes back to the main agent a-and, uh, it becomes a steering signal for the whole page. Um, and you can also visualize lots of things this way. I mean, you might

097. [39:34](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2374s)
     have read, uh, Tariq's, uh, blog post about this, uh, about how HTML is a, is a really cool way to communicate as opposed to Markdown. Um, I agree, and I think also, like, uh, design MD is much better visualized as HTML. In this case, you see the m- design MD of this, you know, not great website for demonstration purposes. But, uh, um, you can use this to your advantage as well if you hijack the in-app browser and use it to your advantage. Um, so this is how

098. [40:04](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2404s)
     I make use of it.

099. [40:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2407s)
     Okay. Number eight, it worked on my machine. Um, well, I mean, everybody who, who's a developer here knows this problem. Um, this is-- this hits really hard when you ship a skill. Uh, there are so many times, uh, I kind of saw this argument on X was like, "Hey bro, just symlink. Just, you know, symlink dot Claude and all your problems will be gone." Um, well, that's great if you're

100. [40:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2437s)
     building a simple skill and if you're doing it for yourself. By all means, go for it, right? Symlink your Claude MD to agents.md. Amazing. Like symlink the shit out of everything. But it's not great if you're trying to ship a skill to lots of users because, again, we just talked about a whole lot of differences these har- harnesses have. And I'm gonna talk about more differences, and I know it's annoying because it would be great to symlink those things. But unfortunately, we don't live in that world. And unfortunately, uh, Anthropic has still not adopted

101. [41:06](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2466s)
     agents.md. So, uh, what are the actual differences? For example, we talked about sub-agents already. We talked about how... Well, on the bright side, they're widely supported now, um, but who can spawn one is very, very different. Uh, so with Claude, you can programmatically do it very easily. Codex needs the user okay. Um, in Cursor, it's agent chosen most of the time. Um, so there are clear differences. Also, if you want to predefine these

102. [41:36](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2496s)
     agents, Codex has a different syntax for that, uh, than Claude and, a-a-and, uh, and Cursor, et cetera. Another one is the Ask User tool. So one of the coolest tools in, uh, in the, um, Claude Code harness is the Ask User Question tool. Uh, it's a really nice tool that you can use to ask the user a question, right? It brings up this menu, say like, "Hey, what would you like to do?" And then you pick some option. Well, turns out Codex has a tool like this. That's the good news.

103. [42:06](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2526s)
     The bad news is that tool is only available in plan mode. So again, big differences between how these things work. Uh, and, um, what does that mean? That means that if you're not running Codex in plan mode, but your skill wants to ask questions, most of the time it simply doesn't. It will simply infer from the current context and not ask any questions to the user, uh, which is not great. So there's a lot of sentences in the Impeccable skill that specifically say, "If you're Codex-"

104. [42:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2557s)
     You have to stop and ask questions. No, you're not smart enough to infer the context. Um, so if you see lines like this, that's why. Another one is background jobs, and it's also something you learn through the hard way by doing this. For example, uh, this live mode that I just showed you, it's spawning a background task. So it's running a shell in a background task. Uh, and that, that's cool because you can keep using the session, um, and then when the background task finishes,

105. [43:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2587s)
     the model is automatically waken up, gets a-- gets the message back, and then can do something and re-react to it, uh, where Codex cannot. Uh, Codex and other harnesses do not react when a background task finishes. You actually have to manually say, "Hey, by the way, this background task, can you take a look at what it did?" And that's not great, right? If you were doing an automation like this. So there are differences in how these tasks are spawned and, uh, and how they work. So that's why if you're using the live mode in Cursor

106. [43:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2617s)
     or in Codex, it creates a foreground task, and it keeps the actual chat thread blocked. Um, not ideal, but it makes it actually work. So there are subtle differences on how these, uh, tasks are spawned. Watchers is another example. Tailwind Watch exists now. That's really cool. I mean, most of the harnesses have a way to watch, for instance, a log file. Um, but those are throttled way harder than, uh, simply spawning a background task. Edit hooks, we talked about this already. Um, they are different. And so lots and lots of behavioral

107. [44:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2647s)
     differences. But there's also model differences. So for example, in my case, um, they all have different tells in the ways they're overfitted. Uh, for example, Gemini, again, I mentioned this, loves to animate pictures. It just loves it. Um, you have to tell it not to animate pictures if you don't want a hover effect on every picture. Doesn't matter where it is. It loves it. Um, Codex loves bad letter spacing. I don't know why, but it does.

108. [44:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2677s)
     Um, Codex also loves extremely rounded borders. Uh, it will round anything you throw at it. Uh, it loves it. Doesn't matter if it's hospital website or a kids website. Uh, it also loves hairline borders. And so there are specific tells that are unique to every model. And that's not just for design. It's for architecture. It's for code architecture. It's for, you know, preferred NPM packages. Now, every model is overfitted in different ways. Uh, finding out how to

109. [45:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2707s)
     overfit it usually happens by accident. In my case, I have a pretty extensive eval harness that I run behind the scenes. In fact, every line of Impeccable is ablation tested. So I test every single line and see what it does across all models. I don't expect you to do that, but it is very good to know that, uh, that the models are different and are following instructions differently and, and the behav-behavior, the harness behavior is different as well. Um, and so what Impeccable does, it creates

110. [45:36](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2736s)
     harness-specific and model-specific builds for every single, uh, model. Um, you might not have to go all this way, uh, for your own purposes, but I just wanted to show you, uh, how far you can go with this. Uh, for example, it actually has a, um, substitute variable that picks the right user question tool depending on the harness. Or it has these XML blocks for Gemini, for Codex, et cetera, uh, that will actually insert specific

111. [46:05](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2765s)
     overfitting avoidance rules for the given models. Because it turns out if you, if you tell Claude not to letter space too much, it will letter space in the exact opposite direction. So you can't just include it all in the same scope. Um, and that's why, you know, you can, you know, if you, if you instrument this well enough, you can actually get to this write once ship to all of them, uh, skill that actually works everywhere. It's a lot of work, but it does pay off and allows you to create beautiful pictures

112. [46:36](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2796s)
     like this. Um,

113. [46:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2799s)
     now the only other problem is that, uh, typical install methods like for, um, uh, npx skills, for instance, if you've been using npx skills, do not honor, um, different directories for different harnesses. So they actually just take the first directory and then copy it or symlink it into all sorts of folders. Um, that's why if you go to the Impeccable website, uh, I've built my own CLI to solve this problem. Uh, that's why it doesn't use npx skills. So I think the community hasn't quite yet gotten to the

114. [47:09](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2829s)
     point where, uh, this is a, this is an accepted idea. And it's annoying. I get it. It's annoying to compile for different harnesses, but, uh, I found it worthwhile. Finally, um, again, build for the lowest common denominator. Um, a weaker model has opinions just fine, but what it loses is the discipline to follow yours. Um, so, uh, Codex, for example, uh, and GPT specifically loves the word gate. If you've built a

115. [47:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2859s)
     skill in Codex before, it loves gates. Um, whenever you say, "Hey, why didn't you follow these instructions?" You're like, "Well, I think we need a gate." Um, so I gave it what it loves the most, gates. Um, but I only do that for Codex. So there's a Codex MD that gets loaded on the fly for Codex, um, and GPT, uh, and then, uh, it actually follows like, you know, "Okay, here are your eight gates. You have to pass every single gate, and you are

116. [48:09](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2889s)
     not allowed to compress those gates." Um, that's really important because it loves compressing these instructions as well. Just skim over it and say like, "Well, I guess I'll do one and two and five and good." Um, and so, um, the way you solve this is by actually having it log every single result of every gate and say like, "Well, I just passed gate one. Great success." Um, and the most important lesson from this is if the gate can be skipped, it will be. I mentioned this before, right? If the model can wiggle itself out,

117. [48:39](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2919s)
     out of a difficult situation, it will absolutely do that. Uh, it will not do all the, all the things it needs to do to, uh, to complete the end result. Um, so be careful. Make it unskippable. Um, so we just built a harness extension. We went from prompting all the way to building a monster.

118. [49:02](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2942s)
     Um, but, uh, I think it turned out to be pretty powerful in my case, and I wanted to share what I've learned on the way. Uh, I don't expect you to use all of those techniques. I think some of them are pretty exotic and maybe not applicable to every use case. Um, but I hope that you find value in, uh, some of the advice that I've given today. Uh, so we've done a whole bunch of things today. Nine things a prompt can't do. We made it much more deterministic, um, and, uh, and made Impeccable better for that reason.

119. [49:33](https://www.youtube.com/watch?v=SQMCtZX3trg&t=2973s)
     Uh, if you'd like to try it out yourself, um, again, you can clone the repository for this talk. You can clone, uh, impeccable-talks. Um, but of course, it also is useful to just take a look at the actual skill and see how it's built. Um, the project is completely open source, uh, licensed under Apache two. Um, you can install Impeccable, mpx impeccable skills install, um, and check out the source code on GitHub. Um, with that,

120. [50:03](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3003s)
     um, I'm at the end of it. Thank you.

121. [50:12](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3012s)
     And, uh, now I think we have, uh, about ten minutes for any questions that you have.

122. [50:19](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3019s)
     Does anybody have questions? Yes.

123. [50:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3024s)
     Um, can you remind us where we can get the repository?

124. [50:26](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3026s)
     Oh, sorry, what was that?

125. [50:27](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3027s)
     Is there a link-

126. [50:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3029s)
     A link?

127. [50:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3029s)
     -to the repository?

128. [50:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3029s)
     To the repository? Yeah. Um, so the, the-- uh, this is hard to see, but, uh, let me, let me put it up here. Um, this is the repository,

129. [50:44](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3044s)
     uh, for the talks. Yeah.

130. [50:47](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3047s)
     Uh, awesome. Uh, my question was you mentioned that, um, having the agent get prompts from return of, uh, scripts, uh, series as well, which I noticed in this also, but you mentioned it breaks prompt caching.

131. [51:03](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3063s)
     Yeah. I-- The question is, I mentioned that it breaks prompt caching. Um, the, the actual sort of trick, the technique to actually get, uh, something back from a script, um, within a skill. And the reason is because the result is dynamic, right? It could be anything. Um, so unless the result is always the same, it's a dynamic shell execution. Um, so it gets inserted into the, into the thread. Now the-- Now, to be fair, the skill will still be cached.

132. [51:33](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3093s)
     So the skill will still be cached, but, uh, but I guess I'm differentiating between the skill with inline, uh, you know, static content versus the skill with sort of like a dynamic instruction to call out. So this part will not get cached.

133. [51:48](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3108s)
     Oh, okay.

134. [51:49](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3109s)
     Yeah. That was, that was my main point.

135. [51:51](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3111s)
     Yeah.

136. [51:52](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3112s)
     Yeah. Yeah.

137. [51:53](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3113s)
     What is the process by which you evaluate and iterate on the skill itself?

138. [51:59](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3119s)
     Yeah. What is the process on how I evaluate and iterate on the skill? Um, so I-- The process is pretty involved. Um, let me see. Uh, let me see if I can bring this up on screen.

139. [52:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3142s)
     Uh... Uh, okay, here we go. So h-here is a glimpse. Oh, no. Okay. I just shut down the server. That's fine. Um...

140. [52:31](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3151s)
     Actually, you can-

141. [52:31](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3151s)
     Okay, I'll just voice over. So, um, yeah, I mentioned I built an, uh, evals harness. And, um, and so I've created myself a harness that, uh, re-- closely recreates the conditions and the tools of every harness that I care about. So for instance, it, it uses the Claude Code SDK.

142. [52:56](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3176s)
     Yes, uh, sorry guys. Can you, uh, can you lower your volume a little bit? Um, because, uh, people are still trying to hear the questions. Um, thank you. So how do I, how do I test this? How do I build it? So this-- it's a combination. So first of all, Impeccable has a ton of end-to-end tests in the repository. Um, uh, that's both LLM-driven tests as well as, um, end-to-end Playwright tests. So that's one. Uh, and that's useful for things like testing the live mode scripts, for example. Um,

143. [53:26](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3206s)
     but then beyond that, how do I test that it actually works? Uh, well, I've built a evals harness. That one is not open source yet. Um, but I built a evals harness that closely replicates every, um, every model harness that I care about right now. Specifically right now, uh, uh, Claude Code, Codex, and Gemini. And, um, and I'm trying to expand it to more. And it also recreates the tools, like for instance, a browser screenshot tools, uh, or something along those lines. And, um, and then it also

144. [53:56](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3236s)
     recreates, um, the-- Because so-some parts of Impeccable are interactive. In the initialization of Impeccable, oftentimes the user gets asked, "So what," you know, "what would you, what would you like your page not to feel like?" And so you get these interactive, like, back and forth. And so I've built this LLM that acts as the user against the other LLM, and so it does like an interactive, uh, you know, back and forth turn. Um, so I've built that harness, and then I've built a, um, mixture of expert design judge that runs

145. [54:26](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3266s)
     on top of it. So basically give it eyes, uh, to evaluate each result. Uh, and then I can run, uh, across twenty different niches, like for instance, Italian restaurant. Um, I run across all models that I care about, GPT Five Five, Opus, Sonnet, um, and do like five to ten tests, um, for each of those, uh, for each skill release to see, you know, how it changed. I also run against Competitors. For instance, I run against the front-end design

146. [54:56](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3296s)
     skill to see does it make a difference, um, um, and, and, and how does it make it worse or better? Um, and then beyond that, I'm doing ablation testing. That's, uh, harder and more expensive, I would say. Um, so I don't recommend it for everyone. But this-- the ablation testing-- So every-- You'll see this in the source code of Impeccable. Every rule has sort of an XML tag that says, like, you know, a, a unique identifier of that particular line. Um, and that, that will be used by the harness

147. [55:26](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3326s)
     to then do a test where it removes that line, um, runs the evals against all models, and then adds the line back in, and then, uh, uh, uses the detection engine of Impeccable, the deterministic one, to see did it actually change, right? So if there's a line that says, "Hey, don't, don't do like gray on colorful backgrounds for, for contrast purposes," um, there's a, there's, um, an ablation test and then a deterministic check or

148. [55:56](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3356s)
     feedback loop that tests against it. So, uh, in short, quite involved. Um, but, uh, but I really-- It started, you know, vibes-based, uh, and now it's really, uh, truly, um, well-tested. Yeah. Yep, go ahead.

149. [56:11](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3371s)
     Do you set up evals for taste-- for evaluating taste? How good the design looks?

150. [56:15](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3375s)
     Sorry?

151. [56:16](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3376s)
     Do you set up evals for evaluating taste-

152. [56:18](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3378s)
     Yes

153. [56:18](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3378s)
     ... um, and evaluating how good a design looks?

154. [56:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3382s)
     Yes. Um, I do have, I do have, um, evals for evaluating taste, but I don't think they work particularly well. Um, I just talked to, uh, Ben from Contra about this. Um, I don't think-- I mean, I know, I know, um, some of my colleagues might disagree, um, but I don't think taste can be solved at a model level. Um, I actually think it's a, it's a fundamentally human thing. Um, because taste is scarce and unique, and once everybody

155. [56:52](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3412s)
     uses the same taste, uh, it becomes ubiquitous, and then we don't think it's tasteful anymore. So it's-- It-- I think it's, uh, um, I think it's hard. Um, and I also think the models are particularly bad at eval-evaluating taste. So for example, um, there are certain things that our models can evaluate well, like, "Hey, is this-- is, is the correct thing in the first viewport?" Right? So functional stuff, that works. But what doesn't work, and here's one example, I've built, again, this mixture of judges, and

156. [57:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3442s)
     one judge rates whether the first viewport looks great, right? And, and is effective. Um, and one of the tells is that, uh, Gemini, for example, the more stuff there is in the first viewport, the higher it rates it. Right? This is just a general rule. Like, if you just cram the viewport full, it gives it a higher ranking. And so there's a, like, an interesting example of, like, you know, the models are often maximalist, right? They're just like,

157. [57:52](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3472s)
     "Well, more is more, I guess." Um, and so oftentimes I build judges that actually invert the response of the model, uh, which is really strange, but it works. Um, where it sort of judges something very high. I'm like, "Okay, that's definitely not a good design." Um, so anyway, I don't think it's solved and I don't think it's solvable, but, um, I do have, I would say, a tool that gives you the design director eyes that works marginally better than random, and that's good enough

158. [58:22](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3502s)
     for me for like a first pass, and then I use my own human eyes to evaluate results and annotate them.

159. [58:30](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3510s)
     Any other questions? Yeah, over here.

160. [58:32](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3512s)
     What do you see as the future for skills in general? Do you have any ideas?

161. [58:36](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3516s)
     The future for skills? So I would say-- Hmm. That's a, that's a broad question. Um-

162. [58:43](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3523s)
     It seems right now you're doing a lot of steps to try and wrangle the-

163. [58:46](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3526s)
     Yeah

164. [58:46](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3526s)
     ... model following your procedures. Do you think there's a better way to do that?

165. [58:51](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3531s)
     Yeah. So I'll, I'll first answer for Impeccable and for me. So in the, in the case of Impeccable, I think we're, we're, we're definitely outgrowing, uh, the skill platform, kind of what's possible with skills. I think the, the live mode is a good example of that. The live mode, um, was sort of like a Jurassic Park experiment to see, like, can I do this? And the answer is yes-ish. Um, I think it's, it's, it's working better than I expected, but,

166. [59:21](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3561s)
     um, it still has a lot of problems. I mean, it would be way better to do this in a first-party harness integration or like a, like a first-party tool. Um, so I think there are limits that I'm hitting, uh, where, um, where skills might not be effective anymore. I think in general, I would say most skills should probably be written by the individual users. I think those that actually go, go through the effort of packaging a skill and sharing it with others need to invest more time than they currently do. So I guess

167. [59:51](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3591s)
     that's my hot take. I think right now I've, I've seen plenty of skills that are distributed that, uh, do not work well in a model that the author didn't use, for example, right? And so I think, I think we just have to raise the bar of what's acceptable to ship, uh, to, to, to people. I mean, again, this is like the works on my machine thing. Um, I would rather see less skills in the ecosystem that are really battle-tested and proven. Um, and I, I hope w-we're shifting towards that because right now it's sort of like a Wild

168. [1:00:21](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3621s)
     West. Yeah, go ahead.

169. [1:00:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3624s)
     In that regard, there's no, like, common way to test a skill to make sure that it works across all harnesses, all models. So potentially there could be an opportunity there for you to build something.

170. [1:00:37](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3637s)
     There's no common way to test the skills. Yeah. And then that could be an opportunity. That's a good point. Yeah. I guess I could-- I do have the tool for that. That's true. Yes. Um, I could do something with it. Yeah. Uh, right now it's purely built for my own purposes. But, uh, but yeah, the same is true for, for instance, like the, the Impeccable installer and compiler. Um, I don't think most people know that it exists. Uh, that it can compile to every harness and that it has these substitution techniques and stuff like this. Like, I could probably release that standalone as well.

171. [1:01:07](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3667s)
     Yeah, it's a good point. Yeah, go ahead.

172. [1:01:10](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3670s)
     Wondering about your thoughts on, uh, if you have any thoughts on that MCP having skills on the server?

173. [1:01:17](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3677s)
     MCP having skills on a server? How would that work?

174. [1:01:21](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3681s)
     The new, the new spec, the new spec coming up with skills on the server.

175. [1:01:25](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3685s)
     Oh, I see. Yeah. Um,

176. [1:01:29](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3689s)
     to be honest, I haven't tried it out yet. Um, or I haven't really read too much into it. I think MCP in general, um, you know, I worry greatly about context pollution and, um, I do that with skills too. And I think, um, I'm not using MCP a lot for that reason, um, because it polluted my context many times. Um, how do skills work in MCP?

177. [1:01:58](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3718s)
     Well, they're, they're coming up with, uh, you, you'll be able to download MCP, that skill from your, your MCP server.

178. [1:02:05](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3725s)
     Oh, you can download a skill from MCP server. Yeah. Okay.

179. [1:02:08](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3728s)
     So one of the issues that I, I think, um, I also have a question about is, is basically what's the recommended way to package them so that they are installable everywhere? Like-

180. [1:02:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3740s)
     Yeah

181. [1:02:20](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3740s)
     ... plugins, uh-

182. [1:02:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3744s)
     Yeah, yeah, yeah

183. [1:02:24](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3744s)
     ... what is the, what is the best practice for-

184. [1:02:27](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3747s)
     So what's the recommended way of packaging them and distributing them? Yeah, it's a good, good topic. Um, so of course, like the harnesses and the, and the Frontier labs have their own ways. I mean, um, Codex has a marketplace that you can use for distribution, plugin marketplace. Um, uh, Claude Code has a marketplace as well. I think they started with the marketplace technique. Those marketplaces don't work particularly well. I mean, the Claude Code one for sure doesn't work particularly well. I know this for a fact because, I mean, the uptick me-

185. [1:02:57](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3777s)
     mechanism often doesn't work a- and people are like, "Well, my skill doesn't update." And oftentimes there's a caching issue. So it, it-- My experience has been hit or miss with the native methods of distributing, and then of course it's only for that particular provider. That's why projects like, uh, skills.sh exist. But again, the problem with npx skills right now, it doesn't, it does, it, it doesn't allow for like, you know, more advanced skill use cases like, you know, compiled for every different harness. I have a pull

186. [1:03:27](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3807s)
     request, um, i- in the, in the repository. Um, and I've, uh, I've bugged Andrew a couple of times about it . But, um, he, uh, he still has to, uh, get it merged or agree to agree with me on that, I guess. Um, I think, uh, we're still discussing. Um, but yeah, npx skills I think is a great project in general. I think it'd be great if we could sort of like standardize around it. Um, there's also one from Microsoft that's trying to do that. Um, a project from Microsoft, I forgot the

187. [1:03:57](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3837s)
     name of it. Um, but there's definitely no, no industry standard for distribution yet. Um, yeah, I'm not-- I don't love having to maintain my own CLI installer. I would rather not. Uh, it's annoying. Um, but, uh, it does make it so it plays safe with all harnesses, install the hooks in the right part of the system, et cetera. So it's, um, yeah. Yeah. Okay. I think I'm, uh, way out of time. Um, but come up and speak with me if you like.

188. [1:04:27](https://www.youtube.com/watch?v=SQMCtZX3trg&t=3867s)
     Yeah. Uh, I would say I'll end it here, but yeah, come, come up if you like. Um, let me just, uh... Thank you.


