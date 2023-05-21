PACKAGE_NAME := gitlab-changelog
PACKAGE_PATH := $(shell echo ${PACKAGE_NAME} | tr - _)

create-environment:
	conda env create -f environment.yaml

install:
	pip install .

install-development:
	pip install -e .[development]

sort-import:
	isort .

format:
	autopep8 --recursive --in-place .

check-typing:
	mypy .

lint:
	pylint setup.py ${PACKAGE_PATH}/ tests/

fix: sort-import format check-typing lint

test:
	pytest

report-coverage:
	pytest --cov

clean-source:
	git clean -Xdf

clean-install:
	pip uninstall -y ${PACKAGE_NAME}

clean-environment:
	conda remove -y -n ${PACKAGE_NAME} --all

clean: clean-source clean-install clean-environment
