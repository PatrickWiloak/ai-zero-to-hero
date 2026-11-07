# NCP-AIN - Scenarios

**Last reviewed:** 2026-11-07

Eight original scenarios written for this guide, with answers drawn from the cited NVIDIA documentation.

## 1. Training jobs stall with no obvious packet loss counters

Bandwidth tests between two nodes look fine but jobs stall. **Next step:** run `ib_write_lat` (and `rdma statistic` during a test). NVIDIA's NCCL guide says bandwidth can look healthy while tail latency is poor, and growing `local_ack_timeout_err` or `packet_seq_err` suggests loss or retries.

## 2. RoCE is enabled but you cannot tell whether PFC is working

Run `nv show qos roce` and check `pfc-priority 3`, `rx-enabled` and `tx-enabled`, ECN congestion mode and thresholds, then `nv show interface <port> qos roce counters` for the port in question.

## 3. A tenant must be isolated from others on a shared leaf-spine fabric

Put the tenant in its own VRF mapped to an L3 VNI (`nv set vrf RED evpn vni 4001`) with its own route targets, and keep the overlay out of the default VRF. Cumulus Linux does not support an L3 VNI for the default VRF.

## 4. NetQ is installed and WJH data looks duplicated or missing

When the NetQ agent runs on the switch, the on-switch WJH service must be disabled (`nv set system wjh state disabled`), because NetQ exports WJH data itself.

## 5. Two InfiniBand tenants must reach a shared storage port but not each other

Use one partition where the storage port is a full member and tenant ports are limited members (the NVIDIA SM manual's ShareIO pattern). Note the caveat in note 3: the rule that limited members cannot reach each other is the InfiniBand specification's, not restated in the pages used for this guide.

## 6. A fat-tree InfiniBand fabric should stop using adaptive routing

Change `routing_engine` in opensm.conf from `ar_updn` to a non-AR engine such as `updn`, then `pkill -HUP opensm` (NVIDIA bring-up guide). AR is on by default.

## 7. Pods on a new GPU cluster cannot get an RDMA device

Check `kubectl -n nvidia-network-operator get pods`, the NicClusterPolicy (the `rdmaSharedDevicePlugin` resource name and the `ifNames` match the node's real interface), and that the pod's `requests` and `limits` use the exact resource name.

## 8. A leaf's route table stops accepting entries

Check hardware resources with `cl-resource-query` (or `nv show platform asic <asic-id> resource` in newer releases) and the forwarding table profile.
