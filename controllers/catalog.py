import os
import json
import random
import urllib.parse
from flask import Blueprint

from data.catalogs import get_catalog, CATALOG_GROUPS, ALL_CATALOGS
from data.catalogs._base import to_meta
from data.config import EXTRA_NAME, POSTER_METAHUB_URL
from utils.responses import respond_with
from utils.logger import log_request

catalog_bp = Blueprint('catalog', __name__)

# Mapeamento reverso de labels para IDs de saga (para processar o filtro 'genre')
# Carregado na inicialização para performance
from data.config import AVAILABLE_CATEGORIES
LABEL_TO_ID = {cat["label"]: cat["id"] for cat in AVAILABLE_CATEGORIES}

def build_metas_modular(items, media_type):
    """Converte lista de CatalogItem para formato Stremio metas."""
    return [to_meta(item, POSTER_METAHUB_URL) for item in items if item.type == media_type]

from utils.cache import cache_get, cache_set

@catalog_bp.route("/catalog/<media_type>/<catalog_id>.json", defaults={"config_b64": None})
@catalog_bp.route("/<config_b64>/catalog/<media_type>/<catalog_id>.json")
@log_request
def addon_catalog_default(config_b64, media_type, catalog_id):
    """
    Fallback acionado quando o Stremio abre a aba sem saga selecionada.
    Exibe uma seleção aleatória de itens do grupo correspondente.
    """
    cache_key = f"catalog_{config_b64}_{media_type}_{catalog_id}"
    cached = cache_get(cache_key)
    if cached:
        return respond_with(cached)

    if catalog_id not in CATALOG_GROUPS:
        return respond_with({"metas": []})

    saga_ids = CATALOG_GROUPS[catalog_id]
    
    # Coleta o primeiro item de cada saga do grupo para servir de "preview"
    preview_items = []
    for sid in saga_ids:
        items = get_catalog(sid)
        if items:
            # Filtra por tipo de mídia
            filtered = [it for it in items if it.type == media_type]
            if filtered:
                preview_items.append(filtered[0])

    # Se não houver itens (ex: pedindo 'movie' em catálogo de 'series'), retorna vazio
    if not preview_items:
        return respond_with({"metas": []})

    # Mostra uma amostra aleatória se houver muitos
    sample_size = min(20, len(preview_items))
    selected = random.sample(preview_items, sample_size)

    result = {"metas": build_metas_modular(selected, media_type)}
    cache_set(cache_key, result)
    return respond_with(result)


@catalog_bp.route("/catalog/<media_type>/<catalog_id>/<extra_str>.json", defaults={"config_b64": None})
@catalog_bp.route("/<config_b64>/catalog/<media_type>/<catalog_id>/<extra_str>.json")
@log_request
def addon_catalog_com_extra(config_b64, media_type, catalog_id, extra_str):
    """
    Rota chamada quando o usuário seleciona uma saga específica (genre),
    ou realiza uma busca (search) ou paginação (skip).
    """
    cache_key = f"catalog_extra_{config_b64}_{media_type}_{catalog_id}_{extra_str}"
    cached = cache_get(cache_key)
    if cached:
        return respond_with(cached)

    if catalog_id not in CATALOG_GROUPS:
        return respond_with({"metas": []})

    params = dict(urllib.parse.parse_qsl(extra_str))
    saga_label = params.get(EXTRA_NAME)
    search_param = params.get("search")
    
    try:
        skip_param = int(params.get("skip", 0))
    except ValueError:
        skip_param = 0

    lista_itens = []

    # 1. Filtro por Busca (search) em todo o grupo
    if search_param:
        search_query = search_param.lower()
        group_saga_ids = CATALOG_GROUPS[catalog_id]
        vistos = set()
        for sid in group_saga_ids:
            for item in get_catalog(sid):
                if item.id not in vistos and search_query in item.name.lower():
                    vistos.add(item.id)
                    lista_itens.append(item)
                    
    # 2. Filtro por Saga (genre)
    elif saga_label:
        saga_id = LABEL_TO_ID.get(saga_label, saga_label)
        lista_itens = get_catalog(saga_id)

    # 3. Fallback se não houver extra (não deveria cair aqui pela lógica das rotas, mas por segurança)
    else:
        return addon_catalog_default(config_b64, media_type, catalog_id)

    # Filtra por tipo de mídia
    lista_itens = [it for it in lista_itens if it.type == media_type]

    # 4. Paginação (skip)
    lista_itens = lista_itens[skip_param:skip_param+100]

    result = {"metas": build_metas_modular(lista_itens, media_type)}
    cache_set(cache_key, result)
    return respond_with(result)
