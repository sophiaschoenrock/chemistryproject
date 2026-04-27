# AP Chemistry · Units 1–9 Practice (Reaction Rush)

Static website for **AP Chemistry Units 1–9** built around a single multiple-choice question bank. The main experience is **Reaction Rush**: a timed, game-style MCQ mode with streaks, scoring, and **explanations for every choice (A–D)**.

## What’s in this repo

| Part | Description |
|------|-------------|
| **Reaction Rush (homepage)** (`index.html`) | Timed “game” mode that loads `questions.json`, filters by Unit 1–9, and reveals explanations for all choices after each answer. |
| **Reaction Rush (direct)** (`reaction-rush.html`) | Same game page as the homepage (kept as a direct link too). |
| **Landing page (optional)** (`landing.html`) | The earlier GitHub Pages one‑pager (kept as a separate page). |
| **Quiz (classic mode)** (`quiz.html` + `quiz.js`) | Practice mode with unit/topic dropdowns (Units 1–9), full rationales, and non-timed navigation. |
| **Unit 1 curriculum landing (optional)** (`unit1-landing.html`) | Original Unit 1 topic grid and links into quizzes. |
| **Unit 2 curriculum landing (optional)** (`index-unit2.html`) | Original Unit 2 topic grid and links into quizzes. |
| **Notes (optional)** (`notes.html`, `notes-unit2.html`) | Notes pages for Unit 1 and Unit 2. |
| **Data** (`questions.json`) | Single source of truth (array of items with `subsection`, `stem`, `stimulus`, `correct`, `options`). |
| **Import script** (`scripts/import_external_mcqs.py`) | Converts an external MCQ JSON array into this repo’s `questions.json` format and merges with dedupe. |

Most pages use `styles.css` (formal, document-style look). Reaction Rush is self-contained in the page.

## Run the website locally

Browsers block `fetch()` for `questions.json` when you open HTML as `file://`. Use a tiny HTTP server from the project root:

```bash
cd /path/to/chemistryproject
python3 -m http.server 8080
```

Then open:

- **Reaction Rush (homepage):** `http://localhost:8080/`
- **Reaction Rush (direct):** `http://localhost:8080/reaction-rush.html`
- **Classic quiz:** `http://localhost:8080/quiz.html`

## GitHub Pages

If Pages is enabled for this repository, the same files are served over HTTPS—no extra build step. After you push, allow a minute for the site to refresh.

- **Homepage:** Reaction Rush loads at `.../chemistryproject/`
- **Direct link:** `.../chemistryproject/reaction-rush.html`

## Question bank

- **Web:** `questions.json` at the repository root (same folder as `index.html`).

Items are written for practice; they are **not** copied from secure College Board exams.

## Importing more questions

If you have questions in the external format (`unit`, `topic`, `question`, `choices`, `correct_answer`, `explanations`), you can merge them into the bank:

```bash
python3 scripts/import_external_mcqs.py data/imported_mcqs.json
```

## License

MIT — see [LICENSE](LICENSE).
