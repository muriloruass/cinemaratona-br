import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import urllib.request
import json

CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/movie/{}.json"

test_ids = {
    "tt5344444": "Minha Mãe é uma Peça 2",
    "tt11311974": "Minha Mãe é uma Peça 3",
    "tt1329451": "Se Eu Fosse Você 2",
    "tt7529618": "Os Farofeiros",
    "tt4496634": "Vai Que Cola",
    "tt2960014": "Minha Mãe é uma Peça",
    "tt0448927": "Se Eu Fosse Você",
    "tt0082325": "Eles Não Usam Black-Tie",
    "tt0109380": "Carlota Joaquina",
    "tt0114212": "O Quatrilho"
}

for imdb_id, name in test_ids.items():
    try:
        req = urllib.request.Request(CINEMETA_URL.format(imdb_id), headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            actual_name = data.get("meta", {}).get("name", "NOT FOUND")
            print(f"{imdb_id} ({name}) -> {actual_name}")
    except Exception as e:
        print(f"{imdb_id} ({name}) -> ERROR: {e}")
