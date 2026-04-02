import os
import json
import random
import urllib.parse
from flask import Blueprint

from catalogs import CATALOGS, ANIMATIONS, SERIES
from utils.responses import respond_with, build_metas

catalog_bp = Blueprint('catalog', __name__)

# --- Cache calculado uma única vez na inicialização do controller ---
SAGA_NAMES_SORTED = [dados["name"] for dados in CATALOGS.values()]
CATALOG_BY_NAME = {dados["name"]: dados for dados in CATALOGS.values()}
ALL_SAGAS = list(CATALOGS.values())

ANIM_NAMES_SORTED = [dados["name"] for dados in ANIMATIONS.values()]
ANIM_BY_NAME = {dados["name"]: dados for dados in ANIMATIONS.values()}
ALL_ANIM = list(ANIMATIONS.values())

SERIES_NAMES_SORTED = [dados["name"] for dados in SERIES.values()]
SERIES_BY_NAME = {dados["name"]: dados for dados in SERIES.values()}
ALL_SERIES = list(SERIES.values())

# Catálogo de destaque dinâmico
_DESTAQUE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'destaque.json')
try:
    with open(_DESTAQUE_PATH, encoding='utf-8') as f:
        DESTAQUE = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    DESTAQUE = {"id": "destaque", "title": "⭐ Em Destaque", "items": []}


@catalog_bp.route("/catalog/movie/cine_destaque.json")
@catalog_bp.route("/<config_b64>/catalog/movie/cine_destaque.json")
def addon_catalog_destaque(config_b64=None):
    """Retorna o catálogo de destaque da semana."""
    return respond_with({"metas": build_metas(DESTAQUE.get("items", []), "movie")})


@catalog_bp.route("/catalog/<media_type>/<catalog_id>.json", defaults={"config_b64": None})
@catalog_bp.route("/<config_b64>/catalog/<media_type>/<catalog_id>.json")
def addon_catalog_default(config_b64, media_type, catalog_id):
    """
    Fallback acionado quando o Stremio abre a aba sem saga selecionada.
    Exibe uma seleção aleatória de sagas.
    """
    if media_type not in ["movie", "series"]:
        return respond_with({"metas": []})

    if catalog_id == "cine_maratona":
        pool = ALL_SAGAS
    elif catalog_id == "cine_animacoes":
        pool = ALL_ANIM
    elif catalog_id == "cine_series":
        pool = ALL_SERIES
    elif catalog_id == "cine_destaque":
        return addon_catalog_destaque()
    else:
        return respond_with({"metas": []})

    sagas_aleatorias = random.sample(pool, min(15, len(pool)))
    lista_filmes = [saga["items"][0] for saga in sagas_aleatorias if saga["items"]]

    return respond_with({"metas": build_metas(lista_filmes, media_type)})


@catalog_bp.route("/catalog/<media_type>/<catalog_id>/<extra_str>.json", defaults={"config_b64": None})
@catalog_bp.route("/<config_b64>/catalog/<media_type>/<catalog_id>/<extra_str>.json")
def addon_catalog_com_extra(config_b64, media_type, catalog_id, extra_str):
    """
    Rota chamada quando o usuário seleciona uma saga/série específica,
    ou realiza uma busca (search) ou paginação (skip).
    """
    if media_type not in ["movie", "series"]:
        return respond_with({"metas": []})

    # Fazer parsing da string `genre=marvel&skip=20` ou `search=Avatar`
    params = dict(urllib.parse.parse_qsl(extra_str))
    
    saga_param = params.get("genre")
    search_param = params.get("search")
    
    try:
        skip_param = int(params.get("skip", 0))
    except ValueError:
        skip_param = 0

    if catalog_id == "cine_maratona":
        pool = ALL_SAGAS
        catalog_by_name = CATALOG_BY_NAME
    elif catalog_id == "cine_animacoes":
        pool = ALL_ANIM
        catalog_by_name = ANIM_BY_NAME
    elif catalog_id == "cine_series":
        pool = ALL_SERIES
        catalog_by_name = SERIES_BY_NAME
    else:
        return respond_with({"metas": []})

    lista_itens = []

    # 1. Filtro por Busca (search)
    if search_param:
        search_query = search_param.lower()
        # Evitar dupes se o mesmo item estiver em múltiplas sagas
        vistos = set()
        for saga in pool:
            for item in saga["items"]:
                if item["id"] not in vistos and search_query in item["name"].lower():
                    vistos.add(item["id"])
                    lista_itens.append(item)
                    
    # 2. Filtro por Saga (genre)
    elif saga_param:
        saga = catalog_by_name.get(saga_param)
        if saga:
            lista_itens = saga["items"]

    # 3. Paginação (skip)
    # Stremio costuma requisitar os itens aos poucos se houver 'skip'.
    # Retornamos os próximos 100 resultados.
    lista_itens = lista_itens[skip_param:skip_param+100]

    return respond_with({"metas": build_metas(lista_itens, media_type)})
