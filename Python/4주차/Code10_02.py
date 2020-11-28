class SoccerPlayer(object) :
    def __init__(self, name, position, back_number) :
        self.name = name
        self.position = position
        self.back_number = back_number
    
    def change_back_number(self, new_number) :
        print(f"선수의 등번호를 변경한다: From {self.back_number} to {new_number}")
        self.back_number = new_number

    def __str__(self) :
        return f"Hello, My name is {self.name}. I play in {self.position} in center."

jihyun = SoccerPlayer("Jihyun", "MF", 10)

print(f"현재 선수의 등번호는 {jihyun.back_number}번 입니다.")
jihyun.change_back_number(5)
print(f"현재 선수의 등번호는 {jihyun.back_number}번 입니다.")