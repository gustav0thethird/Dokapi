# Output

Dokapi provides various output formats and reporting capabilities to facilitate the analysis of reconnaissance data. Below are the details regarding these features.

## Output Formats

### CSV Reporting

Dokapi supports CSV output for both API hunting and port scanning functionalities. When enabled, the results of these operations are saved in a structured CSV format, which can be easily imported into spreadsheet applications for further analysis.

- **Directory**: The default directory for CSV reports is `./Reports`.
- **File Naming**: The filenames are generated dynamically based on the type of scan and the target, ensuring clarity and organization.

### Console Output

In addition to CSV files, Dokapi provides real-time feedback in the console during operations. This includes:

- **API Hunt Results**: As the API hunt progresses, results are printed directly to the console, indicating the status of the hunt.
- **Port Scan Results**: Open ports are displayed in real-time, allowing users to monitor the scanning process.

## Reporting Capabilities

### API Hunt Reporting

When performing an API hunt, Dokapi outputs the results directly to the console. The specific details of the APIs discovered are not explicitly documented in the provided files, but the process is initiated with a prompt for the target URL or IP.

### Port Scan Reporting

The port scanning functionality includes comprehensive reporting:

- **Open Ports**: After scanning, the open ports are listed in the console output.
- **CSV Output**: If CSV output is enabled, the results of the port scan are saved in a CSV file, including:
  - Target IP or URL
  - Date and time of the scan
  - Type of scan performed
  - Results (open ports or a message indicating no open ports found)

### Error Handling

In the event of an error during the scanning processes, an error message is printed to the console, providing immediate feedback on the issue encountered.

## Summary

Dokapi's output formats and reporting capabilities are designed to provide users with both immediate feedback and long-term data storage options. The combination of console output and CSV reporting allows for flexible analysis and record-keeping of reconnaissance activities.
