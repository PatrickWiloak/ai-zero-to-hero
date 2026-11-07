# Section 3: Customizing USD (6%)

**Last reviewed:** 2026-11-07

The smallest content section, and the one that needs a compiled USD build to practice: extending USD with plug-ins. NVIDIA's [study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/sjrg2vjhic7285sph487x53f5e54erf7.pdf) lists eight objectives: build a USD plug-in against a given USD version; build USD from scratch with custom dependencies; create custom model kinds; create custom schemas for proprietary data; integrate a custom resolver; use schemas to carry nonstandard attributes during import/export; write a SceneIndex plug-in that generates renderable geometry as Hydra prims; and write an AssetResolver that generates in-memory renderable primitives.

None of the build-based code can be run with the pip package `usd-core` (it ships no compiler toolchain or headers), so everything here is documentation, quoted and marked not run. Where the documentation I could read does not cover an objective, I say so.

## How USD finds plug-ins

USD discovers extensions through `plugInfo.json` files registered with the plug-in registry (`PlugRegistry`). A plug-in can contribute schemas, file formats, asset resolvers and kinds. The same registration pattern appears in each topic below. (That a plug-in has to be built against the USD version it runs in is the premise of objective 3.1, not something these pages state.)

**[📖 Asset resolution (Ar)](https://openusd.org/release/api/ar_page_front.html)** - How Ar uses plugInfo.json to find resolvers

## Custom model kinds (objective 3.3)

The kind registry begins with the core hierarchy (model, group, assembly, component, subcomponent), and you extend it in `plugInfo.json` under `Info` with a `Kinds` dictionary that names each kind, its `baseKind` and a description:

```json
// Not run: from the OpenUSD Kind documentation
"Info": {
    "Kinds": {
        "chargroup": { "baseKind": "assembly",
                       "description": "A chargroup is an assembly comprised of a single character plus some associated models." },
        "charprop":  { "baseKind": "component" }
    }
}
```

You cannot change core kinds, their position in the hierarchy or their data this way; attempting it causes a registration error. Create a custom kind when your pipeline needs a role that the core kinds cannot express (for example a character prop that is a kind of component) and it should be queryable by kind. Don't create one if a core kind and a naming convention already do the job.

**[📖 Kind](https://openusd.org/release/api/kind_page_front.html)** - Core kinds and custom registration

## Custom schemas (objectives 3.4 and 3.6)

A schema is a typed definition of the properties a prim should have. Two families:

- **IsA (typed) schemas** give a prim a type name and must derive from `UsdTyped` (like `Mesh`). A concrete one has both a schema name and a type name; a non-concrete (abstract) one is only a base class.
- **API schemas** add an interface to a prim without changing its type name; by convention their names end in "API"; they can be single-apply, multiple-apply or non-applied, and applied ones need an explicit `Apply()` call.

You write the definition in a `schema.usda` layer that sets a `libraryName` in its `GLOBAL` customData and run `usdGenSchema`, which generates C++ and Python wrapper code, `generatedSchema.usda` and `plugInfo.json`. Code written after the `// --(BEGIN CUSTOM CODE)--` delimiter survives regeneration. Setting `skipCodeGeneration` produces **codeless schemas**: only `generatedSchema.usda` and `plugInfo.json`, usable without recompiling USD, though clients can query them only through the basic USD APIs.

```
# Not run: from the OpenUSD docs
usdGenSchema
usdGenSchema --help
```

For nonstandard attributes during import/export (3.6), a schema gives that data a typed, discoverable home with declared types and fallbacks, instead of loose custom attributes that every tool treats differently. Whether to write a schema or to use plain namespaced attributes is a design decision: schema when many tools must agree on the data; namespaced attributes when it is one tool's private state.

**[📖 Generating new schema classes](https://openusd.org/release/api/_usd__page__generating_schemas.html)** - usdGenSchema, IsA and API schemas, codeless schemas
**[📖 Tutorial: generating new schema classes](https://openusd.org/release/tut_generating_new_schema.html)** - Step-by-step schema tutorial

- **IsA schema** - a typed schema that gives a prim its type name (for example Mesh).
- **API schema** - a schema that adds properties and behavior to a prim without changing its type name.
- **usdGenSchema** - the tool that reads a schema.usda layer and generates the schema's classes, registration files and generatedSchema.usda.
- **Codeless schema** - a schema generated with skipCodeGeneration, which produces only generatedSchema.usda and plugInfo.json.

## Custom resolvers (objectives 3.5 and 3.8)

The Ar library queries, reads and writes asset data so USD can access assets without knowing how they are stored. `ArResolver` is the central interface; `ArDefaultResolver` is the fallback and "treats asset paths as filesystem paths", searching a list of directories. A custom resolver is a subclass of `ArResolver` registered with `AR_DEFINE_RESOLVER` and declared in `plugInfo.json`; and, importantly for the exam, "Ar does not support custom resolvers implemented in Python to avoid performance issues". A **URI/IRI resolver** declares its schemes (for example `http`) under `uriSchemes` and receives only paths that begin with them. **Resolver contexts** carry configuration such as extra search paths; a context-dependent resolved path should be usable without the context. Resolvers are "responsible for validation, normalization, and parsing of asset paths", which is how a pipeline maps a logical asset id like `asset://chair/v3` to a file, or a database fetch.

Writing an AssetResolver that generates in-memory renderable primitives (3.8) means the resolver returns data produced on demand rather than read from a file. The Ar page documents the interface and registration; it does not give an in-memory-geometry example, and I could not retrieve one, so that objective is not covered at code level.

- **ArResolver** - the interface through which USD resolves, reads and writes assets; custom resolvers are plug-ins implemented in C++.
- **Resolver context** - configuration (such as search paths) bound to a stage to guide how asset paths resolve.

## File format plugins, SceneIndex, building USD (objectives 3.1, 3.2, 3.7)

- **File format plug-ins** teach USD to read other formats. The Sdf documentation links to a "Creating a File Format Plugin" page, which I could not retrieve; from the study guide I know only that it is a listed API reference.
- **SceneIndex plug-ins** (3.7) generate Hydra prims directly. The study guide lists the objective, but the documentation I fetched does not cover it, so it is not described here.
- **Building a plug-in against a given USD version, and building USD from scratch** (3.1, 3.2) are build-system tasks. The pages I read do not cover them (and the pip package has no build tooling), so they are outside study here; the study guide lists them as objectives.

## Check yourself against the objectives

Write the `Kinds` JSON for a new kind; tell IsA from API schemas and say what codeless means; say why a resolver cannot be written in Python; and say what must match between USD and a plug-in. Questions are in the [NCP-OUSD practice bank](../../../practice-questions/nvidia-openusd-development-professional.md).
