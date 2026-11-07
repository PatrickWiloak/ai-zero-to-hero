# Section 2: Content Aggregation (10%)

**Last reviewed:** 2026-11-07

Content aggregation is building large scenes out of reusable parts: model kinds, instancing (native and point) and strategies for overriding instances. The five objectives in NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) are: add a prototype to a point instancer; edit the color of an instance-proxy mesh without changing its instancing status; hide instances of a point instancer efficiently; implement and manage USD instances for asset reuse in large scenes; and remove properties from instanced component prims in an assembly stage. Code ran with `usd-core` 0.26.11 in a scratch environment.

## Model kinds: building blocks of an aggregate

The `kind` metadata classifies prims into a model role, a higher-level categorization than the prim's schema type (the Kind page calls kinds "useful for classifying scenegraph objects"). The core hierarchy: **model** is the root ("everything in the model hierarchy is a kind of model"); a **component** is a terminal model (a leaf that cannot contain other models); a **group** contains other models; an **assembly** is a group important enough to stand on its own, often a published asset; and a **subcomponent** marks articulable sub-trees within a component. A scene aggregates components into groups and assemblies, which lets tools select and traverse "things" rather than every mesh.

**[📖 Kind: extensible categorization](https://openusd.org/release/api/kind_page_front.html)** - The core kind hierarchy and custom kinds

- **Kind** - metadata that classifies a prim into a model role (model, group, assembly, component, subcomponent).
- **Component** - a leaf model that can contain subcomponents but no other models.
- **Assembly** - a group that is important enough to be treated as a unit, such as a published set or building.

## Native instancing

Native (scenegraph) instancing shares one composed copy of a prim's subtree among many instances: "Instancing in USD is a feature that allows many instances of 'the same' object to share the same representation." You mark a prim `instanceable`; it must bring in scene description through a composition arc such as a reference. USD groups instanceable prims that share a composition structure, variant selections, value clips, load rules and population mask into a hidden **prototype**; the instance's hierarchy sits under it.

**[📖 Scenegraph instancing](https://openusd.org/release/api/_usd__page__scenegraph_instancing.html)** - Authoring instances, prototypes, instance proxies and edit limits

I created three instanceable references to one tree asset:

```python
for i in range(3):
    p = s.DefinePrim(f"/World/Tree{i}", "Xform")
    p.GetReferences().AddInternalReference("/Assets/Tree"); p.SetInstanceable(True)
```

```
instanceable: True | prototypes: 1 | instance children via GetChildren: []
proxy: /World/Tree0/Crown IsInstanceProxy: True
```

Three instances, one prototype, and the instance has no children of its own. You reach what is beneath through **instance proxies** by traversing with `Usd.TraverseInstanceProxies()`; proxies are read-only views.

### Editing instances

The docs give the rules, and I tested them:

- You can override properties and metadata **on the instance prim itself** (`override on the instance prim itself works: ok`).
- You cannot override descendants of an instance, including through proxies. The API raises an error and (per the page) properties and metadata on descendant prims beneath instance prims cannot be overridden. Setting a color on the proxy's mesh raised `ErrorException` in my run.
- To customize an instance's inside, make it non-instanceable (`after SetInstanceable(False) children: ['Crown']`), or add inherit or specializes arcs to the instance and edit the class they target.

This is objective 2.2: to change the color of an instance-proxy mesh without losing the instancing, you cannot edit the proxy; you use the class-based route (an inherits or specializes arc to a class whose opinion drives the color), or you drive color from a primvar on the instance if the shader reads one (note 8), or accept de-instancing for that one instance. Which of these suits depends on the asset's design; the documentation states the first and the editing limits, and the primvar idea is a design pattern, not a documented procedure.

**Removing properties from instanced component prims (2.5)** follows from the same rules: you cannot remove or override a descendant's property through the instance. Make the instance non-instanceable and block or deactivate there (see note 1 on blocking), or change the source asset so all instances change.

Prototype paths are not stable: the docs warn "Consumers should not save or hard-code the paths to prims in prototypes." Native instancing is the right style for repeated *assets with internal structure* (a chair, a rack, a vehicle) used tens to thousands of times.

- **Instanceable** - metadata on a prim that asks USD to share its composed subtree with other identical instances.
- **Prototype** - the internal prim USD creates to hold the shared subtree for a group of identical instances; it is not part of the scene description.
- **Instance proxy** - a read-only view of a descendant of an instance, reached by traversing with instance proxies enabled.

## Point instancing

`UsdGeomPointInstancer` is "vectorized instancing of multiple, possibly animated, prototypes". It is for very large numbers of simple repeated elements (leaves, grass, debris, particles): "designed to scale to billions of instances", with a transform stored as position, orientation and scale (the docs give 32 bytes per instance against 64 for a single-precision matrix).

**[📖 UsdGeomPointInstancer](https://openusd.org/release/api/class_usd_geom_point_instancer.html)** - Prototypes, protoIndices, positions and masking

- The `prototypes` relationship lists prototype root prims; list order gives each a zero-based index.
- `protoIndices` (required, per instance) selects each instance's prototype; its length is the instance count.
- `positions` (required, per instance) gives the translation.

**Adding a new prototype (2.1):** add a target to the `prototypes` relationship; it takes the next index, and you then point instances at it through `protoIndices`. I ran it:

```python
pi.GetPrototypesRel().AddTarget("/Forest/Protos/Ball")      # becomes index 1
pi.GetProtoIndicesAttr().Set([0, 1, 0, 1, 0])
```

```
instance count 5
new prototype index: 1 protoIndices: [0, 1, 0, 1, 0]
```

The docs recommend placing prototypes under a `class` or `over` prim so default traversals skip them.

**Hiding instances efficiently (2.3):** the schema has two independent mechanisms: `inactiveIds` (list-edited, sparse, not animatable: `DeactivateId()`) and `invisibleIds` (animatable, cannot be authored sparsely: `InvisId()`). `ComputeMaskAtTime()` combines them. Hiding is done by id, without touching the instance data:

```python
pi.InvisIds([1, 3], 0)
```

```
hide ids 1,3 at t=0 -> invisibleIds: [1, 3] | mask: [True, False, True, False, True]
```

Choose `invisibleIds` when visibility must change over time, and `inactiveIds` for a static removal. Do not delete elements from `protoIndices` and `positions` just to hide them: that rewrites every per-instance array.

## Choosing between them (objective 2.4 and 1.2)

| Need | Style |
|---|---|
| Hundreds to thousands of copies of an asset that has internal structure, materials and variants | Native instancing |
| Millions of simple repeated elements, or per-element animated transforms | Point instancer |
| A one-off or a few copies, each customized | Plain references (no instancing) |

Mix them when the scale justifies it, for example a point instancer whose prototype is itself a natively instanced asset. The study guide lists the NVIDIA course *Learn OpenUSD: Asset Modularity and Instancing* for this topic.

- **PointInstancer** - a USD schema that draws many copies of a few prototypes with per-instance position, orientation and scale stored in arrays.
- **protoIndices** - the per-instance integer array in a PointInstancer that selects which prototype each instance uses.

## Check yourself against the objectives

Name the kind hierarchy; author an instanceable reference and say what you can and cannot edit on it; add a prototype and hide two instances in a point instancer; and choose native versus point instancing from a scale. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
