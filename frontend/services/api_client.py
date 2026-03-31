import requests

BASE_URL = "http://127.0.0.1:5000"

def daily_plan(form_data):
    return requests.post(f"{BASE_URL}/diet-plan", json=form_data).json()

def weekly_plan(form_data):
    return requests.post(f"{BASE_URL}/weekly-diet-plan", json=form_data).json()

def log_meal_api(form_data):
    return requests.post(f"{BASE_URL}/log-meal", json=form_data).json()

def get_adherence_api(user_id):
    return requests.get(f"{BASE_URL}/user-adherence/{user_id}").json()

'''def get_dashboard_data(user_id):
    try:
        r = requests.get(f"{BASE_URL}/dashboard-data/{user_id}", timeout=10)
        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)

        if r.status_code != 200:
            return {"error": "Backend error"}

        return r.json()
    except Exception as e:
        print("API ERROR:", e)
        return {"error": "Backend unavailable"}'''
    
def get_dashboard_data(user_id):
    url = f"{BASE_URL}/api/v1/dashboard/{user_id}"

    try:
        res = requests.get(url, timeout=3)
    except requests.exceptions.ConnectionError:
        return {"error": "Backend server is not running"}

    if res.status_code != 200:
        return {"error": "Backend error"}

    return res.json()

