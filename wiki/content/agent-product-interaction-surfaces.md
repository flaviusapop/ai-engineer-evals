An agent can act through a desktop, share a view with a person, manipulate application state or answer through a structured interface. These are product interaction choices: they determine what the person can see and do while the agent works. They are distinct from the executable interface contract and the permissions that govern actions.

## Choose an execution desktop without blocking the user

A computer-use agent that takes over the mouse and keyboard can leave the person unable to work on the same desktop. If concurrent work matters, consider a separate execution desktop that the user can inspect or return to. One team moved toward separately hosted desktops after users complained about foreground contention. This is a usability response to those complaints, not a measured productivity gain or a requirement to use cloud hosting. A separate device is also not, by itself, proof of security isolation. [cite:tyFPqtyOK5w:c11] For security controls, see [[agent-authority-isolation-and-runtime-controls]].

## Elicit intent and ground it in shared visible context

The application can ask for missing intent at the moment of interaction, when the user's immediate purpose is available. Carry the clarification into generation and checking rather than expecting general model training to supply this particular context. This is an architectural argument, not a controlled comparison. [cite:sDMGWK4wZ_w:c05]

Shared visible context can make that conversation more precise. In an early design-oriented demonstration, a user could identify a heading spatially and associate feedback about its styling with the target, rather than reconstructing the page entirely in prose. The proposed benefit is less explanation and lost intent, but explanation savings were not measured and the visual demonstration is only partly accessible. [cite:2JX6JYyQG4Y:c03]

Distinguish this annotated, turn-based interaction from the aspiration of an agent that reacts while a person continues working. The latter has a different timing objective from submitting a batch request and waiting; the source did not demonstrate a complete real-time collaborator or establish its latency. [cite:2JX6JYyQG4Y:c06]

## Let agents interact with application state

Not every interaction has to be a visual click. A product can expose structured access to the state the user is already viewing, allowing an agent to read current data or change a setting in the application. In one reported implementation, a frontend-bound programming surface in a web worker used two-way browser-state binding; the agent could change a time range and read application data. The product consequence is that both participants can work with the same state rather than requiring every operation to be reconstructed visually. The account did not provide a reproducible task or measured reliability. [cite:dAoOYFx7ZYw:c06]

This product-facing state-sharing choice is not itself an execution protocol or permission grant. See [[tool-interfaces]] for executable interfaces and [[agent-authority-isolation-and-runtime-controls]] for enforcement.

## Show useful progress while structured components arrive

Time to first readable output and total answer latency are different. A single-client case initially waited for a complete validated structured answer before rendering anything; the reported median answer time was roughly 38 seconds in that pipeline. The team changed the experience to stream readable Markdown and append a structured source card after the answer. A person could start reading sooner while the later card preserved a clickable structured component. [cite:gonAewBZxfU:c10]

This reduces blank waiting in the reported design; it does not establish faster retrieval or a shorter total answer. Nor does the initial complete-object constraint prove that partial structured streaming is impossible in other designs. The latency figure is a speaker-reported case metric, not a general estimate.

## Separate domain expertise from presentation control

In a shopping agent, a merchant may know how user constraints map to its own catalog metadata. That knowledge need not give each merchant control over how options from different merchants are presented. One team retained response-format decisions with the agent to support a consistent cross-merchant experience while using merchant knowledge for mapping. This is a product-specific authority choice, not proof of fair comparisons or a universal commerce standard. [cite:AhQpRalYlyg:c11] Broader preference evaluation is covered in [[preference-discovery-and-recommendations]].

## Evaluate discovery, onboarding and use separately

An agent may recommend a product to a person, discover it as a potential tool, onboard to it and then use it directly. Test these as distinct stages: being recommended does not establish that setup will succeed; being usable does not establish that an agent will find or recommend it. The proposed framing is an advocacy framework, not evidence that agents always make purchasing decisions. A speaker also argues that multiple sales interactions can obstruct onboarding; no controlled onboarding experiment was presented. [cite:Lrw0jqBNaw0:c01] [cite:Lrw0jqBNaw0:c07]

Use observed questions and traces to locate friction. A documentation search endpoint can return relevant chunks while recording agent queries; those queries are leads about missing documentation, not proof of the user's intent. In another case an agent recovered from a parameter mismatch using the error message but spent a turn doing so. Route patterns to product and engineering, while treating specific interface repair as the responsibility of [[tool-interfaces]]. A proposed content campaign would test whether clearer use-case messaging changes search-based recommendations; no causal lift was reported. [cite:vNCY9kXXyDQ:c04] [cite:Lrw0jqBNaw0:c03] [cite:Lrw0jqBNaw0:c05] [cite:Lrw0jqBNaw0:c08]

Simplification can itself trade off against discovery. One team replaced a visible worktree selector with a slash command, reducing maintenance and allowing mid-chat switches but making the feature harder to find; feedback was mixed. The team accepted that tradeoff for a power-user feature, not as a general rule to hide advanced functionality. [cite:WE_Gnowy3uw:c07]
