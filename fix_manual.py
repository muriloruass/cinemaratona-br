import urllib.request
import urllib.parse
import re
import time

movies = {
    "A Supremacia Bourne": "The Bourne Supremacy",
    "A Cantiga dos Pássaros e das Serpentes": "The Hunger Games: The Ballad of Songbirds & Snakes",
    "De Volta ao Jogo": "John Wick",
    "Missão: Impossível - Efeito Fallout": "Mission: Impossible - Fallout",
    "O Senhor dos Anéis: O Retorno do Rei": "The Lord of the Rings: The Return of the King",
    "Fuga do Planeta dos Macacos": "Escape from the Planet of the Apes",
    "Predador 2": "Predator 2",
    "Rocky IV": "Rocky IV",
    "Sexta-Feira 13 - Parte 2": "Friday the 13th Part 2",
    "Sexta-Feira 13 - Parte 5: Um Novo Começo": "Friday the 13th: A New Beginning",
    "Sexta-Feira 13 - Parte 8: Jason Ataca Nova York": "Friday the 13th Part VIII: Jason Takes Manhattan",
    "Jason X": "Jason X",
    "Star Trek (2009)": "Star Trek 2009",
    "Transformers: O Lado Oculto da Lua": "Transformers: Dark of the Moon",
    "Amnésia": "Memento",
    "Dunkirk": "Dunkirk 2017"
}

def get_imdb(en_title):
    try:
        query = urllib.parse.quote(en_title + " imdb")
        req = urllib.request.Request(f"https://html.duckduckgo.com/html/?q={query}", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'imdb\.com/title/(tt\d+)', res)
        if match: return match.group(1)
    except: pass
    return "UNKNOWN"

for pt, en in movies.items():
    time.sleep(1)
    print(f"[{pt}] CORRECT IMDB: {get_imdb(en)}")
