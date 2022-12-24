SHELL = /usr/bin/env bash -xeuo pipefail

black:
	poetry run black lib main.py

isort:
	poetry run isort lib main.py

format: black isort

.PHONY: \
	black \
	isort \
	format
