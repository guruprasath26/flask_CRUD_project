import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('db_web.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to execute a query that doesn't return data (e.g., INSERT, UPDATE, DELETE)
def execute_query(query, params=None):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.lastrowid  # Return the ID of the last inserted row
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        conn.close()

# Function to execute a query that returns data (e.g., SELECT)
def execute_select_query(query, params=None):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        data = cursor.fetchall()
        return data
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        conn.close()
