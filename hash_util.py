import hashlib
import sys

class PasswordManager:
    def store_password(self, password):
        print(f"[*] Hashing password for storage...")
        
        # VULNERABILITY: Weak Hashing Algorithm (MD5)
        # MD5 is vulnerable to collision attacks and is too fast for passwords.
        # It should be replaced with SHA-256 or bcrypt.
        hasher = hashlib.md5()
        
        hasher.update(password.encode('utf-8'))
        hashed_pw = hasher.hexdigest()
        
        print(f"Stored Hash: {hashed_pw}")
        return hashed_pw

    def verify_password(self, stored_hash, input_password):
        # Verify using the same weak algorithm
        check_hasher = hashlib.md5()
        check_hasher.update(input_password.encode('utf-8'))
        return check_hasher.hexdigest() == stored_hash

if __name__ == "__main__":
    pm = PasswordManager()
    pwd = sys.argv[1] if len(sys.argv) > 1 else "my_secret_pass"
    pm.store_password(pwd)
