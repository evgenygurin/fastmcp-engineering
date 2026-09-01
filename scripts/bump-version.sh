#!/usr/bin/env bash
# Bump version across all fastmcp-engineering manifests.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="$REPO_ROOT/.version-bump.json"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <new-version>" >&2
    exit 1
fi
NEW_VERSION="$1"

if ! command -v node >/dev/null 2>&1; then
    echo "node required" >&2
    exit 1
fi

node - "$CONFIG" "$NEW_VERSION" <<'EOF'
const [configPath, newVersion] = process.argv.slice(2);
const fs = require("fs");
const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
let changed = 0;
for (const entry of config.files) {
    const full = require("path").resolve(configPath, "..", entry.path);
    if (!fs.existsSync(full)) {
        console.warn(`skip (missing): ${entry.path}`);
        continue;
    }
    const raw = fs.readFileSync(full, "utf8");
    const json = JSON.parse(raw);
    const parts = entry.field.split(".");
    let cursor = json;
    for (let i = 0; i < parts.length - 1; i++) cursor = cursor[parts[i]];
    cursor[parts[parts.length - 1]] = newVersion;
    fs.writeFileSync(full, JSON.stringify(json, null, 2) + "\n");
    console.log(`updated ${entry.path} -> ${newVersion}`);
    changed++;
}
if (changed === 0) {
    console.error("no manifests updated");
    process.exit(1);
}
EOF
