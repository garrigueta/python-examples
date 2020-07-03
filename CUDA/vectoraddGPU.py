import numpy as np
from timeit import default_timer as timer
from numbapro import vectorize
from ply.cpp import xrange


@vecotrize(["float32(float32, float32)"], target='gpu')
def vectoradd(a, b):
    for i in xrange(a.size):
        return a + b


def main():
    N = 32000000

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    C = vectoradd(A, B)
    vectored_time = timer() - start

    print("C[:5] = " + str(C[:5]))
    print("C[-5:] = " + str(C[-5:]))

    print("VectorAdd took %f seconds" % vectored_time)


if __name__ == '__main__':
    main()
