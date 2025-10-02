from tkinter import *

def getanswer():
    number=choice.get()
    print('가장 좋아하는 프로그래밍 언어는',end=" ")
    if number==1:
        print('python',end="")
    elif number ==2:
        print('c',end="")
    elif number==3:
        print('java',end="")
    elif number==4:
        print('swift',end="")
    print('입니다')

root = Tk()
choice=IntVar()

Label(root,text='가장 선호하는 프로그래밍언어는 무엇입니까?',justify=LEFT,padx=10).pack()

Radiobutton(root,text='python',padx=20,variable=choice,value=1).pack(anchor=W)
Radiobutton(root,text='c',padx=20,variable=choice,value=2).pack(anchor=W)
Radiobutton(root,text='java',padx=20,variable=choice,value=3).pack(anchor=W)
Radiobutton(root,text='swift',padx=20,variable=choice,value=4).pack(anchor=W)

button=Button(root,text='submit',command=getanswer)
button.pack()

root.mainloop()