# Core Features

Dokapi is designed with a focus on privacy and modularity, providing users with a robust toolkit for reconnaissance tasks. Below are the core features of Dokapi:

- 🌐 **Full Tor-native Routing**  
  Dokapi automatically routes all network requests through Tor via `socks5h://127.0.0.1:9050`. This ensures that all traffic is anonymized, providing a DNS-safe environment for reconnaissance activities.

- 🧩 **Modular Scans**  
  Dokapi includes several modular scanning capabilities:
  - **Port Scanning**: A multi-threaded port scanner that identifies open ports on the target.
  - **Passive API/JS Endpoint Discovery**: This feature analyzes JavaScript to discover potential API endpoints without making direct requests to the target.

- 💻 **Interactive Shell**  
  The tool offers an interactive terminal shell that is styled and colorized for better user experience. Users can execute commands and receive live output, with results that can be exported for further analysis.

- 🛡️ **Privacy-Prioritized Design**  
  Dokapi is built with a strong emphasis on privacy. It does not collect telemetry data, has minimal dependencies, and allows for optional CSV output, enabling users to conduct offline analysis without compromising their privacy.

These features make Dokapi a valuable tool for ethical reconnaissance, allowing users to perform stealth audits, explore the dark web, or conduct red team operations effectively.
