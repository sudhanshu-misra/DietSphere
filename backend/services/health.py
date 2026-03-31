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
        "protein_g": round((0.3 * calories) / 4, 1),
        "carbs_g": round((0.4 * calories) / 4, 1),
        "fats_g": round((0.3 * calories) / 9, 1)
    }
