from flask import jsonify
from data.config import POSTER_METAHUB_URL

def respond_with(data):
    """Retorna respostas no formato JSON requerido pelo Stremio com headers de cache e CORS."""
    response = jsonify(data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    # Cache de 5 minutos (300s) com revalidação em background (60s)
    response.headers["Cache-Control"] = "public, max-age=300, stale-while-revalidate=60"
    return response

def build_metas(items: list, media_type: str) -> list:
    """
    Constrói a lista de metas no formato esperado pelo Stremio.
    Centraliza a lógica usada por todos os handlers de catálogo.
    """
    return [
        {
            "id": item["id"],
            "type": media_type,
            "name": item["name"],
            "poster": POSTER_METAHUB_URL.format(item["id"]),
        }
        for item in items
    ]
