#!/usr/bin/env bash
# Automatic restore of virtual environments on Linux
set -e
cd "$(dirname "$0")"
ROOT="$(pwd)"
PY39="$HOME/.pyenv/versions/3.9.13/bin/python"

echo "===== TEAM 1: virtualenv ====="
cd "$ROOT/team1"
"$PY39" -m pip install --quiet virtualenv
"$PY39" -m virtualenv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python test_ols.py

echo "===== TEAM 1: Poetry ====="
poetry config virtualenvs.in-project true
poetry env use "$PY39"
poetry install --no-root
poetry run python test_ols.py

echo "===== TEAM 2: conda ====="
cd "$ROOT/team2"
source "$HOME/miniforge3/etc/profile.d/conda.sh"
conda env remove -n team2 -y >/dev/null 2>&1 || true
conda env create -f environment.yml
conda run -n team2 python test_linreg.py

echo "===== DONE: all environments restored ====="