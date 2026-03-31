from backend.food_data import FOOD_DB
from backend.ml_storage import save_food_ml_features

for f in FOOD_DB:
    save_food_ml_features(f)

print("Loaded Kaggle foods into ML table")