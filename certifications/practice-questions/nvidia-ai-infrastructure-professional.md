---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - AI Infrastructure (NCP-AII) - Practice Questions

15 questions for NCP-AII prep, evenly weighted across DGX and GPU hardware, cluster design and networking, Kubernetes and GPU orchestration, job scheduling, and performance tuning (20% each).

> **Cert page:** [exams/nvidia/ai-infrastructure-professional/](../nvidia/ai-infrastructure-professional/README.md)

---

### Question 1
**Scenario:** A DGX system's eight GPUs must communicate at full bandwidth for tensor-parallel training.

A. InfiniBand
B. PCIe switching on the node's root complex, which gives every GPU a dedicated x16 link to the CPUs
C. NVLink with NVSwitch giving all-to-all GPU bandwidth within the node
D. Ethernet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVSwitch gives every GPU full-bandwidth access to every other GPU in the chassis, which is what makes intra-node tensor parallelism viable. InfiniBand is the inter-node fabric. PCIe is an order of magnitude slower and would make tensor parallelism a bottleneck rather than a technique.
</details>

---

### Question 2
**Scenario:** A multi-node training cluster is being designed for 64 nodes with 8 GPUs each.

A. A rail-optimized fat-tree InfiniBand fabric with non-blocking bandwidth and one NIC per GPU
B. A single top-of-rack switch
C. Wireless
D. Standard 10 GbE with TCP and a two-tier leaf-spine design oversubscribed 4:1 to save on switch cost

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Collective operations at this scale need non-blocking bisection bandwidth, and rail-optimized designs put each GPU's traffic on its own rail so all-reduce traffic does not contend. A single switch cannot supply the port count, and commodity Ethernet without RDMA leaves the GPUs waiting on the network.
</details>

---

### Question 3
**Scenario:** What does GPUDirect RDMA enable?

A. Display streaming
B. GPU virtualization
C. Direct memory transfer between GPU memory and the network adapter, bypassing host memory
D. Faster local disk access by letting the GPU read NVMe drives directly into its own memory buffers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Removing the host bounce buffer cuts latency and CPU overhead for inter-node GPU communication, which is what makes NCCL collectives scale. GPUDirect Storage is the sibling technology that does the same for NVMe reads into GPU memory.
</details>

---

### Question 4
**Scenario:** RoCE is used instead of InfiniBand. What must be configured for it to perform?

A. A separate VLAN only, with RDMA traffic isolated from management traffic and a dedicated subnet per rack
B. Nothing special
C. Lossless Ethernet with PFC flow control and ECN congestion marking set end to end
D. Jumbo frames only, with a 9000 byte MTU on every switch port and every NIC in the data path

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** RDMA assumes a lossless fabric, so priority flow control and explicit congestion notification must be enabled and tuned on every switch and NIC in the path. A single misconfigured hop causes packet loss that collapses RoCE throughput, which is why RoCE deployments fail in the middle rather than at the edges.
</details>

---

### Question 5
**Scenario:** A Slurm cluster must guarantee that all ranks of a distributed job start together.

A. Preemption
B. First-come-first-served per node as they free up
C. Backfill only
D. Gang scheduling, so the job runs only when all requested nodes are available at once

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A distributed training job with some ranks running and others queued deadlocks at the first collective and burns the allocated GPUs doing nothing. Gang scheduling is the requirement; backfill is a complementary technique for filling gaps with small jobs.
</details>

---

### Question 6
**Scenario:** Storage must feed 512 GPUs reading a large image dataset.

A. Local disk only, copying the dataset to every node before the job starts and again each epoch
B. A parallel filesystem or high-throughput object store sized for aggregate bandwidth
C. A cloud bucket reached over the public internet through a NAT gateway, with every node fetching its own copy of the data
D. A single, well-provisioned NFS server with a large RAM cache and a 100 GbE link to every compute node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GPU clusters starve on storage long before they starve on compute, and aggregate read bandwidth is the number to size against. Node-local NVMe caching for repeated epochs is the standard multiplier. A single NFS head becomes the bottleneck well before this scale.
</details>

---

### Question 7
**Scenario:** MIG is enabled on a node in a Kubernetes cluster. How do workloads request a slice?

A. MIG is not supported in Kubernetes, so MIG mode must be turned off on the node before any pod can use the GPU at all, and pods then request whole GPUs only
B. They request the specific MIG profile resource advertised by the device plugin, such as `nvidia.com/mig-1g.10gb`
C. They request CPU only
D. They request `nvidia.com/gpu` with a limit of 1 and then pick the slice size at runtime with a CUDA environment variable in the container

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In the mixed strategy the device plugin advertises each MIG profile as a distinct resource name, so pods request the slice size they need. The single strategy presents uniform slices as `nvidia.com/gpu` instead. Choosing the strategy is a cluster-level decision that affects every manifest.
</details>

---

### Question 8
**Scenario:** Training throughput is well below the theoretical FLOPS of the hardware.

A. Reduce the model size until the job reaches the hardware's theoretical throughput
B. Profile with Nsight Systems and Nsight Compute to find the actual bottleneck
C. Increase the learning rate and batch size together so each step does more work per kernel launch and utilization rises on every GPU
D. Buy newer GPUs with a higher peak FLOPS rating and rerun the same job without any changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Utilization percentage does not tell you why. Nsight Systems gives the timeline across CPU, GPU, and communication so you can see gaps, and Nsight Compute drills into individual kernels. Optimizing without profiling usually improves the part that was not the bottleneck.
</details>

---

### Question 9
**Scenario:** Mixed precision training is enabled and loss becomes NaN.

A. Use loss scaling (or BF16, which has FP32's exponent range) to prevent gradient underflow
B. Lower the batch size
C. Increase the epochs
D. Disable mixed precision permanently and train in FP32 only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FP16 has limited exponent range, so small gradients underflow to zero and large activations overflow. Dynamic loss scaling shifts gradients into representable range. BF16 avoids the problem by trading mantissa bits for exponent range, which is why it is the default on modern hardware.
</details>

---

### Question 10
**Scenario:** A multi-tenant cluster must prevent one team from monopolizing GPUs.

A. Manual approval for every job by a platform administrator, who checks the requested GPU count against the team's allocation
B. One large namespace
C. Trust the teams to self-limit and let them submit as many GPU jobs as they like, since usage is visible in dashboards
D. Resource quotas per namespace, priority classes, and fair-share limits in the scheduler

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Quotas cap consumption, priority classes decide who is preempted under contention, and scheduler fair-share prevents one account draining the queue over time. Manual approval does not scale and moves the bottleneck to a human.
</details>

---

### Question 11
**Scenario:** NCCL collectives are unexpectedly slow across nodes.

A. Add more nodes so the collective is spread across more links and each GPU handles a smaller share of the traffic
B. Set `NCCL_DEBUG=INFO` to see the chosen transport and any fallback from RDMA to sockets
C. Reduce the model size so that each collective moves fewer gradients across the cluster network
D. Restart the job on the same nodes several times and keep the run that picks the fastest transport

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NCCL logs which transport and rings it chose, and a silent fallback to TCP sockets because RDMA was unavailable is the classic cause of a tenfold slowdown. Environment variables such as `NCCL_IB_HCA` and `NCCL_SOCKET_IFNAME` pin it to the right interfaces.
</details>

---

### Question 12
**Scenario:** Power and cooling must be planned for a rack of DGX systems.

A. Cooling is unnecessary
B. Standard office-grade power with a single circuit per rack
C. Plan per-rack power and cooling capacity against the systems' rated consumption, including redundancy and possibly liquid cooling
D. Buy the racks first and size power and cooling after the systems arrive

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Dense GPU racks reach power and heat densities that ordinary data center rows cannot support, and this constraint often decides the physical layout before anything else does. Facility limits are the reason many deployments end up with partially populated racks.
</details>

---

### Question 13
**Scenario:** A node's GPU fails mid-training in a 64-node run.

A. Continue with 63 nodes and no changes, since data parallel training tolerates a missing worker without any reconfiguration or restart of the remaining ranks
B. Ignore the failed GPU and let the run carry on with the remaining GPUs in the same node
C. Restart the whole run from scratch with the original random seed and the same data order
D. Resume from the latest checkpoint on healthy nodes with the failed node cordoned

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** At this scale hardware failure during a long run is expected rather than exceptional, so checkpoint frequency is a design parameter chosen against mean time between failures. Elastic frameworks can reconfigure the world size and continue, which turns a failure into a pause.
</details>

---

### Question 14
**Scenario:** Which tool manages and monitors an InfiniBand fabric?

A. NVIDIA UFM (Unified Fabric Manager)
B. DCGM, which monitors GPU health but not switches
C. Nsight
D. NGC

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UFM handles subnet management, fabric telemetry, congestion analysis, and cable and port health across the InfiniBand network. DCGM covers the GPUs themselves, so a healthy cluster needs both views.
</details>

---

### Question 15
**Scenario:** Benchmarking should validate a new cluster before handing it to users.

A. Run benchmarks per layer: single-GPU compute, NCCL all-reduce bandwidth, storage throughput, then end to end
B. Run one training job
C. Trust the vendor's acceptance report and published specifications, since the system was already tested at the factory and again by the integrator
D. Check `nvidia-smi` only, since a clean GPU listing, driver version and temperature readings show the fabric and storage also work

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layered benchmarking localizes a shortfall: if single-GPU numbers are right but all-reduce is slow, the fabric is at fault, and if both are right but the end-to-end run is slow, look at storage or the data pipeline. A single end-to-end number tells you something is wrong without telling you where.
</details>

---

## Where to go deeper

- [NCP-AII cert page](../nvidia/ai-infrastructure-professional/README.md) - notes, practice plan, strategy
- [NCA-AIIO practice questions](nvidia-ai-infrastructure-operations-associate.md) - the associate level below this
- [NCP-AIN practice questions](nvidia-ai-networking-professional.md) - the fabric in depth
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - the hardware concepts in plain English
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
