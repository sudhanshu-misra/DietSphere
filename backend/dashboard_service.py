from backend.db import get_connection

def get_dashboard_data(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM adherence_logs WHERE user_id=%s", (user_id,))
    total_meals = cursor.fetchone()["total"]

    cursor.execute("""
        SELECT date, AVG(adherence_percent) as avg_adherence
        FROM adherence_logs
        WHERE user_id=%s
        GROUP BY date
        ORDER BY date
    """, (user_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "total_meals": total_meals,
        "history": rows
    }