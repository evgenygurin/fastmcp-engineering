#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
HOOK="$REPO_ROOT/hooks/session-start"
FAILURES=0
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEST_ROOT"' EXIT

pass() { echo "  [PASS] $1"; }
fail() { echo "  [FAIL] $1"; FAILURES=$((FAILURES + 1)); }

assert_shape() {
    local name="$1" expected_shape="$2" home="$3"
    shift 3
    local output
    output="$(env -i PATH="${PATH:-}" HOME="$home" "$@" 2>&1)"
    local json
    json="$(printf '%s' "$output" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(JSON.stringify(j));})')"
    local shape
    shape="$(printf '%s' "$json" | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s);console.log(Object.keys(j).join(","));})')"
    if [ "$shape" != "$expected_shape" ]; then
        fail "$name: expected shape '$expected_shape', got '$shape'"
        return
    fi
    if ! printf '%s' "$json" | grep -q 'EXTREMELY_IMPORTANT'; then
        fail "$name: bootstrap marker missing"
        return
    fi
    if ! printf '%s' "$json" | grep -q 'fastmcp-engineering'; then
        fail "$name: fastmcp-engineering text missing"
        return
    fi
    pass "$name"
}

HOME_C="$TEST_ROOT/home-cursor"; mkdir -p "$HOME_C"
HOME_CC="$TEST_ROOT/home-cc"; mkdir -p "$HOME_CC"
HOME_CP="$TEST_ROOT/home-copilot"; mkdir -p "$HOME_CP"
HOME_N="$TEST_ROOT/home-none"; mkdir -p "$HOME_N"

assert_shape "cursor" "additional_context" "$HOME_C" env CURSOR_PLUGIN_ROOT=/x "$HOOK"
assert_shape "claude" "hookSpecificOutput" "$HOME_CC" env CLAUDE_PLUGIN_ROOT=/x "$HOOK"
assert_shape "copilot" "additionalContext" "$HOME_CP" env CLAUDE_PLUGIN_ROOT=/x COPILOT_CLI=1 "$HOOK"
assert_shape "none" "additionalContext" "$HOME_N" "$HOOK"

# No double injection: claude output must not contain additional_context top-level
OUT_CC="$(env -i PATH="${PATH:-}" HOME="$HOME_CC" CLAUDE_PLUGIN_ROOT=/x "$HOOK" 2>&1)"
if printf '%s' "$OUT_CC" | grep -q '"additional_context"'; then
    fail "claude: must not emit additional_context (double injection risk)"
else
    pass "claude: no additional_context field"
fi

echo
if [ "$FAILURES" -eq 0 ]; then
    echo "All hook tests passed."
    exit 0
else
    echo "$FAILURES hook test(s) failed."
    exit 1
fi
