# Section 4: Data Exchange (15%)

**Last reviewed:** 2026-11-07

Data exchange is moving content between USD and everything else: converting to formats like glTF, writing and extending importers and exporters, round-tripping through a DCC (digital content creation tool such as Maya or Blender), documenting how one data model maps to another, and validating what comes out. The eight objectives are in NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf). Code ran on `usd-core` 0.26.11. glTF conversion and DCC plug-ins need tools not available here and are marked not run.

## USD is not just another file format

The USD FAQ answers directly: no. USD's main function is to compose scene description from many files into one scenegraph, while formats like OBJ, FBX and Alembic mainly interchange flat or cached geometry. That framing drives the exchange problem: exporting USD to a flat format means flattening composition and losing structure, and importing a flat format into USD means deciding how to author it as layered scene description.

**[📖 USD FAQ](https://openusd.org/release/usdfaq.html)** - Why USD is not just another file format, and the usda/usdc question

## 4.3 USDC versus USDA

`.usda` is "human-readable UTF-8 text" and `.usdc` is "the random-access binary Crate format"; a plain `.usd` can be either, and you convert with `usdcat --usdFormat` (the `USD_DEFAULT_FILE_FORMAT` environment variable sets the default for `.usd`). Trade-offs: usda is readable, diffable and good for archives, review, tests and hand edits; usdc is compact and fast to read and the right choice for large production assets. I exported a mesh of 20,000 points both ways:

```
sizes: usda 307815 bytes; usdc 240664 bytes;  first bytes of usdc: b'PXR-USDC'
```

The binary file is about 22 percent smaller here, and starts with a `PXR-USDC` magic number. A `.usdz` is a zip-based package; I wrote one with `UsdUtils.CreateNewUsdzPackage` and its first two bytes were `PK`, the zip signature. The USDZ spec and `usdzip` are in the toolset page. (`usdcat`, `usdchecker` and `usdzip` are command-line tools in the full USD build and are not in the pip package, so I used the Python equivalents; the flags below are from the toolset page.)

**[📖 USD toolset](https://openusd.org/release/toolset.html)** - usdcat, usdchecker, usdzip, usdview, usdedit, usddiff

- `usdcat -o out.usda in.usdc` writes a file; `--usdFormat usda|usdc` sets the encoding for `.usd` output; `-f, --flatten` composes the input as a root layer and writes the flattened result.
- `usdzip` creates or inspects `.usdz` packages (`-a` isolates a root layer and its assets, `-c` fails if compliance checks fail, `-l` lists contents).
- `usdchecker` validates a USD or usdz file for interchangeability and renderability by Hydra.

- **USDA** - the human-readable text encoding of USD.
- **USDC (Crate)** - USD's binary, random-access file format with extension .usdc.
- **USDZ** - a zip-based package that bundles a USD file and its assets for delivery.

## 4.1 and 4.7 Converting to other formats, writing an exporter

Fidelity is the point of the objective: what survives the conversion. USD concepts that glTF and similar formats lack (variants, payloads, layered overrides, custom schemas) are lost or must be flattened first; concepts the target has (a particular material model) must be mapped. I could not run a glTF conversion (the pip package does not include the glTF plug-in). The mechanics of an exporter are simple and I wrote one: traverse the stage, read mesh points and topology, write the target format. This minimal OBJ exporter and importer pair, run on a quad:

```python
def export_obj(stage, path):
    for prim in stage.Traverse():
        if prim.IsA(UsdGeom.Mesh):
            m = UsdGeom.Mesh(prim)
            pts = m.GetPointsAttr().Get(); cnt = m.GetFaceVertexCountsAttr().Get(); idx = m.GetFaceVertexIndicesAttr().Get()
            ...  # write "v x y z" and "f i j k l" lines (1-based indices)
```

```
round trip identical geometry: True | up axis Y | metersPerUnit 0.01 (OBJ carries no units or up axis: the importer had to choose)
```

This is objective 4.4 in miniature. The round trip reproduced the points and face indices exactly, but the OBJ file has no field for up axis or units, so the importer had to *choose* them (here Y up and centimeters). That silent assumption is where real round-trip pipelines go wrong. USD records them as stage metadata (`UsdGeom.SetStageUpAxis`, `SetStageMetersPerUnit`), and the OpenUSD API docs list "Encoding Stage UpAxis" and "Encoding Stage Linear Units" in the study guide.

## 4.2 Conceptual data mapping documents

A conceptual mapping document says, for each concept in the source model, what it becomes in the target and what is lost. For USD to MaterialX, for example, the rows would be shader node types, parameter names, units and color spaces. The study guide lists "Conceptual Data Mapping" as a technical reference but I did not retrieve it, so a template is not quoted here. A usable document has: source concept, target concept, transform rule, loss or approximation, and a test asset that proves it.

## 4.5 and 4.8 Nonstandard data, writing or extending an importer

Nonstandard attributes and structures should survive the trip: keep them in a namespaced custom attribute or, when many tools must agree, in a schema (note 3). Importers in DCCs are written against each application's API and the USD Python or C++ API; the pip package cannot run inside a DCC, so those are not run here. The Stage traversal and property reading pattern is the same as my exporter above (and see the Traversing a Stage tutorial).

**[📖 Tutorial: traversing a stage](https://openusd.org/release/tut_traversing_stage.html)** - The pattern every importer and exporter uses
**[📖 Tutorial: converting between layer formats](https://openusd.org/release/tut_converting_between_layer_formats.html)** - usda and usdc conversion

## 4.6 Write a validator for exported assets

A validator checks an asset's integrity before it enters the pipeline. USD has a validation framework; I loaded the built-in `usdUtilsValidators:MissingReferenceValidator` and ran it on a stage with a broken reference:

```python
v = UsdValidation.ValidationRegistry().GetOrLoadValidatorByName("usdUtilsValidators:MissingReferenceValidator")
errs = v.Validate(Usd.Stage.Open("bad.usda"))
```

```
MissingReferenceValidator errors on bad.usda: 1 | ["Found unresolvable external dependency '/tmp/claude-1000/-home-plw-cod"]
```

The registry also includes validators such as `usdShadeValidators:MaterialBindingCollectionValidator`, `usdGeomValidators:StageMetadataChecker` and `usdValidation:AttributeTypeMismatch`. For a pipeline, wrap a set of validators and your own rules (naming, default prim, units set, no absolute paths) in a script that returns a non-zero exit code, and run it as the exporter's last step.

- **Round trip** - exporting from a tool to USD and importing it back and getting equivalent content.
- **Validator** - a check that a USD asset meets rules for integrity, such as no unresolvable references or required metadata.

## Check yourself against the objectives

Choose usda or usdc for a use; explain what is lost converting USD to a flat format; say what an OBJ round trip cannot carry; write down a mapping row; and name three things a validator should check. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
