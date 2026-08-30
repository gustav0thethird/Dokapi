# Architecture

Dokapi is structured to provide a modular and efficient reconnaissance toolkit that operates primarily through a command-line interface. The architecture is designed to facilitate interaction with the Tor network while performing various scanning tasks. Below is an overview of the main components and their interactions.

## Main Components

### 1. **dokapi.py**
This is the main entry point of the application. It handles user input for the target URL or IP address and whether to use the Tor proxy. It orchestrates the execution of the API hunting and port scanning functionalities by importing and utilizing the `recon` and `ports` modules.

### 2. **ports.py**
This module is responsible for performing port scans on the specified target. It includes:
- **scan_port**: A function that checks if a specific port is open by attempting to connect to it.
- **scan_ports**: This function manages the scanning process, allowing the user to specify a range of ports. It utilizes multi-threading to improve performance and reports open ports back to the user. If CSV output is enabled, it saves the results to a file.

### 3. **recon.py**
The `recon` module focuses on discovering potential API endpoints on the target website. It includes:
- **hunt_apis**: This function fetches the target page, extracts JavaScript files, and searches for API endpoints within those scripts. It also handles proxy settings if Tor is being used. Results can be saved to a CSV file if configured.

### 4. **tor_proxy.py**
This module provides the necessary proxy settings to route requests through the Tor network. The `get_proxies` function returns the appropriate SOCKS5 proxy configuration for HTTP and HTTPS requests.

### 5. **settings.py**
The `settings` module defines global configuration options, including:
- **csv_output_enabled**: A flag to enable or disable CSV report generation.
- **csv_output_directory**: Specifies the directory where reports will be saved.
- **generate_csv_filename**: A utility function that creates a timestamped filename for output files based on the scan type and target.

### 6. **utils.py**
This module contains helper functions, such as `generate_csv_filename`, which is used to create safe and timestamped filenames for CSV outputs.

## Interaction Flow

1. **User Input**: The user initiates the process by running `dokapi.py`, entering the target URL or IP, and deciding whether to use Tor for anonymity.
   
2. **Proxy Configuration**: If the user opts to use Tor, `tor_proxy.py` provides the necessary proxy settings.

3. **API Hunting**: The main script calls `recon.hunt_apis`, which fetches the target page, extracts JavaScript files, and identifies potential API endpoints.

4. **Port Scanning**: Concurrently, `ports.scan_ports` is invoked to scan the specified port range, reporting any open ports found.

5. **Output Generation**: Results from both the API hunt and port scan can be displayed in the console and optionally saved to CSV files in the specified directory.

## Folder Structure

The project follows a clear folder structure, which includes:

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

This architecture allows for modular development and easy extension of functionalities, making Dokapi a flexible tool for reconnaissance tasks.
