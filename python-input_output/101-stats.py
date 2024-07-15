#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """ Print the accumulated metrics """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            file_size += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            # Skip lines with unexpected format
            continue

        if line_count % 10 == 0:
            print_stats(file_size, status_codes)
except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise
print_stats(file_size, status_codes)
