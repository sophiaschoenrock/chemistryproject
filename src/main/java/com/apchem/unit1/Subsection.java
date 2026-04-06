package com.apchem.unit1;

/**
 * AP Chemistry Unit 1 — Atomic Structure and Properties (CED alignment).
 */
public enum Subsection {
  S1_1("1.1 Moles and Molar Mass"),
  S1_2("1.2 Mass Spectra of Elements"),
  S1_3("1.3 Elemental Composition of Pure Substances"),
  S1_4("1.4 Composition of Mixtures"),
  S1_5("1.5 Atomic Structure and Electron Configuration"),
  S1_6("1.6 Photoelectron Spectroscopy"),
  S1_7("1.7 Periodic Trends"),
  S1_8("1.8 Valence Electrons and Ionic Compounds");

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
