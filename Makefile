venv:
	python3 -m venv .venv
	venv/bin/python3 pip install -r requirements/requirements.txt

test:
	coverage run --data-file tests/.coverage -m pytest --cov=src -s

run:
	.venv/bin/python3 -m src.app