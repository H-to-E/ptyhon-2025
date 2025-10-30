class Inventory:
    stock =0
    def __init__(self):
        print("새 상품이 등록되었습니다.")
    def get_stock(self):
        return Inventory.stock
    def set_stock(self,number):
        if number >0:
            Inventory.stock=number
    def add_stock(self,number):
        if number>0:
            Inventory.stock += number
            print('상품',number,'개가 입고되었습니다')
    def remove_stock(self,number):
        if number<Inventory.stock:
            Inventory.stock-=number
            print('상품',number,'개가 출고되었습니다')

i1=Inventory()
i1.add_stock(10)
i1.remove_stock(3)
print("현재 재고 수량:",i1.get_stock())

i1.set_stock(20)
print("수정된 재고 수량:",i1.get_stock())