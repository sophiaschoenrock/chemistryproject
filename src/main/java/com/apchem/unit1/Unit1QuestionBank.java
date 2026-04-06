package com.apchem.unit1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;

/**
 * Question bank backed by {@code src/main/resources/questions.json} (same content as the website’s
 * {@code questions.json}). Items are original practice written to mirror AP Chemistry multiple-choice
 * structure; they are not verbatim reproduced from secure College Board exams.
 */
public final class Unit1QuestionBank {
  private static final List<McqQuestion> ALL = QuestionJsonLoader.load();

  private Unit1QuestionBank() {}

  public static List<McqQuestion> allQuestions() {
    return ALL;
  }

  public static Map<Subsection, List<McqQuestion>> bySubsection() {
    Map<Subsection, List<McqQuestion>> map = new EnumMap<>(Subsection.class);
    for (Subsection s : Subsection.values()) {
      map.put(s, new ArrayList<>());
    }
    for (McqQuestion q : ALL) {
      map.get(q.subsection()).add(q);
    }
    for (Subsection s : Subsection.values()) {
      map.put(s, List.copyOf(map.get(s)));
    }
    return map;
  }

  public static List<McqQuestion> shuffledCopy() {
    List<McqQuestion> copy = new ArrayList<>(ALL);
    Collections.shuffle(copy);
    return copy;
  }
}
