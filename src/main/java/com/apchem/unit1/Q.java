package com.apchem.unit1;

import java.util.List;

/** Short helpers for building MCQs. */
final class Q {
  private Q() {}

  static McqOption o(String label, String text, String rationale) {
    return new McqOption(label, text, rationale);
  }

  static McqQuestion m(
      Subsection subsection, String stimulus, String stem, String correctLabel, List<McqOption> options) {
    return new McqQuestion(subsection, stimulus, stem, options, correctLabel);
  }
}
