import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import urllib.request
import json

CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/{}/{}.json"

ids_to_check = [
    ("movie", "tt1921043"),
    ("movie", "tt0271383"),
    ("movie", "tt30868610"),
    ("movie", "tt1730133"),
    ("movie", "tt4657092"),
    ("movie", "tt3034258"),
    ("movie", "tt4302740"),
    ("movie", "tt1564916"),
    ("movie", "tt0448927"),
    ("movie", "tt1099227"),
    ("movie", "tt2332518"),
    ("movie", "tt3148528"),
    ("movie", "tt4491640"),
    ("movie", "tt13354204"),
    ("movie", "tt0293007"),
    ("movie", "tt0082912"),
    ("movie", "tt0077452"),
    ("movie", "tt0080482"),
    ("movie", "tt7986672"),
    ("movie", "tt0367859"),
    ("movie", "tt0241663"),
    ("movie", "tt0317887"),
    ("movie", "tt35301431"),
    ("series", "tt0281447"),
    ("movie", "tt2464018"),
    ("movie", "tt10611372"),
    ("movie", "tt3212812")
]

for mtype, imdb_id in ids_to_check:
    try:
        req = urllib.request.Request(CINEMETA_URL.format(mtype, imdb_id), headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            name = data.get("meta", {}).get("name", "NOT FOUND")
            year = data.get("meta", {}).get("year", "")
            print(f"{imdb_id} | {mtype} | {name} ({year})")
    except Exception as e:
        print(f"{imdb_id} | {mtype} | ERROR: {e}")
