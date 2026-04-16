.PHONY: dev test sync install

# Ambiente virtual
VENV = venv/bin

# Variáveis (substitua se necessário em dev)
export PORT ?= 7000

install:
	@echo "📦 Instalando dependências..."
	python3 -m venv venv
	$(VENV)/python3 -m pip install -r requirements.txt

dev:
	@echo "🚀 Iniciando servidor de desenvolvimento na porta $(PORT)..."
	$(VENV)/python3 api/index.py || $(VENV)/python3 app.py

test:
	@echo "🧪 Executando testes..."
	@if [ -d "tests" ]; then \
		$(VENV)/pytest tests/test_api.py && \
		$(VENV)/python3 tests/test_ids.py && \
		$(VENV)/python3 tests/test_posters.py && \
		$(VENV)/python3 tests/verify_animations.py; \
	else \
		echo "Nenhuma pasta 'tests/' encontrada."; \
	fi

sync:
	@echo "🔄 Testando sincronização de uma saga via TMDB (Local)..."
	$(VENV)/python3 scripts/sync_saga.py "Marvel Cinematic Universe" marvel
