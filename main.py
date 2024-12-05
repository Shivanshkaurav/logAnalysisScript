from count_request import count_requests_per_ip
from frequent_endpoint import most_frequent_endpoint
from suspicious_activity import detect_suspicious_activity
from save_results import save_results_to_csv

def main():
    log_file_path = "server_logs.txt"  # Replace with your log file path
    threshold = 10  # Configurable threshold for suspicious activity

    with open(log_file_path, 'r') as file:
        log_lines = file.readlines()

    # Step 1: Count Requests per IP
    ip_counts = count_requests_per_ip(log_lines)

    # Step 2: Find Most Accessed Endpoint
    most_accessed = most_frequent_endpoint(log_lines)

    # Step 3: Detect Suspicious Activity
    suspicious_activity = detect_suspicious_activity(log_lines, threshold)

    # Display Results
    print("Requests per IP:")
    for ip, count in ip_counts:
        print(f"{ip:<20} {count}")
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")
    
    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_activity.items():
        print(f"{ip:<20} {count}")
    
    # Step 4: Save Results to CSV
    save_results_to_csv(ip_counts, most_accessed, suspicious_activity)

if __name__ == "__main__":
    main()
