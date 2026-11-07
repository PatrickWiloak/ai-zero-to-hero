# NVIDIA-Certified Professional - AI Networking (NCP-AIN)

**Last reviewed:** 2026-11-07, against the [official exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/).

## Exam Overview

The exam validates deploying, configuring, managing and troubleshooting NVIDIA networking for AI data centers: Spectrum Ethernet, InfiniBand, Kubernetes integration and automation. NVIDIA's name for it is "NVIDIA AI Networking Certification Exam"; the code is **NCP-AIN** (this guide called it NCP-NET until 2026-10-22).

**Exam facts (from the exam page, 2026-11-07):**
- **Exam code:** NCP-AIN
- **Duration:** 2 hours
- **Questions:** 70-75
- **Price:** $500
- **Format:** Includes a hands-on lab ("Hands-on lab: Yes"); the page gives no further detail. Scoring is pass/fail, and you need a Certiverse account to take the exam
- **Level:** Professional
- **Validity:** Two years from issuance; recertify by retaking the exam
- **Languages:** English
- **Prerequisites:** None formal. Recommended: 2-3 years of hands-on data center networking experience
- **Passing score:** Not published
- **Credential:** Digital badge and optional certificate

## Exam Blueprint

Six sections, in NVIDIA's order. Each note covers one section, objective by objective.

| # | Section | Weight | Note |
|---|---------|-------:|------|
| 1 | AI Data Center Design and Optimization | 5% | [01-ai-data-center-design.md](notes/01-ai-data-center-design.md) |
| 2 | NVIDIA Spectrum Networking | 30% | [02-spectrum-networking.md](notes/02-spectrum-networking.md) |
| 3 | NVIDIA InfiniBand Networking | 30% | [03-infiniband-networking.md](notes/03-infiniband-networking.md) |
| 4 | Kubernetes Integration | 5% | [04-kubernetes-integration.md](notes/04-kubernetes-integration.md) |
| 5 | Troubleshooting Tools | 20% | [05-troubleshooting-tools.md](notes/05-troubleshooting-tools.md) |
| 6 | Automation and Configuration | 10% | [06-automation-and-configuration.md](notes/06-automation-and-configuration.md) |

The notes were rewritten on 2026-11-07 to match this blueprint one-to-one. The earlier notes were written in May 2026 against a domain list NVIDIA no longer publishes; Kubernetes, debugging tools and automation were missing and are now covered.

## What is and is not covered at command level

Everything on this exam needs NVIDIA hardware or a simulator, so no command in these notes was run; each is quoted from NVIDIA documentation and labelled. Gaps the sources could not fill are said in the notes: the DSX Air user guide, `ibdiagnet`'s manual page, SuperNIC congestion-control mechanics, the PFC watchdog (not on the RoCE page), and the exact OpenSM tie-break between equal priorities (the man page confirms priority and GUID decide the master).

## NVIDIA's recommended training (as listed on the exam page)

- InfiniBand Essentials and InfiniBand Network Administration (NVIDIA Academy)
- Cumulus Linux Essentials (NVIDIA Academy)

The exam page links these courses and lists many suggested readings for each section; see the [exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/) for the links.

## Quick Links

- **[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/ai-networking-professional/)** - blueprint, price, registration
- **[📖 NVIDIA Networking Documentation](https://docs.nvidia.com/networking/)** - networking product docs
- **[📖 Cumulus Linux documentation](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/)** - Spectrum switch operating system

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Logistics, blueprint and key facts with documentation links |
| [practice-plan.md](practice-plan.md) | Study schedule |
| [scenarios.md](scenarios.md) | Troubleshooting and design scenarios |
| [strategy.md](strategy.md) | Exam tactics |
| [notes/](notes/01-ai-data-center-design.md) | The six section notes |
