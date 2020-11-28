import numpy as np

a = np.random.randint(1,100,size=15).reshape(3,5)
print(f'a = {a}')

print(f'a의 열방향 최댓값: {a.max(axis=0)}')
print(f'a의 열방향 최솟값: {a.min(axis=0)}')
print(f'a의 열방향 평균: {a.mean(axis=0)}')

print(f'a의 행방향 최댓값: {a.max(axis=1)}')
print(f'a의 행방향 최솟값: {a.min(axis=1)}')
print(f'a의 행방향 평균: {a.mean(axis=1)}')