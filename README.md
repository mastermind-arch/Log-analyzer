Here is a detailed description you can use for your `README.md` file on GitHub:

---

# Log Analyzer

## Overview
This project is a basic log analyzer tool written in Python. It reads a web server log file, parses the log entries, and provides a summary of HTTP status code counts. This tool is useful for quickly analyzing server logs to identify the distribution of response codes.

## Features
- Parses common web server log formats.
- Extracts key information such as IP address, datetime, HTTP method, URL, status code, and response size.
- Counts occurrences of each HTTP status code.

## Requirements
- Python 3.x
- Pydroid 3 (for running the script on Android devices)

## Usage
1. **Prepare the Log File**: Ensure you have a log file named `sample.log` in the same directory as the script. The log file should contain log entries similar to the format below:
    ```
    127.0.0.1 - - [10/Jul/2024:22:14:15 +0000] "GET /index.html HTTP/1.1" 200 1043
    127.0.0.1 - - [10/Jul/2024:22:14:17 +0000] "POST /submit-form HTTP/1.1" 404 32
    127.0.0.1 - - [10/Jul/2024:22:14:19 +0000] "GET /about.html HTTP/1.1" 200 2048
    192.168.1.1 - - [10/Jul/2024:22:15:20 +0000] "GET /index.html HTTP/1.1" 200 1043
    ```

2. **Run the Script**: Execute the `log_analyzer.py` script. The script will read `sample.log`, parse the entries, and print a summary of HTTP status code counts.

## Example Output
```
HTTP Status Code Counts:
200: 3
404: 1
```

## Code
python
import re

# Function to parse log lines
def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) HTTP/(?P<http_version>\d\.\d)" (?P<status>\d+) (?P<size>\d+)"
    )
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

# Function to analyze logs
def analyze_logs(log_file_path):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    parsed_logs = [parse_log_line(log) for log in logs if parse_log_line(log) is not None]

    # Analyze logs
    status_counts = {}
    for log in parsed_logs:
        status = log['status']
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1

    return status_counts

# Input log file path
log_file_path = 'sample.log'

# Analyze the logs and print results
status_counts = analyze_logs(log_file_path)
print("HTTP Status Code Counts:")
for status, count in status_counts.items():
    print(f"{status}: {count}")
```

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.
