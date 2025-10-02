from tkinter import *

def display_text():
    text=text_widge.get("1.0",END)
    print('입력된 정보:',text)

root=Tk()

text_widge=Text(root,width=70,height=10)
text_widge.pack()

button=Button(root,text='출력',command=display_text)
button.pack()
root.mainloop()