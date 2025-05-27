PIP := venv/bin/pip
PYTEST := venv/bin/pytest

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) --cov=app --cov-report=term-missing

coverage-html:
	$(PYTEST) --cov=app --cov-report=html:htmlcov

