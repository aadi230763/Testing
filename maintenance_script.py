import os
import sys

def backup_logs(log_file_name):
    print("[*] Starting log backup process...")
    
    # VULNERABILITY: Command Injection
    # If 'log_file_name' contains characters like ";", "|", or "&&", 
    # it can execute arbitrary system commands.
    # Example input: "system.log; rm -rf /"
    command = f"tar -czf backup.tar.gz /var/logs/{log_file_name}"
    
    print(f"DEBUG: Running command -> {command}")
    
    # This executes the command in the shell
    exit_code = os.system(command)
    
    if exit_code == 0:
        print("Backup successful.")
    else:
        print("Backup failed.")

if __name__ == "__main__":
    # Simulating user input
    target = sys.argv[1] if len(sys.argv) > 1 else "app.log; echo 'HACKED'"
    backup_logs(target)
