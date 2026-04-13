#!/usr/bin/env python3
"""
Replace all Unit 2 questions (subsection starting with '2.') in repo-root questions.json
with the curated bank from unit2_items.py (detailed AP-style rationales).

Copies the merged file to src/main/resources/questions.json for the Java loader.

  python3 scripts/rebuild_unit2_bank.py
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "questions.json"
RES_PATH = ROOT / "src" / "main" / "resources" / "questions.json"

sys.path.insert(0, str(ROOT / "scripts"))
from unit2_items import get_unit2_questions  # noqa: E402


def main() -> None:
    with open(JSON_PATH, encoding="utf-8") as f:
        bank: list = json.load(f)
    u1 = [q for q in bank if not str(q.get("subsection", "")).startswith("2.")]
    u2 = get_unit2_questions()
    out = u1 + u2
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    RES_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(JSON_PATH, RES_PATH)
    print(f"Wrote {len(out)} total questions ({len(u1)} non–Unit 2 + {len(u2)} Unit 2).")


if __name__ == "__main__":
    main()
