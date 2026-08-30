# Architecture

Dokapi consists of several main components that interact to perform API hunting and port scanning tasks. Below is an overview of these components and their interactions.

## Main Components

### 1. `dokapi.py`
This is the entry point of the application. It orchestrates the overall functionality by:
- Accepting user input for the target URL or IP address.
- Asking whether to use a Tor proxy for the requests.
- Calling the `recon` module to hunt for APIs on the specified target.
- Calling the `ports` module to scan specified ports on the target.

### 2. `recon.py`
The `recon` module is responsible for hunting APIs. Its main functions include:
- Establishing a session using the `requests` library, optionally configured to use Tor proxies.
- Fetching the target URL and parsing the HTML to find script tags.
- Extracting potential API endpoints from the JavaScript files linked in the HTML.
- Saving the results to a CSV file if configured to do so.

### 3. `ports.py`
The `ports` module handles port scanning. Key functionalities include:
- Accepting a range of ports to scan from the user.
- Using a thread pool to concurrently check the status of each port on the target.
- Reporting open ports and saving the results to a CSV file if enabled.

### 4. `tor_proxy.py`
This module provides a method to retrieve proxy settings for Tor. It returns a dictionary with the necessary configuration for HTTP and HTTPS requests.

### 5. `settings.py`
The `settings` module defines configuration settings for the application, including:
- Enabling or disabling CSV output.
- Specifying the directory for saving reports.
- A method to ensure the reports folder exists.

### 6. `utils.py`
The `utils` module contains utility functions, including:
- A function to generate CSV filenames based on the scan type and target, ensuring the filenames are safe for the operating system.

## Interactions
- The `main` function in `dokapi.py` initiates the workflow by calling functions from `recon.py` and `ports.py`.
- The `recon` module interacts with the `requests` library to fetch data from the target, while the `ports` module uses the `socket` library to check port statuses.
- Both modules can save their results to CSV files using the functionality provided by `utils.py` and configurations from `settings.py`.
- The `tor_proxy` module is utilized by the `recon` module to route requests through the Tor network if specified by the user.

This architecture allows Dokapi to effectively perform its intended tasks of API discovery and port scanning in a structured manner.
