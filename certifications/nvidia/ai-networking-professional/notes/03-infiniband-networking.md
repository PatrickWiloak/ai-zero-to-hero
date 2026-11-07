# Section 3: NVIDIA InfiniBand Networking (30%)

**Last reviewed:** 2026-11-07

InfiniBand is a managed fabric: a subnet manager (SM) discovers the topology, assigns addresses, programs forwarding tables and applies partitions and quality of service. The blueprint's four objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) are initial configuration and provisioning including high availability, partition keys (PKeys) for secure multi-tenancy, QoS and adaptive routing, and using UFM to monitor link status and bandwidth.

The main source here is NVIDIA's InfiniBand Cluster Bring-up Procedure (v1.0) and the NVIDIA SM (OpenSM) manual, both read as PDFs, plus UFM release notes. Nothing was run, as it needs InfiniBand hardware; configuration text is quoted from these documents.

**[📖 InfiniBand Cluster Bring-up Procedure](https://docs.nvidia.com/infiniband-cluster-bring-up-procedure.pdf)** - Planning, deployment, configuration and verification steps for an IB cluster
**[📖 NVIDIA SM (OpenSM)](https://docs.nvidia.com/doca/sdk/nvidia-sm.pdf)** - Partition, QoS and routing configuration

## Initial configuration and provisioning, including HA

The bring-up procedure orders the work: plan the topology and create a point-to-point file and a topology file; confirm topology against the cabling (with UFM); confirm component firmware and software versions; install MLNX_OFED, switch software and firmware; configure switches (initial management configuration, zero touch provisioning, split ports); configure UFM; then verify (SM logs, UFM fabric health, UFM telemetry, events and alarms) and run performance tests.

**Subnet manager.** The SM runs on a switch, on a host with OpenSM, or inside UFM. `sminfo` locates it; the bring-up guide's sample output ends with `SMINFO_MASTER`. `smpquery nd <lid>` shows a node description. Common SM log errors from the guide: `TIMEOUT` (look for a bad cable), trap 128 (link state changed; if frequent on one cable, check the cable), trap 131 (a bad cable), trap 144 (change in link width, speed or node description), and traps 257 to 259 (bad partitions). The guide's diagnostic for a flapping link is to read `LinkDownedCounter` with `perfquery`: a very large counter means a corrupted cable.

**High availability.** For UFM the model is active/standby: if the primary fails or is disconnected from the fabric, a secondary takes over fabric management transparently (UFM release notes; heartbeat and DRBD services keep the pair in step). The bring-up guide installs the UFM HA package on both servers with a DRBD partition, and after a configuration change you "stop and restart the ufm_ha_cluster" (`ufm_ha_cluster stop`, `ufm_ha_cluster start`). OpenSM itself supports multiple SMs where one is master and others standby; the SM priority option was not found in the pages read, so the election rule is not covered here.

**[📖 UFM Enterprise User Manual (v6.23.11 LTS)](https://docs.nvidia.com/networking/display/nvidia-ufm-enterprise-user-manual-v6-23-11-lts-2025-lts-u1.11%20LTS%20(2025%20LTS%20U1).pdf)** - UFM feature list, HA and release notes

- **Subnet manager (SM)** - the control-plane software that discovers an InfiniBand fabric, assigns LIDs, computes routes and applies partitions and QoS; it can run on a switch, a host (OpenSM) or in UFM.
- **UFM HA** - an active/standby pair of UFM servers kept in sync with heartbeat and DRBD so a standby can take over fabric management.
- **LinkDownedCounter** - a port error counter read with `perfquery`; a very high value points to a flapping or corrupted link.

## Partition keys (PKeys) and multi-tenancy

A partition is an InfiniBand isolation domain. Every packet carries a 16-bit PKey; NVIDIA's InfiniBand security guide (via search results) says the top bit of the PKey indicates full or limited membership. A port is placed in a partition by the SM, and members of a partition communicate only within it. In `/etc/opensm/partitions.conf` the NVIDIA SM manual shows:

```
# Not run: partitions.conf examples from the NVIDIA SM manual
Default=0x7fff : ALL, SELF=full ;
NewPartition , ipoib : 0x123456=full, 0x3456789034=limi, 0x2134af2306 ;
ShareIO = 0x80 , defmember=full : 0x123451, 0x123452;
```

The format is `[PartitionName][=PKey][,indx0][,ipoib_bc_flags][,defmember=full|limited] : <port GUID list>`. Port GUIDs may carry `=full`, `=limited` or `=both`, and the manual states that when membership is omitted "limited membership is assumed". The `ipoib` flag creates the IPoIB broadcast group for the partition. The default partition is PKey 0x7fff. The two bits: 0x7fff with the top bit set is 0xffff (full), without it 0x7fff (limited). I checked that arithmetic:

```
0x7fff limited (top bit 0): 0x7fff  full (top bit 1): 0xffff
```

The standard InfiniBand rule is that two limited members cannot communicate with each other, while full members can talk to everyone in the partition. I did not find that rule restated in the NVIDIA pages read here, so treat it as the specification's rule, unverified in this guide. That rule is what makes shared-service designs work: servers are limited members and a storage or service port is a full member of the same partition, so tenants reach the service but not one another (the `ShareIO` example in the manual is that pattern).

In UFM, PKeys are managed in the Fabric Segmentation view, where ports are associated with defined PKeys and QoS parameters (MTU, rate, service level) are set per PKey; release notes for 6.14 and later add REST API calls to add or remove hosts from PKeys. The management PKey's MTU and SL can only be changed through the PKey management interface (GUI or REST API), per the UFM 6.11.2 notes.

- **PKey (partition key)** - a 16-bit value carried in every InfiniBand packet that defines which partition (isolation domain) the traffic belongs to.
- **Full and limited membership** - the two membership types of a partition member, shown by the top bit of the PKey; limited is assumed when membership is omitted in partitions.conf.
- **partitions.conf** - the OpenSM file that defines partitions, their PKeys and member port GUIDs.
- **Fabric segmentation** - UFM's feature for assigning ports to PKeys and setting per-partition QoS parameters.

## QoS and adaptive routing

**QoS.** InfiniBand QoS maps service levels (SL) to virtual lanes (VL). The bring-up guide's recommended settings go in OpenSM's configuration file:

```
# Not run: from the bring-up guide, /opt/ufm/files/conf/opensm/opensm.conf
max_op_vls 2
qos TRUE
qos_sl2vl 0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1
```

then restart with `ufm_ha_cluster stop` and `ufm_ha_cluster start`. The NVIDIA SM manual adds that SL2VL and VL arbitration tables belong in the OpenSM options file, and that QoS is off unless enabled. A search result from UFM documentation says QoS is `False` by default in UFM's opensm.conf.

**Adaptive routing (AR).** Per the bring-up guide, AR lets the switch select the output port based on the port's load. The SM scans the fabric, identifies switches that support AR and configures AR groups and AR LFT tables, using one of three algorithms: **LAG** (all ports to the same remote switch form a group, for topologies with multiple links between switches such as torus), **TREE** (ports with minimal hops to the destination, for fat-tree and variants), and **DF_PLUS** (for Dragonfly plus). "AR is enabled by default in the opensm.conf file", the `routing_engine` default is `ar_updn` (for fat-tree), and to disable AR you change `routing_engine` to a non-AR engine (the guide's example is `updn`); apply with `pkill -HUP opensm`. It recommends setting the root GUID file (`root_guid_file`).

Related resilience features in the same section: **SHIELD** (fast link fault recovery, which lets the switch choose an alternative output port when the port in the forwarding table is not Armed/Active, without the SM), **Fast Link Fault Notification** (fat-tree only) and **Adaptive Routing Notification (ARN)**, which makes a congested switch tell its neighbors to choose other ports. SHIELD is on by default through `shield_mode`.

- **Service level (SL) and virtual lane (VL)** - the QoS tag in an InfiniBand packet (SL) and the independent buffer queue on a link (VL); an SL-to-VL map decides which VL carries each class.
- **Adaptive routing (InfiniBand)** - switch-side output port selection by load, configured by the subnet manager using LAG, TREE or DF_PLUS grouping.
- **SHIELD** - InfiniBand fast link fault recovery: switches choose an alternative port when a link fails, without waiting for the SM.
- **ARN** - Adaptive Routing Notification: a congested switch tells neighbor switches to pick another output port.

## Using UFM to monitor links and bandwidth

UFM (Unified Fabric Manager) is the management and monitoring platform for the fabric. From the bring-up guide: UFM Telemetry "collects over 120 unique counters (BER, Temperature, Histograms, Retransmissions, and many more) for each port" to predict problems; the Fabric Health report runs a series of checks (summary table of errors and warnings, a fabric summary, and per-check detail) from the System Health tab, "Run New Report"; and Events and Alarms report faults. Link status (active, down, error counters) and bandwidth utilization come from the same telemetry. UFM also provides a REST API, a readiness check and periodic health reports (release notes), and UFM Infra gives access to the REST API within about 3 seconds after failover (v6.21.0 notes).

- **UFM (Unified Fabric Manager)** - NVIDIA's platform for InfiniBand fabric management, telemetry, health checks, events and partitioning.
- **UFM Telemetry** - the UFM component that collects per-port counters (error rates, temperature, histograms, retransmissions) for monitoring and prediction.

## Check yourself against the objectives

Order the bring-up stages; say where the SM runs and what UFM HA does on failover; read a partitions.conf line including membership; list the QoS settings and what AR does and how to turn it off; name the three AR algorithms and their topologies; and say what UFM telemetry and fabric health give you. Questions are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
