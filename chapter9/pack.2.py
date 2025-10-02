from tkinter import *

root = Tk()
root.geometry('300x200')

button1=Button(root,text="버튼1",bg='red',fg='white')
button2=Button(root,text="버튼2",bg='blue',fg='white')
button3=Button(root,text="버튼3",bg='green',fg='black')

button1.pack(side=LEFT,padx=20)
button2.pack(side=LEFT,padx=10)
button3.pack(side=LEFT,padx=30)

root.mainloop()