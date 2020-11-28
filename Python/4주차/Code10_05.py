from Code10_04 import Person

class Employee(Person) :
    def __init__(self, name, age, gender, salary, hire_date) :
        super().__init__(name, age, gender) # 부모 객체 사용
        self.salary = salary
        self.hire_date = hire_date
    
    def do_work(self) :
        print('열심히 일을 한다.')

    def about_me(self) : # Overriding
        super().about_me()
        print(f'제 급여는 {self.salary}원 이고, 제 입사일은 {self.hire_date}입니다.')