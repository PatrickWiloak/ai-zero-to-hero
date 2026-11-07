# NCP-AIN - Study Plan

**Last reviewed:** 2026-11-07

A six-week reading schedule, one week per section for the two big ones, built on the blueprint weights (5 / 30 / 30 / 5 / 20 / 10). No command in this guide can be run without NVIDIA hardware, so hands-on time is best spent in NVIDIA's simulator (DSX Air, described in note 2) or on lab equipment if you have it.

## Week 1: Section 1 (5%) and the Spectrum vocabulary

- [ ] Read [README.md](README.md) and [notes/01-ai-data-center-design.md](notes/01-ai-data-center-design.md)
- [ ] Read NVIDIA's [HGX AI Factory network architecture](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/network-logical-architecture.html) page
- [ ] Start [notes/02-spectrum-networking.md](notes/02-spectrum-networking.md) through the RoCE sections

## Week 2: Section 2 (30%)

- [ ] Finish note 02: adaptive routing, EVPN, DSX Air, WJH, NetQ, DOCA, SuperNIC
- [ ] Read the Cumulus Linux RoCE and EVPN pages the note cites and compare the commands for your release
- [ ] If you have lab access, type the RoCE enable and verify commands and read the output

## Week 3: Section 3 (30%)

- [ ] Read [notes/03-infiniband-networking.md](notes/03-infiniband-networking.md)
- [ ] Read the first chapters of the NVIDIA [InfiniBand Cluster Bring-up Procedure](https://docs.nvidia.com/infiniband-cluster-bring-up-procedure.pdf)
- [ ] Read the partitions section of the [NVIDIA SM manual](https://docs.nvidia.com/doca/sdk/nvidia-sm.pdf) and decode each example line

## Week 4: Sections 4 and 6 (5% and 10%)

- [ ] Read [notes/04-kubernetes-integration.md](notes/04-kubernetes-integration.md) and the Network Operator deployment guide
- [ ] Read [notes/06-automation-and-configuration.md](notes/06-automation-and-configuration.md)

## Week 5: Section 5 (20%)

- [ ] Read [notes/05-troubleshooting-tools.md](notes/05-troubleshooting-tools.md)
- [ ] Read NVIDIA's NCCL networking troubleshooting page end to end

## Week 6: Review

- [ ] Read [scenarios.md](scenarios.md) and [strategy.md](strategy.md)
- [ ] Take the [practice questions](../../practice-questions/nvidia-ai-networking-professional.md) in one sitting and read every explanation
- [ ] Re-read the notes for the sections where you were surprised
- [ ] Recheck the [exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) for blueprint or price changes before booking
