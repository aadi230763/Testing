"""
Demo Vulnerable Application for CodeJanitor Testing
WARNING: This code contains intentional security vulnerabilities for demonstration purposes.
DO NOT use in production!
"""

import sqlite3
import os
import subprocess


# VULNERABILITY 1: SQL Injection (CRITICAL - Risk: 9.5/10)
def login(username, password):
    """
    User authentication function
    Vulnerable to SQL injection through unsanitized user input
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {"status": "success", "user": user[0]}
    return {"status": "failed"}


# VULNERABILITY 2: Command Injection (HIGH - Risk: 8.7/10)
def ping_server(ip_address):
    """
    Network diagnostic tool
    Vulnerable to command injection through shell=True
    """
    result = subprocess.run(
        ["ping", "-c", "1", ip_address], 
        capture_output=True,
        text=True
    )
    
    return {
        "output": result.stdout,
        "error": result.stderr,
        "return_code": result.returncode
    }


# VULNERABILITY 3: Path Traversal (HIGH - Risk: 7.8/10)
def read_user_file(filename):
    """
    File reader for user uploads
    Vulnerable to path traversal attacks
    """
    safe_path = os.path.abspath(os.path.join("uploads", filename))
    if not safe_path.startswith(os.path.abspath("uploads/")):
        raise ValueError("Invalid path")
    
    try:
        with open(safe_path, 'r') as f:
            content = f.read()
        return {"status": "success", "content": content}
    except FileNotFoundError:
        return {"status": "error", "message": "File not found"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Additional vulnerable function for demonstration
def search_products(search_term):
    """
    Product search function
    Another SQL injection vulnerability
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM products WHERE name LIKE ?"
    cursor.execute(query, ('%' + search_term + '%',))
    
    results = cursor.fetchall()
    conn.close()
    
    return results


def get_user_data(user_id):
    """
    Fetch user data by ID
    Vulnerable to SQL injection via numeric input
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    
    user = cursor.fetchone()
    conn.close()
    
    return user


if __name__ == "__main__":
    # Demo usage (DO NOT RUN WITH REAL USER INPUT!)
    print("Demo Vulnerable Application")
    print("=" * 50)
    
    # Example 1: Normal login
    result = login("admin", "password123")
    print(f"Login result: {result}")
    
    # Example 2: Network check
    ping_result = ping_server("8.8.8.8")
    print(f"Ping result: {ping_result['output'][:50]}...")
    
    # Example 3: File read
    file_result = read_user_file("example.txt")
    print(f"File result: {file_result}")