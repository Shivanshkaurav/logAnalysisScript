from collections import Counter
import re

def detect_suspicious_activity(log_lines, threshold=10):
    """
    Detect suspicious activity by identifying IPs with failed login attempts exceeding the threshold.
    """
    try:
        failed_login_pattern = r'(\d+\.\d+\.\d+\.\d+).* 401'
        failed_ips = [
            re.search(failed_login_pattern, line).group(1)
            for line in log_lines
            if re.search(failed_login_pattern, line)
        ]
        failed_counts = Counter(failed_ips)
        suspicious = {ip: count for ip, count in failed_counts.items() if count > threshold}
        return suspicious

    except AttributeError:
        print("Error: Failed to extract IP addresses from some log lines due to an invalid format.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while detecting suspicious activity: {e}")
        return {}

# Test block (optional)
if __name__ == "__main__":
    try:
        with open("server_logs.txt", 'r') as f:
            lines = f.readlines()
        result = detect_suspicious_activity(lines)
        print(result)
    except FileNotFoundError:
        print("Error: The file 'server_logs.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to read 'server_logs.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the log file: {e}")