from flask import Flask, request, jsonify
from logic import calculate_bmr, calculate_tdee, adjust_calories
from food_rules import filter_foods, recommend_meals_ml

app = Flask(__name__)

@app.route("/diet-plan", methods=["POST"])
def diet_plan():
    d = request.json

    bmr = calculate_bmr(d["weight_kg"], d["height_cm"], d["age"], d["gender"])
    tdee = calculate_tdee(bmr, d["activity_level"])
    target = adjust_calories(tdee, d["goal"])

    foods = filter_foods([], [])
    plan = recommend_meals_ml(foods, target, [], [])

    return jsonify({"target_calories": target, "diet_plan": plan})

if __name__ == "__main__":
    app.run(debug=True)