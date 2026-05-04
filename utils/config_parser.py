import base64
import json
import logging
from typing import Any, Dict, List
from data.config import DEFAULT_CATEGORIES, CATEGORY_IDS
from utils.i18n import safe_lang

logger = logging.getLogger(__name__)

def parse_addon_config(config_b64: str | None) -> Dict[str, Any]:
    """
    Decodifica o payload base64 do Stremio e normaliza as configurações do usuário.
    
    Args:
        config_b64 (str | None): A string de configuração em base64 da URL.
        
    Returns:
        Dict[str, Any]: Dicionário contendo o idioma ('lang') e as categorias ('categories').
    """
    default_config: Dict[str, Any] = {"lang": "pt-br", "categories": DEFAULT_CATEGORIES}
    
    if not config_b64:
        return default_config
        
    try:
        # Corrige padding do base64 dinamicamente
        padding = "=" * (4 - len(config_b64) % 4)
        decoded_str = base64.b64decode(config_b64 + padding).decode("utf-8")
        cfg: Dict[str, Any] = json.loads(decoded_str)
        
        if not isinstance(cfg, dict):
            return default_config
            
        lang: str = safe_lang(cfg.get("l", cfg.get("lang", "pt-br")))
        categories: List[str] = _extract_categories(cfg)
        
        return {"lang": lang, "categories": categories}
        
    except (base64.binascii.Error, json.JSONDecodeError, UnicodeDecodeError) as e:
        logger.warning(f"Erro ao decodificar config_b64: {e}. Usando defaults.")
        return default_config

def _extract_categories(cfg: Dict[str, Any]) -> List[str]:
    """
    Extrai e valida as categorias do payload JSON.
    Suporta o formato compacto 'c': [index] e o formato longo 'categories': [ids].
    """
    compact_categories = cfg.get("c")
    if isinstance(compact_categories, list):
        valid_categories = []
        for idx in compact_categories:
            if isinstance(idx, int) and 0 <= idx < len(CATEGORY_IDS):
                valid_categories.append(CATEGORY_IDS[idx])
        return valid_categories if valid_categories else DEFAULT_CATEGORIES
    
    categories = cfg.get("categories", DEFAULT_CATEGORIES)
    if isinstance(categories, list) and categories:
        return categories
        
    return DEFAULT_CATEGORIES
