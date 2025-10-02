from tkinter import *
from random import randint

def place_random():
    for button in buttons:
        x=randint(50,400)
        y=randint(50,250)
        button.place(x=x,y=y)
root= Tk()
root.geometry('500x300')

buttons=[]
colors=['red','blue','green','yellow']

for color in colors:
    button=Button(root,text=color,bg=color,fg='white')
    buttons.append(button)

place_random()

refresh_button=Button(root,text='새로고침',command=place_random)
refresh_button.place(x=150,y=150)

root.mainloop()