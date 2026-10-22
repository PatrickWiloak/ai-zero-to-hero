---
last-updated: 2026-10-22
---

# NVIDIA-Certified Professional - AI Networking (NCP-AIN) - Fact Sheet

## Quick Reference

**Exam code:** NCP-AIN  
**Duration:** 2 hours  
**Questions:** 70-75  
**Cost:** $400 USD; NVIDIA says lab exercises are being added on November 1 (2026), when the price rises to $500  
**Level:** Professional  
**Validity:** 2 years from issuance  
**Prerequisites:** 2-3 years of hands-on data center networking experience with NVIDIA hardware (recommended)  
**Passing score:** Not published  

**[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/)**

## Exam Blueprint

| Topic | Weight | Where in this guide |
|---|---|---|
| AI Data Center Design and Optimization | 5% | [04 Network topologies](notes/04-network-topologies.md) |
| NVIDIA Spectrum Networking | 30% | [02 Spectrum Ethernet](notes/02-spectrum-ethernet.md), [03 RDMA and RoCE](notes/03-rdma-roce.md) |
| NVIDIA InfiniBand Networking | 30% | [01 InfiniBand](notes/01-infiniband.md) |
| Kubernetes Integration | 5% | Not covered in the notes yet |
| Troubleshooting Tools | 20% | [05 UFM](notes/05-ufm.md) |
| Automation and Configuration | 10% | [02 Spectrum Ethernet](notes/02-spectrum-ethernet.md) (Cumulus Linux, automation) |

> **Blueprint updated 2026-10-22** from [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) (checked 2026-10-22). The notes below were written in May 2026 against an earlier domain list that NVIDIA no longer publishes, so they do not yet map one-to-one onto these topics; topics marked "not covered" need outside study.

## Domain 1: InfiniBand Technology

### InfiniBand Speed Generations

| Generation | Data Rate | Effective BW (per lane) | 4x Port BW |
|-----------|-----------|------------------------|-------------|
| FDR | 14.0625 Gb/s | 13.64 Gb/s | 56 Gb/s |
| EDR | 25 Gb/s | 25 Gb/s | 100 Gb/s |
| HDR | 50 Gb/s | 50 Gb/s | 200 Gb/s |
| NDR | 100 Gb/s | 100 Gb/s | 400 Gb/s |
| XDR | 200 Gb/s | 200 Gb/s | 800 Gb/s |

### InfiniBand Protocol Layers
- **Physical Layer** - Signaling, encoding, link training
- **Link Layer** - Packet framing, flow control, error detection
- **Network Layer** - Routing, forwarding between subnets
- **Transport Layer** - End-to-end reliable delivery, QoS
- **Upper Layer Protocols** - Verbs API, MPI, storage protocols

### Subnet Management
- **Subnet Manager (SM)** - Controls fabric configuration and routing
- **Subnet Administrator (SA)** - Provides fabric query interface
- OpenSM - open-source subnet manager
- UFM-based SM - NVIDIA's enterprise subnet manager
- Master/standby SM for high availability

### Key Concepts
- **LID (Local Identifier)** - 16-bit address within a subnet
- **GID (Global Identifier)** - 128-bit globally unique address
- **GUID** - Hardware identifier for ports and nodes
- **Partition Key (P_Key)** - Network isolation mechanism
- **Service Level (SL)** - QoS classification
- **Virtual Lane (VL)** - Traffic separation within a link

**[📖 InfiniBand Documentation](https://docs.nvidia.com/networking/)** - NVIDIA InfiniBand guides

## Domain 2: Spectrum Ethernet

### NVIDIA Spectrum Switch Family

| Platform | Ports | Speed | Use Case |
|----------|-------|-------|----------|
| Spectrum-2 | Up to 64x100GbE | 100GbE | Standard data center |
| Spectrum-3 | Up to 64x400GbE | 400GbE | AI/HPC clusters |
| Spectrum-4 | Up to 64x800GbE | 800GbE | Next-gen AI fabric |

### Cumulus Linux
- Linux-based network operating system for Spectrum switches
- Standard Linux networking tools (ip, bridge, iptables)
- NVUE - NVIDIA network configuration CLI
- Automation via Ansible, Puppet, Salt
- BGP, OSPF, EVPN-VXLAN support
- **[📖 Cumulus Linux Docs](https://docs.nvidia.com/networking-ethernet-software/)** - Switch OS documentation

### NVIDIA DOCA
- Data-center infrastructure on a chip architecture
- SDK for DPU (BlueField) programming
- Network function acceleration
- Security and storage offload
- **[📖 DOCA Documentation](https://docs.nvidia.com/doca/)** - DPU SDK

### Ethernet for AI Features
- RoCE support for RDMA over Ethernet
- Priority Flow Control (PFC) for lossless Ethernet
- ECN (Explicit Congestion Notification)
- Large MTU support (jumbo frames)
- ECMP (Equal Cost Multi-Path) for load balancing

## Domain 3: RDMA and RoCE

### RDMA Fundamentals

**Benefits:**
- Zero-copy data transfer (no CPU involvement)
- Kernel bypass (user-space to NIC directly)
- Low latency (microseconds)
- High throughput (near wire speed)
- Low CPU overhead

**RDMA Operations:**
- **Send/Receive** - Two-sided operations
- **RDMA Write** - One-sided remote memory write
- **RDMA Read** - One-sided remote memory read
- **Atomic** - Remote atomic operations (compare-and-swap)

### RoCE Versions

**RoCE v1:**
- RDMA over Ethernet Layer 2
- Uses Ethertype for RDMA packets
- Limited to single broadcast domain (same VLAN)
- No IP routing support

**RoCE v2:**
- RDMA over UDP/IP
- Routable across subnets
- Standard choice for modern deployments
- Requires lossless Ethernet (PFC or similar)

### Lossless Ethernet Configuration

**Priority Flow Control (PFC):**
- Per-priority pause mechanism
- Prevents packet loss for RDMA traffic
- Configured on specific traffic classes
- Must be consistent across all switches in path
- Risk of deadlock if misconfigured

**Explicit Congestion Notification (ECN):**
- End-to-end congestion notification
- Switches mark packets when queue exceeds threshold
- Receivers echo congestion to senders
- Senders reduce rate in response
- Preferred over PFC for congestion management

**DCQCN (Data Center QoS for Converged Networks):**
- Combines PFC and ECN
- Rate-based congestion control for RoCE
- Widely used in AI data centers
- Implemented in ConnectX adapters

### GPUDirect RDMA
- Direct data path between GPU memory and network adapter
- Bypasses CPU and system memory
- Requires GPU and NIC on same PCIe root complex (or NVSwitch)
- Essential for efficient multi-node GPU communication
- Used by NCCL for distributed training

**[📖 GPUDirect Documentation](https://developer.nvidia.com/gpudirect)** - GPU networking

## Domain 4: Network Topologies for AI

### Fat-Tree
- Standard leaf-spine architecture
- Full bisection bandwidth (non-blocking)
- Predictable latency
- Scales to hundreds of nodes
- Higher switch count at scale

### Rail-Optimized
- Each GPU NIC connects to a dedicated rail switch
- Corresponding ranks across nodes share a rail
- Optimized for all-reduce communication pattern
- Fewer switches than full fat-tree
- Used in DGX SuperPOD reference architecture

### Dragonfly
- Groups connected by global links
- Low diameter (few hops between any two nodes)
- Efficient for very large clusters
- More complex routing algorithms
- Lower cost at extreme scale

### Adaptive Routing
- Dynamically select paths based on congestion
- Avoids hot spots in the fabric
- Supported by InfiniBand and Spectrum switches
- Improves effective bisection bandwidth
- Critical for large-scale AI workloads

## Domain 5: UFM and Network Management

### NVIDIA UFM (Unified Fabric Manager)

**Core Features:**
- Fabric discovery and visualization
- Subnet manager with HA support
- Real-time monitoring and telemetry
- Event management and alerting
- Performance analysis and optimization
- **[📖 UFM Documentation](https://docs.nvidia.com/networking/software/management-software/index.html)**

**UFM Telemetry:**
- Per-port counters (data, errors)
- Latency histogram collection
- Congestion detection
- Traffic pattern analysis
- Historical trend reporting

**UFM Health Monitoring:**
- Link error detection (symbol errors, CRC errors)
- Cable health monitoring
- Switch health status
- Temperature and power monitoring
- Automated fault isolation

### Diagnostics Tools
- `ibdiagnet` - Comprehensive fabric diagnostics
- `ibstat` - Local HCA port status
- `ibswitches` - List switches in fabric
- `perfquery` - Performance counter query
- `smpquery` - Subnet management queries

## Exam Tips

### Key Concepts to Master
1. InfiniBand speed generations and bandwidth calculations
2. RoCE v1 vs v2 differences and configuration
3. PFC and ECN for lossless Ethernet
4. Fat-tree vs rail-optimized topologies
5. UFM capabilities and diagnostic tools
6. GPUDirect RDMA requirements and benefits
