# Core Features

- 🌐 **Full Tor-native routing**  
  Dokapi automatically routes all requests through `socks5h://127.0.0.1:9050`, ensuring DNS-safe traffic anonymization. This feature is essential for users prioritizing privacy and stealth in their reconnaissance activities.

- 🧩 **Modular scans**  
  Dokapi includes several modular scanning capabilities:
  - **Port scanning**: A multi-threaded port scanner that efficiently identifies open ports on the target.
  - **Passive API/JS endpoint discovery**: This feature analyzes JavaScript to discover potential API endpoints without making direct requests, enhancing stealth during reconnaissance.

- 💻 **Interactive shell**  
  The interactive shell provides a styled, colorized terminal interface that allows users to execute various commands. It features:
  - Modular command options for different types of scans.
  - Live output with colorized feedback, making it easier to interpret results.
  - The ability to export results, including optional CSV output for offline analysis.

- 🛡️ **Privacy-prioritized design**  
  Dokapi is designed with privacy in mind, featuring:
  - No telemetry or data collection.
  - Minimal dependencies to reduce the attack surface.
  - Optional CSV output for users who prefer to analyze results offline.

These core features make Dokapi a robust tool for ethical reconnaissance and operational security (OPSEC) education, suitable for users engaged in stealth audits, dark web exploration, or red team operations.
