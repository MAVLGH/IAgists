install-local:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip freeze > req_freeze.txt