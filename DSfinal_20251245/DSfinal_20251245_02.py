from tkinter import *

class Person:
    def __init__(self,name):
        self.name=name
class Hobbyperson(Person):
    def __init__(self,name,hobbylist=[ ]):
        super().__init__(name)
        self.hobbylist=hobbylist
    def add_hobby(self,hobby):
            if hobby not in self.hobbylist:
                self.hobbylist.append(hobby)
    def clearhobby(self):
        self.hobbylist = [ ] 
    
root=Tk()
root.title('문제4')
root.geometry('380x280')

stu= Hobbyperson('홍길동')

def addcourse():
    global stu
    if choice.get()==1:
        stu.add_hobby('독서')
    if choice.get()==2:
        stu.add_hobby('게임')
    if choice.get()==3:
        stu.add_hobby('운동')
    coulabel.config(text=f'현재 선택된 취미:{stu.hobbylist}')
def delateall():
    global stu
    stu.clearhobby()
    choice.set(0)
    coulabel.config(text='모든 선택을 해제했습니다')

Label(root,text='이름:홍길동').pack()

frame1=Frame(root)
frame1.pack()



choice=IntVar()
Radiobutton(frame1,text='독서',padx=20,variable=choice,value=1).pack(side=LEFT)
Radiobutton(frame1,text='게임',padx=20,variable=choice,value=2).pack(side=LEFT)
Radiobutton(frame1,text='운동',padx=20,variable=choice,value=3).pack(side=LEFT)

coulabel = Label(root,text='취미을 선택하고 [등록하기]를 누르세요')
coulabel.pack()

frame2=Frame(root)
frame2.pack()
button1=Button(frame2,text='등록하기',command= addcourse).pack(side=LEFT,padx=20)
button2=Button(frame2,text='초기화',command=delateall).pack(side=LEFT,padx=20)


root.mainloop()

