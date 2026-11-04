A plausible image, a coherent video and a robot that completes one action are not interchangeable evidence of competence. Evaluation must ask what was actually perceived, what changed over time, whether modalities and physical relationships agree, and whether an action can be repeated and recovered when it fails.

## Test the scene, not the familiar category

A model may recognize a chessboard and answer with a standard board's count rather than count the squares actually visible. A narrated partial-board example elicited 32 white squares; it is a selected failure, not an estimate of accuracy, and the source image is unavailable. Construct cases where the familiar prior conflicts with the observed scene, and check the answer against the visible objects and their relationships. [cite:A_I8mw8yfns:c01]

The same distinction matters for policy grounding. A proposed construction-safety application would need to connect a written rule to the particular workers and locations to which it applies; detecting a helmet somewhere in a frame would not establish that each worker required to wear one is compliant. This is a prospective application, not evidence of a deployed safety system or reduced incidents. [cite:A_I8mw8yfns:c09]

## Follow state and narrative over time

Test what changed and what remains true across frames. In one described robot video, models reportedly missed a lifted lid and later stove activation. Questions about the state before and after each event test more than whether the system recognizes a kitchen. The example does not establish the cause of the failure or a general memory error rate. [cite:A_I8mw8yfns:c02]

For generated video, a frame can match the prompt and still fail the intended story. Examine character identity across shots, pacing, plausible movement and event order alongside frame quality. For existing video, timestamped embeddings, OCR and tags can help a reviewer locate a brief anomalous content shift that a whole-video description misses. Reports and comments can point to emerging concerns after publication, but audience reaction is supplementary evidence, not ground truth about abuse or originality; its added benefit and resistance to manipulation were not quantified. [cite:b_PmGocP4rc:c01] [cite:jNE8No-wvok:c03] [cite:jNE8No-wvok:c05]

## Separate physical and audiovisual checks

Attractive visuals need not depict a physically coherent process. Likewise, clear studio-quality sound may be wrong for a distant speaker in a reverberant room. Evaluate geometry, causal sequence and scene-consistent acoustics separately from aesthetic quality. These are qualitative evaluation arguments, not measured physical-model performance. [cite:A_I8mw8yfns:c06] [cite:KLDdXOw6jIc:c06]

A door-slam check illustrates why individual metrics have narrow meanings: locate the closing frame and look for an audio spike at the corresponding time. A spike supports timing alignment, but it does not identify the sound as a door. Nor does it validate continuous lip synchronization; animated mouth movement was an unresolved problem in the described setup, not a universally unsolved task. [cite:b_PmGocP4rc:c09] [cite:b_PmGocP4rc:c10]

## Route edits for authenticity, then gate revisions

Not every image needs enhancement. An already-good food photo can consume compute and become worse if edited; an image showing six pieces alongside a description of eight can invite invented food. Evaluate the routing decision and the resulting edit against the original content and merchant identity, not aesthetic polish alone. The reported system's diversity and trust goals were not measured outcomes, and the source's wing-routing terminology is ambiguous. [cite:31GUkCBD-Uc:c01] [cite:31GUkCBD-Uc:c04]

A reported workflow generates image-specific edits, checks dimensions such as plating, faithfulness and color, and feeds rejection reasons into another attempt. Bound the attempts: publish an enhancement that passes the gate, or leave the image unenhanced when the limit is reached. This exchanges coverage for protection against repeatedly failing edits; the retry limit and acceptance rates were not supplied, and passing an imperfect gate is not proof of no defects. Similarly, a generation agent can use intermediate quality checks to revise output, but the reported move from a fixed pipeline to such agents is not a controlled reliability comparison. [cite:31GUkCBD-Uc:c08] [cite:b_PmGocP4rc:c08]

Visual feedback can also help reconstruct a dense chart: generate a table, plot it, compare against the image and revise. A visually plausible trend is weaker evidence than correct individual values; the described demonstration gives no numerical reconstruction accuracy. [cite:0I07YAuF8xA:c07]

## Measure sustained action and recovery

A compelling robot clip demonstrates that one sequence occurred, not that the system can operate reliably over a shift. Record all attempts, failures, interventions and recoveries; report per-task success separately from sustained operation over the full sequence. Test recovery from physical states not deliberately rehearsed, particularly with deformable objects that can assume many configurations. A vendor describes a robot recovering after pulling over a napkin stack, but this observation is not a held-out recovery benchmark. [cite:Sjfz1TqxzEs:c02] [cite:Sjfz1TqxzEs:c05]

A media demonstration or simulated task is not proof of physical deployment reliability. Even real-site trials must distinguish adaptation at a familiar location from transfer to a new one; see [[protect-holdouts-and-historical-evidence]].

## Validate bootstrapped vision labels independently

A prototype workflow uses a vision-language model to propose labels, separate vision models to review them, and the accepted examples to train a smaller detector. Agreement among those models can still share errors, so compare predictions with held-out human labels where available. In the reported road-sign experiment, existing annotations allowed such a comparison, though the metric configuration and complete numerical comparison were not supplied. In document parsing, an illustrative detector found a signature missed by its teacher, but the presenter lacked equivalent ground truth; one recovered signature does not establish an unseen-document generalization rate. [cite:dKcTBQzR7jI:c01] [cite:dKcTBQzR7jI:c04] [cite:dKcTBQzR7jI:c05]
