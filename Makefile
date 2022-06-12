install:
	poetry install
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
build:
	poetry build
selfcheck:
	poetry check
check: selfcheck test lint
build: check
	poetry build

.PHONY: install test lint selfcheck check build
