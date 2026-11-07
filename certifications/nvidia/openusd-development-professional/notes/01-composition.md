# Section 1: Composition (23%)

**Last reviewed:** 2026-11-07

Composition is the biggest topic on the exam and the heart of OpenUSD: how many layers of scene description are assembled into one stage, and which opinion wins when they disagree. NVIDIA's official [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) (version 1.1.0, read 2026-11-07) lists eleven objectives under it, and this note follows them. Logistics and weights are on the [exam page](https://www.nvidia.com/en-us/learn/certification/openusd-development-professional/).

All the code in this guide was run in a throwaway virtual environment under `~/.cache` with `usd-core` 0.26.11 (`pip install usd-core`), so the output shown is real. Snippets that need a full USD build, a DCC or a plug-in toolchain are marked not run.

## Composition arcs and LIVERPS

A stage is built by **composition**, "the process that assembles multiple layers together by the composition arcs that relate them". The arcs the glossary lists are sublayers, inherits, variant sets, references, payloads and specializes (plus relocates in the strength ordering). When two layers have opinions about the same attribute, the strength order is **LIVERPS**: "Local, Inherits, VariantSets, Relocates, References, Payload, Specializes". Local opinions (the layer stack's own, including sublayers) are strongest; specializes are weakest. The study guide spells it LIVRPS in places; it is the same list.

**[📖 OpenUSD glossary](https://openusd.org/release/glossary.html)** - Definitions of the arcs, LIVERPS, edit targets and flattening

Explaining LIVERPS in simple terms (objective 1.6): when you ask a prim for a value, USD looks at the opinions in this order and takes the first one it finds. What you wrote right there in the layer stack wins; then what the prim inherits from a class; then the selected variant; then references; then payloads; and last, specializes.

I ran the classic check: a reference supplies `size = 1`, a sublayer of the root layer overrides it with `size = 2`:

```python
st = Usd.Stage.Open("root.usda")          # root has subLayers=[sub.usda], prim references ref.usda
a = st.GetPrimAtPath("/World/Asset").GetAttribute("size")
print(a.Get(), [(s.layer.GetDisplayName(), s.default) for s in a.GetPropertyStack()])
```

```
size = 2.0
property stack: [('sub.usda', 2.0), ('ref.usda', 1.0)]
```

The sublayer's opinion is "local" to the layer stack, so it beats the reference. Add a direct opinion in the root layer and it wins over both (`size = 3.0` in my run).

- **LIVERPS** - the strength ordering of composition arcs: Local, Inherits, VariantSets, Relocates, References, Payload, Specializes.
- **Composition arc** - an operator that combines layers: subLayers, inherits, variantSets, references, payloads, specializes.

## 1.1 Change the strength of an opinion

You change which opinion wins by changing where it is authored, not by editing the stronger one. Options: author in a stronger layer (an override in a layer higher in the root layer stack, or the session layer), use a different arc (a local opinion beats a referenced one), or change the **edit target** so that an edit lands in a different layer. The glossary describes an edit target as specifying which contributing site in the stage's network of composition arcs should receive the authored opinions. Running with the edit target set to the session layer:

```python
with Usd.EditContext(st, st.GetSessionLayer()):
    a.Set(9.0)
```

```
session layer opinion 9 wins: 9.0 | root layer unchanged: True
```

I confirmed the ordering on a stage whose root lists two sublayers: the layer stack was `['ord-session.usda', 'ord.usda', 'l1.usda', 'l2.usda']`, the session layer first (strongest), and the first-listed sublayer's value (1) beat the second's (2).

- **Edit target** - the layer (or variant, or reference) where `Set()` and other authoring calls put their opinions on a composed stage.

## 1.3 Referencing, payloads and sublayers

| Arc | What it does | Use it for |
|---|---|---|
| Sublayer | Adds a layer into the layer stack of the layer that lists it; paths stay in the same namespace | Splitting one scene or asset into departmental layers (modeling, shading, animation) in the same namespace |
| Reference | Pulls a prim's subtree from another layer into a place in this namespace, remapping the path | Building an assembly out of assets: the same asset placed many times at different paths |
| Payload | A reference that can be unloaded | Heavy content you may not want in memory |

The USD FAQ gives the rule of thumb: "If it satisfies your requirements, prefer sublayering over referencing"; references are better when layers have different namespaces, since they can remap prims (the FAQ's example remaps /Bob to /Characters/Bob_1) and can expose only selected prims. The glossary calls a payload "a special kind of a Reference" and notes payloads are weaker than references. I ran load and unload:

```python
pp.GetPayloads().AddPayload("heavy.usda", "/Heavy")
```

```
payload loaded: True ['S']
after Unload: [] | HasPayload: True
```

After `Unload()` the prim still *has* a payload, but its content is not composed in memory.

**[📖 USD FAQ: sublayers or references?](https://openusd.org/release/usdfaq.html)** - The recommendation and the namespace argument
**[📖 Tutorial: referencing layers](https://openusd.org/release/tut_referencing_layers.html)** - Reference syntax and behavior

- **Sublayer** - a layer added into another layer's layer stack, in the same namespace, ordered by strength.
- **Reference** - an arc that composes a prim hierarchy from another layer into a prim, used to build larger aggregates from smaller units.
- **Payload** - a reference that can be loaded or unloaded, used to defer heavy content.

## 1.4 The same animation at different time offsets

A reference (or sublayer) can carry a **layer offset**: a time offset and scale applied to the data it brings in. The glossary says "Composition arcs such as References and SubLayers can include an offset and scaling of time". Two prims referencing one clip, one offset by five frames:

```python
s.DefinePrim("/A").GetReferences().AddReference("anim.usda", "/Ball", Sdf.LayerOffset(0, 1))
s.DefinePrim("/B").GetReferences().AddReference("anim.usda", "/Ball", Sdf.LayerOffset(5, 1))
```

```
layer offset A at t=10: (10, 0, 0)   at t=5: (5, 0, 0)
layer offset B at t=10: (5, 0, 0)   at t=5: (0, 0, 0)
```

B shows at time 10 what A showed at time 5: it starts five frames later. This is how one animated asset is reused as a crowd with staggered timing. The tutorial for it is [Transformations, Animation, and Layer Offsets](https://openusd.org/release/tut_xforms.html).

- **Layer offset** - a time offset and scale applied to the values brought in by a reference or sublayer.

## 1.7 When variants are or are not appropriate

A **variant set** is a named set of alternative contents on a prim, with one selected variant. I authored a `finish` variant set with `wood` and `metal` variants that change an attribute, and selecting `metal` gave the metal color (`variants ['metal', 'wood'] selected metal`).

Variants are right for a small set of mutually exclusive alternatives of the same asset that belong inside it: finishes, levels of detail, states. They are wrong when the alternatives are really different assets, differ in large structure, or need to be assembled by different people in parallel; use references there. They are also wrong for per-instance tweaks of an asset used many times, where an override or an instance-level choice is cheaper. Variant selections are part of what makes instances share a prototype (see note 2), so many different selections defeat instancing.

**[📖 Tutorial: authoring variants](https://openusd.org/release/tut_authoring_variants.html)** - Variant sets, edit contexts and selection

- **Variant set** - a set of named alternatives on a prim from which one variant is selected at a time.

## 1.5 and 1.11 Layering strategies, and splitting a monolithic asset

Layering strategy is the design of which layers exist and in what order. The sublayer arc makes strength follow list order (first listed is strongest), so a shot layer stack can put a lighting layer above an animation layer above a set layer, and each department writes only its own file. Splitting a monolithic asset follows the same logic: break a big file into a geometry layer, a materials layer and an animation layer, each owned by one workstream, and bring them together with sublayers in a thin top-level file, so that two people never edit the same file. NVIDIA's reading list for these objectives includes the ASWF asset structure guidelines and "Principles of Scalable Asset Structure in OpenUSD" (listed in the study guide's Pipeline Development section); this guide did not fetch them, so the specific layer names above are an illustration, not their recommendation.

## 1.8 Why an opinion does not take effect

When an edit seems ignored, work through the causes in order:

1. **A stronger opinion exists.** Read the property stack (`GetPropertyStack()`) or the prim stack to see every contributing spec and their order. In my run the prim stack of `/World/Asset` was `[('root.usda', ...), ('sub.usda', ...), ('ref.usda', '/Asset')]`.
2. **Wrong arc or wrong target.** Your override was authored in a layer the stage does not use, or you authored on the referenced path rather than the composed path.
3. **The layer is muted.** After `MuteLayer()` on the sublayer, the stage fell back to the reference's value (`size = 1.0`).
4. **The prim is inactive or the payload is unloaded**, so nothing composes there.
5. **Instancing blocks it.** Opinions on descendants of an instance are ignored (note 2).
6. **The arc did not compose**, so the target does not exist; the `Pcp` composition errors report why (note 6).

## 1.9 Prepare an internal asset for external delivery

The tool is flattening: `UsdStage::Flatten()` (and `usdcat --flatten`) collapse the stage into one layer with no arcs left. The glossary describes flattening as collapsing a stage into one layer with no composition arcs left. I flattened the example stage and checked:

```
flattened layer has subLayers: [] | references on prim: () | size 2.0
```

The value is baked in (2.0) and the sublayer and reference are gone. Flattening also resolves internal dependencies, but it has a cost: variants and structure are lost, so deliver a flattened copy and keep the layered original. Before shipping, check no proprietary paths remain (note 7 covers validation and USDZ packaging).

## 1.2 and 1.10 Instancing style, and removing properties from instanced prims

Which instancing style to use at different scales belongs to note 2. For 1.10, the OpenUSD instancing page is explicit that "properties and metadata on descendant prims beneath instance prims cannot be overridden"; to customize an instance you make it non-instanceable, or add inherit or specializes arcs to the instance and edit the class they target. To make an attribute produce no value you can **block** it: the glossary says "the value that an attribute produces can be blocked by an overriding opinion of None". I ran this:

```
blocked attribute value: None | HasAuthoredValue: False
```

Blocking removes the value without deleting the underlying spec in the weaker layer, so it is reversible; deactivating a prim (`SetActive(False)`) removes a whole subtree from the stage (`still in stage? False`).

## Check yourself against the objectives

State LIVERPS and predict which of two opinions wins; say where an edit lands for a given edit target; choose between sublayer, reference and payload; build a time-offset reference; say when a variant is the wrong tool; explain why an opinion is not taking effect; and flatten for delivery. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
