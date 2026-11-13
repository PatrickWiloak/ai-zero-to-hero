# Drafts

Pages drafted by the nobler-os `content-z2h-ai` loop (`scripts/loops/content-refill.mjs`, pilot since
2026-11-13). This folder is **not part of the site**: `scripts/build_manifest.py` copies only the pillar,
explainer, paper and certification folders into `site-build/`, so nothing here is published, and
`check_links.py` / `check_counts.py` do not read it.

Each draft sits at `drafts/<pillar>/<section>/<slug>.md`, and its relative links are written for where it
will live once published (`<pillar>/<section>/<slug>.md`), so they only resolve after the move. The loop
drafts at most two pages a week and stops while two are waiting here.

## Publish a draft

Read it first. Model names, prices and features should be cited to the vendor page with a date. Then:

```bash
cd ~/coding/ai-zero-to-hero
f=drafts/learn/concepts/example.md            # the draft
git mv "$f" "${f#drafts/}"
python3 scripts/build_manifest.py             # hubs, nav, site-build/
python3 scripts/check_links.py && python3 scripts/check_counts.py
git add -A && git commit -m "content: publish <slug> (loop draft)"
ship ai-zero-to-hero --no-deploy              # the push deploys the site (pages.yml)
```

## Reject a draft

Delete it (`git rm`) and commit. The loop remembers every topic it drafted and will not draft the same
one again.
