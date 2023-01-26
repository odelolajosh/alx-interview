#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8
    encoding. """
    n_bytes = 0
    for x in data:
        if n_bytes == 0:
            # get the number of 1s in the most significant bits
            mask = 1 << 7
            while x & mask:
                n_bytes += 1
                mask >>= 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # invalid scenarios according to the problem statement
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (x >> 6 == 0b10):    # data byte is not a continuation byte
                return False
        n_bytes -= 1
    return n_bytes == 0
