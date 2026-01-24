def test_health_api(client):
    payload = {
        "weight": 70,
        "height": 175,
        "age": 22,
        "gender": "male",
        "activity": "moderate",
        "goal": "weight_loss"
    }

    response = client.post("/api/v1/health", json=payload)

    assert response.status_code == 200

    data = response.get_json()
    assert "BMI" in data
    assert "BMR" in data
    assert "TDEE" in data
    assert "Daily Calories" in data
    assert "Macros" in data
