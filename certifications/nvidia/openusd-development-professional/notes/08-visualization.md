# Section 8: Visualization (8%)

**Last reviewed:** 2026-11-07

Visualization covers the three domains used in almost every USD scene: `UsdGeom` (meshes, cameras), `UsdShade` (materials) and `UsdLux` (lights). NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) has four objectives: add a primvar to a mesh; assign `UsdPreviewSurface` materials for visualization; bind materials to a mesh; and create a `UsdPreviewSurface` network that reads diffuse color from a primvar. Everything ran on `usd-core` 0.26.11.

## 8.1 Add a primvar to a mesh

Covered in note 5: `UsdGeom.PrimvarsAPI(mesh).CreatePrimvar(name, type, interpolation)` is the only way to create a primvar, and the interpolation (constant, uniform, varying, vertex, faceVarying) must match the element count. Per-vertex `displayColor` on a four-point quad gave `primvar primvars:displayColor interp vertex values 4`.

**[📖 UsdGeomPrimvar](https://openusd.org/release/api/class_usd_geom_primvar.html)** - Creating primvars and interpolation

## 8.2 UsdPreviewSurface materials

`UsdPreviewSurface` is a shading node in the OpenUSD spec (the page header says version 2.5, while its changelog lists 2.6 as current head) that provides "a basic physically based material for exchanging assets between content creation tools, game engines, and production renderers". It supports specular and metallic workflows and deliberately omits subsurface scattering and anisotropic highlights. Key inputs and defaults from the spec:

| Input | Type | Default | Meaning |
|---|---|---|---|
| `diffuseColor` | color3f | 0.18 gray | Albedo in the metallic workflow |
| `useSpecularWorkflow` | int | 0 | 1 drives reflectance with `specularColor`; 0 uses `metallic` |
| `metallic` | float | 0.0 | Near 1 for metals |
| `roughness` | float | 0.5 | 0 smooth to 1 rough |
| `opacity` | float | 1.0 | Transparency (with `opacityMode` and `opacityThreshold`) |
| `normal` | normal3f | (0, 0, 1) | Tangent-space normal |

**[📖 UsdPreviewSurface specification](https://openusd.org/release/spec_usdpreviewsurface.html)** - Inputs, UsdUVTexture and primvar readers

A material is a `UsdShade.Material` prim with a shader child and a `surface` output connected to the shader's output. I built one:

```python
mat = UsdShade.Material.Define(s, "/Looks/Red")
sh = UsdShade.Shader.Define(s, "/Looks/Red/Surface"); sh.CreateIdAttr("UsdPreviewSurface")
sh.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(.8, 0, 0))
sh.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(.4)
mat.CreateSurfaceOutput().ConnectToSource(sh.ConnectableAPI(), "surface")
```

Texture inputs use `UsdUVTexture` (with `file`, `st`, `wrapS`/`wrapT`, `scale`/`bias`, `sourceColorSpace`), with `st` usually connected from a primvar reader. For an 8-bit normal map the spec recommends setting the source color space to raw so the data is not converted to sRGB.

- **UsdPreviewSurface** - a basic physically based shading node in the OpenUSD spec for exchanging assets between tools, engines and renderers.
- **UsdUVTexture** - the shading node that reads an image texture using texture coordinates.

## 8.3 Bind materials to a mesh

`UsdShade.MaterialBindingAPI` authors the bindings. `Bind(material)` makes a direct binding; the relationship is `material:binding`. Rules from the API docs:

- **Strength** is stored in `bindMaterialAs`: `weakerThanDescendants` (the default) or `strongerThanDescendants`. Bindings lower in the namespace are stronger than ancestor bindings unless the ancestor is `strongerThanDescendants`.
- **Collection bindings** beat direct bindings at the same prim; **purpose-restricted** bindings (`full`, `preview`) beat all-purpose ones.
- **Subset binding** binds a material to some faces: `CreateMaterialBindSubset()` makes `GeomSubset`s in the `materialBind` family; renderers honor subset bindings only for that family name.

**[📖 UsdShadeMaterialBindingAPI](https://openusd.org/release/api/class_usd_shade_material_binding_a_p_i.html)** - Binding, strength, purposes and subsets

I tested the rules:

```
subset family: materialBind | elements [1] | mesh binding: /Looks/Red | subset binding: /Looks/Blue
child bound blue but parent strongerThanDescendants red -> /Looks/Red
```

The first line: a two-face mesh bound to Red with face 1 given a subset bound to Blue. The second: a child bound to Blue still resolved to Red because its parent's binding was `strongerThanDescendants`. That override is a typical cause of "my material is ignored".

- **MaterialBindingAPI** - the UsdShade schema that binds a material to a prim or collection with a strength and purpose.
- **GeomSubset** - a UsdGeom prim that selects a subset of a mesh's elements, used to bind different materials to different faces.

## 8.4 A UsdPreviewSurface network that reads diffuse color from a primvar

Color has no dedicated reader type. Choose the primvar reader by the primvar's type: `UsdPrimvarReader_float3` for color3f/float3 and `UsdPrimvarReader_float4` for color4f/float4, set its `varname` to the primvar's name, and connect its `result` output to the surface's `diffuseColor`. The spec adds that color read from a mesh is ready for use as is, with no premultiplication. I built it:

```python
rd = UsdShade.Shader.Define(s, "/Looks/Red/ColorReader"); rd.CreateIdAttr("UsdPrimvarReader_float3")
rd.CreateInput("varname", Sdf.ValueTypeNames.String).Set("displayColor")
rd.CreateOutput("result", Sdf.ValueTypeNames.Float3)
sh.GetInput("diffuseColor").ConnectToSource(rd.ConnectableAPI(), "result")
```

```
diffuseColor now reads: /Looks/Red/ColorReader varname displayColor
```

The primvar reader reads the mesh's `displayColor` primvar (the per-vertex colors from 8.1); the surface now takes its albedo from the geometry.

## Lights and cameras

`UsdLux` defines lights. I authored a `DistantLight` (intensity 3, angle 0.53 degrees) and the prim carried the applied schemas `LightAPI` and the light/shadow link collections. The study guide's API reading list covers `UsdLuxLightAPI`, `UsdLuxShadowAPI`, `UsdLuxDistantLight` and `UsdLuxShapingAPI`. `UsdGeom.Camera` has `focalLength` (35 in my test) and `clippingRange`. Prim **purpose** (`default`, `render`, `proxy`, `guide`) says how a prim participates in rendering; a mesh with purpose `proxy` is a stand-in drawn only in proxy displays (the study guide lists "Imageable Purpose" as reading).

- **UsdLux** - the USD domain for lights (distant, dome, rect, sphere and others) and light-related schemas.
- **Purpose (imageable)** - an attribute (default, render, proxy, guide) that says in which kinds of display a prim is drawn.

## Check yourself against the objectives

Build a preview surface and connect it to a Material; bind it to a mesh and to a face subset; predict which binding wins given two strengths; wire a primvar reader into `diffuseColor`; and name two inputs of `UsdPreviewSurface`. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
