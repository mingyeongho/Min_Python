from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None :
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    for i in range(n-1) :
        print(f'패스 {i + 1}')
        for j in range(n-1, i, -1) :
            for m in range(n-1) :
                print(f'{a[m]:2}' + ('  ' if m != j -1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n-1]:2}')
            # for m in range(n) :
            #     print(f'{a[m]:2}' + ('  ' if m != j -1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
            # print()
            ccnt += 1
            if a[j] < a[j-1] :
                scnt += 1
                a[j], a[j-1] = a[j-1], a[j]
        # for m in range(n -1) :
        #     print(f'{a[m]:2}', end='  ')
        # print(f'{a[n-1]:2}')
        for m in range(n) :
            print(f'{a[m]:2}', end='  ')
        print()
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == "__main__" :
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    arr = [None] * num

    for i in range(num) :
        arr[i] = int(input(f'arr[{i}] : '))
    
    bubble_sort(arr)

    print('오름차순으로 정렬했습니다.')
    print(arr)