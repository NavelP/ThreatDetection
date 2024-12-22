def detect_threat(log):
    """
    Analyzes a log entry to determine if it's a threat.
    Args:
        log (dict): A log entry containing details of an action.
    Returns:
        bool: True if a threat is detected, False otherwise.
    """
    # Rule-based detection logic
    if log["action"] == "login_attempt" and log["status"] == "failed":
        # Failed login attempts are suspicious
        return True
    if log["action"] == "file_upload" and log["source_ip"] in ["203.0.113.5"]:
        # Malicious IP uploading files
        return True
    return False
