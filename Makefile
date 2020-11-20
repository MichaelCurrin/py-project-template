default: install install-dev

all: install install-dev lint format-check test


# Show summary of make commands.
h help:
	@echo 'Print lines that are not indented (targets and comments) or empty, plus any indented echo lines.'
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


# Install core dependencies.
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Install dev dependencies.
install-dev:
	pip install -r requirements-dev.txt


# Format with Black.
format:
	black .
format-check:
	# Exit with error status if fixes need to be applied.
	black . --diff --check

# Lint with PyLint.
pylint:
	# Exit on fatal error code.
	pylint pyproject || pylint-exit $$?  # TODO: Replace project name on an new projects.

# Lint with Flake8.
flake8:
	# Stop the build if there are Python syntax errors or undefined names.
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide.
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: pylint flake8

# Apply formatting and lint fixes.
fix: format lint


# Run tests.
unit:
	pytest

# TODO: Add integration tests etc here or remove this target.
test: unit
