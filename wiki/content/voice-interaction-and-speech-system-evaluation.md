A voice agent can sound natural, repeat a reassuring confirmation and still perform the wrong action. Evaluate the interaction at two levels: whether the user and system successfully completed the task, and which speech, language, timing or tool component caused a failure. Neither a fluent recording nor a strong isolated component score establishes the outcome. [cite:qStB9GbppMU:c01] [cite:IDNfAZVKvPE:c06]

## Verify outcomes, not just fluency

Check both the conversation and the external state: Was the requested action authorized? Were the right arguments sent? Did the intended booking or refund actually appear in the relevant system? Score helpfulness and tone separately from domain rules such as eligibility. Track task failure, escalation, abandonment and silent errors alongside conversational quality; these are useful outcomes to investigate, not proof that a particular speech defect caused a business change. [cite:ZdheJTfLu-s:c03] [cite:IDNfAZVKvPE:c09]

In a deliberately generated refund call, the customer asks about order 14 but the system processes order 40 despite a spoken confirmation. The useful test compares the audio, recognized order, tool arguments and resulting state—not just whether the final sentence sounds correct. This is a synthetic illustration, not a documented customer incident or a measured failure rate. [cite:42Bz0TUfeOQ:c05] [cite:42Bz0TUfeOQ:c01]

## Localize errors across the voice stack

Align the audio, transcript, timing and tool trace. Ask what the caller actually said, what recognition supplied to the language model, what the model decided, and what was spoken or executed. An appointment example changes the third to the thirtieth at recognition, so a downstream model can confidently book the wrong day. Conversely, a correct transcript can still produce a generated note with additions or omissions. Diagnose the boundary before changing the wrong component; these examples do not quantify the relative frequency of each failure. [cite:j4AmIK6OvHc:c01] [cite:yqF6XhzbWBk:c02]

A useful diagnostic framework crosses **listening and speaking** with sounds, words, interaction and the participants' understanding. For example, confusing spelled M and N is a listening error; pronouncing the corrected name badly is a separate speaking error. Both can affect the same task. The framework is conceptual, not a validated universal scoring scheme. [cite:IDNfAZVKvPE:c02] [cite:IDNfAZVKvPE:c03]

Build component tests for consequential fields—names, phone digits, dates, addresses and domain terms—under the noise, accents, language switching and devices representative of deployment. A field test can quickly localize a broken collection step, but passing fields does not prove the whole conversation works. In one speaker's reported diarization benchmarks, telephone conditions were around 8% error and a noisy multiperson setting around 41%; those figures describe those settings, not universal bounds. [cite:vblnYHzBgS4:c03] [cite:vblnYHzBgS4:c08] [cite:mFLlVpnGpds:c06]

## Test turn-taking and repair

Include pauses *within* an identifier, interruptions, short acknowledgments, changed requests and multiple turns of misunderstanding. In an account-number anecdote, the user paused while reading an unfamiliar sequence; the bot interrupted, reported no record and asked again. The component and timing threshold were not instrumented. Evaluate whether the system recognizes uncertainty, clarifies the missing part and retains earlier corrections rather than simply restarting the exchange. Clarification is proposed guidance, not a demonstrated comparative recovery rate. [cite:IDNfAZVKvPE:c04] [cite:IDNfAZVKvPE:c05]

Preserve speaker and word timing so an interruption can be distinguished from a brief backchannel. Prosody, stress and acoustic context may carry useful information, but are not certain labels of emotion or intent. A hotel demonstration included an interruption and changed dates; parts were sped up, so it illustrates interaction behavior rather than measured response latency. Also test whether a safety warning resumes after an interruption or a backchannel; reported hazards lack incidence estimates. [cite:mFLlVpnGpds:c01] [cite:mFLlVpnGpds:c02] [cite:j4AmIK6OvHc:c05] [cite:McknwOzbmyg:c12]

Compare premature cutoffs **at the same latency budget**, since waiting longer can reduce interruption at the cost of slower response. A vendor reported 9.9% versus 4.5% cutoffs at matched latency for an alternative and its audio-based turn detector; dataset size, uncertainty, baseline identity and the exact latency were not supplied. The comparison motivates a matched test, not a general performance ranking. [cite:j4AmIK6OvHc:c06]

## Combine listening, simulation and live tests

Listen to real calls to discover unexpected conversational failures, then encode recurring issues in rubrics and field checks for broader coverage. Use controllable simulated calls to reproduce a pause, correction or interruption, including risky cases that should not be induced with real users. Neither automated scoring nor simulation alone proves the system works for real people. When the hypothesis depends on genuine reaction—such as the effect of an outbound opening or vocal delivery—consider a suitably governed live comparison. The cited opening guidance is practitioner advice, not a controlled study. [cite:qStB9GbppMU:c04] [cite:qStB9GbppMU:c08]

## Score diarization and the word-to-speaker join separately

Diarization asks **who spoke when**. Compare predicted speaker timelines with a human-labeled reference and break diarization error rate into speaker confusion, false-alarm speech and missed reference speech, divided by total reference speech duration. A missed second speaker during overlap counts as missed speech even if the first speaker was detected. Inspect the timelines as well as the aggregate: a selected 30-second telephone clip showed approximately 5% versus 3% DER for two displayed systems, but cannot establish general superiority. [cite:mFLlVpnGpds:c05] [cite:mFLlVpnGpds:c11]

Then test the join between recognized words and speaker times. ASR and diarization timestamps may disagree; one may detect speech the other misses, and overlapping speech may yield only one transcribed word. Examine boundary words and short turns directly. Exclusive diarization selects the speaker most likely represented in the transcript to simplify attribution, but can lose the other overlapping voice; its selection algorithm and full reconciliation process were not disclosed. Choose the representation according to whether the application needs a readable single-speaker transcript or a fuller account of overlap. [cite:mFLlVpnGpds:c08] [cite:mFLlVpnGpds:c09]

## Normalize and test speech output

Before text-to-speech, test a normalization layer for markup, emoji, dates, currency and email addresses, and configure pronunciation for critical names, brands and acronyms. Listen to the actual synthesized output: a correctly recognized name may still be spoken incorrectly, and a generic fluent sample may miss that defect. Targeted dictionaries and slower spelling are practitioner suggestions; verify the result with the chosen provider and relevant users rather than assuming normalization is portable or universally correct. [cite:vblnYHzBgS4:c09] [cite:vblnYHzBgS4:c10] [cite:IDNfAZVKvPE:c03]
