# VRV Security Assignment

This repository contains the implementation of a log analysis tool to detect suspicious activity from web server logs, specifically focusing on:

1. IP Address Request Count
2. Most Frequently Accessed Endpoint
3. Suspicious Activity Detection (Failed login attempts)

## Prerequisites

Before running the code, ensure you have the following installed:
- Python 3.6 or higher
- Required Python libraries (`pandas`)

To run the code:
  - python main.py

**Steps Implemented**

Step 1: Parse Web Server Logs
The first step is to parse the raw log data into structured format (IP address, request type, status code, etc.). This data will be processed to identify patterns.

Step 2: Analyze IP Address Request Count
The code counts the number of requests each IP address has made to the server. It collects all IP addresses from the log entries and calculates their frequency.

Step 3: Analyze Most Frequently Accessed Endpoint
The script identifies the most frequently accessed endpoint in the logs (e.g., /login, /home, /about).

Step 4: Detect Suspicious Activity
Suspicious activity is detected by checking failed login attempts. The code flags IP addresses that have more than 10 failed login attempts (HTTP status 401 or failure message "Invalid credentials").

Step 5: Output the Results
The script outputs:
    -The IP addresses with their request count.
    -The most frequently accessed endpoint.
    -Suspicious IP addresses with their failed login attempts.
