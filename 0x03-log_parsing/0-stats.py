#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


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
            total_size += file_size
            status_codes[status_code] += 1
            if int(status_code) in [200, 301, 400, 401, 403, 404, 405, 500]:
                if int(status_code) in status_codes:
                    status_codes[int(status_code)] += 1
            if int(line.count('\n')) % 10 == 0:
                print_stats()
        except ValueError:
            continue

print_stats()
