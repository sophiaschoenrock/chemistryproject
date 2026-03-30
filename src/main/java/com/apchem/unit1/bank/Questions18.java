package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.8 Valence Electrons and Ionic Compounds */
public final class Questions18 {
  private Questions18() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_8,
            "",
            "How many valence electrons does a neutral phosphorus atom (P) have in its ground state?",
            "B",
            List.of(
                o(
                    "A",
                    "3",
                    "Incorrect. Phosphorus is in group 15; valence electrons include all s and p electrons in the highest n."),
                o(
                    "B",
                    "5",
                    "Correct. P has the configuration [Ne] 3s²3p³, giving five valence electrons."),
                o(
                    "C",
                    "15",
                    "Incorrect. 15 is the atomic number (total electrons), not valence count."),
                o(
                    "D",
                    "2",
                    "Incorrect. That would ignore the p electrons in the valence shell."))),
        m(
            Subsection.S1_8,
            "",
            "What is the most likely formula for the ionic compound formed between calcium and chlorine?",
            "C",
            List.of(
                o(
                    "A",
                    "CaCl",
                    "Incorrect. Charges Ca²⁺ and Cl⁻ require two chloride ions for charge balance."),
                o(
                    "B",
                    "CaCl₃",
                    "Incorrect. This implies Ca³⁺ or inconsistent charges for a typical ionic compound of Ca and Cl."),
                o(
                    "C",
                    "CaCl₂",
                    "Correct. Ca²⁺ combines with two Cl⁻ ions to give a neutral compound."),
                o(
                    "D",
                    "Ca₂Cl",
                    "Incorrect. This does not reflect the 2+ and 1− charge ratio correctly."))),
        m(
            Subsection.S1_8,
            "",
            "Which Lewis structure best represents the formation of Na⁺ and Cl⁻ from Na and Cl atoms?",
            "A",
            List.of(
                o(
                    "A",
                    "Na donates one valence electron to Cl, producing Na⁺ and Cl⁻.",
                    "Correct. Sodium loses one electron to achieve a noble-gas-like configuration; chloride gains one electron."),
                o(
                    "B",
                    "Na shares two electrons with Cl to form a double bond.",
                    "Incorrect. Ionic bonding involves electron transfer, not covalent sharing in this classic NaCl case."),
                o(
                    "C",
                    "Cl donates an electron to Na, producing Na⁻ and Cl⁺.",
                    "Incorrect. Chlorine has higher electron affinity than sodium; electron transfer goes from Na to Cl."),
                o(
                    "D",
                    "Na and Cl remain neutral atoms in the solid lattice.",
                    "Incorrect. The ionic compound contains ions, not neutral atoms."))),
        m(
            Subsection.S1_8,
            "",
            "How many electrons does a sulfide ion, S²⁻, have in the ground state? (Sulfur has atomic number 16.)",
            "C",
            List.of(
                o(
                    "A",
                    "16",
                    "Incorrect. 16 is the electron count for a neutral sulfur atom."),
                o(
                    "B",
                    "17",
                    "Incorrect. Gaining one electron would give 17; sulfide has gained two electrons."),
                o(
                    "C",
                    "18",
                    "Correct. A neutral sulfur atom has 16 electrons; adding two electrons gives 18 electrons in S²⁻."),
                o(
                    "D",
                    "32",
                    "Incorrect. This confuses mass number with electron count."))));
  }
}
