package com.apchem.unit1;

import com.apchem.unit1.bank.Questions11;
import com.apchem.unit1.bank.Questions12;
import com.apchem.unit1.bank.Questions13;
import com.apchem.unit1.bank.Questions14;
import com.apchem.unit1.bank.Questions15;
import com.apchem.unit1.bank.Questions16;
import com.apchem.unit1.bank.Questions17;
import com.apchem.unit1.bank.Questions18;
import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;

/**
 * All Unit 1 items are original practice written to mirror AP Chemistry multiple-choice
 * structure (four-option stems, data-based prompts where appropriate). They are not
 * verbatim reproduced items from secure College Board exams.
 */
public final class Unit1QuestionBank {
  private Unit1QuestionBank() {}

  public static List<McqQuestion> allQuestions() {
    List<McqQuestion> list = new ArrayList<>();
    list.addAll(Questions11.all());
    list.addAll(Questions12.all());
    list.addAll(Questions13.all());
    list.addAll(Questions14.all());
    list.addAll(Questions15.all());
    list.addAll(Questions16.all());
    list.addAll(Questions17.all());
    list.addAll(Questions18.all());
    return List.copyOf(list);
  }

  public static Map<Subsection, List<McqQuestion>> bySubsection() {
    Map<Subsection, List<McqQuestion>> map = new EnumMap<>(Subsection.class);
    for (Subsection s : Subsection.values()) {
      map.put(s, new ArrayList<>());
    }
    for (McqQuestion q : allQuestions()) {
      map.get(q.subsection()).add(q);
    }
    for (Subsection s : Subsection.values()) {
      map.put(s, List.copyOf(map.get(s)));
    }
    return map;
  }

  public static List<McqQuestion> shuffledCopy() {
    List<McqQuestion> copy = new ArrayList<>(allQuestions());
    Collections.shuffle(copy);
    return copy;
  }
}
