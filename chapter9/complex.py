from tkinter import *

root=Tk()
root.geometry('300x200')

f=Frame(root)

button1=Button(f,text="버튼1",bg='red',fg='white')
button2=Button(f,text="버튼2",bg='blue',fg='white')
button3=Button(f,text="버튼3",bg='green',fg='black')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

l=Label(root,text='이 문구는 버튼 위에 설치됩니다')
l.pack()
f.pack()

root.mainloop()