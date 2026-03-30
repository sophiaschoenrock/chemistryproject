package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.2 Mass Spectra of Elements */
public final class Questions12 {
  private Questions12() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_2,
            "The mass spectrum of a sample of element X shows peaks at m/z = 64 and m/z = 66 with relative abundances of approximately 50% and 50%.",
            "Based on the spectrum, which statement is most consistent with the data?",
            "C",
            List.of(
                o(
                    "A",
                    "X must be a compound with two molecular ions.",
                    "Incorrect. Mass spectra of elements show atomic (or isotopic) peaks, not molecular ions from a compound in this context."),
                o(
                    "B",
                    "The weighted average atomic mass must be exactly 64.5 amu.",
                    "Incorrect. With isotope masses 64 and 66 and about equal abundance, the average is near 65 amu, not 64.5 amu."),
                o(
                    "C",
                    "The element has at least two isotopes with different mass numbers.",
                    "Correct. Two distinct m/z peaks with substantial abundance indicate two isotopes (different neutron counts)."),
                o(
                    "D",
                    "The peak at m/z = 66 must be the base peak.",
                    "Incorrect. The base peak is the tallest peak; here the abundances are roughly equal, so neither is necessarily the base peak by height alone."))),
        m(
            Subsection.S1_2,
            "",
            "A mass spectrum of chlorine-containing molecules often shows peaks at whole-number m/z values differing by 2 with a characteristic ratio. For a monatomic Cl sample, which pair is expected for the two major isotopes?",
            "B",
            List.of(
                o(
                    "A",
                    "35 and 36",
                    "Incorrect. 36 is not a major isotope of chlorine in natural abundance."),
                o(
                    "B",
                    "35 and 37",
                    "Correct. Natural chlorine is mostly 35Cl and 37Cl; their masses differ by 2 amu."),
                o(
                    "C",
                    "34 and 35",
                    "Incorrect. 34 is not a major isotope of chlorine in natural abundance."),
                o(
                    "D",
                    "37 and 39",
                    "Incorrect. 39 is not a major isotope of chlorine in natural abundance."))),
        m(
            Subsection.S1_2,
            "",
            "A sample of boron has two isotopes with masses 10.0 amu and 11.0 amu. If the relative atomic mass of boron is 10.8 amu, which abundance is closest?",
            "A",
            List.of(
                o(
                    "A",
                    "About 80% 11B and 20% 10B",
                    "Correct. Solving 10x + 11(1−x) = 10.8 gives x = 0.2 for 10B and 0.8 for 11B."),
                o(
                    "B",
                    "50% 10B and 50% 11B",
                    "Incorrect. That would give an average mass of 10.5 amu, not 10.8 amu."),
                o(
                    "C",
                    "90% 10B and 10% 11B",
                    "Incorrect. That would give an average mass near 10.1 amu, far below 10.8 amu."),
                o(
                    "D",
                    "100% 11B",
                    "Incorrect. That would give an average mass of 11.0 amu, not 10.8 amu."))));
  }
}
