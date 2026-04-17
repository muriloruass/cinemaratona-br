from flask import Flask, jsonify, render_template, request, send_file, redirect
from flask_cors import CORS
from data.catalogs import CATALOG_GROUPS
from data.config import (
    ADDON_ID,
    ADDON_VERSION,
    BASE_URL,
    LOGO_URL,
    AVAILABLE_CATEGORIES,
    DEFAULT_CATEGORIES,
    EXTRA_NAME,
)
import urllib.parse
import json
import base64
import os

from utils.i18n import t, safe_lang, category_label, get_locale, SUPPORTED_LANGS
from utils.responses import respond_with

from controllers.catalog import catalog_bp
from controllers.meta import meta_bp

CATEGORY_BY_ID = {cat["id"]: cat for cat in AVAILABLE_CATEGORIES}
CATEGORY_IDS = [cat["id"] for cat in AVAILABLE_CATEGORIES]

def create_app(testing=False):
    app = Flask(__name__)
    CORS(app)
    
    if testing:
        app.config['TESTING'] = True

    app.register_blueprint(catalog_bp)
    app.register_blueprint(meta_bp)

    def decode_config(config_b64: str) -> dict:
        default = {"lang": "pt-br", "categories": DEFAULT_CATEGORIES}
        if not config_b64:
            return default
        try:
            decoded = base64.b64decode(config_b64 + "==").decode("utf-8")
            cfg = json.loads(decoded)
            if not isinstance(cfg, dict):
                return default
            lang = safe_lang(cfg.get("l", cfg.get("lang", "pt-br")))

            compact_categories = cfg.get("c")
            if isinstance(compact_categories, list):
                categories = [
                    CATEGORY_IDS[idx]
                    for idx in compact_categories
                    if isinstance(idx, int) and 0 <= idx < len(CATEGORY_IDS)
                ]
            else:
                categories = cfg.get("categories", DEFAULT_CATEGORIES)

            if not isinstance(categories, list) or not categories:
                categories = DEFAULT_CATEGORIES
            return {"lang": lang, "categories": categories}
        except Exception:
            return default

    def build_manifest(config: dict) -> dict:
        lang = config.get("lang", "pt-br")
        active_cats = set(config.get("categories", DEFAULT_CATEGORIES))

        def get_options_for_group(group_id):
            ids = CATALOG_GROUPS.get(group_id, [])
            return [
                category_label(lang, sid, CATEGORY_BY_ID.get(sid, {}).get("label", sid))
                for sid in ids 
                if sid in active_cats or group_id in ["cine_sagas_animacoes", "cine_especiais"]
            ]

        catalogs_specs = [
            {"id": "cine_sagas_filmes",    "type": "movie",  "name": t(lang, "catalog_sagas_filmes")},
            {"id": "cine_sagas_animacoes", "type": "movie",  "name": t(lang, "catalog_sagas_animacoes")},
            {"id": "cine_especiais",       "type": "movie",  "name": t(lang, "catalog_especiais")},
        ]

        catalogs = []
        for spec in catalogs_specs:
            options = get_options_for_group(spec["id"])
            if options or spec["id"] in ["cine_especiais", "cine_sagas_animacoes"]:
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
            "types": ["movie"],
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

    @app.route("/")
    def index():
        return redirect("/configure")

    @app.route("/ping")
    def ping():
        return "pong", 200

    @app.route("/CineMaratonaLogo.png")
    def addon_logo():
        return send_file("CineMaratonaLogo.png", mimetype="image/png")

    @app.route("/manifest.json")
    def addon_manifest_default():
        return respond_with(build_manifest({"lang": "pt-br", "categories": DEFAULT_CATEGORIES}))

    @app.route("/<config_b64>/manifest.json")
    def addon_manifest_configured(config_b64):
        config = decode_config(config_b64)
        return respond_with(build_manifest(config))

    @app.route("/configure")
    def configure_page():
        accept_header = request.headers.get("Accept", "").lower()
        user_agent = request.headers.get("User-Agent", "").lower()

        # Some Stremio clients may try to parse /configure as JSON.
        # Return a valid manifest for non-HTML clients to avoid install failures.
        wants_json = (
            "application/json" in accept_header
            or ("stremio" in user_agent and "text/html" not in accept_header)
        )
        if wants_json:
            return respond_with(build_manifest({"lang": "pt-br", "categories": DEFAULT_CATEGORIES}))

        default_lang = "pt-br"
        groups = {
            "filmes": {"name": t(default_lang, "catalog_sagas_filmes"), "items": []},
            "animacoes": {"name": t(default_lang, "catalog_sagas_animacoes"), "items": []},
            "especiais": {"name": t(default_lang, "catalog_especiais"), "items": []}
        }
        id_to_group = {}
        for gid, ids in CATALOG_GROUPS.items():
            if gid == "cine_sagas_filmes": group_key = "filmes"
            elif gid == "cine_sagas_animacoes": group_key = "animacoes"
            else: group_key = "especiais"
            for cid in ids: id_to_group[cid] = group_key

        for cat in AVAILABLE_CATEGORIES:
            gkey = id_to_group.get(cat["id"], "especiais")
            groups[gkey]["items"].append({
                **cat,
                "label": category_label(default_lang, cat["id"], cat["label"])
            })

        locales_payload = {lang: get_locale(lang) for lang in SUPPORTED_LANGS}

        return render_template(
            "configure.html",
            groups=groups,
            base_url=BASE_URL,
            locales_payload=locales_payload,
            category_ids=CATEGORY_IDS,
            supported_langs=SUPPORTED_LANGS,
        )

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=7000, debug=True)
