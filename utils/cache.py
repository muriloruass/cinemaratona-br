import time
from typing import Any, Optional

_CACHE: dict = {}
_TTL = 300  # 5 minutos

def cache_get(key: str) -> Optional[Any]:
    """Recupera um item do cache se ainda for válido."""
    entry = _CACHE.get(key)
    if entry and time.time() - entry["ts"] < _TTL:
        return entry["data"]
    return None

def cache_set(key: str, data: Any):
    """Armazena um item no cache com timestamp atual."""
    _CACHE[key] = {"data": data, "ts": time.time()}
