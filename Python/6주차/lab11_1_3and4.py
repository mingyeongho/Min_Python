import numpy as np

c = np.array([i for i in range(10) if i % 2 == 0])

print(c)
print(c.shape) # (5,)
print(c.ndim) # 1
print(c.dtype) # int32
print(c.itemsize) # 4
print(c.size) # 5