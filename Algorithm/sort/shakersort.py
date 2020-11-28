from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1 # n - 1
    last = right # last = n - 1
    while left < right:
        # 홀수, 작은 것을 뒤에서 앞으로
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        # 짝수, 큰 것을 앞에서 뒤로
        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last

if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    arr = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        arr[i] = int(input(f'arr[{i}] : '))

    shaker_sort(arr)      # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    print(arr)