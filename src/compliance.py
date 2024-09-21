import subprocess

def run_compliance_check(script_name):
    """Executes a compliance script and returns the result"""
    script_path = f'../scripts/{script_name}'
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        return f"Error: {result.stderr.decode('utf-8')}"
    
    return result.stdout.decode('utf-8')

def iso27001_compliance():
    return run_compliance_check('compliance_iso27001.ps1')

def pci_dss_compliance():
    return run_compliance_check('compliance_pci_dss.ps1')

def hipaa_compliance():
    return run_compliance_check('compliance_hipaa.ps1')
