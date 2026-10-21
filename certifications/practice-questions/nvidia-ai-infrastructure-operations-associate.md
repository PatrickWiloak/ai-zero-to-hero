---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - AI Infrastructure Operations (NCA-AIIO) - Practice Questions

15 questions for NCA-AIIO prep, weighted toward GPU fundamentals and monitoring (25%) and container and runtime management (25%), then Kubernetes GPU operations (20%).

> **Cert page:** [exams/nvidia/ai-infrastructure-operations-associate/](../nvidia/ai-infrastructure-operations-associate/README.md)

---

### Question 1
**Scenario:** You need current GPU utilization, memory use, temperature, and the processes using each GPU on a node.

A. `nvidia-smi`, which reports utilization, memory, temperature, and the compute processes on each GPU
B. `lspci -v`, which lists PCIe devices with their link speed, including each installed GPU
C. `top` with the per-thread view enabled, which shows CPU time per process including processes driving the GPU
D. `df -h` on the node, which shows filesystem usage and so the space left for datasets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `nvidia-smi` is the first tool for any GPU question: utilization, memory, power, temperature, ECC state, and the compute processes attached to each device. `nvidia-smi -l 1` loops it, and `dmon` gives a compact time series. `lspci` only confirms the card is present on the bus.
</details>

---

### Question 2
**Scenario:** Fleet-wide GPU health metrics must be exported to Prometheus with alerting.

A. Grafana alone, with a dashboard at each node, since Grafana collects GPU metrics itself
B. `nvidia-smi` in a cron job on each node writing CSV files that a central script merges
C. NVIDIA DCGM with the DCGM exporter, which exposes GPU health and profiling metrics to Prometheus
D. Node exporter alone, using its default collectors, which report CPU, memory, disk, and network but not GPU counters

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DCGM is the managed monitoring layer for GPUs, providing health checks, diagnostics, and profiling metrics, and the DCGM exporter presents them to Prometheus. Node exporter has no GPU visibility, and Grafana visualizes data it is given rather than collecting it.
</details>

---

### Question 3
**Scenario:** A container must access the host's GPUs.

A. Install the matching NVIDIA driver inside the container image so the image carries everything it needs, whatever the host runs
B. Use the NVIDIA Container Toolkit so the runtime injects the driver libraries and devices
C. Mount `/dev` manually into the container, which exposes device nodes but not the user-space driver libraries
D. Run the container as privileged with no other change, which exposes host devices but still provides no driver libraries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The toolkit's runtime hook exposes the devices and mounts the matching driver user-space libraries from the host, which is why the container ships CUDA runtime but not the driver. Installing a driver in the image would conflict with the host kernel module version.
</details>

---

### Question 4
**Scenario:** A CUDA application fails with a driver and runtime version mismatch.

A. Reboot the node, because a mismatch is cleared once the kernel module is reloaded at start-up
B. Increase GPU memory by moving the job to a larger card, since the error comes from a failed allocation
C. Reinstall the application and rebuild its virtual environment, which replaces Python packages but leaves the host driver unchanged
D. The container's CUDA runtime needs a newer driver than the host has; upgrade the host driver or use a matching image

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The compatibility rule is that the driver must be at least as new as the CUDA runtime, and newer drivers support older runtimes. CUDA forward compatibility packages relax this on data center GPUs. Checking the driver version against the image's CUDA version is the fast diagnosis.
</details>

---

### Question 5
**Scenario:** Kubernetes must schedule pods onto GPU nodes and advertise GPU resources automatically.

A. The NVIDIA GPU Operator, which manages drivers, container toolkit, device plugin, and DCGM exporter on every GPU node
B. A node label such as `gpu=true` on each GPU node, which lets selectors target nodes and also advertises GPU capacity to the scheduler
C. A DaemonSet running `nvidia-smi` on every node, which prints utilization but registers no schedulable resource
D. The CNI plugin, which configures pod networking but also handles discovery of GPU devices on each node

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The GPU Operator installs and lifecycle-manages the whole GPU software stack on nodes, including the device plugin that advertises `nvidia.com/gpu` as a schedulable resource. Labeling alone tells the scheduler nothing about capacity.
</details>

---

### Question 6
**Scenario:** One A100 should be shared by several small inference workloads with hardware-level isolation.

A. Running them sequentially on the whole GPU, which avoids interference but does not share the card between workloads
B. MPS, which lets processes share a GPU concurrently, without dedicated memory or a separate fault domain per client
C. Time-slicing through the device plugin, which gives each workload dedicated memory and bandwidth for the whole duration of its slice
D. MIG, partitioning the GPU into isolated instances

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MIG partitions the GPU into instances with dedicated SMs, cache, and memory bandwidth, giving fault and performance isolation. Time-slicing shares the whole GPU by interleaving contexts with no memory isolation, and MPS allows concurrent kernels from multiple processes without hard isolation.
</details>

---

### Question 7
**Scenario:** A pod requests `nvidia.com/gpu: 1` and stays Pending.

A. Rebuild the image with a newer CUDA base, because a Pending pod means the image failed to start on the node
B. Restart the API server so it reloads node resources, since Pending pods usually come from stale control-plane state
C. Check for schedulable GPU nodes, whether the device plugin is running and advertising capacity, and whether taints block placement
D. Increase the pod's memory request, because a pod waiting on `nvidia.com/gpu` is held back by missing RAM on the node

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `kubectl describe node` shows whether `nvidia.com/gpu` appears under Capacity and Allocatable, which immediately separates "no GPU nodes" from "plugin not running" from "all GPUs already allocated." GPU nodes are also frequently tainted so that only GPU workloads land on them.
</details>

---

### Question 8
**Scenario:** What does NVLink provide compared with PCIe?

A. Network connectivity between nodes, so NVLink replaces InfiniBand for multi-node training across the cluster
B. Storage access from GPUs straight to NVMe drives, bypassing the CPU and host memory on the node
C. Higher bandwidth, lower latency GPU-to-GPU interconnect within a node
D. Display output for multi-monitor workstation setups, replacing DisplayPort on data center cards

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVLink and NVSwitch create a high-bandwidth fabric between GPUs inside a server, which is what makes tensor parallelism practical. Between nodes the equivalent role is played by InfiniBand or high-speed Ethernet with RDMA.
</details>

---

### Question 9
**Scenario:** GPU memory is reported as full but no training job is running.

A. Buy more GPUs for the node, because memory reported full means the existing devices have too little capacity for the workload
B. Check for orphaned processes holding memory in the `nvidia-smi` process list, and reset the GPU if needed
C. Reinstall CUDA and the driver, because reported memory use after a job ends points to a corrupted toolkit installation
D. Reduce the batch size in the training script, which lowers memory use of a new job but frees nothing already held

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A crashed or zombie process can retain its CUDA context and memory. Identify it in the `nvidia-smi` process list and terminate it; `nvidia-smi --gpu-reset` is the escalation when no process is visible and the device is idle. This is one of the most common day-to-day GPU operations tickets.
</details>

---

### Question 10
**Scenario:** Which registry hosts NVIDIA's optimized containers for frameworks and models?

A. PyPI, which hosts Python wheels but not GPU-tuned containers
B. Conda-forge, the community channel for conda packages built by volunteers without NVIDIA-specific container images
C. Docker Hub only, since NVIDIA publishes no images of its own and community images are the only option
D. The NGC catalog, with containers versioned against specific CUDA and driver combinations

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NGC provides tuned framework containers, Helm charts, pretrained models, and NIM microservices, versioned against specific CUDA and driver combinations. Using them avoids most of the version-matching problems in question 4.
</details>

---

### Question 11
**Scenario:** ECC errors are reported on a GPU.

A. Distinguish correctable from uncorrectable: trend correctable ones, and drain the GPU and engage the vendor for repeated uncorrectable ones
B. Disable ECC permanently to reclaim memory and stop the error reports, accepting the small loss of capacity on the card
C. Ignore them, because every ECC error is corrected in hardware and none can affect the results of a running training job
D. Reformat the node and reinstall the OS image, since ECC errors indicate corrupted filesystems on local disk

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Correctable single-bit errors are expected at low rates. Uncorrectable errors corrupt computation and typically require row remapping or hardware replacement, so the operational response is to cordon and drain the node before it silently poisons a training run.
</details>

---

### Question 12
**Scenario:** A training job needs to be scheduled with other jobs on a shared cluster, with queueing and fair share.

A. NVIDIA Base Command or Slurm, which provide queues, priorities, fair-share accounting, and gang scheduling for multi-node jobs
B. systemd timers on each node, which start jobs at set times but keep no shared queue or fair-share accounting
C. `docker run` on any free node by each user, which launches at once but gives no queueing or accounting
D. cron entries on a shared login node, which can start containers but cannot track GPU allocation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch schedulers provide queues, priorities, fair-share accounting, and gang scheduling for multi-node jobs, which is what a shared GPU cluster needs. Running containers directly gives no queueing, so the cluster is allocated first-come-first-served by whoever types fastest.
</details>

---

### Question 13
**Scenario:** GPU utilization is high but the job is slow, and profiling shows most time in host-to-device copies.

A. Increase the learning rate, which changes convergence behaviour but does not shorten time spent copying data
B. The data pipeline is the bottleneck: add dataloader workers, prefetch, use pinned memory, and consider GPUDirect Storage
C. Reduce model size to lower the compute per step, which helps arithmetic cost but not the time waiting on host-to-device copies
D. Add more GPUs to the job, which divides the compute but leaves each GPU waiting on the same slow host-to-device transfers from the CPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A GPU waiting on data is a data pipeline problem, and adding GPUs multiplies the starvation. Pinned memory enables asynchronous transfers, more workers keep the queue full, and GPUDirect Storage bypasses the host bounce buffer entirely for storage reads.
</details>

---

### Question 14
**Scenario:** Driver upgrades must be rolled out to a Kubernetes GPU fleet with minimal disruption.

A. Upgrade only the containers, since the image's CUDA version is what the host driver must match
B. Use the GPU Operator's driver upgrade with node draining, one pool at a time, validating before proceeding
C. Skip upgrades entirely, because a working driver never needs patching and changing it only adds risk to the fleet
D. Upgrade all nodes at once in a maintenance window, which is fastest but removes every GPU from service together

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Driver changes require workloads off the node, so cordon, drain, upgrade, validate, uncordon is the sequence, done in waves so a bad driver never takes the fleet. Staying on old drivers eventually blocks newer CUDA runtimes and leaves known bugs in place.
</details>

---

### Question 15
**Scenario:** An escalation must include enough evidence for NVIDIA support.

A. The application source code and a description of the model architecture, which NVIDIA needs to reproduce the fault on its own hardware
B. A description of the symptom only, written in plain words with the time it started, which is enough for support to locate the cause
C. `nvidia-bug-report.sh` output, driver and CUDA versions, `nvidia-smi -q` output, DCGM diagnostics, and the reproduction steps
D. A screenshot of the failing console output, which shows the error text but not the driver state or system configuration

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The bug report script collects driver logs, kernel messages, and configuration in one bundle, and DCGM diagnostics distinguish hardware faults from software issues. Gathering this before escalating typically removes a full round trip.
</details>

---

## Where to go deeper

- [NCA-AIIO cert page](../nvidia/ai-infrastructure-operations-associate/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the professional level above this
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - VRAM, FLOPS, and bandwidth in plain English
- [CKA practice questions](https://cloud.noblerworks.com/resources/practice-questions/kubernetes-cka/) - the Kubernetes baseline this assumes
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
