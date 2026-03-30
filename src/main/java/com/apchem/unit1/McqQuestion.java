package com.apchem.unit1;

import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Four-option multiple choice in the style used on AP Chemistry (stimulus optional).
 */
public final class McqQuestion {
  private final Subsection subsection;
  private final String stimulus;
  private final String stem;
  private final List<McqOption> options;
  private final String correctLabel;

  public McqQuestion(
      Subsection subsection,
      String stimulus,
      String stem,
      List<McqOption> options,
      String correctLabel) {
    if (subsection == null) {
      throw new IllegalArgumentException("subsection required");
    }
    if (stem == null || stem.isBlank()) {
      throw new IllegalArgumentException("stem required");
    }
    if (options == null || options.size() != 4) {
      throw new IllegalArgumentException("exactly four options required");
    }
    if (correctLabel == null || correctLabel.isBlank()) {
      throw new IllegalArgumentException("correctLabel required");
    }
    String normalized = correctLabel.trim().toUpperCase(Locale.ROOT);
    Map<String, McqOption> byLabel =
        options.stream()
            .collect(Collectors.toMap(o -> o.label().toUpperCase(Locale.ROOT), o -> o));
    if (!byLabel.containsKey(normalized)) {
      throw new IllegalArgumentException("correctLabel must match an option label");
    }
    this.subsection = subsection;
    this.stimulus = stimulus == null ? "" : stimulus;
    this.stem = stem.trim();
    this.options = List.copyOf(options);
    this.correctLabel = normalized;
  }

  public Subsection subsection() {
    return subsection;
  }

  public String stimulus() {
    return stimulus;
  }

  public String stem() {
    return stem;
  }

  public List<McqOption> options() {
    return options;
  }

  public String correctLabel() {
    return correctLabel;
  }

  public boolean isCorrect(String answer) {
    if (answer == null) {
      return false;
    }
    return correctLabel.equals(answer.trim().toUpperCase(Locale.ROOT));
  }
}
