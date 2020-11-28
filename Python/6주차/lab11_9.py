import numpy as np

a = np.arange(0,16).reshape(4,4)
print('a')
print(a)

b = a[:,1]
print('b')
print(b)

c = a[2, 1:]
print('c')
print(c)

d = a[:2, :2]
print('d')
print(d)

e = a[1:3, 1:3]
print('e')
print(e)

f = a[:2, :3]
print(f'f = {f.flatten()}')

g = a[2:, :]
print(f'g = {g.flatten()}')

h = np.concatenate((a[1, 1:], a[3, 1:]))
print(f'h = {h.flatten()}')