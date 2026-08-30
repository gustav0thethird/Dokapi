# API Hunting

The API hunting feature in Dokapi is designed to identify potential API endpoints on a specified target. This functionality leverages web scraping techniques to analyze the target's HTML content and extract relevant API paths.

## How It Works

1. **Session Initialization**: The process begins by creating a session using the `requests` library. If proxy settings are provided, they are applied to the session.

2. **Fetching Target Content**: The target URL is accessed with a GET request. If the request fails, an error message is printed, and the process is halted.

3. **HTML Parsing**: Upon successfully retrieving the target's content, the HTML is parsed using `BeautifulSoup`. The script searches for all `<script>` tags and collects their `src` attributes, which may contain links to JavaScript files.

4. **Endpoint Extraction**: For each script URL found:
   - If the URL is relative, it is converted to an absolute URL based on the target.
   - A GET request is made to fetch the JavaScript content.
   - Regular expressions are used to search for patterns that likely represent API endpoints (e.g., paths containing `/api/`, `/v1/`, or `/admin/`).

5. **Unique Endpoints**: The identified endpoints are stored in a list, ensuring that duplicates are removed.

6. **Results Display**: The number of potential API endpoints found is printed. If no endpoints are detected, a corresponding message is displayed.

7. **CSV Output**: If CSV output is enabled in the settings, the results are saved to a CSV file. The file includes the target URL, the current date and time, the type of hunt, and the discovered endpoints. If no endpoints were found, this is also recorded in the CSV.

This feature provides a systematic approach to discovering APIs that may not be explicitly documented, aiding in reconnaissance and security assessments.
