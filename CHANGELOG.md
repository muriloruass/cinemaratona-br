# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Nova rota de saúde `/health` via `health_bp` (substituindo `/ping`).
- Módulo `utils/config_parser.py` para unificação da decodificação de base64.
- Suíte de testes automatizados (`tests/`) com cobertura para manifest, paginação e saúde.
- Arquivos de dependências separados: `requirements-prod.txt` e `requirements-dev.txt`.

### Changed
- Refatoração rigorosa do algoritmo de busca e paginação usando `itertools.islice` e generators para evitar bugs de early exit.
- Atualização dos headers de cache para `s-maxage=86400` (24h na Edge) e `stale-while-revalidate`.
- Migração do sistema de cache local para `cachetools.TTLCache` com teto de memória.
- Unificação de constantes (`CATEGORY_IDS`) em `data/config.py`.
- Melhoria na tipagem (Type Hints) e adesão estrita ao PEP 8.

### Fixed
- Bug crítico na paginação do catálogo onde resultados eram cortados prematuramente.
- Vulnerabilidade de decodificação de Base64 com preenchimento (padding) incorreto.
- Redundância de código (DRY) na decodificação de configurações entre múltiplos controladores.

### Removed
- Rota legada `/ping` (substituída por `/health`).
- Implementações duplicadas de `decode_config`.
- Função morta `build_metas` em `utils/responses.py`.

## [2.5.0] - 2024-05-04
### Added
- Lançamento inicial com suporte a sagas Marvel, Star Wars e Coleções Disney.
