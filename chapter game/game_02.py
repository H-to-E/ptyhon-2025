from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle = paddle
        self.id= canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x= starts[0]
        self.y=-3

        self.canvas_heights=self.canvas.winfo_height()
        self.canvas_widths=self.canvas.winfo_width()
        self.hitthebottom= False

        self.count =0
        self.countrate=self.canvas.create_text(50,50,text=f'점수:{self.count}')
    def hittheball(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >=paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.count +=1
                self.canvas.itemconfig(self.countrate,text=f'점수:{self.count}')
                return True

        else:
            return False    

    


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        print(self.canvas.coords(self.id))


        if pos[1] <=0:
            self.y=1
        if pos[3]>=self.canvas_heights:
            self.hitthebottom=True
        
        
        if not self.hitthebottom:
            if self.hittheball(pos):
                self.y= -3

        if pos[0] <=0:
            self.x=3
        if pos[2]>=self.canvas_widths:
            self.x=-3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id= canvas.create_rectangle(0,0,100,10,fill= color)
        self.canvas.move(self.id,200,300)

        self.x=0
        self.canvas_widths=self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x=0
        if pos[2] >= self.canvas_widths:
            self.x=0


root=Tk()
root.title('game')
root.resizable(0,0)
root.wm_attributes("-topmost",1)

canvas= Canvas(root,width=500, height=400)
canvas.pack()
root.update()

paddle=Paddle(canvas,'blue')
ball= Ball(canvas,paddle,'red')


def playagain():
    global ball
    global paddle
    ball.hitthebottom = False
    canvas.delete('all')
    paddle=Paddle(canvas,'blue')
    ball= Ball(canvas,paddle,'red')
    play_game()
    

def play_game():
    while (ball.hitthebottom == False):
        ball.draw()
        paddle.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
        if ball.hitthebottom == True:
            text=canvas.create_text(250,200,text='GAME OVER')
            button=Button(canvas,text='재시작',command=playagain)
            window=canvas.create_window(250,230,window=button)
play_game()


    


root.mainloop()
