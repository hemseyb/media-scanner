from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="media_scanner", user="hems", password="nFGV6saMTubzs8gBLaKJSDrVIxghA1zj", host="dpg-cvkfii8gjchc73cbk5m0-a", port="5432"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.media_data ORDER BY id ASC;")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)