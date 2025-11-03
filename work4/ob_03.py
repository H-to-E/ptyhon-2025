class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self,rate):
        rate= 1-rate
        self.price= self.price*rate
        self.price=int(self.price)
    def get_info(self):
        print('싱품명:',self.name,',가격:',self.price,'원')

p1=Product('운동화',30000)
p1.discount(0.1)
p1.get_info()
