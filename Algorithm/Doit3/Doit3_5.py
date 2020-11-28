from __future__ import annotations
from typing import Any, Type
import hashlib

class Node :
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash :
    def __init__(self, capacity: int) -> None :
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int : #해쉬 함수
        if isinstance(key, int) :
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % 16) % self.capacity

    def search(self, key: Any) -> Any :
        hash = self.hash_value(key) #검색하는 키의 해쉬값
        p = self.table[hash]

        while p is not None : #table[hash]가 None이 아니면 
            if p.key == key :
                return p.value
            p = p.next # 다음 노드 스캔

        return None #검색 실패

    def add(self, key: Any, value: Any) -> bool :

        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None : #linear search
            if p.key == key :
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # Node 추가
        return True

    def remove(self, key: Any) -> bool :
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None # 바로 앞의 노드 주목

        while p is not None :
            if p.key == key : # key 발견
                if pp is None :
                    self.table[hash] = p.next # 삭제 후 table[hash]를 다음 노드에 연결
                else :
                    pp.next = p.next # pp가 None이 아니면 p의 다음 노드를 pp의 다음 노드로 연결
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None :
        for i in range(self.capacity) :
            p = self.table[i]
            print(i, end='')
            while p is not None :
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()