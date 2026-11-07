# NVIDIA-Certified Professional - OpenUSD Development (NCP-OUSD)

**Last reviewed:** 2026-11-07, against the [official exam page](https://www.nvidia.com/en-us/learn/certification/openusd-development-professional/) and NVIDIA's official [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) (version 1.1.0, linked from the exam page).

## Exam Overview

The exam validates building, maintaining and optimizing 3D content creation pipelines with OpenUSD. NVIDIA's code for the exam is **NCP-OUSD** (this guide called it NCP-USD until 2026-10-22); the page also calls it the NCP-OpenUSD Development certification.

**Exam facts (from the exam page, 2026-11-07):**
- **Exam code:** NCP-OUSD
- **Duration:** 120 minutes
- **Questions:** 60-70
- **Price:** $200
- **Delivery:** Online, proctored remotely; a Certiverse account is needed to access the exam
- **Level:** Professional
- **Validity:** Two years from issuance; recertify by retaking the exam
- **Languages:** English
- **Labs:** The page does not mention labs
- **Prerequisites:** Two to three years of experience with the OpenUSD framework plus Python or C++ (or completion of the study guide materials)
- **Passing score:** Not published

## Exam Blueprint

Eight sections, in NVIDIA's alphabetical order. Each note covers one section, objective by objective, using the numbered objectives from the study guide.

| # | Section | Weight | Note |
|---|---------|-------:|------|
| 1 | Composition | 23% | [01-composition.md](notes/01-composition.md) |
| 2 | Content Aggregation | 10% | [02-content-aggregation.md](notes/02-content-aggregation.md) |
| 3 | Customizing USD | 6% | [03-customizing-usd.md](notes/03-customizing-usd.md) |
| 4 | Data Exchange | 15% | [04-data-exchange.md](notes/04-data-exchange.md) |
| 5 | Data Modeling | 13% | [05-data-modeling.md](notes/05-data-modeling.md) |
| 6 | Debugging and Troubleshooting | 11% | [06-debugging-and-troubleshooting.md](notes/06-debugging-and-troubleshooting.md) |
| 7 | Pipeline Development | 14% | [07-pipeline-development.md](notes/07-pipeline-development.md) |
| 8 | Visualization | 8% | [08-visualization.md](notes/08-visualization.md) |

The notes were rewritten on 2026-11-07 to match this blueprint one-to-one. The earlier notes (May 2026) were organized by a domain list NVIDIA no longer publishes, and had no debugging coverage.

## How the code in these notes was checked

Most of OpenUSD can be run locally. The code in the notes was run in a throwaway virtual environment (`pip install usd-core`, version 0.26.11, Python 3.12) and the outputs shown are real. What `usd-core` cannot do is marked "not run" in the notes: building USD or plug-ins, `usdGenSchema`, custom resolvers (C++ only), SceneIndex plug-ins, glTF conversion, DCC importers, and `TfMallocTag`. The command-line tools (`usdcat`, `usdchecker`, `usdzip`) are not in the pip package, so the notes use Python equivalents and take flags from the toolset page.

## Gaps the sources could not fill

The notes say so where they occur: the "Conceptual Data Mapping" reference, ASWF asset structure guidelines, "Principles of Scalable Asset Structure", the file format plug-in page, SceneIndex plug-ins, in-memory resolvers, and build configuration. They are listed in `TODO.md` for follow-up.

## NVIDIA's recommended training (from the exam page)

The Learn OpenUSD learning path, modules 1 to 8 (Setting the Stage, Scene Description Blueprints, Composition Basics, Beyond the Basics, Creating Composition Arcs, Asset Structure Principles and Content Aggregation, Developing Data Exchange Pipelines, Asset Modularity and Instancing), and the self-paced courses Creating Composition Arcs, Asset Structure Principles and Content Aggregation, and Developing Data Exchange Pipelines.

## Quick Links

- **[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/openusd-development-professional/)** - Blueprint, price, registration
- **[📖 Official study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf)** - Objectives with numbered items and reading lists
- **[📖 OpenUSD documentation](https://openusd.org/release/index.html)** - Reference for every API named in the notes

## File Index

| File | Description |
|------|-------------|
| [fact-sheet.md](fact-sheet.md) | Logistics, blueprint and key facts with documentation links |
| [practice-plan.md](practice-plan.md) | Study schedule |
| [scenarios.md](scenarios.md) | Pipeline and debugging scenarios |
| [strategy.md](strategy.md) | Exam tactics |
| [notes/](notes/01-composition.md) | The eight section notes |
