# recur() 함수의 재귀 호출을 거꾸로 출력
def recur(n: int) -> int :
    if n > 0 :
        recur(n-2)
        print(n)
        recur(n-1)

x = int(input('정숫값을 입력하세요 : '))

recur(x)