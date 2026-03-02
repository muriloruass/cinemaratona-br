from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from catalogs import CATALOGS, ANIMATIONS
import urllib.parse
import random

app = Flask(__name__)
# Habilitar CORS para permitir que o Stremio se comunique com nossa API sem bloqueios
CORS(app)

# URL padrão e confiável para obter posters do Stremio via ID do IMDb
POSTER_METAHUB_URL = "https://images.metahub.space/poster/medium/{}/img"

# --- Cache calculado uma única vez na inicialização do servidor ---
# Lista ordenada de nomes de sagas para o manifest (evita recalcular a cada request)
SAGA_NAMES_SORTED = [dados["name"] for dados in CATALOGS.values()]

# Índice de sagas por nome para busca O(1) (evita loop linear a cada seleção de gênero)
CATALOG_BY_NAME = {dados["name"]: dados for dados in CATALOGS.values()}

# Lista de todas as sagas para o sorteio aleatório da tela inicial
ALL_SAGAS = list(CATALOGS.values())

# Cache equivalente para o catálogo de Animações Disney & Pixar
ANIM_NAMES_SORTED = [dados["name"] for dados in ANIMATIONS.values()]
ANIM_BY_NAME = {dados["name"]: dados for dados in ANIMATIONS.values()}
ALL_ANIM = list(ANIMATIONS.values())

# Nome do campo extra — usa 'genre' (padrão oficial Stremio) para garantir compatibilidade de URL
EXTRA_NAME = "genre"

def respond_with(data):
    """
    Função utilitária para retornar as respostas no formato JSON requerido pelo Stremio,
    garantindo que os cabeçalhos de CORS e acesso permitam qualquer origem.
    """
    response = jsonify(data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

@app.route("/")
def index():
    """
    Rota inicial de boas vindas para verificar rapidamente se o servidor está online.
    """
    return "CineMaratona BR 🎬 Stremio Addon está rodando! Instale no Stremio usando a rota /manifest.json"

@app.route("/ping")
def ping():
    """Endpoint leve para manter o servidor acordado via UptimeRobot ou similar."""
    return "pong", 200

@app.route("/cinemaratonaBR.png")
def addon_logo():
    """Rota para servir a logo oficial do Addon diretamente, sem depender de sites externos."""
    return send_file("cinemaratonaBR.png", mimetype="image/png")

@app.route("/manifest.json")
def addon_manifest():
    """
    Gera o manifesto que o Stremio lê para instalar e entender nosso addon.
    Ele cria UM catálogo único na aba Filmes chamado "Sagas e Maratonas" 
    e usa as chaves do CATALOGS como um menu 'extra' no topo do catálogo.
    """
    # Manifesto usa SAGA_NAMES_SORTED pré-computado na inicialização

    manifest = {
        "id": "br.cinemaratona.addon",
        "version": "1.1.5",
        "name": "CineMaratona BR 🎬",
        "description": "Sagas e Maratonas organizadas cronologicamente com metadados em PT-BR para Stremio. Escolha suas franquias e listas favoritas usando o filtro superior!",
        "logo": "https://raw.githubusercontent.com/muriloruass/cinemaratona-br/main/cinemaratonaBR.png",
        "resources": ["catalog"],
        "types": ["movie"],
        "catalogs": [
            {
                "type": "movie",
                "id": "cine_maratona",
                "name": "Sagas e Maratonas",
                "extra": [
                    {
                        "name": EXTRA_NAME,
                        "isRequired": False,
                        "options": SAGA_NAMES_SORTED
                    }
                ],
                "extraSupported": [EXTRA_NAME]
            },
            {
                "type": "movie",
                "id": "cine_animacoes",
                "name": "Animações Disney & Pixar",
                "extra": [
                    {
                        "name": EXTRA_NAME,
                        "isRequired": False,
                        "options": ANIM_NAMES_SORTED
                    }
                ],
                "extraSupported": [EXTRA_NAME]
            }
        ],
        "stremioAddonsConfig": {
            "issuer": "https://stremio-addons.net",
            "signature": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..01bufPwIGEuO8R9okmf43g.eqmi2c8kR0SG7OAWfGNvVMgT8JTy8BPTtN-S8FatjxUoh0sXZxiEAXRMYu3hfa68kO_WMHtkEw_kYtHCpbJP1rMcHXVpj5WWi1o0kGtmIapWiYQOH4MPZcut1bfS0QfM.YT0FeLMuRummbV3hBIqeYw"
        }
    }
    
    return respond_with(manifest)

@app.route("/catalog/<media_type>/<catalog_id>.json")
def addon_catalog_default(media_type, catalog_id):
    """
    Esta rota de fallback é acionada caso o Stremio abra a aba pela primeira vez sem um <saga_param> na URL.
    Exibe uma seleção aleatória de sagas do catálogo correspondente.
    """
    if media_type != "movie":
        return respond_with({"metas": []})

    if catalog_id == "cine_maratona":
        pool = ALL_SAGAS
    elif catalog_id == "cine_animacoes":
        pool = ALL_ANIM
    else:
        return respond_with({"metas": []})

    sagas_aleatorias = random.sample(pool, min(15, len(pool)))
    lista_filmes = [saga["items"][0] for saga in sagas_aleatorias if saga["items"]]

    metas = []
    for filme in lista_filmes:
        metas.append({
            "id": filme["id"],
            "type": "movie",
            "name": filme["name"],
            "poster": POSTER_METAHUB_URL.format(filme["id"])
        })

    return respond_with({"metas": metas})

@app.route("/catalog/<media_type>/<catalog_id>/genre=<saga_param>.json")
def addon_catalog_com_extra(media_type, catalog_id, saga_param):
    """
    Rota chamada pelo Stremio quando o usuário seleciona uma saga específica no menu.
    Funciona tanto para 'cine_maratona' quanto para 'cine_animacoes'.
    """
    if media_type != "movie":
        return respond_with({"metas": []})

    saga_selecionada = urllib.parse.unquote(saga_param)

    if catalog_id == "cine_maratona":
        saga = CATALOG_BY_NAME.get(saga_selecionada)
    elif catalog_id == "cine_animacoes":
        saga = ANIM_BY_NAME.get(saga_selecionada)
    else:
        return respond_with({"metas": []})

    lista_filmes = saga["items"] if saga else []

    metas = []
    for filme in lista_filmes:
        metas.append({
            "id": filme["id"],
            "type": "movie",
            "name": filme["name"],
            "poster": POSTER_METAHUB_URL.format(filme["id"])
        })

    return respond_with({"metas": metas})

@app.route("/meta/movie/<imdb_id>.json")
def addon_meta(imdb_id):
    """
    Rota stub (simples) para detalhes do meta. Eventualmente o Stremio pode chamar essa rota
    se não usar o seu Cinemeta interno, retornamos o mínimo para evitar erro vermelho na interface.
    """
    return respond_with({
        "meta": {
            "id": imdb_id,
            "type": "movie",
            "poster": POSTER_METAHUB_URL.format(imdb_id)
        }
    })

if __name__ == "__main__":
    # Inicia localmente na porta 7000 como exigido, com modo debug para desenvolvimento
    app.run(host="0.0.0.0", port=7000, debug=True)
