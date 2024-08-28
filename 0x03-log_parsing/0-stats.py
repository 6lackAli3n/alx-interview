#!/usr/bin/python3
"""
log parsing
"""


import sys
import signal

# Initialize the total size and a dictionary for status codes
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """
    Print the current statistics: total file size and status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C) and print the stats.
    """
    print_stats()
    sys.exit(0)

    # Register the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    # Process input from stdin
    for line in sys.stdin:
        try:
            parts = line.split()
            # Extract status code and file size from the line
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats()

        except Exception:
            # If any error occurs (e.g., malformed line), skip it
            continue

        # Print the final stats if the script ends naturally
        print_stats()
