import urllib.request
import urllib.parse
import json
import time

movies_to_search = [
    "A Supremacia Bourne",
    "A Cantiga dos Pássaros e das Serpentes",
    "De Volta ao Jogo",
    "Missão: Impossível - Efeito Fallout",
    "O Senhor dos Anéis: O Retorno do Rei",
    "O Planeta dos Macacos (1968)",
    "Fuga do Planeta dos Macacos",
    "Planeta dos Macacos: A Guerra",
    "Predador 2",
    "Rocky IV",
    "Sexta-Feira 13 - Parte 2",
    "Sexta-Feira 13 - Parte 5: Um Novo Começo",
    "Sexta-Feira 13 - Parte 8: Jason Ataca Nova York",
    "Jason X",
    "Star Trek (2009)",
    "Transformers: O Lado Oculto da Lua",
    "Amnésia",
    "Dunkirk"
]

def search_cinemeta(title):
    try:
        query = urllib.parse.quote(title)
        url = f"https://v3-cinemeta.strem.io/catalog/movie/top/search={query}.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        data = json.loads(res)
        if data and "metas" in data and len(data["metas"]) > 0:
            return data["metas"][0]["id"]
    except Exception as e:
        print(f"Error searching {title}: {e}")
    return None

for title in movies_to_search:
    time.sleep(1)
    imdb_id = search_cinemeta(title)
    print(f"[{title}] Cinemeta ID: {imdb_id}")
