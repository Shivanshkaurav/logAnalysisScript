from collections import Counter
import re

def count_requests_per_ip(log_lines):
    """
    Count the number of requests made by each IP address.
    """
    ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'  # Matches IP addresses
    ips = [re.search(ip_pattern, line).group(1) for line in log_lines if re.search(ip_pattern, line)]
    ip_counts = Counter(ips)
    return ip_counts.most_common()

# Test block (optional)
if __name__ == "__main__":
    with open("server_logs.txt", 'r') as f:
        lines = f.readlines()
    print(count_requests_per_ip(lines))
