import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import urllib.request
import json

CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/movie/{}.json"

test_ids = {
    "tt2939064": "Minha Mãe é uma Peça",
    "tt5615632": "Minha Mãe é uma Peça 2",
    "tt10417728": "Minha Mãe é uma Peça 3",
    "tt1340838": "Se Eu Fosse Você 2",
    "tt7841174": "Os Farofeiros",
    "tt4835532": "Vai Que Cola",
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
