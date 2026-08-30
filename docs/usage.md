# Usage

Dokapi is designed for reconnaissance tasks, providing a terminal-first interface that integrates seamlessly with the Tor network for enhanced privacy. Below are guidelines on how to run Dokapi effectively, including command examples and expected outputs.

## Running Dokapi

### Quick Recon

To initiate a quick reconnaissance task, run the following command:

```bash
python dokapi.py
```

This command will prompt you for a target URL or IP address and whether to use the Tor proxy.

### Starting the Interactive Shell

For a more interactive experience, you can start the Dokapi shell:

```bash
python dokapi_shell.py
```

This launches a styled terminal interface where you can choose from various reconnaissance options.

## Example Recon Flow

When you run `dokapi.py`, you will be prompted as follows:

```text
Enter target URL or IP: example.com
Use Tor proxy? (y/n): y
```

If you choose to use the Tor proxy, the tool will proceed with the reconnaissance tasks. The expected output will look like this:

```text
[+] Starting API Hunt...
  - /api/status
  - /v1/users
  - /admin/panel

[+] Starting Port Scan...
  - 80 open
  - 443 open
```

### Output Details

- **Live Console Output**: The results of the reconnaissance tasks will be displayed in real-time with color indicators for better readability.
- **CSV Reports**: If enabled, results can be saved as CSV files in the `/Reports/` directory, with filenames generated automatically for easy audit logging.

## Folder Structure

Understanding the folder structure can help you navigate the Dokapi project:

```
Dokapi/
├── dokapi.py              # Main entrypoint for reconnaissance tasks
├── dokapi_shell.py        # Interactive shell for user interaction
├── ports.py               # Multi-threaded port scanner
├── recon.py               # JavaScript endpoint reconnaissance
├── tor_proxy.py           # Configuration for SOCKS5H proxy
├── utils.py               # Helper functions (e.g., filename generation)
├── settings.py            # Global configuration and flags
├── requirements.txt       # Dependencies
└── Reports/               # Directory for CSV output
```

## Conclusion

Dokapi provides a straightforward and effective way to conduct reconnaissance tasks while prioritizing user privacy through Tor integration. Use the commands and examples provided to get started with your reconnaissance efforts.
