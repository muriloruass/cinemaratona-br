#!/usr/bin/env python3
"""
scripts/sync_saga.py — Sincronização de sagas via API TMDB
Uso:
  python scripts/sync_saga.py "Marvel Cinematic Universe" mcu
  python scripts/sync_saga.py "James Bond Collection" 007
  python scripts/sync_saga.py "The Dark Knight Collection" batman-nolan

Gera/atualiza /data/sagas/<nome>.json com os IDs IMDB corretos.
Requer: TMDB_API_KEY no ambiente (ou arquivo .env na raiz do projeto).
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error

# Tenta carregar .env da raiz do projeto
_ROOT = os.path.join(os.path.dirname(__file__), '..')
_ENV_PATH = os.path.join(_ROOT, '.env')
if os.path.exists(_ENV_PATH):
    with open(_ENV_PATH) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _v = _line.split('=', 1)
                os.environ.setdefault(_k.strip(), _v.strip())

TMDB_API_KEY = os.environ.get('TMDB_API_KEY', '')
TMDB_BASE = 'https://api.themoviedb.org/3'
REQUEST_DELAY = 0.3  # segundos entre requests para respeitar rate limit TMDB


def tmdb_get(path: str, params: dict = None) -> dict:
    """Faz um GET na API TMDB e retorna o JSON."""
    if not TMDB_API_KEY:
        print("❌ TMDB_API_KEY não definida. Configure no .env ou variável de ambiente.")
        sys.exit(1)
    p = {'api_key': TMDB_API_KEY, 'language': 'pt-BR'}
    if params:
        p.update(params)
    qs = urllib.parse.urlencode(p)
    url = f"{TMDB_BASE}{path}?{qs}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code} ao acessar: {url}")
        return {}
    except Exception as e:
        print(f"❌ Erro de rede: {e}")
        return {}


def get_imdb_id(tmdb_movie_id: int) -> str | None:
    """Busca o IMDB ID de um filme via ID interno do TMDB."""
    data = tmdb_get(f'/movie/{tmdb_movie_id}/external_ids')
    imdb_id = data.get('imdb_id')
    if imdb_id and imdb_id.startswith('tt') and len(imdb_id) >= 9:
        return imdb_id
    return None


def search_and_sync_collection(collection_name: str, output_name: str):
    """Busca uma coleção no TMDB e sincroniza os IDs IMDB para um arquivo JSON."""
    print(f"\n🔍 Buscando coleção: \"{collection_name}\"...")

    # 1. Buscar a coleção pelo nome
    search = tmdb_get('/search/collection', {'query': collection_name})
    results = search.get('results', [])
    if not results:
        print(f"❌ Coleção não encontrada: {collection_name}")
        sys.exit(1)

    collection = results[0]
    print(f"✅ Encontrada: {collection['name']} (TMDB ID: {collection['id']})")

    # 2. Buscar detalhes da coleção
    detail = tmdb_get(f"/collection/{collection['id']}")
    parts = detail.get('parts', [])
    if not parts:
        print("⚠️  Nenhum filme encontrado nesta coleção.")
        return

    # 3. Para cada filme, buscar o IMDB ID
    movies = []
    for part in parts:
        time.sleep(REQUEST_DELAY)
        imdb_id = get_imdb_id(part['id'])
        if imdb_id:
            year = (part.get('release_date') or '')[:4]
            title = part.get('title', 'Sem título')
            movies.append({
                'id': imdb_id,
                'name': title,
                'year': year,
                'type': 'movie'
            })
            print(f"  ✓ {title} ({year}) → {imdb_id}")
        else:
            print(f"  ⚠ {part.get('title')} — IMDB ID não encontrado, pulando.")

    # 4. Ordenar por ano
    movies.sort(key=lambda m: m.get('year') or '0')

    # 5. Salvar JSON
    output_dir = os.path.join(_ROOT, 'data', 'sagas')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f'{output_name}.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Salvo em {output_path} com {len(movies)} filmes.")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    collection_name = sys.argv[1]
    output_name = sys.argv[2]
    search_and_sync_collection(collection_name, output_name)


if __name__ == '__main__':
    main()
