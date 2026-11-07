---
last-updated: 2026-11-07
---

# NVIDIA-Certified Professional - OpenUSD Development (NCP-OUSD) - Fact Sheet

## Quick Reference

**Exam code:** NCP-OUSD  
**Duration:** 120 minutes  
**Questions:** 60-70  
**Cost:** $200 USD (exam page, 2026-11-07)  
**Delivery:** Online, proctored remotely; Certiverse account required  
**Level:** Professional  
**Validity:** 2 years from issuance  
**Languages:** English  
**Prerequisites:** 2-3 years with OpenUSD and Python or C++ (or the study guide materials)  
**Passing score:** Not published  

**[📖 Official exam page](https://www.nvidia.com/en-us/learn/certification/openusd-development-professional/)** - Blueprint and registration
**[📖 Official study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf)** - Numbered objectives and reading lists

## Exam Blueprint

| Topic | Weight | Note |
|---|---|---|
| Composition | 23% | [01](notes/01-composition.md) |
| Content Aggregation | 10% | [02](notes/02-content-aggregation.md) |
| Customizing USD | 6% | [03](notes/03-customizing-usd.md) |
| Data Exchange | 15% | [04](notes/04-data-exchange.md) |
| Data Modeling | 13% | [05](notes/05-data-modeling.md) |
| Debugging and Troubleshooting | 11% | [06](notes/06-debugging-and-troubleshooting.md) |
| Pipeline Development | 14% | [07](notes/07-pipeline-development.md) |
| Visualization | 8% | [08](notes/08-visualization.md) |

## Key Facts by Section

**[📖 OpenUSD glossary](https://openusd.org/release/glossary.html)** - Terms used throughout

- **Composition:** LIVERPS = Local, Inherits, VariantSets, Relocates, References, Payload, Specializes. Prefer sublayers when namespace allows; references remap prims; payloads can be unloaded. Layer offsets shift time on an arc.
- **Content aggregation:** kinds model > group > assembly; component is a leaf; native instancing shares a prototype (edit only the instance prim itself); PointInstancer has `prototypes`, `protoIndices`, `positions`, `inactiveIds`, `invisibleIds`.
- **Customizing:** custom kinds via plugInfo.json `Kinds`; schemas via `usdGenSchema` (IsA versus API; codeless with skipCodeGeneration); resolvers are C++ `ArResolver` plug-ins, not Python.
- **Data exchange:** usda is text, usdc is binary Crate, usdz is a zip-based package; `usdcat -f` flattens; USD is not just a file format; validate on export.
- **Data modeling:** attributes versus relationships; primvars in `primvars:` with five interpolation modes; recompute `extent` after changing points; customData for private metadata.
- **Debugging:** prim stack and property stack show contributing specs; `SdfChangeBlock` batches edits (no Usd calls inside); diagnostic delegates, TfDebug, Trace, TfMallocTag.
- **Pipeline:** relative anchored paths; default prim; flatten a copy for delivery; round trips are proven by diffing.
- **Visualization:** `UsdPreviewSurface` (diffuseColor, metallic, roughness, opacity, normal); `material:binding` with `weakerThanDescendants` default; subsets in the `materialBind` family; `UsdPrimvarReader_float3` for color primvars.
