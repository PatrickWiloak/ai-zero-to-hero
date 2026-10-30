# Feature Catalogue

The canonical list of what a reader of AI Zero to Hero (<https://ai.noblerworks.com/>) can see and do, plus the generators and checks that keep it current.
Update this file in the same commit as any user-visible change. It lists sections and capabilities, not every article - the generated [INDEX.md](../INDEX.md), [EXPLAINERS.md](../EXPLAINERS.md) and pillar hubs list the pages.
Repo-only file: it is excluded from the published site (`exclude_docs` in [mkdocs.yml](../mkdocs.yml)).

## Site sections

- **Landing page** (`/`, [.github/site/home.md](../.github/site/home.md)) - site-only front page with entry buttons (start from zero, AI for your job, build, read the research), a stat strip and "where are you starting" cards. Every number on it is a `{{token}}` filled by `render_home()` in [scripts/build_manifest.py](../scripts/build_manifest.py), so counts cannot drift from the tree. The repo `README.md` stays the GitHub front page and is not published.
- **Learn pillar** (`learn/`) - paths by audience (everyone, leaders, engineers, ML engineers, researchers, the full zero-to-hero path), day-one basics and core concepts. Sections: Start Here, Day One, Core Concepts.
- **AI at Work pillar** (`work/`) - team enablement, playbooks by role, and use cases.
- **Build pillar** (`build/`) - hands-on projects and production patterns. Some project code is still untested against live APIs (see [TODO.md](../TODO.md), 2026-11-08 items).
- **Tools pillar** (`tools/`) - comparisons and decision guides for models, frameworks, vector stores, serving and coding assistants.
- **Safety & Governance pillar** (`safety/`) - security, and governance and compliance.
- **Careers pillar** (`careers/`) - roles and roadmaps, interview prep, and a certifications guide.
- **Pillar hubs** (`<pillar>/README.md`) - one generated overview page per pillar listing its sections and pages (`write_pillar_hubs()` in [scripts/build_manifest.py](../scripts/build_manifest.py)); never hand-edited.
- **Certifications hub** (`certifications/`) - AI and ML certification study guides per provider (Anthropic, NVIDIA, AWS, Azure, Google Cloud, Databricks, GitHub, Oracle): overview, fact sheet, notes, practice plan, and for most an exam strategy, scenarios, a flashcard deck and a practice question bank (`certifications/practice-questions/`). Hub and provider tables are generated from the hand-kept [certifications/certs.json](../certifications/certs.json) by [scripts/build_certs.py](../scripts/build_certs.py). Some guides have no deck yet (the hub shows "-").
- **Flashcard pages** (`certifications/.../flashcards.md`) - generated into `site-build/` only from each `flashcards.csv`: click a question to reveal the answer, or download the CSV for Anki or Quizlet (`render_flashcard_pages()` in [scripts/build_certs.py](../scripts/build_certs.py)).
- **"Which site?" page** ([learn/start-here/which-site.md](../learn/start-here/which-site.md)) - points readers to the right sibling site; byte-identical across all four Zero to Hero repos.
- **Paper summaries** (`papers/<category>/<slug>/summary.md`) - plain-language summaries of foundational papers and landmark essays in seven categories (architectures, language models, image/video/3D generation, multimodal and audio, robotics, techniques, essays). Count: see [papers.json](../papers.json).
- **Related in This Collection footers** - each summary ends with generated links to the other summaries it mentions ([scripts/add_cross_links.py](../scripts/add_cross_links.py), alias map `ALIASES`).
- **Explainers** (`explainers/<section>/`, hub [EXPLAINERS.md](../EXPLAINERS.md)) - unnumbered, dated pages on history, model families, benchmarks, concepts, compute and economics, policy and governance, ecosystem, and open questions. Each carries an "In one line" pitch and a "Last reviewed" date.
- **Research Library indexes** - [BROWSE.md](../BROWSE.md) (hand-kept card grid with badges), [INDEX.md](../INDEX.md) (generated, by category) and [TAGS.md](../TAGS.md) (generated, by topic tag from the `TOPICS` map).
- **Reading guides** (`docs/`) - [Learning Roadmap](ROADMAP.md), [Reading Guide](READING_GUIDE.md), [Quick Reference](QUICK_REFERENCE.md), [Comparisons](COMPARISONS.md), [Glossary](GLOSSARY.md) and [Coverage & Gaps](GAPS.md) (what is covered and what is queued).
- **Contributing page** ([CONTRIBUTING.md](../CONTRIBUTING.md)) - how to add a paper, house style, build workflow; published as the last nav entry.
- **Machine-readable manifest** ([papers.json](../papers.json), [papers.csv](../papers.csv)) - every paper's number, title, authors, year, category, source URL, path and topic tags, downloadable from the site.

## Reading and navigation

- **One left sidebar everywhere** ([mkdocs.yml](../mkdocs.yml)) - section navigation with no tabs, the page's table of contents folded into it (`toc.integrate`, `toc.follow`), back-to-top, footer prev/next, and URL tracking of the current heading.
- **Generated navigation** - the nav is built by `write_mkdocs()` in [scripts/build_manifest.py](../scripts/build_manifest.py) into the git-ignored `mkdocs.generated.yml`: Home, the six pillars, Certifications, Research Library, Reading Guides, Explainers, Papers, Contributing.
- **Full-text search** - Material search with suggestions, highlighting and shareable result links; press `/` to search. A custom separator splits on hyphens, punctuation and camelCase.
- **Light, dark and system themes** - three-way toggle; near-black plus red accent palette in [.github/site/extra.css](../.github/site/extra.css); Geist and Geist Mono fonts shared with the sibling sites.
- **Zero to Hero family bar** (`announce` block in [.github/site-overrides/main.html](../.github/site-overrides/main.html)) - the same top bar on all four sibling sites linking Cloud, Data, Security and AI (`*.noblerworks.com`) and Nobler Works, with the current site marked.
- **Edit on GitHub** - every page links to its source for editing (`content.action.edit`).
- **Content helpers** - code copy buttons, tooltips, abbreviations, admonitions, tabs, task lists, collapsible details, Mermaid diagrams, and GitHub-compatible heading anchors so in-summary links work on both GitHub and the site.

## Sharing and search engines

- **Per-page titles and descriptions** ([scripts/site_hooks.py](../scripts/site_hooks.py)) - short "<Short name> Paper Summary (<year>)" titles, descriptions from the page's pitch or first prose paragraph, cert pages titled by exam code from `certs.json`.
- **Link previews** - Open Graph and Twitter card tags with one shared social image (`assets/brand/social-preview-1280x640.png`), via [.github/site-overrides/main.html](../.github/site-overrides/main.html).
- **Structured data** - schema.org BreadcrumbList on every page, WebSite on the home page, Article with `isBasedOn` the original paper on summaries; noindex on the authoring templates.
- **robots.txt and sitemap** - robots.txt written at the domain root by `build_site_tree()`, pointing at the MkDocs sitemap.
- **IndexNow ping on deploy** ([scripts/notify_indexnow.py](../scripts/notify_indexnow.py)) - after Pages publishes, sends changed page URLs (or the whole sitemap when site-wide files change, or with `--all`) to IndexNow. A failed ping warns, never fails the deploy. Google Search Console sitemap submission is still Patrick's to do ([TODO.md](../TODO.md)).
- **Analytics** - none. Planned, not built ([TODO.md](../TODO.md)).

## Generators and automation that keep it current

- **Manifest and site builder** (`python3 scripts/build_manifest.py`, [scripts/build_manifest.py](../scripts/build_manifest.py)) - one stdlib-only, idempotent run regenerates summary frontmatter, `papers.json`/`papers.csv`, `INDEX.md`, `TAGS.md`, `EXPLAINERS.md`, pillar hubs, the certifications hub, README's by-year block, `mkdocs.generated.yml` and the staged `site-build/` tree. Warns on explainers and guide pages not reviewed in 180 days.
- **Certifications builder** ([scripts/build_certs.py](../scripts/build_certs.py)) - imported by the manifest builder: certifications hub, provider tables, the Certifications nav section and flashcard pages.
- **Cross-link footers** (`python3 scripts/add_cross_links.py`, [scripts/add_cross_links.py](../scripts/add_cross_links.py)) - regenerates the "Related in This Collection" footer on every summary.
- **Source measurement** (`python3 scripts/measure_sources.py`, [scripts/measure_sources.py](../scripts/measure_sources.py)) - the only networked script, run by hand: fetches each paper's PDF, counts words with `pdftotext`, caches them in [source_lengths.json](../source_lengths.json); the landing page's "words of research read" and "Nx shorter" figures come from it. Papers with no retrievable PDF are excluded.
- **Link checker** (`python3 scripts/check_links.py`, [scripts/check_links.py](../scripts/check_links.py)) - fails on a broken relative Markdown link.
- **Count checker** (`python3 scripts/check_counts.py`, [scripts/check_counts.py](../scripts/check_counts.py)) - fails when a hand-typed count drifts: BROWSE.md tallies, the glossary term count, GAPS.md's coverage map, and `certs.json` against the certifications tree and README badge. Also enforces the three-line header on explainers and guide pages.
- **CI** ([.github/workflows/ci.yml](../.github/workflows/ci.yml)) - link check, count check, and a freshness gate that fails if generated files are stale.
- **Site build and deploy** ([.github/workflows/pages.yml](../.github/workflows/pages.yml)) - strict MkDocs build on every PR and push; deploys to GitHub Pages from `main`, then notifies IndexNow.
- **Local push gate** ([scripts/check-ci-local.mjs](../scripts/check-ci-local.mjs), wired by `.githooks/pre-push`, config `.ci-local.json`) - runs the CI gate at `git push` unless GitHub Actions already has a recent green push run; writes `.local-ci-pass.json`. A trimmed MkDocs variant of the fleet gate.
- **Gate verdict** ([scripts/ci-local-verdict.sh](../scripts/ci-local-verdict.sh)) - answers whether the local gate already passed for exactly this code and the named steps.
- **SEO hook** ([scripts/site_hooks.py](../scripts/site_hooks.py)) - MkDocs hook run at build time; see Sharing and search engines.
- **Authoring templates** ([papers/_TEMPLATE.md](../papers/_TEMPLATE.md), [explainers/_TEMPLATE.md](../explainers/_TEMPLATE.md), [templates/guide.md](../templates/guide.md)) - starting points for a summary, an explainer and a guide page.
