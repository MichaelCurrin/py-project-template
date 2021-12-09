SHELL = /bin/bash
APP_DIR = pyproject  # TODO: Replace with the name of your app directory.

export PYTHONPATH

default: install install-dev

all: hooks install install-dev fmt-check lint typecheck test


h help:
	@grep '^[a-z]' Makefile


.PHONY: hooks
hooks:
	cd .git/hooks && ln -s -f ../../hooks/pre-push pre-push


install:
	pip install pip --upgrade
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	
upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
	isort .

fmt-check:
	black . --diff --check
	isort . --diff --check-only

pylint:
	source .env \
		&& pylint $(APP_DIR) \
		|| pylint-exit $$?

flake8:
	# Error on syntax errors or undefined names.
	flake8 . --select=E9,F63,F7,F82 --show-source
	# Warn on everything else.
	flake8 . --exit-zero

lint: pylint flake8

fix: fmt lint


t typecheck:
	mypy $(APP_DIR) tests


unit:
	pytest

# TODO: Add integration tests here.
test: unit

run:
	cd $(APP_DIR) && python ./pyproject.py World
