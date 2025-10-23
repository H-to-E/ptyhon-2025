from tkinter import *

class Student:
    def __init__(self,stu_id,name):
        self.name=name
        self.stu_id=stu_id
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.stu_id == other.stu_id
        return False
def print_fields():
    e1.

root=Tk()
root.title('중간고사 5번')

Label(root,text='아이디').grid(row=0)
Label(root,text='패스워드').grid(row=1)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(root,text='학번',command=print_fields).grid(row=3,column=0,sticky=W,pady=4)
Button(root,text='이름',command=root.quit).grid(row=3, column=1,sticky=W,pady=4)

root.mainloop()

