from flask import Flask, request, jsonify
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

app = Flask(__name__)

# ======================================================
# HOME ROUTE (Browser-safe)
# ======================================================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Diet Planner Backend is running 🚀",
        "endpoints": [
            "POST /health",
            "POST /ml-recommend",
            "POST /nlp",
            "POST /auto-meal-plan"
        ]
    })

# ======================================================
# FOOD DATASET
# ======================================================
food_dataset = [
    {"name": "Oats", "type": "veg", "protein": 11, "calories": 150, "meal": "breakfast"},
    {"name": "Tofu Scramble", "type": "veg", "protein": 15, "calories": 160, "meal": "breakfast"},
    {"name": "Egg Omelette", "type": "non-veg", "protein": 14, "calories": 180, "meal": "breakfast"},
    {"name": "Paneer Curry", "type": "veg", "protein": 18, "calories": 265, "meal": "lunch"},
    {"name": "Dal Rice", "type": "veg", "protein": 12, "calories": 220, "meal": "lunch"},
    {"name": "Chicken Breast", "type": "non-veg", "protein": 31, "calories": 165, "meal": "lunch"},
    {"name": "Veg Salad", "type": "veg", "protein": 8, "calories": 120, "meal": "dinner"},
    {"name": "Grilled Tofu", "type": "veg", "protein": 16, "calories": 180, "meal": "dinner"},
    {"name": "Grilled Fish", "type": "non-veg", "protein": 28, "calories": 190, "meal": "dinner"}
]

# ======================================================
# ML TRAINING DATA
# ======================================================
training_data = [
    [18, 265, 1, "weight_loss", 1],
    [9, 120, 1, "weight_loss", 0],
    [31, 165, 0, "weight_loss", 1],
    [8, 120, 1, "weight_gain", 0],
    [28, 190, 0, "weight_gain", 1],
    [12, 220, 1, "maintenance", 1],
]

df = pd.DataFrame(
    training_data,
    columns=["protein", "calories", "is_veg", "goal", "label"]
)

# Encode goal
goal_encoder = LabelEncoder()
df["goal_encoded"] = goal_encoder.fit_transform(df["goal"])

X = df[["protein", "calories", "is_veg", "goal_encoded"]]
y = df["label"]

# ======================================================
# TRAIN / TEST SPLIT + MODEL TRAINING
# ======================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

ml_model = LogisticRegression()
ml_model.fit(X_train, y_train)

# ======================================================
# MODEL EVALUATION (PRINTED AT STARTUP)
# ======================================================
y_pred = ml_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\n===== ML MODEL EVALUATION =====")
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)
print("================================\n")

# ======================================================
# HEALTH CALCULATIONS
# ======================================================
def calculate_bmi(weight, height_cm):
    return round(weight / ((height_cm / 100) ** 2), 2)

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity):
    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }
    return round(bmr * factors.get(activity, 1.2), 2)

def calorie_goal(tdee, goal):
    if goal == "weight_loss":
        return tdee - 500
    if goal == "weight_gain":
        return tdee + 500
    return tdee

def macros(calories):
    return {
        "protein_g": round((0.30 * calories) / 4, 1),
        "carbs_g": round((0.40 * calories) / 4, 1),
        "fats_g": round((0.30 * calories) / 9, 1)
    }

# ======================================================
# ML RECOMMENDATION (NO WARNINGS VERSION)
# ======================================================
def ml_recommend(preference, goal):
    results = []
    goal_encoded = goal_encoder.transform([goal])[0]

    for food in food_dataset:
        is_veg = 1 if food["type"] == "veg" else 0

        if preference == "veg" and is_veg == 0:
            continue
        if preference == "non-veg" and is_veg == 1:
            continue

        features_df = pd.DataFrame([{
            "protein": food["protein"],
            "calories": food["calories"],
            "is_veg": is_veg,
            "goal_encoded": goal_encoded
        }])

        if ml_model.predict(features_df)[0] == 1:
            results.append(food)

    return results

# ======================================================
# NLP
# ======================================================
def parse_text(text):
    text = text.lower()
    preference = "veg"
    goal = "maintenance"

    if "non veg" in text or "chicken" in text or "egg" in text:
        preference = "non-veg"
    if "lose" in text:
        goal = "weight_loss"
    if "gain" in text or "muscle" in text:
        goal = "weight_gain"

    return preference, goal

# ======================================================
# API ROUTES
# ======================================================
@app.route("/health", methods=["POST"])
def health_api():
    data = request.get_json()

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

@app.route("/ml-recommend", methods=["POST"])
def ml_api():
    data = request.get_json()
    foods = ml_recommend(data["preference"], data["goal"])
    return jsonify({"recommended_foods": foods})

@app.route("/nlp", methods=["POST"])
def nlp_api():
    data = request.get_json()
    preference, goal = parse_text(data["text"])
    foods = ml_recommend(preference, goal)
    return jsonify({
        "preference": preference,
        "goal": goal,
        "recommended_foods": foods
    })

@app.route("/auto-meal-plan", methods=["POST"])
def auto_meal_plan():
    data = request.get_json()

    bmr = calculate_bmr(data["weight"], data["height"], data["age"], data["gender"])
    tdee = calculate_tdee(bmr, data["activity"])
    calories = calorie_goal(tdee, data["goal"])

    foods = ml_recommend(data["preference"], data["goal"])

    return jsonify({
        "daily_calories": calories,
        "recommended_foods": foods
    })

# ======================================================
# RUN
# ======================================================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
