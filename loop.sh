#!/bin/bash

while true; do
  echo "=== RUN $(date) ==="

  codex "$(cat task.txt)"

  echo "=== DONE ==="
  sleep 30
done
