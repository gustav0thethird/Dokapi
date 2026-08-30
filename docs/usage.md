# Usage

## Running Dokapi

To run Dokapi, you can use either the command line interface or the interactive shell. Follow the instructions below for each method.

### Command Line Interface

1. **Open your terminal.**
2. **Navigate to the directory containing `dokapi.py`.**
3. **Run the script:**
   ```bash
   python dokapi.py
   ```
4. **Input the required information:**
   - Enter the target URL or IP address when prompted.
   - Choose whether to use the Tor proxy by entering `y` or `n`.

The script will then perform the following actions:
- Start an API hunt on the specified target.
- Conduct a port scan on the specified target.

### Interactive Shell

1. **Open your terminal.**
2. **Navigate to the directory containing `dokapi_shell.py`.**
3. **Run the shell script:**
   ```bash
   python dokapi_shell.py
   ```

The interactive shell provides a user-friendly interface for utilizing Dokapi's features. You can perform API hunts and port scans similar to the command line interface.

## Features

### API Hunt

- The API hunt feature scans the specified target for available APIs. 
- It utilizes the `recon` module to identify APIs.

### Port Scanning

- The port scanning feature checks for open ports on the specified target.
- It utilizes the `ports` module to perform the scan.

### Tor Proxy Support

- You can choose to run the scans through the Tor network for anonymity.
- The `tor_proxy` module manages the proxy settings.

## Output

- The results of the API hunt and port scan will be displayed in the terminal.
- If enabled, reports will be saved in the `Reports` directory.

## Error Handling

If an error occurs during execution, an error message will be displayed in the terminal. Ensure that the target URL or IP is valid and that you have the necessary permissions to scan the target.
