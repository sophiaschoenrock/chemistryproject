// =============================================================================
// quiz.js — AP Chemistry MCQ practice (quiz.html)
// Runs in the browser only. No bundler; modern ES (const/let, fetch) is fine for target browsers.
//
// Execution flow (high level):
//   init() → resolve ?unit= (1–9) or infer from ?section= → build unit + topic dropdowns → loadQuestions()
//   fetches questions.json → startSession() filters by unit + subsection → renderQuestion() …
// URL: quiz.html, quiz.html?unit=5&section=5.4, etc. Missing unit: inferred from section prefix or 1.
// Data: subsection strings must start with "n." to match the selected unit.
// =============================================================================

(function () {
  // Wrap all code in an IIFE (Immediately Invoked Function Expression) so no
  // `const`/`let`/`function` names leak into the global `window` object.

  "use strict";
  // Enable strict mode: catches silent errors (e.g. assigning to undeclared vars)
  // and disables some legacy sloppy behaviors.

  // This file intentionally uses plain (framework-free) JavaScript so it can run on
  // GitHub Pages with zero build steps.

  /**
   * JSDoc types for editors (VS Code / Cursor) — not enforced at runtime.
   * Option: one answer choice (A–D) with text and explanation string.
   * Question: one MCQ item as stored in questions.json.
   * @typedef {{ label: string, text: string, rationale: string }} Option
   * @typedef {{ subsection: string, stimulus: string, stem: string, correct: string, options: Array<Option> }} Question
   */

  // Cache references to DOM nodes once at load time (faster than repeated getElementById).
  // If quiz.html is missing an id, the value is `null` — init() checks before use.
  const els = {
    error: document.getElementById("quiz-error"), // Red error banner when JSON fails to load
    app: document.getElementById("quiz-app"), // Main quiz UI wrapper (hidden until data loads)
    scope: document.getElementById("quiz-scope"), // Subtitle: current filter / topic description
    sectionSelect: document.getElementById("section-select"), // Dropdown: rebuilt per unit (n.x)
    unitSelect: document.getElementById("unit-select"), // Dropdown: CED units 1–9
    progress: document.getElementById("quiz-progress"), // "Question i of n" text
    score: document.getElementById("quiz-score"), // Running count of correct answers
    stimulusWrap: document.getElementById("stimulus-wrap"), // Container for optional passage (hidden if empty)
    stimulusText: document.getElementById("stimulus-text"), // Passage / figure description text
    stemText: document.getElementById("stem-text"), // The actual question sentence
    optionsWrap: document.getElementById("options-wrap"), // Parent for four radio + label rows
    btnCheck: document.getElementById("btn-check"), // Submits the selected answer for grading
    btnNext: document.getElementById("btn-next"), // Advances after feedback is shown
    btnRestart: document.getElementById("btn-restart"), // Starts a new session with current filter
    feedbackPanel: document.getElementById("feedback-panel"), // Correct/incorrect + rationales block
    feedbackResult: document.getElementById("feedback-result"), // "Correct." or "Incorrect." line
    correctLabel: document.getElementById("correct-label"), // Letter of the keyed correct answer
    rationales: document.getElementById("rationales"), // Container for four rationale paragraphs
    completePanel: document.getElementById("complete-panel"), // End-of-session summary (hidden until done)
    completeSummary: document.getElementById("complete-summary"), // Score sentence at end
    btnAgain: document.getElementById("btn-again"), // "Practice again" after session complete
  };

  /** @type {Question[]} */
  let allQuestions = []; // Full array parsed from questions.json (never mutated in place for filters)
  /** @type {Question[]} */
  let session = []; // Current quiz run: either shuffled copy of all, or filtered list in file order
  let index = 0; // Zero-based index into `session` for the question currently shown
  let correctCount = 0; // Number of questions answered correctly this session (incremented on check)
  let selected = null; // String "A"|"B"|"C"|"D" from the chosen radio, or null if none chosen
  let answered = false; // True after "Check answer" for current question; locks radios until Next

  /** @type {string} Active CED unit number as string key, e.g. "1" or "2". */
  let currentUnit = "1";

  /** Subsection dropdown labels per unit (must match `subsection` prefixes in questions.json / importer). */
  const UNIT_SECTIONS = {
    "1": {
      scopeAll: "Unit 1 · Atomic Structure and Properties",
      sections: [
        { value: "1.1", label: "1.1 Moles and Molar Mass" },
        { value: "1.2", label: "1.2 Mass Spectra of Elements" },
        { value: "1.3", label: "1.3 Elemental Composition of Pure Substances" },
        { value: "1.4", label: "1.4 Composition of Mixtures" },
        { value: "1.5", label: "1.5 Atomic Structure and Electron Configuration" },
        { value: "1.6", label: "1.6 Photoelectron Spectroscopy" },
        { value: "1.7", label: "1.7 Periodic Trends" },
        { value: "1.8", label: "1.8 Valence Electrons and Ionic Compounds" },
      ],
    },
    "2": {
      scopeAll: "Unit 2 · Compound Structure and Properties",
      sections: [
        { value: "2.1", label: "2.1 Types of Chemical Bonds" },
        { value: "2.2", label: "2.2 Intramolecular Force and Potential Energy" },
        { value: "2.3", label: "2.3 Structure of Ionic Solids" },
        { value: "2.4", label: "2.4 Structure of Metals and Alloys" },
        { value: "2.5", label: "2.5 Lewis Diagrams" },
        { value: "2.6", label: "2.6 Resonance and Formal Charge" },
        { value: "2.7", label: "2.7 VSEPR and Hybridization" },
      ],
    },
    "3": {
      scopeAll: "Unit 3 · Intermolecular Forces and Properties",
      sections: [
        { value: "3.1", label: "3.1 Intermolecular Forces" },
        { value: "3.2", label: "3.2 Properties of Solids" },
        { value: "3.3", label: "3.3 Solids, Liquids, and Gases" },
        { value: "3.4", label: "3.4 Ideal Gas Law" },
        { value: "3.5", label: "3.5 Kinetic Molecular Theory" },
        { value: "3.6", label: "3.6 Deviation from Ideal Gas Law" },
        { value: "3.7", label: "3.7 Solutions and Mixtures" },
        { value: "3.8", label: "3.8 Representations of Solutions" },
      ],
    },
    "4": {
      scopeAll: "Unit 4 · Chemical Reactions",
      sections: [
        { value: "4.1", label: "4.1 Introduction for Reactions" },
        { value: "4.2", label: "4.2 Net Ionic Equations" },
        { value: "4.3", label: "4.3 Representations of Reactions" },
        { value: "4.4", label: "4.4 Physical and Chemical Changes" },
        { value: "4.5", label: "4.5 Stoichiometry" },
        { value: "4.6", label: "4.6 Introduction to Titration" },
        { value: "4.7", label: "4.7 Types of Chemical Reactions" },
        { value: "4.8", label: "4.8 Acid-Base Reactions" },
        { value: "4.9", label: "4.9 Oxidation-Reduction Reactions" },
      ],
    },
    "5": {
      scopeAll: "Unit 5 · Kinetics",
      sections: [
        { value: "5.1", label: "5.1 Reaction Rates" },
        { value: "5.2", label: "5.2 Introduction to Rate Law" },
        { value: "5.3", label: "5.3 Concentration Changes Over Time" },
        { value: "5.4", label: "5.4 Elementary Reactions" },
        { value: "5.5", label: "5.5 Collision Model" },
        { value: "5.6", label: "5.6 Reaction Energy Profile" },
        { value: "5.7", label: "5.7 Introduction to Mechanisms" },
        { value: "5.8", label: "5.8 Multistep Reaction Energy Profile" },
        { value: "5.9", label: "5.9 Pre-Equilibrium Approximation" },
        { value: "5.10", label: "5.10 Mode of Energy Transfer" },
        { value: "5.11", label: "5.11 Kinetics of Spectroscopy" },
      ],
    },
    "6": {
      scopeAll: "Unit 6 · Thermodynamics",
      sections: [
        { value: "6.1", label: "6.1 Endothermic and Exothermic Processes" },
        { value: "6.2", label: "6.2 Heat Capacity and Phase Changes" },
        { value: "6.3", label: "6.3 Energy of Phase Changes" },
        { value: "6.4", label: "6.4 Energy of Formation" },
        { value: "6.5", label: "6.5 Hess's Law" },
        { value: "6.6", label: "6.6 Bond Enthalpies" },
        { value: "6.7", label: "6.7 Spontaneity" },
      ],
    },
    "7": {
      scopeAll: "Unit 7 · Equilibrium",
      sections: [
        { value: "7.1", label: "7.1 Introduction to Equilibrium" },
        { value: "7.2", label: "7.2 Direction of Reversible Reactions" },
        { value: "7.3", label: "7.3 Reaction Quotient and Equilibrium Constant" },
        { value: "7.4", label: "7.4 Calculating the Equilibrium Constant" },
        { value: "7.5", label: "7.5 Properties of the Equilibrium Constant" },
        { value: "7.6", label: "7.6 Le Châtelier's Principle" },
        { value: "7.7", label: "7.7 Introduction to Solubility Equilibria" },
        { value: "7.8", label: "7.8 pH and Solubility" },
        { value: "7.9", label: "7.9 Free Energy and Equilibrium" },
      ],
    },
    "8": {
      scopeAll: "Unit 8 · Acids and Bases",
      sections: [
        { value: "8.1", label: "8.1 Introduction to Acids and Bases" },
        { value: "8.2", label: "8.2 pH and pOH of Strong and Weak Acids and Bases" },
        { value: "8.3", label: "8.3 Acid-Base Titrations" },
        { value: "8.4", label: "8.4 Buffers" },
        { value: "8.5", label: "8.5 Acid-Base Titration Curves" },
        { value: "8.6", label: "8.6 Molecular Structure of Acids and Bases" },
        { value: "8.7", label: "8.7 pH and pKa" },
        { value: "8.8", label: "8.8 Properties of Buffers" },
        { value: "8.9", label: "8.9 Buffer Capacity" },
        { value: "8.10", label: "8.10 pH and Solubility" },
      ],
    },
    "9": {
      scopeAll: "Unit 9 · Applications of Thermodynamics",
      sections: [
        { value: "9.1", label: "9.1 Introduction to Entropy" },
        { value: "9.2", label: "9.2 Gibbs Free Energy and Thermodynamic Favorability" },
        { value: "9.3", label: "9.3 Thermodynamics and Kinetics" },
        { value: "9.4", label: "9.4 Free Energy of Formation" },
        { value: "9.5", label: "9.5 Free Energy Under Nonstandard Conditions" },
        { value: "9.6", label: "9.6 Electrochemistry and Gibbs Free Energy" },
        { value: "9.7", label: "9.7 Cell Potential Under Nonstandard Conditions" },
      ],
    },
  };

  function resolveUnit() {
    const sec = getParam("section");
    let u = getParam("unit");
    if (sec && /^\d+\./.test(sec)) {
      u = sec.split(".")[0];
    } else if (!u) {
      u = "1";
    }
    if (!UNIT_SECTIONS[u]) u = "1";
    currentUnit = u;
    return u;
  }

  function buildUnitSelect() {
    if (!els.unitSelect) return;
    const sel = els.unitSelect;
    sel.innerHTML = "";
    const keys = Object.keys(UNIT_SECTIONS).sort((a, b) => Number(a) - Number(b));
    for (const k of keys) {
      const o = document.createElement("option");
      o.value = k;
      o.textContent = UNIT_SECTIONS[k].scopeAll;
      sel.appendChild(o);
    }
    sel.value = currentUnit;
  }

  function buildSectionSelect(unit) {
    const meta = UNIT_SECTIONS[unit];
    if (!meta || !els.sectionSelect) return;
    const sel = els.sectionSelect;
    sel.innerHTML = "";
    const allOpt = document.createElement("option");
    allOpt.value = "all";
    allOpt.textContent = "All topics (shuffled)";
    sel.appendChild(allOpt);
    for (const row of meta.sections) {
      const o = document.createElement("option");
      o.value = row.value;
      o.textContent = row.label;
      sel.appendChild(o);
    }
  }

  function questionsInUnit(qs, unit) {
    const prefix = String(unit) + ".";
    return qs.filter(
      (q) => typeof q.subsection === "string" && q.subsection.startsWith(prefix)
    );
  }

  function shuffle(array) {
    // Fisher–Yates shuffle to randomize practice order without bias.
    const a = array.slice(); // Copy so we never mutate the caller's array
    for (let i = a.length - 1; i > 0; i--) {
      // i walks from last index down to 1
      const j = Math.floor(Math.random() * (i + 1)); // Random index from 0..i inclusive
      [a[i], a[j]] = [a[j], a[i]]; // Swap elements at i and j using destructuring assignment
    }
    return a; // New order; original `array` argument unchanged
  }

  function getParam(name) {
    const params = new URLSearchParams(window.location.search); // Parse ?section=1.1&foo=bar
    return params.get(name); // Returns string or null if key missing
  }

  function filterBySection(qs, section, unit) {
    const inUnit = questionsInUnit(qs, unit);
    if (!section || section === "all") return inUnit.slice();
    return inUnit.filter(
      (q) => typeof q.subsection === "string" && q.subsection.startsWith(section)
    );
  }

  function setScopeLabel(section) {
    if (!els.scope) return; // No DOM node — nothing to update
    const meta = UNIT_SECTIONS[currentUnit];
    const unitLine = meta ? meta.scopeAll : "AP Chemistry";
    if (!section || section === "all") {
      els.scope.textContent = `All ${unitLine} · order shuffled`;
      return;
    }
    const first = session[0]; // First question in filtered list (subsection string is full title)
    els.scope.textContent = first ? first.subsection : "Topic filter"; // Fallback if empty
  }

  function showError(msg) {
    // If the site is opened via `file://`, browsers block fetch() of questions.json.
    // We fail gracefully and show a message with the fix (run a local server).
    if (els.error) els.error.textContent = msg; // Visible error text for the user
    if (els.error) els.error.classList.remove("hidden"); // Unhide the error panel (CSS .hidden)
    if (els.app) els.app.hidden = true; // Hide main quiz so user doesn't see broken UI
  }

  function loadQuestions() {
    const url = "questions.json"; // Must live next to quiz.html on the server
    return fetch(url) // Returns a Promise<Response>
      .then((r) => {
        if (!r.ok) throw new Error("Could not load questions.json"); // 404 / network error
        return r.json(); // Parse body as JSON → Promise<any>
      })
      .then((data) => {
        // Expected shape: an array of Question objects. We validate lightly at runtime
        // because this is static JS (no build-time typechecking).
        if (!Array.isArray(data)) throw new Error("questions.json must be a JSON array");
        allQuestions = data; // Assign global (within IIFE) question bank
      });
  }

  function startSession() {
    // A "session" is the working set of questions the student will see this run:
    // either all topics shuffled, or a single subsection in listed order.
    const section = els.sectionSelect.value; // Current dropdown value: "all" or e.g. "2.3"
    const qs = filterBySection(allQuestions, section, currentUnit); // Subset within this unit
    if (qs.length === 0) {
      showError("No questions for this filter."); // Should not happen if JSON matches UI
      return;
    }
    session = section === "all" ? shuffle(qs) : qs.slice(); // Shuffled vs stable order from JSON
    index = 0; // Start at first question
    correctCount = 0; // Reset score for new session
    answered = false; // User has not checked an answer yet on Q1
    selected = null; // No radio selected yet
    if (els.error) els.error.classList.add("hidden"); // Clear any previous load error state
    if (els.app) els.app.hidden = false; // Show quiz UI
    if (els.completePanel) els.completePanel.classList.add("hidden"); // Hide end screen if restarting
    if (els.feedbackPanel) {
      els.feedbackPanel.classList.add("hidden"); // Hide previous question's feedback
      els.feedbackPanel.setAttribute("aria-hidden", "true"); // Assistive tech: panel not visible
    }
    setScopeLabel(section); // Update subtitle under the page title
    renderQuestion(); // Paint first question
    updateScore(); // Show "0 correct"
  }

  function renderQuestion() {
    const q = session[index]; // Current question object
    if (!q) return; // Safety: no question at this index
    if (!els.progress || !els.stemText || !els.optionsWrap || !els.btnCheck || !els.btnNext) return; // Missing DOM

    // Render stimulus (if present), stem, then four A–D choices.
    els.progress.textContent = `Question ${index + 1} of ${session.length}`; // 1-based display for humans
    if (q.stimulus && q.stimulus.trim()) {
      if (els.stimulusWrap) els.stimulusWrap.classList.remove("hidden"); // Show stimulus box
      if (els.stimulusText) els.stimulusText.textContent = q.stimulus.trim(); // Passage text
    } else {
      if (els.stimulusWrap) els.stimulusWrap.classList.add("hidden"); // Collapse stimulus area
      if (els.stimulusText) els.stimulusText.textContent = ""; // Clear old text
    }
    els.stemText.textContent = q.stem; // Question stem (plain text, no HTML)

    els.optionsWrap.innerHTML = ""; // Remove previous question's radios (avoids duplicate listeners)
    q.options.forEach((opt) => {
      const id = `opt-${opt.label}` + "-" + index; // Unique id per question index (avoid duplicate ids)
      const row = document.createElement("label"); // Clicking label toggles associated radio
      row.className = "option-row"; // CSS flex row for radio + text
      row.setAttribute("for", id); // Associates label with input#id
      const radio = document.createElement("input");
      radio.type = "radio"; // Mutually exclusive within name="answer"
      radio.name = "answer"; // Same name → only one selected at a time
      radio.value = opt.label; // "A" | "B" | "C" | "D"
      radio.id = id; // Matches label[for]
      radio.disabled = answered; // After check, radios stay disabled until Next clears state
      const span = document.createElement("span");
      span.className = "option-text"; // Styles choice text next to radio
      span.innerHTML = `<span class="opt-letter">${opt.label}</span> ${escapeHtml(opt.text)}`; // Letter bold + escaped text
      row.appendChild(radio);
      row.appendChild(span);
      els.optionsWrap.appendChild(row);
    });

    els.btnCheck.disabled = answered; // Can't re-check until new question (answered false here)
    els.btnNext.disabled = !answered; // Can't advance until after Check sets answered=true
    if (els.feedbackPanel) {
      els.feedbackPanel.classList.add("hidden"); // Hide feedback while viewing new question
      els.feedbackPanel.setAttribute("aria-hidden", "true");
    }

    if (!answered) {
      // Keep state in `selected` rather than reading the DOM later. This makes the
      // check/next logic simpler and avoids querySelector pitfalls.
      els.optionsWrap.querySelectorAll('input[type="radio"]').forEach((r) => {
        r.addEventListener("change", () => {
          selected = r.value; // Store "A" etc. when user picks an option
        });
      });
    }
  }

  function escapeHtml(s) {
    // Prevent HTML injection since option text is inserted via innerHTML to preserve
    // simple formatting like subscripts (if you choose to add them later).
    return s
      .replace(/&/g, "&amp;") // Must be first so we don't double-escape entities
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function checkAnswer() {
    const q = session[index];
    if (!q) return;
    if (
      !els.feedbackPanel ||
      !els.feedbackResult ||
      !els.correctLabel ||
      !els.rationales ||
      !els.optionsWrap
    ) {
      return;
    }
    if (!selected) {
      // User clicked Check without choosing — show prompt only, no grading
      els.feedbackResult.textContent = "Select an answer before checking.";
      els.correctLabel.textContent = "";
      els.rationales.innerHTML = "";
      const wrap = document.getElementById("correct-line-wrap");
      if (wrap) wrap.classList.add("hidden"); // Hide "Correct answer: X" row for this edge case
      els.feedbackPanel.classList.remove("hidden");
      els.feedbackPanel.setAttribute("aria-hidden", "false");
      return;
    }
    answered = true; // Locks UI: radios disabled, Next enabled
    const ok = selected === q.correct; // Compare user letter to JSON correct field
    if (ok) correctCount += 1; // Bump session score
    updateScore(); // Refresh pill text

    const wrap = document.getElementById("correct-line-wrap");
    if (wrap) wrap.classList.remove("hidden"); // Show which letter was keyed

    els.feedbackResult.textContent = ok
      ? "Correct."
      : "Incorrect.";
    els.correctLabel.textContent = q.correct; // Display official correct letter
    els.rationales.innerHTML = ""; // Clear prior rationales
    q.options.forEach((opt) => {
      // Show explanations for every choice (AP-style rationales), not only the correct one.
      const div = document.createElement("div");
      div.className = "rationale-block"; // One block per option
      const title = document.createElement("p");
      title.className = "rationale-title"; // Option letter + text
      title.innerHTML = `<span class="opt-letter">${opt.label}</span> ${escapeHtml(opt.text)}`;
      const body = document.createElement("p");
      body.className = "rationale-body"; // Why right/wrong (plain text, no HTML in JSON)
      body.textContent = opt.rationale;
      div.appendChild(title);
      div.appendChild(body);
      els.rationales.appendChild(div);
    });

    els.feedbackPanel.classList.remove("hidden");
    els.feedbackPanel.setAttribute("aria-hidden", "false");
    els.btnCheck.disabled = true; // Cannot re-submit same question
    els.btnNext.disabled = false; // Allow advance

    els.optionsWrap.querySelectorAll('input[type="radio"]').forEach((r) => {
      r.disabled = true; // Prevent changing answer after reveal
    });
  }

  function nextQuestion() {
    // Students should always see feedback before moving on, so Next is disabled
    // until after "Check answer" is pressed.
    if (index + 1 >= session.length) {
      finish(); // No more questions — show summary
      return;
    }
    index += 1; // Move to next index
    answered = false; // Fresh question: radios active again
    selected = null; // Clear selection state (new change listeners in renderQuestion)
    renderQuestion(); // Paint next item
  }

  function finish() {
    const card = els.app && els.app.querySelector(".question-card"); // The article wrapping stem + options
    if (card) card.hidden = true; // Hide question UI on completion screen
    if (els.feedbackPanel) els.feedbackPanel.classList.add("hidden"); // Hide last feedback too
    if (els.completePanel) els.completePanel.classList.remove("hidden"); // Show "Session complete"
    if (els.completeSummary) {
      els.completeSummary.textContent = `You answered ${correctCount} of ${session.length} correctly in this session.`;
    }
  }

  function resetQuizCard() {
    const card = els.app && els.app.querySelector(".question-card");
    if (card) card.hidden = false; // Show question card again after restart
    if (els.completePanel) els.completePanel.classList.add("hidden"); // Hide completion overlay
  }

  function updateScore() {
    if (els.score) els.score.textContent = `${correctCount} correct`; // Live score pill
  }

  function syncSelectFromUrl() {
    const s = getParam("section"); // e.g. "1.3" or "2.5" from topic cards
    if (s && [...els.sectionSelect.options].some((o) => o.value === s)) {
      els.sectionSelect.value = s;
    }
  }

  function syncUnitInUrl() {
    const u = new URL(window.location.href);
    u.searchParams.set("unit", currentUnit);
    window.history.replaceState({}, "", u);
  }

  function syncUnitSelectValue() {
    if (els.unitSelect) els.unitSelect.value = currentUnit;
  }

  /** Switch unit: reset topic to “all”, update URL, restart session if bank is loaded. */
  function switchQuizUnit(u) {
    if (!UNIT_SECTIONS[u] || u === currentUnit) return;
    currentUnit = u;
    buildSectionSelect(currentUnit);
    if (els.sectionSelect) els.sectionSelect.value = "all";
    const url = new URL(window.location.href);
    url.searchParams.set("unit", currentUnit);
    url.searchParams.delete("section");
    window.history.replaceState({}, "", url);
    syncUnitSelectValue();
    resetQuizCard();
    if (allQuestions.length) startSession();
  }

  function setUnitSwitchDisabled(disabled) {
    if (els.unitSelect) els.unitSelect.disabled = disabled;
  }

  function init() {
    // Guard against running on pages that don't have the quiz UI.
    if (
      !els.app ||
      !els.sectionSelect ||
      !els.unitSelect ||
      !els.btnCheck ||
      !els.btnNext ||
      !els.btnRestart ||
      !els.btnAgain
    ) {
      return; // quiz.js may be absent on other pages — do nothing
    }

    resolveUnit();
    buildUnitSelect();
    buildSectionSelect(currentUnit);
    syncSelectFromUrl(); // Honor ?section= when landing from topic cards
    syncUnitInUrl(); // Keep ?unit= in the address bar for sharing / reload
    syncUnitSelectValue();

    setUnitSwitchDisabled(true);
    els.unitSelect.addEventListener("change", () => {
      switchQuizUnit(els.unitSelect.value);
    });

    loadQuestions() // Async fetch
      .then(() => {
        setUnitSwitchDisabled(false);
        startSession(); // After JSON is in memory, build first session
      })
      .catch(() => {
        setUnitSwitchDisabled(true);
        showError(
          "Could not load questions.json. If you opened this file directly (file://), run a local server (for example: python3 -m http.server) and open http://localhost:8080/quiz.html"
        );
      });

    els.sectionSelect.addEventListener("change", () => {
      const u = new URL(window.location.href); // Clone current URL for history API
      u.searchParams.set("unit", currentUnit);
      if (els.sectionSelect.value === "all") {
        u.searchParams.delete("section"); // Clean URL when viewing all topics
      } else {
        u.searchParams.set("section", els.sectionSelect.value); // Persist filter in address bar
      }
      window.history.replaceState({}, "", u); // Update URL without full page reload
      resetQuizCard(); // Ensure question card visible if coming from finish()
      startSession(); // New session with new filter
    });

    els.btnCheck.addEventListener("click", checkAnswer);
    els.btnNext.addEventListener("click", nextQuestion);
    els.btnRestart.addEventListener("click", () => {
      resetQuizCard();
      startSession();
    });
    els.btnAgain.addEventListener("click", () => {
      resetQuizCard();
      startSession();
    });
  }

  init(); // Run setup when script loads (quiz.html body end, defer)
})(); // End IIFE — semicolon optional before EOF
