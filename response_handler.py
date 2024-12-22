def respond_to_threat(log):
    """
    Responds to detected threats by taking appropriate action.
    Args:
        log (dict): A log entry identified as a threat.
    """
    if log["action"] == "login_attempt":
        print(f"🔒 Action Taken: IP {log['source_ip']} has been blocked.")
        block_ip(log["source_ip"])
    elif log["action"] == "file_upload":
        print(f"📢 Action Taken: Alert sent for suspicious file upload from {log['source_ip']}.")
        send_alert(log)

def block_ip(ip_address):
    """
    Simulates blocking an IP address.
    """
    print(f"Simulated Action: IP {ip_address} blocked successfully.")

def send_alert(log):
    """
    Simulates sending an alert about a threat.
    """
    print(f"Simulated Alert: Suspicious activity detected - {log}")
