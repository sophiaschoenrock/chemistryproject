// =============================================================================
// index.js — Homepage-only script (index.html)
// Loads questions.json to show how many practice items exist per subsection (1.1–1.8).
// Safe to fail: if fetch breaks, the homepage still works without counts.
//
// What it does: fetch("questions.json") → parse array → countBySection() buckets each
// question by leading "1.x" in subsection string → applyCounts() writes "N questions"
// into every .topic-meta under [data-section] cards. No globals; runs once at page load.
// =============================================================================

(function () {
  // IIFE: keeps variables out of the global scope so they cannot clash with other scripts.

  "use strict";
  // Strict mode for safer JS (e.g. no accidental globals).

  function countBySection(questions) {
    // Homepage cards have `data-section="1.6"` etc. We compute counts from the
    // JSON so you don't have to manually update the UI when you add questions.
    /** @type {Record<string, number>} */
    const counts = {}; // Map: "1.1" → number of questions whose subsection starts with that
    for (const q of questions) {
      // Each element of questions.json should have subsection like "1.1 Moles and ..."
      const s = typeof q.subsection === "string" ? q.subsection : "";
      const match = s.match(/^(\d+\.\d+)/); // Capture leading "1.1" from full title string
      if (!match) continue; // Skip malformed rows rather than crashing
      const key = match[1]; // e.g. "1.6"
      counts[key] = (counts[key] || 0) + 1; // Increment bucket (default 0 if first time)
    }
    return counts; // e.g. { "1.1": 4, "1.2": 3, ... }
  }

  function applyCounts(counts) {
    // Each topic card includes a `.topic-meta` element that we fill with
    // "N questions". If fetch fails, we simply leave it blank.
    document.querySelectorAll("[data-section]").forEach((card) => {
      // Every <a class="topic-card" data-section="1.2"> on index.html
      const sec = card.getAttribute("data-section"); // "1.2" etc.
      const n = sec ? counts[sec] : 0; // Lookup count; 0 if subsection had no questions
      const meta = card.querySelector(".topic-meta"); // Span under the title for the count line
      if (!meta) return; // Defensive: old HTML without span
      if (!n) {
        meta.textContent = ""; // No questions or missing key — show nothing
        return;
      }
      meta.textContent = `${n} question${n === 1 ? "" : "s"}`; // English pluralization
    });
  }

  fetch("questions.json")
    // fetch returns Promise; browser resolves relative URL against current page URL.
    .then((r) => (r.ok ? r.json() : Promise.reject(new Error("load failed"))))
    // r.ok is false for 404/5xx; reject so .catch runs.
    .then((data) => {
      // Defensive checks because this is a static site: malformed JSON shouldn't
      // break the homepage.
      const counts = countBySection(Array.isArray(data) ? data : []);
      // If JSON is not an array (wrong file), treat as empty → all counts blank.
      applyCounts(counts);
    })
    .catch(() => {
      // Non-fatal: homepage still works without counts.
      // Typical causes: file:// blocking fetch, 404, network offline, invalid JSON.
    });
})(); // Immediately invoke; no globals exported.
