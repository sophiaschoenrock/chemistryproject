# AP Chemistry · Unit 1 Practice

Static website and optional Java CLI for **AP Chemistry Unit 1** (Atomic Structure and Properties, CED topics **1.1–1.8**). Practice is **original** multiple-choice with four options and a **rationale for every choice**—similar in spirit to AP Classroom feedback.

## What’s in this repo

| Part | Description |
|------|-------------|
| **Home** (`index.html` + `index.js`) | Unit overview and topic cards; `index.js` loads `questions.json` and shows how many questions exist per subsection. |
| **Quiz** (`quiz.html` + `quiz.js`) | Filter by topic or all topics (shuffled); check answers and read all rationales. |
| **Notes** (`notes.html`) | Study notes aligned to the same subsections. |
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
