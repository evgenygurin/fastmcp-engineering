#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PLUGIN="$REPO_ROOT/.opencode/plugins/fastmcp-engineering.js"
FAILURES=0

# Scenario: skill present (real repo)
if ! node "$SCRIPT_DIR/test-bootstrap-caching.mjs" "$PLUGIN" present >/tmp/oc-present.json 2>&1; then
  echo "  [FAIL] present scenario"
  cat /tmp/oc-present.json
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] present scenario (bootstrap injects once, cached)"
fi

# Scenario: skill missing (fake repo root) — relocate plugin into a temp layout
# whose ../../skills dir has no using-fastmcp-engineering/SKILL.md, so the
# plugin's __dirname-relative resolution finds nothing (superpowers setup.sh pattern).
TMP_MISSING="$(mktemp -d)"
mkdir -p "$TMP_MISSING/plugins"
cp "$PLUGIN" "$TMP_MISSING/plugins/fastmcp-engineering.js"
if ! node "$SCRIPT_DIR/test-bootstrap-caching.mjs" "$TMP_MISSING/plugins/fastmcp-engineering.js" missing >/tmp/oc-missing.json 2>&1; then
  echo "  [FAIL] missing scenario"
  cat /tmp/oc-missing.json
  FAILURES=$((FAILURES + 1))
else
  echo "  [PASS] missing scenario (no bootstrap, no crash)"
fi
rm -rf "$TMP_MISSING"

# Config hook registers skills dir
if node -e '
const mod = await import("file://" + process.argv[1]);
const plugin = await mod.FastMcpEngineeringPlugin({ client: {}, directory: "." });
const cfg = {};
await plugin.config(cfg);
if (!cfg.skills || !cfg.skills.paths || !cfg.skills.paths.some(p => p.includes("skills"))) {
  console.error("config hook did not register skills path");
  process.exit(1);
}
console.log("config hook registered skills path");
' "$PLUGIN" >/tmp/oc-config.json 2>&1; then
  echo "  [PASS] config hook registers skills path"
else
  echo "  [FAIL] config hook"
  cat /tmp/oc-config.json
  FAILURES=$((FAILURES + 1))
fi

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All opencode plugin tests passed."
  exit 0
else
  echo "$FAILURES opencode plugin test(s) failed."
  exit 1
fi
