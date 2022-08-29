#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

if [[ ! -d build ]]; then
	echo "Directory 'build' doesn't exist, creating it..."
	mkdir -p build
fi

echo "Running tests..."
python3 -m unittest discover -s tests -p "*_test.py" -v
