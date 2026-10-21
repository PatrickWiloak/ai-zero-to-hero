---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - OpenUSD (NCP-USD) - Practice Questions

15 questions for NCP-USD prep, weighted toward USD fundamentals (25%) and scene composition (25%), then the Omniverse platform (20%), rendering and materials (15%), and collaboration (15%).

> **Cert page:** [exams/nvidia/openusd-professional/](../nvidia/openusd-professional/README.md)

---

### Question 1
**Scenario:** What is a prim in USD?

A. The primary container object in a scene hierarchy, carrying a type, properties, and metadata
B. A file format, either .usda or .usdc, that stores layers of scene description on disk in text or binary form
C. A material shader node that computes how light reflects off the surface of a mesh when it is rendered
D. A rendering pass

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Prims are the nodes of the scene graph, identified by a path such as `/World/Vehicle/Wheel`. They have a type (Mesh, Xform, Camera, and so on), attributes, and relationships. Everything in a USD stage is addressed as a prim path.
</details>

---

### Question 2
**Scenario:** What does LIVRPS describe?

A. The composition arc strength order: Local, Inherits, VariantSets, References, Payloads, Specializes
B. A file naming convention
C. A rendering pipeline order in which the engine processes lights, shadows, indirect bounces, and post effects
D. A physically based material model that describes how surfaces reflect, absorb and transmit light in a renderer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** LIVRPS is the order in which USD resolves conflicting opinions about a prim's properties, strongest first. Understanding it is what lets you predict which layer's value wins, which is the single most important concept in USD composition.
</details>

---

### Question 3
**Scenario:** A large asset should not be loaded until it is needed.

A. A reference
B. A payload, which can be loaded and unloaded on demand
C. An inherit
D. A variant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Payloads are references that are not composed by default, so a stage can be opened with heavy geometry deferred. This is the primary mechanism for working with scenes far larger than memory, and the choice between reference and payload is a scalability decision.
</details>

---

### Question 4
**Scenario:** One asset must be available in three configurations, switchable at runtime.

A. Three sibling prims referencing different files, switched by hand-editing the visibility attribute
B. Three separate stages opened in three viewports and switched by hand
C. A variant set with three variants on the prim
D. Three separate files with no relationship between them, one for each configuration

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Variant sets encode alternatives inside a single asset and let a consumer select one by name, which keeps configuration a property of the asset rather than a file-management problem. Nested variant sets handle combinations such as model and trim level.
</details>

---

### Question 5
**Scenario:** Several artists must work on the same scene simultaneously without overwriting each other.

A. Take turns
B. One shared file that everyone opens and edits at the same time, with the last person to save winning
C. Layer-based workflow: each artist authors in their own layer, composed by the layer stack
D. Duplicate the scene per artist and have a supervisor merge the changed prims back into a master file each evening

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Non-destructive layering is the collaboration model USD was designed for: lighting, animation, and modeling opinions live in separate layers with defined strength, so nobody edits the same bytes. This is also why USD suits pipelines with many departments touching one asset.
</details>

---

### Question 6
**Scenario:** What is a stage in USD?

A. The composed scene graph produced by evaluating the root layer and its composition arcs
B. A single .usd file on disk that holds every prim, read directly with no composition step involved
C. A rendering device
D. A material library

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The stage is the runtime view, not a file: it is what you get after composition has resolved references, payloads, variants, and layer strength. Distinguishing the authored layer from the composed stage explains most confusion about "why is my edit not showing."
</details>

---

### Question 7
**Scenario:** An edit must be made without modifying the referenced source asset.

A. Author an override in a stronger local layer; the source stays unchanged
B. Copy the asset and edit the copy, then point the scene at the new copy instead of the source
C. Edit the source file directly and republish it, since every other reference will pick up the change automatically
D. Delete the reference and re-author the whole asset from scratch directly in the shot layer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Non-destructive override is the core USD workflow: your opinion in a stronger layer wins during composition while the upstream asset keeps updating independently. Copying breaks the link and guarantees divergence when the source changes.
</details>

---

### Question 8
**Scenario:** Which describes Omniverse Nucleus?

A. A renderer that ray traces USD stages on RTX GPUs and writes final frames to disk for review
B. A physics engine
C. The server that stores USD content and syncs live changes between connected clients
D. A file format

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Nucleus is the server component providing versioned storage and the live-sync channel that makes multi-user editing possible. RTX Renderer and Hydra handle rendering, PhysX handles simulation, and Kit is the application framework.
</details>

---

### Question 9
**Scenario:** Materials must be portable across renderers.

A. Hard-coded colors
B. Renderer-specific shaders only, since each renderer then reads its own native material network at full quality
C. Textures with no material
D. MaterialX or UsdPreviewSurface, with renderer-specific shaders only where needed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** UsdPreviewSurface gives a baseline PBR material every USD-aware renderer understands, and MaterialX expresses richer node graphs portably. Authoring only in a renderer-specific language locks the asset to one pipeline, which defeats the interchange purpose of USD.
</details>

---

### Question 10
**Scenario:** Which layer wins when two sublayers in the same layer stack both set a prim's attribute?

A. It is undefined
B. They are averaged
C. The stronger one, meaning the one earlier in the sublayer list
D. The last one listed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sublayer order is strength order, strongest first, and the strongest opinion wins with no blending. This is deterministic by design, which is what makes a pipeline reproducible. `usdview`'s composition inspector shows exactly which layer supplied a value.
</details>

---

### Question 11
**Scenario:** Hydra is used in the rendering path. What is its role?

A. It stores the assets in a versioned database that clients read from and write to over the network
B. It authors USD files from DCC applications by exporting each tool's native scene data into layers
C. It handles physics, solving rigid body dynamics and collisions for every prim on the stage each frame
D. The scene delegate architecture that lets many render delegates draw the same stage

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hydra sits between the scene and the renderer so the same USD stage can be drawn by Storm, RTX, or a third-party delegate without changing the data. That separation is what lets a studio switch renderers without reauthoring content.
</details>

---

### Question 12
**Scenario:** A schema must add domain-specific properties to prims consistently.

A. External spreadsheets that list each prim's expected properties, checked by a script before export
B. Comments in the file
C. Ad-hoc attributes on each prim
D. A typed or applied API schema defining the properties, so tooling can rely on them

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Schemas make properties discoverable and validated rather than conventional, which is what allows tools to interoperate. Applied API schemas add capabilities to existing prim types without changing their type, which is the usual choice for domain metadata.
</details>

---

### Question 13
**Scenario:** A scene opens very slowly with high memory use.

A. Reduce the screen resolution and viewport sampling so fewer pixels and textures are held in GPU memory
B. Convert heavy references to payloads, instance repeated geometry, and check for deep composition
C. Disable materials
D. Buy more RAM and a faster GPU, so that the entire scene fits in memory without changing how it is built

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Composition cost and geometry duplication are the two usual causes. Point instancers and scenegraph instancing collapse thousands of identical prims into shared data, and payloads defer what is not needed yet. Hardware only postpones the ceiling.
</details>

---

### Question 14
**Scenario:** Assets from several tools must combine into one scene.

A. Convert every asset to one proprietary format and require each tool in the pipeline to import it directly
B. Use USD as the interchange format, with connectors per tool, and run the USD validator
C. Screenshot each asset from every tool and paste the images into a single scene as flat planes
D. Rebuild everything in one tool so that a single native format is used, then re-export the combined result

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Interchange is USD's original purpose and the reason it spread beyond film into simulation and industrial digital twins. Validation matters because a syntactically valid file can still violate pipeline conventions, and catching that at export is far cheaper than downstream.
</details>

---

### Question 15
**Scenario:** Time-varying data such as animation is stored how in USD?

A. Only as a single static value
B. As time samples on attributes, evaluated at a given time code against the stage's frame rate
C. As a material property
D. In a separate video file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Attributes hold either a default value or a set of time samples, and the stage's timeCodesPerSecond relates time codes to seconds. Layer offsets and scales let a referenced animation be retimed without editing the source, which is the composition system applied to time.
</details>

---

## Where to go deeper

- [NCP-USD cert page](../nvidia/openusd-professional/README.md) - notes, practice plan, strategy
- [NCA-MMGA practice questions](nvidia-multimodal-genai-associate.md) - generative content for 3D pipelines
- **[📖 OpenUSD documentation](https://openusd.org/release/index.html)** - primary source
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
