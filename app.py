from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from catalogs import CATALOGS
import urllib.parse

app = Flask(__name__)
# Habilitar CORS para permitir que o Stremio se comunique com nossa API sem bloqueios
CORS(app)

# URL padrão e confiável para obter posters do Stremio via ID do IMDb
POSTER_METAHUB_URL = "https://images.metahub.space/poster/medium/{}/img"

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

@app.route("/cinemaratona.png")
def addon_logo():
    """Rota para servir a logo oficial do Addon diretamente, sem depender de sites externos."""
    return send_file("cinemaratona.png", mimetype="image/png")

@app.route("/manifest.json")
def addon_manifest():
    """
    Gera o manifesto que o Stremio lê para instalar e entender nosso addon.
    Ele cria UM catálogo único na aba Filmes chamado "Sagas e Maratonas" 
    e usa as chaves do CATALOGS como um menu 'extra' no topo do catálogo.
    """
    # Ordenar os nomes das listas alfabeticamente
    saga_names = [dados["name"] for dados in CATALOGS.values()]
    saga_names.sort()

    manifest = {
        "id": "br.cinemaratona.addon",
        "version": "1.0.1",
        "name": "CineMaratona BR 🎬",
        "description": "Sagas e Maratonas organizadas cronologicamente com metadados em PT-BR para Stremio. Escolha suas franquias e listas favoritas usando o filtro superior!",
        "logo": "https://raw.githubusercontent.com/muriloruass/cinemaratona-br/main/cinemaratona.png",
        "resources": ["catalog"],
        "types": ["movie"],
        "catalogs": [
            {
                "type": "movie",
                "id": "cine_maratona",
                "name": "Sagas e Maratonas",
                "extra": [
                    {
                        "name": "genre",
                        "isRequired": False,
                        "options": saga_names
                    }
                ],
                "extraSupported": ["genre"]
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
    Ela carrega a primeira saga baseada na ordem alfabética.
    """
    if media_type != "movie" or catalog_id != "cine_maratona":
        return respond_with({"metas": []})
        
    saga_names = [dados["name"] for dados in CATALOGS.values()]
    saga_names.sort()
    
    import random
    
    # Criar uma lista "Destaques" pegando o primeiro filme de 15 sagas aleatórias
    lista_filmes = []
    todas_sagas = list(CATALOGS.values())
    
    # Escolhe até 15 sagas aleatórias (ou todas se tiver menos de 15)
    sagas_aleatorias = random.sample(todas_sagas, min(15, len(todas_sagas)))
    
    for saga in sagas_aleatorias:
        if len(saga["items"]) > 0:
            # Pegar apenas o primeiro filme de cada saga selecionada para dar um "gostinho"
            lista_filmes.append(saga["items"][0])

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
    O param entra na URL no formato -> "genre=Alien%20..."
    """
    if media_type != "movie" or catalog_id != "cine_maratona":
        return respond_with({"metas": []})
    
    # Decodificar o nome da saga que vem na URL protegida
    saga_selecionada = urllib.parse.unquote(saga_param)
    
    lista_filmes = []
    for saga in CATALOGS.values():
        if saga["name"] == saga_selecionada:
            lista_filmes = saga["items"]
            break

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
