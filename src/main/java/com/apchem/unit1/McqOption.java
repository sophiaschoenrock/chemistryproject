package com.apchem.unit1;

/**
 * One answer choice with a College Board–style rationale explaining why the choice
 * is correct or incorrect (original practice items; not copied from secure AP materials).
 */
public record McqOption(String label, String text, String rationale) {
  public McqOption {
    if (label == null || label.isBlank()) {
      throw new IllegalArgumentException("label required");
    }
    if (text == null || text.isBlank()) {
      throw new IllegalArgumentException("text required");
    }
    if (rationale == null || rationale.isBlank()) {
      throw new IllegalArgumentException("rationale required");
    }
  }
}
