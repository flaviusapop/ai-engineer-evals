# 200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI

Source: https://www.youtube.com/watch?v=AN65uc645mE

Uploaded: 2026-08-19

Transcript source: first-party AI Engineer publisher transcript JSON (https://assets.ai.engineer/sites/aiecode2025/knowledge-corpus/objects/sha256/33/33acee02493f7dedee20c3c4a1b9442724842c57e37ae1511beefeb7c3d0ec29.json). Transcript text is preserved; transcription errors may remain. Segment timestamps are retained in publisher-transcripts-4/AN65uc645mE.json.

## Transcript

[on-hold music] Hope everyone's having a great conference. Super excited to get started.

Uh, how many of you all, just quick show of hands, have ever gotten a proactive healthcare call from your provider?

Looks like no one. Me neither. Uh, I'm, uh, Vivek... Oh, a few hands over there. Uh, I'm Vivek. I run AI engineering at Hippocratic. Uh, we've built a product that calls patients and can have clinical conversations, uh, and we're over two hundred million conversations in at this point.

Uh, here's the reality of, like, healthcare. Uh, across all of human history, the entire system has been built on scarcity, right? Not enough clinicians, not enough time, not enough money, and hence the word triage.

We're always trying to fig-figure out who amongst us is the sickest and deserves to get care and attention.

As an engineer, I like to think about the math, and for most of human history, the math has just never been in our favor, until now. We're finally at the point where we've seen enough of technology progress, and we also have AI systems that can do clinically safe conversations, and the cost for these conversations continues to drop.

So the math now flips. We can stop rationing, and you don't have to have calls just for the sickest five percent, but you can call everyone. So that's the mission.

We're trying to build clinically safe abundance for all, and it's not about replacing clinicians. In fact, what we're trying to do is help clinicians reach everyone that they couldn't do before because there was simply not enough of them to do this work.

So how are we doing this? Um, our product and our company is predicated on three things. First, do no harm. Next, patient first, and access for all.

Um, and here's a cool thing. Uh, this is plastered across our walls in our company, uh, but it's not just a poster. Uh, this is an oath every employee in the company takes.

I did, too, on, on my first day. Uh, and we build our product, uh, based on this oath. Um, and this is working at scale. Uh, at this point, we've had two hundred million clinical interactions.

We've had zero significant safety incidents. We're deployed in over sixty-plus health systems and have an eight-point-five on ten patient satisfaction rating. Now, uh, I could put an architecture diagram and explain how all of this works, and don't worry, we'll do that.

But before we get there, uh, I want to show you the product in action. So we'll have one of our agents interact with the patient so that you get a feel for what we're up to. [instrumental music]

I'm your AI care manager. I'm calling to check in on how you're doing with your health monitoring devices. Do you have time to chat now?

I, I need to know if I'm talking to a human being or a, a, some kind of computer. You sound like either one.

I understand your concern, Mr. [beep]. I'm an AI, which stands for artificial intelligence.

Okay.

How are you doing today? [laughs]

Well, I was tired earlier, but I'm somewhat revived and incredibly amused.

Delivering at this level of care required building clinical capabilities you won't find anywhere else. On the safety side, accurate drug name recognition.

Could you tell me the name of the medication you're currently on?

Prazosin, and there's one other, but I don't remember the name.

Could you help me out by spelling the name of this medication?

P-R-O-Z-I-N, I guess.

It seems like you might be talking about Prazosin. Does that sound-

Yeah.

Vital sign clarification.

Then I took it again, and it was a hundred and twenty-one over forty-five, ninety-one.

Just to confirm, your blood pressure is one hundred twenty-one over forty-five, and your heart rate is ninety-one, right?

Right.

Med stoppage detection.

What about the Nifedipine tablet? Were you able to stop taking that one as instructed?

Well, I took it this morning. Well, no, I took it last night because I didn't have the other prescription, and I don't think that would keep my blood pressure down.

I understand your concern about your blood pressure, and it's great that you're thinking ahead. I would recommend that you do talk to your primary care doctor about the Nifedipine and get their guidance on what to do.

And real-time nurse escalation when clinically necessary.

How are you feeling?

Okay. Just a little tired and weak.

It's quite common to feel this way after being in the hospital. Could you tell me more about it?

My legs feel weak when I walk.

Got it. Along with the weakness in your legs, have you noticed any chest discomfort or difficulty breathing?

I just was, was, was having shortness of breath for a while.

I'm so sorry to hear that you're experiencing shortness of breath. Given your symptoms, it would be best to have a nurse speak with you immediately.

Yeah, so that's a sneak peek into our product, and so we'll get into why this is hard and why a generic stack doesn't work for us. Okay, so if I were to strip out all of the complexity around the audio and speaking back, it boils down to two things, intelligence and latency, right?

On the top left, you see some of our ever-evolving smart, intelligent models, and these models are fantastic at what they do. They're clinically safe. But unfortunately, many of these models take tens of seconds to respond, sometimes over a minute, and that's completely useless when we're trying to have a two-way conversation on a telephone.

On the bottom right, we have models that are fantastic. They are really fast, but then they're just not at the same level of clinical accuracy for us to have a safe conversation.

When we started building out this product, where we wanted to be was on the top right corner, and in order to accomplish this, what we had to do was build a vertically integrated stack ground up, bit by bit, optimizing every part of the sto- stack.

When we started out building our own models, we also had several seconds of like latency, but hundreds of optimizations later, where we landed at was a product that is insanely fast but also doesn't lose its intelligence.

And we continue to benchmark all of this consistently. All of these results are on our website and more. Um, and there's three typical ways in which folks build, uh, voice systems.

One, you could use an ensemble o-of models, or you use cascaded models or use speech-to-speech real-time models. Again, all of these models and architectures are great at different things.

As an example, let me take two specific benchmarks amongst the many hundreds that are critical for our workflows: uh, lab results check and IVR navigation. Now, these are things that you don't typically hear about or see in the most common benchmarks, and most of the generic models out there don't perform well at those.

And we needed our models and our product to be over ninety-nine percent accuracy on those specific benchmarks, amongst other things. Uh, and one-- that's one of the key reasons why we continued on investing our own stack.

And latency is key to this entire system. So every time we work on an optimization, we buy back some latency, and we just don't bank that latency. We use that extra gap now to pack more intelligence into the overall system such that we can have a more reliable conversation with the patient.

Um, and when we do that, we go back, work on more optimization, and that flywheel compounds. So what seems like a tug-of-war between latency and intelligence for us is a compounding flywheel.

So what does this entire machine look like? Uh, this is Polaris. This is our constellation architecture. Left to right, you have the system that hears. The middle is the brain that reasons.

The right is the system that talks back, and all of this round trip needs to be really fast. So on the left-hand side, what you're seeing are a collection of models, uh, that are used for speech detection, so everything from bilingual switching to background noise detection, um, to contextual understanding of the conversation.

The brain isn't a singular model. We, in fact, run thirty-one models at any given point of time for every conversation. So we have one central model that's handling, handling the conversation, where we have other thirty specialist models, everything from labs to medications to scheduling, uh, that are feeding input into this model.

And then finally, on the output side, we have a custom personality, voice, HD quality, and clinical documentation engine that makes sure the patient gets back all of the right information and all of the same information flows back into the health system.

W-- The reason we have the system is because we see a singular model being as, like, one point of failure, and that's just unacceptable for a patient conversation. Uh, this architecture gives us the redundancy and safety that we otherwise couldn't get to.

And the patient never can tell the difference. It's pretty seamless from their perspective. Let me double-click into some of these systems for you.

Uh, first, we'll talk about our, uh, ASR system.

So the real world, as all of us know, is fairly loud and noisy. Uh, but most of the audio benchmarks get recorded in a quiet room. And something we learned the hard way was most of what looks like model reasoning failures end up actually being model mishearing things, right?

So the Spanish sí or yes gets transcribed as the alphabet C, or you could have an Arabic drug name that gets over thirty percent inacc-inaccuracy in terms of, like, word error rate.

So we had to build a system to co-- to combat all of these challenges. A typical speech-to-text system just takes in the audio and then outputs some text. So ours is a decoder-only, um, audio LLM system.

So we take in the audio, but in addition to that, we're giving it two additional pieces of data. One is the context around the conversation thus far, and second, it's the domain knowledge around that entire conversation, and that is sort of like the trick that makes this work for us.

So under the hood, what's happening? So we have-- First, we have a encoder, which is the ear. Uh, so we took an open source Whisper large-v3-turbo model and fine-tuned that on millions of clinical conversations, uh, to get to the accuracy we need.

Next, we have a con-conformer projector. What this does is takes the audio and compacts it and projects it into tokens that the language model would und-understand. But the key over here is it also maintains all the prosody.

So all the pauses and the stresses are maintained. So the model hears not just the what, but also the how. Next, we're passing in the context around, let's say, the medications this pa-patient's taking in or the task at hand.

Are we trying to fill in a form? Uh, what kind of, like, details that need to go in there and the policy? And how this helps is, now, when a patient mentions a medication name, we aren't guessing from like an infinite list of medications, but we have the chance to optimize around a finite list, and that helps

it getting the word error rate down. Next, we also have contextual biasing as a part of, like, the training. So during the training process, uh, we have millions of these synthetic patients with their addresses, phone numbers, uh, and other details, uh, that are fed into the training process.

So as a concrete example, let's say someone mentions their address on a conversation as [REDACTED:location_address]. Now, that specific utterance is ripe for phonetic garbage for most ASR systems.

But given we're feeding that as additional context to the audio LLM, we have a high degree of accuracy and are able to get to the right transcription, which then feeds into the brain accurately.

Further, what we see is for most clinical conversations, many of the patient responses are mono- mono words, right? Uh, and those often get transcribed incorrectly. A now becomes a no, or a five becomes a fine.

And in a patient conversation, that's catastrophic. So what we do is a secondary round of sca- scoring, specifically when we see a patient has said only a singular word.

And again, we use the context of the entire conversation to do this. So all of these like help us bring down the medical word error rate by over, uh, fifty percent, um, from what we see as standard off-the-shelf models.

In addition to that, uh, the specific system we've built allows us to, uh, check in the latency, and at a P99, it's three X faster than every other system out there.

Next, let's look into the constellation, uh, the brain. So as I said, we have thirty-one models live running in, uh, at any given point of time. So how do we do this without falling apart on latency?

Uh, the answer is a bit counterintuitive. We actually run every single one of these models in parallel. Uh, but the trick over here is, uh, every single model does a really quick check, uh, to see if they even need to say something on this conversation, right?

So every specialist first decides, "Hey, do I need to speak?" If not, it's a short circuit, and that's what helps us keep, uh, in the budget. So that's the synchronous part.

In addition to that, we also have asynchronous run-- models running in the background that are doing verification. And let's take two specific examples to walk through, uh, how we use these models.

Again, going back to our medication example. For example, if the patient talks about ibuprofen or is talking about another medication, that's when the med engine specialist will kick in and it will say, "Oh, I have something to say over here, main model."

We'll pass in that context to the main model. The main model with along, along with everything else that already knows around the goal and the conversation, will take this input from the specialist and steer the conversation as appropriate.

Next, uh, like many other agentic systems, we heavily use like tool calls, and I think pretty much every one of us has experienced tool calls have, uh, innumerable failure modes.

Um, so we have these like verifiers in the background that are running to make sure all the parameters into the tool calls and the responses and the tool calls are accurate.

Uh, and for use cases like scheduling, this is what's gotten us to get to a three nines, four nines accuracy. And finally, for certain use cases, we're also running these verifiers offline where possible.

Um, so again, going back to scheduling, sometimes we have the luxury of time to go back and check to make sure, uh, if there was an inaccurate appointment, we can course correct that on the back end or call a patient back and apologize.

Um, all of these changes would be meaningless if we didn't optimize our, uh, inference stack. Uh, and we have a fantastic research and engineering team that lives and breathes on this problem.

Uh, and for inference itself, quality is our constraint and speed is our work, so we can never compromise on the quality of the output. Every speed optimization has to be, uh, lossless.

We've worked on like many, many of these like optimizations. Let me talk you through three specific ones, uh, that we found to be the most meaningful. Uh, one is four-bit quantization.

Uh, so basically what we've done is we've shrunk down the math for, uh, model computation to be from sixteen-bit to four-bit. Again, lossless, and this has like really, uh, helped us with overall latency.

The next is speculative decoding. So we have a smaller model that's generating the tokens ahead of time, and then the main model just checks this in one go, and this also has greatly improved latency for us.

Finally, a KV cache compression system. So, uh, as these conversations get like really long in length, uh, we've figured out a way to keep a large chunk of these conversations warm on cache, giving us an over ninety-six percent hit rate, uh, and then also helps us with the prefill portion, uh, which goes eighteen times faster.

So this style of across the board, board optimizations is what's, uh, getting us ahead, uh, during the product development phase. Now, evals are obviously key, as we've seen across many of these, uh, talks.

Um, so some quick math, right? Uh, for example, let's take the scheduling use case again. Um, with over ten thousand calls a day, uh, a one, one percent failure rate like sounds all right.

Most agentic systems would claim eighty percent, ninety percent accuracy, uh, and that's great for them. For us, even the ninety-nine percent is pretty bad, uh, because one percent error means a hundred people a day are gonna get the wrong appointment type.

Uh, and it's physically bad because they'll show up on the wrong date, wrong time. But worse off, they could actually be missing a critical, uh, appointment, and that's unacceptable from our standpoint.

Uh, so it's not just an annoyance, right? Um, and the challenge over here is in order to catch this, like statistically the math like is like incredibly challenging, right?

You need about four hundred and fifty tests to be ninety-nine percent sure that you can catch this like one percent error rate, uh, and nineteen hundred tests to be able to see that you've caught it like ten times.

Um, so you can't purely rely on synthetic data from our experience to be able to get to the scale of a-accuracy. Uh, so we use a combination of human beings and synthetic data.

So we have over seven thousand trained clinicians on our platform who are continuously helping us like evaluate our platform. Uh, they've done over, uh, seven hundred thousand, close to eight hundred thousand clinical conversations to help us figure out the accuracy of our system, and we do this on a continuous basis.

Finally, uh, coming, uh, to safety. Um, uh, we've shipped five versions of our product, uh, thus far, and each one's gotten better, um, compared to the previous one. So we don't just grade the output of our models on the correctness or validity of it.

So we use the same scale that-- as they do for human beings. So they're graded across correctness, no harm, minor harm, severe harm, and death. And across five generations, where we're at with our Polaris system is a ninety-nine point eight nine percent, uh, accuracy, uh, with respect to like no harm.

And humans on the same rubric are at about eighty-one percent. It's not because, like, we're terrible, but, uh, AI systems don't get tired, and unfortunately we do. And we also don't have the luxury of having thirty-plus supervisors helping us at any, any given point of time.

And finally, safe is not enough, right? A key part of the product is the empathy for human beings to open up to AI systems. We needed to make sure, uh, the voice and how we actually lead these conversations are empathetic.

And, uh, as with most other things during our product journey, we found that there weren't actually accurate or good benchmarks to measure the empathy of these systems. So we actually built one, what's called HEART.

Uh, the paper for this is public. Uh, so encourage you guys to, like, read it. Uh, and, uh, we, we had to make sure the end system was not just safe, but also empathetic so that people would actually prefer it and use it.

And finally, uh, all of this, like, comes down to the people. Uh, we wouldn't be here if we didn't invest in, uh, people from an AI native perspective. Uh, everything in our company across the last couple of years, uh, has been transformed, uh, our hiring processes to how we use, like, tokens.

We still have unlimited tokens for everyone at our company. We also have two great programs for anyone who comes into, uh, um, Hippocratic. For early career engineers, we have an agent deployment residency program where they're trained to write some of the best, like, healthcare safest agents.

And then for experienced software engineers, we have an AI residency program where we help you start, like, training models, uh, and build the next great system along with us.

So yeah, we're told you gotta pick, uh, two of these options aro-around quality, speed, and safety. We didn't, and we decided to go with all of them, and we're hoping, uh, the rest of us would come and build with us.

Thank you. [audience applauding] [upbeat music]
