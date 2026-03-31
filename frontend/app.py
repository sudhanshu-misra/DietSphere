from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

from services.api_client import (
    daily_plan,
    weekly_plan,
    log_meal_api,
    get_adherence_api,
    get_dashboard_data
)

from db import get_connection

app = Flask(__name__)
app.secret_key = "supersecret123"
app.config["DEBUG"] = True

bcrypt = Bcrypt(app)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password_raw = request.form.get("password")

        print("REGISTER DATA:", name, email)

        password = bcrypt.generate_password_hash(password_raw).decode("utf-8")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
                (name, email, password)
            )
            conn.commit()
            conn.close()

            print("REGISTER SUCCESS → redirecting to login")

            return redirect("/login")

        except Exception as e:
            print("REGISTER ERROR:", e)
            return render_template("register.html", error=str(e))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user["password"], password):
            session["user"] = user["email"]
            session["user_id"] = user["id"]
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/")
def root():
    return redirect("/dashboard")


'''@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    raw = get_dashboard_data(session["user_id"])
    print("DASHBOARD DATA:", raw)

    dashboard_data = {
    "health_metrics": raw.get("health_metrics", {
        "BMI": "-",
        "BMR": "-",
        "TDEE": "-",
        "Calories": "-"
    }),
    "diet_plan": raw.get("diet_plan", {}),
    "ayurveda": raw.get("ayurveda", {
        "disease": "N/A",
        "dosha": "N/A",
        "recommended_foods": [],
        "avoid_foods": [],
        "herbs": []
    }),
    "adherence": raw.get("adherence", {
        "total_meals": 0,
        "history": []
    })
}

    return render_template("dashboard.html", dashboard_data=dashboard_data)'''

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    raw = get_dashboard_data(session["user_id"])

    print("========== FRONTEND RECEIVED ==========")
    print(raw)
    print("=======================================")

    if not raw or not isinstance(raw, dict):
        return render_template("dashboard.html", error="Dashboard data not available")

    if "error" in raw:
        return render_template("dashboard.html", error=raw["error"])

    return render_template("dashboard.html", dashboard_data=raw)


@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")

    return render_template("profile.html", user=session["user"])


@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/login")

    result = None
    form_data = None

    if request.method == "POST":
        form_data = request.form.to_dict()
        result = daily_plan(form_data)

    return render_template("home.html", result=result, form_data=form_data)


@app.route("/weekly-plan", methods=["POST"])
def weekly():
    if "user" not in session:
        return redirect("/login")

    result = weekly_plan(request.form.to_dict())
    return render_template("weekly_plan.html", result=result)


@app.route("/log-meal", methods=["GET", "POST"])
def log_meal():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        result = log_meal_api(request.form.to_dict())

    return render_template("log_meal.html", result=result)


@app.route("/adherence", methods=["GET", "POST"])
def adherence():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        user_id = request.form.get("user_id")
        result = get_adherence_api(user_id)

    return render_template("adherence.html", result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)