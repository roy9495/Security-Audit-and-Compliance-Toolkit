import subprocess

def run_powershell_script(script_name):
    """Executes a PowerShell script and returns the result"""
    script_path = f'../scripts/{script_name}'
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        return f"Error: {result.stderr.decode('utf-8')}"
    
    return result.stdout.decode('utf-8')

def patch_management():
    return run_powershell_script('patch_management.ps1')

def system_hardening():
    return run_powershell_script('system_hardening.ps1')

def privilege_escalation_test():
    return run_powershell_script('privilege_escalation_test.ps1')

def intrusion_detection():
    return run_powershell_script('intrusion_detection.ps1')
