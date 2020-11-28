import numpy as np

a = np.array([[1,1,-1],[2,-1,3],[1,2,1]])
b = np.array([0,9,8])

result = np.linalg.solve(a,b)
print(f'x = {np.round_(result[0],1)}, y = {np.round_(result[1],1)}, z = {np.round_(result[2],1)}')
# 소수점 한자리까지 반올림

A = np.array([[1,1,-1],[2,-1,3],[1,2,1]], dtype='int32')
print(f'det(A) = {np.round_(np.linalg.det(A),1)}')