from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum) :
    OOCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket :
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value 
        self.stat = stat
    
    def set(self, key:Any, value: Any, stat: Status) -> None :
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None :
        self.stat = stat
class OpenHash :
    def __init__(self, capacity: int) -> None :
        self.capacity = capacity 
        self.talbe = [Bucket()] * self.capacity
    
    def hash_value(self, key: Any) -> int :
        if isinstance(key, int) :
            return key % self.capacity
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity