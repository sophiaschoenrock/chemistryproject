(function () {
  "use strict";

  /**
   * @typedef {{ label: string, text: string, rationale: string }} Option
   * @typedef {{ subsection: string, stimulus: string, stem: string, correct: string, options: Option[] }} Question
   */

  const els = {
    error: document.getElementById("quiz-error"),
    app: document.getElementById("quiz-app"),
    scope: document.getElementById("quiz-scope"),
    sectionSelect: document.getElementById("section-select"),
    progress: document.getElementById("quiz-progress"),
    score: document.getElementById("quiz-score"),
    stimulusWrap: document.getElementById("stimulus-wrap"),
    stimulusText: document.getElementById("stimulus-text"),
    stemText: document.getElementById("stem-text"),
    optionsWrap: document.getElementById("options-wrap"),
    btnCheck: document.getElementById("btn-check"),
    btnNext: document.getElementById("btn-next"),
    btnRestart: document.getElementById("btn-restart"),
    feedbackPanel: document.getElementById("feedback-panel"),
    feedbackResult: document.getElementById("feedback-result"),
    correctLabel: document.getElementById("correct-label"),
    rationales: document.getElementById("rationales"),
    completePanel: document.getElementById("complete-panel"),
    completeSummary: document.getElementById("complete-summary"),
    btnAgain: document.getElementById("btn-again"),
  };

  /** @type {Question[]} */
  let allQuestions = [];
  /** @type {Question[]} */
  let session = [];
  let index = 0;
  let correctCount = 0;
  let selected = null;
  let answered = false;

  function shuffle(array) {
    const a = array.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function getParam(name) {
    const params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function filterBySection(qs, section) {
    if (!section || section === "all") return qs.slice();
    return qs.filter((q) => q.subsection.startsWith(section));
  }

  function setScopeLabel(section) {
    if (!els.scope) return;
    if (!section || section === "all") {
      els.scope.textContent = "All Unit 1 topics · order shuffled";
      return;
    }
    const first = session[0];
    els.scope.textContent = first ? first.subsection : "Topic filter";
  }

  function showError(msg) {
    if (els.error) els.error.textContent = msg;
    if (els.error) els.error.classList.remove("hidden");
    if (els.app) els.app.hidden = true;
  }

  function loadQuestions() {
    const url = "questions.json";
    return fetch(url)
      .then((r) => {
        if (!r.ok) throw new Error("Could not load questions.json");
        return r.json();
      })
      .then((data) => {
        allQuestions = data;
      });
  }

  function startSession() {
    const section = els.sectionSelect.value;
    const qs = filterBySection(allQuestions, section);
    if (qs.length === 0) {
      showError("No questions for this filter.");
      return;
    }
    session = section === "all" ? shuffle(qs) : qs.slice();
    index = 0;
    correctCount = 0;
    answered = false;
    selected = null;
    if (els.error) els.error.classList.add("hidden");
    if (els.app) els.app.hidden = false;
    if (els.completePanel) els.completePanel.classList.add("hidden");
    if (els.feedbackPanel) {
      els.feedbackPanel.classList.add("hidden");
      els.feedbackPanel.setAttribute("aria-hidden", "true");
    }
    setScopeLabel(section);
    renderQuestion();
    updateScore();
  }

  function renderQuestion() {
    const q = session[index];
    if (!q) return;
    if (!els.progress || !els.stemText || !els.optionsWrap || !els.btnCheck || !els.btnNext) return;

    els.progress.textContent = `Question ${index + 1} of ${session.length}`;
    if (q.stimulus && q.stimulus.trim()) {
      if (els.stimulusWrap) els.stimulusWrap.classList.remove("hidden");
      if (els.stimulusText) els.stimulusText.textContent = q.stimulus.trim();
    } else {
      if (els.stimulusWrap) els.stimulusWrap.classList.add("hidden");
      if (els.stimulusText) els.stimulusText.textContent = "";
    }
    els.stemText.textContent = q.stem;

    els.optionsWrap.innerHTML = "";
    q.options.forEach((opt) => {
      const id = `opt-${opt.label}` + "-" + index;
      const row = document.createElement("label");
      row.className = "option-row";
      row.setAttribute("for", id);
      const radio = document.createElement("input");
      radio.type = "radio";
      radio.name = "answer";
      radio.value = opt.label;
      radio.id = id;
      radio.disabled = answered;
      const span = document.createElement("span");
      span.className = "option-text";
      span.innerHTML = `<span class="opt-letter">${opt.label}</span> ${escapeHtml(opt.text)}`;
      row.appendChild(radio);
      row.appendChild(span);
      els.optionsWrap.appendChild(row);
    });

    els.btnCheck.disabled = answered;
    els.btnNext.disabled = !answered;
    if (els.feedbackPanel) {
      els.feedbackPanel.classList.add("hidden");
      els.feedbackPanel.setAttribute("aria-hidden", "true");
    }

    if (!answered) {
      els.optionsWrap.querySelectorAll('input[type="radio"]').forEach((r) => {
        r.addEventListener("change", () => {
          selected = r.value;
        });
      });
    }
  }

  function escapeHtml(s) {
    return s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function checkAnswer() {
    const q = session[index];
    if (!q) return;
    if (!selected) {
      els.feedbackResult.textContent = "Select an answer before checking.";
      els.correctLabel.textContent = "";
      els.rationales.innerHTML = "";
      const wrap = document.getElementById("correct-line-wrap");
      if (wrap) wrap.classList.add("hidden");
      els.feedbackPanel.classList.remove("hidden");
      els.feedbackPanel.setAttribute("aria-hidden", "false");
      return;
    }
    answered = true;
    const ok = selected === q.correct;
    if (ok) correctCount += 1;
    updateScore();

    const wrap = document.getElementById("correct-line-wrap");
    if (wrap) wrap.classList.remove("hidden");

    els.feedbackResult.textContent = ok
      ? "Correct."
      : "Incorrect.";
    els.correctLabel.textContent = q.correct;
    els.rationales.innerHTML = "";
    q.options.forEach((opt) => {
      const div = document.createElement("div");
      div.className = "rationale-block";
      const title = document.createElement("p");
      title.className = "rationale-title";
      title.innerHTML = `<span class="opt-letter">${opt.label}</span> ${escapeHtml(opt.text)}`;
      const body = document.createElement("p");
      body.className = "rationale-body";
      body.textContent = opt.rationale;
      div.appendChild(title);
      div.appendChild(body);
      els.rationales.appendChild(div);
    });

    els.feedbackPanel.classList.remove("hidden");
    els.feedbackPanel.setAttribute("aria-hidden", "false");
    els.btnCheck.disabled = true;
    els.btnNext.disabled = false;

    els.optionsWrap.querySelectorAll('input[type="radio"]').forEach((r) => {
      r.disabled = true;
    });
  }

  function nextQuestion() {
    if (index + 1 >= session.length) {
      finish();
      return;
    }
    index += 1;
    answered = false;
    selected = null;
    renderQuestion();
  }

  function finish() {
    const card = els.app && els.app.querySelector(".question-card");
    if (card) card.hidden = true;
    if (els.feedbackPanel) els.feedbackPanel.classList.add("hidden");
    if (els.completePanel) els.completePanel.classList.remove("hidden");
    if (els.completeSummary) {
      els.completeSummary.textContent = `You answered ${correctCount} of ${session.length} correctly in this session.`;
    }
  }

  function resetQuizCard() {
    const card = els.app && els.app.querySelector(".question-card");
    if (card) card.hidden = false;
    if (els.completePanel) els.completePanel.classList.add("hidden");
  }

  function updateScore() {
    if (els.score) els.score.textContent = `${correctCount} correct`;
  }

  function syncSelectFromUrl() {
    const s = getParam("section");
    if (s && [...els.sectionSelect.options].some((o) => o.value === s)) {
      els.sectionSelect.value = s;
    }
  }

  function init() {
    if (
      !els.app ||
      !els.sectionSelect ||
      !els.btnCheck ||
      !els.btnNext ||
      !els.btnRestart ||
      !els.btnAgain
    ) {
      return;
    }

    syncSelectFromUrl();

    loadQuestions()
      .then(() => {
        startSession();
      })
      .catch(() => {
        showError(
          "Could not load questions.json. If you opened this file directly (file://), run a local server (for example: python3 -m http.server) and open http://localhost:8080/quiz.html"
        );
      });

    els.sectionSelect.addEventListener("change", () => {
      const u = new URL(window.location.href);
      if (els.sectionSelect.value === "all") {
        u.searchParams.delete("section");
      } else {
        u.searchParams.set("section", els.sectionSelect.value);
      }
      window.history.replaceState({}, "", u);
      resetQuizCard();
      startSession();
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

  init();
})();
