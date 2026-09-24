#!/bin/sh -eu

if ! ~/ansible-venv/bin/pip freeze | grep -q ^pytest; then
	echo "Installing test packages..."
	~/ansible-venv/bin/pip install pytest pytest-testinfra
fi

echo "Downloading test cases..."
curl -s https://raw.githubusercontent.com/romankuchin/ica0002-2026/refs/heads/tests/tests/test_all.py > test_all.py
git diff test_all.py

~/ansible-venv/bin/pytest -rA --tb=no
