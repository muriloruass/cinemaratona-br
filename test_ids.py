import urllib.request
import json

ids = {
    "Moana 2": "tt33475149",
    "Zootopia 2": "tt26443597",
    "Universidade Monstros": "tt1453405",
    "Carros 2": "tt1216475",
    "O Rei Leao 2": "tt0120131",
    "O Rei Leao 2019": "tt6105098",
    "Mufasa": "tt22675690",
    "Frozen 2": "tt4520988",
    "Encanto": "tt2953050",
    "Lilo 2": "tt0386265",
    "Leroy": "tt0486761",
    "Cinderela 1950": "tt0042332",
    "Peter Pan & Wendy": "tt5280232"
}

CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/movie/{}.json"

for name, imdb_id in ids.items():
    try:
        req = urllib.request.Request(CINEMETA_URL.format(imdb_id), headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            print(name, "->", data.get("meta", {}).get("name", "NOT FOUND"))
    except Exception as e:
         print(name, "-> ERROR", e)
