from tkinter import *



def getanswer():
    canvas.delete("all")
    number=choice.get()
    if number==1:
        canvas.create_rectangle(100,100,200,200,fill='red')
    elif number ==2:
        canvas.create_oval(100,100,200,200,fill='blue')
    elif number==3:
        canvas.create_text(200,100,text="Hello Duksung",font=("Helvetica",20),fill="blue")
root = Tk()
root.title('중간고사 4번')
root.geometry("400x400")
choice=IntVar()

canvas=Canvas(root,width=400,height=300)
canvas.pack()

radioframe= Frame(root)
radioframe.pack()

Radiobutton(radioframe,text='사각형',padx=20,variable=choice,value=1).pack(side=LEFT,padx=10)
Radiobutton(radioframe,text='원',padx=20,variable=choice,value=2).pack(side=LEFT,padx=10)
Radiobutton(radioframe,text='텍스트',padx=20,variable=choice,value=3).pack(side=LEFT,padx=10)

button=Button(root,text='그리기',command=getanswer)
button.pack(anchor=CENTER)

root.mainloop()
