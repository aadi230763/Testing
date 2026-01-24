import bcrypt
import sys

class PasswordManager:
    def store_password(self, password):
        print(f"[*] Hashing password for storage...")
        
        # Use bcrypt for password hashing
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        print(f"Stored Hash: {hashed_pw.decode('utf-8')}")
        return hashed_pw

    def verify_password(self, stored_hash, input_password):
        # Verify using bcrypt
        return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

if __name__ == "__main__":
    pm = PasswordManager()
    pwd = sys.argv[1] if len(sys.argv) > 1 else "my_secret_pass"
    pm.store_password(pwd)