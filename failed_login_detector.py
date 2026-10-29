# Project: Failed Login Detector
# Purpose: Identify repeated failed login attempts.
# Author: Stuti

sample_logs = [
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.20", "status": "success"},
    {"ip": "192.168.1.10", "status": "failed"},
    {"ip": "192.168.1.30", "status": "failed"},
]

failed_attempts = {}

for log in sample_logs:
    if log["status"] == "failed":
        ip = log["ip"]
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

threshold = 3

print("Failed Login Detection Report")
print("-" * 35)

for ip, count in failed_attempts.items():
    print(f"IP address: {ip} | Failed attempts: {count}")

    if count >= threshold:
        print("ALERT: Repeated failed login attempts detected!")
