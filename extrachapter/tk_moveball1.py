from tkinter import  *
root = Tk()

def move_ball():
    canvas.move(id,3,0)
    if canvas.coords(id)[2]<400:
        root.after(50,move_ball)

canvas=Canvas(root,width=400,height=300)
canvas.pack()

id =canvas.create_oval(10,100,20,150,fill='orange')
move_ball()

root.mainloop()