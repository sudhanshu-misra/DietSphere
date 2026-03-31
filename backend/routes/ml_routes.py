from flask import Blueprint, request, jsonify, current_app
from services.recommender import recommend_food

ml_bp = Blueprint("ml", __name__, url_prefix="/api/v1")

@ml_bp.route("/ml-recommend", methods=["POST"])
def ml_recommend_api():
    """
    ML Food Recommendation
    ---
    tags:
      - ML Recommendation
    """
    data = request.get_json()

    model = current_app.config["ML_MODEL"]
    encoder = current_app.config["GOAL_ENCODER"]

    foods = recommend_food(model, encoder, data["preference"], data["goal"])
    return jsonify({"recommended_foods": foods})
