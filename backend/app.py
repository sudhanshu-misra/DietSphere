from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)


# ---------------- DB CONNECTION ----------------

db = mysql.connector.connect(
host="localhost",
user="root",
password="1234", 
database="dietsphere"
)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return jsonify({"message": "DietSphere Backend API is running"})

# --------------- REGISTER ----------------

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hashed_pw)
        )
        db.commit()
        return jsonify({"status": "registered"})
    except:
        return jsonify({"status": "error", "message": "User already exists"}), 400 
    

# ---------------- LOGIN (IMPORTANT) ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user["password"], password):
        return jsonify({
            "status": "success",
            "user_id": user["id"]
        })

    return jsonify({
        "status": "fail",
        "message": "Invalid credentials"
    }), 401
# ---------------- DASHBOARD ----------------
@app.route("/dashboard/<int:user_id>")
def dashboard(user_id):
    print("HTML DASHBOARD HIT")  # debug

    data = {
        "bmi": 22.86,
        "bmr": 1673.75,
        "tdee": 2594.31,
        "calories": 2094,
        "diet_plan": {
            "breakfast": "Paneer",
            "lunch": "Dal",
            "dinner": "Oats",
            "snacks": "Rice"
        }
    }

    return render_template("dashboard.html", data=data)


# ---------------- NLP ----------------
@app.route("/nlp-query", methods=["POST"])
def nlp_query():
    query = request.json.get("query", "").lower()

    return jsonify({
        "query": query,
        "intent": "diet_request"
    })

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)