# Section 2: NVIDIA Spectrum Networking (30%)

**Last reviewed:** 2026-11-07

Spectrum-X is NVIDIA's Ethernet platform for AI: Spectrum switches running Cumulus Linux, with SuperNICs on the servers, carrying RDMA over Converged Ethernet (RoCE). This section is 30 percent of the exam and has the most objectives. They follow [NVIDIA's blueprint](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) in order: configure RoCE; enable and verify QoS, ECN and PFC (and verify adaptive routing and telemetry); BGP-EVPN multi-tenancy; DSX Air; WJH and in-band telemetry; NetQ; DOCA installation; and SuperNIC functionality.

Everything here needs Spectrum hardware or NVIDIA's simulator, so nothing was run. Commands are quoted from NVIDIA documentation (Cumulus Linux 5.18 unless stated) and syntax changes between releases, so check the page for your release before using any of it.

## Why RoCE needs configuring: lossless Ethernet

RDMA over Ethernet performs badly when packets are dropped, so a RoCE fabric is engineered to avoid loss and to tell senders to slow down before queues overflow. Two mechanisms do that:

- **ECN (explicit congestion notification)** marks packets when a queue grows past a threshold, so the receiver can signal the sender to slow down before loss happens.
- **PFC (priority flow control)** pauses a single traffic class on a link when a buffer fills, so RoCE traffic is not dropped. It acts per priority, not on the whole port.

NVIDIA's RoCE page describes two modes: **lossless** (PFC plus ECN) and **lossy** (ECN only). The NVUE default is lossless.

## Configure Spectrum-X switches for RoCE

**[📖 RDMA over Converged Ethernet - RoCE (Cumulus Linux)](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/)** - NVUE commands, default values and verification

```
# Not run: needs a Spectrum switch running Cumulus Linux (from the NVIDIA docs, 5.18)
cumulus@switch:~$ nv set qos roce
cumulus@switch:~$ nv config apply
```

The page says "NVUE defaults to RoCE lossless", and that `nv set qos roce` and `nv set qos roce mode lossless` are equivalent. Lossy mode is `nv set qos roce mode lossy`. The page also lists `lossless-single-ipool`, `lossy-multi-tc` and `dci-1` (marked Beta, Spectrum-4 through Spectrum-6), and `nv unset qos roce` removes the configuration. Search results for older releases show different spellings for these commands, which is why the exam-prep habit is to read the page for the release in front of you.

Defaults from the page: PFC is enabled on switch priority 3 (the RoCE traffic class) in lossless mode only. The page's table gives the ECN absolute threshold for traffic class 3, and for Spectrum-4 it says the system-level ECN minimum threshold value intended for programming is 150,000 bytes (the hardware programs 159,744 bytes). The sample output shows `pfc-priority 3`, `congestion-mode ECN`, `enabled-tc 0,3`, a min-threshold of 146.48 KB and max-threshold of 1.43 MB, and `trust-mode pcp,dscp`.

- **RoCE (RDMA over Converged Ethernet)** - RDMA carried over Ethernet, which depends on a lossless or near-lossless fabric.
- **Lossless RoCE mode** - the NVUE RoCE mode that enables PFC on the RoCE priority together with ECN; it is the default.
- **Lossy RoCE mode** - the NVUE RoCE mode that uses ECN without PFC.
- **PFC** - priority flow control: pauses one traffic class on a link when buffers fill so RoCE traffic is not dropped.
- **ECN** - explicit congestion notification: marks packets when a queue passes a threshold so senders slow down before loss occurs.

## Enable and verify QoS, ECN and PFC

Verification is a set of `nv show` commands, all from the same page:

```
nv show qos roce
nv show interface <interface-id> qos roce status
nv show interface <interface-id> qos roce counters
nv show interface <interface> qos roce status pool-map
nv action clear interface <interface-id> qos roce counters
```

Read `nv show qos roce` as a checklist: the mode matches what you intended, PFC priority 3 is enabled in both directions (`rx-enabled`, `tx-enabled`), congestion mode is ECN with thresholds in place for the RoCE traffic class, and the trust mode (`pcp,dscp`) matches how the servers mark RoCE traffic. Per-interface status and counters then show whether the policy is actually working on a given port. The page does not describe a PFC watchdog, so it is not covered here.

## Adaptive routing and telemetry

Adaptive routing (AR) on Spectrum-X switches is load balancing that picks the path per packet from switch state such as queue occupancy and port utilization, rather than from a flow hash. The Cumulus Linux 5.18 page lists tight conditions: only the Spectrum-X platform with Spectrum-4 ASICs at 400G or 200G (not 800G links), RoCE2 unicast and VXLAN-encapsulated RoCE traffic, layer 3 interfaces only (not subinterfaces, SVIs, bonds or bond members), and no resilient hashing. Do not mix AR and non-AR ports in the same ECMP route; the page warns this can cause "Unexpected route hashing".

**[📖 Equal Cost Multipath Load Sharing - Adaptive Routing](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-3/Routing/Equal-Cost-Multipath-Load-Sharing/)** - Adaptive routing commands, restrictions and link utilization

```
# Not run: from the NVIDIA docs (5.18)
nv set router adaptive-routing state enabled
nv set interface <interface-id> router adaptive-routing state enabled
nv config apply
nv show router adaptive-routing
```

The page says changing the state "reloads the switchd service". Older documentation (5.6 and 5.13, from search results) uses `enable on` instead of `state enabled`, so again check your release. Link utilization (default threshold 70 percent, off by default) needs the `profile-custom`.

Telemetry on this platform comes from two places: the switch's own counters and the WJH service (below), and NetQ, which gathers both across the fabric.

## BGP-EVPN for multi-tenancy

EVPN is "a standards-based control plane for VXLAN" with "inherent support for multi-tenancy". For a fabric shared by tenants, each tenant gets its own VRF, and each VRF maps to one L3 VNI. The L3 VNI in the VXLAN header tells the egress VTEP which VRF to route in, and per-tenant route targets keep EVPN routes separate.

**[📖 Ethernet Virtual Private Network - EVPN](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/)** - EVPN overview and multi-tenancy
**[📖 EVPN basic configuration](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration/)** - VXLAN source address, VLAN to VNI, BGP address family
**[📖 EVPN inter-subnet routing](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/)** - Tenant VRF and L3 VNI

```
# Not run: from the NVIDIA docs
nv set nve vxlan source address 10.10.10.1
nv set evpn state enabled
nv set bridge domain br_default vlan 10 vni 10
nv set vrf default router bgp address-family l2vpn-evpn state enabled
nv set vrf default router bgp neighbor swp51 address-family l2vpn-evpn state enabled
# tenant VRF with an L3 VNI
nv set vrf RED evpn vni 4001
nv set vrf RED router bgp address-family ipv4-unicast route-export to-evpn state enabled
nv config apply
```

Three rules from the pages: the overlay goes in dedicated VRFs, separate from the underlay in the default VRF; Cumulus Linux does not support L3 VNI mapping for the default VRF; and for layer 2, "there is a direct one-to-one mapping between layer 2 VNIs and VLANs".

- **EVPN** - the standards-based BGP control plane for VXLAN that distributes MAC and IP reachability between VTEPs.
- **L3 VNI** - the VXLAN network identifier that maps a tenant VRF so routed traffic stays inside that tenant.
- **VRF** - a virtual routing and forwarding instance: a separate routing table per tenant.

## NVIDIA DSX Air

DSX Air is NVIDIA's cloud-based simulation platform for AI factories. NVIDIA describes it as software-as-a-service for logically simulating AI factories, able to model Spectrum-X switches, ConnectX SuperNICs, BlueField DPUs and the NetQ, Run:ai and Base Command Manager software, for both east-west and north-south networks. It is used to test provisioning, automation and security policy before hardware ships, applying changes to the live environment only after they succeed in simulation. The exam objective is to "use NVIDIA DSX Air to simulate network environments and identify potential issues": that is the use case. I could not retrieve the DSX Air user guide, so how to build a topology in the product is not covered here.

**[📖 NVIDIA DSX Air accelerated simulation for AI factories](https://blogs.nvidia.com/blog/dsx-air-simulation-ai-factories)** - What DSX Air models and why it is used

- **DSX Air** - NVIDIA's cloud-based platform for simulating AI factory networks and software before hardware is installed.

## WJH and in-band telemetry

**What Just Happened (WJH)** gives real-time visibility into network problems with two components: an agent that streams telemetry for off-switch analysis (such as NetQ), and a service that diagnoses dropped packets across layers 1, 2, 3, tunnel, buffer and ACL. The docs say Cumulus Linux enables and runs the WJH service by default. Drops are grouped into channels:

```
# Not run: from the NVIDIA docs (5.18)
nv set system wjh channel forwarding trigger l2
nv set system wjh channel layer-1 trigger l1
nv set system wjh channel buffer trigger buffer
nv config apply
nv show system wjh channel
nv-wjh-cli poll --data aggregates
```

A channel name is 4 to 16 characters, and a trigger can be enabled for only one channel. `nv-wjh-cli poll` accepts `--data drops|aggregates|l1`, `--output-type table|json|pcap` and `--channels`. Be careful: some search summaries quote `what-just-happened poll`, which is the older command; the 5.18 page uses `nv-wjh-cli`.

**[📖 What Just Happened (WJH)](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH/)** - Channels, triggers, polling and the NetQ interaction

**Congestion or packet loss diagnosis** is therefore a short loop: the WJH output gives the drop reason (for example buffer drops point to congestion, ACL drops to policy, layer 1 to physical problems) and the interface counters from `nv show interface <interface-id> qos roce counters` show whether PFC and ECN reacted. NVIDIA's docs do not define an in-band telemetry procedure in the pages fetched, so treat "in-band telemetry" as the switch and NIC telemetry that NetQ collects, and check NVIDIA's Spectrum-X documentation for the specific feature.

- **WJH (What Just Happened)** - the switch service and agent that report why packets were dropped, grouped by layer and channel.
- **Channel (WJH)** - a named group of WJH drop triggers (forwarding, layer-1, buffer, ACL) with its own polling interval and cache size.

## NetQ

NetQ is NVIDIA's network monitoring and management platform. It collects telemetry, including WJH data, and offers a UI and a CLI. From the NetQ WJH page: `netq config add agent wjh` enables collection (then restart the agent), `netq show wjh-drop` shows drop counts by type with `details` adding reasons, `netq show wjh-drop l1 port-aggregate` groups layer 1 errors by ingress port, and `netq config add agent wjh-threshold` sets latency and congestion thresholds. Latency and congestion monitoring needs Spectrum-2 or later (NetQ 5.2 page).

There is an interaction to remember: when the NetQ agent is on the switch, the on-switch WJH service must be disabled, because NetQ exports WJH data itself:

```
nv set system wjh state disabled
nv config apply
```

**[📖 Configure and monitor WJH events (NetQ 5.2)](https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-52/Manage-Events-and-Notifications/Monitor-WJH-Events/)** - NetQ commands for drop events and thresholds

- **NetQ** - NVIDIA's fabric-wide monitoring platform that collects switch telemetry, events and WJH data, with a UI and CLI.

## Install NVIDIA DOCA

DOCA is the software framework and driver stack for BlueField DPUs and ConnectX/SuperNIC adapters. On a host the workflow is: install the DOCA host repository package, then install a profile; for the full set, `apt install -y doca-all mlnx-fw-updater` on Debian-family systems (`yum` on RPM systems). Before that, install DKMS and kernel headers that match the running kernel. After installation restart the driver and MST services (`/etc/init.d/openibd restart` and `mst restart`). If the kernel is not supported, NVIDIA points to the DOCA Extra Package.

**[📖 DOCA-Host installation and DKMS management](https://docs.nvidia.com/doca/sdk/doca-host-installation-and-dkms-management-guide/index.html)** - Host installation profiles and requirements

- **DOCA** - NVIDIA's SDK and driver framework for BlueField DPUs and ConnectX and SuperNIC adapters; `doca-all` is the full host installation profile.

## SuperNIC functionality

A SuperNIC (BlueField-3 SuperNIC, ConnectX-8) is the server-side half of Spectrum-X. The Spectrum-X pages I fetched say the platform delivers lossless RoCE, mention a "DOCA SPC-X CC Algorithm Package" for congestion control and "SPC-X optimizations", and show the Kubernetes Network Operator discovering NICs, configuring rails and exposing them to pods. From 26.7.0, NIC tuning comes from a versioned Spectrum-X profile applied as a labeled ConfigMap and the operator carries no built-in profiles. The mechanics of SuperNIC congestion control and packet processing are not described in the pages I could read, so that part of the objective ("configure SuperNIC functionality for advanced packet processing and congestion control") is not covered at command level here; see [NVIDIA Spectrum-X NIC Configuration](https://docs.nvidia.com/networking/display/kubernetes2670/spectrum-x/spectrum-x-configuration.html).

## Check yourself against the objectives

Explain the roles of PFC and ECN and the difference between lossless and lossy mode; write the RoCE enablement and verification commands; state the adaptive routing restrictions; sketch a tenant with a VRF and L3 VNI; say what WJH and NetQ each report and why only one of them should run on a switch; and describe how DOCA is installed on a host. Questions are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
