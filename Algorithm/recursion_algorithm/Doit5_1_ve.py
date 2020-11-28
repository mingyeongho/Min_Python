# def factorial(n: int) -> int :
#     if n > 0 :
#         return n * factorial(n-1)
#     elif n == 0 :
#         return 1
#     else :
#         raise ValueError

import math

if __name__ == "__main__" :
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    try:
        print(f'{n}의 팩토리얼은 {math.factorial(n)}입니다.')
    except ValueError:
        print(f'{n}의 팩토리얼은 구할 수 없습니다.')