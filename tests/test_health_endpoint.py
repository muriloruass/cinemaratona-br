import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    return app.test_client()

class TestHealthEndpoint:
    def test_health_check_status_ok(self, client):
        """Valida se a nova rota /health retorna status 200 e JSON correto."""
        # Falhará inicialmente (404) pois a rota ainda não foi movida/criada
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "ok"
        assert "version" in data
        assert data["env"] == "production"

    def test_legacy_ping_is_removed(self, client):
        """Garante que a rota antiga /ping não responde mais."""
        response = client.get("/ping")
        # No estado atual retorna 200 "pong"
        assert response.status_code == 404
