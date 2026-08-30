# Usage

Dokapi is designed for reconnaissance tasks, allowing users to perform API hunting and port scanning through a Tor-native interface. Below are guidelines on how to run Dokapi effectively, including command examples and expected outputs.

## Running Dokapi

### Quick Recon

To initiate a quick reconnaissance task, run the following command:

```bash
python dokapi.py
```

This command will prompt you for a target URL or IP address and whether to use the Tor proxy.

### Starting the Interactive Shell

For a more interactive experience, you can start the Dokapi shell using:

```bash
python dokapi_shell.py
```

This will launch a styled terminal interface where you can execute various reconnaissance commands.

## Example Workflow

When you run `dokapi.py`, you will be prompted to enter a target and whether to use Tor:

```text
Enter target URL or IP: example.com
Use Tor proxy? (y/n): y
```

### Expected Outputs

1. **API Hunting**:
   After confirming the use of the Tor proxy, Dokapi will start hunting for APIs associated with the target. The output will display discovered endpoints:

```text
[+] Starting API Hunt...
  - /api/status
  - /v1/users
  - /admin/panel
```

2. **Port Scanning**:
   Following the API hunt, Dokapi will perform a port scan on the target. The output will indicate open ports:

```text
[+] Starting Port Scan...
  - 80 open
  - 443 open
```

## Output Formats

- **Live Console Output**: The results of the reconnaissance tasks will be displayed in real-time on the console with color indicators for better readability.
- **CSV Reports**: If enabled, results can be exported to CSV files, which are saved in the `/Reports/` directory. The filenames are automatically generated for organized audit logs.

## Folder Structure

The Dokapi repository contains the following key files:

```
Dokapi/
├── dokapi.py              # Main entrypoint for API hunting and port scanning
├── dokapi_shell.py        # Interactive shell interface
├── ports.py               # Multi-threaded port scanner implementation
├── recon.py               # JavaScript endpoint reconnaissance
├── tor_proxy.py           # Configuration for SOCKS5H proxy
├── utils.py               # Utility functions (e.g., filename generation)
├── settings.py            # Global configuration and flags
├── requirements.txt       # Dependencies
└── Reports/               # Directory for CSV output
```

## Important Notes

- Ensure that the Tor daemon is running on `127.0.0.1:9050` before executing the commands.
- Use responsibly and only on systems you own or have permission to audit, as misuse may violate laws in your jurisdiction.
