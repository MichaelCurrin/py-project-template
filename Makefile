SHELL = /bin/bash
APP_DIR = htmlscreenshot


default: install install-dev

all: hooks install install-dev fix typecheck


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
	mypy $(APP_DIR)


clean:
	rm $(APP_DIR)/var/*.png


page-help:
	@python -m htmlscreenshot.scrape

pages-help:
	@python -m htmlscreenshot

pdf-help:
	@python -m htmlscreenshot.download


page-demo:
	python -m htmlscreenshot.scrape 'https://www.python.org'

pages-demo:
	python -m htmlscreenshot "$(APP_DIR)/sample.txt"

pdf-demo:
	python -m htmlscreenshot.download 'http://ciir.cs.umass.edu/downloads/SEIRiP.pdf'

demos: page-demo pages-demo pdf-demo


run:
	python -m htmlscreenshot "$(APP_DIR)/var/input.txt"
