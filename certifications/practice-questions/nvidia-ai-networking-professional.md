---
last-updated: 2026-11-07
difficulty: advanced
---

# NVIDIA-Certified Professional - AI Networking (NCP-AIN) - Practice Questions

30 original questions in the weights of NVIDIA's blueprint: AI data center design (5%, 2 questions), Spectrum networking (30%, 9), InfiniBand networking (30%, 8), Kubernetes integration (5%, 2), troubleshooting tools (20%, 6) and automation and configuration (10%, 3). They are written for this guide, not taken from the exam, and each explanation names the NVIDIA source it rests on.

> **Cert page:** [exams/nvidia/ai-networking-professional/](../nvidia/ai-networking-professional/README.md)

---

### Question 1
**Section 1. Scenario:** A reference architecture splits the cluster network into separate fabrics. Which traffic belongs on the compute (east-west) fabric?

A. Out-of-band BMC and switch management traffic
B. End-user connections to the cluster
C. GPU-to-GPU RDMA traffic during training
D. Storage access for all nodes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NVIDIA's HGX AI Factory design puts GPU-to-GPU RDMA on the compute fabric, storage and in-band management on the converged north-south network, and BMC and switch management on a separate 1 Gb out-of-band network.
</details>

---

### Question 2
**Section 1. Scenario:** In a rail-optimized topology, which GPUs share a rail?

A. All eight GPUs inside one server
B. The GPUs in the same position (index) in each server
C. GPUs chosen at random by the scheduler
D. Only GPUs attached to the same storage array

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NVIDIA's architecture connects GPUs to the fabric through their SuperNICs with GPUs of the same index across nodes sharing a rail and leaf switches.
</details>

---

### Question 3
**Section 2. Scenario:** A Spectrum switch running Cumulus Linux 5.18 needs lossless RoCE with the NVUE defaults. Which command enables it?

A. nv set qos roce mode lossy, followed by nv config apply
B. nv set router adaptive-routing state enabled, followed by nv config apply
C. nv unset qos roce, followed by nv config apply
D. nv set qos roce, followed by nv config apply

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The RoCE page says NVUE defaults to RoCE lossless, and nv set qos roce is equivalent to nv set qos roce mode lossless. Lossy mode uses ECN without PFC, and nv unset removes the configuration.
</details>

---

### Question 4
**Section 2. Scenario:** Which pair of mechanisms does lossless RoCE mode combine?

A. PFC on the RoCE priority together with ECN
B. ECN only, with PFC disabled
C. BGP graceful restart and MLAG
D. PKeys and service levels

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lossless mode enables priority flow control (priority 3 by default) and ECN. Lossy mode is ECN without PFC. PKeys and SLs are InfiniBand concepts.
</details>

---

### Question 5
**Section 2. Scenario:** An engineer wants to check the RoCE mode, PFC priority and ECN thresholds on a switch. Which command shows them?

A. nv show router adaptive-routing
B. nv show qos roce
C. nv show system wjh channel
D. ibstat

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** nv show qos roce lists the mode, PFC settings, congestion control thresholds and trust mode. The other commands show adaptive routing, WJH channels and InfiniBand port status.
</details>

---

### Question 6
**Section 2. Scenario:** Which statement about adaptive routing on Spectrum-X switches (Cumulus Linux 5.18) is correct?

A. It works on bonds and bond members
B. It requires resilient hashing
C. It is supported on Spectrum-X with Spectrum-4 ASICs at 400G or 200G, not on 800G links
D. It can be mixed freely with non-AR ports in the same ECMP route

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The page lists Spectrum-4 at 400G or 200G only, no support on 800G, layer 3 interfaces only (not bonds, SVIs or subinterfaces), no resilient hashing, and warns of unexpected route hashing when AR and non-AR ports are mixed.
</details>

---

### Question 7
**Section 2. Scenario:** A multi-tenant EVPN fabric needs each tenant's routed traffic kept inside the tenant. What maps a tenant to its routing domain across VXLAN?

A. A shared default VRF with the L2 VNI
B. A tenant VRF mapped to an L3 VNI
C. A PKey in the VXLAN header
D. One physical switch per tenant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each tenant gets a VRF with its own L3 VNI and route targets. Cumulus Linux does not support an L3 VNI for the default VRF, and PKeys belong to InfiniBand.
</details>

---

### Question 8
**Section 2. Scenario:** A switch runs the NetQ agent. What must be done about the on-switch WJH service?

A. Disable it, because the NetQ agent exports WJH data itself
B. Run both services at once for redundancy
C. Enable more WJH channels
D. Replace it with an ECN threshold

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The WJH page says that when you use the NetQ agent on the switch you must disable the WJH service, for example nv set system wjh state disabled.
</details>

---

### Question 9
**Section 2. Scenario:** What is the purpose of NVIDIA DSX Air in network operations?

A. To simulate AI factory networks and test provisioning, automation and policy before changes reach hardware
B. To capture packet drops on a live switch
C. To install DOCA drivers on a host
D. To manage InfiniBand partitions

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NVIDIA describes DSX Air as a cloud-based simulation platform for AI factories, used to test provisioning, automation and security policy before a single piece of hardware ships and to apply changes to the live environment only after they succeed in simulation.
</details>

---

### Question 10
**Section 2. Scenario:** What is installed with apt install -y doca-all mlnx-fw-updater on a Debian-family host?

A. The Cumulus Linux switch operating system
B. The DOCA host profile and the NIC firmware updater, after installing DKMS and matching kernel headers
C. The UFM server
D. The Kubernetes Network Operator

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DOCA host installation installs a profile such as doca-all (plus mlnx-fw-updater) from the DOCA repository; DKMS and kernel headers matching the running kernel are prerequisites, and the driver and MST services are restarted afterward.
</details>

---

### Question 11
**Section 2. Scenario:** Which WJH command polls aggregate drop data on a Cumulus Linux 5.18 switch?

A. what-just-happened poll --data aggregates (the older command name)
B. nv set router adaptive-routing state enabled
C. nv-wjh-cli poll --data aggregates
D. ib_write_bw -d mlx5_0 -a

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In 5.18 the documented command is nv-wjh-cli poll with --data drops, aggregates or l1. The what-just-happened service name belongs to releases up to 5.17.
</details>

---

### Question 12
**Section 3. Scenario:** Which component of an InfiniBand fabric discovers topology, assigns LIDs and computes routes?

A. The Kubernetes scheduler
B. A BGP route reflector
C. The PFC watchdog
D. The subnet manager

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The SM is the control plane for InfiniBand: it discovers the fabric, assigns addresses, programs routes and applies partitions and QoS.
</details>

---

### Question 13
**Section 3. Scenario:** UFM is deployed in high availability mode. What happens if the active server fails?

A. The standby server takes over fabric management
B. The fabric stops forwarding traffic
C. All PKeys are deleted
D. Adaptive routing is permanently disabled

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UFM HA is active/standby, kept in sync by heartbeat and DRBD services, so a secondary can take over management tasks if the primary goes down.
</details>

---

### Question 14
**Section 3. Scenario:** In partitions.conf, a port GUID is listed with no membership keyword. What membership does it receive?

A. Limited membership
B. Full membership
C. No membership
D. Both full and limited

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The NVIDIA SM manual states that when membership is omitted (or unrecognized), limited membership is assumed.
</details>

---

### Question 15
**Section 3. Scenario:** Which InfiniBand adaptive routing algorithm groups all ports with minimal hops to the destination and suits fat-tree topologies?

A. LAG
B. TREE
C. DF_PLUS
D. Torus-2QoS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The bring-up guide lists LAG (ports to the same remote switch, for torus and mesh), TREE (minimal hops to destination, for fat-tree variants) and DF_PLUS (Dragonfly plus).
</details>

---

### Question 16
**Section 3. Scenario:** A fat-tree InfiniBand fabric must stop using adaptive routing. What is the documented change?

A. Set ar_updn in the switch BIOS
B. Delete the root GUID file
C. Change routing_engine in opensm.conf to a non-AR engine such as updn and signal OpenSM with pkill -HUP opensm
D. Run ibnodes on every host

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The bring-up guide says AR is on by default through the ar_updn routing engine; to disable it, set a non-AR engine (for example updn) and run pkill -HUP opensm after the change.
</details>

---

### Question 17
**Section 3. Scenario:** Which opensm.conf settings does the bring-up guide recommend for QoS?

A. qos FALSE and max_op_vls 0
B. routing_engine torus-2QoS only
C. shield_mode off
D. qos TRUE and max_op_vls 2, with an SL-to-VL map

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The recommended configuration sets max_op_vls 2, qos TRUE and qos_sl2vl (0,0,1,1,...), then restarts ufm_ha_cluster.
</details>

---

### Question 18
**Section 3. Scenario:** What does SHIELD (fast link fault recovery) allow an InfiniBand switch to do?

A. Choose an alternative output port when the port in the forwarding table is not Armed or Active, without waiting for the subnet manager
B. Create new partitions
C. Encrypt traffic between hosts
D. Raise the MTU on a link

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SHIELD lets a switch pick an alternative output port quickly after a link fault, which gives the fastest recovery from link flaps or neighbor reboots; it is enabled by default through shield_mode.
</details>

---

### Question 19
**Section 3. Scenario:** After an InfiniBand OpenSM log shows trap 131 repeatedly on one cable, what does the bring-up guide say it indicates?

A. A bad cable connected
B. Bad partitions
C. A change in node description
D. A successful failover

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The guide's table: TIMEOUT means a bad cable somewhere, trap 128 a link state change, trap 131 a bad cable, trap 144 a change in width, speed or description, traps 257-259 bad partitions.
</details>

---

### Question 20
**Section 4. Scenario:** Which Kubernetes custom resource tells the NVIDIA Network Operator which components, such as the OFED driver and RDMA shared device plugin, to deploy?

A. ClusterRole
B. PodDisruptionBudget
C. StorageClass
D. NicClusterPolicy

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The deployment guide configures the operator through a NicClusterPolicy with fields such as ofedDriver and rdmaSharedDevicePlugin.
</details>

---

### Question 21
**Section 4. Scenario:** A cluster already runs Node Feature Discovery. How should the Network Operator be installed?

A. Uninstall NFD first
B. Label every node as privileged
C. Set nfd.enabled=false in the Helm values so the operator does not deploy a second NFD
D. Disable RDMA in the NicClusterPolicy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The guide says the operator deploys NFD by default and to set nfd.enabled=false if NFD is already running.
</details>

---

### Question 22
**Section 5. Scenario:** An engineer wants to know why packets are being dropped on a Spectrum switch right now, by layer and reason. Which tool?

A. ibnodes
B. cl-resource-query
C. nvidia.nvue
D. What Just Happened (WJH)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** WJH diagnoses dropped packets across layers 1, 2, 3, tunnel, buffer and ACL and reports reasons. cl-resource-query shows hardware table use, and ibnodes is an InfiniBand node listing.
</details>

---

### Question 23
**Section 5. Scenario:** A host-memory ib_write_bw test shows good bandwidth but a GPU-memory test is far lower. What does the NCCL troubleshooting guide suggest?

A. A GPUDirect RDMA path problem worth investigating
B. The Network Operator is not installed
C. The subnet manager is the standby
D. PFC is set to priority 0

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The guide says a large gap between host-memory and GPU-memory results points to a GPUDirect RDMA path problem.
</details>

---

### Question 24
**Section 5. Scenario:** Bandwidth tests pass but jobs show stalls and long tails. Which test should be run next?

A. ibnodes on a single host
B. ib_write_lat between the same nodes
C. A second ib_write_bw with a larger message
D. nv unset qos roce

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NVIDIA's guide notes that bandwidth can look healthy while tail latency is poor and recommends measuring point-to-point latency, plus watching rdma statistic counters.
</details>

---

### Question 25
**Section 5. Scenario:** Which ibstat observation indicates a healthy port?

A. State Init
B. State Armed with the rate downshifted
C. State Down with a link layer of Ethernet
D. State Active, physical state link up, expected link layer and the expected rate

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The guide says Down, Init or Armed indicates a problem, and the link layer and rate should match the fabric without unexpected downshift.
</details>

---

### Question 26
**Section 5. Scenario:** Which tool lists the InfiniBand nodes (channel adapters and switches) in the subnet topology?

A. ibping
B. ib_write_bw
C. ibnodes
D. cl-resource-query

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** ibnodes walks the topology or a saved topology file and extracts the nodes; iblinkinfo reports link information per port, and ibping checks connectivity.
</details>

---

### Question 27
**Section 5. Scenario:** In UFM, where do you run a Fabric Health report?

A. Fabric Segmentation
B. The NVUE REST API
C. The Network Operator Helm chart
D. System Health, under Fabric Health, with Run New Report

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The bring-up guide gives that path and says the goal is for all sections of the report to be green.
</details>

---

### Question 28
**Section 6. Scenario:** Where does NVUE save the configuration applied at boot?

A. /etc/network/interfaces only
B. /var/lib/ufm/partitions.conf
C. /etc/nvue.d/startup.yaml
D. /etc/opensm/opensm.conf

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The automation guide says NVUE saves the configuration in /etc/nvue.d/startup.yaml.
</details>

---

### Question 29
**Section 6. Scenario:** What is an NVUE snippet applied with nv config patch used for?

A. Installing DOCA drivers
B. Features NVUE does not yet expose; its content is not validated by NVUE
C. Enabling the Kubernetes device plugin
D. Running ib_write_bw

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snippets patch raw YAML into the configuration for unsupported features. NVUE does not parse or validate them, and they can become invalid as NVUE adds the feature.
</details>

---

### Question 30
**Section 6. Scenario:** Which Ansible collection contains modules to interact with devices managed by NVUE?

A. nvidia.doca
B. community.kubernetes only
C. cumulus.opensm
D. nvidia.nvue

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NVIDIA's quick start describes the nvidia.nvue collection with a CLI module, a REST API module and object-specific modules (bridge, router, interface, evpn, mlag, system, vrf, vxlan).
</details>

---

## Where to go deeper

- [NCP-AIN cert page](../nvidia/ai-networking-professional/README.md) - notes, plan, strategy
- **[📖 NVIDIA AI Networking exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/)** - official blueprint
- **[📖 NVIDIA Networking documentation](https://docs.nvidia.com/networking/)** - product docs
