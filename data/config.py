# data/config.py — Configurações centrais do CineMaratona BR
#
# Todas as constantes de ambiente e metadados do addon vivem aqui.
# Para sobrescrever em produção, defina as variáveis de ambiente correspondentes.

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env caso exista (para dev local)
load_dotenv()

# ── Metadados do Addon ────────────────────────────────────────────────────────
ADDON_ID = "br.cinemaratona.addon"
ADDON_VERSION = "2.1.0"

# ── URLs ──────────────────────────────────────────────────────────────────────
# BASE_URL pode ser sobrescrita por variável de ambiente (útil em staging/dev)
BASE_URL = os.environ.get("BASE_URL", "https://cinemaratona-br.vercel.app")

POSTER_METAHUB_URL = "https://images.metahub.space/poster/medium/{}/img"

LOGO_URL = (
    "https://raw.githubusercontent.com/muriloruass/cinemaratona-br/main/CineMaratonaLogo.png"
)

# Nome do campo 'extra' usado para filtrar gêneros/sagas no Stremio
EXTRA_NAME = "genre"

# ── Categorias disponíveis ────────────────────────────────────────────────────
# Cada entrada contém:
#   id        — chave que bate com as chaves de catalogs.py (CATALOGS/SERIES)
#   label     — nome exibido na página /configure
#   label_key — chave i18n opcional (se None, usa label diretamente)
AVAILABLE_CATEGORIES = [
    # 🎬 Sagas de Filmes (Mainstream)
    {"id": "marvel",             "label": "Universo Marvel (MCU)",          "label_key": "categories.marvel"},
    {"id": "starwars",           "label": "Star Wars",                      "label_key": None},
    {"id": "harrypotter",        "label": "Harry Potter",                   "label_key": None},
    {"id": "senhordosaneis",     "label": "Senhor dos Anéis & O Hobbit",   "label_key": None},
    {"id": "007",                "label": "007 – James Bond",               "label_key": "categories.007"},
    {"id": "missaoimpossivel",   "label": "Missão Impossível",              "label_key": None},
    {"id": "johnwick",           "label": "John Wick",                      "label_key": None},
    {"id": "velozesefuriosos",   "label": "Velozes & Furiosos",             "label_key": None},
    {"id": "jurassic",           "label": "Jurassic Park & World",          "label_key": None},
    {"id": "rocky",              "label": "Rocky & Creed",                  "label_key": None},
    {"id": "matrix",             "label": "Matrix",                         "label_key": None},
    {"id": "piratasdocaribe",    "label": "Piratas do Caribe",              "label_key": None},
    {"id": "transformers",       "label": "Transformers",                   "label_key": None},

    # 📺 Sagas de Séries
    {"id": "dragonball_series",  "label": "Dragon Ball (Séries)",           "label_key": None},
    {"id": "starwars_series",    "label": "Star Wars (Séries)",             "label_key": None},
    {"id": "theboys",            "label": "The Boys Universe",              "label_key": None},
    {"id": "gameofthrones",      "label": "Game of Thrones",                "label_key": None},
    {"id": "walkingdead",        "label": "The Walking Dead Universe",      "label_key": None},

    # ✨ Sagas de Animações
    {"id": "disney_filmes",      "label": "Disney — Filmes Avulsos",        "label_key": None},
    {"id": "pixar_filmes",       "label": "Pixar — Filmes Avulsos",         "label_key": None},
    {"id": "toystory_anim",      "label": "Toy Story",                      "label_key": None},
    {"id": "procurandonemo",     "label": "Procurando Nemo & Dory",         "label_key": None},
    {"id": "monstros",           "label": "Monstros S.A.",                  "label_key": None},
    {"id": "osincrivel",         "label": "Os Incríveis",                   "label_key": None},
    {"id": "carros",             "label": "Carros",                         "label_key": None},
    {"id": "inside_out",         "label": "Divertida Mente",                "label_key": None},
    {"id": "leao",               "label": "O Rei Leão",                     "label_key": None},
    {"id": "frozen",             "label": "Frozen",                         "label_key": None},
    {"id": "moana",              "label": "Moana",                          "label_key": None},
    {"id": "zootopia",           "label": "Zootopia",                       "label_key": None},
    {"id": "liloestitch",        "label": "Lilo & Stitch",                  "label_key": None},
    {"id": "wreck_it_ralph",     "label": "Detona Ralph",                   "label_key": None},
    {"id": "mulan_disney",       "label": "Mulan (Animação)",               "label_key": None},
    {"id": "aladdin_disney",     "label": "Aladdin (Animação)",             "label_key": None},
    {"id": "cinderela_disney",   "label": "Cinderela (Animação)",           "label_key": None},
    {"id": "bela_fera",          "label": "A Bela e a Fera",                "label_key": None},
    {"id": "pequena_sereia",     "label": "A Pequena Sereia",                "label_key": None},
    {"id": "dumbo",              "label": "Dumbo",                          "label_key": None},
    {"id": "peter_pan",          "label": "Peter Pan",                      "label_key": None},
    {"id": "pinoquio",           "label": "Pinóquio",                       "label_key": None},
    {"id": "alicenopaisdasmaravilhas", "label": "Alice no País das Maravilhas", "label_key": None},
    {"id": "malefica",           "label": "Malévola",                       "label_key": None},

    # ⭐ Coleções Especiais
    {"id": "nolan",              "label": "Melhor de Christopher Nolan",    "label_key": "categories.nolan"},
    {"id": "tarantino",          "label": "Melhor de Quentin Tarantino",    "label_key": None},
    {"id": "cinemanacional",     "label": "🇧🇷 Cinema Brasileiro",           "label_key": None},
    {"id": "halloween",          "label": "Maratona Terror Halloween",      "label_key": "categories.terror"},
    {"id": "comedias_br",        "label": "Comédias Brasileiras",           "label_key": None},
    {"id": "alien",              "label": "Alien (Ordem Cronológica)",      "label_key": None},
    {"id": "predador",           "label": "Predador",                       "label_key": None},
    {"id": "xmen",               "label": "X-Men",                          "label_key": None},
    {"id": "bourne",             "label": "Jason Bourne",                   "label_key": None},
    {"id": "indianajones",       "label": "Indiana Jones",                  "label_key": None},
    {"id": "planetadosmacacos",  "label": "Planeta dos Macacos",            "label_key": None},
    {"id": "exterminador",       "label": "O Exterminador do Futuro",       "label_key": None},
    {"id": "madmax",             "label": "Mad Max",                        "label_key": None},
    {"id": "rambo",              "label": "Rambo",                          "label_key": None},
    {"id": "narnia",             "label": "As Crônicas de Nárnia",          "label_key": None},
    {"id": "jogosvorazes",       "label": "Jogos Vorazes",                  "label_key": None},
    {"id": "divergente",         "label": "Divergente",                     "label_key": None},
    {"id": "shrek",              "label": "Shrek & Gato de Botas",          "label_key": None},
    {"id": "meumalvadofavorito", "label": "Meu Malvado Favorito",           "label_key": None},
    {"id": "sextafeira13",       "label": "Sexta-Feira 13",                 "label_key": None},
    {"id": "horadopesadelo",     "label": "A Hora do Pesadelo",             "label_key": None},
    {"id": "poderosochefao",     "label": "O Poderoso Chefão",              "label_key": None},
    {"id": "sherlockholmes",     "label": "Sherlock Holmes & Enola",        "label_key": None},
    {"id": "animaisfantasticos", "label": "Animais Fantásticos",            "label_key": None},
]

# IDs habilitados por padrão para novos usuários (todas as categorias)
DEFAULT_CATEGORIES: list[str] = [cat["id"] for cat in AVAILABLE_CATEGORIES]
