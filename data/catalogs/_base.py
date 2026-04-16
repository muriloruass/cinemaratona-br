from dataclasses import dataclass, field
from typing import Optional

@dataclass
class CatalogItem:
    id: str                          # tt... (IMDb)
    name: str
    year: Optional[int] = None
    type: str = "movie"              # "movie" | "series"
    saga: Optional[str] = None       # slug da saga pai (ex: "mcu")
    order: Optional[int] = None      # posição dentro da saga
    watch_order_note: Optional[str] = None  # "Assista antes de Endgame"
    featured: bool = False           # destaque semanal
    tags: list[str] = field(default_factory=list)

def to_meta(item: CatalogItem, poster_base_url: str) -> dict:
    """Converte para formato Stremio meta."""
    meta = {
        "id": item.id,
        "type": item.type,
        "name": item.name,
        "poster": poster_base_url.format(item.id),
    }
    if item.year:
        meta["year"] = item.year
    if item.watch_order_note:
        meta["description"] = item.watch_order_note
    return meta
