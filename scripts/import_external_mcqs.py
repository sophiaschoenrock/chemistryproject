#!/usr/bin/env python3
"""
Convert external MCQ JSON (id, unit, topic, question, choices, correct_answer, explanations)
into this repo's questions.json shape and merge with dedupe on (subsection, stem).

Usage (from repo root):
  python3 scripts/import_external_mcqs.py data/imported_mcqs.json
Also copies merged bank to src/main/resources/questions.json.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_MAIN = ROOT / "questions.json"
OUT_JAVA = ROOT / "src" / "main" / "resources" / "questions.json"

# Full subsection titles (CED-style) so quiz filters ?section=3.2 match subsection.startswith("3.2")
TOPIC_TO_SUBSECTION: dict[str, str] = {
    # Unit 1
    "1.1": "1.1 Moles and Molar Mass",
    "1.2": "1.2 Mass Spectra of Elements",
    "1.3": "1.3 Elemental Composition of Pure Substances",
    "1.4": "1.4 Composition of Mixtures",
    "1.5": "1.5 Atomic Structure and Electron Configuration",
    "1.6": "1.6 Photoelectron Spectroscopy",
    "1.7": "1.7 Periodic Trends",
    "1.8": "1.8 Valence Electrons and Ionic Compounds",
    # Unit 2
    "2.1": "2.1 Types of Chemical Bonds",
    "2.2": "2.2 Intramolecular Force and Potential Energy",
    "2.3": "2.3 Structure of Ionic Solids",
    "2.4": "2.4 Structure of Metals and Alloys",
    "2.5": "2.5 Lewis Diagrams",
    "2.6": "2.6 Resonance and Formal Charge",
    "2.7": "2.7 VSEPR and Hybridization",
    # Unit 3 — Intermolecular Forces and Properties
    "3.1": "3.1 Intermolecular Forces",
    "3.2": "3.2 Properties of Solids",
    "3.3": "3.3 Solids, Liquids, and Gases",
    "3.4": "3.4 Ideal Gas Law",
    "3.5": "3.5 Kinetic Molecular Theory",
    "3.6": "3.6 Deviation from Ideal Gas Law",
    "3.7": "3.7 Solutions and Mixtures",
    "3.8": "3.8 Representations of Solutions",
    # Unit 4 — Chemical Reactions
    "4.1": "4.1 Introduction for Reactions",
    "4.2": "4.2 Net Ionic Equations",
    "4.3": "4.3 Representations of Reactions",
    "4.4": "4.4 Physical and Chemical Changes",
    "4.5": "4.5 Stoichiometry",
    "4.6": "4.6 Introduction to Titration",
    "4.7": "4.7 Types of Chemical Reactions",
    "4.8": "4.8 Acid-Base Reactions",
    "4.9": "4.9 Oxidation-Reduction Reactions",
    # Unit 5 — Kinetics
    "5.1": "5.1 Reaction Rates",
    "5.2": "5.2 Introduction to Rate Law",
    "5.3": "5.3 Concentration Changes Over Time",
    "5.4": "5.4 Elementary Reactions",
    "5.5": "5.5 Collision Model",
    "5.6": "5.6 Reaction Energy Profile",
    "5.7": "5.7 Introduction to Mechanisms",
    "5.8": "5.8 Multistep Reaction Energy Profile",
    "5.9": "5.9 Pre-Equilibrium Approximation",
    "5.10": "5.10 Mode of Energy Transfer",
    "5.11": "5.11 Kinetics of Spectroscopy",
    # Unit 6 — Thermodynamics
    "6.1": "6.1 Endothermic and Exothermic Processes",
    "6.2": "6.2 Heat Capacity and Phase Changes",
    "6.3": "6.3 Energy of Phase Changes",
    "6.4": "6.4 Energy of Formation",
    "6.5": "6.5 Hess's Law",
    "6.6": "6.6 Bond Enthalpies",
    "6.7": "6.7 Spontaneity",
    # Unit 7 — Equilibrium
    "7.1": "7.1 Introduction to Equilibrium",
    "7.2": "7.2 Direction of Reversible Reactions",
    "7.3": "7.3 Reaction Quotient and Equilibrium Constant",
    "7.4": "7.4 Calculating the Equilibrium Constant",
    "7.5": "7.5 Properties of the Equilibrium Constant",
    "7.6": "7.6 Le Châtelier's Principle",
    "7.7": "7.7 Introduction to Solubility Equilibria",
    "7.8": "7.8 pH and Solubility",
    "7.9": "7.9 Free Energy and Equilibrium",
    # Unit 8 — Acids and Bases
    "8.1": "8.1 Introduction to Acids and Bases",
    "8.2": "8.2 pH and pOH of Strong and Weak Acids and Bases",
    "8.3": "8.3 Acid-Base Titrations",
    "8.4": "8.4 Buffers",
    "8.5": "8.5 Acid-Base Titration Curves",
    "8.6": "8.6 Molecular Structure of Acids and Bases",
    "8.7": "8.7 pH and pKa",
    "8.8": "8.8 Properties of Buffers",
    "8.9": "8.9 Buffer Capacity",
    "8.10": "8.10 pH and Solubility",
    # Unit 9 — Applications of Thermodynamics
    "9.1": "9.1 Introduction to Entropy",
    "9.2": "9.2 Gibbs Free Energy and Thermodynamic Favorability",
    "9.3": "9.3 Thermodynamics and Kinetics",
    "9.4": "9.4 Free Energy of Formation",
    "9.5": "9.5 Free Energy Under Nonstandard Conditions",
    "9.6": "9.6 Electrochemistry and Gibbs Free Energy",
    "9.7": "9.7 Cell Potential Under Nonstandard Conditions",
}


def convert_item(raw: dict) -> dict:
    topic = str(raw.get("topic", "")).strip()
    if topic not in TOPIC_TO_SUBSECTION:
        raise ValueError(f"Unknown topic code {topic!r} — add to TOPIC_TO_SUBSECTION in import_external_mcqs.py")
    sub = TOPIC_TO_SUBSECTION[topic]
    stem = str(raw["question"]).strip()
    correct = str(raw["correct_answer"]).strip().upper()
    if correct not in "ABCD":
        raise ValueError(f"Bad correct_answer {correct!r} for id {raw.get('id')}")
    choices = raw["choices"]
    expl = raw["explanations"]
    options = []
    for lab in "ABCD":
        if lab not in choices or lab not in expl:
            raise ValueError(f"Missing choice or explanation {lab} for id {raw.get('id')}")
        options.append(
            {
                "label": lab,
                "text": str(choices[lab]).strip(),
                "rationale": str(expl[lab]).strip(),
            }
        )
    return {
        "subsection": sub,
        "stimulus": "",
        "stem": stem,
        "correct": correct,
        "options": options,
    }


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/import_external_mcqs.py <path-to-import.json>", file=sys.stderr)
        print("   or: python3 scripts/import_external_mcqs.py -  < data/imported_mcqs.json", file=sys.stderr)
        sys.exit(1)
    arg = sys.argv[1]
    if arg == "-":
        incoming = json.load(sys.stdin)
    else:
        path = Path(arg)
        incoming = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(incoming, list):
        raise SystemExit("Import file must be a JSON array")

    converted = [convert_item(x) for x in incoming]
    existing: list = json.loads(OUT_MAIN.read_text(encoding="utf-8"))
    seen = {(q.get("subsection"), q.get("stem")) for q in existing}
    added = 0
    for q in converted:
        k = (q["subsection"], q["stem"])
        if k in seen:
            continue
        seen.add(k)
        existing.append(q)
        added += 1

    OUT_MAIN.write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JAVA.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(OUT_MAIN, OUT_JAVA)
    print(f"Merged {added} new questions ({len(converted)} in import file, {len(existing)} total in bank).")


if __name__ == "__main__":
    main()
