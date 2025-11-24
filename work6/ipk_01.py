from tkinter import *

class Vehicle:
    def __init__(self,name):
        self.name=name
class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def drive(self):
        clabel.config(text=f'승용차 {self.name}이 주행합니다')
class Truck(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def drive(self):
        clabel.config(text=f'트럭 {self.name}이 화물을 싣고 주행합니다')

root=Tk()
root.geometry("400x300")

Label(root,text="버튼을 눌러보세요").pack()
frame1=Frame(root)
frame1.pack()

def drivecar():
    c=Car('car1')
    c.drive()
def drivetruck():
    t=Truck('truck1')
    t.drive()

button1=Button(frame1,text="자동차 주행",command=drivecar).pack(side=LEFT,padx=20)
button2=Button(frame1,text="트럭 주행",command=drivetruck).pack(side=LEFT,padx=20)


clabel = Label(root,text=' ')
clabel.pack()
root.mainloop()