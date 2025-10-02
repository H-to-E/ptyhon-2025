from tkinter import *

root=Tk()
root.geometry('300x200')

button1=Button(root,text="버튼1",bg='red',fg='white')
button2=Button(root,text="버튼2",bg='blue',fg='white')
button3=Button(root,text="버튼3",bg='green',fg='black')

button1.grid(row=0,column=0)
button2.grid(row=1,column=1)
button3.grid(row=3,column=3)

root.mainloop()