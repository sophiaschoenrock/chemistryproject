#!/bin/sh
# Serve the project root over HTTP so quiz.html can fetch questions.json.
# Usage (from anywhere):
#   sh scripts/serve.sh
#   sh scripts/serve.sh 3000
# Then open: http://localhost:8080/quiz.html  (default port 8080)

PORT="${1:-8080}"
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
cd "$ROOT" || exit 1
echo "Serving $ROOT at http://localhost:$PORT/"
echo "Quiz: http://localhost:$PORT/quiz.html"
exec python3 -m http.server "$PORT"
