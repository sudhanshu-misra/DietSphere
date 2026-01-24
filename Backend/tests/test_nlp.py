def test_nlp_api(client):
    payload = {
        "text": "I want veg high protein food for weight loss"
    }

    response = client.post("/api/v1/nlp", json=payload)

    assert response.status_code == 200

    data = response.get_json()
    assert "preference" in data
    assert "goal" in data
    assert "recommended_foods" in data
