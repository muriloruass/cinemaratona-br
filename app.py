from flask import Flask, jsonify, request
from flask_cors import CORS
from catalogs import CATALOGS

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

@app.route("/manifest.json")
def addon_manifest():
    """
    Gera o manifesto que o Stremio lê para instalar e entender nosso addon.
    Ele lista dinamicamente todos os catálogos disponíveis baseados no 'catalogs.py'.
    """
    catalogs_list = []
    
    # Percorrer o dicionário e adicionar cada saga como um catálogo independente na aba Filmes -> Descobrir
    for codinome, dados in CATALOGS.items():
        catalogs_list.append({
            "type": "movie",
            "id": f"cine_{codinome}",
            "name": dados["name"]
        })

    manifest = {
        "id": "br.cinemaratona.addon",
        "version": "1.0.0",
        "name": "CineMaratona BR 🎬",
        "description": "Sagas e Maratonas organizadas cronologicamente com metadados em PT-BR para Stremio. Descubra coleções épicas de cinema, das sagas clássicas até maratonas temáticas.",
        "logo": "https://i.imgur.com/gK6B58M.png",
        "resources": ["catalog"],
        "types": ["movie"],
        "catalogs": catalogs_list,
        "stremioAddonsConfig": {
            "issuer": "https://stremio-addons.net",
            "signature": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..01bufPwIGEuO8R9okmf43g.eqmi2c8kR0SG7OAWfGNvVMgT8JTy8BPTtN-S8FatjxUoh0sXZxiEAXRMYu3hfa68kO_WMHtkEw_kYtHCpbJP1rMcHXVpj5WWi1o0kGtmIapWiYQOH4MPZcut1bfS0QfM.YT0FeLMuRummbV3hBIqeYw"
        }
    }
    
    return respond_with(manifest)

@app.route("/catalog/<media_type>/<catalog_id>.json")
def addon_catalog(media_type, catalog_id):
    """
    Rota chamada pelo Stremio quando o usuário clica em um catálogo específico.
    Exemplo de catalog_id recebido: 'cine_marvel'
    """
    # Apenas lidamos com filmes, se for série ou canal, retornamos vazio
    if media_type != "movie":
        return respond_with({"metas": []})
    
    # Nosso ID tem o prefixo 'cine_', vamos remover para pegar o codinome do CATALOGS
    raw_id = catalog_id.replace("cine_", "")
    
    if raw_id not in CATALOGS:
        return respond_with({"metas": []})
        
    saga = CATALOGS[raw_id]
    lista_filmes = saga["items"]
    metas = []
    
    # Construir o array 'metas' conforme a exigência do Stremio (id, tipo, nome e poster)
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
