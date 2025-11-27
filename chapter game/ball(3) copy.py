from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id= canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        
        self.starts=[-3,-2,-1,1,2,3]
        random.shuffle(self.starts)
        self.x= self.starts[0]
        self.y=-3

        self.canvas_heights=self.canvas.winfo_height()
        self.canvas_widths=self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        print(self.canvas.coords(self.id))
        self.starts=[-3,-2,-1,1,2,3]
        random.shuffle(self.starts)


        if pos[1] <=0:
            self.y=abs(self.starts[1])
        if pos[3]>=self.canvas_heights:
            self.y=-abs(self.starts[1])

        if pos[0] <=0:
            self.x=abs(self.starts[0])
        if pos[2]>=self.canvas_widths:
            self.x=-abs(self.starts[0])




root=Tk()
root.title('game')
root.resizable(0,0)
root.wm_attributes("-topmost",1)

canvas= Canvas(root)
canvas.pack()
root.update()

ball= Ball(canvas,'red')

while True:
    ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)


root.mainloop()
