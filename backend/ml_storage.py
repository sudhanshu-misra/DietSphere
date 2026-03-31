from backend.db import get_connection

def save_food_ml_features(food: dict):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO food_ml_features
        (food_id, calories, protein, carbs, fats, veg, gluten_free, dairy_free)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
            calories=VALUES(calories),
            protein=VALUES(protein),
            carbs=VALUES(carbs),
            fats=VALUES(fats),
            veg=VALUES(veg),
            gluten_free=VALUES(gluten_free),
            dairy_free=VALUES(dairy_free)
        """

        cursor.execute(query, (
            food["id"],
            food["calories"],
            food["protein"],
            food["carbs"],
            food["fats"],
            int(food["veg"]),
            int(food["gluten_free"]),
            int(food["dairy_free"])
        ))

        conn.commit()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def load_food_ml_features():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM food_ml_features")
        rows = cursor.fetchall()

        return rows

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()