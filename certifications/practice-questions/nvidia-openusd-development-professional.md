---
last-updated: 2026-10-22
difficulty: advanced
---

# NVIDIA-Certified Professional - OpenUSD Development (NCP-OUSD) - Practice Questions

30 questions for NCP-OUSD prep, weighted toward composition (23%), then data exchange (15%), pipeline development (14%), data modeling (13%), debugging and troubleshooting (11%), content aggregation (10%), visualization (8%), and customizing USD (6%).

> **Cert page:** [exams/nvidia/openusd-development-professional/](../nvidia/openusd-development-professional/README.md)

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

### Question 16
**Scenario:** A forest scene contains 400 tree prims that reference different tree assets. The art director wants one change, such as a wind-strength attribute, to reach all of them at once while letting individual trees still override it.

A. Write a script that sets the attribute on all 400 prims and rerun it after every new change
B. Have each tree inherit from a class prim such as `/_class_Tree` and edit the class
C. Put the attribute in every tree asset's source file, so that each reference carries the change
D. Add the attribute to the stage's root layer metadata, which every prim on the stage reads first

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An inherits arc lets many prims receive opinions from one class prim, so an edit on the class broadcasts to every inheriting prim, while stronger local opinions on a single tree still win. A script creates 400 separate opinions to maintain. Editing every source asset is invasive, and layer metadata is not inherited by prims as attribute values.

**Key Concept:** [USD glossary: inherits](https://openusd.org/release/glossary.html)
</details>

---

### Question 17
**Scenario:** A shot references an animated character clip, and the clip must start 48 frames later and play at half speed in this shot only.

A. Re-export the animation with shifted and stretched time samples and save it as a new asset file
B. Change the stage's `timeCodesPerSecond` so that every animation in the shot plays at half speed
C. Author a layer offset (offset and scale) on the reference to retime the referenced data
D. Add a variant set for each possible timing and select the variant that matches this shot's timing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** References and sublayers can carry a layer offset (an offset and a scale) that maps the referenced layer's time codes into the referencing context, so the clip is retimed non-destructively for this shot. Re-exporting duplicates data. Changing `timeCodesPerSecond` affects the whole stage, and variants for every possible timing do not scale.

**Key Concept:** [SdfLayerOffset](https://openusd.org/release/api/class_sdf_layer_offset.html)
</details>

---

### Question 18
**Scenario:** A city scene references the same streetlight asset 10,000 times, and every copy is composed separately, using a lot of memory and load time.

A. Mark the referencing prims `instanceable` so that identical composed subtrees share one prototype
B. Merge all 10,000 streetlights into a single mesh, so the stage holds one prim instead of many
C. Convert each reference into a sublayer, which composes the streetlight asset only once per stage
D. Move the streetlights into a variant set, which loads only the variant that is selected on the stage

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With scenegraph instancing, prims marked `instanceable` that share the same composition arcs share a single prototype, so USD composes the subtree once instead of 10,000 times, while each instance keeps its own transform. Merging into one mesh loses per-light control. Sublayers combine layers at the root rather than placing assets, and a variant does not deduplicate repeated assets.

**Key Concept:** [Scenegraph instancing](https://openusd.org/release/api/_usd__page__scenegraph_instancing.html)
</details>

---

### Question 19
**Scenario:** Tools need to traverse a large set down to whole assets only, such as a building or a car, without walking every mesh and material inside them.

A. Put every asset in a separate sublayer, so traversals stop at each layer boundary
B. Name every asset's root prim with the prefix `asset_` and filter on that string
C. Give every mesh a custom attribute called `isAsset` and test it during traversal
D. Set `kind` metadata to build a model hierarchy of assemblies, groups and components

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The `kind` metadata defines USD's model hierarchy, with assemblies and groups above component models, so tools can traverse just the models and treat each component as an asset boundary, using standard APIs and predicates. Sublayers do not partition namespace this way. Naming conventions and custom attributes are fragile and invisible to standard tools.

**Key Concept:** [USD glossary: kind and model hierarchy](https://openusd.org/release/glossary.html)
</details>

---

### Question 20
**Scenario:** A set dresser is assembling 300 separately published prop assets into one environment, each at its own location in the scene namespace.

A. Sublayer all 300 asset files into the environment layer, so each prop lands at its own path
B. Reference each prop's asset into its own prim under the environment, with a transform per prim
C. Copy every prop's geometry into the environment file, so the environment needs no other files
D. Use one variant set with 300 variants, one per prop, and select all of them on the stage at once

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** References bring an asset's root prim into a chosen namespace location, so each prop can sit under its own prim with its own transform while staying linked to the published asset; payloads can be used where deferred loading helps. Sublayering merges every asset's namespace at the root and would collide. Copying breaks the link to updates, and only one variant per set can be selected.

**Key Concept:** [USD glossary: references](https://openusd.org/release/glossary.html)
</details>

---

### Question 21
**Scenario:** A studio needs a new applied API schema with a few properties for its pipeline. It wants the schema available in Python and in tools without compiling any C++ code.

A. Add the properties as custom attributes on each prim and document their names on the team wiki
B. Write a full typed schema in C++ and compile it into every USD build the studio uses
C. Generate a codeless schema with `usdGenSchema` and register it through a plugin's `plugInfo.json`
D. Store the properties as metadata in each layer's comment field so that tools can parse them later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Codeless schemas are generated by `usdGenSchema` with code generation skipped; the schema is defined by its generated schema file and plugin registration, so it is available at runtime without a compiled library. Custom attributes on a wiki are not discoverable by tools. A compiled C++ schema works but adds the build step the studio wanted to avoid, and comments are not structured data.

**Key Concept:** [Generating schemas with usdGenSchema](https://openusd.org/release/api/_usd__page__generating_schemas.html)
</details>

---

### Question 22
**Scenario:** A simulation team stores results in a proprietary file format and wants USD stages to reference those files directly, without a nightly conversion step.

A. Rename the files with a `.usda` extension so that the USD runtime parses them as text layers
B. Convert each file to USDZ every night, since USD can only read files that were converted first
C. Load the data in Python each time a scene opens and copy it into the session layer by hand
D. Write an `SdfFileFormat` plugin that reads the proprietary format as a USD layer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** USD's file format plugins let any format be read, and optionally written, as an `SdfLayer`, so stages can reference those files directly; formats such as Alembic are supported this way. Renaming does not change the contents. Nightly conversion is the step the team wants to remove, and manual copying into the session layer is fragile and not shareable.

**Key Concept:** [SdfFileFormat](https://openusd.org/release/api/class_sdf_file_format.html)
</details>

---

### Question 23
**Scenario:** Props from one tool appear 100 times too large and lying on their side when added to a stage authored in another tool.

A. Compare the `metersPerUnit` and `upAxis` stage metadata and correct the difference
B. Scale every prop by 0.01 by hand in the viewport and rotate it upright before saving the layer
C. Convert the props to USDZ, which normalizes their units and axes when the package is created
D. Delete the props' transforms, which makes USD use a single default unit and axis for all of them

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** USD records linear units in `metersPerUnit` and the up direction in `upAxis` as stage metadata, and a centimeters, Z-up layer brought into a meters, Y-up stage shows exactly this symptom. Tools should read the metadata and apply a corrective transform at the boundary. Hand-fixing each prop does not scale, USDZ packaging does not convert units, and removing transforms loses placement.

**Key Concept:** [UsdGeom overview](https://openusd.org/release/api/usd_geom_page_front.html)
</details>

---

### Question 24
**Scenario:** An asset must be delivered as a single file for AR viewing on mobile devices, including its geometry and textures.

A. Save it as a `.usda` text layer, which embeds the texture images inside the text as strings
B. Package it as USDZ, an uncompressed zip archive of USD and texture files, using `usdzip`
C. Flatten the stage and send the layer alone, since flattening also copies every texture into it
D. Compress the asset folder as a standard `.zip` with maximum compression and rename it `.usd`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** USDZ is a zip archive with specific constraints, uncompressed with aligned files so it can be read in place, holding a USD layer and its textures; `usdzip` creates it. Text layers reference textures rather than embedding them. Flattening composes layers but does not pack textures, and a compressed zip renamed to `.usd` is not a valid USD file.

**Key Concept:** [USDZ file format specification](https://openusd.org/release/wp_usdz.html)
</details>

---

### Question 25
**Scenario:** A mesh needs a color value per vertex that renderers should interpolate smoothly across each face.

A. Add a custom string attribute listing all colors, which renderers parse on load
B. Add a child prim per vertex, each holding one color in its own attribute value
C. Set the color in the prim's `customData` dictionary, which renderers read per vertex
D. Author a primvar such as `displayColor` with `vertex` interpolation on the mesh

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Primvars are geometric attributes with an interpolation mode (constant, uniform, varying, vertex or faceVarying) that tells renderers how to map values over the surface, and `vertex` gives smooth per-vertex interpolation. A custom string is not understood by renderers. Child prims per vertex would be enormous, and `customData` is for metadata, not renderable data.

**Key Concept:** [UsdGeomPrimvar](https://openusd.org/release/api/class_usd_geom_primvar.html)
</details>

---

### Question 26
**Scenario:** An attribute on a composed prim has an unexpected value, and a developer needs to see every layer that holds an opinion on it, from strongest to weakest.

A. Call `GetPropertyStack()` on the attribute, or inspect it in usdview, to list the contributing specs
B. Flatten the stage and search the flattened file, which shows every layer's opinion in strength order
C. Read each layer file in a text editor in the order it was saved to disk, newest file first
D. Call `Get()` on the attribute several times, which returns one opinion from each layer in turn

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `UsdProperty.GetPropertyStack()` returns the property specs that contribute opinions, ordered strongest to weakest, and usdview shows the same layer stack, so the winning layer is found directly. Flattening keeps only the resolved result and discards the losing opinions. File save order is not composition strength, and `Get()` always returns the single resolved value.

**Key Concept:** [UsdProperty](https://openusd.org/release/api/class_usd_property.html)
</details>

---

### Question 27
**Scenario:** Before publishing an asset, the pipeline must catch problems such as missing references, invalid schema usage and USDZ packaging rule violations.

A. Open the asset in a viewer and approve it if nothing looks wrong on screen
B. Run `usdchecker` on the asset as a publish gate and fail the publish on errors
C. Run `usdcat` on the asset, since a file that prints without errors is valid
D. Check that the file size is under 1 GB, since large files are the main risk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `usdchecker` runs a suite of compliance checks, including unresolvable dependencies, schema and stage metadata rules and USDZ package constraints, and its exit status makes it easy to use as an automated gate. A visual check misses many structural problems. `usdcat` only prints or converts a layer, and file size says nothing about validity.

**Key Concept:** [USD toolset: usdchecker](https://openusd.org/release/toolset.html)
</details>

---

### Question 28
**Scenario:** A stage opens with errors saying that an asset path cannot be found, and the studio uses a custom asset resolver with logical asset identifiers.

A. Replace every logical identifier with an absolute file path, since resolvers cannot be debugged
B. Delete the failing references from the layer so that the stage opens without any errors
C. Rename the asset files to match the identifier text exactly, which bypasses the asset resolver
D. Run `usdresolve` on the identifier and enable `TF_DEBUG` output to trace the resolver

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `usdresolve` asks the configured resolver to resolve an asset path exactly as USD would, which shows whether the resolver, its configuration or the context is at fault, and `TF_DEBUG` flags give detailed diagnostic output from the libraries. Hard-coding paths throws away the pipeline's resolver. Deleting references hides the problem, and file naming does not bypass a custom resolver.

**Key Concept:** [USD toolset: usdresolve](https://openusd.org/release/toolset.html)
</details>

---

### Question 29
**Scenario:** A pipeline script authors attributes on 50,000 prims, and it runs slowly because each edit triggers change processing and notifications.

A. Write the layer as text by hand and reload it, since the USD API is slow for any number of edits
B. Open the stage once for each prim, author its single attribute, and close the stage again
C. Wrap the edits in an `Sdf.ChangeBlock`, so change processing runs once when the block ends
D. Turn off composition entirely while editing, then turn it back on once the script has finished

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An `Sdf.ChangeBlock` batches layer edits so notification and recomposition happen once at the end of the block instead of after each edit, which greatly speeds bulk authoring; it is commonly used with the lower-level `Sdf` API. Hand-writing text is error-prone, reopening the stage per prim is far slower, and composition cannot simply be switched off.

**Key Concept:** [SdfChangeBlock](https://openusd.org/release/api/class_sdf_change_block.html)
</details>

---

### Question 30
**Scenario:** A lighting tool opens a shot stage with several department layers, and its edits must go only into the lighting layer, not the root layer.

A. Set the stage's edit target to the lighting layer before authoring, so new opinions go there
B. Make the lighting layer the weakest sublayer, so edits on the stage fall through to it by default
C. Save the whole stage to a new file after editing, which moves the edits into the lighting layer
D. Author the edits in the session layer, which writes them into the lighting layer when it is saved

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A `UsdEditTarget` controls which layer receives opinions authored through the stage API, so setting it to the lighting layer keeps each department's work in its own file. The edit target is the root layer by default, whatever the sublayer order. Saving a stage does not move opinions between layers, and the session layer is never saved into other layers.

**Key Concept:** [UsdEditTarget](https://openusd.org/release/api/class_usd_edit_target.html)
</details>

---

## Where to go deeper

- [NCP-OUSD cert page](../nvidia/openusd-development-professional/README.md) - notes, practice plan, strategy
- [NCA-GENM practice questions](nvidia-generative-ai-multimodal-associate.md) - generative content for 3D pipelines
- **[📖 OpenUSD documentation](https://openusd.org/release/index.html)** - primary source
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
