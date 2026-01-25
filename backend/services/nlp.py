def parse_text(text):
    text = text.lower()
    preference = "veg"
    goal = "maintenance"

    if "non veg" in text or "chicken" in text or "egg" in text:
        preference = "non-veg"
    if "lose" in text or "fat" in text:
        goal = "weight_loss"
    if "gain" in text or "muscle" in text:
        goal = "weight_gain"

    return preference, goal
