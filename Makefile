.DEFAULT_GOAL := help
.PHONY: changelog coverage deps help lint publish pull push schemas test tox

changelog:  ## Generate changelog
	conventional-changelog -p angular -i CHANGELOG.md -s

coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=iuliia/* -m pytest -ra
	python -m coverage report -m

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black coverage flake8 flit mccabe mypy pylint pytest tox tox-gh-actions

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

tox:  ## Run tests
	python -m tox

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done