import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
DATASET_DIR = os.path.join(BASE_DIR, "datasets")


def load_food_dataset():
    path = os.path.join(DATASET_DIR, "Indian_Food_Nutrition_Processed.csv")
    df = pd.read_csv(path)

    foods = []

    for _, row in df.iterrows():
        foods.append({
            "name": str(row["Dish Name"]).strip(),
            "calories": float(row["Calories (kcal)"]),
            "protein": float(row["Protein (g)"]),
            "carbs": float(row["Carbohydrates (g)"]),
            "fats": float(row["Fats (g)"]),
            "veg": True,
            "gluten_free": True,
            "dairy_free": True
        })

    return foods


def load_ayurvedic_dataset():
    path = os.path.join(DATASET_DIR, "DietSphere_Ayurvedic_Dataset.csv")
    df = pd.read_csv(path)

    records = []

    for _, row in df.iterrows():
        records.append({
            "disease": str(row["Disease"]),
            "symptoms": str(row["Symptoms"]),
            "diet": str(row["Diet and Lifestyle Recommendations"]),
            "yoga": str(row["Yoga & Physical Therapy"]),
            "herbs": str(row["Ayurvedic Herbs Recommended"]),
            "dosha": str(row["Doshas"])
        })

    return records