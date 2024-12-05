from count_request import count_requests_per_ip
from frequent_endpoint import most_frequent_endpoint
from suspicious_activity import detect_suspicious_activity
from save_results import save_results_to_csv

def main():
    log_file_path = "server_logs.txt"  # Replace with your log file path
    threshold = 10  # Configurable threshold for suspicious activity

    try:
        # Attempt to open the log file and read lines
        with open(log_file_path, 'r') as file:
            log_lines = file.readlines()

        # Step 1: Count Requests per IP
        ip_counts = count_requests_per_ip(log_lines)

        # Step 2: Find Most Accessed Endpoint
        most_accessed = most_frequent_endpoint(log_lines)

        # Step 3: Detect Suspicious Activity
        suspicious_activity = detect_suspicious_activity(log_lines, threshold)

        # Step 4: Display Results

        # Print Requests per IP
        print("\nRequests per IP:")
        print(f"{'IP Address':<20}{'Request Count':<15}")
        print("-" * 35)
        if ip_counts:
            for ip, count in ip_counts:
                print(f"{ip:<20}{count:<15}")
        else:
            print("No IP addresses found in the log file.")

        # Print Most Frequently Accessed Endpoint
        print("\nMost Frequently Accessed Endpoint:")
        print(f"{'Endpoint':<20}{'Access Count':<15}")
        print("-" * 35)
        if most_accessed:
            print(f"{most_accessed[0]:<20}{most_accessed[1]:<15}")
        else:
            print("No endpoints found in the log file.")

        # Print Suspicious Activity Detected
        print("\nSuspicious Activity Detected:")
        print(f"{'IP Address':<20}{'Failed Login Attempts':<25}")
        print("-" * 45)
        if suspicious_activity:
            for ip, count in suspicious_activity.items():
                print(f"{ip:<20}{count:<25}")
        else:
            print("No suspicious activity detected.")

        # Step 5: Save Results to CSV
        try:
            save_results_to_csv(ip_counts, most_accessed, suspicious_activity)
            print("\nResults successfully saved to 'log_analysis_results.csv'.")
        except Exception as e:
            print(f"Error while saving results to CSV: {e}")

    except FileNotFoundError:
        print(f"Error: The log file '{log_file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing the file '{log_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")
