install:
	python setup.py install

test:
	python -m unittest discover -p "*_test.py"

dev:
	python setup.py develop

.PHONY: install test