from tkinter import *

def button_clicked():
    print('버튼이 클릭되었습니다')
root =Tk()

button = Button(root,text="click",width=30,height=10,bg='blue',fg='yellow',command=button_clicked)

button.pack()
root.mainloop()