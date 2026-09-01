#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FAILURES=0

MANIFEST="$REPO_ROOT/gemini-extension.json"
CTX="$REPO_ROOT/FME.md"

if ! node -e '
const fs = require("fs");
const m = JSON.parse(fs.readFileSync(process.argv[1], "utf8"));
if (m.contextFileName !== "FME.md") throw new Error("contextFileName mismatch");
if (!m.name || !m.version) throw new Error("missing name/version");
console.log("manifest OK");
' "$MANIFEST" >/dev/null 2>&1; then
  echo "  [FAIL] manifest invalid"
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] manifest valid"
fi

for line in \
  "./skills/using-fastmcp-engineering/SKILL.md" \
  "./skills/using-fastmcp-engineering/references/gemini-tools.md"; do
  if grep -qF "@${line}" "$CTX"; then
    target="$REPO_ROOT/${line#./}"
    if [ -f "$target" ]; then
      echo "  [PASS] @-include resolves: $line"
    else
      echo "  [FAIL] @-include target missing: $line"
      FAILURES=$((FAILURES + 1))
    fi
  else
    echo "  [FAIL] @-include not found in FME.md: $line"
    FAILURES=$((FAILURES + 1))
  fi
done

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All gemini extension tests passed."
  exit 0
else
  echo "$FAILURES gemini extension test(s) failed."
  exit 1
fi
