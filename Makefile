test:
	python3 setup.py test

coverage:
	coverage run --source=src setup.py test
	coverage report
	coverage html