import recon
import ports
import tor_proxy

def main():
    try:
        target = input("Enter target URL or IP: ").strip()
        use_tor = input("Use Tor proxy? (y/n): ").lower().startswith('y')

        proxies = tor_proxy.get_proxies() if use_tor else None

        print("\n[+] Starting API Hunt...")
        recon.hunt_apis(target, proxies)

        print("\n[+] Starting Port Scan...")
        ports.scan_ports(target)

    except Exception as e:
        print(f"[!] Error occurred: {e}")

if __name__ == "__main__":
    main()
