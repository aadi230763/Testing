This is a testing repository for the project "Code-Janitor"

Link for the Guthub Repository is https://github.com/Preet2006/CODE-JANITOR

# Demo Vulnerable Application

⚠️ **WARNING: This repository contains intentionally vulnerable code for CodeJanitor demonstration purposes.**

## Vulnerabilities Included

### 1. SQL Injection (CRITICAL)
- **Location:** `app.py:11` - `login()` function
- **Risk Score:** 9.5/10
- **Issue:** F-strings used for SQL query construction with unsanitized user input
- **Exploit:** `username = "admin' OR '1'='1"`

### 2. Command Injection (HIGH)
- **Location:** `app.py:31` - `ping_server()` function  
- **Risk Score:** 8.7/10
- **Issue:** User input passed to shell command with `shell=True`
- **Exploit:** `ip_address = "8.8.8.8; cat /etc/passwd"`

### 3. Path Traversal (HIGH)
- **Location:** `app.py:51` - `read_user_file()` function
- **Risk Score:** 7.8/10
- **Issue:** No validation on user-supplied filename
- **Exploit:** `filename = "../../etc/passwd"`

## Usage for Demo

1. Push this repository to GitHub
2. Use CodeJanitor to scan: `yourusername/demo-vulnerable-app`
3. Watch as CodeJanitor:
   - Detects all 3+ vulnerabilities
   - Generates exploits to verify they're real
   - Creates secure patches
   - Submits pull requests

## Expected CodeJanitor Fixes

### SQL Injection Fix
```python
# Before (Vulnerable)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cursor.execute(query)

# After (Secure)
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
