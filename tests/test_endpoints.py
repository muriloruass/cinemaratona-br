import pytest
import json
import base64
from app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    return app.test_client()

class TestManifest:
    def test_default_manifest_structure(self, client):
        r = client.get("/manifest.json")
        assert r.status_code == 200
        data = r.get_json()
        assert "id" in data
        assert "catalogs" in data
        assert len(data["catalogs"]) == 3

    def test_configured_manifest_filters_catalogs(self, client):
        config = base64.b64encode(json.dumps({
            "lang": "pt-br",
            "categories": ["marvel"]
        }).encode()).decode()
        r = client.get(f"/{config}/manifest.json")
        assert r.status_code == 200
        data = r.get_json()
        # Verifica se o catálogo de filmes tem a opção filtrada
        filmes_cat = next(c for c in data["catalogs"] if c["id"] == "cine_sagas_filmes")
        assert "Universo Marvel (MCU)" in filmes_cat["extra"][0]["options"]

class TestCatalog:
    def test_catalog_returns_metas(self, client):
        r = client.get("/catalog/movie/cine_sagas_filmes.json")
        assert r.status_code == 200
        data = r.get_json()
        assert "metas" in data
        assert len(data["metas"]) > 0

    def test_catalog_meta_has_required_fields(self, client):
        r = client.get("/catalog/movie/cine_sagas_filmes.json")
        meta = r.get_json()["metas"][0]
        assert "id" in meta
        assert "type" in meta
        assert "name" in meta
        assert meta["id"].startswith("tt")

    def test_search_returns_relevant_results(self, client):
        r = client.get("/catalog/movie/cine_sagas_filmes/search=vingadores.json")
        assert r.status_code == 200
        data = r.get_json()
        assert any("Vingadores" in m["name"] for m in data["metas"])

class TestMeta:
    def test_meta_returns_poster(self, client):
        # tt0371746 -> Homem de Ferro
        r = client.get("/meta/movie/tt0371746.json")
        assert r.status_code == 200
        data = r.get_json()
        assert "meta" in data
        assert "poster" in data["meta"]

class TestHealth:
    def test_ping(self, client):
        r = client.get("/ping")
        assert r.status_code == 200
        assert r.data.decode() == "pong"
