from flask import Blueprint, jsonify
from data.config import ADDON_VERSION

health_bp = Blueprint('health', __name__)

@health_bp.route("/health")
def health_check():
    """Endpoint de monitoramento para UptimeRobot e dashboards de SRE."""
    return jsonify({
        "status": "ok",
        "version": ADDON_VERSION,
        "env": "production"
    }), 200
