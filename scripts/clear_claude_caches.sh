#!/usr/bin/env bash
set -euo pipefail

CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"

echo "Deleting local Claude session/history/state/cache data from: $CLAUDE_HOME"
echo "Kept: settings, CLAUDE.md, statusline command, commands, and skills."
echo

rm -rf \
  "$CLAUDE_HOME/projects" \
  "$CLAUDE_HOME/history.jsonl" \
  "$CLAUDE_HOME/file-history" \
  "$CLAUDE_HOME/plans" \
  "$CLAUDE_HOME/cache" \
  "$CLAUDE_HOME/plugins/cache" \
  "$CLAUDE_HOME/plugins/data" \
  "$CLAUDE_HOME/plugins/plugin-catalog-cache.json" \
  "$CLAUDE_HOME/security" \
  "$CLAUDE_HOME/ide" \
  "$CLAUDE_HOME/session-env" \
  "$CLAUDE_HOME/paste-cache" \
  "$CLAUDE_HOME/sessions" \
  "$CLAUDE_HOME/shell-snapshots" \
  "$CLAUDE_HOME/telemetry" \
  "$CLAUDE_HOME/jobs" \
  "$CLAUDE_HOME/debug" \
  "$CLAUDE_HOME/backups" \
  "$CLAUDE_HOME/daemon" \
  "$CLAUDE_HOME/daemon.log" \
  "$CLAUDE_HOME/stats-cache.json" \
  "$CLAUDE_HOME/.last-cleanup" \
  "$CLAUDE_HOME/.DS_Store"

echo "Done."

