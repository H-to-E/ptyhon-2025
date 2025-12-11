from tkinter import *
from math import *
from random import randint

class DrawableShape:
    def __init__(self,canvas):
        self.canvas=canvas
    def draw(self):
        pass

class Square(DrawableShape):
    def __init__(self,x,y,size,canvas):
        super().__init__(canvas)
        self.x=x
        self.y=y
        self.size=size
    def draw(self):
        re=sqrt(self.size)
        self.canvas.create_rectangle(self.x,self.y,self.x+re,self.y+re)

class Circle(DrawableShape):
    def __init__(self,x,y,radius,canvas):
        super().__init__(canvas)
        self.x=x
        self.y=y
        self.radius=radius
    def draw(self):
        self.canvas.create_oval(self.x,self.y,self.x+self.radius,self.y+self.radius)


def draw_rec():
    global canvas,dlist
    x=randint(1,350)
    y=randint(1,250)
    s=randint(100,1000)
    
    d=Square(x,y,s,canvas)
    d.draw()
    dlist.append(f'Square-x:{x} y:{y} size:{s}')
    l2.config(text=dlist)


def draw_cir():
    global canvas
    x=randint(1,350)
    y=randint(1,250)
    r=randint(50,100)
    d=Circle(x,y,r,canvas)
    d.draw()
    dlist.append(f'Circle-x:{x} y:{y} radius:{r}')  
    l2.config(text=dlist)
def draw_all():
    global canvas
    x=randint(1,350)
    y=randint(1,250)
    r=randint(50,100)
    s=randint(100,200)
    d=Square(x,y,s,canvas)
    c=Circle(x,y,r,canvas)
    d.draw()
    c.draw()
    dlist.append(f'Square-x:{x} y:{y} size:{s}')
    dlist.append(f'Circle-x:{x} y:{y} radius:{r}')  
    l2.config(text= dlist)




root = Tk()
root.title('문제1')
root.geometry("420x440")
choice=IntVar()

dlist=[]
canvas=Canvas(root,width=400,height=300,bg="white")
canvas.pack()
d= DrawableShape(canvas) 



buframe= Frame(root)
buframe.pack()
frame1= Frame()
frame1.pack()
l1= Label(frame1,text='생성된 도형 목록').pack(side=LEFT)
l2=Label(frame1,text=dlist)
l2.pack(side=LEFT)

Button(buframe,text='사각형',command=draw_rec).pack(side=LEFT,padx=10)
Button(buframe,text='원',command=draw_cir).pack(side=LEFT,padx=10)
Button(buframe,text='모두그리기',command=draw_all).pack(side=LEFT,padx=10)


Label(root,text="버튼을 눌러 도형을 선택하세요").pack()


root.mainloop()
