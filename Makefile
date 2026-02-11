
all:
	@echo Here are some valid "make" targets. && echo
	@egrep '^[a-z-]*:' Makefile | awk '{print $$1}' | tr -d :

ACTIVATE := echo && source .venv/bin/activate
PYTHONPATH := .

.venv:
	uv sync

test: .venv
	$(ACTIVATE) && python -m unittest tests/*_test.py

lint: .venv
	$(ACTIVATE) && black . && isort . && ruff check
	$(ACTIVATE) && pyright
