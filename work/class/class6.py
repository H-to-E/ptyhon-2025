class Account():
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def desposit(self,money):
        print(f'초기잔고:{self.balance}')
        self.balance += money
        print(f'저축 후 잔고:{self.balance}' )

    def withdraw(self,money):
        print(f'초기잔고:{self.balance}')
        if money <= self.balance:
            self.balance -= money
            print('인출성공')
            print(f'인출 후 잔고:{self.balance}')
        else:
            print('잔고부족')


a=Account('kim','98194',2000)
a.desposit(500)
a.withdraw(500)
a.withdraw(5000)     
