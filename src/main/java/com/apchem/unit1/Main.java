package com.apchem.unit1;

import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;

/** AP Chemistry Unit 1 — Atomic Structure and Properties (MCQ practice, Java). */
public final class Main {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    try (Scanner scanner = new Scanner(System.in)) {
      System.out.println("AP Chemistry — Unit 1: Atomic Structure and Properties");
      System.out.println("Original four-option MCQs with per-choice explanations.");
      System.out.println();
      while (true) {
        printMenu();
        String choice = readMenuChoice(scanner);
        if (choice == null || "0".equals(choice)) {
          System.out.println("Goodbye.");
          return;
        }
        switch (choice) {
          case "1" -> QuizRunner.run(scanner, Unit1QuestionBank.shuffledCopy());
          case "2" -> runBySubsection(scanner);
          default -> System.out.println("Unknown choice.");
        }
        System.out.println();
      }
    }
  }

  private static void printMenu() {
    System.out.println("--------------------------------------------------");
    System.out.println("1) Practice all Unit 1 questions (shuffled)");
    System.out.println("2) Practice one subsection (1.1–1.8)");
    System.out.println("0) Quit");
    System.out.print("Choose: ");
  }

  private static String readMenuChoice(Scanner scanner) {
    if (!scanner.hasNextLine()) {
      return null;
    }
    return scanner.nextLine().trim();
  }

  private static void runBySubsection(Scanner scanner) {
    Subsection[] values = Subsection.values();
    for (int i = 0; i < values.length; i++) {
      System.out.printf(Locale.US, "%d) %s%n", i + 1, values[i].getTitle());
    }
    System.out.print("Pick subsection number (1–8), or 0 to cancel: ");
    if (!scanner.hasNextLine()) {
      return;
    }
    String line = scanner.nextLine().trim();
    int pick;
    try {
      pick = Integer.parseInt(line);
    } catch (NumberFormatException e) {
      System.out.println("Invalid number.");
      return;
    }
    if (pick == 0) {
      return;
    }
    if (pick < 1 || pick > values.length) {
      System.out.println("Out of range.");
      return;
    }
    Subsection sub = values[pick - 1];
    Map<Subsection, List<McqQuestion>> map = Unit1QuestionBank.bySubsection();
    List<McqQuestion> list = map.get(sub);
    System.out.println();
    System.out.println("Starting: " + sub.getTitle() + " (" + list.size() + " questions)");
    QuizRunner.run(scanner, list);
  }
}
