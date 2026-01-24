import sys

class EmailRenderer:
    def generate_welcome_email(self, username):
        print(f"[*] Generating email for user: {username}")
        
        # VULNERABILITY: Cross-Site Scripting (XSS)
        # We are directly embedding user input into an HTML string without escaping.
        # Attacker Input: "<script>alert('XSS')</script>"
        # If this string is rendered in a browser, the script executes.
        html_content = f"""
        <html>
            <body>
                <h1>Welcome, {username}!</h1>
                <p>Thanks for joining our platform.</p>
            </body>
        </html>
        """
        
        print(f"Generated HTML:\n{html_content}")
        return html_content

if __name__ == "__main__":
    renderer = EmailRenderer()
    if len(sys.argv) > 1:
        renderer.generate_welcome_email(sys.argv[1])
    else:
        print("Usage: python template_render.py <username>")
