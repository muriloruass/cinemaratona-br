from flask import Flask, jsonify, render_template, request, send_file, redirect
from flask_cors import CORS
from catalogs import CATALOGS, ANIMATIONS, SERIES
from data.config import (
    ADDON_ID,
    ADDON_VERSION,
    BASE_URL,
    LOGO_URL,
    POSTER_METAHUB_URL,
    AVAILABLE_CATEGORIES,
    DEFAULT_CATEGORIES,
    EXTRA_NAME,
)
import urllib.parse
import random
import json
import base64
import os

from utils.i18n import t, safe_lang
from utils.responses import respond_with

from controllers.catalog import catalog_bp, ANIM_NAMES_SORTED
from controllers.meta import meta_bp

app = Flask(__name__)
# Habilitar CORS para permitir que o Stremio se comunique com nossa API sem bloqueios
CORS(app)

app.register_blueprint(catalog_bp)
app.register_blueprint(meta_bp)


def decode_config(config_b64: str) -> dict:
    """
    Decodifica a configuração do usuário a partir de Base64.
    Retorna um dict com 'lang' e 'categories'.
    Se inválido, retorna a config padrão.
    """
    default = {"lang": "pt-br", "categories": DEFAULT_CATEGORIES}
    if not config_b64:
        return default
    try:
        decoded = base64.b64decode(config_b64 + "==").decode("utf-8")
        cfg = json.loads(decoded)
        if not isinstance(cfg, dict):
            return default
        lang = safe_lang(cfg.get("lang", "pt-br"))
        categories = cfg.get("categories", DEFAULT_CATEGORIES)
        if not isinstance(categories, list):
            categories = DEFAULT_CATEGORIES
        return {"lang": lang, "categories": categories}
    except Exception:
        return default


def build_manifest(config: dict) -> dict:
    """Constrói o manifesto do addon com base na config do usuário."""
    lang = config.get("lang", "pt-br")
    active_cats = set(config.get("categories", DEFAULT_CATEGORIES))

    # Filtrar sagas disponíveis com base nas categorias ativas
    filtered_saga_names = [
        dados["name"]
        for key, dados in CATALOGS.items()
        if key in active_cats
    ]
    filtered_series_names = [
        dados["name"]
        for key, dados in SERIES.items()
        if key in active_cats
    ]
    filtered_anim_names = ANIM_NAMES_SORTED  # animações sempre disponíveis

    catalogs = [
        # Catálogo de destaque (sempre primeiro)
        {
            "type": "movie",
            "id": "cine_destaque",
            "name": t(lang, "catalog_featured"),
        },
        # Sagas e Maratonas
        {
            "type": "movie",
            "id": "cine_maratona",
            "name": t(lang, "catalog_sagas"),
            "extra": [
                {
                    "name": EXTRA_NAME,
                    "isRequired": False,
                    "options": filtered_saga_names
                },
                {"name": "search", "isRequired": False},
                {"name": "skip", "isRequired": False}
            ],
            "extraSupported": [EXTRA_NAME, "search", "skip"]
        },
        # Séries
        {
            "type": "series",
            "id": "cine_series",
            "name": t(lang, "catalog_series"),
            "extra": [
                {
                    "name": EXTRA_NAME,
                    "isRequired": False,
                    "options": filtered_series_names
                },
                {"name": "search", "isRequired": False},
                {"name": "skip", "isRequired": False}
            ],
            "extraSupported": [EXTRA_NAME, "search", "skip"]
        },
        # Animações Disney & Pixar
        {
            "type": "movie",
            "id": "cine_animacoes",
            "name": t(lang, "catalog_animations"),
            "extra": [
                {
                    "name": EXTRA_NAME,
                    "isRequired": False,
                    "options": filtered_anim_names
                },
                {"name": "search", "isRequired": False},
                {"name": "skip", "isRequired": False}
            ],
            "extraSupported": [EXTRA_NAME, "search", "skip"]
        }
    ]

    return {
        "id": ADDON_ID,
        "version": ADDON_VERSION,
        "name": t(lang, "addon_name"),
        "description": t(lang, "addon_description"),
        "logo": LOGO_URL,
        "resources": ["catalog", "meta"],
        "types": ["movie", "series"],
        "catalogs": catalogs,
        "behaviorHints": {
            "configurable": True,
            "configurableUrl": f"{BASE_URL}/configure"
        },
        "stremioAddonsConfig": {
            "issuer": "https://stremio-addons.net",
            "signature": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..01bufPwIGEuO8R9okmf43g.eqmi2c8kR0SG7OAWfGNvVMgT8JTy8BPTtN-S8FatjxUoh0sXZxiEAXRMYu3hfa68kO_WMHtkEw_kYtHCpbJP1rMcHXVpj5WWi1o0kGtmIapWiYQOH4MPZcut1bfS0QfM.YT0FeLMuRummbV3hBIqeYw"
        }
    }


# ─── Rotas principais ─────────────────────────────────────────────────────────

@app.route("/")
def index():
    return redirect("/configure")


@app.route("/ping")
def ping():
    """Endpoint leve para manter o servidor acordado."""
    return "pong", 200


@app.route("/CineMaratonaLogo.png")
def addon_logo():
    """Serve a logo do addon diretamente."""
    return send_file("CineMaratonaLogo.png", mimetype="image/png")


# ─── Manifest (com e sem userdata em Base64) ──────────────────────────────────

@app.route("/manifest.json")
def addon_manifest_default():
    """Manifest padrão sem configuração de usuário."""
    return respond_with(build_manifest({"lang": "pt-br", "categories": DEFAULT_CATEGORIES}))


@app.route("/<config_b64>/manifest.json")
def addon_manifest_configured(config_b64):
    """Manifest personalizado com configuração do usuário em Base64."""
    config = decode_config(config_b64)
    return respond_with(build_manifest(config))


# ─── Página de Configuração ───────────────────────────────────────────────────

@app.route("/configure")
def configure_page():
    """Página HTML interativa para o usuário configurar o addon."""
    return render_template(
        "configure.html",
        categories=AVAILABLE_CATEGORIES,
        base_url=BASE_URL,
    )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
