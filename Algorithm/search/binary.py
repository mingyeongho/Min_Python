from typing import Any,Sequence

def search(a:Sequence, key:Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True :
        pc = (pl + pr) // 2
        if a[pc] == key :
            return pc
        elif a[pc] < key :
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr :
            break
    return -1

if __name__ == "__main__" :
    capacity = int(input('capacity: '))
    a = [None] * capacity

    a[0] = int(input('a[0] = '))
    for i in range(1,capacity) :
        while True :
            a[i] = int(input(f'a[{i}] = '))
            if a[i] >= a[i-1] :
                break
    
    key = int(input(f'key = '))

    index = search(a, key)

    if index == -1 :
        print("None")
    else :
        print(f'a[{index}]에 key가 있습니다.')