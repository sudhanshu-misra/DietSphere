def test_ml_recommend(client):
    payload = {
        "preference": "veg",
        "goal": "weight_loss"
    }

    response = client.post("/api/v1/ml-recommend", json=payload)

    assert response.status_code == 200

    data = response.get_json()
    assert "recommended_foods" in data
    assert isinstance(data["recommended_foods"], list)
