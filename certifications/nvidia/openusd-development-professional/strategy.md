# NCP-OUSD - Exam Strategy

**Last reviewed:** 2026-11-07

## What the exam looks like

Two hours, 60 to 70 questions, online and remotely proctored. NVIDIA's own study guide includes sample questions across composition, data modeling, pipeline development, customizing, visualization, content aggregation and data exchange, so expect scenario-style questions that name specific USD concepts and API calls.

## Tactics

1. **Resolve composition questions by LIVERPS.** Write the opinions down in strength order and take the first one. Remember the layer stack inside "Local": the session layer, then the root layer, then sublayers in list order (first listed is strongest).
2. **Know what you cannot do.** You cannot override descendants of a native instance; payloads are weaker than references; a typeless `over` does not create a prim; an Ar resolver cannot be written in Python.
3. **Match the tool to the scale.** Few unique copies: references. Many copies of a structured asset: native instancing. Huge numbers of simple elements: PointInstancer.
4. **Match the format to the use.** usda to read and review, usdc to ship large data, usdz to deliver a self-contained package, flattened copy to remove dependencies.
5. **When a result looks wrong, think data first:** extent, primvar length and interpolation, units and up axis, purpose and visibility, binding strength, and composition errors.
6. **Read answer options for the word "efficiently".** For hiding point instances, the answer works by id (`invisibleIds`/`inactiveIds`), not by rewriting arrays.
7. **Look for what is unsupported or deprecated in the option text** and eliminate it before choosing.
