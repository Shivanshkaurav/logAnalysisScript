from collections import Counter
import re

def count_requests_per_ip(log_lines):
    """
    Count the number of requests made by each IP address.
    """
    try:
        ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'  # Matches IP addresses
        ips = [
            re.search(ip_pattern, line).group(1)
            for line in log_lines
            if re.search(ip_pattern, line)
        ]
        ip_counts = Counter(ips)
        return ip_counts.most_common()

    except AttributeError:
        print("Error: Failed to extract an IP address from some log lines due to an invalid format.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while processing IPs: {e}")
        return []

# Test block (optional)
if __name__ == "__main__":
    try:
        with open("server_logs.txt", 'r') as f:
            lines = f.readlines()
        result = count_requests_per_ip(lines)
        print("Requests per IP:")
        for ip, count in result:
            print(f"{ip:<20} {count}")
    except FileNotFoundError:
        print("Error: The file 'server_logs.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied. Unable to read 'server_logs.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the log file: {e}")