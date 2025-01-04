.DEFAULT_GOAL := all
.PHONY: all changelog coverage deps lint publish pull push schemas test

all:  ## Run tests with coverage, lint and static-check code
	make coverage
	make lint

coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=iuliia/* -m pytest -ra
	python -m coverage report -m

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black coverage flake8 flit mccabe mypy pylint pytest

lint:  ## Lint and static-check code
	python -m flake8 iuliia
	python -m pylint iuliia
	python -m mypy iuliia

publish:  ## Publish to PyPi
	python -m flit publish

pull:  ## Pull code and schemas
	git pull
	cd iuliia/schemas && git pull && cd ../..

push:  ## Push commits and tags
	git push && git push --tags

schemas:  ## Update schemas
	cd iuliia/schemas && git submodule update --init --recursive && cd ../..

test:  ## Run tests
	python -m pytest -ra
