#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0
MANIFEST="$REPO_ROOT/.codex-plugin/plugin.json"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.name !== "fastmcp-engineering") throw new Error("name mismatch");
if (m.skills !== "./skills/") throw new Error("skills path mismatch");
if (!m.hooks || Object.keys(m.hooks).length !== 0) throw new Error("hooks must be empty to suppress auto-discovery");
console.log("codex manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] codex manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] codex manifest valid"
fi

if [ -f "$REPO_ROOT/skills/using-fastmcp-engineering/references/codex-tools.md" ]; then
  echo "  [PASS] codex-tools reference present"
else
  echo "  [FAIL] codex-tools reference missing"
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All codex tests passed."
  exit 0
else
  echo "$FAILURES codex test(s) failed."
  exit 1
fi