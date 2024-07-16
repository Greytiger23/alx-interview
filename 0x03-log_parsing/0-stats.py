#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re
import signal

def parse_log_line(line):
    """Parse a log line and extract IP, status code, and file size"""
    pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /project/260 HTTP/1.1\" (\d{3}) (\d+)$"
    match = re.match(pattern, line)
    if match:
        ip = match.group(1)
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return (ip, status_code, file_size)
    return None

