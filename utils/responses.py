from flask import jsonify, Response
from data.config import POSTER_METAHUB_URL

def respond_with(data: dict) -> Response:
    """Retorna respostas no formato JSON requerido pelo Stremio com headers de cache e CORS."""
    response = jsonify(data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    
    # Cache de 24h na CDN (Vercel Edge) com revalidação em background de 1h
    response.headers["Cache-Control"] = (
        "public, s-maxage=86400, stale-while-revalidate=3600"
    )
    response.headers["Vary"] = "Accept-Encoding"
    return response
