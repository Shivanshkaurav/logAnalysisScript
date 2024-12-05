# VRV Security Log Analysis Assignment

This repository contains a Python implementation for analyzing web server logs to detect suspicious activity, count IP requests, and find the most frequently accessed endpoints. The goal is to parse logs and perform various analyses, including detecting brute force login attempts, counting requests per IP, and identifying the most accessed endpoints.

## Project Steps

### 1. **Count Requests Per IP**
   - This script counts the number of requests made by each IP address in the server logs.
   - It outputs a list of IPs with their corresponding request counts.

### 2. **Most Frequently Accessed Endpoint**
   - The script identifies the most frequently accessed endpoint in the server logs (e.g., `/home`, `/login`, `/about`).
   - It outputs the endpoint with the highest access count.

### 3. **Detect Suspicious Activity**
   - The code detects suspicious activity by looking for IPs that have failed login attempts (HTTP status code `401` with message `"Invalid credentials"`).
   - It flags IP addresses that exceed a specified threshold (default is 10 failed login attempts).

### 4. **Save Results to CSV**
   - The results of the analysis (IP counts, most frequently accessed endpoint, and suspicious activity) are saved into a CSV file (`log_analysis_results.csv`).

## Requirements

Before running the code, ensure that you have Python 3.6+ installed along with the required libraries. The script uses the following libraries:

- `re` (Regular Expressions) for parsing log data.
- `collections.Counter` for counting IPs and endpoints.

To run the code:
  - python main.py
