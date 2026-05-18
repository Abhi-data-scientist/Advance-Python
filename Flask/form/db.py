import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         # apna MySQL username
        password="mr.abhi1149",         # apna MySQL password
        database="python_db"
    )
    return connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return 0 # Already exist

    # Insert new user
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    conn.commit()
    conn.close()
    return "success"

def search(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from users where email = %s and password = %s", (email, password))
    existed_user = cursor.fetchone()

    if existed_user:
        return 1
    else:
        return 0