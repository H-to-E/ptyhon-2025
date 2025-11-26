from tkinter import *

class Pet:
    pass
class Dog(Pet):
    def speak(self):
        return "멍멍!"
class Cat(Pet):
    def speak(self):
        return "야옹!"
class Person:
    def __init__(self,name='이름없음',pet=None):
        self.name=name
        self.pet=pet()
    def getsound(self,sound=None):
        self.sound= self.pet.speak()
        return self.sound
    

def getname():
    name=entry.get()
    if name:
        return name
    else:
        return '이름없음'
def chechhealth():
    fi= ''
    se=''
    if value1.get()==1:
        fi='O'
    else:
        fi='X'
    if value2.get()==1:
        se='O'
    else:
        se='X'
    return f'예방접종:{fi},중성화:{se}'

def checkall():
    astring=''
    name= getname()
    value=choice.get()
    if value==1:
        p= Person(name,Dog)
        name=name+'(강아지)'
    else:
        p= Person(name,Cat)
        name=name+'(고양이)'
    health=chechhealth()
    astring = f'홍길동의 반려동물 등록 완료!\n 이름:{name}\n소리:{p.getsound()}\n{health}'
    label.config(text=astring)


def delateall():
    value1.set(0)
    value2.set(0)
    choice.set(0)
    entry.delete(0,len(entry.get()))
    label.config(text=' ')


    

    




root=Tk()
root.title('문제 5')
root.geometry('700x300')

Label(root,text='반려동물 등록하기').pack()

frame1=Frame(root)
frame1.pack()

Label(frame1,text='반려동물 이름').pack(side=LEFT)
entry=Entry(frame1)
entry.pack(side=LEFT)

frame2=Frame(root)
frame2.pack()

choice=IntVar()
Radiobutton(frame2,text='강아지',padx=20,variable=choice,value=1).pack(side=LEFT)
Radiobutton(frame2,text='고양이',padx=20,variable=choice,value=2).pack(side=LEFT)

frame3=Frame(root)
frame3.pack()

value1=IntVar()
Checkbutton(frame3,text='예방접종 완료',variable=value1).pack(side=LEFT)
value2=IntVar()
Checkbutton(frame3,text='중성화 완료',variable=value2).pack(side=LEFT)

label=Label(root,text='')
label.pack()


frame4= Frame(root)
frame4.pack()

button1=Button(frame4,text='등록하기',command=checkall).pack(side=LEFT,padx=20)
button2=Button(frame4,text='초기화',command=delateall).pack(side=LEFT,padx=20)

root.mainloop()