import bcrypt
import sys

class PasswordManager:
    def store_password(self, password):
        print(f"[*] Hashing password for storage...")
        
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        print(f"Stored Hash: {hashed_pw}")
        return hashed_pw

    def verify_password(self, stored_hash, input_password):
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

if __name__ == "__main__":
    pm = PasswordManager()
    pwd = sys.argv[1] if len(sys.argv) > 1 else "my_secret_pass"
    stored_hash = pm.store_password(pwd)
    input_password = sys.argv[2] if len(sys.argv) > 2 else "my_secret_pass"
    print(f"Password is valid: {pm.verify_password(stored_hash, input_password)}")