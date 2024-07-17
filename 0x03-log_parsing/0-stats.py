#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics"""
import sys
import re
import signal


def parse_log_line(line):
    """Parse a log line and extract IP, status code, and file size"""
    pattern = r"^ (\d{1, 3}\.\d{1, 3}\.\d{1, 3}) - \[(.*?)\] \"GET /project/260 HTTP/1.1\" (\d{3}) (\d+)$"
    match = re.match(pattern, line)
    if match:
        ip = match.group(1)
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return (ip, status_code, file_size)
    return None


def print_stats(total_size, status_codes):
    """ Print stats including total file size and status codes counts"""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d[:d]".format(code, status_codes, code))


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_data = parse_log_line(line)
            if parsed_data:
                ip, status_code, file_size = parsed_data
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
