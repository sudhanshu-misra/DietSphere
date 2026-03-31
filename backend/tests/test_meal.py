def test_auto_meal_plan(client):
    payload = {
        "weight": 70,
        "height": 175,
        "age": 22,
        "gender": "male",
        "activity": "moderate",
        "goal": "weight_loss",
        "preference": "veg"
    }

    response = client.post("/api/v1/auto-meal-plan", json=payload)

    assert response.status_code == 200

    data = response.get_json()
    assert "daily_calories" in data
    assert "recommended_foods" in data
