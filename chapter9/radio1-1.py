from tkinter import *

def getanswer():
    number=choice.get()
    if number==1:
        Label(root,text='가장 좋아하는 프로그래밍 언어는 python 입니다',padx=20).pack()
    elif number ==2:
        Label(root,text='가장 좋아하는 프로그래밍 언어는 c 입니다',padx=20).pack()
    elif number==3:
        Label(root,text='가장 좋아하는 프로그래밍 언어는 java 입니다',padx=20).pack()
    elif number==4:
        Label(root,text='가장 좋아하는 프로그래밍 언어는 swift 입니다',padx=20).pack()
    
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