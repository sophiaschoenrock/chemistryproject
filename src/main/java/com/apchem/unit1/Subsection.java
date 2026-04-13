package com.apchem.unit1;

/**
 * AP Chemistry CED subsections used in the question bank (Units 1–2 in this repo).
 */
public enum Subsection {
  S1_1("1.1 Moles and Molar Mass"),
  S1_2("1.2 Mass Spectra of Elements"),
  S1_3("1.3 Elemental Composition of Pure Substances"),
  S1_4("1.4 Composition of Mixtures"),
  S1_5("1.5 Atomic Structure and Electron Configuration"),
  S1_6("1.6 Photoelectron Spectroscopy"),
  S1_7("1.7 Periodic Trends"),
  S1_8("1.8 Valence Electrons and Ionic Compounds"),

  S2_1("2.1 Types of Chemical Bonds"),
  S2_2("2.2 Intramolecular Force and Potential Energy"),
  S2_3("2.3 Structure of Ionic Solids"),
  S2_4("2.4 Structure of Metals and Alloys"),
  S2_5("2.5 Lewis Diagrams"),
  S2_6("2.6 Resonance and Formal Charge"),
  S2_7("2.7 VSEPR and Hybridization");

  private final String title;

  Subsection(String title) {
    this.title = title;
  }

  public String getTitle() {
    return title;
  }

  /** Maps JSON {@code subsection} strings (e.g. {@code "1.6 Photoelectron..."}) to this enum. */
  public static Subsection fromCedLabel(String label) {
    if (label == null || label.isBlank()) {
      throw new IllegalArgumentException("subsection label required");
    }
    for (Subsection s : values()) {
      if (label.startsWith(s.title.substring(0, 3))) {
        return s;
      }
    }
    throw new IllegalArgumentException("Unknown subsection label: " + label);
  }

  @Override
  public String toString() {
    return title;
  }
}
