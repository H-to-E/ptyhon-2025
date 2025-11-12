from tkinter import *
class Animal:
    pass
class Dog(Animal):
    def make_sound(self):
        return '멍멍!'
class Cat(Animal):
    def make_sound(self):
        return '야옹!'
class Duck(Animal):
    def make_sound(self):
        return '꽥꽥!'

root=Tk()
root.title('동물 소리 듣기')

Label(root,text='동물 버튼을 눌러 소리를 들어보세요.').pack()

bframe= Frame(root)
bframe.pack()



def choicedog():
    dog=Dog()
    rlabel.config(text=dog.make_sound())
def choicecat():
    cat=Cat()
    rlabel.config(text=cat.make_sound())
def choiceduck():
    duck=Duck()
    rlabel.config(text=duck.make_sound())
    

dogbutton = Button(bframe,text='강아지',command=choicedog)
dogbutton.pack(side=LEFT)
catbutton = Button(bframe,text='고양이',command=choicecat)
catbutton.pack(side=LEFT)
duckbutton = Button(bframe,text='오리',command=choiceduck)
duckbutton.pack(side=LEFT)

rlabel=Label(root,text='(여기에 울음소리가 나옵니다)')
rlabel.pack()

root=mainloop()