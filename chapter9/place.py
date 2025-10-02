from tkinter import *
root=Tk()
root.geometry("300x200")

button1=Button(root,text="버튼1",bg='red',fg='white')
button2=Button(root,text="버튼2",bg='blue',fg='white')
button3=Button(root,text="버튼3",bg='green',fg='black')

button1.place(x=0,y=0)
button2.place(x=10,y=7)
button3.place(x=27,y=46)

root.mainloop()