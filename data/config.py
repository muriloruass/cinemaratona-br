# data/config.py — Configurações centrais do CineMaratona BR
#
# Todas as constantes de ambiente e metadados do addon vivem aqui.
# Para sobrescrever em produção, defina as variáveis de ambiente correspondentes.

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env caso exista (para dev local)
load_dotenv()

# ── Metadados do Addon ────────────────────────────────────────────────────────
ADDON_ID = "br.cinemaratona.addon.movies"
ADDON_VERSION = "2.5.0"

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
    {"id": "marvel",             "label": "Universo Marvel (MCU)",          "label_key": "catalog_ids.marvel"},
    {"id": "starwars",           "label": "Star Wars",                      "label_key": "catalog_ids.starwars"},
    {"id": "harrypotter",        "label": "Harry Potter",                   "label_key": "catalog_ids.harrypotter"},
    {"id": "senhordosaneis",     "label": "Senhor dos Anéis & O Hobbit",   "label_key": "catalog_ids.senhordosaneis"},
    {"id": "007",                "label": "007 — James Bond",               "label_key": "catalog_ids.007"},
    {"id": "missaoimpossivel",   "label": "Missão Impossível",              "label_key": "catalog_ids.missaoimpossivel"},
    {"id": "johnwick",           "label": "John Wick",                      "label_key": "catalog_ids.johnwick"},
    {"id": "velozesefuriosos",   "label": "Velozes & Furiosos",             "label_key": "catalog_ids.velozesefuriosos"},
    {"id": "jurassic",           "label": "Jurassic Park & World",          "label_key": "catalog_ids.jurassic"},
    {"id": "rocky",              "label": "Rocky & Creed",                  "label_key": "catalog_ids.rocky"},
    {"id": "matrix",             "label": "Matrix",                         "label_key": "catalog_ids.matrix"},
    {"id": "piratasdocaribe",    "label": "Piratas do Caribe",              "label_key": "catalog_ids.piratasdocaribe"},
    {"id": "transformers",       "label": "Transformers",                   "label_key": "catalog_ids.transformers"},
    {"id": "alien",              "label": "Alien (Ordem Cronológica)",      "label_key": "catalog_ids.alien"},
    {"id": "xmen",               "label": "X-Men",                          "label_key": "catalog_ids.xmen"},
    {"id": "indianajones",       "label": "Indiana Jones",                  "label_key": "catalog_ids.indianajones"},
    {"id": "planetadosmacacos",  "label": "Planeta dos Macacos",            "label_key": "catalog_ids.planetadosmacacos"},
    {"id": "rambo",              "label": "Rambo",                          "label_key": "catalog_ids.rambo"},
    {"id": "narnia",             "label": "As Crônicas de Nárnia",          "label_key": "catalog_ids.narnia"},
    {"id": "poderosochefao",     "label": "O Poderoso Chefão",              "label_key": "catalog_ids.poderosochefao"},
    {"id": "halloween",          "label": "Halloween",                      "label_key": "catalog_ids.halloween"},
    {"id": "horadopesadelo",     "label": "A Hora do Pesadelo",             "label_key": "catalog_ids.horadopesadelo"},
    {"id": "sextafeira13",       "label": "Sexta-Feira 13",                 "label_key": "catalog_ids.sextafeira13"},
    {"id": "panico",             "label": "Pânico",                         "label_key": "catalog_ids.panico"},
    {"id": "premonicao",         "label": "Premonição",                     "label_key": "catalog_ids.premonicao"},
    {"id": "invocacaodomal",     "label": "Universo Invocação do Mal",      "label_key": "catalog_ids.invocacaodomal"},

    # ✨ Sagas de Animações
    {"id": "disney_filmes",      "label": "Disney — Filmes Avulsos",        "label_key": "catalog_ids.disney_filmes"},
    {"id": "pixar_filmes",       "label": "Pixar — Filmes Avulsos",         "label_key": "catalog_ids.pixar_filmes"},
    {"id": "toystory_anim",      "label": "Toy Story",                      "label_key": "catalog_ids.toystory_anim"},
    {"id": "procurandonemo",     "label": "Procurando Nemo & Dory",         "label_key": "catalog_ids.procurandonemo"},
    {"id": "monstros",           "label": "Monstros S.A.",                  "label_key": "catalog_ids.monstros"},
    {"id": "osincrivel",         "label": "Os Incríveis",                   "label_key": "catalog_ids.osincrivel"},
    {"id": "carros",             "label": "Carros",                         "label_key": "catalog_ids.carros"},
    {"id": "inside_out",         "label": "Divertida Mente",                "label_key": "catalog_ids.inside_out"},
    {"id": "leao",               "label": "O Rei Leão",                     "label_key": "catalog_ids.leao"},
    {"id": "frozen",             "label": "Frozen",                         "label_key": "catalog_ids.frozen"},
    {"id": "moana",              "label": "Moana",                          "label_key": "catalog_ids.moana"},
    {"id": "zootopia",           "label": "Zootopia",                       "label_key": "catalog_ids.zootopia"},
    {"id": "liloestitch",        "label": "Lilo & Stitch",                  "label_key": "catalog_ids.liloestitch"},
    {"id": "wreck_it_ralph",     "label": "Detona Ralph",                   "label_key": "catalog_ids.wreck_it_ralph"},
    {"id": "mulan_disney",       "label": "Mulan (Animação)",               "label_key": "catalog_ids.mulan_disney"},
    {"id": "aladdin_disney",     "label": "Aladdin (Animação)",             "label_key": "catalog_ids.aladdin_disney"},
    {"id": "cinderela_disney",   "label": "Cinderela (Animação)",           "label_key": "catalog_ids.cinderela_disney"},
    {"id": "bela_fera",          "label": "A Bela e a Fera",                "label_key": "catalog_ids.bela_fera"},
    {"id": "pequena_sereia",     "label": "A Pequena Sereia",               "label_key": "catalog_ids.pequena_sereia"},
    {"id": "dumbo",              "label": "Dumbo",                          "label_key": "catalog_ids.dumbo"},
    {"id": "peter_pan",          "label": "Peter Pan",                      "label_key": "catalog_ids.peter_pan"},
    {"id": "pinoquio",           "label": "Pinóquio",                       "label_key": "catalog_ids.pinoquio"},
    {"id": "alicenopaisdasmaravilhas", "label": "Alice no País das Maravilhas", "label_key": "catalog_ids.alicenopaisdasmaravilhas"},
    {"id": "malefica",           "label": "Malévola",                       "label_key": "catalog_ids.malefica"},
    {"id": "shrek",              "label": "Shrek & Gato de Botas",          "label_key": "catalog_ids.shrek"},
    {"id": "meumalvadofavorito", "label": "Meu Malvado Favorito",           "label_key": "catalog_ids.meumalvadofavorito"},

    # ⭐ Coleções Especiais
    {"id": "nolan",              "label": "Melhor de Christopher Nolan",    "label_key": "catalog_ids.nolan"},
    {"id": "tarantino",          "label": "Melhor de Quentin Tarantino",    "label_key": "catalog_ids.tarantino"},
    {"id": "cinemanacional",     "label": "Cinema Brasileiro",              "label_key": "catalog_ids.cinemanacional"},
    {"id": "terror_avulsos",     "label": "Terror — Filmes Avulsos",        "label_key": "catalog_ids.terror_avulsos"},
    {"id": "predador",           "label": "Predador",                       "label_key": "catalog_ids.predador"},
    {"id": "bourne",             "label": "Jason Bourne",                   "label_key": "catalog_ids.bourne"},
    {"id": "exterminador",       "label": "O Exterminador do Futuro",       "label_key": "catalog_ids.exterminador"},
    {"id": "madmax",             "label": "Mad Max",                        "label_key": "catalog_ids.madmax"},
    {"id": "jogosvorazes",       "label": "Jogos Vorazes",                  "label_key": "catalog_ids.jogosvorazes"},
    {"id": "divergente",         "label": "Divergente",                     "label_key": "catalog_ids.divergente"},
    {"id": "sherlockholmes",     "label": "Sherlock Holmes & Enola",        "label_key": "catalog_ids.sherlockholmes"},
    {"id": "animaisfantasticos", "label": "Animais Fantásticos",            "label_key": "catalog_ids.animaisfantasticos"},
]

# IDs habilitados por padrão para novos usuários (todas as categorias)
DEFAULT_CATEGORIES: list[str] = [cat["id"] for cat in AVAILABLE_CATEGORIES]
