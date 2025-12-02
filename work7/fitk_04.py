from tkinter import *
import os

base_dir=os.path.dirname(__file__)
file=os.path.join(base_dir,"drive_log.txt")
outfile=open(file,"a",encoding="UTF-8")

class Vehicle:
    def __init__(self,name):
        if name == "":
            self.name='이름없음'
        else:
            self.name=name
class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def drive(self):
        clabel.config(text=f'승용차 {self.name}이 주행합니다')
        outfile.write(f'승용차 {self.name}이 주행합니다\n')
class Truck(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def drive(self):
        clabel.config(text=f'트럭 {self.name}이 화물을 싣고 주행합니다')
        outfile.write(f'트럭 {self.name}이 화물을 싣고 주행합니다\n')

def drivecar():
    name=e1.get()
    c= Car(name)
    c.drive()

def drivetruck():
    name=e1.get()
    t=Truck(name)
    t.drive()

def delatelog():
    global outfile
    outfile.close()
    outfile=open(file,"w",encoding="UTF-8")
    outfile.close()



root= Tk()
root.title('문제4')
root.geometry('400x320')

Label(root,text='저장 이름을 입렷하세요').pack()

e1= Entry(root)
e1.pack()

clabel = Label(root,text='글자가 여기에 표시됩니다')
clabel.pack()

b1= Button(root,text='자동차 주행',command=drivecar).pack()
b2= Button(root,text='트럭 주행',command=drivetruck).pack()
b3= Button(root,text='로그 비우기',command=delatelog).pack()

root.mainloop()
outfile.close()