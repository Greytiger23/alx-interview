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

# read lines from stdin
for line in sys.stdin:
    parts = line.split()
    if len(parts) < 9:
        continue
    try:
        ip_address = parts[0]
        date = parts[3][1:] + ' ' + parts[4][:-1]
        method = parts[5][1:]
        url = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[8])
        file_size = int(parts[9])

        if method != "GET" or url != "/projects/260" or protocol != "HTTP/1.1":
            continue
        total_size += file_size
        if status_code in valid_status_codes:
            status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except (IndexError, ValueError):
        continue
print_stats()
