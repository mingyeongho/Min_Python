from typing import Any, Sequence

def seq_Search(a:Sequence, key: Any) -> int :
    i = 0

    while True :
        if i == len(a) :
            return -1
        if a[i] == key :
            return i
        i += 1

if __name__ == '__main__' :
    num = int(input('원소 수 : '))
    x = [None] * num

    for i in range(num) :
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값 : '))

    idx = seq_Search(x,ky)

    if idx == -1 :
        print('존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')
        