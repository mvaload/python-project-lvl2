install:
	poetry install
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests
build:
	poetry build
package-install:
	pip install --user dist/*.whl
publish:
	poetry publish --dry-run
