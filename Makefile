.PHONY: build clean clean-pyc clean-build


dev-env:
	docker build -t giles-dev . -f Dockerfile.dev --no-cache 

build:	clean
	python3 setup.py bdist_wheel

upload:
	twine upload -u $(PYPI_USER) -p $(PYPI_PASSWORD) dist/*

test-upload:
	twine upload --repository-url -u $(PYPI_TEST_USER) \
	-p $(PYPI_TEST_PASSWORD) https://test.pypi.org/legacy/ dist/*

clean:	clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

clean-build:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
