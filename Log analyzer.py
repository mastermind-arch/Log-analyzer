import re

# Function to parse log lines
def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) HTTP/(?P<http_version>\d\.\d)" (?P<status>\d+) (?P<size>\d+)'
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
