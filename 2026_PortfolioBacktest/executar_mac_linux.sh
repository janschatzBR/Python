#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

PYTHON=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON="python"
else
  echo "Python 3.10+ não encontrado."
  exit 1
fi

if [ ! -d .venv ]; then
  echo "Criando ambiente virtual..."
  "$PYTHON" -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python download.py

echo
echo "Concluído. Veja a pasta output."
