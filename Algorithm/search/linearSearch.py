from typing import Any, Sequence

# def search(a: Sequence, value: Any) -> Any:
#     for i in range(len(a)) :
#         if a[i] == value :
#             return i
#     return -1

def search(a:Sequence, value: Any) -> Any :
    i = 0
    while True :
        if i == len(a) :
            return -1
        if a[i] == value :
            return i
        i += 1

if __name__ == "__main__" :
    capacity = int(input("원소의 개수: "))
    a = [None] * capacity

    for i in range(capacity) :
        a[i] = int(input(f'a[{i}] = '))
    
    key = int(input('key = '))

    index = search(a,key)
    if index == -1 :
        print('None')
    else :
        print(f'a[{index}]에 key가 있습니다.')