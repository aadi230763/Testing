import sys
import math

class PricingEngine:
    def __init__(self):
        self.base_rate = 100

    def calculate_custom_price(self, formula):
        print(f"[*] Calculating price using formula: {formula}")
        
        try:
            # VULNERABILITY: Code Injection (Eval)
            # The 'eval' function executes arbitrary Python code.
            # An attacker can pass: "__import__('os').system('echo PWNED')"
            # Real-world usage: Often found in dynamic reporting tools.
            price = eval(formula)
            
            print(f"Calculated Price: {price}")
            return price
        except Exception as e:
            print(f"Error executing formula: {e}")
            return None

if __name__ == "__main__":
    engine = PricingEngine()
    if len(sys.argv) > 1:
        engine.calculate_custom_price(sys.argv[1])
    else:
        # Default test case
        print("Usage: python math_service.py <formula_string>")m
