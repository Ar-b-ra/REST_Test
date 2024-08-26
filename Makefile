venv:
	python3 -m venv .venv
	venv/bin/python3 pip install -r requirements.txt

test:
	coverage run -m pytest --cov=src

run:
	.venv/bin/python3 -m src.app