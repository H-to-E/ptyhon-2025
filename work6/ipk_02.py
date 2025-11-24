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
    def __init__(self,name,pet=None):
        self.name=name
        self.pet=pet()
    def speak(self):
        plabel.config(text=f'{self.name}의 반려동물 -> {self.pet.speak()}')


def cat():
    global p
    p=Person('홍길동',Cat)
    plabel.config(text='고양이를 선택했습니다')
def dog():
    global p
    p=Person('홍길동',Dog)
    plabel.config(text='강아지를 선택했습니다')
def speak():
    global p
    p.speak()

root=Tk()
root.title('문제2')
root.geometry('400x200')

Label(root,text='동물을 선택해 주세요.').pack()
frame1=Frame(root)
frame1.pack()

button1=Button(frame1,text='강아지 선택',command=dog).pack(side=LEFT,padx=25)
button2=Button(frame1,text='고양이 선택',command=cat).pack(side=LEFT,padx=25)

button3=Button(root,text='말하기',command=speak).pack(padx=100)

plabel=Label(root,text=' ')
plabel.pack()


root.mainloop()