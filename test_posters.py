import urllib.request
import urllib.error
from catalogs import CATALOGS

POSTER_URL = "https://images.metahub.space/poster/medium/{}/img"

missing_posters = []
total_movies = 0

for saga_id, saga_data in CATALOGS.items():
    for movie in saga_data["items"]:
        total_movies += 1
        url = POSTER_URL.format(movie["id"])
        try:
            req = urllib.request.Request(url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
            urllib.request.urlopen(req, timeout=5)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                missing_posters.append((saga_data["name"], movie["name"], movie["id"]))
        except Exception as e:
            print(f"Error checking {movie['name']}: {e}")

print(f"Checked {total_movies} movies.")
if missing_posters:
    print(f"Found {len(missing_posters)} movies missing posters on MetaHub:")
    for saga, name, imdb_id in missing_posters:
        print(f"[{saga}] {name} (ID: {imdb_id})")
else:
    print("All movies have valid posters on MetaHub!")
