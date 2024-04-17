#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    global total_file_size, status_counts
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Extract file size and status code
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update statistics
        total_file_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()

