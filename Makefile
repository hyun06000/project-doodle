init:
	pip install -e .
	pip install -r requirements.txt

format:
	black .
	isort .