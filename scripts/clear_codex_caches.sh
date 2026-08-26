  #!/usr/bin/env bash
  set -euo pipefail

  CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"

  echo "Deleting local Codex session/history/state/cache data from: $CODEX_HOME"
  echo "This also deletes Computer Use helper files."
  echo "Kept: auth, config, skills, plugins, and installation_id."
  echo

  rm -rf \
    "$CODEX_HOME/sessions" \
    "$CODEX_HOME/archived_sessions" \
    "$CODEX_HOME/attachments" \
    "$CODEX_HOME/shell_snapshots" \
    "$CODEX_HOME/browser/sessions" \
    "$CODEX_HOME/sqlite" \
    "$CODEX_HOME/process_manager" \
    "$CODEX_HOME/thread-writer-locks" \
    "$CODEX_HOME/generated_images" \
    "$CODEX_HOME/visualizations" \
    "$CODEX_HOME/node_repl" \
    "$CODEX_HOME/tmp" \
    "$CODEX_HOME/.tmp" \
    "$CODEX_HOME/cache" \
    "$CODEX_HOME/vendor_imports" \
    "$CODEX_HOME/computer-use"

  rm -f \
    "$CODEX_HOME/history.jsonl" \
    "$CODEX_HOME/session_index.jsonl" \
    "$CODEX_HOME/models_cache.json" \
    "$CODEX_HOME/model.json" \
    "$CODEX_HOME/version.json" \
    "$CODEX_HOME/thread_history_1.sqlite" \
    "$CODEX_HOME/thread_history_1.sqlite-wal" \
    "$CODEX_HOME/thread_history_1.sqlite-shm" \
    "$CODEX_HOME/logs_2.sqlite" \
    "$CODEX_HOME/logs_2.sqlite-wal" \
    "$CODEX_HOME/logs_2.sqlite-shm" \
    "$CODEX_HOME/goals_1.sqlite" \
    "$CODEX_HOME/goals_1.sqlite-wal" \
    "$CODEX_HOME/goals_1.sqlite-shm" \
    "$CODEX_HOME/queue_1.sqlite" \
    "$CODEX_HOME/memories_1.sqlite" \
    "$CODEX_HOME/state_5.sqlite" \
    "$CODEX_HOME/state_5.sqlite-wal" \
    "$CODEX_HOME/state_5.sqlite-shm" \
    "$CODEX_HOME/.codex-global-state.json" \
    "$CODEX_HOME/.codex-global-state.json.bak" \
    "$CODEX_HOME/.DS_Store"

  echo "Done."


