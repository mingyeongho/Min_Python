class Person(object) :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    
    def about_me(self) :
        print(f"저의 이름은 {self.name}이고, 제 나이는 {self.age}살 입니다.")