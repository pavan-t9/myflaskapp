
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask app is running!</h1>"

@app.route("/db")
def db():
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        return "<h1>Successfully connected to PostgreSQL!</h1>"
    except Exception as e:
        return f"<h1>Database error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
