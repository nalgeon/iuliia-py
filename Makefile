.PHONY: changelog coverage lint pull push schemas test

changelog:
	conventional-changelog -p angular -i CHANGELOG.md -s
coverage:
	coverage erase
	coverage run --include=iuliia/* -m pytest
	coverage report -m
lint:
	flake8 iuliia
	pylint iuliia
	mypy iuliia
pull:
	git pull
	cd iuliia/schemas && git pull && cd ../..
push:
	git push --follow-tags
schemas:
	cd iuliia/schemas && git submodule update --init --recursive && cd ../..
test:
	pytest
