import os

def read_report(report_name):
    base_dir = "/var/www/reports/"
    print(f"[*] Attempting to read report: {report_name}")
    
    # VULNERABILITY: Path Traversal (Directory Traversal)
    # Attacker can use "../" to move up directories and read sensitive files.
    # Example input: "../../../etc/passwd"
    file_path = base_dir + report_name
    
    try:
        # This will open whatever path is constructed
        with open(file_path, 'r') as file:
            content = file.read()
            print("Report Content Preview:")
            print(content[:100])
    except FileNotFoundError:
        print("Report not found.")
    except PermissionError:
        print("Permission denied.")

if __name__ == "__main__":
    # Simulating an attack to read the system password file
    read_report("../../../etc/passwd")
