---
last-updated: 2026-10-22
difficulty: intermediate
---

# NVIDIA Certified Associate - AI Infrastructure Operations (NCA-AIIO) - Practice Questions

30 questions for NCA-AIIO prep, weighted toward GPU fundamentals and monitoring (25%) and container and runtime management (25%), then Kubernetes GPU operations (20%).

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

### Question 16
**Scenario:** On a headless inference server, the first CUDA call after an idle period takes several seconds, and `nvidia-smi` itself is slow to respond.

A. Set the GPU's compute mode to Exclusive Process, which keeps the device ready between client processes
B. Lower the GPU's power limit, which shortens the time that the card takes to wake from its idle state
C. Run the NVIDIA persistence daemon so that the driver stays initialized when no client is using the GPU
D. Reinstall the CUDA toolkit, because a slow first call means the runtime libraries are partly missing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Without persistence, the kernel driver tears down GPU state when the last client exits and must reinitialize it on the next call, which adds the delay seen on headless systems. `nvidia-persistenced` keeps that state loaded. Compute mode controls how many processes may share the GPU, a lower power limit does not speed initialization, and the toolkit is not involved in driver startup.

**Key Concept:** [Driver persistence](https://docs.nvidia.com/deploy/driver-persistence/index.html)
</details>

---

### Question 17
**Scenario:** A team training a transformer on recent data center GPUs sees low Tensor Core activity in DCGM, and all math runs in FP32.

A. Enable mixed precision such as BF16 so that matrix math runs on the Tensor Cores
B. Increase the number of CPU data-loader workers until the Tensor Cores become busy
C. Turn off ECC on the GPUs, which frees the Tensor Cores for the training math
D. Switch the GPUs to the Default compute mode, which unlocks Tensor Core usage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tensor Cores accelerate reduced-precision matrix math, so training entirely in FP32 leaves most of their throughput unused; BF16 or FP16 mixed precision is the standard fix. More data-loader workers help an input-bound job but do not change which units do the math. ECC and compute mode have no effect on Tensor Core use.

**Key Concept:** [DCGM feature overview](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html)
</details>

---

### Question 18
**Scenario:** A GPU was replaced in a server after repeated memory errors, and the node must be checked thoroughly before it rejoins the production pool.

A. Run `nvidia-smi` once and confirm that all eight GPUs appear in the device list
B. Run `dcgmi diag -r 1`, the quick check that takes a few seconds per node
C. Start a short user training job and return the node if the job does not crash
D. Run a long DCGM diagnostic such as `dcgmi diag -r 3`, which adds stress tests

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** DCGM diagnostics have run levels: level 1 is a seconds-long sanity check, while levels 3 and 4 add hardware stress tests, including memory stress, that take many minutes and are suited to validating repaired hardware. Seeing the GPU in `nvidia-smi` proves only that it enumerates. Using a user's job as the test risks their work and gives weak evidence.

**Key Concept:** [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html)
</details>

---

### Question 19
**Scenario:** Before pinning processes to CPUs and GPUs, an administrator needs to see which GPUs are connected by NVLink and which CPU NUMA node each GPU is closest to.

A. Run `nvidia-smi -q -d CLOCK`, which lists the link speed and NUMA node of each GPU
B. Run `nvidia-smi topo -m`, which prints the GPU interconnect matrix and CPU affinity
C. Run `lspci -v`, which shows the NVLink connections between each pair of the GPUs
D. Run `dcgmi discovery -l`, which prints the NVLink matrix and the PCIe switch layout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `nvidia-smi topo -m` prints a matrix showing how each GPU pair is connected (NVLink, PCIe switch, host bridge) along with CPU and NUMA affinity, which is the input for process pinning. The clock query shows clocks only. `lspci` shows PCIe devices but not NVLink, and DCGM discovery lists the GPUs it can manage rather than the topology matrix.

**Key Concept:** [nvidia-smi documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html)
</details>

---

### Question 20
**Scenario:** A host runs Podman rather than Docker, and containers must get GPU access through the NVIDIA Container Toolkit.

A. Generate a CDI specification with `nvidia-ctk cdi generate` and request devices such as `nvidia.com/gpu=all`
B. Copy the NVIDIA driver libraries into each image at build time so that Podman can find them at run time
C. Install Docker alongside Podman, because the NVIDIA Container Toolkit supports only the Docker engine
D. Run every container with `--privileged`, which passes all host devices and drivers into the container

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Container Device Interface (CDI) is a vendor-neutral way to describe devices for container runtimes, and the toolkit's `nvidia-ctk` generates the CDI spec that Podman and others consume. Baking driver libraries into images ties them to one host driver version. The toolkit is not Docker-only, and `--privileged` grants far more than GPU access.

**Key Concept:** [Container Device Interface support](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)
</details>

---

### Question 21
**Scenario:** Two inference containers share an 8-GPU Docker host, and each must see only its own assigned GPU.

A. Set `CUDA_LAUNCH_BLOCKING=1` in each container so that the CUDA calls run on separate GPUs
B. Start both containers with `--gpus all` and trust each application to choose a different device
C. Enable MIG on every GPU, because Docker cannot assign whole GPUs to separate containers
D. Start each container with a specific device, such as `--gpus '"device=3"'`, so only that GPU is exposed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Docker's `--gpus` flag, backed by the NVIDIA Container Toolkit, can expose specific devices by index or UUID, so each container sees only its own GPU. `CUDA_LAUNCH_BLOCKING` makes kernel launches synchronous for debugging. Relying on applications to pick different devices is not isolation, and MIG is for partitioning one GPU, not assigning whole ones.

**Key Concept:** [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
</details>

---

### Question 22
**Scenario:** A team wants the newest NGC PyTorch container, but the cluster's data center driver is a few releases old.

A. Always pick the newest tag, because NGC containers ship with their own kernel driver inside the image
B. Rebuild the container from source on the cluster, which removes any driver version requirement
C. Check the container's release notes for its minimum driver and forward-compatibility support first
D. Use the oldest available tag, since older containers are the only ones that run on older drivers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Each NGC framework release lists the CUDA version it is built on and the driver versions it supports, including data center GPUs that can use CUDA forward compatibility with an older driver. Containers include the CUDA user-space libraries, not the kernel driver. Rebuilding from source does not remove the driver dependency, and the oldest tag gives up fixes needlessly.

**Key Concept:** [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
</details>

---

### Question 23
**Scenario:** After installing the NVIDIA Container Toolkit on a Kubernetes node that uses containerd, pods still cannot see GPUs.

A. Reinstall the NVIDIA driver, because containerd requires a separate driver build
B. Run `nvidia-ctk runtime configure --runtime=containerd` and restart containerd
C. Install Docker on the node, since Kubernetes only uses the toolkit through Docker
D. Add `privileged: true` to every GPU pod spec so that the devices become visible

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Installing the toolkit does not by itself register the NVIDIA runtime with containerd; `nvidia-ctk runtime configure` updates the containerd configuration, and the service must restart to pick it up. The GPU Operator automates this. The driver is not runtime-specific, Kubernetes no longer uses Docker as its runtime, and privileged pods are a security shortcut rather than a fix.

**Key Concept:** [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)
</details>

---

### Question 24
**Scenario:** Twenty data scientists run light notebook work and want to share four GPUs. Memory and fault isolation between them are not required.

A. Configure GPU time-slicing in the GPU Operator so that each GPU is advertised as several replicas
B. Enable MIG on the GPUs, because it is the only way to let more than one pod share a GPU
C. Give each data scientist a full GPU and keep the other sixteen people in a waiting queue
D. Request `nvidia.com/gpu: 0.2` in each pod spec, since Kubernetes accepts fractional GPU requests

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Time-slicing oversubscribes a GPU by advertising replicas, letting several pods share it in turn, which suits light interactive work when isolation is not needed. MIG gives hardware isolation but is not the only sharing method and needs supported GPUs. Dedicated GPUs waste capacity, and the standard device plugin does not accept fractional GPU requests.

**Key Concept:** [Time-slicing GPUs in Kubernetes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)
</details>

---

### Question 25
**Scenario:** A cluster mixes nodes with different GPU models, and a training job must land only on nodes with a specific GPU product.

A. Add a node name to the pod spec for every job, chosen by hand from a list of the right nodes
B. Request a larger `nvidia.com/gpu` count, which makes the scheduler prefer the newer GPU nodes
C. Use a nodeSelector or affinity on the GPU product label that GPU Feature Discovery applies
D. Set the pod's priority class to high, which places the job on the most capable GPUs available

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GPU Feature Discovery, deployed by the GPU Operator, labels each node with GPU attributes such as product name, memory and MIG capability, and pods select on those labels. Hard-coding node names breaks when nodes change. GPU count and priority class do not express which GPU model a job needs.

**Key Concept:** [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html)
</details>

---

### Question 26
**Scenario:** MIG is enabled with the mixed strategy, and a pod needs one specific slice size rather than a whole GPU.

A. Request `nvidia.com/gpu: 1` and add an annotation that names the slice size the pod needs
B. Set `CUDA_VISIBLE_DEVICES` in the pod to the MIG device ID of a free slice on the node
C. Request a fraction such as `nvidia.com/gpu: 0.25`, which the plugin maps to a MIG slice
D. Request the slice's own resource name, such as `nvidia.com/mig-1g.10gb: 1`, in the pod spec

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** With the mixed strategy the device plugin advertises each MIG profile as its own extended resource, so pods request the profile by name. In the single strategy every slice is the same and is advertised as `nvidia.com/gpu`. Annotations do not change scheduling, hand-set device IDs bypass the scheduler, and fractional requests are not supported.

**Key Concept:** [GPU Operator with MIG](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html)
</details>

---

### Question 27
**Scenario:** A new 32-node GPU cluster needs bare-metal provisioning, OS image management and node health monitoring from one NVIDIA tool.

A. NVIDIA Triton Inference Server
B. NVIDIA Base Command Manager
C. NVIDIA Nsight Systems profiler
D. NVIDIA NGC container catalog

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Base Command Manager provisions and manages clusters: it images nodes, manages software, integrates workload managers such as Slurm and Kubernetes, and monitors health. Triton serves models, Nsight Systems profiles applications, and NGC is a catalog of containers and models.

**Key Concept:** [NVIDIA Base Command Manager](https://docs.nvidia.com/base-command-manager/index.html)
</details>

---

### Question 28
**Scenario:** A rack's power budget is temporarily reduced, and each GPU's power draw must be lowered without taking the nodes offline.

A. Disable ECC on the GPUs, which reduces their power draw by about a third
B. Lower the fan speed in the BMC so that each GPU draws less power overall
C. Set a lower power limit on each GPU with `nvidia-smi -pl`, within its range
D. Stop the persistence daemon, which drops every GPU to its minimum power state

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A GPU power limit caps board power within the range the device supports, and the GPU manages clocks to stay under it, trading some performance for lower draw. ECC is about memory error protection, not a power control. Slower fans risk thermal throttling, and stopping persistence affects driver initialization, not the power ceiling under load.

**Key Concept:** [nvidia-smi documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html)
</details>

---

### Question 29
**Scenario:** The kernel log on a node shows Xid 79, "GPU has fallen off the bus," and that GPU no longer responds.

A. Drain the node, collect logs such as `nvidia-bug-report.sh`, and treat it as a hardware or PCIe fault
B. Restart the training job on the same node, because Xid 79 is a transient application error
C. Raise the GPU's power limit, because Xid 79 means the card ran out of power during a kernel
D. Reinstall the CUDA toolkit in the container, because Xid 79 is caused by a toolkit mismatch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Xid 79 means the system lost contact with the GPU over PCIe, which points at hardware, power delivery, thermals or the bus rather than application code. The node should be drained and evidence collected before reseating or replacing parts. Rerunning on the same node will fail again, and power limits and toolkit versions do not cause the device to disappear.

**Key Concept:** [Xid errors](https://docs.nvidia.com/deploy/xid-errors/index.html)
</details>

---

### Question 30
**Scenario:** After a routine OS update and reboot, `nvidia-smi` reports that it cannot communicate with the NVIDIA driver on one node.

A. Replace the GPUs, because a failed driver connection after a reboot always means dead hardware
B. Reinstall the CUDA toolkit, which contains the kernel driver that `nvidia-smi` talks to
C. Disable Secure Boot on every node in the cluster as a precaution, then reboot all of them
D. Check whether the kernel changed and rebuild or reinstall the driver module for the new kernel

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A kernel update can leave the NVIDIA kernel module built for the old kernel, so it fails to load; DKMS or a reinstall builds it for the running kernel. Hardware failure is unlikely when every GPU vanished right after an update. The toolkit is user-space, and changing Secure Boot cluster-wide is a broad change made before diagnosing one node.

**Key Concept:** [nvidia-smi documentation](https://docs.nvidia.com/deploy/nvidia-smi/index.html)
</details>

---

## Where to go deeper

- [NCA-AIIO cert page](../nvidia/ai-infrastructure-operations-associate/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - the professional level above this
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - VRAM, FLOPS, and bandwidth in plain English
- [CKA practice questions](https://cloud.noblerworks.com/resources/practice-questions/kubernetes-cka/) - the Kubernetes baseline this assumes
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
