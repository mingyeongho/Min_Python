class Animal :
    def __init__(self, name: any) :
        self.name = name
    def talk(self) :
        raise NotImplementedError('subClass must implement abstract method')