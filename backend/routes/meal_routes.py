from flask import Blueprint, request, jsonify, current_app
from services.health import calculate_bmr, calculate_tdee, calorie_goal
from services.recommender import recommend_food

meal_bp = Blueprint("meal", __name__, url_prefix="/api/v1")

@meal_bp.route("/auto-meal-plan", methods=["POST"])
def auto_meal_plan():
    """
    Automatic Meal Plan
    ---
    tags:
      - Meal Plan
    """
    data = request.get_json()

    bmr = calculate_bmr(
        data["weight"], data["height"], data["age"], data["gender"]
    )
    tdee = calculate_tdee(bmr, data["activity"])
    calories = calorie_goal(tdee, data["goal"])

    model = current_app.config["ML_MODEL"]
    encoder = current_app.config["GOAL_ENCODER"]

    foods = recommend_food(model, encoder, data["preference"], data["goal"])

    return jsonify({
        "daily_calories": calories,
        "recommended_foods": foods
    })
