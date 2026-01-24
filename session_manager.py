import random
import string
import sys

def generate_session_token(length=32):
    print(f"[*] Generating secure session token of length {length}...")
    
    characters = string.ascii_letters + string.digits
    
    # VULNERABILITY: Insecure Randomness
    # 'random' is a pseudo-random number generator (Mersenne Twister).
    # It is not cryptographically secure and can be predicted.
    # Should use 'secrets' module instead.
    token = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Generated Token: {token}")
    return token

def generate_temp_password():
    # Another instance of the same issue
    return random.randint(100000, 999999)

if __name__ == "__main__":
    generate_session_token()
    print(f"Temp OTP: {generate_temp_password()}")
