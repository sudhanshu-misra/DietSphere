# DietSphere – AI-Powered Personalized Diet Recommendation System

DietSphere is a smart nutrition assistant that generates personalized diet plans based on a user’s body metrics, goals, dietary restrictions, and food preferences.

It combines nutrition science, machine learning, rule-based logic, natural language processing, and real-world food datasets (Kaggle) to deliver accurate and adaptive diet recommendations.

---

# Table of Contents
1. About the Project  
2. Key Features  
3. System Architecture  
4. How DietSphere Works  
5. Tech Stack  
6. Project Structure  
7. Installation & Setup  
8. API Endpoints  
9. ML/NLP Models Used  
10. Data Cleaning & Normalization  
11. Restrictions & Substitution Logic  
12. Tracking User Adherence  
13. Feedback Loop Mechanism  
14. Future Scope  
15. Contributors  

---

## 1. About the Project

DietSphere aims to simplify healthy eating by automatically creating customized meal plans using:

- Age, gender, height, weight  
- Activity level  
- Health goals (weight loss, gain, maintenance)  
- Dietary preferences & restrictions  

The system supports Indian food datasets sourced from Kaggle and is designed to expand toward Ayurvedic-based dietary recommendations.

It also tracks user adherence and improves recommendations over time using feedback.

---

## 2. Key Features

- Personalized daily & weekly diet plans  
- BMI, BMR, and TDEE calculations  
- Calorie & macronutrient optimization  
- Kaggle-based Indian food nutrition dataset  
- Handles dietary restrictions (vegetarian, gluten-free, dairy-free, etc.)  
- Rule-based + ML-based food recommendation  
- NLP support for basic user queries  
- Meal logging & adherence tracking  
- Feedback-driven recommendation improvement  
- Flask-based frontend using Jinja templates  

---

## 3. System Architecture

User (Browser)
|
Flask Frontend (Jinja Templates)
|
Flask Backend API
|
Rule Engine + ML Recommendation Logic
|
MySQL Database (Adherence + ML Features)
|
Kaggle Nutrition Dataset (CSV)


---

## 4. How DietSphere Works

1. User enters personal details & goals  
2. Data is validated, cleaned, and normalized  
3. BMR is calculated using Mifflin-St Jeor formula  
4. TDEE is computed using activity multipliers  
5. Calories are adjusted based on the goal  
6. Macronutrients are distributed  
7. Kaggle food dataset is filtered using preferences & restrictions  
8. ML model ranks foods based on calorie & protein similarity  
9. Portions are calculated to match targets  
10. Weekly plans are generated using rotation logic  
11. User meals are logged into MySQL  
12. Adherence % is calculated and stored  
13. Feedback refines future recommendations  

---

## 5. Tech Stack

### Frontend
- Flask  
- Jinja Templates (HTML only)  

### Backend
- Flask REST API  

### AI / ML
- Python  
- Scikit-Learn  

### Data Processing
- Pandas  
- NumPy  

### Database
- MySQL  

### Dataset
- Kaggle Indian Food Nutrition CSV  

---

## 6. Project Structure

DietSphere/
│
├── backend/
│ ├── app.py
│ ├── logic.py
│ ├── food_rules.py
│ ├── ml_recommender.py
│ ├── ml_storage.py
│ ├── populate_ml_features.py
│ ├── data_loader.py
│ ├── food_data.py
│ ├── adherence.py
│ ├── db.py
│ └── datasets/
│ └── Indian_Food_Nutrition_Processed.csv
│
├── frontend/
│ ├── app.py
│ ├── services/
│ │ └── api_client.py
│ └── templates/
│ ├── home.html
│ ├── weekly_plan.html
│ ├── log_meal.html
│ └── adherence.html
│
└── README.md

---

## 7. Installation & Setup

### Requirements

- Python 3.10+  
- MySQL Server  
- pip  

---

### Step 1: Start MySQL

---cmd

net start MySQL80

---

### Step 2: Create Databases & Tables

---mysql

CREATE DATABASE dietsphere;
USE dietsphere;

CREATE tables:

CREATE TABLE food_ml_features (
    food_id INT PRIMARY KEY,
    calories FLOAT,
    protein FLOAT,
    carbs FLOAT,
    fats FLOAT,
    veg TINYINT,
    gluten_free TINYINT,
    dairy_free TINYINT
);

CREATE TABLE adherence_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    date DATE,
    meal_type VARCHAR(20),
    food VARCHAR(100),
    portion_eaten_g INT,
    recommended_portion_g INT,
    adherence_percent FLOAT
);

---

### Step 3: Install Python packages

---cmd

pip install flask requests pandas numpy scikit-learn mysql-connector-python

---

### Step 4: Load Kaggle dataset into MySQL

---cmd

python -m backend.populate_ml_features

---

### Step 5: Runs Backend API

---cmd

python -m backend.app

---

Runs on:

---cmd

http://127.0.0.1:5000

---

### Step 6: Start Frontend

---cmd

cd frontend
python app.py

---

Runs on:

---cmd

http://127.0.0.1:8000

---

## 8. API Endpoints

Method                    Endpoint                       Description
 POST                    /diet-plan                  Generate daily diet plan
 POST                    /weekly-diet-plan           Generate weekly diet plan
 POST                    /log-meal                   Log eaten meals
 GET                     /user-adherence/<id>        Get adherence statistics
 POST                    /nlp-query                  Parse user query

---

## 9. ML / NLP Models Used

* Feature-based food similarity ranking

* Cosine similarity / distance scoring

* Rule-based filtering engine

* Keyword-based NLP intent detection

---

## 10. Data Cleaning & Normalization

* Removes invalid calorie/macronutrient values

* Converts numeric values to float

* Normalizes column names

* Maps Kaggle dataset fields to internal format

* Converts boolean attributes to numeric flags

---

## 11. Restrictions & Substitution Logic

* Vegetarian → removes meat

* Gluten-free → removes wheat-based items

* Dairy-free → removes milk products

* Low-calorie → prefers low energy density foods

* High-protein → ranks protein rich foods higher

---

## 12. Tracking User Adherence

* Users log meals using frontend form

* Stored in adherence_logs table

* Adherence % = (portion eaten / recommended portion) × 100

* Weekly average adherence calculated

---

## 13. Feedback Loop Mechanism

* Logs eating behavior

* Adjusts food ranking based on adherence

* Improves portion recommendations

* Learns long-term preferences

---

## 14. Future Scope

* Ayurvedic diet engine

* Diabetes-aware meal planning

* Mobile application

* Grocery planning system

* Deep learning-based recommendation model

* Wearable device integration

---

## 15. Contributors

* Shivam Mantri

* Sudhanshu Misra

* Pratik Shende

---