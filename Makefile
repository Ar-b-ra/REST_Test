venv:
	python3 -m venv .venv
	venv/bin/python3 pip install -r requirements.txt

test:
	pytest

run:
	.venv/bin/python3 -m src.app