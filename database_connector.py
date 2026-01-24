import sqlite3

def get_user_data(username):
    print(f"[*] Fetching data for user: {username}")
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: SQL Injection
    # Using an f-string allows an attacker to inject SQL commands.
    # Example input: "admin' OR '1'='1" would dump the whole table.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        print(f"DEBUG: Executing Query: {query}")
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Simulating malicious input
    get_user_data("admin' --")
