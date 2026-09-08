#!/bin/sh
set -eu

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: 需要 Node.js 20 以上版本" >&2
  exit 1
fi

major=$(node -p 'process.versions.node.split(".")[0]')
if [ "$major" -lt 20 ]; then
  echo "ERROR: 目前 Node.js $major，請升級到 20 以上" >&2
  exit 1
fi

if [ ! -d .git ]; then
  git init
  git add .
  git -c user.name="Codex Student" -c user.email="student@example.invalid" commit -m "chore: initialize tideflow lab"
fi

echo "READY: 執行 npm test 與 npm run lint"
