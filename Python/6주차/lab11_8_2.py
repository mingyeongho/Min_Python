import numpy as np

a = np.arange(0,24).reshape(4,3,2)

b = np.concatenate((a[0,0], a[1,0]),axis = 0)
print(f'{b}\n')

c = np.concatenate((a[0,0], a[2,1]), axis= 0)
print(f'{c}\n')

d = np.concatenate((a[0], a[1]),axis = 0)
print(f'{d}\n')

e = np.concatenate((a[0], a[1]), axis= 1)
print(f'{e}\n')