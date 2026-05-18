# AP Chemistry Study System

A full-stack, self-directed study platform for all nine AP Chemistry units.

Live site: https://sophiaschoenrock.github.io/chemistryproject/
Repository: https://github.com/sophiaschoenrock/chemistryproject

---

## Overview

A complete AP Chemistry practice platform built from scratch, with no third-party quiz frameworks and no external component libraries. Students open it in a browser, select a unit, and study through four distinct tools, each targeting a different mode of exam preparation.

---

## Tools

**Reaction Rush**
A timed, score-driven study mode built for retrieval practice under exam-like pressure. Questions are drawn from a filterable unit-specific subset of the JSON question bank and rendered dynamically via DOM manipulation. A countdown timer enforces pacing, a streak counter rewards consecutive correct responses, and a post-session results screen presents per-question explanations. The interface requires no installation and no authentication.

**Unit Quiz Engine**
A structured multiple-choice quiz filtered by unit identifier and subsection tag, parsed client-side from `questions.json` using vanilla JavaScript. Every question carries four answer choices, a correct-key field, and an individual rationale for each distractor, not only the correct response. Progress is tracked within the session and presented as a final score summary.

**Annotated Notes**
Each AP unit has a dedicated notes page authored in semantic HTML, structured to mirror the College Board subsection hierarchy. Content includes conceptual definitions, key equations rendered as formatted inline HTML without external rendering libraries, and worked vocabulary. Notes pages are statically served and linked from their respective unit landing pages.

**Java Command-Line Interface**
A standalone Maven project that implements the same question-bank domain model in Java 17. The object model defines `McqQuestion`, `McqOption`, and `Subsection` as discrete typed classes, demonstrating that the data architecture designed for the JavaScript frontend translates directly into a statically typed, compiled environment. The interactive terminal runner is compiled and executed via `mvn compile` and `mvn exec:java`.

---

## Content Coverage

**Unit 1, Atomic Structure and Properties.**
Moles and molar mass, mass spectrometry, electron configurations, photoelectron spectroscopy, periodic trends in atomic radius, ionization energy, and electronegativity. Subsections 1.1 through 1.8 with over 100 questions and complete annotated notes.

**Unit 2, Molecular and Ionic Compound Structure and Properties.**
Ionic and covalent bonding, Lewis dot structures, formal charge, resonance, VSEPR geometry, molecular polarity, and intermolecular forces. Subsections 2.1 through 2.7 with a complete question bank, per-choice rationales, and annotated notes.

**Unit 3, Intermolecular Forces and Properties.**
London dispersion forces, dipole-dipole interactions, hydrogen bonding, properties of solids and liquids, solutions, solubility, and the photoelectric effect. Notes structure and question entries are in place across subsections 3.1 through 3.10.

**Unit 4, Chemical Reactions.**
Synthesis, decomposition, single and double replacement reactions, oxidation states, net ionic equations, and stoichiometric calculations. Notes structure and question entries are in place across subsections 4.1 through 4.10.

**Unit 5, Kinetics.**
Reaction rate, rate laws, the method of initial rates, integrated rate laws for zeroth, first, and second order reactions, the Arrhenius equation, activation energy, reaction mechanisms, and catalysis. Notes structure and question entries are in place across subsections 5.1 through 5.7.

**Unit 6, Thermodynamics.**
Endothermic and exothermic processes, enthalpy of reaction, calorimetry, Hess's law, bond enthalpies, entropy, Gibbs free energy, and thermodynamic spontaneity. Notes structure and question entries are in place across subsections 6.1 through 6.7.

**Unit 7, Equilibrium.**
Dynamic equilibrium, the equilibrium constant expression K, reaction quotient Q, ICE tables, the relationship between K and Gibbs free energy, and Le Chatelier's principle. Notes structure and question entries are in place across subsections 7.1 through 7.9.

**Unit 8, Acids and Bases.**
Bronsted-Lowry acid-base theory, Ka and Kb, percent dissociation, pH and pOH calculations, buffer solutions, the Henderson-Hasselbalch equation, and acid-base titration curves. Notes structure and question entries are in place across subsections 8.1 through 8.8.

**Unit 9, Electrochemistry.**
Oxidation and reduction half-reactions, galvanic and electrolytic cell construction, standard reduction potentials, cell potential calculations using the Nernst equation, and Faraday's laws of electrolysis. Notes structure and question entries are in place across subsections 9.1 through 9.7.

Total question bank: 282 or more original items, each carrying a unit tag, subsection identifier, four answer choices, the correct key, and a per-choice explanation.

---

## Technology

**Frontend.**
HTML5, CSS3 using Flexbox and Grid layout, vanilla JavaScript (ES6 and later). Zero build tools, served as static files. `questions.json` serves as the flat data model powering all quiz views. Typography via Google Fonts.

**Backend.**
Java 17 with Maven 3. Domain model includes `McqQuestion`, `McqOption`, and `Subsection` as discrete typed classes. Run with `mvn compile` followed by `mvn exec:java`.

**Build Scripts.**
`scripts/expand_question_bank.py` generates and syncs question bank entries. `scripts/import_external_mcqs.py` deduplicates and merges imported MCQ sets. Both are written in Python 3.

**Deployment.**
GitHub Pages, branch main, root directory. Every push to main deploys immediately with no continuous integration configuration required.

---

## Project Structure

```
chemistryproject/
  index.html                homepage, Reaction Rush
  reaction-rush.html        direct link duplicate of Reaction Rush
  quiz.html                 structured unit quiz
  quiz.js                   quiz engine, filtering, scoring, rationale display
  index.js                  landing page, loads question counts from JSON
  questions.json            282 or more questions, Units 1 through 9
  styles.css                shared stylesheet
  notes.html                Unit 1 notes
  notes-unit2.html          Unit 2 notes
  notes-unit3.html through notes-unit9.html
  index-unit2.html          Unit 2 landing page
  landing.html              original project summary page
  scripts/
    expand_question_bank.py
    import_external_mcqs.py
  src/main/java/
    McqQuestion.java
    McqOption.java
    Subsection.java
    QuizRunner.java
  pom.xml
  README.md
```

---

## Running Locally

Website:
```
cd chemistryproject
python3 -m http.server 8080
```
Open http://localhost:8080 in a browser. The site must be served over HTTP rather than opened as a local file, because JavaScript fetches `questions.json` via a network request.

Java CLI:
```
mvn compile
mvn exec:java
```

---

## Design Decisions

**Dependency-light frontend.** No React, no bundler, no Node.js required. Students can access the platform on any device with a browser, including the day of an exam.

**Flat JSON question bank.** A single file drives every quiz view, keeping data and presentation logic cleanly separated and easy to extend independently.

**Per-choice rationales.** AP distractors are engineered to surface specific misconceptions. Explaining why a wrong answer is wrong engages the student more deeply than confirming only the correct response.

**No verbatim AP Classroom text.** All questions are original, written to align with College Board learning objectives without reproducing secure exam content.

---

## Author

Sophia Schoenrock, 2026
https://github.com/sophiaschoenrock/chemistryproject
