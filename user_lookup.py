import sqlite3

def get_user_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # look up a user by their username from the users table
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
