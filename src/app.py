from flask import Flask, render_template, jsonify
import audit  # Import our audit logic
import compliance
import security_tools


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/firewall')
def api_firewall():
    firewall_result = audit.audit_firewall()
    return jsonify({"result": firewall_result})

@app.route('/api/users')
def api_users():
    user_result = audit.audit_users()
    return jsonify({"result": user_result})

# API routes for compliance tests
@app.route('/api/compliance/iso27001')
def api_iso27001():
    result = compliance.iso27001_compliance()
    return jsonify({"result": result})

@app.route('/api/compliance/pci-dss')
def api_pci_dss():
    result = compliance.pci_dss_compliance()
    return jsonify({"result": result})

@app.route('/api/compliance/hipaa')
def api_hipaa():
    result = compliance.hipaa_compliance()
    return jsonify({"result": result})

# API routes for security tasks
@app.route('/api/patch_management')
def api_patch_management():
    result = security_tools.patch_management()
    return jsonify({"result": result})

@app.route('/api/system_hardening')
def api_system_hardening():
    result = security_tools.system_hardening()
    return jsonify({"result": result})

@app.route('/api/privilege_escalation_test')
def api_privilege_escalation_test():
    result = security_tools.privilege_escalation_test()
    return jsonify({"result": result})

@app.route('/api/intrusion_detection')
def api_intrusion_detection():
    result = security_tools.intrusion_detection()
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
