import requests

BASE_URL = "http://127.0.0.1:5000"

def daily_plan(data: dict):
    return requests.post(f"{BASE_URL}/diet-plan", json=data).json()

def weekly_plan(data: dict):
    return requests.post(f"{BASE_URL}/weekly-diet-plan", json=data).json()

def log_meal_api(data: dict):
    return requests.post(f"{BASE_URL}/log-meal", json=data).json()

def get_adherence_api(user_id):
    return requests.get(f"{BASE_URL}/user-adherence/{user_id}").json()