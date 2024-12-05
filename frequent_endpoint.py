from collections import Counter
import re

def most_frequent_endpoint(log_lines):
    """
    Find the most frequently accessed endpoint and its count.
    """
    try:
        endpoint_pattern = r'\"(?:GET|POST|PUT|DELETE) (/[^ ]*)'
        endpoints = [
            re.search(endpoint_pattern, line).group(1)
            for line in log_lines
            if re.search(endpoint_pattern, line)
        ]
        endpoint_counts = Counter(endpoints)
        most_accessed = endpoint_counts.most_common(1)
        return most_accessed[0] if most_accessed else ("N/A", 0)

    except AttributeError:
        print("Error: Failed to extract an endpoint from some log lines due to an invalid format.")
        return ("Error", 0)
    except Exception as e:
        print(f"An unexpected error occurred while processing endpoints: {e}")
        return ("Error", 0)

# Test block (optional)
if __name__ == "__main__":
    try:
        with open("server_logs.txt", 'r') as f:
            lines = f.readlines()
        result = most_frequent_endpoint(lines)
        print(result)
    except FileNotFoundError:
        print("Error: The file 'server_logs.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to read 'server_logs.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the log file: {e}")