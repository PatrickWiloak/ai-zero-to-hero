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
