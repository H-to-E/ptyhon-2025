from tkinter import *
from math import pi
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Rectengle(Shape):
    def __init__(self,x,y,w,h):
        super().__init__(x,y)
        self.w=w
        self.h=h
        canvas.create_rectangle(x,y,x+w,y+h,fill='tomato')
    def area(self):
        return int(self.w *self.h)
    def perimeter(self):
        return int(2*(self.w+self.h))

class Circle(Shape):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r=r
        canvas.create_oval(x,y,x+r,y+r,fill='skyblue')
    def area(self):
        return int(pi*self.r*self.r)
    def perimeter(self):
        return int(2*pi*self.r)

def draw():
    canvas.delete("all")
    number=choice.get()
    if number==1:
      shape=Rectengle(50,50,100,60)  
      

    elif number ==2:
       shape=Circle(150,110,40)
    arealabel.config(text=f'면적={str(shape.area())},둘레={str(shape.perimeter())}')  

root = Tk()
root.title('문제 3번')
root.geometry("400x400")
choice=IntVar()

canvas=Canvas(root,width=400,height=300,background='white')
canvas.pack()

arealabel= Label(root,text='도형을 선택하고 그리기를 누르세요.')
arealabel.pack()

frame1= Frame(root)
frame1.pack()
Radiobutton(frame1,text='사각형',padx=20,variable=choice,value=1).pack(side=LEFT)
Radiobutton(frame1,text='원',padx=20,variable=choice,value=2).pack(side=LEFT)

button=Button(root,text='그리기',command=draw)
button.pack()

root.mainloop()