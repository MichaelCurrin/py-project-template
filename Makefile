# Show summary of make commands.
help:
	@echo Includes lines that are non-indented (targets and comments) or empty, plus indented echo lines.
	@egrep '(^\S)|(^$$)|\s+@echo' Makefile


# Install core dependencies.
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Install dev dependencies.
dev-install:
	pip install -r requirements-dev.txt


# Run PY linting with flake8.
lint:
	# Stop the build if there are Python syntax errors or undefined names.
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide.
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
