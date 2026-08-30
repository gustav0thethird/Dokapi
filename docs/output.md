# Output

Dokapi provides various output formats and reporting capabilities to facilitate the analysis of reconnaissance data. The primary output formats include console output and CSV files.

## Console Output

When running Dokapi, the results of API hunts and port scans are displayed directly in the terminal. This immediate feedback allows users to quickly assess the findings without needing to navigate through files. The console output includes:

- **API Hunt Results**: After initiating an API hunt, the results are printed to the console, detailing the discovered APIs associated with the target.
- **Port Scan Results**: Following a port scan, the open ports are listed in the console. If no open ports are found, a message indicating this is displayed.

## CSV Output

Dokapi also supports exporting results to CSV files, which can be useful for further analysis or record-keeping. The CSV output includes:

- **Port Scan Results**: If the CSV output feature is enabled, the results of the port scan are saved in a CSV file. The file includes the following columns:
  - **Target**: The IP address or URL of the scanned target.
  - **Date**: The timestamp of when the scan was performed.
  - **Type**: The type of scan conducted (e.g., "Port Scan").
  - **Result**: The specific results of the scan, such as the open ports found.

### Enabling CSV Output

To enable CSV output, ensure that the `csv_output_enabled` setting is set to `True` in the configuration. The results will be saved in the specified directory, which defaults to `./Reports`. If the directory does not exist, it will be created automatically.

### File Naming

The CSV files are generated with a timestamped filename format, allowing for easy identification of when the scan was performed. The naming convention follows the pattern: `portscan_<target>_<timestamp>.csv`.

## Summary

Dokapi's output capabilities are designed to provide both immediate feedback through console output and long-term storage through CSV files. This dual approach allows users to efficiently analyze reconnaissance data in real-time while also maintaining records for future reference.
