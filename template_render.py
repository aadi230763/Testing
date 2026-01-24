import sys
from jinja2 import Template

class EmailRenderer:
    def generate_welcome_email(self, username):
        print(f"[*] Generating email for user: {username}")
        
        template = Template("""
        <html>
            <body>
                <h1>Welcome, {{ username | e }}!</h1>
                <p>Thanks for joining our platform.</p>
            </body>
        </html>
        """)
        
        html_content = template.render(username=username)
        
        print(f"Generated HTML:\n{html_content}")
        return html_content

if __name__ == "__main__":
    renderer = EmailRenderer()
    if len(sys.argv) > 1:
        renderer.generate_welcome_email(sys.argv[1])
    else:
        print("Usage: python template_render.py <username>")