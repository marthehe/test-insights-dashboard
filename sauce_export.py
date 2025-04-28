# sauce_export.py - Pull test results from Sauce Labs API to CSV
import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

# 🔒 Load .env file for credentials
load_dotenv()
USERNAME = os.getenv("SAUCE_USERNAME")
ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")

if not USERNAME or not ACCESS_KEY:
    print("❌ Missing Sauce Labs credentials! Check your .env file.")
    exit()

# 🌐 Sauce Labs EU Central API URL
API_URL = f"https://api.eu-central-1.saucelabs.com/rest/v1/{USERNAME}/jobs?limit=10"

# 🛰️ Make the request
response = requests.get(API_URL, auth=(USERNAME, ACCESS_KEY))

if response.status_code != 200:
    print(f"❌ API call failed! Status: {response.status_code}")
    print(response.text)
    exit()

jobs = response.json()

# 📝 Write results to CSV
output_file = 'test-results.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['test_id', 'test_name', 'status', 'duration_seconds', 'date', 'browser', 'platform']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for job in jobs:
        start = job.get('start_time', 0)
        end = job.get('end_time', 0)
        readable_date = datetime.utcfromtimestamp(start).strftime('%Y-%m-%d') if start else 'N/A'
        duration = end - start if end else 0

        writer.writerow({
            'test_id': job.get('id'),
            'test_name': job.get('name', 'Unnamed Test'),
            'status': job.get('status', 'unknown'),
            'duration_seconds': duration,
            'date': readable_date,
            'browser': job.get('browser', 'N/A'),
            'platform': job.get('os', 'N/A')
        })

print(f"✅ Export complete! File saved as {output_file}")
