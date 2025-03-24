# # The Fundamental package for scientific computing in Python

# # The ndarray object
# c = []
# for i in range(len(a)):
#     c.append(a[i] * b[i])
    
import numpy as np
a  = np.arange(15).reshape(3, 5)
print(a)

a.shape
a.dtype.name
a.size
type(a)

b = np.array([6, 7, 8])
b
type(b)

from numpy import pi
np.linspace(0, 2, 9)


array = np.set_printoptions(threshold=sys.maxsize)arange(10000).reshape(100,100)
print(array)

import sys
