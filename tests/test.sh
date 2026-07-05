#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

if pytest /tests/test_outputs.py -rA; then
  cat > /logs/verifier/ctrf.json <<'JSON'
{
  "results": {
    "tool": {
      "name": "pytest"
    },
    "summary": {
      "tests": 1,
      "passed": 1,
      "failed": 0,
      "skipped": 0,
      "pending": 0,
      "other": 0,
      "start": 0,
      "stop": 0
    },
    "tests": []
  }
}
JSON
  echo 1 > /logs/verifier/reward.txt
else
  cat > /logs/verifier/ctrf.json <<'JSON'
{
  "results": {
    "tool": {
      "name": "pytest"
    },
    "summary": {
      "tests": 1,
      "passed": 0,
      "failed": 1,
      "skipped": 0,
      "pending": 0,
      "other": 0,
      "start": 0,
      "stop": 0
    },
    "tests": []
  }
}
JSON
  echo 0 > /logs/verifier/reward.txt
fi
