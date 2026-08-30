# Dokapi Overview

Dokapi is a terminal-first reconnaissance toolkit designed for stealthy research and scanning, operating natively over Tor. It is built for users who prioritize operational security (OPSEC) in their reconnaissance activities.

![Dokapi](https://github.com/user-attachments/assets/5ab2b23b-6139-4c3d-822b-8fe05dc53650)

## Core Features

- **Full Tor-native routing**  
  Automatically routes requests through `socks5h://127.0.0.1:9050`, ensuring DNS-safe traffic anonymization.

- **Modular scans**  
  Includes:
  - Multi-threaded port scanning
  - Passive API and JavaScript endpoint discovery

- **Interactive shell**  
  Provides a styled, colorized terminal interface with modular command options and the ability to export results.

- **Privacy-prioritized design**  
  No telemetry is collected, minimal dependencies are required, and optional CSV output is available for offline analysis.

## Installation

**Requirements:**
- Python 3.7 or higher
- Tor daemon running on `127.0.0.1:9050`

**Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

**Run quick recon:**
```bash
python dokapi.py
```

**Start interactive shell:**
```bash
python dokapi_shell.py
```

## Output

- Live console output with color indicators
- Optional CSV reports saved to the `/Reports/` directory
- Automatic filename generation for organized audit logs

## Example Recon Flow

```text
Enter target URL or IP: example.com
Use Tor proxy? (y/n): y

[+] Starting API Hunt...
  - /api/status
  - /v1/users
  - /admin/panel

[+] Starting Port Scan...
  - 80 open
  - 443 open
```

## Folder Structure

```
Dokapi/
├── dokapi.py              # Main entrypoint
├── dokapi_shell.py        # Interactive shell
├── ports.py               # Multi-threaded port scanner
├── recon.py               # JS endpoint recon
├── tor_proxy.py           # SOCKS5H config
├── utils.py               # Helpers (e.g., filename generation)
├── settings.py            # Global config and flags
├── requirements.txt       # Dependencies
└── Reports/               # (Auto-created) CSV output
```

## Potential Roadmap

- [ ] HTTP header recon module  
- [ ] Subdomain/DNS recon support  
- [ ] Plugin loader for future extensions  
- [ ] Argparse CLI refactor  
- [ ] Test suite for module verification  

## Disclaimer

Dokapi is a research tool intended for ethical reconnaissance and OPSEC education. Misuse may violate laws in your jurisdiction; use responsibly and only on systems you own or have permission to audit.

## Links

- [GitHub Repository](https://github.com/Tahl0s/dokapi)
- [Website](https://duskcabin.club)
- [Tor Project](https://www.torproject.org)
