package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.4 Composition of Mixtures */
public final class Questions14 {
  private Questions14() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_4,
            "",
            "A student has a homogeneous mixture of water and ethanol. Which statement is most accurate?",
            "B",
            List.of(
                o(
                    "A",
                    "The mixture has a single fixed composition by mass.",
                    "Incorrect. Mixture composition can vary depending on how it was prepared."),
                o(
                    "B",
                    "The mixture can be separated by physical processes such as distillation.",
                    "Correct. Mixtures are separable by physical means; distillation exploits different boiling points."),
                o(
                    "C",
                    "The mixture must be a compound because it is homogeneous.",
                    "Incorrect. Homogeneity does not imply a compound; solutions can be homogeneous mixtures."),
                o(
                    "D",
                    "The mixture has a single boiling point like a pure substance.",
                    "Incorrect. Many liquid mixtures show a boiling range or depend on composition; not like a single pure substance in general."))),
        m(
            Subsection.S1_4,
            "",
            "A solid mixture of iron filings and sand is separated using a magnet. The separation relies primarily on differences in which property?",
            "A",
            List.of(
                o(
                    "A",
                    "Magnetic behavior (physical property)",
                    "Correct. Magnetic separation exploits differences in magnetic response."),
                o(
                    "B",
                    "Chemical reactivity with oxygen",
                    "Incorrect. The described method does not require combustion or oxidation."),
                o(
                    "C",
                    "Molar mass",
                    "Incorrect. Molar mass is not what separates the solids in magnetism."),
                o(
                    "D",
                    "Solubility in water",
                    "Incorrect. No dissolution step is described; the magnet acts on iron directly."))),
        m(
            Subsection.S1_4,
            "",
            "Which is a characteristic of a heterogeneous mixture?",
            "C",
            List.of(
                o(
                    "A",
                    "It must contain only one phase.",
                    "Incorrect. Heterogeneous mixtures often show distinct regions/phases."),
                o(
                    "B",
                    "It must be a pure element.",
                    "Incorrect. Elements are not mixtures."),
                o(
                    "C",
                    "Its composition can differ from one region to another.",
                    "Correct. Heterogeneity means non-uniform distribution at the macroscopic scale."),
                o(
                    "D",
                    "It has a fixed chemical formula.",
                    "Incorrect. Fixed formulas describe compounds, not mixtures."))));
  }
}
