import numpy as np

a = np.arange(1,11)
print(f'a = {a}')

b = a[np.array([1,3,5,7])]
print(f'b = {b}')

bb = a[5:]
print(f'bb = {bb}')

c = a[6:]
print(f'c = {c}')

d = a[0:3]
print(f'd = {d}')

e = a[::2]
print(f'e = {e}')

f = a[::-2]
print(f'f = {f}')