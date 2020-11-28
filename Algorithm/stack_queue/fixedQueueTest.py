from enum import Enum
from fixedQueue import FixedQueue

Menu = Enum('Menu', ['enqueue', 'dequeue', 'peek', 'find', 'dump', 'exit'])

def select_menu() -> Menu :
    s = [f'({m.value}){m.name}' for m in Menu]
    while True :
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

q = FixedQueue(64)

while True :
    print(f'현재 데이터 수: {len(q)}/{q.capacity}')
    menu = select_menu()

    if menu == Menu.enqueue :
        x = int(input('인큐할 데이터를 입력하세요: '))
        try :
            q.enqueue(x)
        except FixedQueue.Full :
            print('큐가 가득 찼습니다.')

    elif menu == Menu.dequeue :
        try :
            x = q.dequeue()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty :
            print('큐가 비어있습니다.')

    elif menu == Menu.peek :
        try :
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty :
            print('큐가 비어있습니다.')

    elif menu == Menu.find :
        x = int(input('검색할 값을 입력하세요.: '))
        if x in q :
            print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else :
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.dump :
        q.dump()
    
    else :
        break