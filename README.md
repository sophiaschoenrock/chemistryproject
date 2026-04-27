# AP Chemistry · Unit 1-9 Practice

Static website and optional Java CLI for **AP Chemistry Unit 1** (Atomic Structure and Properties, CED topics **1.1–1.8**). Practice is **original** multiple-choice with four options and a **rationale for every choice**—similar in spirit to AP Classroom feedback.

## What’s in this repo

| Part | Description |
|------|-------------|
| **Unit 1 home** (`index.html` + `index.js`) | Unit1 overview and topic cards; `index.js` loads `questions.json` and shows how many questions exist per subsection (any `1.x` / `2.x` prefix on the page’s cards). |
| **Unit 2 home** (`index-unit2.html` + `index.js`) | Same pattern for CED **2.1–2.7**; links use `quiz.html?unit=2&section=2.x`. |
| **Quiz** (`quiz.html` + `quiz.js`) | `?unit=1` or `?unit=2` selects the topic list; filter by subsection or all topics in that unit (shuffled); check answers and read all rationales. |
| **Notes** (`notes.html`, `notes-unit2.html`) | Static notes for Unit 1 and Unit 2 subsections. |
| **Data** (`questions.json`) | Single source of truth for the web quiz (array of items with `subsection`, `stem`, `stimulus`, `correct`, `options`). |
| **Java** (`src/main/java/...`) | Optional command-line practice using the same bank via `src/main/resources/questions.json`. |

Styling is in `styles.css`; the site uses a formal, document-style look (Times New Roman).

## Run the website locally

Browsers block `fetch()` for `questions.json` when you open HTML as `file://`. Use a tiny HTTP server from the project root:

```bash
cd /path/to/chemistryproject
python3 -m http.server 8080
```

Then open **http://localhost:8080/** (homepage), **http://localhost:8080/quiz.html**, and **http://localhost:8080/notes.html**.

## GitHub Pages

If Pages is enabled for this repository, the same files are served over HTTPS—no extra build step. After you push, allow a minute for the site to refresh.

## Java CLI (optional)

Requires **JDK 17** and **Maven**.

```bash
mvn -q compile exec:java
```

The app loads questions from the classpath copy at `src/main/resources/questions.json`. When you change the bank at the repo root, copy or regenerate into `src/main/resources/` so Java and the website stay aligned (see `scripts/expand_question_bank.py` if you use it).

## Question bank

- **Web:** `questions.json` at the repository root (same folder as `index.html`).
- **Java:** `src/main/resources/questions.json` should mirror the web data when you care about parity.

Items are written for practice; they are **not** copied from secure College Board exams.

## License

MIT — see [LICENSE](LICENSE).
