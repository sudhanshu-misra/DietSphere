from flask import Blueprint, request, jsonify
from services.health import *

health_bp = Blueprint("health", __name__, url_prefix="/api/v1")

@health_bp.route("/health", methods=["POST"])
def health_api():
    """
    Health Metrics API
    ---
    tags:
      - Health
    """
    data = request.get_json()
    required = ["weight", "height", "age", "gender", "activity", "goal"]

    if not data or any(k not in data for k in required):
        return jsonify({"error": "Invalid input"}), 400

    bmr = calculate_bmr(data["weight"], data["height"], data["age"], data["gender"])
    tdee = calculate_tdee(bmr, data["activity"])
    calories = calorie_goal(tdee, data["goal"])

    return jsonify({
        "BMI": calculate_bmi(data["weight"], data["height"]),
        "BMR": round(bmr, 2),
        "TDEE": tdee,
        "Daily Calories": calories,
        "Macros": macros(calories)
    })
