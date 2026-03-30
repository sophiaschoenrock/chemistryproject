package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.1 Moles and Molar Mass — original AP-style practice (not copied from secure exams). */
public final class Questions11 {
  private Questions11() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_1,
            "",
            "How many moles of CO2 are present in 44.0 g of CO2? (Molar mass of CO2 ≈ 44.0 g/mol.)",
            "B",
            List.of(
                o(
                    "A",
                    "0.500 mol",
                    "Incorrect. 0.500 mol would correspond to about half the molar mass in grams (≈22 g of CO2), not 44.0 g."),
                o(
                    "B",
                    "1.00 mol",
                    "Correct. Moles = mass / molar mass = 44.0 g ÷ 44.0 g/mol = 1.00 mol."),
                o(
                    "C",
                    "2.00 mol",
                    "Incorrect. 2.00 mol of CO2 would have a mass about twice the molar mass (≈88 g), not 44.0 g."),
                o(
                    "D",
                    "44.0 mol",
                    "Incorrect. This would mean each mole has a mass of 1 g, which is inconsistent with the molar mass of CO2."))),
        m(
            Subsection.S1_1,
            "",
            "How many atoms are in 0.25 mol of elemental sulfur, S, assuming sulfur is atomic in this sample?",
            "C",
            List.of(
                o(
                    "A",
                    "0.25 atoms",
                    "Incorrect. This confuses moles with atoms; 1 mol contains Avogadro’s number of atoms."),
                o(
                    "B",
                    "6.02 × 10²³ atoms",
                    "Incorrect. That is the number of atoms in 1 mol of S, not 0.25 mol."),
                o(
                    "C",
                    "1.51 × 10²³ atoms",
                    "Correct. Atoms = moles × Avogadro’s constant = 0.25 × 6.02 × 10²³ atoms."),
                o(
                    "D",
                    "2.41 × 10²⁴ atoms",
                    "Incorrect. This is roughly 4× larger than expected for 0.25 mol (a common error if you multiplied by 4 instead of 0.25)."))),
        m(
            Subsection.S1_1,
            "",
            "What is the molar mass of magnesium nitrate, Mg(NO3)2, rounded to the nearest g/mol? (Use Mg = 24.3, N = 14.0, O = 16.0.)",
            "A",
            List.of(
                o(
                    "A",
                    "148 g/mol",
                    "Correct. Mg = 24.3; two NO3 groups: 2 × (14.0 + 3×16.0) = 124.0; total ≈ 148.3 g/mol."),
                o(
                    "B",
                    "86.3 g/mol",
                    "Incorrect. This would ignore one nitrate group or mis-count oxygen atoms."),
                o(
                    "C",
                    "164 g/mol",
                    "Incorrect. This is too high, often from adding an extra NO3 or mis-subscripting the formula."),
                o(
                    "D",
                    "112 g/mol",
                    "Incorrect. This is too low, often from using only one NO3 or missing an oxygen atom."))),
        m(
            Subsection.S1_1,
            "",
            "Which of the following numerical expressions gives the number of moles in 5.0 g of CaO? (Use M_Ca = 40.0 g/mol and M_O = 16.0 g/mol.)",
            "B",
            List.of(
                o(
                    "A",
                    "5.0 × (40.0 + 16.0)",
                    "Incorrect. This multiplies mass by molar mass instead of dividing mass by molar mass."),
                o(
                    "B",
                    "5.0 / (40.0 + 16.0)",
                    "Correct. Moles = mass / molar mass, and M(CaO) = 40.0 + 16.0 g/mol."),
                o(
                    "C",
                    "(40.0 + 16.0) / 5.0",
                    "Incorrect. This inverts the relationship; it is not moles of sample."),
                o(
                    "D",
                    "5.0 / (40.0 × 16.0)",
                    "Incorrect. Molar mass of CaO is the sum of atomic masses, not the product of Ca and O masses."))));
  }
}
