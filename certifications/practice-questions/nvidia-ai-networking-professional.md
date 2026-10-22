---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA-Certified Professional - AI Networking (NCP-AIN) - Practice Questions

30 questions for NCP-AIN prep, weighted toward NVIDIA Spectrum networking (30%) and NVIDIA InfiniBand networking (30%), then troubleshooting tools (20%), automation and configuration (10%), and AI data center design and Kubernetes integration (5% each).

> **Cert page:** [exams/nvidia/ai-networking-professional/](../nvidia/ai-networking-professional/README.md)

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

### Question 16
**Scenario:** A Spectrum-X fabric sprays the packets of each RoCE flow across many equal-cost paths. Packets therefore reach the receiver out of order.

A. The leaf switch holds every packet in a reorder buffer and releases the flow in sequence
B. The receiving application must detect the gaps and request retransmission of each missing packet
C. Adaptive routing stays off for RDMA traffic, so RoCE packets always follow a single path
D. The SuperNIC on the receiving host places packets directly into memory in the correct order

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Spectrum-X pairs Spectrum-4 switches, which spray packets across paths for even load, with BlueField-3 SuperNICs, whose direct data placement writes each packet to its correct place in host or GPU memory regardless of arrival order. Switches do not reassemble flows. Treating reordering as loss would trigger needless retransmissions, and adaptive routing for RoCE is the point of the platform.

**Key Concept:** [NVIDIA SuperNICs and Spectrum-X](https://developer.nvidia.com/blog/powering-next-generation-ai-networking-with-nvidia-supernics/)
</details>

---

### Question 17
**Scenario:** On a standard Ethernet fabric using static ECMP hashing, a few large all-reduce flows land on the same uplink while other uplinks sit nearly idle.

A. Increase the switch buffer size on the busy uplink so that it can absorb the colliding flows
B. Lower the MTU on all links so that each flow is split into more packets across the uplinks
C. Use adaptive routing, which spreads traffic by current path load rather than by a fixed hash
D. Disable ECN on the fabric so that the senders stop slowing down when the uplink fills up

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Static ECMP hashes each flow to one path, so a handful of long-lived elephant flows can collide on the same link no matter how idle the others are. Adaptive routing, as in Spectrum-X, chooses paths using live load and balances the traffic. Bigger buffers delay the collision rather than prevent it, a smaller MTU does not change hashing, and disabling ECN removes congestion signals.

**Key Concept:** [NVIDIA SuperNICs and Spectrum-X](https://developer.nvidia.com/blog/powering-next-generation-ai-networking-with-nvidia-supernics/)
</details>

---

### Question 18
**Scenario:** A new set of Spectrum switches running Cumulus Linux must carry lossless RoCE, and the engineer wants NVIDIA's recommended PFC and ECN settings without configuring each queue by hand.

A. Enable link-level pause on every port, which is the recommended lossless method for RoCE
B. Configure only ECN on the uplinks, because PFC is not supported on Spectrum switches
C. Write a custom buffer profile for each port before the fabric is allowed to carry RoCE
D. Run `nv set qos roce` and apply the configuration, which enables lossless RoCE defaults

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In Cumulus Linux, `nv set qos roce` turns on the RoCE profile, lossless by default, which configures PFC on the RoCE priority, ECN marking and the matching buffer settings in one step. Link-level pause stops the whole link rather than one class, which is why PFC is preferred. Spectrum switches support PFC, and hand-built buffer profiles are rarely needed.

**Key Concept:** [Cumulus Linux: RoCE](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/)
</details>

---

### Question 19
**Scenario:** PFC is enabled on the switches, yet RoCE traffic still sees drops under load. Captures show the RoCE packets arriving with a DSCP value that maps to a lossy queue.

A. Make the hosts' NICs and the switches agree on the DSCP and priority used for RoCE
B. Raise the switch MTU to 9216 bytes, which moves RoCE packets into the lossless queue
C. Turn off PFC and rely on TCP retransmission, which handles the drops for RDMA traffic
D. Add more spine switches so that the lossy queue has more capacity during busy periods

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lossless behavior applies only to traffic classified into the PFC-enabled priority, so the NIC's marking and the switch's DSCP-to-priority mapping must match end to end. MTU does not decide the queue. RoCE does not run over TCP, and extra spine capacity does not fix packets landing in the wrong class.

**Key Concept:** [Cumulus Linux: RoCE](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/)
</details>

---

### Question 20
**Scenario:** A GPU cloud provider on Spectrum Ethernet must give each tenant an isolated Layer 2 and Layer 3 network that spans many racks of the same routed fabric.

A. Give each tenant its own physical leaf switches and never connect them to the shared spine layer
B. Put every tenant on one large VLAN and rely on host firewalls to separate their traffic
C. Use BGP EVPN with VXLAN, mapping each tenant to its own VNIs and VRF across the fabric
D. Use InfiniBand P_Keys on the Ethernet switches to place each tenant in its own partition

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** EVPN-VXLAN overlays give each tenant its own virtual networks and routing table over a shared, routed underlay, which is the standard multi-tenant design that Cumulus Linux supports. Dedicated hardware per tenant wastes capacity. One shared VLAN leaves isolation to the hosts, and P_Keys are an InfiniBand feature.

**Key Concept:** [Cumulus Linux: EVPN](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/)
</details>

---

### Question 21
**Scenario:** Two research groups share one InfiniBand fabric, and their nodes must not be able to communicate with each other.

A. Give each group its own subnet manager on the same fabric so that each manages its own nodes
B. Assign each group a different MTU so that their packets cannot be delivered to the other group
C. Use separate IP subnets on the IPoIB interfaces, which also blocks the native RDMA traffic
D. Configure InfiniBand partitions (P_Keys) so that each group's ports belong to its own partition

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Partition keys work much like VLANs for InfiniBand: the subnet manager places ports in partitions, and hosts cannot communicate across partitions they do not share. A subnet has one master SM, so competing SMs are a fault. MTU does not isolate traffic, and IP subnets on IPoIB do not stop native verbs traffic.

**Key Concept:** [UFM Enterprise user manual](https://docs.nvidia.com/networking/display/ufmenterpriseumv6200/)
</details>

---

### Question 22
**Scenario:** The InfiniBand fabric has one subnet manager. The team worries about what happens if that node fails.

A. Nothing, because the switches keep their tables and the fabric never needs an SM again
B. Run standby SMs on other nodes, which take over as master if the current master fails
C. Run two master SMs at the same priority, so that each serves half of the fabric
D. Put the SM on a compute node, since compute nodes rarely fail and need no backup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** InfiniBand supports one master SM with standby SMs; the standbys monitor the master and one takes over if it disappears, and priority settings control which node wins. Existing routes keep working briefly, but without an SM the fabric cannot handle changes such as link flaps or new nodes. A subnet cannot be split between two masters, and the SM's placement does not remove the need for redundancy.

**Key Concept:** [UFM Enterprise user manual](https://docs.nvidia.com/networking/display/ufmenterpriseumv6200/)
</details>

---

### Question 23
**Scenario:** A large InfiniBand fat-tree is brought up with a generic shortest-path routing algorithm, and traffic distribution across the spines is poor.

A. Disable adaptive routing everywhere, since it is incompatible with every fat-tree design
B. Lower the link speed on the spine ports so that traffic spreads more evenly across them
C. Configure a topology-aware routing engine in the SM, such as fat-tree (ftree) or up/down
D. Replace the fat-tree with a ring topology, which a shortest-path engine routes evenly

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The subnet manager's routing engine decides how forwarding tables are computed, and engines designed for fat-trees balance routes across spines and avoid credit loops. Adaptive routing complements fat-trees rather than conflicting with them. Slowing links reduces capacity, and a ring has far less bisection bandwidth.

**Key Concept:** [UFM Enterprise user manual](https://docs.nvidia.com/networking/display/ufmenterpriseumv6200/)
</details>

---

### Question 24
**Scenario:** A legacy monitoring agent and a few storage clients speak only TCP/IP, but the nodes' only high-speed interface is InfiniBand.

A. Use IP over InfiniBand (IPoIB), which presents an IP network interface on the IB adapter
B. Replace the InfiniBand adapters with Ethernet adapters, since IB cannot carry IP traffic
C. Run the TCP traffic over the BMC network, since IB ports can carry only RDMA verbs
D. Convert the agents to use RDMA verbs, because no IP traffic can be sent over an IB link

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IPoIB encapsulates IP over InfiniBand and gives the host a normal network interface, so TCP/IP software runs unchanged while RDMA applications keep using verbs on the same fabric. IB adapters do not need replacing, the BMC network is for out-of-band management, and rewriting the agents is unnecessary.

**Key Concept:** [MLNX_OFED documentation](https://docs.nvidia.com/networking/display/mlnxofedv24100700/)
</details>

---

### Question 25
**Scenario:** After cabling a new node, `ibstat` shows its port's physical state as LinkUp but the logical state as Initializing, and the port never becomes Active.

A. The cable is faulty, because Initializing means that the physical link failed to train
B. The port is working normally, because Initializing is the steady state for a host port
C. The adapter firmware is too new, and the port must be downgraded before it becomes Active
D. The port has not been configured by a subnet manager, so check that an SM is running and can reach it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A physical state of LinkUp shows the cable and link training are fine; the logical state moves from Initializing to Active only when the subnet manager assigns a LID and configures the port. So the question is whether an SM is running and can reach that port, for example across a partition or a switch issue. Initializing is not a steady state, and firmware is not the first suspect.

**Key Concept:** [InfiniBand fabric utilities](https://docs.nvidia.com/networking/display/mlnxofedv24100700/infiniband+fabric+utilities)
</details>

---

### Question 26
**Scenario:** On Kubernetes, latency-sensitive training pods each need their own isolated RDMA virtual function on the NIC instead of sharing one RDMA device with other pods.

A. Use the RDMA shared device plugin, which gives each pod a dedicated virtual function
B. Set `hostNetwork: true` on each pod so that it gets exclusive use of the host's NIC
C. Request `nvidia.com/gpu` for each pod, which also gives the pod its own RDMA device
D. Use SR-IOV through the Network Operator, which assigns a dedicated VF to each pod

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Network Operator supports two models: the RDMA shared device plugin, where pods share one RDMA device, and SR-IOV, where each pod gets its own virtual function with hardware isolation. The pods need the second. Host networking shares the full NIC with everything on the node, and GPU requests do not allocate network devices.

**Key Concept:** [NVIDIA Network Operator](https://docs.nvidia.com/networking/display/kubernetes2610/index.html)
</details>

---

### Question 27
**Scenario:** One link keeps showing errors, and the engineer needs that single port's physical-layer details: bit error rate, cable and module information, and the negotiated speed.

A. Run `ibping` between the two ends, which reports the bit error rate and cable type of the link
B. Restart the subnet manager, which re-trains the link and prints its physical-layer statistics
C. Run `mlxlink` against the port, which reports BER counters, module data and link status
D. Run `nvidia-smi nvlink -e`, which reports the error counters for InfiniBand ports as well

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `mlxlink`, part of the NVIDIA Firmware Tools, examines a single port's physical layer, including link state, speed, BER and FEC counters, and cable or transceiver information. `ibping` tests reachability and latency. Restarting the SM changes logical state, not physical diagnostics, and `nvidia-smi nvlink` covers NVLink, not InfiniBand ports.

**Key Concept:** [mlxlink utility](https://docs.nvidia.com/networking/display/mftv4330/mlxlink+utility)
</details>

---

### Question 28
**Scenario:** After a maintenance window on a Spectrum Ethernet fabric, some jobs are slower. The operator wants to check fabric-wide state and see what changed compared with before the window.

A. Log in to each switch in turn and compare `show` outputs from memory of the old state
B. Use NetQ validations and snapshots to check fabric state and compare it with earlier state
C. Reboot every switch in sequence, which resets any change made during the maintenance window
D. Run `ibdiagnet`, which scans Ethernet fabrics and reports changes made to switch settings

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NetQ collects telemetry from the fabric, runs validation checks across protocols and devices, and can compare network state at two points in time, which answers "what changed". Checking switches one by one is slow and error-prone. Rebooting does not undo configuration changes, and `ibdiagnet` is an InfiniBand tool.

**Key Concept:** [NVIDIA NetQ user guide](https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/)
</details>

---

### Question 29
**Scenario:** An engineer changes a BGP setting with NVUE on a Cumulus Linux switch and wants to review the change before it takes effect.

A. Edit the FRR configuration file directly, since NVUE changes take effect the moment they are typed
B. Restart the switch after typing the commands, which commits the staged changes and runs them
C. Type the change in `vtysh` instead, since NVUE has no way to preview a change before it applies
D. Stage with `nv set`, review with `nv config diff`, then commit the change with `nv config apply`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NVUE uses a candidate-and-apply model: `nv set` edits a pending revision, `nv config diff` shows what would change, and `nv config apply` commits it, with saved revisions to fall back on. Changes do not apply as they are typed. Editing generated files or bypassing NVUE with `vtysh` creates drift, and reboots are not a commit mechanism.

**Key Concept:** [Cumulus Linux: NVUE](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/)
</details>

---

### Question 30
**Scenario:** A network team wants to test an automation playbook and a new fabric design against realistic switch operating systems before touching production hardware.

A. Run it in NVIDIA DSX Air, a cloud-hosted digital twin of the data center network
B. Run it on one production leaf switch during a quiet hour and roll back if anything breaks
C. Review the playbook by reading it carefully, since network changes cannot be simulated
D. Test the playbook on a laptop switch emulator that supports only generic Linux bridges

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DSX Air simulates full network architectures with real network operating systems, so configurations and automation code can be validated against a digital twin before deployment. Testing on production hardware risks an outage. Reading code misses runtime behavior, and a generic bridge emulator does not behave like Cumulus Linux on Spectrum.

**Key Concept:** [NVIDIA DSX Air user guide](https://docs.nvidia.com/networking-ethernet-software/nvidia-air/)
</details>

---

## Where to go deeper

- [NCP-AIN cert page](../nvidia/ai-networking-professional/README.md) - notes, practice plan, strategy
- [NCP-AII practice questions](nvidia-ai-infrastructure-professional.md) - cluster design in context
- [Networking topic index](https://cloud.noblerworks.com/topics/networking/) - cross-cloud networking
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
