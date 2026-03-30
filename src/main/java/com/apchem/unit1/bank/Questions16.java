package com.apchem.unit1.bank;

import static com.apchem.unit1.Q.m;
import static com.apchem.unit1.Q.o;

import com.apchem.unit1.McqOption;
import com.apchem.unit1.McqQuestion;
import com.apchem.unit1.Subsection;
import java.util.List;

/** 1.6 Photoelectron Spectroscopy */
public final class Questions16 {
  private Questions16() {}

  public static List<McqQuestion> all() {
    return List.of(
        m(
            Subsection.S1_6,
            "The photoelectron spectrum of a neutral atom shows the lowest binding-energy peak corresponding to valence electrons and higher binding-energy peaks for core electrons.",
            "Compared with core electrons, valence electrons typically appear at which position in the PES plot?",
            "A",
            List.of(
                o(
                    "A",
                    "Lower binding energy (closer to zero)",
                    "Correct. Valence electrons are less tightly held, so they require less energy to remove."),
                o(
                    "B",
                    "Higher binding energy",
                    "Incorrect. Higher binding energy corresponds to more tightly held electrons, usually core electrons."),
                o(
                    "C",
                    "The same binding energy as core electrons",
                    "Incorrect. Core and valence electrons differ greatly in binding energy."),
                o(
                    "D",
                    "Binding energy cannot be read from PES",
                    "Incorrect. PES directly reports electron binding energies."))),
        m(
            Subsection.S1_6,
            "",
            "For a neutral atom in its ground state, which subshell typically has the greatest electron binding energy among the following?",
            "A",
            List.of(
                o(
                    "A",
                    "1s",
                    "Correct. Core 1s electrons are closest to the nucleus and are the hardest to remove, giving the highest binding energy."),
                o(
                    "B",
                    "2s",
                    "Incorrect. 2s is less tightly bound than 1s for the same element."),
                o(
                    "C",
                    "2p",
                    "Incorrect. 2p is generally less tightly bound than inner-shell 1s electrons."),
                o(
                    "D",
                    "3s",
                    "Incorrect. Valence 3s electrons are removed more easily than core 1s electrons."))),
        m(
            Subsection.S1_6,
            "",
            "In many introductory PES plots, the relative size (integrated intensity) of a peak associated with a subshell is related most directly to which quantity?",
            "B",
            List.of(
                o(
                    "A",
                    "The speed of the ejected photoelectrons only",
                    "Incorrect. Speed relates to kinetic energy, not the number of electrons contributing to the signal."),
                o(
                    "B",
                    "The number of electrons occupying that subshell (under the same experimental conditions)",
                    "Correct. More electrons in a subshell generally produce a larger signal for that subshell."),
                o(
                    "C",
                    "The nuclear mass of the atom",
                    "Incorrect. Nuclear mass does not directly scale PES peak area in this way."),
                o(
                    "D",
                    "The number of neutrons in the nucleus",
                    "Incorrect. Neutron count does not determine peak area for electron spectroscopy in this context."))),
        m(
            Subsection.S1_6,
            "The photoelectron spectrum of boron shows peaks associated with binding energies for electron removal from the 1s, 2s, and 2p subshells.",
            "Which of the following best explains how the spectrum is consistent with the electron shell model of the atom?",
            "B",
            List.of(
                o(
                    "A",
                    "The peaks show that only valence electrons are ejected, so inner-shell peaks should not appear.",
                    "Incorrect. PES can show peaks for core and valence subshells; inner-shell electrons appear at higher binding energies."),
                o(
                    "B",
                    "Distinct peaks at different binding energies reflect electrons organized in different shells and subshells, as described by the shell model.",
                    "Correct. Each subshell peak corresponds to a group of electrons with similar binding energy in that subshell."),
                o(
                    "C",
                    "All ejected photoelectrons must have the same kinetic energy, so multiple peaks contradict the experiment.",
                    "Incorrect. Different binding energies produce different kinetic energies for ejected electrons."),
                o(
                    "D",
                    "Equal peak areas for 1s, 2s, and 2p prove that each subshell holds the same number of electrons.",
                    "Incorrect. Peak areas relate to electron counts but are not generally equal across these subshells for boron."))));
  }
}
