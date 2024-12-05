from collections import Counter
import re

def most_frequent_endpoint(log_lines):
    """
    Find the most frequently accessed endpoint and its count.
    """
    endpoint_pattern = r'\"(?:GET|POST|PUT|DELETE) (/[^ ]*)'
    endpoints = [re.search(endpoint_pattern, line).group(1) for line in log_lines if re.search(endpoint_pattern, line)]
    endpoint_counts = Counter(endpoints)
    most_accessed = endpoint_counts.most_common(1)
    return most_accessed[0] if most_accessed else ("N/A", 0)

# Test block (optional)
if __name__ == "__main__":
    with open("server_logs.txt", 'r') as f:
        lines = f.readlines()
    print(most_frequent_endpoint(lines))
