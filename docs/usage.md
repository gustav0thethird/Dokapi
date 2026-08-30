# Usage

## Running Dokapi

To run Dokapi, you can use either the command line interface or the provided shell script. Follow the instructions below for both methods.

### Command Line Interface

1. **Open a terminal.**
2. **Navigate to the directory** where Dokapi is located.
3. **Run the following command:**

   ```bash
   python dokapi.py
   ```

4. **Input the required information:**
   - Enter the target URL or IP address when prompted.
   - Choose whether to use the Tor proxy by entering `y` for yes or `n` for no.

### Using the Shell Script

1. **Open a terminal.**
2. **Navigate to the directory** where Dokapi is located.
3. **Run the shell script:**

   For Windows:
   ```bash
   launch_dokapi.bat
   ```

   For Unix-based systems, you may need to create a similar script or run `dokapi.py` directly.

## Features

Dokapi provides the following features:

### API Hunting

- **Functionality:** The tool performs API hunting on the specified target.
- **Execution:** This is automatically initiated after entering the target URL or IP.

### Port Scanning

- **Functionality:** Dokapi scans for open ports on the specified target.
- **Execution:** This is automatically initiated after the API hunting process.

### Using Tor Proxy

- **Functionality:** You can choose to route your requests through the Tor network for anonymity.
- **Execution:** When prompted, enter `y` to enable Tor proxy usage.

## Output

The results of the API hunt and port scan will be displayed in the terminal. If configured, reports will be saved in the `Reports` directory.

## Error Handling

If any errors occur during execution, they will be printed to the terminal. Ensure that the target URL or IP is valid and that you have the necessary permissions to perform the scans.
