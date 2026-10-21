#!/usr/bin/env python3
"""
build_certs.py - the certification guides under certifications/.

Called by build_manifest.py (CI runs that, then fails if anything it writes is
stale), so there is no separate step to remember. Reads the hand-maintained
index certifications/certs.json plus the tree itself, and (re)generates:

  - certifications/README.md   the hub: provider, cert, code, level, status, links
  - the provider-certs block in certifications/<provider>/README.md
  - the "Certifications" section of the site nav (nav_lines)
  - a flashcards page per cert with a flashcards.csv deck, written into
    site-build/ only (render_flashcard_pages) - the CSV stays the source

certs.json says what the tree cannot: each cert's exam code, level and status,
and which of the same provider's certs live on the sibling Zero to Hero sites.
Names come from each cert README's `# Title`, note counts from its notes/ folder,
so those cannot drift. check_counts.py fails CI when certs.json and the tree
disagree.

Standard library only, idempotent. Run directly to regenerate just these:
    python3 scripts/build_certs.py
"""

from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CERTS_DIR = ROOT / "certifications"
INDEX = CERTS_DIR / "certs.json"
BANKS_DIR = CERTS_DIR / "practice-questions"

LEVEL_ORDER = ["Foundational", "Associate", "Professional", "Specialty"]
# Standard pages of a cert guide, in reading order, with their nav labels.
STANDARD_PAGES = [
    ("README.md", "Overview"),
    ("fact-sheet.md", "Fact Sheet"),
    ("strategy.md", "Exam Strategy"),
    ("practice-plan.md", "Practice Plan"),
    ("scenarios.md", "Scenarios"),
]
STUDY_TRACK = "Study track"
BLOCK_START = "<!-- BEGIN GENERATED: provider-certs - edit scripts/build_certs.py, not this block -->"
BLOCK_END = "<!-- END GENERATED: provider-certs -->"
BLOCK_RE = re.compile(r"<!-- BEGIN GENERATED: provider-certs[^>]*-->.*?<!-- END GENERATED: provider-certs -->", re.S)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
CERT_PAGE_RE = re.compile(r"\*\*Cert page:\*\*\s*\[[^\]]*\]\(\.\./([^)]+?)/README\.md\)")
SIBLINGS = [
    ("Cloud Zero to Hero", "https://cloud.noblerworks.com/", "cloud architecture, DevOps, networking and the core cloud certs"),
    ("Data Zero to Hero", "https://data.noblerworks.com/", "data engineering, analytics and the data certs"),
    ("Security Zero to Hero", "https://security.noblerworks.com/", "cloud and AI security and the security certs"),
]


def h1(path: Path) -> str:
    text = FRONTMATTER_RE.sub("", path.read_text(encoding="utf-8"), count=1)
    m = H1_RE.search(text)
    return m.group(1).strip() if m else path.stem


def clean_name(title: str) -> str:
    """Drop the " - RETIRED" banner some titles carry; status has its own column."""
    return re.sub(r"\s*-\s*RETIRED\s*$", "", title).strip()


def notes_in_order(cert_dir: Path) -> list[Path]:
    """Notes in the order the cert README lists them, then any it does not mention."""
    notes_dir = cert_dir / "notes"
    if not notes_dir.is_dir():
        return []
    files = sorted(notes_dir.glob("*.md"))
    readme = (cert_dir / "README.md").read_text(encoding="utf-8")
    pos = {}
    for f in files:
        i = readme.find(f"notes/{f.name}")
        pos[f] = i if i >= 0 else len(readme)
    return sorted(files, key=lambda f: (pos[f], f.name))


def load() -> dict:
    """certs.json plus everything derived from the tree, in display order."""
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    banks = {}
    if BANKS_DIR.is_dir():
        for bank in sorted(BANKS_DIR.glob("*.md")):
            m = CERT_PAGE_RE.search(bank.read_text(encoding="utf-8"))
            if m:
                banks[m.group(1)] = bank
    providers = []
    for prov in data["providers"]:
        certs = []
        for c in prov["certs"]:
            d = CERTS_DIR / c["path"]
            cert = dict(c)
            cert["dir"] = d
            cert["name"] = clean_name(h1(d / "README.md"))
            cert["notes"] = notes_in_order(d)
            cert["deck"] = d / "flashcards.csv" if (d / "flashcards.csv").exists() else None
            cert["bank"] = banks.get(c["path"])
            cert["track"] = c["status"] == STUDY_TRACK
            certs.append(cert)
        certs.sort(key=lambda c: (c["track"], LEVEL_ORDER.index(c["level"]) if c["level"] in LEVEL_ORDER else len(LEVEL_ORDER), c["name"].lower()))
        providers.append({**prov, "certs": certs})
    all_certs = [c for p in providers for c in p["certs"]]
    return {
        "providers": providers,
        "certs": all_certs,
        "banks": banks,
        "count": sum(1 for c in all_certs if not c["track"]),
        "tracks": sum(1 for c in all_certs if c["track"]),
    }


def deck_size(deck: Path | None) -> int:
    if not deck:
        return 0
    with deck.open(encoding="utf-8", newline="") as f:
        return max(0, sum(1 for _ in csv.reader(f)) - 1)


def _cell(v) -> str:
    return (v or "-").replace("|", "\\|")


def _plural(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def write_hub(idx: dict) -> None:
    lines = [
        "# AI Certifications",
        "",
        f"Free study guides for **{idx['count']}** AI and machine learning certifications from "
        f"**{len(idx['providers'])}** providers, plus {_plural(idx['tracks'], 'self-directed study track')}. "
        "Each guide has an overview, a fact sheet with the exam logistics, study notes and a practice plan; "
        "most add an exam strategy, scenarios, a flashcard deck and a bank of practice questions. "
        "Generated by `scripts/build_certs.py` from [certs.json](certs.json) - do not edit by hand.",
        "",
        "Not sure which one to take? Start with the [AI certifications guide](../careers/certifications/ai-certifications-guide.md).",
        "",
    ]
    for p in idx["providers"]:
        lines += [f"## {p['name']}", "",
                  f"[All {p['name']} guides]({p['id']}/README.md)", "",
                  "| Cert | Code | Level | Status | Notes | Flashcards | Practice questions |",
                  "|------|------|-------|--------|------:|-----------:|--------------------|"]
        for c in p["certs"]:
            rel = c["path"]
            deck = f"[{deck_size(c['deck'])}]({rel}/flashcards.csv)" if c["deck"] else "-"
            bank = f"[Questions](practice-questions/{c['bank'].name})" if c["bank"] else "-"
            lines.append(f"| [{_cell(c['name'])}]({rel}/README.md) | {_cell(c['code'])} | {_cell(c['level'])} "
                         f"| {c['status']} | {len(c['notes'])} | {deck} | {bank} |")
        lines.append("")
    lines += [
        "**Retired** - the exam is no longer offered. The guide is kept for anyone holding the credential, "
        "and points to its replacement. **Study track** - a self-directed guide spanning several exams or none; "
        "not a certification, and not counted as one.",
        "",
        "Flashcard decks are plain CSV (Question, Answer, Tags): import them into Anki or Quizlet, "
        "or read them on the site.",
        "",
        "## Cloud, data and security certifications",
        "",
        "The non-AI certifications live on the sibling sites:",
        "",
    ]
    lines += [f"- [{name}]({url}) - {pitch}" for name, url, pitch in SIBLINGS]
    lines.append("")
    (CERTS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def provider_block(p: dict) -> str:
    local = p["certs"]
    n = sum(1 for c in local if not c["track"])
    t = len(local) - n
    count = _plural(n, "certification") + (f" and {_plural(t, 'self-directed study track')}" if t else "")
    lines = [BLOCK_START, "",
             f"{count} on this site. Statuses are kept in [certs.json](../certs.json); "
             "every AI certification is listed on the [Certifications](../README.md) hub.", "",
             "| Cert | Code | Level | Status | Notes |",
             "|------|------|-------|--------|------:|"]
    for c in local:
        rel = c["path"][len(p["id"]) + 1:]
        lines.append(f"| [{_cell(c['name'])}]({rel}/README.md) | {_cell(c['code'])} | {_cell(c['level'])} "
                     f"| {c['status']} | {len(c['notes'])} |")
    if p.get("elsewhere"):
        lines += ["", f"Other {p['name']} certifications are covered on the sibling Zero to Hero sites:", "",
                  "| Cert | Code | Level | Status |", "|------|------|-------|--------|"]
        for e in p["elsewhere"]:
            lines.append(f"| [{_cell(e['name'])}]({e['url']}) | {_cell(e['code'])} | {_cell(e['level'])} | {e['status']} |")
    statuses = {c["status"] for c in local} | {e["status"] for e in p.get("elsewhere", [])}
    legend = []
    if "Retired" in statuses:
        legend.append("**Retired** - the exam is no longer offered. The guide is kept for anyone holding the "
                      "credential, and points to its replacement.")
    if STUDY_TRACK in statuses:
        legend.append("**Study track** - a self-directed guide spanning several exams or none. Not a "
                      "certification, and not counted as one.")
    if "Anticipated" in statuses:
        legend.append("**Anticipated** - announced but not yet bookable.")
    for item in legend:
        lines += ["", item]
    lines += ["", BLOCK_END]
    return "\n".join(lines)


def write_provider_readmes(idx: dict) -> None:
    for p in idx["providers"]:
        path = CERTS_DIR / p["id"] / "README.md"
        text = path.read_text(encoding="utf-8")
        block = provider_block(p)
        new = BLOCK_RE.sub(lambda _: block, text, count=1) if BLOCK_RE.search(text) else text.rstrip("\n") + "\n\n" + block + "\n"
        if new != text:
            path.write_text(new, encoding="utf-8")


def _q(label: str) -> str:
    return '"' + label.replace('"', "'") + '"'


def nav_lines(idx: dict, indent: str = "  ") -> list[str]:
    """The site nav's Certifications section, as YAML lines."""
    i1, i2, i3, i4, i5 = (indent + "    " * k for k in range(5))
    out = [f"{i1}- Certifications:", f"{i2}- Overview: certifications/README.md"]
    for p in idx["providers"]:
        out.append(f"{i2}- {_q(p['name'])}:")
        out.append(f"{i3}- Overview: certifications/{p['id']}/README.md")
        for c in p["certs"]:
            base = f"certifications/{c['path']}"
            out.append(f"{i3}- {_q(c['name'])}:")
            for fname, label in STANDARD_PAGES:
                if (c["dir"] / fname).exists():
                    out.append(f"{i4}- {_q(label)}: {base}/{fname}")
            extra = sorted(f for f in c["dir"].glob("*.md") if f.name not in dict(STANDARD_PAGES))
            for f in extra:
                out.append(f"{i4}- {_q(h1(f))}: {base}/{f.name}")
            if c["notes"]:
                out.append(f"{i4}- Notes:")
                for n in c["notes"]:
                    out.append(f"{i5}- {_q(h1(n))}: {base}/notes/{n.name}")
            if c["deck"]:
                out.append(f"{i4}- Flashcards: {base}/flashcards.md")
    if idx["banks"]:
        out.append(f"{i2}- Practice Questions:")
        by_bank = {c["bank"]: c for c in idx["certs"] if c["bank"]}
        for c in idx["certs"]:
            if c["bank"]:
                out.append(f"{i3}- {_q(c['name'])}: certifications/practice-questions/{c['bank'].name}")
        for bank in sorted(set(idx["banks"].values()) - set(by_bank)):
            out.append(f"{i3}- {_q(h1(bank))}: certifications/practice-questions/{bank.name}")
    return out


def render_flashcard_pages(idx: dict, site: Path) -> int:
    """One readable page per deck, written into the staged site only.

    The CSV is the source and stays importable (Anki, Quizlet); this page lets a
    reader use the same cards in the browser: question visible, answer behind a
    click. Grouped by each card's last tag (the topic), in deck order.
    """
    written = 0
    for c in idx["certs"]:
        if not c["deck"]:
            continue
        with c["deck"].open(encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))[1:]
        groups: dict[str, list[tuple[str, str]]] = {}
        for row in rows:
            if len(row) < 2 or not row[0].strip():
                continue
            tags = [t.strip() for t in (row[2] if len(row) > 2 else "").split(",") if t.strip()]
            topic = (tags[-1] if tags else "cards").replace("-", " ")
            groups.setdefault(topic[:1].upper() + topic[1:], []).append((row[0], row[1]))
        total = sum(len(v) for v in groups.values())
        desc = f"{total} free flashcards for {c['name']}: click a question to reveal the answer, or download the deck for Anki or Quizlet."
        lines = [
            "---",
            f"description: {json.dumps(desc, ensure_ascii=False)}",
            "---",
            "",
            f"# {c['name']} Flashcards",
            "",
            f"{total} cards from this guide's fact sheet and notes. Click a question to reveal the answer.",
            "",
            "To study with spaced repetition, download [flashcards.csv](flashcards.csv) and import it into "
            "Anki or Quizlet (comma separated, first row is the header). Back to the [study guide](README.md).",
            "",
        ]
        for topic, cards in groups.items():
            lines += [f"## {topic}", ""]
            for q, a in cards:
                lines.append(f'<details class="flashcard"><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>')
            lines.append("")
        dest = site / "certifications" / c["path"] / "flashcards.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n".join(lines), encoding="utf-8")
        written += 1
    return written


def build() -> dict:
    """Regenerate the hub and provider tables; return the index for nav and site."""
    if not INDEX.exists():
        return {"providers": [], "certs": [], "banks": {}, "count": 0, "tracks": 0}
    idx = load()
    write_hub(idx)
    write_provider_readmes(idx)
    return idx


if __name__ == "__main__":
    idx = build()
    print(f"{idx['count']} certifications + {idx['tracks']} study tracks across "
          f"{len(idx['providers'])} providers; wrote certifications/README.md and provider tables.")
