#!/usr/bin/env python3
"""
build_flashcards.py - fill certifications/<provider>/<cert>/flashcards.csv for certs with no deck.

Ported from cloud-zero-to-hero's build-flashcards.py. Cards are extracted, never invented:

  1. Exam logistics from the cert's fact-sheet.md (duration, questions, passing score,
     cost, delivery, validity). Three fact-sheet shapes are read: a "| Key | Value |"
     table row, "**Key:** value" and "- **Key:** value".
  2. Term-definition pairs from notes/*.md, in the house shape
         - **Term** - definition
     Fenced code blocks are skipped. Headings alone never make a card.

Rules: at least MIN_CARDS cards or no deck; at most MAX_CARDS (a truncation row says so).
Output is CSV with the header Question,Answer,Tags.

Ownership: most decks here were written by hand and are NOT regenerated. Only certs listed in
certifications/flashcards-generated.txt are owned by this script. Write mode creates a deck
for any cert with none (and adds it to that list), and refreshes owned decks. A hand deck is
never touched. To hand over a deck, delete its line from the list.

    python3 scripts/build_flashcards.py            # write missing + owned decks
    python3 scripts/build_flashcards.py --report   # counts only, no writes
    python3 scripts/build_flashcards.py --check    # CI-style: fail if owned decks are stale
                                                   # or a cert with no deck could now have one

build_manifest.py runs this in write mode (via generate()) before build_certs, so CI's
freshness gate covers owned decks. Standard library only, idempotent.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CERTS_DIR = ROOT / "certifications"
INDEX = CERTS_DIR / "certs.json"
OWNED = CERTS_DIR / "flashcards-generated.txt"
OUTPUT_NAME = "flashcards.csv"
MIN_CARDS = 15
MAX_CARDS = 300

DEFINITION = re.compile(r"^\s*[-*]\s+\*\*([^*]{2,60})\*\*\s*[-–—:]\s+(.{15,400})$", re.M)
FENCE = re.compile(r"^\s*(```|~~~)")
TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")
BOLD_LINE = re.compile(r"^\s*(?:[-*]\s+)?\*\*([^*]+?):?\*\*:?\s*(.+)$")
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)
FM = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)

# fact-sheet key (lowercase) -> (field, question template)
KEYS = {
    "duration": "duration", "number of questions": "questions", "questions": "questions",
    "passing score": "passing_score", "cost": "cost", "delivery": "delivery",
    "validity": "validity", "valid for": "validity",
}
SPECS = [
    ("duration", "How long is the {n} exam?"),
    ("questions", "How many questions are on the {n} exam?"),
    ("passing_score", "What is the passing score for {n}?"),
    ("cost", "What does the {n} exam cost?"),
    ("delivery", "How is the {n} exam delivered?"),
    ("validity", "How long is {n} valid for?"),
]


def clean(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split()).strip(" -:|")


def strip_fenced(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def cert_name(d: Path) -> str:
    m = H1.search(FM.sub("", (d / "README.md").read_text(encoding="utf-8"), count=1))
    return re.sub(r"\s*-\s*RETIRED\s*$", "", m.group(1).strip()) if m else d.name


def logistics_cards(d: Path, name: str) -> list[tuple[str, str, str]]:
    sheet = d / "fact-sheet.md"
    if not sheet.exists():
        return []
    found: dict[str, str] = {}
    for line in sheet.read_text(encoding="utf-8").splitlines():
        m = TABLE_ROW.match(line) or BOLD_LINE.match(line)
        if not m:
            continue
        field = KEYS.get(clean(m.group(1)).lower().rstrip(":"))
        value = clean(m.group(2))
        if field and field not in found and value and not set(value) <= set("-: "):
            found[field] = value
    return [(q.format(n=name), found[f], "exam-logistics") for f, q in SPECS if f in found]


def definition_cards(d: Path) -> list[tuple[str, str, str]]:
    notes = d / "notes"
    if not notes.is_dir():
        return []
    cards = []
    for f in sorted(notes.glob("*.md")):
        text = strip_fenced(f.read_text(encoding="utf-8"))
        topic = re.sub(r"^\d+[-.]?\s*", "", f.stem).replace("-", " ")
        for term, definition in DEFINITION.findall(text):
            term, definition = clean(term), clean(definition)
            if not term or len(definition) < 15 or term.lower() == definition.lower():
                continue
            cards.append((f"{term} ({topic})", definition, f"notes,{topic.replace(' ', '-')}"))
    return cards


def build_deck(d: Path) -> list[tuple[str, str, str]]:
    cards, seen = [], set()
    for q, a, t in logistics_cards(d, cert_name(d)) + definition_cards(d):
        if q.lower() in seen:
            continue
        seen.add(q.lower())
        cards.append((q, a, t))
    return cards


def render(cards, truncated: int) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    w.writerow(["Question", "Answer", "Tags"])
    w.writerows(cards)
    if truncated:
        w.writerow([f"NOTE: deck truncated at {MAX_CARDS} cards",
                    f"{truncated} further term-definition pairs exist in this cert's notes. "
                    f"Raise MAX_CARDS in scripts/build_flashcards.py to include them.", "meta"])
    return buf.getvalue()


def owned_paths() -> set[str]:
    if not OWNED.exists():
        return set()
    return {l.strip() for l in OWNED.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")}


def write_owned(paths: set[str]) -> None:
    head = ("# Decks written by scripts/build_flashcards.py (refreshed on every run, checked by --check).\n"
            "# A deck not listed here is hand-written and is never touched. One cert path per line.\n")
    OWNED.write_text(head + "".join(p + "\n" for p in sorted(paths)), encoding="utf-8")


def main(argv: list[str] | None = None, quiet: bool = False) -> int:
    argv = sys.argv[1:] if argv is None else argv
    report, check = "--report" in argv, "--check" in argv
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    owned = owned_paths()
    problems, created, refreshed, short, hand = [], [], [], [], 0
    for prov in data["providers"]:
        for c in prov["certs"]:
            rel = c["path"]
            d = CERTS_DIR / rel
            deck = d / OUTPUT_NAME
            mine = rel in owned
            if deck.exists() and not mine:
                hand += 1
                continue
            cards = build_deck(d)
            if len(cards) < MIN_CARDS:
                short.append((len(cards), rel))
                if mine:
                    problems.append(f"{rel}: owned deck now yields only {len(cards)} cards")
                continue
            out = render(cards[:MAX_CARDS], max(0, len(cards) - MAX_CARDS))
            old = deck.read_text(encoding="utf-8") if deck.exists() else None
            if old == out:
                continue
            if check:
                problems.append(f"{rel}: " + ("owned deck is stale" if mine else f"no deck, but {len(cards)} cards could be generated"))
            elif not report:
                deck.write_text(out, encoding="utf-8")
                owned.add(rel)
                (refreshed if mine else created).append((rel, min(len(cards), MAX_CARDS)))
            else:
                (refreshed if mine else created).append((rel, min(len(cards), MAX_CARDS)))
    if check:
        if problems:
            print("Flashcard decks need attention:")
            for p in problems:
                print("  " + p)
            print("Run: python3 scripts/build_flashcards.py")
            return 1
        print(f"Flashcard decks are up to date ({hand} hand decks untouched, {len(owned)} generated).")
        return 0
    if not report:
        write_owned(owned)
    if quiet:
        return 0
    verb = "would write" if report else "wrote"
    print(f"{hand} hand-written decks left alone; {verb} {len(created)} new, {len(refreshed)} refreshed.")
    for rel, n in created + refreshed:
        print(f"  {n:3d} cards  {rel}")
    print(f"{len(short)} certs without a deck (under {MIN_CARDS} cards):")
    for n, rel in sorted(short, reverse=True):
        print(f"  {n:3d}  {rel}")
    return 0


def generate() -> None:
    """Write missing and owned decks; used by build_manifest.py."""
    main([], quiet=True)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)
