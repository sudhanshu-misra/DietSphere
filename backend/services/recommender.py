import pandas as pd
from data.food_data import food_dataset

def recommend_food(model, encoder, preference, goal):
    results = []
    goal_encoded = encoder.transform([goal])[0]

    for food in food_dataset:
        is_veg = 1 if food["type"] == "veg" else 0

        if preference == "veg" and is_veg == 0:
            continue
        if preference == "non-veg" and is_veg == 1:
            continue

        features = pd.DataFrame([{
            "protein": food["protein"],
            "calories": food["calories"],
            "is_veg": is_veg,
            "goal_encoded": goal_encoded
        }])

        if model.predict(features)[0] == 1:
            results.append(food)

    return results
