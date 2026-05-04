import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    return app.test_client()

class TestManifestEndpoint:
    def test_manifest_headers_cache_control(self, client):
        """Valida se o Cache-Control segue a regra de ouro: s-maxage=86400."""
        response = client.get("/manifest.json")
        
        assert response.status_code == 200
        cache_header = response.headers.get("Cache-Control", "")
        
        # Este teste FALHARÁ no estado atual (que usa max-age=300)
        assert "s-maxage=86400" in cache_header
        assert "stale-while-revalidate=3600" in cache_header
        assert "Vary" in response.headers
        assert response.headers["Vary"] == "Accept-Encoding"

    def test_manifest_content_structure(self, client):
        """Valida campos obrigatórios do Stremio SDK."""
        data = client.get("/manifest.json").get_json()
        
        assert data["id"] == "br.cinemaratona.addon.movies"
        assert "catalogs" in data
        assert "resources" in data
