package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.7 Periodic Trends */
public final class Questions17 {
  private Questions17() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_7,
            "",
            "For the elements Na, Mg, and Al in Period 3, which ordering matches typical first ionization energies?",
            "B",
            List.of(
                o(
                    "A",
                    "Na < Mg < Al",
                    "Incorrect. Although IE generally increases across a period, Al’s first IE is lower than Mg’s because removing a 3p electron is easier than removing a 3s electron in Mg."),
                o(
                    "B",
                    "Na < Al < Mg",
                    "Correct. Na is lowest; Mg is highest among these three; Al falls between Na and Mg."),
                o(
                    "C",
                    "Na > Mg > Al",
                    "Incorrect. Sodium has the lowest first ionization energy in this set."),
                o(
                    "D",
                    "Na = Mg = Al",
                    "Incorrect. These are distinct elements with different effective nuclear charges and valence arrangements."))),
        m(
            Subsection.S1_7,
            "",
            "Which atom has the larger atomic radius: K or Br?",
            "A",
            List.of(
                o(
                    "A",
                    "K",
                    "Correct. Potassium is farther left in Period 4 and has a larger radius than bromine on the right."),
                o(
                    "B",
                    "Br",
                    "Incorrect. Atomic radius decreases across a period due to increasing effective nuclear charge."),
                o(
                    "C",
                    "They are equal",
                    "Incorrect. Different positions in the period yield different radii."),
                o(
                    "D",
                    "Cannot be determined without molar mass",
                    "Incorrect. Periodic position determines the trend here."))),
        m(
            Subsection.S1_7,
            "",
            "Which statement best explains why atomic radius increases down a group (e.g., Li to Cs)?",
            "C",
            List.of(
                o(
                    "A",
                    "Effective nuclear charge increases dramatically down the group.",
                    "Incorrect. Zeff trends are not the primary reason radius increases down a group; additional electron shells dominate."),
                o(
                    "B",
                    "Electronegativity increases down the group.",
                    "Incorrect. Electronegativity generally decreases down a group."),
                o(
                    "C",
                    "Additional occupied principal energy levels increase electron shielding and distance from the nucleus.",
                    "Correct. Each step down adds a shell, increasing atomic size."),
                o(
                    "D",
                    "The number of protons decreases down the group.",
                    "Incorrect. Proton number increases down the group."))),
        m(
            Subsection.S1_7,
            "",
            "Which pair shows the correct trend in electronegativity?",
            "D",
            List.of(
                o(
                    "A",
                    "F < O < N",
                    "Incorrect. Fluorine is the most electronegative element; F should be greatest."),
                o(
                    "B",
                    "Cl > F",
                    "Incorrect. F is more electronegative than Cl."),
                o(
                    "C",
                    "Na > S",
                    "Incorrect. Sodium is a metal with low electronegativity compared with sulfur."),
                o(
                    "D",
                    "O > Se",
                    "Correct. Electronegativity decreases down a group; oxygen is above selenium."))));
  }
}
