from flask import Blueprint
from utils.responses import respond_with
from data.config import POSTER_METAHUB_URL

meta_bp = Blueprint('meta', __name__)

@meta_bp.route("/meta/<media_type>/<imdb_id>.json")
@meta_bp.route("/<config_b64>/meta/<media_type>/<imdb_id>.json")
def addon_meta(media_type, imdb_id, config_b64=None):
    """
    Stub de meta para evitar erro vermelho na interface do Stremio.
    O Stremio usa Cinemeta internamente para dados completos.
    """
    if media_type not in ["movie", "series"]:
        media_type = "movie"

    return respond_with({
        "meta": {
            "id": imdb_id,
            "type": media_type,
            "poster": POSTER_METAHUB_URL.format(imdb_id)
        }
    })
