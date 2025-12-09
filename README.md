DietSphere – AI-Powered Personalized Diet Recommendation System

DietSphere is a smart nutrition assistant that creates personalized diet plans tailored to an individual’s body metrics, goals, dietary restrictions, and food preferences.
It blends nutrition science, AI/ML models, rule-based logic, and NLP to deliver precise and dynamic diet recommendations.

#Table of Contents
1. About the Project
2. Key Features
3. System Architecture
4. How DietSphere Works
5. Tech Stack
6. Project Structure
7. Installation 8L Setup
8. API Endpoints
9. ML/NLP Models Used
10. Data Cleaning 81 Normalization
1 1. Restrictions 8L Substitutions Logic
12. Tracking User Adherence
13. Feedback Loop Mechanism
14. Future Scope
15. Contributors


#1. About the Project

DietSphere aims to simplify healthy eating by generating fully customized meal plans based on user inputs such as height, weight, age, gender, lifestyle, and health goals.
It adapts to user feedback, tracks adherence, understands natural language queries, and supports Indian + Ayurvedic food systems.


#2. Key Features

Personalized daily/weekly diet plans
BMR, TDEE & BMI calculation
Calorie & macronutrient optimization
Nutrition API integration (free sources)
Handles dietary restrictions (vegan, low-carb, gluten-free, diabetic-friendly, etc.)
Indian food database + Ayurvedic recommendations
NLP for understanding user queries
Tracks user adherence to assigned meals
Feedback loop for improving future diet plans
Fully containerized deployment with Docker

#3. System Architecture
Frontend (Flask)
        |
Backend API (Flask / FastAPI)
        |
Rule Engine + ML Models (Python)
        |
Nutrition Database (MySQL)
        |
External Nutrition APIs

#4. How DietSphere Works

User provides personal details & goals.
System cleans and normalizes data.
BMR is computed using Mifflin–St Jeor or Harris–Benedict.
TDEE is derived using activity multipliers.
Macros are distributed based on the goal (weight loss, muscle gain, etc.).
Nutrition database is filtered according to preferences & restrictions.
Portions are calculated to match calorie & macro targets.
NLP identifies user intents for custom requests.
User adherence logs refine future recommendations.

#5. Tech Stack
Frontend:
React, Tailwind/Material UI
Backend:
Flask 
AI/ML:
Python, Scikit-Learn, TensorFlow
Data Processing:
Pandas, NumPy
Database:
MySQL
Deployment:
Docker, Docker Compose
APIs:
Free food nutrition APIs (CalorieNinjas / Edamam free tier)

#6. Project Structure
DietSphere/
│── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   ├── utils/
│   ├── diet_logic/
│   └── models/
│
│── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── utils/
│
│── data/
│── notebooks/
│── docker-compose.yml
│── README.md

#7. Installation & Setup

##Backend Setup
cd backend
pip install -r requirements.txt
python app.py

##Frontend Setup
cd frontend
npm install
npm start

##Docker Setup
docker-compose up --build

#8. API Endpoints

| Method | Endpoint       | Description                     |
| ------ | -------------- | ------------------------------- |
| POST   | /generate-plan | Generate personalized diet plan |
| POST   | /calculate-bmi | Calculate BMI                   |
| POST   | /calculate-bmr | Compute BMR & TDEE              |
| GET    | /foods         | Get list of allowed foods       |
| POST   | /feedback      | Submit user feedback            |
| POST   | /adherence     | Track meals eaten/skipped       |



#9. ML/NLP Models Used

Simple text classification model for query understanding
Keyword extraction for restrictions & preferences
Rule-based engine for diet generation
(Optional) Recommendation model using similarity scoring for foods


#10. Data Cleaning & Normalization

Remove invalid entries (negative weight/height)
Convert units to metric system
Normalize categories (gender, goals, activity level)
Handle missing values via median imputation
Normalize features using MinMax or Z-score if ML is used


#11. Restrictions & Substitution Logic

Gluten → replaced with millet/rice options
Sugar-free → replaces sugary items with low GI alternatives
Low-carb → reduces grains & boosts proteins/fats
Dairy-free → substitutes milk/curd with lactose-free or soy options
Vegan → removes all animal-based items

#12. Tracking User Adherence

Users mark meals as eaten or skipped
Logs are stored in the database
Adherence % is calculated daily/weekly
Future plans adapt based on adherence behavior

#13. Feedback Loop Mechanism

User feedback collected after each plan
System learns likes/dislikes
Diet plan improves using preference patterns
Food suggestions become more personalized over time


#14. Future Scope

Workout recommendations
Wearable/health tracker integration
Real-time glucose-based meal suggestions
Weekly grocery planner
Advanced food recommendation ML models


#15. Contributors

Pratik Shende
Shivam Mantri
Sudhanshu Misra










