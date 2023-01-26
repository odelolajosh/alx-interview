#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8
    encoding. """
    count = 0
    for x in data:
        if count == 0:
            if x >> 5 == 0b110:         # two byte character
                count = 1
            elif x >> 4 == 0b1110:      # three byte character
                count = 2
            elif x >> 3 == 0b11110:     # four byte character
                count = 3
            elif x >> 7 != 0:           # Invalid byte
                return False
        elif x >> 6 != 0b10:            # check for continuation byte
            return False
        else:
            count -= 1
    return count == 0
