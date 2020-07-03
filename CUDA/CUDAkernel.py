from numba import cuda
import numpy as np
from timeit import default_timer as timer


@cuda.jit
def cudakernel(_array):
    for i in range(array.size):
        _array[i] += 0.5

@cuda.jit
def cudakernel1(_array):
    thread_position = cuda.grid(1)
    _array[thread_position] += 0.5


array = np.array([0, 1], np.float32)
print('Initial array:', array)

print('Kernel launch: cudakernel[1, 1](array)')
start = timer()
cudakernel[1, 1](array)
time = timer() - start
print('Updated array:', array, ' time: ', time)

array = np.array([0, 1], np.float32)
print('Initial array: ', array)
gridsize = 1024
blocksize = 1024
print("Grid size: {}, Block size: {}".format(gridsize, blocksize))

print("Total number of threads:", gridsize * blocksize)

print('Kernel launch: cudakernel[gridsize, blocksize](array)')
start = timer()
cudakernel[gridsize, blocksize](array)
time = timer() - start

print('Updated array: ', array, ' time: ', time)

array = np.array([0, 1], np.float32)
print('Initial array:', array)

print('Kernel launch: cudakernel1[1, 2](array)')
start = timer()
cudakernel1[1, 2](array)
time = timer() - start

print('Updated array: ', array, ' time: ', time)

array = np.array([0, 1], np.float32)
print('Initial array:', array)

print('Kernel launch: cudakernel1[1, 1](array)')
start = timer()
cudakernel1[1, 1](array)
time = timer() - start

print('Updated array:', array, ' time: ', time)

array = np.zeros(1024 * 1024, np.float32)
print('Initial array:', array)

print('Kernel launch: cudakernel1[1024, 1024](array)')
start = timer()
cudakernel1[1024, 1024](array)
time = timer() - start

print('Updated array:', array, ' time: ', time)

# Since it is a huge array, let's check that the result is correct:
print('The result is correct:', np.all(array == np.zeros(1024 * 1024, np.float32) + 0.5))