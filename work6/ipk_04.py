from tkinter import *

class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,classes=[ ]):
        super().__init__(name)
        self.classes=classes
    def enrollCourse(self,subject):
            if subject not in self.classes:
                self.classes.append(subject)
    def clearCourse(self):
        self.classes = [ ] 
    
root=Tk()
root.title('문제4')
root.geometry('380x280')

stu= Student('홍길동')

def addcourse():
    global stu
    if value1.get()==1:
        stu.enrollCourse('Python')
    if value2.get()==1:
        stu.enrollCourse('AI')
    if value3.get()==1:
        stu.enrollCourse('DataScience')
    coulabel.config(text=f'등록된 과목:{stu.classes}')
def delateall():
    global stu
    stu.clearCourse()
    value1.set(0)
    value2.set(0)
    value3.set(0)
    coulabel.config(text='모든 선택을 해제했습니다')

Label(root,text='학생:홍길동').pack()

frame1=Frame(root)
frame1.pack()

value1=IntVar()
Checkbutton(frame1,text='Python',variable=value1).pack(side=LEFT)
value2=IntVar()
Checkbutton(frame1,text='AI',variable=value2).pack(side=LEFT)
value3=IntVar()
Checkbutton(frame1,text='DataScience',variable=value3).pack(side=LEFT)

coulabel = Label(root,text='과목을 선택하고 [등록하기]를 누르세요')
coulabel.pack()

frame2=Frame(root)
frame2.pack()
button1=Button(frame2,text='등록하기',command= addcourse).pack(side=LEFT,padx=20)
button2=Button(frame2,text='초기화',command=delateall).pack(side=LEFT,padx=20)


root.mainloop()