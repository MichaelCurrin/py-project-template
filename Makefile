default: install install-dev

all: hooks install install-dev format-check lint typecheck test


h help:
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


.PHONY: hooks
hooks:
	cd .git/hooks && ln -s -f ../../hooks/pre-push pre-push

# Install core dependencies.
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Install dev dependencies.
install-dev:
	pip install -r requirements-dev.txt

upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


format:
	black .
	isort .
format-check:
	black . --diff --check
	isort . --diff --check-only

# Lint with PyLint.
pylint:
	# Exit on fatal error code.
	pylint pyproject || pylint-exit $$?  # TODO: Replace pyproject with your app directory.

# Lint with Flake8.
flake8:
	# Error on syntax errors or undefined names.
	flake8 . --select=E9,F63,F7,F82 --show-source
	# Warn on everything else.
	flake8 . --exit-zero

lint: pylint flake8

# Apply formatting and lint fixes.
fix: format lint

t typecheck:
	mypy pyproject tests  # TODO: Replace pyproject with your app directory.


# Run tests.
unit:
	pytest

# TODO: Add integration tests etc here or remove this target.
test: unit
