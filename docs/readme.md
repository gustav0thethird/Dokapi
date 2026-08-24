# Readme

## 🐙 Dokapi – Tor-Native Recon Toolkit  
> _“A terminal-first recon shell that speaks Tor natively. Built for those who prefer quiet steps.”_

![Dokapi](https://github.com/user-attachments/assets/5ab2b23b-6139-4c3d-822b-8fe05dc53650)

Dokapi is a lightweight reconnaissance CLI built for OPSEC-first research. It optionally routes all network traffic through Tor and comes with modular scanners for port scanning and passive API endpoint discovery via JavaScript analysis. The interactive shell offers a command set with live output and colorized feedback, ideal for stealth audits, dark web exploration, or red team recon.

---

### 🧠 Core Features

- 🌐 **Full Tor-native routing**  
  Automatically routes requests through `socks5h://127.0.0.1:9050` for DNS-safe traffic anonymization.

- 🧩 **Modular scans**  
  Includes:
  - Port scanning (multi-threaded)
  - Passive API/JS endpoint discovery

- 💻 **Interactive shell**  
  Launches a styled, colorized terminal shell with modular command options and exportable results.

- 🛡️ **Privacy-prioritized design**  
  No telemetry, minimal dependencies, and optional CSV output for offline analysis.

---

### 📦 Installation

**Requirements:**
- Python 3.7+
- Tor daemon running on `127.0.0.1:9050`

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

### 🚀 Usage

**Run quick recon:**
```bash
python dokapi.py
```

**Start interactive shell:**
```bash
python dokapi_shell.py
```

---

### 📁 Output

- Console-based live output with color indicators
- Optional CSV reports saved to `/Reports/` directory
- Automatic filename generation for clean audit logs

---

### 🧪 Example Recon Flow

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

---

### 🧱 Folder Structure

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

---

### 🗺️Potential Roadmap

- [ ] HTTP header recon module  
- [ ] Subdomain/DNS recon support  
- [ ] Plugin loader for future extensions  
- [ ] Argparse CLI refactor  
- [ ] Test suite for module verification

---

### ⚠️ Disclaimer

> Dokapi is a research tool built for ethical recon and OPSEC education.  
> Misuse may violate laws in your jurisdiction — use responsibly and only on systems you own or have permission to audit.

---

### 🔗 Links

- [GitHub Repository](https://github.com/Tahl0s/dokapi)
- [Website](https://duskcabin.club)
- [Tor Project](https://www.torproject.org)

---

Built for those who prefer quiet steps.
