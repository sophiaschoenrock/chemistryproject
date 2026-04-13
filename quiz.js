// =============================================================================
// quiz.js — AP Chemistry MCQ practice (quiz.html)
// Runs in the browser only. No bundler; modern ES (const/let, fetch) is fine for target browsers.
//
// Execution flow (high level):
//   init() → resolve ?unit= (1 or 2) → build topic dropdown → sync ?section= → loadQuestions()
//   fetches questions.json → startSession() filters by unit + subsection → renderQuestion() …
// URL: quiz.html, quiz.html?unit=2&section=2.3, etc. Missing unit defaults to 1.
// Data: subsection strings must start with "1." or "2." (etc.) to match the selected unit.
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
    sectionSelect: document.getElementById("section-select"), // Dropdown: rebuilt per unit (1.x or 2.x)
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

  /** Subsection dropdown labels per unit (must match `subsection` prefixes in questions.json). */
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
  };

  function resolveUnit() {
    let u = getParam("unit");
    if (!u) {
      const sec = getParam("section");
      if (sec && sec.startsWith("2.")) u = "2";
      else u = "1";
    }
    if (!UNIT_SECTIONS[u]) u = "1";
    currentUnit = u;
    return u;
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

  /** Highlight Unit 1 / Unit 2 toggle to match `currentUnit`. */
  function updateUnitSwitcher() {
    document.querySelectorAll("[data-quiz-unit]").forEach((btn) => {
      const u = btn.getAttribute("data-quiz-unit");
      const on = u === currentUnit;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
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
    updateUnitSwitcher();
    resetQuizCard();
    if (allQuestions.length) startSession();
  }

  function setUnitSwitchDisabled(disabled) {
    document.querySelectorAll("[data-quiz-unit]").forEach((btn) => {
      btn.disabled = disabled;
    });
  }

  function init() {
    // Guard against running on pages that don't have the quiz UI.
    if (
      !els.app ||
      !els.sectionSelect ||
      !els.btnCheck ||
      !els.btnNext ||
      !els.btnRestart ||
      !els.btnAgain
    ) {
      return; // quiz.js may be absent on other pages — do nothing
    }

    resolveUnit();
    buildSectionSelect(currentUnit);
    syncSelectFromUrl(); // Honor ?section= when landing from topic cards
    syncUnitInUrl(); // Keep ?unit= in the address bar for sharing / reload
    updateUnitSwitcher();

    setUnitSwitchDisabled(true);
    document.querySelectorAll("[data-quiz-unit]").forEach((btn) => {
      btn.addEventListener("click", () => {
        switchQuizUnit(btn.getAttribute("data-quiz-unit"));
      });
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
