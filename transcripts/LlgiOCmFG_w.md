# Fixing the PR Bottleneck — Matt Pocock, AIHero

Source: https://www.youtube.com/watch?v=LlgiOCmFG_w

Uploaded: 2026-09-25

Transcript source: complete timestamped publisher transcript at https://ai.engineer/talks/LlgiOCmFG_w-youtube-40c0a903db79223717ca . Includes slide text interleaved by publisher. Native YouTube extract lacked captions.

## Transcript

01. [0:01](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1s)
    All right. I'm here to talk about Fixing the PR Bottleneck, and this is kind of a grand title for trying to fix the thing that most organizations struggle with, I think, and have kind of historically struggled with before AI. You know, we have always had huge numbers of PRs just laying around that no one's bothered to review, and this has now increased massively because of the new strains on us, because of AI imposing all these weird constraints. And to do this, I'm gonna use the

02. ![Title slide for Matt Pocock’s talk on automated checks, automated review, and human review.](https://assets.ai.engineer/sites/aiecode2025/sha256/b7ad0029ed537b90c21c49f752e87b50ae8737eda07aa8cbb9e867016b5c8d5e.webp)


    Fixing the PR Bottleneck



    Matt Pocock frames the PR bottleneck as a long-standing backlog of unreviewed pull requests, intensified by AI. He introduces automated checks, automated review, and human review.

    Text in image

    ```
    Fixing The PR Bottleneck
    Automated Checks, Automated Review, Human Review

    Matt Pocock

    AI Engineer
    PARIS
    Organized by Mistral
    ```





    [0:18](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=18s)

03. ![Stage screen displaying the AI Hero skills page and the phrase “Skills For Real Engineers.”](https://assets.ai.engineer/sites/aiecode2025/sha256/fa8f7e2df2a43520982a726bf2472b3c0325d9dc4d93482b72ed85421b72ec4d.webp)


    Skills for Real Engineers



    Pocock introduces his skills as the framework for the talk and announces new skills intended to speed up pull request work and review.

    Text in image

    ```
    aihero.dev/skills
    Skills For Real Engineers

    Other visible text:
    AI Engineer
    [illegible]
    ```





    [0:28](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=28s)

04. [0:31](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=31s)
    rubric of my skills, which is-- you've kind of heard about, maybe you've used them. And I have a couple of new skills to announce that are going to hopefully improve the way that you do PRs, improve the way that or improve the speed at which you can review them and do them. Speed. Now, we're being pushed to do more with less, essentially, or more PRs, more work, more stuff. And this is kind of the central promise of AI, that we're going to be able to use these agents to

05. ![Slide with the word “SPEED.”](https://assets.ai.engineer/sites/aiecode2025/sha256/98e5a0baab98e1ca478ca9cfc9e22246c31358f945375dcd8cce269e8ad42380.webp)


    Speed



    Pocock describes pressure to do more PRs with less, and the promise of using AI agents to scale up the work people can do.

    Text in image

    ```
    SPEED

    Interface text:
    AI Engineer
    PARIS
    Organized by Mistral
    ```





    [0:45](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=45s)

06. [1:01](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=61s)
    scale ourselves up to do more work. And this has resulted in the software factory, probably the biggest buzzword of the day. Everyone's talking about software factory that I've chat to. And I think of a software factory as primarily something where instead of the human initiating all of this work, we're gonna pass some of that initiation. Some of the initiation is gonna be done by agents. And I think of there

07. ![Stage screen displaying “Software Factory.”](https://assets.ai.engineer/sites/aiecode2025/sha256/6f9e91526ee09acf81f97525718f2fb2c8065ac2d815aa396745d9fc0c6b58c7.webp)


    Software Factory



    Pocock describes a software factory where agents initiate some of the work, helping people scale what they can do.

    Text in image

    ```
    Software Factory
    ```





    [1:09](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=69s)

08. [1:50](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=110s)
    Maybe from there you have a classifier like Jev come in and say, "Okay, let's turn that into a fix or turn that into a reproduction," or maybe I ping people straight away. And maybe you have other things. Maybe you have PlanetScale hooked up, so it gives you query reports on the slow queries on your database. Maybe that then triggers a different, um, thing of your software factory. All of this is not humans triggering it, it's, uh, deterministic code triggering it, right? And so these accelerate your software factory. They push more code through it. But then you need brakes,

09. ![Slide describing software factory inputs such as bug reports, support tickets, and slow queries.](https://assets.ai.engineer/sites/aiecode2025/sha256/e8b5bbb44477842bd4f12f0fe693cc7b6cebafcab616fb0524d8206197f3df7f.webp)


    Accelerators



    Bug reports, support tickets, and slow queries feed the software factory. Deterministic code can trigger workflows that push more code through it.

    Text in image

    ```
    Accelerators

    Inputs to the software factory - bug reports, support tickets, slow queries
    ```





    [2:00](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=120s)

10. [2:20](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=140s)
    right? If you just have permanent acceleration pushing stuff through your factory, you're gonna end up with a slop cannon, right? You're just gonna end up with a ton of slop crappy PRs that you're not gonna be able to touch or review or even freaking look at. So you need brakes. These are mechanisms that slow down, that increase quality, that make sure that your code base doesn't turn into a software entropy nightmare, because code is the environment your agent operates in. And if you have bad code in your code

11. ![A presenter stands before a slide defining brakes as mechanisms that slow down and increase software factory output quality.](https://assets.ai.engineer/sites/aiecode2025/sha256/035c81a54c41a1690498f2ffc9bbbea09860d6a1b2182bc49c738f2087a8f5b4.webp)


    Brakes



    Brakes slow the software factory and improve output quality, helping prevent a flood of low-quality PRs that humans cannot review.

    Text in image

    ```
    Brakes

    Mechanisms that slow down and increase output quality of the software factory.
    ```





    [2:23](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=143s)

12. [2:50](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=170s)
    base, that is going to beget more bad code. And so I'm gonna talk about these three brakes in this talk, and talk about how we can use them to counterintuitively go faster. So automated checks. These are the deterministic checks in your repo that we've had for thousands of years or, you know, since the '50s. Deterministic checks where we have linting and tests and type checking and code quality metrics, all of these things going together, and they all work the same every time.

13. [3:21](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=201s)
    Layered on top of that, we have automated review. So we have agents who look at our code and say, "Okay, you know, these are for the things that the tests didn't catch," or, "This is looking at the structure of the code base in general." And then on top of that, the third layer, the final layer is human review. So people looking at the PR. And these three layers form this kind of cake that we end up with when we get to human review. And so more speed of course means more PRs, and so the goal here is to make human review

14. ![A slide says humans review the pull request and describes this as the most costly step in the process.](https://assets.ai.engineer/sites/aiecode2025/sha256/2bf5780788c9f5484f4c056926ddf765343ee5b939064b9b3f2e254462ba0231.webp)


    Human Review



    Human review is the final and **most costly layer**. Automated checks and review help catch issues earlier, so people can review PRs faster.

    Text in image

    ```
    Human Review

    Humans review the PR. The most costly step in the process.
    ```





    [3:36](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=216s)

15. [3:51](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=231s)
    faster by leaning on those first two phases. And we've got to stop the slop. That's the first principle here, which is if you raise the quality of the code that you're shipping, you're gonna end up doing less human review because it's just gonna be better work, and so you're gonna end up needing to, uh, make fewer interventions. So automated checks. Now, automated checks are cheap. That's the cool thing about them, is that they don't cost tokens like automated review does. They don't cost human effort, they just

16. ![A slide says higher code quality leads to faster human review.](https://assets.ai.engineer/sites/aiecode2025/sha256/51b3332dfe258e79d084c0c5c42b062fc1cf8284d58b4c1c795d678fcf10bf60.webp)


    Stop The Slop



    Pocock argues that higher-quality code needs **fewer reviewer interventions**, making human review faster.

    Text in image

    ```
    Stop The Slop
    Higher code quality = faster human review
    ```





    [4:04](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=244s)

17. [4:21](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=261s)
    cost CPU cycles. So these are, for instance, you know, you run your tests on every code change. Maybe those tests do incur some tokens because let's say, um, an agent, uh, creates a bug and the tests catch it, then you need to spend some tokens to go and fix it. But those are tokens pretty well spent in my opinion. So checks are cheap. That means you can layer on loads and loads and loads of them on your repos, and you're probably not using enough of them or not being creative enough with your use. But checks can

18. [4:50](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=290s)
    lie.

19. [4:53](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=293s)
    Does a green CI mean that the code is ready for merge? No, it does not. And so we've always needed on top of these checks some extra layer to figure out if there's anything catastrophically wrong with the code before we ship it. And so all of the other phases, the human review and automated review, these are lie detectors. These are for finding lies in the automated checks. Now, I wanna show you some of these lies first of all, because this helps when we're thinking about code and thinking about automated checks to see how bad it is and how

20. ![An automated checks slide asks whether green CI means code is ready to merge and answers no.](https://assets.ai.engineer/sites/aiecode2025/sha256/f1c6a09be1b098292b572fb00fde9dae3bec2441785ed64418af5325d8e8eff9.webp)


    Checks Can Lie



    A **green CI** does not mean code is ready to merge. Human and automated review provide another layer to catch serious problems that checks miss before shipping.

    Text in image

    ```
    Automated Checks

    Checks Can Lie

    Does a green CI mean that the code is ready for merge? No.
    ```





    [4:54](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=294s)

21. [5:23](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=323s)
    bad things can get. The first is tautological tests, a test that just reasserts the implementation. Opus 5 got addicted to these. I don't quite understand why. It would have, for instance, x post character limit equals two hundred and eighty. Can anyone guess the test that was written to test this behavior, right? You've probably seen this a thousand times. This is real code from agents or from stuff that I found my agents doing. It said expect x post character limit to be two hundred and eighty. So the implementation

22. ![A tautological test only reasserts the implementation.](https://assets.ai.engineer/sites/aiecode2025/sha256/d6a41a34eafd1331ceda453aa9fda16c9b5ca2959b06e6ecd4a53ea98ef49055.webp)


    Tautological Tests



    Pocock describes an agent-written test that checks whether a 280-character post limit equals 280, simply repeating the implementation.

    Text in image

    ```
    Tautological Tests

    Automated Checks

    A test that only re-asserts the implementation.
    ```





    [5:24](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=324s)

23. ![Code exports a post character limit of 280.](https://assets.ai.engineer/sites/aiecode2025/sha256/a5097f41d461cf72b4ffaa5d88ee89f4113d6c8c2723ca4de3331392d7a7a9c7.webp)


    Post Character Limit



    Pocock uses the 280-character constant to illustrate a **tautological test**: asserting the same value ties the test to implementation details, so renaming the constant can break it.

    Text in image

    ```
    export const X_POST_CHARACTER_LIMIT = 280;
    ```





    [5:34](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=334s)

24. [5:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=352s)
    looked like that, and the test essentially reasserted the implementation. That is a tautological test. And tautological tests are bad because they're extremely structure sensitive. They're very sensitive to the actual internal workings of the system. So it means I cannot change that constant without a test failing. But I cannot rename that constant without a test failing. Like I have to do-- it's so tied into the structure of my system. And I found another

25. ![A test asserts that the exported post character limit equals 280.](https://assets.ai.engineer/sites/aiecode2025/sha256/4fa0b8b128c85fb66b42f32435781a76d9ba80ea873163c1dfe677d3f80b8289.webp)


    Tautological Test Example



    The test checks that the exported constant equals 280, reasserting the implementation. Pocock says this ties the test to the system’s structure, so even renaming the constant breaks it.

    Text in image

    ```
    import { X_POST_CHARACTER_LIMIT } from "./x-character-count";

    describe("x-character-count", () => {
      it("has a limit of 280 characters", () => {
        expect(X_POST_CHARACTER_LIMIT).toBe(280);
      });
    });
    ```





    [5:54](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=354s)

26. ![A structure-sensitive test knows too much about the system's internal workings.](https://assets.ai.engineer/sites/aiecode2025/sha256/f3e4c5f5ee2fc7075a4b201596ae196b70f43bc161e0b77c7dfb0e96c1892cf2.webp)


    Structure-Sensitive Tests



    A test tied to **internal structure** can fail when a constant is renamed, even if its value stays the same.

    Text in image

    ```
    Automated Checks

    Structure-Sensitive Tests

    A test that knows too much about the internal workings of the system
    ```





    [6:05](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=365s)

27. [6:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=382s)
    one which is even more egregious, I would say. This is incredible, uh, test. What it's doing here is it's essentially testing whether two things in the UI appear in the right order. So it's checking that the pitch detail page, uh, or rather the video section comes after the content plan. What it does is it doesn't render it to a screen, it just reads the actual file, the module into its own memory, and then it's-- finds the right thing, so

28. ![Test code reads a source file and checks that Videos appears after Content Plan.](https://assets.ai.engineer/sites/aiecode2025/sha256/893073e9e3c74d42c416cd750def346f10d3d5b0e798c888cb0afc4c364d0a07.webp)


    Checking section order in source code



    The test reads the pitch detail source file and **compares text positions** to check section order. A change to the source structure can make it fail even if the UI still shows the sections in the right order.

    Text in image

    ```
    const PITCH_DETAIL_PATH = path.join(
      __dirname,
      "..",
      "routes",
      "_app.pitches.$pitchId.tsx",
    );

    describe("pitch detail page section order", () => {
      it("renders Videos section after Content Plan", () => {
        const content = fs.readFileSync(PITCH_DETAIL_PATH, "utf-8");

        const contentPlanIndex = content.indexOf(">Content Plan<");
        const videosIndex = content.indexOf('title="Videos"');

        expect(contentPlanIndex).toBeGreaterThan(-1);
        expect(videosIndex).toBeGreaterThan(-1);

        expect(videosIndex).toBeGreaterThan(contentPlanIndex);
      });
    });
    ```





    [6:33](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=393s)

29. [6:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=412s)
    finds content plan, finds videos, and then it expects the videos to be after it in the source material. Which is crazy if you think about it, 'cause I can just m-- like change the way the source material looks and this test will fail. It's too sensitive to the structure of my code base. So that's another way that automated checks can fail. And there are also-- or sorry, automated checks can lie. There are also tests that literally cannot fail, and this will feel familiar to you if you've abused mocking in the past or

30. [7:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=442s)
    abused various things. For instance, here we have a useAudioBoost function, and this useAudioBoost function, uh, its internals use the AudioContext API in the DOM. Don't worry if you don't know any of this. But what we're doing here is we're just stubbing it out with some fake methods. And it turns out that AudioContext has some complicated error modes, and it will fail if you use it under strange conditions. And so just doing this means our tests cannot fail using those modes, and we're gonna hit strange errors in

31. [7:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=472s)
    production that our tests can't fix. And so the question is then, if you can cheat on automated checks, if, you know, and even in good faith ways as well. The, the AI isn't trying to write bad tests here, it's just taking our instructions and writing tests that are too tied into the structure instead of actually executing code. So how do we make automated checks harder to cheat? If we can do that, then we can increase the quality of those checks, which means which

32. ![Slide asks how to make automated checks harder to cheat.](https://assets.ai.engineer/sites/aiecode2025/sha256/52a1b2c784323bdb8bfa345df56b726d8cfb937d11db45195fab55b75011eae4.webp)


    Making automated checks harder to cheat



    Tests that stub out AudioContext can **miss its failure modes**. Pocock asks how to make automated checks harder to cheat, even in good faith.

    Text in image

    ```
    Automated Checks

    How do we make automated checks harder to cheat?
    ```





    [8:01](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=481s)

33. [8:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=502s)
    increases our quality bar. And the first thing I really like about this is codebase design. So you can actually design your way out of these bad checks. So what does good codebase design look like? I've talked about this before in previous AI engineer talks I've given, which are deep modules. These are modules that hide complex behavior behind simple interfaces. This is a John Ousterhout idea from the philosophy of software design. If we look at these two modules, we've got A, which has a

34. ![Codebase Design section title.](https://assets.ai.engineer/sites/aiecode2025/sha256/d93f28b5e7d525acff999b0f5c44df314867b0e255d463997306618920ca0864.webp)


    Codebase Design



    Pocock introduces codebase design as a way to make automated checks harder to cheat.

    Text in image

    ```
    Codebase Design

    Codebase Design
    ```





    [8:28](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=508s)

35. ![Deep modules hide complex behavior behind simple interfaces.](https://assets.ai.engineer/sites/aiecode2025/sha256/05a0e622adec3a8541565360a84ff5cdd32e4bda077b63a4bbe4d47256a2b7dd.webp)


    Deep Modules



    Pocock recommends **deep modules** that hide complex behavior behind simple interfaces. Tests can focus on the interface, making them less sensitive to implementation structure.

    Text in image

    ```
    Codebase Design

    Deep Modules

    Modules that hide complex behavior behind simple interfaces.
    ```





    [8:40](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=520s)

36. [8:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=532s)
    large implementation hiding behind a tiny little interface at the top, okay? And then B is a large interface, lots of functions you can call, and those functions individually don't do very much. Does that make sense? Yeah? Now, if you have a deep module like A here, you're gonna have fewer structure-sensitive tests because you're hiding more of the implementation behind that interface. If it's just testing at that interface, you're gonna get better tests. And so your job

37. [9:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=562s)
    here is to force the agent to use that little interface instead of reaching into the implementation to test these weird implementation details. So I've got a skill for this. You can have like the weirdest vibe coded like code base, the crappiest code base that you've ever set your eyes on, and you can run this skill on it, and it will make it better. What this does, it essentially gives you opportunities for deepening modules, and kind of looks like this. Raise your hands if you've used this skill, by

38. [9:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=592s)
    the way. Not sure how many of my folks are in this room. Yeah, okay. It's really freaking nice. Essentially, it gives you a HTML document, and I'll get out of the way here, of all of the different, um, potential opportunities it sees. So we can see here we have a before and we have an after where we're sort of like reducing duplication. We're creating a nice deep testable module. And then you can go ahead and implement that. And attached to this, there's also this kind of language that I've put together for describing modules because like if you

39. [10:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=622s)
    ever try and read up about how to structure a code base, you're gonna find 20 different approaches, and they're all gonna be called DDD. And like what you need is a consistent language that you can use in your team to talk about this stuff. And so I have a little codebase design skill that defines what locality is, defines what leverage is, defines what a seam is. I was using seams before they were cool. And what locality means is kind of how, uh, well located together all of the code is. How can you

40. [10:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=652s)
    change like a small change in one module and have it ripple out? And also leverage is what you get when you have a deep module because the caller, the person who's actually calling that module, gets a lot of value of calling a simple function. Both of those are very good in code bases, and good for agents too it turns out. But I'm sort of describing all of these highfalutin coding standards, but how do we actually make sure the agent does them, right? How do you make sure the agent

41. [11:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=682s)
    creates deep modules and creates good tests and doesn't write these crap tautological ones or structure sensitive tests?

42. [11:30](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=690s)
    Well, I do think most people get this wrong. And my first piece of advice is don't put coding standards in your implementer agents, okay? Let me explain this. If you imagine the implementer agent kind of looks like this, where this is all of the things the agent needs to be able to do in its single context window. It needs to be able to explore, like to look for the code that it's going to change. It then needs to actually change it, so make the updates to the files in the

43. [12:00](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=720s)
    green. And then it needs some budget for actually debugging the thing, so for running those, uh, automated checks, for actually checking and verifying that it works. Now this is quite a lot of work it turns out, and if you try to impose your coding standards on it as well, it's going to perform worse.

44. [12:21](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=741s)
    So implementation is overloaded. That's the mental model I want you to have. And so can we find a way to impose those coding standards in a way that isn't so overloaded? Well, this is my effort. This is my code review skill, and it receives a diff, and it reads a file inside the repository called coding standards, which you can write, you can customize, and then it checks if the code follows those standards. And so if we look at the reviewer agent here, it also crucially

45. [12:51](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=771s)
    runs it in a sub-agent. So it's got its own context window to kind of handle here. It's got its own budget. This one, it needs to do some exploration, right? Because sure, it receives the diff, so it knows exactly where it's located, where the code is, but it should probably do a bit of exploration just so it has the wider context, understands the code. But it doesn't need to do any implementation, doesn't need to do any debugging. So while implementation is overloaded, review is actually underloaded, so it doesn't have that many

46. [13:21](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=801s)
    jobs to do. This means you can pile in a bunch of coding standards to it, and it will do a much better job than if you tried to do it with implement. So I think of this, and this is uncomfortable, right? 'Cause we, we all want to be able to just get good code out the first time. But I think of this as the two-part process for writing good code, which is implement, you make it work, and then code review, you actually make it good. You impose your coding standards. And for, you know, the retro developers among us,

47. [13:51](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=831s)
    this is essentially a red-green refactor approach. We use one context window to make it okay, do the red-green, and then we do another context window to refactor it. That's at least how it works in my head, and it's been very successful for me. This means that when you have coding standards, you don't put them in global scope. You don't put them in agents.md 'cause then they sort of drown out your implementer. It may read them, it may not. You put them in codingstandards.md, and that way just the code review agent does it.

48. [14:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=862s)
    Now, I've got another idea here, which is I've been talking to lots of people today, and lots of people saying, you know, I've been talking about review and automated review increased, you know, Fixing the PR Bottleneck. So many folks say, "Oh yeah, we just use a third-party service. We use, uh, Cursor Bug Bot, we use CodeRabbit," or something like that. I think that I've, I've really tried to make a generic code review skill in the past that finds all the bugs and does security review and that kind of thing. It turns out it's really, really hard because you either

49. [14:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=892s)
    make it too general and it just gives you false positives that aren't actually relevant to your use case, or you make it too specific. You say, "Okay, find all the TypeScript stuff," and then Rust people can't use it. So I would say don't outsource automated review. Build your own. Build up your own coding standards over time. Share them across your team. And if you have an opportunity to impose coding standards, if you've got some docs sitting around that no one reads, this is the place to put them in. And also,

50. [15:22](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=922s)
    when you have this automated reviewer, a really natural inclination for lots of people is to say, "Oh yeah, my code review agent, what it does is it reads the code and then it comments on the PR." Ugh. So what your code review d- agent is doing in that case is it's providing more work for the human reviewer. The human reviewer then has to read all of these verbose comments and figure out, "Okay, do we implement this? Do we implement that?" The reviewer should commit. It should make fixes. So it should actually change the things that it finds,

51. [15:53](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=953s)
    'cause then when the human comes around, you're reviewing a really nice artifact. If it finds anything that it has any questions over, then of course it can comment, but the default should be commits. Stop trying to one-shot good code. Stop trying to make the implementer agent the only thing that you do and go, "Okay, I'm gonna force it to be amazing." It takes a little bit of, you know, thinking your way out of there, but once you realize it, it is fabulous. So okay, with all of that process, we've run our automated

52. [16:23](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=983s)
    checks. We've now run our automated review to make sure the automated checks aren't lying. How do we then maximize the PR's quality in terms of human review? How do we get it, like, working the best it can? So we need a human-friendly PR, and this is a new skill, uh, coming into the repo, which is currently in progress, but I'll be releasing it soon, which is the PR skill. And this is one I've been mulling over for a long, long time, haven't quite figured out what the state of the art is, and I've realized the best way to make a

53. [16:52](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1012s)
    PR skill is just to steal all the best ideas that everyone's got, and it's very nice. Now, what does a good PR body look like? How would you recreate this skill on your own? Well, the first principle is some reviews are more important than others. Not every review is essential, right?

54. [17:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1034s)
    And once you understand this, you realize, okay, that means I can focus my energy on the really important reviews. But how do we categorize that? Well, you gotta think about the PR as using this AWS terminology, which is, is it a one-way door or is it a two-way door? Now, most PRs that you have will be two-way doors. You can merge the PR and then always pull it back later. It's the glorious benefit of being a software engineer as opposed to a civil engineer, right? Mostly when you're a civil engineer, it's a, it's a

55. [17:44](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1064s)
    one-way door, right? If you get something wrong, that bridge is going down. But if you have a two-way door, it means that you can easily revert the change. Now, that might be more, um, a bit more nuanced than you might expect. It might be that a very simple change accidentally blasts out an email to 60,000 people or something, in which case that is a one-way door. You wanna review that very, very carefully. Involves expensive migrations or data loss, that is a one-way door. Review the hell out of that PR. But also tied onto

56. [18:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1094s)
    that, we need to understand the blast radius of this PR. What can go wrong? And if things do go wrong, how bad is it? And this means I end up with a nice little sort of summary right at the bottom of all of my PRs, which is the merge danger. I can see this one is a two-way door. Its blast radius is localized, and so I can see, fantastic, I don't need to pay that much attention to this. I'm just gonna sort of review it a little. That's really important. Next, we need to understand what the PR is even doing, right? And I've

57. [18:44](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1124s)
    tried lots of different ways of figuring this out, and the best thing I've come up with is using pseudocode. Now, a huge, um, point of gratitude here to the Show Me skill from the HumanLayer skills repo by Dex Hawley. This is a phenomenal skill that just essentially dispenses with most text and shows things to you in images and diagrams instead. This makes it a lot easier to grasp actually what's changing and why it's changing. So you get the kind of standard

58. [19:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1154s)
    sort of set of like mermaid diagrams and UML for, you know, this is a sort of sequence of things that happened. You also just get these lovely simple ones like this, for instance. We can look at this and go, "Okay, we're working in a CLI. We can see a new command has been added, and we've got two new things, little flags up the top here." Just little summaries like this. It really does make a massive difference. It's hard to overstate. So you're m- trying to, uh, like make understanding the why as fast as possible. And

59. [19:44](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1184s)
    I think a third principle here is something you should be thinking about whenever you do human review. Because, because we're not doing like, um... Because our processes now are so sort of streamlined and all-- we're all collaborating around these same skill files, these same steering files. We're all building an environment for our agents to operate in together. You should think of the process that produces your code as just as important as the

60. [20:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1214s)
    code itself. In other words, when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it. And the theory here is that you never want to write the same comment twice, right? You never want to catch the agent doing the same thing over two PRs. And so what's the mechanism by which you can make your human review matter? Well, this is a new skill. This is called Retro. Retro for retrospective. You essentially take a session that you've done. It can either be like a single,

61. [20:44](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1244s)
    um, agent session, or it can be a PR plus the session, or you can just get it to look at, okay, look at all of the PRs that we've done over the last week, all of the reviews, pull them all in. Let's do a retrospective on them. And it will suggest automated checks and coding standards to make the next one better. So this is the compounding effect, where you essentially by doing human review, you're making the quality of the next human review higher, and you're sort of saving less work from yourself next time. And

62. [21:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1274s)
    Retro is a really smart skill. It adds a bunch of stuff. So obviously it suggests automated checks. It suggests updates to codingstandards.md. It does other smart stuff too. So it looks at navigation pointers. How easily did the agent find its information? Can we provide a pointer inside agents.md to help it out next time? It looks at tool economy. Are there different tools that we're using in the session that can, you know, could be made more token efficient? It's amazing how many things this catches actually, 'cause those are often really

63. [21:44](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1304s)
    hard to debug from the outside. It just looks at bloat as well. So are there bloated steering files? Are there bloated skills that contribute to these bad results? Can we make them more organized? So that's the goal, is to make human review faster. We do that by layering up automated checks. We're layering up automated review, and we make the human review as painless, as simple, and as kind of optional as we need it to. You really don't need to review every single two-way door. Every

64. [22:14](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1334s)
    single one-way door you do. So these are my skills. aihero.dev/skills. I'm gonna be shipping version one point three this week. It has been glorious hanging out with you. It's been a really nice conference. I'm gonna be outside in the lobby if anyone wants to have a chat. Uh, thank you so much for having me. Thank you, Paris.


