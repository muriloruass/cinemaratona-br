from flask import Flask, jsonify, render_template, request, send_file, redirect
from flask_cors import CORS
from data.catalogs import CATALOG_GROUPS
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

from controllers.catalog import catalog_bp
from controllers.meta import meta_bp

app = Flask(__name__)
# Habilitar CORS para permitir que o Stremio se comunique com nossa API sem bloqueios
CORS(app)

app.register_blueprint(catalog_bp)
app.register_blueprint(meta_bp)

# Mapeamento rápido de IDs para Labels (usado no manifest para opções de gênero)
SAGA_LABELS = {cat["id"]: cat["label"] for cat in AVAILABLE_CATEGORIES}


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

    def get_options_for_group(group_id):
        ids = CATALOG_GROUPS.get(group_id, [])
        return [
            SAGA_LABELS.get(sid, sid) 
            for sid in ids 
            if sid in active_cats or group_id in ["cine_animacoes", "cine_maratonas"]
        ]

    catalogs_specs = [
        {"id": "cine_sagas",        "type": "movie",  "name": t(lang, "catalog_sagas")},
        {"id": "cine_universos",    "type": "movie",  "name": t(lang, "catalog_universos")},
        {"id": "cine_cronologica",  "type": "movie",  "name": t(lang, "catalog_cronologica")},
        {"id": "cine_maratonas",    "type": "movie",  "name": t(lang, "catalog_maratonas")},
        {"id": "cine_series_saga",  "type": "series", "name": t(lang, "catalog_series_saga")},
        {"id": "cine_animacoes",    "type": "movie",  "name": t(lang, "catalog_animacoes")},
    ]

    catalogs = []
    for spec in catalogs_specs:
        options = get_options_for_group(spec["id"])
        # Só expõe o catálogo se houver opções ou se for maratona/animação (sempre visível)
        if options or spec["id"] in ["cine_maratonas", "cine_animacoes"]:
            catalogs.append({
                "type": spec["type"],
                "id": spec["id"],
                "name": spec["name"],
                "extra": [
                    {
                        "name": EXTRA_NAME,
                        "isRequired": False,
                        "options": sorted(list(set(options)))
                    },
                    {"name": "search", "isRequired": False},
                    {"name": "skip", "isRequired": False}
                ],
                "extraSupported": [EXTRA_NAME, "search", "skip"]
            })

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
