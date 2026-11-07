# Section 6: Debugging and Troubleshooting (11%)

**Last reviewed:** 2026-11-07

This section is about introspecting a stage to fix unexpected composition results, find badly authored data and speed up load and render. This was the gap the old guide listed as "not covered". The five objectives in NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf): identify when `SdfChangeBlock` removes a bottleneck; identify why one layer's opinions do not take effect; resolve asset management issues; understand what causes unexpected visual results; and work with diagnostics (`TfDebug`, diagnostic delegates, Trace, `TfMallocTag`). Code ran on `usd-core` 0.26.11.

## 6.2 Why an opinion from a layer does not take effect

The method is to ask the stage, not guess. In order:

1. **Read the stacks.** `prim.GetPrimStack()` lists every spec that contributes to a prim, strongest first; `prop.GetPropertyStack()` does the same for a property value. In my example a sublayer's `size = 2` outranked a reference's `size = 1`, which the stacks showed directly (note 1). `usdview` has a LayerStack tab for the same purpose.
2. **Check LIVERPS** against what you expected: local before inherits, variants, references, payloads, specializes.
3. **Check for mutes, deactivation and unloaded payloads** (`MuteLayer`, `SetActive(False)`, `Unload()`).
4. **Check the edit target.** Your `Set()` may have gone to a different layer than the one you are looking at.
5. **Check for composition errors.** A reference that failed to compose contributes nothing. I built a stage with a reference to a missing file and one prim referencing itself; the prim index reported both:

```python
for n in ("A", "B"):
    print(n, [type(e).__name__ + ": " + str(e)[:90] for e in s.GetPrimAtPath("/" + n).GetPrimIndex().localErrors])
```

```
A ... ['ErrorInvalidAssetPath: Could not open asset @/tmp/.../missing.usda@ ...']
B ... ['ErrorArcCycle: Cycle detected: ... CANNOT reference: ...']
```

The Pcp library ("PrimCache Population", composition) produces these errors; the study guide lists "Pcp: PrimCache Population (Composition) - Errors" and "UsdReferences - Reasons Why Adding a Reference May Fail" as reading. Also note that `over` does not create a typed prim: the FAQ says a `def` "tells the system to expect a type", while an `over` layers opinions onto a prim only if some layer defines it; `GetChildren()` skips prims that exist only as overs. A stack of overrides for a prim nobody defined is a common reason that "nothing shows up".

**[📖 USD FAQ: over versus typeless def](https://openusd.org/release/usdfaq.html)** - Why overs do not create prims on their own

## 6.1 SdfChangeBlock: when it removes a bottleneck

Every authoring edit to a layer sends notifications; with a stage open, each change triggers change processing. `Sdf.ChangeBlock` batches them: "Opening a block delays Sdf change notifications until the outermost block exits", so downstream consumers do one round of processing. I created 3,000 prim specs with a stage observing the layer, with and without a block:

```
3000 prim specs with stage open: no block 1.061s  | with ChangeBlock 0.025s
```

That is about 42 times faster here (one run on one machine, so read it as the shape of the effect, not a benchmark). Use it when authoring many specs at the `Sdf` level in a loop. The docs give two hard rules: "It is not safe to use Usd or other downstream API while a changeblock is open!!" (views would be stale and handles may be expired), and changeblocks "are very easy to use in an unsafe way that could make the system crash or corrupt data". The recommended pattern: gather the changes using the Sdf API first, then submit them all inside one block without calling Usd.

**[📖 SdfChangeBlock](https://openusd.org/release/api/class_sdf_change_block.html)** - Behavior and safety rules

- **SdfChangeBlock** - a scope that delays Sdf change notifications until the outermost block exits, so many edits cost one round of change processing; no Usd API may be used inside it.
- **Prim stack** - the ordered list of specs (strongest first) that contribute to a composed prim.

## 6.3 Asset management issues

The usual causes: an asset path that resolves differently on another machine (absolute paths, workstation-specific drives); a missing file; a resolver context not bound, so search paths are unavailable; a path changed by a version bump. Tools: the resolver docs say a resolved path "should be usable by downstream clients that do not have a resolver context bound", and `UsdStage.Open(..., pathResolverContext)` lets you give a stage its context. `Layer.GetExternalReferences()` lists a layer's dependencies, and the built-in `MissingReferenceValidator` flags unresolvable ones (note 4). Checking a layer's references for non-portable paths took a few lines:

```
external refs: ('./ok.usda', '/abs/studio/path.usda', 'C:\\proj\\win.usda') | not portable: ['/abs/studio/path.usda', 'C:\\proj\\win.usda']
```

(The backslashes printed doubled because I wrote them escaped in the test file.) Prefer anchored relative paths such as `./ok.usda`, or logical identifiers resolved by a custom resolver.

## 6.4 Unexpected visual results

Walk from data to pixels: wrong **extent** (note 5); wrong **primvar** length or interpolation; **visibility** or **purpose** (a prim with `purpose = proxy` is not drawn by a default render; I set `proxy` on a test mesh); **units and up axis**; **draw mode**; a **stronger material binding** at an ancestor (note 8: `strongerThanDescendants` on a parent beat a child's own binding in my run); **instancing** hiding your override (note 2); and **time** (an animated value evaluated at the wrong time code).

## 6.5 Diagnostics: TfDebug, delegates, Trace, TfMallocTag

- **Diagnostic delegates.** `UsdUtils.CoalescingDiagnosticDelegate` collects `Tf` warnings and errors (in the study guide's list as `UsdUtilsCoalescingDiagnosticDelegate`) instead of letting them print. Opening my broken stage produced two warnings from `stage.cpp`, available as a list of items, each with a source file and diagnostic code. Use it in a pipeline tool to turn warnings into a report or a failure.
- **TfDebug** enables named debug output by symbol. The registry has symbols such as `PCP_CHANGES`, `PCP_DEPENDENCIES`, `PCP_NAMESPACE_EDIT` and `PCP_PRIM_INDEX`, which trace composition. They are enabled by name through the Tf.Debug API or an environment variable.
- **Trace** records scoped timings. `Trace.Collector` with `Trace.TraceScope` works in the pip package (I recorded a scope while opening and traversing a stage; the collector ran). Use a Trace report to find what part of a load or traversal is slow.
- **TfMallocTag** tracks memory allocation by tag. It requires a USD build with malloc-tag support and was not run here.

Profiling load and render time ties to the study guide's "Maximizing USD Performance" reference (not fetched). Common remedies you can justify from this guide: payloads and population masks to load less; instancing to share data (note 2); `SdfChangeBlock` for bulk authoring; flatten for delivery; usdc for large files (note 4).

- **Diagnostic delegate** - a Tf hook that receives USD warnings and errors so a tool can collect or reroute them.
- **TfDebug** - USD's named debug-output facility (for example PCP_PRIM_INDEX traces composition).
- **Trace** - USD's scoped-timing profiler.

## Check yourself against the objectives

Name the call that shows every spec contributing to a prim; list five reasons an edit is ignored; say when a change block helps and what you must not do inside it; check a layer for non-portable paths; and name the four diagnostic tools. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
