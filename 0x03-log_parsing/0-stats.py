#!/usr/bin/python3
""" 0. Log parsing """
import sys


statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_stats(total_size, status_codes):
    """ Prints a log stats. """
    print(f"File size: {total_size}")
    for status, count in sorted(status_codes.items()):
        print(f"{status}: {count}")


total_size = 0
status_codes = dict()
count = 0

try:
    for line in sys.stdin:
        fields = line.split()[::-1]     # reverse split log

        if count == 10:
            print_stats(total_size, status_codes)
            count = 0
            continue

        total_size += int(fields[0])
        status = fields[1]
        if status in statuses:
            status_codes[status] = status_codes.get(status, 0) + 1
        count += 1
finally:
    print_stats(total_size, status_codes)
