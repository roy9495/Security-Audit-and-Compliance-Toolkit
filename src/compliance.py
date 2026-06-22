import subprocess
import os

def run_compliance_check(script_name):
    """Executes a compliance script and returns the result"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, '..', 'scripts', script_name)
    
    if not os.path.exists(script_path):
        return f"Error: Script {script_path} not found!"
        
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        error_msg = result.stderr.decode('utf-8', errors='replace')
        # If output is empty, try to get stdout since returncode might be non-zero but contain stdout
        if not error_msg.strip():
            error_msg = result.stdout.decode('utf-8', errors='replace')
        return f"Error ({result.returncode}): {error_msg}"
    
    return result.stdout.decode('utf-8', errors='replace')

def iso27001_compliance():
    return run_compliance_check('compliance_iso27001.ps1')

def pci_dss_compliance():
    return run_compliance_check('compliance_pci_dss.ps1')

def hipaa_compliance():
    return run_compliance_check('compliance_hipaa.ps1')

