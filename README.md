# 🥗 DietSphere

DietSphere is a full-stack web application that generates personalized diet plans based on user inputs such as BMI, BMR, and TDEE. It combines backend logic, database integration, and a clean UI to deliver a real-world health tech solution.

---

## 🚀 Features

* 🔐 User Authentication (Register/Login with MySQL + Bcrypt)
* 📊 Personalized Dashboard (BMI, BMR, TDEE, Calories)
* 🥗 AI-Based Diet Plan Generation
* 🎨 Modern UI with Glassmorphism Design
* ⚡ Fast API-based communication (Flask backend)
* 🌐 Full-stack architecture (Frontend + Backend)

---

## 🛠️ Tech Stack

### Backend:

* Python
* Flask
* MySQL
* Flask-Bcrypt
* Flask-CORS

### Frontend:

* HTML
* CSS (Custom + Bootstrap)
* JavaScript (Fetch API)

---

## 📂 Project Structure

```
DietSphere/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── ml_recommender.py
│   └── ...
│
├── frontend/
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   └── js/
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sudhanshu-misra/DietSphere.git
cd DietSphere
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

Run this in MySQL:

```sql
CREATE DATABASE dietsphere;

USE dietsphere;

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL
);
```

---

### 4️⃣ Update DB config

In `backend/app.py`:

```python
password="your_mysql_password"
```

---

### 5️⃣ Run the app

```bash
cd backend
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/login
```

---

## 📸 Screenshots

* Login Page
* Register Page
* Dashboard with diet plan

*(Add screenshots here for better presentation)*

---

## 🧠 Future Improvements

* 📈 Track calorie history (charts)
* 👤 User profile (weight, height, goals)
* 🤖 ML-based diet recommendation improvements
* 📱 Mobile responsiveness enhancements

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Sudhanshu Misra**

* GitHub: https://github.com/sudhanshu-misra

---

⭐ If you like this project, give it a star!
