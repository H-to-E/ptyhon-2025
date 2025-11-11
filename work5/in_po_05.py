class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f'메뉴:{self.name},가격:{self.price}'

class DeliveryFood(Food):
    def __init__(self,name,price,delivery_fee):
        super().__init__(name,price)
        self.delivery_fee=delivery_fee
    def __str__(self):
        return f'메뉴:{self.name},가격:{self.price + self.delivery_fee}(배달비 포함)'   