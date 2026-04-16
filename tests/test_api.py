import pytest
import json
import base64
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_manifest_default(client):
    """Verifica se o manifesto padrão retorna os 4 catálogos novos."""
    response = client.get('/manifest.json')
    assert response.status_code == 200
    data = response.json
    assert "catalogs" in data
    catalog_ids = [c["id"] for c in data["catalogs"]]
    assert "cine_sagas_filmes" in catalog_ids
    assert "cine_sagas_series" in catalog_ids
    assert "cine_sagas_animacoes" in catalog_ids
    assert "cine_especiais" in catalog_ids
    assert len(catalog_ids) == 4

def test_manifest_configured(client):
    """Verifica manifesto customizado via Base64."""
    # Config: apenas marvel e nolan em espanhol
    config = {"lang": "es", "categories": ["marvel", "nolan"]}
    config_b64 = base64.b64encode(json.dumps(config).encode()).decode()
    
    response = client.get(f'/{config_b64}/manifest.json')
    assert response.status_code == 200
    data = response.json
    assert "Sagas de Películas" in str(data)  # Nome em espanhol
    
    # Verifica opções do catálogo de filmes (deve ter Marvel)
    filmes_cat = next(c for c in data["catalogs"] if c["id"] == "cine_sagas_filmes")
    options = filmes_cat["extra"][0]["options"]
    assert "Universo Marvel (MCU)" in options

def test_catalog_random_fallback(client):
    """Verifica se o catálogo retorna itens aleatórios quando sem filtro."""
    response = client.get('/catalog/movie/cine_sagas_filmes.json')
    assert response.status_code == 200
    assert "metas" in response.json
    assert len(response.json["metas"]) > 0

def test_catalog_with_filter(client):
    """Verifica se o filtro de gênero funciona corretamente."""
    # Filtro: Universo Marvel (MCU)
    from urllib.parse import quote
    genre_filter = quote("genre=Universo Marvel (MCU)")
    response = client.get(f'/catalog/movie/cine_sagas_filmes/{genre_filter}.json')
    
    assert response.status_code == 200
    metas = response.json["metas"]
    assert len(metas) >= 30  # Marvel tem muitos filmes
    assert any("Homem de Ferro" in m["name"] for m in metas)

def test_cache_headers(client):
    """Verifica se os headers de cache estão presentes."""
    response = client.get('/catalog/movie/cine_sagas_filmes.json')
    assert "Cache-Control" in response.headers
    assert "public, max-age=300" in response.headers["Cache-Control"]

def test_special_catalog_labels(client):
    """Verifica se o catálogo especial contém labels amigáveis e não IDs crus."""
    response = client.get('/manifest.json')
    especiais_cat = next(c for c in response.json["catalogs"] if c["id"] == "cine_especiais")
    options = especiais_cat["extra"][0]["options"]
    # Não deve ter IDs crus como 'nolan' ou 'tarantino'
    assert "nolan" not in options
    assert "Melhor de Christopher Nolan" in options
