import numpy as np
from timeit import default_timer as timer

from ply.cpp import xrange


def vectoradd(a, b, c):
    for i in xrange(a.size):
        c[i] = a[i] + b[i]


def main():
    N = 32000000

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    vectoradd(A, B, C)
    vectored_time = timer() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))

    print("VectorAdd took %f seconds" % vectored_time)


if __name__ == '__main__':
    main()
