# Port Scanning

The port scanning functionality in Dokapi allows users to identify open ports on a specified target. This feature is implemented in the `ports.py` file and utilizes Python's `socket` library to perform the scans.

## Functionality Overview

### Scanning Process

1. **Input Port Range**: The user is prompted to enter a range of ports to scan. The expected format is `start-end`, where both `start` and `end` are integers between 0 and 65535. If the input is invalid, a default set of ports (80, 443, 8080, 8443) is used.

2. **Port Scanning**: The scanning is performed using a thread pool to enhance performance. The `scan_port` function attempts to connect to each port in the specified range. If the connection is successful (indicated by a result of 0), the port is considered open.

3. **Concurrency**: The scanning process employs `ThreadPoolExecutor` to manage multiple threads, allowing simultaneous scanning of ports. This is particularly useful for large ranges, as it significantly reduces the time required to complete the scan.

4. **Progress Tracking**: The `tqdm` library is used to provide a progress bar during the scanning process, giving users visual feedback on the scan's progress.

### Output

- **Open Ports**: After scanning, the program outputs a list of open ports found on the target. If no open ports are detected, a message indicating this is displayed.

- **CSV Output**: If enabled in the settings, the results of the scan are saved to a CSV file. The filename is generated based on the target and includes a timestamp. The CSV file contains the following columns:
  - Target
  - Date
  - Type (always "Port Scan")
  - Result (either the open port number or "No open ports")

### Code Structure

- **scan_port(target, port)**: This function attempts to connect to a specified port on the target. It returns the port number if the connection is successful; otherwise, it returns `None`.

- **scan_ports(target)**: This function orchestrates the port scanning process. It handles user input for the port range, manages the threading for scanning, collects results, and handles CSV output.

### Example Usage

To initiate a port scan, the user runs the `scan_ports` function with the desired target IP address or hostname. The user will be prompted to enter a port range, and the scan will commence.

### Error Handling

The implementation includes basic error handling for invalid input formats and exceptions that may occur during socket operations. If an error occurs, the user is notified, and the scan defaults to the predefined set of ports.

This functionality is crucial for network reconnaissance and security assessments, allowing users to identify potential vulnerabilities in their systems.
