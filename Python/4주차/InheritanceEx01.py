class Person(object) :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

class Korean(Person) :
    pass

first_Korean = Korean('Min Gyeong Ho', 23)
print(first_Korean.name)