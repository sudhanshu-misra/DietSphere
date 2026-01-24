import pandas as pd

def load_food_dataset(path="datasets/Indian_Food_Nutrition_Processed.csv"):
    df = pd.read_csv(path)

    foods = []
    for i, row in df.iterrows():
        foods.append({
            "id": int(i),
            "name": row["food_name"],
            "calories": float(row["calories"]),
            "protein": float(row["protein"]),
            "carbs": float(row["carbs"]),
            "fats": float(row["fat"]),
            "veg": True,
            "gluten_free": True,
            "dairy_free": True
        })
    return foods