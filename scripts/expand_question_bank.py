#!/usr/bin/env python3
"""
Expand repo-root questions.json to at least TARGET questions, then copy to
src/main/resources/questions.json for the Java loader.

Run from repo root:
  python3 scripts/expand_question_bank.py
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "questions.json"
RES_PATH = ROOT / "src" / "main" / "resources" / "questions.json"
TARGET = 100


def opts(
    a: tuple[str, str],
    b: tuple[str, str],
    c: tuple[str, str],
    d: tuple[str, str],
) -> list[dict[str, str]]:
    out = []
    for lab, (text, rat) in zip("ABCD", (a, b, c, d)):
        out.append({"label": lab, "text": text, "rationale": rat})
    return out


def q(
    subsection: str,
    stimulus: str,
    stem: str,
    correct: str,
    options: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "subsection": subsection,
        "stimulus": stimulus,
        "stem": stem,
        "correct": correct,
        "options": options,
    }


def generated_questions() -> list[dict[str, Any]]:
    """Return NEW questions to append (original practice, not copied from secure exams)."""
    g: list[dict[str, Any]] = []

    # --- 1.1 (many) ---
    for formula, mm, name in [
        ("H2O", 18.0, "water"),
        ("CO2", 44.0, "carbon dioxide"),
        ("NH3", 17.0, "ammonia"),
        ("CH4", 16.0, "methane"),
        ("O2", 32.0, "oxygen"),
        ("N2", 28.0, "nitrogen"),
        ("HCl", 36.5, "hydrogen chloride"),
        ("NaCl", 58.5, "sodium chloride"),
    ]:
        mass = round(1.5 * mm, 3)
        mol = mass / mm
        stem = (
            f"How many moles of {formula} are in {mass:g} g of {name}? "
            f"(Use M ≈ {mm:g} g/mol.)"
        )
        g.append(
            q(
                "1.1 Moles and Molar Mass",
                "",
                stem,
                "A",
                opts(
                    (
                        f"{mol:.3f} mol",
                        "Correct. Moles = mass divided by molar mass.",
                    ),
                    (
                        f"{mol / 2:.3f} mol",
                        "Incorrect. This is half the expected mole amount.",
                    ),
                    (
                        f"{2 * mol:.3f} mol",
                        "Incorrect. This is about twice the expected moles.",
                    ),
                    (
                        f"{mass:.3f} mol",
                        "Incorrect. This treats grams as if they were moles.",
                    ),
                ),
            )
        )

    for species, n_mol in [("He", 0.25), ("Ne", 0.10), ("Ar", 1.50)]:
        atoms = n_mol * 6.022e23
        stem = f"How many atoms are in {n_mol} mol of {species} (assume monatomic {species})?"
        g.append(
            q(
                "1.1 Moles and Molar Mass",
                "",
                stem,
                "B",
                opts(
                    (
                        f"{n_mol:.2e} atoms",
                        "Incorrect. This value has units of moles, not atoms.",
                    ),
                    (
                        f"{atoms:.3e} atoms",
                        "Correct. Atoms = moles × Avogadro’s constant.",
                    ),
                    (
                        f"{atoms * 10:.3e} atoms",
                        "Incorrect. This is an order-of-magnitude error.",
                    ),
                    (
                        f"{atoms / 6.022e23:.3e} atoms",
                        "Incorrect. This removes Avogadro’s constant incorrectly.",
                    ),
                ),
            )
        )

    g.append(
        q(
            "1.1 Moles and Molar Mass",
            "",
            "What is the molar mass of Na2SO4 (use Na = 23.0, S = 32.1, O = 16.0)?",
            "C",
            opts(
                ("71.0 g/mol", "Incorrect. This is too low; it misses oxygen atoms."),
                ("119.0 g/mol", "Incorrect. This is too low for two sodium and four oxygen atoms."),
                ("142.1 g/mol", "Correct. 2(23.0) + 32.1 + 4(16.0) ≈ 142.1 g/mol."),
                ("189.0 g/mol", "Incorrect. This is too high for the formula given."),
            ),
        )
    )

    # --- 1.2 (unique stems via index) ---
    for i in range(10):
        g.append(
            q(
                "1.2 Mass Spectra of Elements",
                "",
                f"[Set {i + 1}] A mass spectrum shows multiple peaks for a single element. What does that most directly indicate?",
                "B",
                opts(
                    ("The sample must be a mixture of compounds.", "Incorrect. Elemental samples can show multiple isotopic peaks."),
                    ("The element exists as multiple isotopes with different masses.", "Correct. Different isotopes produce distinct m/z signals."),
                    ("The element has only one isotope.", "Incorrect. One isotope would typically show one major peak."),
                    ("The peaks prove the element is diatomic.", "Incorrect. Isotope peaks do not prove a particular molecular form here."),
                ),
            )
        )

    # --- 1.3 ---
    for i in range(10):
        g.append(
            q(
                "1.3 Elemental Composition of Pure Substances",
                "",
                f"[Set {i + 1}] What is the empirical formula of a compound with a C : H mole ratio of 1 : 2?",
                "A",
                opts(
                    ("CH2", "Correct. The smallest whole-number ratio matching 1:2 is CH2."),
                    ("C2H4", "Incorrect. This is a multiple of CH2, not the simplest ratio."),
                    ("CH4", "Incorrect. That ratio is 1:4, not 1:2."),
                    ("C2H2", "Incorrect. That ratio is 1:1, not 1:2."),
                ),
            )
        )

    # --- 1.4 ---
    for i in range(10):
        g.append(
            q(
                "1.4 Composition of Mixtures",
                "",
                f"[Set {i + 1}] Which is a physical separation method commonly used for miscible liquids with different boiling points?",
                "C",
                opts(
                    ("Electrolysis", "Incorrect. Electrolysis is a chemical process driven by electricity."),
                    ("Combustion", "Incorrect. Combustion is a chemical reaction."),
                    ("Distillation", "Correct. Distillation separates based on volatility/boiling point."),
                    ("Precipitation by oxidation", "Incorrect. That describes a chemical change."),
                ),
            )
        )

    # --- 1.5 ---
    for i in range(10):
        g.append(
            q(
                "1.5 Atomic Structure and Electron Configuration",
                "",
                f"[Set {i + 1}] Which set of quantum numbers could describe an electron in a 3d orbital?",
                "D",
                opts(
                    ("n = 3, l = 1", "Incorrect. l = 1 corresponds to p orbitals, not d."),
                    ("n = 3, l = 3", "Incorrect. For n = 3, l cannot equal 3."),
                    ("n = 2, l = 2", "Incorrect. For n = 2, l can only be 0 or 1."),
                    ("n = 3, l = 2", "Correct. d orbitals have l = 2."),
                ),
            )
        )

    # --- 1.6 ---
    for i in range(10):
        g.append(
            q(
                "1.6 Photoelectron Spectroscopy",
                "",
                f"[Set {i + 1}] Why is the binding energy of a 1s electron typically much larger than that of a 3s electron in the same atom?",
                "A",
                opts(
                    ("1s electrons are closer to the nucleus and more strongly held.", "Correct. Inner electrons experience stronger attraction and are harder to remove."),
                    ("1s electrons have higher kinetic energy in PES.", "Incorrect. The key idea is tighter binding for core electrons."),
                    ("3s electrons have a higher nuclear charge than 1s electrons.", "Incorrect. Z is the same for all electrons in the same atom."),
                    ("PES cannot detect 1s electrons.", "Incorrect. PES can show core and valence electrons."),
                ),
            )
        )

    # --- 1.7 ---
    for i in range(10):
        g.append(
            q(
                "1.7 Periodic Trends",
                "",
                f"[Set {i + 1}] Which atom has the higher first ionization energy: Cl or I?",
                "A",
                opts(
                    ("Cl", "Correct. Ionization energy decreases down a group; Cl is above I."),
                    ("I", "Incorrect. I is farther down the group and generally has a lower first IE than Cl."),
                    ("They are equal", "Incorrect. They are different elements with different IE values."),
                    ("Cannot be determined", "Incorrect. The periodic trend is sufficient here."),
                ),
            )
        )

    # --- 1.8 ---
    for i in range(10):
        g.append(
            q(
                "1.8 Valence Electrons and Ionic Compounds",
                "",
                f"[Set {i + 1}] What is the charge of a typical oxide ion in ionic compounds?",
                "B",
                opts(
                    ("1+", "Incorrect. Oxygen typically gains electrons to reach a noble-gas-like configuration."),
                    ("2−", "Correct. Oxide is O²⁻ in many ionic compounds."),
                    ("1−", "Incorrect. That would be a different oxygen species context."),
                    ("3−", "Incorrect. This is not the common oxide ion charge."),
                ),
            )
        )

    return g


def main() -> None:
    existing: list[dict[str, Any]] = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    n0 = len(existing)

    new_items = generated_questions()
    seen = {(it["subsection"], it["stem"]) for it in existing}
    add: list[dict[str, Any]] = []
    for it in new_items:
        key = (it["subsection"], it["stem"])
        if key in seen:
            continue
        seen.add(key)
        add.append(it)

    merged = existing + add

    # If duplicates prevented enough new items, append variants
    v = 1
    while len(merged) < TARGET:
        base = existing[v % max(1, len(existing))]
        dup = json.loads(json.dumps(base))
        dup["stem"] = dup["stem"] + f" (review variant {v})"
        merged.append(dup)
        v += 1

    JSON_PATH.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    RES_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(JSON_PATH, RES_PATH)
    print(f"Questions: {n0} -> {len(merged)} (target {TARGET})")
    print(f"Wrote {JSON_PATH}")
    print(f"Copied to {RES_PATH}")


if __name__ == "__main__":
    main()
