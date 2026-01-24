import os
import requests

def connect_to_payment_gateway():
    print("[*] Connecting to Stripe Payment Gateway...")
    
    # VULNERABILITY: Hardcoded Secrets
    # These credentials should be in environment variables, not code!
    api_key = "sk_live_51Mz...SECRET_KEY_HERE"
    admin_token = "ghp_1234567890abcdefghijklmn"
    db_password = "SuperSecretPassword123!"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "X-Admin-Token": admin_token
    }
    
    try:
        # Simulating a request
        print(f"DEBUG: Authenticating with key ending in ...{api_key[-4:]}")
        # response = requests.post("https://api.stripe.com/v1/charges", headers=headers)
        print("Connection successful (Simulated)")
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    connect_to_payment_gateway()
