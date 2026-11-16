# Queue

Content work the **queue loop** builds for this site (nobler-os `scripts/loops/queue-loop.mjs`, loop `queue-z2h-ai`, docs/LOOPS.md "queue"). Items are written by the **content-gaps loop** (`content-gaps-z2h-ai`, since 2026-11-13) from the gap docs, TODO.md content lines, Search Console and the vendors' cert pages, already `approved` (Patrick, 2026-11-13: "auto-build, I land"). Patrick may add, edit or delete items by hand too. The loop reads this file at `origin/main` only.

**A push to this repo publishes the site**, so nothing here lands on its own: each built item waits on a local branch for Patrick.

## Format

Each item is a `## Q-NNN: title` section with these fields, then `### Spec` and `### Done when`:

- `status`: `proposed` | `approved` (the loop may build it) | `in-progress` | `done` | `failed`. The loop builds `approved` items, oldest `added` first. It writes `done` + a `result` line on its branch; `failed` (with the reason) lives in its state file (`~/.cache/loops/queue/state-ai-zero-to-hero.json`). To retry, change the spec or run `node ~/coding/nobler-os/scripts/loops/queue-loop.mjs --repo ai-zero-to-hero --retry Q-NNN`.
- `added`: YYYY-MM-DD. `source`: where the item came from (gap doc, TODO line, search data, vendor page). `after` (optional): items that must be landed first.
- `allow`: the backticked paths the change may touch (`*` within a folder, `**` any depth), including generated files its generators rewrite. Anything else changed fails the item. Never QUEUE.md or gate configuration.
- `### Done when`: one backticked command per line, run by the loop in the worktree; every one must exit 0. Allowed commands start with `python3 scripts/check_links.py`, `python3 scripts/check_counts.py`, `python3 scripts/build_flashcards.py --check`, `python3 scripts/check_freshness.py`, `grep`, `test -f`, `test ! -f` - no `;`, `&`, `|`, `<`, `>`, `$`, backticks or backslashes. The repo's full local gate (`scripts/check-ci-local.mjs`) always runs after them, and an independent reviewer must approve the diff.

The builder may read vendor docs sites (WebFetch, vendor domains only) to check exam codes and facts.

## Landing a built item

The loop commits to a local `loop/queue-<id>` branch and never pushes; the branch expires after 14 days. Read it, then land it:

```bash
git -C ~/coding/ai-zero-to-hero log -p main..loop/queue-q-001
git -C ~/coding/ai-zero-to-hero merge --ff-only loop/queue-q-001
ship ai-zero-to-hero --no-deploy        # the push deploys the site
```

## Q-001: PMLE flashcards for Model Garden, Model Armor and Model Monitoring

- status: approved
- added: 2026-11-16
- source: TODO.md line "Add PMLE flashcards for monitoring, Model Garden and Model Armor"
- allow: `certifications/gcp/machine-learning-engineer/flashcards.csv`

### Spec

Append cards to the hand-written deck `certifications/gcp/machine-learning-engineer/flashcards.csv` (header `Question,Answer,Tags`; keep the existing 26 cards untouched; the deck is not in `certifications/flashcards-generated.txt`, so do not touch that list). Today the deck has no card on Model Garden, Model Armor or Model Monitoring, although the notes cover all three. Add 12 to 16 cards, each answer taken from the notes, tagged `notes,ml-foundation-models-and-tuning` or `notes,ml-monitoring-ai-solutions` like the existing rows:

- Model Garden (`notes/ml-foundation-models-and-tuning.md`, "Model Garden" section): the three content groups (foundation, fine-tunable, task-specific); the three open-model serving routes (MaaS serverless API, self-deployment on your own endpoint/VPC, prebuilt containers such as vLLM, Hex-LLM, TGI) and when to pick each; the order of selection constraints.
- Model Armor (`notes/ml-monitoring-ai-solutions.md`, "Model Armor" part): what it screens for (prompt injection, jailbreaks, sensitive data, malicious URLs, responsible-AI categories); templates, with separate ones for prompts and responses; the `SanitizeUserPrompt` and `SanitizeModelResponse` methods; inspect only versus inspect and block as the rollout path; why regex and built-in Gemini safety filters are the wrong answer to prompt injection.
- Model Monitoring (same file, "6.2 Monitoring predictive models"): skew versus drift versus concept drift versus attribution drift and which need labels; v1 (GA, per endpoint, default alert threshold 0.3) versus v2 (Preview, per model version); L-infinity for categorical and Jensen-Shannon for numerical features.

Use the notes' wording and facts only; do not add facts the notes lack. Quote fields containing commas. Run `python3 scripts/build_flashcards.py --check` and the link checker.

### Done when

- `grep -qF 'Model Armor' certifications/gcp/machine-learning-engineer/flashcards.csv`
- `grep -qF 'SanitizeUserPrompt' certifications/gcp/machine-learning-engineer/flashcards.csv`
- `grep -qF 'Model Garden' certifications/gcp/machine-learning-engineer/flashcards.csv`
- `grep -qF 'Jensen-Shannon' certifications/gcp/machine-learning-engineer/flashcards.csv`
- `python3 scripts/build_flashcards.py --check`
- `python3 scripts/check_links.py`
