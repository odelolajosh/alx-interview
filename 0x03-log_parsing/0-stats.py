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
    counter = 0
    for line in sys.stdin:
        fields = line.split()[::-1]
        try:
            acc_size += int(fields[0])
            code = fields[1]

            if code in status_obj:
                status_obj[code] += 1

            counter += 1

            if counter == 10:
                print_stats(acc_size, status_obj)
                counter = 0
        except Exception:
            pass
finally:
    print_stats(acc_size, status_obj)
