package com.apchem.unit1;

import java.util.List;
import java.util.Locale;
import java.util.Scanner;

/** Interactive AP-style MCQ runner with full per-choice explanations after each item. */
public final class QuizRunner {
  private QuizRunner() {}

  public static void run(Scanner scanner, List<McqQuestion> questions) {
    int correct = 0;
    for (int i = 0; i < questions.size(); i++) {
      McqQuestion q = questions.get(i);
      printQuestion(i + 1, questions.size(), q);
      String answer = readAnswer(scanner);
      if (answer == null) {
        System.out.println("Ending session.");
        return;
      }
      boolean ok = q.isCorrect(answer);
      if (ok) {
        correct++;
      }
      System.out.println();
      System.out.println(ok ? "Result: Correct." : "Result: Incorrect.");
      System.out.println("Correct answer: " + q.correctLabel());
      System.out.println();
      System.out.println("Explanations for each answer choice:");
      for (McqOption opt : q.options()) {
        System.out.println(" (" + opt.label() + ") " + opt.text());
        System.out.println("     " + opt.rationale());
        System.out.println();
      }
      printSeparator();
    }
    System.out.printf(Locale.US, "Score: %d / %d%n", correct, questions.size());
  }

  private static void printQuestion(int index, int total, McqQuestion q) {
    printSeparator();
    System.out.printf(Locale.US, "Question %d of %d — %s%n", index, total, q.subsection());
    if (!q.stimulus().isBlank()) {
      System.out.println();
      System.out.println("Information:");
      System.out.println(wrapIndent(q.stimulus(), 2));
    }
    System.out.println();
    System.out.println(wrapIndent(q.stem(), 0));
    System.out.println();
    for (McqOption opt : q.options()) {
      System.out.println("(" + opt.label() + ") " + opt.text());
    }
    System.out.println();
    System.out.print("Enter your answer (A, B, C, or D), or Q to quit: ");
  }

  private static String readAnswer(Scanner scanner) {
    while (true) {
      if (!scanner.hasNextLine()) {
        return null;
      }
      String line = scanner.nextLine().trim();
      if (line.isEmpty()) {
        System.out.print("Try again (A–D or Q): ");
        continue;
      }
      String u = line.toUpperCase(Locale.ROOT);
      if ("Q".equals(u) || "QUIT".equals(u)) {
        return null;
      }
      if (u.length() == 1 && "ABCD".indexOf(u.charAt(0)) >= 0) {
        return u;
      }
      System.out.print("Enter A, B, C, D, or Q: ");
    }
  }

  private static void printSeparator() {
    System.out.println("--------------------------------------------------");
  }

  private static String wrapIndent(String text, int indent) {
    String pad = " ".repeat(indent);
    int max = 88 - indent;
    String[] words = text.split("\\s+");
    StringBuilder line = new StringBuilder();
    StringBuilder out = new StringBuilder();
    for (String w : words) {
      if (line.length() == 0) {
        line.append(pad).append(w);
      } else if (line.length() + 1 + w.length() > max) {
        out.append(line).append(System.lineSeparator());
        line = new StringBuilder().append(pad).append(w);
      } else {
        line.append(" ").append(w);
      }
    }
    if (line.length() > 0) {
      out.append(line);
    }
    return out.toString();
  }
}
