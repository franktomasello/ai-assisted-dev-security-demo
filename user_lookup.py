import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # look up a user by their username from the users table
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()
    return str(user)