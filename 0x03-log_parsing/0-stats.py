#!/usr/bin/python3
""" 0. Log parsing """
import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """ Prints a log stats. """
    print("File size: {}".format(total_size_)
    for status, count in sorted(status_codes.items()):
        print("{}: {}".format(status, count)


exp = r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s-\s\[.*\]\s\".*\"\s(\d{3})\s(\d+)\n$"


if __name__ == "__main__":
    total_size = 0
    status_codes = defaultdict(lambda: 0)
    count = 0
    statuses = ("200", "301", "400", "401", "403", "404", "405", "500")

    try:
        for line in sys.stdin:
            count += 1

            print(line, end='')
            match = re.fullmatch(exp, line)   # match standard log expression
            if not match:
                continue

            code, file_size = match.groups()

            total_size += int(file_size)
            if code in statuses:
                status_codes[code] += 1

            if count == 10:
                print_stats(total_size, status_codes)
                count = 0
    except KeyboardInterrupt as err:
        print_stats(total_size, status_codes)
        raise err
