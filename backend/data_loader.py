import pandas as pd
import os

def load_food_dataset(filename="Indian_Food_Nutrition_Processed.csv"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, "datasets", filename)

    df = pd.read_csv(dataset_path)

    foods = []

    for i, row in df.iterrows():
        foods.append({
            "id": int(i),
            "name": str(row["Dish Name"]),
            "calories": float(row["Calories (kcal)"]),
            "protein": float(row["Protein (g)"]),
            "carbs": float(row["Carbohydrates (g)"]),
            "fats": float(row["Fats (g)"]),
            "veg": True,
            "gluten_free": True,
            "dairy_free": True
        })

    return foods