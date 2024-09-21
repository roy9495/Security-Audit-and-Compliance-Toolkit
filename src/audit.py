import subprocess
import platform
import os

def run_bash_script(script_name):
    """Executes a batch script using a corrected relative path"""
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get absolute path of current script (src/)
    script_path = os.path.join(base_dir, '..', 'scripts', script_name)  # Go up one level to find scripts/
    
    # Check if the script file exists
    if not os.path.exists(script_path):
        return f"Error: Script {script_path} not found!"
    
    # Execute the batch file
    result = subprocess.run(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Return any error messages if the script fails
    if result.returncode != 0:
        return f"Error: {result.stderr.decode('utf-8')}"
    
    return result.stdout.decode('utf-8')

def audit_firewall():
    """Runs the firewall audit"""
    return run_bash_script('audit_firewall.bat')

def audit_users():
    """Runs the user audit"""
    return run_bash_script('audit_users.bat')