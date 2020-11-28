from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None :
    n = len(a)
    for i in range(n - 1) :
        exchng = 0 # 패스에서 교환 횟수
        for j in range(n - 1, i, -1) :
            if a[j - 1] > a[j] :
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0 :
            break
        
if __name__ == "__main__" :
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    arr = [None] * num

    for i in range(num) :
        arr[i] = int(input(f'arr[{i}] : '))

    bubble_sort(arr)

    print('오름차순으로 정렬했습니다.')
    print(arr)