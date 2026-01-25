from flask import Flask, request, render_template
from services.api_client import (
    daily_plan,
    weekly_plan,
    log_meal_api,
    get_adherence_api
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    form_data = None

    if request.method == "POST":
        form_data = request.form.to_dict()
        result = daily_plan(form_data)

    return render_template("home.html", result=result, form_data=form_data)

@app.route("/weekly-plan", methods=["POST"])
def weekly():
    data = request.form.to_dict()
    result = weekly_plan(data)
    return render_template("weekly_plan.html", result=result)

@app.route("/log-meal", methods=["GET", "POST"])
def log_meal():
    result = None

    if request.method == "POST":
        data = request.form.to_dict()
        result = log_meal_api(data)

    return render_template("log_meal.html", result=result)

@app.route("/adherence", methods=["GET", "POST"])
def adherence():
    result = None

    if request.method == "POST":
        user_id = request.form.get("user_id")
        result = get_adherence_api(user_id)

    return render_template("adherence.html", result=result)

if __name__ == "__main__":
    app.run(port=8000, debug=True)