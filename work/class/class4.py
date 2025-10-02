class Employee:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        print(f'{self.name}의 연봉은 {self.money}입니다.')

    def raise_salary(self,money):
        self.money+=money
        print(f'{self.name}의 연봉이 {self.money}으로 인상되었습니다.')
    
    def info(self):
        print('f{self.name}의 연봉은 {self.money}입니다.')

a=Employee('kim',5000)
b=Employee('lee',6000)

a.raise_salary(2000)
b.raise_salary(2000)