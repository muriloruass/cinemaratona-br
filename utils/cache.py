from cachetools import TTLCache
from typing import Any, Optional
import time

# Cache thread-safe com limite de 1000 chaves e TTL de 5 minutos (300s).
# Ideal para ambiente Serverless com instâncias recicladas.
_CACHE = TTLCache(maxsize=1000, ttl=300)

def cache_get(key: str) -> Optional[Any]:
    """Recupera um item do cache se ainda for válido."""
    return _CACHE.get(key)

def cache_set(key: str, data: Any):
    """Armazena um item no cache."""
    _CACHE[key] = data
