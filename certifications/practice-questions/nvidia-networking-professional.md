---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Networking (NCP-NET) - Practice Questions

15 questions for NCP-NET prep, weighted toward InfiniBand (25%), Spectrum Ethernet (20%), RDMA and RoCE (20%), and UFM fabric management (20%).

> **Cert page:** [exams/nvidia/networking-professional/](../nvidia/networking-professional/README.md)

---

### Question 1
**Scenario:** Which component assigns LIDs and computes routing tables in an InfiniBand fabric?

A. The DHCP server, which hands out the addresses that the fabric then uses to route traffic between hosts
B. BGP, which exchanges routes between the switches and installs them into each forwarding table
C. The spine switch, which learns the topology from the leaf switches and assigns identifiers to them
D. The subnet manager

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** InfiniBand is a managed fabric: the subnet manager discovers the topology, assigns local identifiers, and programs forwarding tables. It can run on a switch or a host, and a fabric with no active subnet manager does not pass traffic at all, which is the first thing to check on a dead fabric.
</details>

---

### Question 2
**Scenario:** What does RDMA provide that TCP/IP sockets do not?

A. Direct memory-to-memory transfer with kernel bypass and near-zero CPU involvement
B. Reliable, ordered delivery with retransmission and congestion windows handled by the operating system kernel
C. Encryption of every payload in flight, which sockets leave to the application layer to deal with
D. A larger MTU of up to 9000 bytes, which sockets cannot be configured to use

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RDMA writes into remote memory without the receiving CPU copying buffers through the kernel, which removes both latency and CPU overhead. That is why it matters at scale: with sockets, the CPUs become the bottleneck of a collective operation long before the wire does.
</details>

---

### Question 3
**Scenario:** RoCEv2 is deployed and throughput collapses under load with high retransmission counts.

A. Increase the MTU only, from 1500 to 9000 bytes on the hosts
B. The fabric is not lossless: verify PFC on the right priority end to end, and tune ECN marking and DCQCN
C. Replace the NICs with a newer generation, since the retransmissions come from faulty adapter firmware in the current cards
D. Disable RDMA and fall back to TCP sockets, which gives the same throughput as RoCE with no CPU cost and no tuning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RoCE assumes losslessness, and go-back-N recovery makes even small loss rates catastrophic for throughput. PFC must be consistent on every hop for the priority carrying RoCE traffic, and ECN with DCQCN handles congestion before PFC pause frames start causing head-of-line blocking.
</details>

---

### Question 4
**Scenario:** A rail-optimized topology is chosen for a GPU cluster. What does that mean?

A. Each GPU has its own NIC and switch plane, so same-rank traffic across nodes stays on one rail and avoids cross-rail contention
B. Switches are stacked physically in the same rack so that their backplanes act as one large switch
C. Only one switch is used per row of racks, with every NIC cabled into it to keep latency uniform
D. All GPUs in a node share one NIC, which is cabled to a single top-of-rack switch for simplicity

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Collectives such as all-reduce exchange between corresponding ranks across nodes, so putting each rank on its own rail keeps that traffic on a dedicated plane and avoids cross-rail contention. It also localizes failure: a rail outage degrades rather than halts the fabric.
</details>

---

### Question 5
**Scenario:** Which topology provides non-blocking bandwidth between any pair of endpoints at scale?

A. A single switch chain, where each switch uplinks to the next one in a line down the row
B. A star with oversubscription, where many leaf ports share a few uplinks into a central switch
C. A ring, where each switch connects to two neighbors and traffic travels around the loop
D. A fat-tree (Clos) with full bisection bandwidth

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A fat-tree provisions enough uplink capacity at each tier that any permutation of traffic can be carried, which is what all-to-all collectives demand. Oversubscribed designs are cheaper and fine for general datacenter traffic but throttle synchronized training.
</details>

---

### Question 6
**Scenario:** GPUDirect RDMA must work between nodes.

A. It works automatically over any network, because the kernel stages GPU memory through the host whenever it is needed and no drivers are involved
B. Only a driver update is needed
C. The NIC and GPU need a peer-to-peer capable PCIe path with the right drivers loaded, ideally under one PCIe switch
D. It requires Ethernet only, because InfiniBand adapters cannot register GPU memory for direct transfers, whatever the driver version

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Peer-to-peer DMA depends on PCIe topology, so a NIC and GPU on different root complexes may fall back to staging through host memory and lose most of the benefit. `nvidia-smi topo -m` shows the affinity matrix, which is how you verify the pairing before blaming the fabric.
</details>

---

### Question 7
**Scenario:** Which tool monitors InfiniBand fabric health, congestion, and cable errors?

A. NVIDIA UFM
B. Prometheus alone, scraping node exporters on each host to chart link errors on the switches
C. `nvidia-smi`, which reports GPU utilization, memory, and temperature for each device on a host
D. DCGM, which collects GPU health and telemetry across the nodes in a cluster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UFM provides subnet management, real-time telemetry, congestion analysis, and cable and port diagnostics across the fabric, with alerting on error counter thresholds. DCGM and `nvidia-smi` see GPUs, not the network between them.
</details>

---

### Question 8
**Scenario:** Symbol errors are rising on one InfiniBand port.

A. Ignore them if throughput looks fine, because the link layer corrects symbol errors and they only matter if the port goes down
B. Check the physical layer: reseat or replace the cable or optic, compare counters at each end, isolate the link
C. Reboot the switch, because a restart clears the port counters and retrains every link in the fabric
D. Reduce the link speed permanently on that port so the errors fall, accepting lower bandwidth in return

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rising symbol and link-downed counters are the classic signature of a marginal cable or optic, and a degraded link silently slows every collective that crosses it. Reducing speed masks the fault rather than fixing it, and one bad link can pace an entire training job.
</details>

---

### Question 9
**Scenario:** SHARP is enabled on the fabric. What does it do?

A. Provides routing, calculating the forwarding tables that switches use to send each packet across the fabric
B. Encrypts traffic between the hosts at line rate, using keys held by the subnet manager
C. In-network aggregation of collective operations in the switches, cutting data movement and latency
D. Compresses packets in the switch hardware so that more data fits on each link

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Scalable Hierarchical Aggregation and Reduction Protocol offloads reduction operations to the switch hierarchy, so partial sums are combined in the network rather than every value traversing to every endpoint. It measurably shortens all-reduce time at scale.
</details>

---

### Question 10
**Scenario:** Adaptive routing is enabled in an InfiniBand fabric.

A. Packets always follow the shortest static path computed once by the subnet manager when the fabric starts
B. It applies only to Ethernet fabrics running RoCE, where switches rehash flows after a link failure
C. Traffic is spread across alternative paths based on congestion
D. It disables the subnet manager, since the switches then compute their own routes without central input

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Static routing can create hotspots when several flows hash to the same path. Adaptive routing spreads them, which matters for the bursty synchronized patterns of distributed training. Applications must tolerate potential out-of-order delivery, which InfiniBand transport handles.
</details>

---

### Question 11
**Scenario:** Spectrum switches are managed with Cumulus Linux. What is the operational model?

A. Windows-based management through a graphical console installed on an administrator workstation, with settings saved in a registry
B. A Linux-based network OS where standard tooling, automation, and NVUE or Linux commands configure the switch
C. Manual cabling only, because the switch ports have no software configuration of their own
D. A proprietary CLI only, with no access to a Linux shell or to standard automation tools

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cumulus treats the switch as a Linux host, so configuration management tools and the same automation practices used for servers apply. That is the operational argument for it: one toolchain across compute and network rather than two.
</details>

---

### Question 12
**Scenario:** A DPU (BlueField) is deployed in the cluster. What is its purpose?

A. A storage array that exposes NVMe volumes to the cluster over the fabric
B. Offloading networking, storage, and security functions from the host CPU onto the adapter's own isolated cores
C. A display adapter that drives monitors and remote consoles for the compute nodes in the rack, replacing the onboard graphics chip
D. Additional GPU compute that adds more tensor cores to each host, so it is used for training workloads

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A DPU runs infrastructure services (virtual switching, encryption, storage virtualization, telemetry) on the adapter, freeing host cores for application work and creating a control boundary the tenant OS cannot reach. That isolation property is why it appears in multi-tenant AI cloud designs.
</details>

---

### Question 13
**Scenario:** Congestion control must prevent one heavy flow starving others on a RoCE fabric.

A. Nothing is needed, because the switches share bandwidth fairly between flows without any tuning
B. ECN marking with DCQCN and tuned thresholds, with PFC kept as a last-resort backstop rather than the primary mechanism
C. PFC alone, enabled on every priority so that no packet is ever dropped, whatever the load
D. Larger buffers only, sized so large that the queues never fill under any traffic pattern

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ECN signals congestion early so senders slow down gradually, while PFC pauses entire priority classes and can spread congestion backward through the fabric, causing head-of-line blocking and in bad cases pause storms. Correct designs rely on ECN and treat PFC as the safety net.
</details>

---

### Question 14
**Scenario:** A new cluster must be validated before production.

A. Visual inspection of every cable, transceiver, and port LED, confirming that the link lights are green on every port in the racks and that nothing is loose
B. Trust the installer's sign-off and handover documents, and confirm the cluster simply by starting the first production training job on it
C. Verify the fabric: link speed and width per port, error baselines, point-to-point tests, and NCCL all-reduce at full scale
D. Ping tests between every pair of hosts, confirming that each node can reach every other node on the fabric

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Ping proves reachability and nothing about bandwidth. A link that negotiated a lower width, one bad optic, or a missing PFC configuration will pass ping and destroy training performance, so measure per-link and then measure the collective that the cluster exists to run.
</details>

---

### Question 15
**Scenario:** Choosing between InfiniBand and Ethernet for a new AI fabric.

A. InfiniBand has lossless transport, adaptive routing, and SHARP natively; RoCE Ethernet can compete but needs careful lossless tuning
B. InfiniBand cannot scale beyond a few hundred nodes because the subnet manager becomes a bottleneck
C. Ethernet is always better because it is cheaper and every operations team already knows how to run it
D. They are identical in behavior; the only difference is the connector and cable type used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The honest comparison is about built-in guarantees versus operational familiarity and ecosystem. InfiniBand gets lossless behavior and in-network aggregation by design; RoCE gets there with configuration discipline across every hop, which is where deployments most often go wrong.
</details>

---

## Where to go deeper

- [NCP-NET cert page](../nvidia/networking-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - cluster design in context
- [Networking topic index](https://cloud.noblerworks.com/topics/networking/) - cross-cloud networking
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
