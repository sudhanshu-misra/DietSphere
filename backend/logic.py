def calculate_bmr(w,h,a,g):
    return 10*w + 6.25*h - 5*a + (5 if g=="male" else -161)

def calculate_tdee(bmr, act):
    return bmr * 1.55

def adjust_calories(tdee, goal):
    return tdee - 500 if goal=="weight_loss" else tdee