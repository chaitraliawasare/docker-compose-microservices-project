from flask import Flask
import psycopg2
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    db_status = check_db_connection()
    hostname = socket.gethostname()
    return f"{db_status} from {hostname}"
     
def check_db_connection():
    try:
        conn = psycopg2.connect(
            host="database",
            database="devopsdb",
            user="admin",
            password="password",
            port=5432
        )
        conn.close()
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
