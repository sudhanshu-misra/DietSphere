from flask import Blueprint, request, jsonify, current_app
from services.nlp import parse_text
from services.recommender import recommend_food

nlp_bp = Blueprint("nlp", __name__, url_prefix="/api/v1")

@nlp_bp.route("/nlp", methods=["POST"])
def nlp_api():
    """
    NLP Diet Recommendation
    ---
    tags:
      - NLP
    """
    data = request.get_json()
    preference, goal = parse_text(data["text"])

    model = current_app.config["ML_MODEL"]
    encoder = current_app.config["GOAL_ENCODER"]

    foods = recommend_food(model, encoder, preference, goal)

    return jsonify({
        "preference": preference,
        "goal": goal,
        "recommended_foods": foods
    })
