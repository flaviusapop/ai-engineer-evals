A visual agent needs more than the ability to name what appears on a screen. It must take in the right evidence, connect it to the user’s task, reason about details and changes, and act through an interface available on the particular platform. Each step can fail independently.

## Condition on reference media when words underspecify targets

A user may recognize a desired speaking rhythm or visual style without being able to describe it precisely. An example clip or image gives the model another conditioning channel: the request can say what to do while the reference conveys qualities that are difficult to specify in words. This is an input expressing the target, not a gold answer proving the output is correct. One vendor panel proposed this use for sound, prosody and visual aesthetics; its members disagreed on whether the apparent limitation of language is fundamental or could be addressed by better data and focused development. The account does not establish a general ceiling on text instructions. [cite:KLDdXOw6jIc:c05]

## Combine partial interface observations and inspect changes

A screenshot shows rendered pixels, including visual content that may not appear in a DOM or accessibility tree. But it only shows the captured viewport; a structural representation may reveal elements below it or provide roles and labels that pixels alone leave ambiguous. Accessibility information can also omit visible elements. Choose channels according to the task and cross-check when the distinction matters, rather than assuming any one is complete. A described browser demonstration included an advertisement whose image carried information absent from the DOM; the examples do not quantify overall channel coverage. [cite:Cc0_nyxROBA:c03] [cite:tyFPqtyOK5w:c01]

Grounding means determining which visible or structural element actually serves the intended purpose, not merely finding a button with matching text. In the browser example, an early trajectory followed a sponsored submit button away from the intended expense workflow; later behavior distinguished it. These are selected trajectories, not a measured reliability improvement. After an action, compare the new observation with the intended change: a click arriving at a target is not evidence that the correct operation happened. Capturing a screenshot after each step provides observations, but the agent still has to interpret them. [cite:Cc0_nyxROBA:c03] [cite:Cc0_nyxROBA:c09]

A reported alternative architecture pairs a general reasoning model with a smaller screen recognizer, sometimes fine-tuned for that role. This makes grounding a separable component to investigate; the reported combined harness does not isolate how much the specialized recognizer contributed. Likewise, a workshop’s screen-understanding proposal should not be reconstructed from unavailable visuals or treated as a validated production capability. [cite:tyFPqtyOK5w:c02] [cite:ZGzthw4BZiA:c02]

## Distinguish recognition from visual reasoning

Recognizing a familiar scene is different from inspecting the particular arrangement needed for a count or localization. In a narrated failure, a model reportedly supplied the standard white-square count for a complete chessboard when shown only part of one. The source image and full protocol are unavailable, so this is a selected failure illustrating a possible shortcut, not an accuracy estimate. [cite:A_I8mw8yfns:c01]

For a detail-intensive task, evaluate intermediate decisions as well as the final answer. A narrated example counts red hotels by locating candidate hotels, filtering them by color, then counting the remainder. A wrong result can arise at localization, attribute filtering or counting; inspecting the stages makes the next investigation more specific. The example does not establish general superiority over text-based reasoning. To scope a task, the speaker suggests asking whether a human could answer after viewing the image for roughly one second: a quick recognition question may need less inspection than counting a detailed arrangement. This is a qualitative heuristic, not a formal definition of reasoning or a permanent model limit. [cite:A_I8mw8yfns:c03] [cite:A_I8mw8yfns:c07]

A visually plausible sequence also need not maintain the correct state over time or obey physical constraints. One narrated robot example described missed changes to a lid and a stove; it does not establish the cause of the error. For physical designs, programmatic checks or simulation were proposed to test specified constraints, but simulator fidelity and real-world transfer were not evaluated. Treat those as additional tests under modeled conditions, not as proof of safety or manufacturability. [cite:A_I8mw8yfns:c02] [cite:A_I8mw8yfns:c10]

## Check coherence between modalities

Good audio and good-looking video can still disagree: visible lip motion and speech are observations of the same event and must line up. Assess their timing and correspondence together, not only each stream in isolation. A vendor panel described joint audiovisual modeling as an approach to that coupling, but supplied no controlled comparison against staged generation. It is a design proposal, not evidence that joint generation always wins. [cite:KLDdXOw6jIc:c04]

## Bound background action by platform

Perceiving an interface and controlling it in the background are separate capabilities. One desktop driver reportedly attempts an accessibility action first and falls back to a pixel click when necessary. Test both routes on the actual application and operating system: accessibility support differs, undocumented APIs were mentioned, and equivalent behavior across desktop platforms was not established. [cite:ZSQb5fzRFPw:c01]

Do not infer phone GUI control from desktop results. In an exploratory answer, the same team described Android background containerized workloads and activity-framework tool use as closer to tool use than control of the visible GUI; it did not demonstrate unrestricted mobile automation or establish an iOS capability. [cite:ZSQb5fzRFPw:c13]

For simulated interaction settings, see [[build-and-validate-simulated-agent-worlds]].