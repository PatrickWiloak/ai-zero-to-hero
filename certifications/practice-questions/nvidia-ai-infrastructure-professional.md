---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA Certified Professional - AI Infrastructure (NCP-AII) - Practice Questions

30 questions for NCP-AII prep, evenly weighted across DGX and GPU hardware, cluster design and networking, Kubernetes and GPU orchestration, job scheduling, and performance tuning (20% each).

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

### Question 16
**Scenario:** A team training a large mixture-of-experts model wants expert-parallel traffic to stay on NVLink across far more than eight GPUs. They are comparing an HGX 8-GPU server with a GB200 NVL72 rack.

A. Either system works the same way, because NVLink always spans every GPU in the data center
B. The NVL72 rack, whose 72 GPUs share one NVLink domain through NVLink switch trays
C. The HGX server, because NVLink cannot connect more than eight GPUs in any NVIDIA system
D. Neither system, because expert parallelism always runs over the InfiniBand fabric

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GB200 NVL72 connects 72 Blackwell GPUs into a single NVLink domain, so communication-heavy parallelism such as expert or tensor parallelism can span the rack without leaving NVLink. An HGX 8-GPU board's NVLink domain ends at the server, beyond which traffic crosses the scale-out network. NVLink does not span a whole data center, and expert parallelism uses whichever interconnect links the ranks.

**Key Concept:** [NVIDIA DGX documentation](https://docs.nvidia.com/dgx/index.html)
</details>

---

### Question 17
**Scenario:** Data loading for a training job is limited by copies from NVMe through a CPU bounce buffer into GPU memory.

A. NVLink Switch, which connects the NVMe drives into the GPUs' NVLink domain
B. Multi-Instance GPU, which splits each GPU so one slice can manage data loading
C. GPUDirect Storage, which gives a direct DMA path between storage and GPU memory
D. GPUDirect RDMA, which moves data between two GPUs in the same server over PCIe

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GPUDirect Storage lets storage, local NVMe or remote, DMA directly into GPU memory, removing the bounce buffer in system memory and reducing CPU load. GPUDirect RDMA covers network adapters reading and writing GPU memory across nodes. NVLink Switch does not attach storage, and MIG partitions compute rather than changing the I/O path.

**Key Concept:** [GPUDirect Storage overview](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html)
</details>

---

### Question 18
**Scenario:** On a new HGX H100 8-GPU system with NVSwitch, CUDA applications fail to initialize, while `nvidia-smi` lists all eight GPUs.

A. Check that the NVIDIA Fabric Manager service is installed, matches the driver, and is running
B. Enable MIG on all eight GPUs, which is required before NVSwitch systems can start CUDA work
C. Reinstall the CUDA toolkit inside the container, because the host driver cannot see NVSwitch
D. Disable NVLink in the BIOS so that the GPUs fall back to PCIe and initialize normally

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** On NVSwitch-based HGX and DGX systems, Fabric Manager configures the NVSwitch memory fabric, and CUDA initialization fails until it is running at a version that matches the driver. GPUs still enumerate without it, which is the symptom described. MIG is optional, the container toolkit does not manage switches, and disabling NVLink gives up the system's main interconnect.

**Key Concept:** [NVIDIA Fabric Manager](https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/index.html)
</details>

---

### Question 19
**Scenario:** A cluster design puts training traffic, storage traffic, node provisioning and BMC access on one shared Ethernet network to save on switches.

A. Accept the design if every port runs at 400 Gb/s, since enough speed removes any need for separation
B. Move only BMC access onto the compute fabric and keep the other three kinds of traffic together
C. Merge everything onto InfiniBand, because a single InfiniBand fabric also serves BMC management
D. Separate the compute fabric, storage network, in-band management and out-of-band management

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NVIDIA's reference architectures keep distinct networks: a dedicated compute (east-west) fabric for collective traffic, a storage network, in-band management for provisioning and services, and out-of-band management for BMCs. Mixing them lets storage or management bursts disturb collectives and puts management access at risk during an outage. Raw speed does not fix interference, and BMCs use Ethernet out-of-band.

**Key Concept:** [DGX SuperPOD documentation](https://docs.nvidia.com/dgx-superpod/index.html)
</details>

---

### Question 20
**Scenario:** An organization wants to grow its DGX deployment in validated, repeatable steps instead of designing each expansion from scratch.

A. Add servers one at a time and redesign the network cabling plan after each new server arrives
B. Build in scalable units from the DGX SuperPOD reference architecture, adding whole units at a time
C. Buy the largest single InfiniBand switch available so that every future server plugs into one box
D. Mix server generations freely in each expansion, since the reference designs ignore GPU models

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The DGX SuperPOD reference architecture is built from scalable units, fixed groups of systems with a defined compute, storage and management network design, so growth means adding validated blocks. Ad hoc single-server growth produces inconsistent topologies. A single giant switch cannot scale indefinitely, and reference designs are specific to system generations.

**Key Concept:** [DGX SuperPOD documentation](https://docs.nvidia.com/dgx-superpod/index.html)
</details>

---

### Question 21
**Scenario:** Budget pressure leads to a proposal to oversubscribe a network 3:1 between leaf and spine. The cluster has a compute fabric for collectives and a separate storage network.

A. Oversubscribe the compute fabric, since collective traffic is light and mostly stays inside a server
B. Oversubscribe both networks equally, since all traffic in an AI cluster has the same pattern
C. Keep the compute fabric non-blocking and accept oversubscription only where its impact is measured
D. Remove the spine layer and connect every leaf directly, which is always non-blocking at any scale

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Large-scale training runs all-reduce and all-to-all collectives across every node at once, so the compute fabric is designed non-blocking; any oversubscription belongs on networks whose demand has been measured, such as some storage or management paths. Collective traffic is heavy and crosses servers. Traffic patterns differ by network, and a flat leaf mesh does not scale.

**Key Concept:** [DGX SuperPOD documentation](https://docs.nvidia.com/dgx-superpod/index.html)
</details>

---

### Question 22
**Scenario:** GPU nodes are built from an OS image with the NVIDIA driver already installed, and the GPU Operator is being added to the Kubernetes cluster.

A. Install the GPU Operator with its driver component disabled, so it manages the rest of the stack
B. Remove the host driver first, because the GPU Operator refuses to start when one is present
C. Install the GPU Operator with defaults, so a second driver container loads beside the host one
D. Skip the GPU Operator and install only the device plugin, since it needs no driver at all

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The GPU Operator can deploy the driver as a container, but when the driver is preinstalled on the host you disable that component and let the operator manage the container toolkit, device plugin, GPU Feature Discovery, DCGM exporter and MIG manager. Removing a working driver is unnecessary. Two drivers conflict, and the device plugin depends on a working driver.

**Key Concept:** [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)
</details>

---

### Question 23
**Scenario:** Distributed training pods on Kubernetes need RDMA-capable secondary network interfaces on the InfiniBand or RoCE fabric, in addition to the default pod network.

A. Use only the default CNI, which gives every pod RDMA access to the high-speed fabric
B. Enable host networking on every pod and let each container configure the adapters
C. Install the GPU Operator alone, since it also manages NICs, RDMA and secondary networks
D. Deploy the NVIDIA Network Operator for the NIC driver, RDMA device plugins and Multus networks

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Network Operator manages the networking stack on Kubernetes: the NIC driver, RDMA shared or SR-IOV device plugins, and secondary networks through Multus, so pods get fabric interfaces next to their default network. The default CNI does not provide RDMA. Host networking bypasses isolation and per-pod resource accounting, and the GPU Operator manages GPUs, not NICs.

**Key Concept:** [NVIDIA Network Operator](https://docs.nvidia.com/networking/display/kubernetes2610/index.html)
</details>

---

### Question 24
**Scenario:** A 16-pod distributed training job on Kubernetes sometimes starts with only some pods scheduled, and those pods hold GPUs while waiting for the rest.

A. Use a gang-aware batch scheduler, such as NVIDIA Run:ai or Volcano, so the pods start together
B. Raise the job's pod priority so the default scheduler places all sixteen pods in a single pass
C. Reduce the job to one pod with 16 GPUs, since Kubernetes cannot run multi-pod training jobs
D. Add a startup script that exits when the other pods are missing, so the job retries until it starts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Gang scheduling admits all pods of a job together or none, which prevents partial starts that hold GPUs idle and can deadlock two jobs. The default scheduler places pods one at a time, whatever their priority. No single node has 16 GPUs in most designs, and crash-looping pods waste capacity and add churn.

**Key Concept:** [NVIDIA Run:ai documentation](https://docs.nvidia.com/run-ai/index.html)
</details>

---

### Question 25
**Scenario:** On a new Slurm cluster, jobs that request `--gres=gpu:8` are rejected, although the nodes have eight GPUs each.

A. Define GPUs as a generic resource in the Slurm config and `gres.conf`, for example with NVML autodetection
B. Request the GPUs with `--mem=8G`, which Slurm converts into eight GPUs on the node
C. Export `CUDA_VISIBLE_DEVICES` in the user's shell profile so Slurm learns the GPU count
D. Install the GPU Operator on the compute nodes, which publishes GPU counts to Slurm

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Slurm schedules GPUs as generic resources (GRES): the controller must list the GRES type and the node definitions, and `gres.conf` on each node describes the devices, which NVML autodetection can fill in. Memory requests do not map to GPUs, a user's environment variable does not inform the scheduler, and the GPU Operator is a Kubernetes component.

**Key Concept:** [Slurm generic resources (GRES)](https://slurm.schedmd.com/gres.html)
</details>

---

### Question 26
**Scenario:** Researchers on a Slurm cluster want to run NGC containers in their batch jobs without Docker on the compute nodes and without root access.

A. Give each researcher sudo on the compute nodes so they can start a Docker daemon in each job
B. Use the Pyxis plugin with Enroot, so `srun --container-image` runs NGC images without privileges
C. Convert every NGC container into a Python virtual environment by hand before each run
D. Run the containers on the login node and forward the GPU calls to compute nodes over SSH

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Enroot turns container images into unprivileged sandboxes, and the Pyxis SPANK plugin adds container options to `srun`, so jobs run NGC images under the user's own identity. Granting sudo for Docker undermines multi-user security. Rebuilding environments by hand loses the tested stack, and GPU calls cannot be forwarded over SSH.

**Key Concept:** [Pyxis container plugin for Slurm](https://github.com/NVIDIA/pyxis)
</details>

---

### Question 27
**Scenario:** Urgent jobs must be able to take GPUs from long-running research jobs on a shared Slurm cluster without the research jobs losing days of work.

A. Disable preemption and ask urgent users to wait until the research jobs finish on their own
B. Limit every job on the cluster to one hour, which removes long-running jobs from the queue entirely
C. Give urgent users root access so they can cancel any research job that holds the GPUs they need
D. Add a high-priority partition or QOS with preemption and require long jobs to checkpoint regularly

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Preemption by partition or QOS lets urgent work reclaim resources, and regular checkpointing makes preempted jobs resumable, so lost work is bounded by the checkpoint interval. Waiting fails the urgency requirement. Root access for cancellations is uncontrolled, and a one-hour cap blocks legitimate long training.

**Key Concept:** [Slurm preemption](https://slurm.schedmd.com/preempt.html)
</details>

---

### Question 28
**Scenario:** Multi-node all-reduce is far slower than expected, and the team suspects NCCL is not using the InfiniBand adapters.

A. Set `NCCL_IB_DISABLE=1`, which makes NCCL log the adapters it would have chosen without using them
B. Increase the batch size until the all-reduce time falls, which proves that the adapters are in use
C. Run with `NCCL_DEBUG=INFO` and check whether NCCL selected the IB transport or fell back to sockets
D. Check `nvidia-smi` on each node, which reports the network transport that NCCL selected for each job

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** With `NCCL_DEBUG=INFO`, NCCL logs the network plugin and transport it chose, so a fallback to TCP sockets (for example from a missing RDMA library or wrong interface) is visible immediately. `NCCL_IB_DISABLE=1` forces the slow path. Batch size changes the ratio of compute to communication, not the transport, and `nvidia-smi` does not report NCCL's choices.

**Key Concept:** [NCCL environment variables](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html)
</details>

---

### Question 29
**Scenario:** GPU utilization drops to near zero for a short time every few seconds during image training, and CPU cores are saturated decoding JPEGs.

A. Add more GPUs to each node, which spreads the decoding work across more devices
B. Profile with Nsight Systems to confirm the gaps, then move decoding to the GPU with DALI
C. Lower the learning rate so that each step takes longer and gives the CPU time to catch up
D. Turn off mixed precision, because faster GPU steps are what cause the GPU to wait for data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A periodic drop in utilization with busy CPUs is the signature of an input-bound pipeline. Nsight Systems shows the GPU idle while waiting for batches, and DALI moves decoding and augmentation onto the GPU. More GPUs make the bottleneck worse, the learning rate does not change step time, and slowing the GPU on purpose hides the problem instead of fixing it.

**Key Concept:** [NVIDIA DALI documentation](https://docs.nvidia.com/deeplearning/dali/user-guide/docs/index.html)
</details>

---

### Question 30
**Scenario:** On a two-socket node, training throughput varies between runs, and profiling shows that some ranks run on CPU cores and memory far from their GPU and NIC.

A. Disable one CPU socket in the BIOS so that every rank must use the same memory controller
B. Increase the number of data-loader threads until the slow ranks catch up with the fast ones
C. Turn off NVLink between the GPUs so that each rank uses only its local PCIe connection
D. Bind each rank to the CPU cores and memory of the NUMA node closest to its GPU and NIC

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Topology-aware binding keeps each rank's CPU threads and buffers on the NUMA node attached to its GPU and NIC, avoiding cross-socket traffic that adds latency and run-to-run variance; `nvidia-smi topo -m` shows the affinity. Disabling a socket halves CPU capacity. More threads on the wrong socket add more remote traffic, and disabling NVLink slows GPU-to-GPU communication.

**Key Concept:** [nvidia-smi documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html)
</details>

---

## Where to go deeper

- [NCP-AII cert page](../nvidia/ai-infrastructure-professional/README.md) - notes, practice plan, strategy
- [NCA-AIIO practice questions](nvidia-ai-infrastructure-operations-associate.md) - the associate level below this
- [NCP-AIN practice questions](nvidia-ai-networking-professional.md) - the fabric in depth
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - the hardware concepts in plain English
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
