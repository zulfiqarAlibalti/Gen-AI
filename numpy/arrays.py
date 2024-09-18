import numpy as np
import time
import sys

a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype = float)
print(b)

S = range(1000)
print(sys.getsizeof(5) * len(S))

D = np.arange(1000)
print(D.size * D.itemsize)

SIZE = 100000
L1  = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

START = time.time()
result = [(x, y) for x, y in zip(L1, L2)]

START1 = time.time()
result = A1 + A2

print((time.time() - START) * 1000)
print((time.time() - START1) * 1000)