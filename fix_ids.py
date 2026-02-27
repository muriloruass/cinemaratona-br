from catalogs import CATALOGS
import urllib.request
import json
import time

def get_imdb_id(title, year=None):
    # Using TMDB API via a free proxy or simple OMDB if available
    # For simplicity, let's just use duckduckgo HTML search to grab the first IMDb link
    try:
        query = title.replace(" ", "+") + "+imdb"
        req = urllib.request.Request(f"https://html.duckduckgo.com/html/?q={query}", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        import re
        match = re.search(r'imdb\.com/title/(tt\d+)', res)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"Error searching for {title}: {e}")
    return None

def test_metahub(imdb_id):
    if not imdb_id: return False
    url = f"https://images.metahub.space/poster/medium/{imdb_id}/img"
    try:
        req = urllib.request.Request(url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req, timeout=5)
        return True
    except:
        return False

missing = [
    ("Capitão América: Admirável Mundo Novo", "tt14511704"),
    ("Os Novos Mutantes", "tt4677138"),
    ("A Cantiga dos Pássaros e das Serpentes", "tt10545634"),
    ("Meu Malvado Favorito 4", "tt7569228"),
    ("Transformers: O Início", "tt4622012"),
    ("Prometheus", "tt1179518"),
    ("Predadores", "tt0440259"),
    ("Sexta-Feira 13 - Parte 3", "tt0083952"),
    ("Sexta-Feira 13 - Parte 5: Um Novo Começo", "tt0089232"),
    ("Jason X", "tt0311438"),
    ("O Novo Pesadelo: O Retorno de Freddy Krueger", "tt0110662"),
    ("F1", "tt7097310"),
    ("Blue Moon", "tt32452296"),
    ("Ainda Estou Aqui", "tt28014526"),
    ("O Auto da Compadecida 2", "tt11124208"),
    ("Maníaco do Parque", "tt27382209"),
    ("Bacurau", "tt6566958"),
    ("Marighella", "tt10800030"),
    ("Turma da Mônica: Laços", "tt10851866"),
    ("Pânico", "tt0117646"),
    ("Minha Mãe é uma Peça: O Filme", "tt2400332"),
    ("Minha Mãe é uma Peça 2", "tt4858054"),
    ("Minha Mãe é uma Peça 3", "tt9685324"),
    ("Se Eu Fosse Você 2", "tt1122588")
]

fixes = {}
for title, old_id in missing:
    time.sleep(1) # rate limit
    new_id = get_imdb_id(title)
    if new_id and new_id != old_id:
        if test_metahub(new_id):
            print(f"[{title}] Old: {old_id} -> New Valid: {new_id}")
            fixes[old_id] = new_id
        else:
            print(f"[{title}] Found new ID {new_id} but it STILL fails on MetaHub.")
    else:
         print(f"[{title}] Could not find better ID (Current: {old_id}, Found: {new_id})")

print("\nSuggestions to manually replace in catalogs.py:")
for old, new in fixes.items():
    print(f"'{old}' -> '{new}'")

