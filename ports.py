import socket
import datetime
import csv
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from settings import Settings
from utils import generate_csv_filename
from tqdm import tqdm

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))
        sock.close()
        return port if result == 0 else None
    except Exception:
        return None

def scan_ports(target):
    print(f"\n[!] Tip: Enter range like '20-1000' or '1-65535'!")

    port_range = input("\nEnter port range to scan (e.g., 20-1000): ").strip()
    ports = [80, 443, 8080, 8443]  # fallback default
    try:
        start, end = map(int, port_range.split('-'))
        if 0 <= start <= 65535 and 0 <= end <= 65535 and start <= end:
            ports = list(range(start, end + 1))
        else:
            raise ValueError
    except Exception:
        print("[!] Invalid range format. Using default ports (80,443,8080,8443).")

    total_ports = len(ports)
    open_ports = []

    print(f"\n[*] Scanning {total_ports} ports...")

    with ThreadPoolExecutor(max_workers=300) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in ports}
        with tqdm(total=total_ports, desc="Scanning", unit="port") as pbar:
            for future in as_completed(futures):
                port_result = future.result()
                if port_result:
                    open_ports.append(port_result)
                pbar.update(1)

    print("\n")

    if open_ports:
        print(f"[+] Open ports on {target}:")
        for port in sorted(open_ports):
            print(f"  - Port {port}")
    else:
        print("[!] No open ports found.")

    if Settings.csv_output_enabled:
        os.makedirs(Settings.csv_output_directory, exist_ok=True)
        filename = os.path.join(Settings.csv_output_directory, generate_csv_filename("portscan", target))
        with open(filename, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Target", "Date", "Type", "Result"])

            for port in sorted(open_ports):
                writer.writerow([
                    target,
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Port Scan",
                    f"Port {port}"
                ])

            if not open_ports:
                writer.writerow([
                    target,
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Port Scan",
                    "No open ports"
                ])

        print(f"\n[+] Results saved to {filename}")
