# CineMaratona BR - Mini Documentacao Tecnica Para IA

Este arquivo resume a arquitetura, os arquivos e o fluxo do projeto para facilitar analise automatizada e sugestao de melhorias por outra IA.

## 1) Visao Geral

- Tipo: Addon do Stremio (catalogos de filmes e series com foco em maratonas/sagas)
- Linguagem: Python
- Framework web: Flask
- Deploy: Vercel serverless
- Idiomas: pt-br, en-us, es

Fluxo principal:

1. O Stremio consulta o manifesto.
2. O manifesto expone catalogos e opcoes de filtro.
3. O cliente chama endpoints de catalogo.
4. A API retorna `metas` no formato esperado pelo Stremio.

## 2) Entrypoints E Arquivos Centrais

- `app.py`
  - Aplicacao Flask principal.
  - Registra blueprints de catalogo/meta.
  - Expoe rotas de manifesto, configuracao e healthcheck.
  - Decodifica configuracao em Base64 para manifesto personalizado.

- `api/index.py`
  - Entrypoint para Vercel.
  - Importa o app Flask de `app.py`.

- `data/catalogs/` (Novo em v2.1)
  - Estrutura modular de dados substituindo o antigo `catalogs.py`.
  - `__init__.py`: Exporta `get_catalog(id)` e define `CATALOG_GROUPS`.
  - `_base.py`: Dataclass `CatalogItem` e helpers de conversão para Stremio meta.
  - `sagas.py`, `cronologica.py`, `maratonas.py`, `series.py`, `animacoes.py`: Dados categorizados.
  - Aplica overrides dinâmicos lendo JSONs em `data/sagas/`.

## 3) Estrutura De Pastas

### `controllers/`

- `controllers/catalog.py`
  - Endpoint principal de catálogos.
  - Processa filtros (`genre`/saga), busca textual e paginação (`skip`).
  - Implementa cache in-process de 5 minutos para performance.
  - Gerencia os 6 novos catálogos: `cine_sagas`, `cine_universos`, `cine_cronologica`, `cine_maratonas`, `cine_series_saga`, `cine_animacoes`.

- `controllers/meta.py`
  - Endpoint de meta por item.
  - Retorna estrutura minima com poster para o Stremio.

### `data/`

- `data/config.py`
  - Constantes globais do addon.
  - IDs e nomes de catalogos.
  - Versao, base URL, categorias disponiveis e defaults.

- `data/destaque.json`
  - Lista de itens do catalogo em destaque.

- `data/sagas/`
  - Overrides gerados por script (ex.: TMDB sync).
  - Permite atualizar listas sem mexer no hardcode principal.

### `locales/`

- `locales/pt-br.json`
- `locales/en-us.json`
- `locales/es.json`

Arquivos de traducao usados pela funcao de i18n.

### `utils/`

- `utils/cache.py` (Novo em v2.1)
  - Sistema de cache simples in-memory com TTL.

- `utils/i18n.py`
  - Funcao de traducao por chave (`dot notation`).
  - Fallback para pt-br quando necessario.
  - Cache LRU para carregar locale com eficiencia.

- `utils/responses.py`
  - Helper para respostas JSON com headers adequados.
  - Adiciona `Cache-Control` para Edge Caching (Vercel/CDN).
  - Builder de `metas` com campos esperados pelo Stremio.

### `templates/`

- `templates/configure.html`
  - UI de configuracao do addon.
  - Permite escolher idioma e categorias.
  - Gera URL de instalacao com config codificada.

### `scripts/`

- `scripts/sync_saga.py`
  - Script CLI para sincronizar colecoes via TMDB API.
  - Resolve IDs IMDb e salva em `data/sagas/<slug>.json`.
  - Requer `TMDB_API_KEY`.

### `tests/`

- `tests/test_ids.py`
  - Valida IDs de itens contra Cinemeta.

- `tests/test_posters.py`
  - Verifica disponibilidade de posters (metahub).

- `tests/verify_animations.py`
  - Valida IDs das animacoes no provedor de metadados.

### Raiz

- `requirements.txt`: dependencias Python.
- `Makefile`: comandos de install/dev/test/sync.
- `vercel.json`: configuracao de roteamento/build no Vercel.
- `CHANGELOG.md`: historico de versoes e features.
- `check_types.py`: utilitario para verificar tipo de itens via API.

## 4) Endpoints Principais

Rotas de app:

- `GET /`
  - Redireciona para `/configure`.

- `GET /ping`
  - Healthcheck simples (`pong`).

- `GET /manifest.json`
  - Manifesto default do addon.

- `GET /<config_b64>/manifest.json`
  - Manifesto personalizado por config codificada em Base64.

- `GET /configure`
  - Pagina web para gerar link de instalacao customizado.

Rotas de catalogo:

- `GET /catalog/movie/cine_destaque.json`
- `GET /<config>/catalog/movie/cine_destaque.json`
  - Catalogo de destaque semanal.

- `GET /catalog/<type>/<id>.json`
- `GET /catalog/<type>/<id>/<extra_str>.json`
  - Catalogos com filtros, busca e paginacao.

Rotas de meta:

- `GET /meta/<type>/<id>.json`
  - Retorna meta minima por item.

## 5) Modelo De Dados (Resumo)

Itens de catalogo normalmente contem:

- `id` (IMDb, formato `tt...`)
- `name`
- `year`
- `type` (`movie` ou `series`)

Resposta do catalogo no formato Stremio:

- `{ "metas": [...] }`

Cada `meta` costuma incluir:

- `id`
- `type`
- `name`
- `poster`

## 6) Internacionalizacao (i18n)

- O idioma vem da configuracao do usuario (UI + Base64 no link).
- Chaves de traducao cobrem nome/descricao do addon, labels da configuracao e nomes de categorias.
- Se chave/idioma nao existir, ha fallback para pt-br.

## 7) Como A Configuracao Personalizada Funciona

1. Usuario marca categorias e idioma em `/configure`.
2. Frontend gera payload JSON de config.
3. Payload e codificado em Base64.
4. Link final inclui `<config_b64>`.
5. Backend decodifica e monta manifesto filtrado para aquele perfil.

## 8) Dependencias E Execucao

Dependencias principais (requirements):

- Flask
- flask-cors
- gunicorn
- Werkzeug
- python-dotenv

Comandos comuns (Makefile):

- `make install` -> cria venv e instala deps
- `make dev` -> sobe servidor local
- `make test` -> roda validadores de dados
- `make sync` -> sincroniza saga (TMDB)

## 9) Qualidade Atual E Riscos Tecnicos

Pontos fortes:

- Estrutura simples e direta para addon Stremio.
- Suporte a multiplos idiomas.
- Mecanismo de override via JSON em `data/sagas/`.
- Script para sincronizacao automatizada de colecoes.

Gaps e riscos:

- Poucos testes de logica HTTP/manifest/catalog (foco atual em integridade de dados).
- `catalogs.py` e grande e centraliza muito conteudo hardcoded.
- Falta maior cobertura de erros em chamadas externas e casos de borda.
- Config em Base64 e apenas codificacao (nao e protecao).
- Ausencia de pipeline de CI explicita no repositorio para regressao automatica.

## 10) Sugestoes De Melhorias Para IA Avaliar

1. Quebrar `catalogs.py` em modulos por dominio (`movies`, `animations`, `series`, `specials`).
2. Criar testes de endpoint com `pytest` + `Flask test client` para manifesto/catalog/meta.
3. Adicionar validacoes mais estritas de schema para itens de catalogo.
4. Introduzir observabilidade basica (logs estruturados por rota e erros externos).
5. Melhorar estrategia de cache para respostas de catalogo mais acessadas.
6. Adicionar CI para lint/test/validacao de dados em PR.
7. Padronizar tratamento de erros de APIs externas com fallback previsivel.

## 11) Checklist Rapido Para Outra IA

Se voce (IA) for sugerir mudancas, comece por:

1. Ler `app.py`, `controllers/catalog.py`, `catalogs.py`, `utils/responses.py`, `utils/i18n.py`.
2. Executar os comandos de teste atuais e mapear lacunas de cobertura.
3. Revisar consistencia entre `data/config.py`, `locales/*.json` e filtros de catalogo.
4. Propor plano incremental sem quebrar compatibilidade do formato Stremio.
