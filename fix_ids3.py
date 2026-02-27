import urllib.request
import urllib.parse
from catalogs import CATALOGS
import re
import time

def scrape_tmdb(title):
    try:
        query = urllib.parse.quote(title)
        req = urllib.request.Request(f"https://www.themoviedb.org/search?query={query}", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        # Find first movie link
        match = re.search(r'href="/movie/(\d+)[^"]*"', res)
        if match:
            tmdb_id = match.group(1)
            # Fetch TMDB page to get IMDb link
            req_movie = urllib.request.Request(f"https://www.themoviedb.org/movie/{tmdb_id}", headers={'User-Agent': 'Mozilla/5.0'})
            res_movie = urllib.request.urlopen(req_movie).read().decode('utf-8')
            imdb_match = re.search(r'href="https://www.imdb.com/title/(tt\d+)"', res_movie)
            if imdb_match:
                return imdb_match.group(1)
    except Exception as e:
        print(f"Error on TMDB for {title}: {e}")
    return None

missing = [
    ("O Auto da Compadecida 2", "tt11124208"),
    ("Minha Mãe é uma Peça 2", "tt4858054"),
    ("Transformers o inicio", "tt4622012")
]

for title, old_id in missing:
    time.sleep(1)
    new_id = scrape_tmdb(title)
    if new_id:
        print(f"[{title}] Old: {old_id} -> TMDB found: {new_id}")
    else:
        print(f"[{title}] Still not found.")

