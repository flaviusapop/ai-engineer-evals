A GPU optimization is a hypothesis about a particular workload and machine, not a transferable speedup. First identify where wall-clock time and memory go; then choose a transformation, verify it on the target stack and measure both isolated and combined effects. [[performance-and-kernel-verification]] covers the separate correctness and integrity gates.

## Profile before choosing a kernel

Distinguish compute saturation from memory movement, launch overhead and dependency waits. A low-FLOP operation can still cost time if it is invoked repeatedly or launches many small kernels: the normalization example in one talk illustrates this, but its invocation count depends on the model. Inspect CPU hot paths too. In one vendor case, a tensor-merge path involving repeated immutable-map copies accounted for a reported 8.8% of sampled CPU in one service and period; that sample is not a fleet-wide savings estimate. [cite:vrDvatGtIxs:c03] [cite:c1hGBoWw20A:c01] [cite:CgsWxRUY5Eo:c03]

Try a compiler baseline before paying the development cost of a custom kernel. One speaker reports a newer compiler outperforming handwritten normalization in displayed comparisons, but exact compiler versions, hardware and code are unavailable. Treat that as a reason to measure, not a rule that custom kernels are obsolete. Give an optimizer accurate device-generation and interconnect capabilities, and inspect the model's actual architecture: experience can transfer, while an existing kernel may not. Benchmark on deployment hardware at relevant shapes, precision and workload ranges, with a communication-aware baseline for multi-GPU paths. A local open implementation makes this test possible, not automatically successful. [cite:uIiA6DquRiE:c12] [cite:vrDvatGtIxs:c04] [cite:AVMr9PMINyo:c04] [cite:7BcQdtRA3Tc:c03] [cite:pOvWgX7IJsc:c01]

A specialized kernel can win for some context lengths and lose elsewhere. Measure each regime and dispatch to a validated fallback where necessary; the source's example range is not a portable threshold. Re-measure the combined stack because improvements may interact and eventually meet hardware limits. One vendor reports roughly 25% improvement from bare-metal changes and a threefold combined gain with kernels, without controlled attribution or a complete workload and stability protocol. Neither is a guaranteed kernel-only speedup. [cite:vrDvatGtIxs:c08] [cite:vrDvatGtIxs:c09] [cite:vrDvatGtIxs:c10]

## Memory movement and recomputation are different levers

Fusion and cache reuse reduce intermediate transfers or repeated loads; a row-wise fused loss can avoid materializing the full logits tensor, with savings dependent on dimensions and context. Gradient checkpointing instead retains selected activations and recomputes omitted intermediates during training. It can lower memory at the cost of extra work and longer runtime. One speaker reports roughly 70% memory reduction and 10–15% slower training in an example; neither number is a general bound. Measure memory, runtime and quality for the chosen implementation. [cite:uIiA6DquRiE:c13]

## Three distinct normalization transformations

1. **Offline gain folding:** where the algebra and architecture permit, combine a normalization gain with adjacent weights in a transformed checkpoint, avoiding repeated communication during inference. This is not the same as removing normalization altogether. [cite:c1hGBoWw20A:c02]
2. **Deferred scaling:** rearrange compatible work so matrix multiplication and RMS computation run concurrently, then apply post-scale only after both finish. This needs lower-level scheduling and correct synchronization; algebra alone does not establish a correct or faster implementation. [cite:c1hGBoWw20A:c03]
3. **Conditional elimination:** the speaker proposes dropping a redundant normalization only in a particular two-normalization structure when the relevant scale-invariance argument applies. It is not permission to delete arbitrary layers. The available account omits the exact algebra, full architecture proof and independent equivalence tests. [cite:c1hGBoWw20A:c04]

Test each change and its combination with the actual compiler, quantization and serving stack; reported compatibility is not a versioned support matrix. [cite:c1hGBoWw20A:c08]

## Schedule communication with computation

Multi-GPU performance depends on transfer and synchronization as well as arithmetic. In the NVIDIA-specific discussion, a host-initiated copy engine suits large transfers while conserving compute resources; device-initiated tensor-memory mechanisms can support finer-grained overlap, and register-based instructions can enable in-network reductions at different resource costs. Select for message size, registers, processor availability and topology rather than assuming one mechanism wins everywhere. [cite:pOvWgX7IJsc:c02]

When communication and compute data patterns align, different warps may overlap the work; when their requirements do not align, specialization across processors may be preferable. Both approaches still depend on data readiness and the interconnect. Compare against a baseline that includes communication, not a compute-only ideal. [cite:pOvWgX7IJsc:c03] [cite:pOvWgX7IJsc:c01]

## Overlap training without ignoring stale policies

Long agent rollouts finish at different times. A synchronous trainer waits for stragglers to preserve a fresher policy; an asynchronous design overlaps generation, grading and training, but some trajectories were generated by older policies. The learning recipe must handle that off-policy lag and be checked for stability—no universal safe lag or controlled throughput advantage is established by the cited workshop. [cite:V-EDrhIhHzQ:c10]

One proposed architecture separates environment execution, inference replicas and the trainer behind services, with an orchestrator collecting and batching rollouts. This allows their counts to scale independently and an environment to run as an evaluation without starting a trainer. Large multimodal artifacts and mixture-of-experts router metadata can be moved out of process memory into object or file storage while preserving what is needed to reconstruct training inputs. These are architectural recommendations, not measured savings. [cite:V-EDrhIhHzQ:c11] [cite:V-EDrhIhHzQ:c13]

An anecdotal classifier example used a provisioned sandbox for an agent to compare and train candidates, test, clean up resources and report hosting considerations; classifier metrics were not disclosed. It illustrates bounded experimentation, not proof of model quality. [cite:bdHaOXZOhcM:c07] For request-level latency and service objectives, see [[inference-serving]].
