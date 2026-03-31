from backend.food_data import FOOD_DB

def filter_foods(preferences, restrictions):
    filtered = []

    for food in FOOD_DB:
        if "vegetarian" in preferences and not food["veg"]:
            continue
        filtered.append(food)

    return filtered


def recommend_meals(foods):
    if not foods:
        return {"error": "No foods found"}

    return {
        "breakfast": foods[0]["name"],
        "lunch": foods[1 % len(foods)]["name"],
        "dinner": foods[2 % len(foods)]["name"],
        "snacks": foods[3 % len(foods)]["name"]
    }