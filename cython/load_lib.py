import ctypes
import os
import sys

_sum = ctypes.CDLL(os.path.join(
    os.path.dirname(
        os.path.abspath(
            sys.argv[0])),
    'lib/libsum.so'))
_sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))


def our_function(numbers):
    global _sum
    num_numbers = len(numbers)
    array_type = ctypes.c_int * num_numbers
    result = _sum.our_function(ctypes.c_int(num_numbers), array_type(*numbers))
    return int(result)


print(our_function([1, 4, 7]))
