#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_codes.keys())
line_count = 0


def print_stats():
    """ Print accumulated statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """ Handle the CTRL+C signal and print stats before exiting"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

pattern = re.compile(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$")
# read lines from stdin
for line in sys.stdin:
    match = pattern.match(line)
    if match:
        ip, date, status_code, file_size = match.groups()
        try:
            status_code = int(status_code)
            file_size = int(file_size)
            if status_code in valid_status_codes:
                total_size += file_size
                status_codes[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
        except ValueError:
            continue

print_stats()
