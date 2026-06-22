from flask import Flask, render_template, jsonify, request
import audit  # Import our audit logic
import compliance
import security_tools
import db  # Import our SQLite database module


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def home():
    return render_template('index.html')

# API routes for audits
@app.route('/api/firewall')
def api_firewall():
    result = audit.audit_firewall()
    db.save_audit_result("Firewall Audit", result)
    return jsonify({"result": result})

@app.route('/api/users')
def api_users():
    result = audit.audit_users()
    db.save_audit_result("User Audit", result)
    return jsonify({"result": result})

# API routes for compliance tests
@app.route('/api/compliance/iso27001')
def api_iso27001():
    result = compliance.iso27001_compliance()
    db.save_audit_result("ISO 27001 Compliance", result)
    return jsonify({"result": result})

@app.route('/api/compliance/pci-dss')
def api_pci_dss():
    result = compliance.pci_dss_compliance()
    db.save_audit_result("PCI-DSS Compliance", result)
    return jsonify({"result": result})

@app.route('/api/compliance/hipaa')
def api_hipaa():
    result = compliance.hipaa_compliance()
    db.save_audit_result("HIPAA Compliance", result)
    return jsonify({"result": result})

# API routes for security tasks
@app.route('/api/patch_management')
def api_patch_management():
    result = security_tools.patch_management()
    db.save_audit_result("Patch Management Check", result)
    return jsonify({"result": result})

@app.route('/api/system_hardening')
def api_system_hardening():
    result = security_tools.system_hardening()
    db.save_audit_result("System Hardening Check", result)
    return jsonify({"result": result})

@app.route('/api/privilege_escalation_test')
def api_privilege_escalation_test():
    result = security_tools.privilege_escalation_test()
    db.save_audit_result("Privilege Escalation Test", result)
    return jsonify({"result": result})

@app.route('/api/intrusion_detection')
def api_intrusion_detection():
    result = security_tools.intrusion_detection()
    db.save_audit_result("Intrusion Detection Check", result)
    return jsonify({"result": result})

# API routes for History Management
@app.route('/api/history')
def api_history():
    history = db.get_audit_results()
    return jsonify({"history": history})

@app.route('/api/history/delete/<int:item_id>', methods=['POST'])
def api_delete_history(item_id):
    db.delete_audit_result(item_id)
    return jsonify({"status": "success", "message": f"Record {item_id} deleted."})

@app.route('/api/history/clear', methods=['POST'])
def api_clear_history():
    db.clear_all_results()
    return jsonify({"status": "success", "message": "All history cleared."})

if __name__ == '__main__':
    # Initialize the SQLite database tables
    db.init_db()
    app.run(debug=True)

