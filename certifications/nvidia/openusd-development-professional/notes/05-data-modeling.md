# Section 5: Data Modeling (13%)

**Last reviewed:** 2026-11-07

Data modeling is the nuts and bolts: prims, properties (attributes and relationships), value types, time samples, primvars and the built-in schemas. NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) lists six objectives: add a primvar to a mesh; choose value types for attribute data; represent custom metadata; retrieve properties of a prim; understand what causes unexpected visual results; and update a mesh's extent after changing its points. Everything runs on `usd-core` 0.26.11.

## Prims, properties and value types

A stage is a tree of **prims**. A prim has **properties**: **attributes** (typed values, which can vary over time) and **relationships** (pointers to other prims or properties). Each attribute has a value type from Sdf, such as `float`, `token`, `matrix4d`, `color3f` or arrays like `float3[]`. Choosing the right value type matters: `token` for fixed vocabularies (cheap, interned), `string` for free text, `float`/`double` for scalars depending on precision, `matrix4d` for 4x4 transforms, `color3f` and `normal3f`/`point3f` for values with semantic roles (so tools treat them as colors, normals or points when transforming).

**[📖 Sdf basic datatypes](https://openusd.org/release/api/sdf_page_front.html)** - The Sdf value types and scene description foundations
**[📖 Tutorial: inspecting and authoring properties](https://openusd.org/release/tut_inspect_and_author_props.html)** - Reading and writing properties

I authored typed attributes and read them back (UsdGeom's Xform adds its own properties):

```python
a = p.CreateAttribute("mass", Sdf.ValueTypeNames.Float, custom=True)
b = p.CreateAttribute("label", Sdf.ValueTypeNames.Token)
c = p.CreateAttribute("pivot", Sdf.ValueTypeNames.Matrix4d)
print([(q.GetName(), str(q.GetTypeName())) for q in p.GetAttributes()])
```

```
types: [('label', 'token'), ('mass', 'float'), ('pivot', 'matrix4d'), ('purpose', 'token'), ('visibility', 'token'), ('xformOp:translate', 'double3'), ('xformOpOrder', 'token[]')]
properties: ['label', 'mass', 'pivot', 'proxyPrim', 'purpose', 'visibility', 'xformOp:translate', 'xformOpOrder'] | authored only: ['label', 'mass', 'pivot', 'xformOp:translate', 'xformOpOrder']
```

## 5.4 Retrieve properties of a prim

`prim.GetProperties()` and `GetAttributes()` return everything the prim *has*, including properties that come from its schema even if unauthored (note `purpose`, `visibility` and `proxyPrim` in the first list); `prim.GetAuthoredPropertyNames()` returns only what some layer actually wrote. Know the difference: a missing value on an unauthored schema property returns the schema's fallback, not an error. Relationships: `rel.GetTargets()` (mine returned `[Sdf.Path('/B')]`). To see where a property's value comes from, use `GetPropertyStack()` (note 1).

## Time samples and TimeCode

Attributes can have a **default** value, **time samples**, or both. A time-sampled attribute stores (time, value) pairs; between samples USD interpolates (linear by default for types that support it) or holds, depending on `Stage.SetInterpolationType`. I authored a translate op with samples at 0 and 10:

```
time samples: [0.0, 10.0] at 5 (linear): (5, 0, 0) at 12 (held): (10, 0, 0)
held interpolation at 5: (0, 0, 0)
```

Linear interpolation gives (5, 0, 0) at time 5; after the last sample the value is held; switching the stage to held interpolation gives the earlier sample's value (0, 0, 0). Time itself is a `UsdTimeCode`; `Usd.TimeCode.Default()` addresses the default (non-animated) value, so `mass` had a default of 2.5 and, after authoring a time sample at 5, 3.0 at time 5 while the default stayed 2.5. The glossary mentions "UsdTimeCode::Default()" as the reserved sentinel for static, time-independent values. Layer offsets (note 1) shift time when a layer is brought in by a reference.

**[📖 Time and animated values](https://openusd.org/release/user_guides/time_and_animated_values.html)** - Time samples and interpolation

- **Prim** - a node in a USD stage's namespace hierarchy that holds properties and children.
- **Attribute** - a typed property that holds a value, optionally varying over time.
- **Relationship** - a property that points to other prims or properties by path.
- **Time sample** - a (time, value) pair stored on an attribute; USD interpolates or holds between samples.
- **TimeCode** - the time at which an attribute is evaluated; the default time code addresses the non-animated default value.

## 5.3 Custom metadata

Metadata is data about a prim or property, not part of its attributes. USD offers core metadata fields (such as `comment` and `kind`) and a free-form dictionary called **customData** for pipeline-specific data. I set both:

```python
p.SetCustomDataByKey("pipeline:owner", "lighting"); p.SetMetadata("comment", "wip")
```

```
custom metadata: {'pipeline': {'owner': 'lighting'}, ...} | comment: wip
```

Note the colon in the key created a nested dictionary (`pipeline` containing `owner`). Use customData for tool-private annotations that should not be a schema, namespaced by your pipeline's prefix. Use a custom attribute instead when the value needs to animate, be connected, or be visible to every renderer's property tools; metadata cannot vary over time. The Sdf docs describe `plugInfo.json` registration of new metadata fields (`SdfMetadata`) when you want a new official field.

## Primvars (5.1)

A primvar is "a special attribute that a renderer associates with a geometric primitive" and interpolates across its surface, living in the `primvars:` namespace. Primvars "inherit down scene namespace", and can serve as per-primitive overrides for the bound material. The interpolation mode says how many values and how they spread: **constant** (one value for the whole primitive), **uniform** (one per face for meshes), **varying** (per corner of each patch, bilinear), **vertex** (per vertex, interpolated with the surface basis) and **faceVarying** (per face corner, for polygons, which allows hard edges). Indexed primvars store unique values once and map elements with an indices array.

**[📖 UsdGeomPrimvar](https://openusd.org/release/api/class_usd_geom_primvar.html)** - Interpolation modes, indexing and creation

`UsdGeom.PrimvarsAPI.CreatePrimvar()` is described as "the only way to create a new Primvar in scene description" (you cannot turn an existing attribute into a primvar by renaming). I created per-vertex colors on a quad:

```python
pv = UsdGeom.PrimvarsAPI(mesh).CreatePrimvar("displayColor", Sdf.ValueTypeNames.Color3fArray, UsdGeom.Tokens.vertex)
pv.Set([(1,0,0),(0,1,0),(0,0,1),(1,1,1)])
```

```
primvar primvars:displayColor interp vertex values 4 | namespace: primvars
```

A common wrong-looking-result cause: a vertex primvar needs one value per point; a uniform one needs one per face; the wrong length is ignored or misrendered by renderers.

- **Primvar** - a geometry attribute in the `primvars:` namespace that a renderer interpolates across a surface (colors, UVs, widths).
- **Interpolation (primvar)** - the rule for how a primvar's values map to a surface: constant, uniform, varying, vertex or faceVarying.
- **customData** - a free-form metadata dictionary on a prim or property for pipeline-specific annotations.

## 5.6 Update the extent after changing points

A boundable prim's `extent` attribute is its bounding box (min and max corners), used by renderers and tools for culling and framing. Changing `points` does *not* update it. A stale extent is a classic cause of geometry that disappears or is mis-framed. Recompute it after editing points:

```python
m.GetPointsAttr().Set([(0,0,0),(5,0,0),(5,5,0),(0,5,0)])
m.GetExtentAttr().Set(UsdGeom.Boundable.ComputeExtentFromPlugins(m, Usd.TimeCode.Default()))
```

```
extent before recompute: None      # I never authored one
extent after recompute : [(0, 0, 0), (5, 5, 0)]
```

The study guide's reading list names `UsdGeomBoundable::ComputeExtentFromPlugins()` and `GetExtentAttr()` for exactly this.

## 5.5 Unexpected visual results: a short list of causes

From this section's material: a stale or missing extent; a primvar with the wrong interpolation or element count; wrong up axis or units (the stage metadata: my test stage set `upAxis Z` and `metersPerUnit 0.01`); time interpolation (held versus linear); a stronger opinion hiding your edit (note 1); and visibility or purpose settings (note 8). Note 6 covers how to find out which.

## Check yourself against the objectives

Pick a value type for an attribute and defend it; list the properties a prim has and the ones that are authored; read an animated value at an unsampled time; write a customData key; create a vertex primvar; and recompute an extent. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
