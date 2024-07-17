#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re


total_size = 0
status_codes = {}

for i, line in enumerate(sys.stdin):
    match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /project/260 HTTP/1.1\" (\d{3}) (\d+)$', line)
    if match:
        ip, date, status_code, file_size = match.groups()
        status_code = int(status_code)
        total_size= int(file_size)
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

    if (i + 1) % 10 == 0 or i == 9:
        print(f'Total file size: {total_size}')
        for code in sorted(status_codes.keys()):
            print(f'{code}: {status_codes[code]}')
    try:
        if i % 10 == 9:
            sys.stdout.flush()
    except KeyboardInterrupt:
        print(f'Total file size: {total_size}')
        for code in sorted(status_codes.key()):
            print(f'{code}: {status_codes[code]}')
        break
