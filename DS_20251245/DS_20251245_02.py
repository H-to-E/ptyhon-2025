class BankAccount():
    def __init__(self,name):
        self.owner=name
        self.__balance=0
        print(self.owner,'의 계좌가 생성되었습니다')
    def get_balance(self):
        return self.__balance
    def set_balance(self,money):
        if money >= 0:
            self.__balance = money
    def desposit(self,money):
        if money >=0:
            self.__balance += money
            print(self.owner,'통장에서',money,'원이 입금되었습니다')

    def withdraw(self,money):
        if money <= self.__balance:
            self.__balance -= money
            print(self.owner,'통장에서',money,'원이 출금되었습니다')

a= BankAccount('A')
b= BankAccount('B')

a.desposit(100)
b.desposit(200)
a.withdraw(30)
b.withdraw(50)

print(f'{a.owner} 계좌의 현재 잔액:',a.get_balance())
print(f'{b.owner} 계좌의 현재 잔액:',b.get_balance())

a.set_balance(500)
print(f'{a.owner} 계좌의 수정된 잔액:',a.get_balance())