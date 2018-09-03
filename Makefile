all:
	install

install:
	python setup.py install

test:
	python -m pytest --pyargs --black  --doctest-modules topojson

test-coverage:
	python -m pytest --black  --cov=topojson  --pyargs  --doctest-modules topojson

test-coverage-html:
	python -m pytest --black  --pyargs --doctest-modules --cov=topojson --cov-report html topojson
