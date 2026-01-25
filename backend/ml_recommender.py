import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def food_to_vector(food):
    return [
        food["calories"], food["protein"],
        food["carbs"], food["fats"],
        int(food["veg"]), int(food["gluten_free"]), int(food["dairy_free"])
    ]

def build_user_vector(calories, protein, veg, gluten, dairy):
    return np.array([[calories, protein, 40, 20, int(veg), int(gluten), int(dairy)]])

def recommend_foods_ml(foods, user_vector):
    food_matrix = np.array([food_to_vector(f) for f in foods])
    sim = cosine_similarity(user_vector, food_matrix)[0]
    ranked = sim.argsort()[::-1]
    return [foods[i] for i in ranked[:4]]