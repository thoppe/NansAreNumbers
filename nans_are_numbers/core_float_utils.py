import struct
from codecs import decode


def float_to_bin(value):  # For testing.
    """Convert float to 64-bit binary string."""
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return "{:064b}".format(d)


def float_to_binary_list(value):
    return [int(bit) for bit in float_to_bin(value)]


def int_to_bytes(n, length):  # Helper function
    """Int/long to byte string.

    Python 3.2+ has a built-in int.to_bytes() method that could be used
    instead, but the following works in earlier versions including 2.x.
    """
    return decode("%%0%dx" % (length << 1) % n, "hex")[-length:]


def bin_to_float(b):
    """Convert binary string to a float."""
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack(">d", bf)[0]
