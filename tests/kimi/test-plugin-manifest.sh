#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0
MANIFEST="$REPO_ROOT/.kimi-plugin/plugin.json"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.name !== "fastmcp-engineering") throw new Error("name mismatch");
if (m.skills !== "./skills/") throw new Error("skills path mismatch");
if (!m.sessionStart || m.sessionStart.skill !== "using-fastmcp-engineering") throw new Error("sessionStart.skill mismatch");
if (!m.skillInstructions) throw new Error("skillInstructions missing");
console.log("kimi manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] kimi manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] kimi manifest valid"
fi

if [ -f "$REPO_ROOT/skills/using-fastmcp-engineering/references/kimi-tools.md" ]; then
  echo "  [PASS] kimi-tools reference present"
else
  echo "  [FAIL] kimi-tools reference missing"
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All kimi tests passed."
  exit 0
else
  echo "$FAILURES kimi test(s) failed."
  exit 1
fi