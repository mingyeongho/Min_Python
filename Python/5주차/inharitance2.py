from inharitance1 import Animal

class Dog(Animal) :
    def talk(self) :
        print(self.name + ": 댕댕")

nana = Dog('nana')
print(nana.talk())