# Architecture

Dokapi is structured around several key components that interact to perform API hunting and port scanning tasks. Below is an overview of these components and their interactions.

## Main Components

### 1. `dokapi.py`
This is the entry point of the application. It orchestrates the execution of the main functionalities by:
- Prompting the user for a target URL or IP address.
- Asking whether to use a Tor proxy for the operations.
- Calling the `recon.hunt_apis` function to search for APIs on the target.
- Calling the `ports.scan_ports` function to perform a port scan on the target.

### 2. `recon.py`
This module is responsible for hunting APIs on the specified target. It performs the following tasks:
- Establishes a session using the `requests` library, optionally utilizing Tor proxies.
- Fetches the HTML content of the target and parses it using BeautifulSoup.
- Extracts script URLs and attempts to find potential API endpoints within the JavaScript files.
- Outputs the found endpoints and can save the results in CSV format if enabled.

### 3. `ports.py`
This module handles the port scanning functionality. It includes:
- A function to scan individual ports (`scan_port`), which attempts to connect to each port on the target.
- A function to manage the overall port scanning process (`scan_ports`), which:
  - Prompts the user for a range of ports to scan.
  - Utilizes a thread pool to scan multiple ports concurrently.
  - Outputs the results of the scan and can save them in CSV format if enabled.

### 4. `tor_proxy.py`
This module provides functionality to retrieve Tor proxy settings. It defines a single function:
- `get_proxies`, which returns a dictionary of proxy settings for HTTP and HTTPS connections.

### 5. `settings.py`
This module contains configuration settings for the application, including:
- A flag to enable or disable CSV output.
- A directory path for saving reports.
- A method to ensure the reports directory exists.

### 6. `utils.py`
This module contains utility functions used across the application. Notably:
- `generate_csv_filename`, which creates a safe and timestamped filename for CSV reports based on the scan type and target.

## Interactions
- The `dokapi.py` file serves as the main controller, invoking functions from `recon.py` and `ports.py` based on user input.
- `recon.py` and `ports.py` can both generate CSV reports using the utility functions defined in `utils.py` and respect the settings defined in `settings.py`.
- The use of Tor proxies is managed through `tor_proxy.py`, which integrates seamlessly with the API hunting and port scanning processes.

This architecture allows for modular development and easy maintenance, enabling the addition of new features or modifications to existing functionalities without significant disruption to the overall system.
