#리스트 컴프리헨션의 성능
iteration_max = 10000

vector = list(range(iteration_max)) #0~9999
scalar = 2

for _ in range(iteration_max) : # _는 반복만 하겠다
    [scalar * value for value in range(iteration_max)]