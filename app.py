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
    
    # UNSAFE: Using f-strings for SQL query construction
    # Attacker can inject SQL: username = "admin' OR '1'='1"
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
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
    # UNSAFE: Passing user input directly to shell command
    # Attacker can inject commands: ip_address = "8.8.8.8; cat /etc/passwd"
    result = subprocess.run(
        f"ping -c 1 {ip_address}", 
        shell=True, 
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
    # UNSAFE: No validation on user-supplied filename
    # Attacker can access any file: filename = "../../etc/passwd"
    file_path = f"uploads/{filename}"
    
    try:
        with open(file_path, 'r') as f:
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
    
    # UNSAFE: String concatenation in SQL
    query = "SELECT * FROM products WHERE name LIKE '%" + search_term + "%'"
    cursor.execute(query)
    
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
    
    # UNSAFE: Direct interpolation without type checking
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
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
