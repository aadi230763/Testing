import sys
import os

LOG_DIRECTORY = "/var/log/app/"

def view_log_file(filename):
    print(f"[*] Attempting to read log file: {filename}")
    
    # Simulate a log directory if it doesn't exist for the demo
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY, exist_ok=True)
        with open(os.path.join(LOG_DIRECTORY, "system.log"), "w") as f:
            f.write("Normal system logs...")
    
    # VULNERABILITY: Path Traversal
    # We simply join the directory with the user input.
    # Attacker Input: "../../etc/passwd" (or any file outside the folder)
    file_path = os.path.join(LOG_DIRECTORY, filename)
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                print(f"--- LOG START ---\n{content}\n--- LOG END ---")
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    # Create a dummy secret file to prove the hack works
    with open("secret_config.txt", "w") as f:
        f.write("SUPER_SECRET_API_KEY=12345")

    if len(sys.argv) > 1:
        view_log_file(sys.argv[1])
    else:
        print("Usage: python log_viewer.py <filename>")
