from collections import Counter
import re

def detect_suspicious_activity(log_lines, threshold=10):
    """
    Detect suspicious activity by identifying IPs with failed login attempts exceeding the threshold.
    """
    failed_login_pattern = r'(\d+\.\d+\.\d+\.\d+).* 401'
    failed_ips = [re.search(failed_login_pattern, line).group(1) for line in log_lines if re.search(failed_login_pattern, line)]
    failed_counts = Counter(failed_ips)
    suspicious = {ip: count for ip, count in failed_counts.items() if count > threshold}
    return suspicious

# Test block (optional)
if __name__ == "__main__":
    with open("server_logs.txt", 'r') as f:
        lines = f.readlines()
    print(detect_suspicious_activity(lines))
