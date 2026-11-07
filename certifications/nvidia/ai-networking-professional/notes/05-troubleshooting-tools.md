# Section 5: Troubleshooting Tools (20%)

**Last reviewed:** 2026-11-07

Twenty percent of the exam is knowing which tool answers which question. The objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) (checked 2026-11-07) are: `cl-resource-query` for resource allocation on Spectrum-X; WJH for real-time event analysis; verifying low-latency interconnects between GPUs, CPUs and storage; UFM system health for InfiniBand; and the commands `ib_write_lat`, `ib_write_bw`, `ibping`, `ibstat`, `ibdiagnet`, `ibnodes` and `iblinkinfo`. Nothing here was run (no fabric available); commands come from NVIDIA docs and man pages.

A useful way to hold them: **Ethernet side** asks "is the switch out of table space, and why was this packet dropped?" (`cl-resource-query`, WJH). **Path side** asks "is the link up, and how fast and how low-latency is it?" (`ibstat`, `ib_write_bw`, `ib_write_lat`). **InfiniBand fabric side** asks "which nodes and links exist, and is the whole fabric healthy?" (`ibnodes`, `iblinkinfo`, `ibping`, `ibdiagnet`, UFM).

## cl-resource-query: resource allocation on Spectrum switches

Cumulus Linux synchronizes routes between the kernel and the switching silicon. The docs' point (from the Cumulus Linux resource diagnostics page, search summary of release 5.9) is that when hardware resource pools fill, existing routes can move from fully to partially allocated, so you monitor hardware entries against ASIC limits. `cl-resource-query` reports how many host entries, MAC entries, layer 2 and layer 3 routes and ECMP routes are in use, and on Spectrum switches it also shows ACL TCAM usage. The active forwarding table profile appears in the output; profiles are set with `forwarding_table.profile` in `/etc/cumulus/datapath/traffic.conf` and `switchd` must be restarted after a change. In newer releases the NVUE equivalent is `nv show platform asic <asic-id> resource`.

I could not open the page itself (the current-release URL returned 404), so the sample output and per-platform limits are not reproduced; read the page for your release.

**[📖 Resource Diagnostics Using cl-resource-query (5.9)](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-59/Monitoring-and-Troubleshooting/Resource-Diagnostics-Using-cl-resource-query/)** - Resource counters and forwarding table profiles

- **cl-resource-query** - the Cumulus Linux tool that shows how much of the switch ASIC's forwarding and ACL resources are in use.
- **Forwarding table profile** - the setting that divides the ASIC's memory between MAC, neighbor and route entries.

## WJH: real-time event analysis

WJH explains drops. The channels, triggers and `nv-wjh-cli poll` command are in [Section 2](02-spectrum-networking.md), with the NetQ interaction: with the NetQ agent on the switch, disable the on-switch WJH service. The troubleshooting use is to start at the drop reason, since a drop list that is dominated by buffer drops points at congestion, ACL drops at policy, layer 1 at the cable or optic.

**[📖 What Just Happened (WJH)](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH/)** - WJH channels and `nv-wjh-cli poll`

## Verifying low-latency interconnects: ibstat, ib_write_bw, ib_write_lat

NVIDIA's NCCL networking troubleshooting guide gives the sequence for testing the path between nodes:

1. **`ibstat`** shows per-HCA and per-port status. A healthy port is `Active` (`Down`, `Init` or `Armed` is a problem), has a physical state of link up, a link layer that matches the fabric (InfiniBand, or Ethernet for RoCE) and consistent across the NICs, and a rate matching what the fabric should give, without unexpected downshift. `ibstatus` is a companion summary.
2. **`ib_write_bw`** measures bandwidth. Start the server on one node and point the client at it:

```
# Not run: from the NCCL networking troubleshooting guide
# Server node
ib_write_bw -d mlx5_0 -a
# Client node
ib_write_bw -d mlx5_0 <server_hostname_or_ip> -a
```

   Replace `mlx5_0` with the device `ibstat` shows. To test GPU memory (GPUDirect RDMA), add `--use_cuda=<gpu_id>` (and `--use_cuda_dmabuf` where the kernel, driver and perftest build support it); a large gap between host-memory and GPU-memory results points to a GPUDirect RDMA path problem.
3. **`ib_write_lat`** measures latency with the same server/client pattern: `ib_write_lat -d <device>` on the server and `ib_write_lat -d <device> <server>` on the client. The guide's reasoning: bandwidth can look healthy while tail latency is poor, and high or unstable latency, especially if bandwidth also fluctuates, can indicate congestion, retransmissions or a degraded link.

Two related checks on the same page: `rdma statistic` (watch `rnr_nak_retry_err`, `packet_seq_err`, `implied_nak_seq_err` and `local_ack_timeout_err` during a test; growing values suggest loss or retries), and `mlxlink -d <mst_device>` for link width, speed and error state. For RoCE deployments NVIDIA's examples add `-F` (skip the CPU frequency check) and `--report_gbits`; the GPU Operator docs show an Ethernet run reaching about 92 Gb/s at large message sizes. The GPU Operator example only illustrates the output format, not a target number.

**[📖 NCCL networking troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html)** - `ibstat`, `ib_write_bw` and `ib_write_lat` procedure
**[📖 DOCA Perftest](https://docs.nvidia.com/doca/sdk/doca-perftest/index.html)** - `doca_perftest`, NVIDIA's native replacement for the legacy perftest tools

Verifying "GPUs, CPUs and storage" interconnects follows the same approach on each path: confirm the port is active at the right rate, then measure bandwidth and latency end to end, host memory first and GPU memory second.

- **ibstat** - lists each InfiniBand or RDMA adapter and port with state, physical state, link layer and rate.
- **ib_write_bw** - the perftest tool that measures RDMA write bandwidth between a server and a client.
- **ib_write_lat** - the perftest tool that measures RDMA write latency between a server and a client.

## UFM system health for InfiniBand

In UFM the **System Health** tab holds the Fabric Health report: "Run New Report" executes a series of checks and shows a summary table of errors and warnings, a fabric summary of devices and ports, and the results of each check, and the goal after bring-up is that every section is green (NVIDIA's bring-up guide). UFM Telemetry gives per-port counters (over 120 per port) and Events and Alarms flag faults. The SM log gives the lower-level story: `TIMEOUT` (bad cable), trap 128 (link state change), trap 131 (bad cable), trap 144 (link width, speed or description change), traps 257 to 259 (bad partitions).

## ibnodes, iblinkinfo, ibping, ibdiagnet

These come from the infiniband-diags suite and ibdiagnet:

- **`ibnodes`** "either walks the IB subnet topology or uses an already saved topology file and extracts the IB nodes (CAs and switches)". The bring-up guide uses `ibnodes | grep <node-name>` to confirm the tested HCAs appear as active.
- **`iblinkinfo`** "reports link info for each port in an IB fabric, node by node", with optional partial scans.
- **`ibping`** "uses vendor mads to validate connectivity between IB nodes" and runs as client/server: `-S` starts a server that does not return control, and the client takes a destination LID or GUID (`-L` marks a LID).
- **`ibdiagnet`** is the fabric diagnostic tool: the NVIDIA documents I read list it (with a Topology Comparison feature in the user manual contents) but its user manual page was not retrievable, so its checks and output are not described here.

The infiniband-diags tools "use directed route MADs", so they "may therefore work even in unconfigured subnets" (man page summary). **[📖 ibping man page](https://man7.org/linux/man-pages/man8/ibping.8.html)** - Description and options.

- **ibnodes** - lists the InfiniBand nodes (channel adapters and switches) in the subnet topology.
- **iblinkinfo** - reports link information for each port in the fabric, node by node.
- **ibping** - validates connectivity between InfiniBand nodes using vendor management datagrams, in client/server mode.
- **ibdiagnet** - the NVIDIA InfiniBand fabric diagnostic tool.

## Choosing the tool

| Symptom | First tool |
|---|---|
| New routes will not install, tables look full | `cl-resource-query` / `nv show platform asic ... resource` |
| Packets disappear, you need the reason | WJH (`nv-wjh-cli poll`, `netq show wjh-drop`) |
| A port is not at the speed you expect | `ibstat`, `mlxlink` |
| Throughput lower than the link rate | `ib_write_bw`, then GPU-memory variant |
| Throughput fine but stalls and jitter | `ib_write_lat`, `rdma statistic` |
| Which nodes are visible? | `ibnodes` |
| Which links are degraded fabric-wide? | `iblinkinfo`, UFM Fabric Health |
| Is node A reachable from node B at IB level? | `ibping` |
| Flapping link | SM log traps, `perfquery` LinkDownedCounter |

## Check yourself against the objectives

Say what each of the listed tools answers; run the host-memory then GPU-memory bandwidth test; explain why a latency test is a separate step; and read an SM log trap code. Questions are in the [NCP-AIN practice bank](../../../practice-questions/nvidia-ai-networking-professional.md).
