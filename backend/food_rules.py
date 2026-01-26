from backend.food_data import FOOD_DB
from backend.ml_recommender import recommend_foods_ml, build_user_vector

def filter_foods(prefs, restr):
    return FOOD_DB

def recommend_meals_ml(foods, target_calories, prefs, restr):
    user_vec = build_user_vector(target_calories/4, 30, True, False, False)
    ranked = recommend_foods_ml(foods, user_vec)

    return {
        "breakfast": ranked[0]["name"],
        "lunch": ranked[1]["name"],
        "dinner": ranked[2]["name"],
        "snacks": ranked[3]["name"]
    }