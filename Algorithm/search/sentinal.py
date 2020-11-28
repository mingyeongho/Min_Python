from typing import Any, Sequence
import copy

def search(a: Sequence, key: Any) -> Any :
    seq = copy.deepcopy(a)
    seq.append(key)

    i = 0
    while True :
        if a[i] == key :
            break
        i += 1
    
    return -1 if i == len(a) else i

if __name__ == "__main__" :
    capacity = int(input('capacity: '))
    a = [None] * capacity

    for i in range(capacity) :
        a[i] = int(input(f'a[{i}] = '))

    value = int(input('value: '))

    index = search(a,value)

    if index == -1 :
        print('None')
    else :
        print(f'a[{index}]에 key가 있습니다.')