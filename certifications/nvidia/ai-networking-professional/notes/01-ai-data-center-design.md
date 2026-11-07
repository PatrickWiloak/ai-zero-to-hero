# Section 1: AI Data Center Design and Optimization (5%)

**Last reviewed:** 2026-11-07

The smallest section by weight, and the one that sets the vocabulary for the rest: what an AI factory network is made of, why GPUs are wired in rails, and what GPU-to-GPU communication demands of the fabric. The three objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) (checked 2026-11-07) are to describe an AI factory networking architecture and its components, to describe rail-optimized topologies, and to describe GPU-to-GPU communications.

None of the commands in this guide can be run without NVIDIA switches, NICs or a simulator, so any code or CLI text is quoted from NVIDIA documentation and marked as not run.

## An AI factory network is several networks, not one

A training cluster is not wired as one big Ethernet. NVIDIA's HGX AI Factory reference architecture describes separate networks for separate jobs:

- **The compute (east-west) fabric** carries GPU-to-GPU traffic. The docs call it "an RDMA based fabric in a leaf-spine architecture", built from Spectrum-X switches in a full nonblocking fat-tree.
- **The converged (north-south) network** carries node communication with storage, in-band management and end users. Each node connects with two 400 GbE ports to two separate switches for redundancy, and storage is principally attached here.
- **The out-of-band management network** is a separate 1 Gb network for BMC ports on servers, DPUs and SuperNICs and for switch management ports, using low-cost bulk management switches.

**[📖 Networking logical architecture - HGX AI Factory](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/network-logical-architecture.html)** - The compute, converged and out-of-band networks, rails and scalable units

The reason for the split is that the traffic is different. Training traffic between GPUs is bursty, synchronized and extremely sensitive to loss and imbalance, so it gets its own lossless, RDMA-capable fabric tuned for it. Storage and management traffic is ordinary traffic that should not compete with it.

### The components

In the same reference architecture each node has eight ConnectX-8 SuperNICs on the compute fabric (each 800 GbE port broken out to 2x400 Gb), and one BlueField-3 B3240 dual-port 400 GbE DPU on the converged fabric. A **SuperNIC** is the NIC end of NVIDIA Spectrum-X: NVIDIA's Spectrum-X docs describe the platform as pairing Spectrum switches with BlueField-3 SuperNIC, ConnectX-7 and ConnectX-8 SuperNIC families to "deliver high-bandwidth, lossless RoCE for the GPU-to-GPU compute (east-west) network". A **DPU** such as BlueField-3 offloads infrastructure work and, in this design, is the node's connection to the north-south network.

**[📖 NVIDIA Spectrum-X Ethernet Networking Platform](https://docs.nvidia.com/networking/display/kubernetes2670/spectrum-x/spectrum-x.html)** - Platform components and NIC families

Deployments are built from **scalable units (SU)**, each of four compute nodes in this reference architecture. Each 4-node SU provides 64 400 Gb compute connections (25.6 Tb/s aggregate), and clusters grow by replicating SUs: 8 SUs make 32 nodes (256 GPUs), 16 make 64 nodes (512 GPUs), 32 make 128 nodes (1,024 GPUs). The size of a unit differs between reference architectures (other NVIDIA documents use other unit sizes), so treat 4 nodes as this document's figure, not a universal one.

- **AI factory network** - the set of separate fabrics (compute, converged north-south, out-of-band management) that connect GPU servers, storage and users in an AI data center.
- **Compute fabric** - the east-west RDMA network that carries GPU-to-GPU traffic during training.
- **Scalable unit (SU)** - a repeatable building block of servers and network ports; clusters scale by replicating SUs.
- **SuperNIC** - an NVIDIA network adapter (such as BlueField-3 SuperNIC or ConnectX-8) used on the Spectrum-X compute fabric for lossless RoCE.
- **BlueField-3 DPU** - a data processing unit that connects a node to the converged north-south network in the enterprise reference architecture.

## Rail-optimized topologies

In a rail-optimized topology the GPUs in the same position in every server share a "rail". The docs say GPUs are "connected using a rail-optimized network topology through their respective SuperNICs". In the dual-plane 256- and 512-GPU designs, each plane's leaf switches serve pairs of rails (1+5, 2+6, 3+7, 4+8).

Why this wiring? Collective operations such as all-reduce mostly exchange data between GPUs of the same index in different servers. If those GPUs sit on the same rail and therefore the same leaf switch, that traffic crosses one switch hop instead of going up to the spine. Traffic between different rails or beyond the leaf uses the spine. The one-hop rail property is a consequence of the wiring described here; the per-collective traffic pattern comes from how NCCL organizes its communication, which this guide does not fetch, so the rail argument is explained, not benchmarked.

Spectrum-X also supports **Multiplane**: the docs say it "splits each SuperNIC across multiple independent planes", which can scale a flat, two-tier Ethernet fabric to very large GPU counts. The Network Operator exposes this as a `multiplaneMode` field (`none`, `hwplb` for Hardware Multiplane, `swplb` for Software Multiplane) and says Hardware Multiplane is recommended on multiplane platforms; typical single-plane deployments use BlueField-3 on HGX H100/H200/B200 while dual- and quad-plane designs use ConnectX-8 on B300 and GB300 systems.

- **Rail-optimized topology** - a wiring pattern where the GPUs with the same index in each server connect to the same leaf switches, so same-rail traffic stays within one switch hop.
- **Spectrum-X Multiplane** - a Spectrum-X capability that splits each SuperNIC across independent network planes to improve resiliency and scale.

## GPU-to-GPU communication

The compute fabric exists so that GPUs can move tensors to each other directly, without the CPU in the middle. The mechanism is **RDMA** (remote direct memory access) over either InfiniBand or RDMA over Converged Ethernet (RoCE), and with **GPUDirect RDMA** the network adapter reads and writes GPU memory directly. NVIDIA's NCCL networking troubleshooting guide, which compares host-memory and GPU-memory paths with `ib_write_bw --use_cuda`, says a large gap between them points to a GPUDirect RDMA path problem.

**[📖 NCCL networking troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)** - Host versus GPU memory tests and link checks

What this demands of the network is why the later sections look the way they do: very high bandwidth (400 and 800 Gb ports), no packet loss for RoCE (hence PFC and ECN, Section 2), balanced use of all paths (adaptive routing, Sections 2 and 3), and visibility into drops and congestion (WJH, NetQ and UFM, Section 5).

- **RDMA** - remote direct memory access: a NIC moves data directly between the memory of two machines without involving their CPUs in each transfer.
- **GPUDirect RDMA** - a path where the network adapter reads and writes GPU memory directly, avoiding a copy through host memory.

## Check yourself against the objectives

Draw the three networks of an AI factory and say which traffic each carries; say what a SuperNIC, a DPU and a scalable unit are; explain why same-index GPUs share a rail; and say why GPU-to-GPU traffic needs a lossless, RDMA-capable fabric. The questions for this section are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
