# Configuration

This document outlines the configuration settings and options available for Dokapi.

## Settings Overview

Dokapi's configuration is primarily managed through the `settings.py` file. The key settings include options for CSV output.

### CSV Output Settings

- **csv_output_enabled**: This boolean setting determines whether CSV output is enabled. By default, it is set to `False`.

- **csv_output_directory**: This string setting specifies the directory where CSV reports will be saved. The default directory is `./Reports`.

### Ensuring Reports Folder

The `ensure_reports_folder` class method is provided to create the reports directory if it does not already exist. It uses the `os.makedirs` function with the `exist_ok=True` parameter to ensure that the directory is created without raising an error if it already exists.

### CSV Filename Generation

Dokapi includes a utility function for generating CSV filenames based on the scan type and target URL. The function `generate_csv_filename(scan_type, target)` constructs a filename using the following format:

```
dokapi_{scan_type}_{safe_target}_{date}.csv
```

- **scan_type**: The type of scan being performed.
- **target**: The target URL, which is sanitized by removing `http://`, `https://`, and replacing slashes with underscores.
- **date**: The current date in the format `YYYY-MM-DD`.

This function ensures that the generated filenames are unique and informative, making it easier to identify reports.

## Example Usage

To enable CSV output and specify a custom directory, you can modify the settings as follows:

```python
Settings.csv_output_enabled = True
Settings.csv_output_directory = "./CustomReports"
Settings.ensure_reports_folder()
```

This configuration will enable CSV output and create a directory named `CustomReports` for storing the reports.
