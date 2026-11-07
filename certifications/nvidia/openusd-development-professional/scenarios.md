# NCP-OUSD - Scenarios

**Last reviewed:** 2026-11-07

Eight original scenarios written for this guide, with answers backed by the code run in the notes.

## 1. The override that does nothing

An artist adds an override in a new layer and the value does not change. **Check:** `GetPropertyStack()` and the prim stack to see every contributing spec and its order; whether the layer is actually in the stage's layer stack (and not muted); the edit target; and any composition errors on the prim index (`localErrors`).

## 2. The same cycle, staggered

An animated asset must appear five times, each starting two frames later. **Answer:** reference it five times with `Sdf.LayerOffset(0, 1)`, `(2, 1)`, `(4, 1)` and so on; in the run in note 1, an offset of 5 made the value at time 10 equal the original's value at time 5.

## 3. A forest with a million trees

**Answer:** a `PointInstancer` with a few prototypes, `protoIndices` and `positions`. To hide some trees use `invisibleIds` (animatable) or `inactiveIds` (static) rather than rewriting arrays. For a few hundred copies of one building with internal structure, use native instancing instead.

## 4. Recolor one instanced chair

You cannot edit the proxy beneath an instance (the API raises an error). Options: change the instance prim's own properties, make that single instance non-instanceable, or add an inherits/specializes arc whose class drives the change.

## 5. An export that opens fine but loads slowly

Profile before changing: a Trace report for the slow section, `usdcat -f` to see whether composition is deep, and check for payloads that could be unloaded. For bulk authoring in a tool, use `Sdf.ChangeBlock` (about 42 times faster in the note 6 run) with no Usd calls inside it.

## 6. A mesh disappears after editing its points

The authored `extent` is stale. Recompute it with `UsdGeom.Boundable.ComputeExtentFromPlugins()` and set it (note 5).

## 7. Material ignored on a child mesh

A parent's material binding is `strongerThanDescendants`, which beats the child's own binding (note 8). Change the parent's strength or bind lower.

## 8. Delivering to an external party

Flatten a copy so no composition arcs or proprietary layers remain, validate asset paths (no absolute or drive-letter paths), run the missing-reference validator, and package as `.usdz` if a single file is needed.
