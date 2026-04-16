import os
import glob
import json
from typing import Dict, List, Optional

from ._base import CatalogItem
from .sagas import SAGAS
from .cronologica import CRONOLOGICA
from .maratonas import MARATONAS
from .series import SERIES
from .animacoes import ANIMACOES

# Unificação de todos os catálogos para facilitar busca por ID
ALL_CATALOGS = {
    **SAGAS,
    **CRONOLOGICA,
    **MARATONAS,
    **SERIES,
    **ANIMACOES
}

# Organização dos catálogos por grupo (IDs de catálogo do Stremio)
CATALOG_GROUPS = {
    "cine_sagas_filmes": [
        "marvel", "starwars", "harrypotter", "senhordosaneis", 
        "007", "missaoimpossivel", "johnwick", "velozesefuriosos", 
        "jurassic", "rocky", "matrix", "piratasdocaribe", "transformers",
        "alien", "xmen", "indianajones", "planetadosmacacos", "rambo",
        "narnia", "poderosochefao", "halloween", "horadopesadelo",
        "sextafeira13", "panico", "premonicao", "invocacaodomal"
    ],
    "cine_sagas_series": [
        "dragonball_series", "starwars_series", "theboys", 
        "gameofthrones", "walkingdead"
    ],
    "cine_sagas_animacoes": [
        "disney_filmes", "pixar_filmes", "toystory_anim", "procurandonemo", 
        "monstros", "osincrivel", "carros", "inside_out", "leao", "frozen", 
        "moana", "zootopia", "liloestitch", "wreck_it_ralph", "mulan_disney", 
        "aladdin_disney", "cinderela_disney", "bela_fera", "pequena_sereia", 
        "dumbo", "peter_pan", "pinoquio", "alicenopaisdasmaravilhas", "malefica",
        "shrek", "meumalvadofavorito"
    ],
    "cine_especiais": [
        "nolan", "tarantino", "cinemanacional", "terror_avulsos",
        "predador", "bourne", "exterminador", "madmax",
        "jogosvorazes", "divergente", "sherlockholmes", "animaisfantasticos"
    ]
}

def get_catalog(catalog_id: str) -> List[CatalogItem]:
    """Retorna a lista de itens de um catálogo específico."""
    return ALL_CATALOGS.get(catalog_id, [])

def _apply_tmdb_overrides():
    """
    Aplica overrides do TMDB (sincronizados em data/sagas/*.json)
    nos catálogos carregados em memória.
    """
    sagas_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sagas")
    if not os.path.isdir(sagas_dir):
        return

    for json_path in glob.glob(os.path.join(sagas_dir, "*.json")):
        key = os.path.splitext(os.path.basename(json_path))[0]
        if key not in ALL_CATALOGS:
            continue

        try:
            with open(json_path, encoding="utf-8") as f:
                raw_items = json.load(f)
            
            # Converte itens do JSON para CatalogItem
            new_items = []
            for item in raw_items:
                if isinstance(item, dict) and item.get("id") and item.get("name"):
                    new_items.append(CatalogItem(
                        id=item["id"],
                        name=item["name"],
                        year=int(item["year"]) if item.get("year") else None,
                        type=item.get("type", "movie")
                    ))
            
            if new_items:
                ALL_CATALOGS[key] = new_items
        except (json.JSONDecodeError, OSError, ValueError):
            continue

# Inicializa overrides ao importar o módulo
_apply_tmdb_overrides()
