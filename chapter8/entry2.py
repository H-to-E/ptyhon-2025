from tkinter import *

def get_entery():
    name=entry_name.get()
    age=entry_age.get()
    print('name',name)
    print('age',age)

root = Tk()
root.geometry("300x200")

Label(root,text='name').pack()
entry_name=Entry(root)
entry_name.pack()

Label(root,text='age').pack()
entry_age= Entry(root)
entry_age.pack()

button=Button(root,text='send',command=get_entery)
button.pack()

root.mainloop()