from tkinter import *
from tkinter import messagebox

class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def total_price(self,qty):
        self.qty=qty
        self.total = qty*self.price
    def __str__(self):
        return f'메뉴:{self.name},단가:{self.price}'

class DeliveryFood(Food):
    def __init__(self,name,price,delivery_fee):
        super().__init__(name,price)
        self.delivery_fee=delivery_fee
    def total_price(self,qty):
        self.qty=qty
        self.total= qty*self.price + self.delivery_fee
    def __str__(self):
        return f'메뉴:{self.name}, 단가:{self.price},배달비:{self.delivery_fee}'   

class Order:
    def __init__(self):
        self.menu_list=[]
    def add_food(self,menu):
        self.menu_list.append(menu)
    def clear(self):
        self.menu_list=[]
    def total(self):
        total = 0
        for price in self.menu_list:
            total += price.total
        return total
    def summary_list(self):
        result = ''
        for i in self.menu_list:
            result += f'{i.name} x {i.qty} -> {i.total}\n'
        result += '-----------------------\n'
        result += f'합계:{self.total()}'
        return result

order=Order()
def addcart():
    menu=Leftlb.curselection()
    qty = max(1, int(qty_var.get()))
    menu=menu_list[menu[0]]
    menu.total_price(qty)
    order.add_food(menu)

    result= f'{menu.name} x {qty}'
    Rightlb.insert(END,result)

    resultlabel.config(text=f'합계:{order.total()}')
def allorder():
    messagebox.showinfo("영수증", order.summary_list())
 

root= Tk()
root.title('주문,배달 시스템')
root.geometry('680x440')


leftframe = Frame(root)
leftframe.pack(side=LEFT, fill="both", expand=True)
rightframe=Frame(root)
rightframe.pack(side=RIGHT, fill="both", expand=True)

Leftlabel=Label(leftframe,text='메뉴 목록')
Leftlabel.pack()

menu_list = [
    Food("김밥", 3000),
    Food("라면", 4000),
    Food("떡볶이", 5000),
    DeliveryFood("치킨", 18000, 3000),
    DeliveryFood("피자", 20000, 3000),
]

Leftlb = Listbox(leftframe, height=20,width=40)
Leftlb.pack()
for i in menu_list:
    Leftlb.insert(END,i.__str__())

ctrl=Frame(leftframe)
ctrl.pack()
c1=Label(ctrl,text='수량').pack(side=LEFT)
qty_var = IntVar(value=1)
Spinbox(ctrl, from_=1, to=20, width=5, textvariable=qty_var, justify="center").pack(side="left", padx=6)
Button(ctrl,text='장바구니 담기',command=addcart).pack()

Rightlabel=Label(rightframe,text='장바구니')
Rightlabel.pack()

Rightlb=Listbox(rightframe,height=20,width=40)
Rightlb.pack()

bottom=Frame(rightframe)
bottom.pack()

resultlabel=Label(bottom,text='합계:')
resultlabel.pack(side=LEFT)

oderbutton= Button(bottom,text='주문하기',command=allorder)
oderbutton.pack(side=LEFT)


root.mainloop()



