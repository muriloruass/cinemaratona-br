import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import urllib.request
import json
from data.catalogs.maratonas import MARATONAS

CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/movie/{}.json"

items = MARATONAS.get("cinemanacional", [])
print(f"Verificando {len(items)} filmes do catálogo Cinema Brasileiro...\n")

errors = 0
for item in items:
    try:
        req = urllib.request.Request(CINEMETA_URL.format(item.id), headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            actual_name = data.get("meta", {}).get("name", "NOT FOUND")
            if actual_name == "NOT FOUND":
                print(f"❌ {item.name} ({item.id}) -> NÃO ENCONTRADO")
                errors += 1
            else:
                print(f"✅ {item.name} ({item.id}) -> {actual_name}")
    except Exception as e:
        print(f"⚠️ {item.name} ({item.id}) -> ERRO: {e}")
        errors += 1

if errors == 0:
    print("\n🎉 Todos os IDs estão corretos!")
else:
    print(f"\n❌ Foram encontrados {errors} erros.")
    sys.exit(1)
