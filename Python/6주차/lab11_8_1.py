import numpy as np

a = np.arange(0,24).reshape(4,3,2)
print("index       element")

for index in np.ndindex(4,3,2) :
    print(f'{index}    {a[index]}')