#!/usr/bin/python3
""" Method that determines if given data set represent valid UTF-8 encoding """


def validUTF8(data):
    """ determines if given set is valid encoding """
    def check_continuation_bytes(start, count):
        """ checks continuation bytes """
        for a in range(start + 1, start + count + 1):
            if a >= len(data) or (data[a] & 0b11000000) != 0b10000000:
                return False
        return True

    a = 0
    while a < len(data):
        byte = data[a]
        if (byte & 0b10000000) == 0:
            a += 1
            continue
        elif (byte & 0b11100000) == 0b11000000:
            if not check_continuation_bytes(a, 1):
                return False
            a += 2
        elif (byte & 0b11110000) == 0b11100000:
            if not check_continuation_bytes(a, 2):
                return False
            a += 3
        elif (byte & 0b11111000) == 0b11110000:
            if not check_continuation_bytes(a, 3):
                return False
            a += 4

        else:
            return False
    return True
