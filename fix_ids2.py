from catalogs import CATALOGS
import urllib.request
import urllib.parse
import time
import re

def get_imdb_id(title):
    try:
        query = urllib.parse.quote(title + " imdb")
        req = urllib.request.Request(f"https://html.duckduckgo.com/html/?q={query}", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
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
    ("A Cantiga dos Passaros e das Serpentes", "tt10545634"),
    ("Meu Malvado Favorito 4", "tt7569228"),
    ("Transformers O Inicio", "tt4622012"),
    ("O Auto da Compadecida 2", "tt11124208"),
    ("Maniaco do Parque", "tt27382209"),
    ("Turma da Monica Lacos", "tt10851866"),
    ("Panico", "tt0117646"),
    ("Minha Mae e uma Peca", "tt2400332"),
    ("Minha Mae e uma Peca 2", "tt4858054"),
    ("Minha Mae e uma Peca 3", "tt9685324"),
    ("Se Eu Fosse Voce 2", "tt1122588")
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

