import secrets
import string
import sys

def generate_session_token(length=32):
    print(f"[*] Generating secure session token of length {length}...")
    
    characters = string.ascii_letters + string.digits
    
    token = ''.join(secrets.choice(characters) for _ in range(length))
    
    print(f"Generated Token: {token}")
    return token

def generate_temp_password():
    return secrets.randbelow(900000) + 100000

if __name__ == "__main__":
    generate_session_token()
    print(f"Temp OTP: {generate_temp_password()}")