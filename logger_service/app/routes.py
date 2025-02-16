from flask import Blueprint, request, jsonify
from app.services import LogService

bp = Blueprint('logger', __name__)

@bp.route('/log', methods=['POST'])
def log_message():
    """Recibe logs desde otros servicios y los pasa al LogService."""
    data = request.json
    level = data.get("level", "INFO")
    message = data.get("message")
    service = data.get("service", "unknown")

    LogService.save_log(level, message, service)
    return jsonify({"status": "ok"}), 200