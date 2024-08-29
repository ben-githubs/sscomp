activate:
	poetry shell

install-poetry:
	which poetry || python -m pip install poetry

install: install-poetry
	poetry install

install-dev: install-poetry
	poetry install --with=dev

lint-pylint:
	poetry run bandit -r sscomp
	poetry run pylint sscomp

lint-fmt:
	poetry run black --line-length=100 --check sscomp

lint: lint-pylint lint-fmt

fmt:
	poetry run black --line-length=100 sscomp