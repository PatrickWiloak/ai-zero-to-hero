# NCP-AIN - Exam Strategy

**Last reviewed:** 2026-11-07

## What the exam looks like

Two hours, 70 to 75 questions, and a hands-on lab (NVIDIA's exam page says "Hands-on lab: Yes" and gives no detail). Spectrum and InfiniBand together are 60 percent, troubleshooting 20 percent. The blueprint verbs are practical ("configure", "diagnose", "use"), so expect command-level and scenario questions rather than definitions.

## Tactics

1. **Identify the fabric first.** A question about PKeys, the subnet manager, UFM or `ibstat` is InfiniBand; PFC, ECN, NVUE `nv set qos`, EVPN and WJH are Spectrum Ethernet. Mixing them up is the commonest distractor.
2. **Know what each tool answers.** WJH says why packets were dropped; `cl-resource-query` says whether table space is the problem; `ibstat` says whether the port is up at the right rate; `ib_write_bw` says bandwidth; `ib_write_lat` says latency; UFM Fabric Health says whether the whole fabric is clean.
3. **Remember the defaults.** NVUE RoCE defaults to lossless with PFC on priority 3; the default partition is 0x7fff; membership defaults to limited; AR is on by default in opensm.conf with `ar_updn`; WJH runs by default on Cumulus Linux.
4. **Remember the conflicts.** NetQ agent on the switch means the on-switch WJH service is off; AR and non-AR ports should not share an ECMP route; changing AR state reloads switchd.
5. **For a lab, read the output.** Do not just type the verification command; check that the mode, priority, thresholds and trust mode match what was asked.
6. **Check the release.** Command spellings change across Cumulus Linux releases (for example `enable on` versus `state enabled` for adaptive routing). Use the syntax of the release shown in the question.
