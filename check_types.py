import urllib.request
import json
import time
from catalogs import CATALOGS

wrong_type = []
total = 0

for saga_id, saga_data in CATALOGS.items():
    for movie in saga_data["items"]:
        total += 1
        try:
            url = f"https://v3-cinemeta.strem.io/meta/movie/{movie['id']}.json"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
            data = json.loads(res)
            meta_type = data.get("meta", {}).get("type", "unknown")
            if meta_type != "movie":
                wrong_type.append((saga_data["name"], movie["name"], movie["id"], meta_type))
            time.sleep(0.3)
        except Exception as e:
            wrong_type.append((saga_data["name"], movie["name"], movie["id"], f"ERRO: {e}"))

print(f"\nChecked {total} movies.")
if wrong_type:
    print(f"Found {len(wrong_type)} entries with wrong type or error:")
    for saga, name, imdb_id, t in wrong_type:
        print(f"  [{saga}] {name} ({imdb_id}) -> type: {t}")
else:
    print("All movies have correct type 'movie'!")
