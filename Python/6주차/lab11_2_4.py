import numpy as np

a = np.array([23,45,67,7,2,30,34,82])
b = np.random.randint(0,100,size=10)

c = np.append(a,b)
print(c)