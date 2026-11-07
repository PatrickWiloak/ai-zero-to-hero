---
last-updated: 2026-11-07
difficulty: advanced
---

# NVIDIA-Certified Professional - OpenUSD Development (NCP-OUSD) - Practice Questions

30 original questions in the weights of NVIDIA's blueprint: Composition (23%, 8 questions), Content Aggregation (10%, 3), Customizing USD (6%, 2), Data Exchange (15%, 4), Data Modeling (13%, 4), Debugging and Troubleshooting (11%, 3), Pipeline Development (14%, 4) and Visualization (8%, 2). They are written for this guide, not taken from the exam or from NVIDIA's sample questions, and the explanations cite the code run in the notes or the OpenUSD documentation.

> **Cert page:** [exams/nvidia/openusd-development-professional/](../nvidia/openusd-development-professional/README.md)

---

### Question 1
**Section: Composition. Scenario:** A prim has size=1 from a reference and size=2 from a sublayer of the root layer, and nothing is authored on the prim itself. What does the composed stage report?

A. 1, because references are always stronger than sublayers
B. The stage reports an error because two opinions conflict
C. 2, because local layer-stack opinions (including sublayers) are stronger than references
D. 3, the average of both values

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** LIVERPS puts Local first and References after VariantSets, and sublayers are part of the local layer stack. I ran exactly this: the property stack was [sub 2.0, ref 1.0] and the value 2.0.
</details>

---

### Question 2
**Section: Composition. Scenario:** Which is the correct order of composition arc strength, strongest first?

A. References, Payload, Local, Inherits, VariantSets, Specializes
B. Local, Inherits, VariantSets, Relocates, References, Payload, Specializes
C. Specializes, Payload, References, Local, Inherits, VariantSets
D. Local, References, Payload, Inherits, VariantSets, Specializes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The OpenUSD glossary: LIVERPS is an acronym for Local, Inherits, VariantSets, Relocates, References, Payload, Specializes.
</details>

---

### Question 3
**Section: Composition. Scenario:** A team needs to reuse one animated clip on many characters, each starting at a different frame. Which mechanism applies the shift?

A. A variant set with one variant per start frame
B. A native instance with a different prototype for each character
C. A change to the stage's up axis
D. A layer offset on the reference or sublayer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Composition arcs such as references and sublayers can carry an offset and scale of time. In my run an offset of 5 made the value at time 10 equal the original's value at time 5.
</details>

---

### Question 4
**Section: Composition. Scenario:** A very large environment should only be loaded when the artist asks for it. Which arc supports that?

A. A payload, which is a reference that can be loaded and unloaded
B. A sublayer, which is always loaded with the layer stack
C. An inherits arc
D. A specializes arc

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The glossary calls a payload a special kind of reference, and after Unload() the prim still has a payload but its content is not composed.
</details>

---

### Question 5
**Section: Composition. Scenario:** Two departments edit the same asset in the same namespace and should not conflict in files. According to the USD FAQ, which arc should be preferred when it meets the need?

A. References, because they always rename the prims
B. Sublayers, one layer per department in the same namespace
C. Variants, one per department
D. A single monolithic layer with comments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The FAQ says that if sublayering satisfies your requirements, prefer it over referencing; references are better when layers have different namespaces.
</details>

---

### Question 6
**Section: Composition. Scenario:** An override authored in a layer does not show on the composed stage. Which is a likely cause?

A. The stage's meters-per-unit is not 1
B. The mesh uses the usdc format
C. The layer is muted, or a stronger opinion exists elsewhere in the prim stack
D. The prim's kind is component

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Muting removes a layer's opinions from the stage (after MuteLayer in my test the value fell back to the reference's), and a stronger opinion wins regardless. The prim stack shows every contributing spec.
</details>

---

### Question 7
**Section: Composition. Scenario:** A pipeline lead wants a deliverable that has no composition arcs and no dependencies on internal layers. What do they produce?

A. A stage with all payloads unloaded
B. A flattened copy of the stage (UsdStage::Flatten or usdcat --flatten)
C. A set of variants named external
D. A copy with kind set to assembly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Flattening collapses the stage into one layer with no arcs left. In my test the flattened layer had no sublayers or references and kept the composed value.
</details>

---

### Question 8
**Section: Composition. Scenario:** Which statement about a variant set is correct?

A. It holds named alternatives on a prim, with one variant selected at a time
B. It composes all of its variants at once
C. It can only select among payloads
D. It is weaker than specializes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A variant set is a set of mutually exclusive alternatives with a selection; VariantSets rank above References and Payload in LIVERPS.
</details>

---

### Question 9
**Section: Content aggregation. Scenario:** Which instancing style suits 500 copies of a building asset that has internal structure and materials?

A. Native (scenegraph) instancing with instanceable references
B. A PointInstancer with one prototype
C. Flattening each copy
D. Variants, one per copy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Native instancing shares one composed subtree among instances, ideal for structured assets used many times; point instancing is for huge numbers of simple elements.
</details>

---

### Question 10
**Section: Content aggregation. Scenario:** A PointInstancer should show a second kind of object. What is the correct change?

A. Add a second PointInstancer prim and delete the first
B. Add a target to its prototypes relationship and point entries of protoIndices at the new index
C. Change the instancer's kind to assembly
D. Set instanceable on every instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prototype indices follow the order of the prototypes relationship. In my run the added prototype became index 1 and protoIndices [0, 1, 0, 1, 0] used it.
</details>

---

### Question 11
**Section: Content aggregation. Scenario:** A user tries to set a different display color on a mesh beneath an instanceable prim and the API raises an error. What is the documented way to customize an instance's contents?

A. Switch the stage to usdc
B. Raise the payload's load rule
C. Make it non-instanceable, or add an inherits or specializes arc and edit the class
D. Delete the prototype

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The instancing page says you cannot override descendants of an instance, including through proxies; overrides on the instance prim itself are allowed.
</details>

---

### Question 12
**Section: Customizing USD. Scenario:** Which statement about custom asset resolvers is correct?

A. They are written as USD layers
B. They are Python classes registered with the stage
C. They are configured with usdGenSchema
D. They are C++ ArResolver plug-ins registered through plugInfo.json; Python resolvers are not supported

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Ar documentation says custom resolvers are ArResolver subclasses registered with AR_DEFINE_RESOLVER and plugInfo.json, and that Ar does not support Python implementations to avoid performance issues.
</details>

---

### Question 13
**Section: Customizing USD. Scenario:** What is a codeless schema?

A. A schema generated with skipCodeGeneration that produces only generatedSchema.usda and plugInfo.json
B. A schema with no properties
C. A schema written directly in a USD layer with no schema.usda
D. A schema that cannot be applied to prims

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Codeless schemas can be used without recompiling USD, but clients query them only through the basic USD APIs.
</details>

---

### Question 14
**Section: Data exchange. Scenario:** A team wants a compact, fast-loading binary encoding for a large production asset and a readable one for review. Which pair?

A. usdc for production, usda for review
B. usda for production, usdz for review
C. usdz for production, usdc for review
D. usdc for both because usda cannot be diffed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** usda is human-readable text and usdc is the random-access binary Crate format. In my test a 20,000-point mesh was 307,815 bytes as usda and 240,664 as usdc.
</details>

---

### Question 15
**Section: Data exchange. Scenario:** An OBJ importer produces geometry that matches the source exactly but the scene is rotated and the wrong size in another tool. What is the likely reason?

A. The mesh must use faceVarying primvars
B. OBJ carries no up axis or units, so the importer had to choose them and the stage metadata must be set deliberately
C. The importer must write a payload
D. usdz files cannot hold meshes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In my round trip the points and indices were identical, but the importer chose Y up and centimeters because OBJ has no fields for them. USD stores both as stage metadata.
</details>

---

### Question 16
**Section: Data exchange. Scenario:** Why is USD described as more than another file format?

A. It stores only flat cached geometry
B. It is a binary-only format
C. Its main function is composing scene description from many files into a single scenegraph
D. It is a rendering engine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The USD FAQ contrasts formats like OBJ, FBX and Alembic, which mainly interchange flat or cached geometry, with USD's composition engine and scenegraph.
</details>

---

### Question 17
**Section: Data exchange. Scenario:** Which check belongs in an exporter's validation step?

A. Only the file size
B. Only the number of materials
C. Nothing, because USD always validates itself
D. Unresolvable references, required metadata such as default prim and units, and non-portable asset paths

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** USD ships validators such as MissingReferenceValidator, which flagged a broken reference in my test; the other checks are pipeline rules enforced the same way.
</details>

---

### Question 18
**Section: Data modeling. Scenario:** After a script moves a mesh's points, the model is clipped in the viewport. What should be recomputed?

A. The extent attribute, with UsdGeom.Boundable.ComputeExtentFromPlugins
B. The prim's kind
C. The variant selection
D. The payload's load rule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Changing points does not update the extent. I recomputed it and got [(0,0,0), (5,5,0)].
</details>

---

### Question 19
**Section: Data modeling. Scenario:** A mesh has 4 vertices and a primvar must give each vertex its own color. Which interpolation mode?

A. vertex
B. constant
C. uniform
D. faceVarying with one value total

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Vertex primvars are interpolated between vertices; constant is one value for the whole primitive and uniform is one per face.
</details>

---

### Question 20
**Section: Data modeling. Scenario:** What does GetAuthoredPropertyNames return compared with GetPropertyNames?

A. The reverse
B. Only relationships
C. The properties of the parent prim
D. Only the properties some layer actually wrote, whereas GetPropertyNames also includes unauthored schema properties

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In my run purpose, visibility and proxyPrim appeared in the full list but not in the authored list.
</details>

---

### Question 21
**Section: Data modeling. Scenario:** Where should a pipeline put a free-form owner annotation that does not need to animate?

A. In a time-sampled relationship
B. In the extent attribute
C. In customData metadata, namespaced by the pipeline
D. In the prim's kind

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** customData is the free-form metadata dictionary; metadata cannot vary over time, so use an attribute when the value must animate.
</details>

---

### Question 22
**Section: Debugging. Scenario:** Which API shows every spec that contributes to a composed prim, strongest first?

A. stage.Flatten()
B. prim.GetKind()
C. UsdGeom.PrimvarsAPI
D. prim.GetPrimStack()

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The prim stack lists contributing specs in order; in my run it was root, sub and ref.
</details>

---

### Question 23
**Section: Debugging. Scenario:** A script creates thousands of prim specs and is slow because each edit triggers change processing. What helps, and what is the rule?

A. Group the edits in an SdfChangeBlock and use no Usd API while it is open
B. Wrap them in a payload
C. Switch the layer to usdz
D. Use TfMallocTag to disable notifications

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A change block delays notifications until the outermost block exits; the docs warn it is not safe to use Usd or other downstream API while one is open. In my run 3,000 specs took 1.061 s without and 0.025 s with a block.
</details>

---

### Question 24
**Section: Debugging. Scenario:** How can a tool collect USD warnings and errors instead of printing them?

A. With usdzip
B. With a diagnostic delegate such as UsdUtils.CoalescingDiagnosticDelegate
C. By changing the layer's format
D. With a variant set

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A diagnostic delegate receives Tf diagnostics; in my broken-stage run it returned two warnings with their source locations.
</details>

---

### Question 25
**Section: Pipeline development. Scenario:** Which asset path is a portability problem in a layer that will be shipped to another studio?

A. ./chair.usd
B. ./textures/wood.png
C. ../shared/chair.usd
D. /mnt/studio/assets/chair.usd

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Absolute paths depend on one machine's layout; anchored relative paths resolve wherever the files are delivered. A path check flagged the absolute and drive-letter entries in my test.
</details>

---

### Question 26
**Section: Pipeline development. Scenario:** What is the purpose of the layer metadata defaultPrim?

A. It sets the stage's up axis
B. It selects the first variant
C. It names the prim used when the layer is referenced without an explicit prim path
D. It marks the layer as flattened

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The default prim is what a reference without a prim path targets; I set and read it with SetDefaultPrim and GetDefaultPrim.
</details>

---

### Question 27
**Section: Pipeline development. Scenario:** How is a DCC-to-USD round trip best verified in a pipeline?

A. By opening the file once and looking at it
B. By checking only the file extension
C. By flattening and deleting the original
D. Export, import and compare the results automatically, such as with usddiff or a script

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A round trip is proven by comparing; usddiff diffs usdcat output of two files, though it does no fuzzy numerical comparison.
</details>

---

### Question 28
**Section: Pipeline development. Scenario:** What is lost when you flatten an asset for delivery?

A. The composed values
B. The mesh points
C. Composition structure such as variants, references and layered overrides
D. The material bindings' targets

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Flattening bakes the composed result into one layer with no arcs left, so the structure is gone; deliver a flattened copy and keep the layered original.
</details>

---

### Question 29
**Section: Visualization. Scenario:** A parent prim's material binding is set strongerThanDescendants and a child mesh has its own binding. Which material does the child resolve to?

A. The child's, because lower bindings always win
B. The parent's, because strongerThanDescendants wins over the child's binding
C. Neither; the binding is an error
D. The material with the higher roughness

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bindings lower in the namespace are stronger than ancestor bindings unless the ancestor is strongerThanDescendants. My test resolved the child to the parent's Red.
</details>

---

### Question 30
**Section: Visualization. Scenario:** How should diffuseColor in a UsdPreviewSurface read per-vertex colors from a mesh's displayColor primvar?

A. Set diffuseColor to the primvar's path as a string
B. Use a UsdUVTexture with the file set to displayColor
C. Bind the mesh to a collection named displayColor
D. Connect a UsdPrimvarReader_float3 shader (varname displayColor) result output to diffuseColor

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The spec says to choose the reader by the primvar's type, set varname and connect result to the color input; color from a mesh needs no premultiplication.
</details>

---

## Where to go deeper

- [NCP-OUSD cert page](../nvidia/openusd-development-professional/README.md) - notes, plan, strategy
- **[📖 NVIDIA OpenUSD Development exam page](https://www.nvidia.com/en-us/learn/certification/openusd-development-professional/)** - official blueprint and study guide
- **[📖 OpenUSD documentation](https://openusd.org/release/index.html)** - API and glossary
