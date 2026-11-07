# Section 7: Pipeline Development (14%)

**Last reviewed:** 2026-11-07

Pipeline development is the architect's view: designing the pipeline, managing assets and versions, documenting, building exporter hooks that transform data into your pipeline's preferred structure, managing build configurations, and flattening assets to remove proprietary dependencies. The eight objectives in NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) are: convert to common formats such as glTF with fidelity; document asset structure guidelines; explain USDC versus USDA trade-offs; implement a round-trip pipeline; integrate custom resolvers; represent custom metadata; validate asset paths; and write or extend a DCC importer. Several overlap with Data Exchange (note 4) and Customizing USD (note 3); this note covers the pipeline view and what is new.

## Designing the pipeline

A USD pipeline is a set of agreements: what an asset looks like on disk, what each step may change, and how changes are checked and delivered. The study guide's reading list for this section names two references on asset structure: "Principles of Scalable Asset Structure in OpenUSD" and the "ASWF Asset Structure Guidelines". I did not fetch either, so I do not quote them. What the OpenUSD documentation I did read supports as design principles:

- **Layers per concern, merged by sublayers** so teams do not edit the same file (note 1, and the FAQ's "prefer sublayering").
- **Assets as referenced components** with a default prim and a kind (`component`, `assembly`), so they can be instanced and managed as units (notes 2 and 5).
- **Stable, portable paths**: anchored relative paths or logical ids through a resolver (notes 3 and 6).
- **Declared units and up axis** on every layer (note 5).
- **Validation at the boundary**: every export is checked before it is published (note 4).

I confirmed the default-prim mechanism in code: `stage.SetDefaultPrim(...)` records which prim is used when a layer is referenced without an explicit path (`defaultPrim: /Root`). The FAQ's `UsdReference - Expressing References Without Prim Paths` and the USD Book "Default Prim" are listed in the study guide.

## 7.2 Document asset structure guidelines

The artifact is a short, enforceable document, ideally enforced by the validator: naming; the layer breakdown of an asset (geometry, materials, variants); the required metadata (default prim, kind, units, up axis); the allowed arcs; the versioning scheme; and delivery rules. The pipeline value of the document is that each rule has a check in the validator and a failing example. For the exam, remember that documentation, diagramming and UI/UX are explicitly part of this section's description ("designing the pipeline, asset management, versioning, diagramming, documenting, UI/UX").

## 7.1, 7.3, 7.4, 7.8 Conversion, formats, round trips, importers

These are covered in note 4 with runnable code: usda versus usdc (307,815 versus 240,664 bytes for a 20,000-point mesh), the OBJ round trip (geometry identical, but up axis and units had to be chosen by the importer), and the validator. The pipeline lesson: a round trip is only proven by comparing results, so build a test that exports, imports and diffs. `usddiff` runs a diff on `usdcat` output of two files (`-f` fully composes first), which is a ready-made comparison step, but note it performs no fuzzy numerical comparison, so floating point noise shows as differences.

**[📖 USD toolset](https://openusd.org/release/toolset.html)** - usddiff, usdcat and usdchecker

## 7.5 Custom resolvers in the pipeline

A resolver lets assets be addressed by logical id (and by version) rather than by path, so the pipeline can relocate or version the files without editing every layer. This is note 3's content: a C++ `ArResolver` plug-in, never Python, with a resolver context for search paths.

## 7.6 Custom metadata

Use `customData` and namespaced custom attributes as described in note 5; the pipeline rule is that a metadata key has an owner, a documented meaning and a validator check.

## 7.7 Validate asset paths

The check is mechanical, and I ran it: list a layer's external references and flag absolute or drive-letter paths.

```
external refs: ('./ok.usda', '/abs/studio/path.usda', 'C:\\proj\\win.usda') | not portable: ['/abs/studio/path.usda', 'C:\\proj\\win.usda']
```

Put that in the exporter hook so a bad path fails at export, not at the consumer's desk. Combine with `MissingReferenceValidator` to catch paths that are well-formed but unresolvable.

## Flattening and removing proprietary dependencies

To remove proprietary dependencies from an asset for delivery, flatten it (`UsdStage::Flatten()`), after which no composition arcs remain (my flattened stage had no sublayers or references and kept the composed value). The study guide also lists `UsdPhysics`, `SdfChangeBlock` and `UsdNotice` among this section's API references, and `UsdStage::Traverse()`, which is the traversal an exporter hook uses. Flattening has a cost (variants and structure disappear), so a delivery step flattens a *copy*. Packaging with `usdzip` (compliance check with `-c`) or `UsdUtils.CreateNewUsdzPackage` (I wrote a `.usdz` and confirmed the zip signature) yields a single deliverable file.

## Managing build configurations

The study guide names "managing build configurations" in the section description but lists no objective or reference for it. A USD-based pipeline typically needs a controlled USD build and its plug-in set (note 3); the documentation I read does not describe build configuration, so it is not covered here.

- **Exporter hook** - pipeline code that runs when an asset is exported and transforms the data into the pipeline's preferred structure and runs checks.
- **Default prim** - the layer metadata naming the prim to use when the layer is referenced without a prim path.

## Check yourself against the objectives

List the elements of an asset structure guideline and the check that enforces each; flag non-portable paths in a layer; decide when to flatten and what is lost; and explain how a round trip is proven. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
