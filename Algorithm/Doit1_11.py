print("a부터 b까지 정수의 합을 구하라.")
# for문이 n번 반복할 때 if문도 n번 반복하는 것을 피하는 방법
# 분기의 횟수가 줄어든다.

a = int(input('a: '))
b = int(input('b: '))

if a > b :
    a,b = b,a

sum = 0
for i in range(a,b) :
    print(f'{i} + ', end="")
    sum += i

sum += b
print(f'{b} = {sum}')