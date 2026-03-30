package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.3 Elemental Composition of Pure Substances */
public final class Questions13 {
  private Questions13() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_3,
            "",
            "A compound contains only carbon and hydrogen. Combustion of a 1.00 g sample produces 3.00 g of CO2 (assume complete combustion and capture of all carbon as CO2). Which expression gives the mass of carbon in the sample?",
            "B",
            List.of(
                o(
                    "A",
                    "3.00 g × (32.0/(12.0+32.0))",
                    "Incorrect. 32.0/(12.0+32.0) is the mass fraction of oxygen in CO2, not carbon."),
                o(
                    "B",
                    "3.00 g × (12.0/(12.0+2×16.0))",
                    "Correct. The mass fraction of carbon in CO2 is 12.0/(44.0 g/mol worth of CO2), so multiply by sample CO2 mass."),
                o(
                    "C",
                    "3.00 g × (2×16.0/44.0)",
                    "Incorrect. That uses the oxygen fraction in CO2, not carbon."),
                o(
                    "D",
                    "1.00 g − 3.00 g",
                    "Incorrect. This subtracts masses incorrectly; the CO2 mass is not the sample mass."))),
        m(
            Subsection.S1_3,
            "",
            "Which is the empirical formula of a compound with a mole ratio C : H : O equal to 1 : 2 : 1?",
            "C",
            List.of(
                o(
                    "A",
                    "C2H4O2",
                    "Incorrect. That ratio is a multiple of 1:2:1 (it would be CH2O scaled by 2)."),
                o(
                    "B",
                    "C6H12O6",
                    "Incorrect. That is also a multiple of CH2O, not the simplest whole-number ratio."),
                o(
                    "C",
                    "CH2O",
                    "Correct. The simplest integer ratio matching 1:2:1 is CH2O."),
                o(
                    "D",
                    "CHO2",
                    "Incorrect. That ratio is 1:1:2, not 1:2:1."))),
        m(
            Subsection.S1_3,
            "",
            "Which statement best describes a pure substance?",
            "D",
            List.of(
                o(
                    "A",
                    "It must be an element.",
                    "Incorrect. Pure substances include compounds as well as elements."),
                o(
                    "B",
                    "It must be a mixture of isotopes only.",
                    "Incorrect. Isotope mixtures can still be elements; pure substances are defined by chemical composition, not isotope mixing alone."),
                o(
                    "C",
                    "It must be a solution.",
                    "Incorrect. A solution is typically a homogeneous mixture, not a pure substance."),
                o(
                    "D",
                    "It has fixed composition and distinct properties for a given compound.",
                    "Correct. A pure substance has a definite composition (element or compound)."))));
  }
}
