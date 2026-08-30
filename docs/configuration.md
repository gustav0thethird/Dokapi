# Configuration

This document outlines the configuration settings and options available for Dokapi.

## Settings Overview

Dokapi's configuration is primarily managed through the `settings.py` file. The key settings include options for CSV output.

### CSV Output Settings

- **csv_output_enabled**: 
  - Type: Boolean
  - Default: `False`
  - Description: This setting determines whether CSV output is enabled. Set to `True` to enable CSV report generation.

- **csv_output_directory**: 
  - Type: String
  - Default: `"./Reports"`
  - Description: This specifies the directory where CSV reports will be saved. The directory will be created if it does not already exist.

### Reports Folder Management

Dokapi includes a method to ensure that the reports folder exists:

- **ensure_reports_folder()**: 
  - This class method checks for the existence of the `csv_output_directory` and creates it if it does not exist. It is advisable to call this method before attempting to generate CSV reports.

### CSV Filename Generation

Dokapi provides a utility function for generating CSV filenames based on the scan type and target:

- **generate_csv_filename(scan_type, target)**: 
  - Parameters:
    - `scan_type`: The type of scan being performed (e.g., port scan).
    - `target`: The target URL or IP address.
  - Returns: A string representing the filename formatted as `dokapi_{scan_type}_{safe_target}_{date}.csv`, where `safe_target` replaces `http://`, `https://`, and `/` with underscores, and `date` is the current date in `YYYY-MM-DD` format.

### Example Usage

To enable CSV output and ensure the reports folder exists, you can use the following code snippet:

```python
from settings import Settings

Settings.csv_output_enabled = True
Settings.ensure_reports_folder()
```

This configuration will prepare Dokapi to generate CSV reports in the specified directory.
