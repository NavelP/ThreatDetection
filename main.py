import sys
import time
from threat_detection import detect_threat
from response_handler import respond_to_threat

def monitor_logs_from_file(file_path):
    """
    Monitor logs from a file for demonstration purposes.
    """
    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                log = eval(line.strip())  # Convert string to Python dictionary
                print(f"Processing log: {log}")
                is_threat = detect_threat(log)
                if is_threat:
                    print(f"⚠️ Threat detected: {log}")
                    respond_to_threat(log)
                else:
                    print(f"✅ No threat detected: {log}")
                time.sleep(2)
    except FileNotFoundError:
        print(f"Log file {file_path} not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        monitor_logs_from_file(sys.argv[1])
    else:
        monitor_logs_from_file("logs.txt")