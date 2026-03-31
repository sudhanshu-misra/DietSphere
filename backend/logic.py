def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)


def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender.lower() == "male":
        return round(10 * weight_kg + 6.25 * height_cm - 5 * age + 5, 2)
    else:
        return round(10 * weight_kg + 6.25 * height_cm - 5 * age - 161, 2)


def calculate_tdee(bmr, activity_level):
    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }
    return round(bmr * factors.get(activity_level, 1.2), 2)


def adjust_calories(tdee, goal):
    if goal == "weight_loss":
        return tdee - 500
    elif goal == "weight_gain":
        return tdee + 400
    return tdee


def macro_split(calories):
    return {
        "protein_g": round((0.30 * calories) / 4, 2),
        "carbs_g": round((0.40 * calories) / 4, 2),
        "fats_g": round((0.30 * calories) / 9, 2)
    }