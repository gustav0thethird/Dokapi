# API Hunting

The API hunting feature in Dokapi is designed to identify potential API endpoints on a specified target website. This functionality leverages web scraping techniques to extract relevant information from the target's HTML content.

## How It Works

1. **Session Initialization**: 
   The feature begins by creating a session using the `requests` library. If proxy settings are provided, they are applied to the session to facilitate the requests.

2. **Fetching the Target**: 
   The target URL is accessed with a GET request. If the request fails (due to timeout or other issues), an error message is printed, and the process is halted.

3. **HTML Parsing**: 
   Upon successfully fetching the target page, the HTML content is parsed using `BeautifulSoup`. The script searches for all `<script>` tags to identify JavaScript files that may contain API endpoint information.

4. **Endpoint Extraction**: 
   For each script URL found:
   - If the URL is relative, it is converted to an absolute URL based on the target.
   - A GET request is made to fetch the JavaScript content.
   - Regular expressions are used to search for patterns that typically indicate API endpoints (e.g., paths containing `/api/`, `/v1/`, or `/admin/`).

5. **Unique Endpoints**: 
   The identified endpoints are stored in a list, which is then filtered to remove duplicates.

6. **Output**: 
   - If any endpoints are found, they are printed to the console.
   - If no endpoints are identified, a message indicating this is displayed.

7. **CSV Output**: 
   If CSV output is enabled in the settings, the results are saved to a CSV file. The file includes the target URL, the current date and time, the type of hunt, and the found endpoints. If no endpoints were found, this is also recorded in the CSV.

This feature provides a systematic approach to discovering potential API endpoints, which can be useful for further analysis or testing.
