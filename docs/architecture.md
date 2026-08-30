# Architecture

Dokapi is structured to facilitate lightweight reconnaissance tasks while ensuring privacy through Tor integration. The architecture consists of several key components that interact seamlessly to provide a terminal-first recon experience.

## Main Components

### 1. **dokapi.py**
This is the main entry point for the application. It orchestrates the reconnaissance tasks by:
- Prompting the user for a target URL or IP address.
- Asking whether to use the Tor proxy for anonymity.
- Initiating the API hunting and port scanning processes by calling functions from the `recon` and `ports` modules.

### 2. **ports.py**
Responsible for performing port scans, this module includes:
- A function to scan specified ports on a target using multi-threading for efficiency.
- It reports open ports and can save the results to a CSV file if configured to do so.
- Utilizes a thread pool to handle multiple port scans concurrently, improving performance.

### 3. **recon.py**
This module focuses on discovering potential API endpoints on a target website. It:
- Uses the `requests` library to fetch the target's HTML content.
- Parses the HTML to find JavaScript files and extracts potential API endpoints using regular expressions.
- Saves the discovered endpoints to a CSV file if CSV output is enabled.

### 4. **tor_proxy.py**
This component provides the necessary proxy settings for routing traffic through Tor. It defines a function that returns the appropriate SOCKS5 proxy configuration, ensuring that all requests can be anonymized.

### 5. **settings.py**
This file manages global configuration settings for the application, including:
- Options for enabling CSV output and specifying the output directory.
- A method for generating filenames for CSV reports based on the scan type and target.

### 6. **utils.py**
Contains utility functions that support various operations within the application, such as generating CSV filenames based on the scan type and target.

## Interaction Flow

1. **User Input**: The user initiates the process by running `dokapi.py`, entering a target URL or IP, and choosing whether to use the Tor proxy.
2. **API Hunting**: The application calls `recon.hunt_apis()` to search for potential API endpoints, utilizing the Tor proxy if selected.
3. **Port Scanning**: Concurrently, `ports.scan_ports()` is invoked to check for open ports on the target.
4. **Output Generation**: Results from both the API hunt and port scan are displayed in the console and can be saved to CSV files in the specified directory.

## Folder Structure

The project is organized as follows:

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

## Conclusion

The architecture of Dokapi is designed to provide a streamlined and efficient reconnaissance tool that prioritizes user privacy through Tor. Each component plays a crucial role in ensuring that the application functions effectively while maintaining a focus on operational security.
