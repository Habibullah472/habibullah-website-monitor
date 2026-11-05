import requests
import csv
from datetime import datetime

def check_website(url):
    timestamp = datetime.now().isoformat(timespec="seconds")

    try:
        response = requests.get(url, timeout=15)
        status = response.status_code
        response_time = round(response.elapsed.total_seconds(), 2)
        result = "ONLINE" if response.ok else "HTTP ERROR"

    except requests.RequestException as error:
        status = "FAILED"
        response_time = ""
        result = str(error)

    print("-" * 40)
    print(f"Website: {url}")
    print(f"Status: {status}")
    print(f"Response time: {response_time} seconds")
    print(f"Result: {result}")

    return [timestamp, url, status, response_time, result]

with open("websites.txt", "r", encoding="utf-8") as file:
    websites = [line.strip() for line in file if line.strip()]

if not websites:
    print("No websites found in websites.txt")
    raise SystemExit(1)

results = []

print("\nSAILHAB PROFESSIONAL WEBSITE MONITOR")
print("=" * 40)
print(f"Total websites: {len(websites)}")

for website in websites:
    results.append(check_website(website))

online = sum(1 for row in results if row[4] == "ONLINE")
failed = len(results) - online
success_rate = (online / len(results)) * 100

with open("monitor_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Website", "Status", "Response Time", "Result"])
    writer.writerows(results)

print("\n========== MONITORING SUMMARY ==========")
print(f"Total websites: {len(results)}")
print(f"Online: {online}")
print(f"Failed or errors: {failed}")
print(f"Success rate: {success_rate:.1f}%")
print("========================================")
print("REPORT SAVED: monitor_report.csv")
