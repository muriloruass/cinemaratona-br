# utils/i18n.py — Helper de internacionalização do CineMaratona BR
# Suporta dot-notation: t('pt-br', 'configure.title')
# Fallback automático para pt-br se idioma não encontrado.

import json
import os
import functools

SUPPORTED_LANGS = ['pt-br', 'en-us', 'es', 'fr']
DEFAULT_LANG = 'pt-br'

# Caminho para a pasta locales (relativo ao diretório pai deste arquivo)
_LOCALES_DIR = os.path.join(os.path.dirname(__file__), '..', 'locales')


@functools.lru_cache(maxsize=8)
def _load_locale(lang: str) -> dict:
    """Carrega e faz cache do arquivo JSON de um idioma."""
    safe_lang = lang if lang in SUPPORTED_LANGS else DEFAULT_LANG
    file_path = os.path.join(_LOCALES_DIR, f'{safe_lang}.json')
    try:
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback para pt-br em caso de erro
        if safe_lang != DEFAULT_LANG:
            return _load_locale(DEFAULT_LANG)
        return {}


def get_locale(lang: str) -> dict:
    """Retorna o payload de locale para um idioma válido com fallback."""
    return _load_locale(lang if lang in SUPPORTED_LANGS else DEFAULT_LANG)


def t(lang: str, key: str) -> str:
    """
    Retorna a string traduzida para o idioma especificado.
    Suporta dot-notation para chaves aninhadas (ex: 'configure.title').
    Se a chave não existir, retorna a própria chave como fallback.
    """
    locale = get_locale(lang)
    parts = key.split('.')
    value = locale
    for part in parts:
        if isinstance(value, dict):
            value = value.get(part)
        else:
            return key  # chave não encontrada
    return value if isinstance(value, str) else key


def safe_lang(lang: str) -> str:
    """Normaliza e valida um código de idioma, retornando DEFAULT_LANG se inválido."""
    if not lang:
        return DEFAULT_LANG
    normalized = lang.lower().strip()
    return normalized if normalized in SUPPORTED_LANGS else DEFAULT_LANG


def category_label(lang: str, category_id: str, fallback: str) -> str:
    """Resolve o rótulo traduzido de uma categoria pelo ID."""
    value = t(lang, f"catalog_ids.{category_id}")
    return fallback if value == f"catalog_ids.{category_id}" else value


def title_label(lang: str, imdb_id: str, fallback: str) -> str:
    """Resolve o título traduzido de um item pelo IMDb ID."""
    value = t(lang, f"titles.{imdb_id}")
    return fallback if value == f"titles.{imdb_id}" else value
