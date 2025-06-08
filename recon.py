import requests
import datetime
import csv
import os
import re
from bs4 import BeautifulSoup
from settings import Settings
from utils import generate_csv_filename

def hunt_apis(target, proxies=None):
    session = requests.Session()
    if proxies:
        session.proxies.update(proxies)

    try:
        r = session.get(target, timeout=5)
        r.raise_for_status()
    except Exception as e:
        print(f"[!] Error fetching {target}: {e}")
        return

    soup = BeautifulSoup(r.text, 'html.parser')
    scripts = [s.get('src') for s in soup.find_all('script') if s.get('src')]

    endpoints = []

    for script_url in scripts:
        if not script_url.startswith('http'):
            script_url = target.rstrip('/') + '/' + script_url.lstrip('/')

        try:
            js = session.get(script_url, timeout=5)
            found = re.findall(r'(/[a-zA-Z0-9_\-\/]+)', js.text)
            for f in found:
                if '/api/' in f or '/v1/' in f or '/admin/' in f:
                    endpoints.append(f)
        except:
            continue

    endpoints = list(set(endpoints))

    if endpoints:
        print(f"[+] Found {len(endpoints)} potential API endpoints on {target}:")
        for ep in endpoints:
            print(f"  - {ep}")
    else:
        print("[!] No APIs found.")

    if Settings.csv_output_enabled:
        os.makedirs(Settings.csv_output_directory, exist_ok=True)
        filename = os.path.join(Settings.csv_output_directory, generate_csv_filename("apihunt", target))

        with open(filename, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Target", "Date", "Type", "Result"])

            for endpoint in endpoints:
                writer.writerow([
                    target,
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "API Hunt",
                    endpoint
                ])

            if not endpoints:
                writer.writerow([
                    target,
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "API Hunt",
                    "No APIs found"
                ])

        print(f"\n[+] Results saved to {filename}")
