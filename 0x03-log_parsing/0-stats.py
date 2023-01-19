#!/usr/bin/python3
""" 0. Log parsing """
import sys


def print_stats(size, obj):
    """ Prints log stats """
    print("File size: {}".format(size))
    for key, val in sorted(obj.items()):
        if val != 0:
            print("{}: {}".format(key, val))


codes = ("200", "301", "400", "401", "403", "404", "405", "500")
status_obj = {code: 0 for code in codes}
acc_size = 0

try:
    count = 0
    for line in sys.stdin:
        count += 1
        fields = line.split()[::-1]    # reverse split
        try:
            acc_size += int(fields[0])
            code = fields[1]

            if code in codes:
                status_obj[code] += 1

            if count == 10:
                print_stats(acc_size, status_obj)
                count = 0
        except Exception:
            pass
except KeyboardInterrupt:
    print_stats(acc_size, status_obj)
    raise
