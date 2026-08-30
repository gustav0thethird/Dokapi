# Output

Dokapi generates output in two primary formats: live console feedback and optional CSV reports.

## Live Console Feedback

When using Dokapi, users receive real-time feedback directly in the terminal. The interactive shell provides colorized output to enhance readability and user experience. This live feedback includes:

- **Status Updates**: As scans progress, users see updates indicating the current actions being performed, such as API hunting and port scanning.
- **Results Display**: Detected endpoints and open ports are displayed in a clear format, allowing users to quickly assess the findings.

### Example Console Output

An example of the console output during a reconnaissance session might look like this:

```text
Enter target URL or IP: example.com
Use Tor proxy? (y/n): y

[+] Starting API Hunt...
  - /api/status
  - /v1/users
  - /admin/panel

[+] Starting Port Scan...
  - 80 open
  - 443 open
```

## CSV Report Generation

Dokapi also supports optional CSV report generation for users who prefer to save their findings for offline analysis. The CSV reports are automatically generated and saved in the `/Reports/` directory. Key features of the CSV output include:

- **Automatic Filename Generation**: Each report is saved with a unique filename based on the scan type and target, ensuring organized and easily retrievable logs.
- **Structured Data**: The CSV files contain structured data that can be easily imported into spreadsheet applications for further analysis.

### Example CSV Output

The CSV report may include entries similar to the following:

```csv
Endpoint, Status
/api/status, 200
/v1/users, 200
/admin/panel, 403
```

## Summary

Dokapi's output capabilities are designed to provide users with immediate feedback during reconnaissance tasks while also allowing for detailed offline analysis through CSV reports. This dual-output approach enhances the tool's usability for various operational needs.
