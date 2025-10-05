class Employee:
    empcount=0
    def __init__(self,name,money):
        self.count= 0
        self.name=name
        self.money=money
        print(f'{self.name}의 연봉은 {self.money}입니다.')
        Employee.empcount+=1
        
    def display(self):
        print(f'name:{self.name},Salary:{self.money}')

emp=Employee('kim',5000)
emp1=Employee('Lee',6000) 
print(f'Total employee:{Employee.empcount}')
