import numpy as np

a = np.array(range(1,10))
a.shape = (3,3)

b = np.array([2]*9)
b.shape = (3,3)
print(f'a = {a}')
print(f'b = {b}')

print(f'a + b = {a + b}')
print(f'a - b = {a - b}')
print(f'a * b = {a * b}')
print(f'a / b = {a / b}')
print(f'a @ b = {a @ b}') #matmul()
print(f'a ** 2 = {a ** 2}')
