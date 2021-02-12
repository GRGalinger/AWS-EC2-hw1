import sqlite3

try:
    conn = sqlite3.connect('database.db')
    query = '''CREATE TABLE users (
                                firstname TEXT NOT NULL,
                                lastname TEXT NOT NULL,
                                username TEXT NOT NULL,
                                email TEXT NOT NULL,
                                password TEXT NOT NULL);'''

    cursor = conn.cursor()
    print("Successfully connected to SQLite")
    cursor.execute(query)
    conn.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (conn):
        conn.close()
        print("sqlite connection is closed")