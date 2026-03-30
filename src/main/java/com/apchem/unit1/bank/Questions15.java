package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.5 Atomic Structure and Electron Configuration */
public final class Questions15 {
  private Questions15() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_5,
            "",
            "Which electron configuration corresponds to a neutral sulfur atom in the ground state (Z = 16)?",
            "C",
            List.of(
                o(
                    "A",
                    "1s²2s²2p⁶3s⁶",
                    "Incorrect. The 3s subshell holds at most 2 electrons."),
                o(
                    "B",
                    "1s²2s²2p⁶3s²3p²",
                    "Incorrect. This configuration has 14 electrons, not 16."),
                o(
                    "C",
                    "1s²2s²2p⁶3s²3p⁴",
                    "Correct. Sulfur has 16 electrons; filling through 3p⁴ matches the periodic position."),
                o(
                    "D",
                    "1s²2s²2p⁶3s²3d⁴",
                    "Incorrect. For Z = 16, the 3p subshell fills before 3d for the ground state."))),
        m(
            Subsection.S1_5,
            "",
            "Which set of quantum numbers (n, l, ml, ms) is allowed for an electron in a many-electron atom?",
            "B",
            List.of(
                o(
                    "A",
                    "n = 2, l = 2, ml = 0, ms = +½",
                    "Incorrect. For n = 2, l can be 0 or 1 only (l must be less than n)."),
                o(
                    "B",
                    "n = 3, l = 2, ml = −1, ms = −½",
                    "Correct. l = 2 is allowed for n ≥ 3, ml ranges from −l to +l, and ms is ±½."),
                o(
                    "C",
                    "n = 4, l = 0, ml = 1, ms = +½",
                    "Incorrect. If l = 0, ml must be 0."),
                o(
                    "D",
                    "n = 2, l = 1, ml = −2, ms = +½",
                    "Incorrect. For l = 1, ml can only be −1, 0, or +1."))),
        m(
            Subsection.S1_5,
            "",
            "Which orbital diagram rule explains why one fills 2p orbitals singly before pairing (for degenerate p orbitals)?",
            "A",
            List.of(
                o(
                    "A",
                    "Hund’s rule",
                    "Correct. Electrons occupy degenerate orbitals singly with parallel spins before pairing."),
                o(
                    "B",
                    "The Pauli exclusion principle",
                    "Incorrect. Pauli forbids two electrons with the same four quantum numbers in one orbital; it does not specify the order of filling separate degenerate orbitals."),
                o(
                    "C",
                    "The Aufbau principle",
                    "Incorrect. Aufbau describes subshell energy order (e.g., 4s before 3d), not pairing within a subshell."),
                o(
                    "D",
                    "Heisenberg uncertainty principle",
                    "Incorrect. This relates position and momentum uncertainty, not orbital filling patterns."))),
        m(
            Subsection.S1_5,
            "",
            "How many unpaired electrons are in the ground-state configuration of a neutral chromium atom (Z = 24)?",
            "D",
            List.of(
                o(
                    "A",
                    "0",
                    "Incorrect. Chromium’s anomalous configuration leads to unpaired electrons."),
                o(
                    "B",
                    "1",
                    "Incorrect. There is more than one unpaired electron in the ground state."),
                o(
                    "C",
                    "4",
                    "Incorrect. This count does not match the common ground-state configuration for Cr."),
                o(
                    "D",
                    "6",
                    "Correct. Cr is commonly written as [Ar] 4s¹ 3d⁵, giving 6 unpaired electrons (one in 4s and five in 3d)."))));
  }
}
