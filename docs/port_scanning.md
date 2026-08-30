# Port Scanning

The port scanning functionality in Dokapi allows users to identify open ports on a specified target. This feature is implemented in the `ports.py` module and utilizes Python's `socket` library to perform the scans.

## Functionality Overview

### Scanning Process

1. **Input Port Range**: The user is prompted to enter a range of ports to scan. The input format should be `start-end` (e.g., `20-1000`). If the input is invalid, a default set of ports (80, 443, 8080, 8443) is used.

2. **Port Scanning**: The `scan_ports` function initiates the scanning process. It creates a list of ports based on the user input or defaults. The function then uses a `ThreadPoolExecutor` to scan multiple ports concurrently, improving efficiency.

3. **Port Check**: Each port is checked using the `scan_port` function, which attempts to establish a TCP connection to the target on the specified port. If the connection is successful (indicated by a return value of `0`), the port is considered open.

4. **Results Compilation**: After scanning, the results are compiled. If open ports are found, they are displayed to the user. If no open ports are detected, a corresponding message is shown.

5. **CSV Output**: If CSV output is enabled in the settings, the results are saved to a CSV file. The file includes the target, date, type of scan, and results for each port.

### Code Implementation

- **scan_port(target, port)**: This function attempts to connect to a specified port on the target. It returns the port number if successful or `None` if unsuccessful.

- **scan_ports(target)**: This function handles user input for the port range, manages the scanning process, and compiles results. It also handles CSV output if configured.

### Example Usage

To initiate a port scan, the user will be prompted to enter a port range. The following is a typical interaction:

```
[!] Tip: Enter range like '20-1000' or '1-65535'!
Enter port range to scan (e.g., 20-1000): 20-100
[*] Scanning 81 ports...
[+] Open ports on target:
  - Port 22
  - Port 80
```

### Output

The results of the scan are printed to the console. If CSV output is enabled, a file will be created in the specified directory, containing the scan results.

### Error Handling

The implementation includes basic error handling for invalid input formats and connection issues. If an invalid port range is entered, the user is notified, and the default ports are used instead.

### Dependencies

This functionality requires the following Python modules:
- `socket`
- `datetime`
- `csv`
- `os`
- `concurrent.futures`
- `tqdm`

### Configuration

CSV output can be configured through the `Settings` module. Ensure that the output directory exists or is created during the scan process.

This concludes the detailed explanation of the port scanning functionality in Dokapi. For further information, refer to the other documentation pages.
