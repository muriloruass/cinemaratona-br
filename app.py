from flask import Flask, jsonify, request, send_file, redirect
from flask_cors import CORS
from catalogs import CATALOGS, ANIMATIONS, SERIES
import urllib.parse
import random
import json
import base64
import os
import sys

# Adiciona utils/ ao path para imports locais
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from utils.i18n import t, safe_lang

app = Flask(__name__)
# Habilitar CORS para permitir que o Stremio se comunique com nossa API sem bloqueios
CORS(app)

# URL padrão e confiável para obter posters do Stremio via ID do IMDb
POSTER_METAHUB_URL = "https://images.metahub.space/poster/medium/{}/img"

# URL base do addon em produção
BASE_URL = "https://cinemaratona-br.vercel.app"

# Categorias disponíveis para filtro de usuário na página /configure
AVAILABLE_CATEGORIES = [
    {"id": "marvel",     "label_key": "categories.marvel"},
    {"id": "starwars",   "label_key": None, "label": "Star Wars"},
    {"id": "xmen",       "label_key": None, "label": "X-Men"},
    {"id": "007",        "label_key": "categories.007"},
    {"id": "missaoimpossivel", "label_key": None, "label": "Missão Impossível"},
    {"id": "johnwick",   "label_key": None, "label": "John Wick"},
    {"id": "bourne",     "label_key": None, "label": "Jason Bourne"},
    {"id": "velozesefuriosos", "label_key": None, "label": "Velozes & Furiosos"},
    {"id": "indianajones", "label_key": None, "label": "Indiana Jones"},
    {"id": "jurassic",   "label_key": None, "label": "Jurassic Park & World"},
    {"id": "planetadosmacacos", "label_key": None, "label": "Planeta dos Macacos"},
    {"id": "exterminador", "label_key": None, "label": "O Exterminador do Futuro"},
    {"id": "madmax",     "label_key": None, "label": "Mad Max"},
    {"id": "rambo",      "label_key": None, "label": "Rambo"},
    {"id": "rocky",      "label_key": None, "label": "Rocky & Creed"},
    {"id": "senhordosaneis", "label_key": None, "label": "Senhor dos Anéis & O Hobbit"},
    {"id": "startrek",   "label_key": None, "label": "Star Trek"},
    {"id": "matrix",     "label_key": None, "label": "Matrix"},
    {"id": "harrypotter", "label_key": None, "label": "Harry Potter"},
    {"id": "animaisfantasticos", "label_key": None, "label": "Animais Fantásticos"},
    {"id": "narnia",     "label_key": None, "label": "As Crônicas de Nárnia"},
    {"id": "jogosvorazes", "label_key": None, "label": "Jogos Vorazes"},
    {"id": "divergente", "label_key": None, "label": "Divergente"},
    {"id": "shrek",      "label_key": None, "label": "Shrek & Gato de Botas"},
    {"id": "meumalvadofavorito", "label_key": None, "label": "Meu Malvado Favorito"},
    {"id": "transformers", "label_key": None, "label": "Transformers"},
    {"id": "alien",      "label_key": None, "label": "Alien (Ordem Cronológica)"},
    {"id": "predador",   "label_key": None, "label": "Predador"},
    {"id": "sextafeira13", "label_key": None, "label": "Sexta-Feira 13"},
    {"id": "horadopesadelo", "label_key": None, "label": "A Hora do Pesadelo"},
    {"id": "poderosochefao", "label_key": None, "label": "O Poderoso Chefão"},
    {"id": "piratasdocaribe", "label_key": None, "label": "Piratas do Caribe"},
    {"id": "sherlockholmes", "label_key": None, "label": "Sherlock Holmes & Enola"},
    {"id": "oscar2026",  "label_key": "categories.oscar", "label": "Oscar 2026: Melhor Filme"},
    {"id": "oscar2026_intl", "label_key": None, "label": "Oscar 2026: Filme Internacional"},
    {"id": "cinemanacional", "label_key": None, "label": "🇧🇷 Cinema Brasileiro"},
    {"id": "nolan",      "label_key": "categories.nolan"},
    {"id": "tarantino",  "label_key": None, "label": "Quentin Tarantino"},
    {"id": "halloween",  "label_key": "categories.terror", "label": "Maratona Terror Halloween"},
    {"id": "comedias_br", "label_key": None, "label": "Comédias Brasileiras"},
    {"id": "dragonball_series", "label_key": None, "label": "Dragon Ball (Séries)"},
    {"id": "starwars_series", "label_key": None, "label": "Star Wars (Séries)"},
    {"id": "theboys", "label_key": None, "label": "The Boys Universe"},
    {"id": "gameofthrones", "label_key": None, "label": "Game of Thrones"},
    {"id": "walkingdead", "label_key": None, "label": "The Walking Dead Universe"},
]

# IDs padrão habilitados para novos usuários (todas as categorias)
DEFAULT_CATEGORIES = [cat["id"] for cat in AVAILABLE_CATEGORIES]

# --- Cache calculado uma única vez na inicialização do servidor ---
SAGA_NAMES_SORTED = [dados["name"] for dados in CATALOGS.values()]
CATALOG_BY_NAME = {dados["name"]: dados for dados in CATALOGS.values()}
ALL_SAGAS = list(CATALOGS.values())

ANIM_NAMES_SORTED = [dados["name"] for dados in ANIMATIONS.values()]
ANIM_BY_NAME = {dados["name"]: dados for dados in ANIMATIONS.values()}
ALL_ANIM = list(ANIMATIONS.values())

SERIES_NAMES_SORTED = [dados["name"] for dados in SERIES.values()]
SERIES_BY_NAME = {dados["name"]: dados for dados in SERIES.values()}
ALL_SERIES = list(SERIES.values())

EXTRA_NAME = "genre"

# Catálogo de destaque dinâmico (carregado do JSON)
_DESTAQUE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'destaque.json')
try:
    with open(_DESTAQUE_PATH, encoding='utf-8') as f:
        DESTAQUE = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    DESTAQUE = {"id": "destaque", "title": "⭐ Em Destaque", "items": []}


def respond_with(data):
    """Retorna respostas no formato JSON requerido pelo Stremio com headers CORS."""
    response = jsonify(data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


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
            "name": t(lang, "catalog_series") if lang == "en-us" else "📺 Maratonas de Séries",
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
        "id": "br.cinemaratona.addon",
        "version": "2.0.0",
        "name": t(lang, "addon_name"),
        "description": t(lang, "addon_description"),
        "logo": "https://raw.githubusercontent.com/muriloruass/cinemaratona-br/main/CineMaratonaLogo.png",
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
    categories_html = ""
    for cat in AVAILABLE_CATEGORIES:
        label = cat.get("label") or cat["id"]
        cat_id = cat["id"]
        categories_html += f"""
        <div class="category-item">
          <label>
            <input type="checkbox" value="{cat_id}" checked>
            <span>{label}</span>
          </label>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CineMaratona BR — Configurar Addon</title>
  <meta name="description" content="Configure o CineMaratona BR: escolha idioma e categorias de sagas e maratonas de filmes para Stremio.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0a0a0f;
      --surface: #13131a;
      --surface2: #1c1c26;
      --border: #2a2a3a;
      --accent: #e63946;
      --accent2: #ff6b6b;
      --blue: #4361ee;
      --blue-hover: #3a56d4;
      --text: #f0f0f5;
      --text-muted: #8888a8;
      --radius: 10px;
      --radius-sm: 6px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      padding: 0;
    }}
    header {{
      background: linear-gradient(135deg, #0d0d14 0%, #1a0a0f 100%);
      border-bottom: 1px solid var(--border);
      padding: 28px 24px;
      text-align: center;
    }}
    header h1 {{
      font-size: 2rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 6px;
    }}
    header p {{
      color: var(--text-muted);
      font-size: 0.95rem;
    }}
    .container {{
      max-width: 680px;
      margin: 0 auto;
      padding: 32px 20px 60px;
    }}
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 20px;
    }}
    .card h2 {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card h2::before {{
      content: '';
      display: inline-block;
      width: 3px;
      height: 16px;
      background: var(--accent);
      border-radius: 2px;
    }}
    /* Language select */
    select {{
      width: 100%;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text);
      padding: 12px 16px;
      font-family: inherit;
      font-size: 1rem;
      cursor: pointer;
      appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%238888a8' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 14px center;
      transition: border-color 0.2s;
    }}
    select:focus {{
      outline: none;
      border-color: var(--accent);
    }}
    /* Category grid */
    .categories-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}
    @media (max-width: 480px) {{
      .categories-grid {{ grid-template-columns: 1fr; }}
    }}
    .category-item label {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 14px;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: border-color 0.2s, background 0.2s;
      user-select: none;
    }}
    .category-item label:hover {{
      border-color: var(--accent);
      background: #1e1218;
    }}
    .category-item input[type=checkbox] {{
      accent-color: var(--accent);
      width: 16px;
      height: 16px;
      cursor: pointer;
      flex-shrink: 0;
    }}
    .category-item span {{
      font-size: 0.9rem;
      color: var(--text);
    }}
    /* Bulk actions */
    .bulk-actions {{
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
    }}
    .btn-text {{
      background: none;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.82rem;
      cursor: pointer;
      transition: border-color 0.2s, color 0.2s;
    }}
    .btn-text:hover {{
      border-color: var(--accent);
      color: var(--text);
    }}
    /* Generate button */
    .btn-generate {{
      width: 100%;
      background: linear-gradient(135deg, var(--accent), #c1121f);
      color: white;
      border: none;
      padding: 15px 24px;
      border-radius: var(--radius);
      font-family: inherit;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.2s, transform 0.1s;
      margin-top: 8px;
    }}
    .btn-generate:hover {{ opacity: 0.92; transform: translateY(-1px); }}
    .btn-generate:active {{ transform: translateY(0); }}
    /* Result box */
    #result-box {{
      display: none;
      margin-top: 20px;
    }}
    .install-url {{
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      font-family: 'Courier New', monospace;
      font-size: 0.82rem;
      color: #a8d8ff;
      word-break: break-all;
      line-height: 1.5;
    }}
    .result-actions {{
      display: flex;
      gap: 10px;
      margin-top: 12px;
    }}
    .btn-copy {{
      flex: 1;
      background: var(--surface2);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 12px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.9rem;
      cursor: pointer;
      transition: border-color 0.2s;
    }}
    .btn-copy:hover {{ border-color: var(--blue); }}
    .btn-install {{
      flex: 1;
      background: var(--blue);
      color: white;
      border: none;
      padding: 12px;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .btn-install:hover {{ background: var(--blue-hover); }}
    .note {{
      margin-top: 12px;
      font-size: 0.8rem;
      color: var(--text-muted);
      text-align: center;
    }}
    .badge-v2 {{
      display: inline-block;
      background: linear-gradient(135deg, var(--blue), #7b2fbe);
      color: white;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 20px;
      margin-left: 8px;
      vertical-align: middle;
      letter-spacing: 0.05em;
    }}
  </style>
</head>
<body>
  <header>
    <h1>🎬 CineMaratona BR <span class="badge-v2">v2.0</span></h1>
    <p>Sagas e Maratonas organizadas cronologicamente para Stremio</p>
  </header>

  <div class="container">

    <div class="card">
      <h2>Idioma</h2>
      <select id="lang" aria-label="Selecionar idioma">
        <option value="pt-br">🇧🇷 Português (BR)</option>
        <option value="en-us">🇺🇸 English (US)</option>
        <option value="es">🇪🇸 Español</option>
      </select>
    </div>

    <div class="card">
      <h2>Categorias</h2>
      <div class="bulk-actions">
        <button class="btn-text" onclick="selectAll()">Selecionar todas</button>
        <button class="btn-text" onclick="deselectAll()">Desmarcar todas</button>
      </div>
      <div class="categories-grid" id="categories">
        {categories_html}
      </div>
    </div>

    <button class="btn-generate" id="btn-generate" onclick="generateLink()">
      🔗 Gerar Link de Instalação
    </button>

    <div id="result-box">
      <div class="card">
        <h2>Seu Link Personalizado</h2>
        <div class="install-url" id="link-text"></div>
        <div class="result-actions">
          <button class="btn-copy" id="btn-copy" onclick="copyLink()">📋 Copiar</button>
          <button class="btn-install" onclick="installStremio()">▶ Instalar no Stremio</button>
        </div>
        <p class="note">
          Ou vá em Stremio → Addons → Community Addons → cole a URL acima
        </p>
      </div>
    </div>

  </div>

  <script>
    function selectAll() {{
      document.querySelectorAll('#categories input[type=checkbox]').forEach(cb => cb.checked = true);
    }}
    function deselectAll() {{
      document.querySelectorAll('#categories input[type=checkbox]').forEach(cb => cb.checked = false);
    }}
    function generateLink() {{
      const lang = document.getElementById('lang').value;
      const categories = [...document.querySelectorAll('#categories input:checked')].map(el => el.value);
      if (categories.length === 0) {{
        alert('Selecione ao menos uma categoria!');
        return;
      }}
      const config = {{ lang, categories }};
      const b64 = btoa(unescape(encodeURIComponent(JSON.stringify(config))));
      const baseUrl = '{BASE_URL}';
      const link = baseUrl + '/' + b64 + '/manifest.json';
      document.getElementById('link-text').textContent = link;
      const box = document.getElementById('result-box');
      box.style.display = 'block';
      box.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
    function copyLink() {{
      const link = document.getElementById('link-text').textContent;
      navigator.clipboard.writeText(link).then(() => {{
        const btn = document.getElementById('btn-copy');
        btn.textContent = '✅ Copiado!';
        setTimeout(() => {{ btn.textContent = '📋 Copiar'; }}, 2500);
      }});
    }}
    function installStremio() {{
      const link = document.getElementById('link-text').textContent;
      const stremioUrl = 'stremio://' + link.replace('https://', '');
      window.open(stremioUrl);
    }}
  </script>
</body>
</html>"""

    from flask import Response
    return Response(html, mimetype='text/html')


# ─── Catálogo de Destaque ─────────────────────────────────────────────────────

@app.route("/catalog/movie/cine_destaque.json")
@app.route("/<config_b64>/catalog/movie/cine_destaque.json")
def addon_catalog_destaque(config_b64=None):
    """Retorna o catálogo de destaque da semana."""
    metas = []
    for filme in DESTAQUE.get("items", []):
        metas.append({
            "id": filme["id"],
            "type": "movie",
            "name": filme["name"],
            "poster": POSTER_METAHUB_URL.format(filme["id"])
        })
    return respond_with({"metas": metas})


# ─── Catálogos principais (padrão — sem saga selecionada) ────────────────────

@app.route("/catalog/<media_type>/<catalog_id>.json")
def addon_catalog_default(media_type, catalog_id):
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

    metas = []
    for filme in lista_filmes:
        metas.append({
            "id": filme["id"],
            "type": media_type,
            "name": filme["name"],
            "poster": POSTER_METAHUB_URL.format(filme["id"])
        })


    return respond_with({"metas": metas})


@app.route("/<config_b64>/catalog/<media_type>/<catalog_id>.json")
def addon_catalog_default_configured(config_b64, media_type, catalog_id):
    """Versão com userdata do fallback de catálogo."""
    return addon_catalog_default(media_type, catalog_id)


# ─── Catálogos com saga selecionada / busca ─────────────────────────────────

@app.route("/catalog/<media_type>/<catalog_id>/<extra_str>.json")
def addon_catalog_com_extra(media_type, catalog_id, extra_str):
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

    metas = []
    for item in lista_itens:
        metas.append({
            "id": item["id"],
            "type": media_type,
            "name": item["name"],
            "poster": POSTER_METAHUB_URL.format(item["id"])
        })

    return respond_with({"metas": metas})


@app.route("/<config_b64>/catalog/<media_type>/<catalog_id>/<extra_str>.json")
def addon_catalog_com_extra_configured(config_b64, media_type, catalog_id, extra_str):
    """Versão com userdata do catálogo com saga selecionada ou busca."""
    return addon_catalog_com_extra(media_type, catalog_id, extra_str)


# ─── Meta stub ────────────────────────────────────────────────────────────────

@app.route("/meta/<media_type>/<imdb_id>.json")
@app.route("/<config_b64>/meta/<media_type>/<imdb_id>.json")
def addon_meta(media_type, imdb_id, config_b64=None):
    """
    Stub de meta para evitar erro vermelho na interface do Stremio.
    O Stremio usa Cinemeta internamente para dados completos.
    """
    if media_type not in ["movie", "series"]:
        media_type = "movie"

    return respond_with({
        "meta": {
            "id": imdb_id,
            "type": media_type,
            "poster": POSTER_METAHUB_URL.format(imdb_id)
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
