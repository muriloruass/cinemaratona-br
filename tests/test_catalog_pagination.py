import pytest
from unittest.mock import patch, MagicMock
from app import create_app
from data.catalogs._base import CatalogItem

@pytest.fixture
def client():
    app = create_app(testing=True)
    return app.test_client()

class TestCatalogPagination:
    @patch("controllers.catalog.get_catalog")
    def test_pagination_returns_different_results_for_pages(self, mock_get_catalog, client):
        """
        Provas que página 1 (skip=0) e página 2 (skip=100) são distintas.
        """
        # Criamos 150 itens mockados
        mock_items = [
            CatalogItem(id=f"tt{i:07d}", name=f"Movie {i}", type="movie")
            for i in range(150)
        ]
        # Mockamos para qualquer ID que for solicitado
        mock_get_catalog.return_value = mock_items

        # Página 1
        # Usamos um gênero que o build_label_lookup não conheça para ele usar o literal
        resp1 = client.get("/catalog/movie/cine_sagas_filmes/genre=AnySaga&skip=0.json")
        data1 = resp1.get_json()
        metas1 = data1.get("metas", [])

        # Página 2
        resp2 = client.get("/catalog/movie/cine_sagas_filmes/genre=AnySaga&skip=100.json")
        data2 = resp2.get_json()
        metas2 = data2.get("metas", [])

        assert len(metas1) == 100
        assert len(metas2) == 50
        assert metas1[0]["id"] == "tt0000000"
        assert metas2[0]["id"] == "tt0000100"
