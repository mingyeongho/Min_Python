from enum import Enum
from Doit3_7 import OpenHash

Menu = Enum('Menu', ['add', 'remove', 'search', 'dump', 'exit'])

def select_menu() -> Menu :
    s = [f'({m.value}){m.name}' for m in Menu]
    while True :
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu) :
            return Menu(n)

hash = OpenHash(13)
while True :
    menu = select_menu()

    if menu == Menu.add :
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val) :
            print('추가를 실패했습니다.')
    elif menu == Menu.remove :
        key = int(input('살제할 키를 입력하세요.: '))
        if not hash.remove(key) :
            print('삭제를 실패했습니다.')
    elif menu == Menu.search :
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None :
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else :
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.dump :
        hash.dump()
    else :
        break