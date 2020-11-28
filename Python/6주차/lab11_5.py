import numpy as np

a1 = np.arange(1,13).reshape(2,6)
print(f'a1 = {a1}')

a2 = np.arange(1,31).reshape(3,10)
print(f'a2 = {a2}')

a3 = a2.reshape(6,5)
print(f'a3 = {a3}')

a4 = np.transpose(a3)
print(f'a4 = {a4}')