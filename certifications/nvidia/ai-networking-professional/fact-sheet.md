---
last-updated: 2026-11-07
---

# NVIDIA-Certified Professional - AI Networking (NCP-AIN) - Fact Sheet

## Quick Reference

**Exam code:** NCP-AIN  
**Exam name:** NVIDIA AI Networking Certification Exam  
**Duration:** 2 hours  
**Questions:** 70-75  
**Cost:** $500 USD (exam page, 2026-11-07)  
**Format:** Includes a hands-on lab; pass/fail; Certiverse account required  
**Level:** Professional  
**Validity:** 2 years from issuance  
**Languages:** English  
**Prerequisites:** None formal; 2-3 years of hands-on data center networking experience recommended  
**Passing score:** Not published  

**[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/)** - Blueprint, price and registration

## Exam Blueprint

| Topic | Weight | Note |
|---|---|---|
| AI Data Center Design and Optimization | 5% | [01](notes/01-ai-data-center-design.md) |
| NVIDIA Spectrum Networking | 30% | [02](notes/02-spectrum-networking.md) |
| NVIDIA InfiniBand Networking | 30% | [03](notes/03-infiniband-networking.md) |
| Kubernetes Integration | 5% | [04](notes/04-kubernetes-integration.md) |
| Troubleshooting Tools | 20% | [05](notes/05-troubleshooting-tools.md) |
| Automation and Configuration | 10% | [06](notes/06-automation-and-configuration.md) |

## Key Facts by Section

### 1 Design

**[📖 HGX AI Factory network architecture](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/network-logical-architecture.html)** - Compute, converged and out-of-band networks
- Compute (east-west) fabric: RDMA leaf-spine, nonblocking fat-tree of Spectrum-X; converged north-south carries storage and in-band management; separate 1 Gb out-of-band network
- GPUs of the same index share a rail; scalable unit in this reference architecture = 4 compute nodes

### 2 Spectrum

**[📖 RoCE on Cumulus Linux](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/)** - NVUE RoCE commands
- `nv set qos roce` (lossless, default: PFC priority 3 plus ECN); `nv set qos roce mode lossy` (ECN only); verify with `nv show qos roce`
- Adaptive routing: `nv set router adaptive-routing state enabled`; Spectrum-4 at 400G/200G only; reloads switchd
- EVPN multi-tenancy: tenant VRF plus L3 VNI (`nv set vrf RED evpn vni 4001`)
- WJH: `nv set system wjh channel ...`, `nv-wjh-cli poll`; disable on-switch WJH when the NetQ agent runs
- DOCA host install: `apt install -y doca-all mlnx-fw-updater` after DKMS and kernel headers

### 3 InfiniBand

**[📖 InfiniBand Cluster Bring-up Procedure](https://docs.nvidia.com/infiniband-cluster-bring-up-procedure.pdf)** - Bring-up, AR, QoS and verification
- SM discovers, addresses and routes; UFM HA is active/standby (heartbeat and DRBD)
- PKeys defined in partitions.conf; default 0x7fff; membership defaults to limited
- AR on by default in opensm.conf (`routing_engine ar_updn`); algorithms LAG, TREE, DF_PLUS
- QoS: `qos TRUE`, `max_op_vls 2`, `qos_sl2vl`

### 4 Kubernetes

**[📖 Network Operator deployment guide](https://docs.nvidia.com/networking/display/kubernetes2570/deployment-guide-kubernetes.html)** - Helm and NicClusterPolicy
- `helm install network-operator nvidia/network-operator -n nvidia-network-operator --create-namespace`
- NicClusterPolicy: `ofedDriver` plus `rdmaSharedDevicePlugin`; NFD required

### 5 Troubleshooting

**[📖 NCCL networking troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)** - ibstat, ib_write_bw, ib_write_lat
- `ibstat` port Active and expected rate; `ib_write_bw` then `ib_write_lat`; GPU-memory variant with `--use_cuda`
- `ibnodes`, `iblinkinfo`, `ibping`, `ibdiagnet`; UFM System Health, Fabric Health report

### 6 Automation

**[📖 Automation with Cumulus Linux](https://docs.nvidia.com/networking-ethernet-software/guides/Data-Center-Network-Automation-Quick-Start-Guide/Automation-with-Cumulus-Linux)** - NVUE CLI, REST API, startup.yaml, nvidia.nvue
- NVUE saves to `/etc/nvue.d/startup.yaml`; `nv config patch` applies snippets; `nvidia.nvue` has CLI, REST and object modules
