import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import urllib.request
import json
from catalogs import ANIMATIONS

# Cinemeta API URL
CINEMETA_URL = "https://v3-cinemeta.strem.io/meta/movie/{}.json"

errors = []
print("Verificando IDs de Animações...\n")

for saga_id, saga in ANIMATIONS.items():
    print(f"--- Verificando {saga['name']} ---")
    for item in saga['items']:
        imdb_id = item['id']
        expected_name = item['name']
        try:
            req = urllib.request.Request(CINEMETA_URL.format(imdb_id), headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    meta = data.get('meta', {})
                    actual_name = meta.get('name', 'NOME_NAO_ENCONTRADO')
                    
                    if not actual_name or actual_name == 'NOME_NAO_ENCONTRADO':
                         print(f"❌ {expected_name} ({imdb_id}) -> NÃO ENCONTRADO NO CINEMETA")
                         errors.append(item)
                    else:
                         print(f"✅ {expected_name} ({imdb_id}) -> {actual_name}")
                else:
                    print(f"❌ {expected_name} ({imdb_id}) -> ERRO API {response.status}")
                    errors.append(item)
        except Exception as e:
            print(f"❌ {expected_name} ({imdb_id}) -> ERRO DE CONEXÃO: {e}")
            errors.append(item)

print("\nConcluído!")
