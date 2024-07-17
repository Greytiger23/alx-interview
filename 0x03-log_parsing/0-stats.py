#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re
import signal


total_size = 0
status_codes = {}

def print_stats(signum, frame):
    """ Print stats including total file size and status codes counts"""
    global total_size, status_codes
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{:d}: {:d[:d]".format(code, status_codes, code))
    sys.exit(0)
signal.signal(signal.SIGINT, print_stats)

for i, line in enumerate(sys.stdin):
    match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /project/260 HTTP/1.1\" (\d{3}) (\d+)$", line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    if (i + 1) % 10 == 0:
        print_stats(None, None)
