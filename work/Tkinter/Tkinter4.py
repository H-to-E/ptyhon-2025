import tkinter as tk
import random
import time
 
root=tk.Tk()
root.title('changing word')
interval=1000

canvas= tk.Canvas(root,width=400,height=200)
canvas.pack()
textid=canvas.create_text(200,100,text="Hello",font=("Helvetica",12),fill="red")
def animatetext():
   for i in range(10):
        updatetextsize()
        updatetextcolor()
        canvas.update()
        time.sleep(0.5)

    
    

def updatetextsize():
    k= random.randint(10,100)
    canvas.itemconfig(textid,font=("Helvetica",k))

def updatetextcolor():
    colors=['red','orange','green','blue','pink','purple']
    color = random.choice(colors)
    canvas.itemconfig(textid,fill=color)


animatetext()
root.mainloop()